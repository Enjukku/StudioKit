---
name: vfx-craft
description: Use when building a planned visual effect in Roblox — turning a vfx-design frame script into layers, exact property values, named curves, textures, meshes, beams, trails, lights and an effect spec file. Covers particles, flipbooks, meshes (rings, domes, crescents, pillars, waves), beams and trails, object changes (flash, swap, pop, shine), world events, cutscene effects, pro default values per layer job from 30 measured pro effects, recipes per effect type, the curve library, texture picking, budgets and the spec.json format. Read vfx-design first for what the effect must make the player feel and which technique to use; this skill is how to build it. Game-agnostic; does not write game code.
---

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20 (split from vfx-design v2)

# VFX craft: building effects in Roblox

## 1. When this skill starts
You arrive here **after** `vfx-design` steps 1-4: you have the brief (job, ratings, rate, gameplay truth), the context and technique choice, and **our frame script** with screen sizes. If any of those is missing, go back to `vfx-design` and make it first. This skill turns the frame script into a layer plan and a spec file that look pro on the first build.

## 2. Read this file when
| You need | Open (in this order) |
| --- | --- |
| How to build the chosen tool (particles, mesh, beam/trail, object change, world event, cutscene, fake destruction) | `references/techniques.md` |
| Layers for the effect type and values per layer job | `references/pro-defaults.md` §B, then §A |
| Curves (size, transparency, squash, colour, beam, trail) | `knowledge/reference/vfx/training/curve-library.md`; keypoints in `content/vfx/curves.json` |
| Exact property ranges, enums, engine limits | `knowledge/reference/vfx/roblox-vfx-api-card.md` |
| Spec file, sound brief and texture-pick formats, screen-size math | `references/plan-and-spec.md` |
| Mesh shapes and what Roblox cannot do with meshes | `knowledge/reference/vfx/mesh-vfx.md` |
| Tutorial craft rules and full recipes (explosion, slash, beam, strike, aura) | `knowledge/reference/vfx/tutorials.md` |
| Flipbook sheets, kitbashing, cadence | `references/flipbooks-and-kitbash.md` |
| Roblox costs, quality tiers, cut order | `references/roblox-vfx.md` |
| Full pro statistics per job, per effect, per type | `knowledge/reference/vfx/training/building-blocks.md` |
| How a pro effect looks frame by frame | `knowledge/reference/vfx/training/frame-scripts/` |
Where older text in `flipbooks-and-kitbash.md` or `roblox-vfx.md` conflicts with this file or `pro-defaults.md`, this file wins (§6).

## 3. Build steps
1. **Layer plan from the type recipe** (`pro-defaults.md` §B). Every frame-script moment must be made by named layers; add the dark twin, glow and ground mark the recipe lists.
2. **Values per layer:** copy the job row (`pro-defaults.md` §A); move a value only with a reason written in `why`. Scale size and speed together with the effect size the frame script needs.
3. **Curves:** the default size + transparency pair per job from the curve library; copy keypoints, keep envelopes, never average two curves.
4. **Textures:** shared set first, then the library shortlist; open every pick with Read; one style family per effect (`plan-and-spec.md` §E).
5. **Meshes, beams, object changes, world-event or cutscene parts:** follow `techniques.md` T2-T6.
6. **Write `spec.json`** (`plan-and-spec.md` §C) with a budget block, then the self-check (§5), then the capture request: one clip in the dark test place, game camera, 30 fps; compare with the frame script using `tools/vfx/clip_metrics.py`; fix clear misses once; then the owner's final look.

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
| C-10 | **Fade every layer by size or transparency**; impact layers may appear instantly; nothing pops out | 50% of S+A layers stay opaque and shrink instead (CL, TU-01/02) |
| C-11 | **Bodies are flipbooks** (fire, smoke); billboards (flare, impact, ring, glow) do not move | 94% of flame and smoke bodies; flares Speed 0 (BB) |
| C-12 | **Direction from orientation:** streaks VelocityParallel + Squash; rings, slashes, ground VelocityPerpendicular; bolts FaceCameraWorldUp; never Speed 0 with velocity orientations (use 0.01) | BB §9.11, TU-05 |
| C-13 | **Randomise decoration:** rotation, size envelope, lifetime and speed ranges | TU-09 |
| C-14 | **Glow over everything:** Speed 0, FaceCamera, ZOffset 2-3, hold or V transparency, subtle | glow peak 13-15 studs (BB, TU-14) |
| C-15 | **Accents stay faint:** rainbow and lens flares, sun rays, halftones, realistic smoke under anime layers | TU-19, TU-22 |
| C-16 | **Impact leaves a mark:** ring, ground decal or crack that grows fast then stops | ground decal life ~1-1.3 s (BB, TU) |

## 5. Build self-check
- [ ] Every frame-script moment maps to named layers; every layer has one job and a `why`.
- [ ] Values start from `pro-defaults.md`; departures have reasons. Curves are named library curves with keypoints copied.
- [ ] LightInfluence 0 on every emitter, beam and trail; LightEmission set on purpose; Brightness set.
- [ ] Impact: flash 0.03-0.05 s, shape 0.1-0.2 s, sparks with drag, a dark twin, a glow, a ground mark.
- [ ] Every texture opened with Read; unique textures listed; shared set reused; no invented asset id.
- [ ] Budget block: unique textures, emitters, est. live at peak (Σ EmitCount + Rate × Lifetime) ≤ ~1000 near the camera, Rate ≤400/s (100 mobile), lights; low-tier drops listed (decoration only).
- [ ] Meshes and beams follow `techniques.md`; nothing relies on a mesh feature Roblox lacks.
- [ ] Spec is valid for a tool: enums by name, ≤20 keypoints per sequence, t from 0 to 1.

## 6. v2 overrides of older reference text
| Old | v2 | Why |
| --- | --- | --- |
| "Hero blast ≤5 emitters + 1 light; normal effect ≤4 layers" | type recipe for layers; budget = textures + live particles | pros use 20-150 emitters |
| "Do not paint effects; kitbash pre-made sheets only" | you specify every layer; meshes and own textures allowed | the VFX agent plans every layer itself |
| Effect card as the build output | `spec.json` (+ brief.md, frame-script.md) | effects are data |

## 7. Game specifics
- **Textures:** tagged VFX Studio library `content/vfx/library/catalog.json`; `python tools/vfx/vfxlib_catalog.py shortlist --group <G> --style anime --min-quality A`. No manual tagging rounds.
- **Files per effect:** `content/vfx/<effect-id>/` → `brief.md`, `frame-script.md`, `spec.json`; captures in `output/vfx/<effect-id>/captures/` (per-game working output, optional, git-ignored).
- **Player:** cosmetic effects play on clients, started by one network event from the server (ZO-04; the transport layer is named in the game profile). A player module and spec compiler are game code: until the game has them, the orchestrator turns `spec.json` into a test script.
- **Existing code (read, never edit):** the game's client VFX modules and render tuning, if any (paths in the game profile).
- **Related skills:** `performance` (client budgets beyond VFX), `ui-basics` (UI effects: `ui-basics/references/ui-effects.md`), the game's animation skill when present.
- **Studio:** you do not drive Studio; the studio-operator records the capture you name. Dark test place.
- **Visuals only:** specs and test scripts create and clean up their own instances only, including cosmetic fake-destruction parts (T8). Never touch real map parts, players or gameplay objects; no damage, no hit areas. A test target is a marker point, not a gameplay hit.
- **Test place:** build and test in a separate test place, not the game place (name and sync file in the game profile), opened in its own Studio session by the owner (one Studio at a time). Dark lighting, plain dark floor, a wall and floor patch for fake-destruction tests, an R15 dummy for scale. If it does not exist yet, create it (orchestrator task) before the first build.
