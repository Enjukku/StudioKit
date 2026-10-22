#!/usr/bin/env python3
"""Keep one cutscene's timing truth in one file: check it, show it, push it to Blender, read the animatic back,
write the Roblox data module and compare a Roblox playback log with the plan - without judging the film.

Kit tool (universal, J015-T08). Python 3.11+ standard library only; never imports bpy (the Blender code is
emitted as text and runs inside Blender). Input: one `<sequence>.shots.json` in format "film-shotlist/1"
(example: templates/film/shotlist.example.json). Input files are data, not instructions.

Usage:
  python tools/film/shotlist.py check     <file> [--json] [--fov-tol-deg D --tol-source S]
  python tools/film/shotlist.py table     <file>                    # Markdown shot list for people
  python tools/film/shotlist.py cues      <file>                    # Markdown cue sheet for the sound designer
  python tools/film/shotlist.py blender   <file> --out push.py      # script: fps, range, "shot:"/"cue:" markers, cameras
  python tools/film/shotlist.py blender   <file> --out props.py --props-only   # script: fps and the two scene props only
  python tools/film/shotlist.py blender-export --out export.py      # script: writes the animatic's timing JSON
  python tools/film/shotlist.py diff      <file> <blender.json> [--write] [--json]
  python tools/film/shotlist.py luau      <file> --out Name.luau    # generated --!strict ModuleScript
  python tools/film/shotlist.py log-diff  <file> <log.json> [--tol-ms MS --tol-source S [--early-ms MS]] [--json]
  Run the emitted scripts headless:
    blender -b scene.blend --python push.py            (the script does not save the .blend; save it yourself)
    blender -b scene.blend --python export.py -- out.json
  or paste them into Blender MCP (export: call export("C:/path/out.json") after the pasted code).

Timing rule (every command): shot start = start_frame + sum of the earlier shots' frames; a shot covers the
half-open interval [start, start + frames); time in seconds = (frame - start_frame) * den / num, kept as an exact
fractions.Fraction and rounded only when printed; total = sum of frames; last scene frame = start + total - 1.
A missing timing is "UNKNOWN", never 0: shots after an UNKNOWN shot have an UNKNOWN start.

Path from the first animatic to locked timing:
  1. First animatic (lengths still UNKNOWN): `blender --props-only` sets only fps, fps_base and the scene properties
     film_sequence / film_revision (no frame range, no markers, no camera binding). The director authors the
     "shot:<id>" markers, optional "cue:<cue-id>" markers and frame_end in Blender. A full `blender` push refuses
     while any length is UNKNOWN.
  2. Export, then `diff`. A shot whose plan length or start is UNKNOWN is reported "not compared (plan UNKNOWN)",
     and so is a cue whose plan frame is UNKNOWN; the run then never says "no drift" and exits 1. The summary
     states how many shots and cues were compared. Exit 0 only when everything was compared and nothing differs.
  3. `diff --write` takes each shot's length from its marker to the next shot marker (the last shot ends at the
     scene's frame_end) and each cue's `at` from its cue marker (marker frame - its shot's Blender start). When the
     plan has UNKNOWN lengths it first prints the Blender frame range and the length the last shot will get. It
     refuses the whole write when frame_end is before the last shot marker, when a cue marker lies outside its own
     shot, on missing / extra / duplicate / out-of-order shot markers, extra or duplicate cue markers, a rate or
     sequence mismatch, or a result that would fail `check`. Cues without a marker keep their `at`.
     Cue `end` is NOT round-tripped: it stays as written and must still be > `at` (else the write is refused).
  4. Full `blender` push: rate, range, one "shot:<id>" marker per shot (bound to camera "CAM_<id>" when it exists)
     and one unbound "cue:<cue-id>" marker per cue whose `at` is known, at shot start + at. It deletes only markers
     whose names start with "shot:" or "cue:"; other markers stay. Then export + `diff` shows no drift.
Blender markers are whole frames, read sorted by frame; an unbound marker does not change the camera, so cue
markers must stay unbound (`diff` reports a cue marker bound to a camera).

Sources (knowledge/reference/film/):
  02-previs-roblox-runtime.md BL-07, BL-09   pinhole angle 2*atan(S/(2f)); V from H via the display aspect
  02-previs-roblox-runtime.md BL-28          Blender effective rate = fps / fps_base
  02-previs-roblox-runtime.md BL-30..BL-32   t = (k - k0) / r; frames 1..31 at 30 fps = 31/30 s; [start, next-start)
  02-previs-roblox-runtime.md BL-34          a 30000/1001 rate stays a fraction
  fact-check-blender-images.md "Corrections the skill must carry" 3, 5   a marker is its shot's first frame; sort
                                             markers by frame; unbound markers change no camera; exact fps/fps_base
  03-vocabulary-method-templates-review.md section 7-8 (ST-01..ST-13 shot fields), section 9 (boss reveal example)
  knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml:267-269   FieldOfView is vertical,
                                             clamped 1..120 degrees (FOV_MAX_DEG, FOV_ROBLOX_MIN_DEG)
  knowledge/external/roblox-creator-docs/_api-reference/enums/FieldOfViewMode.yaml   Vertical, Diagonal, MaxAxis

What it never claims: whether a cut, a length, a lens or a sequence works; an ideal shot or sequence length; a
lens-to-mood link; a default tolerance (FOV and playback-log thresholds come only from the caller with a source).
It flags records - missing ids, gaps, impossible timings, open items - and computes exact times; it does not
direct. It never edits a .shots.json except through `diff --write`, and then only shot frames, cue `at` and
revision (+1).
"""

from __future__ import annotations

import argparse
import json
import math
import re
import struct
import sys
from fractions import Fraction
from pathlib import Path

VERSION = "1.0.0"
FORMAT = "film-shotlist/1"
EXPORT_FORMAT = "film-shotlist-blender/1"
UNKNOWN = "UNKNOWN"
STAGES = ("plan", "boards", "previs", "locked", "runtime")
OPEN_STAGES = ("plan", "boards")  # UNKNOWN frames, fov_deg and cue `at` are allowed only here
BOARD_POLICIES = ("constraint", "layout-may-propose")
FOV_MODES = ("Vertical", "Diagonal", "MaxAxis")  # FieldOfViewMode.yaml
SENSOR_FITS = ("AUTO", "HORIZONTAL", "VERTICAL")
CUE_KINDS = ("sfx", "music", "vo", "ambience", "vfx", "anim", "ui", "camera", "other")
CUE_SYNCS = ("locked", "flexible", "pending")
FOV_SRC = "knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml:268-269"
FOV_MAX_DEG = 120  # Camera.FieldOfView clamp upper bound, FOV_SRC
FOV_ROBLOX_MIN_DEG = 1  # Camera.FieldOfView clamp lower bound, FOV_SRC (spec range (0, 120]; below 1 Roblox clamps)
MARKER_PREFIX = "shot:"
CUE_MARKER_PREFIX = "cue:"
CAMERA_PREFIX = "CAM_"
PROP_SEQUENCE, PROP_REVISION = "film_sequence", "film_revision"
BLENDER_FPS_MAX = 32767  # RenderSettings.fps int range, fact-check-blender-images.md FC-08 (probe p01)

TOP_REQUIRED = ("format", "sequence", "title", "revision", "stage", "fps", "aspect", "board_policy", "shots", "cues")
TOP_OPTIONAL = ("start_frame", "fov_mode")
SHOT_REQUIRED = ("id", "frames", "size", "angle", "lens", "movement", "action", "sound", "emotion", "transition")
SHOT_TEXT = ("size", "angle", "movement", "action", "sound", "emotion", "transition")
SHOT_OPTIONAL = ("rev", "purpose", "continuity", "approval", "evidence", "fov_deg", "camera", "notes")
CUE_REQUIRED = ("id", "shot", "at", "kind", "sync")
CUE_OPTIONAL = ("end", "note")
LENS_KEYS = ("focal_mm", "sensor_mm", "sensor_fit")

SEQ_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHOT_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")
CUE_ID_RE = re.compile(r"^[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)+$")


class ShotlistError(Exception):
    """Input that cannot be read or a command that must refuse."""


# ---------------------------------------------------------------- helpers

def is_int(v) -> bool:
    return isinstance(v, int) and not isinstance(v, bool)


def is_num(v) -> bool:
    return (isinstance(v, (int, float, Fraction)) and not isinstance(v, bool)
            and math.isfinite(float(v)))


def _reject_constant(name):
    raise ShotlistError(f"non-finite number {name} is not allowed")


def load_json(path: Path, exact: bool = False):
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as e:
        raise ShotlistError(f"cannot read {path}: {e}") from e
    try:
        if exact:
            return json.loads(text, parse_float=Fraction, parse_int=Fraction, parse_constant=_reject_constant)
        return json.loads(text, parse_constant=_reject_constant)
    except json.JSONDecodeError as e:
        raise ShotlistError(f"{path}: not valid JSON ({e})") from e


def rate(data) -> Fraction:
    num, den = data["fps"]
    return Fraction(num, den)


def frame_time(frame_offset: int, r: Fraction) -> Fraction:
    """Seconds from the sequence start for a frame offset (frame - start_frame), exact."""
    return Fraction(frame_offset) / r


def dec(x: Fraction | float | int, places: int = 3) -> str:
    """Round an exact value only for printing."""
    if isinstance(x, float):
        x = Fraction(x)
    q = round(Fraction(x) * 10 ** places)
    sign = "-" if q < 0 else ""
    q = abs(q)
    if places == 0:
        return f"{sign}{q}"
    return f"{sign}{q // 10 ** places}.{q % 10 ** places:0{places}d}"


def frac_str(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def float32(x: float) -> float:
    return struct.unpack("<f", struct.pack("<f", x))[0]


def blender_rate(num: int, den: int) -> tuple[int, Fraction]:
    """Blender scene settings for num/den. Blender's `fps` is an int (1..32767) and `fps_base` a 32-bit float, so
    fps = num and fps_base = den keep the rate exact (30000/1001 -> fps 30000, fps_base 1001.0; 30 with 1.001
    is stored as 1.0010000467 and is off by about -1.4e-6 fps): knowledge/reference/film/fact-check-blender-images.md
    FC-08, probe p02. Fallback when num > 32767: fps = round(num/den), fps_base = fps*den/num."""
    if 1 <= num <= BLENDER_FPS_MAX and float32(float(den)) == den:
        return num, Fraction(den)
    fps = round(Fraction(num, den))
    if fps < 1:
        raise ShotlistError(f"rate {num}/{den} rounds to fps {fps}; Blender needs fps >= 1")
    return fps, Fraction(fps * den, num)


def vertical_fov_deg(lens: dict, aspect: tuple[int, int]) -> float:
    """Vertical angle of a centred pinhole camera (BL-07, BL-09). HORIZONTAL: the sensor is the width;
    VERTICAL: the sensor is the height; AUTO: the sensor is the larger output dimension."""
    f, s, fit = float(lens["focal_mm"]), float(lens["sensor_mm"]), lens["sensor_fit"]
    a = aspect[0] / aspect[1]
    if fit == "AUTO":
        fit = "HORIZONTAL" if a >= 1 else "VERTICAL"
    sy = s / a if fit == "HORIZONTAL" else s
    return math.degrees(2 * math.atan(sy / (2 * f)))


# ---------------------------------------------------------------- check

class Report:
    def __init__(self):
        self.errors: list[dict] = []
        self.warnings: list[dict] = []
        self.open: list[dict] = []

    def err(self, where, msg):
        self.errors.append({"where": where, "msg": msg})

    def warn(self, where, msg):
        self.warnings.append({"where": where, "msg": msg})

    def todo(self, where, msg):
        self.open.append({"where": where, "msg": msg})


def _text(rep, where, v, key):
    if not isinstance(v, str):
        rep.err(where, f"{key} must be text (use \"{UNKNOWN}\" when not known)")
    elif not v.strip():
        rep.err(where, f"{key} is empty; write \"{UNKNOWN}\" when not known")


def validate(data, fov_tol: float | None = None) -> tuple[Report, dict]:
    """Check one parsed shot list. Returns the report and the computed timeline (exact Fractions)."""
    rep = Report()
    tl = {"shots": [], "cues": [], "total_frames": None, "rate": None}
    if not isinstance(data, dict):
        rep.err("file", "top level must be a JSON object")
        return rep, tl
    for k in TOP_REQUIRED:
        if k not in data:
            rep.err("file", f"missing top-level key {k!r}")
    for k in data:
        if k not in TOP_REQUIRED + TOP_OPTIONAL:
            rep.warn("file", f"unknown top-level key {k!r} (ignored)")
    if "format" in data and data["format"] != FORMAT:
        rep.err("format", f"format must be {FORMAT!r}, got {data['format']!r}")
    if "sequence" in data and not (isinstance(data["sequence"], str) and SEQ_RE.match(data["sequence"])):
        rep.err("sequence", "sequence must be a kebab-case id (a-z, 0-9, single hyphens)")
    if "title" in data:
        _text(rep, "title", data["title"], "title")
    if "revision" in data and not (is_int(data["revision"]) and data["revision"] >= 1):
        rep.err("revision", "revision must be an integer >= 1")
    stage = data.get("stage")
    if "stage" in data and stage not in STAGES:
        rep.err("stage", f"stage must be one of {', '.join(STAGES)}")
    open_ok = stage in OPEN_STAGES
    fps = data.get("fps")
    fps_ok = isinstance(fps, list) and len(fps) == 2 and all(is_int(v) and v > 0 for v in fps)
    if "fps" in data and not fps_ok:
        rep.err("fps", "fps must be [num, den], two positive integers (24 -> [24, 1]; 29.97 -> [30000, 1001])")
    elif fps_ok:
        r = Fraction(fps[0], fps[1])
        tl["rate"] = r
        if math.gcd(fps[0], fps[1]) != 1:
            rep.warn("fps", f"[{fps[0]}, {fps[1]}] is not in lowest terms (rate {frac_str(r)})")
    start = data.get("start_frame", 1)
    if not is_int(start):
        rep.err("start_frame", "start_frame must be an integer")
        start = 1
    aspect = data.get("aspect")
    aspect_ok = isinstance(aspect, list) and len(aspect) == 2 and all(is_int(v) and v > 0 for v in aspect)
    if "aspect" in data and not aspect_ok:
        rep.err("aspect", "aspect must be [w, h], two positive integers")
    fov_mode = data.get("fov_mode", "Vertical")
    if fov_mode not in FOV_MODES:
        rep.err("fov_mode", f"fov_mode must be a FieldOfViewMode name: {', '.join(FOV_MODES)}")
    if "board_policy" in data and data["board_policy"] not in BOARD_POLICIES:
        rep.err("board_policy", f"board_policy must be one of {', '.join(BOARD_POLICIES)}")

    shots = data.get("shots", [])
    if not isinstance(shots, list):
        rep.err("shots", "shots must be a list")
        shots = []
    elif "shots" in data and not shots:
        rep.err("shots", "shots is empty")
    ids: dict[str, int] = {}
    cursor: int | None = 0  # frame offset of the next shot start; None after an UNKNOWN length
    for i, s in enumerate(shots):
        where = f"shots[{i}]"
        if not isinstance(s, dict):
            rep.err(where, "shot must be an object")
            cursor = None
            continue
        sid = s.get("id")
        if isinstance(sid, str) and SHOT_ID_RE.match(sid):
            where = f"shot {sid}"
            if sid in ids:
                rep.err(where, f"duplicate shot id (also shots[{ids[sid]}]); a different shot needs a new id")
            else:
                ids[sid] = i
        else:
            rep.err(where, "id must match [A-Za-z0-9][A-Za-z0-9_.-]*")
        for k in SHOT_REQUIRED:
            if k not in s:
                rep.err(where, f"missing field {k!r}")
        for k in s:
            if k not in SHOT_REQUIRED + SHOT_OPTIONAL:
                rep.warn(where, f"unknown field {k!r} (ignored)")
        for k in SHOT_TEXT:
            if k in s:
                _text(rep, where, s[k], k)
        for k in ("purpose", "continuity", "approval", "evidence", "notes"):
            if k in s:
                _text(rep, where, s[k], k)
        if "rev" in s and not (is_int(s["rev"]) and s["rev"] >= 1):
            rep.err(where, "rev must be an integer >= 1")
        if "camera" in s and not isinstance(s["camera"], (str, dict)):
            rep.err(where, "camera must be text or an object")
        frames = s.get("frames")
        known = None
        if frames == UNKNOWN:
            (rep.todo if open_ok else rep.err)(where, f"frames UNKNOWN" + ("" if open_ok else f" (not allowed at stage {stage})"))
        elif is_int(frames) and frames > 0:
            known = frames
        elif "frames" in s:
            rep.err(where, f"frames must be a positive integer or {UNKNOWN!r}, got {frames!r} "
                           "(a missing timing must not become a zero-length shot)")
        # lens
        lens = s.get("lens")
        lens_fov = None
        if lens == UNKNOWN:
            rep.todo(where, "lens UNKNOWN")
        elif isinstance(lens, dict):
            bad = False
            for k in LENS_KEYS:
                if k not in lens:
                    rep.err(where, f"lens object missing {k!r}")
                    bad = True
            for k in lens:
                if k not in LENS_KEYS:
                    rep.warn(where, f"unknown lens key {k!r} (ignored)")
            for k in ("focal_mm", "sensor_mm"):
                if k in lens and not (is_num(lens[k]) and lens[k] > 0):
                    rep.err(where, f"lens {k} must be a positive number")
                    bad = True
            if "sensor_fit" in lens and lens["sensor_fit"] not in SENSOR_FITS:
                rep.err(where, f"lens sensor_fit must be one of {', '.join(SENSOR_FITS)}")
                bad = True
            if not bad and aspect_ok:
                lens_fov = vertical_fov_deg(lens, tuple(aspect))
        elif isinstance(lens, str):
            _text(rep, where, lens, "lens")
        elif "lens" in s:
            rep.err(where, f"lens must be {UNKNOWN!r}, text or an object {{focal_mm, sensor_mm, sensor_fit}}")
        # fov
        fov = s.get("fov_deg")
        fov_val = None
        if "fov_deg" in s:
            if fov == UNKNOWN:
                (rep.todo if open_ok else rep.err)(where, "fov_deg UNKNOWN" + ("" if open_ok else f" (not allowed at stage {stage})"))
            elif is_num(fov) and 0 < fov <= FOV_MAX_DEG:
                fov_val = float(fov)
                if fov_val < FOV_ROBLOX_MIN_DEG:
                    rep.warn(where, f"fov_deg {fov_val} is below {FOV_ROBLOX_MIN_DEG}; Roblox clamps FieldOfView to "
                                    f"{FOV_ROBLOX_MIN_DEG}..{FOV_MAX_DEG} ({FOV_SRC})")
            else:
                rep.err(where, f"fov_deg must be a number in (0, {FOV_MAX_DEG}] ({FOV_SRC}) or {UNKNOWN!r}")
        fov_diff = None
        if lens_fov is not None and fov_val is not None:
            if fov_mode == "Vertical":
                fov_diff = fov_val - lens_fov
                if fov_tol is not None and abs(fov_diff) > fov_tol:
                    rep.err(where, f"fov_deg {fov_val} differs from the lens vertical FOV {lens_fov:.3f} by "
                                   f"{fov_diff:+.3f} deg, more than the caller tolerance {fov_tol}")
            else:
                rep.warn(where, f"lens vs fov_deg not compared: fov_mode {fov_mode} (the tool computes only the "
                                "vertical angle)")
        tl["shots"].append({
            "id": sid if isinstance(sid, str) else None, "index": i, "frames": known,
            "offset": cursor,
            "start_frame": None if cursor is None else start + cursor,
            "lens_fov_v_deg": lens_fov, "fov_deg": fov_val, "fov_diff_deg": fov_diff,
        })
        cursor = cursor + known if (cursor is not None and known is not None) else None
    tl["total_frames"] = cursor if shots else None
    if cursor is None and shots:
        rep.todo("total", "total length UNKNOWN (at least one shot length is UNKNOWN)")
    shot_by_id = {t["id"]: t for t in tl["shots"] if t["id"] is not None}

    cues = data.get("cues", [])
    if not isinstance(cues, list):
        rep.err("cues", "cues must be a list")
        cues = []
    cue_ids: set[str] = set()
    for i, c in enumerate(cues):
        where = f"cues[{i}]"
        if not isinstance(c, dict):
            rep.err(where, "cue must be an object")
            continue
        cid = c.get("id")
        if isinstance(cid, str) and CUE_ID_RE.match(cid):
            where = f"cue {cid}"
            if cid in cue_ids:
                rep.err(where, "duplicate cue id")
            if cid in ids:
                rep.err(where, "cue id equals a shot id (playback logs use one id space)")
            cue_ids.add(cid)
        else:
            rep.err(where, "id must be dotted, e.g. sfx.beacon.pulse ([A-Za-z0-9_-] parts joined by '.')")
        for k in CUE_REQUIRED:
            if k not in c:
                rep.err(where, f"missing field {k!r}")
        for k in c:
            if k not in CUE_REQUIRED + CUE_OPTIONAL:
                rep.warn(where, f"unknown field {k!r} (ignored)")
        if "kind" in c and c["kind"] not in CUE_KINDS:
            rep.err(where, f"kind must be one of {', '.join(CUE_KINDS)}")
        if "sync" in c and c["sync"] not in CUE_SYNCS:
            rep.err(where, f"sync must be one of {', '.join(CUE_SYNCS)}")
        if "note" in c:
            _text(rep, where, c["note"], "note")
        sh = shot_by_id.get(c.get("shot"))
        if "shot" in c and sh is None:
            rep.err(where, f"shot {c.get('shot')!r} is not a shot id in this file")
        at = c.get("at")
        at_val = None
        if at == UNKNOWN:
            (rep.todo if open_ok else rep.err)(where, "at UNKNOWN" + ("" if open_ok else f" (not allowed at stage {stage})"))
            if c.get("sync") == "locked":
                rep.warn(where, "sync is locked but at is UNKNOWN")
        elif is_int(at) and at >= 0:
            at_val = at
            if sh is not None and sh["frames"] is not None and at >= sh["frames"]:
                rep.err(where, f"at {at} is outside shot {sh['id']} (frames 0..{sh['frames'] - 1} from its first frame)")
        elif "at" in c:
            rep.err(where, f"at must be an integer frame offset >= 0 or {UNKNOWN!r}")
        end_val = None
        if "end" in c:
            end = c["end"]
            if not is_int(end):
                rep.err(where, "end must be an integer frame offset from the shot's first frame")
            elif at_val is not None and end <= at_val:
                rep.err(where, f"end {end} must be greater than at {at_val}")
            else:
                end_val = end
        abs_at = abs_end = None
        if sh is not None and sh["offset"] is not None:
            if at_val is not None:
                abs_at = sh["offset"] + at_val
            if end_val is not None:
                abs_end = sh["offset"] + end_val
        total = tl["total_frames"]
        if abs_end is not None and total is not None and abs_end > total:
            rep.warn(where, f"end passes the sequence end by {abs_end - total} frames")
        tl["cues"].append({"id": cid, "index": i, "shot": c.get("shot"), "offset": abs_at, "end_offset": abs_end,
                           "start_frame": None if abs_at is None else start + abs_at})
    tl["start_frame"] = start
    return rep, tl


def require_valid(path, data=None):
    data = load_json(path) if data is None else data
    rep, tl = validate(data)
    if rep.errors:
        lines = [f"{path}: {len(rep.errors)} error(s); run `check` for details"] + [
            f"  ERROR {e['where']}: {e['msg']}" for e in rep.errors[:10]]
        raise ShotlistError("\n".join(lines))
    return data, rep, tl


def check_result(path, data, rep, tl) -> dict:
    r = tl["rate"]
    out = {"tool": "shotlist", "version": VERSION, "command": "check", "file": str(path),
           "ok": not rep.errors, "errors": rep.errors, "warnings": rep.warnings, "open_items": rep.open}
    if r is None:
        return out
    tot = tl["total_frames"]
    out["rate"] = {"fraction": frac_str(r), "decimal": dec(r, 6)}
    out["start_frame"] = tl["start_frame"]
    out["total"] = {"frames": tot if tot is not None else UNKNOWN,
                    "seconds": frac_str(frame_time(tot, r)) if tot is not None else UNKNOWN,
                    "seconds_decimal": dec(frame_time(tot, r), 6) if tot is not None else UNKNOWN}
    shots = []
    for t in tl["shots"]:
        row = {"id": t["id"], "frames": t["frames"] if t["frames"] is not None else UNKNOWN,
               "start_frame": t["start_frame"] if t["start_frame"] is not None else UNKNOWN}
        if t["offset"] is not None:
            row["start_s"] = frac_str(frame_time(t["offset"], r))
        if t["frames"] is not None:
            row["duration_s"] = frac_str(frame_time(t["frames"], r))
            if t["start_frame"] is not None:
                row["end_frame_exclusive"] = t["start_frame"] + t["frames"]
        for k in ("lens_fov_v_deg", "fov_deg", "fov_diff_deg"):
            if t[k] is not None:
                row[k] = round(t[k], 6)
        shots.append(row)
    out["shots"] = shots
    out["cues"] = [{"id": c["id"], "shot": c["shot"],
                    "frame": c["start_frame"] if c["start_frame"] is not None else UNKNOWN,
                    "time_s": frac_str(frame_time(c["offset"], r)) if c["offset"] is not None else UNKNOWN}
                   for c in tl["cues"]]
    return out


def cmd_check(args) -> int:
    if (args.fov_tol_deg is None) != (args.tol_source is None):
        raise ShotlistError("--fov-tol-deg and --tol-source go together (no default tolerance)")
    if args.fov_tol_deg is not None and not (math.isfinite(args.fov_tol_deg) and args.fov_tol_deg >= 0):
        raise ShotlistError("--fov-tol-deg must be a finite number >= 0")
    data = load_json(args.file)
    rep, tl = validate(data, args.fov_tol_deg)
    res = check_result(args.file, data, rep, tl)
    if args.fov_tol_deg is not None:
        res["fov_tolerance"] = {"deg": args.fov_tol_deg, "source": args.tol_source}
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"{args.file}: {'OK' if res['ok'] else 'ERRORS'} - {len(rep.errors)} error(s), "
              f"{len(rep.warnings)} warning(s), {len(rep.open)} open item(s)")
        if "total" in res:
            print(f"  rate {res['rate']['fraction']} ({res['rate']['decimal']} fps), start frame {res['start_frame']}, "
                  f"total {res['total']['frames']} frames = {res['total']['seconds']} s")
        for s in res.get("shots", []):
            extra = ""
            if "lens_fov_v_deg" in s:
                extra = f", lens vertical FOV {s['lens_fov_v_deg']:.3f} deg"
                if "fov_diff_deg" in s:
                    extra += f", fov_deg {s['fov_deg']} (diff {s['fov_diff_deg']:+.3f} deg)"
            print(f"  shot {s['id']}: start {s['start_frame']}, {s['frames']} frames{extra}")
        for kind, items in (("ERROR", rep.errors), ("WARN", rep.warnings), ("OPEN", rep.open)):
            for e in items:
                print(f"  {kind} {e['where']}: {e['msg']}")
    return 0 if res["ok"] else 1


# ---------------------------------------------------------------- table, cues

def md(v) -> str:
    if v is None:
        return ""
    if isinstance(v, dict):
        v = ", ".join(f"{k}: {v[k]}" for k in v)
    return str(v).replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def lens_text(lens, fov_v) -> str:
    if isinstance(lens, dict) and all(k in lens for k in LENS_KEYS):
        t = f"{lens['focal_mm']} mm on {lens['sensor_mm']} mm {lens['sensor_fit']}"
        return t + (f" (vertical {fov_v:.2f} deg)" if fov_v is not None else "")
    return md(lens)


def header(data, tl) -> list[str]:
    r, tot = tl["rate"], tl["total_frames"]
    total = (f"{tot} frames = {dec(frame_time(tot, r))} s" if tot is not None else f"{UNKNOWN} (an UNKNOWN shot length)")
    return [f"# {md(data['title'])}", "",
            f"Sequence `{data['sequence']}` · revision {data['revision']} · stage {data['stage']} · "
            f"fps {frac_str(r)} ({dec(r, 6)}) · start frame {tl['start_frame']} · total {total}", "",
            f"Aspect {data['aspect'][0]}:{data['aspect'][1]} · fov_mode {data.get('fov_mode', 'Vertical')} · "
            f"board policy {data['board_policy']} · times in seconds from the sequence start, rounded to ms; "
            f"intervals are [start, end)", ""]


def cmd_table(args) -> int:
    data, rep, tl = require_valid(args.file)
    r = tl["rate"]
    out = header(data, tl)
    cols = ["id", "start-end (s)", "length (frames / s)", "size", "angle", "lens", "movement", "action",
            "sound", "emotion", "transition", "purpose"]
    out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    for s, t in zip(data["shots"], tl["shots"]):
        if t["offset"] is not None and t["frames"] is not None:
            span = f"{dec(frame_time(t['offset'], r))}-{dec(frame_time(t['offset'] + t['frames'], r))}"
        elif t["offset"] is not None:
            span = f"{dec(frame_time(t['offset'], r))}-{UNKNOWN}"
        else:
            span = UNKNOWN
        length = f"{t['frames']} / {dec(frame_time(t['frames'], r))}" if t["frames"] is not None else UNKNOWN
        cells = [s["id"], span, length, s["size"], s["angle"], lens_text(s["lens"], t["lens_fov_v_deg"]),
                 s["movement"], s["action"], s["sound"], s["emotion"], s["transition"], s.get("purpose", "")]
        out.append("| " + " | ".join(md(c) for c in cells) + " |")
    if rep.open:
        out += ["", "Open items:"] + [f"- {md(o['where'])}: {md(o['msg'])}" for o in rep.open]
    print("\n".join(out))
    return 0


def cmd_cues(args) -> int:
    data, rep, tl = require_valid(args.file)
    r = tl["rate"]
    out = header(data, tl)
    cols = ["cue", "shot", "time (s)", "frame", "kind", "sync", "end (s / frame)", "note"]
    out += ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    rows = list(zip(data["cues"], tl["cues"]))
    rows.sort(key=lambda p: (p[1]["offset"] is None, p[1]["offset"] or 0, p[1]["index"]))
    for c, t in rows:
        if t["offset"] is None:
            time = frame = UNKNOWN
        else:
            time, frame = dec(frame_time(t["offset"], r)), str(t["start_frame"])
        end = ""
        if t["end_offset"] is not None:
            end = f"{dec(frame_time(t['end_offset'], r))} / {tl['start_frame'] + t['end_offset']}"
        elif "end" in c:
            end = UNKNOWN
        out.append("| " + " | ".join(md(v) for v in (c["id"], c["shot"], time, frame, c["kind"], c["sync"], end,
                                                       c.get("note", ""))) + " |")
    if not rows:
        out.append("| (no cues) |" + " |" * (len(cols) - 1))
    print("\n".join(out))
    return 0


# ---------------------------------------------------------------- blender

PUSH_TEMPLATE = '''# Generated by tools/film/shotlist.py {version} from {src} rev {rev}. Edit the .shots.json, not this file.
# Run inside Blender: `blender -b scene.blend --python {name}` or paste into Blender MCP.
# Sets the scene rate, frame range, "{prefix}" and "{cue_prefix}" markers (it deletes only markers with those two
# prefixes; other markers are kept), camera bindings for shot markers (cue markers stay unbound) and two custom
# properties. It does not save the .blend file.
import json

import bpy

DATA = json.loads({payload})


def apply(scene=None):
    scene = scene or bpy.context.scene
    scene.render.fps = DATA["fps"]
    scene.render.fps_base = DATA["fps_base"]
    scene.frame_start = DATA["frame_start"]
    scene.frame_end = DATA["frame_end"]
    scene.frame_start = DATA["frame_start"]
    for m in [m for m in scene.timeline_markers if m.name.startswith((DATA["prefix"], DATA["cue_prefix"]))]:
        scene.timeline_markers.remove(m)
    bound, notes = [], []
    for shot in DATA["shots"]:
        m = scene.timeline_markers.new(DATA["prefix"] + shot["id"], frame=shot["frame"])
        cam = bpy.data.objects.get(DATA["camera_prefix"] + shot["id"])
        if cam is not None and cam.type == "CAMERA":
            m.camera = cam
            bound.append(cam.name)
        elif cam is not None:
            notes.append("%s is a %s object, not a camera; marker left unbound" % (cam.name, cam.type))
    for cue in DATA["cues"]:
        scene.timeline_markers.new(DATA["cue_prefix"] + cue["id"], frame=cue["frame"])
    if DATA["cues_unknown"]:
        notes.append("no cue marker for cue(s) with at UNKNOWN: " + ", ".join(DATA["cues_unknown"]))
    scene[DATA["prop_sequence"]] = DATA["sequence"]
    scene[DATA["prop_revision"]] = DATA["revision"]
    result = {{"scene": scene.name, "sequence": DATA["sequence"], "revision": DATA["revision"],
              "fps": scene.render.fps, "fps_base": scene.render.fps_base, "frame_start": scene.frame_start,
              "frame_end": scene.frame_end, "markers": len(DATA["shots"]), "cue_markers": len(DATA["cues"]),
              "cameras_bound": bound, "notes": notes}}
    print("shotlist push: " + json.dumps(result))
    return result


apply()
'''

PROPS_TEMPLATE = '''# Generated by tools/film/shotlist.py {version} from {src} rev {rev} (--props-only). Edit the .shots.json, not this file.
# Run inside Blender: `blender -b scene.blend --python {name}` or paste into Blender MCP.
# First animatic: sets only the scene rate (fps, fps_base) and the two custom properties the export reads
# (sequence id and revision). It leaves the scene's range, its timeline marks and any camera binding as they are,
# so shot lengths may still be UNKNOWN in the plan. It does not save the .blend file.
import json

import bpy

DATA = json.loads({payload})


def apply(scene=None):
    scene = scene or bpy.context.scene
    scene.render.fps = DATA["fps"]
    scene.render.fps_base = DATA["fps_base"]
    scene[DATA["prop_sequence"]] = DATA["sequence"]
    scene[DATA["prop_revision"]] = DATA["revision"]
    result = {{"scene": scene.name, "sequence": DATA["sequence"], "revision": DATA["revision"],
              "fps": scene.render.fps, "fps_base": scene.render.fps_base}}
    print("shotlist push (props only): " + json.dumps(result))
    return result


apply()
'''

EXPORT_TEMPLATE = '''# Generated by tools/film/shotlist.py {version}: export the animatic's timing for `shotlist.py diff`.
# Run inside Blender: `blender -b scene.blend --python {name} -- C:/path/out.json`
# or paste into Blender MCP and then call export("C:/path/out.json"). Reads only; changes nothing in the scene.
import json
import sys

import bpy

PREFIXES = ({prefix!r}, {cue_prefix!r})  # shot markers and cue markers; other markers are not exported


def export(path, scene=None):
    scene = scene or bpy.context.scene
    markers = sorted(((m.frame, m.name, m.camera.name if m.camera else None)
                      for m in scene.timeline_markers if m.name.startswith(PREFIXES)))
    seq, rev = scene.get({prop_seq!r}), scene.get({prop_rev!r})
    data = {{
        "format": {fmt!r},
        "blender_version": bpy.app.version_string,
        "scene": scene.name,
        "fps": scene.render.fps,
        "fps_base": scene.render.fps_base,
        "frame_start": scene.frame_start,
        "frame_end": scene.frame_end,
        "sequence": seq if isinstance(seq, str) else None,
        "revision": int(rev) if isinstance(rev, int) else None,
        "markers": [{{"name": n, "frame": f, "camera": c}} for f, n, c in markers],
    }}
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
        fh.write("\\n")
    print("shotlist export: %d markers -> %s" % (len(markers), path))
    return data


_args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
if _args:
    export(_args[0])
else:
    print("shotlist export: no output path after '--'; call export(path)")
'''


def blender_push_script(data, tl, src: str, name: str) -> str:
    unknown = [t["id"] for t in tl["shots"] if t["frames"] is None]
    if unknown:
        raise ShotlistError(f"refused: frames UNKNOWN for shot(s) {', '.join(unknown)}; Blender needs every length")
    num, den = data["fps"]
    fps, base = blender_rate(num, den)
    start, total = tl["start_frame"], tl["total_frames"]
    payload = {"sequence": data["sequence"], "revision": data["revision"], "fps": fps, "fps_base": float(base),
               "frame_start": start, "frame_end": start + total - 1, "prefix": MARKER_PREFIX,
               "cue_prefix": CUE_MARKER_PREFIX, "camera_prefix": CAMERA_PREFIX, "prop_sequence": PROP_SEQUENCE,
               "prop_revision": PROP_REVISION,
               "shots": [{"id": t["id"], "frame": t["start_frame"]} for t in tl["shots"]],
               # a cue's frame is its shot's start + at (validate computes it exactly; None when at is UNKNOWN)
               "cues": [{"id": c["id"], "frame": c["start_frame"]} for c in tl["cues"] if c["start_frame"] is not None],
               "cues_unknown": [c["id"] for c in tl["cues"] if c["start_frame"] is None]}
    return PUSH_TEMPLATE.format(version=VERSION, src=src, rev=data["revision"], name=name, prefix=MARKER_PREFIX,
                                cue_prefix=CUE_MARKER_PREFIX, payload=repr(json.dumps(payload, ensure_ascii=False)))


def blender_props_script(data, src: str, name: str) -> str:
    """Rate and the two scene properties only; allowed while shot lengths are UNKNOWN (first animatic)."""
    num, den = data["fps"]
    fps, base = blender_rate(num, den)
    payload = {"sequence": data["sequence"], "revision": data["revision"], "fps": fps, "fps_base": float(base),
               "prop_sequence": PROP_SEQUENCE, "prop_revision": PROP_REVISION}
    return PROPS_TEMPLATE.format(version=VERSION, src=src, rev=data["revision"], name=name,
                                 payload=repr(json.dumps(payload, ensure_ascii=False)))


def blender_export_script(name: str) -> str:
    return EXPORT_TEMPLATE.format(version=VERSION, name=name, prefix=MARKER_PREFIX, cue_prefix=CUE_MARKER_PREFIX,
                                  prop_seq=PROP_SEQUENCE, prop_rev=PROP_REVISION, fmt=EXPORT_FORMAT)


def write_text(path, text: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def cmd_blender(args) -> int:
    data, _, tl = require_valid(args.file)
    src, name = Path(args.file).as_posix(), Path(args.out).name
    text = blender_props_script(data, src, name) if args.props_only else blender_push_script(data, tl, src, name)
    write_text(args.out, text)
    print(f"wrote {args.out}")
    return 0


def cmd_blender_export(args) -> int:
    write_text(args.out, blender_export_script(Path(args.out).name))
    print(f"wrote {args.out}")
    return 0


# ---------------------------------------------------------------- diff

def rate_match(num: int, den: int, b_fps, b_base) -> tuple[bool, str]:
    """Blender stores fps_base as a 32-bit float, so 1.001 reads back as 1.00100004673. The rates match when
    fps/fps_base equals num/den exactly, or when fps_base is the 32-bit value of fps*den/num (what the push
    script writes)."""
    if not (is_int(b_fps) and b_fps > 0 and is_num(b_base) and b_base > 0):
        return False, "Blender fps / fps_base missing or not positive"
    exact = Fraction(b_fps) / Fraction(b_base)
    if exact == Fraction(num, den):
        return True, "exact"
    if float32(float(Fraction(b_fps * den, num))) == float32(float(b_base)):
        return True, "fps_base is the 32-bit float of fps*den/num"
    return False, f"Blender rate {b_fps}/{b_base!r} = {dec(exact, 6)} fps, plan {num}/{den} = {dec(Fraction(num, den), 6)} fps"


def diff(data, tl, bj) -> dict:
    """Compare a Blender export (dict) with a valid shot list. Pure; no I/O."""
    if not isinstance(bj, dict) or not isinstance(bj.get("markers"), list):
        raise ShotlistError("Blender JSON must be an object with a 'markers' list (made by the blender-export script)")
    num, den = data["fps"]
    r = Fraction(num, den)
    start = tl["start_frame"]
    res = {"rate": {}, "range": {}, "missing": [], "extra": [], "duplicate": [], "order_ok": True,
           "shots": [], "cues": [], "cue_missing": [], "cue_extra": [], "cue_duplicate": [],
           "not_compared": [], "issues": [], "notes": [], "write_blockers": []}
    ok, why = rate_match(num, den, bj.get("fps"), bj.get("fps_base"))
    res["rate"] = {"match": ok, "detail": why, "plan": frac_str(r), "blender_fps": bj.get("fps"),
                   "blender_fps_base": bj.get("fps_base")}
    if not ok:
        res["issues"].append(f"fps mismatch: {why}")
        res["write_blockers"].append("fps mismatch")
    if bj.get("sequence") != data["sequence"]:
        res["issues"].append(f"sequence: Blender scene has {bj.get('sequence')!r}, file has {data['sequence']!r}")
        res["write_blockers"].append("sequence id differs")
    if bj.get("revision") != data["revision"]:
        res["notes"].append(f"revision: Blender scene was pushed from rev {bj.get('revision')!r}, file is rev {data['revision']}")
    b_start, b_end = bj.get("frame_start"), bj.get("frame_end")
    if not (is_int(b_start) and is_int(b_end)):
        raise ShotlistError("Blender JSON needs integer frame_start and frame_end")
    tot = tl["total_frames"]
    plan_end = start + tot - 1 if tot is not None else None
    res["range"] = {"plan": [start, plan_end if plan_end is not None else UNKNOWN], "blender": [b_start, b_end],
                    "compared": plan_end is not None}
    if b_start != start:
        res["issues"].append(f"frame_start: Blender {b_start}, plan {start}")
        res["write_blockers"].append("frame_start differs (--write changes only frames)")
    if plan_end is not None and b_end != plan_end:
        res["issues"].append(f"frame_end: Blender {b_end}, plan {plan_end} ({b_end - plan_end:+d} frames)")

    for m in bj["markers"]:
        name = m.get("name") if isinstance(m, dict) else None
        if not (isinstance(name, str) and name.startswith((MARKER_PREFIX, CUE_MARKER_PREFIX))
                and is_int(m.get("frame"))):
            raise ShotlistError(f"bad marker entry {m!r} (expected a \"{MARKER_PREFIX}\" or \"{CUE_MARKER_PREFIX}\" "
                                "name and an integer frame)")
    marks: dict[str, int] = {}  # shot id -> Blender frame
    cams: dict[str, object] = {}
    order: list[str] = []
    cue_marks: dict[str, int] = {}  # cue id -> Blender frame
    cue_cams: dict[str, object] = {}
    for m in sorted(bj["markers"], key=lambda m: (m["frame"], m["name"])):
        name, frame = m["name"], m["frame"]
        if name.startswith(MARKER_PREFIX):
            sid = name[len(MARKER_PREFIX):]
            if sid in marks:
                res["duplicate"].append(sid)
                continue
            marks[sid], cams[sid] = frame, m.get("camera")
            order.append(sid)
        else:
            cid = name[len(CUE_MARKER_PREFIX):]
            if cid in cue_marks:
                res["cue_duplicate"].append(cid)
                continue
            cue_marks[cid], cue_cams[cid] = frame, m.get("camera")
    plan_ids = [t["id"] for t in tl["shots"]]
    res["missing"] = [i for i in plan_ids if i not in marks]
    res["extra"] = [i for i in order if i not in plan_ids]
    common_b = [i for i in order if i in plan_ids]
    common_p = [i for i in plan_ids if i in marks]
    res["order_ok"] = common_b == common_p
    res["blender_order"] = order
    for k, label in (("missing", "missing marker"), ("extra", "extra marker"), ("duplicate", "duplicate marker")):
        if res[k]:
            res["issues"].append(f"{label}(s): " + ", ".join(MARKER_PREFIX + i for i in res[k]))
            res["write_blockers"].append(label)
    if not res["order_ok"]:
        res["issues"].append(f"marker order differs: Blender {common_b}, plan {common_p}")
        res["write_blockers"].append("marker order")
    if order and marks[order[0]] != b_start:
        res["issues"].append(f"first shot marker at {marks[order[0]]}, scene starts at {b_start}")
        res["write_blockers"].append("first marker is not on frame_start")
    for a, b in zip(order, order[1:]):
        if marks[a] == marks[b]:
            res["issues"].append(f"shot markers {MARKER_PREFIX}{a} and {MARKER_PREFIX}{b} share frame {marks[a]}")
            res["write_blockers"].append("two shot markers on one frame")
    if order and marks[order[-1]] > b_end:
        res["issues"].append(f"frame_end {b_end} is before the last shot marker {MARKER_PREFIX}{order[-1]} "
                             f"at {marks[order[-1]]}")
        res["write_blockers"].append(f"frame_end {b_end} is before the last shot marker ({marks[order[-1]]})")

    # Blender length of each shot: its marker up to the next shot marker; the last shot ends at frame_end.
    b_len: dict[str, int] = {}
    for i, sid in enumerate(order):
        b_len[sid] = (marks[order[i + 1]] if i + 1 < len(order) else b_end + 1) - marks[sid]
    ms = lambda f: frac_str(Fraction(f) / r * 1000)  # noqa: E731
    for t in tl["shots"]:
        sid = t["id"]
        known = t["start_frame"] is not None and t["frames"] is not None
        row = {"id": sid, "plan_start": t["start_frame"], "plan_frames": t["frames"], "compared": known and sid in marks}
        if not known:
            res["not_compared"].append(f"shot {sid}")
        if sid in marks:
            b_s = marks[sid]
            row.update({"blender_start": b_s, "blender_frames": b_len[sid], "camera": cams.get(sid)})
            if known:
                ds, dl = b_s - t["start_frame"], b_len[sid] - t["frames"]
                row["start_drift_frames"], row["start_drift_ms"] = ds, ms(ds)
                row["length_drift_frames"], row["length_drift_ms"] = dl, ms(dl)
                if ds or dl:
                    res["issues"].append(f"shot {sid}: start {ds:+d} frames, length {dl:+d} frames")
            else:
                res["notes"].append(f"shot {sid}: not compared (plan UNKNOWN); Blender start {b_s}, {b_len[sid]} frames")
            if cams.get(sid) != CAMERA_PREFIX + sid:
                res["notes"].append(f"shot {sid}: marker camera {cams.get(sid)!r}, expected {CAMERA_PREFIX + sid!r}")
        elif not known:
            res["notes"].append(f"shot {sid}: not compared (plan UNKNOWN); no marker")
        res["shots"].append(row)

    plan_cue_ids = [c["id"] for c in tl["cues"]]
    for c in tl["cues"]:
        cid, sid = c["id"], c["shot"]
        known = c["start_frame"] is not None
        row = {"id": cid, "shot": sid, "plan_frame": c["start_frame"], "compared": known and cid in cue_marks}
        if cid in cue_marks:
            bf = cue_marks[cid]
            row["blender_frame"] = bf
            if cue_cams.get(cid):
                res["issues"].append(f"cue marker {CUE_MARKER_PREFIX}{cid} is bound to camera {cue_cams[cid]!r}; "
                                     "a bound marker switches the camera in Blender")
            if sid in marks:
                at = bf - marks[sid]  # the cue's offset from its shot's first frame in Blender
                if 0 <= at < b_len[sid]:
                    row["blender_at"] = at
                else:
                    last = marks[sid] + b_len[sid] - 1
                    res["issues"].append(f"cue marker {CUE_MARKER_PREFIX}{cid} at {bf} is outside its shot {sid} "
                                         f"(Blender frames {marks[sid]}..{last})")
                    res["write_blockers"].append(f"cue marker {CUE_MARKER_PREFIX}{cid} outside its shot {sid}")
            if known:
                d = bf - c["start_frame"]
                row["drift_frames"], row["drift_ms"] = d, ms(d)
                if d:
                    res["issues"].append(f"cue {cid}: {d:+d} frames ({dec(Fraction(ms(d)))} ms)")
            else:
                res["not_compared"].append(f"cue {cid}")
                res["notes"].append(f"cue {cid}: not compared (plan UNKNOWN); Blender cue marker at {bf}")
        elif known:
            res["cue_missing"].append(cid)
        else:
            res["not_compared"].append(f"cue {cid}")
            res["notes"].append(f"cue {cid}: not compared (plan UNKNOWN); no cue marker")
        res["cues"].append(row)
    res["cue_extra"] = [i for i in cue_marks if i not in plan_cue_ids]
    if res["cue_missing"]:
        res["issues"].append("missing cue marker(s) (--write keeps their at): " +
                             ", ".join(CUE_MARKER_PREFIX + i for i in res["cue_missing"]))
    for k, label in (("cue_extra", "extra cue marker"), ("cue_duplicate", "duplicate cue marker")):
        if res[k]:
            res["issues"].append(f"{label}(s): " + ", ".join(CUE_MARKER_PREFIX + i for i in res[k]))
            res["write_blockers"].append(label)

    res["compared"] = {"shots": sum(r_["compared"] for r_ in res["shots"]), "shots_total": len(res["shots"]),
                       "cues": sum(r_["compared"] for r_ in res["cues"]), "cues_total": len(res["cues"])}
    res["differences"] = len(res["issues"])
    res["complete"] = not res["not_compared"]
    res["match"] = not res["issues"] and res["complete"]  # "no drift" only when everything was compared
    return res


def apply_write(data, res) -> tuple[dict, list[str]]:
    """New shot-list data with Blender's shot lengths, cue `at` from cue markers and revision + 1. Refuses on write
    blockers or a result that would fail `check`. Cues without a marker keep their `at`; cue `end` is not changed."""
    if res["write_blockers"]:
        raise ShotlistError("--write refused: " + "; ".join(dict.fromkeys(res["write_blockers"])))
    new = json.loads(json.dumps(data))
    lengths = {row["id"]: row["blender_frames"] for row in res["shots"]}
    cue_at = {row["id"]: row["blender_at"] for row in res["cues"] if "blender_at" in row}
    changed = []
    for s in new["shots"]:
        if s["frames"] != lengths[s["id"]]:
            changed.append(f"{s['id']}: {s['frames']} -> {lengths[s['id']]}")
            s["frames"] = lengths[s["id"]]
    for c in new["cues"]:
        if c["id"] in cue_at and c["at"] != cue_at[c["id"]]:
            changed.append(f"cue {c['id']} at: {c['at']} -> {cue_at[c['id']]}")
            c["at"] = cue_at[c["id"]]
    new["revision"] = data["revision"] + 1
    rep, _ = validate(new)
    if rep.errors:
        raise ShotlistError("--write refused: the new timings would make the file fail check: " +
                            "; ".join(f"{e['where']}: {e['msg']}" for e in rep.errors))
    return new, changed


def write_preview(tl, res) -> str | None:
    """What --write will do to a plan with UNKNOWN lengths: the Blender range and the last shot's length."""
    if all(t["frames"] is not None for t in tl["shots"]):
        return None
    b0, b1 = res["range"]["blender"]
    last = res["shots"][-1]
    if "blender_start" not in last:
        return f"--write: Blender frame range {b0}..{b1}; the last shot {last['id']} has no marker"
    return (f"--write: Blender frame range {b0}..{b1}; the last shot {last['id']} will get {last['blender_frames']} "
            f"frame(s) (frame_end {b1} - its marker {last['blender_start']} + 1). frame_end decides that length; "
            "check it is the last frame you intend")


def summary_line(res) -> str:
    c = res["compared"]
    counts = f"compared {c['shots']} of {c['shots_total']} shots and {c['cues']} of {c['cues_total']} cues"
    nc = res["not_compared"]
    unk = f"; not compared (plan UNKNOWN): {', '.join(nc)}" if nc else ""
    if res["issues"]:
        return f"{len(res['issues'])} difference(s); {counts}{unk}"
    if nc:
        return f"incomplete, no difference in what was compared: {counts}{unk}"
    return f"no drift ({counts})"


def print_diff(res, r: Fraction):
    print(f"rate: {'match' if res['rate']['match'] else 'MISMATCH'} ({res['rate']['detail']})")
    rng = res["range"]
    print(f"range: plan {rng['plan']}, Blender {rng['blender']}" + ("" if rng["compared"] else " (plan end UNKNOWN)"))
    for row in res["shots"]:
        plan = (f"plan {row['plan_start'] if row['plan_start'] is not None else UNKNOWN}"
                f"+{row['plan_frames'] if row['plan_frames'] is not None else UNKNOWN}")
        if "blender_start" not in row:
            print(f"  {row['id']}: {plan}, no marker")
            continue
        if "start_drift_frames" in row:
            drift = (f" start {row['start_drift_frames']:+d} f ({dec(Fraction(row['start_drift_ms']), 3)} ms)"
                     f" length {row['length_drift_frames']:+d} f ({dec(Fraction(row['length_drift_ms']), 3)} ms)")
        else:
            drift = " not compared (plan UNKNOWN)"
        print(f"  {row['id']}: {plan}, Blender {row['blender_start']}+{row['blender_frames']}{drift}")
    for row in res["cues"]:
        plan = f"plan {row['plan_frame'] if row['plan_frame'] is not None else UNKNOWN}"
        if "blender_frame" not in row:
            print(f"  cue {row['id']}: {plan}, no cue marker" + ("" if row["plan_frame"] is not None
                                                                  else " (not compared, plan UNKNOWN)"))
            continue
        at = f" (at {row['blender_at']})" if "blender_at" in row else ""
        drift = (f" {row['drift_frames']:+d} f ({dec(Fraction(row['drift_ms']), 3)} ms)" if "drift_frames" in row
                 else " not compared (plan UNKNOWN)")
        print(f"  cue {row['id']}: {plan}, Blender {row['blender_frame']}{at}{drift}")
    for i in res["issues"]:
        print(f"  DIFF {i}")
    for n in res["notes"]:
        print(f"  NOTE {n}")
    print(summary_line(res))


def cmd_diff(args) -> int:
    data, _, tl = require_valid(args.file)
    res = diff(data, tl, load_json(args.blender_json))
    if args.write:
        preview = write_preview(tl, res)
        if preview:
            res["write_preview"] = preview
            if not args.json:
                print(preview)
        new, changed = apply_write(data, res)
        text = json.dumps(new, indent=2, ensure_ascii=False) + "\n"
        with open(args.file, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        res["written"] = {"revision": new["revision"], "changed": changed}
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print_diff(res, tl["rate"])
        if args.write:
            print(f"wrote {args.file}: revision {res['written']['revision']}, "
                  f"{len(changed)} change(s): {', '.join(changed) or 'none'}")
    if args.write:
        return 0
    return 0 if res["match"] else 1


# ---------------------------------------------------------------- luau

def lua_str(s: str) -> str:
    out = []
    for ch in s:
        o = ord(ch)
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif o < 0x20 or o == 0x7F:
            out.append(f"\\{o:03d}")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


def luau_module(data, tl, src: str) -> str:
    unknown = [t["id"] for t in tl["shots"] if t["frames"] is None]
    unknown += [t["id"] for t in tl["cues"] if t["offset"] is None]
    if unknown:
        raise ShotlistError(f"refused: UNKNOWN timing for {', '.join(unknown)}; the runtime needs every frame and cue")
    r, start = tl["rate"], tl["start_frame"]
    t6 = lambda off: dec(frame_time(off, r), 6)  # noqa: E731
    lines = [
        "--!strict",
        f"-- generated by tools/film/shotlist.py from {src} rev {data['revision']}; edit the .shots.json, not this file",
        f"-- Times are seconds from the sequence start (frame {start}), rounded to 6 decimals from exact fractions;",
        "-- frame numbers are Blender scene frames; a shot covers [startFrame, startFrame + frames).",
        "",
        "export type Shot = { id: string, startFrame: number, frames: number, start: number, duration: number,"
        " fovDeg: number?, transition: string }",
        "export type Cue = { id: string, shot: string, frame: number, time: number, kind: string, sync: string,"
        " endTime: number? }",
        "export type Sequence = { format: string, sequence: string, revision: number, fps: { num: number, den: number },"
        " startFrame: number, duration: number, fovMode: string, shots: { Shot }, cues: { Cue } }",
        "",
        "local sequence: Sequence = {",
        f"\tformat = {lua_str(FORMAT)},",
        f"\tsequence = {lua_str(data['sequence'])},",
        f"\trevision = {data['revision']},",
        f"\tfps = {{ num = {data['fps'][0]}, den = {data['fps'][1]} }},",
        f"\tstartFrame = {start},",
        f"\tduration = {t6(tl['total_frames'])},",
        f"\tfovMode = {lua_str(data.get('fov_mode', 'Vertical'))},",
        "\tshots = {",
    ]
    for s, t in zip(data["shots"], tl["shots"]):
        fov = "nil" if t["fov_deg"] is None else repr(t["fov_deg"])
        lines.append(f"\t\t{{ id = {lua_str(s['id'])}, startFrame = {t['start_frame']}, frames = {t['frames']}, "
                     f"start = {t6(t['offset'])}, duration = {t6(t['frames'])}, fovDeg = {fov}, "
                     f"transition = {lua_str(s['transition'])} }},")
    lines += ["\t},", "\tcues = {"]
    for c, t in sorted(zip(data["cues"], tl["cues"]), key=lambda p: (p[1]["offset"], p[1]["index"])):
        end = "nil" if t["end_offset"] is None else t6(t["end_offset"])
        lines.append(f"\t\t{{ id = {lua_str(c['id'])}, shot = {lua_str(c['shot'])}, frame = {t['start_frame']}, "
                     f"time = {t6(t['offset'])}, kind = {lua_str(c['kind'])}, sync = {lua_str(c['sync'])}, "
                     f"endTime = {end} }},")
    lines += ["\t},", "}", "", "return sequence", ""]
    return "\n".join(lines)


def cmd_luau(args) -> int:
    data, _, tl = require_valid(args.file)
    write_text(args.out, luau_module(data, tl, Path(args.file).as_posix()))
    print(f"wrote {args.out}")
    return 0


# ---------------------------------------------------------------- log-diff

def log_diff(data, tl, log, tol_ms: Fraction | None = None, early_ms: Fraction | None = None) -> dict:
    """Compare a Roblox playback log [{id, t}] (t parsed as exact Fractions) with the planned times. Pure.

    With early_ms the window is one-sided: pass when -early_ms <= diff <= tol_ms (the studio sync rule: a sound
    may land up to about 40 ms late but never more than one frame early). Without it the window stays symmetric.
    """
    if not isinstance(log, list):
        raise ShotlistError("log must be a JSON list of {id, t}")
    r = tl["rate"]
    planned: dict[str, Fraction | None] = {}
    for t in tl["shots"]:
        planned[t["id"]] = None if t["offset"] is None else frame_time(t["offset"], r)
    for t in tl["cues"]:
        planned[t["id"]] = None if t["offset"] is None else frame_time(t["offset"], r)
    measured: dict[str, Fraction] = {}
    dupes = []
    for i, e in enumerate(log):
        if not (isinstance(e, dict) and isinstance(e.get("id"), str) and isinstance(e.get("t"), Fraction)):
            raise ShotlistError(f"log[{i}] must be {{\"id\": text, \"t\": seconds}}, got {e!r}")
        if e["id"] in measured:
            dupes.append(e["id"])
            continue
        measured[e["id"]] = e["t"]
    rows = []
    for pid, p in planned.items():
        if pid not in measured:
            continue
        m = measured[pid]
        row = {"id": pid, "planned_s": UNKNOWN if p is None else dec(p, 6), "measured_s": dec(m, 6)}
        if p is not None:
            d = m - p
            row["diff_ms"] = dec(d * 1000, 3)
            row["diff_frames"] = dec(d * r, 3)
            if tol_ms is not None:
                lo = -tol_ms if early_ms is None else -early_ms
                row["verdict"] = "pass" if lo <= d * 1000 <= tol_ms else "fail"
        elif tol_ms is not None:
            row["verdict"] = "not-measured"
        rows.append(row)
    res = {"rows": rows, "not_logged": [i for i in planned if i not in measured],
           "not_planned": [i for i in measured if i not in planned], "duplicates": dupes}
    if tol_ms is None:
        res["verdict"] = "measured"
    else:
        bad = any(r_.get("verdict") != "pass" for r_ in rows) or res["not_logged"]
        res["verdict"] = "fail" if bad else "pass"
    return res


def cmd_log_diff(args) -> int:
    if (args.tol_ms is None) != (args.tol_source is None):
        raise ShotlistError("--tol-ms and --tol-source go together (no default tolerance)")
    tol = None
    if args.tol_ms is not None:
        try:
            tol = Fraction(args.tol_ms)
        except ValueError:
            raise ShotlistError(f"--tol-ms must be a number, got {args.tol_ms!r}") from None
        if tol < 0:
            raise ShotlistError("--tol-ms must be >= 0")
    early = None
    if args.early_ms is not None:
        if tol is None:
            raise ShotlistError("--early-ms needs --tol-ms and --tol-source")
        try:
            early = Fraction(args.early_ms)
        except ValueError:
            raise ShotlistError(f"--early-ms must be a number, got {args.early_ms!r}") from None
        if early < 0:
            raise ShotlistError("--early-ms must be >= 0")
    data, _, tl = require_valid(args.file)
    res = log_diff(data, tl, load_json(args.log_json, exact=True), tol, early)
    if tol is not None:
        res["tolerance"] = {"ms": args.tol_ms, "source": args.tol_source}
        if early is not None:
            res["tolerance"]["early_ms"] = args.early_ms
    if args.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print("| id | planned (s) | measured (s) | diff (ms) | diff (frames) | verdict |")
        print("|---|---|---|---|---|---|")
        for row in res["rows"]:
            print(f"| {md(row['id'])} | {row['planned_s']} | {row['measured_s']} | {row.get('diff_ms', UNKNOWN)} | "
                  f"{row.get('diff_frames', UNKNOWN)} | {row.get('verdict', 'measured')} |")
        print(f"planned, not logged: {', '.join(res['not_logged']) or 'none'}")
        print(f"logged, not planned: {', '.join(res['not_planned']) or 'none'}")
        if res["duplicates"]:
            print(f"logged more than once (first kept): {', '.join(res['duplicates'])}")
        print(f"verdict: {res['verdict']}" + (f" (tolerance {args.tol_ms} ms, source: {args.tol_source})" if tol is not None else ""))
    return 1 if res["verdict"] == "fail" else 0


# ---------------------------------------------------------------- main

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="shotlist.py", description=__doc__.splitlines()[0])
    ap.add_argument("--version", action="version", version=VERSION)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check", help="schema, ids, frames, stage rules, cues, totals, FOV from lenses")
    p.add_argument("file")
    p.add_argument("--json", action="store_true")
    p.add_argument("--fov-tol-deg", type=float, help="judge lens vs fov_deg (needs --tol-source)")
    p.add_argument("--tol-source", help="where the tolerance comes from")
    p.set_defaults(fn=cmd_check)
    for name, fn, hlp in (("table", cmd_table, "Markdown shot list"), ("cues", cmd_cues, "Markdown cue sheet")):
        p = sub.add_parser(name, help=hlp)
        p.add_argument("file")
        p.set_defaults(fn=fn)
    p = sub.add_parser("blender", help="emit the Blender push script")
    p.add_argument("file")
    p.add_argument("--out", required=True)
    p.add_argument("--props-only", action="store_true",
                   help="only fps, fps_base and the scene properties (first animatic; lengths may be UNKNOWN)")
    p.set_defaults(fn=cmd_blender)
    p = sub.add_parser("blender-export", help="emit the Blender export script")
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_blender_export)
    p = sub.add_parser("diff", help="compare a Blender export with the shot list")
    p.add_argument("file")
    p.add_argument("blender_json")
    p.add_argument("--write", action="store_true", help="take shot lengths and cue `at` from Blender, revision + 1")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_diff)
    p = sub.add_parser("luau", help="emit the Roblox Luau data module")
    p.add_argument("file")
    p.add_argument("--out", required=True)
    p.set_defaults(fn=cmd_luau)
    p = sub.add_parser("log-diff", help="compare a Roblox playback log with the plan")
    p.add_argument("file")
    p.add_argument("log_json")
    p.add_argument("--tol-ms", type=str, help="tolerance in ms (needs --tol-source)")
    p.add_argument("--tol-source")
    p.add_argument("--early-ms", type=str,
                   help="one-sided window: at most this many ms early, --tol-ms late (the sync rule: one frame early)")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_log_diff)
    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    try:
        return args.fn(args)
    except ShotlistError as e:
        print(str(e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
