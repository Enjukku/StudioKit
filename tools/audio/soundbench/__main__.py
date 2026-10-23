"""soundbench command line: `python -m tools.audio.soundbench <command>`.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Every number is a screening aid, never a taste verdict (design G-4). Exit codes: 0 done, 1 doctor found a missing
item, 2 refused or failed (the reason on stderr).

Usage:
  python -m tools.audio.soundbench doctor [--root DIR] [--json]
  python -m tools.audio.soundbench measure <file> [--low-cut HZ] [--high-pitch] [--json] [--picture PNG]
  python -m tools.audio.soundbench compare <a> <b> [--low-cut HZ] [--high-pitch] [--json]
  python -m tools.audio.soundbench parity <file> <file> [...] --mode integrated|momentary [--json]
  python -m tools.audio.soundbench render <cue-folder> [--picture] [--json]
Exit codes for render: 0 every must-target and the family check passed; 1 one failed (file written, report says
why); 2 refused.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import doctor, measures
from .core import SoundbenchError

COMPARE_LAG_SEARCH_S = 0.1


def flatten(rec: dict, prefix: str = "") -> dict:
    out: dict = {}
    for k, v in rec.items():
        key = f"{prefix}{k}"
        if isinstance(v, dict):
            out.update(flatten(v, key + "."))
        else:
            out[key] = v
    return out


def compare(a: Path, b: Path, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    ra, rb = measures.measure(a, low_cut, high_pitch), measures.measure(b, low_cut, high_pitch)
    fa, fb = flatten(ra), flatten(rb)
    rows = []
    for key in [k for k in fa if k not in ("tool", "file", "verdict")] + [k for k in fb if k not in fa]:
        va, vb = fa.get(key), fb.get(key)
        num = all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in (va, vb))
        rows.append({"measure": key, "a": va, "b": vb, "b_minus_a": round(vb - va, 4) if num else None})
    out = {"tool": "soundbench compare", "a": str(a), "b": str(b), "rows": rows,
           "verdict": "measured (screening aid: look at both waveforms before any fix note)"}
    xa, rate_a = measures.load(Path(a))
    xb, rate_b = measures.load(Path(b))
    if rate_a == rate_b:
        out["lag_b_vs_a"] = measures.lag(xa, xb, rate_a, int(COMPARE_LAG_SEARCH_S * rate_a))
    else:
        out["lag_b_vs_a"] = f"not measured: rates differ ({rate_a} vs {rate_b})"
    return out


def _print(rec: dict) -> None:
    if "rows" in rec and rec.get("tool") == "soundbench compare":
        width = max(len(r["measure"]) for r in rec["rows"])
        print(f"a: {rec['a']}\nb: {rec['b']}")
        print(f"{'measure':<{width}}  {'a':>14}  {'b':>14}  {'b-a':>10}")
        for r in rec["rows"]:
            d = "" if r["b_minus_a"] is None else r["b_minus_a"]
            print(f"{r['measure']:<{width}}  {str(r['a']):>14}  {str(r['b']):>14}  {str(d):>10}")
        print(f"lag_b_vs_a: {rec['lag_b_vs_a']}")
        print(f"verdict: {rec['verdict']}")
        return
    for k, v in rec.items():
        print(f"{k}: {v}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m tools.audio.soundbench", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("doctor", help="ffmpeg, filters, libraries, the ElevenLabs key entry")
    d.add_argument("--root", type=Path, default=doctor.ROOT, help="repo root holding knowledge/design/keys.json")
    d.add_argument("--json", action="store_true")
    for name, helptext in (("measure", "every measure of one file"), ("compare", "two files side by side")):
        m = sub.add_parser(name, help=helptext)
        m.add_argument("files", type=Path, nargs=1 if name == "measure" else 2)
        m.add_argument("--low-cut", type=float, help="the layer's low cut in Hz (F-06 share below it)")
        m.add_argument("--high-pitch", action="store_true", help="F-10 band up to 12 kHz (chimes, sparkles, ticks)")
        m.add_argument("--json", action="store_true")
        if name == "measure":
            m.add_argument("--picture", type=Path, metavar="PNG", help="also write a waveform + spectrogram PNG")
    p = sub.add_parser("parity", help="F-13 loudness parity across files")
    p.add_argument("files", type=Path, nargs="+")
    p.add_argument("--mode", choices=("integrated", "momentary"), required=True,
                   help="integrated: options and siblings; momentary: paid random results (trimmed, 100 ms)")
    p.add_argument("--json", action="store_true")
    r = sub.add_parser("render", help="apply recipe.json to the take, export FLAC, check the card's targets")
    r.add_argument("cue", type=Path, help="the cue folder (card.json, recipe.json, takes/)")
    r.add_argument("--picture", action="store_true", help="always write the before and after pictures")
    r.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        if a.cmd == "doctor":
            return doctor.main(a.root, a.json)
        if a.cmd == "render":
            from . import render as rendermod

            doc, code = rendermod.render(a.cue, a.picture)
            rep = {"cue": doc["cue"], "file": doc["export"]["file"], "exit_code": code, "must_failed": doc["must_failed"],
                   "targets": doc["targets"], "family": doc["family"],
                   "audio_sha256_float32": doc["export"]["audio_sha256_float32"]}
            if a.json:
                print(json.dumps(rep, indent=2))
            else:
                for t in rep["targets"]:
                    print(f"{t['result']:<8} {t['target']:<18} {t['measure']:<28} {t['value']} "
                          f"(min {t['min']}, max {t['max']}, {'must' if t['must'] else 'aim'})")
                if rep["family"]:
                    print(f"family {rep['family']['id']}: {rep['family']['result']} {rep['family'].get('reason', '')}")
                print(f"file: {rep['file']}  exit {code}")
            return code
        if a.cmd == "measure":
            rec = measures.measure(a.files[0], a.low_cut, a.high_pitch)
            if a.picture:
                from . import pictures
                from .core import read_float32

                x, rate = read_float32(a.files[0])
                rec["picture"] = str(pictures.picture(x, rate, a.picture, title=a.files[0].name))
        elif a.cmd == "compare":
            rec = compare(a.files[0], a.files[1], a.low_cut, a.high_pitch)
        else:
            rec = measures.parity(a.files, a.mode)
    except SoundbenchError as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(rec, indent=2))
    else:
        _print(rec)
    return 0


if __name__ == "__main__":
    sys.exit(main())
