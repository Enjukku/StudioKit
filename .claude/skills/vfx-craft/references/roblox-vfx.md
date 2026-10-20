> Author: skill-builder · claude-opus-5-5 · low · 2026-10-13

# Roblox VFX toolset: instances, ranges, cost, tiers, budgets

Lookup for effect cards. Every property name and range was re-read in the local docs mirror
(`knowledge/external/roblox-creator-docs/`, 2026-10-12/13); engine facts change, so re-check at each milestone.
Evidence rows: `07 RT` = 07 Roblox table (Output 7), `07 PM` = 07 Performance and mobile (Part 10), `07 C-n` / `O-n`
= its Conflicts / Open rows, `X-nn` / `PD-nn` = `contradictions.md`. Provenance: [spec] Roblox docs or a standard,
[practice] shipped-game or vendor practice, [study], [inference] arithmetic or reasoning, [P] PROPOSAL start value
(untested, owner may change). A (P) number is never evidence; "no number found" stays empty, never filled.

## A. Instance lookup (key properties, documented ranges)

### A1. ParticleEmitter (R-209, R-211; 07 RT)

| Property | Values / range [spec] | Card note |
| --- | --- | --- |
| Parent | BasePart (spawn in box or Shape) or Attachment (spawn at point) | Use an Attachment at the contact point; Sphere/Cylinder Shape misbehave on an Attachment parent |
| Shape / ShapeStyle / ShapeInOut / ShapePartial | Box, Sphere, Cylinder, Disc / Volume, Surface / Outward, Inward, InAndOut / radius or angle factor | Disc + Surface for ground rings |
| EmissionDirection | NormalId; on an Attachment rotate the Attachment instead | |
| Orientation | FacingCamera (default), FacingCameraWorldUp, VelocityParallel, VelocityPerpendicular | VelocityParallel for streak sparks [inference] |
| Rate | particles/s while Enabled; change does not touch live particles | Cap 400/s, 100/s on mobile |
| Lifetime | NumberRange s, 0-20 (above 20 capped); 0 = no emission | Live count ≈ Rate x mean Lifetime [inference] |
| Emit(n) / Clear() | burst n (default 16) / remove all live | No burst cap documented |
| Speed | NumberRange studs/s; negative reverses | |
| SpreadAngle | Vector2 degrees | |
| Drag | s to lose half the speed; negative grows | WindAffectsDrag needs Drag > 0 |
| Acceleration | Vector3 studs/s² | |
| Rotation / RotSpeed | degrees / deg/s (NumberRange) | |
| LockedToPart / VelocityInheritance | bool / 0 none to 1 full parent velocity | |
| Size | NumberSequence, world studs of the square texture | Fill-rate lever |
| Transparency | NumberSequence 0 opaque to 1 not rendered | Fade start and end to avoid popping |
| Color | ColorSequence tint | Greyscale texture + Color = one asset, many looks |
| Squash | NumberSequence; > 0 narrow and tall, < 0 wide and flat | |
| Sequences | 2-20 keypoints, first at t 0, last at t 1, non-descending | |
| LightEmission | 0 normal blend to 1 additive; applies to live particles | Does not light the world |
| LightInfluence | 0-1 (outside undefined); 0 self-lit, 1 black in darkness. Default 1 from Studio insert, 0 from `Instance.new()` | Always set explicitly |
| Brightness | float, scales emitted light when LightInfluence 0; no range stated | |
| ZOffset | studs toward camera, fractional; screen size unchanged | Render order only |
| TimeScale | 0-1 (0 frozen, no value > 1) | Cleanup timers must allow for frozen emitters |
| FlipbookLayout | None, Grid2x2 (4), Grid4x4 (16), Grid8x8 (64), Custom (FlipbookSizeX cols, FlipbookSizeY rows) | Cell px = 1024 / grid: 512, 256, 128 [inference] |
| FlipbookMode | Loop, OneShot, PingPong, Random | OneShot: one pass over Lifetime, Framerate ignored |
| FlipbookFramerate | NumberRange, max 30 fps (Loop, PingPong, Random) | |
| FlipbookStartRandom / FlipbookBlendFrames | bool / bool (linear crossfade) | |
| LocalTransparencyModifier | client-only, not replicated; shown T = 1-(1-T)(1-LTM); Hidden on ParticleEmitter | Per-viewer toning |
| Texture | .png with transparent background works best | See D |

### A2. Other instances

| Instance | Key properties and ranges [spec] | Cost and limits | Evidence |
| --- | --- | --- | --- |
| Beam | Attachment0/1; CurveSize0/1 (Bezier); Width0/1 studs; Segments int default 10, needs ≥ n-1 for n Color/Transparency keypoints; TextureMode Wrap/Static/Stretch + TextureLength; TextureSpeed cycles/s default 1, negative reverses; FaceCamera; LightEmission 0-1; LightInfluence 0-1; Brightness 0-10000 default 1; ZOffset; no Texture = solid line | Each segment = 2 triangles; one draw call per beam [practice, single C]; streams textures | R-177, R-178, R-351; 07 RT |
| Trail | Attachment0/1 sampled every frame; Lifetime 0.01-20 s default 2; MinLength, MaxLength (0 = none); WidthScale 0-1 x attachment gap; TextureMode Wrap/Static/Stretch; FaceCamera; LightEmission, LightInfluence, Brightness as Beam; Color repaints old segments; Clear() | QualityLevel scales trail fidelity; not texture-streamed; changing an attachment wipes segments | R-236, R-221; 07 RT, C-10 |
| Attachment | CFrame, Position, Orientation, Axis (1,0,0), SecondaryAxis (0,1,0), WorldCFrame; Visible debug | Valid parent for emitters and lights; no count limit found | R-175, R-229 |
| Highlight | Adornee; DepthMode AlwaysOnTop / Occluded; FillColor, FillTransparency 0-1 (default 0); OutlineColor, OutlineTransparency 0-1; Enabled | 255 per client, extras silently ignored, disabled ones hold a slot; first on screen up to 1 ms GPU on mobile; cost grows with coverage; add/remove = geometry rebuild + spike | R-195, R-196; 07 C-14 |
| PointLight | Brightness (default 1), Color, Range (clamped 120 studs), Shadows, Enabled; direct child of BasePart or Attachment | Shadow-casting lights costly; no per-light ms, no count cap found; may not render far from Camera.Focus | R-218, R-203; 07 C-12 |
| SpotLight / SurfaceLight | Angle (Spot max 180; Surface 0 straight out to 180 parallel), Face, Range ≤120 | As PointLight; SurfaceLight on an Attachment acts as SpotLight | R-226, R-229, R-202 |
| Lighting | Technology deprecated, Studio-only (Voxel, ShadowMap, Future); use LightingStyle Realistic/Soft + PrioritizeLightingQuality; ExposureCompensation -5..5 (1 = 2x exposure); ShadowSoftness default 0.2 | Shadows degrade with quality, off below level 4; Future costliest [practice, single C] | R-203, R-457, R-375; 07 C-11 |
| Atmosphere | Density, Offset, Color, Decay (needs Haze, Glare > 0), Glare (needs Haze > 0), Haze; ranges not stated | No cost number found | R-173, R-174 |
| BloomEffect | Intensity (no range stated), Size px (0 = no bleed), Threshold (1 only white, 0 all); stacks; Lighting = all, Camera = one player | Full-screen pass, cost not stated | R-180, R-219 |
| ColorCorrectionEffect | Brightness -1..1, Contrast, Saturation (-1 grey), TintColor (multiplicative); stacks; Lighting or Camera | Full-screen; not on GuiObjects | R-184 |
| DepthOfFieldEffect | FocusDistance, InFocusRadius, NearIntensity, FarIntensity (no ranges stated) | May differ on low-end; hides threats | R-190 |
| SunRaysEffect | Intensity, Spread 0-1 | May not render on low-end; sun only | R-228 |
| BlurEffect | Size px Gaussian; one applies (largest) | Not radial or motion blur | R-181 |
| ColorGradingEffect | TonemapperPreset Default / Retro; Lighting parent only, latest wins | Not a per-player tint | R-185; 07 C-13 |
| Decal / Texture | Transparency 0-1, Color3 tint (true only on white image); Decal ZIndex, UVOffset, UVScale, Rotation; Texture StudsPerTileU/V, OffsetStudsU/V; LocalTransparencyModifier | Batch poorly, add draw calls; texture-streamed | R-452, R-462, R-200 |
| Camera | CFrame (no shake property); FieldOfView 1-120 default 70; `BindToRenderStep(name, RenderPriority.Camera.Value + 1, fn)` runs after default camera (Camera = 200) | Values live in the camera reference | R-182, R-187, R-459; 07 C-15 |
| Accessibility hooks | `GuiService.ReducedMotionEnabled`; `GuiService.PreferredTransparency` 0-1 | Docs scope UI tweens; camera use = inference | R-455, R-450 |

**Not native (R-211, R-219, R-220):** chromatic aberration, radial/motion blur, refraction, soft-particle depth fade,
per-cell frame hold, ParticleEmitter UV scroll or flip, particle collision, noise, sub-emitters. Fake with overlays,
meshes, timed stages or baked sheet variants (repeat cells for holds); never call BlurEffect radial blur.

## B. Tunables

| Parameter | Default | Range | Move up when | Move down when | Hard cap | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| Continuous emitter live particles (phone) | ≤40 live, e.g. 20/s x ≤2 s [P] | ambient: lower Rate, longer Lifetime (motes ≤5/s, 6-10 s) [P] | look thin at gameplay distance and GPU ms has room | RenderGPUFrameTime over budget; overlap | 100/s mobile, 400/s, Lifetime 20 s [spec] | R-209, R-248; PD-20, 07 P01 |
| Primary burst Emit count | High 12-20, Low 4-8 per emitter [P] | 3-10 per effect under heavy concurrency [practice] | burst unreadable on a phone | many simultaneous blasts | no burst cap documented | R-248, R-385, R-375; 07 P02 |
| Flipbook grid | Grid4x4 hero blasts, Grid8x8 small or fast [P] | 2x2 / 4x4 / 8x8 / Custom | stepping visible | blur at 10-30 studs | sheet 1024x1024 [spec] | R-214, R-200; 07 P03, X-50 |
| FlipbookFramerate (Loop) | 15 fps [P] | 7.5-30; smooth smoke 24-30 [P] | smoke looks choppy | stylised held drawings wanted | 30 fps [spec]; OneShot frames / Lifetime ≤30 [P] | R-211; PD-15, X-42 |
| LightInfluence | 0 emissive (flash, fire, sparks); 1 dust, smoke, debris [P] | 0-1 | layer floats unlit on a dark stage | glows when it should sit in scene light | 0-1 [spec] | R-211; 07 P04 |
| ZOffset by layer | flash +1, sparks +0.5, smoke 0, ground dust -0.5 studs [P] | studs | layer hidden behind neighbour | layer pokes in front wrongly | very negative draws inside parent [spec] | R-211; 07 P05 |
| Keypoints per curve | 3-5 (fade in, hold, fade out) [P] | 2-20 | visible popping in 30 fps capture | — | 20 [spec] | R-206, R-209; 07 P06 |
| Beam Segments | max(n-1, 1) straight; 10 curved [P] | int | curve looks angular | straight beam | ≥ n-1 [spec] | R-177; 07 P08 |
| Trail Lifetime (streaks) | 0.15-0.3 s [P] | 0.01-20 s | direction unreadable | streak lingers and misleads | 20 s [spec] | R-236; 07 P09 |
| Blast PointLight | Range 2-3x fireball radius, Shadows false, hold 2 frames, fade ≤0.3 s [P] | Range ≤120 | blast does not light blocks on darkest stage | GPU ms over budget | Range 120 [spec]; ≤4 transient per client [P] | R-200, R-203, R-344; PD-21, 07 P11 |
| Bloom Threshold | ≥0.9, Intensity never pulsed [P] | 0-1 | sky or UI blooms | effect cores fail to glow | pulse = flash (safety) | R-180; 07 P12 |
| ColorCorrection pulse | ≤2/s, never saturated red full-screen [P] | — | — | any flash-analyser fail | 3 flashes/s [spec] | R-165, R-167; 07 P13 |
| Others' effects LocalTransparencyModifier | Reduced 0.5; Essential 1 on secondary layers; own and threats 0 [P] | 0-1; test 0/0.3/0.6/1 | own threats hard to spot | others' actions unreadable | no shipped % found | R-028, R-008; PD-08, 07 P07 |
| Live Highlights per client | ≤20, small objects [P] | test 10/20/50 | — | GPU ms with coverage | 255 [spec] | R-196; PD-09 |
| Live scorch decals per client | ≤30, persist until regeneration, oldest fades first [P] | — | aftermath reads empty | draw calls over budget | — | R-200; PD-18, 07 P14 |
| Static particle texture | 256 (sparks, chips, motes), 512 (smoke, big glows) [P] | ≤512 unless large on screen; minor <256 [spec] | blur at gameplay distance | memory pressure on 2 GB phone | upload 4096 [spec] | R-200, R-332, R-233; 07 P18, X-52 |
| Unique flipbook sheets resident per stage | ≤8 (≈32 MiB uncompressed) [P] | — | — | flipbooks auto-deactivate on low memory | no number found | R-209, R-036; 07 P21 |
| Distance cull | secondary layers off >150 studs, whole cosmetic effect >400 [P]; gameplay cues never culled | engine mesh LOD 250/500 [spec] | far blasts look bare | far blasts cost frame time | — | R-458, R-204; 07 P22 |
| VFX draw calls at worst blast (phone) | ≤60 of a 500 scene target [P] | docs example <1,000 [spec]; community 500 [practice, single C] | — | Render Stats over target | — | R-191, R-351; X-76, 07 P19 |
| VFX GPU time at worst blast | ≤4 ms RenderGPUFrameTime over no-effect baseline [P] | frame 16.67 ms at 60 FPS [spec] | — | over on baseline Android | — | R-217, R-196; 07 P20 |

## C. Rules

| ID | Rule | Evidence |
| --- | --- | --- |
| RB-01 | One Attachment per contact point, axis on the surface normal, shared by every layer of the effect; rotate it, do not set EmissionDirection. | R-209, R-175; 07 RT [spec + inference] |
| RB-02 | Never use Sphere or Cylinder Shape on an Attachment-parented emitter; parent to a Part or use Box/Disc. | R-209 [spec] |
| RB-03 | Bursts use `Emit(n)` on a persistent emitter (Rate 0 or Enabled false); continuous looks use Rate. Never set Rate above 100 for phone content. | R-209, R-211 [spec]; R-467 [inference] |
| RB-04 | Card states Rate x mean Lifetime as the expected live count; it must fit the B budgets. | R-209 [inference] |
| RB-05 | Set LightInfluence explicitly on every emitter, Beam and Trail (Studio default 1, `Instance.new()` default 0). | R-211 [spec] |
| RB-06 | LightEmission 1 only for glow, sparks, fire core; 0 for smoke and dust so dark values survive. Need world light → PointLight. | R-211 [spec + inference] |
| RB-07 | Fade Transparency at the start and/or end of every particle; 3-5 keypoints; never more than 20. | R-209, R-206 [spec]; 07 P06 [P] |
| RB-08 | Flipbook sheets are exactly 1024x1024 with a layout that divides it; no 2048; 512 or non-square only after O-1 shows Compatible on a phone. | R-214, R-211; X-50, X-51 [spec] |
| RB-09 | Blasts and impacts use FlipbookMode OneShot (drawing spans Lifetime); keep frames / Lifetime ≤ 30/s. Never PingPong an expanding explosion. | R-213, R-211 [spec]; X-42 [P] |
| RB-10 | Variable holds are baked as repeated cells; there is no per-cell hold property. | R-211 [spec] |
| RB-11 | Static particle textures: one greyscale .png with transparent background, tinted by Color/ColorSequence; reuse the asset id, never upload the same image twice. | R-209, R-200, R-122 [spec + practice] |
| RB-12 | Texture memory follows pixel count (1024² = 4x 512²); compression or dropped alpha does not save memory. Choose size by on-screen size. | R-200 [spec] |
| RB-13 | Avoid atlases unless they serve batchable parts: one high-res region streams the whole atlas. | R-234 [spec] |
| RB-14 | Cosmetic effects (particles, beams, trails, lights, post effects, shake) are built and played on each client from a replicated gameplay event; the server owns only the event and its outcome. | R-211 (LTM client-only), R-180 (Camera parent = one player) [inference] |
| RB-15 | Per-player screen effects (ColorCorrection, Bloom, Blur, DoF) go under `workspace.CurrentCamera`; Lighting parent affects every player. ColorGradingEffect is Lighting-only. | R-180, R-185, R-219 [spec] |
| RB-16 | Pool, do not clone-and-destroy per hit: persistent template emitters, Highlights created once and toggled by property. Pool other instances only if profiling shows a gain (O-12). | R-196 [spec]; R-467 [inference] |
| RB-17 | Before reusing a pooled instance: Clear() particles and trails, reset Enabled, TimeScale, transforms, colours, sequences, lights; never reuse one still playing. | R-467, R-236 [inference] |
| RB-18 | Avoid per-frame property changes on ParticleEmitters; animate with sequences, Emit and TimeScale. | R-200 (improve.md:343-344) [spec] |
| RB-19 | Read `UserGameSettings.SavedQualityLevel` (live engine level is not script-readable). Tiers: Low 1-3, Mid 4-7 and Automatic, High 8-10. | R-239, R-460 [spec]; 07 P17 [P] |
| RB-20 | Scale Emit counts yourself per tier: the engine may not reduce Emit bursts (X-77 open). | R-375 [practice, single C]; O-3 |
| RB-21 | Every effect is reviewed at the lowest and highest Editor Quality Level; essential meaning (danger footprint, source, onset) survives Low and Automatic. | R-209 (:42), R-221 [spec] |
| RB-22 | Gameplay-critical cues never depend on Highlight AlwaysOnTop leaking through walls, on SunRays, DoF, Bloom or shadows (they vanish at low quality). | R-200, R-219, R-228 [spec + inference] |
| RB-23 | Blast lights: Shadows false, Range inside 120, one per large blast, ≤4 transient per client. Never shadow-casting lights for transient VFX. | R-200, R-203 [spec]; PD-21 [P] |
| RB-24 | DepthOfField and Blur only in menus and reveals, never in active danger on phones until O-10 measures them. | R-190, R-181 [spec + inference] |
| RB-25 | Other players' non-threat effects are toned with LocalTransparencyModifier and send no shake, flash or post effect; own effects and threats stay at 0. | R-028, R-211; PD-08 [P] |
| RB-26 | Honour `GuiService.ReducedMotionEnabled`: shake 0%, no FOV kick; re-read on change. | R-455 [spec]; extension to camera [inference] |
| RB-27 | Bloom Intensity and ColorCorrection Brightness/TintColor pulses count as whole-screen flashes; they pass the flash governor (≤3/s, design 2/s). | R-167, R-180, R-184; PD-11 [P] |
| RB-28 | Every effect card names its tier budget line (D) and passes it before review; numbers outside B need a measurement. | 07 PM [inference] |
| RB-29 | Cut cost in the order of E; never shrink the meaningful silhouette before removing secondary layers. | R-467, R-200, R-385 [inference + spec] |
| RB-30 | Measure, do not guess: RenderGPUFrameTime, Render Stats (Shift+F2 "Draw (scene)"), MicroProfiler on device, F9 Memory, 10-15 min sessions for throttling. Emulator memory is not accurate. | R-461, R-200, R-231 [spec] |

## D. Effect budget per quality tier (all [P] unless marked; PD-10, 07 P17/P23)

| Item | Low (1-3) | Mid (4-7, Automatic) | High (8-10) |
| --- | --- | --- | --- |
| Hero blast | truth + flash + impact shape + ring + ground mark (drop decoration) | No separate value found: start at High, tune by O-2 | type recipe (pro-defaults.md §B), live ≤~1000, shared textures (v2) |
| Normal hit | ≤4 channels; secondary layers dropped | ≤4 channels | ≤4 channels |
| Emit per primary emitter | 4-8 (High halved) | 12-20 until measured | 12-20 |
| Live particles per blast | ≤60 | ≤150 until measured | ≤150 |
| Full-detail blasts at once | ≤4; extras play primary layer only | same | same |
| Continuous emitter | ≤40 live; secondary ambient off | ≤40 live | ≤40 live |
| Transient lights / Highlights / scorch decals per client | ≤4 / ≤20 / ≤30 | same | same |
| VFX draw calls at worst blast | ≤60 | ≤60 | ≤60 (4 blasts x 5 emitters + 4 lights + 30 decals = 54, ~6 left) |
| VFX GPU over baseline | ≤4 ms | ≤4 ms | ≤4 ms |
| Post effects in play | none pulsed; Bloom only if measured | Bloom Threshold ≥0.9 | Bloom Threshold ≥0.9 |
| Engine (not ours) [spec] | shadows off below level 4; some post effects off; fewer particles rendered | — | more particles, trail fidelity, post quality |

Shipped reference: mobile game cut impact 30 → 2, 10 impacts 300 → 20, smoke + sparks 200 → 50 with fewer, larger
particles [practice, R-248]. Epic halves overdraw-heavy emitters at Medium and below [spec, R-204].

## E. Keep the look, cut the cost (order; R-467, R-200, R-385, R-114, R-122)

1. Keep the danger footprint, source/target identity and onset frame. Never cut these.
2. Remove offscreen, far (>150 studs) and irrelevant cosmetic layers.
3. Thin broad overlapping smoke and glow and long low-information tails; cost = count x covered pixels x layers
   (X-83). Fewer, larger particles with detail baked into the texture beat many small ones.
4. Reuse asset ids and one greyscale texture tinted per use; fewer unique flipbooks (the lever is unique-sheet count).
5. Simplify distant effects; a flipbook explosion can read with 1-2 key frames [practice, single C].
6. Replace per-frame property scripts with sequences, Emit and TimeScale.
7. Reprofile after each change; stop when the B/D line passes.

## F. Overdraw and cost facts

| Fact | Number | Evidence |
| --- | --- | --- |
| Transparent overdraw is the main particle GPU cost | no layer count given | R-209, R-200 [spec] |
| Overdraw tool scale (Arm) | 10 draws/pixel = definitely too much; 2.44-2.48 already "quite high" | R-132 [practice, 2015] |
| Draw calls | each emitter and each beam = 1 call (40 emitters = 40) | R-351 [practice, single C] |
| Low-end phone | Android <2 GB RAM; OOM a top crash cause; Android ≈65% of players | R-036, R-231 [practice/spec] |
| Texture memory (RGBA8 arithmetic, not measured) | 256 = 0.25, 512 = 1, 1024 = 4, 2048 = 16 MiB; mips x4/3 | R-200 [inference] |
| Debris service | MaxItems hard-coded 1,000, oldest destroyed first | R-446 [internal] |
| Client Luau on phones | assumed interpreted; per-frame VFX scripts may cost more | R-449 [internal, unconfirmed] |

## G. Open (test before trusting a number)

| ID | Question | Test |
| --- | --- | --- |
| O-1 | Do 512, 2048, non-square or Custom sheets play? | Upload each, read flipbook compatibility state in Studio and on a phone |
| O-2 | Particles rendered per SavedQualityLevel | 400/s emitter, count live at Editor Quality 1-10 and on phone |
| O-3 | Does Emit obey the 100/s mobile cap and quality reduction? | Emit(200) at quality 1 and 10 on a phone |
| O-4 | Overdraw ms on target phones | Stack 1/2/4/8/16 emitters on one area; RenderGPUFrameTime |
| O-9 / O-10 | Cost of lights and post effects on phones | Toggle each; RenderGPUFrameTime |
| O-12 | Pooling gain | Emit on persistent vs clone/destroy; MicroProfiler |
| O-13 | Unique flipbook memory | F9 Memory with 4/8/16 sheets on 2 GB Android; watch deactivation |
| O-14 | Highlight cost | 1/5/20 Highlights small vs screen-filling |
| O-17 | Are particles occlusion-culled? | Render Stats, emitter behind a wall vs in view |
