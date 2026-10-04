"""Measure a mix export: integrated loudness, true peak, loudness range, and where the peaks are.

usage: loudness_check.py mix.wav [--hot -1.5] [--target -14]
Export the sequence first with the Premiere MCP export_sequence and the "Waveform Audio 48kHz 16-bit" preset
(takes seconds). Prints I / LRA / TP, then every 50 ms window whose true-ish peak (4x oversampled) is above --hot,
so you can find which clip causes an over (compare with the timeline) instead of guessing.
needs: ffmpeg, numpy
"""
import argparse, re, subprocess
import numpy as np


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wav"); ap.add_argument("--hot", type=float, default=-1.5); ap.add_argument("--target", type=float, default=-14)
    a = ap.parse_args()
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", a.wav, "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True).stderr.decode("utf-8", "replace")
    I = re.findall(r"I:\s+(-?[0-9.]+) LUFS", err); LRA = re.findall(r"LRA:\s+(-?[0-9.]+) LU", err)
    TP = re.findall(r"Peak:\s+(-?[0-9.]+) dBFS", err)
    print(f"integrated {I[-1] if I else '?'} LUFS (target {a.target}), LRA {LRA[-1] if LRA else '?'} LU, true peak {TP[-1] if TP else '?'} dBFS")
    sr = 192000
    raw = subprocess.run(["ffmpeg", "-v", "quiet", "-i", a.wav, "-af", f"aresample={sr}", "-f", "f32le", "-ac", "2", "-"],
                         capture_output=True).stdout
    x = np.abs(np.frombuffer(raw, np.float32).reshape(-1, 2)).max(1)
    w = int(0.05 * sr); n = len(x) // w
    pk = 20 * np.log10(x[: n * w].reshape(n, w).max(1) + 1e-12)
    hot = [(round(i * 0.05, 2), round(float(p), 1)) for i, p in enumerate(pk) if p > a.hot]
    print(f"windows above {a.hot} dBFS:", hot if hot else "none")


if __name__ == "__main__":
    main()
