---
name: environment-design
description: Decide what a Roblox stage, level, hub or world must look, sound and feel like before and while it is built - turning the game designer's layout and the art bible into a place that reads from the player camera, feels real (light, air, sound and motion with causes), keeps the routes and runs on phones. Covers the stage order (reference images, blueprint the owner approves, built-where choice, blockout, target slice, light and atmosphere, ambience map, dressing, review), guidance and landmarks, real scale against the player, terrain everywhere, finished faces, set dressing, biomes, light and haze as composition and readability, ambience zones and point sources, the camera set and review packet, and measured budgets. Use when a place is planned, built, changed or reviewed, or when the owner says "it looks flat", "too dark", "players get lost", "it feels empty", "the cave should echo", "make the swamp feel alive", "it sounds the same everywhere". Read by the environment designer first; the game designer, art director, sound designer and VFX designer read it for the shared rules. Pair with environment-craft for the build.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J008. Sources: owner environment research paper (notes `knowledge/reference/environment/01`-`03`, fact-checked in `fact-check-*.md`), first-game stage practice with owner words (`04-first-game-stages.md`, **FS** rows), Roblox docs mirror. Tags: **V** VERIFIED, **E** EXPERIENCE, **O** OPINION, **U** UNKNOWN.

# Environment design: a place the player can read, feel and play

## 1. When this skill starts
A stage, level, hub, lobby or world is planned, built, changed or reviewed. It answers: what must the player notice and feel in each area; how the place guides without words; what is built where; how light, air, sound and motion tell the player where they are; what proves it works before the owner sees it.
**Who owns what** (CO04 O): game designer = routes, interactions, pacing (`level-design`); art director = style limits and hierarchy (art bible); modeler = every reusable asset; sound designer = how it sounds; VFX designer = how effects are built; the environment designer = the place: space, terrain, assembly, set dressing, lighting, atmosphere, ambience map, placement, transitions, and what must stay visible. The owner decides.
**Order:** this skill §3 → `environment-craft` for each build step → this skill's review (`references/review.md`) → owner.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Guidance, landmarks, scale, set dressing, terrain, biomes, art-bible cohesion | `references/place-reading.md` |
| What light, haze, sky and post effects must do (design side) | `references/light-and-air.md` |
| How a place sounds and moves; the ambience map rules | `references/ambience.md` |
| Review order, camera set, checks, budgets, fixing | `references/review.md` |
| A symptom to diagnose (flat, cluttered, wrong scale, same-sounding zones, too costly, stepped ground, wrong colours in renders, gaps that checks missed) | `references/diagnosis.md` |
| Route graph, pacing, walk times, teaching, encounters | `level-design` skill |
| Values, recipes and how to build in Blender and Studio | `environment-craft` skill |
| Templates | `templates/environment/stage-blueprint.md`, `ambience-map.md`, `review-packet.md` |
| The evidence behind a row | `knowledge/reference/environment/` (notes 00-05, fact-checks) |

## 3. Steps (each step's output is a file; owner gates in bold)
1. **Intake.** Read the game designer's route graph and actions, the camera and player envelope, the target phones, the art bible version, the set list and the brief. Missing fact that changes a hard-to-undo choice: ask; otherwise state an assumption and keep the work easy to change (W02 O; ST01 O).
2. **Set list and references.** List what players expect to find here (iconic, not trivia) and plan every decoration up front (FS-P06, FS-P09). Make key-place reference images with `reference-images` (concept and environment families; real photos first for real places, FS-R01); annotate each as a spatial target (PR-02). **Owner reviews the references** (FS-R06).
3. **Site plan, then building blueprints** (`stage-blueprint.md`): zones, path network, heights, terrain per area, scale sheet, elevations compared with the reference silhouettes, guidance per decision point, built-where table. Check the plan with a script, not by eye (FS-P07). **Owner approves the blueprint before any building** (FS-P01, FS-P05).
4. **Blockout and one round trip.** Calibrate scale with a player-size dummy; prove one asset Blender → Studio before bulk work (ST03 O). Block out in Studio against the real avatar and camera; walk it (BW02 O; W03 O).
5. **Target slice.** Build the hardest representative section to final quality first, with a character, UI and gameplay effects in view, at low and high quality (W04 O). Art director reviews; the owner rules on direction changes.
6. **Full build.** Assembly, terrain, set dressing, light and atmosphere, ambience map and zones (`environment-craft`). Breadth first, then polish (FS-H05).
7. **Review** (`references/review.md`): renders next to the references, then Studio multi-angle captures, scene audit, ambience checks, budget measurement, review packet. Fix and re-shoot before anyone sees it.
8. **Hand-offs and owner.** Briefs to the sound designer and VFX designer (from the ambience map), the modeler (new assets), the game designer (route proposals), the art director (look review), the studio operator (play-tests); `rules/messages.md` format. **Owner sees the packet (G3).**

## 4. Craft core (what separates a great place from a pile of nice objects)
| ID | Practice | Evidence |
| --- | --- | --- |
| E-01 | **A place is a playable composition.** Shapes, light, sound and motion tell the player where they are, what matters and what can happen next. Prove it in the real Roblox scene, never with one polished render. | EC1 O |
| E-02 | **The route is the game designer's.** Keep every approved edge, opening and timing; propose layout changes in the open. | RU01 O; PR-01 |
| E-03 | **Notice first, decorate second.** At each decision point, decide what the player must spot and why it reads, then check it in the real camera. Far landmark orients; near cue gives the next move. | RU02 O; PR-04, PR-05 |
| E-04 | **Real scale, measured against a player.** Real-size buildings felt like miniatures; the owner wants rooms and furniture that make sense at player size. 1 stud = 28 cm is only a unit conversion, not a size target: rooms, doors and furniture are sized from the player envelope, and real-size buildings can still feel too small. How much a game exaggerates is the owner's decision, recorded in the game profile or the blueprint. Three clearances (visual, collision, camera). | FS-S01 ("it's almost like you're making a miniature on purpose", D-091); PR-11-PR-16 |
| E-05 | **Terrain everywhere.** Every area has ground with height changes and visible layers that fit the theme; never buildings on a flat plane. Paths join a network; every door meets a path; the main walkway is never cut by scenery; every pit, river and high place has a way out. | FS-T01 ("we want a little bit of terrain in every stage", D-106); FS-T03-T05 |
| E-06 | **Finished on every face.** Players walk round everything: back and side walls get windows or equal detail; walls close on all sides; every enterable room is furnished and dressed; directional pieces face the right way; organic shapes stay organic; stepped or layered covers (roofs, terraces, stairs) have the vertical faces between their levels, checked from a low oblique view. | FS-B01 (D-192), FS-B02, FS-B03, FS-B06, FS-B07 |
| E-07 | **Compose for the approach.** The main face of a landmark points at the route; each structure has 2-3 iconic traits that must read at play distance. | FS-S08 (D-108); FS-S09 |
| E-08 | **Light and air serve mood and readability.** Light leads to the next choice; haze suggests depth but never hides information; the route reads at low quality without optional effects. Use the engine's own lighting, per stage, with its own sky when the stage needs one. | `light-and-air.md`; FS-L01 (D-126), FS-L03 (D-139) |
| E-09 | **Every sound and motion has a cause.** Each zone gets its own plan (continuous layer only if needed, intermittent life, world sources, weather and exposure), borders blend, streaming is planned, gameplay cues come first. Written as the ambience map. | `ambience.md` AB-01-AB-12 |
| E-10 | **Dressing tells a story of use.** Who used it, why it is still there; calm space where the player must read; detail where the player stops; repetition broken by composition before more meshes. | PR-17-PR-22 |
| E-11 | **A biome is palette, material, wind and sound together,** with a narrow vocabulary. Stages feel different as a whole; repeating a kind of element across stages is fine. | PR-24; FS-P10 (D-194) |
| E-12 | **Reuse a kit.** A shared prop kit first, a few approved building types with variants; ask the modeler for new pieces in the brief format. | FS-B11 (D-098); PR-20 |
| E-13 | **Build and test the heaviest piece first,** then decide; do not pay detail for parts nobody uses. | FS-V11; FS-T09 (D-121) |
| E-14 | **Budgets are measured, never invented.** Platform caps are not targets; the phone trace of the busiest scene sets the budget; the owner sets the frame-time target. | `review.md` §5; BT01-BT09 |

## 5. Rules (final check, short)
- The owner approves the blueprint before building and sees only reviewed work. Agents never mark work owner-approved (FS-P08).
- Route, interaction and pacing changes are proposals to the game designer; craft choices of sound, VFX, models and rigs stay with their owners (DN08 O).
- No number without a source: owner D-id, layout, measurement, doc file:line, or `PROPOSAL`; unknowns stay `UNKNOWN` (DN02 O). Tutorial values are examples, not presets.
- Never copy another game's layout, landmarks, names or assets; real places and cultures checked for accuracy and respect (PR-31).
- Gameplay-critical information never depends on sound alone or on optional effects.
- A passing automatic check (outline score, validator, audit) never overrules a screenshot that shows a defect (FS-V05).
- When a budget forces cuts, ask the owner what to protect (FS-P11); cut by measured cost, never by instance count.
- Never claim you saw, heard, played or measured something without evidence from this task. Label every check gate-verified / MCP-verified / owner-confirmed / not verified.

## 6. Self-check before returning
- [ ] Intake done; assumptions stated; references reviewed by the owner; blueprint approved (date and owner's words).
- [ ] Scale sheet, terrain in every area, path network checks, every visible face and enterable room finished.
- [ ] Guidance per decision point checked in the real camera, both directions.
- [ ] Ambience map complete for every zone and source; borders and streaming tested; listening review done or "pending".
- [ ] Review packet: camera set at low and high quality, scene audit clean (0 floating, 0 buried), budget numbers with sources, 3 weakest points.
- [ ] Hand-off briefs written in the `rules/messages.md` format.

Project overlay: if `knowledge/overlays/environment-design.md` exists, read it after this file; it wins for this game.
