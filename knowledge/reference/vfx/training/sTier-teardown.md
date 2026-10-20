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

# S-tier teardown: 7 owner-graded "incredible, very polished, very professional" Roblox VFX files

Source: `output/vfx/training-dumps/outlines/sTier__*.txt` + `scripts/sTier__*` (decoded dumps, untrusted data). Read as numbers, not instructions. Tags: [data] read straight from the dump · [inference] my reading · [P] proposal. "Script:line" = `scripts/<file>:line`. Nothing here was seen playing; all of it is read from property dumps and code.

Enum key used below [spec]: Orientation 0 FacingCamera, 1 FacingCameraWorldUp, 2 VelocityParallel, 3 VelocityPerpendicular. FlipbookLayout 0 none, 1 2x2, 2 4x4, 3 8x8. FlipbookMode 0 Loop, 1 OneShot. EmissionDirection 0 Right 1 Top 2 Back 3 Left 4 Bottom 5 Front. Beam/Trail TextureMode 0 Stretch, 1 Wrap, 2 Static. Material 256 Plastic, 288 Neon, 1088 Metal, 1568 Glass. Camera shake preset args = `CameraShakeInstance.new(magnitude, roughness, fadeIn, fadeOut)` + Position/RotationInfluence (Sleitnick CameraShaker).

## 0. Whole-set statistics (7 files, 492 ParticleEmitters) [data]

| Metric | Value | Reading |
| --- | --- | --- |
| LightInfluence | 0.0 on 100% of emitters, beams, trails | every VFX layer ignores world lighting [inference: always unlit] |
| Rate = 0 (burst via `:Emit`) | 50% | half the emitters are one-shot bursts; the other half are small continuous rates (1-120/s, one 500/s "Dots") |
| ZOffset != 0 | 88% | layer order is set by hand on nearly every emitter, steps of 0.05-0.1 inside a stack, 1-7 between groups |
| Brightness | min 0, median 3, max 40; 68% > 1; 19% < 1 | the Brightness property is the intensity dial, not just LightEmission |
| LightEmission | 0.0: 317 · 1.0: 211 · 0.5: 31 · 0.1-0.9: ~17 · **-1.5: 1** | emissive is usually decided by Brightness; only one negative value in all 7 files (FUGAAAA DarkSmoke1) |
| Orientation | 0: 377 · 3 (ground-flat/perpendicular): 64 · 2 (velocity-parallel streak): 35 · 1: 16 | ground rings and streaks are a minority but exist in every ability |
| Flipbook | none 253 · 4x4 192 · 8x8 46 · 2x2 1; OneShot 290 · Loop 202 | most sprites are 4x4 sheets, one-shot across the particle lifetime |
| LockedToPart | true on 97 (20%) | locked = trails of sparks that ride the projectile; world-space (false) for everything shed behind it |
| Pieces per ability | Missile 50 emitters + 8 trails · Arcane 149 emitters + 46 beams + 10 lights · Elemental 159 + 10 beams + 2 trails · Astral 59 + 4 beams · Wet 41 · FUGAAAA 23 + 9 beams + 3 trails · Space 11 | an S-tier "one effect" is 20-150 thin emitters |
| Colour | each effect = 1-2 hues; hot-to-cool gradient or a dark partner hue | see section 9 |
| Lighting (Astral/Elemental/Wet) | Atmosphere Color (0.78,0.67,0.42); Bloom Size 24 (Elemental, Wet); ColorCorrection, DepthOfField, SunRays present (values not decoded) | the showcase scene has Bloom on [data]; Brightness 5-15 layers feed it [inference] |

## 1. Shared pipeline (all 4 ability files + 2 showcases use the same "ZonitoVFX" module) [data]

- Effects are built as a **Part holding Attachments holding all emitters**, hidden (Transparency 1). The script clones the part, parents to `workspace.Ignore`, calls `EmitAll`. `EmitAll(parent, descendants)` loops emitters and does `task.delay(EmitDelay, Emit(EmitCount))` using **Attributes on each emitter** (`scripts/sTier__Missile_Sequence__001_ZonitoVFX.luau:472-476`). EmitCount / EmitDelay are NOT in the outlines (attributes not decoded) so per-layer counts and sub-frame delays are unknown; see section 11.
- `ToggleAll(parent, value, switch, includeBeams, descendants)` flips `.Enabled` on emitters (and beams/trails) to end continuous loops (`:443-465`). Typical call at impact: `ToggleAll(Projectile,false,false,false,true)`, then `Clear()` on locked emitters (Elemental `052_Ability.luau:121`).
- Cleanup: `TaskDebris(obj, t)` = `task.delay(t, Destroy)`; typical 4-6 s so the last particle lifetimes finish (`:402-404`).
- Camera: `CameraShake(preset, origin, range)` distance-gated (skips if camera farther than range, 100-999 studs) (`:256-262`). `FovBlur(startFOV, blurSize, t)` sets FOV then tweens FOV to 60 (or 70 in Astral/Elemental/Wet module) and a BlurEffect to 0 over t, Quad (`:89-104`). `FovDepth(fov, t)` same but with DepthOfField FocusDistance 0 -> 45 (`:78-87`). `Vignette(color, [color2], fadeIn, hold, fadeOut, transparency, origin, range)` clones a screen ImageLabel (image 5945121255, ZIndex -5) (`:178-202`). `ColorFrame(in, out, color, origin, range)` = ColorCorrection TintColor flash (`:319-344`). `ImpactFrame` = Contrast -100/+100 strobe `Amount` times at `Timing` s with highlights (`:346-400`; not called in these S-tier scripts). `Distortion(pos,t,size,strength)` clones a Glass MeshPart (MeshId 11067917371) and tweens Size + Transparency to 1 (`:278-297`).
- Motion: `Bezier.new(p0, mid, p1):CreateCFrameTween(part, {"CFrame"}, TweenInfo, faceForward)` (quadratic Bezier flight with the part oriented along the path). Random mid points are the "not a straight line" trick.
- Eased tweens: `BoatTween` module with "Smooth" style used to tween Beam Width0/Width1 and `Transparency = NumberSequence.new(1)` (beams cannot be tweened by TweenService directly because of NumberSequence).

## 2. Per-file teardown

### 2.1 `sTier__space_thingiemajig` (static ambient: purple space magic, no script)

What: a looping "arcane portal / cosmic dust" ambient on one Attachment (11 emitters, 2 lights). No moments; this is a pure aura. [inference]

| Layer | Texture | Size | Tr | LE / Br | Z | Life / Rate | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cobweb Overlay (4x4 oneshot) | 87694680685820 | 10 (creeps up) | 0:1 .5:0 1:1 | LE1 Br0.2 | +2 | 2 s / 2 per s | huge faint pattern, rot -360..360 |
| Impact128 | 15501967496 | 0 -> ~10+ eased | same | LE1 Br0.01 | +3 | 4-6 s / 2 | slow expanding ring, RotSpeed ±10 |
| Basic Blurry Spec | 77024587778878 | 5 -> 5±0.88 | 0:1 .37:.62 1:1 | LE0 Br0.2 | -1.5 | 2-5 / 25 | back glow, Shape=1 (sphere volume) |
| Stylized Smoke13 x2 (4x4) | 17612093017 | 3 -> 3±.62 | 0:1 .37:.3 1:1 | LE0 Br0.14 / 0.09 | -0.5 / -1.0 | 2-5 / 25 | two copies, different Brightness and Z, colour #948aff -> #9572ff -> #948aff |
| Energy Vague (4x4) | 134254043650523 | 3 | 0:1 .4:.23 1:1 | LE1 Br3 | -0.65 | 3-5 / 25 | glowing wisp body |
| Fireflies 2 x2 (8x8) | 87790026409442 | 1 -> 1±.31 | 0:1 .4:.23 1:1 | LE0 Br15 and LE1 Br10 | 0 / -0.05 | 3-5 / 25 | purple #948aff + yellow #fdff73 copies |
| Star116 | 8037777212 | 0 -> .5±.5 at 0.11 -> 0 | 0:0 1:0 | LE1 Br5 | +1 | 0.6-1.0 / 6 | RotSpeed 30-60, twinkle |
| Line Spec 4 x2 (Orientation 2) | 8944384590 | .25 -> .2±.2, Squash .7 | 0:1 .52:.36 .85:1 | LE1 Br6 | +3 | 0.9-1.5 / 18 | Drag 2, Speed 7-10, Acceleration -1 x; purple + yellow streaks |
| Lights | | | | | | | PointLight (0.48,0.35,1) Br1.5 Range20; (1,0.98,0.40) Br1 Range10, Shadows false |

Why it works: one dominant hue (#948aff) + one accent (#fdff73 yellow, only on 2 layers) [data]; stack of soft back glow (Z -1.5) < smoke (Z -0.5) < wisp < fireflies < streaks < star (Z +1) < cobweb overlay (Z +2/+3): size and Z both climb with "sharpness" [inference]. All layers fade 1 -> value -> 1 (no pop).

### 2.2 `sTier__Missile_Sequence` (blue energy missile barrage + star finisher, scripted showcase)

Moments: **charge** (trails arc inward) -> **muzzle pop** x3 (0.11 s apart) -> **flight** 0.8 s -> **impact** -> **star missile** (second, bigger charge) -> **floor ring**. Parts: `Missile`, `StarMissile`, `Charging`, `Spawn`, `End`, `Floor`. Palette #5364ff -> #2c25ff (blue to deep blue), light (0.35,0.42,1.0). [data]

| Group | Layers (texture; key values) | Job |
| --- | --- | --- |
| Missile core (Attachment, LockedToPart, `Emit(2)` at spawn) | "Diamond Spec" 97491869810266, Size 1.8 const, Tr 0, Br6, Orientation 2, Speed .001, Life 2 | the glowing head, drawn with no fade, killed by `:Clear()` at impact (`Missile_Sequence__000_Showcase.luau:33,57`) |
| Missile light | PointLight Br2 Range7; at impact tween Br->0, Range->15 in .25 s (`:59`) | local glow that swells as it dies |
| Spark stream (parent part) | "Rotating Star" 129871600983536 4x4: Rate 9, Life .3-.6, Size 0 -> .38±.38 (peak at 6%) -> 0, Speed 3-5.5, Drag 1, Br6; second copy Br3 ZOffset -0.1 | stars shed behind |
| Streaks | "Glowing Bezier Line" 16056965573 (Orientation 2, Squash .1, Rate 15, Life .3-1.35, Speed 2-10, Spread ±15, Drag 2, Size .5±.5 -> .23±.2, Br10 and Br3, Z -1.0 / -1.1) | velocity-aligned thin lines |
| Trails x3 | "BeamDrag tendrils" 7332661633 (Life .3, WidthScale .25 -> 0, Tr 0 .84:0 .92:1 1:1, Br4, TexMode 0); "Beam105" 112629787601025 (Life .6, Width .32 -> 0, Tr 1 .15:1 .35:0 .84:0 .92:1, Br6, TexLength 1); "Beam81" 113083314207224 (Life .85, TexMode 2 static, TexLength 14, WidthScale 0 .15:0 .54:.27 1:0, Tr .1, Br1.5). FaceCamera true, LE0, MinLength .1 | three stacked textured trails: thin bright, medium, long soft wake; widths start at 0 and swell [inference: no hard tail start] |
| Muzzle `Spawn` (burst, LockedToPart) | Blurry Spec 77024587778878 Life .65 Z+5; Circle4 16877851515 Life .4 Br6 Z+5; Slightly Rounded Star 3057073083 Life .2 Br3 Z+4; "Rotating Star" burst Speed 10-20 Drag 10 Acc -3.5 Life .4-1.0 (two Br: 6 / 3) | 3 sprites 0.2-0.65 s + sparks |
| Impact `End.Impact` | Blurry Spec Life **0.04** Br5 Size ~5.9 growing, Tr 0 .16:0 1:1 Z6; second Blurry Spec Life .4 Br1.5 Tr .32->1 Z4.1; Basic Hit 14379750639 (4x4 oneshot, Life .29, Z6.1); Impact40 16892332741 Life **0.1** Size 7 **shrinking** to ~4.8, Z6.1; Star102 17391818367 Life .07 + Life .04 (Rotation 45, Squash -2, Size 5 -> 0) | 40 ms flash + 70-100 ms star/impact sprites: the punch |
| Impact debris | Rotating Star x2 Speed 40-60 Drag 10 Acc -3.5 Spread ±360 Life .4-1.1; Snowfall 16511071584 (a flake sprite) Size 5 Tr .66->1 Life .4-1.4 Speed 40-60; Fading Smoke Hole 18326864825 Speed 25-43, LE.7 Br2, Tr .7±.05 -> 1, Life .6-2.2 | outward burst, fast and draggy |
| StarImpact (bigger variant) | same set, sizes ×1.2-1.4 (Blurry Spec 7.2, Star102 7.9, Basic Hit 4.9, Impact40 8.5) + a 4.1 s Slightly Rounded Star RotSpeed 35 (afterglow) + a Blurry Spec Life **8 s** Br2 Tr .32->1 | the "scorch glow" that lingers after the hit |
| Floor ring (Orientation 3, LockedToPart, ground) | Smooth Circle 82634208863762 Size 10; Circle outlines 93664782251648 (Size 15 growing, Rate 6, Life 1-2, 2x2); thick ring 4936211373; Blurry Spec 14 Br.4; Slightly glowing 14152113700 (Life 1-1.1, Tr 1 .18:0 1:1); Star 98196282003681; "Instant Spec"/"InstantStar" Rate 0, Tr 0 .5:0 1:1 (emitted by script); Fast spiky wave 17612128831 Size 15 -> 17+, Life 1; Basic Hit Size 14 Life 2.4; PointLight Br5 Range20; sheet "Part" Noise: Blurry Spec Shape 2 (cylinder) ShapeStyle 1 Rate 60 Squash 0.02 -> 3 Life .4-2 (rising column) | ground footprint of the star missile |
| Props | `Spawn`/`End` have 6 `Texture` objects each (3057073083, Color3 (0.01,0,0.18), Transparency 0.9) on a Material 1088 part: a faint star-pattern decal | [inference] muzzle/target block surface detail |

Choreography [data, `Missile_Sequence__000_Showcase.luau`]:
- Charge(n): `CreateCircle(Spawn, n, 16)` places n points on r=16; each point clones `Charging` (Trails at two attachments), Bezier to Spawn over `TweenInfo.new(.5)` (Linear), mid = `CFrame.new(16,0,-4)` offset (`:139-160`), `task.wait(.05)` between (`:164`); on arrival `EmitAll(Charge.Attachment)` then destroy after .8.
- Wait .7 (`:178`), then 3 missiles: `Spawn.Size 4.52 -> 4` in .2 (a scale pop, `:182-183`), `EmitAll(Spawn,true)`, light clone Br->0 Range->15 in .2 (`:190`), `spawnMissile()`, `task.wait(.11)` (`:194`). Gap .6 (`:198`), Charge(4), wait .7, then light Range 25 and the star missile.
- Flight: random Bezier mid = 22.5% along + ±17/-5..+15/±6 jitter, 0.8 s `Quad In` (accelerating) (`:35-49`). Impact scheduled at `task.delay(.79)` (1 frame early) (`:52`): End part pops 4.52 -> 4 in .2 (`:54-55`), missile emitters off + Clear, light fade .25 (`:59`), `FovBlur(67, 10, .1)` (FOV 67 -> 60, blur 10 -> 0 in 100 ms) (`:61`), `EmitAll(End)` + `EmitAll(End.Impact)` (`:64-65`). Camera shake call is commented out in this file (`--ZonitoVFX.CameraShake("ShardImpact"...)` `:62`) but presets exist: ShardImpact (1, 11, 0, .2, rot 0,0,1), StarImpact (1.3, 11, 0, .4, rot 0,0,1) (`Missile_Sequence__004_CameraShakePresets.luau:10-20`): roll-only shake.
- Star: flight 0.7 s Quad In (`:82`); impact at .69: FovBlur(70, 10, .2) (`:95`); floor clone placed 3 below, `InstantStar:Emit(1)`, `Instant Spec:Emit(1)`, `EmitAll(StarFloor.Impact)`; after 4 s missile destroyed; after +1 s the floor Model `ScaleTo` 1 -> 1.2 over 2 s Quad In while emitters disabled and light fades .8 (`:104-130`): **the ring keeps growing as it dies**.

Why it looks good: (1) every flash is 40-100 ms and sized 5-9 studs on a 4-stud target (1.5-2x overscale) with a 3-sprite stack (round glow + star + impact ring) at ZOffset 4-6.1; (2) the impact has both a hard 40 ms white-ish flash AND a 0.4-8 s soft afterglow (two timescales); (3) camera: FOV punch 7-10° + blur 10 decaying in 100-200 ms; (4) the missile is 3 stacked textured trails + spark stream + streaks + point light; (5) anticipation: inward-spiralling charge trails with 50 ms stagger, then 0.7 s beat; (6) three missiles 110 ms apart (a rhythm, not a simultaneous blob).

### 2.3 `sTier__Purple_arcane_showcase` (gold -> purple arcane orb sequence; the largest file)

Moments: **orb charge** (6 wisps fly in) -> **fire projectile** (arc, 0.9 s) -> **impact** + floor sigil + 10 orbiting wisps -> **wisps collapse into the centre one by one** -> **final burst**. Colour sequence on nearly every emitter: **#fff839 (yellow) 0 -> #ff821c (orange) .25 -> #6334ff (violet) .44 -> violet** (hot to cool inside a 0.4 s life) [data]. Lights: PurpleLight (0.52,0.10,1) + GoldLight (1,0.71,0.14), Br 1.

| Group | Layers | Key values |
| --- | --- | --- |
| `PurpleProjectile.Body` | Low Res Burst 13486412595 x3 (4x4 oneshot; Rate 60; Life .48-.96; Size 0 -> peak at **9%** 1.66-2.5 ±100% -> 0; Speed .3-6.4; Drag 1; EmissionDirection Back; Br 15 / 5 / 1 at ZOffset 0 / -.1 / -.2); 360 Slash 76655342066208 (Orientation 3, Life .4-.7, Br15); Rippling Smoke 134788710166485 (Size 0 -> 2±2 -> 6.3, Br .6, Tr 0 -> 1, Life .7-1.1, Z -.25) | three copies of ONE sprite at Br 15/5/1 = hot core / mid / dim body |
| Beams (Folder "Beams", 16 beams on 8 attachment pairs) | Beam75 118613370531472, Segments 20, CurveSize0 2.2, Width0 1.1 -> Width1 3.08, Br6 TexLength 4.4 TexSpeed 6 Tr 0 .79:0 1:1; second set Br4 TexLength 6.6 TexSpeed 5 Tr 0 .73:0 .9:1 ZOffset -.01 | 8 curved flame-like ribbons × 2 texture lengths scrolling at 5-6 studs/s, TextureMode Static (2) |
| Trail | Beam89 83108983635987 Life .4 WidthScale .48 -> 1, Br6, Tr 0 -> 1 | |
| Impact (`Attachment "Impact"`) | Blurry Spec Life **0.04** Br6 Size 21 -> 26+, Z6; Blurry Spec Life .7 LE1 Br1 Tr .7 -> 1 Size 23 Z1; Impact37 16892305780 Life **0.1** Size 30 **shrinking** to ~20 Z6; Blurry Spec Life .04 Size **53** const LE1 Br.1 (single-frame full flash); Impact30 16892282672 Life .04-.06 Size 21 Br3; Magic Symbols 2 11726473936 (8x8 loop FlipbookFramerate 3-5, Speed 76-122, Drag 10, Acc +7.6 y, Spread ±360, Tr 0 .09:0 1:0... fades at the end; runes burst outward); OffCentered Spec 4 17334135713 x2 (Br1 LE0 / Br15 LE1, Speed 76-152, Drag 12, Acc -53 y, RotSpeed ±200, Life .7-1.2 -> sparks that arc down); Erica Water Specs 4x4 95663805385992 Life .7-1 Size 20 LE1 Br.65 | flash of 40 ms + 100 ms impact shape + 700 ms soft ring + sparks |
| `Charging` (the 6 incoming wisps) | continuous: Rippling Smoke, Low Res Burst x3 (Br 1/5/15), OffCentered Spec x2, Glowing Bezier Line x2 (16056965573 Orientation 2, Acc +22 y), Dust Particles 2 138061581256149 x2 (Z -1.4/-.4), Magic Symbols Rate 15, Trail "BeamDrag tendrils" (Width 0 -> .21 at 5% -> 1; Tr 1 .08:1 .12:0 1:0); `Emit` attachment (burst): Star102 Size 10 -> 0 Life .25 Squash .1, Blurry Spec 4 Life 40 ms Size 6 -> 10+, **2 layers thick ring 15268066299** Life .165 Size 8 -> ~4 (**inward**), Blurry Spec Life .3 Size 13 -> 8.5 (inward), Outward Noise Shockwave 92991665171281 Life .26 | arrival burst contains an inward collapsing ring (Size 8 -> 4) -> sells "absorb" [inference] |
| `OrbVFX` / `Orb2VFX` | Thaw Blur 76668908828802 Rate 2 Life 1.5 Size 6, Tr 0 -> 1 .5:0; two copies (violet Br.15 Z5, gold Br.03 Z5.1); 360 Slash; Erica Water Specs; Blurry Spec Life .25 Rate 15; "Thaw energy swirl" 78467141337852 (Orientation 3 RotSpeed 10); Thaw Circle 1/2 103111872922608 / 71741749599073; Beam "BeamThick low glow" 18837316844 Segments **100** Br15 TexLength 5 TexSpeed 1.5, Width starts 0 and is tweened to 3-4 by script, x10 (CylindricalBeam, rotated 15°/s); Beam127 135482100082072 Segments 100 Br.5 LE1 TexLength 15 TexSpeed .16; Cartoony Shards Impact 131725470525741 (4x4, Life .25, Size 5 -> 7, RotSpeed 10, Br10 / 3 Z1.1 / .9) | orb = 2-colour glow + swirls + 10 long thin beams |
| `Floor` (ground sigil, Orientation 3) | Simple Jagged Circle 92606481798283 (violet Br7, gold Br4 Z -.001, Size 14.4, Life 2, Tr 0:1 .05:0 .5:0 1:1); Thaw Blur ×4 (Size 11.5-18); Fancy Shockwave 110017652984281 Size 10 ×2; I LE Flare 1 76256025789778 Z **15**; Text Circle 7 136674083788994 (RotSpeed 15, Size 13.97, gold Br5); Erica Water Specs; 4 beams "BeamThinner fractal" 12781853708 (Width 9.36, CurveSize 5.5, Segments 15) and "BeamMagical dust" 13580357222 (Width 5.76, CurveSize 5.5, TexSpeed .6) x4; "BeamFilled wavey" 18925205019 Width 21.6 -> 8.64 TexSpeed .3 Br3; "BeamBeam399" 13712010201; Noise Smoke (cylinder Shape 2, Rate 120, Squash .02 -> 3, LE1 Br.01, LockedToPart) ; PointLights gold Range13 + purple Range18 Br2 | ground circle: 6 stacked ring/glow layers at Z offsets of 0.001-0.06 (z-fight-safe) |
| `Wisp` | Magic Symbols, Star102 Size 10 -> 0 Life .25 RotSpeed 400, Star102 9.12 Life .1 Rotation 45, Blurry Spec Life 40 ms Size 6 -> 10+; lights Br1 Range 6/5 | each wisp's "pop" on arrival |
| `BigCharge` (final) | Thaw Blur ×2, Erica, Blurry Spec Rate 15, Energy Evaporate 15441275183 (Br .02, 4x4, Life .4-.6, Size 7.5), 2 layers thick ring Size 14 -> 8.8 Life .3 (inward), Cartoony Worm Fog, **Blurry Spec Life 0.04 Size 32 -> 37+ Br2**, Blurry Spec Life .7 Size 24 -> 30, Impact6222 71570654111653 Life .2 Size 18, Smaller version impact 120127136579962 Life .1 Size 13, Basic Hit Life .1 Size 18, Impact30 Life .2 Size 30 -> 20+ (shrinking), **Arrow Impact** (Orientation 1, Squash 1.3 -> -3, Speed **241**, Drag 15, Rotation 180, Life .3, Size 27.7 -> 25: a spike), OffCentered Spec Speed 72-144 Drag 15, Magic Symbols Speed 84-157 Drag 15 | final burst: 40 ms flash, 100-300 ms shape layers, spike spears (Speed 241 with Drag 15 = stops fast), runes + sparks |
| Orb meshes | `Orb1`/`Orb2` MeshPart MeshId 1886703108, Glass (1568), colour (51,51,52), plus 6 Textures (3139000937642842... = 139000937642842 "Simple Pixelated Star 2"), StudsPerTile .15, Transparency .85 | the orb is a Glass sphere with a faint star decal on every face [inference: placeholder art pieces, not the VFX] |

Choreography [data, `Purple_arcane_showcase__000_Showcase.luau`]:
- Charge-in: 6 `Charging` clones spaced `task.wait(.15)` (`:87`), random offset x/z ±18, y 6-11 (`:57-61`), Bezier (mid 50% + ±10/3-7/±10) over `Life = RNG(.4,.6)` Sine (`:74-75`); light Br 0 -> 1 in .1 (`:64`); at `Life-.1` `EmitAll(Charging, true)`, `ToggleAll off`, light Br->0 and Range ×3 over .3 (`:78-82`); destroy +3 s.
- Beams scale in: `Width0 = 3, Width1 = 4` over .4 s Smooth (`:28-46`); CylindricalBeam rotation 15°/s on Heartbeat (`:25`).
- `task.wait(1.5)` (`:91`) then projectile: `EmitAll(orbVFX.Spawn)` + `CameraShake("ArcaneSpawn", origin, 300)` (`:93-94`), arc (mid +20 studs up) 0.9 s `Quad In` (`:99`).
- Impact at +0.85 s (`:102`): Orb2 Size 6.5 -> 5 in .23 Quad (`:104-105`, again a size-pop), `Vignette(gold, violet, .01, .01, .2, .5)` (flash colour shifts gold -> violet while fading) (`:107`), `FovDepth(45, .4)` (FOV 45 -> 60 in .4 + DoF focus 0 -> 45) (`:108`), `EmitAll(Projectile.Impact)`, `CameraShake("ArcaneProjectile")` (`:109-110`), lights tween Br->0, Range 30/25 over .45 `Quart` (`:112-119`), floor beams start at width 0 and tween to authored widths .35 s later over .25 Sine (`:127,137-145`).
- Orbit: 10 wisps with per-axis Lissajous `x = X1*R*sin(a*X2)`, X2 .35-.4, Y2 .1-.4, Speed 1.5-4.5, R 1.5-4 (`:149-200`).
- Resolve: wait 2 -> orb fades (beam Transparency->1 .4, light .5), wait 3, each wisp `task.wait(.11)` apart flies to centre in .6 Quad, at +.5 emits + `Wisp` shake + vignette (transparency .9) + `FovBlur(54, 1, .05)` (`:238-266`); +.55 final `FovDepth(45,.4)` and `bigCharge.Emit`, `:Clear()` on lingering Middle/Noise/Floor emitters (`:274-279`), beams Transparency->1 and Width->0 in .5 (`:285-302`); 5 s later destroy.
- Shake presets (`Purple_arcane_showcase__004_CameraShakePresets.luau:10-26`): ArcaneProjectile (1.3, 13, 0, .6), ArcaneSpawn (1, 9, 0, .6), Wisp (1, 9, 0, .25); all **PositionInfluence (1,1,1), RotationInfluence 0** (translation shake only, no rotation).

Why it looks good: three-copy brightness stacks (15/5/1), yellow -> orange -> violet inside each particle's life, 40 ms mega-flashes (Size 32-53, ZOffset 6), inward-collapsing rings, spike spears with Speed 241 + Drag 15, scrolling textured beams (Segments 20-100) and ground sigil stacked at tiny Z offsets, a screen vignette that changes colour while fading, and 10 separate wisp mini-impacts (each its own shake + vignette) so the "sequence" has a rhythm of small beats before the finale.

### 2.4 `sTier__Astral_Sword` (SwordRain: a blue sword drops onto an aimed circle)

Ability module `Firable/SwordRain` listens for a server packet (`Astral_Sword__052_Ability.luau:30`); server sends `AimPosition` to all (`079_Ei.luau:29`). Colour: one blue (#5c7fff) on everything. Parts: `Sword` MeshPart (MeshId 16540857917, Material Glass 1568, DoubleSided), `Blade`, `Handle`, `TargetCircle`, a Star aura on the body. [data]

| Group | Layers | Key values |
| --- | --- | --- |
| Sword body (LockedToPart) | Star102 17391818367 ×4 (Rate 60, Life .11, Rotation 45, Squash -.5/-.3, Size .55/.97/1.62/2.91, Br 1/5/5/.5, Z 2.8-3.0, Tr 0 .5:... = 1 -> 0 -> 1) ; Spec19 16879789169 Size 9.7 Life .15 LE.3 Br1; Flare16New 108270101876122 Size 3.2±.4->1.2 Life .4-.5 LE1 RotSpeed ±45; Flare240New 15773612675 | 4 concentric star sprites of different size and brightness at Z 2.8-3.0 = lens-flare style hot core |
| Sword beams | Beam121 107746228303534 (Br2 LE1 TexLength 32.4 TexSpeed .2 Width 2.27 -> 1.62 ZOffset .3); Beam127 135482100082072 x2 (Br .2 / .35, Width 3.24 -> 2.59, TexLength 48.5 / 32.4, TexSpeed .4 / .3, Z -.1 / -.05); BeamGlowing Magic 6091474388 (Br .5, Z .4). All Segments 10, Tr 0 .12:0 .75:0 1:1 (fade at both ends), TexMode 2 | four beams between the same two attachments, 2 textures, different scroll speeds |
| Blade shed | Star102 ×2 (Speed 1.6-13, Drag 2, Br 6 / .3, Orientation 2, Squash -1), Constellation Spec 2 80103775847743 (Br 6 LE1 / Br1 LE0), Spec25 16879804431 ×2 (Br .3 / 6, RotSpeed ±60), Grey Galaxy Smoke 14919880888 (25 fps 4x4, LE.1 Br2.5), Energy Bezier Spec 14471362207 (8x8), Fireflies 2 | Rate 35-60 sparkle shed |
| Handle | Star102 ×2, Fancy Dissapearing Smoke 11822996479 ×2 (Br 1.6 / .1, Z .55 / .45, Orientation 2, Rotation -90) | |
| TargetCircle telegraph (Orientation 3 flat on ground; Rate 30, Life .2 = emitter re-seeded constantly) | Circle53 16878142704 Size 9.3; Simple Jagged Circle 92606481798283 ×2 Size 15 / 14.6 (Br 6 / .1, Z -.05); Circle18 16878077936 Size 11.7; Prism Circle 136488378522949 Size 12; Noisy Ripple Overlay 2 76204681346241 Size 12; PointLight Br 0 Range 25 (script tweens Br -> 5 in .25 s) | ring stack fades 1 -> 0 -> 1 in 0.2 s per particle; telegraph reads as shimmering |
| Impact (on TargetCircle, burst) | Spec19 **Size 60 Life 0.05** Br5 Z5 (full-screen flash); Spec19 Size 55 Life 3.5 Br2 Tr 0 .2:0 1:1 (long fade); Impact37 16892305780 (Size 19.5 -> 21+, Life .07-.11) ; Impact432 11037770108 Size 19.5 Life **0.06** LE1 Br6 Z6; Impact37 Orientation 3 (ground) Size 25 Life .05; Star102 ×4 (Speed 35-65, Drag 5, Acc -5, Spread ±67, Life .4-1.1, Size 3.75±1.38 -> 0) with Br 6 / .15; Spec25 / Spec27 gravity -5 / -25; Fancy Dissapearing Smoke Speed 35-65, Life up to 2.67, Size 3 -> 4.88; "Noisy Fading Crescent" 86398684443004 (Orientation 3, Size 10 -> 12+ Life .2-.8 ×2 Br 6 / .1); Ground15 91578195629955 (8x8, Orientation 3, Size 27 / 15, Life 1.3-1.8); **Rainbow5 126685678214657 Size 20 Life 1.5-3**, **Rainbow6 96288653875185 Size 0 -> 18-23 Life 2** (huge slow ring), Impact156 15502029648 Size 25 Life 1.6, Impact346 15264848485 Size 25 Life 1.5 | flash 50-60 ms -> shape 70-110 ms -> sparks 0.4-1.1 s -> smoke 2.7 s -> ring/shock 1.5-3.5 s |
| Ambient star dust (`Part` under Sword) | Star102 / Spec25 / Smoke, Shape 3, Rate 60, Orientation 1, Speed 3-6 | |

Choreography [data, `Astral_Sword__052_Ability.luau`]: sword spawned at aim +25 studs up, rotated to point down (`:36,50`); TargetCircle PointLight Br -> 5 in .25 (`:56`); sword spin 180° `Circular` .3 s (`:60`); wait .35; **rise 25 studs `Back In` .4 s** (anticipation overshoot then drop) (`:64`); wait .3, so impact fires 100 ms before the tween ends (`:66`); impact: `CameraShake("SwordImpact", aim, 999)` = (1.5, 13, 0, .4) rotation (5, .01, .01) i.e. pitch only, no position (`050_CameraShakePresets.luau:10-15`); `ColorFrame(.01, .2, (184,195,255))` blue-white tint flash with 10 ms attack and 200 ms decay (`:69`); light Br -> 0, Range -> 50 over .85 (`:71`); `ToggleAll` off on circle and sword (`:73-74`); `EmitAll(TargetCircle)` (`:75`); sword beams Transparency -> 1 in .1 (`:77-101`); sword hidden (Transparency 1) and destroyed after 5 s.

Why it looks good: telegraph (ring + light ramp 250 ms) before the hit; 4-way impact timescales (50 ms flash, 100 ms shapes, 1 s sparks, 2-3 s ring); pitch-only shake with 400 ms decay; sword is a real mesh with 4 beams + 4 star sprites riding it so it reads as a solid object with energy, not a particle cloud.

### 2.5 `sTier__Elemental_Guns_OPENSOURCE_ZRBLX` (Dual: a fire gun and an ice gun spawn, fire bullets, bullets impact; the most parts)

Colours: fire #ff5c2b (light (1,.51,.08)); ice #3180ff + #89d0ff, light (.31,.64,1). Parts: `FireGun`/`IceGun` MeshParts (MeshIds 7983565983 / 7983562591, Metal), sub-parts Core/Body/Handle/Tip, `FireBullet`/`IceBullet` with `Impact`. Lighting has Bloom Size 24. [data]

| Group | Layers | Key values |
| --- | --- | --- |
| Gun spawn "Core" (bursts, `EmitAll(Core)`) | Spec19 Size 16 Life .04 Br5 Z3; Impact31 16892284280 ×2 (Size 6 -> 0, Life .1/.12, LE.5/0, Br5, Z 2.9/2.8); Noisy Line Spec 2 15059553660 ×4 (Orientation 2, Speed 1-40 Drag 5-6, Size .6±.6 -> 0, Life .3-.7, LE 0/.5 pairs, Z +.1); Spec25, Fireflies 2 (8x8), Spinning Shard 2 16924875355, Watery Crescent 82798669195289, Smoother Fading Slash 13412718273 (all Orientation 3, Size 1.7 -> 3.4, Life .3-1.0), RightUp Smoke 13717823765 (Life .6-3, Tr .8±.08), Flare213New 108523870700360 / Flare170New 12105193694 (Rotation 45, RotSpeed 5-10, Life .7-.85) ; Beam127 ×2 Segments **200** | Pairs everywhere: same texture twice with LE 0 and LE .5 (or Br 5 and Br ~2.5) at Z +0.1 |
| Gun body/handle (continuous, Rate 25-45, LockedToPart) | Star102 ×3 Br 15 / 4 / .7 at Z 2.0/1.9/1.8, Size 0 -> .2±.2 (at 10%) -> 0, Life .4-1.0, Drag .3; Spec19 Br6 LE.2 Size 1.3 Z1.7; Dust Expansion 16503588946 LE1 Br.4 Size .6 | the "idle glow" of the held weapon; three Br levels of one star |
| Fire bullet (LockedToPart idle: Rate 2, Life 1.0) | Star102 Br.6 / 5, Spec19 Size 11 LE.5 Z -2, Flare213New Size 3 Rot 45 RotSpeed 45, Flare170New; Basic Flame Wisp 16504098653 (4x4, Rate 60, Life .4-1.0, Size 1.81±.5 -> 0, Br 2.5/3, LE 0/.5, Z .4/.5); Fancy Dissapearing Smoke Rate 30 Size 1.8 -> 2.9 Tr .85 -> 1; sparks Rate 60 Speed 5-25 Spread ±75 Acc -5 Drag 3-6 (Wisp, Fireflies, Spinning Shard); PointLight Br2 Range6; Trail "BeamDrag Thick" 5155825850 Life 1 LE.5 WidthScale .42 -> 0 Tr .5 | bullet = hot head + flame wisps + smoke + spark spray + textured trail |
| Fire impact (burst) | Spec19 **Size 45 Life .04 Z 15**; Impact13 16892226410 Size 16 -> 0 Life .12/.14 (LE .5 / 0, Br 2 / 3, Z 7.2 / 7.1); **Impact452 1021559161 Size 0 -> 12.1 (expanding), Life .1-.12**; Wisp/Fireflies/Spec25/Smoke burst Speed 15-30 Spread ±360 Acc -5 Drag 5 Life .3-1.75; Spec19 Size 31 Life 1.8 Tr 0 -> 1 LE.5 (long glow); Flare170New Size 9 Life 1.0 Tr 0 .24:0 1:1; Flare213New Size 9 Life .7; Ground15 Size 8-9 Life 1.2-1.65 Orientation 3 Z -.01/-.03 | Impact structure identical to the other files |
| Ice gun | Star Flipbook 15438447436 pair (blue Br15 LE0, pale Br6 LE1, Rotation 22.5 offset), Spec19, Flare314New 11828156780, Flare300New 100545368205823, Flare170New, Flare135New 14657035983, Chromatic2 13972642464, "Fancy" 132184538139052, Impact28 16892272385, Impact13, Star119 10335418884 (a different star), **8 Beam121 beams** (CurveSize0 -1.2, Segments 200, TexSpeed .6, Tr 0 .04:.1 .45:.1 1:1) | ice = same structure, different colour pair + snowflakes |
| Ice bullet | Other45 17226850679 (4x4), Snowflake 87559021239332 (8x8, Tr .18 -> 1, Br 6-15), Spec19, Flare174New 18836944836, Fancy Dissapearing Smoke, Spec25; impact: Spec19 Size 45 Life .04 Z 15, Impact221 12402875536 Size 16 -> 0 Life .12 / .1, Spec19 Size 27 Life 2, Other45 Speed 20-30, Snowflake Speed 20-30, Fireflies Size 2.5 -> 3.5, Fading Smoke Hole 18326864825, Ground15; Trail "BeamStretched Wave" 14543379496 Life 1.75 LE1 Br.4 WidthScale .42 -> 0 | |

Choreography [data, `Elemental_Guns__052_Ability.luau`]: guns spawn ±5 studs sideways, 5 up (`:50-51`); `EmitAll(Core/Body/Handle)` and `CameraShake("Spawned")` = (1.1, 3, 0, .4) rot (1,1,1) (`:60-68`); `task.wait(1)` (`:70`); bullets spawn at `Tip` and `EmitAll(Attachment)` + `EmitAll(Tip)` (`:82-85`); gun light Br -> 0 / Range 30 in .4; guns slide back (0,-1,3) with 15° yaw and fade out in .7 `Quart` (`:87-90`); `CameraShake("Shoot")` = (2.5, 10, 0, .8) rot (1, .1, .1) (`:95`). Bullets: manual Heartbeat move at **50 studs/s** with `Shapecast` (`:28,108,128`); lifetime 5 s (`:27,100`). Hit: `fireBullet.Rotation = 0`, `CameraShake("BulletImpact")` = (1, 20, 0, .55) rot (5, .1, .1) (`:111-113`), `EmitAll(Impact)`, `ToggleAll(bullet, false)`, light Br->0, Range 6 -> 35 in .4 (`:118`), `Clear()` on LockedToPart emitters so no stale glow remains (`:120-122`), debris 5 s. Separate LocalScript `C` key: clones `Cartoon` explosion 5.5 studs ahead, `task.wait(.303)` then light fade + `CartoonPuff` shake (1.4, 13, 0, .55) (`Elemental_Guns__081_LocalScript.luau:17-27`); the `Cartoon` asset is not in this dump.

### 2.6 `sTier__Mildly_wet_projectiles` (water bolts, 4 per cast)

Colour: flat #7ba5ff on every emitter; light (.46,.63,1). `Projectile` (13 emitters, light Br1.5 Range11 Shadows true) and `Impact` (28 emitters + light Br9 Range **0**). Bloom Size 24. [data]

| Group | Layers | Key values |
| --- | --- | --- |
| Projectile (Rate-driven) | Water10 16865899680 ×2 (4x4, Rate 60, Size 0 -> 1.24±.82 at 7% -> 0, Life .5-1.2, Br 10 / 5, Z 0 / -.5), Water12 16865903588 ×2 (Rate 35 / 15, Size 1.65 -> 3.2, RotSpeed ±50, Br 6 / 2.5), Spec24 16879802703 ×2 (Rate 60, Speed 10-15, Acc -10, Drag 5, Br 3 / 1.1), Water41 16866196212 (Rate 35, Size .3, Acc +2, Br10), Smoke33 16867492882 (Rate 60, Size 2, Tr 1 .14:.75 1:1, Z -1), Water23 16866031614 ×2 (8x8, Rate 25, Size 0 -> 1.5±.44, Tr 1 .52:0 1:1) | water bolt = droplets + ripple blobs + sparkle specs + a smoke body at Z -1 |
| Impact flash | Spec19 Size 32 Life .05 Br2 Z7; Impact28 16892272385 Life .1-.15; Impact13 Life .07-.1; Water 122108197100564 Life .1-.3 Size 2.5 -> 5.75; Wavey 137167224180401 (RotSpeed 50, Life .2, Size 10); Rainbow6 ×2 Life .9 (9 / 18 studs); Flare20New 70728001087698 Life .9 | |
| Impact spray | Water12 ×3 (Life .1-.4, Size 5 -> 6+), Water10 ×3 Speed 20-30 Acc -6 Drag 5 Spread ±360 Life .4-1.3, Spec25 / Spec24 Life up to 1.8, Water41 ×2 Life .6-1.7, Smoke33 / Smoke40 16867530947 Speed 15-25 Tr .9±.06, Spec19 Size 35 Life 1.7-2, Water50 76951334461630 ×2 and Water27 16866055035 ×2 (8x8, Orientation 3 ground splash, Size 9-10, Life .3-1.1, LE 0/1 pair, Z -.05) | |

Choreography [data, `Mildly_wet__052_Projectile.luau`]: on cast `CameraShake("WaterMissileSpawn")` = (.3, 3, 0, .3) rot (1,1,1) (`:46`) and a blue `Vignette((181,211,255), .25, .5, .25, .7)` (`:48`), a light on the caster Br 2.5, Range 0 -> 15 over .6 (`:50-56`). Four bolts (`for _ = 1,4`), each aimed at the target + ±6 random in x/z (`:58-60`), path = origin -> 3 random Bezier points (midway ÷1.5-2.5, +±15/5-10/±15) -> aim (`:68-83`), duration `RNG(.65,.95)` linear (`:86`). Impact at `Time - .1` (`:91`): `CameraShake("WaterMissileImpact")` = (.55, 23, 0, .3) pos (.1,.1,.1) rot (2,1,1) (`:93`), `ColorFrame(.001, .25, (237,246,255), aim)` white-blue flash with 1 ms attack (`:94`), Impact clone `EmitAll`, bolt emitters off, impact light Br 9 -> 0 and **Range 0 -> 40 over .3** (`:105`); cleanup 3 s.

### 2.7 `sTier__FUGAAAA` (a character-rig "Fire Arrow" flying kick/arrow; pre-baked animation, no script)

A `Fire Arrow` model with a baked KeyframeSequence "firearro" (641 keyframes, 4292 poses) and a hidden `projectileArrow` part carrying beams/trails/emitters. Timing of the animation is not in the dump. Colours: orange #ff5a08 -> red #ff1100, black #000000 and brown #725f58 smoke. [data]

| Group | Layers | Key values |
| --- | --- | --- |
| Arrow head beams (9 total) | Beam 9541055154 and 14539652514: Width0 **0** -> Width1 10 / 20 / 30 / 50, Br10 LE1, Color #ff5a08/#ff4208 -> #ff1100, Segments 10, FaceCamera true, Tr 0 .15:.76 1:1 or 0 .58:.85 1:1 or 1 .48:.74 1:1 | cones that start as a point and flare out 10-50 studs = speed-cone; transparency high from 15% so mostly the base glows |
| Arrow emitters | ParticleEmitter 12159555294 (Rate 8, RotSpeed 500, Size **-152 -> -11 -> +6.5 ...** (negative start), Life .3-.5, Br5); ParticleEmitter 14762356114 (Br **40**, Drag 20, EmissionDirection Front, Squash -1, Size 0 -> 2.4 -> 0 -> ..., Transparency also a 0 -> .76 -> 0 pulse, Speed ±15); Star 13869207552 (Squash -9 -> -18.4 = a very long sliver, Life 1, LockedToPart, Rate 2, Br15, Z1.5); "Dots" 16034466586 (**Rate 500**, Acc z +45.6, Size 0 -> .1±.1 -> 0, Life .5-.95, Speed 2.3-16, Spread 360, Br10, #ff9327 -> #ff0000) | |
| Trails ×3 (f1-f3) | 14539652514 (Life .25, Width 1 -> 0), 11508013518 (Life .3, TexMode 2 TexLength 10, WidthScale 0 -> .32 -> .46 -> .48 -> .39 -> 0), same at TexLength 20 with LE1; all Br10, #ff5601 -> #ff0000 | 3 trails along one attachment pair, different textures/lengths |
| Smoke wake (`Part`, Acc z +100, Drag 5, Rate 35, Speed 30, Spread 7-180) | smoke 18818002027 (Br 3.25), smokeT 74329932537598, smoke2 105518239092629, smoke1 11827618350, smokeSpecs 5368629557 / smokeSpecs1 7231210720 (Br 10 LE0.8), colour #725f58, Tr starts .1 -> fades by 97% | brown smoke blown backward at 100 studs/s² |
| Wind beams | Beam 18943984835 ×2 white, CurveSize ±1, Segments 30 / 20, Width0 0 -> Width1 30, Tr .64 -> 1, TexSpeed .75 | air streaks |
| Fire body | "Fire1" ×2 (11499447365, 14162711722; Rate 55, Life .2-.5, Size 0 -> ~1.4, Speed 15, ShapeStyle 1); **DarkSmoke1 ×2: 15072761142, same size/lifetime. Copy A: Color #ffffff, Brightness 0, LightEmission -1.5, Tr .91 -> .88 -> 1, Z -0.?; Copy B: #ff3c00, LE1, Br10, Tr 0 .48:.79 1:1, Z -.25** | the only negative LightEmission in the set: a subtractive dark underlay beneath a glowing orange copy |
| Flicker | "15" ×2 11762072190 (Orientation 2, Life **0.075-0.1**, Rate 15, Size 0 -> 2.5±1.3 at 12% -> 0 -> 3 at 82% -> 0 (two pulses), Squash 0 -> 3 at 11% -> 1.2, red Br0 LE0 and orange Br1 LE1) | single-frame-ish streak flicker |
| Black ink layers | "2" ×3 7709167392 (**black #000000**, Orientation 2, Rate 100, Life .15-.4, Tr .4 const, Speed 5 / 25, Size 2.5 -> 3.3 -> 2.2 pulses, Z 2.52) ; "yes" ×4 (17514876643 #ff5411 -> #dc490f -> #050200 -> black over life with Br20; 17749735982; 17507124046 black with RotSpeed 100 + orange copy) | burnt-out cinders: flame gradient ends in black (a colour tail), plus pure-black sprites at Tr .4 to carve contrast under the glow |

Why it looks good: huge width cones starting from 0 width (speed shape), brown smoke wake, black underlay layers (contrast), 500/s tiny dots, three textured trails, a keyframed rig so the VFX are tied to body motion.

## 3. Why the S tier looks good: concrete techniques (consolidated)

1. **Dozens of thin layers, not one big sprite.** 11-150 emitters per effect, each doing ONE job (core, halo, flare, spec, smoke, ring, trail, beam). A fireball would be ~20-30 layers [inference].
2. **Same sprite stacked 2-3x at different Brightness and a hair of ZOffset.** Br 15 / 5 / 1 (Arcane Body, Elemental Body), or LE0 Br5 + LE.5-1 Br2.5-3 at Z ±0.1 (Elemental). Hot core + mid + dim body from a single texture.
3. **Impacts are layered over 4 timescales.** 40 ms flash (Size 21-60, Z 5-15), 70-120 ms shape sprites (some **shrinking** from large, ~Size 7 -> 4.8 or 30 -> 20), 0.4-1.8 s sparks/smoke, 1.5-8 s soft ring or glow tail.
4. **Sizes start at 0 or tiny and peak early.** Sparks: `0:0, 0.06-0.1:peak±peak, 1:0` (random size 0..2×peak). Sprites ease out. Nothing starts at full size and pops.
5. **Colour inside a particle's life.** Arcane: yellow -> orange -> violet in 44% of life. Flame: orange -> dark brown/black. Single-hue effects (Wet, Astral) rely on Brightness differences instead.
6. **Textured trails and beams, never plain.** All 22 beams/trails across files use a texture; widths start at 0, TextureMode static with TexLength 4-48 and TexSpeed .15-6; 2-4 trails/beams stacked with different lengths.
7. **Velocity-aligned streaks** (Orientation 2, Squash .1-.7) for speed; **ground-flat rings** (Orientation 3) for footprints; **8x8 flipbook "specs"** (Fireflies/Snowflake) for sparkle.
8. **Gravity + drag on bursts**: Speed 15-150 with Drag 5-15 and Acc -5 to -53 makes sparks fly out, brake, then fall. (Arrow spike Speed 241 + Drag 15.)
9. **Light/camera hits scripted with it:** light Br -> 0 while **Range expands** (6 -> 15/25/35/50) so the glow "blooms outward"; FOV punch 67-70 (or 45) -> 60 in 100-400 ms with blur 10 -> 0; colour-tint flash 1-10 ms attack + 200-250 ms decay; screen vignette that shifts colour while fading; shake presets with fadeIn 0 and fadeOut .25-.6.
10. **Anticipation and staggering:** charge trails 50 ms apart, 0.7 s hold, barrage at 110 ms, wisps at 110 ms, sword `Back In` pull-back, 250 ms light ramp on the telegraph.
11. **Part-size pop**: muzzle/target part scaled 4.52 -> 4 (+13%) in 0.2 s or 6.5 -> 5 in .23 s on every hit: the surface itself kicks.
12. **The mesh is real**: Sword MeshPart, gun MeshParts, Glass orb: particles dress a solid shape.

## 4. Technique catalog (S tier). All values start points [data from the files], applicability to our brick game is [P].

| ID | Recipe | Exact starting values |
| --- | --- | --- |
| ST-01 | **Triple-brightness stack** for any glow/core | one texture, 3 emitters, same Size/Life/Color; Brightness 15 / 5 / 1 (or 6 / 2.5 / .7); ZOffset +0.0 / -0.1 / -0.2; LE 0 on all (Arcane) or LE1 on the top one only; Tr 0 -> 0 with Size 0 -> peak@9% -> 0 |
| ST-02 | **Hot/dim twin** with LightEmission pair | copy A LE 0 Br 5-6, copy B LE .5-1 Br 2-3, ZOffset B = A + 0.1 (Elemental pattern) |
| ST-03 | **Impact flash ladder** (burst, Rate 0, `Emit`) | (a) round glow "Basic Blurry Spec"/Spec19, **Life 0.04**, Size 5-8× target (4 studs -> 20-45), Br 2-6, ZOffset 6-15, Tr 0 -> 0; (b) star (Star102) Life .04-.07 Size ~1.5× target, Squash -2 or Rotation 45; (c) impact shape (Impact13/37/40) Life .1, Size 7 -> 4.8 (shrinks); (d) soft ring Life .4-.7 Tr .3-.7 -> 1; (e) long tail Life 1.5-8 Br 1-2 Tr .3 -> 1 |
| ST-04 | **Spark burst** | Star/Spec25/OffCentered Spec; Speed 20-65 (or 72-152 for big), Drag 5 (12-15 big), Acc -5 (down to -53), Spread ±67..±360, Life .4-1.4, Size `0:2.9±1.4 1:0`, RotSpeed ±80..±200, two Br tiers (6 and .15) |
| ST-05 | **Peak-at-9% spark** (continuous) | Size `0:0 0.07-0.1:0.2-1.7±100% 1:0`, Rate 45-60, Life .4-1.0, Speed .1-6, Drag .3-1, Tr 0 -> 0 |
| ST-06 | **Fade-in/out sprite** (ambient/aura) | Tr `0:1 0.4-0.5:0.0-0.3 1:1`, Size flat or +10-20%, Life 2-5, Rate 2-25 |
| ST-07 | **Hot-to-cool colour ramp** | ColorSequence `0:#fff839 .25:#ff821c .44:#6334ff 1:#6334ff` on a 0.4-1.2 s life; flames: `#ff5411 -> #dc490f .6 -> #050200 -> #000000` |
| ST-08 | **Dark underlay** | black (#000000) sprites, Tr .4, Orientation 2, Rate 100, Life .15-.4 under the glow; or LE **-1.5**, Color white, Br 0, Tr .9 (copy B orange LE1 Br10 at Z +.25) [FUGAAAA only; 1 of 492 emitters, so treat as optional] |
| ST-09 | **Three-trail projectile** | Trail A "tendrils" Life .3 Width .25 -> 0 Br4; B Life .6 Width .32 -> 0 Br6 Tr `1 .15:1 .35:0 .84:0 .92:1 1:1`; C Life .85 TexMode 2 TexLength 14-20 WidthScale `0 .15:0 .54:.27 1:0` Tr .1 Br1.5; FaceCamera true, MinLength .1-.15, same Attachment pair, own textures |
| ST-10 | **Scrolling ribbon beams** | Beam Segments 10-20 (100-200 only for long curved ones), TexMode 2, TexLength 4-48, TexSpeed .15-6, Width0 1-3 -> Width1 1.6-3, Tr `0 .75:0 1:1`; 2-4 beams on the same attachments with different TexLength/TexSpeed and Z -0.1..+0.4; Brightness .2-6 |
| ST-11 | **Cone from zero width** | Beam Width0 0 -> Width1 10-50, Tr 0 .15-.58:.76-.85 1:1, Br10, LE1 (speed cone / blast) |
| ST-12 | **Velocity streaks** | Orientation 2, Rotation -90, Squash .1 (thin) to .7, Rate 15-60, Speed 2-15, Drag 2, Life .3-1.35, Size `0:.5±.5 1:.23±.2` |
| ST-13 | **Ground telegraph/footprint** | Orientation 3, Speed .001, 5-6 ring/glow layers Size 10-15, Life .2 (re-emitted, Rate 30) or 2 s (Rate 2), Tr `0:1 .5:0 1:1`, ZOffset steps of .001-.06 so rings never z-fight; light Br 0 -> 5 in .25 s |
| ST-14 | **Inward collapse ring** (absorb/charge) | ring texture Size 8 -> ~4 (or 14 -> 8.8), Life .165-.3, Br .01-.15 LE1; ST-14 pairs with a burst sprite Size 6 -> 10 Life .04 |
| ST-15 | **Spike spears** | Orientation 1, Squash `0:1.3 1:-3`, Speed ~240, Drag 15, Life .3, Size ~27 -> 25, Rotation 180 |
| ST-16 | **Light fade with range growth** | PointLight Shadows off; at impact tween Br -> 0 and Range ×2.5-3.5 (6 -> 15, 6 -> 35, 14 -> 30) over .25-.85 s; Wet impact light starts at Range 0, Br 9 and expands to 40 in .3 |
| ST-17 | **FOV + blur punch** | `FovBlur`: FOV 67-70 (or 54) -> 60, BlurEffect 10 (1 for small) -> 0, Quad, 100-200 ms; big finale `FovDepth` FOV 45 -> 60 with DoF focus 0 -> 45 over .4 s |
| ST-18 | **Tint flash** | ColorCorrection TintColor from white to a pale colour of the effect ((184,195,255), (237,246,255)), attack .001-.01 s, decay .2-.25 s, distance-gated |
| ST-19 | **Vignette with colour handoff** | screen ImageLabel (ZIndex -5), fadeIn .01-.25, hold .01-.5, fadeOut .2-.25, peak transparency .5 (big) / .7-.9 (small), colour A -> colour B while fading |
| ST-20 | **Shake presets** (translation OR rotation, never both big) | impact: (1-1.5, 11-20, 0, .2-.55), rot (5,.1,.1) pitch / (0,0,1) roll, pos 0; arcane translation: (1-1.3, 9-13, 0, .25-.6), pos (1,1,1), rot 0; light: (.3-.55, 3-23, 0, .3). fadeIn always 0; magnitude ≤ 2.5 except a one-off thrown impact 15 |
| ST-21 | **Part-size pop** on the hit surface | Size ×1.13 then back in .2-.23 s (`4.52 -> 4`, `6.5 -> 5`) |
| ST-22 | **Anticipation/rhythm timings** | telegraph light ramp .25 s; sword `Back In` .4 s; charge points every .05-.15 s; hold .7 s; barrage every .11 s; flight .65-.95 s `Quad In`; impact scheduled `flight - .01 .. -.1`; resolve cleanup 4-6 s |
| ST-23 | **Curved flight** | 3-5 point Bezier, mid point at 22-50% with jitter (±15 x/z, +5..+15 up, up to +20 arc); orient along path |
| ST-24 | **Orbiting wisps** | Lissajous `sin(a*X2)` per axis, X2 .35-.4 / Y2 .1-.4, R 1.5-4 × amplitude 1-8, speed 1.5-4.5; collapse to centre at .11 s stagger, .6 s Quad, emit at .5 s |
| ST-25 | **Kill switch** | end loops with `Enabled=false`, `:Clear()` on LockedToPart emitters, Transparency tweens on beams (.1-.5 s), destroy after 4-6 s |
| ST-26 | **Locked vs shed** | LockedToPart true for flares riding the head (Rate 2, Life 1, Tr `0:1 .5:0 1:1` = a slow throb), false for debris/smoke trailing |
| ST-27 | **Hold-over layers** | one emitter in the burst set with Life 4-8 s and Br ≤ 2 (the scorch/afterglow), plus `ScaleTo` growth ×1.2 on the floor ring while fading (Missile star) |
| ST-28 | **Fixed texture palette per element** | same 4-5 base textures reused per effect (Star102, Spec19, Spec25, Fireflies 2, Basic Blurry Spec); element identity from colour pair + 1-3 signature sprites (Water10/12/23, Flame Wisp, Snowflake) |

## 5. Texture reuse (counts from emitters/beams in the 7 files; names are the emitter names, which mirror the artist's texture library; purposes are [inference] from names and use)

| Texture id | Name in file | Uses / files | Seems to be |
| --- | --- | --- | --- |
| 17391818367 | Star102 | 46 / 4 | 4-point star flare, used as core, spark, impact star |
| 77024587778878 | Basic Blurry Spec | 31 / 3 | soft round glow disc (flash, back glow) |
| 16879789169 | Spec19 | 24 / 3 | soft glow spec (flash, halo, long tail) |
| 17334135713 | OffCentered Spec 4 | 22 / 1 | spark with off-centre hot spot (spinning sparks) |
| 16879804431 | Spec25 | 16 / 3 | small spark/diamond spec |
| 11822996479 | Fancy Dissapearing Smoke | 16 / 2 | soft smoke puff |
| 118613370531472 | Beam75 | 16 / 1 | flame-like ribbon beam texture |
| 87790026409442 | Fireflies 2 | 15 / 3 | 8x8 sparkle/firefly flipbook |
| 135482100082072 | Beam127 | 14 / 3 | thin energy beam texture |
| 16056965573 | Glowing Bezier Line | 14 / 2 | curved streak line (Orientation 2) |
| 76668908828802 | Thaw Blur | 14 / 1 | soft blur disc (4x4) |
| 11726473936 | Magic Symbols 2 | 13 / 1 | rune/symbol flipbook (8x8) |
| 18837316844 | BeamThick low glow | 10 / 1 | wide soft glow beam |
| 129871600983536 | Rotating Star | 10 / 1 | star flipbook (4x4) |
| 13486412595 | Low Res Burst | 9 / 1 | pixel-ish burst flipbook |
| 107746228303534 | Beam121 | 9 / 2 | beam texture |
| 12105193694 / 108523870700360 / 10335418884 / 100545368205823 | Flare170New / Flare213New / Star119 / Flare300New | 8 / 7 / 8 / 3 | lens-flare / star sprites for halos |
| 92606481798283 | Simple Jagged Circle | 6 / 2 | ground ring (telegraph) |
| 91578195629955 | Ground15 | 6 / 2 | ground splash flipbook (8x8) |
| 16892226410 / 16892272385 / 16892284280 / 16892305780 / 16892332741 / 16892282672 | Impact13/28/31/37/40/30 | 6/2/..: | impact shape sprites (the 100 ms "shape" layer) |
| 14379750639 | Basic Hit | 4 / 2 | hit burst flipbook |
| 80103775847743 | Constellation Spec 2 | 4 / 1 | dotted constellation spec |
| 16865899680 / 16865903588 / 16866196212 / 16866031614 / 16866055035 / 76951334461630 | Water10/12/41/23/27/50 | 5 / 1 each | water droplet / splash flipbooks |
| 16867492882 / 16867530947 | Smoke33 / Smoke40 | 3 / 1 | spray mist |
| 16504098653 | Basic Flame Wisp | 6 / 1 | flame wisp (4x4) |
| 15059553660 | Noisy Line Spec 2 | 6 / 1 | noisy streak |
| 96288653875185 | Rainbow6 | 2 / 2 | large soft ring/aura (Astral, Wet) |
| 86398684443004 / 82798669195289 | Noisy Fading Crescent / Watery Crescent | 2 / 2 | crescent slash |
| 18326864825 | Fading Smoke Hole | 4 / 2 | smoke ring with hole |
| 3057073083 | Slightly Rounded Star | 3 / 1 | rounded star (also as a Texture decal) |
| 8037777212, 8944384590, 17612093017, 87694680685820, 134254043650523, 15501967496, 77024587778878 | Star116, Line Spec 4, Stylized Smoke13, Cobweb Overlay, Energy Vague, Impact128 | 1-2 | space ambient set |

147 unique textures in 7 files, but ~20 account for most of the layers; the artist's own guide says reuse textures (ZO-11) [data: `knowledge/reference/vfx/13-practitioner-optimization-zonito.md`, also the shared `Firable` folder re-uses the same module in 3 files]. Beams/trails: textures like Beam127, Beam75, Beam121 are reused 9-16 times.

## 6. Pattern differences between files (what a fireball should copy)

| Question | Answer from the data |
| --- | --- |
| Is the core a round disc? | Never alone. Core = round glow + 4-point star (Star102) + a flare (Flare170/213) at Rotation 45, Z +3..+5; the round glow is only the Life 0.04 flash and the back halo |
| How is motion shown? | Orientation-2 streaks, 2-3 textured trails (width 0 -> .3 -> 0), a beam cone from 0 width, smoke wake with Acc +100, spark spray with Acc/Drag, Bezier flight with orient-along-path |
| Centre glow | Br 15 LE0 star-copy + Br 5 + Br .7 dim copy, LE1 on the spec, PointLight Br 2 Range 6-14 (Missile 7, Elemental 6), colour from the hue, Shadows false except Wet (true) |
| Trail | always textured, always FaceCamera, width 0 -> 0.25-0.5 -> 0, Life .25-1.75, 1-3 stacked |
| "Real" particles | variation: Size `±` envelopes everywhere, Rotation -360..360, RotSpeed ±50..±200, Speed ranges [20,30], Life ranges [0.4,1.0], Tr fade-in/out; nothing is a single fixed value |

## 7. Moments map

| File | Windup | Travel | Hit | Aura/after |
| --- | --- | --- | --- | --- |
| Missile | Charge circle r16 (50 ms stagger) + 0.7 s | 0.8 s Quad In; 3x at 110 ms | 40 ms flash + 8 s afterglow; FOV 67 | Star floor ring ×1.2 over 2 s |
| Arcane | 6 wisps in (0.4-0.6 s), 1.5 s hold, orb beams | 0.9 s arc | flash + sigil + 10 wisps, vignette | wisps collapse, final burst at ~6 s |
| Astral | ring + light ramp .25 s, sword spin .3 s | pull-back .4 s | 50 ms flash, 2-3.5 s rings, tint + shake | light fades .85 s |
| Elemental | guns spawn (1 s hold, shake Spawned) | 50 studs/s, 5 s | spark ladder + Br light | `Clear()` locked emitters |
| Wet | caster light + vignette | 0.65-0.95 s ×4 curved | 4 impacts, tint, shake 23 Hz | 3 s |
| FUGAAAA | baked animation | cone beams + smoke wake | n/a | n/a |
| Space | n/a | n/a | n/a | continuous ambient |

## 8. Transferable numbers for a fireball [P: starting points only, not measured]

Head: ST-01 stack on Star102 + Flare170 (3 Br tiers), round glow at Life .15 only as a halo; 2 flame wisps (Rate 60, Life .4-1.0, Size 1.8±.5 -> 0, Br 2.5 LE0 and Br 3 LE.5); smoke Rate 30 Tr .85 -> 1; spark spray Rate 60 Speed 5-25 Acc -5 Drag 3-6; ST-09 trails; light Br 2 Range 6; impact via ST-03 + ST-04 + ST-13 ring; camera ST-16 to ST-18 only at the owner's rating band (brick game note: the skill's shake/flash rules apply, CA-01).

## 9. Colour usage [data]

Missile #5364ff -> #2c25ff + (0.01,0,0.18) dark texture tint · Arcane #fff839/#ff821c/#6334ff · Astral #5c7fff + (0,.32,1) light · Elemental #ff5c2b / #3180ff + #89d0ff · Wet #7ba5ff · FUGAAAA #ff5a08 -> #ff1100, black, #725f58 smoke · Space #948aff + #fdff73. Two hues at most per effect; the second hue is a light-source accent or a cold-end of the gradient.

## 10. What differs from our failed fireball (owner complaints) [inference]

| Owner complaint | S-tier answer |
| --- | --- |
| Round sphere reads as no motion | No S-tier effect has a lone sphere; motion = streaks (Orientation 2), cone beams, trails with texture, smoke wake with +Acc, Bezier orientation |
| Bad centre glow | stacked Brightness 15/5/1 + star + flare + point light range 6-14; core is a hot tiny star, halo is a soft disc at low Br |
| Untextured trail | every Trail/Beam uses a texture, TexMode 2, TexLength 14-48, width 0-start, 2-3 stacked |
| Fake-looking particles | all values randomised (Size ±, Rotation, RotSpeed, Speed/Life ranges), gravity/drag, fade in/out, 2 Br tiers per sprite |

## 12. Emit counts per burst layer (attributes, EmitDelay is 0 or absent on every S-tier emitter) [data]

Rule visible in the counts: **flashes/shapes/rings emit 1 (2 for a doubled layer); sparks and smoke emit 10-70; flipbook "specs" 15-50; idle-glow bursts 2-5.** One emitter, one `Emit(n)`; no sub-frame delays are used (all stagger is done in script with `task.wait`).

| Effect / group | EmitCount per layer |
| --- | --- |
| Missile muzzle (`Spawn`) | Blurry Spec 1, Circle4 1, Rounded Star 1, Rotating Star 2 ×2 |
| Missile `End.Impact` (3 missiles) | Blurry Spec 1 ×2, Basic Hit 1, Impact40 1, Star102 1 ×2 (all flashes = 1) |
| Missile `StarImpact` | flashes 1 each; Rotating Star **16** ×2, Snowfall **16** ×2, Fading Smoke Hole 15; `End` debris: Rotating Star 13 ×2, Snowfall 20 ×2, Smoke Hole 12 |
| Missile floor | rings 4 each (Smooth Circle, Circle outlines, thick ring, Blurry Spec, Instant Spec, Star, InstantStar, Slightly glowing, Noise 4); spiky wave 1, Basic Hit 1 |
| Arcane projectile `Impact` | Blurry Spec 1 ×3, Impact37 1, Impact30 2, **Magic Symbols 25 ×2, OffCentered Spec 25 ×2**, Erica Water 2 |
| Arcane `Charging/Emit` (each arrival) | Magic Symbols 32, **OffCentered Spec 50 ×2, Glowing Bezier Line 50 ×2**, Star102 1, Blurry Spec 1, thick ring 1, Shockwave 1 |
| Arcane `Wisp/Emit` | Magic Symbols 50, OffCentered Spec 50 ×2, Bezier Line 50 ×2, Star102 1 ×2, Blurry Spec 1 |
| Arcane `BigCharge/Emit` | flashes/shapes 1 (Blurry Spec ×2, Impact6222, Smaller impact, Basic Hit, Impact30, Arrow Impact), OffCentered Spec 35 ×2, Magic Symbols 50 |
| Arcane orb/floor/loops | all 1 (the loops are Rate-driven; `Emit(1)` seeds the first particle); Floor Noise Smoke 4 |
| Astral `TargetCircle/Impact` | Spec19 1, Impact37 2/1, Impact432 2, **Star102 17 ×3 + 15, Spec25 25 ×2, Spec27 25 ×2**, Fancy Smoke 19 ×2 and **70**, Constellation 17 ×2, Crescent 10 ×2, Ground15 1, Rainbow5 2, Rainbow6 1, Impact156 1 |
| Elemental gun spawn (Core/Body/Handle) | all 2 (glow pulses), Body Star102 15 ×3 (sparks) ; IceGun Body Star119 **45** ×2 |
| Elemental `Tip` muzzle (fire) | Spec19 1, Impact31 1 ×2, Noisy Line Spec 15 ×4, Spec25 20 ×2, Fireflies 15 ×2, Smoke 10 ×2, Shard 10 ×2, Crescent 6 ×2, Slash 3 |
| Elemental fire bullet idle burst | 5 per layer (15 layers) |
| Elemental fire impact | flashes 1 (Spec19, Impact13 ×2, Impact452 ×2, Flare ×2), Flame Wisp 15 ×2, Fireflies 15 ×2, Smoke 15 ×2, Spec25 15 ×2, Ground15 2 ×2 |
| Elemental ice impact | flashes 1; Other45 15 ×2, Snowflake 10 ×2, Fireflies 15 ×2, Smoke 20 ×2, Smoke Hole 20 ×2, Spec24 15 ×2, Ground15 2 ×2 |
| Wet `Impact` | Spec19 1, Impact28 3, Impact13 3, Water 3, Wavey 1, Water12 4 ×2, **Water10 20 ×2, Spec25 25 ×4, Spec24 25 ×2, Water41 10 ×2, Smoke33 10 ×2, Smoke40 12** , Water12 3, Flare 1, Rainbow6 1 |
| FUGAAAA | Dots 15, ParticleEmitter 7/10, Star 1, smoke 7/3/12/12/7/4, Fire1 25 ×2, DarkSmoke1 5 ×2, "15" 15 ×2, "2" 5, "yes" 10 ×4 (all EmitDelay 0) |

Reading [inference]: spark emitters carry the count (25-70 per layer, 2 Brightness copies each = 50-140 sparks per impact); flashes are exactly one particle so they appear as a single hard frame; with ~10 spark layers a Wet impact is ~250-300 particles and an Arcane arrival ~230. Peak lifetimes 0.4-1.8 s, so this is 1-2 hundred live particles for under 2 s, not a sustained load.

## 11. Could not decode / limits

- **EmitCount / EmitDelay**: resolved in section 12 (source `output/vfx/training-dumps/attributes/sTier__*.txt`, coordinator update). Still undecoded: contents of Configuration "VFX Settings" beyond colour attributes, the Arcane `Size_Curve`-type attributes were not present in the S-tier files.
- **Size sequences longer than ~6 keypoints are truncated** in the dump ("..."); I can only see the first 3-6 keys (e.g. impact flash `0:21.29, .1:24.23, .2:26.54...`). Peak sizes of eased growth (the last key) are unknown for ~60 impact layers. Peak-at-X% values only exist where Size has ≤7 keys.
- Lighting/PostProcessing properties (Bloom Intensity/Threshold, ColorCorrection, DepthOfField, SunRays, Atmosphere density) not decoded beyond Bloom Size 24 and Atmosphere Color.
- Baked animation timing (FUGAAAA 641 keyframes) and `Configuration "⚙️ VFX Settings"` contents not decoded; `Cartoon` explosion asset and Server/`Ei` modules for Wet not in dump.
- Sounds referenced (`Squirt Whoosh`, `Squirt Impact`, `PlaySFX`) are not in this teardown.
- Part Transparency/Material for MeshParts is decoded only partly; Textures (Face, StudsPerTile) are decal-like surface patterns.
- Nothing was viewed in motion; every "looks" claim is an inference from numbers.

## 13. Seen in motion (2026-10-16)

Source: `output/vfx/training-captures/` (Studio screen recordings ~30 fps) — viewed `overview_sTier.jpg` and the 12-frame `sheet.jpg` of Elemental_Guns_E_follow, Astral_Sword_E, Mildly_wet_projectiles_E, Purple_arcane_showcase_E, Missile_Sequence_Q. Sheet cells are evenly spaced, so cell time = clip length / 12 (Elemental follow 2.97 s ≈ 270 ms/cell; Astral 4.97 s ≈ 415; Wet 3.47 s ≈ 315; Arcane 9.98 s ≈ 830; Missile Q 6.97 s ≈ 580). Durations below are therefore ±1 cell, not frame-exact; I did not open individual frames.

| Effect | Frame-by-frame (what is visible) | Durations (±1 cell) |
| --- | --- | --- |
| Elemental follow (fire + ice shot, chase cam) | cells 1-5: tiny guns glowing at the caster, then both guns fade out; cell 6: **full-screen white-blue flash** with star sparkles and big snowflake sprites; cells 7-12: orange-yellow bright disc with a cross flare, a long chunky flame-sprite tail behind it; the ice bullet beside it is a big white snowflake sprite with a bright star centre, thin arc rings and a snowflake stream | hold ~1.3 s, flash cell ~270 ms, travel visible ~1.6 s |
| Astral Sword | cell 1: thin sword hanging high, ground already tinted blue (telegraph glow); cell 2: runic circle drawn on the floor, sword still above; cell 3: **spiky blue burst + bright white-blue ground ring**; cell 4-7: glowing dome of blue flame/smoke over the ring that slowly dissolves, wispy ground smoke around the rim, circle fades back to the faint rune; cell 5 and 9-12: the whole scene darkens (sky goes dark) while the effect glows | telegraph ~0.8 s, spike burst ~400 ms, dome linger ~2 s, ring ~2.5 s; darkening lasts across later casts |
| Mildly wet (4 water bolts) | cells 1-2: faint blue patch on ground; cell 3-4: small spray of droplets climbing in an arc; cell 5: **bright white-blue splash dome** on the target; cells 6-8: dome shrinks/dims; cells 9-12: faint mist then nothing | spray ~600 ms, splash peak one cell (~300 ms), fade ~1 s, clean at ~3 s |
| Purple arcane | cell 1-3: orb on a violet pedestal, curved particle comet leaves it (yellow head, violet tail) and flies in an arc to the far orb; cell 4: arc at peak; cells 5-10: far orb sits on a violet sigil disc with a hanging "curtain" of vertical streaks; yellow+violet wisps orbit above and trail in curves; cell 11: **white 4-point starburst flash + warm sky tint**; cell 12: all gone, a few violet motes | arc ~0.8-1 s, orbit phase ~5 s, finale one cell (~800 ms incl. tint), fully clean ~9 s |
| Missile Q | cell 1: thin curved white-blue ribbon trail behind a dark ball; 2: blue glowing sphere with a white **star decal** and a thick ribbon; 3-4: ribbons with small diamond sparks, spark cloud around the target ball; 5-6: next missile ribbon; 7: flat **star-shaped plate** with a rim glow on the ground, then 8-12 the plate with downward vertical streaks and a ring that lingers | missiles ~600 ms apart, star plate stays 3+ s |
| Missile E | not viewed (INDEX says almost nothing visible) | UNSEEN |
| FUGAAAA | overview only: a looping fire/smoke ball (side + front). The arrow animation is not replayed | UNSEEN |

Claims from sections 2-4, checked:
- CONFIRMED: layered impact over several timescales (flash cell, shape burst, dome/ring/mist linger 1-3 s); ground-flat rings and floor sigils (Astral, Arcane, Missile); curved ribbon trails behind the missile; hot-to-cool colour (yellow head to violet tail) in Arcane; clean disappearance with no stuck particles; screen tint/flash on big hits (Elemental white flash, Arcane warm tint).
- WRONG / refined: "no S-tier effect has a lone sphere" — the Elemental fire head IS a bright round disc and the Missile head is a round glowing ball. What is true: the disc always carries a cross flare / star decal and a long tail, so it never reads as a bare sphere. Also "dark scene around effect" is not authored by the effect: Astral's scene darkening comes from the showcase lighting, not from particles [inference].
- UNSEEN: 40 ms flash layers (below one frame at 30 fps, only the afterglow is visible), triple-Brightness stacks (can't separate layers in a video), FOV/blur punches (no obvious zoom in the sheets), shake, light range growth, FUGAAAA cones, Missile E.

Five visual qualities that make S tier look S tier (copyable):
1. **Shape language: every glow has a spike, a ring or a streak.** Flare cross on the fireball disc, star decal on the missile, spiky burst at the sword hit, vertical streak "curtain" under the arcane sigil, snowflake sprites on the ice bullet. Nothing is a plain soft circle.
2. **Value contrast: one tiny near-white core inside a saturated body.** White-blue flash in cell 6 / splash dome / starburst is brighter than everything else for exactly one cell, then drops to saturated mid-value; the sky/scene is darker or desaturated behind it.
3. **Colour: 1 hue plus a hot accent, never rainbow.** Blue family only (Astral, Wet, Missile), orange+ice-blue pair (Elemental), yellow head fading to violet (Arcane). Near-white for the peak.
4. **Timing: short peak, long soft tail.** Peak lasts about one 270-800 ms cell; the aftermath (dome, ring, mist, plate) lingers 1-3 s and fades smoothly; a ground telegraph shows ~0.8 s before the Astral hit.
5. **Scale: effects are several times bigger than the object.** The splash/dome/ring is 3-6x the caster in frame, trails are many body-lengths long, ground sigils are wider than the target; small things (sparks, snowflakes) are scattered at several sizes around the main shape.

Limits: not frame-by-frame (sheets only, ±1 cell), nothing measured for brightness or size in studs, single viewpoint, showcase lighting differs per file.
