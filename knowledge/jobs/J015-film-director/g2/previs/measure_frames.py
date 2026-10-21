# Readability measurements from the shot cameras (no rendering): where each key object lands on screen,
# whether it stays inside the 16:9 frame and the 4:3 centre (the narrowest landscape screen at a fixed
# vertical FOV keeps the same height and loses width: 4:3 keeps the middle 75 % of a 16:9 frame), its
# screen height, and whether a ray from the camera to its centre hits it first (not hidden).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# blender -b <file.blend> --python measure_frames.py -- <out.json> [camera_override_for_D]
import json
import sys

import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector

a = sys.argv[sys.argv.index("--") + 1:]
out = a[0]
d_override = a[1] if len(a) > 1 else None
scene = bpy.context.scene
deps = bpy.context.evaluated_depsgraph_get()

GROUPS = {
    "explorer": lambda o: o.name.startswith("EXP_") and o.type == "MESH",
    "beacon": lambda o: o.name == "PROP_beacon",
    "guardian": lambda o: o.name.startswith("GUARD_") and o.type == "MESH" and o.name != "GUARD_plinth",
    "guardian_head": lambda o: o.name == "GUARD_head",
    "guardian_eyes": lambda o: o.name.startswith("GUARD_eye"),
    "strike_hand": lambda o: o.name == "GUARD_hand_L",
    "exit": lambda o: o.name == "SET_exit_daylight",
    "ripple": lambda o: o.name == "FX_ripple_1",
}
WANT = {"B": ["explorer", "beacon", "ripple", "guardian_head"], "C": ["explorer", "beacon"],
        "D": ["explorer", "beacon", "guardian", "guardian_head", "guardian_eyes"],
        "E": ["explorer", "beacon", "guardian", "guardian_eyes", "strike_hand", "exit"]}

markers = sorted((m.frame, m.name[5:], m.camera) for m in scene.timeline_markers if m.name.startswith("shot:"))
spans = []
for i, (f, sid, cam) in enumerate(markers):
    end = markers[i + 1][0] if i + 1 < len(markers) else scene.frame_end + 1
    if sid == "D" and d_override:
        cam = bpy.data.objects[d_override]
    spans.append((sid, f, end, cam))


def screen_box(cam, objs):
    xs, ys, zs = [], [], []
    for o in objs:
        if o.hide_render:
            continue
        ev = o.evaluated_get(deps)
        for c in ev.bound_box:
            p = world_to_camera_view(scene, cam, ev.matrix_world @ Vector(c))
            xs.append(p.x), ys.append(p.y), zs.append(p.z)
    if not xs or max(zs) <= 0:
        return None
    return min(xs), max(xs), min(ys), max(ys)


SKIP = ("GHOST_", "FX_")  # avatar-range ghosts (hidden in renders) and see-through effect proxies


def first_hit(origin, target):
    """First rendered, opaque object on the ray origin -> target (skips ghosts, effects, hidden objects)."""
    direction = (target - origin).normalized()
    start, left = origin.copy(), (target - origin).length + 0.5
    for _ in range(12):
        hit, loc, _n, _i, hobj, _m = scene.ray_cast(deps, start, direction, distance=left)
        if not hit or hobj is None:
            return None
        if hobj.name.startswith(SKIP) or hobj.hide_render:
            step = (loc - start).length + 0.01
            start, left = loc + direction * 0.01, left - step
            continue
        return hobj.name
    return None


def unhidden(cam, obj_names, objs):
    """True when the ray to at least one member's centre reaches a member first."""
    if not objs:
        return None
    origin = cam.matrix_world.translation
    names = []
    for o in objs:
        h = first_hit(origin, o.evaluated_get(deps).matrix_world.translation)
        names.append(h)
        if h in obj_names:
            return True, h
    return False, names[0]


res = {"file": bpy.data.filepath, "blender_version": bpy.app.version_string, "d_camera": d_override, "shots": {}}
for sid, f0, f1, cam in spans:
    rows = []
    frames = sorted(set(list(range(f0, f1, 3)) + [f1 - 1]))
    for f in frames:
        scene.frame_set(f)
        row = {"frame": f}
        for gname in WANT[sid]:
            objs = [o for o in scene.objects if GROUPS[gname](o)]
            box = screen_box(cam, objs)
            if box is None:
                row[gname] = None
                continue
            x0, x1, y0, y1 = box
            vis = unhidden(cam, {o.name for o in objs}, objs)
            row[gname] = {"x": [round(x0, 3), round(x1, 3)], "y": [round(y0, 3), round(y1, 3)],
                          "in_16x9": x1 > 0 and x0 < 1 and y1 > 0 and y0 < 1,
                          "inside_16x9": x0 >= 0 and x1 <= 1 and y0 >= 0 and y1 <= 1,
                          "inside_4x3": x0 >= 0.125 and x1 <= 0.875 and y0 >= 0 and y1 <= 1,
                          "screen_h": round(min(y1, 1) - max(y0, 0), 3),
                          "centre_ray_hits_it": vis[0] if vis else None, "first_hit": vis[1] if vis else None}
        rows.append(row)
    summ = {}
    for gname in WANT[sid]:
        vals = [r[gname] for r in rows if r.get(gname)]
        last = rows[-1].get(gname)
        summ[gname] = {"sampled": len(rows), "present": len(vals),
                       "in_16x9": sum(v["in_16x9"] for v in vals),
                       "inside_4x3": sum(v["inside_4x3"] for v in vals),
                       "unhidden": sum(1 for v in vals if v["centre_ray_hits_it"]),
                       "last_frame": last}
    res["shots"][sid] = {"camera": cam.name, "frames": [f0, f1 - 1], "summary": summ, "rows": rows}
    # camera speed: static cameras report 0
    scene.frame_set(f0)
    m0 = cam.matrix_world.copy()
    peak = 0.0
    for f in range(f0 + 1, f1):
        scene.frame_set(f)
        m1 = cam.matrix_world.copy()
        ang = m0.to_quaternion().rotation_difference(m1.to_quaternion()).angle
        peak = max(peak, ang)
        m0 = m1
    res["shots"][sid]["camera_peak_rotation_deg_per_frame"] = round(peak * 57.29578, 3)
with open(out, "w", encoding="utf-8") as fh:
    json.dump(res, fh, indent=1)
for sid, v in res["shots"].items():
    print("MEASURE", sid, v["camera"], json.dumps({k: {kk: vv for kk, vv in s.items() if kk != "last_frame"}
                                                 for k, s in v["summary"].items()}),
          "peak_rot_deg_per_frame", v["camera_peak_rotation_deg_per_frame"])
