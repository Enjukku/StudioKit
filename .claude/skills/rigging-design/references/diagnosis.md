> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-design`. Sources: rigging paper RP:275-285, 400-411, 520-549 (notes `knowledge/reference/rigging/02-*.md` §1.2, §5.3, §7.2-7.3); first-game FG01-FG07. All [O] unless marked. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (one named problem per pass, the problem behind a note, read and measurement symptoms; rows marked T were reproduced on Blender 5.1.2 headless, 2026-10-22; repair round 1 added the weighted-cap and small-piece rows; repair round 2 widened the cap row to n-gon and fan caps; repair round 3 added the shared-group row).

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

**One named problem per pass.** Name the layer that fails, fix only that, re-run the whole check (a fix can break another layer), then take the next. "Not right yet" is not a cause: find the layer.

**The problem behind a note.** A rig note often carries a fix ("add a neck bone", "smooth the shoulder"). Restate the problem in one line ("the chest moves when the head turns"), find its layer with the order above, and fix that; if your fix differs from the suggested one, say why in the answer. Re-check the problem, not only the change.

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
| Head turns with the body in a spin although the animator held it | no world-orient switch; or the export skeleton was baked without visual keying (the bake records the head's own channels, not the constraint's result); or a copy got the Action but no slot, so it played nothing and the bake recorded a frozen pose | head drift per frame on the export skeleton after the bake and after FBX re-import (`rigging-craft/references/blender-mcp.md` §6) | T |
| Head jumps when the world-orient switch turns on at rest | the switch's target is not the head's rest world frame (a target at identity rotated the head 90°) | toggle the switch at rest: the head moves 0° | T |
| Wind-ups and throws look dead | no clavicle range, or the hips have no control apart from the root | the manifest has clavicle (or upper-torso) and hip controls with the §B ranges; `clip_check.py` rom on the wind-up clip | [O] |
| A spin pops in one frame | an Euler channel wrapped (170° to -170°) | quaternion rotation mode for spin-heavy controls; `clip_check.py` pops with a landmark off the spin axis (a landmark on the axis measures nothing) | T |
| Costume clips at a stress pose (collar in the jaw, hand through the helmet, cape through the arm) | mass on a joint or a drape (a design problem, not weights) | overlap pairs between parts that are not parent and child at the pose; a design-for-motion note to the modeler | T |
| The hook shape is hidden at the key pose | no control for it, or a chain lag that hides it | a control per hook part; the key-pose black-fill from the game camera | [O] |
| Cap exposure reads 0 but a seam shows in the render | the cap was sampled at its face centre only (the centre can sit on the pivot axis and stay hidden while the rim shows); the cap is an n-gon or a triangle fan (Bisect with Fill makes one n-gon) and the sampler covered only a patch of it; or the cap faces are missing from their cut's `cap_<cut id>` group; or the part was hidden in the viewport (rays pass through it); or a thin strip along the rim of a large low-poly cap (7 points per triangle miss it) | sample every cap face through its triangles (`rigging-craft/references/blender-mcp.md` §6 recipe 1); every cut of the part has its own group with a sampled count above 0 | T |
| Cap exposure above 0 at rest on a box or low-poly part, but no cap shows in the render | one group holds both rims of a part between two cuts, so the side faces whose corners all lie on the two rims are counted as cap (no edge loop between the cuts) | one `cap_<cut id>` group per cut and the count per cut (`rigging-craft/references/blender-mcp.md` §6 recipe 1); at rest the box and low-poly parts read 0 | T |
| Socket reads exposed at rest on a blocky or primitive parent, but nothing shows in the render | the socket group holds the parent's whole closed face on the cut plane (the torso top under the head, a side face under a flush arm), not only the area the child covers; or the group was marked again without deleting it first | mark the socket with `child=` (only faces inside the child's cap outline: `rigging-craft/references/blender-mcp.md` §6 recipe 1); on a closed face cut the child's cap outline in, or record the socket n/a and count the cut on the child's cap only | T |
| A cut socket reads a few points at rest from a high camera, but nothing shows | rays that graze the child's bottom rim pass its edge (a socket cut along the child's outline) | look at the still; the points vanish when moved 0.0001 in the socket's plane: no fix note | T |
| Cap exposure reads 0 on a weighted or skinned part at every pose | the points were taken from `ob.data`, which holds the rest positions; the rays go to where the cap was at rest | take the points from the evaluated mesh (`rigging-craft/references/blender-mcp.md` §6 recipe 1); the 70° tilt test reads the same count as a bone-parented copy | T |
| ROM check passes but the pose is out of range | the manifest names a channel the bone does not use (an Euler channel on a quaternion bone reads 0); a degree range on a quaternion channel (the channel is a raw component, about -1 to 1); a quaternion bone that also turns about a second axis in the clip (the tilt moves into another component); or the control is moved by a constraint or IK, which the basis channels do not show | the manifest channel matches the bone's rotation mode; quaternion channels by index in `quat` units, ±sin(θ/2) (`rigging-craft/references/controls-export-import.md` §3); a two-axis bone measured by swing (recipe 5); constraint-driven controls on the baked export skeleton | T |
| A part came off in the render, but the black-fill count equals rest | the piece is under 0.5 % of the image, so `look_check.py` does not list it (a small figure in a full phone frame) | count on the crop of the figure's box; trust the count only when the listed component areas add up to the mask area (`rigging-craft/references/tests.md` §2) | T |
| Protected region measures 0 but the chest moves | the protected group stops short of the vertices with the remote weight | the protected group reaches the start of the planned transition; re-run the sweep | T |
| Imported clip compares one frame off | the FBX re-import's frame range starts one frame later | compare by clip frame (frame minus the range start), never absolute frames | T |

## 3. Clothing and armour on generated meshes (RP:532)
Decide per piece: bends with the flesh, rides rigidly on a limb, or is a separate animated piece. A broad shoulder pad must not inherit a smooth chest / arm blend. A skirt fused across the legs needs a redesign or a deliberate topology / rig solution; splitting leg weights cannot make the fabric go away.

## 4. After any repair (RP:534)
Repeat the whole gate from bake onward: a manual repair can bring stale bind matrices, lost zero-influence sockets, changed UVs, renamed bones or scale drift. Keep the generator output and the repaired result separately.
