---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J007-T11
supersedes: []
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J007-T11: grades for the hidden test (H1-H6)

Graded from `hidden-answers.md` against the rubric in `hidden-cases.md`. A line passes only when the answer clearly does what the line asks. Case pass rule: at least 80 percent of lines and no (must) line failed. Evidence quotes are 20 words or fewer.

Note on the answers: the agent said the named files do not exist and labelled every check "not verified". The answers are plans with predicted readings. I graded the plan, as the cases ask for a diagnosis. I did not penalise the missing measurements.

## H1. Cinder Wolf

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H1-1 (must) | pass | "primary silhouette and landmarks (ear shape and height, muzzle length, neck ruff, tail...) do not match the approved concept" | Names wrong forms as the cause. Calls the fur pass micro-detail that changes nothing at 128 px. |
| H1-2 (must) | pass | "flat black silhouettes ... at the concept's front and side cameras ... compare ratios (muzzle length / head length, ear height / head height)" | Same-camera comparison with the approved views. Proportions given as numbers (check 4 and IoU in check 2). |
| H1-3 | pass | "downscale ... to 96 and 128 px"; "value contrast of the wolf region vs the lava floor in arena_cam_128px.png" | Tests at icon and arena size, on the lava background, against the fox. |
| H1-4 | pass | "No further surface passes"; "repair the primary masses in Blender, or a Tripo re-run"; fur only "where they change the outline" | Rebuilds the wrong forms. Does not propose more surface detail as the fix. |
| H1-5 | pass | "Audit (triangles under about 7,000 whole model, J007-D5, spent on silhouette)" | Keeps the 7,000 budget. |
| H1-C (must) | pass | "Design control ... IoU ... ΔE2000"; "No approved tolerance → measured, project value → needs-decision" | Numbers come first. No invented limit. |

Score 6/6. Must failed: none. **Verdict: PASS**

## H2. Moss Turtle

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H2-1 (must) | pass | "Version bisect ... v1, v2, v3, final: horn count ... ring present ... head width / shell width"; "Pick the base: the latest version that holds every invariant" | Traces the first bad version per feature. Does not patch the final file. |
| H2-2 (must) | fail | absent for the version comparison; only "one review set at the three concept cameras" (fix step 7) and "projection check of the side image" | The bisect measures the evaluated meshes. It never says to render v1, v2, v3 and the final in the same camera and lens as each reference view. Only the new final gets the concept cameras. Counts and ratios per version are present, but the matched-camera part of the line is not. Borderline. |
| H2-3 | pass | Separate rows: side image, v2 re-roll "from the side picture only", v3 "remesh and merge-by-distance", head scale | Separates causes. Expects different losses per feature (ring lost in v2 or v3, horn in v2). |
| H2-4 | pass | "The mesh is never scaled to a disputed image"; "Head proportion from the approved front (invariant)"; base is v1, not final | The scale is dropped by moving to the earlier base. Does not distort the mesh. |
| H2-5 | pass | "ask the art director/owner which form is right" | Escalates the conflicting views. Does not choose silently. |
| H2-C (must) | pass | "as counts: horns per view, ring present, head width / shell width"; no thresholds invented | Counts and ratios first. |

Score 5/6 (83%). Must failed: H2-2. **Verdict: FAIL** (a must line failed)

## H3. Clockwork Knight

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H3-1 (must) | pass | H3-a "Sky between helmet crest and helmet"; H3-b "Shoulder plate floats off"; H3-c "fused bridge of geometry between arm and torso" | Shells and the fused arm are named as separate defects. |
| H3-2 (must) | pass (weak) | "connected-part count, open edges, floating parts"; "Clay + wireframe from back and back-left"; chest-plate vertex weights | Counts the loose parts, looks from the back, and reads the armpit connectivity. This matches the key's "or read the edge flow at the shoulder". It does not run the arm through the required pose and measure chest movement; the weight reading is a proxy. |
| H3-3 | pass | "arm separated at the shoulder under the pauldron"; chest plate "separate rigid piece"; sword separate; R-skin zones get loops | Decides per part and gives reasons (R-cut / R-mix, ROM overlap). |
| H3-4 | fail | "hand to the rigger for the S4 proxy sweep with the arm overhead" | Names only the arm overhead, hands it to the rigger, and does not name Blender and Studio. Head turn and hand open and close are not re-tested. |
| H3-5 | pass | "More weight painting ... the bridge is geometry"; "Close the crest gap ... with a global merge/fill" listed under Must not | Does not hide gaps by welding. Stops weight painting. |
| H3-C (must) | pass | "rig_audit.py audit_mesh" counts and gaps first; no invented limits | Audit numbers before edits. |

Score 5/6 (83%). Must failed: none. **Verdict: PASS**

## H4. Four props

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H4-1 (must) | pass | "Each prop imports at a different wrong ratio (0.66, 0.32, 3.6, 1.0): there is no single scale chain"; "1.5 × 0.66 ≈ 0.99" | Treats size, pivot and facing as one interchange problem. Uses the per-prop ratios as evidence. The check that the multipliers cancel the errors is stronger than the key. |
| H4-2 (must) | pass (weak) | "Calibration round trip: block of known size with a marked front + player dummy ... import, measure" | A known-size control is used. It sits in the fix order, not the first check. The Blender, file and Studio comparison is only implied (per-file node transforms in check 1, GetExtentsSize in check 4). |
| H4-3 | pass | "apply rotation and scale → size in studs → origin at base centre"; "Versioned export copies" with one kit profile | Fixes at the source. Re-exports with the same settings. |
| H4-4 | pass | "remove all four multipliers in the same change that swaps in the fixed assets"; "measure size vs plan, pivot, orientation, collision" | Both parts present. |
| H4-5 | pass | "Add another multiplier, or fix scale in Studio or code" under Must not | No global factor. No new per-prop number. |
| H4-C (must) | pass | "Predict each Studio ratio from those per-file factors; it must reproduce 0.66 / 0.32 / 3.6 / 1.0" | Numbers first. Unknown plan units go to needs-decision. |

Score 6/6. Must failed: none. **Verdict: PASS**

## H5. Crystal Golem

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H5-1 (must) | pass | "372k → 93k triangles drawn moved the frame only 41.7 → 40.1 ms (24 → ~25 FPS): triangles are not the main cost" | Uses the file numbers. |
| H5-2 (must) | pass | A/B switches: "(a) crystal shells hidden; (b) collision Box/Hull instead of Precise; (c) CastShadow off; (d) one golem with a single merged material" | Names materials, alpha shells and collision. Tests each one at a time before any edit. |
| H5-3 | pass | "give it texel density on purpose, or an emissive mask ... check the rune reads at the arena camera" | The rune is treated as information to keep. Not one global size. |
| H5-4 | pass | "7,750 is still over"; "creature budget (under about 7,000, J007-D5)" | Budget kept as a separate rule. |
| H5-5 | pass | "Re-measure: same scene, same device, 3+ runs, before → after" | Same recipe. |
| H5-C (must) | pass | "FPS = 1000 / frame ms"; capture first; "phone verdict not verified" | Measurement first. No invented thresholds. The 1024² texture plan is labelled PROPOSAL. |

Score 6/6. Must failed: none. **Verdict: PASS**

## H6. Harvest Scarecrow

| Line | Result | Evidence | Reason |
| --- | --- | --- | --- |
| H6-1 (must) | pass | "ΔE2000 of the scarecrow's dominant colours ... and the same for toad and cart as control"; "clay renders of scarecrow, toad and cart" | Compares with the approved toad and cart. Axes covered: palette, value, saturation, shape versus surface, map sets. Edge treatment and detail scale are not compared one by one. |
| H6-2 (must) | fail | "No approved tolerance → measured; the relative result ... is the evidence"; shape judged by "clay" split | The range comes from the approved models, which is right. Numbers exist for palette, value, saturation and map sizes. Shape vocabulary, edge treatment, roughness and detail scale get no number; shape is a visual clay comparison. The line asks for one number per axis. Borderline. |
| H6-3 | pass | palette, "value range, saturation", shape language, "realistic PBR set (albedo, roughness, normal at 2048)" with "high-frequency detail" | At least four axes named. Edge treatment and detail scale are not named on their own. |
| H6-4 | pass | "re-texture: remove baked light, repaint/re-bake to the art bible palette roles and the material treatment of the approved assets"; shape work only "if the split showed shape" | Replaces the generator's surface. Form-level fixes are conditional on the check. |
| H6-5 | pass | "'Passes the gate, clean import' proves construction only"; "Call it done because the gate passed" under Must not | Gate and budget are not proof. |
| H6-C (must) | pass | "ΔE2000 ... No approved tolerance → measured"; range from the approved assets | Numbers first. No outside threshold. |

Score 5/6 (83%). Must failed: H6-2. **Verdict: FAIL** (a must line failed)

## Overall

| Case | Score | Must failed | Verdict |
| --- | --- | --- | --- |
| H1 | 6/6 | none | PASS |
| H2 | 5/6 | H2-2 | FAIL |
| H3 | 5/6 | none | PASS |
| H4 | 6/6 | none | PASS |
| H5 | 6/6 | none | PASS |
| H6 | 5/6 | H6-2 | FAIL |

**Overall: 4 of 6 cases passed.** Both failures are one borderline must line each, and both are the same kind of gap: the comparison was only partly measured.

## Skill gaps

1. H2-2: the skills did not teach that a comparison across versions and reference views must use one camera and lens per view, with the versions rendered and not only read from mesh data.
2. H6-2 (and H6-1 edge treatment and detail scale): the skills did not teach a measurable number for each shape and surface axis (smallest feature as a share of height, edge hardness, roughness-map mean, detail against farm-camera size). The agent measured the colour axes and judged shape by eye.
3. H3-4: the skills did not teach that the hand-back must re-test every pose the animator needs (arm overhead, head turn, hand open and close) in Blender and in Studio, not only the arm in a rigger sweep.
4. H3-2 (weak): the first check did not run the required pose and measure chest-vertex movement. It read weights and topology instead.
5. H4-2 (weak): the known-size control should be the first check, measured at three points (Blender, file, Studio). It appeared only in the fix order.

## Done better than the key (credit, grades unchanged)

- H1: tested whether the approved wolf and fox concepts are themselves confusable before blaming the model. This stops wasted modelling.
- H4: showed the multipliers cancel the import errors (1.5 × 0.66, 3.1 × 0.32, 0.28 × 3.6 all about 1). This proves the cause and confirms that the compensations hide it. It also said to remove the multipliers in the same change as the asset swap, to avoid a double correction.
- H2: found that a ring may exist only in the texture and that a voxel remesh destroys UVs. It also asked for a lineage table.
- H5: counted draw calls (9 materials × 12 golems), noted that 31,000 triangles passed the 20,000 per-mesh ceiling only because it was split, and refused to claim phone fps from Studio numbers.
- H3: tied the chest-plate drag to a route error (rigid armour on auto-weights). Covered the sword and hand fusion that the animator brief needs.
- H6: split shape from surface with clay versus textured renders. This points the fix to the right layer.
- All cases: stated that the files were missing and labelled every reading "not verified". It did not claim results.
