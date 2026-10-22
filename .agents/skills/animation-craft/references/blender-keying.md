> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-craft`. Facts: `knowledge/reference/animation/fact-check-blender-keying.md` (KB rows; every name **run on Blender 5.1.2** headless, J006-T04), `knowledge/reference/rigging/fact-check-blender.md` (RB rows; 5.2.2 source reads). Paper: AP:542-701 (BL rows). MCP and headless rules: `rigging-craft` → `references/blender-mcp.md`. On 5.2, re-run the snippet in §6 once before the first real job (KB recipe 21).

# Blender: key, loop, sample, bake

## 1. Session rules
- Record `bpy.app.version_string`, the build hash and the FBX add-on check (`roblox_fbx.check_exporter() == []`) in the build manifest (KB recipe 1; RB22, RB28).
- Work on a copy of the released rig file; never save over the rigger's file or the source snapshot. Inspect the scene before changing anything (Blender MCP rules). Headless Blender (`blender -b <file> --python <script>`) is the default for scripted passes; the MCP for looking and small edits.
- Batch changes and answer with a short diff and a validation report, not a scene dump after every key; refuse NaN, Inf and repeated frames before writing (BL19, AP:632).
- Key controls only; the export skeleton is baked (follow the control manifest's `keying_policy`, e.g. the teddy's "key controls on the control armature only; the export armature is baked per clip").

## 2. Clip setup
1. **Scene rate:** set `scene.render.fps` and `fps_base` yourself (factory default 24 / 1.0); effective rate = `fps / fps_base`, which the FBX exporter also uses (KB12). Set `scene.frame_start` / `frame_end` to the clip range.
2. **Action and slot:** `act = bpy.data.actions.new(name)`; `slot = act.slots.new(id_type='OBJECT', name=arm.name)` (both arguments required); `ad = arm.animation_data_create(); ad.action = act; ad.action_slot = slot` (KB17).
3. **Channelbag:** `bag = bpy_extras.anim_utils.action_ensure_channelbag_for_slot(act, slot)` (KB18). `act.fcurves`, `act.groups` and `act.id_root` are gone since 5.0 and raise AttributeError (KB19, RB30).
4. **Curve per channel:** `path = pose_bone.path_from_id("rotation_euler")` (or the manifest's channel); `fc = bag.fcurves.ensure(path, index=i, group_name=bone_name)`; `group_name=`, not `action_group=` (TypeError) (KB20).
5. One named Action per deliverable clip; clip ids, events, contacts and loop policy live in the animation set and timing list, not in display names (BL17).

## 3. Keys, interpolation, handles
- **Batch keys:** `kp = fc.keyframe_points; kp.add(n); kp.foreach_set('co', [f0, v0, f1, v1, ...]); fc.update()` — the fast path (20,000 keys in 5 ms vs 360 ms per-key insert, one machine) (KB03).
- **Always write interpolation and handle types**: new keys default to BEZIER and AUTO_CLAMPED from user preferences. `INTERP = {e.identifier: e.value for e in bpy.types.Keyframe.bl_rna.properties['interpolation'].enum_items}`; `kp.foreach_set('interpolation', [INTERP['CONSTANT']] * n)`; same pattern for `handle_left_type` / `handle_right_type` (FREE, ALIGNED, VECTOR, AUTO, AUTO_CLAMPED); then `fc.update()` (KB03-KB05, KB24).
- **Stepped blocking:** `'CONSTANT'` holds the value exactly until the next key; switch the same keys to `'BEZIER'` or `'LINEAR'` later (KB04). Copied-pair holds (a duplicated key) are the other blocking style (03 TS11); both show real holds.
- **Handles:** AUTO_CLAMPED does not overshoot a key value; AUTO can (3.0275 on a 3.0 peak in the test); VECTOR gives straight segments. Moving a key in time: `co_ui` moves the handles with it, `co` moves only the point — an overlap offset must move both (KB05, KB06; BL27).
- **Easing:** `Keyframe.easing` (AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT) applies to the SINE ... ELASTIC interpolation types (KB07). Key `type` (KEYFRAME, BREAKDOWN, MOVING_HOLD, EXTREME, JITTER, GENERATED) can mark blocking poses and breakdowns (KB04).
- **Interpolation per segment, not per clip:** contacts flat or hand-set, ballistic and mechanical motion with their own velocity profile, impacts hard (BL24). Weighted tangents (a Maya habit, 03 TS12) have no checked Blender equivalent: use handle types and handle positions.
- **Rotation:** one rotation mode per bone, the rig's (the manifest names it; bones default to QUATERNION). Quaternion component curves do not give even angular speed: judge orientations and end points, not component curves (KB21, RB42).

## 4. Loops
- The last key pose equals the first; the clip range `K..L` includes L; the period is `L - K`. This matches Roblox, where the runtime does not blend the last key into the first (RA18).
- In Blender, preview the cycle with a Cycles modifier on every curve: `m = fc.modifiers.new('CYCLES'); m.mode_before = m.mode_after = 'REPEAT'` (`'REPEAT_OFFSET'` for travelling channels). It must be the **first** modifier or Blender refuses silently: check `len(fc.modifiers)` (KB08, KB09).
- `act.use_cyclic`, `use_frame_range`, `frame_start`, `frame_end` are intent flags: they neither change evaluation nor add the modifier from Python on 5.1.2 (KB11). For a single-clip export the exporter writes the **scene** range with key times starting at zero (KB26).
- The baked export Action has no Cycles modifier: bake exactly `range(K, L + 1)` (KB16, KB recipe 18).
- In-place locomotion: root travel stays out of the cycle; the controller owns displacement (AP:654, AP:813).

## 5. Sample, bake, export
- **Evaluated world positions** (for clip_check): `scene.frame_set(f)`; `ev = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())`; `ev.matrix_world @ ev.pose.bones[name].tail` (or `.head`, `.matrix`); save and restore `scene.frame_current` (KB13, RB14). `tools/anim/clip_check.py` `sample_clip()` does this; its positions stay in Blender's Z-up world, so run the checks with `--up z`.
- **Bake (Python route, preferred):** `bo = anim_utils.BakeOptions(only_selected=False, do_pose=True, do_object=False, do_visual_keying=True, do_constraint_clear=False, do_parents_clear=False, do_clean=False, do_location=True, do_rotation=True, do_scale=True, do_bbone=False, do_custom_props=False)`; `baked = anim_utils.bake_action(export_arm, action=None, frames=range(K, L + 1), bake_options=bo)`. It returns a new Action named "Action", assigns it, makes a slot, one LINEAR key per frame: rename it and re-assign the authoring Action afterwards (KB16).
- **Bake (operator route):** `bpy.ops.nla.bake(frame_start=K, frame_end=L, step=1, only_selected=False, visual_keying=True, clear_constraints=False, use_current_action=False, clean_curves=False, bake_types={'POSE'})` in Pose Mode with the armature active. Defaults lose constraint results (`visual_keying=False`: 0.4959 error in the test) or cancel ("Nothing to bake" with `only_selected=True` and nothing selected; select with `pose_bone.select`) (KB14, KB25, RB44).
- **Clean-curves off** until the project sets a tolerance: its threshold is a fixed 0.0001 on channel values, not a position error (KB15, BL31). Key reduction is accepted only against measured error at contacts, events and loop joins (BL31-BL32).
- **Export:** `roblox_fbx.export(path, kind="clip")` with the baked Action assigned and the scene range set (never Blender defaults: RB23). Fresh-scene round trip: `bpy.ops.wm.fbx_import` and sample again (RB34).
- **NLA reuse** (previews, combined clips): `tr = ad.nla_tracks.new(); st = tr.strips.new(name, start, act)`; `frame_end = frame_start + (action_end - action_start) * scale * repeat` (KB10). Clear `ad.action` first if the NLA should be the only source.

## 6. Minimal snippet (checked on 5.1.2 as `recipe.py`, J006-T04)
```python
import bpy
from bpy_extras import anim_utils
scn, arm = bpy.context.scene, bpy.data.objects["Ctrl"]          # the control armature from the manifest
scn.render.fps, scn.render.fps_base = 30, 1.0
scn.frame_start, scn.frame_end = 1, 25                          # loop K..L, pose 25 == pose 1
act = bpy.data.actions.new("Idle_Loop")
slot = act.slots.new(id_type='OBJECT', name=arm.name)
ad = arm.animation_data_create(); ad.action = act; ad.action_slot = slot
bag = anim_utils.action_ensure_channelbag_for_slot(act, slot)
INTERP = {e.identifier: e.value for e in bpy.types.Keyframe.bl_rna.properties['interpolation'].enum_items}
pb = arm.pose.bones["c_Head"]
fc = bag.fcurves.ensure(pb.path_from_id("rotation_euler"), index=1, group_name=pb.name)
keys = [(1, 0.0), (13, 0.26), (25, 0.0)]                       # frame, value (radians)
fc.keyframe_points.add(len(keys))
fc.keyframe_points.foreach_set('co', [x for k in keys for x in k])
fc.keyframe_points.foreach_set('interpolation', [INTERP['BEZIER']] * len(keys))
HANDLE = {e.identifier: e.value for e in bpy.types.Keyframe.bl_rna.properties['handle_left_type'].enum_items}
for side in ('handle_left_type', 'handle_right_type'):
    fc.keyframe_points.foreach_set(side, [HANDLE['AUTO_CLAMPED']] * len(keys))
fc.update()
m = fc.modifiers.new('CYCLES'); m.mode_before = m.mode_after = 'REPEAT'
assert len(fc.modifiers) == 1
```
