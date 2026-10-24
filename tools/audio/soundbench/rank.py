"""`rank`: score every take of one round against the cue's card and put them in order (editor-design.md section 6;
build step 5).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 5)

Order of work, each step refusing instead of guessing:
  1. read card.json (every field checked) and refuse an inconsistent family declaration, exactly as `render` does;
     find the round's takes `takes/<cue>.r<k>.t<n>.mp3` or `.wav` (as `generate` saves them; the highest round
     unless `--round`; round 4 or more is
     refused, J020-D7); check every take's sha256 and master against its sidecar (G-1, `render.check_take`);
  2. measure every master (`measures.measure_audio`) and score every target with `render.evaluate`, the function
     `render` uses on the delivered file: inside, near (inside but within the `near` margin of `tables.json`) or
     miss, with `miss_by` (how far outside) or `margin` (how far inside);
  3. reject outright (no fix is simulated): clipped at the source (10 ms or more at or above -1 dBFS: full scale, never
     the decoded take's own peak), near-silent, no sound in a band the card needs;
  4. fixability is computed, never guessed: the edit-pass steps for the take's misses (a late start: `trim`; too long:
     `cut` with a fade-out; an edge click: `trim` or `fade`; mono; the level: `loudness` then `peak`, its ceiling the
     lowest of -1.0, the card's true-peak max and its sample-peak max) are run on the master through the same step
     loop as `render` (`render.apply_steps`), the result is measured again and scored again. Three plans are scored:
     every miss, the must misses only, and no step; the one with the fewest must misses, then aim misses, wins (an aim
     fix plus the level reset can break a must the take passed untouched). A plan an operation refuses is recorded
     with its reason. A miss counts as fixed only when the kept plan's re-measured row passes. The level is also
     derived from the measures (below) and the two must agree within 0.1 dB, or rank refuses (a soundbench bug, never
     a silent wrong number);
  5. order: rejected last; then passing after the fix before not passing; then fewest must-misses after the fix,
     fewest aim-misses, fewest misses that needed a fix, fewest near readings, the take number (`rank_key`,
     recomputable from the table);
  6. proof: the top take's fix recipe is rendered for real (`render.render` on a temp copy of the cue: hash checks,
     parameter checks, the edit pass, FLAC export, the delivered file measured again) and every target row must
     match the simulation, or rank refuses. The temp copy is removed; rank never writes `out/` or family state;
  7. write report/<cue>.r<k>.rank.json and .md; pictures (light-check rule, owner J005-D8) of the top take before and
     after its fix when an after-fix row misses or reads near, or for an important cue; `--picture` draws every take.

The level (review-1 #9). `peak` sets the level by gain only, never a limiter, and sfx and ui do not limit transients,
so a too-quiet take is fixable only when the gain fits inside its true-peak headroom:
    gain_needed  = the gain `loudness` applied (the ratio of the peaks before and after it). For F-09 this equals
                   target - level in; for F-13a and LUFS-I on a quiet take it does not: the -70 LUFS absolute gate
                   moves blocks in or out as the gain changes (review-rank F2)
    peak_limit   = min(-1.0, true_peak_dbtp max, sample_peak_dbfs max) - 0.5  (ops.PEAK_CEILING_DBTP, PEAK_MARGIN_DB)
    headroom     = peak_limit - true peak in
    peak_cut     = max(0, true peak in + gain_needed - peak_limit)
    predicted    = level after loudness (the card's measure) - peak_cut;  fits when |predicted - target| <= tolerance
A take too loud always fits (gain down). For music, ambience and voice a `limit` design step could make room; rank does
not compute design steps, so it does not count that as a fix.

Paid-reveal families (D-03): rank refuses an inconsistent family declaration as `render` does, writes no family
state, and never checks parity: `render` runs D-03 across every member's delivered file, unchanged.

Layered rounds (important cues: `generate` writes each layer's takes as `takes/<cue>.<layer>.r<k>.t<n>`, all at the cue
round). Rounds are counted per cue: the round to rank is the highest of the plain takes and every layer's; a round
holding plain and layer takes is refused. The layer list, each layer's own targets and its placement come from
recipe.json's `layers` (where render reads them; the card has no layer list), through render's own checks (an
important cue's layer without targets is refused with render's message); every layer of the round must be named
there. A layer with no takes in round k is read from its latest round before (a round may regenerate only the layers
that had no passing take).
  1. each take is checked (G-1) and placed alone as recipe.json places its layer, through `render.mix_layers` (gain,
     fades, the layer edge fade, offset or align with its correction; no design pass, as rank judges every take);
     a take render cannot place is rejected with render's reason;
  2. its rows are `render.layer_rows` on the layer as placed in the mix it would make with the other layers' chosen
     takes (render reads a layer's rows at the mix's length, and the length moves them: a real hit's sound_ms 274.6
     -> 294.1 ms with 600 ms more); rejection as for a one-shot (clipped, near-silent, no sound in a band the layer
     must have); a layer has no edit pass of its own, so no fix plan: its rows after are its rows as placed. The
     takes are ordered by `rank_key`; the choice is read again until the tops stay the same (2 passes usually);
  3. when every layer has a passing take, their mix (`render.mix_layers`) is judged as a one-shot take is (`judge`:
     the card's whole-cue rows, the three plans, the peak ceiling, the level derivation); its layer rows must equal
     the ranked ones value for value, or rank refuses;
  4. verdict: `use` (every layer passes and the mix passes every must after its fixable steps: the chosen takes, the
     layers recipe, the mix's edit steps), proven by a real render of that layers recipe on a temp copy (every
     whole-cue row and every layer row compared); `mix_misses` (every layer passes alone, the mix misses a must
     after its fixable steps: said plainly, exit 1, as render exits on that recipe; runner-up passing takes listed;
     no other combination is tried); `regenerate` or `owner` (round 3): the layers without a passing take, each
     with the misses its prompt must change. Report: one section per layer, then the mix and its proof.

Exit codes (command line): 0 the top take passes every must-target after its fixable steps (layered: every layer and
the mix do); 1 no take does: regenerate with a changed prompt (the misses it must change are listed), or after round 3
the cue goes to the owner with its numbers (J020-D7), or the layers pass alone and their mix misses; 2 refused or bad
input (also a rank/render disagreement).

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
from . import export as exportmod
from . import measures, ops, render
from .core import SoundbenchError, versions

TAKES_PER_ROUND = {"minor": 3, "frequent": 4, "important": 6}  # J020-D9 (owner)
MAX_ROUNDS = 3  # J020-D7 (owner): at most 3 rounds, then the cue goes to the owner with its numbers
NEAR: dict = cardmod.TABLES["near"]

# PROPOSAL values (start points a check may change)
NEAR_SILENT_DBFS = -60.0  # a take peaking under -60 dBFS is near-silent (62 real takes: the quietest peaks -43.9)
# Clipped at the source (review-rank F1, R2-2): 10 ms or more at or above -1 dBFS (full scale) inside any 300 ms
# window of the decoded take. The window keeps the reading from growing with the take's length (R2-2: a total grew
# past the limit on clean 2 s takes); 300 ms holds a whole clipped swell, 500 ms let two clean peaks add up (11.5 ms).
# Calibrated on MP3-decoded copies (libmp3lame 128k and 192k). Clean: the 62 real takes as delivered read at most
# 7.23 ms (swish-2.t1); normalised to -0.1 dBFS at most 5.78 ms; 97 long fixtures built from them (each take x4,
# whooshes/swishes/notes slowed x4, beds of 10 crossfaded takes of one family, chord pads of 2 s and 5 s) at most
# 6.6 ms, except slowed full-scale rumble (86-99.97 % of the energy under 120 Hz: 2 of 97 at 128k, 3 at 192k, up to
# 20 ms; a steady tone at full scale spends 30 % of its time within 1 dB of its peak, which no amplitude reading
# tells from clipping). Margin: 2.8 ms over the delivered takes. Clipped (hard clip at full scale, then MP3), caught at
# 128k / 192k: short takes +12 dB 37 / 38 of 62, +6 dB 24 / 24, +3 dB 15 / 15; long takes +12 dB 24 / 25 of 26,
# +6 dB 21 / 22, +3 dB 14 / 16. Not caught: short cracks whose clipped tips last under a millisecond (the MP3 smears
# them). No real ElevenLabs take of 2 s or more was available: the long fixtures are built from 480-800 ms real takes.
CLIP_FULL_SCALE_DBFS = -1.0
CLIP_MS = 10.0
CLIP_WINDOW_MS = 300.0
NO_BAND_FRACTION = 0.1  # a must band holding under a tenth of the card's minimum share has no sound there
FIX_FADE_OUT_MS = 10.0  # the fade-out rank adds with a cut, and for a click at the end edge
CUT_INSIDE_MS = 1.0  # a cut for sound_ms ends 1 ms inside the card's maximum
LEVEL_AGREE_DB = 0.1  # the derived and the simulated level must agree within this
PROOF_ABS, PROOF_REL = 0.02, 0.002  # the proof render's values vs the simulation's: 0.02 or 0.2 %, whichever is larger

TAKE_RE = re.compile(r"^(?P<cue>.+)\.r(?P<round>\d+)\.t(?P<take>\d+)\.(?:mp3|wav)$", re.IGNORECASE)
STEP_FOR = {"onset_ms": "trim", "main_transient_ms": "trim", "sound_ms": "cut", "file_ms": "cut",
            "level": "loudness and peak", "true_peak_dbtp": "loudness and peak", "sample_peak_dbfs": "loudness and peak",
            "form.mono": "mono", "edge_clicks": "trim or fade"}
BANDS = ("below_120", "band_120_500", "band_500_5k", "above_5k")


def _audio_files(cue_dir: Path) -> list[Path]:
    return sorted(q for q in (cue_dir / "takes").glob("*") if q.suffix.lower() in (".mp3", ".wav"))


def plain_rounds(cue_dir: Path, cue: str) -> dict[int, list[tuple[int, str]]]:
    """{round: [(take number, path relative to the cue folder)]} of the cue's one-shot takes `<cue>.r<k>.t<n>`."""
    found: dict[int, list[tuple[int, str]]] = {}
    for p in _audio_files(cue_dir):
        m = TAKE_RE.match(p.name)
        if m and m["cue"] == cue:
            found.setdefault(int(m["round"]), []).append((int(m["take"]), f"takes/{p.name}"))
    return found


def find_takes(cue_dir: Path, cue: str, round_no: int | None) -> tuple[int, list[tuple[int, str]]]:
    """(round, [(take number, path relative to the cue folder)]) for the asked round, or the highest one present."""
    found = plain_rounds(cue_dir, cue)
    if not found:
        raise SoundbenchError(f"no takes named takes/{cue}.r<k>.t<n>.mp3 or .wav in {cue_dir}")
    k = max(found) if round_no is None else round_no
    if k < 1 or k > MAX_ROUNDS:
        raise SoundbenchError(f"round {k}: a cue has at most {MAX_ROUNDS} rounds (J020-D7); after round {MAX_ROUNDS} it "
                              "goes to the owner with its numbers, refused")
    if k not in found:
        raise SoundbenchError(f"round {k} has no takes (rounds present: {sorted(found)})")
    return k, sorted(found[k])


def clip_reading(x: np.ndarray, rate: int) -> dict:
    """Clipped at the source: 10 ms or more at or above -1 dBFS inside some 300 ms window of the decoded take. Full
    scale, never the take's own peak (the MP3 decoder overshoots above a clipped plateau, review-rank F1); inside a
    window, never in total (a total grows with the take's length, R2-2).

    Known false readings: a steady tone or a slow low rumble normalised to full scale sits near full scale for long
    and reads clipped; clipping scaled down after it happened is not seen; short clipped cracks (the clipped tips
    under a millisecond each) are not seen after MP3 (a short crack clipped by 6 dB reads about 2 ms)."""
    a = np.abs(np.asarray(x, dtype=np.float64))
    peak = float(a.max())
    pk_db = measures.db(peak)
    hot = np.any(a >= 10 ** (CLIP_FULL_SCALE_DBFS / 20), axis=1).astype(np.float64)
    c = np.concatenate([[0.0], np.cumsum(hot)])
    w = int(round(CLIP_WINDOW_MS * rate / 1000))
    most = float((c[w:] - c[:-w]).max()) if len(hot) > w else float(c[-1])
    ms = 1000 * most / rate
    return {"sample_peak_dbfs": None if pk_db is None else round(pk_db, 2),
            "ms_at_or_above_-1dbfs_in_window": round(ms, 3), "clipped": ms >= CLIP_MS}


def rejections(card: dict, flat: dict, clip: dict) -> list[str]:
    out = []
    if clip["clipped"]:
        out.append(f"clipped at the source: {clip['ms_at_or_above_-1dbfs_in_window']} ms at or above "
                   f"{CLIP_FULL_SCALE_DBFS} dBFS inside {CLIP_WINDOW_MS:g} ms (>= {CLIP_MS} ms; sample peak "
                   f"{clip['sample_peak_dbfs']} dBFS)")
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
                if r["target"].startswith("layer[") and "]." in r["target"]:  # a layer's row: the target's own margin
                    near = NEAR.get(r["target"].split("].", 1)[1], 0)
                else:
                    near = NEAR.get(r["target"], 0)
                if r["margin"] < near:
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
        steps += [{"op": "loudness"}, {"op": "peak", "ceiling_dbtp": peak_ceiling(card)}]
    return steps


def peak_ceiling(card: dict) -> float:
    """`peak`'s ceiling: the lowest of -1.0 dBTP, the card's true-peak max and its sample-peak max (review-rank F4). A
    sample peak is never above its true peak, so a true-peak ceiling at the sample max keeps both."""
    tg = card.get("targets", {})
    return min([ops.PEAK_CEILING_DBTP] + [tg[k]["max"] for k in ("true_peak_dbtp", "sample_peak_dbfs")
                                          if k in tg and "max" in tg[k]])


def _only_must(rows: list[dict]) -> list[dict]:
    return [r if r["must"] else {**r, "result": "pass"} for r in rows]


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


PLAN_MODES = ("all", "must", "none")  # review-rank F3: every miss; the must misses only; no step at all


def plan_for(card: dict, x: np.ndarray, rate: int, raw_rows: list[dict], flat: dict, mode: str) -> list[dict]:
    """The fix steps for one plan mode. `all`: every miss. `must`: the must misses only (an aim fix plus the level reset
    can break a must the take passed untouched). `none`: no step."""
    if mode == "none":
        return []
    rows = raw_rows if mode == "all" else _only_must(raw_rows)
    head = [s for s in fix_plan(card, rows, flat, None) if s["op"] == "trim"]
    _, planned_head, _ = render.plan(card, {"design": [], "edit": head})
    y_trim, _ = render.apply_steps((("edit", planned_head),), card, render.context(card, planned_head), x, rate)
    rec_t = measures.measure_audio(y_trim, rate)
    rows_t = score(render.evaluate(card, rec_t, y_trim, rate))
    steps = fix_plan(card, rows, flat, (rows_t if mode == "all" else _only_must(rows_t), render._flat(rec_t), y_trim,
                                        rate))
    if not any(s["op"] == "peak" for s in steps) and not _exportable(x, rate):
        # export would refuse the master as it is (a decode over full scale): the edit pass must set the level (R2-1)
        steps += [{"op": "loudness"}, {"op": "peak", "ceiling_dbtp": peak_ceiling(card)}]
    return steps


def _exportable(x: np.ndarray, rate: int) -> bool:
    try:
        exportmod.check_exportable(x, rate, rate)
        return True
    except SoundbenchError:
        return False


def applied_gain_db(before: np.ndarray, after: np.ndarray) -> float:
    """The gain `loudness` applied (it only scales): the ratio of the peaks. For F-13a and LUFS-I on a quiet take this
    is not target - level_in: the -70 LUFS absolute gate moves blocks in or out as the gain changes (review-rank F2)."""
    return 20 * math.log10(float(np.max(np.abs(after))) / float(np.max(np.abs(before))))


def simulate(card: dict, x: np.ndarray, rate: int, steps: list[dict], raw_rows: list[dict]) -> dict:
    """Run a plan through `render`'s own step loop, measure and score again, and derive the level independently:
    predicted = the level after `loudness` (its measure, on the audio it made) - the peak cut, where the peak cut is
    max(0, true peak in + the gain loudness applied - peak limit)."""
    if not steps:
        return {"steps": [], "rows": raw_rows, "level": None, "log": [], "audio": x}
    _, edit, _ = render.plan(card, {"design": [], "edit": steps})
    ctx = render.context(card, edit)
    pre = [s for s in edit if s["op"] in ("trim", "cut", "fade", "mono")]
    loud = [s for s in edit if s["op"] == "loudness"]
    peak = [s for s in edit if s["op"] == "peak"]
    y_pre, log_pre = render.apply_steps((("edit", pre),), card, ctx, x, rate)
    y_loud, log_loud = render.apply_steps((("edit", loud),), card, ctx, y_pre, rate)
    lv = card["level"]
    derived = None
    if loud or peak:
        level_in = measures.level_db(y_pre, rate, lv["measure"])
        tp_in = measures.true_peak_db(y_pre)
        gain = applied_gain_db(y_pre, y_loud) if loud else 0.0
        level_loud = measures.level_db(y_loud, rate, lv["measure"]) if loud else level_in
        limit = (min(peak[0]["params"]["ceiling_dbtp"], peak_ceiling(card)) if peak else math.inf) - ops.PEAK_MARGIN_DB
        cut_db = max(0.0, tp_in + gain - limit) if peak else 0.0
        predicted = level_loud - cut_db
        derived = {"measure": lv["measure"], "level_in": round(level_in, 3), "target": lv["target"],
                   "tolerance": lv["tolerance"], "gain_needed_db": round(gain, 3),
                   "level_after_loudness": round(level_loud, 3), "true_peak_in_dbtp": round(tp_in, 3),
                   "peak_limit_dbtp": limit, "headroom_db": round(limit - tp_in, 3), "peak_cut_db": round(cut_db, 3),
                   "shortfall_db": round(max(0.0, cut_db - lv["tolerance"]), 3) if gain > 0 else 0.0,
                   "predicted_level": round(predicted, 3),
                   "fits": abs(predicted - lv["target"]) <= lv["tolerance"]}
    y, log_post = render.apply_steps((("edit", peak),), card, ctx, y_loud, rate)
    final = measures.measure_audio(y, rate)
    rows = score(render.evaluate(card, final, y, rate))
    if derived is not None:
        sim = next(r for r in rows if r["target"] == "level")["value"]
        derived["simulated_level"] = sim
        if sim is None or abs(sim - derived["predicted_level"]) > LEVEL_AGREE_DB:
            raise SoundbenchError(f"rank: the derived level {derived['predicted_level']} and the simulated level {sim} "
                                  f"disagree by more than {LEVEL_AGREE_DB} dB: a soundbench bug, refused")
    return {"steps": steps, "rows": rows, "level": derived, "log": log_pre + log_loud + log_post, "audio": y}


def best_fix(card: dict, x: np.ndarray, rate: int, raw_rows: list[dict], flat: dict) -> dict:
    """Score every plan mode and keep the one with the fewest must misses after it, then the fewest aim misses, then
    the first in PLAN_MODES (the all-steps plan carries the fullest reasons on a tie) (review-rank F3). A plan the operations refuse (for example a cut that leaves LUFS-I under 0.4 s)
    is recorded with its reason; the empty plan is never refused."""
    tried, refused, seen = [], [], []
    for mode in PLAN_MODES:
        try:
            steps = plan_for(card, x, rate, raw_rows, flat, mode)
            if steps in seen:
                continue
            seen.append(steps)
            fix = simulate(card, x, rate, steps, raw_rows)
            exportmod.check_exportable(fix["audio"], rate, rate)  # render must be able to deliver it (review-rank R2-1)
            tried.append((mode, fix))
        except SoundbenchError as err:
            if "soundbench bug" in str(err):
                raise
            refused.append({"plan": mode, "error": str(err)})
    if not tried:  # every plan refused (a take render cannot export whatever the steps): the raw rows, not passing
        return {"steps": [], "rows": raw_rows, "level": None, "log": [], "audio": None, "plan": None,
                "dropped_aim_fixes": [], "refused_plans": refused}
    count = lambda f, must: sum(r["must"] == must and r["result"] != "pass" for r in f["rows"])  # noqa: E731
    mode, fix = min(tried, key=lambda t: (count(t[1], True), count(t[1], False), PLAN_MODES.index(t[0])))
    first = tried[0][1] if tried[0][0] == "all" else None
    dropped = [] if first is None or first is fix else [
        r["target"] for r, c in zip(first["rows"], fix["rows"])
        if not r["must"] and r["result"] == "pass" and c["result"] != "pass"]
    return {**fix, "plan": mode, "dropped_aim_fixes": dropped, "refused_plans": refused}


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
        return "not simulated (the take is rejected)"
    if r["target"].startswith("layer["):
        return (f"a layer has no edit pass of its own (render runs trim, cut, fade, loudness and peak on the mix): as "
                f"recipe.json places it (offset or align, gain_db, fades) it reads {r['value']}; change the prompt, or "
                "the layer's placement or design in recipe.json (render measures that)")
    refused ="".join(f"the {p['plan']} fix was refused ({p['error']}); " for p in fix.get("refused_plans", []))
    return refused + _why_kept(card, r, fix, a)


def _why_kept(card: dict, r: dict, fix: dict, a: dict | None) -> str:
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
    return {"take": take["take"], "n": n, "rate": rate, "channels": int(x.shape[1]),
            "take_sha256": take["take_sha256"], **judge(card, x, rate)}


def judge(card: dict, x: np.ndarray, rate: int, reject: bool = True) -> dict:
    """One sound against the card's whole-cue rows: rejection (a take only: `reject`), the three plans, the order
    counts. A take (`take_entry`) and a layered round's mix (`rank_layers`) both go through here."""
    rec = measures.measure_audio(x, rate)
    flat = render._flat(rec)
    clip = clip_reading(x, rate) if reject else None
    raw_rows = score(render.evaluate(card, rec, x, rate))
    rej = rejections(card, flat, clip) if reject else []
    fix = None if rej else best_fix(card, x, rate, raw_rows, flat)
    fix_error = "; ".join(f"{p['plan']}: {p['error']}" for p in fix["refused_plans"]) if fix else None
    misses, introduced = classify(card, raw_rows, fix)
    after = fix["rows"] if fix else raw_rows
    must_after = [r["target"] for r in after if r["must"] and r["result"] != "pass"]
    aim_after = [r["target"] for r in after if not r["must"] and r["result"] != "pass"]
    fixed = [m_["target"] for m_ in misses if m_["fix"] == "fixed"]
    near_after = [r["target"] for r in after if r["score"] == "near"]
    passes = not rej and fix["plan"] is not None and not must_after
    return {"clip": clip, "rejected": rej, "raw": raw_rows,
            "fix": None if fix is None else {"steps": fix["steps"], "plan": fix["plan"], "level": fix["level"],
                                             "dropped_aim_fixes": fix["dropped_aim_fixes"],
                                             "refused_plans": fix["refused_plans"], "log": fix["log"]},
            "fix_error": fix_error, "after": after, "misses": misses, "introduced": introduced,
            "must_after": must_after, "aim_after": aim_after, "fixed": fixed, "near_after": near_after,
            "passes_after_fix": passes, "_audio": (x, fix["audio"] if fix else None)}


def rank_key(e: dict) -> list[int]:
    """The order: rejected last; then a take that passes after its fix before one that does not (review-rank F5: a take
    whose fix was refused is judged on the plan it kept); then fewest must-misses after the fix, fewest aim-misses after it, fewest misses that
    needed a fix (a fixable miss counts less than an unfixable one, design section 6), fewest near readings, the take
    number. Every part is a count in the take's table, so a reader can recompute it."""
    return [int(bool(e["rejected"])), int(not e["passes_after_fix"]), len(e["must_after"]), len(e["aim_after"]),
            len(e["fixed"]), len(e["near_after"]), e["n"]]


def order(entries: list[dict]) -> list[dict]:
    for e in entries:
        e["rank_key"] = rank_key(e)
    return sorted(entries, key=lambda e: e["rank_key"])


RANK_KEY = ["rejected (0/1)", "does not pass after fix (0/1)", "must misses after fix", "aim misses after fix", "misses that needed a fix",
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


def form_note(proof: dict | None) -> str:
    """Review step 6 R2: the proof recipe has no loop or variants step, so a loop or variant card's proof can fail form
    rows that only render judges. The "use" text says so; the verdict and exit code do not change."""
    rows = [r for r in (proof or {}).get("must_failed", []) if r.split(":")[-1].startswith(("form.", "variants."))]
    return f"; form rows (loop, variants) are judged at render: {', '.join(rows)}" if rows else ""


def needs_proof(top: dict) -> bool:
    """Only a take rank says to use is proven by a real render (review-rank R2-1: a failing top take may be one render
    cannot export; that round is regenerate, exit 1, never a refusal)."""
    return top["passes_after_fix"]


def render_copy(card: dict, cue_dir: Path, takes: list[str], recipe: dict) -> dict:
    """`render.render` on a temp copy of the cue: its card, the named takes (each with its sidecar and master) and the
    family siblings' cards. The copy is removed; nothing is written in the cue folder."""
    with tempfile.TemporaryDirectory(prefix="soundbench-rank-") as tmp:
        root = Path(tmp)
        dst = root / card["cue"]
        (dst / "takes").mkdir(parents=True)
        shutil.copyfile(cue_dir / "card.json", dst / "card.json")
        for name in takes:
            take = cue_dir / "takes" / name
            for src in (take, take.with_suffix(".json"), take.with_name(take.stem + ".master.wav")):
                shutil.copyfile(src, dst / "takes" / src.name)
        for sib in card.get("family", {}).get("siblings", []):
            (root / sib).mkdir()
            shutil.copyfile(cue_dir.parent / sib / "card.json", root / sib / "card.json")
        (dst / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
        doc, _ = render.render(dst)
    return doc


def row_mismatches(rendered: list[dict], simulated: list[dict]) -> list[dict]:
    """Every row whose result differs, or whose value differs by more than 0.02 or 0.2 %, and a row count that does."""
    sim = {r["target"]: r for r in simulated}
    mismatches = []
    for r in rendered:
        s = sim.get(r["target"])
        if s is None or s["result"] != r["result"] or not _close(s["value"], r["value"]):
            mismatches.append({"target": r["target"], "render": [r["value"], r["result"]],
                               "rank": None if s is None else [s["value"], s["result"]]})
    if len(rendered) != len(sim):
        mismatches.append({"target": "row count", "render": len(rendered), "rank": len(sim)})
    return mismatches


def prove(card: dict, cue_dir: Path, top: dict) -> dict:
    """Render the top take's fix for real on a temp copy of the cue and compare every target row."""
    recipe = {"cue": card["cue"], "take": f"takes/{top['take']}", "design": [], "edit": top["fix"]["steps"]}
    doc = render_copy(card, cue_dir, [top["take"]], recipe)
    mismatches = row_mismatches(doc["targets"], top["after"])
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
    layered = layer_rounds(cue_dir, card["cue"])
    if layered:  # a cue with layer takes: the round is the cue round, over the plain takes and every layer's
        k = cue_round(cue_dir, card["cue"], layered, round_no)
        if any(k in rounds for rounds in layered.values()):
            return rank_layers(cue_dir, card, fam, k, layered, picture)
        round_no = k
    k, takes = find_takes(cue_dir, card["cue"], round_no)
    warnings = []
    want = TAKES_PER_ROUND[card["tier"]]
    if len(takes) != want:
        warnings.append(f"round {k} has {len(takes)} takes; a {card['tier']} cue gets {want} per round (J020-D9)")
    entries = order([take_entry(card, cue_dir, n, rel) for n, rel in takes])
    top = entries[0]
    proof = prove(card, cue_dir, top) if needs_proof(top) else None
    cue = card["cue"]
    if top["passes_after_fix"]:
        code = 0
        verdict = {"action": "use", "take": top["take"], "recipe_edit": top["fix"]["steps"],
                   "say": f"{top['take']} passes every must-target after its fixable steps: start recipe.json from it"
                          + form_note(proof)}
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
            stem = Path(e["take"]).stem
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
    lines += _summary_table(doc["takes"])
    for e in doc["takes"]:
        lines += _take_section(e, f"## {e['take']}")
    if v["action"] != "use":
        lines += _prompt_table(v["prompt_must_change"], "## What the prompt must change")
    if doc["proof"]:
        p = doc["proof"]
        lines += ["", f"Proof: render of {p['take']} with `{json.dumps(p['recipe_edit'])}` agrees on "
                      f"{p['rows_compared']} rows; must failed {p['must_failed']}"]
    return "\n".join(lines) + "\n"


def _summary_table(takes: list[dict]) -> list[str]:
    lines = ["| # | Take | Rejected | Must misses after fix | Aim misses after fix | Fixed | Near | Passes |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for i, e in enumerate(takes, 1):
        lines.append(f"| {i} | {e['take']} | {'; '.join(e['rejected']) or '-'} | {', '.join(e['must_after']) or '-'} | "
                     f"{', '.join(e['aim_after']) or '-'} | {', '.join(e['fixed']) or '-'} | "
                     f"{', '.join(e['near_after']) or '-'} | {'yes' if e['passes_after_fix'] else 'no'} |")
    return lines


def _take_section(e: dict, heading: str) -> list[str]:
    """One take's (or the mix's) rows: value, score, fix or prompt reason, after; then its fix steps."""
    lines = ["", heading, "", "| Target | Measure | Value | Min | Max | Must | Score | Fix | After |",
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
        plan = f"{e['fix']['plan']} plan" if e["fix"]["plan"] else "every plan refused"
        lines.append(f"\nFix steps ({plan}): `{json.dumps(e['fix']['steps'])}`")
        if e["fix"]["dropped_aim_fixes"]:
            lines.append(f"Aim fixes left out (they broke a must-target): {e['fix']['dropped_aim_fixes']}")
        if e["fix"]["level"]:
            lines.append(f"Level: `{json.dumps(e['fix']['level'])}`")
    if e["fix_error"]:
        lines.append(f"\nFix refused: {e['fix_error']}")
    for i_ in e["introduced"]:
        lines.append(f"\nCaused by the fix: {i_['target']} {i_['before']} -> {i_['after']}")
    return lines


def _prompt_table(rows: list[dict], heading: str) -> list[str]:
    lines = ["", heading, "", "| Target | Must | Takes missing | Closest | Min | Max |",
             "| --- | --- | --- | --- | --- | --- |"]
    for d in rows:
        c = d["closest"]
        closest = "-" if c is None else f"{_fmt(c['value'])} ({c['direction']}, {c['take']})"
        lines.append(f"| {d['target']} | {'must' if d['must'] else 'aim'} | {d['takes_missing']} of {d['of']} | "
                     f"{closest} | {_fmt(d['min'])} | {_fmt(d['max'])} |")
    return lines


# ------------------------------------------------------------------------------------------------- layered rounds
# An important cue's layers are generated separately as takes/<cue>.<layer>.r<k>.t<n> (generate, J020-D9), all at
# the cue round. Each layer's takes are judged against that layer's own targets on the layer as recipe.json places it
# (render's own mix_layers and layer_rows: rows layer[<name>].<target>); each layer's best take goes into one mix,
# which gets the three plans and the peak ceiling (`judge`, the one-shot path) against the card's whole-cue rows; a
# `use` is proven by a real render of that layers recipe.

LAYER_FRAME_PASSES = 4  # PROPOSAL: passes to settle the choice (layer rows are read at the mix length); 2 is usual


def layer_rounds(cue_dir: Path, cue: str) -> dict[str, dict[int, list[tuple[int, str]]]]:
    """{layer: {round: [(take number, path relative to the cue folder)]}} of `<cue>.<layer>.r<k>.t<n>.mp3|wav`."""
    from .generate import LAYER_RE  # one source for layer names (imported here: generate imports rank)

    pat = re.compile("^" + re.escape(cue) + r"\.(?P<layer>" + LAYER_RE.pattern.strip("^$") +
                     r")\.r(?P<round>\d+)\.t(?P<take>\d+)\.(?i:mp3|wav)$")
    found: dict[str, dict[int, list[tuple[int, str]]]] = {}
    for p in _audio_files(cue_dir):
        m = pat.match(p.name)
        if m:
            found.setdefault(m["layer"], {}).setdefault(int(m["round"]), []).append((int(m["take"]),
                                                                                     f"takes/{p.name}"))
    return found


def cue_round(cue_dir: Path, cue: str, layered: dict, round_no: int | None) -> int:
    """The round to rank: the asked one, or the highest round of the cue over its plain takes and every layer's
    (rounds are counted per cue, never per layer: lead decision on J020-D7). A round that holds both plain and layer
    takes is refused: a round is one sound or its layers."""
    plain = plain_rounds(cue_dir, cue)
    present = set(plain) | {r for rounds in layered.values() for r in rounds}
    k = max(present) if round_no is None else round_no
    if k < 1 or k > MAX_ROUNDS:
        raise SoundbenchError(f"round {k}: a cue has at most {MAX_ROUNDS} rounds (J020-D7); after round {MAX_ROUNDS} it "
                              "goes to the owner with its numbers, refused")
    if k not in present:
        raise SoundbenchError(f"round {k} has no takes (rounds present: {sorted(present)})")
    in_k = sorted(name for name, rounds in layered.items() if k in rounds)
    if k in plain and in_k:
        raise SoundbenchError(f"round {k} holds one-shot takes ({[rel for _, rel in sorted(plain[k])]}) and takes of the "
                              f"layers {in_k}: a round is one sound or its layers, never both (generate writes one or "
                              "the other from prompts.json); move the stray takes out of takes/, refused")
    return k


def layer_plan(cue_dir: Path, card: dict) -> tuple[list[dict], list[dict], list[str]]:
    """recipe.json's layers, through render's own checks (render.plan, render.plan_form: an important cue's layer
    needs its own targets, ...): (planned layers, the recipe's layer objects, warnings). Per-layer targets and
    placement live in recipe.json, not the card (cue-card.md: layer targets)."""
    path = cue_dir / "recipe.json"
    if not path.is_file():
        raise SoundbenchError(f"{card['cue']}: the round has layer takes; each layer is ranked against its own targets "
                              "and placement, which live in recipe.json's layers (name, take, design, offset_ms or "
                              "align, gain_db, fades, targets), and there is no recipe.json: write its layers first, "
                              "refused")
    recipe = cardmod.load_recipe(path)
    if recipe["cue"] != card["cue"]:
        raise SoundbenchError(f"cue ids differ: card {card['cue']!r}, recipe {recipe['cue']!r}")
    if "layers" not in recipe:
        raise SoundbenchError(f"{card['cue']}: the round has layer takes but recipe.json gives no layers (it gives "
                              f"{'one take' if 'take' in recipe else 'one take per variant'}): write each layer with "
                              "its targets and placement in recipe.json's layers, refused")
    _, edit, _ = render.plan(card, recipe)
    form = render.plan_form(card, recipe, edit)
    warnings = []
    designed = [lay["name"] for lay in form["layers"] if lay["design"]]
    if designed or recipe["design"]:
        warnings.append(f"recipe.json's design steps (layers {designed}, mix {[s['op'] for s in recipe['design']]}) "
                        "are not run: rank judges the takes with their placement only (offset or align, gain, "
                        "fades), as it judges one-shot takes without a design pass; render measures the design")
    return form["layers"], recipe["layers"], warnings


def place_candidate(cue_dir: Path, card: dict, lay: dict, n: int, rel: str, rnd: int) -> dict:
    """One layer take checked (G-1: a changed take refuses the round, as for one-shots) and placed alone as recipe.json
    places the layer, through render's own `mix_layers` (gain, fades, the layer edge fade, offset or align with its
    correction). A take render cannot place (its transient after the marker, a silent take) gets `_err`."""
    x, rate, take = render.check_take(cue_dir, {"take": rel})
    c = {"take": take["take"], "n": n, "round": rnd, "rate": rate, "channels": int(x.shape[1]),
         "take_sha256": take["take_sha256"], "clip": clip_reading(x, rate), "placement": None,
         "_x": x, "_p": None, "_info": None, "_err": None}
    try:
        _, _, _, _, info = render.mix_layers(cue_dir, card, [{**lay, "take": rel, "design": []}],
                                             render.context(card, []))
    except SoundbenchError as err:
        c["_err"] = str(err)
        return c
    c["_p"], c["_info"] = info["placed"][0], info["layers"][0]
    c["placement"] = {k: c["_info"][k] for k in ("offset_samples", "offset_ms", "length_samples",
                                                 "align_correction_samples", "align_unstable")}
    return c


def frame_of(cands: list[dict]) -> tuple[int, int] | None:
    """(samples, channels) of the mix these placed takes make: the latest layer end, the most channels (`place`)."""
    placed = [c["_p"] for c in cands if c["_p"] is not None]
    return None if not placed else (max(len(p) for p in placed), max(p.shape[1] for p in placed))


def in_frame(p: np.ndarray, frame: tuple[int, int]) -> np.ndarray:
    """A layer placed alone, as `assemble.place` lays it in a mix of `frame`: a mono layer on every channel, silence
    after its end. Render measures a layer's rows on it at the mix's length, and the length moves them (a real hit's
    sound_ms 274.6 -> 294.1 ms, tail_snr_db 38.6 -> 46.0 with 600 ms more: the mean removed before reading)."""
    length, channels = frame
    if p.shape[1] != channels:
        if p.shape[1] != 1:
            raise SoundbenchError(f"layers: a {p.shape[1]}-channel layer cannot go into a {channels}-channel mix")
        p = np.repeat(p, channels, axis=1)
    out = np.zeros((length, channels))
    out[:len(p)] = p
    return out


def layer_entry(card: dict, lay: dict, c: dict, frame: tuple[int, int] | None) -> dict:
    """One layer take judged against its layer's own targets, read on the layer as placed in a mix of `frame`
    (`render.layer_rows`, the rows render writes into form_checks). Rejection as for one-shot takes (clipped at the
    source, near-silent, no sound in a band the layer must have), plus a take render cannot place. A layer has no
    edit pass of its own, so there is no fix plan: its rows after are its rows as placed."""
    rows, flat = [], {}
    if c["_p"] is not None:
        p = in_frame(c["_p"], frame)
        rows = score(render.layer_rows(card, [lay], [p], c["rate"], [c["_info"]]))
        if any(spec["must"] and spec.get("min", 0) > 0 for b, spec in lay["targets"].items() if b in BANDS):
            flat = render._flat(measures.measure_audio(p, c["rate"]))
    rej = rejections({"targets": lay["targets"]}, flat, c["clip"])
    if c["_err"] is not None:
        rej.append(f"cannot be placed as recipe.json places layer {lay['name']}: {c['_err']}")
    misses, introduced = classify(card, rows, None if rej else {"steps": [], "rows": rows})
    must_after = [r["target"] for r in rows if r["must"] and r["result"] != "pass"]
    return {"take": c["take"], "n": c["n"], "round": c["round"], "rate": c["rate"], "channels": c["channels"],
            "take_sha256": c["take_sha256"], "clip": c["clip"], "rejected": rej, "raw": rows, "fix": None,
            "fix_error": None, "after": rows, "misses": misses, "introduced": introduced, "must_after": must_after,
            "aim_after": [r["target"] for r in rows if not r["must"] and r["result"] != "pass"], "fixed": [],
            "near_after": [r["target"] for r in rows if r["score"] == "near"],
            "passes_after_fix": not rej and not must_after, "placement": c["placement"], "_audio": (c["_x"], None)}


def rank_layer_takes(card: dict, plan_layers: list[dict], cands: dict) -> tuple[dict, tuple | None, int]:
    """Order each layer's takes, each read in the frame of the mix it would make with the other layers' current
    choices (render reads a layer's rows at the mix's length, and the length moves them). Pass 1 reads every take at
    its own length; each later pass reads them with the other layers' tops of the pass before, until the tops stay the
    same: then every top was read in exactly the mix the tops make. Returns (entries, that mix's frame, passes)."""
    by_n = {name: {c["n"]: c for c in cs} for name, cs in cands.items()}
    tops: dict | None = None
    for passes in range(1, LAYER_FRAME_PASSES + 1):
        entries = {}
        for lay in plan_layers:
            others = frame_of([tops[n] for n in tops if n != lay["name"]]) if tops else None
            entries[lay["name"]] = order([layer_entry(card, lay, c, _with(others, c)) for c in cands[lay["name"]]])
        new = {name: by_n[name][es[0]["n"]] for name, es in entries.items()}
        if tops is not None and all(new[n] is tops[n] for n in new):
            return entries, frame_of(list(new.values())), passes
        tops = new
    raise SoundbenchError(f"rank: the layer rows depend on the mix's length and the chosen takes did not settle in "
                          f"{LAYER_FRAME_PASSES} passes: choose from the layer tables by hand and let render judge, "
                          "refused")


def _with(others: tuple[int, int] | None, c: dict) -> tuple[int, int] | None:
    """The frame of the mix take `c` makes with the others (None: `c` alone, or `c` not placed)."""
    own = frame_of([c])
    if own is None or others is None:
        return own
    return max(own[0], others[0]), max(own[1], others[1])


def mix_entry(cue_dir: Path, card: dict, plan_layers: list[dict], tops: dict) -> dict:
    """The mix of each layer's chosen take, made by render's own `mix_layers` (no design pass, as rank judges every
    take), judged as a one-shot take is (`judge`: the card's whole-cue rows, the three plans, the peak ceiling; no
    rejection: a mix is not a take). Its layer rows must equal the ranked ones value for value (one function, one
    audio), or rank refuses."""
    chosen = [{**lay, "take": f"takes/{tops[lay['name']]['take']}", "design": []} for lay in plan_layers]
    mix, rate, _, _, info = render.mix_layers(cue_dir, card, chosen, render.context(card, []))
    placed = info.pop("placed")
    rows = score(render.layer_rows(card, chosen, placed, rate, info["layers"]))
    ranked = [r for lay in plan_layers for r in tops[lay["name"]]["after"]]
    if [(r["target"], r["value"], r["result"]) for r in rows] != [(r["target"], r["value"], r["result"]) for r in ranked]:
        raise SoundbenchError(f"rank: the chosen layer takes read differently in their mix than ranked ({rows} vs "
                              f"{ranked}): a soundbench bug, refused")
    return {"takes": {lay["name"]: tops[lay["name"]]["take"] for lay in plan_layers}, "rate": rate,
            "channels": int(mix.shape[1]), "length_samples": int(len(mix)), "placement": info["layers"],
            "interference_db": info["interference_db"], "headroom": info["headroom"], "layer_rows": rows,
            **judge(card, mix, rate, reject=False)}


def prove_layers(card: dict, cue_dir: Path, raw_layers: list[dict], mix: dict) -> dict:
    """Render the layers recipe of the chosen takes (recipe.json's placement, no design pass) with the mix's fix steps
    for real on a temp copy, and compare every whole-cue row and every layer row."""
    layers = [{**raw, "take": f"takes/{mix['takes'][raw['name']]}", "design": []} for raw in raw_layers]
    recipe = {"cue": card["cue"], "layers": layers, "design": [], "edit": mix["fix"]["steps"]}
    doc = render_copy(card, cue_dir, list(mix["takes"].values()), recipe)
    rendered_layers = [r for r in doc["form_checks"] if r["target"].startswith("layer[")]
    mismatches = row_mismatches(doc["targets"], mix["after"]) + row_mismatches(rendered_layers, mix["layer_rows"])
    if mismatches:
        raise SoundbenchError(f"rank: the proof render of the layers {mix['takes']} disagrees with the simulation on "
                              f"{mismatches}: a soundbench bug, refused")
    return {"takes": mix["takes"], "recipe_layers": layers, "recipe_edit": mix["fix"]["steps"],
            "must_failed": doc["must_failed"], "rows_compared": len(doc["targets"]),
            "layer_rows_compared": len(rendered_layers), "agrees": True,
            "audio_sha256_float32": doc["export"]["audio_sha256_float32"],
            "family": "not checked by the proof (a temp copy without the siblings' files): render checks D-03"}


def _row_text(r: dict) -> str:
    return f"{r['target']} {_fmt(r['value'])} (min {_fmt(r['min'])}, max {_fmt(r['max'])})"


def layer_verdict(k: int, names: list[str], entries: dict, mix: dict | None, proof: dict | None) -> tuple[dict, int]:
    tops = {n: entries[n][0] for n in names}
    chosen = ", ".join(f"{n}: {tops[n]['take']}" for n in names)
    failing = [n for n in names if not tops[n]["passes_after_fix"]]
    if failing:
        last = k >= MAX_ROUNDS
        keep = {n: tops[n]["take"] for n in names if n not in failing}
        say = (f"round {k} of {MAX_ROUNDS}: the layers {failing} have no passing take and no rounds are left: the cue "
               "goes to the owner with this table (J020-D7)") if last else (
            f"regenerate the layers {failing} with changed prompts (round {k + 1} of {MAX_ROUNDS}): no take of theirs "
            "passes as placed; each prompt must change the misses listed for its layer. "
            + (f"The other layers have a passing take ({keep}): a round may generate only the failing layers "
               "(prompts.json layers), and rank reads every other layer's takes from its latest round" if keep else
               "No layer has a passing take"))
        return {"action": "owner" if last else "regenerate", "layers_without_a_passing_take": failing,
                "prompt_must_change": {n: prompt_misses(entries[n]) for n in failing}, "passing_layers": keep,
                "rejected": {n: {e["take"]: e["rejected"] for e in entries[n] if e["rejected"]} for n in names
                             if any(e["rejected"] for e in entries[n])}, "say": say}, 1
    if mix["passes_after_fix"]:
        return {"action": "use", "takes": mix["takes"], "recipe_layers": proof["recipe_layers"],
                "recipe_edit": mix["fix"]["steps"],
                "say": f"every layer has a passing take ({chosen}) and their mix passes every must-target after its "
                       f"fixable steps: start recipe.json's layers from these takes (their placement as written; a "
                       f"layer has no edit pass of its own) and its edit pass from {json.dumps(mix['fix']['steps'])}"
                       + form_note(proof)}, 0
    missed = [r for r in mix["after"] if r["must"] and r["result"] != "pass"]
    runners = {n: [e["take"] for e in entries[n][1:] if e["passes_after_fix"]] for n in names}
    return {"action": "mix_misses", "takes": mix["takes"], "mix_must_misses": [r["target"] for r in missed],
            "runner_up_passing_takes": runners,
            "say": f"do not use: the layers pass alone ({chosen}); the mix misses {', '.join(map(_row_text, missed))} "
                   "after its fixable steps. Change the layers' placement or gains in recipe.json (or add a design "
                   "step: render measures it), or try a runner-up passing take; rank judged one mix, each layer's "
                   "best take, and tried no other combination"}, 1


def rank_layers(cue_dir: Path, card: dict, fam: dict | None, k: int, layered: dict, picture: bool) -> tuple[dict, int]:
    cue = card["cue"]
    plan_layers, raw_layers, warnings = layer_plan(cue_dir, card)
    names = [lay["name"] for lay in plan_layers]
    stray = sorted(n for n, rounds in layered.items() if k in rounds and n not in names)
    if stray:
        raise SoundbenchError(f"round {k} has takes of the layers {stray}, which recipe.json's layers do not name "
                              f"({names}): name each with its targets and placement, refused")
    want = TAKES_PER_ROUND[card["tier"]]
    sources = {}
    for name in names:
        rounds = [r for r in layered.get(name, {}) if r <= k]
        if not rounds:
            raise SoundbenchError(f"recipe.json's layer {name!r} has no takes named takes/{cue}.{name}.r<k>.t<n> in round "
                                  f"{k} or before, refused")
        r = max(rounds)
        sources[name] = (r, sorted(layered[name][r]))
        if r != k:
            warnings.append(f"layer {name}: no takes in round {k}; its takes of round {r} are ranked (a round may "
                            "generate only the layers that had no passing take)")
        if len(sources[name][1]) != want:
            warnings.append(f"layer {name} round {r} has {len(sources[name][1])} takes; a {card['tier']} cue gets "
                            f"{want} per round (J020-D9)")
    cands = {lay["name"]: [place_candidate(cue_dir, card, lay, n, rel, sources[lay["name"]][0])
                           for n, rel in sources[lay["name"]][1]] for lay in plan_layers}
    rates = sorted({c["rate"] for cs in cands.values() for c in cs})
    if len(rates) > 1:
        raise SoundbenchError(f"the layer takes are at the rates {rates}: render resamples every layer to the first "
                              "layer's rate, which rank cannot know before that layer's take is chosen, refused")
    entries, frame, passes = rank_layer_takes(card, plan_layers, cands)
    tops = {n: entries[n][0] for n in names}
    mix = proof = None
    if all(t["passes_after_fix"] for t in tops.values()):
        mix = mix_entry(cue_dir, card, plan_layers, tops)
        proof = prove_layers(card, cue_dir, raw_layers, mix) if needs_proof(mix) else None
    verdict, code = layer_verdict(k, names, entries, mix, proof)
    rep_dir = cue_dir / "report"
    pics = []
    for n in names:
        top = tops[n]
        flag = card["tier"] == "important" or any(r["score"] != "inside" for r in top["after"])
        for e in entries[n]:
            if picture or (e is top and flag):
                from . import pictures

                rep_dir.mkdir(parents=True, exist_ok=True)
                stem = Path(e["take"]).stem
                pics.append(str(pictures.picture(e["_audio"][0], e["rate"], rep_dir / f"{stem}.rank-before.png",
                                                 title=f"{stem} take")))
    if mix is not None:
        if picture or card["tier"] == "important" or any(r["score"] != "inside" for r in mix["after"]):
            from . import pictures

            rep_dir.mkdir(parents=True, exist_ok=True)
            pics.append(str(pictures.picture(mix["_audio"][0], mix["rate"], rep_dir / f"{cue}.r{k}.mix.rank-before.png",
                                             title=f"{cue} round {k}: the chosen layers mixed")))
            if mix["_audio"][1] is not None:
                pics.append(str(pictures.picture(mix["_audio"][1], mix["rate"],
                                                 rep_dir / f"{cue}.r{k}.mix.rank-after.png",
                                                 title=f"{cue} round {k}: the mix after its fixable steps")))
        del mix["_audio"]
    for es in entries.values():
        for e in es:
            del e["_audio"]
    raw_by = {raw["name"]: raw for raw in raw_layers}
    doc = {"tool": "soundbench rank", "cue": cue, "kind": card["kind"], "category": card["category"],
           "tier": card["tier"], "round": k, "rounds_left": MAX_ROUNDS - k, "form": "layers", "takes_expected": want,
           "warnings": warnings, "rank_key": RANK_KEY,
           "layers": [{"name": n, "round": sources[n][0], "takes_found": len(sources[n][1]),
                       "targets": raw_by[n].get("targets", {}),
                       "placement": {f: raw_by[n][f] for f in ("offset_ms", "align", "gain_db", "fade_in_ms",
                                                               "fade_out_ms") if f in raw_by[n]},
                       "order": [e["take"] for e in entries[n]], "takes": entries[n], "top": tops[n]["take"],
                       "has_passing_take": tops[n]["passes_after_fix"]} for n in names],
           "frame": None if frame is None else {"length_samples": frame[0], "channels": frame[1], "passes": passes,
                                                "note": "every layer row is read on the layer as placed in a mix of "
                                                        "this length, the one the chosen takes make (render reads them "
                                                        "there)"},
           "mix": mix, "proof": proof,
           "family": None if fam is None else {**fam, "note": "rank does not check D-03 and writes no family state; "
                                                               "render checks it on every member's delivered file"},
           "verdict": verdict, "exit_code": code, "pictures": pics, "tools": versions(),
           "screening": "numbers are a screening aid, never a taste verdict; the owner judges in play-tests (J020-D3)"}
    rep_dir.mkdir(parents=True, exist_ok=True)
    base = rep_dir / f"{cue}.r{k}.rank"
    Path(f"{base}.json").write_text(json.dumps(doc, indent=2, default=render._json_default) + "\n", encoding="utf-8")
    Path(f"{base}.md").write_text(markdown_layers(doc), encoding="utf-8")
    return doc, code


def markdown_layers(doc: dict) -> str:
    v = doc["verdict"]
    lines = [f"# {doc['cue']} round {doc['round']} rank (layers)", "",
             f"Exit code {doc['exit_code']}: {v['say']}  ",
             f"Kind {doc['kind']}, {doc['category']}, {doc['tier']}; layers {[l_['name'] for l_ in doc['layers']]}; "
             f"takes expected per layer {doc['takes_expected']}; rounds left {doc['rounds_left']}  ",
             f"Order key: {', '.join(doc['rank_key'])} (a layer has no edit pass of its own: its rows after are its "
             "rows as placed)  ", f"{doc['screening']}", ""]
    if doc["frame"]:
        f = doc["frame"]
        lines.append(f"Layer rows read in a mix of {f['length_samples']} samples, {f['channels']} channel(s) "
                     f"({f['passes']} pass(es)): {f['note']}  ")
    lines += [f"- warning: {w}" for w in doc["warnings"]]
    for lay in doc["layers"]:
        lines += ["", f"## Layer {lay['name']} (round {lay['round']}, {lay['takes_found']} takes; top {lay['top']}; "
                      f"{'has a passing take' if lay['has_passing_take'] else 'no passing take'})", "",
                  f"Targets: `{json.dumps(lay['targets'])}`  ", f"Placement: `{json.dumps(lay['placement'])}`", ""]
        lines += _summary_table(lay["takes"])
        for e in lay["takes"]:
            lines += _take_section(e, f"### {e['take']}")
        if v["action"] in ("regenerate", "owner") and lay["name"] in v["prompt_must_change"]:
            lines += _prompt_table(v["prompt_must_change"][lay["name"]],
                                   f"### What layer {lay['name']}'s prompt must change")
    mix = doc["mix"]
    if mix is None:
        lines += ["", "## Mix", "", "Not built: a layer has no passing take."]
    else:
        lines += ["", "## Mix of the chosen takes", "", f"Takes: `{json.dumps(mix['takes'])}`; interference "
                  f"{_fmt(mix['interference_db'])} dB; headroom `{json.dumps(mix['headroom'])}`", "",
                  "| Layer | Take | Offset ms | Gain dB | Share of mix | Share of energy | Align correction (samples) |",
                  "| --- | --- | --- | --- | --- | --- | --- |"]
        for p in mix["placement"]:
            lines.append(f"| {p['name']} | {p['take']} | {_fmt(p['offset_ms'])} | {_fmt(p['gain_db'])} | "
                         f"{_fmt(p['share_of_mix'])} | {_fmt(p['share_energy'])} | {p['align_correction_samples']} |")
        lines += _take_section({**mix, "take": "the mix"}, "### Whole-cue rows of the mix")
    if doc["proof"]:
        p = doc["proof"]
        lines += ["", f"Proof: render of the layers {json.dumps(p['takes'])} with `{json.dumps(p['recipe_edit'])}` "
                      f"agrees on {p['rows_compared']} whole-cue rows and {p['layer_rows_compared']} layer rows; must "
                      f"failed {p['must_failed']}"]
    return "\n".join(lines) + "\n"
