---
name: modeling-design
description: What and why of a Roblox model - characters, creatures, pets, weapons, props, vehicles, buildings; silhouette, scale, checking the ChatGPT reference, hand vs Tripo, building for the rigger, triangle budgets. Use for "it doesn't look like the reference", "it's too heavy for phones", "make it look really good", "the pieces don't fit". Modeler reads first; modeling-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal (J007). Evidence: owner research paper notes `knowledge/reference/modeling/01-03-*.md` (MP:<line> = paper line), first-game experience `04-first-game-experience.md` (FM ids), fact-checks `fact-check-roblox.md` (MR), `fact-check-blender.md` (MB), `fact-check-tripo.md` (MT). Tags: [V] verified source, [E] experience, [O] studio opinion / policy. Owner decisions J007-D1..D7.

# Modeling design: what to build, why, and how much it may cost

## 1. When this skill starts
When a model is briefed, planned or reviewed. It answers: what the model must show at the game camera, which parts of the reference must match, which route builds it, how it is split for motion, what it may cost, and how it is checked. `modeling-craft` answers how to build it in Blender and bring it into Roblox.

**A model is done only when three things hold** [O] (MP:7): it reads as the approved design at the game camera; it moves the way the rig sheet needs; it stays inside its budget on phones. A good image, a good Tripo result or a clean upload proves none of these by itself.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The asset record, the two image packages, checking a reference, invariants vs negotiables, hand vs Tripo | `references/reference-check.md` |
| Ceilings vs budgets, the per-kind budget table, textures, reuse, collision, streaming | `references/budgets.md` |
| Buildings, modular kits, environment pieces | `references/kits-and-environment.md` |
| The light-check review, the pass/fail list, what to do when a check fails | `references/review.md` |
| Who decides cuts and joints; the rig sheet; the S3 brief | `rig-pipeline` skill, `rig-pipeline/references/modeler-handoff.md` |
| Why the rigger wants a cut or a bend zone | `rigging-design` skill (`references/region-routes.md`) |
| Making and approving the reference image | `reference-images` skill |
| How to build, clean, cut, texture, export, import, audit | `modeling-craft` skill |

## 3. Steps (from brief to an approved build plan)
1. **Open the asset record** (`templates/model/asset-record.md`): kind, role, camera, size against the player, motion, attach points, collision, budget with source. Missing decisions are listed, never invented. Check: no field left blank; unknowns say UNKNOWN.
2. **Get the reference.** If the subject already has an approved image, attach it; never redraw an approved design (owner 2026-10-21). Otherwise make one with `reference-images` (family per kind) and the game's art bible. Check: image id + revision in the record.
3. **Check the reference before building** (`references/reference-check.md` §3). Fail → repair from the anchor or ask; never average views. Check: every check passed or answered.
4. **Choose the route** (hand / Tripo) with the reason (`references/reference-check.md` §5). Tripo: write the input pack for the owner (J007-D4). Check: route and reason in the record.
5. **If it moves: join the rig pipeline.** The animator says what moves, the rigger says which parts are separate and where the cuts go; the modeler makes the cuts, seams and rebuilds, and may counter-propose once (`rig-pipeline` §1, S3). Check: rig sheet path in the record.
6. **Set the budget** (`references/budgets.md` §3): owner number, game profile, or PROPOSAL; texture plan; collision plan; reuse plan. Check: every number has a source or says PROPOSAL.
7. **Blockout, then approve the big shapes** before detail (`references/reference-check.md` §6). Check: blockout revision frozen; deviations from the image listed.
8. **Review with light checks** at each hand-off (`references/review.md`). Check: numbers all pass; one review render set.

## 4. Craft core: what separates great models from weak ones
| ID | Practice | Evidence |
| --- | --- | --- |
| M-01 | Judge a model at its game camera and size, not as a close beauty render: the read (silhouette, facing, the source of its power or use) comes first, surface detail last | [E] Riot, Valve (SG2, CS4-a); [O] RU02-RU03 |
| M-02 | Three layers, in this order: identity-bearing shape → surface that reads under light → construction that can move | [O] SG4 |
| M-03 | Make the flat-colour or grey silhouette work before materials; folds and bevels support the big masses instead of adding noise everywhere | [E] TF2 (CS4-a); [O] CS4-b |
| M-04 | Spend detail where it reads: prominent upper shapes for distance, small detail only where the camera gets close; a weapon's triangle allowance is not a reason to use it | [E] Overwatch (CS3-a), Dota (CS5-b); [O] CS5-c |
| M-05 | Keep the operating principle of an object (grip, load path, moving part, output direction), not only its surface | [E] Splatoon 3 (CS6-a); [O] CS6-b |
| M-06 | Shape language comes from the art bible and the world's rules, not from "round = good, sharp = evil" | [O] SY7 |
| M-07 | A sharp painted edge, a true bevel and a normal-map edge are three different tools; choose by silhouette, bending, camera and what Roblox supports. No universal bevel width exists: test it | [V] B04 (RU05); [O] CS4-d, SY9-SY10 |
| M-08 | Build a reusable base (body, kit piece) and make variety by controlled parts, tints and attachments | [E] Riot base mesh (CS1-a), Sable (CS10-a); [O] CS10-b |
| M-09 | Rigid pieces or one bending skin is chosen **per joint** with the rigger, before final topology and UVs: pieces where a natural cover hides the cut or the part is hard; skin where the surface must look continuous. Never cut every moving limb just because it moves | owner J005-D9; [O] RU07, RG-02, DNT05 |
| M-10 | A cut is hidden by design (collar, cuff, socket, overlap, panel line, an approved gap) and stays hidden through every pose the animator lists, not only at rest | [O] RG-09..RG-16; rig-pipeline S3 |
| M-11 | A Tripo result is a candidate: inspect it raw (clay, wireframe, underside, back, loose parts) before any clean-up work; reject wrong anatomy, fused grips, missing openings, false backs early | [O] RU09, FW-04, TR-32 |
| M-12 | Remeshing, decimation, loose-part separation, semantic segmentation and quad output do not make a model ready to bend | [V] B07, B13 (RU06); [O] DNT04 |
| M-13 | Ceilings are not budgets: 20,000 triangles per mesh is the upload limit; creatures and characters stay under about 7,000; every other budget is a project choice or a measurement | [V] MR01; owner J007-D5; [O] RU14 |
| M-14 | Reuse on purpose: one uploaded mesh duplicated in Studio, tints for palette variants, kits from canonical pieces; an atlas or a Blender linked duplicate does not prove one draw call | [V] MR16, MR24; [O] RU12, DNT10 |
| M-15 | Collision is designed for gameplay, not copied from the visual mesh; openings and walk paths stay open | [V] MR25; [O] BG-41 |
| M-16 | Keep lineage: approved image, route, Tripo model and settings, source .blend, export settings, Roblox asset ids; a later agent must tell the shipped model from a rejected look-alike | [O] PRC22, RTC-4 |

## 5. Rules (final check)
- Every model starts from an approved ChatGPT reference; a subject with an approved image gets that image attached (owner 2026-10-21; `reference-images`).
- Invariants of the approved design never change silently; a needed change goes to the art director and the owner with two options (`references/reference-check.md` §4).
- The modeler never decides joints, ROM or which parts the rig needs separate; it decides how the cut is built and may counter-propose once (rig-pipeline §1).
- Platform limits: ≤ 20,000 triangles per mesh; ≤ 4 influences per vertex; one material and one UV set per mesh; watertight where a closed surface is meant (MR01, MR06, MR12).
- No invented numbers: budgets, tolerances, texel densities and bevel widths are sourced, owner-set, PROPOSAL or UNKNOWN (paper RTC-5).
- Checks are light: numbers for all, one review render set per hand-off, more images only for a failing number (J005-D8, J007-D7).
- No franchise characters, logos or real brands in references or models (`reference-images` §6).

## 6. Self-check before a plan or review goes out
- [ ] Asset record complete; unknowns marked; budget sourced.
- [ ] Approved reference attached and checked; invariants listed.
- [ ] Route and reason recorded; Tripo input pack written if Tripo.
- [ ] Moving models: rig sheet linked; cuts and bend zones come from the rigger.
- [ ] Review used numbers first; renders counted in the hand-back.

Project overlay: if `knowledge/overlays/modeling-design.md` exists, read it after this file; it wins for this game.
