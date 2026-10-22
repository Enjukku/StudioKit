---
name: vfx-craft
description: The how for building a planned Roblox effect - turn a vfx-design frame script into layers, exact property values, curves, textures, meshes, beams, trails, lights and a spec.json file; recipes, budgets. Use when building particles, flipbooks, mesh effects, object changes, world-event or cutscene effects. Read vfx-design first. Does not write game code.
---

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20 (split from vfx-design v2). Rebuilt by J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (build passes with a blocking pass and gates, craft rows C-17 to C-31, the spec lines in §5, the measuring commands in `references/measure.md`). Numbers marked PROPOSAL are starting values a check may change.

# VFX craft: building effects in Roblox

## 1. When this skill starts
You arrive here **after** `vfx-design` §2 steps 1-6: the read card (job, ratings, tier, truth, information areas, budget), the context and technique, the picked option, **our frame script** with screen sizes, the animator's markers and the sound envelope. If any of those is missing, go back to `vfx-design` and make it first. This skill turns the frame script into layers and a spec file in passes: block the read with placeholder sprites and real timing, prove it with numbers, then colour, then polish. **After a context compaction**, re-read §3 and §5 before the next pass.

## 2. Read this file when
| You need | Open (in this order) |
| --- | --- |
| How to build the chosen tool (particles, mesh, beam/trail, object change, world event, cutscene, fake destruction) | `references/techniques.md` |
| Layers for the effect type and values per layer job | `references/pro-defaults.md` §B, then §A |
| Curves (size, transparency, squash, colour, beam, trail) | `knowledge/reference/vfx/training/curve-library.md`; keypoints in `content/vfx/curves.json` |
| The capture request, clip numbers, effect masks, look_check calls, curve shapes, flash and pulse counts; every command a screening aid with its known false readings and the eye check before a fix note | `references/measure.md` |
| Exact property ranges, enums, engine limits | `knowledge/reference/vfx/roblox-vfx-api-card.md` |
| Spec file, sound brief and texture-pick formats, screen-size math | `references/plan-and-spec.md` |
| Mesh shapes and what Roblox cannot do with meshes | `knowledge/reference/vfx/mesh-vfx.md` |
| Tutorial craft rules and full recipes (explosion, slash, beam, strike, aura) | `knowledge/reference/vfx/tutorials.md` |
| Flipbook sheets, kitbashing, cadence | `references/flipbooks-and-kitbash.md` |
| Roblox costs, quality tiers, cut order | `references/roblox-vfx.md` |
| Full pro statistics per job, per effect, per type | `knowledge/reference/vfx/training/building-blocks.md` |
| How a pro effect looks frame by frame | `knowledge/reference/vfx/training/frame-scripts/` |
| The self-review lines per pass | `vfx-design/references/review.md` §I |
Where older text in `flipbooks-and-kitbash.md` or `roblox-vfx.md` conflicts with this file or `pro-defaults.md`, this file wins (§6).

## 3. Build passes
1. **Layer plan from the type recipe** (`pro-defaults.md` §B). Every frame-script moment is made by named layers; each layer has one job, a rank (primary, secondary, tertiary) and a mark (semantic: it carries meaning and is locked; decorative: it may vary). Add the dark twin, glow and ground mark the recipe lists. Put every layer under one root (C-27). Reuse shipped layers first: recolour and retime before making new.
2. **Blocking pass: placeholder sprites, real sizes and timing.** Values: copy the job row of `pro-defaults.md` §A and move a value only with a reason written in `why`; scale size and speed together with the effect size the frame script needs. Curves: the job's size and transparency pair from the curve library (fast-in curves for bursts, C-21); copy keypoints and envelopes, never average two curves. Meshes, beams, object changes, world-event, cutscene and fake-destruction parts follow `techniques.md` T2-T8. Placeholder textures from the shared set (one soft dot, one solid shape, one streak), no flipbook polish; the truth edge at its real size from the data. Write `spec.json` v0. Build it over-strong first, then dial back. Name the capture (`references/measure.md` §1); read the clip numbers for every case and at most 4 key stills (build, peak, result, tail). Bracket the key numbers (size, count, height, start time) too low, too high, then pick, with numbers. Run `review.md` §I2. **Check-in** before any texture pick (BL-13): the blocking capture, its numbers and stills to the reviewer the brief names, the animator's markers and the sound envelope agreed.
3. **Value and silhouette gates** on the blocking stills (`review.md` §I3): grey first (the primary is the brightest at the focus, no blowout), then black-fill at the phone viewport (shape code, one primary shape, solid masses), mesh renders on `#FF00FF`. A failing gate is fixed here, by shape, size, timing or contrast, never by colour or more layers.
4. **Colour and texture pass:** textures (shared set first, then the shortlist, `plan-and-spec.md` §E), colour ramps per role (C-03, C-18), reused layers recoloured to the mood; then `review.md` CP-01 to CP-06 on at most 4 new stills, and VS-01 again on the coloured peak still: colour changes where the eye goes, so the primary must still hold the top luminance.
5. **Polish pass:** fades and blending, decorative variation, staggered exits, glow textures, ambient layers, piles and ground marks (C-10, C-13, C-23 to C-31), one named problem per pass, the worst first; `review.md` CP-07 to CP-15.
6. **Final `spec.json`** (`plan-and-spec.md` §C) with the budget block; run §5.
7. **In-game pass:** name the in-game captures (busiest scene, worst-case count, two-client when per-viewer variants exist, grayscale and reduced, device with audio); run `review.md` §I6; fix clear misses once; then the owner's final look on a playable preview.
A layer that keeps failing is deleted and rebuilt, not patched a third time. "It would be cooler" mid-job is new scope: a ticket with its cost, never a silent addition.

## 4. Craft core (what separates S/A pro effects from weak ones)
Evidence: BB = building-blocks.md (30 pro effects, 980 emitters); CL = curve-library.md; TU = tutorials.md; FS = frame scripts.
| ID | Practice | Numbers |
| --- | --- | --- |
| C-01 | **Many simple layers, one job each.** The look comes from stacking, not clever curves | S+A effect median 38 emitters; projectile unit 13, impact unit 10; 63% of curves have 2 keys (BB, CL) |
| C-02 | **Few textures, reused as twins** at different size, brightness, life | ~12 unique textures per effect, ~3 emitters per texture (BB) |
| C-03 | **Glow = Brightness, not white and not scene light.** LightInfluence 0 always; start colours saturated | Brightness median 5 (flare 5, flame 7.5, spark 5, smoke 2, glow 1.5); LI 0 on 979/980 (BB) |
| C-04 | **LightEmission is a switch:** 1 for glows, cores, flipbook bursts (additive, removes black); 0 for smoke, sparks, embers, dark layers. With LE 1, Brightness also works as opacity | 0 on 45%, 1 on 37% (BB, TU-04) |
| C-05 | **Dark twin** under bright layers gives shape and contrast | same texture darker, ZOffset −0.001 to −1 (BB, TU-08) |
| C-06 | **Everything fires at 0 ms; order comes from lifetime and ZOffset.** EmitDelay only for real beats (10-180 ms) | 81% have no delay (BB) |
| C-07 | **Short and sharp impact:** white flash 0.03-0.05 s, impact shape 0.1-0.2 s, sparks and flares 0.5-1 s, smoke ~1 s | S+A impact 0.12 s vs B+C 0.47 s; rings 0.20 vs 0.75 s (BB, TU-12) |
| C-08 | **Quiet, then a hard peak, then a soft tail.** Peak 1-3 frames; coverage drops within ~300 ms; tail 1-5 s | S peaks 54-79% of screen in close/follow clips (FS) |
| C-09 | **Sparks have physics:** fling and brake | Speed 25 (15-50), Drag 5.5, size 1.3, shrink to 0, spread 360, EmitCount ~15 (BB, TU-11) |
| C-10 | **Every layer exits cleanly, nothing popcorns.** Masses (clouds, smoke, piles, floor bits, ambient) fade in and out by Transparency, never by shrinking alone, and overlapping layers share colours so they blend; sparks, flares and impact shapes may stay opaque and shrink out; must-notice layers (flash, a telegraph's first frame) start at full strength | 50% of S+A layers stay opaque and shrink instead (CL, TU-01/02) |
| C-11 | **Bodies are flipbooks** (fire, smoke); billboards (flare, impact, ring, glow) do not move | 94% of flame and smoke bodies; flares Speed 0 (BB) |
| C-12 | **Direction from orientation:** streaks VelocityParallel + Squash; rings, slashes, ground VelocityPerpendicular; bolts FaceCameraWorldUp; never Speed 0 with velocity orientations (use 0.01) | BB §9.11, TU-05 |
| C-13 | **Randomise decoration only:** rotation, size envelope, lifetime and speed ranges on decorative layers; semantic layers (telegraph, flash, danger edge, team colour) stay locked, never FlipbookStartRandom | TU-09; size ±15 %, lifetime ±20 % (PROPOSAL) |
| C-14 | **Glow over everything:** Speed 0, FaceCamera, ZOffset 2-3, hold or V transparency, subtle | glow peak 13-15 studs (BB, TU-14) |
| C-15 | **Accents stay faint:** rainbow and lens flares, sun rays, halftones, realistic smoke under anime layers | TU-19, TU-22 |
| C-16 | **Impact leaves a mark:** ring, ground decal or crack that grows fast then stops | ground decal life ~1-1.3 s (BB, TU) |
| C-17 | **Rank the layers by value.** The primary (gameplay core) is the brightest, highest-contrast layer at the focus; the secondary (the theme: a trail, a beam with one tiling texture) is narrower and dimmer than the head; the tertiary is few, low Rate, small Size, never brighter or larger than the secondary | PROPOSAL: tertiary ≤ secondary in Brightness × LightEmission and in Size |
| C-18 | **An additive core keeps its colour with a halo behind it.** Core at LightEmission 1; a slightly larger, darker, more saturated halo at LightEmission 0 behind it. Additive layers stacked at the core sum toward white: count them, cut to the fewest that read | one white-hot dot on a pink halo, not six additive dots |
| C-19 | **Energy = a bright core, a softer glow, something moving.** Core locked to the source; a larger soft glow; a shell, ring or swirl with a moving texture (flipbook, Beam TextureSpeed, a rotating streaked texture) so it never looks like a sticker | — |
| C-20 | **Build-ups rise.** The charge core starts small and dim and grows and brightens (Size up to about 2×, settling about 1.5×, PROPOSAL); Rate ramps up over the build (cut back if it clutters); the build starts early enough to be seen; particles spawn on a ring and move inward (negative Speed or an inward shape) to pull the eye to the focus | practice values: PROPOSAL |
| C-21 | **Bursts reach size fast and ease out.** Growing bursts, rings and shockwaves use `ease-out grow`, `bump (early peak)`, `start 60%, grow to full` or an eased ring (≥ about 0.7 of max at t = 0.25, PROPOSAL); never `linear grow` on a burst. NumberSequences are linear between keys, so ease with keys | `references/measure.md` §5 |
| C-22 | **Cause, a hold, then the result.** Stage starts in seconds in the spec, tuned in 0.1-0.2 s steps; each result starts a few frames after its cause; the flash sits on the contact event. At the hit, set the build emitters' Enabled false (live particles finish their life, so keep that life short) and darken them; light the result | at 30 fps, 0.1 s = 3 frames |
| C-23 | **A volume reads solid.** Clouds, smoke and mist overlap until no background shows through: larger Size before more particles; a front and a back layer instead of one thin spread | Rate cap 100/s on mobile |
| C-24 | **Strobes stay low and behind.** A flicker layer sits behind the core at high Transparency; the core never flickers | — |
| C-25 | **Repeated objects vary; resting objects rest.** Symmetric sprites and spawned bits get a full random Rotation and a Size range (about 1-3×, PROPOSAL); RotSpeed 0 once at rest. Piles come from lifetime overlap (a floor layer with a long Lifetime and random early death); spawn width inside the play area; stacks stay low | — |
| C-26 | **Ambient effects are tiny, slow and partly hidden:** low Rate and Brightness, flames slowed (TimeScale below 1), the base hidden behind geometry, away from sightlines | — |
| C-27 | **One root.** Every layer under one root Attachment or Part, offsets relative to it; sizes and heights in one data block, so a global scale or height change is one edit. `Model:ScaleTo` scales emitter sizes with the model; a Part or Attachment resized by hand does not: keep the one factor in data and scale through `ScaleTo` or from that factor (probe once before relying on either) | — |
| C-28 | **Glow textures are soft dots with small irregularities:** a white or grey dot on a transparent PNG, blurred twice, slight noise, no square edge; a greyscale texture without alpha uses LightEmission 1 | — |
| C-29 | **Ground marks taper and stay true.** Cracks vary in width and taper, with a thin highlight edge; marks never extend past the affected area; a ground ring gets a vertical or camera-facing border where a low camera flattens it | — |
| C-30 | **Shape change by a Roblox route.** Stretch on speed = streaks (VelocityParallel + Squash); squash on contact = a ring, dust or a brief scale tween on the effect's own mesh; an overshoot passes the target size once and settles (Back easing or one extra key). Never scale a character's parts | a keyframe pose stores no scale |
| C-31 | **Ground blasts throw clumped cones,** not an even sphere: debris up and out in a few directional bursts (about a 45° cone, PROPOSAL); heavy chunks fly on arcs and brake hard (Acceleration down + Drag), dust drifts slow | — |

## 5. Spec self-check (the SP lines; input: the spec and the frame script)
There is no spec-checking tool yet (proposal filed): read `spec.json` and the wiring notes, do the arithmetic, write each line PASS, FAIL or MEASURED with the numbers.
| ID | Look for |
| --- | --- |
| SP-01 | Every frame-script moment maps to named layers; each layer has one job, a rank, a semantic or decorative mark and a `why` |
| SP-02 | Values start from `pro-defaults.md`; departures have reasons. Curves are named library curves with keypoints copied; every growing burst layer passes the fast-in test (`references/measure.md` §5) |
| SP-03 | LightInfluence 0 set explicitly on every emitter, beam and trail; LightEmission set on purpose; Brightness set |
| SP-04 | Impact: flash 0.03-0.05 s, shape 0.1-0.2 s, sparks with drag, a dark twin, a glow, a ground mark |
| SP-05 | Rank: the primary has the highest Brightness × LightEmission at the focus; the tertiary ≤ the secondary; additive layers stacked at the core counted (no more than the value gate passed) |
| SP-06 | Fades: masses and ambient layers fade in and out by Transparency; must-notice layers start full; no FlipbookStartRandom or random range on a semantic layer; decorative ranges within the read card |
| SP-07 | Every texture opened with Read; unique textures listed; shared set reused; no invented asset id |
| SP-08 | Budget block: unique textures, emitters, est. live at peak (Σ EmitCount + Rate × Lifetime) ≤ ~1000 near the camera, Rate ≤400/s (100 mobile), lights; low-tier drops listed (decoration only); no truth layer dropped or merged |
| SP-09 | One root; sizes and heights come from one scale factor |
| SP-10 | Meshes and beams follow `techniques.md`; nothing relies on a mesh feature Roblox lacks; no mesh spawned in numbers as particles |
| SP-11 | Valid for a tool: enums by name, ≤20 keypoints per sequence, t from 0 to 1; tier, per-viewer (LocalTransparencyModifier level) and reduced fields filled |
| SP-12 | Stage start times equal the timeline's event times in seconds, with the hold between cause and result; the flash on the contact event |
| SP-13 | Wiring notes for the builder name the trigger, event ids, anchors, the per-viewer and reduced settings and the test hooks; the builder's restatement leaves no open question |

## 6. v2 overrides of older reference text
| Old | v2 | Why |
| --- | --- | --- |
| "Hero blast ≤5 emitters + 1 light; normal effect ≤4 layers" | type recipe for layers; budget = textures + live particles | pros use 20-150 emitters |
| "Do not paint effects; kitbash pre-made sheets only" | you specify every layer; meshes and own textures allowed | the VFX agent plans every layer itself |
| Effect card as the build output | `spec.json` (+ brief.md with the read card, frame-script.md) | effects are data |
| "Fade every layer by size or transparency" (C-10) | masses fade by Transparency; sparks, flares and impact shapes may shrink out (J018) | shrink-only exits make masses popcorn |
| Ring size curve "constant size or grow from 38%" (`pro-defaults.md` §A) | an eased ring (≥ about 0.7 of max at t = 0.25) or `ease-out grow` (J018) | linear growth reads flat; the ring must reach its size fast |
| Build every layer, then one capture | blocking with placeholder sprites → numbers → check-in → gates → colour → polish → in-game (J018) | the read and the timing are cheap to change only before textures |

## 7. Game specifics
- **Textures:** tagged VFX Studio library `content/vfx/library/catalog.json`; `python tools/vfx/vfxlib_catalog.py shortlist --group <G> --style anime --min-quality A --out <sheet.jpg>`. No manual tagging rounds.
- **Files per effect:** `content/vfx/<effect-id>/` → `brief.md` (with the read card), `frame-script.md`, `spec.json`; captures in `output/vfx/<effect-id>/captures/<tag>/` and measurements in `output/vfx/<effect-id>/checks/` (per-game working output, optional, git-ignored).
- **Player:** cosmetic effects play on clients, started by one network event from the server (ZO-04; the transport layer is named in the game profile). A player module and spec compiler are game code: until the game has them, the orchestrator turns `spec.json` into a test script.
- **Existing code (read, never edit):** the game's client VFX modules and render tuning, if any (paths in the game profile).
- **Related skills:** `performance` (client budgets beyond VFX), `ui-basics` (UI effects: `ui-basics/references/ui-effects.md`), `animation-design` (the timing list, markers and the hit-stop freeze frame), `sound-design` (the envelope and cue cards).
- **Studio:** you do not drive Studio; the studio-operator records the capture you name (`references/measure.md` §1). Dark test place.
- **Visuals only:** specs and test scripts create and clean up their own instances only, including cosmetic fake-destruction parts (T8). Never touch real map parts, players or gameplay objects; no damage, no hit areas. A test target is a marker point, not a gameplay hit.
- **Test place:** build and test in a separate test place, not the game place (name and sync file in the game profile), opened in its own Studio session by the owner (one Studio at a time). Dark lighting, plain dark floor, a wall and floor patch for fake-destruction tests, an R15 dummy for scale. If it does not exist yet, create it (orchestrator task) before the first build.
