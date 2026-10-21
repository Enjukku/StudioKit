> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-craft`. Facts: `knowledge/reference/rigging/fact-check-blender.md` (RB rows; Blender 5.2.2 source and 5.2 manual, bundled MCP docs = 5.1). Method: rigging paper RP:340-374, 495-556 [O]; animation paper AP:542-701 [O].

# Blender through Python and the Blender MCP

## 1. Version first (every session)
1. Run once and save to the build manifest (`content/rigs/<id>/build-manifest.json`): `bpy.app.version_string`, `bpy.app.version`, `bpy.app.build_hash`, the FBX add-on `bl_info["version"]`, and `roblox_fbx.check_exporter()` (must return `[]`) (RB rule 1; RP:593).
2. API floor: Blender ≥ 5.0 for the slotted-Action calls below (`fcurves.ensure`, `group_name`); the Blender MCP add-on needs ≥ 5.1. The studio PC has 5.1 installed (2026-10-21); facts below hold for 5.1 and 5.2.2 unless marked. Do not mix versions inside one asset.
3. Check API names against the installed Blender before relying on them: `mcp__blender__search_api_docs` (bundled docs are 5.1) or `dir()` / `get_rna_type()` in the live session.

## 2. MCP working rules
- Blender must be running with the MCP add-on server started (`localhost:9876`). If the call fails, the stage is BLOCKED; ask the lead, never fake a result.
- `execute_blender_code` returns data through a variable named `result` (JSON-serialisable). Return compact dicts, not print output or whole scenes.
- **Inspect before you change.** `get_objects_summary` first; never assume names, modes or selection.
- **Idempotent stages** (RP:367, 548): each stage reads the scene, saves a checkpoint (`bpy.ops.wm.save_as_mainfile(filepath=..., copy=True)`), changes one thing, evaluates, records evidence. A rerun replaces its own named output (`<asset>_proxy_rig`, `<asset>_rig`); it never adds a second armature, modifier or joint. After a disconnect, re-read the scene before retrying.
- Never edit the source snapshot. Work in `content/rigs/<id>/work/<asset>_work.blend`.
- Prefer direct data access (`bpy.data`) for repeatable edits; for operators set mode, active object and selection explicitly and use `bpy.context.temp_override(...)`. No Python threads (RB rule 26).

## 3. API facts you will use (RB rules)
| Need | Call / fact | RB |
| --- | --- | --- |
| Split a mesh | `bpy.ops.mesh.separate(type='SELECTED' / 'MATERIAL' / 'LOOSE')`; LOOSE splits only disconnected pieces | 15 |
| Plane cut | `bpy.ops.mesh.bisect(plane_co, plane_no, use_fill, clear_inner, clear_outer)` takes the plane in **world space** and cuts selected geometry of every Edit Mode object; `bmesh.ops.bisect_plane` works in mesh coordinates | 16 |
| Pose matrices | `PoseBone.matrix` = final, armature-object space; world = `arm.matrix_world @ pb.matrix`; `matrix_basis` = relative to parent and rest; `Bone.head_local` armature-relative; `edit_bones` exist only in Edit Mode | 17 |
| Evaluated geometry | re-fetch `bpy.context.evaluated_depsgraph_get()` after every change; `ob.evaluated_get(dg).to_mesh()` (pass `preserve_all_data_layers=True, depsgraph=dg` to keep vertex groups); always `to_mesh_clear()` | 18 |
| Frames | `scene.frame_set(frame)`, then restore; effective rate = `scene.render.fps / scene.render.fps_base` | 19, 25 |
| Weights | `vertex_group_limit_total`, `vertex_group_normalize_all`, `vertex_group_clean` with `group_select_mode='BONE_DEFORM'` | 13 |
| Preserve Volume | `ArmatureModifier.use_deform_preserve_volume` (dual quaternion); set False for Roblox preview | 12 |
| New test clip | `bpy.data.actions.new(name)`; `action.slots.new(id_type='OBJECT', name=arm.name)`; `ad.action = action`; `ad.action_slot = slot`; `bag = anim_utils.action_ensure_channelbag_for_slot(action, slot)`; `bag.fcurves.ensure(path, index=i, group_name=bone)`; `keyframe_points.add(n)`; `foreach_set('co', flat)`; `fcurve.update()`. Legacy `action.fcurves` is gone since 5.0 | 2, 3 |
| Bake constraints | `bpy.ops.nla.bake(..., visual_keying=True, only_selected=...)` (defaults are `visual_keying=False`, `only_selected=True`); `clean_curves` only with a set tolerance | 20 |
| Import a check file | native `bpy.ops.wm.fbx_import` | 24 |
| Export | `tools/rig/roblox_fbx.py` (never defaults) | 4 |

## 4. Stage scripts (what each stage produces)
| Stage | Script does | Output |
| --- | --- | --- |
| S2 inspect | object list, per-mesh `audit_mesh` (triangles, open edges, connected parts), materials, UV maps, bounding sizes in studs | `tests/s2_inventory.json` + 6 orthographic renders with wireframe over shaded |
| S2 plan renders | coloured cut lines and bend zones over the model, 6 views | `renders/plan_*.png` for the modeler |
| S4 proxy sweep | temporary one-bone-per-part armature at the §C pivots; pose each §B extreme; renders + `audit_mesh` per part | `tests/s4_r<n>_*.png`, `tests/s4_r<n>.json`; proxy deleted after |
| S5 rig | export skeleton by allowlist + parent map; authoring controls on top; weights; control manifest | `<asset>_rig.blend`, `control-manifest.json` |
| S5 tests | test clips as named Actions (one per test); `rig_audit.audit_scene` with protected groups and sweeps | `tests/audit_s5.json`, clip renders |
| S5 export | `roblox_fbx.export` rest model + one file per clip; re-import into a fresh scene (`wm.fbx_import`) and compare hierarchy, weights, sizes | `export/*.fbx`, `tests/roundtrip.json` |

Renders for review: Workbench (fast, deterministic), fixed saved cameras so before/after views match (AP:680). Name every evidence file in the rig sheet §G.

## 5. Proposed automation surface (studio wrappers, not Blender or MCP names)
The papers propose wrappers such as `inspect_rig`, `set_pose`, `evaluate_frame`, `sample_deformed_mesh`, `bake_export_skeleton`, `validate_export` (RP:361; AP:634). They do not exist yet. Write them only when a second asset needs the same code (`rules/anti-overengineering.md`); until then, keep stage scripts in `content/rigs/<id>/scripts/` and reuse `tools/rig/`.
