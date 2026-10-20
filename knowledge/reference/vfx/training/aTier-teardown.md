---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: vfx-designer · claude-sonnet-5-5 · medium · 2026-10-16

# A-tier teardown (owner grade: "solid, very good")

Source: `output/vfx/training-dumps/` outlines + scripts + `json/` for the 10 `aTier__*` files. All property values are read from the dump [data]. Role names, "why it works" and anything about how it renders are [inference] until a Studio capture confirms them. Nothing here was seen in motion.

**Decode key.** Enums are numbers in the dump; mapping per Roblox docs [spec recall]: FlipbookLayout 0 none, 1 2x2, 2 4x4, 3 8x8. FlipbookMode 0 Loop, 1 OneShot (framerate ignored), 2 PingPong, 3 Random. Orientation 0 FacingCamera, 1 FacingCameraWorldUp, 2 VelocityParallel (stretch along travel), 3 VelocityPerpendicular (flat disc/ring/slash plane). EmissionDirection = NormalId (0 Right, 1 Top, 2 Back, 3 Left, 4 Bottom, 5 Front). Material 256 Plastic, 288 Neon, 1088 Metal, 1568 Glass. Trail/Beam TextureMode 0 Stretch, 1 Wrap, 2 Static. Size/Transparency/Squash = [time, value] keypoints. "Life x-y" = Lifetime. "live" = Rate x mean Lifetime. Emitters whose LightInfluence is not listed are 0 [data: omitted = default 0].

**Scope limits.** (1) Emit attributes (EmitCount, EmitDelay, EmitDuration, EmitType, `_vfxEditor*`) come from `output/vfx/training-dumps/attributes/aTier__*.txt` (coordinator-verified against Studio); they are folded into each section below as [data]. Attributes are read by `EmitAll`/`Effects.Emit`: `Emit(EmitCount)` after `EmitDelay` s, and if EmitDuration is set the emitter is enabled for that long. (2) Texture sizes/pixels are not in the dump; texture roles are guessed from emitter names, sizes and layout. (3) Flipbook "incompatible" flags in the dump only mean textures were not loaded. (4) Colour sequences longer than 5-6 stops are truncated in the outline text.

## Files overview

| File | Kind | Emitters / other | Scripts that matter | Light + post |
| --- | --- | --- | --- | --- |
| StylizedFireballsTrails | 2 fireball rigs (purple-orange, orange-blue), no script | 82 PE, 6 Trail, 4 PointLight | none | 2 PointLights per rig |
| Flame_Beziers | "Barrage" ability: 10 flaming missiles on Bezier arcs, crater | 38 PE, 1 Trail, 1 PointLight | Barrage, ZonitoVFX, Crater, Bezier, shake presets | Bloom 1.5/size 20/thr 1, CC contrast .32, DoF, Atmosphere |
| Slashes | IceSlash + LeafSlash melee sweeps | ~75 PE, 8 Beam (150 seg) | Slash.luau, Effects.luau | Bloom 1/24/thr 2, SunRays .1, DoF; vignette ImageLabel |
| Ayato_Showcase | sword combo (Q) + charged dash (E), 6 SFX | 84 PE, 3 Beam (500 seg), 6 PointLight | Showcase, ZonitoVFX, CameraFX, ScreenSpace | PointLights 1 / range 7 |
| Zonito_Music_OS | "Music" ability E: twin notes clash, 12 mini-notes | 122 PE, 2 Trail, 6 PointLight | Clash, ZonitoVFX, shake presets, wind | Bloom 1/24/thr 2, CC contrast .1 |
| Death_FX | death burst on a dressed glass avatar | 8 PE | none (default Animate only) | none |
| Colouring_Practice | trail + impact (yellow to green) | 27 PE, 2 PointLight | none | lime/green lights |
| Constellations | star-burst hit, halftone vs plain | 29 PE (2 variants) | none | 1 PointLight each |
| nnoonooooo | blue galaxy projectile + impact | 10 PE, 1 Trail | none | blue PointLight |
| soear | purple lightning spear + aura | 15 PE, 2 Beam, 1 MeshPart | none | violet PointLight |

---

# 1. StylizedFireballsTrails (deep dive; the answer to our failed fireball)

**What it is.** Two anchored Neon, Transparency-1 `ColouredFire` parts. Part 1 palette purple/magenta + brown (`[148,0,161] > [136,59,9] > [179,0,179]`, every emitter Brightness 7.5). Part 2 palette orange `[255,65,17]` with a blue/violet band in the middle (`[255,65,17] 0 > [215,105,14] .45 > [104,29,255] .49 > [28,56,211] .57 > [128,66,15] .67 > ... > orange`), and per-layer Brightness. Each rig has attachments: **D1** (continuous travelling ball, enabled), **E** (15 emitters, Enabled=false = impact/explosion burst), **T** (Trail pair A1 at 0, A2 at +6 studs X, 3 Trails), **D2** (2 locked core flicker emitters), plus 2 PointLights. No script ships with it, but attributes carry the timing [data]: **D1** emitters: EmitCount 0, EmitDelay 0.65, EmitDuration 2.0 (travel layers switch on 0.65 s after trigger and run 2 s; `flare` EmitCount 5, EmitDuration .04). **D2** (locked flicker core): EmitDelay 0.95, EmitDuration 2.0 (starts 0.3 s after D1). **E**: Emit + enable 0.35 s: SP1 12, SP2 5, CH1 4, S1/S2 6 each, F1/F2/F3 5 each, FB1/FB2 12 each, SH1/SH2 5 each, flare 5 (EmitDuration .04); with Rate ~40 on top for .35 s. The Part has an `AllAttributes` demo-motion table: Transparency 1 > 0 (delay .4, 2 s), Move (0,-25,-100) over .8 s (about 100 studs forward; fireball demo flight) [data]. So the sequence is: build-up 0-0.65 s (nothing but the part), ball layers from .65, core flicker from .95 [inference on meaning].

**Live budget (computed, Part 2 D1+D2, enabled):** 26 emitters, about 236 live particles + 3 trails + 2 lights; E burst adds about 200 live for under 0.6 s. This is far above our "<=3 emitters per blast, <=64 per emitter at low" rule, so the recipe must be reduced, not copied (see AT-30).

### 1a. Travelling-ball layer stack (Part 2 D1/D2, Lighting values as shipped)

| Layer | Job [inference] | Texture | Sheet | Size (studs) | Life | Rate / live | LE | Br | Drag / Speed | ZOff | Other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SP1 | inner sphere body | 16865903588 | 4x4 OneShot | 4.27 flat | .25-.35 | 20 / 6 | -0.3 | 5 | 0 / ~0 | 0 | Squash +.25, Rot +-360, TimeScale .8 |
| SP2 | outer sphere body | 14594832130 | 4x4 OneShot | 8.53 flat | .25-.35 | 20 / 6 | -0.3 | 15 | 0 / ~0 | 0 | Squash +.25 |
| CH1 | hot core pulse | 14032901187 | none | 0 > 9 | .25-.35 | 20 / 6 | +1.0 | 2 | 0 / ~0 | 0 | Transp 0 > 1, Squash -.05 |
| flare | star flash | 18457400581 | 2x2 | 0 > 10 > 0 (peak at 55%) | .1 | 12.8 / 1.3 | +0.3 | 7.5 | ~0 | 0 | Rot +-360 |
| S1 | additive spark glow | 9612436472 | 4x4 | 3 flat | .65-.85 | 20 / 15 | +1.0 | 4.5 | 1 / 3-7 | -2.0 | LockedToPart |
| S2 | dark twin of S1 | 11845281419 | 4x4 | 3 flat | .65-.85 | 20 / 15 | **-1.0** | 4.5 | 3 / 3-7 | -1.9 | LockedToPart; sits 0.1 in front |
| SH1 (x2) | big flung embers | 15419189769 | 4x4 | 2.67 > 0 | 1-2 | 9.6 / 14 each | -0.3 | 5 and **0.5** | 2 / 15-21.7 | 0 | Squash +.15; second copy is a dark twin |
| SH2 (x2) | small embers | 11133563100 | 4x4 | .69 > 0 | .65-.85 | 9.6 / 7 each | -0.3 | 5 and **0.5** | 0 / 15-21.7 | 0 | Squash +.15 |
| F1 | flame lick | 11534281007 | 4x4 | 2.67 flat | .35-.55 | 10.2 / 5 | -0.3 | 5 | 0 / 8-13 | 0 | |
| F2 | flame lick, fades | 17507124046 | 4x4 | 2.67 flat | .45-.55 | 10.2 / 5 | -0.3 | 5 | 2 / 10-15 | 0 | Transp 0 > 1 |
| F3 (x3) | flame body | 12780347743 | 4x4 | 2.67 flat | .65-.85 | 20.5 / 15 each | -0.3 | 5, 5 and **0.03** | 0 / 8-11.7 | 0 | third copy near-black twin |
| H1 | halo ring, large | 15386766846 | 4x4 | **-0.27 > 11.3** | .65-.85 | 12 / 9 | -0.3 | 15 | 0 / ~0 | -0.3 | SpreadAngle 0 |
| H3, H4 | halo rings, medium | 17723930633, 16940393267 | 4x4 | -0.27 > 5.65 | .65-.85, .35-.65 | 12 / 9, 6 | -0.3 | 15 | 0 / ~0 | -0.3 | Transp .16 at 95% > 1 |
| H5 | halo, additive, huge | 17860014905 | 4x4 | -0.27 > 17.8 | .65-.85 | 12 / 9 | +1.0 | 15 | 0 / ~0 | -0.3 | |
| H1/H3/H4/H5 again | same four, **Orientation 3**, SpreadAngle 5 | same ids | 4x4 | same | same | 12 each | same | 15 | ~0 | -0.3 | side-view discs |
| mainH | head glow on the ball | 15386766846 | 4x4 | 0 > 4.1 (14%) > 5.9 | .3-.4 | 12 / 4 | +0.3 | 4 | ~0 | **+1.0** | LockedToPart |
| M4 (D2) | locked flicker glow | 14032952906 | none | 4.36 flat | .15 | 60 / 9 | +1.0 | 0.3 | ~0 | -0.3 | Transp .7 flat, LockedToPart |
| Space Star (D2) | locked flicker star | 79705556595545 | 4x4 | 4.36 flat | .15 | 60 / 9 | +0.3 | 3 | ~0 | -0.3 | LockedToPart |

Group readings (10 jobs): core (SP1/SP2/CH1), glow (S1, M4, H5), flare (flare, Space Star), wisps (F1-F3), embers/specs (SH1/SH2), smoke/dark body (S2, near-black F3 and SH twins), halos (H1-H5, billboard + perpendicular sets), head (mainH), trail (3 Trails), lights. [inference]

### 1b. Trail stack (T attachment; same A1/A2 pair, Lifetime .75 s, FaceCamera true, MinLength .0333, MaxLength 0)

| Trail | Texture | TextureMode / Length | Width seq | Transparency | Brightness | LE | Color |
| --- | --- | --- | --- | --- | --- | --- | --- |
| T1 | none (flat colour) | Stretch / 1 | .55 > 0 | .7 flat | 3 | .35 | multi-stop warm/cool ramp |
| arcana_orb_galaxyTrail_color | 119913821922431 | Stretch / **2** | 1 > .81 (57%) > 0 | 0 | **15** | .55 | same |
| BeamFaded Outlines Inward | 86470467217654 | Stretch / 1 | 1 > 0 | 0 | 3 | .35 | same |

Part 1 trails use the same three with width .31 / .71 / .53 and Brightness 3 / 15 / 3 [data]. Trail colour ramp (Part 2): `[255,60,11] 0 > [196,72,23] .25 > [114,32,255] .32 > [255,126,33] .39 > [30,41,255] .67 > ...`; it alternates warm and cold across the trail length, so the ribbon reads as flickering plasma, not a flat stripe.

### 1c. Impact burst group E (Enabled=false; Rate and Flipbook numbers are ~1.6x the D1 values, i.e. a scaled copy [inference])

Layers: SP1/SP2 (7.7 / 10.7 studs, Life .16-.22), CH1 (0 > 13, Transp 0 > .33 > 1), S1/S2 sparks (**Orientation 2**, Rotation 90, Squash +.35, Speed 58-85, **Drag 11.2**, Life .41-.53, size 3.86), F1/F2/F3 flame bits (Speed 52-104, **Drag 12**, Life .22-.53), FB1/FB2 (Speed 35-42, Drag 3.2), SH1/SH2 (Speed 35-50, Drag 3.2, Life .63-1.25), flare (20 studs, Life .06). Pattern: very high launch speed + Drag 11-12 = fast snap outward that stops in about 0.1 s, then the shapes shrink or fade. Lights: PointLight warm `(1, .345, .145)` Brightness 4 Range 12 plus cool `(.184, .361, 1)` Brightness 1.3 Range 17, Shadows false [data].

Burst budget E at the hit (Emit counts only): about 85 particles in the first frame plus 0.35 s of Rate 20-41/s emission [data].

### 1d. Why it looks good [inference, from the numbers]

1. Never one sprite: about 8 jobs overlap (body, hot core, glow, flare, wisps, embers, halos, trail).
2. Motion is written into the world: H rings spawn at Speed ~0 in world space (LockedToPart false) at 12/s, so a moving ball leaves a chain of expanding discs; plus Orientation-3 copies make that chain readable from the side. A static camera-facing sphere cannot do this.
3. Trail is three stacked Trails, one textured at Brightness 15, with a flicker colour ramp.
4. Dark twins (Brightness .03-.5, LE -0.3/-1) behind bright layers add a dark rim, so glow keeps a shape.
5. HDR: Brightness 5-15 on LightInfluence 0 layers (works with a Bloom threshold of 1-2 in the host scenes).
6. Colour moves: warm-cold-warm in one ramp, plus warm and cold PointLights.
7. Many short lifetimes (.1-.35) on the core, long (1-2 s) only on small embers: the core "boils", the embers trail.
8. Flipbooks are OneShot, 4x4, with random Rotation +-360, so every spawn looks different.

---

# 2. Flame_Beziers (Barrage)

**Moments.** Press E: windup shake+blur > 10 missiles launch from random points around the caster > arc to near the mouse > rise ("Up" burst) > dive > impact (blur, burst, crater, light fade) > cleanup 3 s.

**Layer stack** (Part `Fire`, attachments Middle / Spawn / Up / Impact; all LightEmission 0, LightInfluence 0):

| Group | Layer | Texture | Sheet | Size | Life | Rate | Br | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Middle (travel) | Fire2 x2 | 16843151641 | 4x4 Loop 25 fps, start random | .63 > 0 | .7-1.1 / .8-1.25 | 100 each | 4 / **0.05** | ZOffset 2 / 1, Transp 1 > 0 at 4.7% (instant pop-in) |
| | Smoke11 | 16867368702 | 8x8 OneShot | .63 > 3.25 | 1.6-2.7 | 45 | 5 | Transp 1 > .61 (16%) > 1, ZOff -.2 |
| | Spec25 x2 / Spec1 | 16879804431 / 16878181512 | none | 0 > .44 (3%) > 0 | 1.5-2.5 / .5-1 | 60 | 15 / .1 / 10 | Drag 5, Speed 5-10, RotSpeed +-300 |
| Impact (Rate 0, burst) | Impact13 | 16892226410 | none | 6.2x1.9 > 0 | .1 | 0 | 5 | Orientation 3, ZOff 6 (flash) |
| | Spec26/27 pairs | 16879806460 / 16879808635 | none | 1.4x.56 > 0 | .4-.7 | 0 | 5 and 0.1 | Drag 9, Speed 10-20, RotSpeed +-350, twin at ZOff 3 vs 4 |
| | Smoke11, Smoke Circle | 16867368702 | 8x8 | 3 flat | .6-1 | 0 | 5, 2 | Smoke Circle: Accel +15 Y, Drag 7, Speed 40-65 |
| | Crescent17 / 14 | 17388365888 / 17388366339 | none | grows over 12+ keys to ~7 | .6-1.3 | 0 | none | Orientation 3 (ground wave), Accel +7 Y |
| | Ground33 / Ground23 | 127408540362062 / 118883496017040 | none | 0 > 4.8 / 6.8 (eased) | .4-1.2 | 0 | 6 / .1 / 15 | Orientation 3 shockwave ring, Transp 1 > .49 > 1 |
| | Fire2 x4 | 16843151641 | 4x4 | .75 > 0 | .4-1.2 | 0 | 5 and 0.1 | Speed 40-65, Drag 6-15, Accel +5 Y |
| Up / Spawn | Impact19, Spec26/27, Smoke11, Crescents, Fire2 | 16892242416 + above | | | | 0 | | Spawn: Speed 25-35 |
| Trail | Beam89 | 83108983635987 | Stretch / 1 | Width .34 > 0, Lifetime .8 | | | 4 | Transp 1 > .1 at 17%, FaceCamera, LE 0 |

PointLight on missile: `(1, .204, .063)` Brightness 4 Range 8, Shadows false. Colour `(255,60,34)` flat on every layer [data]. Lighting: Ambient 0, Bloom Intensity 1.5 / Size 20 / Threshold 1, CC Brightness .05 / Contrast .32 / Saturation .1, DoF FocusDistance .05 / InFocusRadius 70, Atmosphere density .35 [data].

**Emit counts** [data]: Spawn = Impact19 7, Spec26/27 10 each (delay .03), Fire2 10 each; Up = Impact19 7, Spec 5 each, Smoke11 10, Crescents 15 each; Impact = Impact13 7, Spec26/27 25 each, Smoke11 10/11, Crescent17/14 15 each, Ground33 3 each, Ground23 4, **Smoke Circle 50, Fire2 50 x4**; all with EmitDelay .03 (after the flash sprite, which has none). Part attribute e=4.0 (unknown).

**Choreography** (all client-side; client fires `Replicator`, server rebroadcasts to all, each client runs the ability: `scripts/aTier__Flame_Beziers__050_Server.luau:20` `Server:Fire(BridgeNet.AllPlayers(), Sending)`).

| t | Action | Source |
| --- | --- | --- |
| 0 | `CameraShake("MissileStart")` (mag 1, rough 2, fadeIn 0, fadeOut .4, rotation only) + `BlurFrame(0.01, .2, 6)` | `...000_Barrage.luau:30-31` |
| 0, x10 | Clone `Fire`, place at root * (+-10, 5..15, +-10); `EmitAll(Missile.Spawn)` | `:43-75` |
| 0 > 1.0-1.5 s | Bezier: 2 random control points near halfway (+-10, +10..25, +-10), target = mouse + (+-10, 20, +-10); duration `RNG(1, 1.5)` per missile | `:55-71` |
| arrive | `EmitAll(Missile.Up)`; second Bezier 3 control points (+10..15 up) down to mouse +-10; TweenInfo(1 s, Sine) | `:79-96` |
| +1.0 s | `BlurFrame(0.01, .1, 6)`, `EmitAll(Impact)`, light tween `{Brightness=0, Range=35}` 1 s Quart, `ToggleAll(Missile,false,...)` stops continuous layers, `CameraShake("MissileImpact")` (mag 1, rough 15, fadeOut .4), crater 10 rocks r4 offset -5 life .8 | `:102-113` |
| +3 s | `Missile:Destroy()` | `:115-117` |

Crater (`...008_Crater.luau`): 10 slate rocks in a ring, each raycast to floor, half tilted 10-30 deg, a ground-material "grass cap" cloned from the floor, scale pop 0 > .9-1.3 in .05 s (`:125`), shrink to 0 over 1 s after Lifetime (`:129`). `EmitAll` reads attributes `EmitCount`/`EmitDelay`/`EmitDuration` (`...003_ZonitoVFX.luau:250-265`). Screen helpers in the same module: `BlurFrame` (BlurEffect in Lighting, in/out tween), `ColorFrame` (tint tween), `ImpactFrame` (`:147-154` flips ColorCorrection `Contrast` between -100 and 100 with `Brightness -1`, `Saturation -1` for N pulses plus a Highlight on chosen parts).

**Why it looks good.** Randomised arcs + durations desynchronise the ten impacts for free; "Up" bounce gives an anticipation beat before the dive; every layer is paired bright/dark (Br 5 vs 0.1, ZOffset +1) for a dark rim; ground-plane layers (Orientation 3 Crescent/Ground) read as shockwave on the floor; cleanup is staged (stop emitters, let particles finish, destroy at 3 s) so nothing pops [inference].

---

# 3. Slashes (IceSlash, LeafSlash)

**Moments.** Key 1 or 2 > sweep (0-150 ms) > impact (75 ms) > stop continuous layers (150 ms) > destroy (2.15 s).

**Layer stack, IceSlash** (colours: pale `[183,227,255]`, mid `[51,129,255]`, light `[138,210,255]`, cyan `[51,235,255]`, violet `[89,34,255]`):

| Group | Layer | Texture | Sheet | Size | Life | Rate/Emit | LE | Br | LightInfl | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Attachments (on during sweep) | Firm Smoke | 14727016281 | 8x8 Loop 30 fps | 0 > 4.8 (15%) > 9.5, 5 keys | .5-2 | 250 | .75 | 10 | .25 | Transp .9 flat, Speed 7-89, Drag 7, spread 15, EmissionDir 3 |
| | Spec5 | 16879573368 | 4x4 start rnd | 0 > 1.4x1 (7%) > 0 | .5-2 | 100 | -0.25 | 12 | 0 | Speed 5-107, Drag 6, RotSpeed +-50 |
| | Shards 2x2 2 | 17842430380 | 2x2, fps 0, start rnd | 0 > 1.3x.28 > 0 | .5-2 | 100 | 1 | 10 | 0 | RotSpeed +-300 (static random cell) |
| | Glass Shard Spec | 15831917569 | 2x2 OneShot, start rnd | 0 > .8 > 0 | .5-1.5 | 100 | 1 | 12 | 0 | Speed 5-161 |
| | Line Spec 15 | 84484878548223 | none | 0 > 2.5 (6%) > 0 | .25-.5 | 250 / Emit 100 | 1 | 12 | 0 | **Orientation 2**, Rot 90, Drag 10, Speed 53-213 |
| Slash (Emit) | Wind14/23/41/48 | 75412173597770 / 103000834263561 / 99096695944611 / 80189053385709 | none | 0 > 3x1.6 > 5.8x3 > 8x4.3 > 10x5.4 ... (12+ eased keys) | .2-1 | 150 | 0 | 10 | 0 | **Orientation 3**, Rot +-1000, RotSpeed +-300-500, Transp .96-.975 > 1 (barely visible), colour grey `[67,105,115]`/`[115,115,115]` |
| SlashImpact (Emit 15-50 each) | Impact33 | 16892290479 | none | 9.1 > 18.4 (97%) > 0 | .05 | 15 | 1 | 10 | 0 | Orientation 3, ShapeInOut 2, Squash 1 |
| | Cut Smoke / Expanding Lightening Smoke | 11799607237 / 13712000835 | 8x8 | 0 > 2 > 3.9 ... | .5-1.5 | 25 each | 1 | 2 | .75 | Speed +-120, Drag 10, EditorScale 2 |
| | Moving Forward Line / Line Spec 16 | 15418442509 / 8944381800 | 4x4 / none | 10 flat / 17 > 5.7 > 1.8 > 0 | .2 | 150 | -1 / 1 | 10 | 0 | Orientation 2, Squash 1 |
| Beams (Left attachment to Right attachment; **Segments 150, CurveSize0 19.38, CurveSize1 -19.38, FaceCamera false**) | Bright Blue | 115638000454630 | Stretch / 2 | Width 5 > 1 | | | 1 | 5 | | ZOff +.001 |
| | Slash detail 1 | 106097541846992 | Stretch / 2 | 5 > 0 | | | 0 | 5 | | Transp 1 until 28%, then 0 |
| | Slash detail | 118715717532031 | Stretch / 2 | 5 > 0 | | | 1 | 5 | | colour fades pale blue to white, Transp 1 > .36 |
| | Dark | 80823115982547 | Stretch / 1 | **20 > 1** | | | 0 | 5 | | ZOff -.4, colour blue `[101,124,255] > [0,60,255]` |

LeafSlash is the same skeleton recoloured (greens `[72,255,62]`, `[105,255,127]`; dark `[30,62,9]`, `[70,27,7]`; petals 13802408466; 1-shot "Downward Impact" tex 13997926164 LE -1 LightInfl .75; Beam sizes x5 in code) [data].

**Choreography** (`scripts/aTier__Slashes__004_Slash.luau`):

| t | Action |
| --- | --- |
| 0 | clone to `workspace.FX`, `CFrame = root * Angles(0, 135 deg)`; `effects.Emit(slash.Slash)`; Heartbeat glues position to the root (`:12-17`) |
| 0 > 150 ms | `TweenInfo.new(.15, Linear)` rotates the slash part by **-179 deg** (`:20`): the Left/Right beam anchors swing through the arc |
| 75 ms | `task.delay(.075, ... effects.Emit(slash.SlashImpact))` (`:21-23`) |
| 0 > 75 ms | Beam widths tweened over .075 s (Dark `Width0` 20 > 1; others 5 > 0) (`:27-31`); a second pair of tweens at 200 ms (`:33-36`) |
| 150 ms | `effects.Enable(slash.Attachments)` flips `.Enabled` on all emitters/beams/trails (`:42`): continuous smoke/spec layers that ran during the sweep are cut |
| 2.15 s | `slash:Destroy()` |

`Effects.Emit` is `task.delay(EmitDelay, function() stuff:Emit(EmitCount) end)` (`...000_Effects.luau:9-10`). Emit counts [data]: Slash group: Wind14/23/41/48 25 each, Shards 25, Glass Shard Spec 75; Attachments group (as `Emit`): Spec5 75, Shards 75, Glass Shard 75, Line Spec 15 100; SlashImpact: Glass Shard Spec 50, Shards 25, Line Spec 15 75, Impact33 15, Spec4 25, Spec5 50, Cut Smoke 25, Expanding Lightening Smoke 25 (EditorScale 2), Moving Forward Line 1, Line Spec 16 1; all EmitDelay 0. Firm Smoke has no counts (continuous, EditorScale .5); wind sprites carry `_vfxEditorGraphSize` (the eased Size curve was authored in a graph editor with cubic/linear easing handles). LeafSlash: Spinning Petal 25, Spec16 50 + 5, Downward Impact 25.

`Effects.Blur` and `Effects.FOV` helpers exist (blur in .2x, out .8x of duration; linear FOV tween), not called by these two slashes. Bug to note: two TweenService tweens on the same property start at once (`:27-28`), so the second wins and the "grow then shrink" never plays [inference]. Ground: a `Texture` on the baseplate is swapped through 32 image ids every .05 s by `...006_Script.luau` (20 fps texture flipbook, the thing ZO-03 warns against).

**Why it looks good [inference].** The slash is a 150-segment curved Beam pair (a real arc, not a straight stripe) with 4 stacked beams: narrow bright, detail, wide dark underlayer (Width 20, ZOffset -0.4); wind sprites lie flat in the slash plane and grow with an eased 12-key curve; the hit is a 50 ms bright flat Impact33 + shard/spec burst timed at the midpoint of the arc; the smoke/spec trail exists only while the blade moves.

---

# 4. Ayato_Showcase (sword combo)

**Moments (Q combo, rootPart anchored for all of it; `scripts/aTier__Ayato_Showcase__000_Showcase.luau`).**

| t (ms) | Beat | Source |
| --- | --- | --- |
| 0 | M1 anim; `toggleSword(true)` emits the sword's own emitters | `:47-49` |
| 170 | `Slash` clone, sound "One", EmitAll, PointLight tween `Brightness 0, Range 10` over .3 s (from 1 / 7), destroy 1.5 s | `:51-66` |
| 500 | BackwardsSlash (sound Two) | `:70-88` |
| 1000 | Pierce, placed 2.6 studs forward (sound Three) | `:90-106` |
| 1400 | Speed VFX 6 studs forward (sound Four, light fade .6 s) | `:110-126` |
| 2060 | Slash2 (sound Five), sheath at +1.2 s | `:129-146` |

E (charged): anim, Slash2 at 200 ms, **Dash beams at +900 ms**: part 8 studs ahead, `TweenInfo(.74, Sine, Out)` roll 180 deg (`:181-183`), all Beams tween `Width0=0, Width1=0, CurveSize0=-1, CurveSize1=7.5` in .79 s (`:187-192`), root jumps 14.85 studs in **.075 s** (`:198`); at +.82 s sheath: sword Star PointLight `Brightness 5, Range 1` > `0, 4` in .2 s, `CameraShake("SwordSheath", pos, 150)` and `Emit(1)` on the Star emitters (`:204-215`).

**Layers.** Palette: orange `[255,176,80]` > `[255,121,32]` (C1), a fade-to-black variant `[255,176,80] > [255,121,32] .11 > [94,42,12] > [16,7,1]` for floor dust. All Brightness 6/4/2, LightInfluence 0.

| Layer | Texture | Sheet | Size | Life | LE | Br | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Dark Blue Slash (slash body) | 132395520838872 | 4x4 OneShot | 6.6 flat | .3 (.205 on Slash2) | 0 | 6 | Orientation 3, Transp 0 until 87% then 1; attr counts bin |
| Basic Blurry Spec (flash/halo) | 77024587778878 | none | 6.6 > 7.7 (11 eased keys), or 5-17 | .04 / .55 | .5 / 1 | 2 / .015-.5 | ZOffset 6; long soft one Transp 1 > .85 > 1 |
| Blob 2 pairs | 13271148125 | none | .198 > 0 | .2-.8 / .2-.5 | 0 / 1 | 6 / 4 | **bright + additive twin**, ZOff +.1; Speed 1.3-10.6, Drag 3, EmitCount 3 (decoded) |
| Glowing Bezier Line (streaks) | 16056965573 | 4x4 | .53 > 0 | .45-1.05 | .5 | 6 | **Orientation 2**, Rot -90, Accel -3.3 Y, EmitCount 2-10 |
| Right Spike / Sideways Spec 78 | 14052683457 / 13828261486 | 2x2 / none | 1.5 > 0 / 1 > 0 | .2-.4 / .4-.7 | .3 / 0 | 4 / 6 | Orientation 2, Squash -1 / +.1, Speed 5-40, EmitCount 15 (Right Spike, Sideways Spec) |
| Zigzag 2 | 15435019950 | 4x4 | 6.5 flat | .15 | 0 | 6 | Orientation 2, Squash -1 |
| circleFlipbook2 (ring) | 126034245450101 | 4x4 | 2 > 3.2 (eased) | .4 | 0 | 6 | Orientation 3 |
| Star102 (sheath star) | 17391818367 | none | 2 > 0 / 10 > 0 | .1 / .3 | 1 / 0 | 6 | RotSpeed 360 on the 10-stud one |
| Beam105 x3 (dash) | 112629787601025 | Stretch / 1 | Width 6 > 2, CurveSize -3 / 9, **Segments 500** | | 0 | 5 | Transp 1 > 0 at 6% > .04 > 1 at 85% |
| Speed floor | 13828261486 / 77024587778878 | | Squash 1 > .07/.37 | .1-.35 | 0 | 4-6 | color fades to black; Rate 40-120 continuous while dashing |

**Emit counts [data]: Slash/BackwardsSlash/Slash2: Dark Blue Slash 1, Basic Blurry Spec 1, five sub-attachments each Blob 2 x3 + Glowing Bezier Line x2 at **EmitDelay 0, .05, .10, .15, .18 s** (spark pairs fired along the arc as the blade passes); Pierce: Right Spike 15, Sideways Spec 15, flash 1, ring 1, Bezier Line 10, Blob 10; Speed: continuous emit 0.28 s (Impact21 2, ring 2, flash 1-3, Sideways Spec 2); Dash: Sideways Spec 35, Zigzag 1, flash 1, Bezier 5, Blob 10, Blurry Spec 10; Sword idle: Blob 15 + Bezier 15; sheath Star: 0 (the code emits 1).

**Screen/camera helpers** (`...001_ZonitoVFX.luau`): `CameraShake(name, origin, range)` skips if the camera is beyond `range` studs (`:260-266`; example 150); `PlaySFX` clones a Sound with `PlayOnRemove` and destroys it (`:274-278`); `FovDepth/FovBlur(startFOV, blur, t)`: set FOV low, tween Quad back to 60 with DoF/Blur (`:82-107`); `Vignette(color, in, hold, out, transparency, origin, range)` (`:182`); `Distortion(pos, t, size, strength)` clones a Glass MeshPart (MeshId 11067917371) and tweens Size up and Transparency to 1 (`:282-299`); `CameraVFX/CameraFX` pin an emitter part to the camera at distance d and resize it to the screen frustum via `ScreenSpace` (`...010_CameraFX`, `...011_ScreenSpace`); `HighlightFrame` fills a Highlight on a target (`:157`). Shake preset `SwordSheath = new(.45, 13, 0, .15)`, position influence (1,1,1), rotation (0,0,1) [data] (`...004_CameraShakePresets.luau:11-13`).

**Why it looks good [inference].** Every beat is a different silhouette (arc, back-arc, spike pierce, ground speed lines, wide arc) on a fixed ms schedule that matches the animation; all share one orange palette and one library of ~10 textures; every hit pairs a 40 ms flash disc (Basic Blurry Spec, Br .5, LE 1) with line streaks (Orientation 2) and tiny additive blobs; light is a short pulse that grows range while brightness goes to 0; the final sheath gets its own tiny star + micro shake, an audio-visual full stop.

---

# 5. Zonito_Music_OS (Music ability, "E")

**Moments** (`scripts/aTier__Zonito_Music_OS__052_Clash.luau`; trigger `MusicClash` packet, server sends to all: `...079_Ei.luau`).

| t | Beat | Source |
| --- | --- | --- |
| 0 | sound "Initial"; two note props placed +-6 studs left/right of the caster | `:40-48` |
| 300 ms | SpawnVFX at root: `EmitAll`, light tween `Brightness 0, Range 15` over .4 s; notes enabled; `CameraShake("MusicSpawn")` (mag 1.7, rough 10, fadeOut .4, **position** shake); `ColorFrame(.01, .2, (255,240,230))` white-warm flash | `:50-67` |
| 1050 ms | notes tween to centre, `Back` ease In, 1 s | `:69-72` |
| 2050 ms | clash: notes' emitters switched off and cleared; `NoteImpact` cloned; light `Brightness 0, Range 40` .5 s; `CameraShake("MusicClash")` (1, 3, 0, .9; rotation yaw 3); `EmitAll`; `FovBlur(43, 25, .6)`; `Vignette((255,195,134), .01, .2, .6, .6)` | `:76-210` |
| in parallel | 12 mini-notes, one per frame (`task.wait()`), each flies a 7-point Bezier (5 random controls) for .8-1.4 s up to 15 studs, waits .4, falls to the floor with `Back In` in .4-.65 s, then sound ×2, `MiniNoteImpact` shake (1.3, 13, 0, .45; rotation only), `BlurFrame(.01, .3, 7, pos, 200)`, `ColorFrame(.01, .15, (255,242,228))`, impact emit, light `Range 21` .5 s, destroy at +2 s | `:78-173` |

**Emit counts** [data]: NoteImpact: flash Spec19 1, Note1/Note2 glyphs 11 each, Spec 16 + 15, Rainbow 9/6/2 1 each, Impact13 2 + 1, Impact21 4 + 2, Flare63 1, Smoke33 15 + 10, Wavey 3; SpawnVFX: flash 1, flare 1, Note2 glyphs 10; held notes: Other43 15 (on spawn) + 2 on attachment; Mini impact (x12): Note2 16 + 20, Spec25 10, SlashFlipbook 10, Crescent28 6, Swirls15 5, Wavey 4, Rainbow2 4, Ground18/23 3 each, Impact21 3, Thin 2, Rainbow6 2, flashes 1 each. Rule visible: one flash sprite per layer = Emit(1); particles that must scatter = 10-20.

**Layer stack** (NoteImpact, the hero hit; colour flat `[255,160,82]` on every layer, LightInfluence 0):

| Layer | Texture | Size | Life | LE | Br | ZOff | Role [inference] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Spec19 (flash) | 16879789169 | 28.9 > 27 (eased) | **.046** | 1 | 5 | 3.1 | white-out frame, 29 studs, ~3 frames |
| Spec19 (afterglow) | 16879789169 | 32.9 flat | 2.0 | 1 | .6 | 2.9 | slow fade, Transp 0 > 1 |
| Impact13 x2 | 16892226410 | 7.6 flat / 5.1 | .05 / .1 | 0 | 5 / 4 | 3 / 2.1 | hard flash shape |
| Impact21 x2 | 16892247104 | 5.1x2.5 > ~10 | .25-.5 / .4-.65 | 1 / .1 | .15 / 3 | 2 / 1 | burst blobs (additive + normal) |
| Rainbow9 / 6 / 2 | 75291700184033 / 96288653875185 / 138111953688137 | 5.1 > 6.3 / 5.1 > 8.8 | 1.2 / .7 / 1.1 | 1 | .25-.5 | 2.8-2.9 | soft chromatic glows at very low Br |
| Flare63New | 106225548757766 | 7 > 10+ | .4 | 1 | none | 3.1 | star flare |
| Note1 / Note2 / Spec | 89285314430432 / 94430859745782 / 88990954537761 | 2 > 0, .48 > 0 | .4-1.6 / .6-2 | 0 | 3.5 / 5 | 2.5-2.8 | thrown note glyphs, Accel -16.5 Y, Drag 5, Speed 19-32 |
| Smoke33 x2 | 16867492882 | 2.3 > 4 | .6-2.2 | 0 | 5 / none | 1 / .7 | 4x4 OneShot, Accel -5.8 Y, Transp .85 > 1 |
| Wavey | 137167224180401 | 12.1 > grows (eased) | .4-.75 | .1 | 6 | 0 | ring wave, RotSpeed 100-200 |
| PointLight | | | | | | | `(1, .698, .431)` Brightness 3-4, Range 5-7 (tweened up to 40) |

Projectile notes (`Note1/Note2`, LockedToPart, Rate 15, Life .3-.4, Br up to **25** on "Wavey", Br .01-.3 on soft glows, `Spec19` flash Br 15 Life **.025**) carry the same texture family plus a Trail `Beam89` (tex 83108983635987, Lifetime .5, Brightness 4.5, Transp 0 until 87%, width .39 > 0). Also in the file: wind-lines (`...060_WindLines`, short-lived Trail objects with random attachment pairs, SpawnRate default 25/s, Lifetime 3 s) and a foliage WindShake module (ambient, not combat VFX).

Lighting: Ambient 0, Brightness 2, Bloom 1 / size 24 / **threshold 2**, CC contrast .1 / saturation .1, DoF, SunRays .3, Atmosphere density .4 [data].

**Why it looks good [inference].** Every punch has a stack: <=3-frame white flash, 2-s soft afterglow, hard shape, burst blobs, chromatic glows at low Br, debris glyphs with gravity; camera gets four separate channels with different durations (colour flash 200 ms, vignette 800 ms, FOV/blur 600 ms, shake 450-900 ms); a 12-bolt secondary salvo (one per frame, random duration) turns a single pop into a payoff phase; a 1 s "Back In" pull-in gives anticipation before the clash.

---

# 6. Smaller A-tier files

### 6a. Death_FX (emitters on HumanoidRootPart.Attachment, Rate 0, all `Emit`-driven; EmitCount [data]: Spec7 15+15, Spec27 10+10, flash Spec19 2, Flare24New 2, Ground23 2+2)
Colour flat `[101,175,255]`, LightInfluence 0.

| Layer | Texture | Sheet | Size | Life | LE | Br | Z | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Spec19 flash | 16879789169 | none | 15 flat | **.05** | 1 | .6 | 6 | |
| Ground23 x2 | 118883496017040 | none | 5 flat / 5 > 0 | .06-.08 / .1 | 1 | 1 / 3 | 5 / 4 | Transp 0 > 1, ring flash |
| Flare24New | 76152181726382 | none | 3.6 > 5 | .5 | 1 | 1 | -1 | Transp 1 > .59 > 1 |
| Spec7 pair | 16879578139 | 8x8, 20 fps, start rnd | 1x.56 > 0 | .6-.8 / .7-.9 | 0 | **6 / 0.1** | .5 / 0 | Accel +4 Y, Drag 6, Speed 15-25 (bright + dark twin) |
| Spec27 pair | 16879808635 | none | .5x.1 > 0 | .7-1 | 0 | 6 / 0.1 | | RotSpeed +-200 |

The dressed R6 avatar uses Glass-material parts and `Animate` is the stock Roblox script (no death logic) [data]; how this was triggered is not decodable.

### 6b. Colouring_Practice (colour exercise)
Colour ramp (5 stops, life-mapped): gold `[255,203,71]` > lime `[113,255,84]` at 24% > dark green `[20,59,22]` at 45% > near black `[3,17,7]`; second flat gold for hot layers.
Trail (continuous, Rate 60): "Stylized plain Blob Rise" x3 (tex 13794844031, 4x4 OneShot, Orientation 2, Squash .1/.2/.3, Br 5/2/0, Z 0/-.1/-.2, Speed 2-10, Life .2-.8), "Wiggly Ball" x3 (14004161351, 4x4 at 35 fps, start random, Speed 5-30, Drag 4), Basic Blurry Spec (35/s, Z -2). Impact (Emit): Basic Hit (14379750639 7 studs .3 s), Round Spikey (18350947061, 9-10 studs, **.045 s**), Breaking Splash (13795304468), Water28 (16866058024), Rainbow5 (126685678214657, LE 1, 12 studs, EmitCount 2), 1.5-s soft halo 15 > 20 studs, plus a 42 ms white-gold flash 17 studs (Br .2, LE 1). Emit counts [data]: Blob Rise 15 (x4 + 9), Wiggly Ball 8 (x6), Water28 5, Rainbow5 2, flashes/Hit/Splash/Spikey 1 each. Config folder `⚙️ VFX Settings`: `VFX_Colour` = the gold/lime/dark ramp, `Light_Colour` white, `Colour_Shift_*` off: a one-colour recolour tool. Decoded counts: Blob Rise 15 and 9, Wiggly Ball 8, Water 5, Rainbow5 2. Lights: `(.87,1,.24)` Br 2 R16 and `(.18,1,0)` Br .8 R24. Lesson: one hue family walked through value (bright gold to near black) instead of many hues [inference].

### 6c. Constellations (burst, two variants; timing [data]: attachment 1 Star Emit(1) at 0, attachment 2 Star Emit(1) at **EmitDelay .5 s**, attachment 3 main hit at **.68 s**: Smack/flash/Star/Shards/Overlay/Impact524/Halftone 1 each, Spinning Constellation 7, Spec25 7, Crescent 2; the `⚙️ VFX Settings` config stores a purple/pink recolour (`VFX_Colour` (135,88,255) and (255,96,247); lights (205,87,255)) different from the shipped lime/gold Color sequences, so the same rig is recolourable; Halftone adds a 9.8-12.8-stud dot-screen sprite 109985324958700, LE .6)
Colour: lime `[174,255,96]` and gold `[255,211,88]`. Attachment 1: Star102 (7.4 studs, RotSpeed 500, Squash -.2 > -1.8, Life .5); 2: Star102 (0 > 6.25 at 10%, .165 s); 3 (main): Circular Smack 18140248952 (5.2 studs, 4x4, LE 1, .2 s), flash Basic Blurry Spec (11 studs, **.05 s**), Star102 (7.4, Squash -2, .06 s, Rot 45), Spinning Constellation (79053843420399, 8x8, Speed 45-75, **Drag 16**, 2 studs > 0, Life .4-1) and Spec25 (same motion, two colours, ZOffset -.15 / -.16 for the 2-colour pair), Thin Fading Crescent (16940415246 LE 1 / .8, Orientation 3), Strange Overlay Shards (16015157826, 4.9 > 6.4, LE 1, Br .2), Impact524 (13463779259). Light `(.83,1,0)` Range 8. High Drag 16 = very fast pop that stops almost at once [data].

### 6d. nnoonooooo (blue galaxy projectile, flat `[119,126,255]`; Impact Emit [data]: Galaxy Impact 8 and 1, Impact21 6, Spec19 1+1, Ground18 2, Rainbow5 2; light colour in config (41,70,255))
Middle (continuous, Rate 60): Spec1 (85902520507613, 1.7x.125 studs, Speed 1-2), Spec1 8x8 (98755040853572, 25 fps, start rnd), Star12 (123934808723041, twinkle by a 9-key Size zig-zag). Impact (Emit): Galaxy Impact x2 (119408494827678, 4.95x1.05, **.1-.13 s**, Br 6/2), Impact21 (0 > 3+ eased), Spec19 (13.6 > 14.4, .8 s) and big 11-stud 94698008981093 (1 s), Ground18 ring (79269702153496, Orientation 3, Br **15**, .7-.9 s), Rainbow5 (75178745384174, LE 1). Trail `Beam81` (113083314207224, **TextureMode 2 Static, TextureLength 3**, width 0 > .4 at 6.5% > 0, Lifetime .7, MinLength .1). Light `(.16,.27,1)` Br 3 R10 [data].

### 6e. soear (spear aura, violet `[102,71,255]` / `[170,85,255]`)
Mesh: `Spear` MeshPart MeshId 8599640606, Metal, Anchored, CanCollide true (display prop). Four invisible parts (Handle, Right, Left, Tip) each carry **FrontLightning** (16356874730, 8x8 Loop 25 fps, Br **25**, LE 1, size .3 / .2, Rate 35 or 10, Life 1, LockedToPart, ZOffset +1) + **BackLightning** (same tex, Br 5, ZOffset -2) + **Smoke** (16228000752, 4x4 OneShot, LE 1, 1 > 1.6, Rate 135/30/80, Transp 1 > .77 > 1, Z -2). Aura part: Glow (6430908053, 8 studs, Rate 2, Life 2), Beams poleBeam (16343203857, Static, TextureLength 6, **TextureSpeed 1**, width 2 > 1, Segments 10, Br 5, LE 1, FaceCamera) and auraBeam (16615669232, Static, length 10, speed .1, width 5), "Balls" and "Stars" (16227446933, 16227239760, 8x8 25 fps, **Brightness 50**, size .375 / .15, Rate 40, Life 2). Light `(.67,.33,1)` Br 2 R12 [data]. Attributes [data]: FrontLightning EmitCount 5555 (a placeholder value, the layer is continuous), Smoke 0. Lesson: tiny sparkles at Brightness 50 punch through Bloom without making large areas white [inference].

---

# 7. Technique catalog (A tier)

Starting values are the A-tier shipped values [data]; adapt, do not copy blindly. Ours is a brick toy game on phones: apply AT-30 to every recipe.

| ID | Technique | Exact starting values | Seen in |
| --- | --- | --- | --- |
| AT-01 | **Layer-stack projectile**: core (OneShot 4x4) + hot pulse + glow + flare + wisps + embers + halos + trail; never a single sprite | core 4.3 and 8.5 studs Life .25-.35 Rate 20; hot core 0 > 9 Transp 0 > 1; flare 0 > 10 > 0 Life .1; wisps 2.7 flat Life .35-.85 Rate 10-20; embers Speed 15-22 Drag 2 Life 1-2 | Fireballs |
| AT-02 | **Dark twin**: copy the emitter, Brightness .03-.5 (or .1), LightEmission 0 or -0.3, ZOffset 1 behind, Lifetime +.1 | Br 5 bright + 0.1 dark (Flame, Death_FX); Br 5 + 0.03 (F3); Br 5 + 0.5 (SH) | Fireballs, Flame, Death_FX |
| AT-03 | **HDR brightness ladder** on LightInfluence 0 layers | glow/halo 15, spec 10-15, body 4-6, soft glow .015-.6, mini sparkles 25-50; host Bloom threshold 1-2, size 20-24, intensity 1-1.5 | all |
| AT-04 | **Negative LightEmission** as a darkening layer under an additive one | S1 LE +1 at ZOffset -2.0 with S2 LE -1 at -1.9 (same size, life, locked); -0.3 on bodies, halos, embers | Fireballs [inference: renders darker; verify in capture] |
| AT-05 | **Rings left in the world** to read speed | Size -0.27 > 5.7 / 11.3 / 17.8, Speed .0003, LockedToPart false, Rate 12, Life .65-.85, plus a copy with Orientation 3 SpreadAngle 5; add one LE 1 member | Fireballs |
| AT-06 | **Triple trail** on one attachment pair 6 studs apart | flat soft (W .55 > 0, Transp .7, Br 3), textured hot (W 1 > .8 > 0, TextureLength 2, Br 15, LE .55), outline texture (W 1 > 0, Br 3), Lifetime .75, FaceCamera, MinLength .033 | Fireballs |
| AT-07 | **Colour ramp that changes hue mid-life** (warm, cold band, warm) | `[255,65,17] 0 > [215,105,14] .45 > [104,29,255] .49 > [28,56,211] .57 > [128,66,15] .67 > orange`; Part 1 `[148,0,161] > [136,59,9] .2 > [179,0,179]` at Br 7.5 | Fireballs |
| AT-08 | **Warm + cool pair of PointLights**, no shadows | warm `(1,.345,.145)` Br 4 R12; cool `(.18,.36,1)` Br 1.3 R17; fade Br to 0 while Range grows (10-40) over .3-1 s (Quart) | Fireballs, Flame, Ayato, Zonito |
| AT-09 | **Burst = high Speed + high Drag** | Speed 58-104, Drag 11-12, Life .2-.55; Orientation 2 + Squash +.35 for streaks; second tier Speed 35-50 Drag 3.2 Life .6-1.3 | Fireballs E |
| AT-10 | **Hit flash trio** | white-ish flash sprite 11-29 studs Life .025-.05 s, LE 1, Br .2-5, ZOffset 3-9 + hard shape (Impact13) Life .05-.12 + afterglow same texture Life 1-2 Br .6 Transp 0 > 1 | Zonito, Death_FX, Colouring, Ayato |
| AT-11 | **Impact kit on one attachment (all Rate 0, Emit)**: flash, spec streaks, smoke ball, ground ring, crescent wave, fire blobs | ground ring Orientation 3 size 0 > 4.8-6.8 eased, Life .4-1.2; crescent grows to ~7 over .6-1.3 s Accel +7 Y; sparks Drag 9, Speed 10-20, RotSpeed +-350; fire Speed 40-65 Drag 6-15 | Flame |
| AT-12 | **Curved multi-beam slash** | 3-4 Beams same attachments, Segments 150, CurveSize0 19.4 / CurveSize1 -19.4, FaceCamera false; narrow LE 1 Br 5 (W 5 > 1), detail layers (W 5 > 0), dark wide LE 0 (W 20 > 1, ZOffset -.4); sweep 0-150 ms linear, -179 deg | Slashes |
| AT-13 | **Eased Size by many keypoints** (10-12 keys, front-loaded) instead of a linear grow | wind: 0 > 3.05 (5.6%) > 5.76 (11%) > 8.1 (17%) > 10.2 (22%) > 12 (28%); Blurry spec 6.6 > 6.63 > 6.73 > 6.9 > 7.13 > 7.4 over Life | Slashes, Ayato, Zonito |
| AT-14 | **Barely-there wind sprites** | Orientation 3, Rotation +-1000, RotSpeed +-300-500, Transp .96-.975 > 1, grey `[67,105,115]`, Life .2-1, Rate 150 | Slashes |
| AT-15 | **Time schedule in ms** from one trigger | Ayato: 170 / 500 / 1000 / 1400 / 2060; Slash: 0 sweep, 75 hit, 150 stop; Zonito: 0 / 300 / 1050 / 2050 | scripts |
| AT-16 | **Random Bezier flights, per-item random duration** | 2-5 random control points near the midpoint, +10..25 up, durations 1-1.5 s (missiles) or .8-1.4 s (notes); stagger spawn by one frame | Flame, Zonito |
| AT-17 | **Camera: short rotation-only shakes** | (magnitude, roughness, fadeIn, fadeOut): MissileStart (1, 2, 0, .4), MissileImpact (1, 15, 0, .4), SwordSheath (.45, 13, 0, .15; position (1,1,1), roll only), MiniNoteImpact (1.3, 13, 0, .45), MusicSpawn (1.7, 10, 0, .4), MusicClash (1, 3, 0, .9; yaw) | scripts |
| AT-18 | **Screen pulses at the hit** | BlurFrame in .01 s / out .1-.3 s, size 6-7; ColorFrame warm-white `(255,240,230)` in .01 / out .15-.2 s; Vignette `(255,195,134)` in .01, hold .2, out .6, transparency .6; FovBlur start FOV 43 > 60 in .6 s with blur 25 > 0 | Flame, Zonito |
| AT-19 | **Distance gate on every screen effect** | `CameraShake/BlurFrame/ColorFrame/Vignette(origin, range)`; shake range 150, blur 200, others 999 | Ayato, Zonito |
| AT-20 | **Flipbook roles**: 4x4 OneShot for bodies, 8x8 Loop 25-30 fps + StartRandom for lightning/fire/smoke, static random cell (fps 0, StartRandom) for shard/spec variety | Fire2 25 fps; Firm Smoke 30; Shards fps 0 | Flame, Slashes, soear |
| AT-21 | **Paired additive + normal copies** of the same texture | Blob 2: Br 6 LE 0 Life .2-.8 + Br 4 LE 1 Life .2-.5 ZOffset +.1; Impact21 LE 1 Br .15 + LE .1 Br 3 | Ayato, Zonito |
| AT-22 | **Stretch streaks** | Orientation 2, Rotation +-90, Squash +-1 (or +.35), Speed 5-213, Drag 6-10, Life .15-.5 | Slashes, Ayato, Fireballs |
| AT-23 | **Continuous layers only while moving, cut at the end** | Slashes: continuous Rate 100-250 during the 150 ms sweep, then `Enable` flip; Flame: `ToggleAll(Missile, false)` at impact then 3 s destroy | Slashes, Flame |
| AT-24 | **Aura beams with static scrolling texture** | Beam TextureMode 2, TextureLength 6-10, TextureSpeed .1-1, Segments 10, FaceCamera, LE 1; plus billboard glow 8 studs Rate 2 Life 2 | soear |
| AT-25 | **Tiny sparkles at extreme Brightness** | size .15-.4, Brightness 50, Rate 40, Life 2, LE 1 | soear |
| AT-26 | **One palette, value steps** (not hues): pale / mid / light / saturated from one hue; Dark layer from the deep end | Ice: `[183,227,255]`, `[51,129,255]`, `[138,210,255]`, dark `[0,60,255]` | Slashes, Ayato, Colouring |
| AT-27 | **Dark scene, bright effect** | Ambient 0 or .3, Brightness 1-3, Bloom thr 1-2; CC contrast .1-.32 | Flame, Zonito, Slashes |
| AT-28 | **Cosmetic replicate pattern**: owner client fires a remote, server rebroadcasts to all clients, each client builds the effect locally (matches ZO-04) | `BridgeNet Replicator` / `Packets.MusicClash.sendToAll` | Flame, Zonito |
| AT-29 | **Ground contact props**: ring of rocks, raycast to floor, copy floor material, pop in .05 s scale 0 > 1.1, shrink 1 s | 10 rocks r4, offset -5, life .8 | Flame |
| AT-30 | **Port to a game**: budget each fireball as 1 hero emitter group set <=5 emitters at High, <=3 at Low; keep ideas (halo chain, dark twin, triple trail, hue ramp) and drop counts | A-tier fireball: 26 emitters, ~236 live | our rules (CD-06) |

---

# 8. Texture reuse

Library naming: emitter names are the texture family plus an index (Spec19, Impact21, Ground23, Smoke11, Fire2, Crescent17, Rainbow9, Flare63New, Star102, Blob 2). The same artist's library is behind ZO-11 (reuse a few textures everywhere). Roles are [inference] from name, size and layout.

| Texture id | Library name | Used in (count) | What it seems to be |
| --- | --- | --- | --- |
| 77024587778878 | Basic Blurry Spec | Ayato 12, Colouring 4, Constellations 4 | soft round glow disc: flash (3-17 studs, Life .04) and halo (Life .5-1.5) |
| 16879789169 | Spec19 | Zonito 13, Death_FX 1, nnoonooooo 1 | very soft large disc for white-out flash (8-33 studs, Life .025-2) |
| 16892247104 | Impact21 | Zonito 10, Ayato 1, nnoonooooo 1 | soft elongated impact burst (2:1 ratio) |
| 16879804431 | Spec25 | Constellations 4, Flame 2, Zonito 2 | small sparkle spec |
| 118883496017040 | Ground23 | Death_FX 2, Flame 1, Zonito 2 | flat ring/shockwave (Orientation 3) |
| 17391818367 | Star102 | Constellations 6, Ayato 2 | 4-point star flare |
| 16879808635 | Spec27 | Flame 6, Death_FX 2 | elongated spec/shard, spins |
| 16892226410 | Impact13 | Zonito 4, Flame 1 | hard flash shape, Life .05-.12 |
| 83108983635987 | Beam89 | Zonito 2, Flame 1 | Trail texture |
| 13271148125 | Blob 2 | Ayato 36 | tiny round blob |
| 16056965573 | Glowing Bezier Line | Ayato 19 | curved streak (Orientation 2) |
| 89285314430432 / 94430859745782 / 88990954537761 | Note1, Note2, Spec | Zonito 14 / 13 / 6 | music-note glyphs and a spec (project-specific) |
| 12780347743 (F3), 17507124046 (F2), 11534281007 (F1), 15419189769 (SH1), 11133563100 (SH2) | fireball set | Fireballs 12 / 6 / 6 / 6 / 6 | flame bodies, big and small embers |
| 16843151641 | Fire2 | Flame 8 | 4x4 fire flipbook, 25 fps loop |
| 13794844031 / 14004161351 | Stylized plain Blob Rise / Wiggly Ball | Colouring 8 / 9 | cartoon blob and wiggly ball |
| 16356874730 | FrontLightning / BackLightning | soear 8 | 8x8 lightning loop |
| 75291700184033, 96288653875185 | Rainbow9, Rainbow6 | Zonito 7 each | chromatic glow |

117 unique texture ids across the 10 files; only 9 are shared across files, the rest are per-effect sets. Texture ids reused in 3 files are the "workhorse" set (soft glow, flash disc, impact blob, spec, ground ring).

---

# 9. Could not decode / open questions

1. Fireball launch trigger is still unscripted: the attribute timings (D1 delay .65 s / 2 s, D2 .95 s, E Emit + .35 s) are known, the caller is not.
2. Death_FX trigger/timing, Flame Beziers `e=4.0`, Zonito `Size_Curve`-style attributes (none found in aTier attribute files) not present.
3. Meaning of negative LightEmission (-0.3, -1) and Squash values: [inference] only. Needs an A/B capture (same emitter, LE 0 vs -0.3 vs -1, bright and dark backgrounds).
4. Beam/Trail/Color sequences are truncated after about 5 stops in the outline; true ramps may be longer.
5. Texture pixel content (alpha, soft edges, size) not available; roles inferred from names and sizes.
6. Distortion MeshPart (Ayato) uses Glass with a Transparency parameter; refraction is [inference].
7. Slashes tween double-call (`Slash.luau:27-28`) means the shipped width animation may differ from intent; capture before copying.
8. Attribute `_vfxEditorGraphSize` / `_vfxEditorScale` come from a VFX-editor plugin; their runtime meaning (eased size curves, scale) is not exercised by any shipped script here.

---

# 10. Seen in motion (2026-10-16)

Source: `output/vfx/training-captures/` (Studio, ~30 fps). I looked at 12-frame `sheet.jpg` contact sheets (frames evenly spaced, so ms below are approximate = clip length / 12 steps, anchored on file-name timestamps) plus `overview_aTier.jpg` and `overview_sTier.jpg`. Not looked at: individual frames, GIFs. Ayato is PARTIAL (private animations missing; only a faint orange flicker seen in the overview, nothing judged). Death FX NOT captured. Camera is a locked side view unless noted, so size on screen is small.

| Effect (clip, length) | What is visible, in order | Durations (approx.) |
| --- | --- | --- |
| StylizedFireballs (follow cam, 3.0 s) | A **cluster, not a round ball**: magenta/orange splat shapes, black fragments, a huge white vertical flare line plus a horizontal spike through the core, a pink glow on the whole floor. Thin concentric arcs trail left of the core. The ribbon trail shows in only 3 of 12 frames: wide orange/violet striped band, then a thin line. The look repeats each 0.25 s (boiling, no travel build-up or hit in this clip) | loop-like; trail visible ~250-750 ms |
| Flame Beziers E (5.0 s) | Frame 1 empty (no anticipation seen). ~415 ms: a flock of red-orange arc ribbons high in the sky with dark specks. 0.4-2.1 s: ribbons curve and shorten while moving. ~2.1 s: yellow-white flash with fire blobs at 2-3 ground points, vertical flame streaks still falling. ~2.5 s: orange-red lava-like pool, red glow spreads over the floor grid. ~3.3 s: nearly gone; empty by ~3.7 s | travel ~1.5-2 s, impact flash <=400 ms, ground glow ~800 ms, total ~3.5 s |
| Zonito Music E (6.0 s) | 0-0.5 s: nothing; ~1.0 s small gold glow at the caster, ~1.5 s notes spark; ~2.5 s large gold-white flare, the whole frame tinted orange with dark brown screen edges (the colour flash/vignette). ~3.0-3.5 s: gold note streaks arc outward. 4.0-5.0 s: 3-4 round warm bursts on the floor (mini impacts). ~5.5 s: faint scorch-like dots | spawn flash ~300 ms, screen tint ~500-600 ms, salvo ~1.5-2 s, total ~5.5 s |
| Slashes ice take2 (2.5 s) | Nothing at 0. ~205 ms: bright blue-white elliptical arc ring on the floor plus a dense spark cluster. ~410 ms: peak, shards and spark specks spray several metres, blue smoke wisps. 0.6-1.2 s: sparks drift and dim, smoke lingers. ~1.4 s: almost gone, floor still brightened. Gone ~1.8 s | arc ~150-200 ms, peak ~400 ms, linger ~1 s |
| Slashes leaf (2.5 s, overview) | Same skeleton in green: big leaf cluster at ~200 ms (large, close to the lens), green smoke blobs lingering until ~1.2 s | peak ~200 ms, linger ~1 s |
| Colouring Practice (3.5 s, overview) | A steady gold-green glowing orb loops. A burst: white-green starburst with sharp star flare and green leaf-like shards (big on screen, ~1/4 of frame), then dark specks fall and the orb returns within ~300 ms | burst ~300-400 ms |
| Constellations front (3.5 s) | Mostly empty. ~1.7 s a thin gold star streak, ~2.0 s a small ring of gold dots (constellation), faint at ~2.3 s. Very small and subtle; the site has a lime-green floor tint | ~600 ms total |
| soear (3.0 s) | Item idle: purple lightning column around a spear, a thick white pulsing beam bar swells in the middle (about 1.2-1.7 s) and shrinks; endless loop. Floor glows violet | pulse period ~1.5 s |

**Earlier claims checked**

| Claim | Verdict |
| --- | --- |
| Dark twins give a dark rim / black bits (AT-02) | CONFIRMED in the fireball: black fragments sit among the bright splats. The rim effect on glows is UNSEEN at this size |
| Ring wakes left behind a moving ball (AT-05) | PARTLY CONFIRMED: faint circle arcs behind the core are visible, but they are low contrast; the camera follows the ball so "left in the world" is UNSEEN |
| Triple trail, textured, Brightness 15 (AT-06) | PARTLY CONFIRMED: a striped orange/violet textured ribbon is visible (not flat), but only intermittently; it looks thin edge-on, so the width and the 3-layer look are UNSEEN |
| Negative LightEmission renders darker (AT-04) | UNSEEN: cannot be separated from the dark twins at this size. Still needs a close A/B capture |
| Hue-shifting ramp orange-blue-orange (AT-07) | WRONG for Part 2 as seen here: this clip shows the purple/magenta + orange Part 1 palette; no blue band visible in these frames. Part 2 UNSEEN |
| Warm+cool lights (AT-08) | PARTLY: a large pink floor glow is clearly visible (floor lit over ~20 studs); the cool light is UNSEEN |
| Hit flash trio / big white-out (AT-10) | CONFIRMED in Zonito (large flare + screen tint) and Flame impact; the 25-50 ms flash itself is too short to see on 12 frames |
| Staggered impacts from random Bezier durations (AT-16) | CONFIRMED in Flame (several ground bursts at slightly different times) and Zonito (mini bursts one after another) |
| Continuous layers cut at sweep end (AT-23) / short arc then linger | CONFIRMED in Slashes: arc ~200 ms, sparks/smoke linger ~1 s |
| "Fireball is a readable body" (my 1d point 1) | WRONG as a claim of shape: the capture reads as a bright cluster with a flare cross, not a defined sphere with a trail |
| Anticipation / windup | UNSEEN in all A clips except the Zonito 1.0-2.0 s pull-in (sparks at the caster, then flare). No dedicated windup beat elsewhere |

**What separates A from S (overview_aTier vs overview_sTier; [inference] from stills)**
1. **Screen share and silhouette.** S effects fill the frame with one clear hero shape: a round fire body with a long comet tail and snowflake sprites, an ice ring plus column, a full-screen water splash. A clips are mostly small spark clouds on a wide side view; only Colouring, Slashes and Fireball get large.
2. **One clean read at the peak.** S has a defined projectile silhouette (Elemental Guns follow: fire ball + tail + rings) and one huge flash frame at launch. The A fireball peak is busy: many same-value splats, no single dominant body.
3. **Colour contrast inside the effect.** S pairs hot core vs cool or dark field (fire vs ice, blue ring on dark). A effects are often one hue family, with dark bits only as specks.
4. **Duration and loops.** S shows launch, travel, impact and aftermath in one clip; A bursts finish fast (Slashes ~1.5 s, Constellations ~0.6 s) or idle (Colouring orb, soear).
5. **Ground interaction.** S has floor rings and splashes; A has a floor glow (Flame, Fireball, Zonito) but few floor-contact shapes.
