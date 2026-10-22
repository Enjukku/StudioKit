---
name: environment-craft
description: The how for building a Roblox stage or world in Blender and Studio and proving it - scale, blockout, terrain, kit import, lighting, Atmosphere, skybox, interiors, ambience map, scene audit. Use for "set up the lighting", "add fog", "change the skybox", "make it night", "light leaks through the wall", "it's the wrong size in Studio", "take the review shots". Read environment-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. J008. Facts: `knowledge/reference/environment/fact-check-*.md` (LF, LX, AU, PI, PX rows) and `05-roblox-look-dev.md` (LD rows, every control with its doc file:line); method: owner environment paper notes 01-03; first-game practice `04-first-game-stages.md` (FS). Docs mirror: `knowledge/external/roblox-creator-docs/`. Rebuilt by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (greybox order, grey value and light-direction pass, material zoo, clean floors and grounding in the dress step, the measuring commands in `references/measure-captures.md`, rows C-15 to C-22).

# Environment craft: building the place in Blender and Studio

## 1. When this skill starts
`environment-design` §3 has produced (or the brief gives) an approved blueprint with its read plan, reference images, the route graph and the art bible version. For a fix: the review record that names the problem. Studio work happens in a **test place**, never a live game place unless the brief says so; Blender work on a copy, never on the approved source. After a compaction, re-read §3 and §6 here and `environment-design/references/review.md` §7.

## 2. Read this file when
| You need | Open |
| --- | --- |
| What to build where; the scale chain; export and import; snapping art to the blockout; Blender MCP rules | `references/blender-to-studio.md` |
| Terrain, ground, water, terrain materials, ground that serves the read | `references/terrain-and-water.md` |
| Lighting, atmosphere and haze, sky and skybox swaps, clouds, post effects, local lights, interiors, runtime looks, look lab, value band and material zoo in Studio | `references/studio-light-air.md` |
| Zone volumes, source anchors, audio facts, streaming-safe sources | `references/ambience-in-place.md` |
| Streaming, cheap defaults, what degrades on phones, measuring | `references/performance.md` |
| Scene audit tool, camera set and captures, review packet | `references/audit-and-capture.md` |
| The commands behind every numbered self-review line (M1-M12): value and separation, the colour script (reserved hues, chroma, temperature, flat fill), palette roles, phone size, place listings, quality level | `references/measure-captures.md` |
| Briefs to the game designer, art director, modeler, sound, VFX, studio operator; what to ask each partner for and when | `references/handoffs.md` |
| Every control's doc line, Roblox's own scenes, open look questions | `knowledge/reference/environment/05-roblox-look-dev.md` |
| Studio MCP basics (instances, play mode, safe probes) | `studio-mcp` skill |

## 3. Steps
Image budget throughout: numbers for every case; images only for a failing number and the key views (`environment-design/references/review.md` §3).
1. **Set up.** `list_roblox_studios` → pick the test place's studio_id (name it on every call); `get_studio_state`. Confirm the Blender file and version (`get_objects_summary`). Write the stage folder `content/stages/<stage-id>/`.
2. **Scale and round trip.** Scene scale record; calibration object and player dummy; one asset Blender → Studio and measured before bulk work (`blender-to-studio.md` §2-§3). Measure the jump height (the block ladder of `level-design/references/review-artifact.md` §6.6, once per game, into the game profile) and eye height in Studio and record them.
3. **Greybox in Studio** from the blueprint coordinates, on a fixed snap grid: spawns first, then the route to the objective, then side areas; walkable volumes, openings, heights, boundaries, a `PlayArea` part; shapes that already read as the theme's structures (a market stall, a mine frame), not abstract blocks; a player dummy and a known-size object in every space; collision as simple boxes. Walk it with the real avatar and camera at walk speed; capture the first view, decision views and the top-down. Keep the greybox as a named reference.
4. **Grey value and light-direction pass** (still grey): try 2-3 sun positions (ClockTime and latitude) and measure each on the first view and decision views (M1, M6, `measure-captures.md`); keep the one where the objective wins the focus (`environment-design/references/review.md` RD2 rule) and no key position sits in deep shadow; record it in the look sheet (numbers for every variant; images of the winner only, unless the numbers tie). Mark dead space on the top-down. Layout fixes happen here.
5. **Terrain** big forms from the greybox; height and layers in every area; materials by slope and height from one recorded script; paths, water, exits (`terrain-and-water.md`).
6. **One-off Blender pieces** (cliffs, cave shells, landforms) snapped to the greybox, counted on the evaluated mesh, rendered beside the reference, exported with the project recipe, imported and checked. Ask the modeler for reusable assets (`handoffs.md` §3); import each asset once, place it, and return one in-set capture of it at the game camera with a player in frame.
7. **Material zoo.** Put one sample block of every material the stage uses in the test place under the stage's chosen sun, beside reference blocks for the palette roles, reserved hues and a mid grey, and check it against the band, reserved hues and palette roles as rendered under that light (`studio-light-air.md` §9) before the material reaches the stage.
8. **Dress** by the blueprint's set list and the read plan: story clusters carrying the story facts, calm floors in play areas (cover cut back to a whisper; the smallest gameplay object still reads), detail on the read plan's spots, every object grounded (base, blended seam, contact shadow), size steps in each group, no piece twice at the same angle in a key view, every visible face and enterable room finished, facing checked.
9. **Look**, after the last route change. Follow `studio-light-air.md` §1 in order; write every value with its source into the look sheet `content/stages/<stage-id>/look.md` (per zone and state: Lighting, Atmosphere, Sky, Clouds, post effects, local lights, and how it changes). Run the look-lab questions the look depends on (§8 there).
10. **Ambience in place.** Zone volumes and source anchors from the ambience map with the exact conventions; brief the sound and VFX designers (`ambience-in-place.md`; `handoffs.md` §4-§5).
11. **Self-review** (`environment-design/references/review.md` §7, commands in `measure-captures.md`): fix, re-shoot, then the review packet.
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
| C-09 | Scripts cannot set terrain Decoration, GrassLength, material override names, streaming properties, DefaultListenerLocation: plan them as Properties-window steps. Terrain material colours are a script step: `Terrain:SetMaterialColor(material, Color3)` in `execute_luau`, one material per call, read back with `GetMaterialColor` (the `MaterialColors` property itself is not scriptable). RenderSettings is plugin-only: probe before relying on `execute_luau` to set the quality level (`measure-captures.md` M9) | LX03, LD51, PX02, LD131, AU21; J018 |
| C-10 | Import each asset once and duplicate in Studio; anchor static parts; cheapest collision that plays right; CanCollide/CanTouch/CanQuery off where nothing touches | PI18-PI20 |
| C-11 | Audio on an ordinary streamable part stops at stream-out: give each must-hear source a streaming-safe home and a rebuild rule | AU27; `ambience-in-place.md` §3 |
| C-12 | Caps are not budgets: 20,000 triangles per mesh, particles 400/s (100/s mobile) per emitter, 20 s lifetime, 4096 px heightmap; budgets come from the owner or a phone trace | PI24, LF35-LF36, LF41; PX01 |
| C-13 | Check the result in the real camera at the lowest and highest quality: shadows go below level 4, post effects may drop, refraction is off on mobile | LD130-LD137 |
| C-14 | Tutorial and showcase values are examples for one scene; the look lab and the art bible set the stage's values | A09; LD 3 |
| C-15 | The key light direction comes from the grey pass (§3 step 4), is saved in `TimeOfDay`, and is not moved after the look pass starts; a later move re-runs the key views | J018 |
| C-16 | Shadow sides keep colour: tint Ambient and OutdoorAmbient (and ColorShift_Bottom) toward the art bible's opposite temperature instead of neutral grey, with a hint of the ground's colour so characters sit in the place; ColorShift_Top carries the sun's temperature | `Lighting.yaml:39-50, 129-140`; J018 |
| C-17 | The environment never reaches pure black or a large white: fix it in materials, ambients and exposure, measured on captures, not by a post effect | J018 |
| C-18 | Every material is proved in the zoo under the stage light before it is used; a new floor material also needs the sound designer's footstep entry | J018 |
| C-19 | Grayscale and phone-size views come from the capture (luminance image, thumb), so the place is never edited for a review; when a Studio grey view is needed, a ColorCorrectionEffect with Saturation -1 under the Camera, removed after | `ColorCorrectionEffect.yaml:78-84`; J018 |
| C-20 | Seams where meshes meet ground are covered by burying, a skirt, decals or small debris; a darker ring of terrain paint seats hazards; colour bleed is a soft tinted decal or terrain paint near the object | J018 |
| C-21 | Kit pieces and shared trim-sheet SurfaceAppearances live as packages so a fix updates every copy; grass cards and other alpha cards stay few (each costs overdraw on phones); lights, effects and dressing sit in named folders that can be switched off, so a capture without effects or a variant is one toggle | `projects/assets/packages.md:3, 14-19`; `tutorials/curriculums/environmental-art/assemble-an-asset-library.md:93`; J018 |
| C-22 | Ambient motion near a sight line is slowed and dimmed at the source (ParticleEmitter TimeScale, Brightness, a partly hidden base), never left as the fastest or brightest thing in view | `ParticleEmitter.yaml:78, 962`; J018 |

## 5. Rules (final check, short)
- Test place only; studio_id on every Studio call; one Studio driver at a time; restore the owner's edit camera after captures (FS-V03, FS-V08); undo every review-only toggle (quality level, post effects off, grey view).
- Never edit game scripts through the Studio MCP; never edit the approved source copy; never upload assets or create accounts unless the brief says so; keys only from environment variables.
- Every value in the look sheet, blueprint and map has a source or is `PROPOSAL` / `UNKNOWN`. No invented budgets, ranges or presets.
- Route, sound, VFX and asset craft stay with their owners: change requests go as briefs. Art never moves collision, cover or sight lines of the approved greybox.
- Never claim you saw, heard or measured something without evidence from this task; label every check.

## 6. Self-check before returning
- [ ] Scale record and one measured round trip; every import checked (size, facing, pivot, collision); jump and eye height measured.
- [ ] Greybox walked; grey value and light-direction pass recorded (variants and their numbers); collision diff vs greybox clean or signed off.
- [ ] Terrain in every area; path network joined; exits from pits, water and heights; floors clean for the smallest gameplay object.
- [ ] Material zoo checked; look sheet complete per zone and state with sources; look-lab results recorded with build and date; manual Properties steps listed.
- [ ] Zone volumes and anchors match the ambience map (scene audit: no missing, unlisted or duplicate ids).
- [ ] Scene audit: 0 floating, 0 buried, 0 outside the play area (or each exception explained); counts per zone recorded.
- [ ] `environment-design/references/review.md` §7 lines answered with their inputs; key views at the lowest and highest setting; captures counted against the image budget; review packet filled; 3 weakest points named.

Project overlay: if `knowledge/overlays/environment-craft.md` exists, read it after this file; it wins for this game.
