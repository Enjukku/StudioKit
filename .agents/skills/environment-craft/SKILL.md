---
name: environment-craft
description: Build a Roblox stage, level or world in Blender (Python + Blender MCP) and Roblox Studio (Studio MCP) and prove it - the built-where choice, the scale chain and one round trip, blockout, terrain and water, kit assembly and import checks, lighting style, sun, ambient fill, exposure, shadows, Atmosphere density/offset/haze/glare/decay, skybox making and swapping, clouds and wind, post effects, local lights and glow, interiors without light leaks, runtime looks (time of day, weather, zones, events), what scripts cannot set, putting the ambience map into the place (zone volumes, source anchors, streaming-safe sources), streaming and phone performance, the scene audit, the camera set, the look lab and hand-off briefs. Use while building or fixing a place, for "set up the lighting", "add fog/haze", "change the skybox", "make it night", "the interior is too bright", "light leaks through the wall", "import the cliff from Blender", "it's the wrong size in Studio", "check for floating parts", "take the review shots". Read environment-design first (what and why); this is how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J008. Facts: `knowledge/reference/environment/fact-check-*.md` (LF, LX, AU, PI, PX rows) and `05-roblox-look-dev.md` (LD rows, every control with its doc file:line); method: owner environment paper notes 01-03; first-game practice `04-first-game-stages.md` (FS). Docs mirror: `knowledge/external/roblox-creator-docs/`.

# Environment craft: building the place in Blender and Studio

## 1. When this skill starts
`environment-design` §3 has produced (or the brief gives) an approved blueprint, reference images, the route graph and the art bible version. For a fix: the review record that names the problem. Studio work happens in a **test place**, never a live game place unless the brief says so; Blender work on a copy, never on the approved source.

## 2. Read this file when
| You need | Open |
| --- | --- |
| What to build where; the scale chain; export and import; Blender MCP rules | `references/blender-to-studio.md` |
| Terrain, ground, water, terrain materials | `references/terrain-and-water.md` |
| Lighting, atmosphere and haze, sky and skybox swaps, clouds, post effects, local lights, interiors, runtime looks, look lab | `references/studio-light-air.md` |
| Zone volumes, source anchors, audio facts, streaming-safe sources | `references/ambience-in-place.md` |
| Streaming, cheap defaults, what degrades on phones, measuring | `references/performance.md` |
| Scene audit tool, camera set and captures, review packet | `references/audit-and-capture.md` |
| Briefs to the game designer, art director, modeler, sound, VFX, studio operator | `references/handoffs.md` |
| Every control's doc line, Roblox's own scenes, open look questions | `knowledge/reference/environment/05-roblox-look-dev.md` |
| Studio MCP basics (instances, play mode, safe probes) | `studio-mcp` skill |

## 3. Steps
1. **Set up.** `list_roblox_studios` → pick the test place's studio_id (name it on every call); `get_studio_state`. Confirm the Blender file and version (`get_objects_summary`). Write the stage folder `content/stages/<stage-id>/`.
2. **Scale and round trip.** Scene scale record; calibration object and player dummy; one asset Blender → Studio and measured before bulk work (`blender-to-studio.md` §2-§3).
3. **Blockout in Studio** from the blueprint coordinates: walkable volumes, openings, heights, a `PlayArea` part; walk it with the real avatar and camera; capture approach, decision and return views. Keep the blockout as a named reference.
4. **Terrain** big forms from the blockout; height and layers in every area; paths, water, exits (`terrain-and-water.md`).
5. **One-off Blender pieces** (cliffs, cave shells, landforms) built, counted on the evaluated mesh, rendered beside the reference, exported with the project recipe, imported and checked. Ask the modeler for reusable assets (`handoffs.md` §3); place them, importing each asset once.
6. **Look.** Follow `studio-light-air.md` §1 in order; write every value with its source (example scene, art bible, look-lab result) into the look sheet `content/stages/<stage-id>/look.md` (per zone and state: Lighting, Atmosphere, Sky, Clouds, post effects, local lights, and how it changes). Run the look-lab questions the look depends on (§8 there).
7. **Ambience in place.** Zone volumes and source anchors from the ambience map with the exact conventions; brief the sound and VFX designers (`ambience-in-place.md`; `handoffs.md` §4-§5).
8. **Dress** by the blueprint's set list: story clusters, calm space on the route, every visible face and enterable room finished, facing checked.
9. **Self-review** (`audit-and-capture.md`): scene audit, camera set at low and high quality, renders and captures beside the references, ambience checks, budget numbers. Fix, re-shoot, then the review packet.
**Studio edits:** one bounded change per `execute_luau` call (Edit context); read back what changed; capture; never repeat a call after an uncertain result (it can duplicate hidden parts or lights) (H10 method). Long loops yield (`task.wait`) so Studio does not freeze (PI62). Studio MCP never edits game scripts (files mode).

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | One scale convention: Blender Unit System None (1 unit = 1 stud), FBX Apply Scaling = FBX Unit Scale, importer Scale Unit Stud; never stack the .01 recipes; prove one round trip first | PX05; PI42, PI44, PI53 |
| C-02 | Sky first, then Atmosphere: Atmosphere and environment light take their colour from the sky; the sky's lower half like the terrain and darker | LD63, LD101-LD102 |
| C-03 | Ambient ≤ OutdoorAmbient in every channel unless indoor colour should leak outdoors; GlobalShadows off removes the indoor/outdoor split | LD04-LD05, LD153-LD154 |
| C-04 | Brighten with ExposureCompensation, not Brightness, when shadows must stay clean | LD11, LD66 |
| C-05 | Haze: balance Density with Offset (ghosting vs LoD popping); Glare needs Haze; Decay needs Haze and Glare; never hide route information in haze | LD20-LD25, LD150-LD151 |
| C-06 | Neon and emissive need a real light beside them; light Range ≤ 120 studs; one point light per cluster; shadows only where they add | LD49, LD46, LD135 |
| C-07 | Interiors (Realistic): blockers ≥ 1 stud thick round thin walls; keep windows and approved openings clear | LD120; L12 |
| C-08 | A sky cannot be blended: hide a swap behind a fade, flash or doorway, or tween Atmosphere, ambients, ColorCorrection and orientation instead | LD105, LD89 |
| C-09 | Scripts cannot set terrain Decoration, GrassLength, MaterialColors, material override names, streaming properties, RenderSettings, DefaultListenerLocation: plan them as Properties-window steps | LX03, LD51, PX02, LD131, AU21 |
| C-10 | Import each asset once and duplicate in Studio; anchor static parts; cheapest collision that plays right; CanCollide/CanTouch/CanQuery off where nothing touches | PI18-PI20 |
| C-11 | Audio on an ordinary streamable part stops at stream-out: give each must-hear source a streaming-safe home and a rebuild rule | AU27; `ambience-in-place.md` §3 |
| C-12 | Caps are not budgets: 20,000 triangles per mesh, particles 400/s (100/s mobile) per emitter, 20 s lifetime, 4096 px heightmap; budgets come from the owner or a phone trace | PI24, LF35-LF36, LF41; PX01 |
| C-13 | Check the result in the real camera at low and high quality: shadows go below level 4, post effects may drop, refraction is off on mobile | LD130-LD137 |
| C-14 | Tutorial and showcase values are examples for one scene; the look lab and the art bible set the stage's values | A09; LD 3 |

## 5. Rules (final check, short)
- Test place only; studio_id on every Studio call; one Studio driver at a time; restore the owner's edit camera after captures (FS-V03, FS-V08).
- Never edit game scripts through the Studio MCP; never edit the approved source copy; never upload assets or create accounts unless the brief says so; keys only from environment variables.
- Every value in the look sheet, blueprint and map has a source or is `PROPOSAL` / `UNKNOWN`. No invented budgets, ranges or presets.
- Route, sound, VFX and asset craft stay with their owners: change requests go as briefs.
- Never claim you saw, heard or measured something without evidence from this task; label every check.

## 6. Self-check before returning
- [ ] Scale record and one measured round trip; every import checked (size, facing, pivot, collision).
- [ ] Terrain in every area; path network joined; exits from pits, water and heights.
- [ ] Look sheet complete per zone and state with sources; look-lab results recorded with build and date; manual Properties steps listed.
- [ ] Zone volumes and anchors match the ambience map (scene audit: no missing, unlisted or duplicate ids).
- [ ] Scene audit: 0 floating, 0 buried, 0 outside the play area (or each exception explained); counts per zone recorded.
- [ ] Camera set captured at low and high quality; renders beside references; review packet filled; 3 weakest points named.

Project overlay: if `knowledge/overlays/environment-craft.md` exists, read it after this file; it wins for this game.
