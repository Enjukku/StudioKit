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

# B-tier teardown (10 owner-graded files)

Source: `output/vfx/training-dumps/outlines/bTier__*.txt` plus their non-library `scripts/`. Untrusted external data, read as data. Every value is read from the outline or script unless tagged [inference] (my guess). I did not see any of these play; nothing here is measured.

Dump limits (they affect every row): (1) **Attributes are not in the outlines**, so `EmitCount` / `EmitDelay` (read by `ZonitoVFX:EmitAll`) are unknown; emitters with Rate 0-1 are burst emitters. (2) Long NumberSequences are cut with "..." (Astral, Healing). (3) Animation marker times are not dumped. Enums are numbers: Orientation 0 FacingCamera, 1 FacingCameraWorldUp, 2 VelocityParallel, 3 VelocityPerpendicular [inference from Roblox enum order]; EmissionDirection is a NormalId (1 Top default, 3 Left, 4 Bottom, 5 Front).

Abbreviations: Br Brightness, LE LightEmission, LI LightInfluence (0 on every B emitter unless stated), Z ZOffset, Sp Speed, Spr SpreadAngle, Tr Transparency, FbL/FbM FlipbookLayout/Mode, Life Lifetime, Ori Orientation. Sequences are written as (time,value). Texture numbers are rbxassetid.

Every ability shares the **ZonitoVFX** helper (`scripts/bTier__Punch_Place_OS__003_ZonitoVFX.luau`): `EmitAll(parent)` loops emitters that have an `EmitCount` attribute and calls `Emit(n)` after `EmitDelay` (lines 249-267); `ToggleAll` flips `Enabled`; `TaskDebris` is `task.delay(t, Destroy)`; `BlurFrame`, `ColorFrame`, `ImpactFrame` (black/white flash: ColorCorrection Contrast -100/+100, lines 119-168) and `CameraShake(name)` (CameraShaker presets, `CameraShakeInstance.new(magnitude, roughness, fadeIn, fadeOut)`).

## At a glance
| File | Emitters / Beam / Trail / Light | Moment | Driven by |
| --- | --- | --- | --- |
| explosion | 14 / 0 / 0 / 0 | one blast | attribute bursts (no script in file) |
| Astral_Redesign | 31 / 0 / 0 / 0 | sword-hit impact | Rate 0 on all, so bursts (no script) |
| bow_thngiemajig | 16 / 3 / 0 / 2 | idle glowing bow item | all Enabled, looping |
| orb_thingies | 27 / 0 / 0 / 3 | 3 pickup orbs (red, green, blue) | all Enabled, looping |
| HitEffectOS | 16 (8 x 2 colour variants) / 0 / 0 / 0 | melee hit spark | Rate 1 bursts (no script); about 2,350 of 2,397 lines are MoonAnimator/LunarSound save data |
| Healing_VFX | 10 / 0 / 0 / 0 | heal pulse + floating icon | script every 1.6 s |
| Emerald | 13 / 0 / 1 / 1 | 3-7 homing emerald bolts | ability script |
| Water_Barrage | 27 / 0 / 1 / 2 | 15 water bolts from sky portals | ability script |
| silly_water | 44 / 0 / 0 / 2 | staff slam + 23 falling water bolts | ability script |
| Punch_Place_OS | 82 / 0 / 0 / 0 | 7-hit lightning punch barrage | animation markers |

## explosion.rbxm (14 emitters in one Attachment "VFX"; no light, no script)
| Layer (emitter) | Job | Key values |
| --- | --- | --- |
| "4","3" tex 13366434456 | big soft cloud | white, Br 3, LE 0, size flat 6, Tr (0,1)(.26,.96)(.74,.95)(1,1) so only 4-5% opaque, Sp 70-80 / 40-50, Drag 5.9 / 4.2, Life .95-1.19, Rate 16.8 |
| "5" tex 16867371255 | smoke flipbook | FbL 2, FbM 1, same cloud params |
| "7","6" pink (255,85,127) / peach (255,170,127) | ember bits | Br 5, LE 0, Sp 140-160, Drag 12-15, Life .5-.7, size (0,0)(.285,1.37)(.445,.72)(.789,.99)(1,.47): a **pulsing, non-monotonic curve** |
| "2","1" tex 13580350953 | streak sparks | Ori 2, Rot 90, Sp 142.8, Drag 11.8, Life .30-.41, size 3.38 -> 0 linear, Tr 0 -> 0, Br 5; pink and peach copies of one texture |
| "11","12" tex 18809379295 / 18809407115 | dark-core blobs | **LE -2**, Br 5 / 4, Sp 140-160, Spr 60, Life .9-1.3, size (0,0)(.285,5.9)(.445,3.1)(.789,4.3)(1,2.0) |
| "10","9","8" tex 13463792226 / 16892242416 / 16892332741 | flash / shock discs | Sp 0, Life .16, Rate 74, size 0 -> 11.8 / 13.1 (t .3) -> 17.8 / 19.8 (.74) -> 20.7 / 23 (1), Tr 0,0,1 at .66; peach / pink tints |
| "wind" x2 tex 13272047385 / 13280169445 | ground swirl | **LI 1**, Ori 3, Tr .95 plateau, size (0,10.5)(.32,18.9)(1,30.5) and flat 22 with RotSpeed 171 |
Choreography: none in the file. Pairs share one texture in two tints (pink/peach): cheap colour variation. The negative-LE blobs (11/12) are the only dark layer.
**Holding it back:** no light, no beam/trail; the two big clouds sit at Tr .95 so the white mass carries no weight; discs 8-10 all start at t=0 with the same Life .16 (no staggered onsets); no camera or screen script; one warm family only, no cold counter-colour and no white-hot core flare.

## Astral_Redesign.rbxm (31 emitters, 3 Attachments, Rate 0 on all)
| Group | Layers | Key values |
| --- | --- | --- |
| Attachment "1" ground impact | circleFlipbook2 x2 (126034245450101), "Thin blurred expanding" 15014002418, "Circular Smack" 18140248952 x2, Impact13 16892226410 | Ori 3 (flat disc) on 3 of 6; **Br 6/8 hot layer with a Br 0.15 copy** at Z -0.01; Life .5 / .7 / .4 / .29 / .06-.08; FbL 2, FbM 1; **size curves are hand-baked easing, 15+ keypoints** (8.18, 8.94, 9.58, 10.10, 10.52, 10.86 at t 0, .067, .133 ...: fast then slow growth) |
| Attachment "2" flares | Flare120New (91924863141962) Life .06, LE .2, Squash -3, Z 8; Basic Blurry Spec (77024587778878) LE 1, Life .04, size 25.9, Z 8; Impact587, Unfinished fade, Ground22, Impact145 / 21 / 208 | Life .5-1.35, Br .2-1.5, Z -0.03 to -0.11 (ordered ground-ring stack) |
| Attachment "2" particles | "Wiggly Ball" x9 (14004161351); "Smoke33" x4 (16867492882) | Wiggly: FbFps 10-25, StartRandom, Sp 5-100, Drag 6.5-8, Accel +2/+6, Life .2-1.6, size .5 -> 0, Squash (1,.14) -> (1.58,.44) on Ori 2. Smoke: Accel -5, Sp 5-55, size 5 -> 7.25, Z -1 to -2.1 |
| Attachment "Impact" | Impact40 (16892332741) Life .07 size 27.3 shrinking, Z 5; Impact471 Life .10 Ori 3; Impact30 Life .16 | three discs of different Life (.07 / .10 / .16) = a **flash stagger** |
Colour: yellow (248,255,116) -> blue (96,120,255) -> deep blue (56,42,255) ColorSequence on nearly every layer (keys at .14 or .25 / .42). Z-order is an explicit list: flashes high Z (5-8), dust negative Z.
**Closest to S/A craft in the B set.** Holding it back [inference]: no light, beam or trail in the file; the deep-blue tail (56,42,255) is dark; no hit-stop or shake script; Wiggly Ball is one texture for 9 spark layers, so the sparks never differ from each other.

## bow_thngiemajig.rbxm (looping item; MeshPart bow id 8217608455, Material 1088)
| Layer | Key values |
| --- | --- |
| Attachment "Middle", 7 emitters, Sp 0, Life 2, Rate 1-2 (Rainbow5 15) | Star12 (17062452122) Br 6 Z 1 plus a **Br 0.1 twin, Squash -2, Z .5**; Spec19 (16879789169) LE 1 size 13 Z -2; Flare25New (96748443160245) LE 1 RotSpeed +-15 Z 2; Flare45New (125763891971628) size 0 -> 3.6 Z 1.9; Flares12 (86170160520422) Br .05 size 0 -> 6 Z -5; Rainbow5 (126685678214657) Br .01 LE 1 size 0 -> 8.25 Z -6 |
| 3 sparkle parts One / Two / Three | each a Star12 pair: Br 15 (Tr 0 -> 0) plus Br .5 twin with Tr .8, Z -.5; Rate 60, Life .5-1; size zig-zag (0,0)(.06,.25)(.16,0)(.25,.25)(.35,0)(.42,.37) = twinkle |
| Body | fine-smoke1 (128124707976588) Br 0 and .05 twin; Smoke27 (16867460128) Br 15 **LE -1** FbL 3, Rate 60, Life 1-2, Z -1 to -2.1 |
| Beams x3 | Beam94 x2 tex 76397637545058, TextureMode 2, Length 15 Speed 1 Br 15 and Length 5 Speed .6 Br .1; Beam127 tex 135482100082072 Length 50 Speed .1 Br .15. Width 3 -> 2, Segments 10, FaceCamera true, CurveSize 0, Tr (0,1)(.2,0)(.7,0)(1,1) |
| PointLights | Br 15 Range 5 plus Br .5 Range 12, Shadows false |
Colour: one hue (84,84,255). No script. **Pattern: every bright layer has a twin at Br 0.01-0.5.**
**Holding it back:** one blue hue, no warm accent; everything is Sp 0, so only size and rotation pulse; beams are straight (CurveSize 0).

## orb_thingies.rbxm (3 pickup orbs: Damage red (255,74,74), Health green (96,255,60), "Stasr" blue (69,109,255))
Identical 7-layer stack per orb; only colour and the centre icon change (Damage 80230271052569, Health 86308983539026, Stasr 123830728483153). Life 2.2, Rate 1, Tr (0,1)(.2,0)(.8,0)(1,1) (fade in, hold, fade out); sizes flat.
| Layer (tex) | Br | Z | Job |
| --- | --- | --- | --- |
| Circle78 (99634001621539) | **0.01** | -0.5 | dark disc underlay, size 2 |
| Circle79 (94366814100186) | 3.65 | .05 | glow ring |
| Chrome Plus icon | 6 | .1 | symbol, size 1.1 |
| Spec19 (16879789169) | 1.5 | -1 | big soft halo, size 13 |
| Flare213New (108523870700360) | 5 | -1.5 | star flare, size 3 |
| Foggy Circle Overlay (81276431283103) | .75 | 0 | flipbook fog, Rate 2.1, size 2.6 -> 3.18 |
| Flare240New (15773612675) | 1 | -2 | rotating flare RotSpeed 90, Tr .3 plateau, size 4 |
| Fire55 (17062535921) | 15 | -3 | flame flipbook, Ori 1, Locked, Rate 4, size 4 |
| side Chrome Plus sparkles | 15 | .15 | Rate 10, Sp .5-3, size 0 -> .25 -> 0, Life .5-.85 |
PointLight Br 3, Range 9, Shadows false.
**Holding it back:** "icon in a glow", all quiet; sizes flat; one hue per orb with no accent; the same stack x3 (reuse is memory-friendly, but gives no variety).

## HitEffectOS.rbxl (two identical Parts "HitEffect", Transparency .7, 8 emitters each; the rest is save data)
| Layer (tex) | Key values |
| --- | --- |
| Impact (12363774696 "flare_15", legacy URL) | LE 1, Br 2, Life .1, size 10 -> 0 linear, Z 2 |
| Impact19 (16892242416) | Life .1, size (0,8.9)(.73,0), Squash .37 flat, Tr .8 constant, Z 1 |
| Star109 (13366353306) | Br 15, Life .25, size 7.3 -> 0 at t .73, Tr 0 -> 1 |
| Basic Blurry Spec (77024587778878) x2 | Br 15 LE 1, and a **Br 0 LE 0 twin**; Drag 8, Sp 25-50, Spr 360/-360, Life .25-.75, size .37 -> 0 |
| Spec33 (16879826553) x2 | same hot + dark twin, Ori 2 streak, size 1.06 -> 0 |
| Circular Smack (18140248952) | Br 5, LE 1, FbL 2, Life .3, size 5 -> 10, Z 2 |
Variant A ColorSequence flickers purple / yellow: (140,39,255), (221,226,128) at .09, (163,105,205) at .18, (255,244,88) at .31, (140,53,216) at .52 ... Variant B is per-layer solid blues (95-146,89-124,255). Longest layer 0.75 s. The save data is MoonAnimator2 (M1S Length 300, COMBO 2248, keyframes at 0, 5, 10, 13, 18, 23; units unstated, [inference] frames). No Lua, no shake, no light, no beam.
**Holding it back:** a flat list of one-shot layers with no windup or follow-through; no trail, no shake or hit-stop; every layer except the sparks ends by 0.3 s; Rate 1 on everything, so the sparks are a single particle each [inference: EmitCount attribute decides].

## Healing_VFX.rbxm (rigs "Emirt" and "Enablerd" plus floating icon part "GFX")
| Layer | Key values |
| --- | --- |
| Ring tex 16877946118 | (64,255,64), LE 1, Ori 3, Life .5-1, **size linear 0 -> 0.5 per 0.1** (cut off in dump), Tr 0 -> 1 linear |
| Specs 16878181512 / 16879834064 (Ori 1) / 12072054746 | Br 15 / 25 / 15, LE 0, Sp 1, Life .5-1.25, size 0 -> .31 -> 0, Z 2 |
| Halo 6430908053 | Br **0.2**, LE 1, size 3 flat, Tr (0,1)(.18,.87)(1,1), Z 5 |
| GFX | BillboardGui 6x5 studs, ImageLabel 17577224682, Y bob +1 stud (Tween 2 s, Sine InOut, repeat -1, reverse); no glow |
Script: `scripts/bTier__Healing_VFX__001_Script.luau:3-7` is `while task.wait(1.6) do EmitAll(script.Parent); EmitAll(script.Parent.Attachment) end`. Emirt = bursts every 1.6 s; Enablerd = same emitters at Rate 5-15 continuous.
**Holding it back:** linear ring growth, 5 layers, one pure hue (64,255,64), no cross flare, no dark underlay, no light; the 1.6 s metronome is the only timing; the icon is a flat billboard.

## Emerald.rbxl (3-7 floating bolts that home on the mouse; colour (85,255,127))
Part "beamEnd": Attachment (continuous), "Spawn" and "Explosion" (EmitAll'd).
| Group | Layers |
| --- | --- |
| Attachment (Enabled) | 16879800718 Br 5 Z 1 Rate 5 Life .5; "Arrow2" 17529931231 Br 15 Ori 2 Z 2; sparks 17062454564 / 16878181512 Rate 30 Life 1-2 Sp 5 EmissionDir Bottom Spr +-45, size zig-zag (0,.2,0,.2...) twinkle; glow 6430908053 Rate 35 LE 1 size 2.4 -> 0, Tr .9 |
| "Spawn" (burst) | 17062454564 size 7.5 -> 0, RotSpeed 350, Life .5, Br 6, Z 3; ring 16877946118 size 0 -> 7.2, LE 1 |
| "Explosion" (burst) | 5 emitters Br 15 (one Br 5), Drag 1-5, Sp 1-100, Spr 360, Life .1-2.1, Accel +5; cloud 6430908053 size 5 LE 1 Tr .86; flash 16892332741 Life .1 size 3 -> 0 |
| Trail | tex 16892386886, TextureMode 2, TextureLength 4, Life .4, Br 4, **WidthScale 1 -> 0**, FaceCamera true, Tr 0 -> 0 |
| PointLight | Br 2, Range 12, Shadows false |
Choreography (`scripts/bTier__Emerald__000_Emerald.luau`): `Amount = RNG:NextInteger(3, 7)` (line 44); spawn offset `RNG:NextNumber(-15,15), (4,10), (-15,15)` (51); `ZonitoVFX:EmitAll(beamTracker.Spawn)` (54); Speed 40-80 studs/s (56); `Lifetime = 5` (26); per Heartbeat a raycast plus `GetPartsInPart` (70-71); re-aim `CFrame.lookAt(pos, mouse)` (87). On hit: `CameraShake("Emerald")` (75; preset 1, 8, .01, .25), `EmitAll(Explosion)`, light tween to 0 over 1 s, `ToggleAll(Attachment,false)`, `TaskDebris(beamTracker, 4)`. Key E, 1 s client cooldown (`bTier__Emerald__054_VFX.luau:14`). An unused `--ZonitoVFX:blurFrame(.01, 5)` is commented out at line 76.
**Holding it back:** all bolts identical; explosion has no ground ring or dust; trail is a single layer with no second core; one shake per bolt (up to 7 overlapping) [inference]; no dark underlay.

## Water_Barrage_OPENSOURCE.rbxl (15 bolts; Portal + Projectile templates, colour (112,150,255))
| Template | Layers |
| --- | --- |
| Portal (Attachment, Enabled, Ori 3, EmissionDir Front) | Water31 16866090677 Br 3 **LE -0.6**, and a Br .6 **LE -1** twin; Water30 16866073152 size 1.47 -> 6.76; Circle55; Flare27 86050781839978 (size 10.1 shrinking baked); Flare28 122881636456623 Squash -1.8; Rainbow3 85664013418740 (193,226,255); Water7 / Water50 flipbooks; Rate 6-80, Life .8-1.5; PointLight Br .5 Range 16 |
| Portal "Spawn" burst | Water28 Tr (0,0)(.14,0)(1,1) Z 4; Water41 Z 3.9; Impact22 Life .1-.15 size 5 -> 0 Z 5; Spec1 |
| Projectile "Middle" | Water28 x2 (Br 2.5 and 1.5), Rate 60, Life .6-.9; Water31 LE 1 spec; Water6 Z -1 Br 3 Life 1-1.3 |
| Projectile "Impact" burst | Impact8, Impact62 71570654111653 size 5.9 -> 8.3, Water31 / Water6 / Spec1 / Spec40 Sp 22-29 Drag 5, Water3 expanding disc Ori 3 size 2 -> grows ~0.8 per 0.1, Water19 |
| Trail | tex 112629787601025, TextureMode 0, TextureLength 1, Life .5, WidthScale .6 flat, Br 1.7 |
| PointLight | Br 3, Range 8 (tweens to Br 0, Range 35 over .5 s on hit) |
Choreography (`scripts/bTier__Water_Barrage_OPENSOURCE__000_Water.luau`): `Projectile_Count = 15`, `Projectile_Wait = .1` (spacing, line 112), `Projectile_Speed = 55`, `Projectile_Lifetime = 2`; spawn offset (+-20, 10-15, 3-5); `task.delay(.1)` then `CameraShake("PortalEmit")` (0.1, 0.2, 0, .4) and `EmitAll(Portal.Spawn)`; Heartbeat raycast march; on hit `ToggleAll`, `EmitAll(Projectile.Impact)`, light `Brightness 0, Range 35` over .5 s (85-88), `CameraShake("ProjectileImpact")` (.7, 5, 0, .35), `TaskDebris(2)`; portal emitters off after 0.1 s, light tween 1.5 s, Destroy 2 s later (101-108).
**Holding it back:** 15 shakes at the same strength with no variation; one blue hue; trail is a constant-width ribbon (0.6, no taper); portal is flat discs; no ground splash ring or decal on hit.

## silly_water.rbxl (staff slam; 44 emitters; blue (30-53,79-107,255))
| Template | Layers |
| --- | --- |
| Floor (continuous) | wave 16866196212 Ori 3 size 0 -> ~30 in ~0.1 steps (baked ease), Br 10, Life 1.5-2, Rate 3; same texture flat size 30, Br .15, LE 1, Rate 15; PointLight 0 -> Br 15 Range 32 (tween .9 s); fountains Shape 2, Accel +27..35, Rate 55-60, Drag 5, tex 16866090677 / 16878181512 / 16867514432 / 16867490141 |
| Projectile (falling) | 5 stream emitters on 5 different textures (16866196212 / 16866194949 / 16866197366 / 16866198739 / 16866201822), Br 5, Rate 20, size .27 -> 0, Sp 5.5; 16865839709 stream Br 2 Rate 35. "Hit" burst: 8 layers (Br 5-15, LE 0/1, Sp 5-15, Spr 0-380, Life .05-2.5; flash 16892318504 Life .05-.1 size 4.8 -> 0; wave 16865822115 Ori 3 size 0 -> 10) |
| Staff impact (burst) | about 20 emitters: Accel +50/+100, Sp 50-75, Drag 4-6, Life .1-2.5, flipbooks 16865991773 FbL 3, rings 18675294168 / 18324838775 / 18721568780 with RotSpeed 250-350, sizes up to 15.4 x 4.6 |
| Held staff | MeshPart 8599805892, 3 emitters Rate 50-55, Life .5 |
| Highlight | FillColor (0,.33,1), Fill 1, Outline 1 (animated by script), DepthMode 1 |
Choreography (`scripts/bTier__silly_water__000_Water.luau`): FOV 90 in 0.7 s Quart (15); `humanoidRoot.Anchored = true` for the whole cast (16); `BlurFrame(0.01, 0.3, 8)` (28); Highlight to Fill .75 / Outline .9 in .3 s (79). On marker "Impact": Highlight pulse .1 s, `ColorFrame(0.01, 1, (.43,.58,1))` (36), staff burst at `humanoidRoot.CFrame * CFrame.new(0,-2.6,-2.5)` plus `EmitAll(ImpactVFX, true)` (37-40), FOV 70 in .2 s (42), `BlurFrame(0.01, 0.2, 18)` (43), `CameraShake("Staff")` (44; 3, 20, .01, .7), floor light to Br 15 / Range 32 over .9 s (50). Then **23 bolts every 0.2 s** (52, 75) from y+30, each tweened down 29.5 studs in 0.5 s (66); `task.delay(.45)` fires `CameraShake("Impact")` (.25, 5, .01, .4), the hit sound and `EmitAll(Hit)`; Destroy after 3 s. Cleanup: staff light off at animation end, Floor destroyed about 7.5 s later (82-92). The NPC copy `bTier__silly_water__001_WaterCharacter.luau` comments out FOV, blur, colour and every shake (diff lines 20-106): the same cast with the screen channels removed.
**Holding it back:** the best script choreography in B, but bolts fall on a linear tween at a metronome 0.2 s with 23 identical shakes; 44 emitters in one hue; hit has no ground scorch or decal; no trail on the bolts (stream emitters only).

## Punch_Place_OS.rbxl (lightning punch barrage; 82 emitters = 7 Attachments x 11-12 layers)
Template Part "LightningPart", Attachments "1","3","4","5","6","7","2" named after animation markers. Same stack per hit, blue (120-172,136-191,255).
| Layer (tex) | Key values |
| --- | --- |
| "5Dark" 12602224662 | LE 1, Ori 3, Life .3, size 1.77 -> 3.5, Tr 0 -> 1 |
| "D33ark" 16880037488 | Br 15, Life .4, size 4.6 -> 9.2, Tr .78 -> 1 |
| "Dark" 15953595361 | Br 10, Life .6, size .75 -> 3.4 |
| "Ele1ctric 2" 17005876540 | Br 5, Life .2, size 2.5 -> 5.1, then zig-zag .5 / 4.5 / .35 / 4.3 (jitter), Spr 20 |
| "Li12ghtning33" 17005853287 | **Br 50**, FbFps 30-60, Life .2-.3, size 0 -> 1.56 -> 3.6, Spr 20, Z -1 |
| "Fire1" / "Fire2" 109059450186841 / 18868381955 | Br 10, Ori 2, Locked, ShapePartial 1.25, ShapeStyle 1, FbFps 30, Sp 10, Spr 35 / 45, size 4 -> 1, Life .4-.6, colours (36,58,120) / (78,96,255) |
| "5" 12018086505 | ColorSequence white -> **black**, LI .95, FbFps 4, RotSpeed -300..-100, Sp -2..0, Tr .8 -> 1 |
| "BASTARDDDD" 10439119562 | Br 50, LE .5, Ori 2, Sp 1-25, Spr 70, Life .05-.4, **Squash 1.5 held then -3 at the end**, size 0 -> .5 -> 0 |
| "crack" x2 91843330177990 / 140632400481241 | **LE -1**, Br 10, Life .2, Tr (0,1)(.1,.02)(.7,.15)(1,1), size 1 -> 3.4 at t .08 -> 5 -> 10 |
| "wind" 10316078099 (Attachments 3, 4 only) | white, LI 0, Ori 3, RotSpeed 360, size 0 -> ~4.9 x 3.x |
| Attachment "7" extra "mainimpact" 14674577220 | white Br 5, Life **.04**, **size 156 studs** shrinking, Spr 360, Tr .96 -> 1; bolts there are x1.8 bigger |
Choreography (`scripts/bTier__Punch_Place_OS__000_LightningPunch.luau`): clone at `humanoidRoot.CFrame * CFrame.new(0,0,-3)` (33); play "Fist Barrage" (47 marker values); on each "Punch" marker `ZonitoVFX:EmitAll(VFX[Parameter])` + `CameraShake(`Punch{Parameter}`)` (44-45). Shake: hits 1-6 `new(.4, 9, .01, .4)`, **hit 7 `new(1, 11, .01, .7)`** (`bTier__Punch_Place_OS__010_CameraShakePresets.luau:30-77`). Marker "7": FOV 70 in .05 s + `BlurFrame(0.01, 1, 16)` (49-50); marker "6": FOV 90 in .2 s Quart (54). `Punch.Ended:Once` waits 1 s then Destroy (62-68). Key F, no cooldown (`bTier__Punch_Place_OS__059_VFX.luau`).
**Closest to S/A craft in B** (a dark smudge layer, negative-LE cracks, Br 50 cores, flipbook lightning at 30-60 fps). Holding it back: the 7 hits are the same stack and the same blue, with only hit 7 scaled; shake is identical on hits 1-6; the big finisher frame is a faint white (Tr .96) lasting 0.04 s; no light in the file despite Br 50 layers; no beam or trail; the Quasiduck procedural Lightning module is shipped but never called by the ability.

## Shared and cross-file notes
Player helper scripts are boilerplate, not VFX: `Gloss` sets all character parts to Glass (`bTier__Emerald__050_Gloss.luau:4-8`), `Leaning` (lean while walking), `cam` (follow head), BridgeNet2 networking (library, skipped). The Crater module is present but no B ability calls it (`CreateCrater` appears only in the module). Shake presets in B: Emerald (1, 8, .01, .25), PortalEmit (.1, .2, 0, .4), ProjectileImpact (.7, 5, 0, .35), Staff (3, 20, .01, .7), Impact (.25, 5, .01, .4), Punch1-6 (.4, 9, .01, .4), Punch7 (1, 11, .01, .7), DarkLightningStrike (1.3, 25, .01, .4). PositionInfluence is 0 and RotationInfluence (1,1,1) on all: rotation-only shake.

## Technique catalog (B tier)
| ID | Technique | Where | Concrete value |
| --- | --- | --- | --- |
| BT-01 | **Hot + dark twin**: the same texture twice, one Br 10-15 LE 1, one Br 0-0.5 LE 0 (reads as a dark rim or underlay) | HitEffectOS, bow, orb, Astral | Br 0.01-0.5 twin at Z -0.5..-0.01 |
| BT-02 | **Per-layer Z-stack**: flash and icon high (2-8), halo and dust negative (-0.5..-6) | orb, bow, Astral, Water | 6-9 Z levels per effect |
| BT-03 | Brightness above 1 as the glow dial (3 to 50), LE 0 or 1 chosen per layer | all | Br 15 specs, Br 50 lightning core |
| BT-04 | **Negative LightEmission** for dark cores, cracks, smoke | explosion (-2), Punch crack (-1), bow smoke (-1), Water portal (-0.6, -1) | LE -0.6..-2 with Br 5-10 |
| BT-05 | Hand-baked easing: 15-keypoint decelerating Size curves | Astral, silly_water Floor | +0.76, +0.63, +0.52 per 0.067 |
| BT-06 | Non-monotonic size curve (pop, dip, rebound) | explosion embers (1.37, .72, .99, .47); Punch Ele2 zig-zag | 4-5 keypoints, or 8+ for flicker |
| BT-07 | Squash for stretch streaks, sign flip at the end | Punch (1.5 -> -3), Astral (1 -> 1.58), bow (-2) | Ori 2 plus Squash |
| BT-08 | Flash stagger: 3 discs of different Life for one punch | Astral Impact (.07 / .10 / .16), Punch mainimpact (.04) | Life .04-.16 |
| BT-09 | Hot-to-cold ColorSequence over life (yellow -> blue) | Astral; HitEffect strobe | keys at .14 / .25 / .42 |
| BT-10 | Attribute-driven bursts: `EmitCount` + `EmitDelay` per emitter, one `EmitAll(folder)`, staged by Attachment (Spawn, Impact, Explosion, Hit) | all abilities | `task.delay(EmitDelay)` |
| BT-11 | Light tweened with the moment: ramp 0 -> 15 with Range 32 over .9 s, or flash then Range 35 / Br 0 | silly_water, Water, Emerald | PointLight Shadows false |
| BT-12 | Layered screen channels at the hit: FOV 90 then snap 70, Blur (in .01, out .2-1, size 8-18), ColorCorrection tint 1 s, Highlight pulse | silly_water, Punch | see choreography |
| BT-13 | Per-hit shake with a magnitude ramp: .4 for hits 1-6, 1.0 on the finisher, fadeOut .4 -> .7 | Punch | `CameraShakeInstance.new` |
| BT-14 | Texture reuse across parts and colours (spec 16878181512 in 6 files; orbs x3) | many | memory friendly |
| BT-15 | Textured Beams: 3 layers at 3 scroll speeds, TextureMode 2 | bow | Length 5-50, Speed .1-1 |
| BT-16 | Trail with WidthScale 1 -> 0 and TextureMode 2 | Emerald | Life .4 |
| BT-17 | Flipbooks for flame, smoke, lightning (FbL 2 / 3, FbFps 10-60) | Astral, Punch, orb | lightning 30-60 fps |
| BT-18 | Twinkle through a zig-zag size sequence at Rate 30-60 | bow, Emerald | 8+ keypoints |
| BT-19 | Projectile salvo with a random spawn box | Water (15 at .1 s), silly_water (23 at .2 s), Emerald (3-7) | spawn box +-13..20 studs |
| BT-20 | One cast, two builds: the NPC copy strips camera, blur and colour channels | silly_water WaterCharacter | commented-out lines |
| BT-21 | Animation-marker-driven VFX (marker -> EmitAll + shake) | Punch, silly_water | `GetMarkerReachedSignal` |

## Weaknesses seen (B tier)
| ID | Weakness | Evidence | Fix direction [inference] |
| --- | --- | --- | --- |
| BW-01 | **One hue per effect**; no white-hot core or counter-colour | bow, orb, Healing, Emerald, Water, silly_water, Punch | add a second hue on core and tail |
| BW-02 | **Uniform repetition**: 7 punches, 15 / 23 bolts, 3-7 emeralds share stack, shake and timing | Punch, Water, silly_water, Emerald | vary size, Life, hue; ramp shake |
| BW-03 | **Linear or flat curves**: Healing ring linear, explosion clouds flat 6, orb flat, projectile tween linear | Healing, explosion, orb, silly_water | 3-5 eased keypoints |
| BW-04 | **No light** in 5 of 10 files (explosion, Astral, Healing, HitEffect, Punch); **no Beam** in 9 of 10; no Trail in 8 of 10; the 2 trails are plain | stats.json + outlines | PointLight flash, tapered textured trail |
| BW-05 | **Weak punch frame**: huge but faint frame (Punch 156 studs at Tr .96, 0.04 s) or every layer starting at t=0 | Punch, explosion | stagger onsets, raise the core |
| BW-06 | Cloud / smoke layers nearly transparent (Tr .95) so no mass | explosion | solid mid layer with dark underlay |
| BW-07 | Shake stacks (7-23 hits, one preset each) with no merge | Water, silly_water, Emerald | one preset per salvo |
| BW-08 | Emitter count without hierarchy: silly_water 44, Punch 82 (7 copies of one stack) while HitEffectOS (16) holds the sharpest idea | silly_water, Punch | cut copies, keep distinct layers |
| BW-09 | No lasting ground contact (no scorch / ring decal; Crater module shipped, never used) | Water, Emerald, silly_water | flat Ori 3 ring plus dark splat |

*Layer counts for comparison (stats.json, emitters): B 10-82, A 8-122, S 11-159. I did not read the S/A outlines in this task, so "B lacks X that S/A has" is [inference] from counts only.*

## Seen in motion (2026-10-16)
Source: `output/vfx/training-captures/` (`overview_bTier.jpg`, `overview_sTier.jpg`, `sheet.jpg` of Water_Barrage_E, Emerald_E, Astral_Redesign, orb_thingies, bow; 12-frame contact sheets at about 30 fps, so I saw stills in sequence, not smooth playback; I did not step through single frames). Not capturable: Punch, silly_water, HitEffectOS, Healing (no motion data for them); explosion shows only a few pink specks and a faint haze (capture weak, not a verdict on the effect). Camera is a far side view, so small detail is not judged.

| Effect | Visible per sheet |
| --- | --- |
| Astral_Redesign | Dead air for about 4 frames, then one **blown-out white starburst filling the frame** (the Br 6-8 flash discs), next frame a blue dome with a thin white ground ring, glinting sparks and dark blue smoke plumes that rise and thin out; gone within about 5 more frames. Reads as a punchy hit with a clear flash, body and fade. The ring is a hard thin line on a flat dome |
| Emerald_E | 4 bolts fly in as thin green streaks with a ring-and-star head; a green glow on the wall and floor appears as they land, then one bright white-green blob blooms and holds about 3 frames, fades to a faint green smear. Short, clear, one hue. The blob is soft with no ring or debris |
| Water_Barrage_E | One bright cyan head with a long thin multi-strand streak runs diagonally; it lands as a white splash and then a small flat swirl ring on the ground that fades. Only one bolt is clearly visible; the 15-bolt salvo does not read as a barrage at this camera. Overall dim against the dark floor |
| orb_thingies | A steady dark ring with a white star, blue glow halo, a rainbow-coloured flame at the top, a pink floor wash and small sparkles drifting around the star. Calm loop; the rainbow flame and floor tint are bright and clean. Looks like a UI badge, with little 3D motion |
| bow | A thin glowing blue bow outline with a white inner rim; a star-burst pulse flickers on and off across frames (flares expand, then relax); a soft purple floor wash and a faint blurred streak left of the bow. Reads as a pulsing idle glow; the beams are not visible as beams |

**Weaknesses on screen**
| ID | Verdict | Note |
| --- | --- | --- |
| BW-01 one hue | CONFIRMED | all five frames are single-family blue or green (orb has a rainbow top but that is a separate texture, not a hue plan); no warm accent anywhere |
| BW-02 uniform repetition | NOT CHECKED / partly seen | Emerald shows 4 near-identical streaks; Water shows one dominant bolt; the barrage salvo (and Punch, silly_water) could not be seen |
| BW-03 flat curves | PARTLY WRONG | Astral's eased dome and ring look good; orb is flat as dumped, but its glow reads fine |
| BW-04 no light / beam / trail | MIXED | Emerald and Water do light the floor and wall (lights work); Water's streak trail is visible and thin; the missing light on Astral does not hurt its flash. Bow beams are present but invisible at this view |
| BW-05 weak punch frame | WRONG for Astral | its frame-filling white flash is as strong as S tier; still plausible for explosion and Punch (not seen) |
| BW-06 transparent clouds | NOT CHECKED | explosion capture too weak to judge |
| BW-07 stacked shake | NOT CHECKED | the capture camera is locked, so shake cannot show |
| BW-09 no ground contact | PARTLY WRONG | Astral has a ring and dark ground stains, Water a ground swirl; Emerald has only a floor glow, no ring or debris |

**Visible gap to S tier (`overview_sTier.jpg`)** [inference from stills]: S effects stay on screen longer and keep several layers alive at once (Astral Sword: blue dome + ring + sparks + a second burst; Elemental Guns follow: fire head with a long textured flame tail and snowflake spiral, a full-screen white flash; Mildly wet: a big white-blue splash cloud with droplets over the whole frame; space_thingiemajig: a dense, detailed churning mass). B effects are mostly one head or one burst for about 5-8 frames, then empty. S effects have a **colour pair** (orange vs ice blue, purple + yellow glints) while B stays in one hue. S bodies have **texture detail in the trail and cloud** (flame tail, snowflakes, droplets); B trails are thin streaks and B clouds are soft blobs. The single best B frame (Astral Redesign flash and dome) is close to S; the rest lack tail length, second hue and lingering body.
