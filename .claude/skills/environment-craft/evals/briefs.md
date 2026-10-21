> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Eval briefs for the environment-designer (environment-design + environment-craft)

Give the agent the brief text and the named files only. A separate grader (Sonnet, high, J008-D4) grades each check pass / fail from the agent's files, not its summary. A brief passes at ≥ 80 % of its checks with no "must" check failed. Hidden cases (J008 `hidden-cases.md` and the paper's held-out defect section) are graded separately and were not used to write the skills. Common checks apply to every run.

| ID | Common check |
| --- | --- |
| R1 (must) | No invented numbers: every size, light, atmosphere, sound range, budget and count has a source (blueprint, owner, doc file:line, look-lab result, measurement) or is `PROPOSAL` / `UNKNOWN`; tutorial values labelled examples; platform caps never called budgets |
| R2 (must) | Role boundaries kept: route changes proposed to the game designer, sound and effect craft left to their designers, reusable assets requested from the modeler; no game code |
| R3 (must) | Roblox facts right where used (checked rows): Atmosphere dependencies, Ambient/OutdoorAmbient clamp, light Range cap 120, Neon emits no light, non-scriptable properties, streaming stops parented audio, scale recipe not stacked |
| R4 | Every check labelled gate-verified / MCP-verified / owner-confirmed / not verified; listening never judged from images |
| R5 | Hand-back in `rules/messages.md` §3 shape: STATUS first, coverage per item, evidence paths, 3 weakest points |
| R6 (must, when Studio is used) | Test place only; studio_id on every call; bounded changes read back; no blind repeats |

## 1. New stage slice, full loop (G2 brief, high effort)
> Build a small game-neutral slice for the kit test: a swamp edge (frogs, insects), a waterfall that grows louder as you approach, a cave mouth (drips, echo) and a high ridge (wind). Third-person phone camera, default avatar, 1-4 players. The route: ridge → descent past the falls → swamp boardwalk → cave mouth (route graph in the brief folder). Use the art bible starter locks (`templates/skill/art-bible.md`). Separate Studio test place; Blender with the MCP add-on.

| Check | Expected |
| --- | --- |
| 1.1 (must) | Key-place reference images made with `reference-images` (concept / environment families) and annotated as spatial targets before the blueprint |
| 1.2 (must) | Blueprint from `stage-blueprint.md` with a player figure on every sheet, site plan, scale sheet, guidance per decision point and a built-where table with reasons; shown for approval before building |
| 1.3 (must) | Terrain with height changes in every area; path network joined; a way out of the water and the cave; no flat plane |
| 1.4 | One Blender → Studio round trip measured before bulk import (calibration object, recipe recorded) |
| 1.5 (must) | Look sheet: sky chosen before Atmosphere, values per zone with sources, at least 3 look-lab questions answered with captures |
| 1.6 (must) | Ambience map for all four zones: feeling, causes, point sources with anchors, blends with edge cases, streaming rule, fallback; numbers `UNKNOWN` where unmeasured |
| 1.7 | Zone volumes and anchors in the place with the exact conventions; scene audit shows no missing, unlisted or duplicate ids |
| 1.8 (must) | Review packet: camera set at low and high quality incl. eye-level route, reverse route, top-down, scale-with-player; audit 0 floating, 0 buried; budgets measured or `UNKNOWN` |
| 1.9 | Briefs to the sound and VFX designers in the `rules/messages.md` format, from the map |

## 2. Fix: "players miss the cave entrance" (medium effort)
> Play-testers walk past the cave on the swamp boardwalk. Fix it. Stage files and captures from brief 1.

| Check | Expected |
| --- | --- |
| 2.1 (must) | Cause found before changing anything (off-camera, hidden, blends with background, contradicted cue, shown late, read as inaccessible), with the camera evidence |
| 2.2 (must) | Least disruptive fix (framing, contrast, light, a sound cue with a visible cause) before arrows or signs; route length or timing changes go to the game designer as a proposal |
| 2.3 | Retest of everything the change touches (sightlines, collision, ambience border), before / after captures from the same cameras |

## 3. Look change: dusk hub, dark cave, night sky (medium or high effort)
> The owner wants the hub to feel like a warm dusk, the cave dark with a single glowing crystal that guides you, and a starry night sky after a story event. Phones must still read the path.

| Check | Expected |
| --- | --- |
| 3.1 (must) | Sky handled honestly: no blend feature claimed; swap hidden behind a fade / event moment, or mood moved with tweens of Atmosphere, ambients, ColorCorrection, orientation |
| 3.2 (must) | The crystal glows with Neon or emissive **plus** a light object; Range within the 120 cap; it is the brightest point in the cave |
| 3.3 | Dusk from ClockTime and latitude, sky, warm ambients with Ambient ≤ OutdoorAmbient, exposure rather than Brightness; Atmosphere with Haze before Glare / Decay |
| 3.4 (must) | Path readable at low quality: no reliance on shadows, bloom or SunRays for the route; captures at low and high quality |
| 3.5 | Runtime change specified for a code role (what changes, when, how long); no game code written |

## 4. Import and interior problems
> The cliff imported from Blender is 100 times too small, and the hut interior is lit like outdoors through its walls.

| Check | Expected |
| --- | --- |
| 4.1 (must) | Scale fault traced layer by layer (scene units, transforms, export conversion, importer) and the stacked .01 recipe named as the likely cause; fixed at the source, not by rescaling in Studio |
| 4.2 (must) | Interior: thin walls under Realistic; blockers ≥ 1 stud thick added without closing windows or approved openings; exposure checked |
| 4.3 | Collision and pivots re-checked after the fix; scale shot with the player |

## 5. Hand-off readability (graded with the sound and VFX designer roles)
> Give the ambience map from brief 1 to the sound designer and the VFX designer (separate runs). Each lists what they would make and what they would need to ask.

| Check | Expected |
| --- | --- |
| 5.1 (must) | Each designer can list its work per zone and source from the map alone; any question they must ask is a gap in the map |
| 5.2 | No craft choice was made for them (no clip names, gains, particle counts in the environment designer's keys) |
