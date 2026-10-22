---
name: modeling-design
description: What and why of a Roblox model (character, creature, pet, weapon, prop, vehicle, building) - read plan, silhouette and value at the game camera, identity anchors, reference check, hand vs Tripo, building for the rig, budgets. Use for "it doesn't look like the reference", "it doesn't read on phones", "too heavy for phones", "make it look great". Modeler reads first; modeling-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal (J007). Evidence: owner research paper notes `knowledge/reference/modeling/01-03-*.md` (MP:<line> = paper line), first-game experience `04-first-game-experience.md` (FM ids), fact-checks `fact-check-roblox.md` (MR), `fact-check-blender.md` (MB), `fact-check-tripo.md` (MT). Tags: [V] verified source, [E] experience, [O] studio opinion / policy. Owner decisions J007-D1..D7. Rebuilt by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the read plan, the silhouette and value gates, the core principles (§7).

# Modeling design: what to build, why, and how it must read

## 1. When this skill starts
When a model is briefed, planned or reviewed: what it must say at the game camera and in what order, what of the reference must match, the route, the split for motion, the cost, the checks. `modeling-craft` is how to build it in Blender and bring it into Roblox.

**A model is done only when three things hold** [O] (MP:7): it reads as the approved design at the game camera, at phone size, on its real ground, with the right things read first (silhouette and identity anchors, then value, then material, detail last); it moves the way the rig sheet needs; it stays inside its budget on phones. A good image, a good Tripo result, a beautiful close render or a clean upload proves none of these by itself.

**The camera rule** [O] (the game profile's play camera wins): by default third person behind and above, or top-down, on phones, usually free to orbit. Players see their own character's back, shoulders, head and held item most, and every other model small, from any side and above. Identity goes on the back, shoulders, head, top and the held item's side profile; every side the camera reaches is finished (skip one only when the camera is locked and the record says so); judge from the game camera, never a front beauty render alone.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The read plan, silhouette, value and form, colour and light, detail budget, design for motion, variants and tiers, grounding, worked examples | `references/read-and-form.md` |
| The asset record, the two image packages, checking a reference, iconic qualities and gaps, invariants vs negotiables, hand vs Tripo | `references/reference-check.md` |
| Ceilings vs budgets, the per-kind budget table, textures, reuse, collision, streaming, the detail budget by display size | `references/budgets.md` |
| Buildings, modular kits, environment pieces, props that sit in a place | `references/kits-and-environment.md` |
| The light-check review, the pass/fail list, the self-review before hand-back, what to do when a check fails, when it is done | `references/review.md` |
| Who decides cuts and joints; the rig sheet; the S3 brief | `rig-pipeline` skill, `rig-pipeline/references/modeler-handoff.md` |
| Why the rigger wants a cut or a bend zone | `rigging-design` skill (`references/region-routes.md`) |
| Making and approving the reference image | `reference-images` skill |
| How to build, clean, cut, texture, export, import, audit, measure the reads | `modeling-craft` skill |

## 3. Steps (from brief to an approved build)
Each step has a check; the next step starts only when it passes. Steps 7 and 8 are gates: no detail before the silhouette passes, no texture polish before the value pass and the art director's check-in.
1. **Open the asset record and write the read plan** (`templates/model/asset-record.md`; rows and a worked example: `references/read-and-form.md` §1): job in play, sell list, identity anchors, read order, viewing conditions (on-screen height on the smallest phone), detail spots, shape and value plan, palette roles, stop criteria. Missing decisions are listed, never invented. Check: no field blank (simple models: the four rows of `references/read-and-form.md` §1); unknowns say UNKNOWN; anchors agreed with the art director for any character, hero or variant family.
2. **Get the reference.** An approved image exists: attach it, never redraw it (owner 2026-10-21). Otherwise make one with `reference-images` (family per kind) and the art bible: front, side, back and the game-camera view. Check: image id + revision in the record.
3. **Check the reference and read its intent** before building (`references/reference-check.md` §3, §7): inventory, views agree, can exist, scale; the iconic qualities to keep, the gaps to decide (inside the art bible, or ask), material intent per region with its unlit local colour. Fail → repair from the anchor or ask; never average views. Check: every check passed or answered; iconic qualities and decided gaps in the record.
4. **Choose the route** (hand / Tripo) with the reason (`references/reference-check.md` §5). Tripo: set the budget (step 6) first, then write the input pack for the owner (J007-D4). Check: route and reason in the record.
5. **If it moves: join the rig pipeline and design for motion.** The animator says what moves, the rigger which parts are separate and where the cuts go; you make the cuts, seams and rebuilds and may counter-propose once (`rig-pipeline` §1, S3). Before the final model, check the design against the stress poses (`references/read-and-form.md` §6: mass off the joints, nothing over shoulders and arms, room for moving parts, fixed contact points); costly parts (capes, loose cloth, long hair, new chains) go to the rigger and art director with a cheaper fallback. Check: rig sheet path in the record; every costly part has a written reason or a fallback.
6. **Set the budget** (`references/budgets.md` §3, §8): owner number, game profile or PROPOSAL; texture, collision and reuse plans; detail budget by display size (detail only where the phone view shows it). Check: every number has a source or says PROPOSAL.
7. **Silhouette gate (blockout).** Big masses at player scale, flat colour per material region, proportions and anchors first; judge the black-fill at the game camera and phone size; design open → 2-3 distinct rough options at equal finish, one pick with the reason (`references/read-and-form.md` §2). Proportions are fixed here. Check: silhouette checks of `references/review.md` §5 pass; blockout revision frozen; deviations from the image listed.
8. **Value gate, then materials and detail in passes over the whole model.** Grey value check at the game camera (`references/read-and-form.md` §3), on the real ground once a Studio capture exists (else re-checked after import); one key light direction; then colour, material, detail and wear, each a pass over the whole model; the art director's check-in (game-camera captures on the real background) before texture polish. Check: value checks of `references/review.md` §5 pass before polish; check-in notes answered.
9. **Review with light checks** at each hand-off (`references/review.md` §1, §5). Check: numbers all pass; one review set; renders made and looked at counted; one honest weakness named.

## 4. Craft core: what separates great models from weak ones
| ID | Practice | Evidence |
| --- | --- | --- |
| M-01 | Judge at the game camera, phone size and real ground; what it is, whose, its facing and its source of power read first; zoom out every round → §7 P1, P2 | [E] (SG2, CS4-a); [O] RU02-RU03 |
| M-02 | Four layers in order: identity shape → value → surface under light → construction that moves; no part finished while the rest is blank → §7 P4 | [O] SG4 |
| M-03 | Black-fill and grey version work before materials; folds and bevels support the big masses, never noise → §7 P3, P5 | [E] (CS4-a); [O] CS4-b |
| M-04 | Detail where it reads: 1-3 detail spots on the upper shapes and focal zone, rest areas between; a triangle allowance is not a reason to use it → §7 P6 | [E] (CS3-a, CS5-b); [O] CS5-c |
| M-05 | Keep an object's operating principle (grip, load path, moving part, output direction) and functional parts (buttons, grips, pads, braces): a viewer sees how it is held and used | [E] (CS6-a); [O] CS6-b |
| M-06 | Shape language from the art bible and the subject's character, not habit (sharp danger, round friendly, square stable where the bible's world rules agree) → §7 P5 | [O] SY7 |
| M-07 | Painted edge, true bevel and normal-map edge are three tools; choose by silhouette, bending, camera and Roblox support; no universal bevel width: test at the game camera | [V] B04 (RU05); [O] CS4-d, SY9-SY10 |
| M-08 | A reusable base (body, kit piece); variety by controlled parts, tints and attachments; variants keep anchors, proportions, contact points → §7 P10 | [E] (CS1-a, CS10-a); [O] CS10-b |
| M-09 | Rigid pieces or one bending skin is chosen **per joint** with the rigger before final topology and UVs: pieces where a cover hides the cut or the part is hard; skin where the surface must look continuous; never cut a limb only because it moves | owner J005-D9; [O] RU07, RG-02, DNT05 |
| M-10 | A cut is hidden by design (collar, cuff, socket, overlap, panel line, an approved gap) and stays hidden through every pose the animator lists, not only at rest | [O] RG-09..RG-16; rig-pipeline S3 |
| M-11 | A Tripo result is a candidate: inspect it raw (clay, wireframe, underside, back, loose parts) before clean-up; reject wrong anatomy, fused grips, missing openings, false backs early; restore softened iconic shapes | [O] RU09, FW-04, TR-32 |
| M-12 | Remeshing, decimation, loose-part separation, semantic segmentation and quad output do not make a model ready to bend | [V] B07, B13 (RU06); [O] DNT04 |
| M-13 | Ceilings are not budgets: 20,000 triangles per mesh is the upload limit; creatures and characters stay under about 7,000; every other budget is a project choice or a measurement | [V] MR01; owner J007-D5; [O] RU14 |
| M-14 | Reuse on purpose: one uploaded mesh duplicated in Studio, tints for palette variants, kits from canonical pieces; an atlas or linked duplicate does not prove one draw call | [V] MR16, MR24; [O] RU12, DNT10 |
| M-15 | Collision is designed for gameplay, simple and predictable, not copied from the visual mesh; openings and walk paths stay open | [V] MR25; [O] BG-41 |
| M-16 | Lineage: approved image, route, Tripo model and settings, source .blend, export settings, asset ids; a later agent tells the shipped model from a rejected look-alike | [O] PRC22, RTC-4 |

## 5. Rules (final check)
- Every model starts from an approved ChatGPT reference; a subject with an approved image gets that image attached (owner 2026-10-21; `reference-images`).
- Invariants of the approved design never change silently; a needed change goes to the art director and the owner with two options at the same camera (`references/reference-check.md` §4).
- The modeler never decides joints, ROM or which parts the rig needs separate; it decides how the cut is built and may counter-propose once (rig-pipeline §1).
- Platform limits: ≤ 20,000 triangles per mesh; ≤ 4 influences per vertex; one material and one UV set per mesh; watertight where a closed surface is meant (MR01, MR06, MR12).
- No invented numbers: budgets, tolerances, texel densities, bevel widths and value bands are sourced, owner-set, PROPOSAL or UNKNOWN (paper RTC-5). Starting values in these books are PROPOSAL defaults a check may change.
- Checks are light: numbers for all, one review set per gate and hand-off as listed in `references/review.md` §1, more images only for a failing number (J005-D8, J007-D7). Black-fill, grey, phone-size and mirror views are measurements of that set, not new renders.
- No detail pass before the silhouette gate passes; no texture polish before the value gate and the art director's check-in.
- No franchise characters, logos or real brands in references or models (`reference-images` §6); designs stay non-sexualised for a young audience and respect a stated culture (`platform-policy` for sensitive or real-culture themes).

## 6. Self-check before a plan or review goes out
- [ ] Asset record complete: read plan, anchors, viewing conditions, stop criteria; unknowns marked; budget sourced.
- [ ] Approved reference attached and checked; iconic qualities, decided gaps and material intent listed; invariants listed.
- [ ] Route and reason recorded; Tripo input pack written if Tripo.
- [ ] Moving models: rig sheet linked; cuts and bend zones come from the rigger; costly parts flagged with a fallback.
- [ ] Silhouette and value gates passed before detail and polish; the self-review in `references/review.md` §5 run on the one review set; renders made and looked at counted; one honest weakness named.

Project overlay: if `knowledge/overlays/modeling-design.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's shared principles, stated for a model, each with an example and a check you run on your own review set (line ids: `references/review.md` §5; commands: `modeling-craft` §7; depth: `references/read-and-form.md`).

**P1 The gameplay read comes first; beauty never costs it.** The model's first job is to tell the player what it is, whose it is, what it does and how dangerous or valuable it is; style comes after. *Example:* a boss's weapon arm stays the biggest, brightest shape even when a cape would look grander. *Check:* your cold read (IM2): from the phone-size black-fill and grey views on the real ground, before the colour render, name what it is, its role and its threat in one glance; the receiver's cold read at the check-in matches it.

**P2 Judge it where players meet it.** Game camera, phone size, real ground, from every side the camera reaches, next to its roster neighbours; never approve from a turnaround or a close render alone. *Example:* a pet judged from 12 studs behind and above in the real hub, not from a front orthographic render. *Check:* the review set holds the back and front game-camera views and one Studio capture on the real ground with its mask capture (held items in the hand), each measured at phone size (IM1). A still proves one moment: the read in motion and in the busiest scene (effects and UI on) is judged by the rigger, animator and art director and goes on your could-not-check list.

**P3 Decide what is read first; spend contrast only there.** Rank the reads (silhouette anchor, focal zone, then the rest) and give contrast in that order; calm everything else first; pure white, pure black, the most saturated colour and glow only on small focal accents. *Example:* a knight's bright helmet and shoulder plates over a darker, cooler lower body. *Check:* VL2, VL4, CL7: `look_check.py value` with region masks cut from the black-fill (never boxes that hold background) gives the focal zone the widest luminance spread; the top-5 % images (value, and colour measured as chroma, not HSV saturation) mark only the named accents and the focal zone.

**P4 Big before small.** Silhouette and proportion, then value, then light, then colour, then material and detail, each pass over the whole model; no detail rescues a weak big read. *Example:* a house blockout with roofline, door height and footprint fixed before any shingles. *Check:* the blockout revision and its silhouette result are dated before the first detail pass; no region of a review render is clearly more finished than its equals.

**P5 Shape and silhouette carry identity and meaning.** A few big identifying shapes, broad cuts instead of notches, size steps (big, medium, small), the bible's shape language. *Example:* a sniper rifle's long barrel and oversized scope read in black-fill at 60 px tall. *Check:* SL1, SL2, SL8: subject, role and mood are nameable from the game-camera and phone-size black-fill; aligned IoU against the reference and the nearest roster neighbour (high overlap with a neighbour is a finding).

**P6 Less is more.** The fewest shapes, colours and parts that give the strongest read; detail clumped in 1-3 spots with rest areas; masses indicated with clumps and value blocks. *Example:* fox fur as five clumps with tapered shadow strokes, not strands. *Check:* palette cluster count within the bible's palette size; the detail-density image of the game-camera view (the model at its phone size) has its busy cells on the read plan's detail spots (DT10); features under about 4 px at phone size (starting value) removed or moved into texture (DT2).

**P7 One code for meaning across the game.** Team, faction, rarity and danger colours follow the bible and stay off decoration; materials that play differently look different. *Example:* the reserved enemy red never appears on a friendly vendor's awning. *Check:* CL1-CL2, GR4: the pixels within the bible's colour distance of each reserved swatch (as rendered) on the colour render, gameplay parts excluded, count zero (palette clusters merge a small accent and cannot show it); each gameplay material matches its role row.

**P8 Push what must read past real, on a believable base.** Hook shapes, signature items and heads bigger and sharper than life; anatomy, attachments and weight believable underneath. *Example:* a pirate's hat brim and cutlass pushed until they break the outline; straps and buckles still show how they hold on. *Check:* black-fill before and after the push: each pushed feature changes the outline at phone size (SL2); every attached piece shows how it is held on (DT4).

**P9 The subject's character drives every choice.** Write the character card (two tension words, how it moves) or a prop's 3-5 personality words first; every shape, proportion, material and wear mark traces to it. *Example:* a "rigid, old, timeless" shrine gets heavy square stone, chipped edges and sand half-burying its base. *Check:* RP2: each design choice traces to a card line; your cold read (IM2) gives back the card's words.

**P10 One world, one style; identity survives every variant.** Art-bible anchors over the maker's habit (an AI model's generic default is a habit); variants keep every identity anchor, base proportion and contact point. *Example:* a winter variant pet keeps its ear shape, tail curl and eye spacing; only coat and colours change. *Check:* beside 2-3 approved anchor models at the same camera it reads as one game; VA1 (`silhouette --compare` base vs variant, every anchor ticked).

**P11 Controlled variation, never exact repetition.** Slight bevel and shape variation, one asymmetric element, wear where hands go, no flat single-swatch fills, no visible tiling or identical mirrored marks. *Example:* a crate kit with two lid variants and painted wear only on the handles. *Check:* CL5 (on each material's lit face the hue spread over small blocks is above its flat limit; a value texture in one hue fails as monochrome); SL6 (the mirrored view differs visibly); DT5 (no mirrored text, cracks or tiling).

**P12 Problem, constraints and target before modelling.** The read plan, budgets, rig sheet, camera and contact points are read before the first vertex; deviations from the reference are said out loud. *Example:* a vehicle's seat height and wheelbase come from the player size and the rig sheet before the body is shaped. *Check:* RP1 and the budget rows dated before the blockout; every deviation listed with its reason (IM3).

**P13 Research, then distinct options, then a reasoned pick.** Real reference per material and mechanism, the game's own anchors first; when the design is open, 2-3 distinct rough options, one of them radical, picked with a reason; the first option is a warm-up. *Example:* three tower silhouettes (squat, tall-thin, top-heavy) blocked in grey before one is detailed. *Check:* SL9: options differ in black-fill, not only colour; the pick's reason ties to the read plan; none was polished before the pick.

**P14 Cheap stages first; gates freeze decisions; do not be precious.** Blockout in Studio next to the avatar before detail; after the silhouette gate, proportions do not move without a new decision; a section that misbehaves is rebuilt, not patched. *Example:* a Tripo body whose legs fused is rebuilt from one clean leg, not repaired face by face. *Check:* the record shows the blockout capture before detail and no proportion change after the gate without a decision line.

**P15 Critique against the goal, one named problem at a time.** Name the layer (silhouette, value, colour, material, detail, construction, motion, runtime), fix the worst first, re-check what the fix can break; refresh the eye with the mirror and grey views; ask for a paint-over when words are unclear. *Example:* "reads as a generic knight" is a silhouette problem (anchors too small), not a texture problem. *Check:* every fix in the hand-back names its layer and the re-run check; at least one honest weakness is listed.

**P16 Build for the next craft and the engine.** Ask the rigger, animator, VFX, UI and environment designer what they need before building; deliver cuts, loops, pivots, attach points, separable named parts, clean UVs, simple collision; reuse before making new; repeated steps become scripts. *Example:* a sword ships with a grip pivot and `BladeTip` and `BladeBase` attachments before VFX asks. *Check:* each receiver's packet answers its brief keys with zero open questions; budgets measured; reused assets named.

**P17 Know when it is done.** Stop criteria are written in the read plan: every material reads as itself at game size (gold reads gold), the finish matches the approved neighbours, nothing looks unfinished in one close render, budgets pass. *Example:* a prop stops when it reads at 40 px tall; the extra filigree pass is a follow-up, not a delay. *Check:* the hand-back shows each stop criterion passing and the passes used.

**P18 Look follows real rank.** A rarer, stronger or more valuable tier looks so by silhouette and finish; a cheaper item never wears the top tier's look. *Example:* a legendary pet gains a crest and a separable gloss trim; the common pet never gets the crest. *Check:* VA4: in the tier lineup at the game camera, silhouette size and finish count rise with real rank, in the design table's order.

**P19 Every player can read it.** Team, tier and state never ride on colour alone: shape, trim or an icon carries them too; the model still reads in grey. *Example:* red and blue teams differ by helmet crest shape as well as colour. *Check:* CL2: the grey game-camera view still tells every team, tier and role apart.
