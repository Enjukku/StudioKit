"""`rank`: score every take of one round against the cue's card and put them in order (editor-design.md section 6;
build step 5).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 5)

Order of work, each step refusing instead of guessing:
  1. read card.json (every field checked) and refuse an inconsistent family declaration, exactly as `render` does;
     find the round's takes `takes/<cue>.r<k>.t<n>.mp3` (the highest round unless `--round`; round 4 or more is
     refused, J020-D7); check every take's sha256 and master against its sidecar (G-1, `render.check_take`);
  2. measure every master (`measures.measure_audio`) and score every target with `render.evaluate`, the function
     `render` uses on the delivered file: inside, near (inside but within the `near` margin of `tables.json`) or
     miss, with `miss_by` (how far outside) or `margin` (how far inside);
  3. reject outright (no fix is simulated): clipped at the source, near-silent, no sound in a band the card needs;
  4. fixability is computed, never guessed: the edit-pass steps for the take's misses (a late start: `trim`; too long:
     `cut` with a fade-out; an edge click: `trim` or `fade`; mono; the level: `loudness` then `peak`) are run on the
     master through the same step loop as `render` (`render.apply_steps`), the result is measured again and scored
     again. A miss counts as fixed only when that re-measured row passes. The level is also derived from the measures
     (gain needed against the true-peak headroom, below) and the two must agree within 0.1 dB, or rank refuses
     (a soundbench bug, never a silent wrong number);
  5. order: rejected last; then fewest must-misses after the fix, fewest aim-misses after the fix, fewest misses that
     needed a fix, fewest near readings, the take number (`rank_key`, recomputable from the table);
  6. proof: the top take's fix recipe is rendered for real (`render.render` on a temp copy of the cue: hash checks,
     parameter checks, the edit pass, FLAC export, the delivered file measured again) and every target row must
     match the simulation, or rank refuses. The temp copy is removed; rank never writes `out/` or family state;
  7. write report/<cue>.r<k>.rank.json and .md; pictures (light-check rule, owner J005-D8) of the top take before and
     after its fix when an after-fix row misses or reads near, or for an important cue; `--picture` draws every take.

The level (review-1 #9). `peak` sets the level by gain only, never a limiter, and sfx and ui do not limit transients,
so a too-quiet take is fixable only when the gain fits inside its true-peak headroom:
    gain_needed  = level target - level in (the card's own level measure, on the audio entering `loudness`)
    peak_limit   = min(-1.0, the card's true_peak_dbtp max) - 0.5            (ops.PEAK_CEILING_DBTP, PEAK_MARGIN_DB)
    headroom     = peak_limit - true peak in
    peak_cut     = max(0, true peak in + gain_needed - peak_limit)
    predicted    = level in + gain_needed - peak_cut;  fits when |predicted - target| <= tolerance
A take too loud always fits (gain down). For music, ambience and voice a `limit` design step could make room; rank does
not compute design steps, so it does not count that as a fix.

Paid-reveal families (D-03): rank refuses an inconsistent family declaration as `render` does, writes no family
state, and never checks parity: `render` runs D-03 across every member's delivered file, unchanged.

Exit codes (command line): 0 the top take passes every must-target after its fixable steps; 1 no take does: regenerate
with a changed prompt (the misses it must change are listed), or after round 3 the cue goes to the owner with its
numbers (J020-D7); 2 refused or bad input (also a rank/render disagreement).

Usage:
  python -m tools.audio.soundbench rank content/audio/<cue-id> [--round K] [--picture] [--json]
"""

from __future__ import annotations

import json
import math
import re
import shutil
import tempfile
from pathlib import Path

import numpy as np

from . import card as cardmod
from . import measures, ops, render
from .core import SoundbenchError, versions

TAKES_PER_ROUND = {"minor": 3, "frequent": 4, "important": 6}  # J020-D9 (owner)
MAX_ROUNDS = 3  # J020-D7 (owner): at most 3 rounds, then the cue goes to the owner with its numbers
NEAR: dict = cardmod.TABLES["near"]

# PROPOSAL values (start points a check may change)
NEAR_SILENT_DBFS = -60.0  # a take peaking under -60 dBFS is near-silent (62 real takes: the quietest peaks -43.9)
CLIP_FULL_SCALE_DBFS = -1.0  # clipped at the source: the decoded peak reaches -1 dBFS or more ...
CLIP_TOP_DB = 0.5  # ... and the take stays within 0.5 dB of its own peak ...
CLIP_TOP_MS = 8.0  # ... for 8 ms or more in total (62 real takes: at most 4.4 ms; clipped fixtures 9.5-161 ms)
NO_BAND_FRACTION = 0.1  # a must band holding under a tenth of the card's minimum share has no sound there
FIX_FADE_OUT_MS = 10.0  # the fade-out rank adds with a cut, and for a click at the end edge
CUT_INSIDE_MS = 1.0  # a cut for sound_ms ends 1 ms inside the card's maximum
LEVEL_AGREE_DB = 0.1  # the derived and the simulated level must agree within this
PROOF_ABS, PROOF_REL = 0.02, 0.002  # the proof render's values vs the simulation's: 0.02 or 0.2 %, whichever is larger

TAKE_RE = re.compile(r"^(?P<cue>.+)\.r(?P<round>\d+)\.t(?P<take>\d+)\.mp3$", re.IGNORECASE)
STEP_FOR = {"onset_ms": "trim", "main_transient_ms": "trim", "sound_ms": "cut", "file_ms": "cut",
            "level": "loudness and peak", "true_peak_dbtp": "loudness and peak", "sample_peak_dbfs": "loudness and peak",
            "form.mono": "mono", "edge_clicks": "trim or fade"}
BANDS = ("below_120", "band_120_500", "band_500_5k", "above_5k")


def find_takes(cue_dir: Path, cue: str, round_no: int | None) -> tuple[int, list[tuple[int, str]]]:
    """(round, [(take number, path relative to the cue folder)]) for the asked round, or the highest one present."""
    found: dict[int, list[tuple[int, str]]] = {}
    for p in sorted((cue_dir / "takes").glob("*.mp3")):
        m = TAKE_RE.match(p.name)
        if m and m["cue"] == cue:
            found.setdefault(int(m["round"]), []).append((int(m["take"]), f"takes/{p.name}"))
    if not found:
        raise SoundbenchError(f"no takes named takes/{cue}.r<k>.t<n>.mp3 in {cue_dir}")
    k = max(found) if round_no is None else round_no
    if k < 1 or k > MAX_ROUNDS:
        raise SoundbenchError(f"round {k}: a cue has at most {MAX_ROUNDS} rounds (J020-D7); after round {MAX_ROUNDS} it "
                              "goes to the owner with its numbers, refused")
    if k not in found:
        raise SoundbenchError(f"round {k} has no takes (rounds present: {sorted(found)})")
    return k, sorted(found[k])


def clip_reading(x: np.ndarray, rate: int) -> dict:
    """Clipped at the source: the raw decoded samples reach full scale and sit at their own peak for long.

    Known false readings: a sustained or low tone normalised to full scale stays near its peak for long and reads
    clipped; clipping that was scaled down after it happened is not seen (the full-scale condition); a single short
    clipped crack under 8 ms in total is not seen."""
    a = np.abs(np.asarray(x, dtype=np.float64))
    peak = float(a.max())
    pk_db = measures.db(peak)
    top_ms = 0.0 if peak <= 0 else 1000 * float(np.sum(np.any(a >= peak * 10 ** (-CLIP_TOP_DB / 20), axis=1))) / rate
    clipped = pk_db is not None and pk_db >= CLIP_FULL_SCALE_DBFS and top_ms >= CLIP_TOP_MS
    return {"sample_peak_dbfs": None if pk_db is None else round(pk_db, 2), "ms_within_0.5db_of_peak": round(top_ms, 3),
            "clipped": clipped}


def rejections(card: dict, flat: dict, clip: dict) -> list[str]:
    out = []
    if clip["clipped"]:
        out.append(f"clipped at the source: peak {clip['sample_peak_dbfs']} dBFS (>= {CLIP_FULL_SCALE_DBFS}) and "
                   f"{clip['ms_within_0.5db_of_peak']} ms within {CLIP_TOP_DB} dB of its own peak (>= {CLIP_TOP_MS})")
    pk = clip["sample_peak_dbfs"]
    if pk is None or pk < NEAR_SILENT_DBFS:
        out.append(f"near-silent: sample peak {pk} dBFS (under {NEAR_SILENT_DBFS})")
    for name in BANDS:
        spec = card.get("targets", {}).get(name)
        if spec and spec["must"] and spec.get("min", 0) > 0:
            v = flat.get(cardmod.TARGETS[name])
            if v is not None and v < NO_BAND_FRACTION * spec["min"]:
                out.append(f"no sound in the band the card needs: {name} share {v} is under a tenth of its minimum "
                           f"{spec['min']}")
    return out


def score(rows: list[dict]) -> list[dict]:
    """Add `score` (inside, near or miss), `miss_by` (outside by, > 0) and `margin` (inside by) to evaluate's rows."""
    out = []
    for r in rows:
        r = dict(r)
        v, lo, hi = r["value"], r["min"], r["max"]
        num = isinstance(v, (int, float)) and not isinstance(v, bool)
        r["miss_by"] = r["margin"] = None
        if r["result"] != "pass":
            r["score"] = "miss"
            if num:
                r["miss_by"] = round(lo - v if lo is not None and v < lo else v - hi if hi is not None and v > hi else 0, 4)
        else:
            r["score"] = "inside"
            gaps = [g for g in ((v - lo) if num and lo is not None else None, (hi - v) if num and hi is not None else None)
                    if g is not None]
            if gaps:
                r["margin"] = round(min(gaps), 4)
                if r["margin"] < NEAR.get(r["target"], 0):
                    r["score"] = "near"
        out.append(r)
    return out


def _over(rows: list[dict], target: str) -> bool:
    r = next((r for r in rows if r["target"] == target), None)
    return r is not None and r["result"] != "pass" and r["max"] is not None and r["value"] is not None and \
        r["value"] > r["max"]


def _missed(rows: list[dict], target: str) -> bool:
    return any(r["target"] == target and r["result"] != "pass" for r in rows)


def fix_plan(card: dict, raw_rows: list[dict], raw_flat: dict, trimmed: tuple | None) -> list[dict]:
    """The edit-pass steps for a take's misses (recipe form; render runs them in the fixed edit order).

    `trim` from the raw misses (a late onset or main transient, a click at the start edge). `cut` and the end fade from
    the misses of the audio after `trim` (`trimmed` = (rows, flat, audio, rate)): trimming moves the length and the
    windows the measures read, so the raw length is not the one `cut` meets. Whenever any step runs, `loudness` and
    `peak` close the pass (every step can move the level; render sets the level last)."""
    steps = []
    if _over(raw_rows, "onset_ms") or _over(raw_rows, "main_transient_ms") or \
            (_missed(raw_rows, "edge_clicks") and "start" in (raw_flat.get("clicks.edges") or [])):
        steps.append({"op": "trim"})
    rows, flat, y, rate = trimmed if trimmed else (raw_rows, raw_flat, None, None)
    end = cut_end(card, rows, y, rate) if y is not None else None
    if end is not None:
        steps.append({"op": "cut", "end_ms": end})
    if end is not None or (_missed(rows, "edge_clicks") and "end" in (flat.get("clicks.edges") or [])):
        steps.append({"op": "fade", "out_ms": FIX_FADE_OUT_MS})
    if _missed(raw_rows, "form.mono"):
        steps.append({"op": "mono"})
    if steps or _missed(raw_rows, "level") or _over(raw_rows, "true_peak_dbtp") or _over(raw_rows, "sample_peak_dbfs"):
        steps += [{"op": "loudness"}, {"op": "peak"}]
    return steps


def cut_end(card: dict, rows: list[dict], y: np.ndarray, rate: int) -> float | None:
    """Where `cut` ends (ms, on the audio after `trim`) when sound_ms or file_ms is over its maximum; else None."""
    tg = card.get("targets", {})
    ends = []
    if _over(rows, "file_ms"):
        ends.append(tg["file_ms"]["max"])
    if _over(rows, "sound_ms"):
        a = y - y.mean(axis=0)
        f01 = 1000 * measures.onset_index(a.mean(axis=1)) / rate
        ends.append(f01 + tg["sound_ms"]["max"] - CUT_INSIDE_MS)
    return None if not ends else round(max(1.0, min(ends)), 1)


def simulate(card: dict, x: np.ndarray, rate: int, raw_rows: list[dict], flat: dict) -> dict:
    """Run the fix through `render`'s own step loop, measure and score again, and derive the level independently."""
    def planned(steps):
        _, edit, _ = render.plan(card, {"design": [], "edit": steps})
        return edit

    pre_ops = ("trim", "cut", "fade", "mono")
    head = planned([s for s in fix_plan(card, raw_rows, flat, None) if s["op"] == "trim"])
    y_trim, _ = render.apply_steps((("edit", head),), card, render.context(card, head), x, rate)
    rec_t = measures.measure_audio(y_trim, rate)
    trimmed = (score(render.evaluate(card, rec_t, y_trim, rate)), render._flat(rec_t), y_trim, rate)
    steps = fix_plan(card, raw_rows, flat, trimmed)
    edit = planned(steps)
    ctx = render.context(card, edit)
    pre = [s for s in edit if s["op"] in pre_ops]
    post = [s for s in edit if s["op"] in ("loudness", "peak")]
    y_pre, log_pre = render.apply_steps((("edit", pre),), card, ctx, x, rate)
    lv = card["level"]
    derived = None
    if post:
        level_in = measures.level_db(y_pre, rate, lv["measure"])
        tp_in = measures.true_peak_db(y_pre)
        gain = lv["target"] - level_in if any(s["op"] == "loudness" for s in post) else 0.0
        tp_max = card.get("targets", {}).get("true_peak_dbtp", {}).get("max", 0.0)
        limit = min(ops.PEAK_CEILING_DBTP, tp_max) - ops.PEAK_MARGIN_DB
        cut_db = max(0.0, tp_in + gain - limit) if any(s["op"] == "peak" for s in post) else 0.0
        predicted = level_in + gain - cut_db
        derived = {"measure": lv["measure"], "level_in": round(level_in, 3), "target": lv["target"],
                   "tolerance": lv["tolerance"], "gain_needed_db": round(gain, 3), "true_peak_in_dbtp": round(tp_in, 3),
                   "peak_limit_dbtp": limit, "headroom_db": round(limit - tp_in, 3), "peak_cut_db": round(cut_db, 3),
                   "shortfall_db": round(max(0.0, cut_db - lv["tolerance"]), 3) if gain > 0 else 0.0,
                   "predicted_level": round(predicted, 3),
                   "fits": abs(predicted - lv["target"]) <= lv["tolerance"]}
    y, log_post = render.apply_steps((("edit", post),), card, ctx, y_pre, rate)
    final = measures.measure_audio(y, rate)
    rows = score(render.evaluate(card, final, y, rate))
    if derived is not None:
        sim = next(r for r in rows if r["target"] == "level")["value"]
        derived["simulated_level"] = sim
        if sim is None or abs(sim - derived["predicted_level"]) > LEVEL_AGREE_DB:
            raise SoundbenchError(f"rank: the derived level {derived['predicted_level']} and the simulated level {sim} "
                                  f"disagree by more than {LEVEL_AGREE_DB} dB: a soundbench bug, refused")
    return {"steps": steps, "rows": rows, "level": derived, "log": log_pre + log_post, "audio": y}


def classify(card: dict, raw_rows: list[dict], fix: dict | None) -> tuple[list[dict], list[dict]]:
    """Each raw miss: fixed (by which step) or prompt (why); plus rows the fix itself made miss."""
    after = {r["target"]: r for r in fix["rows"]} if fix else {}
    ran = [s["op"] for s in fix["steps"]] if fix else []
    misses, introduced = [], []
    for r in raw_rows:
        if r["result"] == "pass":
            if fix and after[r["target"]]["result"] != "pass":
                introduced.append({"target": r["target"], "must": r["must"], "before": r["value"],
                                   "after": after[r["target"]]["value"], "steps": ran})
            continue
        item = {"target": r["target"], "must": r["must"], "value": r["value"], "min": r["min"], "max": r["max"],
                "miss_by": r["miss_by"]}
        if fix and after[r["target"]]["result"] == "pass":
            item.update({"fix": "fixed", "by": STEP_FOR.get(r["target"], f"side effect of {ran}"),
                         "after": after[r["target"]]["value"]})
        else:
            item.update({"fix": "prompt", "why": _why(card, r, fix, after.get(r["target"]))})
        misses.append(item)
    return misses, introduced


def _why(card: dict, r: dict, fix: dict | None, a: dict | None) -> str:
    if fix is None:
        return "not simulated (the take is rejected, or its fix was refused)"
    t, v = r["target"], a["value"] if a else None
    if t == "level" and fix["level"] and fix["level"]["gain_needed_db"] > 0:
        d = fix["level"]
        tail = ("sfx and ui do not limit transients (review-1 #9)" if card["category"] in ("sfx", "ui")
                else "a `limit` design step could make room; rank does not compute design steps")
        return (f"needs +{d['gain_needed_db']} dB but the true-peak headroom is {d['headroom_db']} dB (peak limit "
                f"{d['peak_limit_dbtp']} dBTP - true peak {d['true_peak_in_dbtp']} dBTP): the level lands at "
                f"{d['simulated_level']} ({d['shortfall_db']} dB outside the tolerance); {tail}")
    step = STEP_FOR.get(t)
    if step and any(s["op"] in step for s in fix["steps"]):
        return f"{step} ran and it still reads {v}"
    if t in ("onset_ms", "main_transient_ms", "sound_ms", "file_ms") and r["min"] is not None and \
            r["value"] is not None and r["value"] < r["min"]:
        return f"too early or too short ({r['value']} < {r['min']}): no edit-pass step adds time"
    return f"no edit-pass step moves {r['measure']} (rank computes edit-pass fixes only): after the fix it reads {v}"


def take_entry(card: dict, cue_dir: Path, n: int, rel: str) -> dict:
    x, rate, take = render.check_take(cue_dir, {"take": rel})
    rec = measures.measure_audio(x, rate)
    flat = render._flat(rec)
    clip = clip_reading(x, rate)
    raw_rows = score(render.evaluate(card, rec, x, rate))
    rej = rejections(card, flat, clip)
    fix, fix_error = None, None
    if not rej:
        try:
            fix = simulate(card, x, rate, raw_rows, flat)
        except SoundbenchError as err:
            if "soundbench bug" in str(err):
                raise
            fix_error = str(err)
    misses, introduced = classify(card, raw_rows, fix)
    after = fix["rows"] if fix else raw_rows
    must_after = [r["target"] for r in after if r["must"] and r["result"] != "pass"]
    aim_after = [r["target"] for r in after if not r["must"] and r["result"] != "pass"]
    fixed = [m_["target"] for m_ in misses if m_["fix"] == "fixed"]
    near_after = [r["target"] for r in after if r["score"] == "near"]
    passes = not rej and fix is not None and not must_after
    return {"take": take["take"], "n": n, "rate": rate, "channels": int(x.shape[1]),
            "take_sha256": take["take_sha256"], "clip": clip, "rejected": rej, "raw": raw_rows,
            "fix": None if fix is None else {"steps": fix["steps"], "level": fix["level"], "log": fix["log"]},
            "fix_error": fix_error, "after": after, "misses": misses, "introduced": introduced,
            "must_after": must_after, "aim_after": aim_after, "fixed": fixed, "near_after": near_after,
            "passes_after_fix": passes, "_audio": (x, fix["audio"] if fix else None)}


def rank_key(e: dict) -> list[int]:
    """The order: rejected last; then fewest must-misses after the fix, fewest aim-misses after it, fewest misses that
    needed a fix (a fixable miss counts less than an unfixable one, design section 6), fewest near readings, the take
    number. Every part is a count in the take's table, so a reader can recompute it."""
    return [int(bool(e["rejected"])), len(e["must_after"]), len(e["aim_after"]), len(e["fixed"]), len(e["near_after"]),
            e["n"]]


def order(entries: list[dict]) -> list[dict]:
    for e in entries:
        e["rank_key"] = rank_key(e)
    return sorted(entries, key=lambda e: e["rank_key"])


RANK_KEY = ["rejected (0/1)", "must misses after fix", "aim misses after fix", "misses that needed a fix",
            "near readings after fix", "take number"]


def prompt_misses(entries: list[dict]) -> list[dict]:
    """What a changed prompt must change: every target still missed after the fix, over the round's takes."""
    by: dict = {}
    usable = [e for e in entries if not e["rejected"]]
    for e in usable:
        for r in e["after"]:
            if r["result"] == "pass":
                continue
            d = by.setdefault(r["target"], {"target": r["target"], "measure": r["measure"], "must": r["must"],
                                            "min": r["min"], "max": r["max"], "takes_missing": 0, "of": len(usable),
                                            "closest": None})
            d["takes_missing"] += 1
            v = r["value"]
            if isinstance(v, (int, float)) and r["miss_by"] is not None:
                if d["closest"] is None or r["miss_by"] < d["closest"]["miss_by"]:
                    d["closest"] = {"take": e["take"], "value": v, "miss_by": r["miss_by"],
                                    "direction": "too low" if r["min"] is not None and v < r["min"] else "too high"}
    return sorted(by.values(), key=lambda d: (not d["must"], -d["takes_missing"], d["target"]))


def prove(card: dict, cue_dir: Path, top: dict) -> dict:
    """Render the top take's fix for real on a temp copy of the cue and compare every target row."""
    with tempfile.TemporaryDirectory(prefix="soundbench-rank-") as tmp:
        root = Path(tmp)
        cue = card["cue"]
        dst = root / cue
        (dst / "takes").mkdir(parents=True)
        shutil.copyfile(cue_dir / "card.json", dst / "card.json")
        take = cue_dir / "takes" / top["take"]
        for src in (take, take.with_suffix(".json"), take.with_name(take.stem + ".master.wav")):
            shutil.copyfile(src, dst / "takes" / src.name)
        for sib in card.get("family", {}).get("siblings", []):
            (root / sib).mkdir()
            shutil.copyfile(cue_dir.parent / sib / "card.json", root / sib / "card.json")
        recipe = {"cue": cue, "take": f"takes/{top['take']}", "design": [], "edit": top["fix"]["steps"]}
        (dst / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
        doc, code = render.render(dst)
    sim = {r["target"]: r for r in top["after"]}
    mismatches = []
    for r in doc["targets"]:
        s = sim.get(r["target"])
        if s is None or s["result"] != r["result"] or not _close(s["value"], r["value"]):
            mismatches.append({"target": r["target"], "render": [r["value"], r["result"]],
                               "rank": None if s is None else [s["value"], s["result"]]})
    if len(doc["targets"]) != len(sim):
        mismatches.append({"target": "row count", "render": len(doc["targets"]), "rank": len(sim)})
    if mismatches:
        raise SoundbenchError(f"rank: the proof render of {top['take']} disagrees with the simulation on {mismatches}: "
                              "a soundbench bug, refused")
    return {"take": top["take"], "recipe_edit": top["fix"]["steps"], "must_failed": doc["must_failed"],
            "rows_compared": len(doc["targets"]), "agrees": True,
            "audio_sha256_float32": doc["export"]["audio_sha256_float32"],
            "family": "not checked by the proof (a temp copy without the siblings' files): render checks D-03"}


def _close(a, b) -> bool:
    num = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)  # noqa: E731
    if num(a) and num(b):
        return abs(a - b) <= max(PROOF_ABS, PROOF_REL * abs(a))
    return a == b


def rank(cue_dir: Path, round_no: int | None = None, picture: bool = False) -> tuple[dict, int]:
    cue_dir = Path(cue_dir)
    card = cardmod.load_card(cue_dir / "card.json")
    if cue_dir.name != card["cue"]:
        raise SoundbenchError(f"cue ids differ: folder {cue_dir.name!r}, card {card['cue']!r}")
    fam = render.family_members(card, cue_dir)  # refuse an inconsistent family, exactly as render does
    k, takes = find_takes(cue_dir, card["cue"], round_no)
    warnings = []
    want = TAKES_PER_ROUND[card["tier"]]
    if len(takes) != want:
        warnings.append(f"round {k} has {len(takes)} takes; a {card['tier']} cue gets {want} per round (J020-D9)")
    entries = order([take_entry(card, cue_dir, n, rel) for n, rel in takes])
    top = entries[0]
    proof = prove(card, cue_dir, top) if not top["rejected"] and top["fix"] is not None else None
    cue = card["cue"]
    if top["passes_after_fix"]:
        code = 0
        verdict = {"action": "use", "take": top["take"], "recipe_edit": top["fix"]["steps"],
                   "say": f"{top['take']} passes every must-target after its fixable steps: start recipe.json from it"}
    else:
        code = 1
        last = k >= MAX_ROUNDS
        verdict = {"action": "owner" if last else "regenerate", "prompt_must_change": prompt_misses(entries),
                   "rejected": {e["take"]: e["rejected"] for e in entries if e["rejected"]},
                   "say": (f"round {k} of {MAX_ROUNDS}: no take passes after its fixable steps and no rounds are left: "
                           "the cue goes to the owner with this table (J020-D7)") if last else
                          (f"regenerate with a changed prompt (round {k + 1} of {MAX_ROUNDS}): no take passes after its "
                           "fixable steps; the prompt must change the misses listed")}
    rep_dir = cue_dir / "report"
    pics = []
    after_flag = any(r["score"] != "inside" for r in top["after"])
    for e in entries:
        if picture or (e is top and (after_flag or card["tier"] == "important")):
            from . import pictures

            rep_dir.mkdir(parents=True, exist_ok=True)
            stem = Path(e["take"]).name[: -len(".mp3")]
            x, rate = e["_audio"][0], e["rate"]
            pics.append(str(pictures.picture(x, rate, rep_dir / f"{stem}.rank-before.png", title=f"{stem} take")))
            if e["_audio"][1] is not None:
                pics.append(str(pictures.picture(e["_audio"][1], rate, rep_dir / f"{stem}.rank-after.png",
                                                 title=f"{stem} after its fixable steps")))
    for e in entries:
        del e["_audio"]
    doc = {"tool": "soundbench rank", "cue": cue, "kind": card["kind"], "category": card["category"],
           "tier": card["tier"], "round": k, "rounds_left": MAX_ROUNDS - k, "takes_expected": want,
           "takes_found": len(takes), "warnings": warnings, "rank_key": RANK_KEY,
           "order": [e["take"] for e in entries], "takes": entries, "top": top["take"], "proof": proof,
           "family": None if fam is None else {**fam, "note": "rank does not check D-03 and writes no family state; "
                                                               "render checks it on every member's delivered file"},
           "verdict": verdict, "exit_code": code, "pictures": pics, "tools": versions(),
           "screening": "numbers are a screening aid, never a taste verdict; the owner judges in play-tests (J020-D3)"}
    rep_dir.mkdir(parents=True, exist_ok=True)
    base = rep_dir / f"{cue}.r{k}.rank"
    Path(f"{base}.json").write_text(json.dumps(doc, indent=2, default=render._json_default) + "\n", encoding="utf-8")
    Path(f"{base}.md").write_text(markdown(doc), encoding="utf-8")
    return doc, code


def _fmt(v) -> str:
    if isinstance(v, float):
        return f"{v:g}" if math.isfinite(v) else str(v)
    return "-" if v is None else str(v)


def markdown(doc: dict) -> str:
    v = doc["verdict"]
    lines = [f"# {doc['cue']} round {doc['round']} rank", "",
             f"Exit code {doc['exit_code']}: {v['say']}  ", f"Kind {doc['kind']}, {doc['category']}, {doc['tier']}; "
             f"takes {doc['takes_found']} (expected {doc['takes_expected']}); rounds left {doc['rounds_left']}  ",
             f"Order key: {', '.join(doc['rank_key'])}  ", f"{doc['screening']}", ""]
    lines += [f"- warning: {w}" for w in doc["warnings"]]
    lines += ["| # | Take | Rejected | Must misses after fix | Aim misses after fix | Fixed | Near | Passes |",
              "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, e in enumerate(doc["takes"], 1):
        lines.append(f"| {i} | {e['take']} | {'; '.join(e['rejected']) or '-'} | {', '.join(e['must_after']) or '-'} | "
                     f"{', '.join(e['aim_after']) or '-'} | {', '.join(e['fixed']) or '-'} | "
                     f"{', '.join(e['near_after']) or '-'} | {'yes' if e['passes_after_fix'] else 'no'} |")
    for e in doc["takes"]:
        lines += ["", f"## {e['take']}", "", "| Target | Measure | Value | Min | Max | Must | Score | Fix | After |",
                  "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
        miss = {m_["target"]: m_ for m_ in e["misses"]}
        after = {r["target"]: r for r in e["after"]}
        for r in e["raw"]:
            m_ = miss.get(r["target"])
            fix = "-" if m_ is None else (f"fixed by {m_['by']}" if m_["fix"] == "fixed" else f"prompt: {m_['why']}")
            a = after[r["target"]]
            lines.append(f"| {r['target']} | {r['measure']} | {_fmt(r['value'])} | {_fmt(r['min'])} | {_fmt(r['max'])} | "
                         f"{'must' if r['must'] else 'aim'} | {r['score']} | {fix} | {_fmt(a['value'])} ({a['score']}) |")
        if e["fix"]:
            lines.append(f"\nFix steps: `{json.dumps(e['fix']['steps'])}`")
            if e["fix"]["level"]:
                lines.append(f"Level: `{json.dumps(e['fix']['level'])}`")
        if e["fix_error"]:
            lines.append(f"\nFix refused: {e['fix_error']}")
        for i_ in e["introduced"]:
            lines.append(f"\nCaused by the fix: {i_['target']} {i_['before']} -> {i_['after']}")
    if v["action"] != "use":
        lines += ["", "## What the prompt must change", "", "| Target | Must | Takes missing | Closest | Min | Max |",
                  "| --- | --- | --- | --- | --- | --- |"]
        for d in v["prompt_must_change"]:
            c = d["closest"]
            closest = "-" if c is None else f"{_fmt(c['value'])} ({c['direction']}, {c['take']})"
            lines.append(f"| {d['target']} | {'must' if d['must'] else 'aim'} | {d['takes_missing']} of {d['of']} | "
                         f"{closest} | {_fmt(d['min'])} | {_fmt(d['max'])} |")
    if doc["proof"]:
        p = doc["proof"]
        lines += ["", f"Proof: render of {p['take']} with `{json.dumps(p['recipe_edit'])}` agrees on "
                      f"{p['rows_compared']} rows; must failed {p['must_failed']}"]
    return "\n".join(lines) + "\n"
