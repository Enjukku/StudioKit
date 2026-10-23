"""`render`: one cue folder's recipe applied to its take, re-measured against its card (editor-design.md sections
1, 4, 7; build step 3, single take).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 3)

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
from . import intake, measures, ops
from .core import SoundbenchError, audio_sha256, file_sha256, read_float32, versions

FAMILY_LU = 1.0  # R-31 / D-03: paid-reveal results' momentary maxima within 1 LU ...
FAMILY_PEAK_DB = 1.0  # ... and their sample peaks within 1 dB
LOOP_SEAM_MAX = 1.0  # PROPOSAL: a loop card without its own loop_seam target aims at F-08 <= 1.0


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


def evaluate(card: dict, final: dict, out_audio: np.ndarray, rate: int) -> list[dict]:
    """Every target, the level, the key and the form, each passed or missed with its value."""
    flat = _flat(final)
    rows = []
    for name, spec in card.get("targets", {}).items():
        key = cardmod.target_key(card, name)
        v = flat.get(key)
        ok = v is not None and ("min" not in spec or v >= spec["min"]) and ("max" not in spec or v <= spec["max"])
        rows.append({"target": name, "measure": key, "value": v, "min": spec.get("min"), "max": spec.get("max"),
                     "must": spec["must"], "result": "pass" if ok else ("no value" if v is None else "miss")})
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


def family_check(card: dict, cue_dir: Path, out_file: Path) -> dict | None:
    """D-03 on the members' current delivered files (whichever member renders re-checks the whole family). Results:
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
        f = out_file if name == card["cue"] else cue_dir.parent / name / "out" / f"{name}.flac"
        (files if f.is_file() else missing).append(f if f.is_file() else name)
    rec = {"id": fam["id"], "members": fam["members"], "files": [str(f) for f in files],
           "file_sha256": {f.parent.parent.name: file_sha256(f) for f in files},
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


def render(cue_dir: Path, picture: bool = False) -> tuple[dict, int]:
    cue_dir = Path(cue_dir)
    card = cardmod.load_card(cue_dir / "card.json")
    recipe = cardmod.load_recipe(cue_dir / "recipe.json")
    if recipe["cue"] != card["cue"] or cue_dir.name != card["cue"]:
        raise SoundbenchError(f"cue ids differ: folder {cue_dir.name!r}, card {card['cue']!r}, recipe {recipe['cue']!r}")
    design, edit, reordered = plan(card, recipe)
    family_members(card, cue_dir)  # refuse an inconsistent family before any audio is touched
    x, rate, take = check_take(cue_dir, recipe)
    cue = card["cue"]
    fade = next((s for s in edit if s["op"] == "fade"), None)
    ctx = {"kind": card["kind"], "category": card["category"], "binding": cardmod.onset_binding(card),
           "level": card["level"], "key": card.get("key"), "fade_out_ms": fade["params"]["out_ms"] if fade else 0.0}
    start = snapshot(x, rate)
    steps = []
    y = x
    for passname, seq in (("design", design), ("edit", edit)):
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
    out_dir, rep_dir = cue_dir / "out", cue_dir / "report"
    out_file = out_dir / f"{cue}.flac"
    log_file = out_dir / f"{cue}.log.json"
    exp = exportmod.export_flac(y, rate, out_file, source_rate=take["rate"], log=log_file)
    delivered, drate = read_float32(out_file)
    final = measures.measure(out_file)
    rows = evaluate(card, final, delivered.astype(np.float64), drate)
    fam = family_check(card, cue_dir, out_file)
    must_fail = [r["target"] for r in rows if r["must"] and r["result"] != "pass"]
    fam_fail = fam is not None and fam["result"] == "fail"
    fam_incomplete = fam is not None and fam["result"] == "incomplete"
    code = 1 if must_fail or fam_fail else (3 if fam_incomplete else 0)
    doc = {"tool": "soundbench render", "cue": cue, "card": card, "recipe": recipe, "take": take,
           "edit_order": [s["op"] for s in edit], "edit_reordered": reordered, "start": start, "steps": steps,
           "export": exp, "final": final, "targets": rows, "family": fam, "must_failed": must_fail,
           "exit_code": code, "tools": versions(),
           "verdict": "measured (screening aid: numbers are never a taste verdict; the owner judges in play-tests)"}
    if picture or must_fail or any(r["result"] != "pass" for r in rows) or card["tier"] == "important":
        from . import pictures

        rep_dir.mkdir(parents=True, exist_ok=True)
        doc["pictures"] = [str(pictures.picture(x, rate, rep_dir / f"{cue}.before.png", title=f"{cue} take")),
                           str(pictures.picture(delivered, drate, rep_dir / f"{cue}.after.png", title=f"{cue} rendered"))]
    log_file.write_text(json.dumps(doc, indent=2, default=_json_default) + "\n", encoding="utf-8")
    rep_dir.mkdir(parents=True, exist_ok=True)
    report = {k: doc[k] for k in ("cue", "targets", "family", "must_failed", "exit_code", "verdict")}
    report["file"] = str(out_file)
    report["audio_sha256_float32"] = exp["audio_sha256_float32"]
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
        lines.append(f"| {r['target']} | {r['measure']} | {r['value']} | {r['min']} | {r['max']} | "
                     f"{'must' if r['must'] else 'aim'} | {r['result']} |")
    if rep["family"]:
        f = rep["family"]
        lines += ["", f"Family `{f['id']}`: {f['result']}" + (f" ({f['reason']})" if f.get("reason") else "")]
    return "\n".join(lines) + "\n"
