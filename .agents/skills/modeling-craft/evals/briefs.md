> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Eval briefs for the modeler (modeling-design + modeling-craft + rig-pipeline S3)

Give the agent the brief text and the named files only. A separate grader (Sonnet, high, J007-D6) grades each check pass/fail from the agent's files, not its summary. A brief passes at ≥ 80% of its checks with no "must" check failed. Common checks apply to every run. Hidden cases (held out of the skills): `knowledge/jobs/J007-modeler/hidden-cases.md`.

| ID | Common check |
| --- | --- |
| M1 (must) | Starts from an approved reference: attaches the existing approved image, or makes one with `reference-images` and checks it (inventory, views agree, can exist, scale) before any geometry |
| M2 (must) | No invented numbers: every budget, size, tolerance and texture size has a source (owner, game profile, platform doc, measurement) or says PROPOSAL / UNKNOWN; 20,000 triangles is called the upload ceiling, never the target; creatures and characters under about 7,000 (J007-D5) |
| M3 (must) | Light checks: audit numbers for every check; one review render set; extra images only for a failing number; renders made / looked at reported |
| M4 (must) | Role boundaries: no rigging, weights, animation or level placement; cuts come from the rigger's sheet; a counter-proposal names the rig rows it meets and goes back before building; a look change goes to art director / owner with two options |
| M5 | Asset record filled (route and reason, budget source, invariants, results with labels, lineage) |
| M6 (must, when exporting) | Export through `tools/rig/roblox_fbx.py` (or every option named); one scale recipe; import measured in a test place, never the live place; nothing uploaded without the owner's yes |
| M7 | Hand-back in `rules/messages.md` §3 shape: STATUS first, coverage per item, evidence labels |

## 1. Simple held weapon, hand-built (medium effort; G2 test A)
> A one-handed sword for a stylized adventure game, held by the player and seen in third person at ~15 studs; also shown as an inventory icon. Trail effect from the blade tip during swings. Art bible: `templates/skill/art-bible.md` starter locks. Build it.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Route = hand modeling, with a reason; reference made in the `prop` family (single clean view) and checked |
| 1.2 | Triangles within a sourced budget (≤ 2,000 PROPOSAL or the brief's); evaluated count from the audit |
| 1.3 (must) | Grip pivot and a `BladeTip` / `BladeBase` attach-point record (name, parent, position, look and up axes, revision) for VFX |
| 1.4 | Size checked against the player dummy; the blade reads from the front at the game camera |
| 1.5 | Icon render set for UI from the shipped model: fixed camera, light, magenta or alpha background as briefed |
| 1.6 | One material, one UV map; texture size on plan (≤ 512 PROPOSAL) |

## 2. Hero pet from Tripo, through the rig loop (high effort; G2 test B)
> A small hero pet (a round fox-like creature) for the same game, follows the player, idles, hops and looks around; 6 on screen; must look especially good. The owner will run Tripo. The character-rigger's rig sheet is at `content/rigs/<pet-id>/rig-sheet.md`. Build it.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Tripo input pack written: images per Tripo advice (single subject, plain background, ≥ 1024², or separate views named by the subject's own left), family and version, polycount target under the budget, Remove Lighting on, no Tripo auto-rig or segmentation unless the cut list allows, FBX export, what to record |
| 2.2 (must) | Raw-candidate check before clean-up: clay, wireframe, back and underside, loose parts, triangles; reject or accept with reasons |
| 2.3 (must) | Cuts, caps and bend zones exactly as the rig sheet; caps carry continuous texture, rounded rims; no bridge mesh; tuck-and-cap, never face deletion to close shells |
| 2.4 (must) | C1-C5 of the modeler hand-off reported with numbers; whole model under about 7,000 triangles |
| 2.5 | Each cut part has its own UVs and a re-bake from the raw model (no shared atlas across cut parts) |
| 2.6 | Raw folder untouched (file hashes unchanged) |

## 3. Modular building kit for the environment designer
> The environment designer needs a small timber house kit: straight wall, corner, door wall, window wall, floor, roof piece, roof end, for a village hub; players walk inside; third-person camera. Brief from the environment designer attached (`environment-craft/references/handoffs.md` §3 format). Build the kit.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Kit interface contract first: grid and module size with source, snap origin, axes, neighbours, trim direction, interior decision |
| 3.2 (must) | Test assembly (outside and inside corner, door, window, roof join) checked for gaps and z-fighting before more pieces |
| 3.3 | Door opening at real player size; collision keeps the doorway open; walkable floor keeps Default collision |
| 3.4 | Reuse: pieces uploaded once; variants change shape only where needed, else tint |
| 3.5 | Hand-off packet to the environment designer with pivots, sizes in studs, collision roles, import notes |

## 4. Fix a model that "looks wrong in Studio"
> The owner says the imported lantern is huge, faces backwards and its glass is invisible from outside. Files: `content/models/lantern/`. Fix it.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Diagnoses by layer before editing: scene units, transforms, export scale, importer scale; one change at a time; no stacked scale recipes |
| 4.2 (must) | Explains the invisible glass as back-face culling / inverted normals (audit: inverted parts), fixes geometry, not a texture trick |
| 4.3 | Re-runs the checks the fix can break (scale changes pivots and collision) |
| 4.4 | Re-import in a test place with numbers (size, facing) MCP-verified |

## 5. Over-budget creature
> A Tripo creature came back at 38,000 triangles with fused legs. It must walk and run, 4 on screen. Make it game-ready.

| Check | Expected |
| --- | --- |
| 5.1 (must) | Does not decimate the bending regions blindly; retopologizes or rebuilds legs and joints; decimation only on static irregular areas |
| 5.2 (must) | Fused repeated legs: builds one clean leg and copies it, or asks the rigger; never lets weights hide fusion |
| 5.3 (must) | Lands under the creature budget (under about 7,000, J007-D5) with the evaluated count; or returns `needs-decision` with options if the look cannot survive |
| 5.4 | Re-bakes textures from the untouched raw model after retopology |
