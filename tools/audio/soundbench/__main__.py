"""soundbench command line: `python -m tools.audio.soundbench <command>`.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Every number is a screening aid, never a taste verdict (design G-4). Exit codes: 0 done, 1 doctor found a missing
item or a render target failed, 2 refused or failed (the reason on stderr; any unexpected error is 2), 3 a paid-reveal
family is incomplete (render).

Usage:
  python -m tools.audio.soundbench doctor [--root DIR] [--json]
  python -m tools.audio.soundbench measure <file> [--low-cut HZ] [--high-pitch] [--json] [--picture PNG]
  python -m tools.audio.soundbench compare <a> <b> [--low-cut HZ] [--high-pitch] [--json]
  python -m tools.audio.soundbench parity <file> <file> [...] --mode integrated|momentary [--json]
  python -m tools.audio.soundbench render <cue-folder> [--picture] [--json]
  python -m tools.audio.soundbench rank <cue-folder> [--round K] [--picture] [--json]
  python tools/keys.py run --only ELEVENLABS_API_KEY -- python -m tools.audio.soundbench generate <cue-folder>
      [--budget CREDITS] [--dry-run] [--json]
Exit codes for rank: 0 the top take passes every must-target after its fixable steps (a layered round: every layer
and their mix); 1 regenerate with a changed prompt (or, after round 3, the cue goes to the owner; or the layers pass
alone and their mix misses); 2 refused.
Exit codes for render: 0 every must-target and the family check passed; 1 one failed (file written, report says
why); 2 refused; 3 a paid-reveal family is incomplete (re-render after the siblings).
Exit codes for generate: 0 every planned take made and decoded; 1 stopped by the budget or a take rejected; 2 refused
before any call, or a call failed.
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


def _generate(a) -> int:
    """Its own handler: every text it prints passes the key redaction (AGENTS.md section 3.4)."""
    import os

    from . import generate as gen

    key = os.environ.get(gen.KEY_ENV, "").strip()
    try:
        doc, code = gen.generate(a.cue, gen.DEFAULT_BUDGET if a.budget is None else a.budget, dry_run=a.dry_run)
    except SoundbenchError as err:
        print(gen.redact(f"ERROR: {err}", key), file=sys.stderr)
        return 2
    except Exception as err:  # noqa: BLE001 - an unexpected failure is a refusal (2)
        print(gen.redact(f"ERROR (unexpected, a soundbench bug or a malformed input): {type(err).__name__}: {err}",
                         key), file=sys.stderr)
        return 2
    if a.json:
        print(gen.redact(json.dumps(doc, indent=2), key))
        return code
    lines = [f"{doc['cue']} ({doc['tier']}): " + ", ".join(f"{s['name']} round {s['round']}" for s in doc["sounds"]),
             f"predicted {doc['predicted_credits']} credits, budget {doc['budget']:g}"]
    if doc.get("dry_run"):
        lines += [f"  {c['stem']}: {c['predicted']} credits, {c['text'][:70]}" for c in doc["plan"]]
    else:
        lines += [f"  {t['stem']}: {t['format_used']}, {t['credits']} credits" for t in doc["takes"]]
        lines += [f"  {t['stem']}: REJECTED {t['rejected']}" for t in doc["rejected"]]
        lines.append(f"spent {doc['spent_credits']} credits (+ {doc['possibly_spent_credits']} possibly, network "
                     f"failures); formats refused: {doc['formats_refused'] or 'none'}")
        if doc["stopped"]:
            lines.append(f"stopped: {doc['stopped']}")
        lines.append(f"log: {doc['log']}  exit {code}")
    lines += [f"warning: {w}" for w in doc["warnings"]]
    print(gen.redact("\n".join(lines), key))
    return code


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
    k = sub.add_parser("rank", help="score every take of a round against card.json and put them in order")
    k.add_argument("cue", type=Path, help="the cue folder (card.json, takes/)")
    k.add_argument("--round", type=int, help="the round to rank (default: the highest present; at most 3, J020-D7)")
    k.add_argument("--picture", action="store_true", help="pictures of every take (default: the top take when needed)")
    k.add_argument("--json", action="store_true")
    g = sub.add_parser("generate", help="one round of ElevenLabs takes for a cue (prompts.json, card.json)")
    g.add_argument("cue", type=Path, help="the cue folder (card.json, prompts.json)")
    g.add_argument("--budget", type=float, default=None, help="credits this run may spend (default: "
                   "generate.DEFAULT_BUDGET)")
    g.add_argument("--dry-run", action="store_true", help="plan and predict the cost; no call, no key needed")
    g.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "generate":
        return _generate(a)
    try:
        if a.cmd == "doctor":
            return doctor.main(a.root, a.json)
        if a.cmd == "render":
            from . import render as rendermod

            doc, code = rendermod.render(a.cue, a.picture)
            outs = doc.get("outputs") or [{"name": doc["cue"], "file": doc["export"]["file"], "export": doc["export"]}]
            rep = {"cue": doc["cue"], "file": doc["export"]["file"], "files": [str(o["file"]) for o in outs],
                   "exit_code": code, "must_failed": doc["must_failed"], "targets": doc["targets"],
                   "form_checks": doc["form_checks"], "family": doc["family"],
                   "audio_sha256_float32": doc["export"]["audio_sha256_float32"],
                   "audio_sha256_float32_all": {o["name"]: o["export"]["audio_sha256_float32"] for o in outs}}
            if a.json:
                print(json.dumps(rep, indent=2))
            else:
                for t in rep["targets"] + rep["form_checks"]:
                    label = (t["output"] + ": " if "output" in t else "") + t["target"]
                    print(f"{t['result']:<8} {label:<18} {t['measure']:<28} {t['value']} "
                          f"(min {t['min']}, max {t['max']}, {'must' if t['must'] else 'aim'})")
                if rep["family"]:
                    print(f"family {rep['family']['id']}: {rep['family']['result']} {rep['family'].get('reason', '')}")
                print(f"file{'s' if len(rep['files']) > 1 else ''}: {', '.join(rep['files'])}  exit {code}")
            return code
        if a.cmd == "rank":
            from . import rank as rankmod

            doc, code = rankmod.rank(a.cue, a.round, a.picture)
            if doc.get("form") == "layers":  # a layered round: one order per layer, then the mix
                if a.json:
                    out = {k_: doc[k_] for k_ in ("cue", "round", "verdict", "proof", "warnings", "exit_code")}
                    out["layers"] = {lay["name"]: lay["order"] for lay in doc["layers"]}
                    print(json.dumps(out, indent=2, default=str))
                else:
                    for lay in doc["layers"]:
                        print(f"layer {lay['name']} (round {lay['round']}):")
                        for i, e in enumerate(lay["takes"], 1):
                            state = ("rejected: " + "; ".join(e["rejected"]) if e["rejected"] else
                                     "passes as placed" if e["passes_after_fix"] else f"must misses {e['must_after']}")
                            print(f"  {i}. {e['take']:<40} {state}; aim misses {e['aim_after']}")
                    if doc["mix"] is not None:
                        print(f"mix {doc['mix']['takes']}: must misses after fix {doc['mix']['must_after']}")
                    print(f"verdict: {doc['verdict']['say']}")
                    print(f"report: {a.cue / 'report' / (doc['cue'] + '.r' + str(doc['round']) + '.rank.md')}  "
                          f"exit {code}")
                return code
            if a.json:
                print(json.dumps({k_: doc[k_] for k_ in ("cue", "round", "order", "verdict", "proof", "warnings",
                                                         "exit_code")}, indent=2))
            else:
                for i, e in enumerate(doc["takes"], 1):
                    state = ("rejected: " + "; ".join(e["rejected"]) if e["rejected"] else
                             "passes after fix" if e["passes_after_fix"] else f"must misses after fix {e['must_after']}")
                    print(f"{i}. {e['take']:<34} {state}; fixed {e['fixed']}; aim misses {e['aim_after']}")
                print(f"verdict: {doc['verdict']['say']}")
                for d in doc["verdict"].get("prompt_must_change", []):
                    print(f"  prompt must change: {d['target']} ({'must' if d['must'] else 'aim'}) missed by "
                          f"{d['takes_missing']} of {d['of']}; closest {d['closest']}")
                print(f"report: {a.cue / 'report' / (doc['cue'] + '.r' + str(doc['round']) + '.rank.md')}  exit {code}")
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
    except Exception as err:  # noqa: BLE001 - an unexpected failure is a refusal (2), never "a target failed" (1)
        print(f"ERROR (unexpected, a soundbench bug or a malformed input): {type(err).__name__}: {err}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(rec, indent=2))
    else:
        _print(rec)
    return 0


if __name__ == "__main__":
    sys.exit(main())
