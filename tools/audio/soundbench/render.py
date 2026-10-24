"""`render`: one cue folder's recipe applied to its take(s), re-measured against its card (editor-design.md sections
1, 4, 7; build step 3; layers, loops and variants: build step 6, `assemble.py`).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 steps 3 and 6)

Step 6 (layers, loops, variants): `plan_form` checks them before any audio; layers are mixed (`mix_layers`: each
take G-1 checked, resampled to the first layer's rate with a log line, its own design pass, placed to the sample;
shares and headroom measured, the mix put through export's own check), the recipe's design pass then runs on the
mix, then the loop, then each variant (varispeed, level offset on the loudness target), then the edit pass. Each
output is exported and judged: the card's rows go in `targets` (the rows rank simulates); layer targets, the loop's
wrap rows and the variant rows go in `form_checks`. A family member's delivered files are every variant file the card
asks for, so D-03 sees each variant.

Order of work, each step refusing instead of guessing:
  1. read card.json and recipe.json (every field checked); check every step's parameters and the design pass's
     SC-09 order before any audio is touched;
  2. check the take: the MP3's sha256 against its sidecar, the master WAV's float32 audio sha256 against the
     sidecar's intake record, the rate (G-1: originals never change);
  3. design pass in the recipe's order (SC-09 checked); edit pass in the fixed order trim, cut, fade, mono,
     loudness, peak, export, whatever order the recipe lists (the log says when it reordered);
  4. every step logged with its parameters, its own numbers and a before/after snapshot (G-2);
  5. export FLAC (G-8) at the take's rate; the delivered file is re-measured (F-03: measure the delivered format)
     and compared with the card's targets and level;
  6. family check for a paid-reveal family (D-03, R-31): every member's card must declare the same family (checked
     before rendering); F-13 b momentary maxima within 1 LU and F-03 sample peaks within 1 dB across every member's
     current delivered file; a member not rendered yet gives exit 3, never a pass;
  7. write out/<cue>.flac, out/<cue>.log.json, report/<cue>.render.json and .md; pictures (before and after) when a
     target misses, for important cues, or when asked (light-check rule).
Exit codes (command line): 0 every must-target and the family check passed; 1 a must-target, the level or the family
check failed (the file is still written, the report says why); 2 refused before or while rendering (an inconsistent
family declaration included); 3 a paid-reveal family is incomplete: re-render after the siblings (LD-a).

Usage:
  python -m tools.audio.soundbench render content/audio/<cue-id> [--picture] [--json]
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

from . import card as cardmod
from . import export as exportmod
from . import assemble, intake, measures, ops
from .core import SoundbenchError, audio_sha256, file_sha256, read_float32, versions

FAMILY_LU = 1.0  # R-31 / D-03: paid-reveal results' momentary maxima within 1 LU ...
FAMILY_PEAK_DB = 1.0  # ... and their sample peaks within 1 dB
LOOP_SEAM_MAX = 1.0  # PROPOSAL: a loop card without its own loop_seam target aims at F-08 <= 1.0
LOOP_F08_MUST_MAX = 2.0  # R-26: a loop's seam ratio (F-08) at most 2 (a perfect wrap is an ordinary step: P(step >
                         # 2 x p95) is about 1e-4 for Gaussian steps, so the must row does not fail good loops)
LOOP_WRAP_HF_DB = 3.0  # PROPOSAL: the wrap's 2 ms high-frequency energy at most 3 dB over the loop's own 99th
                       # percentile (good loops of 2-30 s read at most -1.2; natural positions over 3: 2 of 1,160)
LOOP_GAP_DB = 6.0  # PROPOSAL: the seam's quietest 50 ms at most 6 dB under the loop's own 5th percentile (fade gaps
                   # of 100 ms caught on 19 of 20 continuous beds; natural positions under -6: 23 of 1,160, all in
                   # beds with near-silent lulls, where a fade gap reads 0 and is not caught)
LOOP_CROSSFADE_DB = 2.0  # PROPOSAL: a loop's crossfade at most 2 dB outside the band of its own two parts' levels
                         # (29 good auto-curve loops read -1.67 to +0.63; wrong curves -1.7 to -3.1 and +2.6 to +3.0)
ALIGN_CORRECTIONS = 1  # align: after placing, the offset is corrected once by the layer read alone at its offset
VARIANT_SPREAD_DB = 1.0  # R-31: variants of one sound, F-09 within +-1 dB (of the set's mean)


def snapshot(x: np.ndarray, rate: int) -> dict:
    """The numbers logged before and after every step."""
    a = np.asarray(x, dtype=np.float64)
    a = a - a.mean(axis=0)
    mono = a.mean(axis=1)
    on = measures.onset_index(mono)
    end, _ = measures.sound_end(mono, rate)
    peak = float(np.max(np.abs(x)))
    tp = measures.true_peak_db(x)
    lv = measures.db(measures.f09_rms(mono[on:end], rate))
    r = lambda v, k=2: None if v is None else round(float(v), k)  # noqa: E731
    return {"samples": int(len(x)), "channels": int(a.shape[1]), "F-01_onset_ms": r(1000 * on / rate),
            "main_transient_ms": measures.main_transient_ms(a, rate), "attack_share_5ms": measures.attack_share(a, rate),
            "sample_peak_dbfs": r(measures.db(peak)), "true_peak_dbtp": r(tp), "F-09_dbfs": r(lv),
            "sound_ms": r(1000 * (end - on) / rate)}


def check_take(cue_dir: Path, recipe: dict) -> tuple[np.ndarray, int, dict]:
    take = cue_dir / recipe["take"]
    if not take.is_file():
        raise SoundbenchError(f"take not found: {take}")
    side = take.with_suffix(".json")
    if not side.is_file():
        raise SoundbenchError(f"take has no sidecar: {side}")
    doc = json.loads(side.read_text(encoding="utf-8"))
    rec = doc.get("intake")
    if not isinstance(rec, dict):
        raise SoundbenchError(f"{side.name}: no intake record (decode the take once with intake.decode_take)")
    sha = file_sha256(take)
    for field_name, want in (("sha256", doc.get("sha256")), ("intake.take_sha256", rec.get("take_sha256"))):
        if want is not None and want != sha:
            raise SoundbenchError(f"{take.name}: sha256 {sha[:12]}... differs from the sidecar's {field_name} "
                                  f"{str(want)[:12]}...: the original take changed (G-1), refused")
    if rec.get("take_sha256") is None:
        raise SoundbenchError(f"{side.name}: the intake record has no take_sha256")
    master = intake.master_path(take)
    x, rate = read_float32(master)
    if audio_sha256(x) != rec.get("master_audio_sha256"):
        raise SoundbenchError(f"{master.name}: its audio differs from the one decoded at intake (G-1), refused")
    if rate != rec.get("rate"):
        raise SoundbenchError(f"{master.name}: rate {rate} differs from the intake record's {rec.get('rate')}")
    return x.astype(np.float64), rate, {"take": take.name, "take_sha256": sha, "master": master.name,
                                         "master_audio_sha256": rec["master_audio_sha256"], "rate": rate,
                                         "decoder": rec.get("decoder"), "ffmpeg_version": rec.get("ffmpeg_version")}


def _flat(rec: dict, prefix: str = "") -> dict:
    out = {}
    for k, v in rec.items():
        if isinstance(v, dict):
            out.update(_flat(v, f"{prefix}{k}."))
        else:
            out[f"{prefix}{k}"] = v
    return out


def target_rows(card: dict, targets: dict, final: dict) -> list[dict]:
    """One row per target ({min, max, must}) on a measure record; the onset binds as the card says."""
    flat = _flat(final)
    rows = []
    for name, spec in targets.items():
        key = cardmod.target_key(card, name)
        v = flat.get(key)
        ok = v is not None and ("min" not in spec or v >= spec["min"]) and ("max" not in spec or v <= spec["max"])
        rows.append({"target": name, "measure": key, "value": v, "min": spec.get("min"), "max": spec.get("max"),
                     "must": spec["must"], "result": "pass" if ok else ("no value" if v is None else "miss")})
    return rows


def evaluate(card: dict, final: dict, out_audio: np.ndarray, rate: int) -> list[dict]:
    """Every target, the level, the key and the form, each passed or missed with its value."""
    rows = target_rows(card, card.get("targets", {}), final)
    lv = card["level"]
    try:
        v = round(measures.level_db(out_audio, rate, lv["measure"]), 3)
        ok = abs(v - lv["target"]) <= lv["tolerance"]
        res = "pass" if ok else "miss"
    except SoundbenchError as err:
        v, res = None, f"no value ({err})"
    rows.append({"target": "level", "measure": lv["measure"], "value": v, "min": lv["target"] - lv["tolerance"],
                 "max": lv["target"] + lv["tolerance"], "must": lv["must"], "result": res})
    if "key" in card:
        k = card["key"]
        f10 = final.get("F-10_pitch", {})
        if not f10.get("trusted"):
            res, v = "no value (F-10 untrusted)", f10.get("note")
        else:
            pc = cardmod.NOTE_NAMES.index(f10["note"].rstrip("-0123456789"))
            root = cardmod.NOTE_NAMES.index(k["root"])
            res, v = ("pass" if (pc - root) % 12 in cardmod.SCALES[k["scale"]] else "miss"), f10["note"]
        rows.append({"target": "key", "measure": "F-10_pitch.note", "value": v, "min": None, "max": None,
                     "must": k.get("must", False), "result": res, "key": f"{k['root']} {k['scale']}"})
    form = card.get("form", {})
    if form.get("mono"):
        rows.append({"target": "form.mono", "measure": "channels", "value": final["channels"], "min": 1, "max": 1,
                     "must": True, "result": "pass" if final["channels"] == 1 else "miss"})
    if form.get("loop") and "loop_seam" not in card.get("targets", {}):
        v = final.get("F-08_loop_seam")
        rows.append({"target": "form.loop", "measure": "F-08_loop_seam", "value": v, "min": None,
                     "max": LOOP_SEAM_MAX, "must": False,
                     "result": "pass" if v is not None and v <= LOOP_SEAM_MAX else "miss"})
    return rows


def family_members(card: dict, cue_dir: Path) -> dict | None:
    """Check the family is declared the same way by every member before anything renders (F2, repair round 2).

    Refused (exit 2) unless every sibling's card.json exists and declares the same family id, the same paid_reveal
    and the same member set, unless every card in the neighbouring cue folders that lists this cue as a family
    member is itself in that set, and unless every neighbouring card that declares the same family id is in that set
    (two pairs sharing one id would otherwise each pass on their own, R2-1). A cue whose own card declares no family is refused when another card lists it (a
    one-sided family could bypass D-03). None when the cue is in no family."""
    cue = card["cue"]
    fam = card.get("family")
    listing, same_id = {}, set()
    for other in sorted(cue_dir.parent.iterdir()):
        cpath = other / "card.json"
        if other.name == cue or not cpath.is_file():
            continue
        try:
            oc = cardmod.load_card(cpath)
        except SoundbenchError:
            continue  # an unreadable neighbour cannot list us; it fails on its own render
        of = oc.get("family")
        if of and cue in of["siblings"]:
            listing[other.name] = of["id"]
        if of and fam and of["id"] == fam["id"]:
            same_id.add(other.name)
    if fam is None:
        if listing:
            raise SoundbenchError(f"{sorted(listing)} list {cue} as a family member, but {cue}'s card declares no family: "
                                  "every member declares the family (D-03 cannot be checked one-sided), refused")
        return None
    members = {cue, *fam["siblings"]}
    for sib in fam["siblings"]:
        spath = cue_dir.parent / sib / "card.json"
        if not spath.is_file():
            raise SoundbenchError(f"family {fam['id']!r}: sibling {sib} has no card.json at {spath}, refused")
        sf_ = cardmod.load_card(spath).get("family")
        if not sf_:
            raise SoundbenchError(f"family {fam['id']!r}: sibling {sib} declares no family, refused")
        problems = []
        if sf_["id"] != fam["id"]:
            problems.append(f"id {sf_['id']!r}")
        if sf_["paid_reveal"] != fam["paid_reveal"]:
            problems.append(f"paid_reveal {sf_['paid_reveal']}")
        if {sib, *sf_["siblings"]} != members:
            problems.append(f"members {sorted({sib, *sf_['siblings']})}")
        if problems:
            raise SoundbenchError(f"family {fam['id']!r}: sibling {sib} declares {', '.join(problems)}; this card declares "
                                  f"id {fam['id']!r}, paid_reveal {fam['paid_reveal']}, members {sorted(members)}: refused")
    outside = sorted(same_id - members)
    if outside:
        raise SoundbenchError(f"{outside} declare the same family id {fam['id']!r} but are not in this card's member set "
                              f"{sorted(members)}: every card of one family declares one member set (D-03 must see "
                              "every member), refused")
    strangers = sorted(n for n in listing if n not in members)
    if strangers:
        raise SoundbenchError(f"{strangers} list {cue} in a family but are not members of {fam['id']!r}: refused")
    return {"id": fam["id"], "paid_reveal": fam["paid_reveal"], "members": sorted(members)}


def delivered_files(cue_dir: Path, card: dict) -> list[Path]:
    """The files a cue delivers, by its card: out/<cue>.flac, or out/<cue>-v1..vn.flac when the card asks n variants
    (a stale file of the other form is never read: the card says which files are current)."""
    n = card.get("form", {}).get("variants", 0)
    out = cue_dir / "out"
    return [out / f"{card['cue']}.flac"] if not n else [out / f"{card['cue']}-v{k}.flac" for k in range(1, n + 1)]


def family_check(card: dict, cue_dir: Path, out_files: list[Path]) -> dict | None:
    """D-03 on the members' current delivered files (whichever member renders re-checks the whole family). Every
    delivered file counts: a member with variants brings every variant file, so no variant may read louder (J020
    step 6). Results:
    pass, fail, incomplete (a member not rendered yet: exit 3, never a pass), or not run for a family that is not a
    paid reveal. The state is also written beside the cue folders as <family-id>.family.json, with every member's file
    sha256, so a report from an earlier render can be told stale."""
    fam = family_members(card, cue_dir)
    if fam is None:
        return None
    if not fam["paid_reveal"]:
        return {"id": fam["id"], "result": "not run (not a paid-reveal family)"}
    files, missing = [], []
    for name in fam["members"]:
        mine = name == card["cue"]
        for f in (out_files if mine else delivered_files(cue_dir.parent / name,
                                                          cardmod.load_card(cue_dir.parent / name / "card.json"))):
            (files if f.is_file() else missing).append(f if f.is_file() else f.stem)
    rec = {"id": fam["id"], "members": fam["members"], "files": [str(f) for f in files],
           "file_sha256": {f.stem: file_sha256(f) for f in files},
           "limits": {"momentary_lu": FAMILY_LU, "sample_peak_db": FAMILY_PEAK_DB}, "checked_by": card["cue"]}
    if missing:
        rec.update({"result": "incomplete", "reason": f"family incomplete: re-render after the siblings ({missing} not "
                                                      "rendered yet; D-03 cannot be checked)"})
    else:
        try:
            par = measures.parity(files, "momentary")
        except SoundbenchError as err:
            par = None
            rec.update({"result": "fail", "reason": str(err)})
        if par is not None:
            peaks = [measures.measure(f)["F-03_peaks"]["sample_peak_dbfs"] for f in files]
            peak_spread = round(max(peaks) - min(peaks), 2)
            rec.update({"momentary_lufs": par["lufs"], "spread_lu": par["spread_lu"], "sample_peaks_dbfs": peaks,
                        "peak_spread_db": peak_spread})
            ok = par["spread_lu"] is not None and par["spread_lu"] <= FAMILY_LU and peak_spread <= FAMILY_PEAK_DB
            rec["result"] = "pass" if ok else "fail"
            if not ok:
                rec["reason"] = (f"F-13 b spread {par['spread_lu']} LU (limit {FAMILY_LU}) and F-03 peak spread "
                                 f"{peak_spread} dB (limit {FAMILY_PEAK_DB}): D-03, a paid result may not read louder")
    (cue_dir.parent / f"{fam['id']}.family.json").write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return rec


def plan(card: dict, recipe: dict) -> tuple[list, list, bool]:
    """Check every step before any audio is touched: (design steps, edit steps in fixed order, reordered?)."""
    stages = ops.check_order(recipe["design"])
    design = []
    for step, stage in zip(recipe["design"], stages):
        design.append({"op": step["op"], "params": ops.check_params(step["op"], step), "why": step.get("why"),
                       "stage": stage})
    listed = [s["op"] for s in recipe["edit"]]
    by_name = {s["op"]: s for s in recipe["edit"]}
    edit = []
    for name in cardmod.EDIT_ORDER:
        if name == "export" or name in by_name:
            step = by_name.get(name, {"op": "export"})
            edit.append({"op": name, "params": ops.check_params(name, step), "why": step.get("why")})
    if any(s["op"] == "loudness" for s in edit) and "level" not in card:
        raise SoundbenchError("loudness: the card has no level")
    asked = [n for n in listed if n != "export"]
    reordered = asked != [n for n in cardmod.EDIT_ORDER if n in asked]
    return design, edit, reordered


def context(card: dict, edit: list) -> dict:
    """The card's context every operation reads (kind, category, onset binding, level, key, the edit pass's fade-out)."""
    fade = next((s for s in edit if s["op"] == "fade"), None)
    return {"kind": card["kind"], "category": card["category"], "binding": cardmod.onset_binding(card),
            "level": card["level"], "key": card.get("key"), "fade_out_ms": fade["params"]["out_ms"] if fade else 0.0}


def apply_steps(passes, card: dict, ctx: dict, x: np.ndarray, rate: int) -> tuple[np.ndarray, list]:
    """Run planned steps in order, each logged with its parameters, its numbers and a before/after snapshot (G-2).
    `passes`: (pass name, planned steps) pairs. `peak` takes the card's true-peak max as its ceiling when lower.
    `render` and `rank` both run their steps through this one loop."""
    steps = []
    y = x
    for passname, seq in passes:
        for st in seq:
            if st["op"] == "export":
                continue
            params = dict(st["params"])
            if st["op"] == "peak" and "true_peak_dbtp" in card.get("targets", {}):
                params["ceiling_dbtp"] = min(params["ceiling_dbtp"], card["targets"]["true_peak_dbtp"].get("max", 0.0))
            before = snapshot(y, rate)
            y, info = ops.run(st["op"], y, rate, params, {**ctx, "why": st["why"]})
            steps.append({"pass": passname, "op": st["op"], "stage": st.get("stage"), "params": params,
                          "why": st["why"], "info": info, "before": before, "after": snapshot(y, rate)})
    return y, steps


def plan_form(card: dict, recipe: dict, edit: list) -> dict:
    """Check layers, loop, variants and per-take variants before any audio is touched (J020 step 6). Returns
    {"layers": [planned layer] or None, "takes": [path] or None, "loop": (op, params) or None,
    "variants": params or None}."""
    kind = cardmod.KINDS[card["kind"]]
    form = card.get("form", {})
    asks = form.get("variants", 0)
    out: dict = {"layers": None, "takes": None, "loop": None, "variants": None}
    if ("variants" in recipe or "takes" in recipe) and kind["no_variants"]:
        raise SoundbenchError(f"variants: a {card['kind']} has no variants (SC-12: the same attack always has the same "
                              "tell), refused")
    if "layers" in recipe:
        if len(recipe["layers"]) > assemble.MAX_LAYERS:
            raise SoundbenchError(f"layers: {len(recipe['layers'])} layers, over {assemble.MAX_LAYERS}")
        layers, names = [], set()
        for i, lay in enumerate(recipe["layers"]):
            where = f"recipe.layers[{i}]"
            name = lay.get("name", f"L{i + 1}")
            if name in names:
                raise SoundbenchError(f"{where}.name: {name!r} is used twice")
            names.add(name)
            p = ops.check_params(where, {k: v for k, v in lay.items() if k in assemble.LAYER_SPEC},
                                 assemble.LAYER_SPEC)
            align = None
            if "align" in lay:
                if not isinstance(lay["align"], dict):
                    raise SoundbenchError(f"{where}.align: needs an object {{to_ms, on}}")
                align = ops.check_params(where + ".align", lay["align"], assemble.ALIGN_SPEC)
            if card["tier"] == "important" and not lay.get("targets"):
                raise SoundbenchError(f"{where}: an important cue's layer needs its own targets (craft-process "
                                      "section 6: per-layer targets for important sounds)")
            layers.append({"name": name, "take": lay["take"], "design": plan(card, {"design": lay["design"],
                                                                                     "edit": []})[0],
                           "align": align, "targets": lay.get("targets", {}), **p})
        out["layers"] = layers
    if "loop" in recipe:
        op = recipe["loop"]["op"]
        if not form.get("loop"):
            raise SoundbenchError(f"loop: {op} on a card whose form.loop is not true: set form.loop on the card")
        if "variants" in recipe or "takes" in recipe:
            raise SoundbenchError("loop: variants of a loop are not built (resampling would cross the seam)")
        breaking = [s["op"] for s in edit if s["op"] in ("trim", "cut", "fade")]
        if breaking:
            raise SoundbenchError(f"loop: {breaking} in the edit pass would cut or fade across the seam after the wrap: "
                                  "choose the loop's region with start_ms / end_ms instead")
        out["loop"] = (op, ops.check_params(op, recipe["loop"], assemble.LOOP_SPEC[op]))
    if "variants" in recipe:
        if "takes" in recipe:
            raise SoundbenchError("variants: one file per take (takes) or seeded from one sound (variants), not both")
        v = ops.check_params("variants", recipe["variants"], assemble.VARIANT_SPEC)
        if not asks:
            raise SoundbenchError("variants: card.form.variants is 0 or absent: the card says how many variants")
        v["count"] = asks if v["count"] is None else v["count"]
        if v["count"] != asks:
            raise SoundbenchError(f"variants: the recipe makes {v['count']} and card.form.variants asks {asks}: "
                                  "the card says how many")
        limit = min(kind["variant_max_cents"], assemble.VARIANT_KEYED_MAX_CENTS if "key" in card else math.inf)
        if v["max_cents"] > limit:
            raise SoundbenchError(f"variants.max_cents: {v['max_cents']} is over {limit:g} for a {card['kind']}"
                                  f"{' with a key' if 'key' in card else ''} (S-90/S-91)")
        out["variants"] = v
    if "takes" in recipe:
        if len(recipe["takes"]) != asks:
            raise SoundbenchError(f"takes: {len(recipe['takes'])} takes and card.form.variants asks {asks}: one variant "
                                  "file per take, the card says how many")
        out["takes"] = list(recipe["takes"])
    return out


def _step_log(passname: str, op: str, params: dict, info: dict, before: np.ndarray, after: np.ndarray, rate: int,
              **extra) -> dict:
    return {"pass": passname, "op": op, "stage": None, "params": params, "why": None, "info": info,
            "before": snapshot(before, rate), "after": snapshot(after, rate), **extra}


def mix_layers(cue_dir: Path, card: dict, layers: list, ctx: dict) -> tuple[np.ndarray, int, dict, list, dict]:
    """Every layer: its take checked (G-1), resampled to the mix rate when needed, its own design pass, gain and fades,
    then placed at its offset or on its marker; the mix's headroom checked with export's own check."""
    steps, parts, takes, info = [], [], [], {"layers": []}
    rate = None
    for lay in layers:
        x, r, take = check_take(cue_dir, {"take": lay["take"]})
        takes.append(take)
        rate = r if rate is None else rate
        if r != rate:
            y, rs = assemble.resample(x, r, rate)
            steps.append(_step_log("layers", "resample", {"to_rate": rate}, rs, x, y, rate, layer=lay["name"]))
            x = y
        x, st = apply_steps((("design", lay["design"]),), card, ctx, x, rate)
        steps += [{**s, "layer": lay["name"]} for s in st]
        y = assemble.shape_layer(x, rate, lay["gain_db"], lay["fade_in_ms"], lay["fade_out_ms"])
        if lay["align"] is not None:
            at = assemble.transient_index(y, rate, lay["align"]["on"])
            standalone = at
            off = assemble.samples(lay["align"]["to_ms"], rate) - at
            if off < 0:
                raise SoundbenchError(f"layers: {lay['name']}'s {lay['align']['on']} is at {1000 * at / rate:.2f} ms, "
                                      f"after the marker {lay['align']['to_ms']} ms: it would start before the file "
                                      "(move the marker later)")
        else:
            off, standalone = assemble.samples(lay["offset_ms"], rate), None
        parts.append((y, off))
        info["layers"].append({"name": lay["name"], "take": take["take"], "rate": take["rate"],
                               "offset_samples": off, "offset_ms": round(1000 * off / rate, 3),
                               "gain_db": lay["gain_db"], "fade_ms": [lay["fade_in_ms"], lay["fade_out_ms"]],
                               "align": lay["align"], "standalone_index": standalone,
                               "reading_dc": None if lay["align"] is None else
                               [round(float(v), 6) for v in y.mean(axis=0)]})
    mix, placed = assemble.place(parts)
    for entry in info["layers"]:
        entry["align_correction_samples"], entry["align_unstable"] = 0, False
    for _ in range(ALIGN_CORRECTIONS):  # read each aligned layer alone at its placed offset and correct once
        moved = False
        for k, (entry, p, lay) in enumerate(zip(info["layers"], placed, layers)):
            if lay["align"] is None:
                continue
            err = assemble.samples(lay["align"]["to_ms"], rate) - assemble.layer_index(
                parts[k][0], rate, lay["align"]["on"], entry["offset_samples"])
            if err and entry["offset_samples"] + err >= 0:
                entry["offset_samples"] += err
                entry["align_correction_samples"] += err
                parts[k] = (parts[k][0], entry["offset_samples"])
                moved = True
        if moved:
            mix, placed = assemble.place(parts)
    for (y, off), entry, p, lay in zip(parts, info["layers"], placed, layers):
        entry["offset_ms"] = round(1000 * off / rate, 3)
        ms = lambda on: None if not np.any(y) else round(1000 * assemble.layer_index(y, rate, on, off) / rate, 3)  # noqa: E731
        entry["measured"] = {"F-01_onset_ms": ms("F-01"), "main_transient_ms": ms("main_transient"),
                             "F-09_dbfs": round(measures.level_db(p, rate, "F-09"), 2) if np.any(p) else None}
        if lay["align"] is not None:  # the log is read the way align was: a disagreement is flagged, never hidden
            entry["placed_index"] = assemble.layer_index(y, rate, lay["align"]["on"], off)
            off_by = assemble.samples(lay["align"]["to_ms"], rate) - entry["placed_index"]
            entry["align_unstable"] = abs(off_by) > 1
            if entry["align_unstable"]:
                entry["align_note"] = (f"the placed layer still reads {off_by} samples from the marker after "
                                       f"{ALIGN_CORRECTIONS} correction: its {lay['align']['on']} reading depends on the "
                                       "position (a layer loud at its first sample, placed under 1 ms in)")
    sh = assemble.shares(placed, mix)
    for k, entry in enumerate(info["layers"]):
        entry["share_energy"], entry["share_of_mix"] = sh["energy"][k], sh["of_mix"][k]
    info["interference_db"] = sh["interference_db"]
    peaks = [float(np.max(np.abs(p))) for p in placed]
    tp = measures.true_peak_db(mix)
    head = {"sample_peak_dbfs": measures.db(float(np.max(np.abs(mix)))), "true_peak_dbtp": tp,
            "loudest_layer_peak_dbfs": measures.db(max(peaks))}
    head = {k: None if v is None else round(v, 2) for k, v in head.items()}
    try:
        exportmod.check_exportable(mix, rate, rate)  # export's own check, on the summed layers
        head["exportable"], head["reason"] = True, None
    except SoundbenchError as err:
        head["exportable"], head["reason"] = False, str(err)
    info["headroom"] = head
    info["placed"] = placed
    return mix, rate, {"layers": takes, "rate": rate}, steps, info


def layer_rows(card: dict, layers: list, placed: list, rate: int) -> list[dict]:
    """Each layer's own targets, measured on the layer as placed in the mix (alone, before the mix's design pass)."""
    rows = []
    for lay, p in zip(layers, placed):
        if not lay["targets"]:
            continue
        rec = measures.measure_audio(p, rate)
        for r in target_rows({"kind": card["kind"], "targets": lay["targets"]}, lay["targets"], rec):
            rows.append({**r, "target": f"layer[{lay['name']}].{r['target']}"})
    return rows


def _row(target: str, measure: str, value, lo, hi, none_reason: str = "no value") -> dict:
    ok = value is not None and (lo is None or value >= lo) and (hi is None or value <= hi)
    return {"target": target, "measure": measure, "value": value, "min": lo, "max": hi, "must": True,
            "result": "pass" if ok else (none_reason if value is None else "miss")}


def f08_limit(card: dict) -> tuple[float, str]:
    """The must F-08 limit of a loop card (review step 6 F1): R-26's 2, or the card's own loop_seam max when it is
    stricter. A card loosens it only with a must target that gives a `why` (the reason is logged with the row); an aim
    target, or a must without a `why`, never lifts a must guardrail."""
    seam = card.get("targets", {}).get("loop_seam", {})
    mx = seam.get("max")
    if mx is None:
        return LOOP_F08_MUST_MAX, "R-26"
    if mx <= LOOP_F08_MUST_MAX:
        return mx, "card (stricter than R-26)"
    if seam.get("must") and seam.get("why"):
        return mx, f"card, looser than R-26: {seam['why']}"
    return LOOP_F08_MUST_MAX, "R-26 (the card's looser limit needs must: true and a why)"


def loop_rows(card: dict, final: dict, delivered: np.ndarray, rate: int, loop: dict | None) -> tuple[list, dict]:
    """A loop card's wrap, read on the delivered file (`measures.loop_wrap`), every row must: F-08 at most R-26's 2
    (a card's loop_seam max only tightens it, or loosens it as a must with a `why`: `f08_limit`), no click at the wrap (the click count and the high-frequency reading) and no
    gap; when the recipe made the loop, its crossfade at most 2 dB outside its two parts' own levels, both ways
    (measured by the loop step), and a music loop exactly its bar length. F-08 alone passes a spike just before the
    end and a fade to silence at both ends."""
    seam_ms = None if loop is None else 1000 * loop["crossfade_samples"] / rate
    w = measures.loop_wrap(delivered, rate, seam_ms)
    f08_max, source = f08_limit(card)
    rows = [{**_row("form.loop_f08", "F-08_loop_seam", final.get("F-08_loop_seam"), None, f08_max),
             "limit_from": source},
            _row("form.loop_wrap_clicks", "loop_wrap.wrap_clicks", w["wrap_clicks"], None, 0),
            _row("form.loop_wrap_hf", "loop_wrap.wrap_hf_db", w["wrap_hf_db"], None, LOOP_WRAP_HF_DB,
                 "no value (loop too short)"),
            _row("form.loop_seam_gap", "loop_wrap.seam_gap_db", w["seam_gap_db"], -LOOP_GAP_DB, None,
                 "no value (loop too short for its seam)")]
    if loop is not None:
        cl = loop["crossfade_level_db"]
        worst = None if cl["min_db"] is None else (cl["min_db"] if -cl["min_db"] >= cl["max_db"] else cl["max_db"])
        rows.append(_row("form.loop_crossfade_level", "loop.crossfade_level_db (worst window)", worst,
                         -LOOP_CROSSFADE_DB, LOOP_CROSSFADE_DB))
        if "exact_samples" in loop:
            n = loop["loop_samples"]
            rows.append(_row("form.loop_length_samples", "samples", int(len(delivered)), n, n))
    return rows, w


def variant_rows(asks: int, levels: dict) -> list[dict]:
    """The card's variant count, and R-31 across the variant files: F-09 within +-1 dB of the set's mean."""
    rows = [{"target": "form.variants", "measure": "files", "value": len(levels), "min": asks, "max": asks,
             "must": True, "result": "pass" if len(levels) == asks else "miss"}]
    if len(levels) > 1:
        vals = [v for v in levels.values() if v is not None]
        dev = None if len(vals) != len(levels) else round(max(abs(v - sum(vals) / len(vals)) for v in vals), 3)
        rows.append({"target": "variants.level_spread", "measure": "F-09 re the set's mean (R-31)", "value": dev,
                     "min": None, "max": VARIANT_SPREAD_DB, "must": True,
                     "result": "no value" if dev is None else "pass" if dev <= VARIANT_SPREAD_DB else "miss"})
    return rows


def render(cue_dir: Path, picture: bool = False) -> tuple[dict, int]:
    cue_dir = Path(cue_dir)
    card = cardmod.load_card(cue_dir / "card.json")
    recipe = cardmod.load_recipe(cue_dir / "recipe.json")
    if recipe["cue"] != card["cue"] or cue_dir.name != card["cue"]:
        raise SoundbenchError(f"cue ids differ: folder {cue_dir.name!r}, card {card['cue']!r}, recipe {recipe['cue']!r}")
    design, edit, reordered = plan(card, recipe)
    form = plan_form(card, recipe, edit)
    family_members(card, cue_dir)  # refuse an inconsistent family before any audio is touched
    cue = card["cue"]
    ctx = context(card, edit)
    form_rows, extra = [], {}
    # sources -> (name, audio before the variant and edit steps, steps so far, variant draw or None)
    if form["layers"] is not None:
        x, rate, take, steps, mixinfo = mix_layers(cue_dir, card, form["layers"], ctx)
        placed = mixinfo.pop("placed")
        extra["layers"] = mixinfo
        if not mixinfo["headroom"]["exportable"] and not design and not any(
                s["op"] in ("loudness", "peak") for s in edit):
            raise SoundbenchError(f"layers: the summed mix is not exportable ({mixinfo['headroom']['reason']}) and no "
                                  "design step, loudness or peak follows to bring it down: refused before the edit pass")
        form_rows += layer_rows(card, form["layers"], placed, rate)
        starts = [(cue, x, take, steps)]
    elif form["takes"] is not None:
        starts = []
        for k, rel in enumerate(form["takes"], 1):
            xk, rate, tk = check_take(cue_dir, {"take": rel})
            starts.append((f"{cue}-v{k}", xk, tk, []))
        if len({s[2]["rate"] for s in starts}) > 1:
            raise SoundbenchError("takes: the takes have different sample rates; one variant set is one rate")
        take = {"takes": [s[2] for s in starts], "rate": rate}
    else:
        x, rate, take = check_take(cue_dir, recipe)
        starts = [(cue, x, take, [])]
    start = snapshot(starts[0][1], rate)
    built = []
    for name, x, tk, steps in starts:
        y, st = apply_steps((("design", design),), card, ctx, x, rate)
        steps = steps + st
        if form["loop"] is not None:
            op, lp = form["loop"]
            y2, info = assemble.LOOPS[op](y, rate, lp)
            steps.append(_step_log("loop", op, lp, info, y, y2, rate))
            y = y2
            extra["loop"] = info
        built.append((name, x, y, steps, None))
    if form["variants"] is not None:
        v = form["variants"]
        draws = assemble.variant_plan(v["count"], v["seed"], v["max_cents"], v["max_db"])
        extra["variants"] = {"params": v, "draws": draws, "note": "pitch is varied in the files: do not add runtime "
                                                                  "PlaybackSpeed jitter on top (S-92: one level only)"}
        _, x, y, steps, _ = built[0]
        built = []
        for d in draws:
            yk, info = ops.run("varispeed", y, rate, {"semitones": d["cents"] / 100}, ctx)
            built.append((f"{cue}-v{d['k']}", x, yk, steps + [_step_log("variants", "varispeed",
                                                                         {"semitones": d["cents"] / 100}, info, y, yk,
                                                                         rate, variant=d["k"])], d))
    outputs = []
    for name, x, y, steps, d in built:
        cctx = ctx
        if d is not None and d["gain_db"]:
            if any(s["op"] == "loudness" for s in edit):  # the level change rides on the loudness target
                cctx = {**ctx, "level": {**ctx["level"], "target": ctx["level"]["target"] + d["gain_db"]}}
            else:
                y0, y = y, y * 10 ** (d["gain_db"] / 20)
                steps = steps + [_step_log("variants", "gain", {"gain_db": d["gain_db"]}, {}, y0, y, rate,
                                           variant=d["k"])]
        y, st = apply_steps((("edit", edit),), card, cctx, y, rate)
        outputs.append({"name": name, "start": x, "audio": y, "steps": steps + st, "draw": d})
    out_dir, rep_dir = cue_dir / "out", cue_dir / "report"
    log_file = out_dir / f"{cue}.log.json"
    many = len(outputs) > 1 or outputs[0]["name"] != cue
    current = {o["name"] for o in outputs}
    stale = [out_dir / f"{cue}.flac"] if many else []
    stale += [f for f in sorted(out_dir.glob(f"{cue}-v*.flac")) + sorted(out_dir.glob(f"{cue}-v*.log.json"))
              if f.name.split(".")[0] not in current]
    for f in stale:
        if f.is_file():
            f.unlink()  # a file of an earlier render's form or count is never left to be read as current
    rows, levels = [], {}
    for o in outputs:
        f = out_dir / f"{o['name']}.flac"
        o["export"] = exportmod.export_flac(o["audio"], rate, f, source_rate=take["rate"],
                                            log=log_file if not many else out_dir / f"{o['name']}.log.json")
        delivered, drate = read_float32(f)
        o["file"], o["delivered"] = f, delivered.astype(np.float64)
        o["final"] = measures.measure(f)
        r = evaluate(card, o["final"], o["delivered"], drate)  # the card's rows: the ones rank simulates
        fr = []
        if card.get("form", {}).get("loop"):  # form checks, kept out of `targets` (rank's proof compares targets)
            fr, o["loop_wrap"] = loop_rows(card, o["final"], o["delivered"], drate, extra.get("loop"))
        o["rows"] = [{**x, "output": o["name"]} for x in r] if many else r
        fr = [{**x, "output": o["name"]} for x in fr] if many else fr
        rows += o["rows"]
        form_rows += fr
        o["rows"] = o["rows"] + fr
        levels[o["name"]] = o["final"]["F-09_loudness_rms_dbfs"]
    if card.get("form", {}).get("variants", 0) > 0:
        form_rows += variant_rows(card["form"]["variants"], levels)
    fam = family_check(card, cue_dir, [o["file"] for o in outputs])
    targets = rows
    must_fail = [(f"{r['output']}:" if "output" in r else "") + r["target"] for r in targets + form_rows
                 if r["must"] and r["result"] != "pass"]
    fam_fail = fam is not None and fam["result"] == "fail"
    fam_incomplete = fam is not None and fam["result"] == "incomplete"
    code = 1 if must_fail or fam_fail else (3 if fam_incomplete else 0)
    first = outputs[0]
    doc = {"tool": "soundbench render", "cue": cue, "card": card, "recipe": recipe, "take": take,
           "edit_order": [s["op"] for s in edit], "edit_reordered": reordered, "start": start, "steps": first["steps"],
           "export": first["export"], "final": first["final"], "targets": targets, "form_checks": form_rows,
           "family": fam, "must_failed": must_fail, "exit_code": code, "tools": versions(),
           "verdict": "measured (screening aid: numbers are never a taste verdict; the owner judges in play-tests)"}
    doc.update(extra)
    if many:
        doc["outputs"] = [{"name": o["name"], "file": str(o["file"]), "draw": o["draw"], "steps": o["steps"],
                           "export": o["export"], "final": o["final"]} for o in outputs]
    if form["loop"] is not None or card.get("form", {}).get("loop"):
        doc["loop_wrap"] = {o["name"]: o.get("loop_wrap") for o in outputs}
    if picture or must_fail or any(r["result"] != "pass" for r in targets + form_rows) or card["tier"] == "important":
        from . import pictures

        rep_dir.mkdir(parents=True, exist_ok=True)
        doc["pictures"] = [str(pictures.picture(first["start"], rate, rep_dir / f"{cue}.before.png", title=f"{cue} take"))]
        for o in outputs:
            if o is first or picture or card["tier"] == "important" or any(r["result"] != "pass" for r in o["rows"]):
                doc["pictures"].append(str(pictures.picture(o["delivered"], rate, rep_dir / f"{o['name']}.after.png",
                                                            title=f"{o['name']} rendered")))
    log_file.write_text(json.dumps(doc, indent=2, default=_json_default) + "\n", encoding="utf-8")
    rep_dir.mkdir(parents=True, exist_ok=True)
    report = {k: doc[k] for k in ("cue", "targets", "form_checks", "family", "must_failed", "exit_code", "verdict")}
    report["file"] = str(first["file"])
    report["files"] = [str(o["file"]) for o in outputs]
    report["audio_sha256_float32"] = first["export"]["audio_sha256_float32"]
    report["audio_sha256_float32_all"] = {o["name"]: o["export"]["audio_sha256_float32"] for o in outputs}
    (rep_dir / f"{cue}.render.json").write_text(json.dumps(report, indent=2, default=_json_default) + "\n",
                                                encoding="utf-8")
    (rep_dir / f"{cue}.render.md").write_text(_markdown(report), encoding="utf-8")
    return doc, code


def _json_default(v):
    if isinstance(v, (np.floating, np.integer)):
        return v.item()
    if isinstance(v, float) and not math.isfinite(v):
        return None
    raise TypeError(f"not JSON serialisable: {type(v).__name__}")


def _markdown(rep: dict) -> str:
    lines = [f"# {rep['cue']} render", "", f"File: `{rep['file']}`  ", f"Exit code: {rep['exit_code']}  ",
             f"Verdict: {rep['verdict']}", "", "| Target | Measure | Value | Min | Max | Must | Result |",
             "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in rep["targets"]:
        lines.append(f"| {r['output'] + ': ' if 'output' in r else ''}{r['target']} | {r['measure']} | {r['value']} | {r['min']} | {r['max']} | "
                     f"{'must' if r['must'] else 'aim'} | {r['result']} |")
    for r in rep.get("form_checks", []):
        lines.append(f"| {r['output'] + ': ' if 'output' in r else ''}{r['target']} | {r['measure']} | {r['value']} | {r['min']} | {r['max']} | "
                     f"{'must' if r['must'] else 'aim'} | {r['result']} |")
    if len(rep.get("files", [])) > 1:
        lines += ["", "Files: " + ", ".join(f"`{f}`" for f in rep["files"])]
    if rep["family"]:
        f = rep["family"]
        lines += ["", f"Family `{f['id']}`: {f['result']}" + (f" ({f['reason']})" if f.get("reason") else "")]
    return "\n".join(lines) + "\n"
