---
name: rigging-design
description: Decide how a Roblox character, creature, pet, weapon, vehicle or moving prop should be rigged before anyone builds it - what makes a game rig great, rigid separate parts vs skinning vs a mix per body region, where joints and pivots go, which parts must be separate pieces and where the cuts go and why, how a seam stays hidden through every pose, what the animation needs from the rig (active vs passive tails, wings, ears, extra legs, held tools, contacts, faces), Tripo merged meshes (when Tripo's segmentation or auto-rig is good enough and when the work is done by hand), Roblox runtime choices (Bone vs Motor6D, Humanoid vs AnimationController, avatar R15 vs custom) and diagnosing a broken rig ("the body skews when the head turns", "the arm wrinkles", "the seam shows"). Use at S2 of rig-pipeline, when reviewing a rig plan or a broken rig, and when the animator or modeler needs to know why a cut or joint is where it is. Read by character-rigger first; animator and modeler read it for the reasons. Pair with rigging-craft for the build.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Evidence: rigging paper notes `knowledge/reference/rigging/01-*.md`, `02-*.md` (RP:<line> = paper line), animation paper notes `knowledge/reference/animation/01-*.md` (AP:<line>), fact-checks `knowledge/reference/rigging/fact-check-*.md` (RR = Roblox, RB = Blender, RT = tools), first-game experience `03-first-game-experience.md` (FG ids). Tags: [V] verified source, [E] experience, [O] studio opinion / policy.

# Rigging design: what to rig, why, and where the cuts go

## 1. When this skill starts
At rig-pipeline S2, with the animator's §B needs and the model in hand. It answers: which route per region, where joints and pivots go, which parts must be separate and why, what each cut must hide through, what the rig must let the animator do, and what is tested before release. `rigging-craft` answers how to build and test it in Blender and Roblox.

**Governing principle [O] (RP:12):** keep the approved silhouette and contacts across the approved motion envelope with the simplest exportable articulation that passes the in-engine tests. A generated mesh, auto segmentation, auto weights or a clean import is a candidate, never an acceptance.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The full region route table (asset type → cut / skin / mix, deciding test) and seam-hiding options | `references/region-routes.md` |
| What motion asks of a rig, part by part (tails, wings, ears, legs, tools, faces, secondary) | `references/motion-needs.md` |
| Non-humans, pets, mechanisms, vehicles, weapons, faces | `references/creatures-mechanisms-faces.md` |
| A broken rig: symptom → cause → decisive check | `references/diagnosis.md` |
| Tripo tools, versions and routes | `rig-pipeline` → `references/tripo-routes.md` |
| Build, weights, controls, export, tests | `rigging-craft` skill |

## 3. Steps (S2: from needs to a rig plan)
1. **Classify the asset** [O] (RP:87): platform avatar body (R15 contract, Roblox template and validator are the authority) / in-experience custom player / NPC / pet / weapon / vehicle / prop. Renaming bones does not make a custom creature an R15 avatar. Check: §A purpose filled.
2. **Read the needs.** Every §B record: driver (active / passive / rigid / mechanical), ROM with unit and the pose that needs it, contacts, own-motion parts, stress poses, sockets. Missing or unsourced → K1 fails, ask the animator. Check: K1 recorded.
3. **Inspect the geometry before deciding** [O] (RP:168): objects, mesh data, connected parts, open edges, intersecting shells, UV islands, materials, floating bits, triangles. One object is not one connected surface; one visibly separate sleeve can be welded to the torso (rule 06). Note where painted texture fakes structure (a drawn mouth has no mouth cavity, RP:327). Check: defect map with views.
4. **Pick a route per region, not per asset** (§4 and `references/region-routes.md`): R-cut, R-skin, R-mix or R-reject, with the reason that names the §B need and the geometry fact. Check: every moving region has a pivot or a deformation plan.
5. **Place joints from landmarks and the needed rotations** [O] (RP:38, 115), never at a bounding-box centre. Head pivot at the neck base, not the skull centre (RP:524). Record pivot coordinates and space, axes, ROM limits from §B. Check: rotation preview of each joint looks right from side and front.
6. **Write the cut list** for R-cut parts: where, why (which need), what hides it (collar, sleeve, cuff, glove, tuft, crease, socket, overlap, or an art-directed gap), and the extremes it must stay hidden through. Write **bend zones** for R-skin parts: which loops are needed where, which regions are protected (must not move). Mark both on renders for the modeler. Check: every cut and zone ties to a §B row.
7. **Set budgets with sources** (rig-pipeline §6): platform limits fixed; everything else a game budget or PROPOSAL until measured on the target phone. Check: §E has no number without a source.
8. **Answer every §B record** (supported / with limit / not supported + alternatives) and send the plan to the animator for K2. A limit that changes the look goes to the owner. Then brief the modeler (`rig-pipeline/references/modeler-handoff.md`).

## 4. Craft core: what separates great rigs from weak ones
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | Judge a rig in motion, not in the bind pose: shoulders keep mass, elbows bend without imploding, hips allow locomotion and crouch, a neck turn does not drag the chest, rigid gear keeps its shape | [O] RP:36 |
| D-02 | Controls are judged by reset, local axes, IK/FK continuity, space switching and contact holding, not by control count; complexity is only worth it if it makes the needed poses easier | [O] RP:36, 12 |
| D-03 | Animation intent changes rig features: prototype a requested motion on a minimal chain, add only the controls it needs, bake secondary motion onto export joints when it must play identically | [V] Riot Fiddlesticks (RP:42); [O] transfer RP:44 |
| D-04 | Route per joint, both methods in one character: rigid separate pieces where a cover hides the cut or the part is hard; skinning where there is no cover and the surface must bend continuously | [O] rule 05, RP:196; owner J005-D9 |
| D-05 | Rigid piece = 100% weight on one bone (or its own Motor6D part); a skinned region gets localized weights; a rigid element can be its own MeshPart (physics, removal, damage) or geometry weighted fully to one bone (visual only) | [O] RP:79, 269 |
| D-06 | Fix topology and joint placement before weights. Weights cannot repair a fused bridge, a wrong pivot or a wrong parent | [O] rule 08, RP:186, 275; [E] FG01 |
| D-07 | Hide a rigid cut with overlap, socket, collar, sleeve or an approved gap, sized from the motion envelope (not a fixed fraction of limb size); then sweep every extreme from the review cameras | [O] rule 07, RP:178; [E] FG11 |
| D-08 | A flat cut across exposed organic skin is a design change, not an invisible repair: either a cover exists, or the region is skinned, or the owner approves a visible break | [O] RP:172 |
| D-09 | Protected regions: name the vertices that must stay still in a head-only or hand-only test; measure their largest move. A smooth gradient can still be wrong; a tiny remote weight moves the mesh | [O] RP:273 |
| D-10 | Combined stress poses, not single-axis sweeps: arm raised + forearm twist, head turn + torso bend, hip flex + leg spread, tail curve + base rotation | [O] RP:285 |
| D-11 | The Roblox result is authoritative. Blender-only deformers (Preserve Volume, drivers, corrective shape keys, IK, spline constraints) do not run in Roblox; bake to supported bones and weights, or treat as film-only | [V] FBX does not carry constraints (RB fact-check); [O] RP:281; [E] FG12 |
| D-12 | Separate visual articulation from physics: bone motion moves the picture, not the collision shape; give physics its own proxies; never drive one degree of freedom from physics, Animator and a script at once without an owner | [V] RR12; [O] RP:310, do-not 18 |
| D-13 | Freeze the motion envelope and asset role before final skinning; later topology, joint, name or rest-pose changes are a versioned migration with retests | [O] RP:119 |
| D-14 | Spend articulation where it reads at the game camera: a small pet may need only a bobbing body and a turning head; choose by camera test and measured crowd cost, not a universal bone count | [O] RP:298, 203 |
| D-15 | A missing number is a result, not a gap to fill: no invented bone cap, joint angle, loop count, tolerance or phone budget | [O] do-not 4; [V] RR31 (no documented custom-rig cap found 2026-10-21) |

## 5. What the animation needs from the rig (summary; detail `references/motion-needs.md`)
| Need from §B | Rig consequence |
| --- | --- |
| Active appendage (balancing or steering tail, gripping tail, pointing ears) | Controls that drive it as a primary part while the body responds; no "always lags" setup [V] gecko tails B05 (AP:228) |
| Passive appendage (strap, floppy ear, tail tip) | Chain with enough segments and geometry to bend both ways from a neutral rest; key, procedural or hybrid decided per part [O] RP:300, AP:508 |
| Wings | Name the type first (feathered, membranous, insect: different systems); wing, body and tail controllable together; left and right retract independently; fold and glide reachable without intersecting the body [V] B06-B10 (AP:234-240) |
| Extra legs | Explicit leg order, side convention, ground-contact map, no cross-limb IK target mix-ups; stance feet must hold in world space [O] RP:304; AP:250 |
| Held tool | Tool root, grip anchors (primary, secondary), impact surface, stable grip / muzzle frames; hand switching and reload detachment are hierarchy changes, not skin gradients [O] RP:306; AP:316-330 |
| Contacts (feet, hands, perch, hinge) | Pivots that allow planted, rolling and sliding states; contact-hold test after export [O] RP:441; AP:209 |
| Face | Texture swap, skeletal face or mix chosen from shot size and needed transitions; dynamic heads follow the FACS mapping [V] RR15-RR17, < 50 face joints where possible RR34 |
| Squash and stretch, smears | Only what the rig and asset contract allow; check after export [O] AP:383 |

## 6. Roblox runtime choices
| Choice | Use when | Evidence |
| --- | --- | --- |
| Skinned mesh with Bones | continuous bending surfaces; many visual joints without a part per bone | [V] RR11-RR12; [O] AP:829 |
| Separate MeshParts + Motor6D | rigid mechanical pieces, detachable or physical parts, doors, turrets, weapons | [V] Motor6D joins two parts animatably (RP:73); [O] RP:75 |
| Humanoid + Animator | player characters and NPCs that need Humanoid behaviour | [V] RR13, RR21 |
| AnimationController + Animator | creatures, pets, props without Humanoid needs; cheaper for static NPCs | [V] RR13 (use `Animator:LoadAnimation`, the controller's own method is deprecated); [V] Roblox Improve Performance (RP:772) |
| Avatar R15 / advanced R15 | only for platform avatar bodies: 15 named meshes, +Z forward, +Y up, I/A/T pose, own triangle budgets, up to 37 optional joints | [V] RR02, RR06, RR07 |
| Choose by measured A/B on the target phone, not folklore that bones or Motor6Ds are always cheaper | [O] AP:829; [E] forum reports only |

## 7. Rules (final check)
- Max 4 influences per vertex; no weights on Root; ≤ 20,000 triangles per mesh; watertight (RR01-RR05).
- Never rely on a Blender-only deformer for anything that plays in Roblox (D-11).
- Never smooth weights globally to hide a wrong joint, wrong parent or fused topology (do-not 5).
- Never assume Separate by Loose Parts can split connected geometry (do-not 6).
- Never treat a semantic segment label or an auto-rig success as a finished joint (do-not 8, rule 12).
- Never move a pivot to hide a bad cut boundary (RP:524).
- Never invent a cap, angle, loop count, tolerance or budget; mark UNKNOWN and measure (D-15).
- A look change forced by a technical limit goes to the owner with both options rendered (rig-pipeline §1).

## 8. Self-check before sending the plan (K2)
- [ ] Asset classified; runtime driver and movement owner stated.
- [ ] Every §B record answered; every "with limit" says the limit in units.
- [ ] Every moving region has a route with a reason tied to a need and a geometry fact.
- [ ] Every pivot has coordinates and space; head and limb pivots at articulation centres.
- [ ] Every cut says where, why, what hides it, and the extremes it must survive; every bend zone names its protected regions.
- [ ] Budgets sourced; no invented numbers.
- [ ] Cut and zone renders attached for the modeler.

Project overlay: if `knowledge/overlays/rigging-design.md` exists, read it after this file; it wins for this game.
