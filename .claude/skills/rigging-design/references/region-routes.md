> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rigging-design`. Sources: rigging paper RP:166-211 (notes `knowledge/reference/rigging/01-*.md` §6), owner J005-D2, first-game FG01-FG13. Revised by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (material and style decide the route, separable parts, numbers at S4; repair round 2: cap sampling pointed to recipe 1; repair round 3: one cap group per cut).

# Region routes: cut, skin, mix or reject

Decide **per region**, not from the asset label: a robot can have soft cables, an animal can wear hard armour (RP:196 [O]).

## 1. Routes
| Route | What it is | Who works |
| --- | --- | --- |
| R-cut | Separate rigid piece, 100% on one bone or its own Motor6D part; the cut hides under a cover or in an overlap | rigger plans → modeler cuts, caps, builds socket |
| R-skin | Keep the surface continuous; rebuild the bend zone; localized weights | rigger names zone + protected regions → modeler rebuilds topology → rigger weights |
| R-mix | Soft body + rigid parts (armour, eyes, teeth, weapons, plates) | both |
| R-reject | Neither repair keeps the approved design within scope | rigger → lead → owner (regenerate or remodel) |

## 2. Studio rule: both methods, chosen per body part (owner J005-D9, 2026-10-21)
Neither method is the default for a whole character; most characters use both (R-mix). Decide each joint on its own:
| The joint has... | Use | Teddy example (J005 G2) |
| --- | --- | --- |
| a natural cover: collar, sleeve, cuff, bandage, glove, boot, belt, tuft, deep crease, armour edge | **R-cut** (separate piece, cut hidden under the cover) | head under the collar; paws and feet at the bandage edges; ears and tail in their creases |
| no cover, and the surface must look continuous while it bends (bare shoulder, hip, neck without a collar, soft body, tail, membrane) | **R-skin** (one surface that bends; needs rebuilt edge rings across the bend) | shoulders and hips: separate pieces showed a ball joint at big moves; bending looked better (owner chose it after renders) |
| hard or mechanical parts (gear, armour plates, weapons, doors) | **R-cut** | — |
| neither works in scope | **R-reject** → owner | — |
- First-game lesson [E]: skinned merged limbs webbed (FG01) and wrinkled (FG04) because the generated topology could not bend. R-skin works only when the bend zone is rebuilt with edge rings and the weights are tuned (teddy S3b/S4b: 0 visible folds in 77 poses after that).
- Elongated cut rings (one side much longer than the other, e.g. 1.8:1 shoulders) cannot be hidden by a rigid ball root at big moves: prefer R-skin there, or render both and let the owner pick.
- **What looks rigid moves rigidly; what looks soft bends** [O]: a gold plate, a spike or a gun body rides one bone; cloth, fur and skin bend. The material line written at S2 (`SKILL.md` §3 step 3) decides; when the reference leaves it open (shiny cloth or metal?), ask the art director before choosing.
- **The style decides how visible a break may be** [O]: a toy look in the art bible allows ball joints and gaps; a stylised organic character does not, so the same shoulder is R-cut on one game and R-skin on another.
- **Separable stays separable** [O]: every part that may be changed, recoloured, removed or swapped on its own (a helmet, a weapon, a pauldron, a variant piece) stays its own named object or MeshPart, joined to its bone, and is judged with the whole character.
- Paper conflict: the paper prefers skinning for plush or furry pets (DT03 below) [O]; the per-joint rule above decides. When unsure, render both as posed proxies at the worst §B pose from the gameplay camera; if both pass, pick the cheaper; if the choice changes the look, ask the owner.

## 3. Decision table (RP:198-211, [O] proposed studio rule)
| Model type or need | Cut | Skin | Mix and the deciding test |
| --- | --- | --- | --- |
| Retro toy humanoid with visible joint breaks | preferred if the silhouette allows sockets | optional for soft accessories | mix if clothing must bend; rotate every seam |
| Bare-skinned humanoid seen close | only at boundaries hidden on purpose | preferred: neck, shoulders, hips continuous | rigid eyes, teeth, gear; head isolation + reach tests |
| Plush or furry pet | only where fur or design hides a break | paper: preferred for body and neck (see §2 conflict) | rigid eyes / feet if the style fits; crouch + head turn |
| Low-detail pet at small screen size | often enough for bobbing body and head | when the bend reads at that size | decide by the game-camera silhouette, not the generator preview |
| Armoured humanoid or mechanical creature | rigid plates, pistons | soft body, cables, seals | mix preferred; clearance through extremes |
| Bird with rigid feather cards | rigid feather groups where useful | wing / body transitions, membranes | mix; fold and full extension without collapse |
| Snake or tentacle | articulated toy only | preferred bending chain | rigid end pieces if needed; opposite-curvature bends |
| Rifle, sword, reload mechanism | preferred: bolt, magazine, blade | flexible strap only | mix; full reload + grip-contact test |
| Vehicle with steering / suspension | preferred: wheels, doors, linkages | hoses, stylized suspension boots | mix; physics rig separate from the visual rig |
| Door, turret, machine, chest | preferred: hinge or rail | only for designed soft deformation | pivot, full travel, collisions, opening clearance |
| Fused limbs, unusable topology | cut and rebuild if breaks are allowed | retopologize if the surface must stay continuous | reject / regenerate if neither meets scope |
| Marketplace R15 avatar | the required separate body objects | skin inside each body part | Roblox template + validator; no shortcuts (RR06) |

## 4. Where cuts can hide (RP:172, 178 [O]; FG11 [E])
| Joint | Cover that can hide a cut |
| --- | --- |
| neck | collar, scarf, hair line, fur ruff; on a no-neck body: bury the head root in the body (no bridge mesh, FG02) |
| shoulder | sleeve, armour socket, buried ball root |
| elbow / knee | cuff, ball joint, kneecap piece |
| wrist / ankle | glove, boot |
| hip | pelvis shell, belt, skirt line |
| tail / ears / fins | tuft, crease, base ring |

- Overlap depth comes from the approved motion envelope, never a fixed fraction of limb size (RP:178).
- Coplanar surfaces flicker; too-deep overlaps clash visibly (RP:178).
- A deliberate, art-directed gap is valid (toy look).
- Ball-root geometry check (identity): a dome of radius r whose centre sits at depth d under a locally flat surface meets that surface in a circle of radius √(r² − d²); the limb's radius at the surface must stay inside that circle at every extreme (FG §3).
- A cap counts as hidden only if it stays hidden through every §B extreme from every review camera (RP:176).

## 5. What the rigger must check when the geometry comes back (S4)
- Rest silhouette and dimensions match the source; geometry fixes are logged apart from articulation changes (RP:182).
- Each rigid piece keeps its shape with its parent held still; unrelated pieces stay still; the seam stays covered from the required cameras (RP:182).
- No fused bridge left in a moving zone: connected-part count per piece matches the plan (`tools/rig/rig_audit.py`).
- Caps: normals out, 0 boundary edges, real thickness, no visible backfaces, texture continues across (RP:176).
- At every §B extreme, as numbers before any image (`rigging-craft/references/tests.md` §3, §6 G-lines): cap exposure 0 from every review camera, per cut, sampled over the whole of each face in that cut's `cap_<cut id>` group, a socket only where the child covers it (`rigging-craft/references/blender-mcp.md` §6 recipe 1; a failing number is checked on the still first); no new overlap between parts that are not parent and child; the game-camera black-fill keeps the rest component count.
