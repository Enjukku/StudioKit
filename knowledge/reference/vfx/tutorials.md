---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20

# VFX tutorial lessons (Roblox practitioners, from transcripts the owner supplied)

Raw transcripts are not stored (other people's text). Paraphrased craft lessons only. Trust: [practice], working Roblox VFX artists, values said aloud while tuning by eye, so treat numbers as **starting points**. Cross-check column: building-blocks.md (BB, 30 pro effects) and the API card (`roblox-vfx-api-card.md`).

## Sources
| ID | Video (as given 2026-10-20) | Effect | Value for us |
| --- | --- | --- | --- |
| TV1 | "What new VFX artists should know" (artist with commission work) | properties, beams, trails, plugins, lighting | property semantics, lighting rules |
| TV2 | Twist (≈2 yrs, works on The Forge): aura tutorial | anime aura with specs, glow, ground, beams, snow | loops, glow, ground, layering |
| TV3 | Twist: explosion | flash, fireball, smoke, embers, wind, ring | **impact recipe** |
| TV4 | Twist: wind-breathing slash | layered slash particles, beam arcs, tweens, ground, debris, highlight | **slash recipe**, scripted beams |
| TV5 | Twist: beam attack | layered beams, start/end effects | **beam recipe** |
| TV6 | Twist: lightning strike | bolt, impact, ground lightning, debris parts | **strike recipe**, debris script |

## A. Universal craft rules (n = videos that say or show it)
| ID | Rule | Numbers | n | Data check |
| --- | --- | --- | --- | --- |
| TU-01 | Every particle fades in or out by size or transparency; nothing pops | — | 4 | BB: most curves end at 0 |
| TU-02 | **Impact effects may appear instantly** (no fade-in) for punch; looping/idle effects fade everything | — | 3 | — |
| TU-03 | LightInfluence 0 on VFX (scene light is for map builders) | 0 | 4 | BB 979/980 |
| TU-04 | LightEmission 1 removes the dark parts of a texture (additive); then **Brightness acts as opacity** for single-colour layers, easier than editing transparency curves | LE 1 | 3 | BB LE 0 45%, 1 37% |
| TU-05 | Never Speed 0 with VelocityParallel/Perpendicular (particle vanishes); use 0.01 | 0.01 | 3 | API card |
| TU-06 | ZOffset layers: between stacked layers a difference of 0.001 is enough; raise 2-4 (glows higher) only to sit over characters/ground; on flat ground layers keep ZOffset 0 and lift the attachment slightly (ZOffset clips into the ground) | 0.001 / 2-4 | 4 | BB flash +1.8 to +3.7 |
| TU-07 | Many textures per job: stack 2-5 textures (base, dark twin under, bright thin over, faint wide under) rather than one | — | 5 | BB 27 emitters, ~11.5 textures |
| TU-08 | Dark twin: same/similar shape, darker colour, under the bright layer, for contrast and shape | — | 4 | BB dark underlay job |
| TU-09 | Randomise per particle: rotation, size (envelope), lifetime and speed ranges; same-speed layers look fake | rotation ±10-45°; wide lifetime ranges on flashing specs | 5 | — |
| TU-10 | Size curves: fast growth at start, slow at end (ease-out), not linear | e.g. 60-70% size early | 4 | BB matches |
| TU-11 | Burst outward = high Speed + high Drag (fling, then brake); slow constant speed reads weak | Speed 100-150 + Drag 5-7 | 3 | BB spark Drag 5.5 |
| TU-12 | Flash = shortest layer: "if you can make out its shape, it lasts too long" | 0.03-0.05 s | 3 | BB S+A flash ~0.12 s (conflict, see D) |
| TU-13 | "One-two" punch: second flash layer slightly longer than the first; one grows, one shrinks | — | 2 | — |
| TU-14 | Glow over everything: Speed 0, FaceCamera, high ZOffset, constant size, V-shaped transparency (rise fast, fade slow), subtle | life 0.8-1 s | 4 | — |
| TU-15 | Steady glow without flicker: Rate 2 with Lifetime 1 and a V transparency curve so two overlapping particles sum to constant | — | 1 | — |
| TU-16 | Flash/sparkle specs: size curve with random bumps + wide lifetime range so they twinkle out of sync | — | 3 | — |
| TU-17 | Smoke: darker, under the fire, more transparent, lasts longer than flames; embers last as long as smoke | — | 2 | — |
| TU-18 | Fire textures need internal contrast; flat white textures look flat | — | 1 | — |
| TU-19 | Mixing a realistic smoke under stylised (anime) layers works if subtle; mixing styles is risky | — | 3 | owner house style anime |
| TU-20 | 3D feel from flat sprites: emit rings with VelocityParallel/Perpendicular + SpreadAngle 180 instead of FaceCamera discs | — | 3 | — |
| TU-21 | Wind: VelocityPerpendicular, spread 180, emit ~5 small with very random size + RotSpeed ±20, plus 1-2 large | — | 2 | — |
| TU-22 | Rainbow/lens flare/sun-rays: very transparent background accent only; stars often beat lens-flare textures | — | 3 | — |
| TU-23 | Shockwave rings: subtle, linear-ish growth, one emitted, random rotation | size 12-15 | 3 | — |
| TU-24 | Static variety: put variants in one sheet, FlipbookMode Loop, framerate ≈0.01, StartRandom on = one random still per particle (one texture load) | — | 3 | ZO-10 |
| TU-25 | Disable and re-enable all emitters together after editing, or offsets you will not see in game hide in the preview | — | 1 | — |
| TU-26 | Emit shape: Disc (circle) or Sphere for area effects; Box shows its corners at high rate | — | 2 | — |
| TU-27 | Particle budget per emitter: Rate × Lifetime ≈ under 50 live; most layers 1-10; one effect example 63 live total | — | 2 | BB ~620 live median (conflict, see D) |
| TU-28 | Use a reference clip for anything you are unsure of; copy pros for practice | — | 3 | workflow |
| TU-29 | Lighting: build in **default (daylight) lighting**; dark lighting only to showcase. Light-to-dark rarely breaks an effect, dark-to-light often does (except dark/shadow effects) | Bloom and ColorCorrection only small (CC ≈0.1 is already strong) | 2 | **conflicts with owner dark test place, see D** |
| TU-30 | Glows need textures with soft fade edges; sharp-edged circles need huge sizes to read as glow | — | 3 | — |

## B. Moment recipes (layer order as built; values said aloud)
| Recipe | Layers (job: key values) |
| --- | --- |
| **Explosion (TV3)** | flash: solid star/burst texture (no holes), life 0.03-0.05, ZOffset up, shrinks · flash 2: slightly longer · fire ring: VelocityParallel, spread 180, Speed high random, Drag high · fireball body: FaceCamera, low speed, size ease-out (≈7.5) · dark smoke: same texture black, under, more transparent, longer life · embers: off-centre spec, small, fade in, lower drag, life ≈ smoke, rise · sparkle specs: size bumps, Speed 35-50, random life · vertical smoke streaks pointing outward (rotation −90, squash) · glow (TU-14) · shockwave ring (TU-23) · wind (TU-21) + dark large wind · faint rainbow flare · embers above |
| **Slash (TV4)** | slash particles: life 0.2-0.3, Speed 0.01, VelocityPerpendicular, EmitCount 1, RotSpeed well above 360°/s for short lives, layered: base colour slash, dark twin (ZOffset −0.001), bright thin highlight slash, noisy faint slash, 1.5-size randomised extra with EmitCount ~3, a slower trailing copy; transparency fade delayed (hold 0 then fade) · beam arcs: 2 attachments ±9.5 studs, CurveSize = diameter × 2/3 for a semicircle, FaceCamera, Segments up to ~50, widths tweened from 1.25× to 0 in the slash time, attachment rotated by tween ≈175° (not 180, avoids reverse spin); many thin beams: black under, bright over, small ones trailing outside · sparks along the arc: parts with emitters, life 0.4-0.6, LockedToPart, acceleration along arc, star with 2 size bumps · impact: star, life 0.05, grow + transparent, second one shrinks · Highlight fill colour tweened to 0.6 and back (circular easing) · ground: wind perpendicular, flat shockwave linear, stylised + one realistic smoke, neon wind meshes · debris: leaves/rocks, Speed 100, Drag 7, few |
| **Beam attack (TV5)** | main flat beam: opaque base texture, ends transparent, TextureSpeed ≈1.3-2, each layer a different speed · wavy layer under, small · faint energy layer ≈0.05 visible · VelocityParallel spiky lines along the beam (Loop random flipbook, black, size shrinks) · stars FaceCamera · crystal 8x8 flipbook Loop ≈100 fps · large squashed stars behind · **start**: crescent/wind ring (perpendicular, size ≈7, grows), impact flipbook + black twin, flickering glow + flare, flat shock rings · **end**: impact, glow, glass shards (Speed high, Drag ~6, ~20), circle impact, specs at constant speed, dark smoke unlocked so it lags, halftone barely visible · side wind beams (3 offset attachments, curved, brightness 0.1) · widths/brightness tweened in on start, set to 0 on end · counted 63 live particles total |
| **Lightning strike (TV6)** | bolt: FaceCameraWorldUp, stylised textures (realistic thin bolts look bad), ≈10 studs radius (≈4× player height), touching the ground · impact: life 0.05, 8 size, shrinks + a flipped growing copy · 3D sparks VelocityPerpendicular spread 180, darker copy for contrast · glow life ≈1 fading · quick bright flash glow · faint rainbow · ground ring perpendicular, fast growth, short · ground lightning: emitted over a duration, Disc shape, fast ones (short life) + slow ones, arc textures flipped to lie on the ground, FaceCameraWorldUp · dust: realistic smoke FaceCamera ZOffset 4 + dark smoke · no fade-in on impact layers · sun-ray texture with negative ZOffset, squashed, rotation limited so none spawn under ground · ground cracks: grow at start then stop, no ZOffset, transparent, darker · long-lasting tiny specs (no LE), drag, random life · slower impact that shrinks + rotates inward · outward smoke ring perpendicular, Speed ~150 + Drag · debris parts with trails flung by AssemblyLinearVelocity, random size 0.5-2.5, random rotation, ground colour, Debris service cleanup |
| **Aura (TV2)** | specs flying around (size fade preferred over transparency for long lives) · larger transparent specs · off-centre textures with rotation ±45 to swirl · PointLight · glow ZOffset 2-4 (TU-14/15) · RNG-game look = spec spam · faint ambient smoke, Sphere shape · ground: perpendicular, Speed 0.01, rings growing fast at start, faint glow, spiky ring texture, magic circle very faint · spiral beams: CurveSize, FaceCamera, segments up, textures that reach both edges, mirrored copy with negative curve · lens flare behind, faint · snowfall from a disc · Highlight fill on the body · per-emitter Rate × Lifetime kept low |

## C. Scripting patterns (wiring notes for VfxPlayer, not design)
- Burst emitters carry an `EmitCount` attribute; one function loops descendants and calls `Emit(EmitCount)`; emitters without it are `Enabled` for an `EmitDuration` then disabled. (TV4, TV6; matches training dumps and ZonitoVFX.)
- Clone then wait one frame before `Emit` or some emitters do not fire (TV6; ZO-04).
- Beams: store Width0/Width1 as attributes, set start width, tween to 0 (or 0 → size on start). Rotate a parent attachment by tween for sweeping arcs.
- Cleanup with the Debris service, not a delay in a player-owned script.
- Note: TV6 played VFX on the server for simplicity; our rule stays client playback from one network event (ZO-04, AGENTS §2).

## D. Conflicts and open points
| # | Tutorials say | Other evidence | Proposed handling |
| --- | --- | --- | --- |
| 1 | Build in default daylight, never in the dark (TV1, TV2) | Owner 2026-10-20 wants a dark test place to see effects better | **Decided: dark test place is the main build and judge place.** Watch for effects that only work in the dark |
| 2 | Flash life 0.03-0.05 s (TV3, TV4, TV6) | BB S+A impact-flash median ≈0.12 s (lifetime of emitters classed "impact burst", which also holds the shape, not only the flash) | Treat 0.03-0.05 as the white flash, 0.1-0.2 as the impact shape; split the BB job before deciding |
| 3 | ≤50 live per emitter; one beam effect 63 live total | BB median ≈620 live at peak (estimate from Rate × Lifetime + EmitCount) | Both can hold: many emitters × few particles. Measure in Studio (Q-71) |
| 4 | Rate max "about 555" (TV1, unsure) | API card: 400/s per emitter, 100/s on mobile | Use 400 / 100 |
