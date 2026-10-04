"""
Motion Design Director - Rhythm Analysis Worker

Runs under the dedicated Python 3.11 environment.

Core rules:
    MEASUREMENT != LISTENING
    GRID STABILITY != MUSICAL CORRECTNESS
    SECONDS ARE THE SOURCE OF TRUTH
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import librosa
import numpy as np


VERSION = "0.1.0"


def classify_grid_stability(
    median_abs_ms: float,
    mean_abs_ms: float,
) -> str:
    if median_abs_ms <= 10.0 and mean_abs_ms <= 15.0:
        return "HIGH"

    if median_abs_ms <= 25.0 and mean_abs_ms <= 30.0:
        return "MEDIUM"

    return "LOW"


def analyze_rhythm(
    wav: Path,
    fps: float,
) -> dict:
    y, sr = librosa.load(
        str(wav),
        sr=None,
        mono=True,
    )

    tempo_raw, detected_beats = librosa.beat.beat_track(
        y=y,
        sr=sr,
        tightness=400,
        units="time",
    )

    tempo_raw = float(
        np.asarray(tempo_raw).reshape(-1)[0]
    )

    detected_beats = np.asarray(
        detected_beats,
        dtype=float,
    )

    result = {
        "worker_version": VERSION,
        "sample_rate": int(sr),
        "raw_bpm": round(tempo_raw, 6),
        "beat_count": int(len(detected_beats)),
        "seconds_source_of_truth": True,
        "grid_stability_is_musical_correctness": False,
    }

    if len(detected_beats) < 2:
        result.update({
            "fitted_bpm": None,
            "beat_period_seconds": None,
            "grid_offset_seconds": None,
            "grid_stability": None,
            "residuals_ms": {
                "median_abs": None,
                "mean_abs": None,
                "max_abs": None,
                "std": None,
            },
            "beats": [],
        })

        return result

    indices = np.arange(
        len(detected_beats),
        dtype=float,
    )

    design = np.vstack([
        np.ones(len(indices)),
        indices,
    ]).T

    t0, period = np.linalg.lstsq(
        design,
        detected_beats,
        rcond=None,
    )[0]

    predicted = t0 + indices * period

    residual_ms = (
        detected_beats - predicted
    ) * 1000.0

    median_abs = float(
        np.median(np.abs(residual_ms))
    )

    mean_abs = float(
        np.mean(np.abs(residual_ms))
    )

    max_abs = float(
        np.max(np.abs(residual_ms))
    )

    std = float(
        np.std(residual_ms)
    )

    fitted_bpm = 60.0 / float(period)

    beats = []

    for index, detected_time in enumerate(detected_beats):
        grid_time = float(
            t0 + index * period
        )

        beats.append({
            "number": index + 1,
            "detected_time_seconds": round(
                float(detected_time),
                6,
            ),
            "grid_time_seconds": round(
                grid_time,
                6,
            ),
            "frame": int(
                round(grid_time * fps)
            ),
            "residual_ms": round(
                float(residual_ms[index]),
                3,
            ),
        })

    result.update({
        "fitted_bpm": round(
            fitted_bpm,
            6,
        ),
        "beat_period_seconds": round(
            float(period),
            9,
        ),
        "grid_offset_seconds": round(
            float(t0),
            9,
        ),
        "grid_stability": classify_grid_stability(
            median_abs,
            mean_abs,
        ),
        "residuals_ms": {
            "median_abs": round(
                median_abs,
                3,
            ),
            "mean_abs": round(
                mean_abs,
                3,
            ),
            "max_abs": round(
                max_abs,
                3,
            ),
            "std": round(
                std,
                3,
            ),
        },
        "beats": beats,
    })

    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Measure beat-grid properties from normalized WAV audio."
        )
    )

    parser.add_argument(
        "wav",
        help="Normalized PCM WAV input",
    )

    parser.add_argument(
        "--fps",
        type=float,
        default=30.0,
        help="Timeline FPS used only for time-to-frame mapping.",
    )

    args = parser.parse_args()

    wav = Path(args.wav)

    if not wav.exists():
        print(
            json.dumps({
                "error": f"File not found: {wav}"
            }),
            file=sys.stderr,
        )
        return 2

    try:
        result = analyze_rhythm(
            wav,
            args.fps,
        )

        print(
            json.dumps(
                result,
                ensure_ascii=True,
            )
        )

        return 0

    except Exception as exc:
        print(
            json.dumps({
                "error": str(exc),
            }),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())