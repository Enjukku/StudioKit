> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-design`. Sources: rigging paper RP:275-285, 400-411, 520-549 (notes `knowledge/reference/rigging/02-*.md` §1.2, §5.3, §7.2-7.3); first-game FG01-FG07. All [O] unless marked.

# Diagnosing a broken rig

## 1. Debug order (RP:275): fix the earliest broken layer first
1. Rest / bind transforms and hierarchy (parents).
2. Joint positions and axes.
3. Unintended geometry bridges.
4. Weight support and normalization.
5. Edge flow and density.
6. Helper-joint distribution.
7. Corrective shapes (and only if they survive Roblox).

A joint inside the skull instead of the neck base cannot be fixed by repainting. If the whole character moves with the head, check parents and animation channels before touching neck weights (RP:275).

## 2. Symptom → cause → decisive check
| Symptom | Inspect | Correction and decisive check | Source |
| --- | --- | --- | --- |
| Head turns and the body skews | whole armature moving? torso inheriting from head? duplicate armature deformation? chest vertices with head weights? | isolate the head bone, measure protected chest vertices (`rig_audit.py --protect`), read weights and evaluated matrices; each cause has a different fix | RP:403, 522 |
| Arms web to the torso on raise | fused bridge (real welded triangles) vs intersecting shells | remove the bridge and rebuild, or cut (R-cut); weights cannot fix it | RP:186, 528; [E] FG01 |
| Arm or elbow wrinkles, pinches, candy-wrapper | hinge centre, compression-side geometry, twist on one joint | refit the hinge, rebuild the zone, spread twist over a justified chain; or R-cut | RP:277, 544; [E] FG04 |
| Shoulder collapses | arm vs clavicle / torso share of the move; armpit crease; rigid pad inheriting a smooth blend | distribute the move; keep the crease; isolate rigid pads; if weights are legal but it still collapses, go back to topology | RP:277, 528 |
| Hip collapses | pelvis support, thigh support, opposing-thigh leakage | deepest crouch, high step, spread pose; an idle proves nothing about hips | RP:277, 530 |
| Neck crease after adding a neck mesh | bridge mesh invented to hide a head cut | bury the head root in the body; no bridge mesh | [E] FG02 |
| Variant deforms the body | variant made by bending the rigged body | build variants from one cut base, re-seat sockets | [E] FG03 |
| Seam flashes or shows holes | coplanar overlaps, uncapped cuts, bad normals, too little socket cover | repair caps / overlap; check backfaces; repeat extreme camera views | RP:409 |
| Holes after closing a generated shell | faces deleted into the body; many open edges in the source | count open edges first; tuck-and-cap, do not delete into the body | [E] FG05 |
| Model rotated, mirrored, wrong size | axis conversion, scene units, exporter scale, negative transforms, importer units | dimensioned reference; change one documented profile stage at a time | RP:402, 546 |
| Armature moves, surface stays | missing weights, wrong group names, wrong Armature target, skin not exported | verify binding in source, export copy and imported MeshPart | RP:404 |
| Bones or sockets missing after import | export allowlist, custom-bone tags, zero-influence removal | keep needed nodes explicitly; Keep Zero Influence Bones on [V RR22]; compare hierarchy manifests | RP:405 |
| Animation absent or wrong clip | unbaked controller keys, wrong Action / slot, NLA ambiguity, wrong range | bake a named clip; read imported joint transforms | RP:406 |
| Rigid part bends or detaches | smoothed weights, wrong parent or joint frame, missing rest offset | restore rigid binding or the Motor6D tree; pivot and shape test | RP:407 |
| Fine in Blender, collapsed in Roblox | Preserve Volume, corrective shape or helper driver that Roblox does not run | reproduce with supported bones and weights; compare the exact pose | RP:408 |
| Mechanism rotates off-axis | pivot or rail | restore the true axis and joint frames; never repaint a hinge | RP:545 |
| VFX or hitbox stays at rest position | reading the undeformed MeshPart placement | use the agreed bone or socket path; verify during playback | RP:411 |
| Repeated armatures / modifiers after retries | non-idempotent automation | inventory diff after every MCP change; each stage replaces only its own output | RP:548 |
| "Validated" with no evidence file | invented validation | mark BLOCKED; run or request the test | RP:549 |

## 3. Clothing and armour on generated meshes (RP:532)
Decide per piece: bends with the flesh, rides rigidly on a limb, or is a separate animated piece. A broad shoulder pad must not inherit a smooth chest / arm blend. A skirt fused across the legs needs a redesign or a deliberate topology / rig solution; splitting leg weights cannot make the fabric go away.

## 4. After any repair (RP:534)
Repeat the whole gate from bake onward: a manual repair can bring stale bind matrices, lost zero-influence sockets, changed UVs, renamed bones or scale drift. Keep the generator output and the repaired result separately.
