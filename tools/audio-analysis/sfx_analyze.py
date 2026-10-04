"""Analyse sound files for placement and levelling.

For each file prints/returns:
  onset   - first time the envelope is within 20 dB of its peak (align this to the visual event for hits/pops)
  peak_t  - time of the loudest 10 ms (align this to the motion peak for whooshes / fly-bys)
  end_t   - last time within 30 dB of peak (audible end)
  tail40  - last time within 40 dB of peak (safe place to cut the file)
  centroid- spectral centroid in Hz (lower = darker / softer)
  L100    - loudest 100 ms RMS in dBFS of the channel mean (level used for matching SFX to each other and to
            the user's own SFX; build_audition.py measures the same way)
  M       - max EBU momentary loudness (400 ms), LUFS

usage: sfx_analyze.py file1.wav [file2 ...] [--json out.json]
import: from sfx_analyze import features, decode, l100
needs: ffmpeg, numpy
"""
import json, re, subprocess, sys
import numpy as np

SR = 48000


def decode(path, ss=None, dur=None, ch=1):
    cmd = ["ffmpeg", "-v", "quiet"]
    if ss is not None:
        cmd += ["-ss", f"{ss:.4f}"]
    cmd += ["-i", path]
    if dur is not None:
        cmd += ["-t", f"{dur:.4f}"]
    cmd += ["-vn", "-f", "f32le", "-ac", str(ch), "-ar", str(SR), "-"]
    x = np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.float32)
    return x.reshape(-1, ch) if ch > 1 else x


def l100(x):
    m = x.mean(1) if x.ndim == 2 else x
    w = SR // 10
    if len(m) < w:
        m = np.pad(m, (0, w - len(m)))
    c = np.convolve(m ** 2, np.ones(w) / w, "valid")
    return float(10 * np.log10(c.max() + 1e-12))


def max_momentary(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "apad=pad_dur=0.5,ebur128",
                          "-f", "null", "-"], capture_output=True).stderr.decode("utf-8", "replace")
    m = [float(v) for v in re.findall(r"M:\s*(-?[0-9.]+)", err)]
    return max(m) if m else -70.0


def features(path):
    x = decode(path, ch=2).mean(1)   # mean of channels, like build_audition (ffmpeg -ac 1 would read ~3 dB hotter)
    if len(x) < 480:
        return None
    w = 480
    n = len(x) // w
    edb = 20 * np.log10(np.sqrt((x[: n * w].reshape(n, w) ** 2).mean(1)) + 1e-9)
    pk = edb.max()
    onset = int(np.argmax(edb > pk - 20)) * 0.01
    peak_t = int(np.argmax(edb)) * 0.01
    a30 = np.where(edb > pk - 30)[0]
    a40 = np.where(edb > pk - 40)[0]
    end_t = (a30[-1] + 1) * 0.01 if len(a30) else len(x) / SR
    tail40 = (a40[-1] + 1) * 0.01 if len(a40) else len(x) / SR
    seg = x[int(onset * SR): int(end_t * SR)]
    if len(seg) < 2048:
        seg = np.pad(seg, (0, 2048 - len(seg)))
    frames = np.lib.stride_tricks.sliding_window_view(seg, 2048)[::1024] * np.hanning(2048)
    mag = np.abs(np.fft.rfft(frames, axis=1))
    cen = float((mag * np.fft.rfftfreq(2048, 1 / SR)).sum() / (mag.sum() + 1e-9))
    return {"path": path, "dur": round(len(x) / SR, 3), "onset": round(onset, 3), "peak_t": round(peak_t, 3),
            "end_t": round(float(end_t), 3), "tail40": round(float(tail40), 3), "centroid": round(cen),
            "L100": round(l100(x), 1), "M": round(max_momentary(path), 1)}


if __name__ == "__main__":
    args = sys.argv[1:]
    out = None
    if "--json" in args:
        i = args.index("--json"); out = args[i + 1]; args = args[:i] + args[i + 2:]
    rows = [r for r in (features(p) for p in args) if r]
    for r in rows:
        print(f"{r['path'].split('/')[-1][:48]:48s} dur {r['dur']:.2f} on {r['onset']:.2f} pk {r['peak_t']:.2f} "
              f"end {r['end_t']:.2f} tail {r['tail40']:.2f} cen {r['centroid']:5d} L100 {r['L100']:6.1f} M {r['M']}")
    if out:
        json.dump(rows, open(out, "w"), indent=1, ensure_ascii=False)
