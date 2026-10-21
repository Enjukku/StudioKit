"""Measure a model against the Roblox mesh limits and its asset record, as numbers, before anyone looks at images.

Kit tool: universal (Studio Kit). Pure checks use the Python standard library only, so they run offline and
in tests. Mesh counting is reused from tools/rig/rig_audit.py (audit_mesh, count_parts, judge), not copied.
The Blender layer (`collect`, `audit_scene`, `main`) imports `bpy` lazily and runs inside Blender:
`blender -b <file.blend> --python tools/model/model_audit.py -- <args>`, or from the Blender MCP with
`import model_audit; model_audit.audit_scene("Export")` after adding tools/model to sys.path.

Hard platform limits, per mesh (PASS/FAIL without a tolerance), mirror root knowledge/external/roblox-creator-docs/:
  - max 20,000 triangles per mesh       art/modeling/specifications.md:34 (MR01)
  - watertight: 0 non-manifold edges    art/modeling/specifications.md:35 (rule as in rig_audit.audit_mesh)
  - one material per mesh               art/modeling/texture-specifications.md:30 (MR12)
  - one UV set                          art/modeling/texture-specifications.md:128 (MR12)
  - UVs inside 0-1                      art/modeling/texture-specifications.md:129 (MR12)
Review-list rules (.agents/skills/modeling-design/references/review.md §2: "no floating ... parts", "no faces fully
inside other faces", "0 flipped faces where a closed surface is required", "no helpers, dummies ... or hidden objects
exported"). Detection uses geometric epsilons only, so any part found is FAIL:
  - floating: a surface part (face island) whose surface distance to every other part and to the ground plane is
    larger than --contact-tol. Parts hidden inside a closed part are reported as hidden, not floating.
  - hidden: every vertex of a part is inside one closed part (ray parity, 3 rays, majority vote).
  - orientation: a closed part with negative signed volume (inverted), or an edge two faces walk in the same
    direction (one face flipped against its neighbour). Volume of a negative-scale object is taken in its own
    winding, as Blender displays it; such objects are listed as `mirrored`.
  - export: hidden objects, cameras, lights, light probes, speakers, and empties not named in --expect.
  - names: object names vs --expect (missing / extra). MEASURED without --expect.
Measurements (PASS/FAIL only with a caller number, else MEASURED; never an invented threshold):
  - total evaluated triangles of all meshes vs --budget (whole model: owner J007-D5, budgets.md §3)
  - bounding-box size in studs vs --size with --size-tol (1 Blender unit = 1 stud: MR36, physics/units.md:38-39)
Data only (no verdict): connected parts, open edges, zero-area faces, texture image sizes (the docs give 1024 at
texture-specifications.md:130 and 4096 elsewhere, MR08/MR09: no single limit to test).
Overall verdict = worst row (FAIL > MEASURED > PASS).

Geometric epsilons (not tolerances; each absorbs float rounding only):
  CONTACT_TOL 0.01 stud  float32 spacing is <= 0.002 stud up to 16,384 studs (as tools/env/scene_audit.py EPS)
  UV_EPS      1e-6       float32 spacing near 1.0 is about 1.2e-7
  ZERO_AREA   1e-8 stud² a face smaller than 0.0001 x 0.0001 stud

Method limits: contact is the true surface distance (vertex-triangle, edge-edge, edge-through-triangle) but parts
that touch only each other and not the ground are not floating (see `contact_groups`); hidden tests vertices only,
so a part whose edges leave a non-convex container between inside vertices is still called hidden; volume sign is
only defined for closed parts; texture sizes read only Image Texture nodes in the material node trees.

Usage (inside Blender):
  blender -b model.blend --python tools/model/model_audit.py -- --collection Export \
      --out content/models/<id>/tests/audit.json --budget 7000 --size 4,2,5 --size-tol 0.1 \
      --expect Body,Head,Hat --contact-tol 0.01 --ground 0
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "rig"))
import rig_audit as ra  # noqa: E402  (audit_mesh, count_parts, judge)

MAX_TRIANGLES = ra.MAX_TRIANGLES
MAX_MATERIALS = 1
MAX_UV_SETS = 1
CONTACT_TOL = 0.01
UV_EPS = 1e-6
ZERO_AREA = 1e-8
HELPER_TYPES = ("CAMERA", "LIGHT", "LIGHT_PROBE", "SPEAKER")
ORDER = ("FAIL", "MEASURED", "PASS")
CAP = 50  # longest list written per check
RAYS = ((0.9033, 0.3613, 0.2316), (-0.3061, 0.8742, 0.3767), (0.1951, -0.4217, 0.8854))


# ---------------------------------------------------------------- vector helpers

def _sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def _dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def _cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def _add_scaled(a, d, t):
    return (a[0] + d[0] * t, a[1] + d[1] * t, a[2] + d[2] * t)


def _clamp01(x):
    return 0.0 if x < 0.0 else 1.0 if x > 1.0 else x


def point_triangle_distance(p, tri) -> float:
    """Closest distance from point p to triangle (a, b, c) (Ericson, Real-Time Collision Detection 5.1.5)."""
    a, b, c = tri
    ab, ac, ap = _sub(b, a), _sub(c, a), _sub(p, a)
    d1, d2 = _dot(ab, ap), _dot(ac, ap)
    if d1 <= 0 and d2 <= 0:
        return math.dist(p, a)
    bp = _sub(p, b)
    d3, d4 = _dot(ab, bp), _dot(ac, bp)
    if d3 >= 0 and d4 <= d3:
        return math.dist(p, b)
    vc = d1 * d4 - d3 * d2
    if vc <= 0 and d1 >= 0 and d3 <= 0:
        return math.dist(p, _add_scaled(a, ab, d1 / (d1 - d3)))
    cp = _sub(p, c)
    d5, d6 = _dot(ab, cp), _dot(ac, cp)
    if d6 >= 0 and d5 <= d6:
        return math.dist(p, c)
    vb = d5 * d2 - d1 * d6
    if vb <= 0 and d2 >= 0 and d6 <= 0:
        return math.dist(p, _add_scaled(a, ac, d2 / (d2 - d6)))
    va = d3 * d6 - d5 * d4
    if va <= 0 and (d4 - d3) >= 0 and (d5 - d6) >= 0:
        return math.dist(p, _add_scaled(b, _sub(c, b), (d4 - d3) / ((d4 - d3) + (d5 - d6))))
    den = va + vb + vc
    if den == 0:  # degenerate triangle: nearest of its edges
        return min(segment_distance(p, p, e0, e1) for e0, e1 in ((a, b), (b, c), (c, a)))
    v, w = vb / den, vc / den
    return math.dist(p, (a[0] + ab[0] * v + ac[0] * w, a[1] + ab[1] * v + ac[1] * w, a[2] + ab[2] * v + ac[2] * w))


def segment_distance(p1, q1, p2, q2) -> float:
    """Closest distance between segments p1q1 and p2q2 (Ericson 5.1.9)."""
    d1, d2, r = _sub(q1, p1), _sub(q2, p2), _sub(p1, p2)
    a, e, f = _dot(d1, d1), _dot(d2, d2), _dot(d2, r)
    if a <= 1e-18 and e <= 1e-18:
        return math.dist(p1, p2)
    if a <= 1e-18:
        s, t = 0.0, _clamp01(f / e)
    else:
        c = _dot(d1, r)
        if e <= 1e-18:
            s, t = _clamp01(-c / a), 0.0
        else:
            b = _dot(d1, d2)
            den = a * e - b * b
            s = _clamp01((b * f - c * e) / den) if den > 1e-18 else 0.0
            t = (b * s + f) / e
            if t < 0:
                s, t = _clamp01(-c / a), 0.0
            elif t > 1:
                s, t = _clamp01((b - c) / a), 1.0
    return math.dist(_add_scaled(p1, d1, s), _add_scaled(p2, d2, t))


def ray_triangle(origin, direction, tri) -> float | None:
    """Möller-Trumbore. Distance along the ray to the hit, or None."""
    a, b, c = tri
    e1, e2 = _sub(b, a), _sub(c, a)
    h = _cross(direction, e2)
    det = _dot(e1, h)
    if abs(det) < 1e-15:
        return None
    inv = 1.0 / det
    s = _sub(origin, a)
    u = inv * _dot(s, h)
    if u < 0 or u > 1:
        return None
    q = _cross(s, e1)
    v = inv * _dot(direction, q)
    if v < 0 or u + v > 1:
        return None
    t = inv * _dot(e2, q)
    return t if t > 1e-12 else None


def segment_hits_triangle(p, q, tri) -> bool:
    t = ray_triangle(p, _sub(q, p), tri)
    return t is not None and t <= 1.0


def face_area(verts, poly) -> float:
    """Area of a planar polygon (Newell normal / 2)."""
    nx = ny = nz = 0.0
    for i, j in zip(poly, poly[1:] + poly[:1]):
        (x1, y1, z1), (x2, y2, z2) = verts[i], verts[j]
        nx += (y1 - y2) * (z1 + z2)
        ny += (z1 - z2) * (x1 + x2)
        nz += (x1 - x2) * (y1 + y2)
    return 0.5 * math.sqrt(nx * nx + ny * ny + nz * nz)


# ---------------------------------------------------------------- per-mesh checks

def uv_outside(uvs, eps: float = UV_EPS) -> int:
    """UV coordinates (one per face corner) outside 0-1."""
    return sum(1 for u, v in uvs if u < -eps or u > 1 + eps or v < -eps or v > 1 + eps)


def mesh_row(mesh: dict) -> dict:
    """mesh: name, verts (world), polygons, uv_sets, uvs, materials, images. Hard limits give the verdict."""
    geo = ra.audit_mesh(mesh["polygons"], len(mesh["verts"]), MAX_TRIANGLES)
    out_uv = uv_outside(mesh.get("uvs", []))
    row = {
        "name": mesh["name"],
        **{k: geo[k] for k in ("triangles", "boundary_edges", "non_manifold_edges", "connected_parts")},
        "materials": mesh.get("materials", 0),
        "uv_sets": mesh.get("uv_sets", 0),
        "uvs_outside_0_1": out_uv,
        "zero_area_faces": sum(1 for p in mesh["polygons"] if face_area(mesh["verts"], p) <= ZERO_AREA),
        "images": mesh.get("images", []),
        "mirrored": bool(mesh.get("mirrored")),
    }
    fails = []
    if row["triangles"] > MAX_TRIANGLES:
        fails.append(f"triangles {row['triangles']} > {MAX_TRIANGLES} (MR01)")
    if row["non_manifold_edges"]:
        fails.append(f"not watertight: {row['non_manifold_edges']} non-manifold edges ({row['boundary_edges']} open)")
    if row["materials"] > MAX_MATERIALS:
        fails.append(f"materials {row['materials']} > {MAX_MATERIALS} (MR12)")
    if row["uv_sets"] > MAX_UV_SETS:
        fails.append(f"UV sets {row['uv_sets']} > {MAX_UV_SETS} (MR12)")
    if out_uv:
        fails.append(f"{out_uv} UV coordinates outside 0-1 (MR12)")
    if geo["verdict"] == "FAIL" and not fails:  # rig_audit rule we did not name above
        fails.append("rig_audit.audit_mesh verdict FAIL")
    row["fails"] = fails
    row["verdict"] = "FAIL" if fails else "PASS"
    return row


# ---------------------------------------------------------------- parts (surface islands)

def face_parts(polygons) -> list[list[int]]:
    """Face index groups joined by shared vertices. Loose vertices join no group (rig_audit.count_parts counts them)."""
    by_vert: dict[int, list[int]] = {}
    for f, poly in enumerate(polygons):
        for v in poly:
            by_vert.setdefault(v, []).append(f)
    seen = [False] * len(polygons)
    groups = []
    for start in range(len(polygons)):
        if seen[start]:
            continue
        seen[start], stack, group = True, [start], []
        while stack:
            f = stack.pop()
            group.append(f)
            for v in polygons[f]:
                for g in by_vert[v]:
                    if not seen[g]:
                        seen[g] = True
                        stack.append(g)
        groups.append(sorted(group))
    return groups


def make_part(obj: str, index: int, verts, polygons, faces, mirrored: bool = False) -> dict:
    tris, directed, vids = [], {}, set()
    for f in faces:
        poly = polygons[f]
        vids.update(poly)
        tris += [(verts[poly[0]], verts[poly[i]], verts[poly[i + 1]]) for i in range(1, len(poly) - 1)]
        for a, b in zip(poly, poly[1:] + poly[:1]):
            directed.setdefault((a, b) if a < b else (b, a), []).append(a < b)
    closed = all(len(d) == 2 for d in directed.values())
    pts = [verts[i] for i in sorted(vids)]
    volume = None
    if closed and pts:
        o = pts[0]
        volume = sum(_dot(_sub(a, o), _cross(_sub(b, o), _sub(c, o))) for a, b, c in tris) / 6.0
        volume = -volume if mirrored else volume
    return {
        "object": obj, "part": index, "points": pts, "tris": tris,
        "edges": [(verts[a], verts[b]) for a, b in directed],
        "closed": closed, "volume": volume,
        "winding_conflicts": sum(1 for d in directed.values() if len(d) == 2 and d[0] == d[1]),
        "lo": tuple(min(p[i] for p in pts) for i in range(3)),
        "hi": tuple(max(p[i] for p in pts) for i in range(3)),
    }


def build_parts(meshes: list[dict]) -> list[dict]:
    parts = []
    for m in meshes:
        for i, faces in enumerate(face_parts(m["polygons"])):
            parts.append(make_part(m["name"], i, m["verts"], m["polygons"], faces, bool(m.get("mirrored"))))
    return parts


def _label(p: dict) -> str:
    return f"{p['object']}#{p['part']}"


def box_gap(a: dict, b: dict) -> float:
    return math.sqrt(sum(max(0.0, a["lo"][i] - b["hi"][i], b["lo"][i] - a["hi"][i]) ** 2 for i in range(3)))


def ground_gap(p: dict, ground: float | None) -> float | None:
    if ground is None:
        return None
    if p["lo"][2] >= ground:
        return p["lo"][2] - ground
    return max(0.0, ground - p["hi"][2])


def touching(a: dict, b: dict, tol: float = CONTACT_TOL) -> bool:
    """True when the surfaces of a and b come within tol (any vertex-triangle, edge-edge or edge-through-face)."""
    lo = [max(a["lo"][i], b["lo"][i]) - tol for i in range(3)]
    hi = [min(a["hi"][i], b["hi"][i]) + tol for i in range(3)]
    if any(lo[i] > hi[i] for i in range(3)):
        return False

    def pin(p):
        return all(lo[i] <= p[i] <= hi[i] for i in range(3))

    def sin(s):  # a triangle or segment whose box meets the overlap box
        return all(min(q[i] for q in s) <= hi[i] and max(q[i] for q in s) >= lo[i] for i in range(3))

    pa, pb = [p for p in a["points"] if pin(p)], [p for p in b["points"] if pin(p)]
    ta, tb = [t for t in a["tris"] if sin(t)], [t for t in b["tris"] if sin(t)]
    ea, eb = [e for e in a["edges"] if sin(e)], [e for e in b["edges"] if sin(e)]
    if any(point_triangle_distance(p, t) <= tol for p in pa for t in tb):
        return True
    if any(point_triangle_distance(p, t) <= tol for p in pb for t in ta):
        return True
    if any(segment_distance(e[0], e[1], f[0], f[1]) <= tol for e in ea for f in eb):
        return True
    return any(segment_hits_triangle(e[0], e[1], t) for e in ea for t in tb) or \
        any(segment_hits_triangle(e[0], e[1], t) for e in eb for t in ta)


def point_inside(p, part: dict) -> bool:
    """Ray parity against a closed part, majority of 3 fixed skew rays (avoids hitting edges on grid models)."""
    votes = 0
    for d in RAYS:
        n = math.sqrt(_dot(d, d))
        d = (d[0] / n, d[1] / n, d[2] / n)
        hits = sum(1 for t in part["tris"] if ray_triangle(p, d, t) is not None)
        votes += hits % 2
    return votes >= 2


def check_hidden(parts: list[dict]) -> dict:
    listed, hidden_ids = [], set()
    for i, a in enumerate(parts):
        for j, b in enumerate(parts):
            if i == j or not b["closed"]:
                continue
            if not all(b["lo"][k] <= a["lo"][k] and a["hi"][k] <= b["hi"][k] for k in range(3)):
                continue
            if all(point_inside(p, b) for p in a["points"]):
                hidden_ids.add(i)
                listed.append({"part": _label(a), "inside": _label(b)})
                break
    return {"count": len(listed), "listed": listed[:CAP], "ids": sorted(hidden_ids),
            "verdict": "FAIL" if listed else "PASS",
            "method": "every vertex inside one closed part (ray parity, 3 skew rays, majority)"}


def check_floating(parts: list[dict], tol: float = CONTACT_TOL, ground: float | None = 0.0,
                   hidden_ids=()) -> dict:
    n = len(parts)
    parent = list(range(n + 1))  # node n = ground

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    contact = [False] * n
    for i in range(n):
        g = ground_gap(parts[i], ground)
        if g is not None and g <= tol:
            contact[i] = True
            parent[find(i)] = find(n)
        for j in range(i + 1, n):
            if box_gap(parts[i], parts[j]) <= tol and touching(parts[i], parts[j], tol):
                contact[i] = contact[j] = True
                parent[find(i)] = find(j)
    hidden = set(hidden_ids)
    listed = []
    for i, p in enumerate(parts):
        if contact[i] or i in hidden:
            continue
        others = [box_gap(p, q) for j, q in enumerate(parts) if j != i]
        g = ground_gap(p, ground)
        listed.append({"part": _label(p), "nearest_box_gap": round(min(others), 4) if others else None,
                       "ground_gap": None if g is None else round(g, 4)})
    roots = {find(i) for i in range(n)}
    return {"count": len(listed), "listed": listed[:CAP], "contact_tolerance": tol, "ground_z": ground,
            "contact_groups": len(roots),
            "groups_off_ground": None if ground is None else len(roots - {find(n)}),
            "verdict": "FAIL" if listed else "PASS",
            "method": "true surface distance to every other part and to the ground plane > tolerance; "
                      "nearest_box_gap is a lower bound of the true gap; parts hidden inside a closed part are excluded"}


def check_orientation(parts: list[dict], meshes: list[dict]) -> dict:
    inverted = [{"part": _label(p), "volume": round(p["volume"], 6)} for p in parts
                if p["volume"] is not None and p["volume"] < 0]
    conflicts = [{"part": _label(p), "edges": p["winding_conflicts"]} for p in parts if p["winding_conflicts"]]
    return {"inverted_parts": len(inverted), "inverted": inverted[:CAP],
            "winding_conflict_edges": sum(c["edges"] for c in conflicts), "winding_conflicts": conflicts[:CAP],
            "open_parts_not_checked": sum(1 for p in parts if not p["closed"]),
            "mirrored_objects": [m["name"] for m in meshes if m.get("mirrored")],
            "verdict": "FAIL" if inverted or conflicts else "PASS"}


# ---------------------------------------------------------------- whole-model checks

def bbox_size(meshes: list[dict]) -> list[float] | None:
    pts = [v for m in meshes for v in m["verts"]]
    if not pts:
        return None
    return [max(p[i] for p in pts) - min(p[i] for p in pts) for i in range(3)]


def check_size(measured, expected=None, tol=None) -> dict:
    row = {"measured_studs_xyz": None if measured is None else [round(x, 4) for x in measured],
           "expected_xyz": expected, "tolerance": tol}
    if measured is None:
        return {**row, "verdict": "FAIL", "why": "no mesh vertices"}
    if expected is None:
        return {**row, "verdict": "MEASURED"}
    row["delta_xyz"] = [round(abs(m - e), 4) for m, e in zip(measured, expected)]
    row["verdict"] = "MEASURED" if tol is None else ("PASS" if max(row["delta_xyz"]) <= tol else "FAIL")
    return row


def check_budget(total: int, budget: int | None) -> dict:
    return {"total_triangles": total, "budget": budget, "verdict": ra.judge(total, budget)}


def check_names(names, expect=None) -> dict:
    if expect is None:
        return {"objects": sorted(names), "verdict": "MEASURED"}
    missing, extra = sorted(set(expect) - set(names)), sorted(set(names) - set(expect))
    return {"missing": missing, "extra": extra, "verdict": "FAIL" if missing or extra else "PASS"}


def check_export(objects: list[dict], expect=None) -> dict:
    known, listed = set(expect or ()), []
    for o in objects:
        why = [f"hidden ({', '.join(o['hidden'])})"] if o.get("hidden") else []
        if o["type"] in HELPER_TYPES:
            why.append(o["type"].lower())
        if o["type"] == "EMPTY" and o["name"] not in known:
            why.append("empty without a role in --expect")
        if why:
            listed.append({"name": o["name"], "type": o["type"], "why": why})
    return {"count": len(listed), "listed": listed[:CAP], "verdict": "FAIL" if listed else "PASS"}


def worst(verdicts) -> str:
    vs = [v for v in verdicts if v in ORDER]
    return min(vs, key=ORDER.index) if vs else "MEASURED"


def audit_model(meshes: list[dict], objects: list[dict] | None = None, budget: int | None = None,
                size=None, size_tol: float | None = None, expect=None,
                contact_tol: float = CONTACT_TOL, ground: float | None = 0.0) -> dict:
    """meshes: [{name, verts (world, studs), polygons, uv_sets, uvs, materials, images, mirrored}].
    objects: [{name, type, hidden: [flag names]}] for every object in the export collection."""
    objects = objects if objects is not None else [{"name": m["name"], "type": "MESH", "hidden": []} for m in meshes]
    rows = [mesh_row(m) for m in meshes]
    parts = build_parts(meshes)
    hidden = check_hidden(parts)
    checks = {
        "mesh_limits": {"failing": [r["name"] for r in rows if r["verdict"] == "FAIL"],
                        "verdict": worst([r["verdict"] for r in rows] or ["PASS"])},
        "budget": check_budget(sum(r["triangles"] for r in rows), budget),
        "size": check_size(bbox_size(meshes), size, size_tol),
        "floating": check_floating(parts, contact_tol, ground, hidden["ids"]),
        "hidden": {k: v for k, v in hidden.items() if k != "ids"},
        "orientation": check_orientation(parts, meshes),
        "names": check_names([o["name"] for o in objects], expect),
        "export": check_export(objects, expect),
    }
    return {
        "tool": "tools/model/model_audit.py",
        "units": "1 Blender unit = 1 stud (MR36)",
        "params": {"budget": budget, "size": size, "size_tol": size_tol, "expect": expect,
                   "contact_tol": contact_tol, "ground": ground},
        "data": {"meshes": len(rows), "surface_parts": len(parts),
                 "texture_images": sorted({(i["image"], tuple(i["size"])) for r in rows for i in r["images"]})},
        "meshes": rows,
        "checks": checks,
        "verdict": worst(c["verdict"] for c in checks.values()),
    }


def summary_md(report: dict) -> str:
    c = report["checks"]
    lines = [f"# Model audit: {report.get('collection', '')}", "",
             f"Verdict: **{report['verdict']}** (worst row). Units: {report['units']}.", "",
             "| Check | Value | Verdict |", "| --- | --- | --- |",
             f"| Mesh limits (20k tris, watertight, 1 material, 1 UV set, UVs 0-1) | failing: "
             f"{', '.join(c['mesh_limits']['failing']) or 'none'} | {c['mesh_limits']['verdict']} |",
             f"| Triangles (whole model, evaluated) | {c['budget']['total_triangles']} / budget "
             f"{c['budget']['budget']} | {c['budget']['verdict']} |",
             f"| Size in studs (x, y, z) | {c['size']['measured_studs_xyz']} vs {c['size']['expected_xyz']} "
             f"± {c['size']['tolerance']} | {c['size']['verdict']} |",
             f"| Floating parts | {c['floating']['count']} (contact groups {c['floating']['contact_groups']}) "
             f"| {c['floating']['verdict']} |",
             f"| Hidden parts | {c['hidden']['count']} | {c['hidden']['verdict']} |",
             f"| Inverted parts / winding-conflict edges | {c['orientation']['inverted_parts']} / "
             f"{c['orientation']['winding_conflict_edges']} | {c['orientation']['verdict']} |",
             f"| Names vs --expect | missing {c['names'].get('missing', '-')}, extra {c['names'].get('extra', '-')} "
             f"| {c['names']['verdict']} |",
             f"| Export hygiene | {c['export']['count']} listed | {c['export']['verdict']} |", "",
             "| Mesh | Tris | Open edges | Non-manifold | Parts | Materials | UV sets | UVs out | Zero-area | Images |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in report["meshes"]:
        imgs = ", ".join(f"{i['image']} {i['size'][0]}x{i['size'][1]}" for i in r["images"]) or "-"
        lines.append(f"| {r['name']} | {r['triangles']} | {r['boundary_edges']} | {r['non_manifold_edges']} | "
                     f"{r['connected_parts']} | {r['materials']} | {r['uv_sets']} | {r['uvs_outside_0_1']} | "
                     f"{r['zero_area_faces']} | {imgs} |")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- Blender layer (bpy, lazy)

def _hidden_flags(obj) -> list[str]:
    flags = []
    try:
        if obj.hide_get():
            flags.append("hidden in view layer")
    except RuntimeError:
        flags.append("not in view layer")
    if obj.hide_viewport:
        flags.append("disabled in viewports")
    if obj.hide_render:
        flags.append("disabled in renders")
    return flags


def collect(collection: str) -> tuple[list[dict], list[dict]]:
    """Evaluated (modifiers applied) world-space mesh data for every MESH object in the collection tree."""
    import bpy  # noqa: PLC0415

    coll = bpy.data.collections.get(collection)
    if coll is None:
        raise KeyError(f"collection {collection!r} not found")
    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    meshes, objects = [], []
    for obj in sorted(coll.all_objects, key=lambda o: o.name):
        objects.append({"name": obj.name, "type": obj.type, "hidden": _hidden_flags(obj)})
        if obj.type != "MESH":
            continue
        ev = obj.evaluated_get(dg)
        me = ev.to_mesh(preserve_all_data_layers=True, depsgraph=dg)
        try:
            mw = ev.matrix_world
            verts = [tuple(mw @ v.co) for v in me.vertices]
            polys = [list(p.vertices) for p in me.polygons]
            uvs = [tuple(d.uv) for layer in me.uv_layers for d in layer.data]
            uv_sets = len(me.uv_layers)
            mirrored = mw.to_3x3().determinant() < 0
        finally:
            ev.to_mesh_clear()
        mats = [s.material for s in obj.material_slots if s.material]
        images = [{"material": m.name, "image": n.image.name, "size": list(n.image.size)}
                  for m in mats if m.node_tree for n in m.node_tree.nodes
                  if n.type == "TEX_IMAGE" and n.image]
        meshes.append({"name": obj.name, "verts": verts, "polygons": polys, "uvs": uvs, "uv_sets": uv_sets,
                       "materials": len({m.name for m in mats}), "images": images, "mirrored": mirrored})
    return meshes, objects


def audit_scene(collection: str, **kwargs) -> dict:
    """Audit one export collection. kwargs: budget, size, size_tol, expect, contact_tol, ground."""
    import bpy  # noqa: PLC0415

    meshes, objects = collect(collection)
    report = audit_model(meshes, objects, **kwargs)
    report["collection"] = collection
    report["blender"] = bpy.app.version_string
    report["data"]["scene_unit_scale_length"] = bpy.context.scene.unit_settings.scale_length
    return report


def _floats(text: str) -> list[float]:
    return [float(x) for x in text.split(",")]


def main(argv: list[str]) -> int:
    import argparse  # noqa: PLC0415

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--collection", required=True, help="the export collection")
    p.add_argument("--out", required=True, help="audit JSON path; a .md summary is written next to it")
    p.add_argument("--budget", type=int, help="whole-model triangle budget from the record (owner / game profile)")
    p.add_argument("--size", type=_floats, help="expected bounding box x,y,z in studs, from the record")
    p.add_argument("--size-tol", type=float, help="allowed difference per axis in studs, from the record")
    p.add_argument("--expect", type=lambda s: [x for x in s.split(",") if x], help="every object name, comma list")
    p.add_argument("--contact-tol", type=float, default=CONTACT_TOL,
                   help="contact epsilon in studs (default 0.01, geometric: float rounding only)")
    p.add_argument("--ground", default="0", help="ground plane z in studs, or 'none' for held or hovering models")
    a = p.parse_args(argv)
    ground = None if a.ground.lower() == "none" else float(a.ground)
    report = audit_scene(a.collection, budget=a.budget, size=a.size, size_tol=a.size_tol, expect=a.expect,
                         contact_tol=a.contact_tol, ground=ground)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    out.with_suffix(".md").write_text(summary_md(report), encoding="utf-8")
    print(f"RESULT: {report['verdict']} -> {out}")
    return 1 if report["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]))
