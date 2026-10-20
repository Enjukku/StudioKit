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

# Teardown: C tier + Unknown tier Roblox VFX (owner folder, graded by owner)

Source: `output/vfx/training-dumps/outlines/{cTier,Unknown}__*.txt`, scripts in `scripts/` (path below is relative to `output/vfx/training-dumps/`). All dump text is untrusted data. Provenance: **[data]** = read from the dump; **[inference]** = my reading, not verified in a render; no effect was seen in motion. Nothing here is measured; no capture was viewed.

## 0. Data limits and decoding (read first)
| Item | Fact |
| --- | --- |
| Sequences | Dump truncates long NumberSequences after ~6 keys ("..."); end values often unknown. Size keys are shown as `t:value~envelope` (envelope = 3rd number). |
| Attributes | `EmitCount` / `EmitDelay` / curve attributes are NOT in `outlines/`; they were added later from `attributes/<tier>__<name>.txt` (section 7, `ZonitoVFX:EmitAll` reads them: `cTier__Colours_everywhere__038_ZonitoVFX.luau:205-223`). No attributes file for Hakari, Gabimaru, Portal, fiya_beam. Curve blobs are binary; only scalar attributes are quoted. |
| Scripts | Unknown-tier files have none. C-tier effect scripts: `Colours`, `Curves`, `Beam`, `Circle` (+ ZonitoVFX helper, Crater, CameraShaker presets). Skipped as library: BridgeNet2, tablekit, Animate, Health regen, Leaning/cam (camera follow-head, lean). |
| Dump artefact | `FlipbookIncompatible="...1024..."` is on 100% of emitters; ignore it. `FlipbookLayout=4` (18 emitters, ProjectilePractice) is not in my enum memory [inference: newer grid; verify]. |
| Enums | Orientation 0 FaceCam, 1 FaceCamWorldUp, 2 VelocityParallel, 3 VelocityPerpendicular. EmissionDirection (NormalId) 0 Right, 1 Top(default), 2 Back, 3 Left, 4 Bottom, 5 Front. Shape 0 Box 1 Sphere 3 Disc; ShapeStyle 1 Surface; ShapeInOut 1 Inward. FlipbookLayout 2 = 4x4, 3 = 8x8; Mode 0 Loop, 1 OneShot. Beam TextureMode 0 Stretch, 1 Wrap, 2 Static. Material 256 Plastic, 288 Neon, 788 Basalt, 800 Slate, 1568 Glass. |
| Squash sign | Which sign makes a sprite thinner is not verified; only compare relative use. |

## 1. Tier statistics from the dump [data, computed over all emitters]
| Metric | cTier (225) | Unknown (169) | aTier (461) | sTier (492) |
| --- | --- | --- | --- | --- |
| LightEmission = 0 | 54% | 29% | 42% | 55% |
| LightEmission < 0 | **0%** | 21% | 14% | 0% |
| Size has >= 4 keys (baked ease) | **7%** | **72%** | 19% | 36% |
| Squash != 0 | **0%** | 17% | 9% | 7% |
| Orientation 2/3 (velocity) | **5%** | 46% | 24% | 20% |
| ZOffset != 0 | 46% | 74% | 63% | 88% |
| Color with 2+ distinct stops | **0%** | 28% | 46% | 35% |
| Acceleration != 0 | **0%** | 17% | 20% | 22% |
| Beams / Trails (count) | 6 / 1 | 41 / 9 | 13 / 10 | 69 / 16 |
Reading: C tier has no velocity alignment, no squash, no colour gradient, no gravity, 2-key sizes. Unknown tier looks like a different library (131 unique texture ids across my files, 15 shared with S/A) built with baked-ease sizes.

## 2. C TIER

### 2.1 cTier__blue_pewpews (E key: 10-15 blue homing bolts curving to the mouse)
**Moments**: spawn cloud above player (0 to ~3 s staggered 0.2 s) -> hold 0.75 s -> fly 1 s on a bezier -> impact + crater + 1-2 flaming rocks -> 3.9 s total per bolt.
| Layer (parent) | Key values [data] | Job |
| --- | --- | --- |
| Arrow (Middle) tex 17529931231 | Or=2 Rot -90, Rate 5, Life 0.4, Size 0.8 constant, ZO 2, Lock=true, LE0 Br5, Color 43,64,255 | only velocity-aligned item; 0.8 studs, constant size |
| Specs (Middle) 16879585719 | Rate 65, Life 1-1.5, Spd 1-3, Size 0.253 -> 0, Drag 1, 4x4 OneShot | sparkle drift |
| Smoke (Middle) 16867514432 | Rate 75, Life 1-1.5, Spd 0, Size 0.3 -> 0, Transparency 0 -> 1 linear, Br5 | body blob |
| Trail1 (Trails) | Texture empty, Lifetime 0.7, WidthScale 0.119 -> 0, Br4, LE0, FaceCamera | untextured trail |
| PointLight Middle | Range 15, Brightness 0 -> 1.5 in 0.3 s | glow |
| Impact: Hit 16892346551 | Life 0.1, Size 3.33~0.87, ZO 6, Br5, LE0 | flash |
| Impact: Specs1/2/3, Smoke | Life 0.5-3, Spd 5-10, Spread -360..360, Drag 1-3, Size 0.35-1.3 | burst |
| FrontEmit smoke 16867514432 | Spd 1-8, Spread +-20, Dir Front | launch puff |
| ReplicatedStorage.VFX.Fire | smoke sheet, Rate 30, Acc (0,15,0), Size 1 -> 0.5, Tr 0 -> 1, Br6, ZO 1.5 | "fire" on rocks (is blue smoke) |
| Rock part | Basalt, PointLight Range 10 Brightness 1.5 **Shadows=true** | debris light |
Every layer: RGB (43,64,255) only, LE0, LightInfluence 0.
**Script** (`scripts/cTier__blue_pewpews__000_Curves.luau`): count `RNG:NextInteger(10, 15)` :27; spawn offset +-15 x, 5-10 y :34-40; light tween 0 -> 1.5 over 0.3 s :49; `bezier:CreateCFrameTween(..., TweenInfo.new(1, Sine))` :62 with 5 random mid points around halfway +-(7,3..7,7) :54-59; `task.delay(.75)` :64 then FrontEmit + CameraShake("CurveStart") :66-68; `task.wait(.9)` ("spawn the impact effects slightly early") :71; impact + `CreateCrater(Projectile, 5, 3, -10, 2, (2,1,2.5))` :81; 1-2 rocks, `ApplyImpulse(+-25, 25-50, +-25)` :107; rocks fire off at 2.5 s, shrink Size -> 0 over 1.5 s :109-116; shake "Curve" :122; `task.wait(1.7)` :124; destroy +0.51 s. Spawn gap `task.wait(.2)` :135. Shake presets: CurveStart (mag 0.5, rough 0.5, in 0, out 0.4 s); Curve (1.4, 25, 0, 0.45) [data: `...blue_pewpews__041_CameraShakePresets.luau`].
**Held back vs S/A**: (1) the bolt is smoke + dots with no hot core, no stretch, no textured trail (CW-04, CW-05); (2) LE0 everywhere, single hue (CW-01, CW-02); (3) 2-key linear size/transparency (CW-03); (4) 10-15 overlapping Curve shakes with no merge window (CW-07); (5) physical rocks + fire made from smoke sheet (CW-08).

### 2.2 cTier__fiya_beam (E key: 2 s charge then 5 s orange beam to the mouse)
| Layer | Key values [data] |
| --- | --- |
| Start (charge/muzzle), 5 PE | dust 16843151641 Rate **350** Life 1 Spd 10-20 Drag 2 Br9; smoke 16867514432 Rate 100 Size 0 -> 8+ (2 envelope) Tr 0.656 -> 1 Br10; 16860284058 Rate 17 Br18 ZO 1; sparks 16878181512 Rate 50 Spd 15-25 Br15; "Front" Rate 50 Dir Front Spread +-10 Size 5.96 -> 0 Br7 (enabled at fire) |
| End (impact), 7 PE | Impact 16892242416 Life 0.1 Size 10 -> ~0 ZO 4 Br10; dust Rate 145 Spd 20-35; smoke Rate 25; fan "Dir Back" Rate 70 Spd 45-65 Life 0.5-1.25 ZO 5; light Range 25 Brightness 2 |
| Beam2 / Beam1 | both tex 16892453445, **TextureMode 2 Static**, TextureLength 25 / 10, TextureSpeed 6 / 10, Width 5 -> 5, Segments 10, FaceCamera, **LE0**, Brightness 15 / 5, Transparency 1,1 then tween to 0, Color 170,73,34 |
All colour 170,73,35 (brown-orange); every emitter LE0. Light on Start: Brightness 0 -> 2 over 0.5 s, Range 25.
**Script** (`scripts/cTier__fiya_beam__000_Beam.luau`): spawn 10 studs above root :24; FOV -> 90 over 1.5 s :32; light 0 -> 2 over 0.5 s :34; `task.wait(2)` charge :36; aim sampled "just before" fire :38; Front on :50; ColorCorrection tint orange (255,85,0) 0.25 s with Reverses, guarded against stacking :52-54; two beam Transparency tweens to 0 in 0.5 s via BoatTween "Smooth" :56-96; shake "Beam" :100 (mag 2, rough 50, in 0, **out 6 s**); FOV -> 70 in 0.25 s :102; `blurFrame(0.25, 15)` :104; `CreateCrater(part, 15, 6.5, -10, 6.5)` :105; End light -> 2 :107; 5 s later lights fade 1 / 0.5 s, beams to Transparency 1 in 0.5 s, `TaskDebris(Beam, 10)` :111-162; during the beam every 0.1 s 1-2 rocks size 1-2 with `HalfIntensity = 1000` impulse, shrink at 3 s :168-196.
**Held back**: beam is a constant-width pipe (Width 5/5, no taper, Transparency flat 0 after tween -> hard ends, no end flare on the beam itself) (CW-06); LE0 beam at Brightness 15 instead of an additive glow layer + body (CW-01); 6 s shake tail and FOV/tint/blur stacked (CW-07); charge is 350/s omni dust (CW-10); no ground scorch/impact ring.

### 2.3 cTier__the_circle_thingie_1_ (E key: blue magic circle + light pillar + aura, 3.7 s, player frozen)
| Layer | Key values [data] |
| --- | --- |
| Aura (cloned onto limbs), 4 PE x 5 parts | smoke 16867514432 Or=1 Rate 20 Life 0.5-1 Spd 2-4 Size 0 -> 0.85 -> 2.74 Tr 1 -> 0.49 -> 1 ZO **-1** Br2 LE1; star 17062454564 Size 0 -> 0.85~0.55 -> 0 ZO 3 Br3; star2 Size 0.35 ZO 3; 16867490141 Rate 25 Size 0.8 Tr 1 -> 0.43 -> 1 ZO 2.9. Color 47,47,255 for all. |
| Circles (loop) 3 PE | tex 16878165349 / 16878097832 / 16878166759 Or=3 (flat), RotSpeed 180, Size 5 / 3 / 6 constant, Tr 1 -> 0 (0.29) -> 0 (0.63) -> 1, Br7, LE1, Rate 2 Life 1 |
| Emit (burst) 11 PE | shock rings Or=3 Size 0 -> 5.9 -> 7.2.. (envelope 1-5); hit 16892346551 Life 0.1 Size 15 -> 3, ZO 2; second Life 0.2 Size 22; sparks Spd 30-100 Drag 8 Spread +-45 (3 textures, Size 3.03~1 -> 0) Color 105,120,255 |
| Second (loop) 4 PE | wind 18329666173 RotSpeed 200-350 Life 2; waves Rate 15; two white-colour LE0 sheets 18374724912/18374738364 Size 10 Tr 1 -> 0.18 -> 1 |
| Beams a / b | tex 16892453445, Static, TextureLength 15 / 20, TextureSpeed 1 / 1.5, Width 12, FaceCamera, LE1, Brightness 2 / 3, **Transparency 1 -> 0.3 (0.37) -> 1** (a), 1 -> 0.3 -> 1 -> 1 (b) |
| PointLight | Range 15 colour (0.28,0.13,1), Brightness 0 -> 5 in 0.7 s |
**Script** (`scripts/cTier__the_circle_thingie_1___000_Circle.luau`): WalkSpeed 0 :31; Scriptable camera, tween to 4 up / 13 back in 0.5 s :33-37; `wait(.5)`; `ColorFrame(0.2, 2, (0.67,0.67,1))` :53; beam Transparency tween 0.5 s to stored sequences :55-76; aura emitters cloned to limbs :78-84; shake "Buildup" (0.5, 4, in 0.2, out 1.5) :86; FOV -> 90 over 2 s :87; light -> 5 :90; `wait(2.5)` :93; beams out 0.3 s, aura off with `TaskDebris(v, Lifetime.Max)` :95-123; FOV -> 70 in 0.2 s :125; crater (10, 5.8, 3, 2) with star emitter on each rock :127-135; `ColorFrame(0.01, 0.35, deep blue)` flash :137; shake "Circle" (0.5, 10, 0.01, 0.8) :138; `EmitAll(Circle.Emit)` :139; light -> 0 in 1 s; `wait(.7)`; control returned :144-148. Total ~3.7 s lock.
**Held back**: best C-tier layering (ZOffset ladder, bell-shaped transparency, flat rings with spin), but single colour 47,47,255 on everything, no negative/contrast layer, no white-hot centre, constant sizes (5/3/6) with no scale-in, pillar is two scrolling beams without a base flare (CW-02, CW-03); player and camera locked 3.7 s (CW-13).

### 2.4 cTier__Colours_everywhere (E key: 7 colour orbs explode in sequence)
| Layer (per orb x 7 colours) | Key values [data] |
| --- | --- |
| 23 PE per orb = 4 recipes x 3 colour variants (1 main, 2 lighter, 3 complementary) + 11 Emit-driven | Gather (Enabled): sphere Surface Inward (Shape 1/1/1), Rate 35 Life 0.5 Spd 7.1 (3.5 studs): star 17062454564 LE1, soft 16867352057 LE0, glow 16867347280 Rate 25 Size 1.77 -> 0 Tr 1 -> 0.945 -> 1, ring 16867389591 Rate 15 LE1 Tr 1 -> 0.34 -> 1. |
| Burst (Rate 0) | star Br7, 16859930558 Br4 (4x4 15 fps), Hit 16892346551 Life 0.1 Size 4.54~0.83 ZO -0.11, smoke 16867347280 Size 2.54 **Tr max opacity 7%** (0.929). Life 1.5-2.1, Spd 12-18, Drag 5, Spread +-360, all LE0 |
| PointLight | Range 9, colour = orb colour, Brightness 0 -> 1 in 0.5 s |
Palettes: Orange 255,85,51 / 255,134,94 / 85,170,255; Red 255,46,49 / 255,115,115 / 85,170,255; Blue 85,170,255 / 170,170,255 / 85,85,255; Purple 91,62,255 / 58,43,98 / 85,85,255; Pink 255,85,255; Green 118,255,87 / 170,255,0 / white; Scarlet 255,46,140 / 255,255,127. Only **6 unique textures** across 161 emitters.
**Script** (`scripts/cTier__Colours_everywhere__000_Colours.luau`): FOV -> 75 and ColorCorrection Saturation -> -0.35 over 1.9 s :26-27; 7 orbs scattered +-10 studs, 0.1 s apart :33,60; light 0 -> 1 in 0.5 s :37; `task.delay(2)` :39: Saturation = 0, **TintColor -> orb colour in 0.1 s** :41-42, FOV hard-set 70 :44, `ToggleAll(off)`, light -> 0 in 0.25 s, `EmitAll(Clone, true)` :46-48, shake "Colour" (0.6, 10, 0.01, 0.275) :50, `blurFrame(.04, 17)` :51, destroy after 2.5 s :53-56; tint back to white 2 s after loop :64-66. Cooldown 1 s (`VFX.luau`:13).
**Held back**: 7 whole-screen tint changes inside 0.7 s (about 10 per s, a flash-safety failure by the project rule; CW-07); 161 emitters, ~200 live per orb at once (CW-10); variants are copy-paste recolours of 4 recipes (CW-11); burst sparks LE0; 7%-opacity layer is invisible waste.

## 3. UNKNOWN TIER (my tier guesses are [inference])

### 3.1 Unknown__CartoonE (12 PE; one cartoon explosion, Emit-driven)
Layers [data], all Enabled=false, LightInfluence 0, 1 Attachment:
| Layer | tex | LE | Br | ZO | Or | Life | Spd / Drag | Size / colour |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Impact450 (flash) | 11037781450 | 1 | 15 | **1.0** | 0 | **0.05** | 0 | 15 constant, 255,74,29 |
| HitImpactD | 93600118618782 | 1 | 15 | 0.001 | 0 | 0.2 | 0 | 0 -> 8.6 -> 11 -> 12.4 -> 13.3 -> 14 (20 keys, ease-out) |
| Impact9 (ring) | 16880037488 | 1 | 5 | 0 | **2** | 0.3-0.6 | 0.001 | 0 -> 10.4@0.1 -> 17 (envelope 3), Rotation +-300 |
| Stylized Smoke56 circle (flat ring) | 15855917528 | 0 | 5 | 0 | **3** | 0.3-0.8 | 0.001, Spread 30 | 0 -> 10.8@0.1 -> 17; 255,116,70 -> black |
| Grey Smoke 7 / 6 | 75900660533054 / 80330286700273 | 0 / **-1** | 15 | 0.002 / 0.003 | 0 | 0.3-1.3 | 15-80, **Drag 8 / 12** | 0 -> 3.5@0.1 -> 5.7; colour 255,77,33 -> 0,0,0; #6 Tr 0 -> 0.007@0.07 -> ... slow ease-in |
| Style Smoke 13 / ImpactBD10 | 105164420635468 / 127457734705398 | 0 | 1 | -0.001 / -0.002 | 0 | 0.3-1.0 | 15-70, Drag 8 | 3-stop colour 255,116,69 -> 251,73,29 -> 0; BD10 Size 0 -> 5.3~2.5@0.1 -> 3.6 -> 0 |
| Star20 x2 | 17062453173 | 1 | 5 | 0.008 / -0.003 | 0 | 0.3-1.0 | 15-70, Drag 8 | **twinkle**: 0 -> 3.77@0.1 -> 0@0.19 -> 1.75@0.4 -> 0 |
| OffCentered Spec 85 | 15658580283 | 1 | 5 | -0.004 | 0 | 0.5-1 | 15-80, Drag 8 | tiny 0.03 -> 0.9 (envelope 0.01-0.3) |
| Oval Fading | 15659089816 | 1 | 5 | 0.009 | **2** | 0.1-0.5 | 30-150, Drag 8, Rot 90 | 0 -> 3 -> 4.7 oval streak |
Moments: t=0 50 ms flash (ZO 1, on top) -> 0.2 s hit disc -> 0.1-0.6 s rings + sparks/stars fly out at 15-150 studs/s and stop by Drag 8 -> smoke outwards and darkens to black 0.3-1.3 s. No script.
**Tier guess: A** (maybe S-). Reasons: every layer has one job; flash 50 ms on top; ZOffset ladder in 0.001 steps; deceleration by Drag; colour cools orange to black; negative LE on one smoke; baked ease-out sizes. Weakness: no ground ring/dust/debris, no light, 12 near-same-hue layers [inference].

### 3.2 Unknown__Goal_VFX (11 PE; "ThunderBolt" lightning burst, Emit-driven)
Layers [data]: Lightning33 16 (tex 17005876540) Life 0.5 Size 0 -> 11.8@0.1 -> 23.8, LE0; Lightning20/23 (LE **-5**, Or=2, Size 0 -> 14.2 -> 26.9 envelope 10, Drag 5, Rate 15), Lightning26 (Or=3), LightningNew6 (LE -1, Squash 1: 2.61~0.39, Spd 30-80); Spec22 (Spd 12-75, Drag 2, Size 0 -> 0.02..); Spec48 + Star12 (LE **-5 / -1**, Or=2, Rot 90, Squash 1.16~0.59, Spd 25-75, Drag 3, Size 0 -> 5 -> 0); Flare28 (tex 122881636456623, **Size 37.3 -> 23 -> 14.3 -> ... shrinking**, Squash -0.41, Life 0.3, ZO **5**); '1' (8x8, LE -1, Size 0 -> 7.6 -> 18, Life 1); Circle2 (ZO **-1**, Size 0 -> 18.9 -> 36, Life 0.5). Colours all orange 255,102,51-255,163,98.
**Tier guess: A.** Reasons: 5 lightning textures stacked at different Orientation (0/2/3) so bolts show from any angle; big flare shrinks (reverse pop) at ZO +5 over a ground circle at ZO -1; negative-LE saturates edges. Limit: monochrome, no script to judge timing [inference].

### 3.3 Unknown__Portal_VFX (6 PE; looping portal, all Enabled)
Black 14944433028 (LE0, **Br0**, white colour, Rate 50, Life 0.5-1, Spread 0-360, Size 1 -> 4.6~3, Tr 0 -> 0.27 (0.85) -> 1, Squash 0~1.2) + Blue same texture (LE1, Br15, 55,85,255, ZO 0.5, Drag 1) = dark underlay + glowing overlay; Dots 14111878332 (LE -5, Br15, RotSpeed +-600, Life 2-4, Size 0 -> 1.2 -> 0, 56,86,255); Smoke 11799607237 (8x8, LE -5, Br0, Rate 100, Tr 1 -> 0 -> 1, ZO -5, Drag 2); CrescentS 13832097149 + Shockwave 14624767785 (LE0 / -5, Rate 15 / 10, Life 1-2, Size 1 -> 10~3, Tr 1 -> 0 -> 1, Squash 0 -> 1.6 / 1.5, ZO -1). Steady ~360 live [data].
**Tier guess: B+.** Compact, correct underlay/overlay and bell transparencies, but a one-colour loop with no motion hierarchy or accent.

### 3.4 Unknown__Gabimaru_Aura (25 PE = 5 emitters x 5 limbs; character fire aura)
Per limb [data], all Enabled, Lock=true, LightInfluence 0: Fire1 16845756972 (LE0 Br15 ZO **-1.0** Rate 50 Life 0.5 Spd 1-2 Size 0 -> 0.2@0.1 -> 0.47 envelope 0.5, 255,43,1); Fire2 16847032740 (LE **-5** ZO -0.9, colour 241,51,255 -> 254,39,20 -> 255,38,0); Fire3 16845151306 (LE -5, ZO -0.8, Rate 100, Tr 0 -> 0 (0.8) -> 1, 4+ colour stops 255,85,0 -> 254,83,44 -> 249,76,255 -> 251,80,150); Glow 16879789169 (LE1, ZO -0.97, Size 1, Tr 1 -> 0.24 -> 1, Life 1); Dots 16997104240 (LE -5, Rate 100, Drag 3, Size 0 -> 0.37 -> 0). Steady live ~1075 [data, Rate x mean Life].
**Tier guess: B/A-.** Strong: ZOffsets negative so flames sit behind the body, hot-to-purple colour sequence, hold-then-fade transparency. Weak: ~1000 live on one character (over the practitioner's 1,000 watch line, ZO-01), identical stack repeated on every limb [inference].

### 3.5 Unknown__Hakari_Aura (14 PE on HumanoidRootPart/Ground; green ground aura)
Layers [data]: Crescents 13832097149 (Or=3, flat, LE0 Br0 white, Size 1 -> 7.7, Tr 1 -> 0.56 -> 1, RotSpeed +-100); Shockwave 14624767785 + Shockwave2 18202540006 (Or=3, LE -5, Br15, Size 1 -> 9.6 / 6.7, Life 0.5); Fire1/2/3 (18202137741 / 18202150088 / 18202244746, 4x4, ZO -1 / -0.8 / -0.5, Size 1 -> 9.5, Tr rise 0.3 -> 0.95); Dots + Dots2 (Rate 50 / **200**, RotSpeed +-600, LE -5); Shards / Shards2 (Or=2, Rate 50 / **150**, Spd 5-100, Spread 100, LE -5, Br10); Stars (Spd 30, Spread 120, Drag 3, LE -5); SmokeGlow (LE1, ZO 0.5); Lightning 18130022460 (Or=3, Size 1 -> 13, LE -5); Glow 1075864321 (LE1, Br3). All green 25-89,255,68-139.
**Tier guess: A-.** Complete ground-aura stack (flat rings, rising fire, velocity shards, lightning, glow). Weak: three nearly duplicate shard/dot layers at Rate 150-200 (overdraw); single hue.

### 3.6 Unknown__Meteor_VFX_Open_Source (32 beams, 16 PE, 2 meshes; 50-stud meteor + impact) - PROJECTILE, extra depth
**Head** [data]: MeshPart "Meteor" Neon (288) 50x50x50 orange 255,142,29, mesh 6585577547, inside "Meteors/meteor_Icosphere_cell.004" Slate (800) 55x55x55 brown 160,95,53, mesh 6585577423 (name = cell-fractured icosphere) [inference: rock shell with cracks showing a hotter neon core].
**Tail beams** (8 radial ribbons x 4 layers = 32), geometry from Attachment CFrames [data]: ring "0" at y -26.35 (radius 0.5, bottom of the head) to "BlackEnd" ring at y +58.4 radius 36 -> a cone of 8 ribbons flaring behind the head (the tail axis is local +Y). A second set from "Center" (y -26.35, r 2-5) to "Wind" (y -6.2, r 65) forms a wide skirt/shock-cone.
| Beam | Texture / mode | Width0 -> Width1 | Curve / Segments | LE / Br / colour | Transparency |
| --- | --- | --- | --- | --- | --- |
| Beam1 (body, x8) | 14050889274 Stretch(0) Speed 5 | 10 -> 50 | CurveSize1 **-100**, Segments **50** | LE0 Br0 white | 1 at head end, 0.987@0.07, 0.947@0.13, 0.874@0.19, 0.683@0.3 (rest truncated) |
| Beam2 (glow, x8) | 16892453445 Stretch Speed 3 | 30 -> 80 | 0 / 50 | **LE1 Br15** white | 1 -> 0.997 -> 0.986 -> 0.967 -> 0.918@0.3 (very faint) |
| Beam1 coloured (x8) | same as Beam1 | 10 -> 50 | -100 / 50 | LE0 Br15, 255,43,28 | 1 -> 0.986 -> 0.943 -> 0.864@0.19 -> 0.659@0.3 |
| Beam2 plain (x8) | as Beam2 | 30 -> 80 | 0 / 50 | LE0 Br0 white | as above |
Each ribbon exists 4 times with different LE/Brightness/colour so body (LE0, keeps opacity and silhouette), additive glow (LE1) and hot colour (red) each have their own layer [inference]. FaceCamera false (ribbons are 3D planes).
**Emitters on Meteor**: Spec34 (Ground attachment; tex 16879828729, **LE -3**, Or=2, Rot 90, Rate 100, Life 1-2, Spd 15-100, **Acceleration (0,100,0)**, Drag 1, Dir Right, Size 0 -> 0.05 -> 0.2 -> 0.46 -> 0.83 with envelope ~50%, 255,43,24) and Spec22 (Rate 100, Spd 50-150, Drag 2, 255,72,26) shoot rising sparks; Main attachment, all **LockedToPart true**: Impact48 (16997086012, Or=3, Size 1 -> 24.9@0.1 -> 40@0.2 -> 48@0.5, envelope 5, 255,63,29 -> 115,0,0), Circle66 (16879522362, Or=3, 1 -> 20 -> 32 -> 38.7, -> black), Circle2 (16877839414, Or=3, 1 -> 29.8 -> 47.9 -> 58, -> black), Fire24 (16849149076, Or=0, **Spd 50-300, Drag 10**, Size 1 -> 7.8 -> 12 -> 14.5), Fire25 (16849232483, Or=2, Rot -90, same motion, 255,86,29 -> 108,0,0). All Life 0.5-1, Rate 20-50, LE0 Br15, Enabled.
**ImpactMeteor** (9 PE, Enabled=false, Emit-driven) [data]: WD 16877839414 (Or=3, Life 1, Size 1 -> 53 -> 90 -> 114 -> 137, Tr 0 until 0.29 then rises, 255,78,24 -> black); Fire38 16860307403 (Or=3, same growth, 255,76,16 -> 99,29,6); Ground15 18646039382 (Or=3, **Life 3.0**, Size 0 -> 77.8@0.1 -> 97, Tr 0.06 -> 0.035 -> rises = long scorch, 255,51,24 -> 0); Impact48 (Size 0 -> 40 -> 92); Crescent12 17388366674 (Or=3, Size 0 -> 35 -> 60 -> 92 envelope 30, Tr 1 -> 0.64@0.3..); Fire11 + Smoke8 (Spd 15-200, Drag 3, Lock true, Size 0 -> 8.8 -> 15 -> 23 / 15.6 -> 19.5); Smoke48 (8x8, Life 1-2, Spd 150, Dir Right, Tr 1 -> 0.98 -> 0.54, 255 white, Br0); Spec40 (16879840263, Or=2, **Spd 30-500**, Drag 3, Size 0 -> 0.16 -> 0.64 -> 1.5 -> 2.7 envelope 55%). 
**Choreography**: no scripts. The Part "ImpactMeteor" has Attachments Main (y -0.5) and Top (y +9.8) [data].
**Tier guess: A (S-possible).** Reasons: head is a real irregular mesh, motion is in 32 flared ribbons plus Drag-decelerated fire and rising negative-LE sparks; impact has scorch, ring, crescent, smoke and fast specs; all sizes baked ease-out. Weakness: monochrome red/orange, 32 transparent big ribbons would overdraw on phones [inference].

### 3.7 Unknown__ProjectilePractice (85 PE, 9 Beam, 9 Trail, 18 meshes, 19 RayValue; reusable projectile kit) - PROJECTILE, extra depth
Structure [data]: Attacker part with `launch1`, `launch2` (muzzle/charge presets), `Bezier` / `Bezier2` (flight: `Points/1/T0,T1` tangent attachments at +-4 studs, RayValues = path data) each with a `Bullet` Part ("trail" attachment pair at x +-1.37 / +-3.09 = trail width 2.8 / 6.2 studs) and a `Folder "EmitOnFinish"` (impact burst). Victim part with PointLight (Range 8, Brightness 0.5). `ScreenEffect` part (4 attachments, Blurred Spec 11 sheet 284205403, **Lock=true, Squash -1/-1/+1/+1**, Size 1.64 / 1.26, Rate 0.5, Life 1, Tr 1 -> ~0) [inference: camera-attached screen-edge glow cards].
Nothing is Enabled (script triggers); Odd Rates (13.3414, 4.4471, 8.0176) and Speeds (54.9 vs 167.2) are the same recipe re-timed per variant: attributes show `TimeScale_Duration` 0.112 (Bezier, flight 0.337 s) vs 0.187 / 0.045 (Bezier2, 0.5 s) [data, section 7].

**A. Bullet (flight) - the part that reads as motion** [data]
| Layer | Values | Job |
| --- | --- | --- |
| Wind29 x2 (tex 109474863702604) | Or=3, Spd 0.0009, Spread 5, Dir Right, LE0 Br1 + LE1 Br1 copies (Rate 4.4 / 17.8, Life 0.56-1.12), Size 0 -> 0.9 -> 1.4 expo (keys at t 0.001, 0.005, 0.014), Tr 0 -> 0.13 -> 0.26 .. | wind-ring stamped across the path (dark LE0 + bright LE1 copy) |
| Sideways Spec 37 (16924383752) | **Or=2, Rot -90, Squash 1, Spd 55 (Bezier2: 167), Spread 15, Life 0.11-0.34 (0.045-0.135), Rate 17.8 (44)**, Size 0 -> 0.85 -> 0, 175,255,101 | thin streaks shot backward (speed streaks) |
| OffCentered Spec 85 (15658580283) | same speed/life, Squash 0 -> 0.92 envelope, Br5 | second streak colour |
| Trail "Trail" | **no texture**, solid 75,255,75, Lifetime 0.1, MinLength 0.1, WidthScale 0 -> 0.0017 -> 0.08 -> 0.13 (flat from 0.18) | solid core |
| Trail "Beam100" tex 85772363699785 | white-green 201,255,201, Lifetime 0.16-0.2, WidthScale 0.03 -> 0.13 -> 0.40 -> 0.54 -> 0.66 -> 0.76 | soft textured glow |
| Trail "Beam105" / "Beam Slash 1" | LE **1**, Brightness 3-5, Lifetime 0.1-0.12, WidthScale 0 -> 0.11 -> 0.22 -> 0.33 -> 0.43 -> 0.52, 161,255,99 | additive hot streak |
| Trail "Beam112" / "Beam2" | tex 137097904100100 / 16892370570, Transparency also ramps 0 -> 0.12 -> 0.25 -> 0.36 (fades with width) | textured streak |
All Trails: FaceCamera true, LightInfluence 0, TextureMode 0, 4 trails on one attachment pair; Brightness 15 / 1 / 3 / 5. Whole bullet has **no head sprite or sphere**: the invisible Part carries streaks and trails; the head glow is the converged trail starts [inference].
**B. Launch (launch1 / launch2)**: swirl 5 14050102591 (LE1 Br5 Size 0 -> 1.2 -> 3.4, Life 0.5, Tr 0 -> 0.02 -> 0.42); 'groundcharge' Wind4 + Stylized Shockwave **Size 9 -> 0** (implosion ring, Tr 1 -> 0.99..); 'groundeffect' Wind18 (Or=3, Dir Bottom, Spd 40-60, Drag 8, Tr 0.7 -> 0.78..), Smokey Crescent 17085222506 (4x4, Spread 15), Whole swirl 17612139917; Star102 17391818367 (**Squash -1.2 -> 0**, Size 8.6 -> 7.5 -> 6.4 shrinking, Life 0.6 = lens-flare star snap); Abstract Lens Flare 97555792571613; 'beam1' x4: BeamDBeam 78081979834607 Width 2 -> 15 CurveSize -2 / 2 Segments 10 LE1 Br5 colour 152,255,88 from 4 points on a ring r=5 (z 5.95) to the muzzle = converging charge rays; sparks 'Sideways Spec 37' x6 fanned with Dir 5/3/0 + Acceleration (+-113,0,0) or (0,-143,0); leaves (SpinModel, Shape 3 Disc, Acc (0,-25..-70,0)); 'Glowing Bezier Line' 16056965573 (Or=2, Acc (0,36,0)). Mesh VFX: Models with Start/End parts, SpecialMesh 8501563708 (Scale -0.39 etc., **negative scale**) + Decal textures 14101024770 / 88983666349740 / 14261953171 (Transparency 1; tween Start scale ~0 -> End scale 0.3-0.7); "Spinnywind" two MeshParts mesh 4681227436 Neon, size 0.001 -> 16.9 [data].
**C. EmitOnFinish (impact, 13-17 layers)**: Impact 111294697054428 (4x4, Life 0.2-0.33, ZO **2**, Size 0 -> 1.06 -> 2.1 -> 3.2 ...; 247,255,94 -> 56,255,61); Wavy Water Circle, Chromatic Water Energy Lens Flare (Tr 0.9 -> 0.96), Impact70, Water Vertical Spiral (Or=3), Moving vertical bezier (Or=2 RotSpeed +-100), Flare Twinkles (Life 0.1-0.3), Outward Fog (4x4 at layout 4, Br 0.1, Tr 0 -> 0.27 -> 0.8), Basic Blurry (Drag 6-8), green leaf spinning, Sideways Spec 37 + OffCentered Spec 70 + Blurred Spec 11 (Spd 13-44, Acc (-100..,-79..)), Wind28/45 (Drag **15**, RotSpeed +-100, Or=3). Colours run bright yellow-green -> saturated green (3-stop sequences).
**Tier guess: A, borderline S.** Reasons: complete, named, reusable pipeline (launch -> flight -> EmitOnFinish); 4-trail stack and speed streaks built for readable motion; baked expo size keys; consistent 3-stop colours; per-variant scaling. Weak: 85 emitters + meshes is heavy for phones, no scripts so timing is unverified.

## 4. Technique catalog (CT)
| ID | Technique | Evidence [data] | Use for our fireball |
| --- | --- | --- | --- |
| CT-01 | **Baked ease-out Size**: 20 keys, ~60-70% of final size at 10% of life, then settle; ProjectilePractice goes to keys at t=0.0004, 0.0035, 0.013 (size 0.9 at 0.04% of life) | CartoonE Impact9 0 -> 10.4@0.1 -> 17; Meteor Impact48 1 -> 24.9 -> 40 -> 48; PP Wind18 | pop-in, never linear |
| CT-02 | Flash sprite = 50-100 ms, large, ZO top, tinted not white | CartoonE Impact450 Life 0.05 Size 15 ZO 1; blue_pewpews Hit Life 0.1 ZO 6 | muzzle/impact punch |
| CT-03 | Velocity-parallel streaks: Or=2, Rot 90/-90, Squash, speed 55-167, Life 0.05-0.35 | PP Sideways Spec 37; CartoonE Oval Fading | motion cue, not a round dot |
| CT-04 | Flat rings: Or=3 + Speed 0.001 + Dir Top/Bottom, Size ease-out, Tr bell | Meteor Circle66/WD; Hakari Shockwave; PP Wind18 | ground/shock rings |
| CT-05 | Speed ~0.001 = stationary billboard that keeps emitter orientation | CartoonE flash/ring; Goal Flare28; PP Wind29 | anchored glow |
| CT-06 | Drag-decelerated burst (Speed 15-500, Drag 3-15): shards fly then stop | CartoonE Drag 8-12; Meteor Fire24 Spd 50-300 Drag 10; Spec40 Spd 30-500 | explosion shape |
| CT-07 | Negative LightEmission (-1 to -5) with Br 5-15 | Hakari 11/14 PE; Goal lightning; Gabimaru Fire2/3, Dots; Meteor Spec34 -3 | saturated dark-edged sparks [inference: mechanism not captured; A/B in Studio] |
| CT-08 | Dark underlay + bright overlay pair of the same texture | Portal Black (LE0 Br0) + Blue (LE1 Br15); PP Wind29 LE0/LE1 copies; Meteor 4x ribbons | keeps opacity AND glow |
| CT-09 | ZOffset ladder in 0.001-0.009 steps plus big offsets (+1 flash, +5 flare, -1 ring) | CartoonE; Meteor 0..-0.005; Gabimaru -1..-0.8 (aura behind body) | fixes sort order |
| CT-10 | Colour cools over life: orange -> deep red -> black, 3-4 stops | CartoonE smoke; Meteor 255,63,29 -> 115,0,0; Gabimaru 4 stops | hot core to ember |
| CT-11 | Trail stack: 4 trails on one attachment pair (solid core, soft glow, additive slash, textured), Lifetime 0.1-0.24, WidthScale spindle 0 -> peak, width = attachment span | PP Bullet | textured, tapered tail |
| CT-12 | Ribbon cone: 8 radial Beams, Width 10 -> 50, CurveSize -100, Segments 50, repeated 4x with LE/Br variants | Meteor | huge flame skirt |
| CT-13 | Twinkle size: 0 -> peak@0.1 -> 0@0.19 -> 0.5x@0.4 -> 0 | CartoonE Star20 | star flicker |
| CT-14 | Reverse pop: Size 37 -> 3 shrink flare; Squash -1.2 -> 0 star | Goal Flare28; PP Star102 | lens-flare snap |
| CT-15 | Implosion telegraph: ring Size 9 -> 0; converging charge rays 2 -> 15 wide | PP groundcharge, beam1 x4 | wind-up read |
| CT-16 | Bezier flight with tangent attachments (T0/T1) and `EmitOnFinish` folder | PP; Curves.luau:52-62 | arc + trigger |
| CT-17 | Mesh VFX by Start/End scale tween (negative-scale SpecialMesh + Decal; Neon MeshPart 0.001 -> 17) | PP | domes, vortex |
| CT-18 | Rock shell + Neon core meshes (Slate 55 over Neon 50) | Meteor | cracked-glow head [inference] |
| CT-19 | Long ground scorch: ring Life 3 s, Size 0 -> 78 -> 97, Tr 0.06 -> 0.04 | Meteor Ground15 | lasting impact mark |
| CT-20 | Aura on limbs: 5 layers (3 fire, glow, dots), Lock true, ZO negative, Rate 50-100, Life 0.5 | Gabimaru | character fire |
| CT-21 | Hold-then-fade Transparency: 0 -> 0 (0.8) -> 1, or bell 1 -> 0.3 -> 1 | Gabimaru Fire3; Circle beams | no pop |
| CT-22 | Inward sphere gather (Shape sphere, Surface, Inward, Speed ~7, Life 0.5) | Colours orb | charge-up |
| CT-23 | Two beams, same texture, different TextureLength / TextureSpeed (25 @ 6, 10 @ 10; 15 @ 1, 20 @ 1.5) | fiya_beam; Circle | parallax scroll |
| CT-24 | Moment bundle: FOV +15-20 over 1.5-2 s, snap back 0.2-0.25 s on release; tint pulse; blur 0.04-0.25 s; shake (mag, rough, in, out) | Circle.luau:87,125; Beam.luau:32,102; Colours.luau:26 | all [practice] only at rating >= 8 (see skill CA-01) |
| CT-25 | Reuse: few texture ids, many roles (Sideways Spec 37 x~11; 6 ids for 161 PE) | PP; Colours | memory (ZO-11) |
| CT-26 | Scale one recipe to several sizes (rate/speed/life multipliers) | PP Bullet vs Bezier2 | variants cheaply [inference] |

## 5. Weaknesses seen (CW)
| ID | Weakness | Where | Fix direction |
| --- | --- | --- | --- |
| CW-01 | Glow/spark layers at LE0 (flat, not additive); beam Brightness 15 at LE0 | blue_pewpews all; fiya beams; Colours bursts | LE1 on cores, sparks, beam glow; keep LE0 body |
| CW-02 | One RGB on every layer; no hot core, no 2nd hue, no colour over life (0% multi-stop) | blue 43,64,255; fiya 170,73,35; Circle 47,47,255 | 3-4 stop sequences, white-hot centre, cool edge |
| CW-03 | 2-key, linear Size/Transparency (47% two-key); smoke Tr 0 -> 1 linear; Circle rings constant 5/3/6 | all C | baked ease-out, 3+ keys |
| CW-04 | No velocity alignment / Squash (5% / 0%): sparks are round camera-facing blobs; only 0.8-stud Arrow | blue_pewpews | Or=2 streaks with Squash, speed 55+ |
| CW-05 | Projectile = smoke + dots + one untextured trail (WidthScale linear 0.119 -> 0, Lifetime 0.7) | blue_pewpews Trail1 | trail stack CT-11, head core |
| CW-06 | Beam is a pipe: Width 5 -> 5, Transparency flat, Segments 10, 2 same-texture layers, no end flare/taper | fiya_beam | taper Width/Tr, additive glow beam, base + end flares |
| CW-07 | Screen channels stacked and unmerged: 6 s shake tail, FOV + tint + blur on one event; 7 tint swaps in 0.7 s; 10-15 overlapping shakes | Beam, Colours, Curves | one shake per event with merge window; flash count rule (guardrails) |
| CW-08 | Physical rocks with impulse 1000 and smoke-sheet "fire"; Shadows=true light on a rock | fiya, blue | cosmetic debris, no shadows |
| CW-09 | Same few sheets in every role (star + smoke) so layers look alike | Colours, Circle | distinct silhouettes per layer job |
| CW-10 | Overdraw: 161 PE, ~200 live per orb x 7; fiya charge 350/s; Gabimaru (Unknown) ~1075 live | Colours, fiya, Gabimaru | Rate x Life budget, burst via Emit |
| CW-11 | Copy-paste recolour variants (4 recipes x 3 colours x 7) and a layer at 7% opacity | Colours | one recipe, tint in code |
| CW-12 | Player/camera locked 3.7 s (WalkSpeed 0, Scriptable camera); script quirks (`ToggleAll` precedence toggles Trails always; server Vector3Value for aim) | Circle, Curves | do not lock input; not VFX craft |

## 6. Projectile anatomy: how ProjectilePractice and Meteor read as motion
| Part | ProjectilePractice (bolt) | Meteor (mass) |
| --- | --- | --- |
| Head shape | invisible Part, no sphere; head = where 4 trails converge + Star102 flare (Squash -1.2 -> 0) + streak sprites | Neon 50-stud mesh inside a 55-stud cracked Slate shell [inference]; Or=3 discs (Impact48/Circle66/Circle2) Locked to part |
| Stretch / Squash | Sideways Spec 37: Or=2, Squash 0-1, speed 55-167, Life 0.05-0.35, Spread 15 | Spec34/22 Or=2 Rot 90 rising sparks Acc +100; Fire25 Or=2 |
| Beams along velocity | 4 charge rays around muzzle (Width 2 -> 15); no beam in flight | 32 ribbons, Width 10 -> 50 / 30 -> 80, CurveSize1 -100, Segments 50, flaring away from head |
| Trail stack | 4 Trails, 2 attachments 2.8 / 6.2 studs apart, Lifetime 0.1-0.24, WidthScale 0 -> 0.1 -> 0.5+, solid core + soft + additive + textured | n/a (ribbons play the trail role) |
| Mesh use | Start/End scale-tween domes, Neon vortex | the head itself |
| Wind / secondary | Wind29 rings stamped along the path (LE0 + LE1 copies) | Fire24/25 Spd 50-300 Drag 10 |
| Impact | `EmitOnFinish`: 13-17 layers, flash ZO 2, Drag 6-15 | ImpactMeteor 9 layers: scorch 3 s, ring to 137 studs, crescent, specs Spd 30-500 |
One-line: motion reads from direction-locked layers (streaks Or=2, tapered multi-trail, flared ribbons, rising sparks) plus a non-spherical or sprite-less head and an eased pop at the end; a round camera-facing sprite never carries it [inference].

## 7. Emit counts and timings from attributes [data: `attributes/*.txt`, owner-verified]
| File | Emit counts / timings |
| --- | --- |
| CartoonE (12 PE, **104 particles total**) | Impact9 4, HitImpactD 1, Grey Smoke 7/6 10+10, Style Smoke 13 10, ImpactBD10 10, Star20 10 + 15, OffCentered Spec 85 15, Oval Fading 15, Impact450 flash **1**, circle 3. Smoke 6 and the two spec/oval layers carry baked `SMOOTHSEQUENCE_*` (smoothed curves stored as attributes). EmitDelay absent: all fire on one frame. |
| Goal_VFX (11 PE, **94**) | Lightning33 1, Spec22 **30**, Spec48 15, Flare28 1, '1' 1, Lightning20/23/26 5 each, Star12 15, LightningNew6 15, Circle2 1; EmitDelay 0 on all. |
| Meteor impact (9 PE, **191**) | WD 2, Fire11 30, Smoke8 **50**, Smoke48 30, Spec40 **50**, Crescent12 15, Fire38 3, Ground15 **1**, Impact48 10. Meteor body beams/emitters carry only `SMOOTHSEQUENCE_Transparency/Size` (no timing). |
| blue_pewpews | Impact: Hit 15, Specs1/2/3 15 each, Smoke 20; FrontEmit 25; Projectile-level smoke 25; rock Fire 25. Spawn burst of 25 + launch 25 per bolt x 10-15 bolts. |
| the_circle_thingie Emit | 1, 5, 5, 10 x4, 5, 5, 3, 3 = **67** across 11 layers (large ring layers 1-5, sparks 10). |
| Colours_everywhere | Per orb colour variant: bursts 30 + 30 + 15 + 2 (+15), **EmitDelay 0.05 s** on the big ones; x3 variants = about 270 per orb, **about 1,900 in the 0.7 s detonation chain** for 7 orbs. |
| ProjectilePractice launch2 | Everything keyed to **EmitDelay 1.0 s** (windup), `groundcharge` / `glowing ring` `EmitDuration 0.8` (Size_End 0, 8: implosion over 0.8 s), `ScreenEffect` EmitDelay 2.0, leaves `SpinDuration 1.5` (`SpinRotation (0,-180,0)`), swirl/lens flare use `Size_Curve` + `Size_End` 6-8 instead of counts. Wind18 ground ring 8; Smokey Crescent 3; Wind4 3; Whole swirl 4; Sideways Spec 37 variants 5/7/5/15 with `TimeScale_Duration 0.112`; Spec16 9; dots 7; Basic Blurry Spec 5; Grey Smoke 1 (Size_End 9). Mesh Models: `EffectDuration` 0.45-1.0 s, `MaxInitRot (360,0,0)`, `Mesh_Scale_Curve`, Decal `Transparency_Start` 0.5-0.9 -> `Transparency_End` 1. Beams: `EffectDuration` 1-2 s, `RayValue` children tween Transparency / TextureSpeed (end 1.0) / TextureLength (end 0.3) with `Easing_Curve` and `EmitDelay` 1 s. |
| Bezier flight | `Duration` **0.337 s** (Bezier) / **0.5 s** (Bezier2), `EmissionDirection Front`, `ArcSpace` False/True (launch2 InwardsBezier `Duration 0.1-0.3`, `DestroyDelay 1.0`, `EmitDuration 0.8`). Bullet trail emitters `EmitCount 1`, `EmitDuration` 0.337 / 0.451 (continuous for the whole flight), Wind29 `Size_End` 3-5 `Size_Envelope` 1-2, streak specs `Size_Start 1 -> Size_End 0`, Trails carry `WidthScale_Curve` / `Transparency_Curve` (so trail shapes are curve-authored, not hand keys). |
| EmitOnFinish (Bezier, 13 PE, **59**) | Wavy Water Circle 1 (Size_End 6), Lens Flare 1 (End 10), Diamond 8, Impact70 2, Outward Fog 3 (End 12, Env 3), Impact 1 (End 8), Blurred Spec 11 **10**, OffCentered Spec 70 **10**, Sideways Spec 5, Basic Blurry 3, Water Spiral 3, Moving vertical bezier **9**, Flare Twinkles 3; model `EffectDuration 0.675`; all `TimeScale_Duration 0.112`. |
| EmitOnFinish (Bezier2, 17 PE, ~**85**) | same recipe, bigger: Impact **7** (End 5), leaf 15, Sideways 5, Diamond 8, Wind28 3 / Wind45 2 (End 10), `TimeScale_Duration 0.187`, model `EffectDuration 1.123` (= 0.675 x 1.664). |
Takeaways: (1) an impact is about 60-190 particles in one frame, with 1-2 hero sprites (counts 1) and 5-50 for specs/smoke; (2) the big sprite always has count 1 and a `Size_End`/`Size_Envelope`, the small ones carry the count; (3) the PP kit **time-scales a whole variant** via `TimeScale_Duration` (0.112 vs 0.187 vs 0.045) and `EffectDuration`, so one authored impact serves a fast and a slow bolt (CT-26 confirmed); (4) windup is a delay (1.0 s), implosion is `EmitDuration 0.8` with `Size_End 0`; (5) Colours fires about 1,900 particles in 0.7 s and 7 tint swaps (CW-07, CW-10 confirmed in numbers).

## 8. Seen in motion (2026-10-16)
Source: `output/vfx/training-captures/` (~30 fps Studio screen grabs): `overview_cTier/Unknown/sTier.jpg` and `sheet.jpg` for fiya_beam, Colours, Meteor, ProjectilePractice. Meteor and ProjectilePractice were flown by our script, so only their look counts. I saw contact sheets, not full clips; frame timings are not read. CONFIRMED / WRONG refer to my claims above.
| Effect | What is visible |
| --- | --- |
| blue_pewpews | Small blue dots and faint wisps scattered over a dark floor; low contrast, no readable head or tail, impact is a few specks. |
| fiya_beam | Charge = orange fire ball over the player (about 2 frames of build), then a fire-stream to the target, wide near the muzzle, ragged tip, black cube rocks flying. Reads as a flame jet, better than the data suggested. No ground scorch or end flare. |
| Colours_everywhere | Small firework-like specks near the player, tiny against the screen. One frame floods the whole sky and floor in saturated blue (tint), the next returns. |
| circle_thingie | Small purple burst and ring on the ground; the pillar and aura are barely visible at side-camera distance. |
| CartoonE | Chunky red-orange cartoon cloud with dark-red puffs and bright core, big, one peak frame then gone. |
| Goal_VFX | A **"GOAL" text sprite** with orange lightning and white sparks, peak for one frame. |
| Hakari_Aura | Screen-filling green: flat shards and ribbons, ground ring, bright core; the character is hidden. |
| Portal_VFX | Black ink swirl around a white-blue core with thin orbit rings. Very readable. |
| Gabimaru_Aura | Pink-magenta glow on head and limbs, thin; not the orange fire I expected. |
| Meteor | Dark cracked rock with orange glowing cracks, thin pink-orange ring arcs around it, vertical orange diamond sparks; impact = flat orange ring + fire burst, then a dark scorch that lingers about 4 sheet frames. |
| ProjectilePractice | Bullet = one thin bright green streak, no head. Impact = swirl rings and a green spark cloud, over in about 3 sheet frames. |
| vs S tier | S frames are larger, higher contrast, with a white-hot flash (Elemental Guns follow fills the screen white) and a fire head trailing a long flame; C frames are small and dim on dark ground. |
**CW / claim verdicts**
- CW-01 flat LE0 glow: CONFIRMED (pewpews dots dull). CW-02 single hue: CONFIRMED (everything one blue). CW-04/05 no head or streak on pewpews: CONFIRMED.
- CW-06 "beam is a pipe": PARTLY WRONG. The stream has body and a ragged tip from the 350/s dust; the weak part is the missing end flare and scorch, not the pipe shape.
- CW-07 screen overuse: CONFIRMED (whole-screen blue tint frame in Colours). CW-08 crude rocks: CONFIRMED (flat black cubes).
- CW-10 overdraw: CONFIRMED for Hakari (clutter hides the character).
- CT-18 cracked-rock plus neon core: CONFIRMED (glowing cracks visible). CT-03 vertical diamond streaks (Or=2): CONFIRMED. CT-19 lingering scorch: CONFIRMED.
- CT-12 "ribbon cone flame skirt": NOT CONFIRMED. Only thin arcs near the head show at this scale; the 84-stud tail is not visible. Treat as unproven.
- Anatomy "no sphere head, bullet is streaks and trails": CONFIRMED for ProjectilePractice (single streak). The 60-190 particle impact: it does look like a short, wide burst. Meteor motion read comes from the lumpy glowing mesh plus streak sparks, not from a tail.
- My Gabimaru "orange fire aura" was WRONG in colour (reads magenta); my Goal description missed that it is a text banner.
**Revised Unknown tier guesses**: CartoonE A; Goal A (banner effect); Portal **A-** (up from B+); Hakari A- (strong but cluttered); Meteor A; ProjectilePractice **B+/A-** (thin bullet, short impact; flight path not judged); Gabimaru **B** (down; weak glow, 1,075 live). All still [inference].
