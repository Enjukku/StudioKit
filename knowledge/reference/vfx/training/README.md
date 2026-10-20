---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-16

# VFX training library: what pro Roblox VFX are made of

**Paths below that start with `output/` (training dumps, captures, library thumbnails) are per-game working output: optional, regenerable from the source folder, git-ignored and not shipped with the kit.**

Source: the owner-supplied folder `VFX_Training` (per-game input, not shipped with the kit; 38 files, graded by the owner: S = incredible / very polished, A = solid, B = alright, C = okay but improvable, Unknown = ungraded). These are other creators' effects. **Study only.** Their textures and meshes must not ship in our game unless the owner holds a licence (`rules/original-content.md` line 16). Even the "OPENSOURCE" places carry no licence text we have checked. This is listed as an open question.

| File | Covers |
| --- | --- |
| `sTier-teardown.md` | 7 S files, ST-01..ST-28 recipes, texture reuse, fireball-complaint map |
| `aTier-teardown.md` | 10 A files incl. the StylizedFireballsTrails deep dive, AT-01..AT-30 |
| `bTier-teardown.md` | 10 B files, BT-01..21, weaknesses BW-01..09 |
| `cTier-unknown-teardown.md` | 4 C + 7 Unknown, CT-01..26, CW-01..12, projectile anatomy |
| `../13-practitioner-optimization-zonito.md` | optimization notes from the artist behind ZonitoVFX |

Raw data (untracked `output/`, regenerable from the source folder): `output/vfx/training-dumps/` holds `outlines/` (instance trees with all VFX props, long sequences cut at 140 chars), `scripts/` + `scripts_index.json` (252 unique scripts, 180 non-library), `attributes/` (EmitCount/EmitDelay/... decoded, matches Studio counts), `json/` (full data incl. untruncated sequences). Motion captures: `output/vfx/training-captures/<effect>/` (27 fps frames, clip.gif, sheet.jpg).
Tools (session scratchpad, to be promoted to `tools/vfx/` if kept): `rbxbin.py` (binary .rbxm/.rbxl reader, pure Python), `outline.py`, `attrs.py`, `wrap_roots.py` (wraps multi-root .rbxm so Rojo can sync it), `record.py` (screen recorder for the Studio viewport, about 27 fps).

## The 12 things that separate S/A from our failed fireball (cross-tier, evidence in the teardowns)
| # | Pro practice | Numbers seen | Our fireball v1-v4 |
| --- | --- | --- | --- |
| 1 | **Many thin single-job layers** | 20-150 emitters per effect, each with one job (core, hot pulse, glow, flare, wisps, embers, rings, specs, smoke, dark rim) | 3-6 layers |
| 2 | **Brightness is the glow dial** | LightInfluence 0 on ~100% of S emitters; Brightness median 3, up to 15-50 on tiny sparkles; the same texture emitted 2-3× at Brightness 15/5/1 with ZOffset steps (ST-01, AT-03) | LightEmission only, Brightness 1, Neon parts |
| 3 | **Dark twin / dark underlay** for shape and contrast | same texture at Brightness 0-0.5 one ZOffset behind; pure black sprites at Transparency 0.4; negative LightEmission is rare in S (1 of 492) but common in A/B/Unknown | none: everything additive, so it washed white |
| 4 | **Painted textures, never primitives** | hand-painted flame tongues, wisps, crescents, star flares, splash shapes; one effect reuses a small texture set | pixel sprites + Roblox balls/cubes |
| 5 | **Motion read from direction-locked layers** | VelocityParallel streaks (Orientation 2) + Squash 0.1-0.7; trails; star flare at the head; Bezier flight paths; head is a flare/converged trails, not a ball | camera-facing round sphere |
| 6 | **Trail stacks with textures** | 2-4 Trails on one attachment pair (soft, textured at Brightness 15, outline); WidthScale 0 → peak taper; TextureLength 14-48 | one plain colour Trail |
| 7 | **World-space rings and wakes** | disc emitters with Speed ~0 not locked to the part leave expanding rings behind the moving head (AT-05) | none |
| 8 | **Eased size curves** | 60-70% of final size in the first 10% of life (keys at t=0.0004/0.0035/0.013), pop-dip-rebound shapes; every sprite fades in and out | 2-3 key linear curves |
| 9 | **Impact ladder over 4 timescales** | flash 25-50 ms (huge, ZOffset on top) → shape 70-120 ms → sparks/smoke 0.4-1.8 s → afterglow 1.5-8 s | flash dome + one burst |
| 10 | **Sparks with physics** | Speed 20-500 + Drag 5-15 + Acceleration down: fly, brake, fall | constant speed |
| 11 | **Colour moves inside a life** | yellow → orange → violet; orange → red → black; warm + cool point lights together | one hue per layer |
| 12 | **One trigger, ms choreography, data-driven** | `EmitCount`/`EmitDelay`/`EmitDuration` attributes per emitter, fired by one `EmitAll(part)` call (ZonitoVFX); screen channels (FOV 67→60 + blur 10→0 in 100 ms, tint flash, vignette, rotation-only shake fadeOut 0.25-0.6) all distance-gated | hand-written tween script per effect |

## Rules of ours that this contradicts
- **Emitter budget.** Our VFX card capped an impact at ≤5 emitters at High. Pro effects use 20-150 thin emitters. The practitioner notes (ZO-01, ZO-11) say emitter or particle count is rarely the real cost: unique textures (memory) are. The budget rule should move from "emitter count" to "unique textures + live particles near the camera". This needs a Studio measurement before it changes (`07-roblox-performance-accessibility.md`).
- **"LightEmission 1 for glow".** Pros use LightInfluence 0 + Brightness > 1 and keep LightEmission mostly 0-1.

## Capture method (proven 2026-10-16)
1. `.rbxm` models: serve through a throwaway Rojo project (`wrap_roots.py` first), disable all fx, show one model, fire `EmitAll`. Script-driven showcases need their original place (missing `workspace.Map`, `Ignore`, PlayerGui).
2. `.rbxl` places: open in Studio (Ctrl+O), Play, send the ability key with Studio MCP `user_keyboard_input` (find the key in `scripts/`, e.g. the water place fires on `E` via the `Ei` module), aim the mouse at the ground first.
3. Record with `record.py <out> 3.5` started just before the key. Studio MCP `screen_capture` is NOT usable for motion: it moves the camera and particles do not update (heads vanish).

## Seen in motion (2026-10-16): what the clips confirm
Source: `output/vfx/training-captures/` (30 effects recorded, 2 partial, 6 not capturable; see its INDEX.md) and the "Seen in motion" sections of each tier teardown. Contact sheets were reviewed as stills, so timing is ±1 cell.
| What separates S from the rest | S (seen) | A / B / C (seen) |
| --- | --- | --- |
| One hero silhouette | one clear dominant shape fills the frame, 3-6× the object's size | A: busy spark clusters with no dominant shape. B/C: small and dim |
| Hot core + accent | a tiny near-white core inside a strong colour, plus one hot accent hue (fire + ice, purple + yellow) | mostly one hue (B: every captured effect) |
| Every glow has a spike | cross flares, star decals, rings, streaks on each glow. **Round heads are fine when they carry a flare and a long textured tail** (Elemental fire head) | glows without spikes; thin heads (ProjectilePractice), plain dot trails (blue pewpews) |
| Timing shape | about 0.8 s warning → a peak lasting one cell → a soft 1-3 s tail (rings, sigils, scorch, smoke) | B: one burst for 5-8 frames, then empty |
| Ground contact | floor rings, sigils, splash domes, scorch | often missing (Emerald: floor glow only) |
| Flash safety | big hits use a white flash or tint for one frame | C/Colours: a full-screen blue tint, which fails our flash rule |
Corrections to the teardowns: S heads can be round (see above). Astral Sword's sky darkening is the showcase lighting, not the effect. The 32-ribbon Meteor skirt is not visible at game distance. Negative LightEmission, Brightness stacks, FOV/blur/shake and 40 ms flash layers are still unseen: they need a close A/B capture at 60 fps.
Our failed fireball against this list: no spike or flare, no white-hot core, no textured tail, no hot accent, no ground contact, no warning, and too small for the frame.
