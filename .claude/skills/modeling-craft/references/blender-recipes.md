> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Facts: `knowledge/reference/modeling/fact-check-blender.md` (MB rows; probed on the studio's Blender 5.1.2 on 2026-10-21; "rule N" = line N of its "Rules a skill may state"). Rig-side Blender rules: `rigging-craft/references/blender-mcp.md`. Method rows marked [O] are studio procedure (paper HM6-HM24), not Blender documentation.

# Blender recipes for models

## 1. Two ways to drive Blender
| Route | When | How |
| --- | --- | --- |
| Blender MCP (GUI) | Blender is open with the MCP add-on server started (`localhost:9876`) | `execute_blender_code`, return data in a `result` dict; inspect with `get_objects_summary` before changing anything |
| Headless | the GUI or MCP is not running (normal for scripted builds, audits and renders) | `"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" -b <file.blend> --python <script.py> -- <args>`; a new file: `-b --factory-startup --python <script>` and save with `bpy.ops.wm.save_as_mainfile(filepath=...)` |

Both run the same scripts. Keep scripts in `content/models/<asset-id>/scripts/`, one script per stage, idempotent: a rerun replaces its own named outputs, never adds a second copy (HM6 [O]). After a disconnect, re-read the scene first.

## 2. Every session starts with
1. Version into the asset record: `bpy.app.version_string`, `bpy.app.version`, `bpy.app.build_hash.decode()` (rule 1). The studio PC has 5.1.2; the paper's docs are 5.2; the 18 manual pages compared are the same except typos (MB). Do not mix versions in one asset.
2. Units: `scene.unit_settings.system = 'NONE'`, `system_rotation = 'DEGREES'` (factory default is METRIC) → 1 Blender unit = 1 stud (rule 24; MR36).
3. Player dummy: a plain block or capsule of the player height from the game profile (5 studs if unset, PROPOSAL), in a `_ref` collection that is never exported.
4. Reference images: the approved views as image empties or camera backgrounds, in `_ref`.
5. Collections: `Export` (only what ships), `_ref`, `_work`. The audit and the exporter read `Export` only.

## 3. Hand-modeling recipes (verified behaviour on 5.1.2)
| Need | Call and the trap to avoid | Source |
| --- | --- | --- |
| Add a modifier | `ob.modifiers.new(name, 'BEVEL' / 'MIRROR' / 'BOOLEAN' / 'DECIMATE' / 'REMESH' / 'WELD' / 'TRIANGULATE')`; new modifiers go to the bottom; order changes the result; reorder with `bpy.ops.object.modifier_move_to_index(modifier=, index=)` | rules 2, 27 |
| Mirror | `use_axis=(x,y,z)`, `mirror_object` for a custom centre; merge on by default (`merge_threshold` 0.001); `use_clip` only helps editing; `use_bisect_axis` cuts a full mesh. Keep approved asymmetry (HM8 [O]) | rule 3 |
| Bevel | defaults: `width` 0.1, `segments` 1, **`limit_method='ANGLE'`** (set `'NONE'` to bevel every edge); `offset_type` OFFSET / WIDTH / DEPTH / PERCENT / ABSOLUTE: write which you use; N segments = N faces across the bevel, 1 = flat chamfer; `profile` does nothing at 1 segment. No universal width: test at the game camera | rule 4; M-07 |
| Boolean | default solver **EXACT**; MANIFOLD only on closed inputs (wrong result otherwise); FLOAT leaves extra faces on coplanar overlaps. Check inputs are manifold first; after the cut check slivers and inside faces; never cut across a bending joint | rule 5; HM12 [O] |
| Decimate | Collapse `ratio` works on triangles (0.5 = half the triangles); the polygon count stays higher unless `use_collapse_triangulate=True`. Only for static irregular shapes | rule 6; HM15 [O] |
| Remesh | `bpy.ops.object.voxel_remesh()` uses the base mesh only and **removes shape keys**; the Remesh modifier reads the stack. Neither gives topology that bends well | rule 7 |
| Origins | `bpy.ops.object.origin_set(type='ORIGIN_CURSOR' / 'ORIGIN_GEOMETRY' / ..., center='MEDIAN' / 'BOUNDS')`; place the 3D cursor at the hinge or base first; `ORIGIN_CURSOR` keeps world positions | rule 17 |
| Apply transforms | `bpy.ops.object.transform_apply(location=, rotation=, scale=)`; shared mesh data needs `isolate_users=True` or a single-user copy; apply before rigging | rule 18 |
| Split | Edit Mode `bpy.ops.mesh.separate(type='SELECTED' / 'MATERIAL' / 'LOOSE')`; LOOSE splits the whole mesh and only disconnected pieces | rule 16 |
| Plane cut | `bpy.ops.mesh.bisect(plane_co, plane_no, use_fill, clear_inner, clear_outer)`: plane in **world** space, Edit Mode, selected geometry; `bmesh.ops.bisect_plane` takes **local** coordinates | rules 14-15 |
| Merge by distance | `bpy.ops.mesh.remove_doubles(threshold=...)` (default 0.0001) or a Weld modifier; never one big global distance (it closes eyelids, fuses clothing: REV05 [O]) | rule 20 |
| Clean-up | `delete_loose`, `dissolve_degenerate`, `dissolve_limited`, `fill_holes(sides=4)`, `face_make_planar`, `select_non_manifold`: only on what the audit flags; never fill every open edge | rule 20; REV07 [O] |
| UVs | Edit Mode: `uv.smart_project`, `uv.unwrap` (default CONFORMAL), `uv.pack_islands(margin=, rotate=, shape_method=, pin=, udim_source=)`; UVs live per face corner | rules 10, 19 |
| Bake | `scene.render.engine='CYCLES'`; low mesh has an active UV map and an **active, selected Image Texture node**; `bpy.ops.object.bake(type='NORMAL' or 'DIFFUSE', use_selected_to_active=True, cage_extrusion=, max_ray_distance=, margin=, margin_type=, normal_space='TANGENT')`; set margin and type explicitly | rule 8 |
| Mesh validity | `Mesh.validate()` **edits** the mesh and returns True when it changed something: run it on a copy for diagnosis; `from_pydata` accepts bad indices | rule 9 |
| Camera projection | `bpy_extras.object_utils.world_to_camera_view(scene, cam, co)` → (x, y, depth); (0,0) bottom-left; negative depth = behind; landmarks need a visibility check too | rule 21; BK9 [O] |

## 4. Measuring (never from the viewport)
- Count and size from the **evaluated** mesh: `ob.evaluated_get(dg).to_mesh(preserve_all_data_layers=True, depsgraph=dg)` … `to_mesh_clear()` in `finally`; triangles = `calc_loop_triangles()` or sum(len(poly) − 2). `Object.dimensions` and `bound_box` missed a Subdivision result in the probe (2.0 vs 1.8254): measure evaluated vertices with the world matrix (rules 11-13).
- The kit tools do this for you:
```text
blender -b <work.blend> --python tools/model/model_audit.py -- --collection Export \
    --out content/models/<id>/tests/audit.json --budget <record budget> --size x,y,z --size-tol <record> \
    --expect <object names> --ground 0            # --ground none for held or hovering models
blender -b <work.blend> --python tools/model/review_renders.py -- --collection Export \
    --out content/models/<id>/renders --player-height <studs> --game-cam <distance,height,fov>
```
  From the MCP: add `tools/model` to `sys.path`, then `import model_audit; model_audit.audit_scene("Export", ...)`. The audit: hard limits (20,000 triangles per mesh, 1 material, 1 UV map, UVs in 0-1, watertight) PASS/FAIL; floating, hidden-inside, inverted and stray export objects FAIL when found; budget and size PASS/FAIL only with a number from the record, else MEASURED (it never invents a threshold). Renders: front, back, left, right, top, three-quarter, scale (player block), optional game camera, Workbench, neutral; the scene is restored afterwards.
- Method limits of the audit: parts touching only each other are not "floating" (see `contact_groups`); hidden-inside tests vertices only; texture sizes are reported without a verdict.

## 5. Export
Kit FBX profile `tools/rig/roblox_fbx.py`: every option name exists on 5.1.2 and every value is valid (rule 23); Blender's own defaults are wrong for Roblox (rule 22: no unit-scale option, leaf bones on, animation baked, `embed_textures` off). `embed_textures` only works with `path_mode='COPY'`. glTF (`bpy.ops.export_scene.gltf`) needs no scale fix but changes the Roblox hierarchy (rule 26; MR40). Not yet run on a written file in this kit: confirm with the first calibration round trip (`references/export-import.md` §1).
