---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J007-T09, Modeler_Research_Paper.txt lines 913-926 (held out)"
supersedes: []
---
> Author: case writer · claude-sonnet-5-5 · high · 2026-10-21

**HIDDEN: do not give this file to the modeler under test.** Show the agent only the "Symptom" and "Files" of one case at a time, as an owner or agent message. "Answer key" and "Rubric" are for the grader only.

# J007 hidden test set: diagnosing AI-made model failures

Held out by order from the modeler's skills (ticket J007-T09). Source: the paper section on common AI-made model failures and targeted diagnosis, `RP:` = paper line. One case per failure type (six).

| id | Failure type | RP |
| --- | --- | --- |
| H1 | Form reads as vague next to the approved concept | 915 |
| H2 | A feature differs from the approved reference, cause unknown | 917 |
| H3 | Parts that look attached are not; an arm cannot move alone | 919 |
| H4 | Props import at inconsistent size, pivot and facing | 921 |
| H5 | Over budget; a blunt cut did not help and hurt the look | 923 |
| H6 | Clean asset that does not look like our game | 925 |

Fixed facts for every case (from the owner's decisions; the agent under test may know them): creatures and characters stay under about 7,000 triangles (20,000 per mesh is only the upload ceiling); the owner runs Tripo and the modeler finishes in Blender; checks are light: numbers first, images only when a number fails.

**Common rubric line (add to every case, id `H#-C`):** (must) The answer uses a number or a measured comparison before it proposes any edit (light checks), and it does not invent thresholds; where it needs a limit it takes it from the approved reference, the control asset, the owner's 7,000 budget or a measurement.

---

## H1. The wolf that will not read

**Symptom (show to the agent).** The Tripo-made Cinder Wolf (6,400 triangles) looks like a vague, lumpy dog next to the approved concept. In the 96 px hotbar icon, and in the arena against the orange lava floor, players cannot tell it from the Cinder Fox. The team already ran a fur-sculpt pass (3,900 to 6,400 triangles); the 4K close-up render looks richer, but the owner says it still reads wrong.

**Files (show).**
- `content/models/cinder-wolf/ref/approved_concept_front.png`, `approved_concept_side.png`
- `content/models/cinder-wolf/work/wolf_v1_raw.glb` (3,900 tris), `wolf_v2_furpass.glb` (6,400 tris)
- `content/models/cinder-wolf/renders/closeup_4k.png`, `arena_cam_128px.png`
- `content/models/cinder-fox/renders/arena_cam_128px.png`

**Answer key (grader only).**
- Diagnosis: a shape-level problem. The large forms and the features that identify the animal (ear size and angle, snout length, tail length and tip, shoulder line) do not match the approved concept. More surface detail does not fix this. The weakness shows only at the real on-screen size and background, not in a large isolated render.
- First decisive check: put the approved side and front views and the model in the same camera, same framing, flat shaded. Measure a few proportions on both (for example snout length over head length, ear height over head height, tail length over body length) and read the gap as numbers. Then shrink to the in-game size (about 96-128 px) on the two typical backgrounds and compare against the fox.
- Fix order: (1) list which major forms are off by the measured gap; (2) rebuild or regenerate only those parts (re-run Tripo with a corrected input, or rework them in Blender) instead of decorating them; (3) re-run the same comparison; (4) remove or reduce the fur-pass detail that does not read at size, so the triangle budget goes to the major forms; (5) final check at screen size on both backgrounds and the count stays under about 7,000.
- Must not: add more sculpt, normal or noise detail to hide wrong forms; judge only from the 4K isolated close-up.

**Rubric.**
- H1-1 (must) Names wrong major forms or identifying features against the approved concept as the cause, not missing detail.
- H1-2 (must) First check compares the model with the approved views in the same camera and reports proportions as numbers.
- H1-3 Tests at the real icon or arena size and on the lava-like background, not only the large render.
- H1-4 Rebuilds or regenerates the wrong parts and does not propose more fur or surface detail as the fix.
- H1-5 Keeps the final model under about 7,000 triangles.
- H1-C (must) Common line.

---

## H2. The turtle that lost its horn and its ring

**Symptom (show to the agent).** The approved concept of the Moss Turtle pet has three horns on the head and a brass ring on the left front leg. The final file has two horns and no ring, and in the front render the head looks about 20 percent wider than in the approved front image. Someone scaled the head in Blender to make the side picture fit, and now the front view is worse. Three versions exist and nobody knows when the features went missing.

**Files (show).**
- `content/models/moss-turtle/ref/concept_front.png`, `concept_side.png` (added a week later than the front), `concept_34.png`
- `content/models/moss-turtle/work/v1_tripo_raw.glb` (from the front picture)
- `content/models/moss-turtle/work/v2_tripo_reroll.glb` (a re-run from the side picture only)
- `content/models/moss-turtle/work/v3_cleanup.blend` (remesh and merge-by-distance pass)
- `content/models/moss-turtle/final/moss-turtle.glb` (v3 with the head scaled)

**Answer key (grader only).**
- Diagnosis: the mismatch has to be traced to the first version where each difference appears; the causes may differ per feature. Likely candidates: the generator reinterpreted or dropped a feature when re-run from a different input (horns, v2, and the side picture may simply hide the third horn), a cleanup step removed a thin feature (ring, v3 merge or remesh), and the two reference views may disagree with each other so one forced match breaks the other.
- First decisive check: render v1, v2, v3 and the final in the same camera and lens as each reference view (same orthographic front and side), then compare per version: horn count, ring present yes or no, head width over body width. The first version that differs is the one to repair. Also measure whether the front and side concept pictures agree on head size.
- Fix order: (1) matched comparison table across versions and views; (2) repair at the stage where the difference first appears (re-generate with a better input, restore the ring from the earlier version, or fix the cleanup settings); (3) undo the head scale; (4) if the concept views contradict each other, send one question to the owner or art director to name the authoritative view; (5) repeat the matched comparison on the new final.
- Must not: keep bending the mesh to satisfy one reference view at a time; compare versions with different cameras; patch only the final file without finding the first bad version.

**Rubric.**
- H2-1 (must) Traces the differences back through the versions (first version where each appears) instead of editing the final file.
- H2-2 (must) Uses matched cameras and lenses for the comparison across versions and reference views, with counts or ratios per version.
- H2-3 Separates possible causes (generator change, cleanup removal, camera or view difference) and does not assume one cause for both features.
- H2-4 Reverts the head scaling and does not distort the mesh to fit each view.
- H2-5 Escalates conflicting reference views to the owner or art director rather than choosing silently.
- H2-C (must) Common line.

---

## H3. The knight who is glued together

**Symptom (show to the agent).** The Clockwork Knight (one object, 5,900 triangles, Tripo output) looks right from the front. From behind and to the left you can see sky between the helmet crest and the helmet, and one shoulder plate sits slightly away from the body. In the rigger's pose test the right arm was raised overhead for the attack animation: the chest plate dragged sideways with it and the upper arm looked stuck to the ribs at the armpit. Painting the weights twice did not remove the stretch.

**Files (show).**
- `content/models/clockwork-knight/work/knight_tripo.glb`
- `content/models/clockwork-knight/rig/knight_armature_test.blend` (auto weights, arm weights repainted twice)
- `content/models/clockwork-knight/tests/pose_tpose_front.png`, `pose_arm_overhead_front.png`, `view_back_left.png`
- `content/models/clockwork-knight/brief.md` (the animator needs: right arm overhead swing, head turn, sword hand open and close)

**Answer key (grader only).**
- Diagnosis: two linked defects. Some pieces are separate surface shells that only look attached from one angle (crest, shoulder plate). The arm is merged into the torso with no clean armpit or shoulder topology, so it cannot rotate without dragging the chest. Weight painting on that geometry cannot fix it.
- First decisive check: count the loose parts and measure the gap between each pair of shells (for example Select Linked or Separate by Loose Parts, then compare shell count and the distance between nearest vertices); then run the arm through the animator's required pose and measure how far chest vertices move, or read the edge flow at the shoulder. The check must look from more than the front.
- Fix order: (1) list the loose shells and decide per part: crest, shoulder plate and sword are rigid items and can be separate pieces with their own pivot and a deliberate attachment; (2) for the arm, which must bend and swing in one surface, rebuild the shoulder and armpit topology (deliberate retopology with edge loops) and then skin it, or cut the arm into a separate piece where the look allows it (agree with the rigger); (3) re-test every required pose (arm overhead, head turn, hand open and close) in Blender and in Studio; (4) check the final count stays under about 7,000.
- Must not: bridge or weld the gaps just to hide them, or keep repainting weights on fused geometry; judge connection from the front view alone.

**Rubric.**
- H3-1 (must) Names the shells that only look attached from one view, and the arm merged with the torso, as separate defects.
- H3-2 (must) First check counts the loose parts and tests the required pose with a measured result, from more than one angle.
- H3-3 Decides per part between a separate rigid piece and continuous deformation with new topology and skinning, and says why.
- H3-4 Re-tests the animator's required poses in Blender and Studio after the fix.
- H3-5 Does not hide gaps by welding or keep repainting weights on the merged arm.
- H3-C (must) Common line.

---

## H4. Four props, four sizes

**Symptom (show to the agent).** Four props from one Blender batch (lamp post, barrel, crate, fence) were placed in Studio next to an R15 dummy. In Blender the dimension panel shows the planned sizes for all four (lamp post 3.0 m tall, barrel 0.9 m, crate 1.0 m, fence 2.0 m long). In Studio, compared to the heights in the layout plan, the lamp post is 0.66 of the planned height, the barrel 0.32, the crate 3.6 times and the fence is right but lies on its side. The lamp post turns around a point about a metre from its base when rotated, and the barrel's collision box hangs outside the visible mesh. Each person who placed a prop typed a different size multiplier into the spawn script.

**Files (show).**
- `content/models/kit-props/lamp_post/lamp_post.blend`, `lamp_post.glb`
- `content/models/kit-props/barrel/barrel.blend`, `barrel.glb`
- `content/models/kit-props/crate/crate.blend`, `crate.glb`
- `content/models/kit-props/fence/fence.blend`, `fence.glb`
- `src/server/spawn_props.luau` (holds the four per-prop size multipliers: 1.5, 3.1, 0.28 and none)
- `content/models/kit-props/_notes/layout_plan_heights.csv`

**Answer key (grader only).**
- Diagnosis: an interchange defect, not four bad models. The ratios differ per asset (0.66, 0.32, 3.6, 1.0), so a single global unit factor cannot explain them; each file has its own transform state (unapplied object scale or rotation, different scene unit settings, origin not at the base, axis settings at export). The multipliers in the spawn script are compensations that leave the transforms and collision wrong.
- First decisive check: run a control asset of known size (for example a cube and a human-height block built to the kit's standard) through the same pipeline, and compare its dimensions at three points: Blender, the exported file, Studio `Size`. Then list per prop the object scale, rotation, scene unit scale, origin position and export axis settings, and compute Studio size over Blender size per prop.
- Fix order: (1) control asset result sets what "correct" means; (2) fix each file at the source (consistent units, apply scale and rotation, origin at the base centre, forward and up axes as the kit requires); (3) re-export with the same settings for all four and re-import; (4) check Studio `Size`, rotation, pivot behaviour and collision box against the control; (5) delete the per-prop multipliers from `spawn_props.luau`; (6) keep one saved export setting for the kit.
- Must not: add or tune another size multiplier or rotation offset in Studio or the script; apply one global rescale to all four.

**Rubric.**
- H4-1 (must) Treats size, pivot and facing as one interchange problem and uses the different per-prop ratios as evidence.
- H4-2 (must) Uses a known-size control asset and compares dimensions before and after export (Blender, file, Studio).
- H4-3 Fixes transforms, origin and axes in the source files and re-exports with identical settings.
- H4-4 Removes the compensating multipliers and re-checks the collision box and pivot behaviour in Studio.
- H4-5 Does not propose one global scale factor or a new per-prop number.
- H4-C (must) Common line.

---

## H5. The golem that stayed slow

**Symptom (show to the agent).** The Crystal Golem boss (31,000 triangles, one 4096 by 4096 texture) runs at 24 fps on the test phone in the arena with 12 golems. The team cut the triangles to 25 percent (7,750) with a decimate pass and shrank the texture to 256 by 256. Phone fps is now 25, and the glowing rune on the chest cannot be read any more. The owner asks why almost nothing changed.

**Files (show).**
- `content/models/crystal-golem/work/golem_v1.blend` (31,0xx tris, 9 material slots, 3 of them alpha blended crystal shells, collision fidelity set to Precise)
- `content/models/crystal-golem/work/golem_v2_decimated.glb` (7,750 tris, same 9 materials)
- `content/models/crystal-golem/tex/golem_albedo_4096.png`, `golem_albedo_256.png`
- `content/models/crystal-golem/perf/arena12_before.txt` (frame 41.7 ms, 372k triangles drawn)
- `content/models/crystal-golem/perf/arena12_after.txt` (frame 40.1 ms, 93k triangles drawn)

**Answer key (grader only).**
- Diagnosis: the reduction was global and not tied to what the scene pays for. A 4x cut in triangles moved frame time by about 4 percent (41.7 to 40.1 ms), so triangles were not the bottleneck. Materials (9 per golem, so 108 for 12), the three alpha-blended shells and the precise collision are the measured candidates in the files. The texture cut removed the identifying rune, so it was the wrong reduction.
- First decisive check: compute the change in frame time against the change in triangles (about 4 percent for 75 percent fewer), then take a breakdown of where the frame goes on the phone (render, physics) and test one variable at a time: merged material count, alpha shells off, collision fidelity changed. Note that 7,750 is still above the owner's budget of about 7,000.
- Fix order: (1) name the cost with a one-variable-at-a-time measurement; (2) fix that cost (fewer materials by atlasing or merging, replace or reduce the transparent shells, collision fidelity set to what gameplay needs); (3) restore the rune at the texel density it needs (give it a larger share of the UV space; shrink low-value areas first) rather than one global texture size; (4) bring triangles under about 7,000 as the budget rule, placing reductions where the shape does not read; (5) re-measure with the same capture recipe and compare to 41.7 ms and the 24 fps baseline.
- Must not: decimate again or shrink the texture further as the performance fix; accept 7,750 triangles or the 256 texture as done; claim a gain without the same-recipe re-measurement.

**Rubric.**
- H5-1 (must) Uses the numbers in the files (small frame-time change for a large triangle cut) to say the triangle cut did not address the bottleneck.
- H5-2 (must) Names the cost candidates in the files (materials, transparent shells, collision) and tests them one at a time before editing.
- H5-3 Treats the rune as information that must stay readable, and fixes the texture by what it must show, not by one global size.
- H5-4 Keeps the owner's 7,000 budget as a separate rule and notes that 7,750 still exceeds it.
- H5-5 Re-measures with the same capture recipe after the change.
- H5-C (must) Common line.

---

## H6. The scarecrow from another game

**Symptom (show to the agent).** The Tripo-made Harvest Scarecrow (6,200 triangles, clean import, passes the gate) is going into the farm zone next to the approved Mossback Toad and the Barrel Cart. The owner says it looks like it belongs to a different game, though nothing is broken. The first fix was to re-run Tripo with "make it stylized, cartoon" added to the prompt, and the result changed very little.

**Files (show).**
- `content/models/scarecrow/work/scarecrow_tripo.glb` (embedded textures: albedo 2048, roughness 2048, normal 2048)
- `content/models/scarecrow/renders/farm_cam_front.png`
- `content/models/mossback-toad/final/mossback-toad.glb`, `renders/farm_cam_front.png` (approved)
- `content/models/barrel-cart/final/barrel-cart.glb`, `renders/farm_cam_front.png` (approved)
- `knowledge/design/art-bible.md`

**Answer key (grader only).**
- Diagnosis: the asset is technically clean but does not match the approved models on one or more style axes; the generator's default look is competing with the studio's style. No single word like "stylized" covers it; the axes must be checked one by one.
- First decisive check: build a comparison table, scarecrow against the toad and cart, with one measured number per axis: value grouping (number of distinct value masses in a greyscale squint), shape vocabulary and edge treatment (smallest feature size as a share of height, bevel or edge hardness), surface roughness (mean of the roughness map), palette (hue count, saturation, colour distance in a perceptual space), detail scale (finest texture detail against the size on the farm camera). Read which axes sit outside the range the two approved models show; take no outside threshold.
- Fix order: (1) the per-axis table decides which axes fail; (2) replace the generator's default material and texture with the studio's own material system and palette; (3) change shape vocabulary and detail scale at the form level for axes that still fail (thicken thin straw and stitching, simplify the cloth, match the edge treatment); (4) re-measure the same table; (5) put it next to the toad and cart at the farm camera and ask for the owner's look only if a number is still outside the range.
- Must not: re-roll with a general "stylized" prompt and call it done; accept the asset because it passes the gate and is under budget; keep the generator's default material.

**Rubric.**
- H6-1 (must) Compares the scarecrow with the approved toad and cart (not with a generic idea of the style), axis by axis.
- H6-2 (must) First check gives a measured number per axis and takes the range from the approved models.
- H6-3 Names at least four of the axes separately: value grouping, shape vocabulary, surface roughness, palette, edge treatment, detail scale.
- H6-4 Replaces the generator's default material with the studio's own, and fixes form-level axes only where the numbers fail.
- H6-5 Does not treat the passing gate or the budget as proof that the asset fits the game.
- H6-C (must) Common line.
