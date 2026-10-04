"""
Motion Design Director - Audio Analysis Pipeline

Analyzes measurable properties of the audio contained in a motion-design
video. This tool does NOT claim perceptual listening.

Core rule:
    MEASUREMENT != LISTENING

Output:
    - human-readable report
    - structured JSON report
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np


VERSION = "0.2.1"


def run(cmd: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )


def require_tool(name: str) -> str:
    path = shutil.which(name)

    if not path:
        raise RuntimeError(
            f"{name} was not found in PATH."
        )

    return path


def probe_media(path: Path) -> dict:
    result = run([
        "ffprobe",
        "-v", "error",
        "-show_streams",
        "-show_format",
        "-of", "json",
        str(path),
    ])

    if result.returncode != 0:
        raise RuntimeError(
            "ffprobe failed:\n" + result.stderr
        )

    raw = json.loads(result.stdout)

    audio_streams = [
        s for s in raw.get("streams", [])
        if s.get("codec_type") == "audio"
    ]

    video_streams = [
        s for s in raw.get("streams", [])
        if s.get("codec_type") == "video"
    ]

    fmt = raw.get("format", {})

    duration = None

    try:
        duration = float(fmt.get("duration"))
    except (TypeError, ValueError):
        pass

    audio = audio_streams[0] if audio_streams else {}
    video = video_streams[0] if video_streams else {}

    return {
        "duration_seconds": duration,
        "audio_present": bool(audio_streams),
        "video_present": bool(video_streams),
        "audio": {
            "codec": audio.get("codec_name"),
            "sample_rate": _int_or_none(audio.get("sample_rate")),
            "channels": audio.get("channels"),
            "channel_layout": audio.get("channel_layout"),
        },
        "video": {
            "codec": video.get("codec_name"),
            "width": video.get("width"),
            "height": video.get("height"),
            "reported_fps": parse_fps(
                video.get("avg_frame_rate")
                or video.get("r_frame_rate")
            ),
        },
    }


def _int_or_none(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def parse_fps(value):
    if not value:
        return None

    try:
        if "/" in str(value):
            a, b = str(value).split("/", 1)
            b = float(b)

            if b == 0:
                return None

            return float(a) / b

        return float(value)

    except (TypeError, ValueError):
        return None


def extract_wav(source: Path, wav: Path):
    result = run([
        "ffmpeg",
        "-y",
        "-hide_banner",
        "-loglevel", "error",
        "-i", str(source),
        "-vn",
        "-ac", "2",
        "-ar", "48000",
        "-c:a", "pcm_s16le",
        str(wav),
    ])

    if result.returncode != 0:
        raise RuntimeError(
            "Audio extraction failed:\n" + result.stderr
        )


def analyze_loudness(source: Path) -> dict:
    result = run([
        "ffmpeg",
        "-hide_banner",
        "-nostats",
        "-i", str(source),
        "-map", "0:a:0",
        "-af", "ebur128=peak=true",
        "-f", "null",
        "-",
    ])

    text = result.stderr

    summary_pos = text.rfind("Summary:")

    if summary_pos >= 0:
        summary = text[summary_pos:]
    else:
        summary = text

    integrated = regex_float(
        summary,
        r"I:\s*(-?\d+(?:\.\d+)?)\s*LUFS"
    )

    lra = regex_float(
        summary,
        r"LRA:\s*(-?\d+(?:\.\d+)?)\s*LU"
    )

    true_peak = regex_float(
        summary,
        r"Peak:\s*(-?\d+(?:\.\d+)?)\s*dBFS"
    )

    return {
        "integrated_lufs": integrated,
        "loudness_range_lu": lra,
        "true_peak_dbfs": true_peak,
    }


def regex_float(text: str, pattern: str):
    matches = re.findall(pattern, text, re.I)

    if not matches:
        return None

    try:
        return float(matches[-1])
    except ValueError:
        return None


def detect_silence(source: Path) -> list[dict]:
    result = run([
        "ffmpeg",
        "-hide_banner",
        "-nostats",
        "-i", str(source),
        "-map", "0:a:0",
        "-af", "silencedetect=noise=-35dB:d=0.25",
        "-f", "null",
        "-",
    ])

    starts = [
        float(x)
        for x in re.findall(
            r"silence_start:\s*([0-9.]+)",
            result.stderr
        )
    ]

    ends = [
        (float(a), float(b))
        for a, b in re.findall(
            r"silence_end:\s*([0-9.]+).*?"
            r"silence_duration:\s*([0-9.]+)",
            result.stderr
        )
    ]

    events = []

    for i, start in enumerate(starts):
        if i < len(ends):
            end, duration = ends[i]

            events.append({
                "start": round(start, 4),
                "end": round(end, 4),
                "duration": round(duration, 4),
            })

    return events


def decode_wav_pcm(wav: Path) -> tuple[np.ndarray, int]:
    # PCM is binary, therefore use a binary subprocess directly.
    proc = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "error",
            "-i", str(wav),
            "-f", "s16le",
            "-ac", "1",
            "-ar", "48000",
            "pipe:1",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if proc.returncode != 0:
        raise RuntimeError(
            proc.stderr.decode(
                "utf-8",
                errors="replace"
            )
        )

    audio = np.frombuffer(
        proc.stdout,
        dtype=np.int16
    ).astype(np.float32)

    if len(audio):
        audio /= 32768.0

    return audio, 48000


def calculate_envelope(
    audio: np.ndarray,
    sr: int,
    window_ms: float = 20.0,
    hop_ms: float = 10.0,
):
    window = max(
        1,
        int(sr * window_ms / 1000)
    )

    hop = max(
        1,
        int(sr * hop_ms / 1000)
    )

    if len(audio) < window:
        return np.array([]), hop

    values = []

    for start in range(
        0,
        len(audio) - window + 1,
        hop
    ):
        chunk = audio[start:start + window]

        rms = math.sqrt(
            float(np.mean(chunk * chunk)) + 1e-12
        )

        values.append(rms)

    return np.asarray(
        values,
        dtype=np.float32
    ), hop


def detect_onsets(
    audio: np.ndarray,
    sr: int,
    fps: float,
) -> list[dict]:

    envelope, hop = calculate_envelope(
        audio,
        sr
    )

    if len(envelope) < 3:
        return []

    db = 20 * np.log10(
        np.maximum(envelope, 1e-8)
    )

    delta = np.diff(
        db,
        prepend=db[0]
    )

    median = float(np.median(delta))
    mad = float(
        np.median(
            np.abs(delta - median)
        )
    )

    threshold = max(
        3.0,
        median + 5.0 * mad
    )

    candidates = np.where(
        delta >= threshold
    )[0]

    min_gap_seconds = 0.08
    min_gap_bins = max(
        1,
        int(
            min_gap_seconds
            * sr
            / hop
        )
    )

    selected = []

    for idx in candidates:
        if (
            not selected
            or idx - selected[-1] >= min_gap_bins
        ):
            selected.append(int(idx))

        elif delta[idx] > delta[selected[-1]]:
            selected[-1] = int(idx)

    events = []

    for idx in selected:
        seconds = idx * hop / sr

        events.append({
            "time_seconds": round(seconds, 4),
            "frame": int(round(seconds * fps)),
            "strength_db_jump": round(
                float(delta[idx]),
                2
            ),
        })

    events.sort(
        key=lambda x: x["strength_db_jump"],
        reverse=True,
    )

    return events[:50]



def find_python311() -> str | None:
    candidates = [
        Path(
            r"C:\Users\TGL Solutions\AppData\Local"
            r"\Programs\Python\Python311\python.exe"
        ),
    ]

    for candidate in candidates:
        if candidate.exists():
            return str(candidate)

    return None


def analyze_rhythm(
    wav: Path,
    fps: float,
) -> dict:
    """
    Execute Librosa rhythm analysis in the isolated Python 3.11 worker.

    The main pipeline intentionally does not import Librosa.
    """

    python311 = find_python311()

    if not python311:
        return {
            "available": False,
            "status": "PYTHON_311_NOT_FOUND",
            "error": (
                "Dedicated Python 3.11 interpreter was not found."
            ),
        }

    worker = (
        Path(__file__).resolve().parent
        / "rhythm_analyzer.py"
    )

    if not worker.exists():
        return {
            "available": False,
            "status": "WORKER_NOT_FOUND",
            "error": f"Rhythm worker not found: {worker}",
        }

    result = subprocess.run(
        [
            python311,
            str(worker),
            str(wav),
            "--fps",
            str(fps),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    if result.returncode != 0:
        return {
            "available": False,
            "status": "WORKER_FAILED",
            "error": result.stderr.strip(),
        }

    try:
        rhythm = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return {
            "available": False,
            "status": "INVALID_WORKER_JSON",
            "error": str(exc),
            "worker_stdout": result.stdout,
        }

    rhythm["available"] = True
    rhythm["status"] = "OK"

    return rhythm


def relate_onsets_to_beats(
    onsets: list[dict],
    rhythm: dict,
    fps: float,
) -> list[dict]:
    """
    Relate measured onset candidates to the fitted rhythmic grid.

    Tested phases inside each beat:
        0.00 = BEAT
        0.25 = QUARTER_PHASE
        0.50 = HALF_BEAT
        0.75 = THREE_QUARTER_PHASE

    Seconds remain the source of truth.

    Mathematical proximity to a rhythmic subdivision does NOT establish
    musical intention or perceptual synchronization.
    """

    t0 = rhythm.get("grid_offset_seconds")
    period = rhythm.get("beat_period_seconds")

    if t0 is None or period is None:
        return []

    t0 = float(t0)
    period = float(period)

    if period <= 0:
        return []

    phase_definitions = [
        (0.00, "BEAT"),
        (0.25, "QUARTER_PHASE"),
        (0.50, "HALF_BEAT"),
        (0.75, "THREE_QUARTER_PHASE"),
    ]

    relationships = []

    for onset in onsets:
        onset_time = float(
            onset["time_seconds"]
        )

        relative = (
            onset_time - t0
        ) / period

        base_index = math.floor(relative)

        candidates = []

        # Check the local beat plus adjacent beats so boundary cases
        # near 0.00 / 1.00 are classified correctly.
        for beat_index in range(
            base_index - 1,
            base_index + 2,
        ):
            for phase, label in phase_definitions:
                target_time = (
                    t0
                    + beat_index * period
                    + phase * period
                )

                delta_seconds = (
                    onset_time - target_time
                )

                candidates.append({
                    "beat_index": beat_index,
                    "phase": phase,
                    "label": label,
                    "target_time": target_time,
                    "delta_seconds": delta_seconds,
                    "abs_delta_seconds":
                        abs(delta_seconds),
                })

        best = min(
            candidates,
            key=lambda item:
                item["abs_delta_seconds"],
        )

        target_time = float(
            best["target_time"]
        )

        delta_seconds = float(
            best["delta_seconds"]
        )

        # beat_index 0 corresponds to fitted beat number 1.
        beat_number = (
            int(best["beat_index"]) + 1
        )

        relationships.append({
            "onset_time_seconds": round(
                onset_time,
                6,
            ),

            "onset_frame": int(
                round(onset_time * fps)
            ),

            "onset_strength_db_jump":
                onset.get("strength_db_jump"),

            "rhythmic_position":
                best["label"],

            "phase":
                best["phase"],

            "reference_beat_number":
                beat_number,

            "rhythmic_target_time_seconds":
                round(target_time, 6),

            "rhythmic_target_frame": int(
                round(target_time * fps)
            ),

            "delta_seconds": round(
                delta_seconds,
                6,
            ),

            "rhythmic_grid_distance_ms": round(
                abs(delta_seconds) * 1000.0,
                3,
            ),

            "signed_delta_ms": round(
                delta_seconds * 1000.0,
                3,
            ),

            "rhythmic_grid_distance_frames": round(
                abs(delta_seconds) * fps,
                3,
            ),

            "signed_delta_frames": round(
                delta_seconds * fps,
                3,
            ),
        })

    return relationships


def signal_stats(
    audio: np.ndarray
) -> dict:

    if len(audio) == 0:
        return {}

    peak = float(
        np.max(np.abs(audio))
    )

    rms = math.sqrt(
        float(np.mean(audio * audio)) + 1e-12
    )

    return {
        "sample_peak_linear": round(
            peak,
            6
        ),
        "sample_peak_dbfs": round(
            20 * math.log10(
                max(peak, 1e-12)
            ),
            2,
        ),
        "global_rms_dbfs": round(
            20 * math.log10(
                max(rms, 1e-12)
            ),
            2,
        ),
    }


def sec_to_timecode(seconds):
    if seconds is None:
        return "?"

    total_ms = round(seconds * 1000)

    minutes = total_ms // 60000
    seconds_part = (
        total_ms % 60000
    ) / 1000

    return (
        f"{minutes:02d}:"
        f"{seconds_part:06.3f}"
    )


def build_report(
    source: Path,
    fps: float,
    media: dict,
    loudness: dict,
    silence: list,
    stats: dict,
    onsets: list,
    rhythm: dict,
    onset_beat_relationships: list,
):
    return {
        "schema": "motion-design-director.audio-analysis",
        "version": VERSION,

        "source": {
            "file": source.name,
            "path": str(source.resolve()),
        },

        "timeline": {
            "fps_used": fps,
            "duration_seconds":
                media.get("duration_seconds"),
        },

        "media": media,

        "capability": {
            "signal_analysis": True,

            "perceptual_listening": False,

            "rule":
                "MEASUREMENT != LISTENING",

            "allowed_claims": [
                "metadata",
                "signal level",
                "loudness",
                "peak",
                "silence",
                "detected transient/onset timing",
                "detected beat timing",
                "estimated tempo",
                "beat-grid mathematical stability",
                "onset-to-rhythmic-grid timing relationship",
                "time-to-frame mapping",
            ],

            "not_verified": [
                "whether an SFX sounds premium",
                "whether timbre matches motion",
                "emotional appropriateness",
                "perceptual mix quality",
                "musical taste",
                "whether a sound feels powerful",
                "whether a sound is pleasant",
                "whether detected beats match the perceived musical beat",
                "whether synchronization feels correct",
            ],
        },

        "measurements": {
            "loudness": loudness,
            "signal": stats,
            "silence": silence,
            "onsets": onsets,
            "rhythm": rhythm,
            "onset_beat_relationships":
                onset_beat_relationships,
        },

        "epistemic_contract": {
            "MEASURED":
                "Directly produced by signal or metadata analysis.",

            "OBSERVED":
                "Directly perceived by a model or human with actual access to the media.",

            "INFERRED":
                "Interpretation derived from measured or observed evidence.",

            "NOT_VERIFIED":
                "Cannot be established with available capabilities.",
        },
    }


def print_report(report: dict):
    media = report["media"]
    timeline = report["timeline"]
    loudness = report["measurements"]["loudness"]
    signal = report["measurements"]["signal"]
    silence = report["measurements"]["silence"]
    onsets = report["measurements"]["onsets"]
    rhythm = report["measurements"]["rhythm"]
    relationships = report["measurements"][
        "onset_beat_relationships"
    ]

    print()
    print("=" * 64)
    print("MOTION DESIGN DIRECTOR - AUDIO ANALYSIS")
    print("=" * 64)

    print("\nSOURCE")
    print(
        "File:       ",
        report["source"]["file"]
    )
    print(
        "Duration:   ",
        sec_to_timecode(
            timeline["duration_seconds"]
        )
    )
    print(
        "FPS used:   ",
        timeline["fps_used"]
    )

    a = media["audio"]

    print(
        "Audio:      ",
        "YES" if media["audio_present"]
        else "NO"
    )

    if media["audio_present"]:
        print(
            "Codec:      ",
            a.get("codec")
        )
        print(
            "Sample rate:",
            a.get("sample_rate")
        )
        print(
            "Channels:   ",
            a.get("channels")
        )

    print("\nLOUDNESS [MEASURED]")
    print(
        "Integrated: ",
        loudness.get(
            "integrated_lufs"
        ),
        "LUFS"
    )
    print(
        "LRA:        ",
        loudness.get(
            "loudness_range_lu"
        ),
        "LU"
    )
    print(
        "True peak:  ",
        loudness.get(
            "true_peak_dbfs"
        ),
        "dBFS"
    )

    print("\nSIGNAL [MEASURED]")
    print(
        "Sample peak:",
        signal.get(
            "sample_peak_dbfs"
        ),
        "dBFS"
    )
    print(
        "Global RMS: ",
        signal.get(
            "global_rms_dbfs"
        ),
        "dBFS"
    )

    print("\nSILENCE / LOW-LEVEL REGIONS [MEASURED]")

    if silence:
        for event in silence[:20]:
            print(
                f"{event['start']:8.3f}s -> "
                f"{event['end']:8.3f}s "
                f"({event['duration']:.3f}s)"
            )
    else:
        print("None detected with current threshold.")

    print("\nSTRONGEST DETECTED ONSETS [MEASURED]")

    if onsets:
        for event in onsets[:15]:
            print(
                f"{event['time_seconds']:8.3f}s | "
                f"frame {event['frame']:5d} | "
                f"+{event['strength_db_jump']:.2f} dB"
            )
    else:
        print("No reliable onset candidates.")

    print("\nRHYTHM / BEAT GRID [MEASURED]")

    if rhythm.get("available"):
        print(
            "Raw BPM:        ",
            rhythm.get("raw_bpm")
        )
        print(
            "Fitted BPM:     ",
            rhythm.get("fitted_bpm")
        )
        print(
            "Beat period:    ",
            rhythm.get("beat_period_seconds"),
            "s"
        )
        print(
            "Grid offset t0: ",
            rhythm.get("grid_offset_seconds"),
            "s"
        )
        print(
            "Detected beats: ",
            rhythm.get("beat_count")
        )
        print(
            "Grid stability: ",
            rhythm.get("grid_stability")
        )

        residuals = (
            rhythm.get("residuals_ms")
            or {}
        )

        print(
            "Median residual:",
            residuals.get("median_abs"),
            "ms"
        )
        print(
            "Mean residual:  ",
            residuals.get("mean_abs"),
            "ms"
        )
        print(
            "Max residual:   ",
            residuals.get("max_abs"),
            "ms"
        )
        print(
            "Residual std:   ",
            residuals.get("std"),
            "ms"
        )
    else:
        print(
            "Unavailable:",
            rhythm.get("status")
        )

        if rhythm.get("error"):
            print(
                "Reason:     ",
                rhythm.get("error")
            )

    print(
        "\nSTRONGEST ONSETS -> RHYTHMIC GRID [MEASURED]"
    )

    if relationships:
        for relation in relationships[:15]:
            print(
                f"{relation['onset_time_seconds']:8.3f}s | "
                f"frame {relation['onset_frame']:5d} | "
                f"{relation['rhythmic_position']:<19} | "
                f"beat {relation['reference_beat_number']:03d} | "
                f"target "
                f"{relation['rhythmic_target_time_seconds']:8.3f}s | "
                f"delta "
                f"{relation['signed_delta_ms']:+7.2f} ms | "
                f"distance "
                f"{relation['rhythmic_grid_distance_ms']:6.2f} ms"
            )
    else:
        print(
            "No onset/beat relationships available."
        )

    print(
        "\nGRID STABILITY != MUSICAL CORRECTNESS"
    )
    print(
        "SECONDS ARE THE SOURCE OF TRUTH"
    )

    print("\nCAPABILITY CONTRACT")
    print("Signal analysis:       YES")
    print("Perceptual listening:  NO")
    print()
    print("MEASUREMENT != LISTENING")

    print("\nNOT VERIFIED BY THIS ANALYSIS")
    for item in report["capability"]["not_verified"]:
        print("- " + item)

    print()
    print("=" * 64)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Analyze measurable audio properties "
            "from a motion-design video."
        )
    )

    parser.add_argument(
        "input",
        help="Video or audio file"
    )

    parser.add_argument(
        "--fps",
        type=float,
        default=None,
        help=(
            "Timeline FPS. If omitted, use "
            "video metadata or 30."
        ),
    )

    parser.add_argument(
        "--json",
        dest="json_path",
        default=None,
        help="Optional JSON output path",
    )

    args = parser.parse_args()

    source = Path(args.input)

    if not source.exists():
        print(
            f"ERROR: file not found: {source}",
            file=sys.stderr,
        )
        return 2

    try:
        require_tool("ffmpeg")
        require_tool("ffprobe")

        media = probe_media(source)

        if not media["audio_present"]:
            print(
                "ERROR: input contains no audio stream.",
                file=sys.stderr,
            )
            return 3

        fps = (
            args.fps
            or media["video"].get(
                "reported_fps"
            )
            or 30.0
        )

        with tempfile.TemporaryDirectory(
            prefix="mdd_audio_"
        ) as temp_dir:

            wav = Path(temp_dir) / "analysis.wav"

            extract_wav(
                source,
                wav
            )

            audio, sr = decode_wav_pcm(
                wav
            )

            loudness = analyze_loudness(
                source
            )

            silence = detect_silence(
                source
            )

            stats = signal_stats(
                audio
            )

            onsets = detect_onsets(
                audio,
                sr,
                fps,
            )

            rhythm = analyze_rhythm(
                wav,
                fps,
            )

            onset_beat_relationships = (
                relate_onsets_to_beats(
                    onsets,
                    rhythm,
                    fps,
                )
            )

        report = build_report(
            source,
            fps,
            media,
            loudness,
            silence,
            stats,
            onsets,
            rhythm,
            onset_beat_relationships,
        )

        print_report(report)

        output = (
            Path(args.json_path)
            if args.json_path
            else source.with_suffix(
                ".audio-analysis.json"
            )
        )

        output.write_text(
            json.dumps(
                report,
                indent=2,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        print(
            f"\nJSON saved: {output.resolve()}"
        )

        return 0

    except Exception as exc:
        print(
            f"ERROR: {exc}",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())