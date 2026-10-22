"""Measure a sampled animation clip with numbers, so images are needed only where a number fails.

Kit tool: universal (Studio Kit). The pure checks use the Python standard library only (time is kept
exact with fractions.Fraction), so they run offline and in tests. The Blender layer (`sample_clip`)
imports `bpy` lazily and runs inside Blender (MCP or `blender -b ... --python`). Counterpart of the
rigger's tools/rig/rig_audit.py. Owner rule J005-D8: light checks by default; images only when a
number fails (animation-design references/review.md §5).

What each check means for an animator (every record: check, item, measured, unit, tolerance, result, where):
  length          Clip length = (frame_end - frame_start) / effective fps, exact (record "exact") and float.
                  Checked against a gameplay window [min_s, max_s] when one is given (never retime the
                  window to fit the clip, AP:986).
  loop_seam       Loop clips only. Position: how far each landmark jumps at the join (last vs first sample;
                  with loop_end_duplicates_start, the duplicate end vs the start). Velocity: the speed across
                  the join vs the mean of the in-clip speeds on each side; matching poses alone do not give
                  smooth motion (sets-and-states §4). Without a duplicate end the last-to-first step is one
                  real frame of motion, so its position number includes that frame's travel.
                  Landmarks are in world space: sample in-place clips (or root-relative landmarks), or a
                  travelling root reports its stride as a seam jump.
  contact_slide   Per declared contact (planted foot, grip): the largest horizontal travel of the landmark
                  from where it was at contact start (foot slide), and the largest vertical drift (sinking or
                  lifting). Up axis is a parameter (default "y", Roblox up).
  events          Clip markers vs timing-list events that name a marker: missing (FAIL: the timing list is
                  the contract), extra (reported, MEASURED), and the time offset in seconds and frames.
  rom             Per manifest control present in the samples: min/max reached vs the manifest min/max;
                  measured = the over-range amount in the manifest's units (0 = inside the range).
  curves          With --curves --root <landmark> [--twin L,R]: hang time, gravity spacing, arcs (longest straight
                  run), overshoot, twinning and the opening hold, all MEASURED (J018 G3-P8).
  pops            Per landmark: the largest frame-to-frame acceleration divided by the clip's median
                  acceleration (all landmarks, all inner frames). A report for finding hitches.

Where tolerances come from: the rig sheet, the game profile, the motion spec or the owner, passed in a
tolerances JSON file. This tool has no thresholds of its own. A check without its tolerance is MEASURED,
never PASS or FAIL (rig_audit.judge; animation-design SKILL.md §7: never invent a foot-slide tolerance).
Only structural faults (a timing-list marker missing from the clip) fail without a tolerance.

Samples JSON:
  {"clip": str, "fps": [num, den], "frame_start": int, "frame_end": int, "loop": bool,
   "loop_end_duplicates_start": bool, "units": "studs",
   "landmarks": {name: [[x, y, z] per frame]}, "controls": {control_id: [value per frame]},
   "contacts": [{"landmark": str, "start": frame, "end": frame, "kind": "planted" | "grip"}],
   "markers": [{"name": str, "frame": number}]}
  One sample per frame, frame_start..frame_end inclusive. Frames in contacts and markers are clip frames.
Tolerances JSON (every key optional): {"loop_seam_position", "loop_seam_velocity", "contact_slide",
  "contact_drift_vertical", "event_offset_frames", "rom_over", "pop_ratio": float, "window": [min_s, max_s]}
Timing JSON: the JSON copy of templates/anim/timing-list.md, {"events": [...]} or a list; per row an id
  ("event_id" | "id" | "event"), a marker ("marker" | "marker_name"; empty, "-" or "—" = no marker) and a
  time ("time_s" | "time" | "seconds", number or "a/b") or a clip frame ("frame" | "source_frame").
Manifest JSON: a rig control manifest ({"controls": [{"control_id", "pose_bone", "channel", "units",
  "min", "max"}]}); controls without numeric min/max are skipped.

Usage:
  python tools/anim/clip_check.py samples.json [--timing t.json] [--manifest m.json] [--tol tol.json] [--out report.json]
  Prints one line per FAIL and the summary. Exit 0 no FAIL, 1 any FAIL, 2 bad input.
Inside Blender:
  import sys; sys.path.append("<kit>/tools/anim"); import clip_check
  s = clip_check.sample_clip(arm, {"foot_L": ("Foot_L", "tail")}, manifest["controls"], 1, 31, contacts, units="studs")
"""

from __future__ import annotations

import json
import math
import statistics
import sys
from fractions import Fraction
from pathlib import Path

TOLERANCE_KEYS = {"loop_seam_position", "loop_seam_velocity", "contact_slide", "contact_drift_vertical",
                  "event_offset_frames", "rom_over", "pop_ratio", "window"}
AXES = {"x": 0, "y": 1, "z": 2}
NO_MARKER = {"", "-", "—", "–"}


# ---------------------------------------------------------------- pure checks (no bpy)

def judge(measured: float | None, tolerance: float | None) -> str:
    """PASS / FAIL only against a given tolerance; else MEASURED (same rule as rig_audit.judge)."""
    if tolerance is None or measured is None:
        return "MEASURED"
    return "PASS" if measured <= tolerance else "FAIL"


def _rec(check, item, measured, unit, tolerance, result, frames, **extra) -> dict:
    return {"check": check, "item": item, "measured": measured, "unit": unit, "tolerance": tolerance,
            "result": result, "where": {"frames": sorted(set(frames)), **extra}}


def fps_of(samples: dict) -> Fraction:
    num, den = samples["fps"]
    return Fraction(num, den)


def frame_count(samples: dict) -> int:
    return samples["frame_end"] - samples["frame_start"] + 1


def validate(samples: dict, up: str = "y") -> None:
    """Raise ValueError on input the checks cannot measure honestly."""
    for key in ("clip", "fps", "frame_start", "frame_end"):
        if key not in samples:
            raise ValueError(f"samples: missing {key!r}")
    fps = samples["fps"]
    if not (isinstance(fps, list) and len(fps) == 2 and all(isinstance(v, int) and v > 0 for v in fps)):
        raise ValueError("samples.fps must be [num, den], positive integers")
    if not all(isinstance(samples[k], int) for k in ("frame_start", "frame_end")):
        raise ValueError("frame_start and frame_end must be integers")
    if samples["frame_end"] <= samples["frame_start"]:
        raise ValueError("frame_end must be after frame_start")
    if up not in AXES:
        raise ValueError(f"up axis must be one of {sorted(AXES)}")
    n = frame_count(samples)
    for name, seq in samples.get("landmarks", {}).items():
        if len(seq) != n:
            raise ValueError(f"landmark {name!r}: {len(seq)} samples, expected {n} (one per frame)")
        for p in seq:
            if len(p) != 3 or not all(isinstance(c, (int, float)) and math.isfinite(c) for c in p):
                raise ValueError(f"landmark {name!r}: every sample must be 3 finite numbers")
    for cid, seq in samples.get("controls", {}).items():
        if len(seq) != n:
            raise ValueError(f"control {cid!r}: {len(seq)} samples, expected {n}")
        if not all(isinstance(v, (int, float)) and math.isfinite(v) for v in seq):
            raise ValueError(f"control {cid!r}: values must be finite numbers")
    lo, hi = samples["frame_start"], samples["frame_end"]
    for c in samples.get("contacts", []):
        if c.get("landmark") not in samples.get("landmarks", {}):
            raise ValueError(f"contact names unknown landmark {c.get('landmark')!r}")
        if not (lo <= c["start"] <= c["end"] <= hi):
            raise ValueError(f"contact {c['landmark']} {c['start']}-{c['end']} is outside frames {lo}-{hi}")
    for m in samples.get("markers", []):
        if "name" not in m or not isinstance(m.get("frame"), (int, float)):
            raise ValueError("every marker needs a name and a numeric frame")


def validate_tolerances(tol: dict | None) -> dict:
    tol = tol or {}
    unknown = set(tol) - TOLERANCE_KEYS
    if unknown:
        raise ValueError(f"unknown tolerance keys: {sorted(unknown)}")
    w = tol.get("window")
    if w is not None and not (isinstance(w, list) and len(w) == 2 and w[0] <= w[1]):
        raise ValueError("tolerance window must be [min_s, max_s]")
    return tol


def _sub(a, b):
    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def _norm(v) -> float:
    return math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])


def check_length(samples: dict, window: list | None = None) -> dict:
    """Clip length in seconds, exact. PASS / FAIL only against a given [min_s, max_s] window."""
    exact = Fraction(samples["frame_end"] - samples["frame_start"]) / fps_of(samples)
    seconds = float(exact)
    if window is None:
        result = "MEASURED"
    else:
        result = "PASS" if Fraction(str(window[0])) <= exact <= Fraction(str(window[1])) else "FAIL"
    return _rec("length", samples["clip"], seconds, "s", window, result,
                [samples["frame_start"], samples["frame_end"]], exact=str(exact),
                intervals=samples["frame_end"] - samples["frame_start"])


def check_loop_seam(samples: dict, tol_pos: float | None = None, tol_vel: float | None = None) -> list[dict]:
    """Position jump and velocity mismatch at the loop join, per landmark. [] for non-loop clips."""
    if not samples.get("loop"):
        return []
    fps = float(fps_of(samples))
    f0, f1 = samples["frame_start"], samples["frame_end"]
    dup = bool(samples.get("loop_end_duplicates_start"))
    unit = samples.get("units", "units")
    out = []
    for name, p in samples.get("landmarks", {}).items():
        n = len(p)
        last = n - 2 if dup else n - 1  # the last distinct sample before the join
        if last < 2:
            raise ValueError(f"loop_seam: clip too short to measure velocity for {name!r}")
        jump = _norm(_sub(p[n - 1], p[0]))
        v_seam = [c * fps for c in _sub(p[0], p[last])]
        v_before = [c * fps for c in _sub(p[last], p[last - 1])]
        v_after = [c * fps for c in _sub(p[1], p[0])]
        mismatch = _norm(_sub(v_seam, [(a + b) / 2 for a, b in zip(v_before, v_after)]))
        # The same measure on every inner frame: curved motion gives a non-zero value even without a seam,
        # so this baseline shows what "smooth" measures for this landmark.
        baseline = max((_norm([(p[j + 1][k] - 3 * p[j][k] + 3 * p[j - 1][k] - p[j - 2][k]) * fps / 2
                               for k in range(3)]) for j in range(2, last)), default=0.0)
        out.append(_rec("loop_seam_position", name, jump, unit, tol_pos, judge(jump, tol_pos), [f1, f0],
                        duplicate_end=dup))
        out.append(_rec("loop_seam_velocity", name, mismatch, f"{unit}/s", tol_vel, judge(mismatch, tol_vel),
                        [f0 + last, f0, f0 + 1], seam_speed=_norm(v_seam), inner_frame_max=baseline))
    return out


def check_contact_slide(samples: dict, tol_slide: float | None = None, tol_vertical: float | None = None,
                        up: str = "y") -> list[dict]:
    """Per declared contact: max horizontal travel and max vertical drift from the contact-start position."""
    ui = AXES[up]
    hi = [i for i in range(3) if i != ui]
    f0 = samples["frame_start"]
    unit = samples.get("units", "units")
    out = []
    for c in samples.get("contacts", []):
        p = samples["landmarks"][c["landmark"]]
        base = p[c["start"] - f0]
        best_h, fh, best_v, fv = 0.0, c["start"], 0.0, c["start"]
        for f in range(c["start"], c["end"] + 1):
            d = _sub(p[f - f0], base)
            h = math.hypot(d[hi[0]], d[hi[1]])
            v = abs(d[ui])
            if h > best_h:
                best_h, fh = h, f
            if v > best_v:
                best_v, fv = v, f
        item = f"{c['landmark']}@{c['start']}-{c['end']}"
        kind = c.get("kind", "planted")
        out.append(_rec("contact_slide", item, best_h, unit, tol_slide, judge(best_h, tol_slide),
                        [c["start"], fh], kind=kind))
        out.append(_rec("contact_drift_vertical", item, best_v, unit, tol_vertical, judge(best_v, tol_vertical),
                        [c["start"], fv], kind=kind))
    return out


def _first(row: dict, keys):
    for k in keys:
        if k in row and row[k] is not None:
            return row[k]
    return None


def _exact(v) -> Fraction:
    return Fraction(v) if isinstance(v, (int, str)) else Fraction(str(v))


def timing_events(timing) -> list[dict]:
    """Timing-list rows that name a marker: [{"event", "marker", "time": Fraction | None, "frame"}]."""
    rows = timing.get("events", []) if isinstance(timing, dict) else (timing or [])
    out = []
    for row in rows:
        marker = _first(row, ("marker", "marker_name"))
        if marker is None or str(marker).strip() in NO_MARKER:
            continue
        t = _first(row, ("time_s", "time", "seconds"))
        if isinstance(t, str) and t.strip() in NO_MARKER:
            t = None
        out.append({"event": _first(row, ("event_id", "id", "event")) or str(marker), "marker": str(marker),
                    "time": None if t is None else _exact(t), "frame": _first(row, ("frame", "source_frame"))})
    return out


def check_events(samples: dict, timing, tol_frames: float | None = None) -> list[dict]:
    """Markers vs timing-list events (matched by marker name): missing, extra, offset in s and frames."""
    fps = fps_of(samples)
    f0 = samples["frame_start"]
    markers: dict[str, list[float]] = {}
    for m in samples.get("markers", []):
        markers.setdefault(m["name"], []).append(m["frame"])
    expected = timing_events(timing)
    out, used = [], set()
    for ev in expected:
        name = ev["marker"]
        if ev["time"] is not None:
            want = ev["time"]
        elif ev["frame"] is not None:
            want = (_exact(ev["frame"]) - f0) / fps
        else:
            raise ValueError(f"timing event {ev['event']!r} names marker {name!r} but has no time or frame")
        want_frame = f0 + want * fps
        if name not in markers:
            out.append(_rec("events", ev["event"], None, "frames", tol_frames, "FAIL", [round(want_frame)],
                            problem="missing", marker=name, expected_s=float(want)))
            continue
        used.add(name)
        got_frame = min(markers[name], key=lambda fr: abs(_exact(fr) - want_frame))
        got = (_exact(got_frame) - f0) / fps
        off_s = got - want
        off_f = off_s * fps
        out.append(_rec("events", ev["event"], abs(float(off_f)), "frames", tol_frames,
                        judge(abs(float(off_f)), tol_frames), [round(want_frame), round(got_frame)],
                        marker=name, offset_s=float(off_s), offset_frames=float(off_f),
                        expected_s=float(want), marker_s=float(got)))
        for extra in markers[name]:
            if extra != got_frame:
                out.append(_rec("events", f"{name}@{extra}", None, "frames", None, "MEASURED", [round(extra)],
                                problem="extra (duplicate marker name)", marker=name))
    for name, frames in markers.items():
        if name in used:
            continue
        for fr in frames:
            out.append(_rec("events", f"{name}@{fr}", None, "frames", None, "MEASURED", [round(fr)],
                            problem="extra (not in the timing list)", marker=name))
    return out


def check_rom(samples: dict, manifest, tol_over: float | None = None) -> list[dict]:
    """Per manifest control present in samples: range reached vs manifest min/max; measured = over-range."""
    controls = manifest.get("controls", []) if isinstance(manifest, dict) else (manifest or [])
    f0 = samples["frame_start"]
    have = samples.get("controls", {})
    out = []
    for c in controls:
        cid = c.get("control_id")
        lo, hi = c.get("min"), c.get("max")
        if cid not in have or not isinstance(lo, (int, float)) or not isinstance(hi, (int, float)):
            continue
        vals = have[cid]
        vmin, vmax = min(vals), max(vals)
        over_each = [max(0.0, v - hi, lo - v) for v in vals]
        over = max(over_each)
        frames = [f0 + i for i, o in enumerate(over_each) if o > 0 and o == over] if over > 0 else []
        out.append(_rec("rom", cid, over, c.get("units", ""), tol_over, judge(over, tol_over), frames,
                        reached=[vmin, vmax], manifest=[lo, hi],
                        over_frames=[f0 + i for i, o in enumerate(over_each) if o > 0][:50]))
    return out


def check_pops(samples: dict, tol_ratio: float | None = None) -> list[dict]:
    """Per landmark: max frame-to-frame acceleration / median acceleration of the whole clip."""
    fps = float(fps_of(samples))
    f0 = samples["frame_start"]
    unit = samples.get("units", "units")
    acc: dict[str, list[float]] = {}
    for name, p in samples.get("landmarks", {}).items():
        acc[name] = [_norm([(p[i + 1][k] - 2 * p[i][k] + p[i - 1][k]) * fps * fps for k in range(3)])
                     for i in range(1, len(p) - 1)]
    pool = [a for seq in acc.values() for a in seq]
    if not pool:
        return []
    median = statistics.median(pool)
    out = []
    for name, seq in acc.items():
        i = max(range(len(seq)), key=seq.__getitem__)
        peak = seq[i]
        if median > 0:
            ratio, note = peak / median, None
        else:
            ratio, note = (0.0, None) if peak == 0 else (None, "median acceleration is 0; ratio undefined")
        rec = _rec("pops", name, ratio, "x median", tol_ratio, judge(ratio, tol_ratio), [f0 + i, f0 + i + 1],
                   peak_acceleration=peak, median_acceleration=median, acceleration_unit=f"{unit}/s^2")
        if note:
            rec["where"]["note"] = note
        out.append(rec)
    return out


# ---------------------------------------------------------------- curve lines (J018 G3-P8; always MEASURED)
# The curve lines of animation-design references/review.md section 8b that animators computed by hand from the
# samples file. Every record is MEASURED: the brief or the rig sheet gives a tolerance, this tool gives none.

def check_curves(samples: dict, root: str, up: str = "y", twins: list[tuple[str, str]] | None = None,
                 hold_frames: int = 4) -> list[dict]:
    lm = samples.get("landmarks", {})
    if root not in lm:
        raise ValueError(f"--root {root!r} is not a landmark in the samples")
    f0, ax = samples["frame_start"], AXES[up]
    unit = samples.get("units", "units")
    p = lm[root]
    h = [q[ax] for q in p]
    out = []
    # hang time (S-09) and gravity spacing (S-07) on the root's height
    apex = max(range(len(h)), key=h.__getitem__)
    base = min(h[0], h[-1])
    rise = next((i - 1 for i in range(1, apex + 1) if h[i] > base + 1e-6), apex)  # the last frame on the ground
    land = next((i for i in range(apex, len(h)) if h[i] <= base + 1e-6), len(h) - 1)
    out.append(_rec("hang_time", root, {"launch_to_apex_frames": apex - rise, "apex_to_landing_frames": land - apex},
                    "frames", None, "MEASURED", [f0 + rise, f0 + apex, f0 + land]))
    step = [_norm([p[i + 1][k] - p[i][k] for k in range(3)]) for i in range(len(p) - 1)]
    near_apex = [step[i] for i in range(max(0, apex - 2), min(len(step), apex + 2))]
    near_ground = step[max(0, rise - 1):rise + 2] + step[max(0, land - 3):land]
    if near_apex and near_ground:
        a_, g_ = statistics.mean(near_apex), statistics.mean(near_ground)
        out.append(_rec("gravity_spacing", root, None if g_ == 0 else a_ / g_, "apex step / ground step", None, "MEASURED",
                        [f0 + apex], apex_step=a_, ground_step=g_, step_unit=f"{unit}/frame",
                        note="well under 1 = slow at the top, fast near the ground (gravity); about 1 = even spacing"))
    # arcs (S-08): per landmark, the longest run of frames that stays on the straight chord between its ends
    for name, q in lm.items():
        path_len = sum(_norm([q[i + 1][k] - q[i][k] for k in range(3)]) for i in range(len(q) - 1))
        tol = max(path_len * 0.01, 1e-6)
        best = (0, 0)
        i = 0
        while i < len(q) - 2:
            j = i + 2
            while j < len(q):
                a, b = q[i], q[j]
                d = [b[k] - a[k] for k in range(3)]
                dl = _norm(d)
                if dl == 0:
                    break
                ok = all(_norm([(q[m][1] - a[1]) * d[2] - (q[m][2] - a[2]) * d[1], (q[m][2] - a[2]) * d[0] - (q[m][0] - a[0]) * d[2],
                                (q[m][0] - a[0]) * d[1] - (q[m][1] - a[1]) * d[0]]) / dl <= tol for m in range(i + 1, j))
                if not ok:
                    break
                j += 1
            if j - 1 - i > best[1] - best[0]:
                best = (i, j - 1)
            i += 1
        if path_len > 0:
            out.append(_rec("arc_straight_run", name, best[1] - best[0], "frames", None, "MEASURED",
                            [f0 + best[0], f0 + best[1]], note="frames moving on a straight line (a long run = a missing arc)"))
    # overshoot (S-12): per control, crossings of the final value before settling and the largest excess
    for cid, seq in samples.get("controls", {}).items():
        if len(seq) < 3:
            continue
        fin, start = seq[-1], seq[0]
        sign = 1 if fin >= start else -1
        crossings = sum(1 for i in range(len(seq) - 1) if (seq[i] - fin) * (seq[i + 1] - fin) < 0)
        excess = max(0.0, max(sign * (v - fin) for v in seq))
        out.append(_rec("overshoot", cid, {"crossings": crossings, "largest_excess": excess}, "control units", None,
                        "MEASURED", [f0 + max(range(len(seq)), key=lambda i: sign * (seq[i] - fin))]))
    # twinning (S-14): left and right turning points on the same frames, and their mirrored difference
    for left, right in twins or []:
        ctl = samples.get("controls", {})
        if left not in ctl or right not in ctl:
            raise ValueError(f"--twin {left},{right}: both must be controls in the samples")
        L, R = ctl[left], ctl[right]
        turns = lambda s: {i for i in range(1, len(s) - 1) if (s[i] - s[i - 1]) * (s[i + 1] - s[i]) < 0}
        tl, tr = turns(L), turns(R)
        shared = len(tl & tr) / max(len(tl | tr), 1)
        mirror = statistics.mean(abs(a + b) for a, b in zip(L, R))
        out.append(_rec("twinning", f"{left}|{right}", round(shared, 3), "share of turning frames in common", None,
                        "MEASURED", [f0 + i for i in sorted(tl & tr)], mean_mirrored_difference=mirror,
                        note="near 1 with a small mirrored difference = twinned limbs (the same pose on both sides)"))
    # opening hold (B-10): the largest pose change over the first frames
    n = min(hold_frames, len(p) - 1)
    if n > 0:
        moves = {name: max(_norm([q[i][k] - q[0][k] for k in range(3)]) for i in range(1, n + 1)) for name, q in lm.items()}
        worst = max(moves, key=moves.get)
        out.append(_rec("opening_hold", worst, moves[worst], unit, None, "MEASURED", [f0, f0 + n],
                        frames_checked=n, note="the largest landmark move over the first frames (a held start reads near 0)"))
    return out


def run_all(samples: dict, timing=None, manifest=None, tolerances: dict | None = None, up: str = "y") -> dict:
    """Every check. Summary counts, failing records, and the frames worth rendering."""
    validate(samples, up)
    tol = validate_tolerances(tolerances)
    results = [check_length(samples, tol.get("window"))]
    results += check_loop_seam(samples, tol.get("loop_seam_position"), tol.get("loop_seam_velocity"))
    results += check_contact_slide(samples, tol.get("contact_slide"), tol.get("contact_drift_vertical"), up)
    if timing is not None:
        results += check_events(samples, timing, tol.get("event_offset_frames"))
    if manifest is not None:
        results += check_rom(samples, manifest, tol.get("rom_over"))
    results += check_pops(samples, tol.get("pop_ratio"))
    summary = {k: sum(1 for r in results if r["result"] == k) for k in ("PASS", "FAIL", "MEASURED")}
    failing = [r for r in results if r["result"] == "FAIL"]
    render = sorted({f for r in failing for f in r["where"]["frames"]})
    return {"clip": samples["clip"], "fps": samples["fps"], "up": up,
            "verdict": "FAIL" if failing else ("MEASURED" if summary["MEASURED"] else "PASS"),
            "summary": summary, "failing": failing, "frames_to_render": render, "results": results}


# ---------------------------------------------------------------- Blender layer (bpy, lazy)

def scene_fps(scene) -> list[int]:
    """Effective fps as [num, den] from render.fps / render.fps_base (fps_base is a float, e.g. 1.001)."""
    f = Fraction(scene.render.fps) / Fraction(scene.render.fps_base).limit_denominator(10_000)
    return [f.numerator, f.denominator]


def _channel_value(pb, channel: str, units: str) -> float:
    """'rotation_euler.y' -> pb.rotation_euler[1]; radians become degrees when the manifest unit is deg.

    Quaternion components follow Blender's order (w, x, y, z): 'rotation_quaternion.w' is index 0. A degree unit on a
    quaternion channel is refused: a quaternion component is not an angle (J018 rigger review F2: a 30 degree tilt
    against +/-15 degrees read 0 and passed).
    """
    attr, _, comp = channel.partition(".")
    v = getattr(pb, attr)
    if attr.startswith("rotation_quaternion") and str(units).startswith("deg"):
        raise ValueError(f"{channel}: degrees on a quaternion channel; give the range in quaternion units "
                         "or key the control in Euler")
    if comp:
        order = "wxyz" if attr.startswith("rotation_quaternion") else "xyzw"
        v = v[order.index(comp)] if comp in order else v[int(comp)]
    v = float(v)
    return math.degrees(v) if attr.startswith("rotation_euler") and str(units).startswith("deg") else v


def sample_clip(arm_obj, landmarks: dict, controls: list[dict] | None, frame_start: int, frame_end: int,
                contacts: list[dict] | None = None, markers_from_action: bool = True, *, clip: str | None = None,
                loop: bool = False, loop_end_duplicates_start: bool = False,
                units: str = "blender_units") -> dict:
    """Sample world-space landmarks and manifest controls per frame into a samples dict.

    landmarks: {name: (pose_bone_name, "head" | "tail")}; positions are arm_obj.matrix_world @ pose_bone.head/tail.
    controls: manifest control records; those with a pose_bone on this armature and a channel are read.
    markers_from_action=True reads the active Action's pose markers (Action > Pose Markers); False reads the
    scene timeline markers. units labels the positions (pass the rig manifest's unit, e.g. "studs").
    Positions keep Blender's world axes (Z up): run the checks with up="z" (CLI --up z).
    Euler channels are radians in Blender and are converted to degrees when the manifest unit is deg.
    The scene frame is restored afterwards. Checked on Blender 5.1.2 headless (generated armature).
    """
    scene = arm_obj.users_scene[0] if arm_obj.users_scene else None
    if scene is None:
        import bpy  # noqa: PLC0415
        scene = bpy.context.scene
    saved = (scene.frame_current, scene.frame_subframe)
    lm = {name: [] for name in landmarks}
    readable = [c for c in (controls or []) if c.get("channel") and c.get("pose_bone") in arm_obj.pose.bones]
    cv = {c["control_id"]: [] for c in readable}
    try:
        for f in range(frame_start, frame_end + 1):
            scene.frame_set(f)
            mw = arm_obj.matrix_world
            for name, (bone, end) in landmarks.items():
                pb = arm_obj.pose.bones[bone]
                lm[name].append([float(c) for c in mw @ (pb.tail if end == "tail" else pb.head)])
            for c in readable:
                cv[c["control_id"]].append(_channel_value(arm_obj.pose.bones[c["pose_bone"]], c["channel"],
                                                          c.get("units", "")))
    finally:
        scene.frame_set(saved[0], subframe=saved[1])
    if markers_from_action:
        ad = arm_obj.animation_data
        src = ad.action.pose_markers if ad and ad.action else []
    else:
        src = scene.timeline_markers
    action_name = arm_obj.animation_data.action.name if arm_obj.animation_data and arm_obj.animation_data.action else None
    return {
        "clip": clip or action_name or arm_obj.name,
        "fps": scene_fps(scene),
        "frame_start": frame_start,
        "frame_end": frame_end,
        "loop": loop,
        "loop_end_duplicates_start": loop_end_duplicates_start,
        "units": units,
        "landmarks": lm,
        "controls": cv,
        "contacts": list(contacts or []),
        "markers": [{"name": m.name, "frame": m.frame} for m in src],
        "markers_source": "action.pose_markers" if markers_from_action else "scene.timeline_markers",
        "controls_skipped": [c.get("control_id") for c in (controls or []) if c not in readable],
    }


# ---------------------------------------------------------------- CLI (pure)

def _load(path: str | None):
    if path is None:
        return None
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main(argv: list[str]) -> int:
    import argparse  # noqa: PLC0415

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("samples")
    p.add_argument("--timing", help="timing-list JSON copy")
    p.add_argument("--manifest", help="rig control manifest JSON")
    p.add_argument("--tol", help="tolerances JSON (from the rig sheet / game profile / owner)")
    p.add_argument("--up", default="y", choices=sorted(AXES))
    p.add_argument("--out", help="write the full report JSON here")
    p.add_argument("--curves", action="store_true", help="also the curve lines (hang time, gravity spacing, arcs, overshoot, "
                   "twinning, opening hold), all MEASURED; needs --root")
    p.add_argument("--root", help="the root (centre of mass) landmark for --curves")
    p.add_argument("--twin", action="append", default=[], metavar="LEFT,RIGHT", help="a left and right control pair for twinning")
    args = p.parse_args(argv)
    try:
        report = run_all(_load(args.samples), _load(args.timing), _load(args.manifest), _load(args.tol), args.up)
        if args.curves:
            if not args.root:
                raise ValueError("--curves needs --root")
            extra = check_curves(_load(args.samples), args.root, args.up, [tuple(t.split(",", 1)) for t in args.twin])
            report["results"] += extra
            report["summary"]["MEASURED"] += len(extra)
            if report["verdict"] == "PASS":
                report["verdict"] = "MEASURED"
    except (OSError, ValueError, KeyError, TypeError, IndexError) as e:
        print(f"BAD INPUT: {type(e).__name__}: {e}")
        return 2
    for r in report["failing"]:
        print(f"FAIL {r['check']} {r['item']}: measured {r['measured']} {r['unit']} "
              f"(tolerance {r['tolerance']}) frames {r['where']['frames']}")
    s = report["summary"]
    print(f"RESULT: {report['verdict']} PASS={s['PASS']} FAIL={s['FAIL']} MEASURED={s['MEASURED']}"
          f" render={report['frames_to_render']}" + (f" -> {args.out}" if args.out else ""))
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 1 if report["failing"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]))
