---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T02, Roblox_Character_Rigger_Research.txt lines 265-596
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Rigging paper part 2: weights, non-humans, faces, controls, export, tests, method, Tripo repair

Paraphrased notes on paper lines 265-596 (sections 5-11, "Do not do", "Open questions"). Source IDs and dates resolved from paper lines 597-849. The paper itself stays outside git. Nothing here was fact-checked; every claim is listed in table CL for step 2.

## 0. How to read

| Key | Meaning |
| --- | --- |
| RP:n | Line n of `Roblox_Character_Rigger_Research.txt` (paper). |
| Tag | Evidence tag copied from the paper: VERIFIED, EXPERIENCE, OPINION, OPINION-unresolved (paper writes "OPINION — unresolved"). Combined tags are kept as the paper wrote them. No EXPERIENCE tag occurs in lines 265-596; the only EXPERIENCE source is E1 (RP:840). |
| Stage | Workflow stage from `workflow.md`: S0 intake, S1 motion needs (animator), S2 rig plan (rigger), S3 geometry (modeler), S4 geometry acceptance (rigger), S5 rig + tests (rigger), S6 rig acceptance (animator), S7 animate and export (animator), S8 owner final. |
| [A] | `[for-animator]`: the animator must know it or supply the input. |
| [M] | `[for-modeler]`: the modeler must know it or must act on it. |
| Src | Paper source ID. Resolved list in section 13. All paper checks were done on 2026-10-20; "undated" means the page showed no date. |
| IDs | W weights, N non-humans/mechanical, F faces, K controls, X export/import, T tests, M method, R repair, P AI failure pattern, D do-not, Q open question, CL claim to check, LM contradiction or limit. |

Global caveats the paper states about itself (RP:847): no Blender rig, generated character, MCP session or Roblox round trip was run to write it. All procedures are proposals. No studio budget, angle table, Tripo rigging cap, success rate or repair-time estimate is given. Where a table here says "project-defined", the number must come from the rig sheet requirements, not from this file.

---

## 1. Section 5: Weight painting and deformation (RP:265-292)

### 1.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| W01 | Blender has Normalize All, Clean, Limit Total and weight-transfer tools. Armature modifier option Preserve Volume uses quaternion deformation. | S5 | | VERIFIED | B1, B2 | 267 |
| W02 | Build a deform-group allowlist from the export bones. When counting influences, ignore control-only selection groups. | S5 | | OPINION | none | 269 |
| W03 | Per deforming vertex inspect: weights finite and not negative; total not zero; group names match the intended bones; at most 4 influences. | S5 | | OPINION | R1 (limit) | 269 |
| W04 | A rigid region gets one designated bone at weight 1. Weight 1 defines "rigid single-bone binding"; it is not a measured quality threshold. | S2, S5 | [M] (cut pieces are bound this way) | OPINION | none | 269, 290 |
| W05 | Cleanup order: (1) remove accidental non-deform groups; (2) repair unweighted regions; (3) remove irrelevant or cross-body support; (4) prune to the allowed influence count; (5) normalize what remains; (6) retest. Normalizing first, then pruning, leaves a non-normalized result. | S5 | | OPINION | none | 271, 289 |
| W06 | Set the tiny-weight removal threshold from measured visual tolerance and asset scale. Never delete all small values blindly. | S5 | | OPINION | none | 271 |
| W07 | Recheck locked groups and settings after cleanup: interactive normalization can leave protected (locked) groups unchanged. | S5 | | OPINION | none | 271 |
| W08 | Use segmentation masks to limit where each bone may influence. | S2, S5 | | OPINION | none | 273 |
| W09 | Mark protected vertices that must stay still in a head-only or hand-only test. Compute per-vertex displacement; report the worst violations with bone names and positions. | S5, S6 | [A] (animator re-runs isolation on the real rig) | OPINION | none | 273 |
| W10 | A smooth weight gradient can still be wrong. The smallest nonzero weight on a remote bone moves the mesh when that bone moves. | S5 | | OPINION | none | 273 |
| W11 | Debug deformation in a fixed order (table 1.2). | S5, S6 | [A] | OPINION | none | 275 |
| W12 | A joint inside the skull instead of at the neck base cannot be fixed by repainting. | S2, S5 | | OPINION | none | 275 |
| W13 | If the whole character moves with the head, inspect parent links and animation channels before touching local neck weights. | S5, S7 | [A] | OPINION | none | 275 |
| W14 | Shoulder collapse: split the approved movement between arm and clavicle/torso, keep the armpit crease, isolate rigid pads. | S1, S2, S3 | [A] (approved shoulder ROM and how it is split), [M] (armpit crease and pad geometry) | OPINION | none | 277 |
| W15 | Knee/elbow pinching: confirm the hinge center and the compression-side geometry before widening the weight span. | S2, S3 | [M] | OPINION | none | 277 |
| W16 | Hip collapse: check pelvis and leg support and leakage from the opposite thigh. | S5 | | OPINION | none | 277 |
| W17 | Twisting forearm or tail: spread the twist over a justified chain with localized weights. Do not put a large relative rotation on one transition. | S1, S2 | [A] (twist range per limb), [M] (length of geometry in the chain) | OPINION | none | 277 |
| W18 | Neither linear blending nor ordinary dual quaternion skinning (DQS) is artifact-free in all cases. Auto-Rig Pro warns that a volume-preserving Blender preview can differ from ordinary game-engine skinning and advises export-aware checks. | S5 | [A] | VERIFIED | D1, D2, B4 | 279 |
| W19 | Historical Roblox skinning documentation names linear skeletal skinning. It is historical evidence, not a 2026 implementation guarantee. | S5 | | VERIFIED (historical) | R10 | 279 |
| W20 | Use Preserve Volume off as a conservative authoring preview; the real Roblox result decides. Do not claim a current Roblox DQS toggle without a current source and a test. | S5 | | OPINION | none | 281 |
| W21 | A helper bone helps only if it survives export and is driven by baked animation or a defined runtime mechanism. Do not assume a Blender driver or corrective modifier runs in Studio. | S2, S5, S7 | [A] (helper must be keyed or baked by the animator or the runtime) | OPINION | none | 281 |
| W22 | Corrective shape recipe: define the target shape in the problem pose; subtract what the base rig already supplies; isolate the correction; test intermediate and combined poses. Use it as an authoring reference or turn it into supported articulation. Arbitrary body shape-key import is not established. Roblox FACS combination corrections are a face pipeline only; do not generalize them to body morphs. | S5 | | OPINION (FACS fact VERIFIED in section 3) | R11 | 283 |
| W23 | Stress tests must combine degrees of freedom: arm raised plus forearm twist; head turned plus torso bend; hip flexed plus leg spread; tail curved plus base rotation. | S1, S5 | [A] (animator's stress poses feed these) | OPINION | none | 285 |
| W24 | Compare shaded, wireframe, silhouette, UV-checker and in-game material views. Reject unapproved spikes, collapsed volume, texture smears, detached seams or self-intersection in required shots. | S4, S5 | [M] (texture smears, seams) | OPINION | none | 285 |

### 1.2 Debug order (W11, RP:275)

| order | check first | notes |
| --- | --- | --- |
| 1 | rest and bind transforms, hierarchy | before any weight work |
| 2 | joint positions and axes | W12: wrong pivot cannot be repainted |
| 3 | unintended geometry bridges | fused surfaces (see P03) |
| 4 | weight support and normalization | W03, W05 |
| 5 | edge flow and density | topology belongs to modeler |
| 6 | helper-joint distribution | W21 |
| 7 | final corrective shapes | W22, last resort |

### 1.3 Rule table (RP:287-292, copied as data)

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Prune and normalize separately | at most 4 deform influences | VERIFIED tools/limit; OPINION order | B2 checked 2026-10-20; R1 checked 2026-10-20 |
| Rigid single-bone binding | weight 1 to the designated bone | OPINION implementation definition | proposed policy 2026-10-20 |
| Do not rely on authoring-only deformations | no guaranteed body corrective transfer | OPINION | B4 undated, checked 2026-10-20 |
| Include combined-pose testing | asset-specific angles and tolerances (none given) | OPINION | D1 2013; D2 2016-07-11 |

---

## 2. Section 6: Non-humans and mechanical rigs (RP:294-317)

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| N01 | Quadruped: separate shoulder mass, front-limb articulation, pelvis/hindlimb articulation, paws or hooves, neck, spine. Build a side-view chain from skeletal landmarks and contact reference. | S1, S2 | [A] | OPINION | none | 296 |
| N02 | Do not call a raised hock a backwards human knee. Decide plantigrade, digitigrade or hoof-supported. Agree the bend plane and contact orientation with the animator; do not guess from fur volume. | S1, S2 | [A], [M] | OPINION | none | 296 |
| N03 | Pets: spend articulation where it reads (head attitude, torso bounce, ear and tail silhouette, paw contact, face). Some pets need only a rigid bobbing body and rotating head; others a full gait. Export joints may be fewer than control joints. Decide by camera tests and measured crowd cost; no universal pet-bone budget. | S1, S2, S5 | [A] | OPINION | R13 | 298, 317 |
| N04 | Tails and tentacles: enough length-wise geometry and distributed joints for the needed curve. Start from a neutral shape that bends both ways. Test base rotation, opposed curves, tip motion, several appendages near each other. Say for each segment: explicit animation, spline authoring control, or runtime secondary motion. A Blender spline constraint does not become a Roblox solver. | S2, S3, S5 | [A] (which segments are keyed vs secondary), [M] (geometry length) | OPINION | none | 300 |
| N05 | Roblox Creature case: dense central tentacles are grouped, tips stay separate, fewer joints. It advises economical joints and a neutral initial shape. | S2 | [A], [M] | VERIFIED (legacy case) | R6 | 302, 314 |
| N06 | Birds: decide separately shoulder/elbow/wrist, feather spread, wing fold, body transition. Use skin membranes or continuous soft transitions; use rigid feather groups where shape must hold. Test spread and fold as full silhouettes. | S1, S2, S3 | [A], [M] | OPINION | none | 304 |
| N07 | Insects and multi-leg chains: write down chain order, side convention, ground-contact map; avoid accidental cross-limb IK target assignment. | S2, S5 | [A] | OPINION | none | 304 |
| N08 | Mechanisms start with a kinematic diagram: fixed frame, moving link, pivot or rail axis, travel envelope, parent relation, physical owner. Weapons need stable grip and muzzle frames; separate magazine, bolt, trigger, hammer or attachments only where they move. Reload detachment and hand switching are explicit hierarchy or ownership changes, not skin gradients. | S1, S2, S3 | [A], [M] | OPINION | none | 306 |
| N09 | Wheels turn on the axle center; steering on the approved steering axis; suspension on its real linkage or a simplified visual contract; doors on the hinge line (not mesh center); sliding parts along a rail; turrets split yaw and pitch frames; pistons need endpoints, linked travel and clearance checks. Rigid metal uses rigid transforms; a rubbery door means bad weights or the wrong representation. | S2, S3, S5 | [A], [M] | OPINION | none | 308 |
| N10 | Visual animation and physics simulation are separate. A bone-driven wheel is not a physics wheel. Specify Roblox constraints, proxies and gameplay collision separately. Never animate one degree of freedom through physics and an Animator at once without an ownership design. Test collision on its own because bone motion does not deform the collision shape. | S2, S5 | [A] | OPINION; collision fact VERIFIED | R7 | 310, 315 |

Rule table (RP:312-317): neutral appendages and economical chains, no universal chain count, VERIFIED case, R6 undated; collision does not follow skin deformation, VERIFIED, R7 undated; chains and pivots chosen by morphology, per-asset ROM and linkage, OPINION, proposed workflow 2026-10-20; pet complexity from camera and crowd test, project-measured budget, OPINION, R13 undated.

---

## 3. Section 7: Faces (RP:319-338)

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| F01 | Pick the face method from shot size, needed expression transitions, customization and avatar compatibility. Texture swaps suit deliberately graphic faces and discrete expressions. Skeletal faces suit lids, brows, mouth, jaw or gaze that must interpolate in space. A mixed face: rigid eyeballs and teeth, skinned lids and lips. A texture face still needs a UV layout and a runtime way to change expressions. | S1, S2 | [A] (which expressions), [M] (UV layout) | OPINION | none | 321 |
| F02 | Texture faces in-experience: define the allowed expression IDs, texture assets, hold time and reset state. Test the real material or decal path on the curved head at camera distance. Prevent duplicated coplanar face cards. Texture swaps give no depth, lip contact or dynamic-head semantics. | S2, S5 | [A], [M] | OPINION | none | 323 |
| F03 | Roblox basic dynamic head: skinned facial joints, FACS poses, frame-to-pose mapping, FaceControls. 50 base poses; 17 required poses for Marketplace sale; neutral at frame 0; each non-neutral pose on its own later frame; combination-pose corrections for overlapping actions. | S2, S5, S7 | [A] (face clips use this frame layout) | VERIFIED | R11 | 325, 335-337 |
| F04 | Build dynamic heads from current Roblox reference files. Isolate jaw, lips, lids, eyes so each can be driven alone. A textured line that looks like a mouth has no mouth cavity: choose remodel, graphic swap, or a deliberately simple jaw. Inspect generated face detail as geometry; a good render does not make it rig-ready. | S2, S3 | [M] | OPINION | none | 327 |
| F05 | Face tests: neutral, eye closure and gaze, smile and frown, jaw open, required speech shapes, and combinations that share lid/cheek or mouth regions. Check lid contact, lip closure, tooth penetration, no weight leak into the neck. Stylize anatomy on purpose; no bone budget below the camera's readability. | S5, S6 | [A], [M] | OPINION | none | 329 |
| F06 | Blender shape keys are not treated as automatically supported dynamic-head input. Use the documented joint-pose pipeline unless a current official path and an import test show another. 50 FACS poses are not 50 mandatory face bones; required expression count is not the joint count. | S2 | [A] | OPINION-unresolved | none | 331 |

Rule table (RP:333-338): FACS semantics for standard dynamic heads, 50 base poses, VERIFIED, R11 undated; Marketplace subset 17 poses in the cited workflow, VERIFIED, R11; neutral at frame 0, VERIFIED, R11; texture or bone face chosen from visual need, no universal face-bone count, OPINION, proposed workflow 2026-10-20.

---

## 4. Section 8: Animator controls and the Python interface (RP:340-374)

### 4.1 Lessons

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| K01 | Keep two things: an authoring control rig and a defined export skeleton. Control bones, IK targets, poles, widgets, drivers, constraints and selection helpers are authoring only. Export carries the deform hierarchy plus approved non-deforming sockets and roots. Exporting only Deform bones can drop a needed non-deforming root; exporting all controls bloats and destabilizes the schema. Use an explicit allowlist and parent map. | S5 | [A] (animator keys controls, export carries bones) | OPINION | none | 342 |
| K02 | Rigify makes a reusable control rig from a metarig, with controls and IK/FK features. Auto-Rig Pro game export supports Humanoid and Universal skeletons and has custom-bone export rules. | S5 | | VERIFIED | B3, B4 | 344 |
| K03 | FK for direct rotation and clean arcs; IK to hold hand or foot contact. Give a consistent pole convention; avoid an exactly straight chain in the working pose. The animator can reset the rig and knows which controls to key. Add foot roll, hand grip, jaw, gaze, tail controls only when the action list needs them. | S1, S5, S6 | [A] | OPINION | none | 346 |
| K04 | IK/FK switching is pose matching: evaluate current result, match destination controls in the documented spaces, keep pole direction, change blend or mode, key the right properties. Test at action extremes and contact frames. A Boolean that snaps is not a finished switch. | S5, S6 | [A] | OPINION | none | 348 |
| K05 | Space switching: capture the current world matrix, change parent or constraint state, compute the offset that keeps the world pose, then key switch and offset. Test hand world-to-weapon and weapon hand-to-holster. State which system drives each object in each phase so motion is not applied twice. | S5, S6 | [A] | OPINION | none | 350 |
| K06 | Blender PoseBone API separates the final evaluated pose matrix from transform channels and bone-relative matrix access. FBX baking exports evaluated motion, not the live constraint graph. | S5, S7 | [A] | VERIFIED | B5, B6 | 352, 371 |
| K07 | An AI animator reads a semantic control manifest, not controller names guessed from viewport shapes (fields in 4.2). | S5, S6 | [A] | OPINION | none | 354-359 |
| K08 | Expose a small, stable automation surface (4.3). The names are proposed studio wrappers, not Blender or MCP names. Read the real MCP tool schema and add-on operators first. MCP is transport; it repairs no context, matrix or unsupported export feature. | S5 | | OPINION | none | 361 |
| K09 | Use direct bpy data access for repeatable edits; use explicit context overrides for operators. Edit armature structure in Edit Mode and pose in Pose Mode as the versioned API requires. edit_bones, rest bones and pose bones are different views. Keep intended rest orientation and roll; do not force rest axes to world zero to clear transform channels. Update the dependency graph before reading final geometry or contact matrices. | S5 | | OPINION | none | 363, 574 |
| K10 | Check source-to-export mapping with evaluated matrices and sampled vertices, not action names. Equal names do not prove equal bone spaces. Audit Actions and slots in the installed Blender; do not hardcode old F-curve traversal or an undocumented add-on operator ID. Record bpy.app.version_string, add-on versions, exporter identity and options, and real action-to-object links in the build manifest. | S5, S7 | [A] (action naming and clip list) | OPINION | B6, B7 | 365 |
| K11 | Make automation reversible and idempotent: inspect, resolve asset IDs, check expected scene state, save a checkpoint, change one stage, evaluate, record evidence. A rerun updates its own named output; it must not add another armature, modifier or joint. After an MCP disconnect, query scene and task IDs before retrying a change. | S5 | | OPINION | none | 367, 548 |

### 4.2 Control manifest fields (RP:354-359, complete, 20 fields)

| # | field | note |
| --- | --- | --- |
| 1 | control_id | |
| 2 | Blender object path | |
| 3 | pose-bone or property identifier | |
| 4 | role | |
| 5 | side | |
| 6 | coordinate_space | K04, K05 need the documented spaces |
| 7 | allowed_channels | |
| 8 | rotation_mode | |
| 9 | units | |
| 10 | minimum/maximum where approved | paper says "where approved": ranges are approved by the animator/owner side (my link to workflow S1 ROM) |
| 11 | neutral value | |
| 12 | dependencies | |
| 13 | IK/FK mode property | |
| 14 | snap routine | K04 |
| 15 | space-switch routine | K05 |
| 16 | export mapping | K01, K10 |
| 17 | keying policy | |
| 18 | named pose library | |
| 19 | contact markers | |
| 20 | validation query | |

### 4.3 Proposed automation operations (RP:361). Proposed studio wrappers, not real Blender or MCP API.

| # | proposed op | paper context (my link, not a paper definition) |
| --- | --- | --- |
| 1 | inspect_scene | K11 "inspect first"; P09 inventory diff |
| 2 | inspect_rig | K07 manifest, K09 bone views |
| 3 | set_control | manifest fields 6-11 |
| 4 | set_pose | manifest field 18 |
| 5 | set_mode_with_match | K04 IK/FK match, K05 space match |
| 6 | evaluate_frame | K09 depsgraph update, K10 evaluated matrices |
| 7 | sample_deformed_mesh | W09 displacement metrics, T04 |
| 8 | bake_export_skeleton | K06, K01, M13 |
| 9 | validate_export | CE checklist items, X03 |
| 10 | export_asset | X01-X05 profile |

### 4.4 Rule table (RP:369-374)

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Bake constraints into target motion | constraint definitions not carried by legacy FBX | VERIFIED | B5, 5.2 manual, checked 2026-10-20 |
| Use versioned API and evaluated matrices | Blender 5.2 documentation baseline | VERIFIED API; OPINION wrapper design | B6/B7 checked 2026-10-20 |
| IK/FK and parent switching must keep the pose | project-defined error tolerance | OPINION | B3/B4 checked 2026-10-20 |
| Keep authoring and export schemas explicit | no universal control or deform count | OPINION | proposed workflow 2026-10-20 |

---

## 5. Section 9: Export and import (RP:376-427)

### 5.1 Export profile (RP:378-388)

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| X01 | Roblox general export guidance: FBX Unit Scale, Add Leaf Bones off, no Bake Animation unless animation data is wanted. Avatar-body guidance also: Custom Properties on; for its animation export NLA Strips, All Actions and Force Start/End Keyframes off; Simplify 0.0. | S5, S7 | [A] | VERIFIED | R4, R5 | 380, 423-424 |
| X02 | Keep a rest-model export and separate, named test-clip exports. Bake the evaluated deform/export skeleton, not only controller keys. Keep timing and source FPS explicit. Use the avatar animation settings when exporting FACS data; do not drop facial pose data under a generic no-animation preset. Do not blindly apply the Armature modifier when told to "apply modifiers"; finish geometry-changing modifiers on a controlled export copy and keep the skin and skeleton data. | S5, S7 | [A] | OPINION | none | 382 |
| X03 | Avatar body spec: characters face +Z and stand on +Y; I, A or T pose accepted; template origins and hierarchy are specified. Importer exposes World Forward, World Up, Scale Unit and pivot settings. | S5 | | VERIFIED | R2, R3 | 384 |
| X04 | Do not equate the avatar +Z convention with the runtime direction of every custom assembly or camera. Export Blender Z-up through a saved profile; test a labeled forward/up reference and the real movement direction. No axis pair is proven universal across exporters. Record axis_forward and axis_up only after checking the installed exporter and import profile. The paper gives no scale multiplier (names 0.01 and 100 as not prescribed). | S5 | [A] (facing in clips) | OPINION | none | 386 |
| X05 | Calibrate units with a dimensioned reference or the official template; compare exported and imported size in studs. Clean object and armature transforms before binding; keep needed rest-bone orientations; no negative or non-uniform scale in the final skeleton; never fix scale by stacking unrelated factors. A scale change after skinning needs a controlled rebake or rebind and a regression test. | S2, S5 | [M] (modeler delivers clean transforms and real scale) | OPINION | R4, R5 | 388 |

### 5.2 Studio procedure (RP:390-396)

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| X06 | Studio import is File > Import. It handles FBX and glTF rig, skin and animation data; OBJ is not suitable for rig data. Rig Type: R15, Custom, No Rig. Keep Zero Influence Bones is off by default. glTF/GLB can give a different hierarchy from FBX, including extra model nodes. | S5 | | VERIFIED | R3 | 392, 425 |
| X07 | Import with the intended rig type. Read the whole proposed hierarchy and warnings before accepting. Keep separate objects where rigid articulation needs them; do not merge parts blindly. Choose Keep Zero Influence Bones on purpose for sockets and non-deforming roots. Inspect MeshParts, joints/Bones, attachments, controller, Animator. Import each test animation against the right rig; check publish and use permissions and playback in the real project. | S5, S7 | [A], [M] (separate objects must stay separate) | OPINION | none | 394 |
| X08 | If R15 compatibility is needed: run Avatar Setup/validation, test attachments and proportions, set advanced rig-description objects for optional articulation. For a custom asset: attach the agreed runtime controller and collision/proxy setup instead of forcing avatar publishing checks. | S2, S5 | | OPINION | R2, R12 | 396 |

### 5.3 Failure table (RP:400-411, complete, 10 rows)

| id | symptom | likely causes to inspect | correction and decisive check | stage | flag | RP |
| --- | --- | --- | --- | --- | --- | --- |
| E01 | Model rotated, mirrored or wrong size | axis conversion, scene units, exporter scale, negative transforms, importer units | compare dimensioned axes and studs; change one documented profile stage | S5 | | 402 |
| E02 | Head rotates and body skews | wrong hierarchy; cross-body weights; shared control transform; duplicate deformation | isolate head bone and protected chest vertices; check weights and evaluated matrices | S5, S6 | [A] | 403 |
| E03 | Armature moves but surface stays | missing weights; bad group names; wrong Armature target; no skin in export | verify the binding in source, export copy and imported MeshPart | S5 | | 404 |
| E04 | Missing bones or sockets | export allowlist; add-on custom-bone tags; zero-influence removal | keep the needed nodes explicitly; compare hierarchy manifests | S5 | | 405 |
| E05 | Animation absent or wrong clip | controller keys not baked; wrong Action/slot; NLA/all-actions ambiguity; wrong frame range | bake a named clip; read imported joint transforms | S7 | [A] | 406 |
| E06 | Rigid part bends or detaches | smoothed weights; wrong parent or joint frame; missing rest offset | restore rigid binding or fix Motor6D tree; run pivot and shape test | S5 | [M] | 407 |
| E07 | Blender view fine, Roblox joint collapsed | authoring-only volume preservation, corrective shape or helper driver | reproduce with supported bones and weights; compare the exact failed pose | S5, S6 | [A] | 408 |
| E08 | Seams flash or show holes | coincident overlapping surfaces; uncapped cuts; bad normals; too little socket coverage | repair caps or overlap; inspect backfaces; repeat extreme camera views | S3, S4 | [M] | 409 |
| E09 | FACS missing or misidentified | lost custom properties; neutral or mapping error; wrong export range | verify current reference mapping; repeat Avatar Setup and import | S5, S7 | [A] | 410 |
| E10 | VFX or hitbox stays at rest location | reading undeformed MeshPart placement instead of animated bone or socket | use the agreed transformed-bone or socket path; verify during playback | S5, S7 | [A] (timing list consumers: VFX, hitbox) | 411 |

### 5.4 Conflicting documentation (RP:413-419)

| id | lesson (paraphrased) | stage | tag | src | RP |
| --- | --- | --- | --- | --- | --- |
| X09 | Older Creature case: under 10,000 triangles per mesh; unweighted joints not imported. Current general spec allows 20,000 triangles; current importer can keep zero-influence bones. | S2 | VERIFIED (the conflict) | R1, R3, R6 | 415, 426 |
| X10 | Precedence: (1) current asset-specific spec and current importer behavior; (2) current general spec; (3) older worked example. Keep the older tutorial's craft advice, but do not silently adopt its superseded number. Do not add arbitrary Root weights to keep a root node (conflicts with the no-Root rule); use the import option and check the hierarchy. | S2, S5 | OPINION | R1, R3, R6 | 417, 426 |
| X11 | Preferring FBX and the importer supporting glTF do not conflict. Pick a tested route; the preference is not an exclusive format rule. | S5 | OPINION | R3, R4 | 419 |

### 5.5 Rule table (RP:421-427)

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| General export | FBX Unit Scale; no leaf bones | VERIFIED | R4 undated, checked 2026-10-20 |
| Avatar animation export simplification | 0.0 | VERIFIED | R5 undated, checked 2026-10-20 |
| Zero-influence retention | import option; off by default | VERIFIED | R3 undated, checked 2026-10-20 |
| Triangle conflict | 10,000 older example vs 20,000 current general ceiling | VERIFIED conflict; OPINION precedence | R6/R1, checked 2026-10-20 |
| Studio model byte ceiling | not established; do not use Tripo's limit | OPINION — unresolved | R3 review, 2026-10-20 |

---

## 6. Section 10: Rig tests and handoff gate (RP:429-493)

| id | lesson (paraphrased) | stage | flag | tag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| T01 | Version test assets separately from production animation. A rig passes only when Blender tests and Roblox import/playback tests both pass for the same source revision. A Blender pose the animator liked and an importer success message are two different facts. A checklist item that cannot be tested is UNKNOWN or BLOCKED, never PASS. | S5, S6 | [A] | OPINION | none | 431, 492 |
| T02 | Record per item: PASS, FAIL or BLOCKED; reviewer; source revision; test clip and frame; evidence file. Numeric thresholds come from the requirements sheet. A failure is not excused because a generator made it. | S4, S5, S6 | [A], [M] | OPINION | none | 452 |
| T03 | Riot's compression article names foot sliding from error accumulated down the hierarchy. Check contacts after bake and import. | S5, S7 | [A] | VERIFIED | S3 (2015-07-25) | 484, 490 |
| T04 | Measure both joint-space and visible-surface results. Protected torso: max vertex displacement during head isolation. Rigid pieces: pairwise distances against rest. Contacts: end-effector world position and orientation against the approved reference, allowing for deliberate root motion. Continuous seams: boundary positions and normals under motion. Overlap seams: visibility and penetration. Record units and tolerances. These are proposed metrics, not Roblox thresholds. | S4, S5 | [M] (seam results) | OPINION | none | 486 |

### 6.1 Test clips (RP:435-448, all 12)

Stage S5 (rigger runs); S6 (animator re-runs on the real rig through the manifest). [A] = the required motion and extremes come from the animator's S1 rows (my link to workflow.md; the paper does not name who supplies them).

| # | test clip | required motion | failure it reveals | flag | RP |
| --- | --- | --- | --- | --- | --- |
| 1 | Rest and reset | neutral pose; change controls; reset; repeat | hidden offsets, non-identity channels, stale driver state | [A] | 437 |
| 2 | Joint isolation | move one deform region while protected regions stay fixed | weight leakage, wrong parents, double transforms | | 438 |
| 3 | Upper-body envelope | head aim, torso bend, arm raise, cross-body reach, forearm twist | neck/chest skew, shoulder collapse, twist artifacts | [A] | 439 |
| 4 | Lower-body envelope | step, crouch, leg spread, knee fold, ankle roll within requirements | hip pinching, bad knee plane, foot dislocation | [A] | 440 |
| 5 | Contact hold | hold paw, foot or hand in the required contact while the body moves | IK drift, export errors, parent-space mistakes | [A] | 441 |
| 6 | Locomotion and turn | required gait plus start, stop, turn | sliding, timing mismatch, loop discontinuity | [A] | 442 |
| 7 | Switch test | IK/FK and space switches during a real action | popping, offsets, wrong keying | [A] | 443 |
| 8 | Face test | required expressions and interfering combinations | lid/lip collision, wrong mapping, leaked weights | [A] | 444 |
| 9 | Appendage test | opposed tail curves, wing fold/spread, ear motion | too few segments, fused surfaces, interpenetration | [A], [M] | 445 |
| 10 | Mechanism test | full reload, open, steer, suspension or rail cycle | wrong pivots, clearance failure, rubbery rigid parts | [A], [M] | 446 |
| 11 | Blend test | transitions between approved clips; additive and priority cases | conflicting channels, unexpected rest snapping | [A] | 447 |
| 12 | Runtime crowd and collision | intended simultaneous instances, cameras, device, proxy interactions | performance regression, visual/physical mismatch | [A] | 448 |

### 6.2 Pass/fail checklist (RP:450-482, all 22 items; IDs are mine)

Every item is recorded PASS / FAIL / BLOCKED with the T02 fields.

| id | group | check | stage | flag | src | RP |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Geometry | Rest silhouette and measured dimensions match the approved model. | S3, S4 | [M] | | 455 |
| G2 | Geometry | No unintended fused bridges, open cut surfaces, inverted normals or visible backfaces. | S3, S4 | [M] | | 456 |
| G3 | Geometry | Caps, overlap, UVs and materials stay valid through the required cameras and poses. | S3, S4 | [M] | | 457 |
| G4 | Geometry | Final triangulated counts meet the applicable general or avatar budget. | S4 | [M] | R1, R2 | 458 |
| SW1 | Skeleton and weights | Exact export node names, parent map, required roots and sockets match the schema. | S5 | | | 461 |
| SW2 | Skeleton and weights | Joint positions, bend planes, local axes and approved motion ranges pass isolation tests. | S5, S6 | [A] | | 462 |
| SW3 | Skeleton and weights | Weights finite and valid; no unintended unweighted deform vertices; at most 4 influences. | S5 | | R1 | 463 |
| SW4 | Skeleton and weights | No weights on the documented Root; rigid regions keep their shape. | S5 | | R1 | 464 |
| SW5 | Skeleton and weights | Head-only and limb-only motion does not move protected regions beyond the approved tolerance. | S5, S6 | [A] | | 465 |
| SW6 | Skeleton and weights | No unapproved collapse, candy-wrapper twist, spikes, texture stretch or seam exposure. | S5, S6 | [A], [M] | | 466 |
| CE1 | Controls and export | Reset, pose setting, IK/FK matching and space switching work from the automation interface. | S5, S6 | [A] | | 469 |
| CE2 | Controls and export | Evaluated export motion matches authoring intent at contacts and extreme poses. | S5, S7 | [A] | | 470 |
| CE3 | Controls and export | Required helpers survive and are driven; no authoring-only feature is silently required. | S5 | [A] | | 471 |
| CE4 | Controls and export | Export profile, units, axes, rest pose, clip names, FPS and frame ranges are recorded. | S5, S7 | [A] | | 472 |
| CE5 | Controls and export | Export read back into a fresh scene shows no missing weights or stray controls. | S5 | | | 473 |
| RB1 | Roblox | Current importer shows no unresolved relevant errors; expected hierarchy kept. | S5 | | | 476 |
| RB2 | Roblox | Scale, forward/up, rig type, controller and attachments match requirements. | S5 | | | 477 |
| RB3 | Roblox | Required test clips play on the intended Animator and rig in Studio. | S5 | [A] | | 478 |
| RB4 | Roblox | Collision proxies and weapon/VFX sockets follow the intended motion independently of skin shape. | S5, S7 | [A] | R7 | 479 |
| RB5 | Roblox | Required expressions and avatar validation pass when applicable. | S5 | [A] | | 480 |
| RB6 | Roblox | Measured crowd performance meets the target device budget. | S5 | | R13 | 481 |
| RB7 | Roblox | Animator and modeler approve actual in-engine motion and appearance. | S6 | [A], [M] | | 482 |

### 6.3 Rule table (RP:488-493)

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Validate contacts after bake/import | project-defined position/angle tolerance | VERIFIED failure mechanism; OPINION metric | S3, 2015-07-25 |
| Enforce influence and geometry limits | 4; applicable asset triangle budgets | VERIFIED | R1/R2 checked 2026-10-20 |
| Pass both DCC and engine tests | both stages required by studio policy | OPINION | proposed gate 2026-10-20 |
| Validate under target concurrency | project-specific, measured | OPINION | R13 checked 2026-10-20 |

---

## 7. Section 11: AI rigger method and Tripo repair (RP:495-556)

### 7.1 The 16-stage method (RP:497-518, all 16)

Applies to handmade models too. Skip generation-only steps only after writing down why. Never auto-approve an untested repair (RP:499, OPINION). Workflow-stage column is my mapping to `workflow.md`.

| step | action | check and stop condition | output | workflow stage | flag | RP |
| --- | --- | --- | --- | --- | --- | --- |
| M01 Intake | keep source, textures, generator/task/model IDs and source pose | files complete; source revision identifiable; no destructive source edit | source snapshot, inventory | S0 | | 503 |
| M02 Agree requirements | fill the joint/part/ROM sheet with modeler and animator | runtime role, key poses, detachments, contacts, unknowns all explicit | approved requirements or listed open items | S1, S2 | [A], [M] | 504 |
| M03 Inspect geometry | count components, triangles, surfaces, materials; look at fusions and interior detail | needed geometry exists; mark where texture stands in for structure | defect map, annotated views | S2 | [M] | 505 |
| M04 Select representation | rigid, skin or mix, per region | every moving region has a pivot or deformation plan | segmentation and skeleton proposal | S2 | [A], [M] | 506 |
| M05 Normalize working scene | calibrate size; set axes; clean transforms before bind | size check against a reference; no mirrored or non-uniform-scale skeleton | versioned working copy | S2, S3 | [M] | 507 |
| M06 Optional Tripo segmentation | pin model/route; run segment or SmartSegment only if it fits the plan | labels and boundaries right; no part missing; compare source shape and UVs | candidate parts, accepted/rejected list | S3 | [M] | 508 |
| M07 Repair geometry | cut, cap and socket rigid regions; retopologize continuous deformation zones | neutral silhouette kept; no false bridges or open boundaries; triangulated budget passes | rig-ready geometry | S3, S4 | [M] | 509 |
| M08 Place skeleton | fit joints from landmarks and required pose tests | neck, shoulder, hip centers and bend planes approved; hierarchy valid | skeleton, rest matrices | S5 | [A] (approves bend planes) | 510 |
| M09 Optional auto-rig candidate | run rig-check; pin the Tripo rig model or the chosen tool and version | output category fits; inspect joint positions, weights, names, roots; reject a poor candidate | candidate rig and audit | S5 | | 511 |
| M10 Bind and repair | rigid single-bone weights or localized skin weights; prune and normalize | no remote influence; all deform vertices covered; influence limit met | weight audit, repaired skin | S5 | | 512 |
| M11 Build controls | semantic controls, IK/FK, poles, switches; define the automation manifest | reset and intended poses work; no dependency cycles or double transforms | authoring rig, control contract | S5 | [A] | 513 |
| M12 Pose and stress | isolation, combined extremes, contacts, face and mechanism tests | all approved shape and contact criteria pass; structural defects go back to geometry or skeleton stage | test clips, defect log | S5 | [A], [M] | 514 |
| M13 Bake export copy | allowlisted skeleton; bake evaluated motion | needed roots and helpers kept; source and export contact results agree | rest model, separate clips, export manifest | S5, S7 | [A] | 515 |
| M14 Round trip | reimport into a clean Blender scene, then Studio, with saved profiles | topology, weights, hierarchy kept; size and axes right | import comparison, warnings | S5 | | 516 |
| M15 Runtime verification | set up Animator, sockets, proxies, optional avatar descriptions | play all clips; test collisions, device budget, crowd count, permissions | recorded Studio acceptance results | S5 | [A] | 517 |
| M16 Handoff | package source, controls, clips, manifests, requirements, tests, limits | modeler, animator and runtime owner sign off; failed items stay listed | approved release or blocked release | S5 to S6 | [A], [M] | 518 |

### 7.2 Tripo repair procedure for a typical merged character (RP:520-534)

All steps OPINION. Rule: find the failure first, then pick the fix; each cause needs a different fix. Compare `workflow.md` section 3 (routes R-cut, R-skin, R-mix, R-reject).

| id | case | procedure (paraphrased, in order) | decisive failure signs | stage | flag | RP |
| --- | --- | --- | --- | --- | --- | --- |
| R01 | Head rotation skews the body | (1) duplicate the scene; (2) turn off production animation; (3) hold torso controls fixed; (4) rotate only the head/neck export control through the approved range; (5) decide which cause: whole armature moves, torso bones inherit from head, mesh has duplicate armature deformation, or chest vertices carry head weight. | each cause needs its own fix | S5, S6 | [A] | 522 |
| R02 | Toy design with a stiff neck (rigid head) | (1) select the head boundary under an approved collar; (2) split and cap both pieces; (3) build an inset or overlap, or a ball socket; (4) place the joint at the true neck articulation center; (5) give the head rigid influence or an explicit runtime joint; (6) check the collar through yaw and tilt. Never move the pivot to head center to hide a bad boundary. | cap visible, z-fighting, silhouette change = failures | S2, S3, S5 | [M] (cap, socket, collar), [A] (neck range) | 524 |
| R03 | Design needs a continuous organic neck | (1) keep continuity; (2) remove fused hair or collar bridges that do not belong; (3) rebuild local neck/shoulder topology; (4) give a deliberate localized blend across the real neck; (5) protect chest vertices outside the transition; (6) add neck joints only with a motion role; (7) rerun head isolation, torso bend with head turn, material/UV check. | | S2, S3, S5 | [M] (topology), [A] (neck motion role) | 526 |
| R04 | Fused arms | (1) tell intersecting shells apart from truly welded triangles; (2) separate or rebuild per the representation decision; (3) place shoulders and elbows from intended reach and bend plane; (4) reset or transfer weights by region; (5) remove torso and other-arm leakage; (6) test overhead raise, cross-body reach, twist. If weights are legal but the armpit collapses, return to topology or articulation; do not smooth the whole body. | | S2, S3, S5 | [M], [A] | 528 |
| R05 | Fused legs and hips | (1) check the pelvis stays an independent mass; (2) hip sockets inside the approved motion structure; (3) each thigh has its own influence support; (4) test deepest required crouch, high step and spread. A good idle animation says nothing about hips. | | S2, S5 | [A] (deepest poses), [M] | 530 |
| R06 | Generated clothing or armor | Decide per piece: bends with flesh, rides rigidly on a limb, or is a separate animated piece. A wide shoulder pad must not get a smooth chest/arm blend by accident. A skirt fused across the legs needs a redesign or a topology/rig solution; splitting leg weights cannot create missing fabric. | | S1, S2, S3 | [A], [M] | 532 |
| R07 | After any manual repair | Repeat the full gate from bake onward. Repairs can bring stale bind matrices, lost zero-influence sockets, changed UVs, renamed bones or scale drift. Save the generator output and the repaired result as separate files. | | S5 | [A] (renamed bones break clips), [M] | 534 |

### 7.3 AI failure patterns (RP:538-549, all 10)

| id | likely AI-made error | early detector | corrective action | stage | flag | RP |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | Joints placed by bounding boxes alone | rotation test, landmark overlay | refit articulation centers and rest axes before binding | S2, S5 | | 540 |
| P02 | Head or limb skews whole body | protected-region displacement plus hierarchy check | fix wrong parent or control, or remove leaked influences | S5 | | 541 |
| P03 | False geometry bridges | wireframe and connectivity check | remove the bridge, rebuild the intended surfaces | S2, S3 | [M] | 542 |
| P04 | Visible cut seams | extreme-pose silhouette and backface check | rebuild caps, socket or overlap, or switch to skinning | S3, S4 | [M] | 543 |
| P05 | Candy-wrapper twist | twist combined with bend | redistribute articulation, weights and topology; verify the target deformation | S2, S5 | [A], [M] | 544 |
| P06 | Mechanism rotates off-axis | pivot or rail motion preview | restore true axis and joint frames; do not repaint a rigid hinge | S5 | [A] | 545 |
| P07 | Wrong scale after export | dimensioned reference, skeleton transform audit | fix the unit-conversion profile; repeat binding and export tests | S5 | | 546 |
| P08 | Good source pose, bad imported pose | evaluated matrix and contact comparison | fix baking, rest transforms, names, kept nodes and action selection | S5, S7 | [A] | 547 |
| P09 | Repeated armatures or modifiers after retries | inventory diff after each MCP change | make the stage idempotent; delete only its own old generated output | S5 | | 548 |
| P10 | Invented successful validation | missing evidence paths or Studio test record | mark BLOCKED; run or request the missing test | all | [A], [M] | 549 |

### 7.4 Rule table (RP:551-556)

| rule | number | tag | src and date |
| --- | --- | --- | --- |
| Pin rig model and use rig-check | v3.0-20260909 for the documented humanoid upgrade | VERIFIED capability; OPINION stage use | T1/T3 checked 2026-10-20 |
| Validate every change stage | no fixed time-saving claim | OPINION | proposed operating procedure 2026-10-20 |
| Repair body skew by diagnosis | no universal repainting recipe | OPINION | B1/B2/R6 synthesis 2026-10-20 |
| Hand off real engine evidence | BLOCKED if not run | OPINION | proposed release policy 2026-10-20 |

---

## 8. Do not do (RP:558-579, all 20)

| id | rule (paraphrased) | tag | src | RP |
| --- | --- | --- | --- | --- |
| D01 | Do not give a vertex more than 4 bone/joint influences, and do not weight anything to the documented Root. | VERIFIED | R1 | 560 |
| D02 | Do not treat the 20,000-triangle general mesh ceiling as the Marketplace body budget or as a mobile target. | OPINION | R1, R2 | 561 |
| D03 | Do not carry the 10,000-triangle limit of the old tutorial over the current general documentation. | OPINION | R1, R6 | 562 |
| D04 | Do not invent a universal Roblox bone cap, joint angle, edge-loop count or Studio file-size ceiling. | OPINION | none | 563 |
| D05 | Do not smooth weights globally to cover wrong joints, wrong parents or fused topology. | OPINION | D1, R6 | 564 |
| D06 | Do not assume Separate by Loose Parts can detach regions that are in fact connected. | OPINION | B8 | 565 |
| D07 | Do not leave open cuts, thin backfaces, coincident seam surfaces or silhouette-changing caps untested. | OPINION | R1, R2 | 566 |
| D08 | Do not treat a semantic segment as a finished mechanical part or a finished anatomical deformation zone. | OPINION | T2, T4 | 567 |
| D09 | Do not leave out the Tripo model field and then claim the latest humanoid rigging model was used. | VERIFIED | T1, T5 | 568 |
| D10 | Do not use a May 2026 practitioner test as proof of October model quality or of a current non-human limit. | OPINION | E1, T1 | 569 |
| D11 | Do not use Mixamo as the default auto-rigger for disconnected toy parts or non-human appendages. | OPINION | A1 | 570 |
| D12 | Do not assume Blender IK, drivers, spline controls, shape corrections or DQS behavior become Roblox features. | OPINION | B4, B5 | 571 |
| D13 | Do not delete required non-deforming roots or sockets because an export filter says Deform Only. | OPINION | R3, B4 | 572 |
| D14 | Do not add forbidden Root weights only to keep a root; use current import settings and check the hierarchy. | OPINION | R1, R3 | 573 |
| D15 | Do not zero valid rest-bone orientations to zero pose or object channels. | OPINION | B6 | 574 |
| D16 | Do not stack arbitrary scale factors, and do not apply the skin modifier destructively on the only source rig. | OPINION | R4, R5 | 575 |
| D17 | Do not expect bone skin deformation to update physical collision geometry. | VERIFIED | R7 | 576 |
| D18 | Do not drive one transform through physics, an Animator and a procedural writer without explicit ownership. | OPINION | R8 | 577 |
| D19 | Do not change skeleton names or the rest pose after animation production starts without a migration and regression test. | OPINION | none | 578 |
| D20 | Do not claim Blender or Studio tests were done when the only evidence is a research paper or a generator preview. | OPINION | none | 579 |

---

## 9. Open questions and required local research (RP:581-595)

| id | question | tag | what closes it (paper) | paper's warning | RP |
| --- | --- | --- | --- | --- | --- |
| Q01 | Maximum bones or Motor6Ds for a custom rig, and the importer's model-file byte ceiling: not established in the inspected current general docs. | OPINION-unresolved | An applicable current official statement, or a recorded importer boundary test that names Studio build, format, mesh layout and import options. | Do not invent either number (also D04). | 583 |
| Q02 | Exact 2026 Roblox skinning internals; support for arbitrary body corrective morph import. | OPINION-unresolved | Keep a target deformation test asset; reproduce problem poses in Studio. | Historical linear-skinning page and ordinary game-engine advice are cautions, not a fresh spec. | 585 |
| Q03 | Independent quality of current Tripo humanoid rigging v3.0-20260909 and of v2 semantic segmentation. | OPINION-unresolved | A reproducible dataset-based test (none exists in the paper). | The one practitioner comparison is older and non-Roblox. Do not make up success rates or repair times. | 587 |
| Q04 | Build a local evaluation set: humanoids of different proportions, a plush quadruped, a winged creature, a tail-heavy creature, an armored body, a weapon, a mechanism; clean handmade and generated sources. Record input identity, tool versions, outputs, failed poses, edit history, studio-measured repair time, import and runtime outcomes. | OPINION | Sample size from real production risk. | Do not state statistical confidence the data cannot support. | 589 |
| Q05 | Exact mobile bone, triangle and material budgets for the studio's intended pet/NPC concurrency. | OPINION-unresolved | Measure on representative target hardware with real animations, lighting, materials, collisions, cameras; compare CPU animation cost and rendered/physics cost. | No universal safe number. | 591 |
| Q06 | Exact installed Blender / MCP / exporter compatibility: the paper checked published documents only. Latest stable found: 5.2 LTS; patch beyond indexed 5.2.2 not confirmed. Several full Blender pages were blocked; indexed official text was used. | OPINION-unresolved | Query the installed API; run round-trip tests before using operator calls. | Doc baseline is not a tested toolchain. | 593 |
| Q07 | Deadlock-specific current rig budgets, and proprietary rigs at other named leaders: no detailed accessible primary evidence. Pixar full PDFs redirected; only limited indexed claims used. | OPINION-unresolved | Not stated. | Do not infer bone counts or hidden pipelines from visual quality. This is a source-access limit, not proof the resources do not exist. | 595 |

---

## 10. Index for the lead

### 10.1 Merged Tripo mesh: lessons that matter most

| need | read |
| --- | --- |
| Is one object one surface? Cuts impossible if parts are connected | D06, P03, R04, M03 |
| Choose rigid cut vs skin vs mix per region | W04, W14, R02, R03, M04, N09 |
| Cut quality: caps, sockets, seams | R02, E08, P04, D07, G2, G3 |
| Tripo tools as candidates | M06, M09, D08, D09, D10, Q03, X09 (version facts in CL) |
| Weight repair on a skinned merged mesh | W05, W08, W09, W10, R01, R04, R05 |
| Re-gate after repair | R07, M13-M15, X02 |
| Fake validation | P10, D20, T01 |

### 10.2 What the animator must also know (all [A] rows, grouped)

| topic | IDs |
| --- | --- |
| ROM, twist, stress poses feed weights and tests | W14, W17, W23, T03, 6.1 clips 3-9 |
| Bend plane and contact orientation of non-humans | N01, N02, N03, N04, N06, N07, N08 |
| Face method and frame layout | F01, F02, F03, F05, F06, E09 |
| Controls, manifest, switches | K01, K03-K07, K10, CE1, CE2 |
| Export profile and clip naming | X01, X02, X04, E05, E10, P08, M13 |
| Helpers must be keyed or baked; physics vs Animator ownership | W21, N10, D18, D19 |
| Never accept "tests pass" without evidence | T01, P10, D20 |

### 10.3 What the modeler must also know (all [M] rows, grouped)

| topic | IDs |
| --- | --- |
| Geometry in bend zones (armpit crease, hinge compression side, tail length) | W14, W15, W17, N04, R03 |
| Rigid pieces, separate parts where motion needs them | W04, N08, N09, X07, E06, R06 |
| Caps, sockets, seams, backfaces | R02, E08, P04, D07, G1-G4 |
| Clean transforms, real scale | X05, M05 |
| Face geometry and UV | F01, F02, F04 |
| Segmentation output is not a finished part | D08, M06 |
| Sign-off on in-engine look | RB7, M16 |

### 10.4 Stage index

| stage | IDs |
| --- | --- |
| S1 motion needs | N01-N03, N06, N08, W14, W17, W23, F01, K03 |
| S2 rig plan | W04, W08, W12, N01-N10, F01, F02, F06, X05, X08-X10, M02-M05, P01, P03, R02-R06 |
| S3 geometry | W14, W15, N04, N06, N08, N09, F04, M05-M07, R02-R06, E08, P03, P04 |
| S4 geometry acceptance | W24, T04, G1-G4, E08, P04, M07 |
| S5 rig + tests | W01-W13, W16, W18-W24, K01-K11, X01-X08, T01-T04, 6.1, SW1-SW6, CE1-CE5, RB1-RB6, M08-M15, R01, R07, P01-P09 |
| S6 rig acceptance | W09, W11, K03-K05, T01, T02, SW2, SW5, SW6, CE1, RB7, M16, R01, F05 |
| S7 animate and export | K06, K10, X01, X02, X07, E05, E09, E10, W13, W21, CE2, CE4, M13 |
| S8 final | none in this range (owner gate) |

---

## 11. Claims to check (CL)

One row per number or per Roblox, Blender, Tripo, other-tool or industry fact in RP:265-596. "Src line" gives where the source is described in the paper (RP:597-849). Verdict column left empty for step 2.

| id | claim | RP | src | kind | src line |
| --- | --- | --- | --- | --- | --- |
| CL01 | A vertex cannot be influenced by more than 4 bones or joints. | 269, 289, 463, 491, 560 | R1 | roblox | 711-714 |
| CL02 | No weights on the documented Root. | 464, 560, 573 | R1 | roblox | 711-715 |
| CL03 | Current general specification allows 20,000 triangles per mesh. | 415, 426, 561 | R1 | roblox | 711-715 |
| CL04 | Older Creature case says fewer than 10,000 triangles per mesh. | 415, 426, 562 | R6 | roblox | 736-739 |
| CL05 | Older Creature case says unweighted joints are not imported. | 415 | R6 | roblox | 736-739 |
| CL06 | Importer can keep bones that do not influence the mesh; option "Keep Zero Influence Bones" is off by default. | 392, 415, 425 | R3 | roblox | 721-724 |
| CL07 | Importer Rig Type options are R15, Custom, No Rig. | 392 | R3 | roblox | 721-724 |
| CL08 | Studio import route is File > Import; FBX and glTF carry rig, skin, animation; OBJ does not suit rig data. | 392, 419 | R3 | roblox | 721-724 |
| CL09 | glTF/GLB import can give a different hierarchy from FBX, including extra model nodes. | 392 | R3 | roblox | 721-724 |
| CL10 | Importer exposes World Forward, World Up, Scale Unit and pivot settings. | 384 | R3 | roblox | 721-724 |
| CL11 | Avatar body spec: characters face +Z and stand on +Y (paper phrase "stand in positive Y"). | 384 | R2 | roblox | 716-719 |
| CL12 | Avatar body spec accepts I, A and T poses. | 384 | R2 | roblox | 716-719 |
| CL13 | Avatar body spec fixes template origins and hierarchy. | 384 | R2 | roblox | 716-719 |
| CL14 | Advanced R15 supports up to 37 additional optional bones/joints (source-list line only). | 718 | R2 | roblox | 716-719 |
| CL15 | Avatar bodies have their own triangle budgets, distinct from the 20,000 general ceiling (no numbers in paper). | 458, 561 | R2 | roblox | 716-719 |
| CL16 | General FBX export: Transform > Apply Scalings = FBX Unit Scale. | 380, 423 | R4 | roblox | 726-729 |
| CL17 | General FBX export: Add Leaf Bones disabled. | 380, 423 | R4 | roblox | 726-729 |
| CL18 | General FBX export: no Bake Animation unless animation data is intended. | 380 | R4 | roblox | 726-729 |
| CL19 | Avatar-body export: Custom Properties enabled. | 380 | R5 | roblox | 731-734 |
| CL20 | Avatar-body animation export: NLA Strips, All Actions, Force Start/End Keyframes disabled. | 380 | R5 | roblox | 731-734 |
| CL21 | Avatar-body animation export: Simplify = 0.0. | 380, 424 | R5 | roblox | 731-734 |
| CL22 | Bone skin deformation does not change physical collision geometry. | 310, 315, 576 | R7 | roblox | 741-744 |
| CL23 | Motor6D Transform may be overwritten by the Animator, so procedural writers need ownership. | 310, 577 | R8 | roblox | 746-749 |
| CL24 | Historical Roblox skinning doc: linear skeletal skinning, each vertex weighted to up to 4 joints. | 279 | R10 | roblox | 756-759 |
| CL25 | Paper claims no current Roblox DQS toggle is documented (negative claim). | 281 | R10, none | roblox | 281 |
| CL26 | Dynamic heads use skinned facial joints, FACS poses, frame-to-pose mapping, FaceControls. | 325 | R11 | roblox | 761-764 |
| CL27 | Dynamic head: 50 base poses. | 325, 335 | R11 | roblox | 761-764 |
| CL28 | Dynamic head: 17 required poses for Marketplace sale. | 325, 336 | R11 | roblox | 761-764 |
| CL29 | Dynamic head: neutral expression at frame 0; each non-neutral pose on a distinct later frame. | 325, 337 | R11 | roblox | 761-764 |
| CL30 | Dynamic head docs describe combination-pose corrections for overlapping facial actions. | 283, 325 | R11 | roblox | 761-764 |
| CL31 | Arbitrary body shape-key/morph import to Roblox is not established (negative claim). | 283, 331, 585 | none | roblox | 585 |
| CL32 | HumanoidRigDescription has 22 joint slots; not a universal exported-bone cap. | 769 | R12 | roblox | 766-769 |
| CL33 | Current Roblox docs state no maximum bones/Motor6Ds for custom rigs and no importer byte ceiling (negative claim). | 427, 563, 583 | R1, R3 | roblox | 583 |
| CL34 | Roblox Creature case: groups dense central tentacles, keeps tips separate, economical joints, neutral initial shape. | 302, 314 | R6 | roblox | 736-739 |
| CL35 | Avatar Setup/validation and advanced rig-description objects exist for R15-compatible assets. | 396 | R2, R12 | roblox | 716-719, 766-769 |
| CL36 | For static NPCs, Roblox suggests a simple AnimationController; no universal pet budget. | 298, 317, 493 | R13 | roblox | 771-774 |
| CL37 | A VFX or hitbox reading MeshPart placement sees rest location, not the animated bone position. | 411 | none | roblox | 411 |
| CL38 | Animation use and publish permissions affect playback of imported animations. | 394 | none | roblox | 394 |
| CL39 | Armature modifier Preserve Volume uses quaternions. | 267, 281 | B1 | blender | 652-655 |
| CL40 | Blender provides Normalize All, Clean, Limit Total and weight transfer tools. | 267, 289 | B2 | blender | 658-662 |
| CL41 | Interactive normalization can leave locked/protected groups unchanged. | 271 | none | blender | 271 |
| CL42 | Separate by Loose Parts only splits disconnected geometry. | 566 | B8 | blender | 692-696 |
| CL43 | Legacy FBX: constraints themselves are not saved in the FBX; bake evaluated motion. | 352, 371 | B5 | blender | 676-680 |
| CL44 | PoseBone API separates evaluated pose matrix, transform channels (matrix_basis) and bone-relative matrix access. | 352, 574 | B6 | blender | 682-685 |
| CL45 | Blender 5.2 has Actions with slots; older F-curve traversal can fail. | 365 | B6, B7 | blender | 682-690 |
| CL46 | Armature structure edits need Edit Mode, pose edits Pose Mode, per versioned API; edit_bones, rest bones, pose bones are separate views. | 363 | B6 | blender | 363 |
| CL47 | Dependency graph must be updated before reading final geometry or contact matrices. | 363 | none | blender | 363 |
| CL48 | Rigify makes controls from a metarig and has IK/FK features. | 344 | B3 | blender | 664-669 |
| CL49 | Blender 5.2 LTS: release 2026-07-14, 5.2.2 on 2026-09-15; patches beyond not confirmed. | 372, 593 | B0 | blender | 647-650 |
| CL50 | Blender 5.2 manual and API are the paper's documentation baseline (installed version unverified). | 372, 593 | B0-B7 | blender | 593 |
| CL51 | Blender exporter option names and defaults match R4/R5 wording in the installed version (Apply Scalings, Add Leaf Bones, Bake Animation, Custom Properties, NLA Strips, All Actions, Force Start/End Keyframes, Simplify). | 380 | R4, R5 | blender | 726-734 |
| CL52 | Applying the Armature modifier destroys the skin binding on that object. | 382, 575 | none | blender | 382 |
| CL53 | Blender IK, drivers, spline constraints, corrective shapes and DQS do not become executable Roblox features. | 300, 571 | B4, B5 | blender | 671-680 |
| CL54 | Blender Preserve Volume preview can differ from ordinary game-engine skinning. | 279 | B4 | other-tool | 671-674 |
| CL55 | Auto-Rig Pro exports Humanoid and Universal skeletons; has custom-bone export rules; Roblox-specific settings not implied. | 344, 572 | B4 | other-tool | 671-674 |
| CL56 | Auto-Rig Pro doc notes a bind-pose issue fixed in 3.78.49. | 671 | B4 | other-tool | 671 |
| CL57 | Exporting only Deform bones can drop a required non-deforming root (add-on and exporter behavior). | 342, 572 | B4, R3 | other-tool | 342 |
| CL58 | Tripo Auto Rigging default model is unchanged; humanoid v3.0-20260909 must be requested explicitly. | 553, 568, 587 | T1, T5 | tripo | 778-781, 798-801 |
| CL59 | Tripo rig-check returns whether a model can be rigged and the recommended rig type; it is not a Studio quality validator. | 511, 553 | T3 | tripo | 788-791 |
| CL60 | Tripo segmentation: geometry and semantic versions; v2.0-20260430 Beta adds semantic labels. | 508, 587 | T2 | tripo | 783-786 |
| CL61 | Tripo SmartSegment includes auto modeling; GLB input; explicit transform. | 508, 567 | T4 | tripo | 793-796 |
| CL62 | Tripo file ceiling is 150 MB (must not be used as the Studio limit). | 427 | T1 | tripo | 781 |
| CL63 | Tripo rigging supports non-biped topology categories and naming presets. | 570, 843 | T1 | tripo | 781, 843 |
| CL64 | Tripo changelog entries 2026-10 and 2026-09; the quoted "default still v2.0" sentence concerns retopology, not rigging. | 568, 801 | T5 | tripo | 798-801 |
| CL65 | Tripo retopology v3.0 quad mesh: face counts and byte limits are not interchangeable with other operations. | 806 | T6 | tripo | 803-806 |
| CL66 | Mixamo auto-rigger and libraries are for bipedal humanoids only (FAQ updated 2021-09-14). | 570 | A1 | other-tool | 810-813 |
| CL67 | No newer 2026 official Mixamo auto-rigger release found. | 812-813 | A1 | other-tool | 813 |
| CL68 | E1 (2026-05-14) found over-smoothed shoulder/chest weights in older auto-riggers; claims biped-only for Tripo, superseded by Tripo topology docs. | 569, 840-843 | E1 | other-tool | 840-843 |
| CL69 | Riot article (2015-07-25): error accumulates as animation affects segments farther from the root; paper reads this as foot sliding. | 484, 490 | S3 | industry | 613-616 |
| CL70 | Disney D1 (SIGGRAPH 2013): enhanced DQS is not a simple drop-in replacement for linear blend skinning. | 279 | D1 | industry | 623-626 |
| CL71 | Disney D2 (SIGGRAPH 2016, dated 2016-07-11 or 2016-07-24): collapsing elbows, candy wrapper twists, bulging near joints are known skinning failures. | 279, 292 | D2 | industry | 628-632 |
| CL72 | Dota 2 workshop (V1) limit of 52 bones and root skinning: cited only to say it must not transfer to Roblox. | 621 | V1 | industry | 618-621 |
| CL73 | Pixar P1 (2020-08-17) and P2 (SIGGRAPH 2024): limited excerpts only; not used in lines 265-596. | 634-643 | P1, P2 | industry | 634-643 |

Number index (every numeric value in range, for quick check): 4 influences (CL01); weight 1 (paper definition, no source); 20,000 (CL03); 10,000 (CL04); 50 (CL27); 17 (CL28); frame 0 (CL29); 0.0 (CL21); 37 (CL14); 22 (CL32); 150 MB (CL62); 52 (CL72); Blender 5.2, 5.2.2, 2026-07-14, 2026-09-15 (CL49); Auto-Rig Pro 3.78.49 (CL56); Tripo v3.0-20260909 (CL58); v2.0-20260430 (CL60); 12 test clips and 22 checklist items and 16 stages and 20 do-not items (paper structure, count verified here, not a fact-check item).

---

## 12. Contradictions and limits (LM)

| id | topic | paper says | other doc or limit | status | handling in skills | RP |
| --- | --- | --- | --- | --- | --- | --- |
| LM01 | Triangle ceiling | Current 20,000 vs old tutorial 10,000; current wins. | Old Creature case (R6) vs R1. `workflow.md` section 6 uses 20,000 (`specifications.md:34`). | VERIFIED conflict; OPINION precedence | Use 20,000 as platform ceiling only, never as phone target (D02). Do not cite 10,000. | 415, 426 |
| LM02 | Unweighted joints | Old case: not imported. Current importer: option to keep, off by default. | R6 vs R3 | VERIFIED conflict | Use the import option on purpose (X07). | 415 |
| LM03 | Root handling | Do not add Root weights to keep root nodes; use the import option. | Valve Dota (V1) tells you to skin a root; paper says never transfer across platforms. | OPINION; platform difference | Roblox rule wins. | 417, 573, 621 |
| LM04 | Mixamo scope | Humanoid only. | E1 says Tripo is biped-only; paper says current Tripo topology docs supersede it. | A1 VERIFIED; E1 superseded | Do not use E1 for Tripo limits (D10). | 570, 843 |
| LM05 | Tripo model default | D09 (VERIFIED) cites T1 and T5. | T5's quoted default sentence is about retopology, not rigging (RP:801). Paper line 553 gives the model string v3.0-20260909; the T1 key line only says v3.0 must be requested. `workflow.md` section 3 says API default is older. | Source mismatch inside the paper | Fact-check the exact model string and default (CL58, CL64). | 553, 568, 781, 801 |
| LM06 | Formats | FBX preferred; glTF supported. | R3 vs R4 | Not a conflict (OPINION) | Pick a tested route (X11). | 419 |
| LM07 | Forward axis | Avatar +Z; custom assembly may differ; no proven universal axis pair. | R2 vs runtime | OPINION | Test with a labeled reference (X04). | 384, 386 |
| LM08 | Baking | General export: no Bake Animation unless intended. Paper advice: bake the evaluated export skeleton for clips. Avatar animation export: Simplify 0.0 and several options off. | R4 vs R5 vs paper | Compatible if rest and clip exports are separate (X02) | Two export profiles: rest model, clip. | 380, 382 |
| LM09 | Apply modifiers | General guidance says apply modifiers; paper says do not destroy skin binding. | R4/R5 vs paper | OPINION | Apply on an export copy only. | 382, 575 |
| LM10 | Volume preservation | Blender Preserve Volume preview vs Roblox skinning. | B1, B4 vs R10 (historical) | Roblox result authoritative | Preview with Preserve Volume off (W20). | 279, 281 |
| LM11 | Disney D2 date | 2016-07-11 (page) vs 2016-07-24 (other listing); not resolved by the paper. | | Open | Cite both or "2016". | 628 |
| LM12 | Blender baseline | Docs are 5.2 LTS; B3 Rigify full page blocked, indexed 5.4 dev docs not used as 5.2 facts. | B0, B3 | Limit | Query installed version (Q06). | 593, 664 |
| LM13 | B5 scope | Constraint-definitions rule is from the Legacy FBX page. | Does the same hold for the non-legacy FBX exporter? Paper does not say. | Limit | Check which exporter is installed (CL43). | 371, 676 |
| LM14 | Source access | B1, B2, B3, B5, B6, B8, B9, B0 read through official indexed excerpts, not full pages; Motor6D page partly interactive. | | Limit | Fact-check against full pages. | 599, 652, 658, 664, 676, 682, 692, 746 |
| LM15 | B7 support | K10 cites B7 for action/slot handling, but B7's key line is about Auto IK behavior. | | Source mismatch | Fact-check CL45 elsewhere. | 365, 687-689 |
| LM16 | R6 age | Verified-tagged lesson relies on a legacy, undated case study. | | Limit | Treat craft advice as sound, numbers as superseded. | 302, 736 |
| LM17 | R10 age | Historical beta page, not a 2026 guarantee. | | Limit | Test in Studio (Q02). | 279, 756 |
| LM18 | R11 currency | 17 required poses is "in the cited workflow"; recheck current head requirements at upload time. | | Limit | Recheck at production. | 336, 764 |
| LM19 | R12 meaning | 22 description slots are not an exported-bone cap. | | Limit | Do not use 22 as a cap (D04). | 769 |
| LM20 | Tag vs source | D02, D03 are tagged OPINION although they rest on VERIFIED figures; T03 marks Riot VERIFIED but foot sliding is the paper's reading of the article. | | Tag inconsistency | Keep the paper's tag; fact-check. | 484, 561-562 |
| LM21 | Nothing was executed | Paper never ran Blender, MCP or Studio. All checklists, thresholds, procedures and wrapper names are proposals. | | Limit | Every skill rule built from OPINION rows needs a first real test. | 847 |
| LM22 | No thresholds | Tolerances, angles, budgets, repair times, success rates not supplied. | | Limit | Take numbers from the rig sheet or measure (Q05). | 452, 486, 847 |
| LM23 | E1 weight | EXPERIENCE only: first-party, commercial interest, not a controlled benchmark; older models. | | Limit | Use as test-design hint only. | 569, 840 |
| LM24 | Open questions | Q01-Q07 above stay unresolved; none may become a skill rule without a source or a recorded local test. | | Open | Mark UNKNOWN in the rig sheet. | 581-595 |

---

## 13. Source legend (IDs cited in RP:265-596, resolved from RP:597-849)

All pages were checked on 2026-10-20 by the paper's author. "Undated" = no reliable publication or update date was shown. Full URLs are in the paper at the listed line; they are not copied here (paper stays outside git). Official indexed excerpts are not full-page reads.

| id | what | date | access limit | used for | RP |
| --- | --- | --- | --- | --- | --- |
| R1 | Roblox Creator Hub, General Specifications (art/modeling/specifications) | undated | full | 4-influence limit, triangle ceiling, watertight, Root weights | 711-715 |
| R2 | Roblox Creator Hub, Character Body Specifications | undated | full | avatar budgets, up to 37 additional optional joints, poses, hierarchy | 716-719 |
| R3 | Roblox Creator Hub, Importer | undated | full | rig types, axis/scale/pivot, zero-influence option, FBX vs glTF | 721-724 |
| R4 | Roblox Creator Hub, Export Settings for general models | undated | full | FBX profile, leaf bones, animation inclusion | 726-729 |
| R5 | Roblox Creator Hub, Export Character Bodies | undated | full | avatar export properties, Simplify 0.0 | 731-734 |
| R6 | Roblox Creator Hub, Beyond the Dark Custom Characters (legacy case study) | undated; original date not found | full | neutral pose, appendage grouping; old 10,000 triangles and zero-influence statements | 736-739 |
| R7 | Roblox Creator Hub, Rigging and Skinning | undated | full | visual vs physical shape | 741-744 |
| R8 | Roblox Creator Hub, Motor6D (API) | undated | summary from indexed content; page partly interactive | rigid joints; Transform may be overwritten by Animator | 746-749 |
| R10 | Roblox, Avatar Evolution Skinning (historical beta) | undated | full | linear skeletal skinning, up to 4 joints | 756-759 |
| R11 | Roblox Creator Hub, Create Basic Dynamic Heads | undated | full | FACS, 50 base poses, Marketplace subset, frame 0 | 761-764 |
| R12 | Roblox Creator Hub, HumanoidRigDescription (API) | undated | indexed content | 22 description slots | 766-769 |
| R13 | Roblox Creator Hub, Improve Performance | undated | indexed text | simple AnimationController for static NPCs; measure | 771-774 |
| B0 | Blender 5.2 LTS release page | base 2026-07-14; 5.2.2 on 2026-09-15 | full page blocked; indexed results | version baseline | 647-650 |
| B1 | Blender 5.2 manual, Armature Modifier | undated | indexed excerpts | Preserve Volume | 652-655 |
| B2 | Blender 5.2 manual, Editing Weight Paint | undated | indexed excerpts | Normalize All, Clean, Limit Total, transfer | 658-662 |
| B3 | Blender 5.2 manual, Rigify | undated | indexed; full page blocked; 5.4 dev docs not used | metarig, generated controls, IK/FK | 664-669 |
| B4 | Auto-Rig Pro, Game Engine Export (Artell/Lucky3D) | undated; mentions fix in 3.78.49 | full | Humanoid/Universal export, custom bones, Preserve Volume warning | 671-674 |
| B5 | Blender 5.2 manual, FBX Legacy | undated | repository and indexed text; stable page blocked | constraints not saved in FBX | 676-680 |
| B6 | Blender 5.2 API, PoseBone | undated | indexed results | matrix vs matrix_basis | 682-685 |
| B7 | Blender 5.2 Animation and Rigging release notes | 2026, no day | indexed text | version-specific rig behavior (key line is Auto IK) | 687-690 |
| B8 | Blender 5.2 manual, Separate | undated | indexed excerpts | Separate by Loose Parts | 692-696 |
| T1 | Tripo Developers, Auto Rigging | undated; model versions carry own dates | live reference | v3.0 must be requested; topology categories; formats; 150 MB ceiling | 778-781 |
| T2 | Tripo Developers, Segmentation | undated | live reference | v2.0-20260430 Beta semantic segmentation | 783-786 |
| T3 | Tripo Developers, Rig Check | undated | live reference | compatibility screen, recommended rig type | 788-791 |
| T4 | Tripo Developers, Smart Segmentation | undated | live reference | includes auto modeling; GLB input | 793-796 |
| T5 | Tripo Developers, Changelog | entries 2026-10 and 2026-09 | live reference | October rigging upgrade; default sentence is about retopology | 798-801 |
| T6 | Tripo Developers, Retopology | undated | live reference | v3.0 quad mesh settings | 803-806 |
| A1 | Adobe, Mixamo Common Questions | updated 2021-09-14 | full | bipedal humanoids only | 810-813 |
| E1 | StraySpark, AI Auto-Rigging Showdown 2026 | 2026-05-14 | full | EXPERIENCE: older failure reports; first-party, sells mesh tooling | 840-843 |
| S3 | Riot Games, Compressing Skeletal Animation Data | 2015-07-25 | full | accumulated error down the hierarchy | 613-616 |
| D1 | Lee et al., Disney Animation, Enhanced Dual Quaternion Skinning for Production Use | SIGGRAPH 2013, day not found | abstract | DQS limits | 623-626 |
| D2 | Le and Hodgins, Disney Research, Optimized Centers of Rotation | 2016-07-11 (other listing 2016-07-24) | abstract | collapsing elbows, candy-wrapper twist | 628-632 |
| V1 | Valve, Dota 2 Workshop NPC requirements (legacy) | undated | full | cited only in section 12 (LM03): limit of 52 bones, root skinning | 618-621 |
