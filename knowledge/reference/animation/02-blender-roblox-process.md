---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T05, Animator_Research_Paper.txt lines 542-1145
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Animation paper part 2: Blender and MCP workflow, Roblox runtime and phone cost, AI motion tools, hand-offs, review, 15 gates, timing library

Paraphrased notes on paper lines 542-1145 (sections 9-14, "Do not do", "Open questions", the 26-action timing library, the numerical ledger). Source IDs and dates are resolved from the paper's source register (AP:1146-2056). The paper stays outside git. Nothing here was fact-checked: every number and every Roblox, Blender and AI-tool fact is listed in table CL (section 12); every conflict and scope limit is in table LM (section 11). Part 1 of the paper (lines 1-541) is in `01-body-motion-timing.md`. The rigger reads section 10.2 first.

## 0. How to read

| Key | Meaning |
| --- | --- |
| AP:n | Line n of `Animator_Research_Paper.txt`. A range means the lesson spans those lines. |
| Tag | Evidence tag copied from the paper: VERIFIED, EXPERIENCE, OPINION, UNSPECIFIED (U), UNKNOWN. Combined tags are kept as the paper wrote them. Where the paper gives no inline tag, the tag of the register entry is used and the cell says "(register)". |
| Src | Paper source ID. P00 is the paper's own protocol (OPINION, 2026-10-21), not an outside source. Resolved list in section 13. All register entries were checked on 2026-10-21 (AP:1148). "Undated" means no trustworthy date was found, not 2026. |
| Stage | Workflow stage from `knowledge/jobs/J005-character-rigger/workflow.md`: S0 intake, S1 motion needs (animator), S2 rig plan (rigger), S3 geometry (modeler), S4 geometry acceptance (rigger), S5 rig + tests (rigger), S6 rig acceptance (animator), S7 animate and export (animator), S8 owner final. |
| [for-rigger] | The rigger must know it, supply it, or test it (rig manifest fields, export skeleton, importer, rig type, AnimationController vs Humanoid, Motor6D vs Bone, AnimationConstraint, IKControl, rigid vs skinned cost, root-motion policy). |
| Prefix IDs | BL Blender workflow lesson (section 9), RT Roblox runtime lesson (section 10), AI AI motion tool lesson (section 11), HC hand-off lesson (section 12), RV review lesson (section 13), GT gate, DN do-not item, OQ open question, TL timing library row, NL numerical ledger item, CL claim to check, LM contradiction or limit. |
| CL id note | The spec asked for claim ids C01... They are written CL01... because C01-C23 are paper source IDs (for example C06, C10, C12, C15, C18 appear here). Claim cross-references in the lesson tables are in the last column. |

Section map (paper to this file):

| Paper part | AP lines | This file |
| --- | --- | --- |
| 9 Blender Python and MCP animation workflow | 542-701 | section 1 |
| 10 Roblox pipeline runtime and mobile cost | 703-881 | section 2 |
| 11 AI motion tools current in 2026 | 883-965 | section 3 |
| 12 Work with rigger, modeler, VFX, sound, UI | 967-992 | section 4 |
| 13 Review from rendered evidence and runtime captures | 994-1034 | section 5 |
| 14 End-to-end process (15 gates) | 1036-1100 (gates 1040-1068, rule table 1096-1100) | section 6 |
| Do not do | 1070-1088 | section 7 |
| Open questions requiring production evidence | 1090-1094 | section 8 |
| Timing library for 26 named actions + exact numerical ledger | 1102-1144 | section 9 |
| Source register | 1146-2056 | section 13 |

Global caveats the paper states about itself: no device benchmark was run (AP:705); no AI tool was generated, installed, uploaded or benchmarked (AP:885); the Blender sketch is not executed code (AP:592); no animation or performance benchmark was created (AP:1148); the MCP operations are proposals, not features of an official Blender MCP (AP:634). Where a table says U, UNSPECIFIED or UNKNOWN, the number must come from the project or a measurement, never from this file.

---

## 1. Section 9: Blender Python and MCP animation workflow (AP:542-701)

### 1.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | AP | claims |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BL01 | Pin in every job manifest: Blender executable, exact build hash, exporter/add-on version, documentation version. | S5, S7 | [for-rigger] | OPINION (last sentence of the version paragraph) | D01-D03 | 546 | CL01 |
| BL02 | Latest stable located: 5.2.2 LTS, 2026-09-15. The 5.2 line began 2026-07-14, supported through July 2028. Daily builds show 5.2.3 RC, 5.3 Beta, 5.4 Alpha, no newer stable. 4.5.14 LTS is still supported but is not the latest stable line. | S5, S7 | [for-rigger] | VERIFIED | D01, D02, D03 | 546, 695 | CL01-CL04 |
| BL03 | Blender 5.0 removed action.fcurves, action.groups and action.id_root. They are not safe shortcuts. Use slots and channelbags with the slot's target ID type. The channelbag F-curve argument is group_name, not the old action_group. | S5, S7 | [for-rigger] | VERIFIED | D04 | 548, 696 | CL05-CL07 |
| BL04 | Source conflict, FBX: the 5.2 FBX Legacy manual gives a scale default of 10 while the pinned 5.2 exporter API declares global_scale=1.0; the manual lists vertex shape keys as unsupported while 5.1 release notes describe exporting shape-key normals. Prefer the pinned API and release notes plus a target round-trip test. Do not repeat the stale limitation list. | S5, S7 | [for-rigger] | VERIFIED | D26, D28, D29 | 552, 701 | CL11, CL12 |
| BL05 | Source conflict, glTF: the manual still has old name-based track-merging text but records that since 4.4 Actions mode merges by Action. NLA Tracks mode still groups by name, so the export mode matters. | S5, S7 | [for-rigger] | VERIFIED | D27 | 554 | CL13 |
| BL06 | Native FBX import exists, but the manual still sends FBX export to the add-on. A new importer does not imply a different exporter API. | S5 | [for-rigger] | VERIFIED | D30 | 556 | CL14 |
| BL07 | Armature bone data to read: names, parent/children, rest matrix_local, head_local, tail_local, length, deform and inheritance flags. Bone-local Y runs head to tail. Envelope radii describe skin influence, not limb thickness. Bone.convert_local_to_pose respects inheritance and local-location settings. | S5 | [for-rigger] | VERIFIED | D08, D34 | 562 | CL15-CL17 |
| BL08 | Per pose bone, read: active rotation mode, location/rotation/scale values, locks, IK flags and limits, constraints, custom properties. Two matrices differ: PoseBone.matrix is the end result after constraints and drivers (armature-object space), matrix_basis is the offset from parent and rest bone. For a world-space pose, multiply the evaluated matrix by the armature object's world matrix. | S5, S7 | [for-rigger] | VERIFIED | D09 | 564 | CL18 |
| BL09 | Constraints to read: type, validity, influence, mute, target and subtarget, owner and target spaces; for IK also chain length and pole settings, for limits their axes. Passing validity says nothing about anatomy. A Limit Rotation constraint is ignored on IK-driven bones, so read the IK limits there. | S5 | [for-rigger] | VERIFIED | D10, D33 | 566 | CL19 |
| BL10 | For objects, record parenting (object and bone), hierarchy, transforms, topology, armature modifiers, skin weights, shape keys and drivers. Bounds are corner points in object space. Evaluated meshes include modifier results; free temporary meshes when done; any re-evaluation makes earlier evaluated references stale. | S5 | [for-rigger] | VERIFIED | D11, D12 | 568 | CL20 |
| BL11 | Save a rig manifest (fields in 1.2). Build a parent-to-children map once instead of re-walking the recursive hierarchy. | S5 | [for-rigger] | OPINION | P00 | 570 | |
| BL12 | Sort every statement into one of three layers. Observed: values read from the file (bone transforms, vertices, control names, weights, set joint limits, measured lengths and bounds). Inferred: guesses such as tail_03 being a tail segment or a symmetric end part being a foot; store the evidence and a confidence, and cross-check names against hierarchy, weighted geometry and images. Authored or unknown: masses, mass distribution, center of mass, stiffness, personality, safe anatomical range, intended gait, how much exaggeration is acceptable. Bone lengths and dimensions cannot supply these, so ask the modeler, rigger or director instead of inventing kilograms, delays or limits. | S1, S5, S6 | [for-rigger] | OPINION | P00 | 572-578 | |
| BL13 | On a single skinned mesh the overall bounding box says nothing about individual limbs. Derive provisional regions from skin influences plus topology, compute bounds per region and mark them approximate. A fat stylized thigh and its thin control bone measure differently. Neither envelope radius (as thickness) nor the mean of bone positions (as center of mass) may be reported as physical fact. | S5, S6 | [for-rigger] | OPINION | P00 | 580 | |
| BL14 | Before any animation, render the rest pose and some representative poses from front, back, side, three-quarter and, where useful, top and bottom. Label joints, show a ground scale, add orthographic geometry views and the planned gameplay camera. Small isolated controller tests on a throwaway copy can show what drives what and which way each axis points; reset state after each test. One flattering three-quarter picture is not enough to deduce how a wing folds. | S6 | [for-rigger] | OPINION | P00 | 582 | |
| BL15 | Hand the motion-profile fields in 1.3 to the rigger and director. | S1, S2 | [for-rigger] | OPINION | P00 | 584 | |
| BL16 | A slot groups the animation of one kind of data-block inside an Action. The pose channels of an armature live in the armature object's Action under a slot. In 5.2 the official helpers create or look up the matching channelbag (the lookup returns the first one that fits). The API also has Action layers and strips, which does not imply a finished multilayer Action UI. NLA remains its own composition system. | S5, S7 | [for-rigger] | VERIFIED | D05, D06, D07 | 588 | CL08-CL10 |
| BL17 | Give each deliverable clip its own named Action and assign the slot explicitly. Leave the source rig and the authoring Action alone; author and export on isolated copies or collections whose active Action, NLA state, frame range and selection you know. Keep clip IDs, event times, contact intervals, loop policy and locomotion policy in data, not in display names. A file with several layers or strips must be enumerated; the first channelbag may hold only part of the motion. | S5, S7 | [for-rigger] | OPINION | P00 | 590 | |
| BL18 | The §9 pseudocode is a design sketch, not executed code. API calls it relies on are claims to check, not working code (list in 1.4). Its two helpers (flatten_frame_value_pairs, planned_channels) are proposed application code, not Blender built-ins. The paper calls the "API basis" VERIFIED but only at documentation level (D05, D06, D04, D16, D17, D15, D36). | S7 | | OPINION (sketch); VERIFIED (doc basis) | D04-D06, D15-D17, D36 | 592-630 | CL21-CL27 |
| BL19 | Write curves in batches and answer with a short diff and a validation report instead of dumping the scene after every key. Cache curve lookups per (slot, data_path, array_index). Check paths before allocating; refuse NaN, Inf and repeated times. Do motion planning outside Blender, but run all Blender changes serially inside Blender's own context. Operators rely on context and may fail their poll, so call them deliberately for bake, export and render only. Blender cautions against Python in background threads. | S7 | | OPINION; cautions supported by D31, D32 | P00, D31, D32 | 632 | CL28 |
| BL20 | Seven proposed MCP operations (contracts in 1.5). | S5, S7 | [for-rigger] | OPINION | P00 | 634 | |
| BL21 | A key's interpolation describes the span from that key to the next. Constant holds the pose; linear removes jumps in value but not in velocity; Bezier uses handles; easing modes and handles are separate tools. Automatic handles may reshape a wider stretch and overshoot, so set interpolation and handles by hand instead of trusting defaults. | S7 | | VERIFIED | D14, D19 | 638 | CL29 |
| BL22 | Block: solve intent, support/contact, silhouette, balance, tool grip, direction changes and timing with stepped poses. Keep root/hips and contacts coherent before secondary motion. Render real holds, not a smooth preview that hides missing decisions. | S7 | | OPINION | P00 | 642 | |
| BL23 | Breakdown stage: lay out paths between poses, moving holds, passing positions, lead and follow, arcs. Write event and contact times in seconds together with exact source frames, using the effective rate fps/base. Formula: frame = origin + seconds x effective_fps. A 30-fps interval lasts exactly 1000/30 ms and a 60-fps interval exactly 1000/60 ms; do not substitute rounded constants. | S7 | | OPINION; fps/base VERIFIED | P00, D35 | 644 | CL32, CL46 |
| BL24 | Splining: pick interpolation channel by channel and segment by segment. Planted contacts may want flat or hand-set tangents, ballistic or mechanical motion may need a deliberate velocity profile, impacts may need hard changes. Easing every joint in and out is the wrong default. | S7 | | OPINION | P00 | 646 | |
| BL25 | Polish by reading position, velocity and acceleration from screen-space and 3D trajectories and by watching at real speed. Remove foot slide, shoulder/hand compensation errors, tool lag, limb snaps, clipping, drifting holds and loop seams. Every piece of secondary motion needs a cause; noise is not a cause. | S7 | | OPINION | P00 | 648 | |
| BL26 | Euler channels are readable but gimbal-prone; quaternion channels are harder to edit; keep one rotation mode per keyed animation. Keep the rig's chosen mode unless conversion is validated. Generated quaternions: normalize and keep sign continuity. Generated Euler: choose equivalents continuous with the previous frame. Judge orientations and end-effectors, not component curves. Do not assume quaternion scalar Bezier curves give uniform angular-speed SLERP. | S7 | [for-rigger] (inf.: rotation mode of control bones) | VERIFIED (modes); OPINION (rules) | D18, P00 | 650 | CL30, CL31 |
| BL27 | An overlap offset moves things in time: shift a key's time and both of its Bezier handles together, otherwise the curve shape changes. Do not delay a planted foot or a constrained grip merely because it sits deeper in the hierarchy. Phases for tails and ears need body-specific reference or authored rules; the paper found no verified universal frames-per-joint rule. | S7 | | OPINION | P00 | 652 | |
| BL28 | Cycles REPEAT loops a value range; REPEAT_OFFSET adds the start-to-end difference on each pass. NLA strips can repeat, scale time and trim ranges; NLA Combine composes quaternions rather than adding components. At the loop wrap check both pose and derivatives, avoid doubling the end pose as an extra hold, and keep travel of the root separate from the in-place locomotion policy. Repeating one scalar cycle is not a locomotion controller. (Roblox's editor gives different loop-end advice: LM11.) | S7 | [for-rigger] (root travel vs in-place) | VERIFIED (modifiers); OPINION (checks) | D20, D21, P00 | 654 | CL33, CL34 |
| BL29 | Retarget by anatomical role and rest-frame alignment, not by matching names or copying Euler numbers. Establish source and target rest transforms, hierarchy, bone orientation, scale and contact mapping. Solve target end-effectors and proportions with temporary constraints or IK; include a root/hip displacement policy. Check reachable contacts and the target's range of motion before publishing. | S7 | [for-rigger] (target rest frames, ROM) | OPINION | P00 | 658 | |
| BL30 | Bake Action can capture final constrained transforms with visual keying; clearing constraints without a proper bake can change the result. Its clean-curves option removes redundant keys but promises no bound on foot drift or visual error. Bake a duplicate export rig, keep an untouched reference, validate after removing constraints, drivers and controllers, then exclude non-export controls. Capture object transforms too when they contribute. Exported files carry evaluated motion, not Blender control-rig semantics. | S5, S7 | [for-rigger] | VERIFIED (bake, constraints not saved); OPINION (procedure) | D22, D28, P00 | 660 | CL35, CL36 |
| BL31 | Blender's decimate can work by ratio or by a maximum allowed curve deviation. A ratio promises nothing perceptual. Protect the start and end of contacts, impacts, event markers, extremes, clip edges and loop joins. Set project tolerances before reducing; the paper gives no universal figures. Test on a dense time grid that includes times between keys: end-effector or contact position error in stated world units; orientation error (CL45); root path and total displacement; contact slip, penetration and timing; landmark and silhouette change in the gameplay camera. | S7 | | VERIFIED (decimate); OPINION (metrics) | D23, P00 | 662-672 | CL37, CL45 |
| BL32 | Accept a deletion only when all relevant tolerances hold and event times are unchanged; otherwise put the keys back. A small change in a proximal angle can throw a long weapon tip far off its arc. Measure the baked and the imported result, not just the authoring curves. A constant key can be what overrides another blended Action, so a channel that looks unchanged locally may still be needed. | S7 | | OPINION | P00 | 674 | |
| BL33 | scene.frame_set evaluates a frame; the evaluated depsgraph gives driven, constrained and modifier results. render(animation=True) renders the animation range; Workbench is built for fast animation previews. | S7 | | VERIFIED | D12, D13, D24, D25 | 678 | CL38, CL39 |
| BL34 | Render short, repeatable image sequences at the declared playback rate, then make a real-speed preview, a slowed diagnostic and annotated contact sheets. Keep camera, framing and frame IDs identical for before/after pairs. Add a ground grid, contact markers, colored body regions and motion-path overlays. After import also record the actual Roblox camera view. Frame-skipping renders prove nothing about the frames they skip. | S7 | | OPINION | P00 | 680 | |
| BL35 | Look at the whole body first, working from hips and support through torso and head, limbs and tool, to secondary parts. Pair each image with numbers: world-space foot speed during contact, penetration depth, joint angle changes, tip paths, root displacement, quaternion continuity, event times. An AI image reviewer should log frame, view, error, cause and severity and suggest a local fix, then rerender. Numbers cannot settle appeal, comic timing, acting or personality; the owner or director decides those. | S7, S8 | | OPINION | P00 | 682 | |
| BL36 | The FBX exporter lets you choose selected objects, leaf bones, which Action or NLA clips to write, sampling and simplification. Its bake_space_transform option is still flagged as experimental or broken for armatures and animation. The sampling step counts frames, not frames per second. glTF offers separate Action, active-action, NLA-track and scene export modes. | S5, S7 | [for-rigger] | VERIFIED | D26, D27 | 686 | CL40-CL43 |
| BL37 | A starting point for tests, not a universal preset: keep skeleton names, hierarchy and rest matrices; export only the checked rig and geometry; no extra leaf bones; name the clips, range and frame rate; export evaluated animation; leave exporter simplification at 0.0 first so later reduction has a known baseline; skip the experimental transform baking. Apply the axis and unit conversion once and confirm it with an asymmetric motion and an object of known size. Do not apply transforms on an already bound rig. Key the required target channels on purpose rather than every control and custom property of the source. | S5, S7 | [for-rigger] | OPINION | P00, D26 | 688, 699 | CL44 |
| BL38 | Current Roblox interoperability: the Animation Clip Editor GA of 2026-03-31 supports multi-clip FBX and glTF import, replacing older one-clip-per-export advice; importer unit, axis and rig-type options must be honored. Do not assume native root motion from a present API property: a dated Roblox source says root motion was unreleased in January 2026 and no later release was found. Do not call a Blender export default Roblox's universal axis, FPS, skeleton-name or root-motion rule. Import success alone does not prove the same runtime result. | S5, S7 | [for-rigger] | VERIFIED | R06, R26 | 690 | CL63, CL64, CL110 |
| BL39 | Check an export by comparing the imported result with the source on: bone identity and rest pose, size, orientation, clip length, sample times, end-effector contacts, root policy, loop boundary and event mapping. Also test blending, transitions and device speed in Roblox. A smaller key count does not show a cheaper Roblox runtime, since exporters and importers may resample or restructure the data. | S5, S7 | [for-rigger] | OPINION | P00 | 692 | |

### 1.2 Rig manifest (AP:570) and job manifest pins (AP:546), complete

| # | field | note |
| --- | --- | --- |
| 1 | stable IDs | |
| 2 | human-readable names | |
| 3 | rest matrices | |
| 4 | world/rig unit conversion | record exactly once (BL37) |
| 5 | frame rate | effective rate = fps/base (BL23) |
| 6 | controllers versus deform/export bones | rigging note K01 asks for the same split |
| 7 | asset hash | |
| 8 | uncertainties | |
| pin a | Blender executable | job manifest (BL01) |
| pin b | exact build hash | |
| pin c | exporter/add-on version | |
| pin d | documentation version | |

### 1.3 Motion-profile fields to hand to the rigger and director (AP:584, complete, 16)

| # | field | # | field |
| --- | --- | --- | --- |
| 1 | body plan | 9 | mass source or unknown |
| 2 | anatomical role per region | 10 | allowable ROM source |
| 3 | controller/deformer mapping | 11 | source of secondary motion |
| 4 | primary driver | 12 | loop/contact constraints |
| 5 | contact surface | 13 | gameplay-camera importance |
| 6 | local axes | 14 | timing source |
| 7 | rest orientation | 15 | inference confidence |
| 8 | measured length and bounds | 16 | export participation |

### 1.4 API calls the pseudocode relies on (AP:594-628). Claims to check, not working code.

| # | call or assumption in the sketch | AP | basis the paper cites | claim |
| --- | --- | --- | --- | --- |
| 1 | armature.animation_data_create(); ad.action = action; ad.action_slot = slot | 598-606 | D05 | CL21 |
| 2 | bpy.data.actions.new(clip_name); action.slots.new(id_type='OBJECT', name=armature.name) | 600-602 | D05 | CL22 |
| 3 | anim_utils.action_ensure_channelbag_for_slot(action, slot) | 608 | D06 | CL09 |
| 4 | bag.fcurves.ensure(path, index=component, group_name=group) | 616 | D04 (ensure migration) | CL23 |
| 5 | a freshly ensured curve has 0 keyframe points (assert guards against wiping user curves) | 618 | none given | CL24 |
| 6 | curve.keyframe_points.add(n); curve.keyframe_points.foreach_set('co', flat list) | 620-622 | D16, D17 | CL25 |
| 7 | key.interpolation = 'CONSTANT' for the block pass; curve.update() | 624-628 | D14, D15, D19 | CL26 |
| 8 | bone data paths from path_from_id, not string concatenation | 612 | D36 | CL27 |
| 9 | proposed application code, not built-ins: flatten_frame_value_pairs, planned_channels (prevalidated, sorted, deduplicated, finite) | 610, 622, 630 | P00 | none |

### 1.5 Proposed MCP operation contracts (AP:634). PROPOSED, OPINION, not an official Blender MCP feature set.

| # | operation | note |
| --- | --- | --- |
| 1 | inspect_rig | rigging note proposes an operation with the same name (RP K08 list) |
| 2 | render_views | |
| 3 | write_action_batch | |
| 4 | sample_pose | |
| 5 | edit_curves | |
| 6 | bake_export_copy | rigging note names the near-equivalent bake_export_skeleton |
| 7 | validate_roundtrip | rigging note names the near-equivalent validate_export |

Common contract for every operation: input takes a scene/asset revision, a clip ID and bounded inputs; output returns changed IDs, warnings, result paths, timing and errors. No operation may silently rename bones, apply transforms, change the rest pose or overwrite a good clip. The two proposals (this paper and the rigging paper) use different vocabularies: LM21.

### 1.6 Section 9 rule table (AP:694-701, copied as data)

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Latest stable release located | 5.2.2 LTS; not 5.2.3 RC or 5.3 beta | VERIFIED | D01-D03; 2026-09-15 patch; checked 2026-10-21 |
| Legacy Action API removal | Blender 5.0 | VERIFIED | D04; 5.0 release notes, 2025 |
| Action access | explicit slots and channelbags | VERIFIED | D05-D07; 5.2 docs, undated; checked 2026-10-21 |
| Timing basis | 30 fps interval = 100/3 ms; 60 fps = 50/3 ms | VERIFIED arithmetic | exact conversion; 2026-10-21 |
| Export reduction baseline | simplification 0.0 is a test setting, not performance advice | OPINION | P00 using D26; 5.2 API; checked 2026-10-21 |
| Key reduction tolerance | UNKNOWN until the project defines it | OPINION | P00; 2026-10-21 |
| FBX scale and shape-key documentation | conflicting manual/API/release text | VERIFIED | D26, D28, D29; 5.1-5.2 docs; checked 2026-10-21 |

---

## 2. Section 10: Roblox pipeline runtime and mobile cost (AP:703-881)

This section keeps four things apart: documented platform behavior, dated releases, developer measurements and proposed tests. No device benchmark was run for the paper, and public evidence sets no universal safe phone budget for bones, tracks, keys or characters at once (AP:705).

### 2.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | AP | claims |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RT01 | Evidence scope: public sources do not set a safe phone budget for bones, tracks, keys or concurrent characters. The evidence reviewed is R18, R24, R25 and R31. | S5, S7 | [for-rigger] | OPINION | P00 | 705 | |
| RT02 | Importer facts: FBX and glTF both bring rig, skin and animation. glTF/GLB may add one more Model level and a MeshPart per primitive, which FBX does not. Rig Type choices are R15, Custom and No Rig; a custom creature need not satisfy every Marketplace avatar-body rule. Axis (forward/up) and scale-unit settings are exposed. Zero-influence bones are dropped by default, so switch Keep Zero Influence Bones on deliberately where they are needed. Importing a model, importing an editable clip and publishing an animation asset are three separate operations. | S5 | [for-rigger] | VERIFIED | R01 | 709 | CL47-CL50 |
| RT03 | Blender FBX guide for Roblox: Apply Scalings = FBX Unit Scale. Bake Animation is off for static exports and kept when exporting animation keys. These are general FBX instructions; they do not mean every Blender control, constraint, modifier or driver survives. Test a scene-specific preset by round-trip inspection. | S5, S7 | [for-rigger] | VERIFIED | R02 | 713 | CL51 |
| RT04 | General rigging rules: unit scale, zero rotations, root at the origin, no vertex influence from the root. A single mesh may import up to 20,000 triangles; that is an import limit, not a mobile target per character. The page's one-track export remark is out of date or narrower than the later multi-clip ACE release, so say which import path you mean. The page sets no general maximum for bones, keyframes or duration. | S2, S5 | [for-rigger] | VERIFIED | R03, R06 | 717 | CL52-CL55 |
| RT05 | Skin influences are held in the mesh asset and the skeleton is made of Bone instances. Bones move the look of parts but not their collision shape. A one-mesh NPC (paper wording: R1) is supported, with less standard R15 animation and humanoid integration. The name R15 counts 15 meshes, not necessarily 15 skeletal joints. | S2, S5 | [for-rigger] | VERIFIED | R04, R05 | 721 | CL57-CL59 |
| RT06 | For avatar bodies the spec fixes named parts, a rig schema, +Z forward and +Y up, and Marketplace component budgets. Advanced R15 allows up to 37 extra optional bones or joints; they are not all mandatory and they are no phone budget. Triangle ceilings: head 4,000, torso 1,750, each arm or leg 1,248, summing to 10,742. These validate avatar assets; they are not demands on custom NPCs nor safe low-end totals. Optional joint names and mapping matter. Extra face or hand detail is not worth adding just because the schema permits it. | S2, S5 | [for-rigger] | VERIFIED | R05 | 725 | CL60-CL62 |
| RT07 | ACE import (release): FBX and glTF files, several clips in one file, saved locally under the clip name, with a rest-pose choice. A local save must still be published before runtime use. The GA notes mention a fixed 180-degree rotation bug from the beta. Both Studio import routes now share the import code; Import 3D uploads animations straight away, while ACE lets you edit and preview first. | S5, S7 | [for-rigger] | VERIFIED | R06 | 729 | CL63-CL65 |
| RT08 | Platform-avatar update: optional finger joints (15 per hand) plus spine, chest, clavicle, head-base and toe-base joints for R15 platform avatars, tied to HRD/DRD/AJU. Standard R15/R6 still work. Torso and head extras needed client 720 at rollout. The post says far-away avatars can have leaf bones dropped by throttling. That is a platform optimization; it does not show that custom rigs get bone LOD or that added bones are free on every phone. | S2, S5 | [for-rigger] | VERIFIED | R07 | 733 | CL66-CL68 |
| RT09 | Adaptive Animation GA: HRD maps humanoid skeletons for cross-rig reuse; DRD maps fingers. Beta naming changed Pelvis to Spine and Left/RightToes to Left/RightToeBase. Standard R6/R15 need no manually added HRD for basic compatibility. Retargeting does not replace checking contact, height and silhouette on each target. Humanoid retargeting is not arbitrary creature locomotion; a GA release is not zero regressions. | S5, S7 | [for-rigger] | VERIFIED | R08 | 737 | CL69-CL71 |
| RT10 | AnimationConstraint: when AJU is on, R15 avatar joints are AnimationConstraints, not Motor6Ds. The old C0/C1/Part0/Part1 names survive as read-only aliases, so class checks must cover the new class. Apply layered transforms in PreSimulation, after the Animator has evaluated, and allow for throttled evaluation. Kinematic mode follows the animation; force-based mode brings in physics, and a full physical ragdoll is not priced like a kinematic clip. | S5 | [for-rigger] | VERIFIED | R09 | 743 | CL72-CL74 |
| RT11 | Motor6D links two BaseParts; bones are not substitutes because they bear no collision. For procedural motion prefer Transform over editing C0/C1; Transform is not replicated like an ordinary property. The Animator normally overwrites it between PreAnimation and PreSimulation, and deferred transform updates are applied in a batch. Mechanical custom rigs may still use Motor6Ds, but not every modern character joint is one. | S5 | [for-rigger] | VERIFIED | R10 | 747 | CL75, CL76 |
| RT12 | Priority is settled joint by joint. Higher-priority tracks supply influence until the weights total one; tracks of equal priority share by normalized weight. From highest: Action4, Action3, Action2, Action, Movement, Idle, Core. Core's number 1000 does not rank it first. An overlay should key only the joints it means to drive. This is blending logic and does not promise that loaded or masked tracks cost nothing. | S7 | | VERIFIED | R11 | 751 | CL77, CL78 |
| RT13 | Animator rules: LoadAnimation makes a track, so keep and reuse tracks (or fetch with GetTrackByAnimationId) instead of loading on every input. The Animator has to be in Workspace first. GetPlayingAnimationTracks also lists fading-out tracks, so IsPlaying alone understates active influence. EvaluationThrottled marks skipped pose evaluation. The API text says PreferLodEnabled=false forces full fidelity and Workspace can turn throttling off; R17 disagrees (LM03). The network-ownership remark under LoadAnimation must not override the replication contract in RT14. | S7 | | VERIFIED | R12 | 755 | CL79-CL83 |
| RT14 | Replication: a server-created Animator inside the owning player's Character lets that player's client play tracks that replicate. NPC animation must be loaded and started on the server to replicate on its own. Tracks on a client-created Animator never replicate. Client-only NPC visuals therefore need explicit syncing of high-level state and time, with gameplay logic owned by the server; they are not authoritative hitboxes and can differ in timeline between clients. Physics network ownership is a different question from client gameplay authority. | S5, S7 | [for-rigger] (where the Animator is created) | VERIFIED | R13 | 759 | CL84 |
| RT15 | Track facts: Length is zero until the track has loaded; Play takes fade, weight and speed; AdjustWeight changes weight over time. Use GetMarkerReachedSignal for named markers (KeyframeReached is deprecated). Stop begins a fade-out and does not destroy; Stopped can fire before influence has fully gone, while Ended fires after the fade-out and suits disposing a one-shot track. Keep reusable tracks stopped and destroy them on teardown. Stop(0) has a documented freeze caveat with Motor6D MaxVelocity=0. Destroying a track does not prove memory returns at once. | S7 | | VERIFIED | R14 | 763 | CL85-CL89 |
| RT16 | IKControl solves a chain toward a target each frame and can sit over authored animation. Turn it off with Enabled=false; setting weight to 0 leaves smoothing and pole effects active. The paper recommends runtime IK only for visible, meaningful contact fixes, and comparing shorter chains or authored solutions on target hardware. No sourced per-chain phone cost or count limit exists. | S5, S7 | [for-rigger] | VERIFIED; OPINION (reserve IK) | R15, P00 | 767, 860 | CL90 |
| RT17 | Roblox performance advice, as summarized: run NPC animators locally to cut server simulation and replication; use AnimationController where Humanoid features are not needed; pool rigs that respawn often; spawn by proximity; turn off unused humanoid states; avoid scale and hierarchy changes. Named profiling scopes: stepAnimation, stepHumanoid, updateInvalidatedFastClusters. A server-side TweenService replicates property changes every frame, so tween cosmetics locally. Strip saved animation metadata from shipped or cloned rigs; disconnect connections and drop table references. Each measure removes specific work; none certifies a rig or removes the phone's cost. | S5, S7 | [for-rigger] (AnimationController vs Humanoid) | VERIFIED | R16 | 771, 862 | CL91-CL93 |
| RT18 | Phase 3 of client animator throttling: per the Roblox Team it becomes always on, covers locally created characters, and lowers the pose rate for far or offscreen rigs. The reported 25-30% animation-CPU saving comes from an internal crowded-scene test, not per-phone timing or a total-FPS promise. PreferLodEnabled=false is only a hint under resource pressure (conflicts with R12). Reply 6 claims track clocks and marker events keep running while posing is skipped, but its author's role is unverified: treat it as a forum explanation. Test offscreen procedural effects and marker timing. | S7 | | VERIFIED (register); reply 6 unverified | R17 | 775, 864 | CL94-CL97 |
| RT19 | MicroProfiler: judge frame-time consistency, not average FPS alone. A 30 FPS frame is exactly 100/3 ms and a 60 FPS frame exactly 50/3 ms, for the whole frame rather than an animation allowance. Profile on a phone to see real thermal and power limits; desktop Studio can hide issues. The tool splits animation, physics, scripts and rendering; add custom scopes around procedural code. Gather target-device and server captures, memory and repeated-spawn behavior before asserting a budget. | S7 | | VERIFIED | R18 | 779 | CL98, CL99 |
| RT20 | ContentProvider: PreloadAsync yields and reports each asset's final fetch status through the callback; a failing asset logs an error and the call still returns, so read the statuses. Preload only imminent, critical animations, then load and cache tracks per Animator. Do not hold entry back for every clip of a large game, and do not read a changing RequestQueueSize as progress. | S7 | | VERIFIED | R19 | 783, 858 | CL100 |
| RT21 | Track cap: BloxHerder separates concurrent playback from the number of loaded clips; the remark followed abuse countermeasures. Older 256 warnings and a temporary 32 cap are history. 64 is the latest reported engine safeguard, not a target. It gives no safe mobile track count. The poster's staff role was not verified, so name BloxHerder only. | S7 | | EXPERIENCE | R20 | 787 | CL101 |
| RT22 | Track limit logs: the October reply reports continued 64-track warnings with avatar walk animations and marker trouble. It supports the cap and motivates diagnostics for leaked or duplicate tracks. It does not prove a universal engine defect or that this project would reproduce it. | S7 | | EXPERIENCE | R21 | 791 | CL102 |
| RT23 | Animation Graphs (full release): run live, build on the animation asset and track system, and cover blending, sequencing, masking and layering visually. LoadAnimation scripts keep working. The paper advises choosing a graph for maintainability or animator control, not novelty, and measuring graph, clip, rig and churn costs against direct tracks. | S7 | | VERIFIED; OPINION (when to use) | R22, P00 | 797 | CL103 |
| RT24 | State Machines and Expressions are a Studio-only beta, unlike released graphs. They describe animation transitions, not Humanoid gameplay states, and expressions read graph parameters only, not arbitrary world properties. Shipping low-end mobile content must not depend on the beta. | S7 | | VERIFIED | R23 | 801 | CL104 |
| RT25 | Pixel 6a report (Khrrxs; Android 17, Roblox 2.743.1136): batches of 20 local R15 rigs played a graph for 10 s, were destroyed and left for 20 s. Three graph rounds kept +133, +120 and +54 MB of total memory, whereas ordinary-keyframe rounds showed no such growth. Studio Animation-tag readings suggested about 5.7 MB per new graph track. It is a described report, not this studio's reproduction nor a confirmed leak, and total memory is noisy. Add graph spawn/despawn/respawn memory tests and do not assume Stop or Destroy frees memory immediately. | S7 | | EXPERIENCE | R24 | 805 | CL105-CL107 |
| RT26 | Large NPC custom renderer (me7474): server single-part proxies, 10 Hz bucketed and parallel updates, compressed replication, client interpolation, a custom keyframe evaluator, distance culling. Reported scaling from trouble around 3-4k to 10k client NPCs. Device and framerate details are too thin for a phone budget; many variables changed; it neither isolates bones from Motor6D nor proves that bypassing Animator is better. Its 256-bones-per-mesh remark is developer commentary, not an importer cap. | S7 | [for-rigger] (do not use 256 as a cap) | EXPERIENCE | R25 | 809 | CL108, CL109 |
| RT27 | Root motion: a documentation reply dated 2026-01-21 says Animator.RootMotion was not released although it appears in the API, and no later public release was found. The September 2026 RDC roadmap lists new default movement with root motion for Early 2027, which is a plan, not a release. Do not assume automatic physical root-motion extraction from the property or from a moved root bone. The paper's recommendation: author locomotion in place and let the gameplay controller own displacement, unless a tested, supported root-motion setup is chosen on purpose. | S2, S5, S7 | [for-rigger] | VERIFIED (R26, R32); OPINION (default policy) | R26, R32, P00 | 813 | CL110, CL111 |
| RT28 | Marketplace animation packs: standard R15, original work, CurveAnimation not KeyframeSequence, looping except Jump. The ten-second limit is for pack uploads, not every experience animation; do not repeat it as a global runtime limit. Upload counts and fees do not matter for a custom-NPC performance budget. | S7 | | VERIFIED | R27 | 817, 880 | CL112 |
| RT29 | Animation Editor: its timeline shows seconds:frames at 30 FPS, which is a display for authoring and not evidence that runtime evaluation runs at 30. Reduce redundant keys and preview the error. A loop does not blend from its last key back to its first, so repeat the first pose at the end. Publish for runtime use and pick the group creator for group-owned experiences. Key reduction simplifies data; no proportional runtime gain is established. | S7 | | VERIFIED | R30 | 821 | CL113 |
| RT30 | 1,000-assembly report (laindecat): gains were credited to testing on a separate local server, Motor6D movement in place of BulkMoveTo, and one-part skinned rigs. Hardware is not given and several things changed together. It counters simple claims but is neither a low-end phone benchmark nor proof that one method always wins. | S7 | [for-rigger] | EXPERIENCE | R31 | 825 | CL114 |
| RT31 | Rig construction choice: a skinned custom mesh suits strong deformation and many visual joints, since it avoids one BasePart per visual bone, but skinning, rendering and evaluation still cost time. Separate rigid parts with joints suit physical pieces and rigid mechanisms. Cost is driven by the number of visible rigs, deforming vertices, effective influences, parts, materials and draw calls, collision bodies, IK chains, active blends and spawn/despawn churn, not by bones alone. Settle it with a controlled A/B test; neither bones nor Motor6Ds are cheaper in general. | S2, S5 | [for-rigger] | OPINION | P00 | 829 | CL115 |
| RT32 | Simple movers: a door, a bobbing pickup or similar mechanical motion can use TweenService or a small procedural transform, skipping the skeletal pipeline. That lowers authoring effort and is not proof of lower CPU. Server-side cosmetic tweens add replication traffic (R16). Replacing a validated skeletal system by per-bone Lua loops without profiling is risky: you may lose engine LOD, replication and tooling and add per-frame cost. | S2, S7 | [for-rigger] | OPINION | P00, R16 | 831 | |
| RT33 | Gameplay and markers: damage, hits, cooldowns and authoritative movement must not rely on a visual marker seen only by one client. Markers fit footsteps, VFX and local sound; server timing needs its own validation and a state or clock design. Test markers at low framerate, late join, network delay, streaming in and out, interruption and looping. Throttling visibility is not the same as removing an actor, and render LOD need not be animation LOD. | S7 | | OPINION | P00 | 833 | |

### 2.2 Roblox animation budget table (AP:835-844, copied as data)

The paper leaves every maximum UNSPECIFIED. A platform ceiling is not a mobile target backed by evidence. The sole concurrent-track figure found is a reported 64 playing tracks on a single character, which is neither a recommendation nor a count of cached clips. Standard R15 compatibility describes a schema, not a bone budget. Tags: EXPERIENCE R20, R21; OPINION P00 (AP:837).

| character type | max bones | max simultaneous tracks | keyframe guideline | client or server | source (as written) |
| --- | --- | --- | --- | --- | --- |
| Player | UNSPECIFIED phone budget | UNSPECIFIED phone budget | cut redundant channels and keys only after an error comparison | owning client may play on the server-created Character Animator; gameplay authority stays separate | R13, R18; docs undated, checked 2026-10-21; P00 |
| Nearby NPC | UNSPECIFIED | UNSPECIFIED | keep contacts, the attack silhouette and transition behavior | server start for automatic replication, or a defined client visual-state protocol | R13, R16; docs undated, checked 2026-10-21; P00 |
| Pet | UNSPECIFIED | UNSPECIFIED | favor recognizable locomotion and interactions | cosmetic motion on the client; authoritative gameplay and position where needed | R16, R18; docs undated, checked 2026-10-21; P00 |
| Distant crowd | UNSPECIFIED | UNSPECIFIED | distance tiers set by measurement, simpler motion and rigs | client-side presentation or proxies are an option, not free | R25; 2026-09-21; P00 |
| Animated prop | UNSPECIFIED | UNSPECIFIED | keep only the articulated channels needed; compare with a simple mover | authority follows collision and gameplay; local cosmetic transforms where suitable | R10, R16; docs undated, checked 2026-10-21; P00 |

### 2.3 Controlled phone acceptance test (AP:846-850, OPINION P00)

| # | item |
| --- | --- |
| 1 | Name the lowest supported devices, frame-time target, resolution, thermal state and a representative scene. |
| 2 | To isolate animated joints, clip count, key density, blending or IK, keep meshes, materials and collisions fixed. |
| 3 | Compare skinned and rigid-part builds separately at the same visible quality. |
| 4 | Include peak visible populations, near/far/offscreen transitions, camera cuts, simultaneous actions, first-use loading, streaming and slow networks. |
| 5 | Record the frame-time distribution and spikes, animation/physics/script/rendering scopes, network traffic and memory. |
| 6 | Repeat spawn, despawn and respawn, and compare direct-track and graph variants. |
| 7 | Save client/engine version and asset hashes. |
| 8 | Accept only when total scene performance and visual/timing fidelity pass together; keep a measured budget record per asset tier, because until those exist no universal integer maximum can be defended. |

### 2.4 Optimization and lifecycle checklist (AP:852-870, all 9)

| id | item | tag | src | AP |
| --- | --- | --- | --- | --- |
| LC01 | Stay within four bone or joint influences per vertex; that is an influence limit, not a bone-count cap. | VERIFIED | R03 | 854 |
| LC02 | Keep and reuse the tracks you intend to use rather than a fresh LoadAnimation result per input; stopping and destroying are different lifecycle steps. | VERIFIED | R12, R14 | 856 |
| LC03 | Preload only imminent essential assets and read each asset's fetch status; a return from PreloadAsync does not mean success. | VERIFIED | R19 | 858 |
| LC04 | Disable unused IK with Enabled=false; weight zero is not equivalent. | VERIFIED | R15 | 860 |
| LC05 | Avoid needless hierarchy or scale invalidation, keep cosmetic motion local where it fits, and release event connections and references at teardown. | VERIFIED | R16 | 862 |
| LC06 | Plan for throttled posing under resource pressure and test it; do not assume a preference setting beats always-on throttling. | VERIFIED R17; conflict R12 | R17, R12 | 864 |
| LC07 | Cut keys only against an approved error measure and an imported comparison; no verified runtime saving per removed source key exists. | OPINION | P00 | 866 |
| LC08 | Track duration, file size, unique curves, keys, export samples, deform joints, influenced vertices and active tracks separately, because each measures a different cost. | OPINION | P00 | 868 |
| LC09 | Test fresh loads, concurrent blends, death and respawn, cancellation and repeated actor churn on a real phone, not a single idle rig in Studio. | OPINION | P00 | 870 |

### 2.5 Section 10 rule table (AP:872-881, copied as data)

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Influences per vertex | maximum 4 | VERIFIED | R03; undated docs; checked 2026-10-21 |
| Multi-clip FBX and glTF import | GA 2026-03-31 | VERIFIED | R06; dated update |
| Platform avatar optional fingers | 15 joints per hand; released, not a phone budget | VERIFIED | R07; 2026-05-04 |
| Concurrent playing-track ceiling located | reported 64 per character; not cached clip count or budget | EXPERIENCE | R20; 2026-01-26; R21; 2026-10-04 |
| Animation Graphs | released 2026-07-15 | VERIFIED | R22; dated release |
| Graph state machines and expressions | Studio-only beta | VERIFIED | R23; 2026-10-08 |
| Phone bones tracks keys and actor maxima | UNSPECIFIED universal budgets | OPINION (evidence limit) | R18, R25, R31; checked 2026-10-21 |
| Marketplace animation pack duration | at most 10 s per clip, pack scope only | VERIFIED | R27; undated docs; checked 2026-10-21 |
| Low-end phone frame allowance | 100/3 ms at 30 fps; 50/3 ms at 60 fps, whole frame | VERIFIED arithmetic | R18; undated docs; exact conversion |

---

## 3. Section 11: AI motion tools current in 2026 (AP:883-965)

Five lanes of primary-source claims and limits, not an independently reproduced quality ranking. No tool was run, installed, uploaded or benchmarked for the paper. Feature availability, output quality and commercial permission are three separate checks (AP:885, OPINION P00). Stage for all rows: S7 (motion source), with S1 for choosing what to ask for; [for-rigger] only where the tool's skeleton limits matter.

### 3.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | AP | claims |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AI01 | Scope: the section lists current claims and limits per tool; availability, authored-output quality and commercial permission are checked separately. | S1, S7 | | OPINION | P00 | 885 | |
| AI02 | Kimodo (offline, controllable humanoid generation). The current Rigplay models are Kimodo-SOMA-RP-v1.2 and Kimodo-SOMA-RP-ArdyRep-v1.2, released 2026-10-15, so neither the March launch nor April's v1.1 is current. The repo ships Python inference, a CLI and an authoring demo. Results come out as joint, root and contact data in NPZ (plus skeleton-specific variants); no verified direct Roblox exporter exists. Code is Apache-2.0; SOMA and G1 weights fall under NVIDIA Open Model terms and the SMPL-X variant under different NVIDIA R&D terms. | S7 | | VERIFIED | A01, A04 | 889 | CL116-CL118 |
| AI03 | Kimodo accepts text, pose keyframes, joint positions and rotations, paths and waypoints. Documented limits: 10 s of motion per prompt; under 20 constrained frames per constraint type (root path excepted). SOMA predicts 30 joints and converts them to a 77-joint export, with most hand and finger detail dropped inside the model. 77 exported joints therefore do not mean 77 learned articulations or a DOF count. | S7 | [for-rigger] (77-joint export skeleton is not the project skeleton) | VERIFIED | A02, A03 | 891, 959 | CL119-CL122 |
| AI04 | ARDY (streaming). Newest listed human checkpoints: ARDY-SOMA-RP-30FPS-Horizon60 and ARDY-SOMA-RP-30FPS-KimodoRep-Horizon60, dated 2026-10-15. Earlier Core checkpoints run at 20 FPS; generation and export rate is model-specific. CLI NPZ holds joint rotations and positions, root motion, foot contacts and FPS. The text encoder needs access to gated Llama weights. | S7 | | VERIFIED | A06 | 893, 960 | CL123, CL124 |
| AI05 | ARDY's July 2026 paper reports a 33 ms mean generation latency for its four-step interactive diffusion demo, run on an RTX 4090 with a 40-frame window at 20 FPS. It says nothing about the October 30-FPS models, a Roblox runtime, networking or Blender integration. The authors admit the model is purely kinematic, so skating or jitter can occur and physical dynamics are absent. | S7 | | VERIFIED (reported experiment) | A07 | 895, 960 | CL125, CL126 |
| AI06 | Paper opinion: use Kimodo and ARDY for humanoid base motion or in-betweens given explicit spatial constraints, while hands, props, collision and contacts are authored separately. A Python or MCP wrapper can run inference and Blender cleanup, but it adds neither motion understanding nor contact correctness. | S7 | | OPINION | P00 | 897 | |
| AI07 | Rokoko Vision 3.0 (single-camera capture) joined Create on 2026-07-16; the dual-camera and web-camera modes ended on 2026-08-16, so older tutorials describe a retired workflow. Present flow: upload a recorded video, refine and retarget in Studio, export FBX or BVH. Finger tracking is absent at launch. Vendor quality comparisons are marketing, not independent tests. | S7 | | VERIFIED | A08, A09 | 901 | CL127, CL128 |
| AI08 | Rokoko rights: the Create FAQ allows commercial use of generated text-to-motion and video-to-motion data. The terms (v2.0.1, 2026-07-16) separate user content, vendor assets and downstream use, contain anonymized-data and sublicensing clauses, and bar automated access without separate permission. Being allowed to export a clip is not permission to automate the service or to train another model on the assets. | S7 | | VERIFIED | A10, A11 | 903 | CL129 |
| AI09 | DeepMotion Animate 3D turns video into body, face and hand motion and exports FBX, BVH and GLB. Hand results depend on visible hands, limited occlusion and a compatible finger skeleton; commercial rights depend on plan; foot-lock modes can keep or disable grounding. Its pricing table gives 25 credits per month while its FAQ states up to 60 seconds per month: confirm the real account offer instead of choosing one. | S7 | | VERIFIED | A12, A13, A14 | 905 | CL130, CL131 |
| AI10 | DeepMotion's public release page stops at V5.1 (2023-12-21). That proves only what the inspected changelog contains, not that the service stopped or lacks backend updates; do not present it as a 2026 model. | S7 | | VERIFIED (date scope) | A15 | 907 | CL132 |
| AI11 | Paper opinion: where exact rhythm, weight shift or personality matters, film your own intended performance. Capture a base, then exaggerate the silhouette, retime the phases, rebuild occluded contacts and verify on the real target rig. | S7 | | OPINION | P00 | 909 | |
| AI12 | Meshy's Text to Motion API went live on 2026-08-21 and applying its result through motion_task_id followed on 2026-08-26, so it is more than a preset list. Prime delivers a raw FBX clip for 10 credits; Swift delivers BVH for 3 credits. Limits: prompts up to 400 characters, durations from 2 to 10 s in 0.5-s steps, raw generated assets deleted after three days. These are API rules, not timing advice. | S7 | | VERIFIED | A21, A22 | 913 | CL133-CL135 |
| AI13 | Meshy Animation API applies preset clips or generated motion; for generated motion the retarget needs a biped and quadrupeds are rejected. A retarget may succeed with only a GLB and an empty FBX field, so read the actual result fields. FPS conversion choices: 24, 25, 30, 60. The Rigging API warns that standard humanoids are the case that works well; do not carry web-app claims about humanoid, quadruped or Smart Rig to every API operation. | S5, S7 | [for-rigger] (rig type limits) | VERIFIED | A23, A24 | 915, 961 | CL136, CL137 |
| AI14 | Meshy rights: its animation workflow page states free-plan assets are CC BY 4.0 and paid plans give private ownership; the 2026-08-27 explanation ties generated-model rights to the plan at creation time and to valid input rights. Review the current terms for a standalone motion clip before shipping; wording about model ownership does not settle it. | S7 | | VERIFIED | A25, A26 | 917 | CL138 |
| AI15 | Paper opinion: Meshy is an easy source for rigged prototypes and short base clips. Keep rigging, preset choice, new motion generation and retargeting to the target rig as separate steps with separate error logs. A success status is not a quality pass. | S7 | | OPINION | P00 | 919 | |
| AI16 | MoCapAnything V2 (research, creature video capture): paper 2026-04-30, code 2026-05-01 (register A16), weights 2026-07-13, hosted demo 2026-07-15, training data and splits 2026-09-04. Given monocular video and a reference skeleton it predicts joint rotations, with no fixed humanoid template. Custom FBX preprocessing and BVH output are documented. Code and weights are MIT, while the BRIA background-removal component and the Truebones data carry their own terms. | S7 | [for-rigger] (custom skeleton preprocessing) | VERIFIED | A16, A29 | 923 | CL139 |
| AI17 | The MoCapAnything repo is a clean reimplementation, not the code behind the paper's experiments. Its released Setting A on the released Zoo-Unseen split gives 5.70 cm mean joint-position error and 19.58 degrees rotation error; the paper's row says 3.39 cm and 6.54 degrees on another split. The two cannot be compared head to head and are not contact-quality scores for games. The repo's configuration limits samples to 150 joints, which is no 150-DOF guarantee. | S7 | | VERIFIED (reported comparison) | A17 | 925, 962 | CL140, CL141 |
| AI18 | Paper opinion: a research candidate when species-matched footage and unusual skeletons are available. Check tails, wings, leaf bones and hidden limbs separately; support for arbitrary skeletons does not guarantee believable dragon flight, grip, ground contact or unseen anatomy. | S7 | | OPINION | P00 | 927 | |
| AI19 | UniMate (research, creature motion from text): paper 2026-09-04, code 2026-09-06, preview checkpoints 2026-09-27, v3 and custom-rig preprocessing 2026-10-05. The recommended checkpoint unimate_uniml3d_f60_v3 takes 5 to 70 joints and produces 60 frames at 30 FPS (longer clips by expansion). GLB and FBX animation output and custom GLB, glTF or FBX inputs are documented. Code is MIT; checkpoints are CC BY-NC 4.0; source assets keep separate rights; the model card carries an unresolved provenance warning. Do not call it cleared for commercial Roblox release. | S7 | [for-rigger] (5-70 joint input range) | VERIFIED | A18, A19 | 931, 963-964 | CL142-CL144 |
| AI20 | UniMate limits from the model card: sliding, drift, hovering, ground penetration, failure on rare topologies, and off-prompt or static output. The paper adds that text plus skeleton conditioning has no built-in way to set exact per-joint targets or environment contacts. Its cross-topology demos show research capability, not dependable wing or tail choreography or authored attack contact. | S7 | | VERIFIED | A19, A20 | 933 | CL145 |
| AI21 | Paper opinion: keep UniMate in a research/reference lane until permissions and tests are suitable; not the production asset lane. | S7 | | OPINION | P00 | 935 | |
| AI22 | Benchmark discipline: Kimodo's October notes report test-data leakage in Rigplay v1.1, corrected in v1.2 (SEED models unaffected), and warn that smooth-root and raw-hips root metrics do not compare directly. Compare only results with the same version, skeleton, dataset split, generation settings and metric definition; do not rank tools from unrelated FID, joint errors, screenshots or curated demos. | S7 | | VERIFIED | A05 | 939 | CL146 |
| AI23 | Older work is not a 2026 release: HY-Motion 1.0 and Lite appeared 2025-12-30 and the 2026-01-29 update only added evaluation code. Official limits: no animals, no multi-person interaction, no seamless loops, no in-place generation. The community licence excludes the EU, UK and South Korea. Treat it as an older comparison or idea source, not the headline 2026 option. | S7 | | VERIFIED | A27, A28 | 955 | CL147 |

### 3.2 Practical acceptance gate for AI motion (AP:941-951, OPINION P00, all 5 steps)

| step | requirement (paraphrased) | stage |
| --- | --- | --- |
| 1 | Attach to every imported clip: provenance, exact model and version, prompt and seed, source-video rights, FPS, rest pose, unit scale, joint mapping, root convention and contact labels. | S7 |
| 2 | Retarget the body base; then author on purpose anything the source cannot be trusted with: grips, props, fingers, face, tail and wing motion, transitions. | S7 |
| 3 | Inspect renders from front, side, three-quarter and the gameplay camera, not only joint numbers. A multimodal assistant can review supplied frames or clips, but visual review still needs time coverage plus numeric checks. | S7 |
| 4 | Measure joint discontinuities, loop seams, root speed, penetration and planted-foot displacement, plus range of motion, weapon-to-hand alignment and phase-event consistency, on the final target rig. Tolerances come from the game's style and scale; the paper gives no universal thresholds. | S7 |
| 5 | Match anticipation, action, impact and recovery timing to the gameplay contract; generated duration and capture FPS do not define that contract. Export again and retest inside Roblox, because an FBX extension proves no compatibility. | S7, S5 |

### 3.3 Licence and rights data (AP:889-955, collected as data; every row needs a fact-check)

| tool | code licence | weights / data / service terms | src | AP |
| --- | --- | --- | --- | --- |
| Kimodo | Apache-2.0 | SOMA and G1 weights: NVIDIA Open Model terms; SMPL-X variant: different NVIDIA R&D terms | A01, A04 | 889 |
| ARDY | not stated in the paper | text encoder needs gated Llama weights | A06 | 893 |
| Rokoko Create | not applicable | commercial use of generated motion allowed per FAQ; terms v2.0.1 (2026-07-16) restrict automated access and include data-use provisions | A10, A11 | 903 |
| DeepMotion Animate 3D | not applicable | commercial rights vary by plan | A12 | 905 |
| Meshy | not applicable | free plan CC BY 4.0; paid plans private ownership; model rights depend on plan at creation and valid input rights | A25, A26 | 917 |
| MoCapAnything V2 | MIT | released weights MIT; BRIA component and Truebones data separate terms | A16 | 923 |
| UniMate | MIT | checkpoints CC BY-NC 4.0; source-asset rights separate; provenance unresolved | A19 | 931 |
| HY-Motion 1.0 | not stated in the paper | community licence excludes EU, UK, South Korea | A28 | 955 |

### 3.4 Section 11 rule table (AP:957-965, copied as data)

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Kimodo current Rigplay versions | v1.2 | VERIFIED | A01, A05; 2026-10-15 |
| Kimodo internal and exported skeleton | 30 predicted joints; 77 exported joints | VERIFIED | A02; undated docs; checked 2026-10-21 |
| ARDY current listed human rate | 30 fps October checkpoints; July latency result is older | VERIFIED | A06-A07; 2026-10-15 and 2026-07 |
| Meshy generated-motion retargeting | biped-only API path; output may be GLB-only | VERIFIED | A23-A24; current API; checked 2026-10-21 |
| MoCapAnything released rotation error | 19.58 degrees on the released Zoo-Unseen split, not the paper's 6.54 | VERIFIED reported result | A17; checked 2026-10-21 |
| UniMate current preview | v3; 60 frames at 30 fps; 5-70 joints | VERIFIED | A19; 2026-10-05 |
| UniMate commercial use | checkpoint licence is CC BY-NC 4.0 | VERIFIED | A19; checked 2026-10-21 |
| Production acceptance | retarget, contact, visual, rights and runtime gates | OPINION | P00; 2026-10-21 |

---

## 4. Section 12: Work with the rigger, modeler, VFX, sound and UI (AP:967-992)

### 4.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | AP |
| --- | --- | --- | --- | --- | --- | --- |
| HC01 | State what the rig must do, not how many bones it needs: reach, bend, twist, compression, grip, wing fold, tail curl, expressions and the camera angles that must hold. Add extreme-pose references and name the features that carry the character's identity. The rigger answers for joint layout, deformation capacity, controls, export skeleton, limits and failure cases; the modeler answers for topology, separate parts, collisions, silhouette and attachment geometry. | S1, S2, S6 | [for-rigger] | OPINION | P00 | 969 |
| HC02 | When a motion needs a degree of freedom the rig does not have, stop and name the missing constraint. Do not hide it by bending a tool around a fixed wrist or by pushing a wing through the body. Offer options: change the pose, revise the rig, split off a rigid part, ease a close-up requirement, or ask the owner to alter the design. The owner makes the creative call; technical agents describe the consequences. | S6, S7 | [for-rigger] | OPINION | P00 | 971 |
| HC03 | A delivery contract keeps requirements, assumptions, decisions, measurements and unknowns in separate places. A rigger saying the pose works is not a rendered deformation test, and an animator meaning the event to fall on a marker is not a captured runtime test. Evidence goes into each acceptance field. | S5, S6, S7 | [for-rigger] | OPINION | P00 | 973 |
| HC04 | Version the rig, the clip, the event contract and the runtime binding together. After a retime, compare each shared event and each consumer before approving. Do not give each craft its own rounded frame list: keep one canonical time representation and derive editor labels from it. The animator reports divergence and never quietly bends gameplay to the clip. | S7 | | OPINION | P00 | 986 |

### 4.2 Cross-craft hand-off checklist (AP:975-984, complete, 7 rows)

| collaborator | animator needs | animator supplies | acceptance evidence |
| --- | --- | --- | --- |
| Owner | intent, personality, readability priorities, approval | alternatives, previews and explicit trade-offs | recorded decision on the current revision |
| Modeler | shape, parts, proportions, materials and silhouette constraints | required contacts and extreme-pose envelope | multi-view deformation and intersection renders |
| Rigger | semantic mapping, axes, limits, IK/FK, export joints, attachment sockets | motion ranges, retarget needs and failed poses | rig test action and export round trip |
| Gameplay | states, speed, hit windows, cancels, authority and interruption | contact timing, displacement, feasibility and animation events | the same event contract used in runtime tests |
| VFX | required origins, directions, lifetimes and cancellation | named events and attachment transforms | effects align on hit, miss and interruption |
| Sound | cue semantics, intensity, surface data and spatial attachment | action accents and confirmed outcomes | no stale loop or false confirmed-hit cue |
| UI | feedback semantics and priority | action-state and result events | UI does not disclose false success |

### 4.3 Section 12 rule table (AP:988-992)

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Required range of motion | explicit per action and part | OPINION | P00; 2026-10-21 |
| Canonical timing contract | one revision shared by consumers | OPINION | P00; 2026-10-21 |
| Silent gameplay retiming | not allowed by this protocol | OPINION | P00; 2026-10-21 |
| Approval authority | studio owner | OPINION | P00; 2026-10-21 |

---

## 5. Section 13: Review from rendered evidence and runtime captures (AP:994-1034)

### 5.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | AP |
| --- | --- | --- | --- | --- | --- | --- |
| RV01 | Evidence base: Insomniac's facial-rigging talk compared poses with scans and checked the engine output, including export-related geometry problems (VERIFIED C15, GDC 2019-03); Riot reports repeated playtests of cosmetic weapon feel and obstruction (EXPERIENCE C06, 2020-05-18). Paper's conclusion (OPINION): review what is delivered in context, not only the authoring preview. | S6, S7 | [for-rigger] | VERIFIED (C15); EXPERIENCE (C06); OPINION | C15, C06, P00 | 996 |
| RV02 | Judge the intended action before polish: can a viewer read subject, goal, direction, key contact, force and result without text? Then look for technical defects. Separate exaggeration the owner approved from accidents, and record disagreement rather than a falsely unanimous review. | S7, S8 | | OPINION | P00 | 998 |
| RV03 | A review pack contains: the brief, the current motion profile, the source and retiming log, a game-camera clip, side and front diagnostic views, a silhouette pass, a contact sheet, an event overlay, rig/clip/export versions and a runtime profile capture. Include effect-free and final-context views. Watch at normal speed, then slowly, then frame by frame at events. A frame count alone does not show impact or appeal. | S7 | | OPINION | P00 | 1000 |
| RV04 | An AI reviewer ties each remark to a timestamp and visible evidence (the paper's examples: left foot drifting from the floor while support is declared; tool contact before the confirmed flash; distal tail changing direction before its declared driver). Vague notes such as add life are out. A proposed change names the channel or body group, the event interval, the intended perceptual result and the regression to check. | S7 | | OPINION | P00 | 1002 |
| RV05 | Set tolerances before a numeric test can pass or fail, because the same foot slide can matter at one scale and not at another. Record units, camera, measurement method and any owner-approved exception. If the tolerance is UNKNOWN, the automated check may report the measurement but must not make up a pass limit. | S7 | | OPINION | P00 | 1023 |

### 5.2 Pass or fail review checklist (AP:1004-1021, complete, 15 rows; IDs are mine)

| id | test | pass condition | fail condition |
| --- | --- | --- | --- |
| RV-T01 | Intent and personality | viewer can identify the intended action and approved character quality | gesture contradicts the brief or needs explanation |
| RV-T02 | Part identity | every animated part has a semantic label and a motion driver | an unknown element is moved by generic procedural noise |
| RV-T03 | Contact | declared planted or gripped parts stay attached within the approved measured tolerance | foot slide, grip separation, unexplained penetration |
| RV-T04 | Support and weight | body motion and the support/force model explain acceleration and recovery | weightless launch, unsupported stopping, absent reaction |
| RV-T05 | Arcs and spacing | paths and spacing serve anatomy, force and style | accidental corners, uniform easing everywhere, popping |
| RV-T06 | Joint and mesh integrity | verified range of motion and acceptable deformation | knee or elbow inversion, collapsing volume, broken wing fold |
| RV-T07 | Secondary causality | lag, active correction and settling have declared causes | all parts move in phase, or follow a generic delayed wave |
| RV-T08 | Tools and props | grip, pivot, collision, trajectory and consequence agree | tool feels detached, hinge translates, impact has no response |
| RV-T09 | Loop seam | pose and velocity continuity, or an approved discontinuity | pause, pop or drift at repeat |
| RV-T10 | Transition and interruption | required state paths keep contacts and clean up | additive residue, stale trails, stuck grips, a pose that does not recover |
| RV-T11 | Gameplay timing | visible threat and result agree with authoritative windows | presentation implies unavailable range or false damage |
| RV-T12 | Export fidelity | imported poses, events and duration match the approved reference | lost action, changed scale, retimed contact, missing channel |
| RV-T13 | Runtime correctness | priority, blending, authority and replication match the design | other clients disagree, or unrelated joints are overridden |
| RV-T14 | Cost | the agreed target-device scene passes measured frame and memory goals | only a desktop or isolated-asset test passes |
| RV-T15 | Owner approval | the current revision is approved with unresolved issues disclosed | approval refers to an earlier revision or an unresolved blocker |

### 5.3 Diagnosing common AI motion failures (AP:1025-1027, OPINION P00, 8 items)

| id | symptom | what the paper says to do first |
| --- | --- | --- |
| RV-F01 | linear or floaty movement | check spacing, support, contact and braking before adding keys |
| RV-F02 | no anticipation | first decide whether a responsiveness constraint explains the missing anticipation; if not, add a readable preparatory cue within approved timing |
| RV-F03 | no overlap | name the active and the passive parts and their order of cause |
| RV-F04 | robotic timing | compare the spacing and accents of events, not random per-channel offsets |
| RV-F05 | bad arcs | plot meaningful world-space landmarks and check the reference and the camera |
| RV-F06 | weightless tools | look at grip, support shift, tool acceleration and how the body reacts after impact |
| RV-F07 | stiff tails or wings | reconsider the anatomy and which part drives which |
| RV-F08 | too many keys or bones | reduce only after measuring what the removal does, keeping required detail |

### 5.4 Section 13 rule table (AP:1029-1034)

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Engine and play-context review | compare the delivered result, not only the DCC | VERIFIED document; EXPERIENCE | C15; GDC 2019; C06; 2020-05-18 |
| Numerical pass thresholds | UNKNOWN until production defines units and tolerances | OPINION | P00; 2026-10-21 |
| Review record | timestamp, observation, proposed change and regression | OPINION | P00; 2026-10-21 |
| Final review environment | imported asset in target gameplay context | OPINION | P00; 2026-10-21 |
| Approval | current revision only | OPINION | P00; 2026-10-21 |

---

## 6. Section 14: End-to-end process for the animator agent, 15 gates (AP:1036-1100)

The gates are a proposed working method (OPINION P00, AP:1038), not a claim that leading studios use this order or these durations. Evidence can send you back to an earlier gate; the paper says never to polish over a rig or gameplay problem. The stage column is my mapping to `workflow.md`; the order conflict with the approved workflow is LM12.

| id | gate (what to do, paraphrased) | pass condition (paraphrased) | stage (extractor mapping) | flag | AP |
| --- | --- | --- | --- | --- | --- |
| GT01 | Read the brief and owner constraints: purpose of the action, audience camera, style, gameplay states, authoritative events, deliverable. | the required result holds no unresolved contradiction | S0, S1 | | 1040 |
| GT02 | Read and validate the rig: list semantic parts, hierarchy, local axes, rest transforms, constraints, deform channels and attachments. | each needed part is mapped and each needed degree of freedom exists or is escalated | S6 (uses S5 rig sheet) | [for-rigger] (the rig must offer the DOFs) | 1042 |
| GT03 | Fill the motion profile, keeping measured geometry, supplied physical values, artistic weight and unknowns apart. | for every moving group the support, driver and secondary behavior are stated | S1 (draft), S6 (update) | [for-rigger] (fields in 1.3) | 1044 |
| GT04 | Collect reference: anatomical and performance evidence, with rights and timebase kept; measure only defined events. | no timing is invented or wrongly converted | S1, S7 | | 1046 |
| GT05 | Draft the timing contract: align gameplay windows, animation phases, effects, audio and UI; get owner or design sign-off on consequential compromises. | a single canonical event definition | S7 (timing list, J006) | | 1048 |
| GT06 | Block the intent and contacts: extreme poses, support changes and readable accents before dense interpolation. | the owner can judge the action from a cheap preview and the silhouette | S7 | | 1050 |
| GT07 | Refine mechanics and spacing: trajectory, contact, weight transfer, arcs, grips, hierarchy. | continuous playback explains the action without effects covering flaws | S7 | | 1052 |
| GT08 | Add secondary and facial performance under control; keep active choices apart from passive response and keep layers and constraints explicit. | the extra motion adds meaning without hurting readability or cost | S7 | | 1054 |
| GT09 | Render and review at normal speed plus diagnostics; log concrete defects and deliberate exceptions. | required review items pass or carry explicit owner-approved exceptions | S7 | | 1056 |
| GT10 | Optimize: drop redundant curves, keys and unused export channels, keeping measured bounds on event and deformation error. | a before/after comparison backs the reduction and exported motion stays within the approved tolerance | S7 | [for-rigger] (unused export channels) | 1058 |
| GT11 | Export with a pinned preset and record tool versions, axes, units, rig and action choice, and sampling. | the file holds only intended deliverables and no export warning is ignored | S5 (profile), S7 | [for-rigger] | 1060 |
| GT12 | Import and bind in Roblox, checking each clip, rig mapping, priority, transitions, markers, attachment and authority. | timing and pose match the approved Blender preview | S5, S7 | [for-rigger] | 1062 |
| GT13 | Test on the intended phone class with the agreed scene, concurrency, camera, effects and movement; read frame time, memory and animation behavior. | the measured budget is met, not just an engine ceiling | S7 | | 1064 |
| GT14 | Exercise edge cases: interruption, death, respawn, tool swap, teleport, late join, visibility or LOD changes, failed load, and cutscene skip where relevant. | no stale state, orphaned track, grip or effect is left | S7 | | 1066 |
| GT15 | Deliver and obtain final approval. Handover: asset identifiers, source files, motion profile, timing contract, source and measurement log, review captures, optimization results, known limits. | the owner approves the exact imported revision | S8 | | 1068 |

Section 14 rule table (AP:1096-1100, copied as data):

| rule | number | evidence mark | source and date |
| --- | --- | --- | --- |
| Workflow gates | 15 proposed gates, not a measured industry standard | OPINION | P00; 2026-10-21 |
| Unsupported quantitative defaults | none admitted as fact | OPINION | P00; 2026-10-21 |
| Runtime completion | imported, reviewed and device-tested revision | OPINION | P00; 2026-10-21 |
| Final creative decision | studio owner | OPINION | P00; 2026-10-21 |

---

## 7. Do not do (AP:1070-1088, all 9, all OPINION P00)

| id | rule (paraphrased) | stage | flag | AP |
| --- | --- | --- | --- | --- |
| DN01 | Do not deduce species, mass, center of mass or anatomy from bone names, sizes or mesh weights. | S1, S6 | [for-rigger] | 1072 |
| DN02 | Do not generalize one passive-tail lesson to all real tails, and do not paste a bird wing cycle onto a bat without changing the mechanical model. | S1, S7 | | 1074 |
| DN03 | Do not invent anticipation, recovery, overlap, frame-rate, key-count or mobile-budget values to complete a table. | all | [for-rigger] | 1076 |
| DN04 | Do not equate extra interpolation, simulation, bones or AI output with better animation. | S7 | [for-rigger] (bones) | 1078 |
| DN05 | Do not let effects cover a missing contact, and do not turn a marker into gameplay authority without examination. | S7 | | 1080 |
| DN06 | Do not overwrite an approved rig or clip unless the earlier revision and its event contract are kept. | S5, S7 | [for-rigger] | 1082 |
| DN07 | Do not treat a preview render as proof of import fidelity, replication or phone performance. | S7 | | 1084 |
| DN08 | Do not ship unreviewed generated motion, uncited numeric timing, or an unresolved right-to-use problem. | S7 | | 1086 |
| DN09 | Do not substitute owner approval with a rule score, a benchmark, or the argument that a famous studio uses the same style. | S8 | | 1088 |

---

## 8. Open questions requiring production evidence (AP:1090-1094, all 8, OPINION P00)

| id | question (paraphrased) | stage | flag | AP |
| --- | --- | --- | --- | --- |
| OQ01 | Which devices, resolution, frame target, thermal conditions and scene populations count as a low-end phone for this studio? | S0, S5 | [for-rigger] | 1092 |
| OQ02 | Which rigs, dynamic-head features, joint extensions, graph features and importer versions will the shipping experience actually enable? | S2, S5 | [for-rigger] | 1092 |
| OQ03 | Which clips need to be deterministic, retargetable, interruptible or visible to other players? | S1, S7 | [for-rigger] | 1092 |
| OQ04 | Which root-motion policy is authoritative? | S2, S7 | [for-rigger] | 1092 |
| OQ05 | Which sources and performances may be reused? | S7 | | 1092 |
| OQ06 | What visual tolerances are accepted for foot slide, key reduction, deformation and event offset? | S7 | [for-rigger] | 1092 |
| OQ07 | Which anatomy is approved for hybrid creatures? | S1, S2 | [for-rigger] | 1092 |
| OQ08 | Which AI model and version has passed the studio's own tests on the target rig? | S7 | | 1092 |

Paper's closing statement (AP:1094): public sources cannot settle these product questions. Leave each open until the responsible owner, the rig, the implementation or a device measurement answers it. A missing number is itself a research finding and gives no licence to invent a plausible default.

---

## 9. Timing library for 26 named actions and the exact numerical ledger (AP:1102-1144)

### 9.1 How the paper says to use the library (AP:1104-1106)

| id | rule (paraphrased) | tag | AP |
| --- | --- | --- | --- |
| TL-R1 | The library keeps a usable phase contract apart from published timing evidence. U means UNSPECIFIED in the source, which is neither zero nor a suggested length. Rows with U need measured reference or a designer-approved timeline before production; no numbers were invented to close gaps. | OPINION | 1104 |
| TL-R2 | The easing column is the paper's own opinion (P00) unless a row says otherwise; it states what to solve, not an industry curve preset. | OPINION | 1104 |
| TL-R3 | Hammer rows keep the study's phase names, and strike/follow-through does not automatically equal gameplay recovery. Gecko and cat rows give event latency, not overlap between joints. Bat and bee rows give cycles, not attack phases. | VERIFIED B05, B07, B09, B16, B21; OPINION (scope protocol P00) | 1106 |
| TL-R4 | Source means and uncertainties stay in the ledger (9.3). No fractional frame count is rounded to a keyframe. An exact duration conversion does not show that the sampling suffices or that the result looks equivalent. | VERIFIED; OPINION | 1106 |
| TL-R5 | Cycles shorter than one 30-fps interval can alias. Use subframe integration, blur or a stated stylized pose proxy instead of typing in fractional keys blindly. | OPINION | 1106 |

### 9.2 The 26 actions (AP:1108-1134, complete). Stage S7 for all (S1 for the needs behind each).

Phase counts are in 30-fps intervals as the paper gives them. U = UNSPECIFIED. "Tag" is copied as the paper wrote it; the register tag is added where the two differ.

| # | named action | phase contract | phase counts at 30 fps | easing or spacing note (paraphrased) | source and tag | AP |
| --- | --- | --- | --- | --- | --- | --- |
| TL01 | Light attack | Startup / active / recovery | U / U / U | keep a clear threat and contact; no default ease on impact | OPINION P00; C12 decision-reading precedent, 2021-05-10 (register: C12 EXPERIENCE) | 1109 |
| TL02 | Heavy attack | Load / accelerate / impact / recover | U / U / U / U | solve support and tool momentum; heavy does not mean globally slow | OPINION P00; B03 weight teaching, 2025-11-14 (register: EXPERIENCE) | 1110 |
| TL03 | Spell cast | Gather / release / recover | U / U / U | protected gameplay release; show effort differences in the pose | EXPERIENCE C10; 2017-08-16; easing OPINION | 1111 |
| TL04 | Revolver reload design problem | Empty / reload / ready | all phase counts U; total source count 45 at unknown FPS | protect readiness; source publishes no internal curves | EXPERIENCE C18; GDC 2017 abstract (register: C18 VERIFIED, LM13) | 1112 |
| TL05 | Nail hammering with a 1-lb hammer | Cock / swing / strike-follow-through | 10.2 +/- 2.1 / 2.1 +/- 1.2 / 11.7 +/- 0.9 | fit measured event spacing; no ease curve published | VERIFIED B21; 2017-04; exact conversion | 1113 |
| TL06 | Nail hammering with a 2-lb hammer | Cock / swing / strike-follow-through | 13.2 +/- 5.4 / 3.6 +/- 2.1 / 12.9 +/- 0.9 | keep the study phases; not a combat-sledge preset | VERIFIED B21; 2017-04; exact conversion | 1114 |
| TL07 | Jump | Prepare / takeoff / flight / land | U / U / U / U | match the approved trajectory and contact release | OPINION P00; no universal phase source | 1115 |
| TL08 | Landing | Approach / contact / absorb / settle | U / U / U / U | separate contact impulse from recovery | OPINION P00; no universal phase source | 1116 |
| TL09 | Hit reaction | Detection / impulse / displaced pose / recover | U / U / U / U | direction and support govern spacing; no arbitrary delay | OPINION P00; no universal phase source | 1117 |
| TL10 | Pickup | Reach / grip / load / lift / settle | U / U / U / U / U | hold the grip through the load change; acceleration reflects the intended load | OPINION P00; B03, 2025-11-14 | 1118 |
| TL11 | Door open | Unlock / accelerate / travel / stop | U / U / U / U | hinge path and actuator; ease depends on the mechanism | OPINION P00; no universal phase source | 1119 |
| TL12 | Pet idle | Attention / optional gesture / return | U / U / U | use motivated holds; no uniform oscillation required | OPINION P00; no universal phase source | 1120 |
| TL13 | Wing takeoff | Prepare / launch / accelerating flight | U / U / U | couple body orientation with the wing and tail task | VERIFIED context B06; 2010-05-15; easing OPINION | 1121 |
| TL14 | Wing landing | Approach / brake / contact / fold | U / U / U / U | species-specific whole-body coordination | VERIFIED context B06-B08; 2010-2015; easing OPINION | 1122 |
| TL15 | Glide | Enter / steady glide / maneuver / exit | U / U / U / U | wings change shape with airspeed; not a frozen flap | VERIFIED context B10; 2011; easing OPINION | 1123 |
| TL16 | Bat wingbeat reference | whole cycle; subphases not published here | approximately 3.75-5.25 per cycle; subphases U | derived from 125-175 frames at 1000 fps; no generic spline supplied | VERIFIED B07; 2015-11-16 | 1124 |
| TL17 | Hovering honeybee wingbeat | whole cycle; down/up phases not partitioned | approximately 3/23 per cycle; phases U | 230 Hz context; subframe, blur or proxy decision needs a renderer test | VERIFIED B09; 2005-12-05; rendering OPINION | 1125 |
| TL18 | Tail swish | Intent / bend propagation / return | U / U / U | first choose active gesture or passive response | EXPERIENCE B02; 2017-06-19; easing OPINION | 1126 |
| TL19 | Gecko tail support response | Slip event / response onset / tail contact | onset 0.867 +/- 0.189; contact 1.41 +/- 0.33 after the source event | event latencies, not delays between joints | VERIFIED B05; 2008-03-17; exact conversion | 1127 |
| TL20 | Cat ear orienting response | Auditory event / early pinna response / later orienting | early onset approximately 0.75; other phases U | active sensory response; not generic head-follow lag | VERIFIED B16; 1998-06-01; exact conversion | 1128 |
| TL21 | Antenna probing | Search / contact / changed sampling | U / U / U | active touch and locomotor coordination | VERIFIED context B17; 2011; easing OPINION | 1129 |
| TL22 | Swimming body or fin stroke | Propulsion / steering / recovery | U / U / U | pick species, medium and task; no decorative universal sine | VERIFIED context B15, B18; dates in register (B15 2008, B18 2005-07-15); easing OPINION | 1130 |
| TL23 | Quadruped walk | Limb-specific stance / swing | U / U; footfall order comes from the chosen gait | do not turn horse gait into every quadruped | VERIFIED context B11; 2007; easing OPINION | 1131 |
| TL24 | Six-legged tripod walk | Opposing tripod contact groups | approximately 0.5C offset, C = measured cycle frames; C unknown | within-group offsets exist; turning not established | VERIFIED B12; 2021; easing OPINION | 1132 |
| TL25 | Eight-legged walk | Pair-specific stance / swing coordination | U / U | speed and anterior/posterior pairs matter | VERIFIED context B13; 2011-10-15; easing OPINION | 1133 |
| TL26 | Floating turn | Intent / torque / reorientation / brake | U / U / U / U | distinguish fluid, free fall and authored magical force | VERIFIED context B22, B25; undated; easing OPINION | 1134 |

Count check: 26 rows. Numeric cells exist only in TL04 (total 45, FPS unknown), TL05, TL06, TL16, TL17, TL19, TL20 and TL24 (0.5C with C unknown). All other phase cells are U.

### 9.3 Exact numerical ledger (AP:1136-1144, complete)

| id | item | tag | src | AP |
| --- | --- | --- | --- | --- |
| NL01 | Hammer study, mean +/- SD in seconds, cock / swing / strike-follow-through. 1-lb: 0.34 +/- 0.07 / 0.07 +/- 0.04 / 0.39 +/- 0.03, total 0.81 +/- 0.11. 2-lb: 0.44 +/- 0.18 / 0.12 +/- 0.07 / 0.43 +/- 0.03, total 0.99 +/- 0.22. For 60 fps, multiply each 30-fps table value and SD by exactly two. The first-phase means of the 1-lb row sum to 0.80 s against the reported 0.81 s: keep the rounding difference and never add SDs. | VERIFIED | B21 (2017-04) | 1138 |
| NL02 | Gecko: response onset approximately 28.9 +/- 6.3 ms; tail contact 47.0 +/- 11.0 ms in the slipping task. Exact 60-fps equivalents: 1.734 +/- 0.378 and 2.82 +/- 0.66 intervals (30-fps values are in TL19). These are whole-tail events relative to the study's forefoot contact, not a reusable per-bone delay. | VERIFIED | B05 (2008-03-17) | 1140 |
| NL03 | Bat: approximately 125-175 capture intervals at 1000 fps = 0.125-0.175 s = approximately 7.5-10.5 intervals at 60 fps (TL16 gives 3.75-5.25 at 30 fps). | VERIFIED | B07 (2015-11-16) | 1142 |
| NL04 | Honeybee: frequency approximately 230 Hz; reciprocal period approximately 1/230 s = 100/23 ms = 3/23 of a 30-fps interval = 6/23 of a 60-fps interval. Exact algebra does not remove the source's approximation. | VERIFIED | B09 (2005-12-05) | 1142 |
| NL05 | Cat pinna component approximately 25 ms = approximately 0.75 interval at 30 fps and 1.5 at 60 fps. | VERIFIED | B16 (1998-06-01) | 1144 |
| NL06 | A normalized 0.5-cycle delay is half of the measured cycle, not automatically 15 frames. | VERIFIED | B12 (2021) | 1144 |
| NL07 | The 45-frame reload example has no convertible timebase. | EXPERIENCE | C18 (2017) | 1144 |

The paper's point (AP:1144): a measurement can be precise in its own domain and still be unfit as a production preset.

### 9.4 Extractor arithmetic re-check (not a paper claim; for step 2)

I recomputed the exact-arithmetic forms. All matched the paper. Forms kept as the paper wrote them.

| item | recomputation | result |
| --- | --- | --- |
| 30-fps interval | 1000/30 ms = 100/3 ms | matches AP:644, 698, 779, 881 |
| 60-fps interval | 1000/60 ms = 50/3 ms | matches |
| TL05 (1-lb) | 0.34, 0.07, 0.39 x 30 = 10.2, 2.1, 11.7; SDs 0.07, 0.04, 0.03 x 30 = 2.1, 1.2, 0.9 | matches |
| TL06 (2-lb) | 0.44, 0.12, 0.43 x 30 = 13.2, 3.6, 12.9; SDs 0.18, 0.07, 0.03 x 30 = 5.4, 2.1, 0.9 | matches |
| NL01 sums | 0.34 + 0.07 + 0.39 = 0.80 (reported 0.81); 0.44 + 0.12 + 0.43 = 0.99 (reported 0.99) | matches the paper's note on 0.80 vs 0.81 |
| TL19 / NL02 | 28.9 ms / (100/3) = 0.867; 6.3 / (100/3) = 0.189; 47.0 / (100/3) = 1.41; 11.0 / (100/3) = 0.33; at 60 fps 1.734, 0.378, 2.82, 0.66 | matches |
| TL16 / NL03 | 125 and 175 intervals at 1000 fps = 0.125 s and 0.175 s; x 30 = 3.75 and 5.25; x 60 = 7.5 and 10.5 | matches |
| TL17 / NL04 | (1000/230) ms = 100/23 ms; divided by 100/3 = 3/23; divided by 50/3 = 6/23 | matches |
| TL20 / NL05 | 25 ms / (100/3) = 0.75; 25 ms / (50/3) = 1.5 | matches |
| Avatar triangle ceilings (RT06) | 4,000 + 1,750 + 4 x 1,248 = 10,742 | matches if the 1,248 applies to each of the four limbs |

---

## 10. Indexes for the lead and the rigger

### 10.1 Stage index (extractor mapping to `workflow.md`)

| stage | IDs |
| --- | --- |
| S0 intake | GT01, OQ01 |
| S1 motion needs | BL12, BL15, HC01, GT01, GT03 (draft), GT04, AI01, OQ03, OQ07, DN01 |
| S2 rig plan | BL12, BL13, RT04, RT05, RT06, RT08, RT27, RT31, RT32, HC01, OQ02, OQ04, OQ07 |
| S3 geometry, S4 geometry acceptance | none in this range (paper lines 542-1145 do not cover modeler work except HC01 and the hand-off table) |
| S5 rig + tests | BL01-BL11, BL16-BL20, BL30, BL36-BL39, RT01-RT11, RT14, RT16, RT17, RT26-RT27, RT31, AI13, GT11, GT12, LC01, LC04, LC05, DN06 |
| S6 rig acceptance | BL12-BL14, GT02, GT03 (update), HC02, HC03, RV01, DN01 |
| S7 animate, export | BL19-BL39, RT12-RT30, RT32, RT33, AI02-AI23, HC04, RV02-RV05, RV-T01..T15, RV-F01..F08, GT04-GT14, TL01-TL26, NL01-NL07, DN02-DN08, LC02, LC03, LC06-LC09 |
| S8 final | BL35, RV02, GT15, DN09 |

### 10.2 Rigger quick sheet ([for-rigger] topics gathered as pointers; no new facts)

The rows say where the paper's position is and how firm it is. Nothing here is a number the rigger may use before the fact-check (table CL).

| topic | paper position (pointer) | IDs | firmness |
| --- | --- | --- | --- |
| Rig manifest fields | 8 manifest fields plus 4 version pins | 1.2, BL01, BL11 | OPINION |
| Motion-profile fields the rigger receives | 16 fields | 1.3, BL15 | OPINION |
| Unknowns the rigger must not invent | mass, center of mass, joint limits, delays, safe range | BL12, BL13, DN01, DN03 | OPINION |
| Export skeleton and bake | bake a duplicate export rig, keep a reference, exclude controls only after validation; exports carry evaluated motion, not control semantics | BL30, BL31, GT10 | VERIFIED (constraints not saved), OPINION (procedure) |
| Export profile | test baseline: no leaf bones, explicit clips and range, simplification 0.0, no experimental transform baking, axis/unit conversion once | BL37, RT03 | OPINION (baseline), VERIFIED (Roblox FBX guide: unit scale, bake animation) |
| Importer behavior | FBX and glTF both carry rig, skin, animation; glTF may add a Model level and MeshParts per primitive; zero-influence bones off by default; forward/up and scale controls | RT02, RT04 | VERIFIED |
| Multi-clip import | ACE GA 2026-03-31, several clips per file, rest-pose selection, local save then publish | RT07, BL38 | VERIFIED |
| Rig type | R15, Custom, No Rig; custom creatures need not meet avatar-body rules; R15 means 15 meshes, not 15 joints | RT02, RT05, RT06 | VERIFIED |
| AnimationController vs Humanoid | Roblox suggests AnimationController when Humanoid functionality is unneeded; disable unused humanoid states | RT17, LC05 | VERIFIED (AG18 wording check) |
| Motor6D vs Bone | Motor6D joins two BaseParts (Transform is the procedural offset, Animator overwrites it); Bones carry skin influences and do not change collision shape; mechanical custom rigs can still use Motor6D | RT11, RT05 | VERIFIED |
| AnimationConstraint | with AJU enabled R15 avatar joints use AnimationConstraints, not Motor6Ds; C0/C1/Part0/Part1 aliases read-only; layer transforms in PreSimulation | RT10, RT08 | VERIFIED |
| IKControl | runtime IK is a per-frame solve; Enabled=false turns it off, weight 0 does not; reserve for visible contact fixes | RT16, LC04 | VERIFIED, OPINION (reserve) |
| Rigid vs skinned cost | no universal winner; count parts, vertices, influences, draw calls, collision bodies, IK, blending, churn; decide by A/B on the target phone | RT31, RT30, RT25, RT26, 2.3 | OPINION, EXPERIENCE |
| Root-motion policy | native root motion was unreleased (2026-01-21), roadmap says Early 2027; default locomotion to in-place; gameplay controller sets displacement | RT27, BL28, BL38, OQ04 | VERIFIED (status), OPINION (policy) |
| Bone, track, key, actor maxima | all UNSPECIFIED; only hard figures: 4 influences per vertex, 20,000 triangles per mesh, reported 64 playing tracks per character | 2.2, RT04, RT21, LC01 | VERIFIED / EXPERIENCE; do not turn into budgets |
| The 256-bones remark | developer commentary, not an importer cap | RT26 | EXPERIENCE |
| Who creates the Animator | server-created for automatic replication; local Animator tracks do not replicate | RT14 | VERIFIED |
| Markers, VFX and hitboxes | markers for cosmetic cues; server gameplay needs its own validation; test at low framerate and late join | RT15, RT33 | VERIFIED (API), OPINION (policy) |
| Throttling | always-on client animator throttling; reduced far/offscreen pose frequency; test procedural effects offscreen | RT18, LC06 | VERIFIED (register), forum reply unverified |
| When the rig lacks a degree of freedom | stop, name the constraint, offer the five alternatives; owner decides | HC02 | OPINION |
| Rotation modes of control bones | keep the rig's chosen mode; consistent mode per keyed animation | BL26 | VERIFIED, OPINION |
| Phone acceptance | named devices, frame-time target, constant meshes while isolating animation cost, repeat spawn/despawn | 2.3, GT13 | OPINION |

---

## 11. Contradictions and limits (LM)

### 11.1 Table LM

| id | topic | paper says | other doc or limit | status | handling | AP |
| --- | --- | --- | --- | --- | --- | --- |
| LM01 | ID namespaces differ between the two papers | The animation paper (AP) numbers Roblox sources R01-R32, Blender sources D01-D36 and science sources B01-B25. The rigging paper (RP) numbers Roblox sources R1-R13, Blender sources B0-B8, Disney D1-D2. Same letters, different meaning. Pairs by title (extractor reading, not paper text): AP R01 Importer = RP R3; AP R02 Export settings = RP R4; AP R03 General specifications = RP R1; AP R04 Rigging and skinning = RP R7; AP R05 Character body specifications = RP R2; AP R10 Motor6D = RP R8; AP R16 Improve performance = RP R13; AP D01 Blender 5.2 release = RP B0; AP D28 FBX Legacy manual = RP B5; AP D09 PoseBone API = RP B6. | | Limit | Always write the pair (AP-R02, RP-R4) when two notes cite the same page. | 1146-2056 |
| LM02 | Blender docs disagree with each other | FBX Legacy manual says scale default 10, exporter API says global_scale=1.0; manual lists vertex shape keys unsupported, 5.1 notes say shape-key normals are exported; glTF manual keeps old name-based merge text but records merge-by-Action since 4.4. | D26, D27, D28, D29 | VERIFIED conflict | Pin the exact build; prefer API and release notes; test the target round trip; do not copy the stale limitation list. | 552-554, 701 |
| LM03 | PreferLodEnabled | Animator API prose says false forces full fidelity and Workspace can disable throttling. The rollout post says the property is only a hint under resource pressure and throttling is always on. | R12 vs R17 | VERIFIED conflict | Treat throttling as always on; test it on the phone. | 755, 775, 864 |
| LM04 | Forum voice vs staff | R20 (64-track cap) is attributed to BloxHerder; the staff role was not verified. R17 "reply 6" (clocks and markers keep running while posing is skipped): author role not verified. R24, R25, R31 are single-developer reports. | R17, R20, R21, R24, R25, R31 | EXPERIENCE; unverified role | Label as forum reports; never state as API guarantees. | 775, 787, 805, 809, 825 |
| LM05 | Root motion: API vs release vs roadmap | A property named RootMotion appears in the API but a 2026-01-21 documentation response says it was unreleased. The 2026-09-11 RDC roadmap lists new default movement with root motion for Early 2027. | R26, R32 | VERIFIED; roadmap is not a release | Default to in-place clips and a gameplay-defined displacement; re-check when released. | 813 |
| LM06 | Single-track export statement | The general specification text is described as stale or narrower than the later multi-clip ACE release. | R03 vs R06 | VERIFIED conflict | Name the import path (ACE, Import 3D, Studio import) instead of a universal limit. | 717, 729 |
| LM07 | Graphs: released vs beta vs memory report | Animation Graphs are released (2026-07-15); State Machines and Expressions are Studio-only beta (2026-10-08); a Pixel 6a report (2026-10-17/18) shows retained memory after graph tracks. | R22, R23, R24 | Mixed: VERIFIED release, EXPERIENCE report | Do not rely on the beta for low-end phones; run own graph spawn/despawn memory tests. | 797-805 |
| LM08 | Track-count evidence | 64 playing tracks per character is reported by a forum reply (2026-01-26); older 256 warnings and temporary 32 caps are historical; an October user log (register 2026-10-04, reply text says October 3rd) still shows 64-track warnings. | R20, R21 | EXPERIENCE | The number is a protection cap, not a budget. Small date mismatch kept as written. | 787, 791, 876 |
| LM09 | EXPERIENCE reports are not reproduced | Pixel 6a memory numbers, 10 Hz NPC renderer, 1,000-assembly gains are reports with confounded variables. R25's 256-bones-per-mesh remark is commentary, and the register key line for R25 speaks of an 8-bone single-mesh rig. | R24, R25, R31 | Limit | Use as test-design hints; no phone budget follows. | 805-825, 1830-1834 |
| LM10 | Internal vs whole-frame figures | 25-30% animation-CPU reduction is internal crowded-scene testing; 100/3 ms and 50/3 ms are whole-frame times, not animation-only allowances. | R17, R18 | Limit | Do not convert either into a per-rig budget. | 775, 779 |
| LM11 | Loop endpoint advice differs by tool | Blender side: avoid a duplicated endpoint hold, check continuity at the wrap. Roblox Animation Editor side: loops do not interpolate from the last key back to the first, so duplicate the starting pose at the end. | D20, D21 vs R30 | Not reconciled in the paper | Decide the loop policy per export route and check the seam after import (RV-T09). | 654, 821 |
| LM12 | Gate order vs the approved workflow | Paper order: gate 2 reads the rig, gate 3 fills the motion profile. Approved `workflow.md`: the animator writes the motion profile first (S1), the rigger plans (S2), the rig is built (S5), the animator accepts it (S6). | GT02, GT03 vs workflow S1-S6 | Conflict of order | Treat gate 3 as a draft at S1 and an update at S6; lead to settle. | 1042-1044 |
| LM13 | Tag inconsistencies | C18 is VERIFIED in the register but EXPERIENCE in the TL04 row (its key line is a rhetorical question; FPS not given; page fetch timed out). The first version paragraph is tagged VERIFIED with a trailing OPINION sentence. The Blender sketch is called a design sketch yet its "API basis" is tagged VERIFIED (documentation level only). | C18, D01-D03, D04-D36 | Tag inconsistency | Keep the paper's tag; fact-check. | 546, 630, 1112 |
| LM14 | Blender source gaps | 4.5.14 LTS and "supported through July 2028" are not shown in any register key line. group_name vs action_group is attributed to D04, whose key line is general. D08, D11, D36 are "current" URLs (not immutable); D22, D31, D32 are 5.0 pages; D16, D20 are staging pages; the register URLs of D07, D18, D19, D21, D23, D27, D33, D34 carry non-English locale codes. | D01-D04, D07-D08, D11, D16, D18-D23, D27, D31-D34, D36 | Limit | Check every Blender claim against the installed build's API and the English 5.2 pages. | 546, 548, 1456-1680 |
| LM15 | Installed toolchain unknown | The paper checked published documents only and never ran Blender or MCP. | | Limit | Query the installed API; run round-trip tests before relying on any call (rigging paper Q06 says the same). | 592, 1148 |
| LM16 | Capture vendors | Vendor quality comparisons are marketing; Rokoko terms restrict automated access; DeepMotion's pricing page contradicts its own FAQ (25 credits/month vs up to 60 seconds/month); DeepMotion's public changelog ends 2023-12-21. | A08-A15 | Limit | Verify the live account offer and terms before use. | 901-907 |
| LM17 | Meshy scope | Generated-motion retargeting is biped-only through the API and may return GLB only; web-app features do not carry over to the API; full contract coverage of a standalone clip is unchecked. | A21-A26 | Limit | Inspect result fields; read current terms before shipping. | 913-917 |
| LM18 | Licence blockers | UniMate checkpoints CC BY-NC 4.0 with unresolved provenance; HY-Motion licence excludes EU, UK, South Korea and the model cannot do animals, multi-person, seamless loops or in-place; Kimodo weights under NVIDIA terms (SMPL-X variant different); MoCapAnything BRIA component and Truebones data separate terms; ARDY needs gated Llama weights. The NVIDIA agreement shows two dates (release 2026-04-02, footer 2026-03-09). | A01, A04, A06, A16, A19, A27, A28 | Limit | No generated clip enters production before a rights check (DN08). | 889-955 |
| LM19 | Research numbers are not comparable | MoCapAnything released vs paper errors use different splits and implementations; Kimodo v1.1 had test-data leakage fixed in v1.2; smooth-root and raw-hips metrics differ; ARDY 33 ms is for an older 20-FPS model on an RTX 4090. | A05, A07, A17 | Limit | Do not rank tools; compare only like for like. | 895, 925, 939 |
| LM20 | Nothing was executed | No pseudocode run, no MCP session, no device benchmark, no AI tool run. All procedures, checklists and operation names are proposals. | P00 | Limit | Every skill rule built from OPINION rows needs a first real test. | 592, 634, 705, 885, 1148 |
| LM21 | Two MCP vocabularies | This paper proposes 7 operations (inspect_rig, render_views, write_action_batch, sample_pose, edit_curves, bake_export_copy, validate_roundtrip). The rigging paper proposes 10 (inspect_scene, inspect_rig, set_control, set_pose, set_mode_with_match, evaluate_frame, sample_deformed_mesh, bake_export_skeleton, validate_export, export_asset). Only inspect_rig is shared. | P00 | Open | Merge into one contract when the rig-pipeline skill is written; read the installed MCP's real tool schema first. | 634 |
| LM22 | No thresholds, no budgets | Key-reduction tolerance UNKNOWN; numeric review thresholds UNKNOWN; budget table maxima UNSPECIFIED; 19 of 26 timing rows have no phase counts (TL01-TL04, TL07-TL15, TL18, TL21-TL23, TL25, TL26). | P00 | Limit | Fill from the project or a measurement; never from this file. | 700, 839-844, 1023, 1104 |
| LM23 | Lab data is not a game preset | Hammer study: ten male nail-driving participants. Gecko, bat, bee, cat rows are event latencies or cycles. R27's 10-s limit is for packs only; R30's 30-FPS timeline is authoring only; R03's 20,000 triangles is an import limit. | B05, B07, B09, B16, B21, R03, R27, R30 | Limit | Use as measured context, not as production values. | 1106, 1138-1144, 817, 821 |
| LM24 | Wording in the register | R04 text speaks of a "single-mesh R1 NPC" (probably R15 or another rig label; the paper does not say). R15 means 15 meshes, not 15 joints. | R04, R05 | Wording | Check the R04 page. | 721 |
| LM25 | Platform-avatar features vs custom rigs | Optional fingers, spine/chest/toe-base joints, HRD/DRD, AJU and leaf-bone dropping are described for R15 platform avatars; client 720 was required at rollout. | R07, R08, R09 | Limit | Do not assume the same bone LOD or joint classes on a custom rig. | 733-743 |
| LM26 | LoadAnimation network-ownership sentence | The Animator page mentions network ownership, but the replication contract on the Animation page governs automatic replication. | R12 vs R13 | Limit | Follow R13; keep gameplay authority separate. | 755, 759 |
| LM27 | Rigid vs skinned evidence | R31 reports gains from Motor6D movement and one-part skinned rigs; R25 reports gains from a custom renderer; neither isolates the cause. | R25, R31 | Limit | Decide by own A/B on the target phone. | 809, 825, 829 |

### 11.2 Agreements and conflicts with the rigging note `02-weights-controls-export-tests.md` (extractor comparison)

"RP" = the rigging paper as recorded in that note. Where both papers cite the same Roblox page under different IDs, see LM01.

| id | topic | animation paper | rigging note | status | handling |
| --- | --- | --- | --- | --- | --- |
| AG01 | Influences and Root weights | at most 4 influences per vertex; no root vertex influences (AP:717, 854) | D01, CL01, CL02, SW3, SW4 | agree | none |
| AG02 | Triangle ceiling | 20,000 per mesh, not a mobile target (AP:717) | D02, LM01 | agree | none |
| AG03 | Avatar triangle budgets | gives numbers: head 4,000, torso 1,750, each arm or leg 1,248, total 10,742 (AP:725) | CL15 says the paper gave no numbers; `workflow.md` section 6 also lists none | AP adds figures | Fact-check against the local docs mirror; avatar-only. |
| AG04 | Optional joints | up to 37 additional (AP:725); 15 joints per hand and other optional joints for platform avatars (AP:733) | CL14 (37) | agree; AP adds R07 | none |
| AG05 | Zero-influence bones | off by default (AP:709) | X06, CL06 | agree | none |
| AG06 | glTF vs FBX hierarchy | glTF can add a Model level and MeshParts per primitive (AP:709) | CL09, X11 | agree | none |
| AG07 | Rig types | R15, Custom, No Rig (AP:709) | CL07 | agree | none |
| AG08 | General FBX export | Apply Scalings = FBX Unit Scale; Bake Animation off for static exports, on for animation (AP:713); no added leaf bones appears as the paper's test baseline (AP:688) and in the register key line of R02 (AP:1692) | X01, CL16-CL18 | agree | none |
| AG09 | Simplify 0.0 | an OPINION test baseline with a known reduction starting point, "not performance advice" (AP:688, 699), based on the Blender API | X01, CL21: VERIFIED for avatar-body animation export (RP source R5) | same value, different tag and scope | Keep both labels. Do not turn it into a universal Roblox rule. |
| AG10 | Constraints and baking | constraints are not saved in FBX (Legacy FBX manual); bake evaluated motion (AP:660) | K06, CL43; RP LM13 asks whether this holds for the non-legacy exporter | agree; open question remains | AP:556 says the manual still sends export to the add-on (D30); check which exporter is installed. |
| AG11 | Separate rest and clip exports | ACE accepts several clips in one FBX or glTF file since 2026-03-31 (AP:690, 729) | X02 advises a rest-model export and separate named clip exports | compatible; RP wording may predate multi-clip | Decide in the rig-pipeline skill; separate exports still work. |
| AG12 | Axis | no universal axis pair; do not call a Blender default Roblox's rule (AP:688, 690) | X04, LM07 | agree | none |
| AG13 | Scale | FBX Legacy manual says default 10, API says 1.0 (AP:552) | X04 names no multiplier; E01 | AP adds a doc conflict | Test with a known-size object. |
| AG14 | Actions, slots, channelbags | Blender 5.0 removed the legacy Action API; slots and channelbags are current (AP:548, 588; D04-D07) | K10, CL45; RP LM15: the source cited there has a key line about Auto IK | AP supplies the missing sources | Cite D04-D07 for CL45 after the fact-check. |
| AG15 | Blender version | 5.2.2 LTS 2026-09-15; daily builds show 5.2.3 RC (AP:546) | CL49: 5.2.2 on 2026-09-15; later patches not confirmed | agree; AP adds the RC | none |
| AG16 | Motor6D Transform | Animator usually overwrites Transform between PreAnimation and PreSimulation (AP:747) | CL23 | agree; AP gives the detail | none |
| AG17 | Collision | bone animation does not change collision shape (AP:721) | D17, CL22 | agree | none |
| AG18 | AnimationController | recommended when Humanoid functionality is unnecessary (AP:771) | CL36: "static NPCs", simple AnimationController | wording differs | Fact-check against the performance page. |
| AG19 | Maximum bone count | neither a bone count nor keyframe/duration ceiling is specified (AP:717); the 256-bones remark is commentary (AP:809) | Q01, D04 | agree | Never write 256 as a cap. |
| AG20 | Physics vs Animator ownership | AnimationConstraint has kinematic and force-based modes (AP:743) | N10, D18 | agree; AP adds modes | none |
| AG21 | Authoring-only features | exports carry evaluated motion, not control-rig semantics (AP:660) | W21, D12, CE3 | agree | none |
| AG22 | Format choice | FBX and glTF both supported; test the route (AP:690, 709) | X11 | agree | none |
| AG23 | Dual test (DCC and engine) | import success is not proof of the same runtime result; test blending and devices (AP:690, 692) | T01, M14, RB1-RB7 | agree | none |
| AG24 | Root-motion policy | default locomotion to in-place; displacement from gameplay (AP:813) | T04 allows for deliberate root motion; no policy | AP adds a policy (OPINION) | The rig sheet needs a root-motion field (OQ04). |
| AG25 | Time basis | exact conversion; effective fps = fps/base (AP:644) | X02: keep timing and source FPS explicit | agree | none |
| AG26 | MCP vocabulary | 7 operations (AP:634) | 10 operations (RP 4.3) | conflict of names | LM21. |

---

## 12. Claims to check (CL)

One row per number and per Roblox, Blender, AI-tool, science or industry fact in AP:542-1145. "Src" is the paper's own source ID (register at AP:1146-2056). Verdict column is left out on purpose: it belongs to step 2. `kind` is one of roblox, blender, ai-tool, science, industry; arithmetic is marked "(arithmetic)" next to its kind. The pseudocode API calls are claims, not working code (BL18).

### 12.1 Blender (CL01-CL46)

| id | claim | AP | src | kind |
| --- | --- | --- | --- | --- |
| CL01 | Blender 5.2.2 LTS (2026-09-15) is the latest stable release; the 5.2 release began 2026-07-14. | 546, 695 | D01-D03 | blender |
| CL02 | Blender 5.2 is supported through July 2028. | 546 | D01-D03 (no register key line shows the date) | blender |
| CL03 | Official daily builds list 5.2.3 Release Candidate, 5.3 Beta and 5.4 Alpha (builds of 2026-10-20), no newer stable. | 546 | D02 | blender |
| CL04 | 4.5.14 LTS is still supported and is not the latest stable line. | 546 | D01-D03 (4.5.14 is not named in any register key line) | blender |
| CL05 | Blender 5.0 removed action.fcurves, action.groups and action.id_root. | 548, 696 | D04 | blender |
| CL06 | Blender 5.0 was released 2025-11-18 (release-notes page undated). | 696, register 1476 | D04 | blender |
| CL07 | The current channelbag F-curve argument is group_name; action_group is legacy. | 548 | D04 | blender |
| CL08 | Slot creation needs an ID type and a name; a slot has a target ID type. | 548, 588, 602 | D05 | blender |
| CL09 | bpy_extras.anim_utils.action_ensure_channelbag_for_slot(action, slot) exists in 5.2; official helpers create or find a channelbag and the get helper returns the first match. | 588, 608 | D06 | blender |
| CL10 | In 5.2 an Action's animation data is always organized into slots; Action layers and strips exist in the API but there is no finished general multilayer Action UI. | 588 | D07 | blender |
| CL11 | The 5.2 FBX Legacy manual states a scale default of 10 while the pinned 5.2 exporter API declares global_scale=1.0. | 552 | D26, D28 | blender |
| CL12 | The FBX Legacy manual lists vertex shape keys as unsupported while the 5.1 release notes (2026-03-17) say the FBX exporter exports shape-key normals. | 552 | D28, D29 | blender |
| CL13 | glTF: since 4.4, Actions mode merges tracks by Action; NLA Tracks mode still groups by name. | 554 | D27 | blender |
| CL14 | A native FBX importer exists; the current manual still directs FBX export to the add-on. | 556 | D30 | blender |
| CL15 | Bone data lists names, parents/children, matrix_local, head_local, tail_local, length, deform and inheritance flags; bone-local Y runs head to tail. | 562 | D08, D34 | blender |
| CL16 | Envelope radii describe skin influence, not limb thickness. | 562 | D08 (inferred) | blender |
| CL17 | Bone.convert_local_to_pose accounts for inheritance and local-location settings. | 562 | D08 | blender |
| CL18 | PoseBone.matrix is the end matrix once constraints and drivers apply (armature-object space); matrix_basis is relative to parent and rest bone; world pose = evaluated matrix times the armature's world transform. | 564 | D09 | blender |
| CL19 | Constraints expose validity, influence, mute, target/subtarget, owner/target spaces, chain/pole and axis settings; Limit Rotation does not govern IK-affected bones. | 566 | D10, D33 | blender |
| CL20 | Object bounds are object-space corners; evaluated meshes include modifiers; temporary meshes must be cleared; re-evaluation invalidates evaluated references. | 568 | D11, D12 | blender |
| CL21 | armature.animation_data_create(), ad.action = action and ad.action_slot = slot assign an Action and slot. (sketch call) | 598-606 | D05 | blender |
| CL22 | bpy.data.actions.new(name) and action.slots.new(id_type='OBJECT', name=...) create an Action and slot. (sketch call) | 600-602 | D05 | blender |
| CL23 | bag.fcurves.ensure(path, index=..., group_name=...) returns an F-curve in a channelbag. (sketch call) | 616 | D04 | blender |
| CL24 | A freshly ensured F-curve has zero keyframe points (the sketch asserts it). | 618 | none stated (D04 cited for ensure) | blender |
| CL25 | keyframe_points.add(n) then foreach_set('co', flat list) is the fast bulk-write path. (sketch call) | 620-622, 630 | D16, D17 | blender |
| CL26 | key.interpolation = 'CONSTANT' gives a hold; curve.update() sorts keys and fixes handles. (sketch call) | 624-628 | D14, D15, D19 | blender |
| CL27 | Bone data paths come from path_from_id. (sketch call) | 612, 630 | D36 | blender |
| CL28 | Operators depend on context and can fail polling; Python threads can crash Blender. | 632 | D31, D32 (5.0 pages) | blender |
| CL29 | Constant interpolation holds until the next key; linear gives no velocity continuity; Bezier handles and easing are different controls; auto-handle smoothing can reach a wider neighborhood and overshoot. | 638 | D14, D19 | blender |
| CL30 | Euler channels have gimbal issues; quaternion channels are harder to edit; one rotation mode per keyed animation. | 650 | D18 | blender |
| CL31 | Quaternion scalar Bezier curves do not give uniform angular-speed SLERP. | 650 | none (P00) | blender |
| CL32 | Effective scene rate is fps divided by base. | 644 | D35 | blender |
| CL33 | Cycles modifier REPEAT repeats a value range; REPEAT_OFFSET adds the endpoint difference each cycle. | 654 | D20 | blender |
| CL34 | NLA Repeat, time scale and ranges reuse clips; NLA Combine uses quaternion composition. | 654 | D21 | blender |
| CL35 | Bake Action can capture final constrained transforms with visual keying; clean-curves removes redundant keys with no bound on foot drift. | 660 | D22 (5.0 API) | blender |
| CL36 | Constraint definitions are not saved in FBX (Legacy FBX manual). | 660 | D28 | blender |
| CL37 | Blender decimation works by ratio or by maximum F-curve deviation. | 662 | D23 | blender |
| CL38 | scene.frame_set evaluates the frame; the evaluated depsgraph gives driven, constrained and modifier results. | 678 | D12, D13 | blender |
| CL39 | bpy.ops.render with animation=True renders the animation range; Workbench is designed for fast animation previews. | 678 | D24, D25 | blender |
| CL40 | The FBX exporter exposes object scope (selected), leaf bones, Action or NLA clip choice, sampling and simplification options. | 686 | D26 | blender |
| CL41 | bake_space_transform=True is warned experimental or broken for armatures and animations. | 686 | D26 | blender |
| CL42 | FBX sampling step is in frames, not FPS. | 686 | D26 | blender |
| CL43 | glTF export has separate Action, active-action, NLA-track and scene modes. | 686 | D27 | blender |
| CL44 | An exporter simplification value of 0.0 is available as a no-simplification baseline. | 688, 699 | D26 | blender |
| CL45 | Orientation error for normalized quaternions: 2*acos(clamp(abs(dot(q_ref, q_test)), 0, 1)). | 666 | none | science |
| CL46 | A 30-fps interval is 1000/30 ms = 100/3 ms; a 60-fps interval is 1000/60 ms = 50/3 ms. | 644, 698 | D35 | science (arithmetic) |

### 12.2 Roblox (CL47-CL115)

| id | claim | AP | src | kind |
| --- | --- | --- | --- | --- |
| CL47 | The importer handles FBX and glTF rigging, skinning and animation; glTF/GLB can produce an extra Model level and MeshParts per primitive, FBX does not. | 709 | R01 | roblox |
| CL48 | Rig Type options are R15, Custom, No Rig. | 709 | R01 | roblox |
| CL49 | The importer exposes forward/up axis and scale-unit controls. | 709 | R01 | roblox |
| CL50 | Keep Zero Influence Bones is off by default. | 709 | R01 | roblox |
| CL51 | Roblox's Blender FBX guide: Apply Scalings = FBX Unit Scale; Bake Animation off for static exports, kept for animation keys. | 713 | R02 | roblox |
| CL52 | General rigging requirements: unit scale, zero rotations, root at origin, no root vertex influences. | 717 | R03 | roblox |
| CL53 | A 20,000-triangle import limit applies to individual meshes. | 717 | R03 | roblox |
| CL54 | The general specification's single-track-export statement is stale or narrower than the multi-clip ACE release. | 717 | R03, R06 | roblox |
| CL55 | No general maximum bone count and no general keyframe or duration ceiling is specified in the general specification. | 717 | R03 (negative claim) | roblox |
| CL56 | A vertex cannot be influenced by more than 4 bones or joints. | 717, 854, 873 | R03 | roblox |
| CL57 | Imported skin influences are stored in mesh asset data; Bone instances represent the skeleton; bone animation changes appearance, not collision shape. | 721 | R04 | roblox |
| CL58 | A single-mesh "R1" NPC (paper wording) is supported but lacks some standard R15 animation/humanoid integration. | 721 | R04 | roblox |
| CL59 | R15 denotes 15 specific meshes, not necessarily 15 skeletal joints. | 721, 725 | R04, R05 | roblox |
| CL60 | Avatar bodies have named parts and rig schema, +Z forward and +Y up, and Marketplace component budgets. | 725 | R05 | roblox |
| CL61 | Advanced R15 supports up to 37 additional optional bones/joints. | 725 | R05 | roblox |
| CL62 | Avatar triangle ceilings: head 4,000; torso 1,750; each arm or leg 1,248; total 10,742. | 725 | R05 | roblox |
| CL63 | ACE imports FBX and glTF, several clips per file, saves locally by clip name, offers rest-pose selection; local saves need separate publication. | 729 | R06 | roblox |
| CL64 | The ACE GA update (2026-03-31; register also lists 2026-01-15) fixed a 180-degree rotation bug from beta. | 690, 729, 874 | R06 | roblox |
| CL65 | Import 3D can upload animations directly; the two Studio import routes share the underlying import code. | 729 | R06 | roblox |
| CL66 | Optional R15 platform-avatar joints (fingers 15 per hand, spine/chest/clavicle/head-base, toe-base) were released 2026-05-04 with HRD/DRD/AJU support. | 733, 875 | R07 | roblox |
| CL67 | Optional torso/head joints required client 720 at rollout. | 733 | R07 | roblox |
| CL68 | Distant avatar leaf bones can be dropped by throttling. | 733 | R07 | roblox |
| CL69 | Adaptive Animation reached GA (2026-04-29); HRD maps humanoid skeletons, DRD maps fingers. | 737 | R08 | roblox |
| CL70 | Beta names changed: Pelvis to Spine, Left/RightToes to Left/RightToeBase. | 737 | R08 | roblox |
| CL71 | Standard R6/R15 need no manually added HRD for basic compatibility. | 737 | R08 | roblox |
| CL72 | With AJU enabled, R15 avatar joints use AnimationConstraints instead of Motor6Ds; C0/C1/Part0/Part1 are read-only aliases. | 743 | R09 | roblox |
| CL73 | Transform layering belongs in PreSimulation after Animator evaluation; evaluation may be throttled. | 743 | R09 | roblox |
| CL74 | AnimationConstraint kinematic mode follows animation directly; force-based mode introduces physics. | 743 | R09 | roblox |
| CL75 | Motor6D connects two BaseParts; Transform is the preferred procedural offset over C0/C1 and is not replicated as an ordinary property. | 747 | R10 | roblox |
| CL76 | The Animator usually overwrites Motor6D Transform between PreAnimation and PreSimulation; deferred transform application is batched (parallel job after PreSimulation). | 747 | R10 | roblox |
| CL77 | AnimationPriority resolves per joint; higher-priority tracks contribute until summed weight reaches one; equal-priority tracks blend by normalized weights. | 751 | R11 | roblox |
| CL78 | Priority order: Action4, Action3, Action2, Action, Movement, Idle, Core; Core's value 1000 does not make it highest. | 751 | R11 | roblox |
| CL79 | LoadAnimation creates a track; reuse a cached track or use GetTrackByAnimationId. | 755 | R12 | roblox |
| CL80 | The Animator must be in Workspace before loading. | 755 | R12 | roblox |
| CL81 | GetPlayingAnimationTracks includes fading-out tracks. | 755 | R12 | roblox |
| CL82 | EvaluationThrottled identifies skipped pose evaluation. | 755 | R12 | roblox |
| CL83 | API prose: PreferLodEnabled=false forces full fidelity and Workspace can disable throttling. | 755 | R12 | roblox |
| CL84 | Replication: an Animator created on the server inside the owning player's Character can have its tracks played by that player's client with replication; NPC tracks replicate only if loaded and started on the server; tracks from a locally created Animator do not replicate. | 759 | R13 | roblox |
| CL85 | AnimationTrack.Length is zero until loaded; Play takes fade, weight, speed; AdjustWeight blends over time. | 763 | R14 | roblox |
| CL86 | GetMarkerReachedSignal is the named-marker API; KeyframeReached is deprecated. | 763 | R14 | roblox |
| CL87 | Stop starts a fade-out; Stopped may precede complete loss of influence; Ended fires after the fade-out. | 763 | R14 | roblox |
| CL88 | Stop(0) has a documented Motor6D/MaxVelocity=0 freeze caveat. | 763 | R14 | roblox |
| CL89 | Destroying a track does not prove asset-cache or engine memory is returned immediately. | 763 | R14 | roblox |
| CL90 | IKControl solves a chain toward a target each frame and can layer over authored animation; Enabled=false disables it, weight 0 does not (smoothing and pole effects remain). | 767, 860 | R15 | roblox |
| CL91 | Roblox performance guidance: local NPC Animators, AnimationController when Humanoid is unneeded, pooling, proximity spawning, disabling unused humanoid states, limiting scale/hierarchy changes, removing unneeded animation metadata. | 771 | R16 | roblox |
| CL92 | Profiling scopes named: stepAnimation, stepHumanoid, updateInvalidatedFastClusters. | 771 | R16 | roblox |
| CL93 | Server-side TweenService replicates property changes each frame. | 771 | R16 | roblox |
| CL94 | ClientAnimatorThrottling Phase 3 (posts 2026-04-10, 2026-04-29): throttling is always-on, includes locally created characters, reduces far/offscreen pose frequency. | 775 | R17 | roblox |
| CL95 | Reported animation-CPU reduction of 25-30% from internal crowded-scene testing. | 775 | R17 | roblox |
| CL96 | PreferLodEnabled=false is only a hint to the LOD controller. | 775 | R17 | roblox |
| CL97 | Forum reply 6: track clocks and marker events continue while posing is skipped (author role unverified). | 775 | R17 | roblox |
| CL98 | 30 FPS is 100/3 ms and 60 FPS is 50/3 ms of whole frame time. | 779, 881 | R18 | roblox (arithmetic) |
| CL99 | MicroProfiler separates animation, physics, scripts and rendering; mobile is the best place to profile; custom scopes are available. | 779 | R18 | roblox |
| CL100 | PreloadAsync yields, reports per-asset final status through its callback, and does not throw when an asset fails. | 783 | R19 | roblox |
| CL101 | A reported limit of 64 simultaneous playing animations per character (2026-01-26); older 256 warnings and temporary 32 caps are historical. | 787, 876 | R20 | roblox |
| CL102 | An October reply (register 2026-10-04) reports continued 64-track warnings with avatar walk animations. | 791, 876 | R21 | roblox |
| CL103 | Animation Graphs are available for all games (2026-07-15); existing LoadAnimation scripts remain supported. | 797, 877 | R22 | roblox |
| CL104 | State Machines and Luau Expressions for graphs are a Studio-only beta (2026-10-08). | 801, 878 | R23 | roblox |
| CL105 | Pixel 6a report (2026-10-17/18): Android 17, Roblox 2.743.1136, batches of 20 local R15 rigs played a graph 10 s, destroyed, then 20 s wait. | 805 | R24 | roblox |
| CL106 | Total memory retained after three graph rounds: +133, +120, +54 MB; ordinary keyframe rounds did not show the same growth. | 805 | R24 | roblox |
| CL107 | About 5.7 MB per fresh graph track (Studio Animation-tag measurement). | 805 | R24 | roblox |
| CL108 | Large NPC report (2026-09-21): server single-part proxies, 10 Hz bucketed/parallel updates, scaling from trouble around 3-4k to 10k client NPCs. | 809 | R25 | roblox |
| CL109 | The developer's 256-bones-per-mesh statement is commentary; the register key line speaks of a single mesh with 8 bones. | 809, 1830-1834 | R25 | roblox |
| CL110 | Animator.RootMotion was unreleased (response dated 2026-01-21) although listed in the API; no later public release located. | 690, 813 | R26 | roblox |
| CL111 | The 2026-09-11 RDC roadmap places new default movement with root motion in Early 2027. | 813 | R32 | roblox |
| CL112 | Marketplace animation packs: standard R15, original work, CurveAnimation not KeyframeSequence, looping except Jump; each clip at most 10 s (pack scope). | 817, 880 | R27 | roblox |
| CL113 | The Animation Editor timeline shows seconds:frames at 30 FPS; loops do not interpolate final to first; the editor offers keyframe optimization. | 821 | R30 | roblox |
| CL114 | 1,000-assembly report (2026-01-01): gains from separate local-server testing, Motor6D movement instead of BulkMoveTo, one-part skinned rigs; register key line cites 180 FPS in Studio; hardware unspecified. | 825, 1868-1870 | R31 | roblox |
| CL115 | A skinned custom mesh avoids needing a BasePart per visual bone but still costs skinning, rendering and evaluation. | 829 | P00 | roblox |

### 12.3 AI tools (CL116-CL147)

| id | claim | AP | src | kind |
| --- | --- | --- | --- | --- |
| CL116 | Kimodo current Rigplay models are Kimodo-SOMA-RP-v1.2 and Kimodo-SOMA-RP-ArdyRep-v1.2, released 2026-10-15; the March launch and April v1.1 are older. | 889, 958 | A01, A05 | ai-tool |
| CL117 | The Kimodo repo provides Python inference, CLI and a motion-authoring demo; output is joint/root/contact data in NPZ with skeleton-specific alternatives; no verified direct Roblox exporter. | 889 | A01 | ai-tool |
| CL118 | Kimodo licences: Apache-2.0 code; SOMA/G1 weights under NVIDIA Open Model terms; SMPL-X variant under different NVIDIA R&D terms (agreement dated 2026-04-02, footer 2026-03-09). | 889 | A01, A04 | ai-tool |
| CL119 | Kimodo controls: text, pose keyframes, joint positions/rotations, paths, waypoints. | 891 | A02, A03 | ai-tool |
| CL120 | Kimodo generation is limited to 10 s per prompt. | 891 | A03 | ai-tool |
| CL121 | Kimodo recommends fewer than 20 constrained frames per constraint type, except the root path. | 891 | A03 | ai-tool |
| CL122 | SOMA predicts 30 joints internally and converts to a 77-joint export; most hand and finger detail is removed. | 891, 959 | A02 | ai-tool |
| CL123 | ARDY newest human checkpoints ARDY-SOMA-RP-30FPS-Horizon60 and ARDY-SOMA-RP-30FPS-KimodoRep-Horizon60 (2026-10-15); earlier Core checkpoints use 20 FPS. | 893, 960 | A06 | ai-tool |
| CL124 | ARDY CLI NPZ holds joint rotations/positions, root motion, foot contacts and FPS; the text encoder needs gated Llama weights. | 893 | A06 | ai-tool |
| CL125 | ARDY paper (2026-07-09): 33 ms average generation latency, four diffusion steps, RTX 4090, 40-frame window at 20 FPS. | 895 | A07 | ai-tool |
| CL126 | ARDY is purely kinematic, with possible skating/jitter and no physical dynamics. | 895 | A07 | ai-tool |
| CL127 | Rokoko Vision 3.0 moved into Create on 2026-07-16; dual-camera and online-webcam capture retired 2026-08-16. | 901 | A08 | ai-tool |
| CL128 | Vision 3.0 works from uploaded recorded video, exports FBX/BVH, and has no finger tracking at launch. | 901 | A08, A09 | ai-tool |
| CL129 | Create's FAQ permits commercial use of generated text and video motion; terms v2.0.1 (2026-07-16) include data-use/sublicensing provisions and restrict automated access. | 903 | A10, A11 | ai-tool |
| CL130 | DeepMotion Animate 3D offers FBX/BVH/GLB export, hand capture dependent on visibility and finger skeleton, foot-lock modes, plan-dependent commercial rights. | 905 | A12, A13, A14 | ai-tool |
| CL131 | DeepMotion pricing table lists 25 credits/month; the FAQ on the same page says up to 60 seconds/month. | 905 | A12 | ai-tool |
| CL132 | DeepMotion's public release-updates page ends at V5.1, 2023-12-21. | 907 | A15 | ai-tool |
| CL133 | Meshy Text to Motion API launched 2026-08-21; motion_task_id application followed 2026-08-26. | 913 | A21 | ai-tool |
| CL134 | Meshy Prime output: raw FBX clip, 10 credits; Swift output: BVH, 3 credits. | 913 | A22 | ai-tool |
| CL135 | Meshy prompts are limited to 400 characters; duration 2-10 s in 0.5-s steps; raw generated assets expire after three days. | 913 | A22 | ai-tool |
| CL136 | Meshy generated-motion retargeting requires a biped and rejects quadrupeds; it can succeed with GLB only and an empty FBX field. | 915, 961 | A23 | ai-tool |
| CL137 | Meshy FPS conversion options are 24, 25, 30, 60; programmatic rigging works well only for standard humanoids. | 915 | A23, A24 | ai-tool |
| CL138 | Meshy free-plan assets are CC BY 4.0, paid plans give private ownership; model rights depend on plan at creation (2026-08-27 explanation). | 917 | A25, A26 | ai-tool |
| CL139 | MoCapAnything V2: paper 2026-04-30; weights 2026-07-13; hosted demo 2026-07-15; data/splits 2026-09-04; predicts joint rotations for arbitrary skeletons; FBX preprocessing and BVH output; MIT code and weights; BRIA and Truebones separate terms. | 923 | A16, A29 | ai-tool |
| CL140 | MoCapAnything released Setting A on Zoo-Unseen: 5.70 cm mean joint-position error and 19.58 degrees rotation error; paper row 3.39 cm and 6.54 degrees on a different split. | 925, 962 | A17 | ai-tool |
| CL141 | The MoCapAnything repo caps samples at 150 joints. | 925 | A17 | ai-tool |
| CL142 | UniMate: paper 2026-09-04; code 2026-09-06; preview checkpoints 2026-09-27; v3 and custom-rig preprocessing 2026-10-05. | 931 | A18, A19, A20 | ai-tool |
| CL143 | unimate_uniml3d_f60_v3 accepts 5-70 joints and outputs 60 frames at 30 FPS; GLB/FBX export; custom GLB/glTF/FBX inputs. | 931, 963 | A19 | ai-tool |
| CL144 | UniMate code is MIT; checkpoints are CC BY-NC 4.0; model card flags unresolved provenance. | 931, 964 | A19 | ai-tool |
| CL145 | UniMate known failures: slide, drift, hover, ground penetration, rare topologies, off-prompt or static output; no native channel for exact per-joint spatial targets or environmental contacts. | 933 | A19, A20 | ai-tool |
| CL146 | Kimodo benchmark notes disclose test-data leakage in Rigplay v1.1 (fixed in v1.2); SEED models unaffected; smooth-root and raw-hips metrics not directly comparable. | 939 | A05 | ai-tool |
| CL147 | HY-Motion 1.0 and Lite released 2025-12-30; 2026-01-29 added evaluation code; no animals, multi-person, seamless loops or in-place generation; licence excludes EU, UK, South Korea. | 955 | A27, A28 | ai-tool |

### 12.4 Science and industry (CL148-CL159)

| id | claim | AP | src | kind |
| --- | --- | --- | --- | --- |
| CL148 | Hammer, 1-lb: cock 0.34 +/- 0.07 s, swing 0.07 +/- 0.04 s, strike-follow-through 0.39 +/- 0.03 s, total 0.81 +/- 0.11 s (ten male nail-driving participants). | 1113, 1138 | B21 | science |
| CL149 | Hammer, 2-lb: 0.44 +/- 0.18 s, 0.12 +/- 0.07 s, 0.43 +/- 0.03 s, total 0.99 +/- 0.22 s. | 1114, 1138 | B21 | science |
| CL150 | The 30-fps phase counts in TL05 and TL06 equal the source seconds in CL148 and CL149 times 30 (extractor re-check matched; see 9.4). | 1113-1114 | B21 | science (arithmetic) |
| CL151 | Gecko: response onset approximately 28.9 +/- 6.3 ms; tail contact 47.0 +/- 11.0 ms relative to forefoot contact; 30-fps 0.867 +/- 0.189 and 1.41 +/- 0.33; 60-fps 1.734 +/- 0.378 and 2.82 +/- 0.66. | 1127, 1140 | B05 | science |
| CL152 | Bat: approximately 125-175 capture intervals at 1000 fps = 0.125-0.175 s = 3.75-5.25 intervals at 30 fps = 7.5-10.5 at 60 fps. | 1124, 1142 | B07 | science |
| CL153 | Honeybee wingbeat approximately 230 Hz: 100/23 ms; 3/23 of a 30-fps interval; 6/23 of a 60-fps interval. | 1125, 1142 | B09 | science |
| CL154 | Cat pinna component approximately 25 ms = approximately 0.75 interval at 30 fps and 1.5 at 60 fps. | 1128, 1144 | B16 | science |
| CL155 | Drosophila tripod gait: approximately 0.5 cycle offset between tripod groups, half the measured cycle. | 1132, 1144 | B12 | science |
| CL156 | The Overwatch reload example uses 45 frames with no stated FPS. | 1112, 1144 | C18 | industry |
| CL157 | Context rows TL13-TL15, TL21-TL23, TL25, TL26 (pigeon takeoff/landing, bat flexion, swift glide, stick-insect antennae, lungfish and sunfish swimming, horse gait, spider locomotion, moment of inertia, microgravity) rest on the cited studies. | 1121-1123, 1129-1134 | B06, B08, B10, B11, B13, B15, B17, B18, B22, B25 | science |
| CL158 | Insomniac's facial-rigging talk compares poses to scans and checks the engine result (GDC 2019-03); Riot reports repeated playtests for cosmetic weapon feel (2020-05-18). | 996, 1030 | C15, C06 | industry |
| CL159 | Timing-row precedents: Uncharted 4 retrospective for decision reading (2021-05-10); WoW patch 7.3 caster animations (2017-08-16). | 1109, 1111 | C12, C10 | industry |

---

## 13. Source legend (IDs cited in AP:542-1145, resolved from the register AP:1146-2056)

All entries were checked by the paper's author on 2026-10-21 (AP:1148). "Undated" means no trustworthy date was found. Full URLs are in the paper at the register line; they are not copied here (the paper stays outside git). Register tag is VERIFIED unless the row says otherwise. R28 (animation capture) and R29 (dynamic head tutorial) are in the register but not cited in AP:542-1145. Note the ID clash with the rigging note (LM01).

### 13.1 Protocol, industry, animation teaching, science

| id | what | date (register) | register tag | reg line |
| --- | --- | --- | --- | --- |
| P00 | The paper's own proposed studio protocol (no outside URL) | 2026-10-21 | OPINION | 1150 |
| C06 | Riot, craft of VALORANT weapon skins | 2020-05-18 | EXPERIENCE | 1182 |
| C10 | Blizzard, WoW patch 7.3 new combat animations | 2017-08-16 | EXPERIENCE | 1208 |
| C12 | Naughty Dog, Uncharted 4 five-year retrospective | 2021-05-10 | EXPERIENCE | 1222 |
| C15 | GDC 2019, Spider-Man faces (Insomniac) | 2019-03 | VERIFIED | 1240 |
| C18 | GDC 2017 bootcamp abstract, first-person Overwatch animation (rhetorical question; FPS unspecified; shipped value not verified; page fetch timed out) | 2017 | VERIFIED (TL04 row says EXPERIENCE: LM13) | 1258 |
| B02 | Animation Mentor, follow-through and overlapping action | 2017-06-19 | EXPERIENCE | 1310 |
| B03 | Animation Mentor, animating weight and force | 2025-11-14 | EXPERIENCE | 1316 |
| B05 | Gecko active tails (PMC article) | 2008-03-17 | VERIFIED | 1328 |
| B06 | Pigeon takeoff and landing kinematics | 2010-05-15 | VERIFIED | 1334 |
| B07 | Bats, aerial rotations by wing inertia | 2015-11-16 | VERIFIED | 1340 |
| B08 | Bat upstroke wing flexion and inertial cost | 2012-04-11 | VERIFIED | 1346 |
| B09 | Honeybee short-amplitude high-frequency wing strokes | 2005-12-05 | VERIFIED | 1352 |
| B10 | Common swift gliding aerodynamics | 2011 | VERIFIED | 1358 |
| B11 | Horse gait characterisation | 2007-01-15 | VERIFIED | 1364 |
| B12 | Drosophila tripod gait | 2021-02-03 | VERIFIED | 1370 |
| B13 | Spider octopedal locomotion | 2011-10-15 | VERIFIED | 1376 |
| B15 | African lungfish undulatory swimming | 2008 | VERIFIED | 1388 |
| B16 | Cat pinna movements during sound localization | 1998-06-01 | VERIFIED | 1394 |
| B17 | Stick insect antennae, active tactile exploration | 2011 | VERIFIED | 1400 |
| B18 | Bluegill sunfish dorsal and anal fins | 2005-07-15 | VERIFIED | 1406 |
| B21 | Hammer mass and upper-extremity joint moments (phase values from the publisher's Results text; ten male nail-driving participants; means kept without repairing rounding) | 2017-04 | VERIFIED | 1424 |
| B22 | NASA, moment of inertia | undated | VERIFIED | 1432 |
| B25 | NASA, what is microgravity | undated | VERIFIED | 1450 |

### 13.2 Blender sources (D)

| id | what | date / version scope (register) | reg line |
| --- | --- | --- | --- |
| D01 | Blender 5.2 LTS release page | 2026-07-14 initial; 2026-09-15 patch | 1456 |
| D02 | Blender daily builds | builds of 2026-10-20 | 1462 |
| D03 | Blender LTS page | undated; accessed 2026-10-21 | 1468 |
| D04 | Blender 5.0 Python API release notes | 5.0 released 2025-11-18; page undated | 1474 |
| D05 | ActionSlot Python API | undated; 5.2 API | 1480 |
| D06 | bpy_extras.anim_utils API | undated; 5.2 API | 1486 |
| D07 | Actions manual | undated; 5.2 manual (non-English locale URL) | 1492 |
| D08 | Bone Python API | undated; current API indexed June 2026; current URL, not immutable | 1498 |
| D09 | PoseBone Python API | undated; 5.2 API | 1506 |
| D10 | Constraint Python API | undated; 5.2 API | 1512 |
| D11 | Object Python API | undated; current API indexed June 2026; current URL | 1518 |
| D12 | Depsgraph Python API | undated; 5.2 API | 1526 |
| D13 | Scene Python API | undated; 5.2 API | 1532 |
| D14 | Keyframe Python API | undated; 5.2 API | 1538 |
| D15 | FCurve Python API | undated; 5.2 API | 1544 |
| D16 | FCurveKeyframePoints Python API | undated; displayed 5.2; staging docs | 1550 |
| D17 | bpy_prop_collection Python API | undated; 5.2 API | 1556 |
| D18 | Rotation modes manual | undated; 5.2 manual (non-English locale URL) | 1562 |
| D19 | F-Curve properties manual | undated; displayed 5.2 (non-English locale URL) | 1568 |
| D20 | FModifierCycles Python API | undated; displayed 5.2; staging docs | 1574 |
| D21 | NLA sidebar manual | undated; 5.2 manual (non-English locale URL) | 1580 |
| D22 | NLA bake Python API | undated; 5.0 API (signature corroborated by official 5.2 staging) | 1586 |
| D23 | Editing F-Curves manual | undated; 5.2 manual (non-English locale URL) | 1594 |
| D24 | Render operators Python API | undated; 5.2 API | 1600 |
| D25 | Workbench manual | undated; displayed 5.2 | 1606 |
| D26 | Export Scene operators Python API | undated; 5.2 API | 1612 |
| D27 | glTF 2.0 manual | undated; 5.2 manual (non-English locale URL) | 1618 |
| D28 | FBX Legacy manual | undated; 5.2 manual | 1624 |
| D29 | Blender 5.1 Pipeline and I/O release notes | 5.1 released 2026-03-17; page undated | 1630 |
| D30 | FBX manual (native importer) | undated; displayed 5.2 | 1636 |
| D31 | Using Operators API gotchas | undated; 5.0 API | 1642 |
| D32 | Python threads are not supported | undated; 5.0 API | 1650 |
| D33 | Limit Rotation constraint manual | undated; 5.2 manual (non-English locale URL) | 1658 |
| D34 | Bone Structure manual | undated; 5.2 manual (non-English locale URL) | 1664 |
| D35 | Output Format manual | undated; displayed 5.2 | 1670 |
| D36 | bpy_struct Python API | undated; current API indexed June 2026; current URL | 1676 |

The register warns for D08, D11, D22, D31, D32, D36: validate the live 5.2 RNA before executing adjacent-version or current-indexed API guidance (AP:1504, 1524, 1592, 1648, 1656, 1682).

### 13.3 Roblox sources (R)

| id | what | date (register) | register tag | reg line |
| --- | --- | --- | --- | --- |
| R01 | Creator Hub, Importer | undated | VERIFIED | 1684 |
| R02 | Creator Hub, export settings (export requirements) | undated | VERIFIED | 1690 |
| R03 | Creator Hub, general specifications | undated | VERIFIED | 1696 |
| R04 | Creator Hub, rigging and skinning | undated | VERIFIED | 1702 |
| R05 | Creator Hub, character body specifications | undated | VERIFIED | 1708 |
| R06 | DevForum, Animation Clip Editor import release | 2026-01-15; 2026-03-31 | VERIFIED | 1714 |
| R07 | DevForum, full-body animation for platform avatars including fingers | 2026-05-04 | VERIFIED | 1720 |
| R08 | DevForum, Adaptive Animation GA | 2026-04-29 | VERIFIED | 1726 |
| R09 | Creator Hub, AnimationConstraint API | undated | VERIFIED | 1732 |
| R10 | Creator Hub, Motor6D API | undated | VERIFIED | 1738 |
| R11 | Creator Hub, AnimationPriority enum | undated | VERIFIED | 1744 |
| R12 | Creator Hub, Animator API | undated | VERIFIED | 1750 |
| R13 | Creator Hub, Animation class (replication contract) | undated | VERIFIED | 1756 |
| R14 | Creator Hub, AnimationTrack API | undated | VERIFIED | 1762 |
| R15 | Creator Hub, IKControl API | undated | VERIFIED | 1768 |
| R16 | Creator Hub, improve performance | undated | VERIFIED | 1774 |
| R17 | DevForum, ClientAnimatorThrottling Phase 3 rollout | 2026-04-10; 2026-04-29 | VERIFIED | 1780 |
| R18 | Creator Hub, MicroProfiler | undated | VERIFIED | 1786 |
| R19 | Creator Hub, ContentProvider API | undated | VERIFIED | 1792 |
| R20 | DevForum reply attributed to BloxHerder, concurrent playing-track limit (staff role unverified) | 2026-01-26 | EXPERIENCE | 1798 |
| R21 | DevForum, track limit logs (latest report) | 2026-02-06; 2026-10-04 | EXPERIENCE | 1804 |
| R22 | DevForum, Animation Graphs full release | 2026-07-15 | VERIFIED | 1812 |
| R23 | DevForum, State Machines and Expressions studio beta | 2026-10-08 | VERIFIED | 1818 |
| R24 | DevForum, Pixel 6a graph memory report (Khrrxs) | 2026-10-18; 2026-10-17 | EXPERIENCE | 1824 |
| R25 | DevForum, large NPC custom renderer (me7474) | 2026-09-21 | EXPERIENCE | 1830 |
| R26 | DevForum, Animator.RootMotion feedback | 2026-01-21 | VERIFIED | 1836 |
| R27 | Creator Hub, Marketplace animation packs | undated | VERIFIED | 1844 |
| R30 | Creator Hub, Animation Editor | undated | VERIFIED | 1862 |
| R31 | DevForum, 1,000-assembly optimization report (laindecat) | 2026-01-01 | EXPERIENCE | 1868 |
| R32 | DevForum, RDC26 what we announced (roadmap) | 2026-09-11 | VERIFIED roadmap | 2052 |

### 13.4 AI motion tool sources (A)

| id | what | date (register) | register tag | reg line |
| --- | --- | --- | --- | --- |
| A01 | Kimodo official repository | 2026-10-15 release update | VERIFIED | 1874 |
| A02 | Kimodo skeleton documentation | undated; accessed 2026-10-21 | VERIFIED | 1880 |
| A03 | Kimodo best practices and limitations | undated; accessed 2026-10-21 | VERIFIED | 1886 |
| A04 | NVIDIA Open Model Agreement | release date 2026-04-02 displayed; footer v. 2026-03-09 | VERIFIED | 1892 |
| A05 | Kimodo current benchmark results | updated 2026-10-15 | VERIFIED | 1898 |
| A06 | ARDY official repository | 2026-10-15 SOMA checkpoint release; initial 2026-07-10 | VERIFIED | 1904 |
| A07 | ARDY paper | 2026-07-09; TOG/SIGGRAPH 2026 | VERIFIED | 1910 |
| A08 | Rokoko Studio 2.6.2 Vision 3.0 support | 2026-07-16 transition; 2026-08-16 legacy retirement | VERIFIED | 1916 |
| A09 | Rokoko Vision product page | undated; accessed 2026-10-21 | VERIFIED | 1922 |
| A10 | Rokoko Create commercial-use FAQ | undated; accessed 2026-10-21 | VERIFIED | 1928 |
| A11 | Rokoko Services Terms of Use | 2026-07-16, version 2.0.1 | VERIFIED | 1934 |
| A12 | DeepMotion Animate 3D pricing | undated; accessed 2026-10-21 | VERIFIED | 1940 |
| A13 | DeepMotion hand-tracking FAQ | 2022-06-16; current FAQ inspected 2026-10-21 | VERIFIED | 1946 |
| A14 | DeepMotion foot-locking documentation | undated; accessed 2026-10-21 | VERIFIED | 1952 |
| A15 | DeepMotion Animate 3D release updates | latest displayed entry 2023-12-21 | VERIFIED | 1958 |
| A16 | MoCapAnything V2 official repository | 2026-05-01 code; 2026-07-13 weights; 2026-07-15 demo; 2026-09-04 data/splits | VERIFIED | 1964 |
| A17 | MoCapAnything V2 reproduction documentation | current release documentation accessed 2026-10-21 | VERIFIED | 1970 |
| A18 | UniMate official repository | 2026-09-06 code; 2026-09-27 preview; 2026-10-05 custom rig pipeline | VERIFIED | 1978 |
| A19 | UniMate model card | v3 2026-10-05; v2 2026-09-28; preview 2026-09-27 | VERIFIED | 1984 |
| A20 | UniMate paper | 2026-09-04; accepted at SIGGRAPH Asia 2026 | VERIFIED | 1992 |
| A21 | Meshy API changelog | 2026-08-21 Text to Motion; 2026-08-26 motion_task_id | VERIFIED | 1998 |
| A22 | Meshy Text to Motion API | undated docs; feature date from A21 | VERIFIED | 2004 |
| A23 | Meshy Animation API | undated current docs; accessed 2026-10-21 | VERIFIED | 2010 |
| A24 | Meshy Rigging API | undated current docs; accessed 2026-10-21 | VERIFIED | 2016 |
| A25 | Meshy commercial-use explanation | 2026-08-27 | VERIFIED | 2022 |
| A26 | Meshy animation workflow page | undated current page; accessed 2026-10-21 | VERIFIED | 2028 |
| A27 | HY-Motion 1.0 official repository | 2025-12-30 models; 2026-01-29 evaluation update | VERIFIED | 2034 |
| A28 | HY-Motion 1.0 licence | 2025-12-30 release licence | VERIFIED | 2040 |
| A29 | MoCapAnything V2 preprint record | 2026-04-30 | VERIFIED | 2046 |
