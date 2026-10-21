---
name: vfx-design
description: Use when deciding what a visual effect must do and feel like in a Roblox game, before building it — importance, emotion and weight, what the player must see first, which context (gameplay moment, world event, object change, cutscene, UI) and which technique (particles, mesh, beam/trail, object change, camera/screen), timing for feel, frame scripts, screen shake, hit-stop, flash safety, readability, clutter, repetition, picture-sound sync, honest paid-random reveals and reviews. Also for feel requests that do not say VFX ("make this hit feel heavy", "the screen is too busy", "players can't see the attack coming"). Pair with vfx-craft to build the effect in Roblox; art-director, sound-designer and UI builders read it for shared feel rules. Game-agnostic; does not write game code.
---

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20 (v2 split: feeling and planning; build craft moved to `vfx-craft`)

# VFX design: what the effect must do, feel and use

## 1. Role and the two skills
This skill answers **what and why**: what the effect means, how strong it is, what the player sees first, which context and technique, and the target picture (a written **frame script**, never a 2D mock-up). Then **`vfx-craft` answers how**: layers, values, curves, textures, meshes and the spec file.

**Order for a new effect:** this skill §2 steps 1-4 → `vfx-craft` (build) → this skill §5 checks → capture → owner's final look .
**Who reads what:** the VFX agent reads both. Art director, sound designer and UI builders read this skill only (shared feel rules). UI effects are built with the `ui-basics` skill (`ui-basics/references/ui-effects.md`).

## 2. Planning steps
1. **Frame the job.** What it is, what it does, how big. Importance 1-10 per viewer (player / ally / threatened), how often it plays, device mix. If a gameplay system is attached, read its truth (area, speed, fuse, radius) from config; never set or invent it. If none is attached, write "visual only, no gameplay" and plan size from the frame script.
2. **Context and technique (the chooser, §3).** Pick the context, then the tool for each part of the picture. Name the crafts that join (animator for pops, rigs and cutscenes; sound designer always; UI side for world→HUD hand-overs) and plan them on one shared beat list.
3. **References.** Open 1-3 pro frame scripts of the same type (`knowledge/reference/vfx/training/frame-scripts/`, S and A first). Note peak coverage, peak time, tail and layer list.
4. **Our frame script** at the game camera (format and screen-size math: `vfx-craft/references/plan-and-spec.md` §A-B): 6-10 moments in ms with screen %, shapes, colours, brightness, motion. Compare peak, timing and tail with the references and fix the plan, not the reference. Then go to `vfx-craft`.

## 3. Technique chooser
**Context sets budget and freedom:**
| Context | Examples | Allows |
| --- | --- | --- |
| Gameplay moment | weapon hit, pickup, object break, sell | short, repeats, phone budget, many at once; merge windows and caps |
| World event | tsunami over the city, meteor shower, stage boss | rare, big, seconds long, everyone sees it; bigger budget, level of detail by distance, shake allowed |
| Object change | wall completes and transforms, building upgrade, freeze, charge | the object itself changes; a flash hides the swap; the animator helps with the pop |
| Cutscene | opening film, stage intro | camera is ours, plays once; heavy assets allowed (even mesh flipbooks, loaded and unloaded); frame per shot; shots, cue ids and times come from the film director's shot list (`film-craft`) |
| UI | button, HUD pop, counter, reward screen | screen layer: build with `ui-basics`; feel rules from here |

**The shape the eye must read picks the tool (one effect can use several):**
| The player must see | Tool (`vfx-craft/references/techniques.md`) |
| --- | --- |
| many small, soft or chaotic bits (fire, smoke, sparks, magic dust) | particles (T1) |
| one big **solid** shape that keeps its form while it moves or grows (wave, dome, tornado, pillar) | mesh + particles on top (T2, T5) |
| a line between two points, a ribbon behind something (laser, arc, sword trail) | beam or trail (T3) |
| an existing object changing (completes, upgrades, charges) | change the object + flash to hide the swap (T4) |
| the ground or a wall looking damaged (crater, crumble, rubble, flying chunks) | fake destruction with the effect's own parts (T8) |
| a feeling over the whole screen (rare heavy moment) | camera and post effects (T7, §4) |
Under ~10 studs, prefer particles over meshes for rings, slashes and streaks (pros do).

## 4. Feel and safety rules
- **VFX is visuals only.** An effect never adds or changes gameplay: no damage, no knockback, no hit areas, no new gameplay numbers, and it never touches real game parts (map parts, players, gameplay objects). **Fake destruction is part of VFX and encouraged:** the effect may spawn its own cosmetic parts (rock rings, crater rubble, floor crumble, flying chunks, cracks) that look like damage, then clean them up (`vfx-craft` T8). You never need to be told this per task.
- **Truth first, only when gameplay exists.** If the effect shows an existing gameplay system, its drawn area matches that system (edge ±5%, read from config) and the big layer fires only on a confirmed success. If no gameplay is attached (tests, showcases, cosmetics), there is no truth area: do not draw radius rings for a value you took or invented; size by the frame script. Gameplay accuracy > readability > theme.
- **Importance drives everything:** size, peak brightness, saturation, sharpness and lifetime rise with the rating; the brightest pixel belongs to the top priority (threat > own feedback > pickups > others' effects > ambient).
- **Weight is not intensity.** Fix a flat effect with outcome link, truth, readability and timing before making it bigger (`juice-repetition-sync.md`).
- **Shape language:** sharp and downward = threat, round = safe; outward = burst, aimed = streak, inward = gathering. One focus, one primary shape, one hue + one accent.
- **Timing shape:** anticipation → 1-3 frame punch → soft tail; frequent effects are shorter and quieter; telegraphs lead by 600-1000 ms and end on the damage frame.
- **Camera shake is occasional :** none on frequent effects or from other players; only rare heavy moments (rating ≥8 or the owner asks); off under reduced motion. Hit-stop never on explosions.
- **Flash safety** on the composite screen: design ≤2 large flashes per rolling second, never >3; no saturated red flashes; Bloom and colour pulses count.
- **Colour is never the only channel.** Reduced-motion and reduced-flash variants keep all information.
- **Repetition:** frequent effects get a merge window, a live-copy cap and variants.
- **Paid random items:** odds first, identical windup for every outcome, no near-miss, no celebration below cost.
- **Sound :** the sound brief says what is on screen and when; the sound designer chooses the sounds. Picture punch and sound transient share one trigger.
- **Claims:** never say you saw, played or measured anything without a capture or log in this task; never invent asset ids, limits or results. Label checks gate-verified / MCP-verified / owner-confirmed / not verified.

## 5. Read this file when
| You need | Open |
| --- | --- |
| Perception: shape, value, colour, timing, readability | `references/elements.md` |
| Recipes by game event (hit, blast, break, ability, warning, pickup, reveal, movement, ambient); pure UI moments moved to `ui-basics` | `references/moment-recipes.md` |
| Shake, hit-stop, FOV, slow motion, flash frames, post pulses, player options | `references/camera-and-screen.md` |
| Composite frame, clutter, prominence, stage palette | `references/scene-and-clutter.md` |
| Repetition, merge windows, escalation, picture-sound sync | `references/juice-repetition-sync.md` |
| Reviewing an effect (findings, ranked fixes) | `references/review.md` |
| Genre presets, older effect-card fields | `references/effect-card-and-presets.md` |
| Pro frame scripts by type | `knowledge/reference/vfx/training/frame-scripts/` |
| Ambient motion in a stage: what moves, its cause, anchor and fallback (written by the environment designer; you fill the `vfx:` keys) | `templates/environment/ambience-map.md` |
| Building it in Roblox | **`vfx-craft` skill** |
| Testing these skills | `evals/briefs.md`, `knowledge/reference/vfx/training/benchmark.md` |
Older numbers in these references that conflict with `vfx-craft` (emitter caps, layer caps) are superseded (§7).

## 6. Planning self-check
- [ ] Three answers, ratings per viewer, rate, gameplay truth from config.
- [ ] Context and tool named for every part; joining crafts named; one shared beat list if more than one craft.
- [ ] Frame script at the game camera with screen-size math, compared with ≥1 pro frame script of the same type.
- [ ] Camera channels allowed by §4; sound brief written as "what is there".
- [ ] Flash count, colour backup, reduced-motion variant; paid-random rules if relevant.
- [ ] After `vfx-craft`: the build matches the frame script (layer per moment); then one capture.

## 7. v2 overrides
| Old | v2 | Why |
| --- | --- | --- |
| Storyboard / 2D look target | written frame script | no 2D mock-ups: the written frame script is the target |
| Shake from rating 3 | shake occasional (§4) | rare heavy moments only |
| "≤4 layers, hero ≤5 emitters" | `vfx-craft` budget (textures + live particles) | pro data |
| Judge in daylight first | dark test place (watch for dark-only effects) | glow and contrast read better in the dark |

## 8. Game specifics
- **Game and style:** read `knowledge/design/game-profile.md` (pillars, art style, camera). Where it is silent, house style is a PROPOSAL: ask the owner before building.
- **Where to build and test:** a separate, dark, plain test place, never the game place (the game profile names it). Judge in the dark first, then check in the game's own lighting.
- **Decisions:** VFX decisions for this game live in `knowledge/design/decisions.md`; the owner's final look closes every effect.
- **Files per effect:** `content/vfx/<effect-id>/` (brief.md, frame-script.md, spec.json).
