"""Measure a delivered sound file (F-01 to F-12) and loudness parity across files (F-13) - without AI taste.

Kit tool (universal). It replaces the hand-written recipes of `sound-design/references/review.md` section 4 (owner
decision J018-D7, G3-P1). The measures and their known false readings are defined there; this tool computes them
the same way. Every number is a screening aid: a FAIL, or a reading near its limit, is looked at on a waveform and
spectrogram before any fix note (review.md section 4).

Since J020 (editor-design.md G-3: one way to measure) this file is a thin wrapper: the measures live in
`tools/audio/soundbench/measures.py`, unchanged in meaning, checked against golden JSON of this tool's output before
the move (`tools/audio/soundbench/golden/cue_check_golden.json`). The command line and the output are unchanged.
Wrapper: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2).

Reading: `soundfile` (always 2-D), the mean of each channel subtracted first (generated audio often carries a DC
offset); mono = the mean of the channels. F-03 true peak needs `scipy`; F-13 needs `pyloudnorm`.

Usage:
  python tools/audio/cue_check.py measure <file> [--low-cut HZ] [--high-pitch] [--json]
  python tools/audio/cue_check.py parity <file> <file> [...] --mode integrated|momentary [--json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.audio.soundbench import measures as _m  # noqa: E402
from tools.audio.soundbench.measures import (  # noqa: E402,F401
    MOMENTARY_S, NOTE_NAMES, ONSET_DB, TAIL_DB, WIN_S, CueError, db, load, onset_index, pitch, sound_end, windows_rms)


def measure(path: Path, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    return _m.cue_record(path, low_cut, high_pitch, tool="cue_check measure")


def parity(paths: list[Path], mode: str) -> dict:
    return _m.parity(paths, mode, tool="cue_check parity")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("measure", help="F-01 to F-12 for one file")
    m.add_argument("file", type=Path)
    m.add_argument("--low-cut", type=float, help="the layer's low cut in Hz (F-06 share below it)")
    m.add_argument("--high-pitch", action="store_true", help="F-10 band up to 12 kHz (chimes, sparkles, ticks)")
    m.add_argument("--json", action="store_true")
    p = sub.add_parser("parity", help="F-13 loudness parity across files")
    p.add_argument("files", type=Path, nargs="+")
    p.add_argument("--mode", choices=("integrated", "momentary"), required=True,
                   help="integrated: options and siblings; momentary: paid random results (trimmed, 100 ms)")
    p.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        rec = measure(a.file, a.low_cut, a.high_pitch) if a.cmd == "measure" else parity(a.files, a.mode)
    except CueError as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(rec, indent=2))
    else:
        for k, v in rec.items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
