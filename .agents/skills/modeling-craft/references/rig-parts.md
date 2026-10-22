> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. The workflow and the brief you receive: `rig-pipeline` (S3) and `rig-pipeline/references/modeler-handoff.md`, adopted as-is. Why a cut is where it is: `rigging-design/references/region-routes.md`. Evidence: rigging first-game rows FG01-FG14, J005 G2 gaps GP07-GP10, paper notes `02-*.md` §10 (RG ids), first-game FM ids. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): design for motion at S3 (§6).

# S3: making the rigger's cuts, caps and bend zones

## 1. What you decide and what you do not (rig-pipeline §1)
| You decide | You do not decide |
| --- | --- |
| how each cut is made, capped, socketed or overlapped; where loops go in a bend zone; UVs and re-bake; counter-proposals | which parts are separate, where cuts go, joints, pivots, ROM, weights |

A counter-proposal names the rig sheet §B/§C rows it still meets, goes to the rigger **before** you build it, one round; disagreement after that goes to the lead. Settle a disagreement with a posed proxy render of both options, not argument.

## 2. Steps
1. **Read** the rig sheet (§B needs, §C route, cut and deformation zone per part), the rigger's plan renders, the approved reference, the asset record. Work on a **copy**; the source snapshot is never edited.
2. **Inventory the working copy** (`tools/model/model_audit.py`): connected parts, open edges, triangles per part. One object is not one connected surface (rule 06): a sleeve that looks separate may be welded to the torso.
3. **For each R-cut part**: cut along the planned line (Bisect with Fill only where the cap is hidden; MB rows), separate by selection (Separate by Loose Parts only splits geometry that is already disconnected, RG-04 [V] B13), then build the hidden join:
   - **socket / overlap**: a rounded root dome on the child buried in a socket of the parent; the visible join is an intersection line in a natural crease, tuft or collar (FG11);
   - **cover**: collar, cuff, glove, boot, belt, armour plate, panel line (region-routes §4);
   - **art-directed gap** only if the art bible allows it (toy look).
   Overlap depth comes from the animator's ROM, never a fixed fraction of the limb (RP:178).
4. **For each R-skin zone**: rebuild topology so the bend has enough loops across it (shoulder, hip, elbow, knee, neck, tail base), poles and long thin triangles away from the bend, protected regions left still (RG-03 [O]). No fixed loop count exists; test the real extremes.
5. **Caps and roots**: normals out, 0 open edges, real thickness, no visible backfaces; **exposed roots and sockets carry the skin's texture and shading continuously, rims rounded, never a flat swatch or a knife-edge ring** (GP07).
6. **Close open shells with tuck-and-cap**: tuck the open rim inward to the first inner surface, then cap. Never delete faces to close a shell: it opened holes (FG05). Never pass every open edge to a hole-fill: an intended open cloth edge is not a hole (REV07).
7. **Never add a bridge mesh** between a separated head and a no-neck body: it creased. Bury the head root in the body instead (FG02).
8. **Repeated limbs fused together** (Tripo legs, arms): build one clean limb and copy it, rather than cutting each fused one apart (FM41, owner, first game).
9. **Joint covers centred on pivots** where a moving limb holds a prop, so the limb does not leave the body when it turns (FM38).
10. **UVs and textures per part**: each cut part gets its own UVs and a re-bake from the raw model; one shared atlas across cut parts failed (FG06). See `references/textures-materials.md`.
11. **Self-check (numbers only, rig-pipeline §4a)** and the one rest review set. Fill only the §D modeler keys. Hand back to the rigger (`references/handoffs.md`).
12. **After any geometry fix** (a fix note, a retopology, a re-cut): list which §B poses the change touches and ask the rigger to re-run the S4 sweep through **every** required pose, then the S5 tests in Blender and Studio; a fix is not done until those pass. Weights never hide a fused bridge: if repainting weights did not stop a stretch, the cause is geometry (FG01, J007 hidden test).

## 3. Checks you hand back (modeler-handoff C1-C5, unchanged)
| Check | How |
| --- | --- |
| C1 every listed part watertight (0 non-manifold edges) | audit json |
| C2 triangles per mesh ≤ 20,000 and within the project budget | audit json; budget source |
| C3 no fused bridge in a moving zone (connected-part count per part matches the plan) | audit json |
| C4 rest silhouette matches the reference in the review views | the one review render set |
| C5 every cap and socket hidden at rest from the review views | the same set |
| Check budget: self-check is numbers; images only where a number fails plus the rest views; the rigger does the full sweep at S4 | count renders in the hand-back |

## 4. Where the files go (GP09)
Scripts, renders and part files only inside `content/rigs/<asset-id>/geometry/` (or the path the brief names). Never write renders outside the asset folder.

## 5. Parts the animation needs, by kind (RG-09..RG-16 [O]; the rigger's sheet wins)
| Kind | Usually separate | Usually one bending skin | Seam cover |
| --- | --- | --- | --- |
| Organic humanoid | jaw, eyes, held tools | body, neck, shoulders | collar, sleeve, or continuous skin |
| Toy / blocky humanoid | head, torso, limb segments | — | ball and socket, cuff, approved gap |
| Quadruped pet | eyes, sometimes ears, tail | body, legs at shoulder and hip | fur clumps, continuous skin |
| Winged creature | rigid feather groups | membrane, wing roots | overlapping feathers; no random membrane cuts |
| Weapon or tool | trigger, bolt, magazine, blade, hinge | strap | housings, rails, sleeves; grip stays constant |
| Vehicle | wheels, steering, doors, turret | soft boots, hoses | fenders, bearings, panel gaps |
| Building or prop | doors, drawers, levers, break chunks | — | frames, reveals, trims |
| Cape, tail, tentacle | — | the whole chain | enough cross-sections for both bend directions |

## 6. Design for motion while you build (checked again by the rigger's S4 sweep)
The standards (mass off the joints, nothing over the arms, costly parts, model what the rig moves, moving parts with room, contact points, hook shapes) live in `modeling-design/references/read-and-form.md` §6. What S3 adds:
| Standard | How at S3 | Check |
| --- | --- | --- |
| Mass off the joints | read the rigger's plan renders: any static mass inside a marked deformation zone or across a cut (collar edges, scarves, armour rims, static hair) is moved, bundled or raised with the rigger; hair is bundled into one unit away from the nape | `modeling-design/references/review.md` §5 MO1 |
| Nothing over the arms | the rest views show the arm outline clear of drapes, cowls and capes | MO2 |
| Costly parts flagged early | sent to the rigger at the blockout with a reason and a rigid or bundled fallback, before they are modelled | MO3 |
| Model what the rig moves | circular loops around the mouth so it can open and fold, eyelids with enough lines to close (`knowledge/external/roblox-creator-docs/art/characters/creating/modeling-best-practices.md` mouth and eye rows); never a mouth sewn shut | a test pose with the mouth open and eyes closed on the proxy rig shows no tear (the rigger's sweep) |
| Shared bodies | a new skin is overlaid on the base mesh and armature in Blender, so joints and fingers stay where the shared clips expect them | joint offsets against the base within the rig sheet's tolerance (MO4) |
| Moving parts with room | separate named objects with pivots and nesting cross-sections that travel without hitting the arms or body | MO4; the animator's inspect or use clip in the rigger's sweep |
| Contact points fixed | grip, seat and hand positions measured against the base in every variant | MO5 (numbers in studs) |
| Signature shape on the held moments | the hook shape (a ponytail swoop, a cape tip, a weapon fin) is built so it can face the camera in the animator's key poses | MO6 on the rigger's posed captures, when they exist |
