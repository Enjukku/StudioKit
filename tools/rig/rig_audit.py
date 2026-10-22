"""Measure a rig against the Roblox platform limits and the rig sheet, without taste.

Kit tool: universal (Studio Kit). Pure checks use the Python standard library only, so they run
offline and in tests. The Blender layer (`collect_*`, `sweep`, `main`) imports `bpy` lazily and
runs inside Blender: `blender -b <file.blend> --python tools/rig/rig_audit.py -- <args>`, or from
the Blender MCP with `import rig_audit; rig_audit.audit_scene(...)` after adding tools/rig to sys.path.

Hard platform limits (fail without a tolerance):
  - max 4 bone or joint influences per vertex      knowledge/external/roblox-creator-docs/art/modeling/specifications.md:59
  - no influences on the Root bone or joint        specifications.md:60
  - watertight: no exposed holes or backfaces      specifications.md:35 (measured here as 0 non-manifold edges)
  - max 20,000 triangles per mesh                  specifications.md:34
Everything else (protected-region movement, rigid-shape drift) is a measurement. It gets PASS or
FAIL only when the caller passes a tolerance from the rig sheet; otherwise the verdict is MEASURED.
Never invent a tolerance (rigging paper §10: no published Roblox acceptance thresholds).

Usage (inside Blender):
  blender -b char.blend --python tools/rig/rig_audit.py -- --mesh Body --armature Rig \
      --root Root --out content/rigs/<id>/tests/audit.json \
      --protect chest_protect --sweep Head:Z:-60:60 --tolerance 0.001
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

MAX_INFLUENCES = 4
MAX_TRIANGLES = 20_000
ZERO = 1e-6  # weights at or below this count as no influence
SUM_TOL = 1e-3  # how far a deform weight sum may be from 1.0 before it counts as not normalized


# ---------------------------------------------------------------- pure checks (no bpy)

def audit_weights(
    vertex_weights: list[list[tuple[str, float]]],
    deform_bones: set[str],
    root: str | None = None,
    max_influences: int = MAX_INFLUENCES,
) -> dict:
    """vertex_weights[i] = [(group_name, weight), ...] for vertex i.

    Only groups named in deform_bones count as influences (control or selection groups are ignored,
    rigging paper §5). Returns counts and the first offending vertex ids per problem.
    """
    over, root_hit, unweighted, invalid, unnormalized = [], [], [], [], []
    stray_groups: set[str] = set()
    for i, groups in enumerate(vertex_weights):
        deform = []
        for name, w in groups:
            if name not in deform_bones:
                if w > ZERO:
                    stray_groups.add(name)
                continue
            if not math.isfinite(w) or w < 0:
                invalid.append(i)
                continue
            if w > ZERO:
                deform.append((name, w))
        if root and any(n == root for n, _ in deform):
            root_hit.append(i)
        if len(deform) > max_influences:
            over.append(i)
        total = sum(w for _, w in deform)
        if total <= ZERO:
            unweighted.append(i)
        elif abs(total - 1.0) > SUM_TOL:
            unnormalized.append(i)
    return {
        "vertices": len(vertex_weights),
        "over_influence_limit": {"count": len(over), "first": over[:20], "limit": max_influences},
        "root_weighted": {"count": len(root_hit), "first": root_hit[:20]},
        "unweighted": {"count": len(unweighted), "first": unweighted[:20]},
        "invalid_weight": {"count": len(invalid), "first": invalid[:20]},
        "not_normalized": {"count": len(unnormalized), "first": unnormalized[:20]},
        "non_deform_groups_with_weight": sorted(stray_groups),
        "verdict": "FAIL" if (over or root_hit or invalid) else "PASS",
    }


def audit_mesh(polygons: list[list[int]], vertex_count: int, max_triangles: int = MAX_TRIANGLES) -> dict:
    """polygons = vertex index lists. Counts export triangles, open and non-manifold edges, parts."""
    edge_faces: dict[tuple[int, int], int] = {}
    triangles = 0
    for poly in polygons:
        triangles += len(poly) - 2
        for a, b in zip(poly, poly[1:] + poly[:1]):
            key = (a, b) if a < b else (b, a)
            edge_faces[key] = edge_faces.get(key, 0) + 1
    boundary = sum(1 for n in edge_faces.values() if n == 1)
    non_manifold = sum(1 for n in edge_faces.values() if n != 2)
    parts = count_parts(vertex_count, edge_faces.keys())
    return {
        "triangles": triangles,
        "triangle_limit": max_triangles,
        "boundary_edges": boundary,
        "non_manifold_edges": non_manifold,
        "connected_parts": parts,
        "verdict": "FAIL" if (triangles > max_triangles or non_manifold) else "PASS",
    }


def count_parts(vertex_count: int, edges) -> int:
    """Connected surface parts (union-find over edges). Loose vertices count as parts."""
    parent = list(range(vertex_count))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return len({find(v) for v in range(vertex_count)})


def max_displacement(rest: list[tuple[float, float, float]], posed: list[tuple[float, float, float]],
                     indices: list[int] | None = None) -> dict:
    """Largest vertex move between rest and posed positions (same order). indices limits the set."""
    idx = range(len(rest)) if indices is None else indices
    best, best_i = 0.0, None
    for i in idx:
        d = math.dist(rest[i], posed[i])
        if d > best:
            best, best_i = d, i
    return {"max": best, "vertex": best_i, "checked": len(idx)}


def rigid_drift(rest: list[tuple[float, float, float]], posed: list[tuple[float, float, float]],
                indices: list[int], samples: int = 64) -> dict:
    """A rigid part keeps its internal distances. Compares pairwise distances on an even sample."""
    if len(indices) < 2:
        return {"max": 0.0, "pairs": 0}
    step = max(1, len(indices) // samples)
    pick = indices[::step][:samples]
    worst, pairs = 0.0, 0
    for a_pos, a in enumerate(pick):
        for b in pick[a_pos + 1:]:
            worst = max(worst, abs(math.dist(rest[a], rest[b]) - math.dist(posed[a], posed[b])))
            pairs += 1
    return {"max": worst, "pairs": pairs}


def judge(measured: float, tolerance: float | None) -> str:
    """PASS / FAIL only against a tolerance from the rig sheet; else MEASURED."""
    if tolerance is None:
        return "MEASURED"
    return "PASS" if measured <= tolerance else "FAIL"


# ---------------------------------------------------------------- Blender layer (bpy, lazy)

def collect_weights(mesh_obj) -> list[list[tuple[str, float]]]:
    names = {g.index: g.name for g in mesh_obj.vertex_groups}
    return [[(names[g.group], g.weight) for g in v.groups if g.group in names] for v in mesh_obj.data.vertices]


def deform_bone_names(arm_obj) -> set[str]:
    return {b.name for b in arm_obj.data.bones if b.use_deform}


def evaluated_world_positions(mesh_obj) -> list[tuple[float, float, float]]:
    import bpy  # noqa: PLC0415

    bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh_obj.evaluated_get(dg)
    me = ev.to_mesh()
    try:
        mw = ev.matrix_world
        return [tuple(mw @ v.co) for v in me.vertices]
    finally:
        ev.to_mesh_clear()


def group_vertices(mesh_obj, group_name: str) -> list[int]:
    g = mesh_obj.vertex_groups.get(group_name)
    if g is None:
        raise KeyError(f"vertex group {group_name!r} not on {mesh_obj.name}")
    return [v.index for v in mesh_obj.data.vertices if any(x.group == g.index and x.weight > ZERO for x in v.groups)]


def sweep(arm_obj, mesh_obj, bone: str, axis: str, angles_deg: list[float], indices: list[int]) -> list[dict]:
    """Rotate one pose bone about a local axis to each angle; measure the given vertices. Restores the pose."""
    pb = arm_obj.pose.bones[bone]
    saved_mode, saved = pb.rotation_mode, (tuple(pb.rotation_quaternion), tuple(pb.rotation_euler))
    rest = evaluated_world_positions(mesh_obj)
    out = []
    try:
        pb.rotation_mode = "XYZ"
        for ang in angles_deg:
            pb.rotation_euler = (0.0, 0.0, 0.0)
            pb.rotation_euler["XYZ".index(axis.upper())] = math.radians(ang)
            posed = evaluated_world_positions(mesh_obj)
            out.append({"bone": bone, "axis": axis, "angle_deg": ang, **max_displacement(rest, posed, indices)})
    finally:
        pb.rotation_mode = saved_mode
        pb.rotation_quaternion, pb.rotation_euler = saved
        evaluated_world_positions(mesh_obj)
    return out


def audit_scene(mesh: str, armature: str, root: str | None = None, protect: str | None = None,
                sweeps: list[str] | None = None, tolerance: float | None = None) -> dict:
    """Full audit of one skinned mesh. sweeps: ["Bone:AXIS:a1:a2:..."] in degrees."""
    import bpy  # noqa: PLC0415

    m, a = bpy.data.objects[mesh], bpy.data.objects[armature]
    me = m.data
    report = {
        "blender": bpy.app.version_string,
        "mesh": mesh,
        "armature": armature,
        "weights": audit_weights(collect_weights(m), deform_bone_names(a), root),
        "geometry": audit_mesh([list(p.vertices) for p in me.polygons], len(me.vertices)),
        "sweeps": [],
    }
    if protect and sweeps:
        idx = group_vertices(m, protect)
        for spec in sweeps:
            bone, axis, *angles = spec.split(":")
            for row in sweep(a, m, bone, axis, [float(x) for x in angles], idx):
                row["protected_group"] = protect
                row["verdict"] = judge(row["max"], tolerance)
                report["sweeps"].append(row)
    hard = [report["weights"]["verdict"], report["geometry"]["verdict"]]
    soft = [r["verdict"] for r in report["sweeps"]]
    report["verdict"] = "FAIL" if "FAIL" in hard + soft else ("MEASURED" if "MEASURED" in soft else "PASS")
    return report


# ---------------------------------------------------------------- caps, overlap, orient (Blender layer, J018 G3-P1)
# The rigger's measuring recipes, moved here from rigging-craft/references/blender-mcp.md section 6 so no book
# carries the code. Every one is a screening aid (its known false readings are in that section): a failing or
# borderline number is checked by eye on the still of that pose and camera before any fix note. Call them through
# the Blender MCP after adding tools/rig to sys.path. They read a fresh depsgraph on every call, so a pose or
# group change is always seen.

TRI_WEIGHTS = [(.6, .2, .2), (.2, .6, .2), (.2, .2, .6), (1 / 3, 1 / 3, 1 / 3), (.45, .45, .1), (.1, .45, .45), (.45, .1, .45)]


def _tri_points(me, tri):
    """7 points inside one triangle, 3 of them near its edges (a face is sampled through all its triangles)."""
    a, b, c = (me.vertices[i].co for i in tri.vertices)
    return [a * u + b * v + c * w for u, v, w in TRI_WEIGHTS]


def _ray_origin(cam, w):
    from mathutils import Vector  # noqa: PLC0415
    if cam.data.type == "ORTHO":  # parallel rays along the view axis, starting on the camera plane
        ax = (cam.matrix_world.to_3x3() @ Vector((0, 0, -1))).normalized()
        return w - ax * ax.dot(w - cam.matrix_world.translation)
    return cam.matrix_world.translation


def _cap_vertices(me, group_index: int) -> set[int]:
    return {v.index for v in me.vertices if any(x.group == group_index and x.weight > 0.99 for x in v.groups)}


def cap_count(ob, cam, cut: str) -> tuple[int, int]:
    """(visible, sampled) points of one cut's cap or socket faces (group `cap_<cut>` at weight 1), posed.

    Points come from the evaluated mesh (an Armature-moved part reads correctly), sampled over every triangle of
    every cap face. Pass per cut and camera: visible 0 with sampled above 0. Stops on a missing group or a hidden
    part (a hidden part reads 0 with no error)."""
    import bpy  # noqa: PLC0415
    g = ob.vertex_groups.get(f"cap_{cut}")
    if g is None:
        raise KeyError(f"{ob.name}: no 'cap_{cut}' vertex group")
    if not ob.visible_get():
        raise RuntimeError(f"{ob.name} is hidden: its caps would read 0")
    dg = bpy.context.evaluated_depsgraph_get()
    sc = bpy.context.scene
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    try:
        me.calc_loop_triangles()
        caps = _cap_vertices(me, g.index)
        pts = [(t.polygon_index, p) for t in me.loop_triangles
               if set(me.polygons[t.polygon_index].vertices) <= caps for p in _tri_points(me, t)]
        seen = 0
        for face, p in pts:
            w = ob.matrix_world @ p
            o = _ray_origin(cam, w)
            d = w - o
            hit, loc, _, idx, hob, _ = sc.ray_cast(dg, o, d.normalized(), distance=d.length + 1e-3)
            seen += bool(hit and hob.original == ob and idx == face and (loc - w).length < 1e-3 * d.length)
        return seen, len(pts)
    finally:
        ev.to_mesh_clear()


def _in_tris(tris, w, eps: float) -> bool:
    for p, q, r in tris:
        n = (q - p).cross(r - p)
        if n.length > 1e-9 and all(n.normalized().dot((b - a).cross(w - a)) >= -eps * (b - a).length
                                   for a, b in ((p, q), (q, r), (r, p))):
            return True
    return False


def mark_plane_caps(ob, cut: str, co, no, child=None, eps: float = 0.005) -> int:
    """Put the faces on a flat cut plane (world space, rest pose) into `cap_<cut>` at weight 1; returns the faces found.

    With child= (ob is the parent) only faces whose corners all lie inside the child's cap outline are kept: the
    socket is the area the child covers, never the parent's whole face. Deletes an existing group first (REPLACE
    keeps old vertices). 0 found on a closed parent face: cut the outline in, or record the socket n/a."""
    old = ob.vertex_groups.get(f"cap_{cut}")
    if old is not None:
        ob.vertex_groups.remove(old)
    mw, no = ob.matrix_world, no.normalized()
    tris = None
    if child is not None:
        cg = child.vertex_groups[f"cap_{cut}"]
        cm = child.data
        cm.calc_loop_triangles()
        cv = _cap_vertices(cm, cg.index)
        tris = [[child.matrix_world @ cm.vertices[i].co for i in t.vertices] for t in cm.loop_triangles
                if set(cm.polygons[t.polygon_index].vertices) <= cv]

    def keep(i):
        w = mw @ ob.data.vertices[i].co
        return abs(no.dot(w - co)) < eps and (tris is None or _in_tris(tris, w, eps))

    vs = {i for p in ob.data.polygons if all(keep(i) for i in p.vertices) for i in p.vertices}
    g = ob.vertex_groups.new(name=f"cap_{cut}")
    g.add(sorted(vs), 1.0, "REPLACE")
    return sum(set(p.vertices) <= vs for p in ob.data.polygons)


def overlap_pairs(a, b) -> int:
    """Overlapping face pairs between two parts (world space, evaluated meshes); compare with the rest count.
    Never use it on a parent and child (they touch by design); split one skinned mesh by region first."""
    import bpy  # noqa: PLC0415
    from mathutils.bvhtree import BVHTree  # noqa: PLC0415
    dg = bpy.context.evaluated_depsgraph_get()

    def tree(ob):
        ev = ob.evaluated_get(dg)
        m = ev.to_mesh()
        try:
            return BVHTree.FromPolygons([ob.matrix_world @ v.co for v in m.vertices], [list(p.vertices) for p in m.polygons])
        finally:
            ev.to_mesh_clear()

    return len(tree(a).overlap(tree(b)))


def head_drift(arm_obj, bone: str, frames: list[int]) -> list[float]:
    """Rotation difference (degrees) of the bone's world orientation from the first frame, per frame.
    Never read a bone matrix's Euler z as yaw: the rest frame is rotated, so the Euler parts mix axes."""
    import bpy  # noqa: PLC0415
    sc = bpy.context.scene
    q1, out = None, []
    for f in frames:
        sc.frame_set(f)
        q = (arm_obj.matrix_world @ arm_obj.pose.bones[bone].matrix).to_quaternion()
        q1 = q1 or q
        out.append(round(math.degrees(q.rotation_difference(q1).angle), 2))
    return out


def swing(arm_obj, bone: str, frames: list[int]) -> list[float]:
    """Angle (degrees) between the bone's own axis at rest and in the pose, from its own channels; for a range on a
    control that turns about two axes in one clip (the pass: the largest swing <= the rig sheet's tilt range)."""
    import bpy  # noqa: PLC0415
    from mathutils import Vector  # noqa: PLC0415
    sc = bpy.context.scene
    out = []
    for f in frames:
        sc.frame_set(f)
        y = arm_obj.pose.bones[bone].matrix_basis.to_3x3() @ Vector((0, 1, 0))
        out.append(round(math.degrees(Vector((0, 1, 0)).angle(y)), 2))
    return out


def scaled_channels(action, eps: float = 1e-4) -> list[str]:
    """Scale F-curves with a value other than 1 (Blender 5.x layered Actions); a Roblox pose stores only a CFrame."""
    return [fc.data_path for lay in action.layers for st in lay.strips for cb in st.channelbags
            for fc in cb.fcurves if fc.data_path.endswith("scale")
            and any(abs(k.co[1] - 1.0) > eps for k in fc.keyframe_points)]


def main(argv: list[str]) -> int:
    import argparse  # noqa: PLC0415

    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--mesh", required=True)
    p.add_argument("--armature", required=True)
    p.add_argument("--root")
    p.add_argument("--protect", help="vertex group that must not move during the sweeps")
    p.add_argument("--sweep", action="append", default=[], help="Bone:AXIS:angle:angle... (degrees)")
    p.add_argument("--tolerance", type=float, help="max protected move in scene units (Blender metres by default), from the rig sheet")
    p.add_argument("--out", required=True)
    args = p.parse_args(argv)
    report = audit_scene(args.mesh, args.armature, args.root, args.protect, args.sweep, args.tolerance)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"RESULT: {report['verdict']} -> {args.out}")
    return 1 if report["verdict"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]))
