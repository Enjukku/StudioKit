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
