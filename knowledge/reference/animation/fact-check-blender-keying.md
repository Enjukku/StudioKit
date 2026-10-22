---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J006-T04
supersedes: []
---
> Author: fact-checker · claude-sonnet-5-5 · high · 2026-10-21

Scope: the Blender animation claims of `02-blender-roblox-process.md` §12.1 (CL01-CL46) and lessons BL01-BL39 / API list §1.4 that J005 did not check, plus a run-test on the installed Blender of every API name the keying recipe needs. J005 verdicts (RB rows) are in `knowledge/reference/rigging/fact-check-blender.md`. Roblox facts are not covered here. The paper file itself (`Animator_Research_Paper.txt`) is not in the repo, so "paper line" means the AP number in the CL table.

## 1. How I checked, and versions

All work on 2026-10-21. Every row says which version the evidence describes. Nothing from another version is used as proof for 5.1.2.

| tag | what | version |
| --- | --- | --- |
| RUN | Blender run headless on an empty scene: `"C:\Program Files\Blender Foundation\Blender 5.1\blender.exe" -b --factory-startup --python <scratch>.py`. Version printed: `bpy.app.version_string` = 5.1.2 release, build hash `ec6e62d40fa9`. Scratch scripts `p1.py` to `p7.py` and `recipe.py` are in the job scratchpad (not in the repo). No .blend file was opened or saved. | **5.1.2** |
| BUN | MCP-bundled docs (`search_api_docs`, `get_python_api_docs`, `search_manual_docs`). Same set J005 found to be 5.1. | 5.1 |
| INST | Python sources shipped with the install: `C:\Program Files\Blender Foundation\Blender 5.1\5.1\scripts\modules\bpy_extras\anim_utils.py` and `...\addons_core\io_scene_fbx\export_fbx_bin.py`. | 5.1.2 |
| RNA | Property description strings read from `bl_rna` in a RUN (the text the API reference is built from). | 5.1.2 |
| WEB | `blender.org` page through WebFetch (summarised by a small model, second-hand). | live |
| RB | J005 row; see its "How I checked" for M52, S522, RN sources (5.2 and 5.2.2). | per row |

Limits:
- **I did not run 5.2.** The papers pin 5.2.2; only 5.1.2 is installed. Where J005 read 5.2.2 source for the same name (RB30, RB39, RB40, RB43, RB44), the names agree with my 5.1.2 run. Where I found a behaviour only by running (cyclic flags, bake outputs, handle defaults), it is 5.1.2 evidence only and is marked "5.2: not checked".
- Verdicts as in J005: confirmed, corrected, partly, unverified, contradicted. "Extra" = a finding the paper did not claim.
- No API name, argument or default below comes from memory. Anything I could not source is in section 5.

## 2. CL to RB map

"RB" = a J005 verdict exists. "KB" = checked here (new evidence or a run-test of a name the recipe uses).

| CL | J005 row(s) | gap left by J005 | checked here |
| --- | --- | --- | --- |
| CL01-CL04 | RB29 (RB21) | none | not re-read |
| CL05 | RB30, RB15 | not run | KB19 |
| CL06 | none | release date | KB01 |
| CL07 | RB30 | not run | KB19 |
| CL08 | RB39 | required arguments | KB17 |
| CL09 | RB39, RB30 | not run | KB18 |
| CL10 | RB39 | API half not run | KB18 |
| CL11, CL12 | RB31, RB32 | none | not re-read |
| CL13, CL14 | RB33, RB34 (RB13) | none | not re-read |
| CL15, CL16, CL17 | RB35, RB14 | none | not re-read |
| CL18 | RB36, RB14 | none | not re-read |
| CL19, CL20 | RB37, RB38 | none | not re-read |
| CL21, CL22 | RB40, RB39 | not run | KB17 |
| CL23 | RB40, RB30 | not run | KB19 |
| CL24 | none | all | KB02 |
| CL25 | RB40 (names only) | "fast" claim, point defaults | KB03 |
| CL26 | RB40, RB41 | `BEZIER` id not opened, update() behaviour not run | KB04, KB05 |
| CL27 | RB51 (not run) | output string | KB20 |
| CL28 | RB50 | none | not re-read |
| CL29 | RB41 | handle types, "wider neighbourhood" | KB06, KB07 |
| CL30 | RB42 | none | not re-read |
| CL31 | none | all | KB21 |
| CL32 | RB49 | exporter use | KB12 |
| CL33 | RB43 | behaviour not run | KB08, KB09 |
| CL34 | RB43 | repeat / scale not run | KB10 |
| CL35 | RB44 | defaults and "no bound on drift" | KB14, KB15, KB16 |
| CL36, CL37 | RB12, RB45 | none | not re-read |
| CL38 | RB46 | not run | KB13 |
| CL39 | RB46 | none | not re-read |
| CL40, CL41, CL43, CL44 | RB47, RB48, RB33 | none | not re-read |
| CL42 | RB47 | none (step is in frames) | not re-read |
| CL45 | none | all | KB22 |
| CL46 | none | all | KB23 |

Coverage: 46 CL ids. No J005 verdict at all: CL06, CL24, CL31, CL45, CL46 (5). J005 verdict with a part left open that I closed: CL25, CL26, CL27, CL29, CL32, CL35 (6). Names J005 confirmed from docs and I re-confirmed by running: CL05, CL07-CL10, CL21-CL23, CL33, CL34, CL38 (13). Not re-opened: the other 22 (J005 stands). Not found: none.

## 3. Claims table

Paper line = AP number from the CL table. "5.2" in the last column = what I know about 5.2.

| id | claim (CL) | paper line | checked against (5.1.2 unless stated) | what it says | verdict | note |
| --- | --- | --- | --- | --- | --- | --- |
| KB01 | Blender 5.0 released 2025-11-18 (CL06). | AP:696 | WEB `blender.org/download/releases/5-0/` | Page date line: "The Blender team. November 18th, 2025". | confirmed | Second-hand (small-model summary). Low stakes. |
| KB02 | A freshly ensured F-curve has zero keyframe points (CL24). | AP:618 | RUN `p1.py`: `bag.fcurves.ensure('pose.bones["child"].rotation_quaternion', index=0, group_name="child")` | `len(fc.keyframe_points)` = 0, `fc.group.name` = "child", `fc.extrapolation` = 'CONSTANT'. A second `ensure` with the same path and index returned the same object (`fc2 == fc`, bag held 1 curve). | confirmed | So `ensure` is safe to call twice; the sketch's "assert 0 keys" guard works. Extra: `bag.groups` then lists "child". 5.2: not checked. |
| KB03 | `keyframe_points.add(n)` then `foreach_set('co', flat)` is the fast bulk path (CL25). | AP:620-622, 630 | RUN `p1.py`, `p5.py`; INST `anim_utils.py` lines 746-748; BUN `FCurveKeyframePoints` | `add(count)` allocates points. New points: `co` (0,0), `interpolation` 'BEZIER', both handle types 'AUTO_CLAMPED', `easing` 'AUTO', `type` 'KEYFRAME'. After `foreach_set('co', [1,1.0, 10,0.5, 20,1.0])` the handles were still (0,0) until `fc.update()`. Timing: 20,000 keys by add + foreach_set + update = 0.0046 s; 20,000 `insert(..., options={'FAST'})` + update = 0.36 s; 2,000 default `insert` = 0.14 s. Blender's own bake code uses the same path: `keyframe_points.add(n)`, `foreach_set("co", ...)`, `foreach_set("interpolation", ...)`. | confirmed | Corrects RB40 on one point: `add` is the fast path; `insert(..., options={'FAST'})` is faster than plain `insert` but about 80x slower than bulk here (one run, one machine). New-key interpolation and handle type come from user preferences (KB24), so set them. |
| KB04 | `key.interpolation = 'CONSTANT'` gives a hold (CL26); interpolation ids. | AP:624-628, 638 | RUN `p1.py`, `p5.py`; RNA `Keyframe.interpolation`, `Keyframe.easing` | Enum ids in order: CONSTANT, LINEAR, BEZIER, SINE, QUAD, CUBIC, QUART, QUINT, EXPO, CIRC, BACK, BOUNCE, ELASTIC. Integer values: CONSTANT 0, LINEAR 1, BEZIER 2, SINE 12 (others in `p5.py` output). Keys at 1, 7, 13, 25 with CONSTANT: `fcurve.evaluate` gives 0.0 at 6.9, 1.0 at 7 and 12.9, 3.0 at 13 and 24. RNA: interpolation is "the segment ... from this Keyframe until the next Keyframe". Setting `foreach_set('interpolation', [0]*n)` (ints) works and reads back as 'CONSTANT'. | confirmed | Closes the "`BEZIER` id not opened" gap in RB41. The last key's interpolation has no segment to act on. Keys 'type' ids: KEYFRAME, BREAKDOWN, MOVING_HOLD, EXTREME, JITTER, GENERATED. |
| KB05 | `curve.update()` sorts keys and fixes handles (CL26); `co` vs `co_ui`. | AP:628 | RUN `p1.py`, `p2.py`; RNA `Keyframe.co_ui`; BUN `FCurveKeyframePoints` | Keys added as (10,1.0),(1,0.0) read back unsorted until `update()`; after it they are sorted (1,0),(10,1). Handles are zero until `update()`. `co` moves the control point only (handles stayed); `co_ui` "also updates the handles". `keyframe_points.handles_recalc()`, `.sort()`, `.deduplicate()` exist. | confirmed | Matches RB40. Run-confirmed. |
| KB06 | Auto handles can overshoot; set handles by hand (CL29). | AP:638 | RUN `p5.py`; RUN `p1.py` (enum ids) | Handle type ids: FREE, ALIGNED, VECTOR, AUTO, AUTO_CLAMPED. Keys (1,0),(7,1),(13,3),(25,0) with BEZIER: AUTO_CLAMPED max over 1..25 = 3.0000; AUTO max = 3.0275 (overshoot). VECTOR on all four keys gave exactly linear (value 0.5 at frame 4). `foreach_set('handle_left_type', ints)` works. | partly | The overshoot of AUTO and the clamp of AUTO_CLAMPED are shown on one curve. The paper's "reshape a wider stretch" (smoothing reaching more than the neighbouring keys) is not tested; `FCurve.auto_smoothing` exists in the RUN property list but I did not test it. |
| KB07 | Easing is a separate control from handles (CL29). | AP:638 | RUN `p5.py`; RNA `Keyframe.easing` | `easing` ids: AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT. It applies to non-Bezier types (set on SINE, value at the middle of the segment 0.5). RNA: "Which ends of the segment ... easing interpolation is applied to". | confirmed | I did not measure easing on BEZIER; RNA text does not say it is ignored. Treat easing as a SINE...ELASTIC tool. |
| KB08 | Cycles REPEAT repeats a value range; REPEAT_OFFSET adds the end-point difference per cycle (CL33). | AP:654 | RUN `p2.py`, `p6.py`; BUN `FModifierCycles`; RNA | `fc.modifiers.new('CYCLES')` gives `mode_before`, `mode_after` = 'REPEAT' by default in this run, `cycles_before/after` = 0. Keys 1 to 25: period = last key frame minus first key frame = 24. REPEAT: `evaluate(26)` = `evaluate(2)` = 0.083, `evaluate(49)` = `evaluate(1)` = 0.0, and before the start `evaluate(-11)` = `evaluate(13)`. REPEAT_OFFSET with values 0 to 2: `evaluate(25)`=2.0, 26=2.083, 49=4.0, -11=-1.0, -23=-2.0. Modes: NONE, REPEAT, REPEAT_OFFSET, MIRROR. | confirmed | Run adds the period rule. The loop length is the key span, so first and last pose must be equal and the last key is the wrap frame, not an extra frame. |
| KB09 | Cycles modifier position and cycle count (extra to CL33). | AP:654 | RUN `p6.py`; BUN `FModifierCycles` | `modifiers.new('CYCLES')` after a NOISE modifier does not add it: Blender logs "Cannot add 'Cycles' modifier to F-Curve, as it can only be first in stack", the call raises no Python exception and the stack stays ['NOISE']. `cycles_after=2` with REPEAT_OFFSET: values 2, 4, 6 at frames 25, 49, 73, then 2.0 at 74 and 97 (falls back to the curve's own extrapolation, constant). 0 = infinite (BUN text). | confirmed | Extra. Add Cycles before any other modifier and check `len(fc.modifiers)` after. |
| KB10 | NLA Repeat, time scale and ranges reuse clips (CL34). | AP:654 | RUN `p3.py`; BUN `NlaStrip` | `tr.strips.new("name", 1, act)` (action with slot) gave `frame_start` 1, `frame_end` 25, `action_frame_start/end` 1 and 25, `action_slot` set. `strip.repeat = 3.0` gave `frame_end` 73; then `strip.scale = 0.5` gave `frame_end` 37. At scene frame 7 the strip evaluated action frame 13 (quaternion 0.707, 0.707, 0, 0). Ranges (BUN): `repeat` 0.1 to 1000, `scale` 0.0001 to 1000; `blend_type` ids REPLACE, COMBINE, ADD, SUBTRACT, MULTIPLY; default REPLACE. | confirmed | `frame_end = frame_start + (action_end - action_start) * scale * repeat` fits all numbers. Combine = quaternion math is RB43. |
| KB11 | Action cyclic and manual-range flags (supports BL28 loop policy). | AP:654 | RNA `Action.use_cyclic`, `use_frame_range`, `frame_range`, `curve_frame_range`; RUN `p2.py`, `p6.py`; manual `animation/animation_editors.rst` (BUN, "Cycle-Aware Keying") | RNA: `use_frame_range` "this range is used by some tools, but does not affect animation evaluation"; `use_cyclic` "enabling this does not automatically make it loop"; `frame_range` = manual range if set, else the curve range. Run: `frame_range` (1,25) with `use_frame_range=True`, `curve_frame_range` (0,0) before any key. The manual says a new curve in a cyclic manual-range Action becomes cyclic automatically. In scripts it did not: `fcurves.ensure` + `keyframe_points.add` left `modifiers` empty, and three `PoseBone.keyframe_insert` calls on such an Action also left it empty. | confirmed (flags); contradicted for scripts (auto-cycle) | The manual's auto-cycle is a UI keying feature; do not rely on it from Python. Add the Cycles modifier yourself (KB08, KB09). 5.2: not checked. |
| KB12 | Effective scene rate is `fps / fps_base` (CL32). | AP:644 | RUN `p3.py`, `p7.py`; INST `export_fbx_bin.py` lines 2063, 2326, 3329 | Factory scene: `render.fps` 24, `fps_base` 1.0. Setting 30 and 1.001 gave 29.97003. `fps_base` hard limits 1e-5 to 1e6. The FBX exporter computes `fps = r.fps / r.fps_base` for key times (line 2326) and for the file's time mode (line 3329). | confirmed | RB49 covered the manual; this adds the exporter source. The factory default is 24, not 30: set it. |
| KB13 | `scene.frame_set` plus the evaluated depsgraph gives constrained results (CL38). | AP:678 | RUN `p3.py`, `p4.py`, `recipe.py`; RNA `Scene.frame_set` | `sc.frame_set(f)`; `ev = arm.evaluated_get(bpy.context.evaluated_depsgraph_get())`; `ev.matrix_world @ ev.pose.bones[name].tail` gave the expected positions on an armature moved to x=5 (tail (5,0,2) at rest, (7,-1,1) at frame 13). A Damped Track constraint result was read the same way. `frame_set` leaves `frame_current` at the last frame set (13 after my loop). | confirmed | Restore `frame_current` yourself. In this run `arm.pose.bones[n].tail` read directly after `frame_set` also matched; the docs do not promise that, so use the evaluated object. |
| KB14 | Bake Action with visual keying captures final constrained transforms (CL35). | AP:660 | RUN `p4.py`, `p5.py`; BUN `bpy.ops.nla.bake` | World tail error vs the constrained reference, constraints muted afterwards: `bpy.ops.nla.bake(frame_start=1, frame_end=25, visual_keying=True, only_selected=True, bake_types={'POSE'})` 0.0; same call with `visual_keying=False` 0.4959 (the constraint result is lost); `anim_utils.bake_action(..., do_visual_keying=True)` 0.0. With the default `only_selected=True` and no bone selected: "Nothing to bake", result `{'CANCELLED'}`. | confirmed | Confirms the RB44 default trap by running. |
| KB15 | Clean-curves removes redundant keys with no bound on visual error (CL35). | AP:660 | INST `anim_utils.py` lines 651-670; BUN `bpy.ops.nla.bake`; RUN `p5.py` | The operator has no tolerance argument. The clean code deletes a key when `abs(val - val_prev) + abs(val - val_next) < 0.0001` (curve values, not world positions) and the value was not in the curve before the bake. Run: `do_clean=True` left 20 curves, key counts {2, 25}, world error 1e-6 on a smooth test. | confirmed | "No bound" is right: the threshold is a fixed 0.0001 on channel values. A 0.0001 rotation change at a long lever can still move a tip; measure in world units (BL31/BL32). |
| KB16 | Bake outputs (extra to CL35; needed for the export copy). | AP:660 | RUN `p4.py`, `p5.py`; INST `anim_utils.py` lines 440-455, 726-748 | `bpy.ops.nla.bake` makes a new Action named "Action" (then "Action.001"...) and assigns it to the object; the authoring Action stays as a separate datablock. `anim_utils.bake_action(obj, action=None, frames=range(a, b+1), bake_options=BakeOptions(...))` returns the new Action and also assigns it to `obj.animation_data`. Slot is created with the object's name (`name_display` "Armature", `identifier` "OBArmature"). Baked keys: one per frame, interpolation LINEAR, handle AUTO_CLAMPED. `frames=range(1,26,2)` gave 13 keys per curve. `BakeOptions` fields: only_selected, do_pose, do_object, do_visual_keying, do_constraint_clear, do_parents_clear, do_clean, do_location, do_rotation, do_scale, do_bbone, do_custom_props. | confirmed | The baked Action has no Cycles modifier (run: 0 on every baked curve), so bake the frames you want in the file. Rename the result and re-assign the authoring Action afterwards. |
| KB17 | `armature.animation_data_create()`, `ad.action`, `ad.action_slot`, `bpy.data.actions.new`, `action.slots.new(id_type=, name=)` (CL08, CL21, CL22). | AP:598-606 | RUN `p1.py` | All work as written. `slots.new()` without `name` raises TypeError (`required parameter "name" not specified`); without `id_type` the same. A new slot: `identifier` "OBArmature" (= "OB" + object name), `name_display` "Armature", `target_id_type` 'OBJECT'. After only `ad.action = act` the single slot was already in `ad.action_slot`. | confirmed | Set `ad.action_slot` anyway (BL17: assign the slot explicitly). |
| KB18 | `action_ensure_channelbag_for_slot(action, slot)` creates or finds a channelbag; layers and strips exist in the API (CL09, CL10). | AP:588, 608 | RUN `p1.py` | First call: 1 layer with 1 strip of type 'KEYFRAME'; `action_get_channelbag_for_slot(act, slot)` then returned the same object. `Channelbag` properties: `fcurves`, `groups`, `slot`, `slot_handle`. `Action` has `layers`, `slots`, `is_action_layered`, `is_action_legacy`. | confirmed | UI half of CL10 is RB39. |
| KB19 | Legacy Action API gone; `group_name` is the channelbag argument (CL05, CL07, CL23). | AP:548, 616 | RUN `p1.py` | `act.fcurves`, `act.groups`, `act.id_root`: AttributeError "'Action' object has no attribute ...". `bag.fcurves.ensure(p, index=1, action_group="child")`: TypeError, "expected (data_path, index, group_name)". | confirmed | Run proof on 5.1.2; RB30 gives the 5.0 release-note source. |
| KB20 | Bone data paths come from `path_from_id` (CL27). | AP:612 | RUN `p1.py` | `arm.pose.bones["child"].path_from_id("rotation_quaternion")` returned `pose.bones["child"].rotation_quaternion`. | confirmed | Closes the "I did not run it" note in RB51. |
| KB21 | Quaternion scalar Bezier curves do not give uniform angular speed (CL31). | AP:650 | RUN `p5.py` (my own numeric test; no doc exists) | Rotation of 160 degrees about Z over 24 frames, four quaternion component curves. LINEAR: per-frame angle 4.87 to 8.00 degrees (mean 6.67), mid-frame quaternion length 0.766 before normalising. BEZIER (auto-clamped): 0.57 to 11.95 degrees per frame. | confirmed | The claim is true for both LINEAR and BEZIER component curves. Evidence is a test, not a doc. |
| KB22 | Orientation error `2*acos(clamp(abs(dot(q_ref, q_test)), 0, 1))` (CL45). | AP:666 | RUN `p5.py`: `mathutils.Quaternion.rotation_difference(...).angle` | Both gave 2.792526 rad for a 160 degree difference. | confirmed | Radians. The `abs` makes q and -q equal, as wanted. |
| KB23 | A 30 fps interval is 100/3 ms, 60 fps is 50/3 ms (CL46). | AP:644, 698 | arithmetic | 1000/30 = 33.333... = 100/3; 1000/60 = 16.666... = 50/3. | confirmed | Pure arithmetic. |
| KB24 | (Extra) New-key defaults and bone rotation mode. | not in paper | RUN `p1.py`, `p7.py` | `preferences.edit.keyframe_new_interpolation_type` = 'BEZIER' and `keyframe_new_handle_type` = 'AUTO_CLAMPED' in factory settings (the RNA default of `Keyframe.interpolation` reads CONSTANT, but points from `add` came out BEZIER). A new armature's pose bone `rotation_mode` = 'QUATERNION'; a new Object's = 'XYZ'. | confirmed | Do not trust defaults: a user preference can change them. Key `rotation_quaternion` for bones, or set `rotation_mode` first. |
| KB25 | (Extra) Bone selection API. | not in paper | RUN `p4.py`, bone property listing | On 5.1.2 `Bone` has `hide`, `hide_select` but no `select`; `PoseBone.select` exists (and `EditBone.select`). `bone.select = ...` raises AttributeError. | confirmed | Matters for `nla.bake(only_selected=True)`: set `pose_bone.select = True`. The 5.0/5.1 note that introduced this is not read. |
| KB26 | (Extra) What the FBX exporter bakes for one clip. | not in paper (supports CL40-CL42) | INST `export_fbx_bin.py` lines 2595, 2621, 2325-2330 | With All Actions and NLA Strips off, the exporter writes one stack over `scene.frame_start` to `scene.frame_end`. With All Actions on it uses `act.frame_range` per Action. Key times are rebased to start at zero (`real_currframes = currframes - f_start if start_zero`). | confirmed | Consistent with RB52. So `Action.frame_range` (manual range when `use_frame_range`) matters only for the All Actions route; for one clip set the scene range. |

## 4. Keying recipe the craft book can rely on

Every name below was run on Blender 5.1.2 (RUN) or read in the 5.1.2 install (INST). The assembled script `recipe.py` (steps 1-8 below) ran clean on an empty scene. 5.2: names agree with J005's 5.2.2 source reads (RB40, RB44); behaviours marked "5.1.2 only" are not checked on 5.2.

1. **Pin first.** Record `bpy.app.version_string` (5.1.2 here) and the build hash; run the recipe on the version the studio ships with (RB28, RB22).
2. **Scene rate.** Set `scene.render.fps` and `fps_base` yourself; factory default is 24 / 1.0; effective rate = `fps / fps_base`; the FBX exporter uses the same ratio (KB12). Set `scene.frame_start` / `frame_end` to the clip range.
3. **Action and slot.** `act = bpy.data.actions.new(name)`; `slot = act.slots.new(id_type='OBJECT', name=arm.name)` (both arguments required); `ad = arm.animation_data_create()`; `ad.action = act`; `ad.action_slot = slot` (KB17).
4. **Channelbag.** `bag = bpy_extras.anim_utils.action_ensure_channelbag_for_slot(act, slot)`; the get helper `action_get_channelbag_for_slot` returns the same object (KB18, RB39). Do not touch `act.fcurves`, `act.groups`, `act.id_root`: they are gone (KB19, RB30).
5. **Curve per channel.** `path = pose_bone.path_from_id("rotation_quaternion")`; `fc = bag.fcurves.ensure(path, index=i, group_name=bone_name)`; a new curve has 0 keys and calling `ensure` twice returns the same curve (KB20, KB02). Argument is `group_name`, not `action_group`.
6. **Batch keys.** `kp = fc.keyframe_points; kp.add(n); kp.foreach_set('co', [f0, v0, f1, v1, ...]); fc.update()`. 20,000 keys took 5 ms; per-key `insert` took 360 ms (KB03). Check inputs first (finite, strictly rising frames; BL19).
7. **Set what the key does, per key.** Defaults come from user preferences, so always write them: `kp.foreach_set('interpolation', [INTERP[name]] * n)` with `INTERP = {e.identifier: e.value for e in bpy.types.Keyframe.bl_rna.properties['interpolation'].enum_items}`; same for `handle_left_type` / `handle_right_type` (ids FREE, ALIGNED, VECTOR, AUTO, AUTO_CLAMPED). Call `fc.update()` after (KB03, KB04, KB05, KB24).
8. **Stepped blocking.** Interpolation `'CONSTANT'` holds each key's value until the next key (value changes exactly at the key frame). Switch the same keys to `'BEZIER'` or `'LINEAR'` later with `foreach_set` and `fc.update()` (KB04).
9. **Handles.** `AUTO_CLAMPED` does not overshoot a key value; `AUTO` can (3.0275 on a 3.0 peak in the test); `VECTOR` handles give straight segments. Moving a key: `co_ui` moves the handles with it, `co` moves the point only (KB05, KB06).
10. **Easing.** `Keyframe.easing` ids AUTO, EASE_IN, EASE_OUT, EASE_IN_OUT; use it with SINE...ELASTIC types (KB07). Key `type` ids (KEYFRAME, BREAKDOWN, MOVING_HOLD, EXTREME, JITTER, GENERATED) can mark blocking poses (KB04).
11. **Rotation.** Key one rotation mode per bone; for bones `rotation_mode` is 'QUATERNION' by default. Quaternion component curves (LINEAR or BEZIER) do not give even angular speed; judge orientation, not components (KB21, RB42, KB24).
12. **Loop policy.** Make the last key pose equal the first. For a `K..L` loop add a Cycles modifier on every curve: `m = fc.modifiers.new('CYCLES'); m.mode_before = m.mode_after = 'REPEAT'` (or `'REPEAT_OFFSET'` for travelling channels). The period is `L - K`. It must be the first modifier or Blender refuses silently (check `len(fc.modifiers)`). `cycles_before/after` = 0 means infinite (KB08, KB09, RB43).
13. **Action cyclic range.** `act.use_frame_range = True; act.frame_start = K; act.frame_end = L; act.use_cyclic = True` are intent flags only: they do not affect evaluation and do not add the modifier from Python (KB11, 5.1.2 only). The exporter reads `act.frame_range` only on the All Actions route; for one clip set the scene range (KB26, RB52).
14. **Read evaluated world positions.** `scene.frame_set(f)`; `ev = obj.evaluated_get(bpy.context.evaluated_depsgraph_get())`; `ev.matrix_world @ ev.pose.bones[name].tail` (or `.head`, or `.matrix`). Save and restore `scene.frame_current` (KB13, RB14, RB18).
15. **Bake the export copy (Python route, preferred).** `bo = anim_utils.BakeOptions(only_selected=False, do_pose=True, do_object=False, do_visual_keying=True, do_constraint_clear=False, do_parents_clear=False, do_clean=False, do_location=True, do_rotation=True, do_scale=True, do_bbone=False, do_custom_props=False)`; `baked = anim_utils.bake_action(obj, action=None, frames=range(K, L + 1), bake_options=bo)`. It returns a new Action named "Action", assigns it to the object, makes a slot named from the object, one LINEAR key per frame (KB16). Rename it, re-assign the authoring Action and slot afterwards.
16. **Bake via operator (if needed).** `bpy.ops.nla.bake(frame_start=K, frame_end=L, step=1, only_selected=False, visual_keying=True, clear_constraints=False, use_current_action=False, clean_curves=False, bake_types={'POSE'})`, in Pose Mode with the armature active. Defaults to distrust: `visual_keying=False` (loses constraint results, 0.4959 error in the test), `only_selected=True` (nothing selected cancels with "Nothing to bake"; select with `pose_bone.select = True`, not `Bone.select`) (KB14, KB25, RB44).
17. **Clean-curves.** Leave `do_clean` / `clean_curves` off until a tolerance is set: the threshold is a fixed 0.0001 on channel values, not a position error (KB15, BL31).
18. **The baked Action has no Cycles modifier.** Bake exactly the frames that go in the file (KB16).
19. **NLA reuse.** `tr = ad.nla_tracks.new(); st = tr.strips.new(name, start_frame, act)`; `st.repeat`, `st.scale`; `frame_end = frame_start + (action_end - action_start) * scale * repeat` (KB10). Clear `ad.action` first if the NLA should be the only source.
20. **Single clip export.** With All Actions and NLA Strips off the exporter writes the scene range, with key times starting at zero (KB26, RB52, RB23).
21. **Names are version-stable inside 5.x, but not forever.** `ensure(... group_name=)` needs 5.0 or newer (RB30). On 5.2 re-run `recipe.py` once before the first real job (not done here).

Assembled check run (RUN `recipe.py`, 5.1.2): range (1.0, 25.0); one Cycles modifier on every curve; value at frame 37 equals value at frame 13 (0.9659); world tail (0,0,2.0) at frames 1, 25 and 37 is at frame 13 (0,-0.6,1.866); baked Action "Idle_Loop_export" has 20 curves, 25 keys each, 0 modifiers; effective fps 30.0.

## 5. Dropped, unverified, or limited

| item | action | reason |
| --- | --- | --- |
| Manual statement "new curves in a cyclic manual-range Action become cyclic automatically" (CL33 context, BL28) | Do not use in scripts | Not true for `fcurves.ensure`, `keyframe_points.add` or `PoseBone.keyframe_insert` on 5.1.2 (KB11). It holds for UI keying only, as far as the manual says. |
| BL21 "automatic handles may reshape a wider stretch" | Keep as OPINION | Overshoot shown (KB06); the wider reach is not tested. `FCurve.auto_smoothing` exists but was not run. |
| Behaviour on 5.2 | Unverified | Only 5.1.2 is installed. Run `recipe.py` first on 5.2.2 if the studio moves. |
| "Bone.select" in older recipes | Do not use | Absent on 5.1.2 (KB25). |
| Easing on BEZIER keys | Unverified | Not measured (KB07). |
| Quaternion sign continuity of baked keys, and the choice between equal rotations at a degenerate constraint | Unverified | My bake test used a degenerate Damped Track at one point and the two bake routes chose different but equal orientations; world positions matched (KB14). Not a claim about quaternion sign. |
| CL01-CL04, CL11-CL20, CL28, CL30, CL36, CL37, CL39-CL44 | Not re-opened | J005 verdicts stand (section 2). |
| Speed numbers in KB03 | Single run, one machine | Order of magnitude only. |
| Roblox's treatment of Cycles, NLA or baked loops | Out of scope | This file is Blender only. Roblox import and loop behaviour: `fact-check-roblox-runtime.md`. |
