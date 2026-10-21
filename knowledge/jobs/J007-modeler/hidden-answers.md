---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J007-T10
supersedes: []
---
> Author: modeler · claude-opus-5-5 · high · 2026-10-21

# J007-T10: diagnosis of six model reports (H1-H6)

The files named in the reports do not exist on disk. Every finding below is a diagnosis from the report text and the skills. Label for every check: **not verified**. The expected readings are predictions to confirm or refute; none is a measured result.

Sources used (short ids): MD = `modeling-design` (M-xx craft rows; RC = `references/reference-check.md`, BU = `budgets.md`, RV = `review.md`, KE = `kits-and-environment.md`); MC = `modeling-craft` (C-xx; BR = `blender-recipes.md`, TF = `tripo-finish.md`, RP = `rig-parts.md`, TM = `textures-materials.md`, EI = `export-import.md`, HO = `handoffs.md`); RPL = `rig-pipeline` (+ `tripo-routes.md`, `modeler-handoff.md`); RI = `reference-images`; PF = `performance` (+ `references/fixes.md`, `measure.md`); MR/FM = `knowledge/reference/modeling/fact-check-roblox.md`, `04-first-game-experience.md`; art-review R-03 (no tolerance, no verdict).

Thresholds used, all sourced: creature/character budget under about 7,000 triangles, whole model (owner J007-D5); 20,000 triangles per mesh is the upload ceiling (MR01); one material and one UV set per mesh (MR12); 16.67 ms = 60 FPS, 33.33 ms = 30 FPS, FPS = 1000 / frame ms (MR34); texture guidance 256² for 5×5 studs, 512² for 10×10, 1024² for 20×20 (MR11); 1 stud = 28 cm as a physics reading, not an export setting (MR35). Where no approved tolerance exists, the number is reported as `measured` and a project value goes to `needs-decision` (art-review R-03; the audit "never invents a threshold", BR §4).

---

## H1. Cinder Wolf: does not read, confused with the Cinder Fox

### 1. Diagnosis (separate defects)
| # | Kind (RV §3.1) | Defect | Why |
| --- | --- | --- | --- |
| H1-a | identity | The primary silhouette and landmarks (ear shape and height, muzzle length, neck ruff, tail, leg length) do not match the approved concept, so at the arena camera and at 96 px it reads as "a dog", and wolf and fox share a silhouette | M-01, M-03: the read is the silhouette at the game camera, before any surface; FM34: two things with one silhouette → change one |
| H1-b | process | The raw Tripo result (3,900) was not rejected or repaired for weak identity before clean-up | M-11; TF §2.4 ("weak identity" is a reject-early reason) |
| H1-c | budget / detail | The fur-sculpt pass added 2,500 triangles (+64 %) of micro-detail that changes nothing at 128 px and probably makes the outline noisier ("lumpy") | M-04, C-15, FM18 (owner: "a lot of triangles that aren't necessarily needed"); BU §3: never spend because the budget has room |
| H1-d | review | The work was judged at a 4K close-up, not at the game camera and icon size | M-01; RV §1 (review set includes the game camera) |
| H1-e | identity (palette/value) | Possible low figure-ground value or hue contrast between a "cinder" palette and the orange lava floor, and wolf/fox palettes too close | palette roles are an invariant from the art bible (RC §4); the art director owns them |

Root cause to test first: is the confusion in the **model** or already in the **design**? If the approved wolf and fox concepts are themselves confusable at 96-128 px, no modelling fixes it.

### 2. First decisive check (numbers before any edit)
1. **Design control**: downscale `approved_concept_front/side.png` and the fox's approved concept to 96 and 128 px; `look_check.py` silhouette (IoU) wolf-concept vs fox-concept, and value/palette (CIELAB, ΔE2000). Expected: the concepts are distinct (wolf-vs-fox IoU clearly lower than wolf-model-vs-fox-model). If not → design problem, go to §5.
2. **Model vs concept**: flat black silhouettes of `wolf_v1_raw` and `wolf_v2_furpass` at the concept's front and side cameras and at the arena camera; IoU vs the concept and vs the fox model. Expected: wolf-model-to-fox-model IoU ≥ wolf-model-to-wolf-concept IoU (confusable by shape); v1 and v2 IoU vs concept nearly equal.
3. **What the fur bought**: mask difference v1 vs v2 at the arena camera (128 px). Expected: near-zero changed pixels for +2,500 triangles.
4. **Landmark numbers**: project the concept's landmarks (ear tip, muzzle tip, tail tip, shoulder height) with `world_to_camera_view` (BR §3) and compare ratios (muzzle length / head length, ear height / head height) with the concept. Expected: the ratios that make a wolf (longer muzzle, ruff mass, tail) are off.
5. **Value vs floor**: `look_check.py` value contrast of the wolf region vs the lava floor in `arena_cam_128px.png`, same for the fox. No approved tolerance → `measured`, project value → needs-decision (R-03).

### 3. Fix order
1. Freeze v2; record lineage (raw file, Tripo settings, v1, v2) in the asset record (M-16). No further surface passes.
2. Run the checks above; sort the defects: identity first (RV §3.2, biggest effect first).
3. If the concepts confuse → stop modelling; needs-decision to the art director and owner (two options at the same camera, e.g. which silhouette feature separates wolf from fox).
4. If the concepts read but the model does not: start again from **v1** (working copy of the raw, never the raw), not v2. Decide route by clean-up cost (RC §5): repair the primary masses in Blender, or a Tripo re-run by the owner with a corrected input pack (TF §1; max 2 regenerations, then the lead decides), or hand route.
5. Rebuild identity as big masses in grey at the arena camera and at 96 px (M-03): muzzle, ear, ruff, tail, leg proportion from the approved front and side. Fur as a few large clumps only where they change the outline (ruff, tail); fine fur in the colour/normal map (TM §2, cheapest representation).
6. Palette and value: apply what the art director decides (palette roles, a value step vs the floor); the modeler applies it in the texture or a tint (MR16), never picks it.
7. If the wolf is rigged: the remodel invalidates cuts, UVs and bakes; re-run every check the fix can break (RV §3.4) and tell the rigger before S3 work restarts.
8. Audit (triangles under about 7,000 whole model, J007-D5, spent on silhouette); one review set incl. arena camera and a 96 px icon-size render; then icon renders of the **shipped** model to UI (HO §4).

### 4. Must not
- Add more fur or judge on the 4K close-up: it spends triangles where nothing reads (M-04, FM18).
- Keep 6,400 because it is "under 7,000": the budget is a ceiling for the kind, not a target (BU §3).
- Change the wolf's design (new feature, new colours) on my own to separate it from the fox: invariants go to the art director and owner as two options (RC §4).

### 5. Who else
- **Art director**: the look_check numbers (silhouette IoU, value, ΔE2000), the concept-level result, a request for palette-role / value decision vs the lava floor and vs the fox.
- **Owner** (via lead): two rendered options if the design must change; the Tripo input pack if a re-run is chosen (J007-D4).
- **UI designer**: new icon renders from the shipped model (HO §4).
- **Character-rigger** (if rigged): notice that geometry will change, before S3 resumes.

---

## H2. Moss Turtle: lost horn, lost ring, head 20 % wide

### 1. Diagnosis (separate defects)
| # | Kind | Defect | Why |
| --- | --- | --- | --- |
| H2-a | reference | `concept_side.png` was added a week later; it may not be the same design as the approved front (horn count, head width/length, ring), or it may be a perspective shot | RC §3 "same design in every view", "projection"; RI I-10 (an extra view of an existing subject must attach the approved image) |
| H2-b | route | v2 was re-rolled from the **side picture only**: one side hides the far side, so the third horn and the ring on the **left** front leg may be absent from the input and invented away | RC §3 "hidden areas"; TF §2 (backs and hidden sides are invented); RI I-04 (three-quarter single view) |
| H2-c | construction | v3 "remesh and merge-by-distance" can fuse or delete small features: a thin ring merges into the leg, a small horn collapses; voxel remesh also destroys UVs, so a ring that existed only as **texture** disappears | REV05 / BR §3 (never one global merge distance; remesh gives no feature-safe topology); TF §2 (texture can paint a feature that has no shape) |
| H2-d | identity | The head was scaled to fit the side picture: an invariant (proportion) changed silently, making the approved front ~20 % wrong. This is averaging two views into a third design | RC §3 ("never average two views"), RC §4 |
| H2-e | process | No lineage: nobody knows which version lost what | M-16 |

### 2. First decisive check
1. **Reference check** of the three concept images (RC §3), as counts: horns per view, ring present (left front leg), head width / shell width and head length / shell length per view; projection check of the side image. Expected: front and ¾ agree (3 horns, ring); side disagrees (head proportion, or horn/ring not visible) or is perspective.
2. **Version bisect** on evaluated meshes (no edits; copies only): per file v1, v2, v3, final: horn count (connected components or landmark peaks in the head region, clay view), ring present as **geometry** (clay) and as **texture** (colour map), head width / shell width. Expected: v1 = 3 horns + ring; v2 = 2 horns, no ring (hidden side not in the input); v3 = same as v2 or further fused; final = v3 with head ratio ≈ 1.2 × the front concept.
3. Approval record: which image ids carry an owner decision line. Only those are invariants.

### 3. Fix order
1. Freeze all four files; write the lineage table (file, source image, route, settings, what changed, what it lost) in the asset record.
2. Settle the reference: if the side image disagrees with the approved front, regenerate it **from the approved front attached** (RI I-10; max 2 tries) or ask the art director/owner which form is right. The mesh is never scaled to a disputed image.
3. Pick the base: the latest version that holds every invariant (expected v1), not `final`.
4. Clean up from that base only where the audit flags (BR §3 clean-up row; C-09): no global merge distance, no voxel remesh over horns and ring.
5. Model any missing feature as **shape** (TF §3.4: a missing part is modelled, never painted): third horn, brass ring as geometry. Ring material: one material per mesh (MR12), so either brass in the same texture set or its own MeshPart; if the pet is rigged, the rigger decides whether the ring is a rigid piece on the leg bone.
6. Head proportion from the approved front (invariant). If v1 is too weak to keep, the owner re-runs Tripo from a clean three-quarter view that shows all three horns and the left-leg ring (TF §1; turn the subject so the features show, RC §2 FM06), or multiview images all made from the approved front.
7. UVs and re-bake after structure is final (TM §3.1, §5); audit; part inventory as numbers (horns = 3, ring = 1 vs the record, RV §2); one review set at the three concept cameras.

### 4. Must not
- Scale the head (or anything) to make one picture fit: that changes an invariant and averages views (RC §3-4).
- Run a global merge-by-distance or voxel remesh again over small features (REV05).
- Re-roll from a single side view, or paint the ring/horn on the texture only.

### 5. Who else
- **Art director**: the view-consistency result; request to regenerate or rule on the side image.
- **Owner** (via lead): approval of the corrected view set; Tripo re-run with the input pack if v1 is not kept.
- **Character-rigger** (if the pet moves): ring on the leg and horns on the head as rigid pieces or skin; heads-up that the head geometry changes.
- **Lead**: the lineage gap (three versions, no record) as a process lesson.

---

## H3. Clockwork Knight: gaps, floating plate, chest drags with the arm

### 1. Diagnosis (separate defects)
| # | Kind | Defect | Why |
| --- | --- | --- | --- |
| H3-a | construction | Sky between helmet crest and helmet (back-left view): a gap or missing surface in a hidden area Tripo invented | TF §2 (false backs); M-11 |
| H3-b | construction | Shoulder plate floats off the body: a loose shell with no contact | RV §2 connectivity; audit "floating" |
| H3-c | construction → motion | Upper arm "stuck to the ribs" at the armpit: a **fused bridge** of geometry between arm and torso. Weights cannot remove geometry, so two weight repaints failed | tripo-routes §1-2, FG01 (fused bridges; weights cannot fix it); M-12 |
| H3-d | motion (route) | Chest plate drags sideways when the arm goes overhead: a rigid armour plate is skinned to arm bones by auto-weights on a merged mesh. Armour is R-cut / R-mix (one bone, rigid), not one skin | M-09; `rigging-design/region-routes.md` (hard plates → R-cut; armoured humanoid → mix) |
| H3-e | motion (needs) | Sword hand open/close and head turn need a separate held sword, hand/finger geometry not fused to the grip, and a head cut under a gorget/collar; a Tripo grip is often fused | M-11 ("fused grips"); RP §5 (held tools separate) |
| H3-f | process | Rigging started on raw Tripo geometry: S2 plan and S3 geometry were skipped | RPL §3 (S2 → S3 → S4 before S5) |

### 2. First decisive check
1. `tools/rig/rig_audit.py audit_mesh` / `model_audit.py` on a copy of `knight_tripo.glb`: connected-part count, open edges, floating parts, intersecting shells (tripo-routes §1: one object is not one connected surface). Expected: arm and torso are one connected surface with shared edges in the armpit (the bridge); the shoulder plate is a separate shell with zero contact (floating); the crest has a measurable gap to the helmet or open edges on the helmet back.
2. In the rigger's test file (read only): vertex weights of the chest-plate vertices. Expected: non-zero upper-arm/shoulder weights → explains the drag.
3. Hand region: connected parts of hand + sword. Expected: fingers fused to the grip (one component).
4. Clay + wireframe from back and back-left (TF §2.2) to see what the back really is.

### 3. Fix order
1. Stop weight painting. Through the lead, get the pipeline in order: animator §B needs with ROM units (arm overhead, head turn, hand open/close) → rigger S2 plan: route per region, cut list, deformation zones (RPL §3). The modeler does not choose joints or cuts.
2. Raw-candidate verdict with the rigger and lead: keep and repair, or route change. A hard-surface knight with plates and many moving parts fits the hand route (RC §5: mechanical pivots, many moving parts); compare repair cost vs rebuild, no invented success rate (TF §4).
3. If kept, S3 on a working copy (RP §2): construction first: seat the crest on the helmet and the shoulder plate on the shoulder as the approved reference shows (the back is "inferred": ask the art director what is intended, RC §4).
4. Make the rigger's cuts: arm separated at the shoulder under the pauldron (natural cover), armpit bridge removed, socket/buried root, caps hidden; chest plate a separate rigid piece with clearance for the arm-overhead ROM (overlap depth from ROM, RP §2.3); head cut under the gorget; sword separate from the hand; hand/fingers rebuilt or one clean finger copied if fused (FM41). Counter-propose once before building if a better cut meets the same §B/§C rows.
5. Bend zones the rigger marks as R-skin (if any): rebuild loops across the bend (RP §2.4).
6. UVs per part and re-bake from the raw model (RP §2.10, FG06). Track triangles: 5,900 now; caps and sockets add some; stay under about 7,000 whole model (J007-D5).
7. C1-C5 numbers (watertight per part, triangles, connected parts vs plan, rest silhouette, caps hidden); one rest review set incl. back-left; hand to the rigger for the S4 proxy sweep with the arm overhead.

### 4. Must not
- More weight painting, or asking the rigger to paint again: the bridge is geometry (FG01).
- Close the crest gap or seat the plate with a global merge/fill: it creates a new fused bridge in a moving zone; no bridge mesh between parts (RP §2.6-2.7).
- Enlarge the pauldron or change armour shapes to hide a cut without the art director and owner (two options, RC §4).

### 5. Who else
- **Character-rigger**: the audit (bridge location, floating plate, weight finding on the chest plate), request for the S2 cut list; at S3 the C1-C5 evidence and any counter-proposal.
- **Animator**: confirm ROM with units for the overhead swing and head turn (needed for overlap depth).
- **Art director**: what the helmet back and crest connection should look like (inferred area).
- **Lead / owner**: route change (owner re-run or hand build) if repair costs more than rebuild.

---

## H4. Four props, four sizes, one on its side

### 1. Diagnosis (separate defects)
| # | Kind | Defect | Why |
| --- | --- | --- | --- |
| H4-a | runtime (scale chain) | Each prop imports at a different wrong ratio (0.66, 0.32, 3.6, 1.0): there is no single scale chain, so causes differ per file. The Blender panel reads metres, so the scene is not "Unit System None, 1 unit = 1 stud"; per-object unapplied scale is likely too. The importer then reads each file differently | EI §1; BR §2.2; C-03 (`Object.dimensions` is not the export number) |
| H4-b | runtime (axes) | Fence lies on its side: an unapplied object rotation or an axis conversion (Z-up vs Y-up) on that file | EI §3 (World Forward/Up), §5 row 1 |
| H4-c | runtime (pivot) | Lamp post rotates about a point ~1 m from its base: origin not at the base, or Set Pivot to Scene Origin with the object off origin | C-11; KE §2 (snap origin); EI §3 (pivot setting) |
| H4-d | construction / runtime | Barrel collision box extends past the visible mesh: the bounds include something invisible (stray vertices, an exported helper, faces culled because they face inward) | RV §2 clean export; C-10 (back-face culling); BU §6 |
| H4-e | process / data | Each placer typed a compensating multiplier in `spawn_props.luau`: the defect is hidden in logic, as numbers in code. Check: 1.5 × 0.66 ≈ 0.99, 3.1 × 0.32 ≈ 0.99, 0.28 × 3.6 ≈ 1.01: the multipliers exactly undo the import errors | AGENTS §2 (content is data); FM57 (fix placement data, not meshes, and vice versa: fix assets at source) |
| H4-f | process | No calibration round trip and no kit contract before a batch | EI §1; KE §2-3; FM66 |

Hypothesis to test, not a conclusion: the crate's 3.6 ≈ 1 / 0.28, the metres-per-stud reading (MR35), so one metre→stud conversion was applied to the crate that the plan did not expect (or the reverse).

### 2. First decisive check
1. Per `.blend` (read only, headless): `scene.unit_settings.system` and `scale_length`; each object's scale and rotation (applied or not); evaluated-mesh size in Blender units (BR §4, not the dimension panel); origin position relative to the mesh base; objects in the export set. Per `.glb`: node transforms. Expected: metric units; object scale ≠ 1 differing per file; fence with a 90° unapplied rotation or Y-up mismatch; lamp origin ~1 m above the base; barrel with a stray element outside the visible shell.
2. Predict each Studio ratio from those per-file factors; it must reproduce 0.66 / 0.32 / 3.6 / 1.0. A match proves the cause per file; a miss means another layer (export or importer setting).
3. Units of `layout_plan_heights.csv` (studs or metres) and the recorded game size factor (FM16). Unknown → needs-decision; never pick one.
4. In the test place (MCP, read only): `GetExtentsSize()`, pivot offset, orientation, and the barrel's collision vs visible bounds.

### 3. Fix order
1. Freeze; change nothing in Studio or the script yet.
2. Write the kit contract once (KE §2): 1 unit = 1 stud, forward/up axes, snap origin base-centre, collision role per prop; target heights in studs agreed with the environment designer (owner size factor if not recorded).
3. Calibration round trip: block of known size with a marked front + player dummy, kit FBX profile, import, measure (EI §1).
4. Per prop, one layer at a time (EI §5): units → apply rotation and scale → size in studs → origin at base centre (lamp) → fence upright with front marked → barrel export set cleaned to the visible mesh only.
5. Versioned export copies with `tools/rig/roblox_fbx.py` (`kind="rest"`); importer: Studs, Front/Top, Set Pivot to Scene Origin off where the origin matters (EI §3).
6. Import in the test place; measure size vs plan, pivot, orientation, collision (barrel: Box only if nobody stands on it, BU §6); MCP-verified.
7. Ticket (via lead) to the owner of `spawn_props.luau`: remove all four multipliers **in the same change** that swaps in the fixed assets; any intended scaling lives in data, not per-person constants.
8. Audit json per prop; one review render of the four next to the R15 dummy.

### 4. Must not
- Add another multiplier, or fix scale in Studio or code: it hides the asset defect and piles corrections.
- Ship the fixed assets while the multipliers are still active: double correction, as when an exporter fix and a place fix met (FM78).
- Stack a 0.01 export scale on a 0.01 unit scale, or edit `spawn_props.luau` myself (out of write scope).

### 5. Who else
- **Environment designer**: kit contract, target heights in studs, placement; confirms the plan's units.
- **Owner** (via lead): the size factor if it is not recorded (FM16).
- **Code owner** (feature-builder / quick-builder via a lead ticket): multiplier removal, timed with the asset swap.
- **Studio operator** or own MCP check: import parity numbers.

---

## H5. Crystal Golem: 75 % fewer triangles, ~1.6 ms gained

### 1. Diagnosis (separate defects)
| # | Kind | Defect | Why |
| --- | --- | --- | --- |
| H5-a | runtime (method) | The team cut triangles and texture without naming the bottleneck, and changed two things in one step. 372k → 93k triangles drawn moved the frame only 41.7 → 40.1 ms (24 → ~25 FPS): triangles are not the main cost | PF F-07 (name the bottleneck first), §3.4 (one change at a time); MR34 (FPS = 1000 / ms) |
| H5-b | runtime (draw calls) | 9 material slots: Roblox allows one material per mesh, so each golem imports as about 9 MeshParts → about 108 meshes for 12 golems before shadows; decimation does not change this | MR12, MR40; PF fixes (draw calls drop only with shared mesh and SurfaceAppearance) |
| H5-c | runtime (transparency) | 3 alpha-blended crystal shells × 12 = 36 overlapping transparent layers: overdraw, poor batching, possibly shadows from transparent parts | PF fixes ("transparency other than 0 or 1 overdraws"; CastShadow off on transparent parts) |
| H5-d | runtime (physics) | CollisionFidelity Precise (PreciseConvexDecomposition) on a moving boss ×12: "most CPU and memory" | PF fixes physics row; BU §6 |
| H5-e | budget | 31,000 triangles is over the 20,000 per-mesh ceiling (it passed only because it was split by materials) and far over the creature budget (under about 7,000, J007-D5); 7,750 is still over. Decimating a creature also damages bending limbs | MR01; BU §1 (never split only to pass the ceiling); C-07 |
| H5-f | identity | The glowing rune is identity-critical; shrinking the whole albedo 4096 → 256 (256 × fewer pixels) erased it | TM §2 (identity-critical forms get a unique painted area; glow = emissive mask); M-04 |

### 2. First decisive check
One capture on the same scene, same device class, with a fixed recipe (PF §3.3, F-07), by the performance engineer:
1. MicroProfiler frame colour and top scopes (blue/red = render or GPU wait; orange = scripts/physics/animation) (`measure.md`).
2. Stats: `RenderCPUFrameTime`, `RenderGPUFrameTime`, `SceneDrawcallCount`, `SceneTriangleCount`, `PhysicsStepTimeMs`; Scene Analysis by pass: Opaque vs Transparent vs Shadows (MR32-MR33).
3. Expected: draw calls roughly the same before and after decimation; a large Transparent and/or Shadows share; GPU wait or physics (`stepContacts`) dominating; triangle share small.
4. One-at-a-time A/B switches on the v1 asset: (a) crystal shells hidden; (b) collision Box/Hull instead of Precise (test only); (c) CastShadow off on shells; (d) one golem with a single merged material. The switch that moves the frame most names the bottleneck.
Studio numbers are not phone numbers: the phone verdict needs the phone (PF F-01, F-11; BU §7).

### 3. Fix order
1. Stop the decimate/shrink path; keep `golem_v1.blend` and the 4096 texture as the source; v2 is not the base.
2. Bottleneck capture (above); report the before → after table per switch.
3. Asset fixes the capture supports, smallest first:
   - Materials: one texture set; as few meshes as the rig plan allows (one per rigid part only where motion needs it), each with one material (MR12); upload once, duplicate 12× with identical SurfaceAppearance so copies can batch (MR24).
   - Crystal shells: opaque crystals with roughness/emissive, or transparency 0/1 only. This changes the look → two options at the arena camera to the art director and owner (RC §4).
   - Collision: a few Box/Hull proxy parts, or Hull, chosen for gameplay (does anyone stand on the golem?) (BU §6, PF fixes).
4. Triangles: rebuild toward the creature budget (under about 7,000, J007-D5): retopology on bending limbs, decimation only on static crystal clusters (C-07), triangles spent on the crystal silhouette.
5. Rune: give it texel density on purpose, or an emissive mask (red channel) + EmissiveTint (MR17, TM §1-2), or modelled relief; texture set to the plan (creature 1024², PROPOSAL, BU §4); check the rune reads at the arena camera.
6. Re-measure: same scene, same device, 3+ runs, before → after (PF §3.5). No phone, phone verdict `not verified`.
7. Raise the scene question: 12 bosses on screen at once is a design budget, not a modelling fix.

### 4. Must not
- Cut more triangles or texture before a capture names the bottleneck (F-07).
- Remove the crystal transparency or change the rune's look silently "for performance": never use an unmeasured performance claim to change the art (RC §4, HND06); after a measurement it is still two options for the owner.
- Claim a phone FPS gain from Studio numbers (F-01, F-11).

### 5. Who else
- **Performance engineer**: the capture recipe, the A/B switch list, the asset variants as switches; owns the bottleneck verdict.
- **Art director + owner**: crystal shell options and rune treatment at the same camera.
- **Character-rigger**: material/part merge changes the part list and pivots; agree it before S3.
- **Game designer / owner** (via lead): the 12-golem worst case as a scene budget.

---

## H6. Harvest Scarecrow: "from another game"

### 1. Diagnosis (separate defects)
| # | Kind | Defect | Why |
| --- | --- | --- | --- |
| H6-a | reference | The Tripo input was probably not made under the art bible's model lock with the approved anchors (Mossback Toad, Barrel Cart), or was never owner-approved. Image-to-3D follows the image; "stylized, cartoon" in a prompt cannot replace a matching reference, and the re-run confirmed this | RI I-01 (one style source), I-02 (anchors beat adjectives), I-03 (no style words in identity); M-06; FM07 (one shared lock for subjects of one world) |
| H6-b | identity (shape) | Shape language and proportion probably differ (e.g. thinner, more realistic proportions, fine wrinkles) from the approved assets | M-03, M-06; RV §2a (FM32, FM19) |
| H6-c | surface | Tripo textures: baked lighting, a realistic PBR set (albedo, roughness, normal at 2048) with high-frequency detail; the approved assets may use a different map set and palette | TM §5 (baked light; re-check palette against the art bible), FM47 (choose maps per kind) |
| H6-d | budget | 3 × 2048 maps exceed the texture plan (PROPOSAL 1024² for a character-size model, less for a prop) | BU §4; MR11 |
| H6-e | review | "Passes the gate, clean import" proves construction only; done needs the read at the game camera | MD §1 (three conditions); RV §2 identity row |

### 2. First decisive check
1. **Lineage**: the scarecrow's reference image id, its family and lock, attached anchors, and an owner decision line (RC §1, RI §4). Expected: missing, off-lock, or no anchors.
2. **Shape vs surface split**: clay renders (no texture, same neutral light) of scarecrow, toad and cart at the farm camera, next to the three textured `farm_cam_front.png`. If the scarecrow still looks foreign in clay → shape language; if clay matches and textured does not → surface.
3. **Numbers** with `look_check.py`: palette in CIELAB (ΔE2000 of the scarecrow's dominant colours to the art bible palette roles, and the same for toad and cart as control), value range, saturation. No approved tolerance → `measured`; the relative result (scarecrow's distance vs the approved assets' distance) is the evidence (R-03).
4. Map set and sizes of the approved toad and cart vs the scarecrow's three 2048 maps.

### 3. Fix order
1. Confirm the art bible has a model lock for this family; if not, the art director writes it and the owner approves (RI §1).
2. Make a new reference with `reference-images`: identity = subject only, anchors = the approved toad and cart (owner-approved anchors only, I-02), quality high or medium per I-13; review (I-05); owner approves.
3. If the split showed surface only: keep the mesh; re-texture: remove baked light, repaint/re-bake to the art bible palette roles and the material treatment of the approved assets, drop normal/roughness maps if the approved painted look does not use them, sizes to the plan.
4. If the split showed shape: route decision (RC §5). A scarecrow is mostly simple stylized masses, a hand-route candidate; or the owner re-runs Tripo from the new on-style reference (TF §1). Not a prompt-only re-run.
5. Blockout/compare at the farm camera with toad, cart and player dummy; audit; one review set; art-director review; owner G3.

### 4. Must not
- Re-run Tripo with more style adjectives: style lives in the art bible locks and anchors, not in prompt text (I-01, I-03).
- Recolour or tint everything "to fit" without the art director: palette roles are invariants.
- Call it done because the gate passed (MD §1).

### 5. Who else
- **Art director**: lock check for the family, the look_check numbers, the clay/textured split, anchor proposal; reviews the rebuilt result.
- **Owner** (via lead): approve the new reference; run Tripo if that route is chosen; G3.
- **Environment designer**: the farm-zone camera and light for the comparison renders, so all three are judged under the same light.

---

## Common pattern across the six cases
| Case | The tempting fix that was tried | Why it failed | The cause it hid |
| --- | --- | --- | --- |
| H1 | more fur triangles | surface before silhouette; wrong camera | identity at game size (maybe the design itself) |
| H2 | scale the head to fit the side | averages two views | inconsistent references; lineage; destructive clean-up |
| H3 | repaint weights twice | weights cannot remove geometry | fused bridge; armour on the wrong route |
| H4 | per-prop multipliers in code | compensation, not correction | no scale chain, no kit contract |
| H5 | decimate + shrink texture | not the bottleneck; two changes at once | draw calls / transparency / collision; budget |
| H6 | "make it cartoon" in the prompt | adjectives do not beat anchors | reference off the art bible lock |

In every case the first step is a measurement or comparison that separates causes, before any edit.
