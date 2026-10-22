> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-craft`. Facts: `knowledge/reference/animation/fact-check-blender-keying.md` (KB rows; every name **run on Blender 5.1.2** headless, J006-T04), `knowledge/reference/rigging/fact-check-blender.md` (RB rows; 5.2.2 source reads). Paper: AP:542-701 (BL rows). MCP and headless rules: `rigging-craft` → `references/blender-mcp.md`. On 5.2, re-run the snippet in §6 once before the first real job (KB recipe 21). Revised by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (holds, handles, §7 game-camera and black-fill renders, §8 reading the samples; `View3DShading.single_color` checked in the bundled Blender API docs).

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
- **Holds while blocking:** make a hold as a copied key pair (copy every channel of the key to the later frame), so the preview runs with normal interpolation and shows the real timing between poses. `'CONSTANT'` (stepped) holds the value exactly until the next key (KB04): use it only for a quick pose-by-pose review, never as the only blocking preview, because it hides the in-between timing.
- **Shape eases with handles, not extra keys:** fewer keys per control are easier to read and retime; an added key can bend a curve unexpectedly.
- **Handles:** AUTO_CLAMPED does not overshoot a key value; AUTO can (3.0275 on a 3.0 peak in the test); VECTOR gives straight segments. Moving a key in time: `co_ui` moves the handles with it, `co` moves only the point — an overlap offset must move both (KB05, KB06; BL27).
- **Easing:** `Keyframe.easing` (AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT) applies to the SINE ... ELASTIC interpolation types (KB07). Key `type` (KEYFRAME, BREAKDOWN, MOVING_HOLD, EXTREME, JITTER, GENERATED) can mark blocking poses and breakdowns (KB04).
- **Interpolation per segment, not per clip:** contacts flat or hand-set, ballistic and mechanical motion with their own velocity profile, impacts hard (BL24). Weighted tangents (a habit from other tools) have no checked Blender equivalent: use handle types and handle positions.
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

## 7. Game-camera and black-fill renders (key frames)
- **Game camera:** one camera per asset from the game profile (third-person behind and above, or top-down; distance, height and vertical field of view as the game uses them; Roblox `Camera.FieldOfView` is vertical, so set `cam.data.sensor_fit = 'VERTICAL'` and `angle_y`). Render at a phone-like size (the game profile's floor device, or PROPOSAL 1170x540 landscape) with a player-sized reference block in frame. Save the transform in `renders/cameras.json` so every pass and every clip uses the same view.
- **Shaded key frames:** Workbench, `STUDIO` light, `TEXTURE` colour, Standard view transform, a capture of the game's ground behind the character where possible.
- **Black-fill from the same pass:** set `scene.display.shading.light = 'FLAT'`, `color_type = 'SINGLE'`, `single_color = (0, 0, 0)` and the world colour to magenta `(1, 0, 1)` (displays as `#FF00FF` under Standard, which `look_check.py` keys automatically); render the same frames; restore every setting in `finally` (the pattern of `tools/model/review_renders.py`). Then `python tools/art/look_check.py silhouette <frame.png>` (area, box, components: separated limbs show as separate components only where they really part) and `look_check.py thumb <frame.png> --size <phone size>`; `silhouette --compare` gives the aligned overlap of two poses (base vs variant, option A vs B). These measure; the read itself is judged by looking at the same ≤ 8 frames.
- **Strips:** for a mass or pop check, render consecutive frames of one short range only when a number (`pops`, a root jump) points there.
- **Contact sheet (plan stage):** render each key-pose option's black-fill once at the game camera, then tile them into one image per clip with a few lines of Python (Pillow: paste the frames side by side, label each option), resampled to phone size. One sheet per key clip is the whole plan-stage silhouette budget (`animation-design/references/review.md` §5).
- **Promo or cutscene still:** set the signature clip's key frame on the rig (never re-pose it from scratch), stage the camera the brief names for its premise, and render shaded plus a black-fill from the game camera; `look_check.py silhouette <still-black-fill> --compare <clip-key-frame-black-fill>` shows that it is the same pose (MEASURED).
- **Playable preview:** for a timing or feel pick by the owner at a gate, render the clip's frame range at the game camera as a video: Workbench, `render.image_settings.media_type = 'VIDEO'` (Blender 5.x; codec under `render.ffmpeg`), the clip's fps, then `bpy.ops.render.render(animation=True)`; restore the settings in `finally`. It is for the owner to watch at normal speed; you do not inspect its frames. Until the owner picks, the take with the better recorded reasons is used as a PROPOSAL.

## 8. Reading the samples (the curve lines of `animation-design/references/review.md` §8b)
`clip_check.py` measures length, loop seam, contact slide, events, ROM and pops. The other curve lines read the same samples file (`landmarks` and `controls` per frame) with a few lines of Python until the tool has a mode for them; report them as MEASURED unless the brief gives a tolerance.
| Line | Compute |
| --- | --- |
| Gravity spacing (S-07) | per-frame step length of the landmark; compare the mean step in the frames around the apex (height maximum) with the mean step near the ground |
| Arcs (S-08) | for each landmark, the longest run of frames whose points stay within a small distance of the straight chord between the run's ends |
| Stalled travel (S-06) | in the flight frames (no planted contact), runs where the root's horizontal step is near zero |
| Driver leads (S-04) | the first frame each of two landmarks or controls moves more than a small threshold from its start value; the driver's frame comes first |
| Push-off (S-05) | frames between the root's first rise and each foot's last contact frame |
| Hang time (S-09) | frames from launch to apex vs apex to landing on the root height |
| Landing depth (S-11) | the root height minimum after contact vs standing height and the stance limit in the rig sheet |
| Overshoot (S-12) | how many times the curve crosses its final value before settling, and by how much |
| Twinning (S-14) | the share of key frames the left and right controls have in common; the difference of their mirrored angles at key frames |
| Head lag (S-15) | the head's world yaw vs the chest's per frame; the lag in frames |
| Hold (B-10) | the largest pose change over the first frames of the clip |
