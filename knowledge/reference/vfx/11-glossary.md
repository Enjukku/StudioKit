---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: vfx-synthesis (vfx-reference-synthesis workflow) · claude-opus-5-5 · default · 2026-10-12

# VFX reference 11: glossary (Output 11)

**Scope and use.** Every VFX, perception, Roblox and evidence term used in files 00-12 and `contradictions.md`, one line each, in the field's own words. The VFX agent uses it to read the other files the same way every time and to name things in effect cards and review notes.
"source" = the R-id (`00-sources.md`) of a source that defines or names the term; "ChatGPT 11" = the ChatGPT package glossary (`11_glossary.json`, a model's definition, inference); "field" = a common term no read source defines; "project" = a convention of this reference. Engine property names keep their exact Roblox spelling; their facts are spec (local docs mirror).

## Elements and design language

| term | meaning | source |
| --- | --- | --- |
| gameplay (element) | the information and decisions an effect must support: what it is, what it does, how much impact it has | R-368 (three questions); R-118 (heading list); ChatGPT 11 |
| shape (element) | silhouette and arrangement of masses that say what is happening and how to respond | R-358; R-118; ChatGPT 11 |
| value (element) | the light-to-dark structure of an effect, independent of hue; the strongest of value, colour, shape for steering the eye (practitioner claim, tier C) | R-358, R-367; ChatGPT 11 |
| colour (element) | hue and saturation and their relations inside the effect and against the scene | R-120, R-360; ChatGPT 11 |
| timing (element) | how visual change is spread over an effect's life and aligned to gameplay events | R-346; ChatGPT 11 |
| composition (element) | arrangement and hierarchy that direct attention inside an effect and across the scene | R-406 (course outline); ChatGPT 11 |
| readability / clarity | how fast and correctly a viewer reads what an effect is, does and how much it matters; Riot's second goal after gameplay accuracy | R-060, R-080 |
| communication job | the event, its consequence and its size that an effect must tell; first field of the effect card | R-368; project (06 Output 8) |
| importance rating | Riot's 1-10 score per spell, rated separately for the player, allies and enemies; scale single-sourced, no mapping to parameters | R-368 |
| visual hierarchy | ordering of on-screen effects so that attention taken matches gameplay importance | R-080, R-368 |
| attention factors | Riot's four inputs to importance: damage, hard/long crowd control, dodgeability, impact on play | R-080 |
| truthful indicator | a drawn danger or range edge that equals the real gameplay area, on every skin and setting | R-060, R-080 |
| hitbox | the gameplay geometry that decides contact or damage; its indicator must show it truthfully | R-060; ChatGPT 11 |
| telegraph | a cue that announces an attack or hazard before it activates; its area and timing must match the real hit | R-080, R-320; ChatGPT 11 |
| danger zone | a lasting hazard area with a stable perimeter that says "this hurts now" and when it ends | project (02a) |
| per-viewer visibility | showing a range or cue only to viewers who can act on it | R-368 (Morgana example), R-049 |
| Spell Density | WoW 11.2 setting (Everything / Reduced / Essential) that tones down only other party and raid members' visuals | R-028 |
| skin parity | every cosmetic variant keeps the base ability's primary silhouette and indicator size | R-080, R-060 |
| style guide | a written rule set that keeps a growing roster's effects consistent | R-120, R-355 |
| one dominant colour | a palette rule: one hue leads, at most one secondary, competitors desaturated | R-120, R-374 |
| area of focus | the part of an effect that carries the message: highest and lowest value, highest saturation, most detail | R-367 |
| areas of rest | calm, low-detail regions around the focus; negative space | R-367, R-003 |
| primary shape | the dominant mass or gesture that carries the effect's meaning (missile head = damage) | R-367; ChatGPT 11 |
| secondary element | a supporting part (trail, sparks) that strengthens the primary without competing with it | R-367; ChatGPT 11 |
| tertiary detail | fine ornament; first to cut for clarity or performance | ChatGPT 11 |
| silhouette | the recognisable outer shape, readable without texture or colour | R-080, R-327; ChatGPT 11 |
| line of action | the dominant directional gesture of a motion or effect; no VFX-specific rule found (01 shape table) | ChatGPT 11; field |
| breakup | fragmenting a solid shape or texture into irregular pieces, often over life | R-344, R-338; ChatGPT 11 |
| erosion | progressive removal of a shape through a mask instead of uniform transparency | R-338; ChatGPT 11 |
| dissolve | spatially varying disappearance driven by a pattern or threshold | ChatGPT 11; R-338 |
| scalloping | sculpting soft volumes into hard-edged graphic shapes (also written "scalping" in a source) | R-271, R-277, R-058 |
| two-tone smoke | smoke split into a dark base and a hot or light layer with few value steps | R-286 |
| gradient crunching | tight gradients in highlights and pop zones, fuller gradients in darks | R-355 |
| hard light/dark split | cel-style lighting where a surface is lit or unlit with nothing between | R-131 |
| textured glow | a painted or textured halo instead of a soft Gaussian bloom blob | R-277 |
| hue convention | learned colour meaning (heal green, frost blue, gunpowder orange-red); breaking it costs readability | R-360, R-368 |
| team colour | an ally/enemy colour keyed to the viewer's relation to the caster, carried by outlines | R-071, R-104, R-111 |
| category colour | one colour per class of object or ability, never reused as decoration (VALORANT teal for placed utility) | R-033 |
| ColorSequence / colour over life | colour keyframes across each particle's own lifetime | R-211, R-186 |

## Phases, timing and the 12 principles

| term | meaning | source |
| --- | --- | --- |
| windup | the preparation phase before the main action; anticipation | R-346, R-345; ChatGPT 11 |
| anticipation | preparation that makes the following action expected and readable; one of the 12 principles | R-115, R-302; ChatGPT 11 |
| crescendo | the build in intensity right before the punch; gives time to react; an instant effect skips it | R-346 |
| punch | the concentrated high-intensity peak at contact or release (climax, pop) | R-346; ChatGPT 11 |
| follow-through | motion and secondary action that continue after the punch as energy settles | R-115; ChatGPT 11 |
| dissipation | the designed ending in which the effect breaks up or loses prominence | R-310, R-345; ChatGPT 11 |
| W · C · P · F · D | project shorthand for windup, crescendo, punch, follow-through, dissipation (a working vocabulary, not a standard) | project (02a, 02b) |
| 12 animation principles | Disney's principles (squash and stretch, anticipation, staging, arcs, slow in and out, secondary action, follow-through and overlap, timing, exaggeration, solid drawing, appeal, straight ahead / pose to pose) applied to VFX | R-115, R-302 |
| squash and stretch | changing proportion to show force, speed or impact while keeping the sense of volume | R-302, R-131; ChatGPT 11 |
| slow in and slow out | acceleration and deceleration so timing is not uniform | R-355, R-082; ChatGPT 11 |
| arc | a curved motion path that organises motion; perfectly clean arcs can look floaty | R-302; ChatGPT 11 |
| overlap (overlapping action) | parts move or settle at different times instead of as one rigid unit | R-312, R-388; ChatGPT 11 |
| secondary action | supporting motion that adds richness to the main action | R-115 |
| exaggeration | pushing a pose or motion beyond reality; one consistent level per project | R-302, R-131 |
| staggered onsets | layer starts offset by a few frames so the punch reads, then layers unfold | R-388 |
| exit order | sequence in which layers leave: main glow, lens flare, sparks, small bokeh last | R-312 |
| front-loading | the main action finishes or starts to dissipate early in the lifetime (Sparkball: first quarter; single tier C) | R-355 |
| linger | time an effect stays visible after its job is done; length signals importance and blocks later effects | R-360, R-120 |
| clear-by time | project term: time by which a sight-blocking cloud must let a target behind it be read | project (02a, contradictions PD-16) |
| hold | a pose or drawing kept still for several frames | R-131, R-308 |
| limited animation | every frame a key, interpolation off, held poses (Guilty Gear Xrd style) | R-131 |
| on ones / on twos | a new drawing every frame / every second frame of a stated base rate (24 images/s on 1s, 12 on 2s) | R-112; ChatGPT 11 |
| exposure | how many base frames one drawing is held (1s to 6s); the lowest-rate element pops most | R-275, R-267 |
| variable cadence | changing the hold length per element or shot | R-271; ChatGPT 11 |
| stepped cadence | animation that updates in held steps instead of smoothly | R-112, R-381 |
| smear | a drawn stretched frame that carries speed instead of CG motion blur | R-251, R-308 |
| impact frame | a brief abstract, often two-tone insert at a hit; "a fraction of a second", no frame count found | R-404, R-278 |
| frames vs ms | a frame count is a duration only with its stated fps; otherwise "fps not stated" | project (merge rule 6) |
| f@60 | project unit: one frame at 60 fps = 16.7 ms | project (02a) |
| heartbeat rule | motion or pulse faster than a heartbeat reads as danger, slower as safe (Julian Love, second-hand) | R-071, R-346 |
| BPM pace | heal pace under 60 BPM, attacks faster (single tier C) | R-346 |
| ADSR | attack-decay-sustain-release envelope used to shape bullet time and slow motion | R-082 |

## Camera and screen

| term | meaning | source |
| --- | --- | --- |
| screen shake | time-varying camera motion that reinforces an event | R-124; ChatGPT 11 |
| trauma | Eiserloh's 0-1 state that events add to and time decays; shake = trauma² or trauma³ | R-124 |
| Perlin noise shake | smoothed noise per axis instead of per-frame random offsets; works with pause and slow motion | R-124 |
| rotational vs translational shake | in 3D rotate the camera; translating it moves the view through geometry | R-124 |
| directional shake | shake along the cause's direction (vertical knock-down, horizontal slash) | R-073, R-134 |
| camera kick | a short directional camera nudge or rotation at a shot or swing peak, then recovery | R-144, R-151; ChatGPT 11 |
| FOV punch / FOV kick | a brief narrowing or widening of Camera.FieldOfView at a big event | R-128, R-182 |
| hit-stop (hitlag) | a brief freeze of the attacker and target at contact, local to the bodies | R-082, R-156; ChatGPT 11 |
| freeze frame | a global halt of game time for a few frames | R-082; ChatGPT 11 |
| slow motion / bullet time | eased slowdown of time to stretch a key moment; raises perceived intentionality | R-068, R-082 |
| flash frame | a frame or two where the target or screen flashes white to confirm a hit | R-082, R-073 |
| hit flash | the struck character or object briefly flashing; the most common hit cue | R-073 |
| vignette | darkening or tinting of the screen edge | R-337; project (01) |
| chromatic aberration | split colour edges; no Roblox post effect provides it | R-219 (absence) |
| radial / motion blur | blur centred on a point or along motion; Roblox BlurEffect is Gaussian only | R-181 |
| depth of field | blurring outside a focus distance to isolate a subject | R-190 |
| camera control | dedicated framing (zoom in, hold, fast zoom out) toward a key event; a top-3 impact feature in one study | R-073 |
| scale anchor | a player-sized or known object in frame that makes a big event read big | R-263 |

## Juice, feel and reward

| term | meaning | source |
| --- | --- | --- |
| juice | excessive amounts of feedback in relation to the user input (Juul's definition, as quoted) | R-043 |
| game feel | the moment-to-moment sensation of control and response; depends on designed elements and the player's anticipation | R-082, R-047 |
| success-dependent feedback | feedback that fires on the achieved outcome, not on every action | R-043 |
| amplification | a more intense version of the same feedback; harmful when not tied to success | R-043 |
| random variety | random pick among several effects per trigger; small enjoyment gain, no curiosity gain | R-043 |
| competence / effectance / curiosity | player-motive measures in Kao CHI 2024: feeling capable, feeling one's actions cause effects, wanting to explore | R-043 |
| outcome binding | seeing that one's action caused the event (authors' proposed mechanism) | R-043 |
| juiciness levels | Kao 2020 builds: None, Medium, High, Extreme | R-101 |
| sense of agency | the feeling of causing an event; rose with stronger shake (abstract level) | R-004 |
| expectation modulation | designing emotional impact by building, subverting or fulfilling expectation | R-020 |
| haptic juice | vibrotactile embellishment of feedback | R-086 |
| juicy text | onomatopoeia or semantic text effects as feedback | R-045 |
| multimodal stacking | one event felt on several channels (shape, flash, sound, shake, haptic) | R-082, R-110 |
| escalation ladder | a step-by-step increase of layers and length by rarity or tier | project (02b) |
| rarity tell | any hint of the result before the reveal; early tells undercut anticipation | R-316 |
| near-miss | showing an almost-better result; not used (design rule, inference) | project (02b, inference) |
| paid random item | an egg, chest or wheel bought with Robux or Robux-bought currency; odds must be shown before purchase | R-208 |
| pity / luck boost | mechanics that change odds over time or by item; must be explained in numbers | R-208 |
| quick-open | opening up to 25 eggs at once | R-465 |
| count-up | a counter that animates to a new value | R-411, R-414 |
| pending state | visible "waiting" feedback while the server has not confirmed | project (02b G1) |
| toast | a small notification that slides in and out | project (02b U4), R-158 |
| habituation | weaker response to repeated identical stimuli | R-094 |
| closure | the sense that an event finished in a stable state; no study found | project (05 5c) |

## Perception and attention

| term | meaning | source |
| --- | --- | --- |
| salience | how strongly an item attracts attention relative to its surround and goals | R-117, R-149; ChatGPT 11 |
| abrupt onset | a sudden appearance that creates an automatic attention priority unless control settings block it | R-087 |
| motion onset | an object starting to move captures attention; ongoing motion does not; depends on the task | R-146, R-002 |
| looming | motion toward the viewer; a possible attention guide, not reliable alone | R-147, R-117, R-065 |
| guiding attribute | a feature that guides visual search: colour, motion, orientation, size (undoubted) | R-117 |
| pop-out / search slope | near 0 ms per item when a target pops out; about 20-50 ms per item for serial search | R-117 |
| inhibition of return | the tendency not to re-attend a recently attended spot | R-149 |
| suppression | proactive ignoring of a repeated salient colour singleton | R-087 |
| crowding | impaired identification of a target when similar items are near it, mainly in peripheral vision | R-138, R-054; ChatGPT 11 |
| Bouma spacing | critical crowding distance about 0.4-0.5 x eccentricity | R-138 |
| clutter | visual competition that makes relevant information harder to find | R-142; ChatGPT 11 |
| Feature Congestion | an image clutter metric that tracks human clutter ratings and search time | R-142, R-014 |
| capacity limit | about 3-5 meaningful items held at once | R-139 |
| multiple-object tracking | following several moving targets; people track four or more | R-145, R-077 |
| launching (causal perception) | contact followed by a reaction read as cause and effect | R-097 |
| reaction time (simple / choice) | time to respond to one known stimulus (mean 230.8 ms) or to choose among several (727-865 ms in one task) | R-130, R-108 |
| JND | just-noticeable difference, e.g. audio latency 49 ms at base 0 | R-048, R-078 |
| PSS | point of subjective simultaneity between sound and picture | R-078, R-133 |
| sound-lead / sound-lag | sound before / after the picture; R-170 sign: positive = sound early | R-170 |
| lip-sync tolerance | broadcast windows for sound-picture offset (detect +45/-125 ms, accept +90/-185 ms) | R-170, R-169 |
| depth cue | information that shows distance, layering or spatial relations | ChatGPT 11; R-063 |
| colour vision deficiency | reduced colour discrimination, mostly red-green (deutan, protan), about 8% of men | R-148, R-107, R-398 |

## Destruction

| term | meaning | source |
| --- | --- | --- |
| material tag | one material id per piece that drives fracture, emitters, decals and sound together | R-021 |
| apple-core collapse | outer shell breaks first, the core goes last | R-019 |
| stress state | visible degrade, sag, lean or partial attachment before a structure fails; "a moment to react" | R-001, R-019 |
| connection groups | breaking along real connectivity: small sections come apart, others stay together | R-324, R-135 |
| knock-on / chain reaction | falling or breaking pieces break the next ones | R-030, R-001 |
| orphan prop | a floating leftover after its support is destroyed; a bug class | R-031 |
| cosmetic vs gameplay debris | collision-bearing ruins vs visual-only fragments culled per client | R-021, R-127 |
| impostor debris | small rubble drawn as textured sprites with several silhouettes instead of meshes | R-056 |
| four dust kinds | debris, trail, impact and ambient dust | R-137 |
| coarse-to-fine | big moving mass first, then fragments, then fine dust | R-287 |
| brick blur | LEGO Movie's brick-built smear instead of motion blur | R-135 |
| legal bricks | Ninjago rule that effects use only real brick colours and shapes | R-313 |
| decal / scorch | a persistent mark on a surface that stays as history | R-295, R-452 |
| deterministic destruction | the same hit gives the same kind of break anywhere | R-255 |

## Flipbooks, kitbashing and the Roblox VFX parts

| term | meaning | source |
| --- | --- | --- |
| flipbook | a sequence of frames stored in one sheet and played as animation | R-209, R-338; ChatGPT 11 |
| sprite sheet / atlas | one image holding many frames or sprites | ChatGPT 11; R-234 |
| sub-UV | Unreal name for one cell of a flipbook sheet | R-394 |
| cell / tile | one frame of a sheet; on a 1024 sheet 2x2 = 512 px, 4x4 = 256 px, 8x8 = 128 px (arithmetic) | R-212 |
| padding | transparent spacing around each cell so neighbours do not bleed in at distance | R-209 |
| mip / mipmap | lower-resolution copies of a texture used at small projected sizes | R-332; ChatGPT 11 |
| one-shot / OneShot | plays once per event; in Roblox all cells are spread across the particle Lifetime and FlipbookFramerate is ignored | R-213, R-211; ChatGPT 11 |
| loop | repeats; the last-to-first wrap needs design | R-213; ChatGPT 11 |
| loop seam | a visible jump where a loop wraps | R-393 |
| PingPong | plays forward then backward; only for reversible motion | R-213 |
| Random (flipbook mode) | cells in random order with crossfade; suits slow twinkle | R-213, R-209 |
| frame blending | crossfade between cells (FlipbookBlendFrames); ghosts stepped drawings | R-211 |
| motion-vector blending | interpolating cells with motion vectors (Unreal practice); not available in Roblox | R-347, R-394 |
| soft particles / depth fade | fading a sprite where it meets geometry; no Roblox property | R-227 |
| billboard | a flat card turned to the camera or another set direction | ChatGPT 11; R-215 |
| kitbashing | building a new effect from existing parts instead of authoring every part | R-283; ChatGPT 11 |
| block-in | first pass with plain shapes and real timing, before texture and detail | R-115, R-340; ChatGPT 11 |
| blur test / squint test | blur an effect: if a defined shape still reads, the shape language works | R-344 |
| greyscale test | view the effect without colour to check its value structure | R-367; R-184 |
| additive blending | light contributions add, brightening overlaps; in Roblox LightEmission 1 | R-211; ChatGPT 11 |
| alpha / normal blending | foreground composited over background by opacity; LightEmission 0 | R-211; ChatGPT 11 |
| emissive | looks self-lit; in Roblox emission alone does not light the scene | R-211; ChatGPT 11 |
| bloom | a post effect that spreads bright pixels into neighbours; not geometry or a damage edge | R-180; ChatGPT 11 |
| ParticleEmitter | Roblox particle source on a BasePart or Attachment | R-211, R-209 |
| Rate / Emit | particles per second while enabled (cap 400, 100 on mobile) / an instant burst of n particles | R-209, R-211 |
| Lifetime | per-particle life as a NumberRange, capped at 20 s | R-209 |
| LightEmission / LightInfluence | blend (0 normal, 1 additive) / how much scene light affects the particle (0 self-lit, 1 lit) | R-211 |
| Brightness | emitted light scale of a particle when LightInfluence is 0 | R-211 |
| ZOffset | render-depth offset in studs toward the camera; does not move geometry | R-211; ChatGPT 11 |
| TimeScale | per-emitter speed 0-1 (0 frozen); not global game time | R-211; ChatGPT 11 |
| Squash | per-particle stretch over life: >0 narrower and taller, <0 wider and shorter | R-211 |
| Orientation | FacingCamera, FacingCameraWorldUp, VelocityParallel (streaks), VelocityPerpendicular (flat rings) | R-215 |
| ShapeInOut | emission toward (Inward) or away from (Outward) the shape | R-211 |
| SpreadAngle / Drag | cone of emission in degrees / seconds to lose half the speed | R-211, R-189 |
| FlipbookLayout / FlipbookSizeX/Y | Grid2x2, Grid4x4, Grid8x8 or Custom columns x rows | R-212, R-211 |
| FlipbookFramerate | playback rate for Loop, PingPong and Random, max 30 fps | R-211, R-209 |
| FlipbookStartRandom | random start cell per particle; with framerate 0 each particle is one static random cell | R-211 |
| ParticleFlipbookTextureCompatible | engine-set state; NotCompatible disables playback (needs a 1024x1024 texture) | R-214 |
| NumberSequence | keyframed values over life, 2-20 keypoints, linear between them | R-206 |
| LocalTransparencyModifier | client-only extra transparency on emitters, beams, trails, decals; per-viewer toning | R-211, R-452 |
| Attachment | a local reference frame that places emitters, lights and Beam/Trail ends | R-175; ChatGPT 11 |
| Beam | a textured strip between two attachments for paths, tethers and lasers | R-177; ChatGPT 11 |
| Trail | a strip drawn behind a moving attachment pair (Lifetime 0.01-20 s, default 2) | R-236; ChatGPT 11 |
| Highlight | outline and fill on a model; 255 at once per client; DepthMode AlwaysOnTop or Occluded | R-195, R-196 |
| PointLight / SpotLight / SurfaceLight | dynamic lights; Range clamped to 120 studs | R-218, R-226, R-229, R-203 |
| BloomEffect Threshold | 1 = only pure white blooms, 0 = everything blooms | R-180 |
| ColorCorrectionEffect | full-screen brightness, contrast, saturation and tint; per player when parented to the Camera | R-184, R-219 |
| ColorGradingEffect | tonemapper preset; works only under Lighting, latest-parented wins | R-185 |
| Atmosphere | haze and density that hide distant objects | R-173, R-174 |
| ExposureCompensation | Lighting exposure -5 to 5; +1 = twice the exposure | R-203 |
| FieldOfView | camera vertical FOV, default 70°, clamped 1-120° | R-182 |
| ReducedMotionEnabled | GuiService flag for the player's Reduce Motion setting | R-455, R-450 |
| PreferredTransparency | GuiService value for the player's background-transparency setting (0 = opaque) | R-455, R-450 |
| SavedQualityLevel | the only graphics-quality value game scripts can read (Automatic, 1-10) | R-239, R-224 |
| RenderGPUFrameTime | Stats counter of GPU frame time used for effect budgets | R-461 |
| EasingStyle | tween curve family (Back overshoots then settles, Quad, Cubic) | R-454 |

## Performance

| term | meaning | source |
| --- | --- | --- |
| overdraw | the same pixel shaded many times by overlapping transparent layers; the main particle GPU cost | R-209, R-132; ChatGPT 11 |
| fill rate | GPU capacity to process screen pixels; a few big sprites can cost more than many small ones | R-209; ChatGPT 11 |
| draw call | one batch sent to the GPU; every emitter or beam costs about one (single tier C) | R-200, R-351 |
| LOD | level of detail: cheaper presentation at distance or low quality, essential information kept | R-200; ChatGPT 11 |
| culling | not rendering or updating what is not needed (off-screen, far, nobody near) | R-200, R-204; ChatGPT 11 |
| pooling | reusing instances instead of create/destroy; needs a full reset | ChatGPT 11; R-196 |
| priority tiers | essential / supporting / environment particle classes dropped bottom-up under load | R-299 |
| effect budget (Effect Types) | a global budget share that scales effect counts down as usage rises (Unreal) | R-216 |
| concurrency budget | a budget set from how many copies of an effect can be on screen at once | R-248 |
| texture streaming | engine loads low-quality textures first and raises quality by memory and screen size | R-234 |
| thermal throttling | phones slow down after sustained load; seen after 10-15 min of play | R-231 |
| low-end device | Roblox: Android under 2 GB RAM | R-036 |
| quality tier | a set of effect layers kept at a given SavedQualityLevel band | R-239; project (07 P17) |

## Accessibility and safety

| term | meaning | source |
| --- | --- | --- |
| general flash | a pair of opposing relative-luminance changes of ≥10% of maximum, with the darker state below 0.80 | R-165, R-167 |
| red flash | a transition pair where one state is saturated red, R/(R+G+B) ≥ 0.8 | R-165 |
| three-flash rule | no more than 3 general and 3 red flashes in any 1 s, or the WCAG area route | R-165, R-167 |
| 10-degree field / 0.006 sr | WCAG area unit: flashes may cover 25% of any 10° visual field (not 25% of the screen) | R-165, R-167 |
| photosensitive epilepsy | seizures triggered by flashes or patterns; about 3% of people with epilepsy | R-330 |
| Harding test | shorthand for automated flash and pattern analysis (HardingFPA); record tool and version | R-155; ChatGPT 11 |
| flash governor | project proposal: a client limiter that keeps the composite at ≤3 flashes per rolling second | project (07 P24) |
| reduce-effects setting | player controls that lower shake, flashes, full-screen effects or density without removing information | R-074, R-028 |
| colour never alone | every colour-coded meaning also has shape, pattern, icon or label | R-015, R-398 |
| non-text contrast | ≥3:1 contrast for graphics needed to understand content | R-238 |

## Evidence and reference conventions

| term | meaning | source |
| --- | --- | --- |
| tier A / spec / B / C / D / internal | provenance classes: makers and studies / engine and standards docs / trade press / expert community / leads only / project notes | 00-sources.md |
| evidence level | study, preprint, industry practice (who, year), spec or inference, tagged per claim | project (merge rule 4) |
| single tier C | a claim that rests on one tier C publication; needs a second source before it becomes a rule | project (merge rule 8) |
| corr N | N distinct publications agree (two models citing one page count once) | project (01) |
| PROPOSAL (inference) | a starting value with no direct evidence: value, basis, tune-by test; stays a proposal until the owner confirms | project (merge rule 5, AGENTS.md §0) |
| no number found | neither research run found a number; never fill it without a test | project (merge rule 4) |
| fps not stated | the source gives frames without a frame rate, so no ms conversion | project (merge rule 6) |
| lead (tier D) | a pointer worth checking, never proof | 00-sources.md |
| owner-measured | a value from our own Studio or phone test, labelled so | project (02a) |
| X-nn / PD-nn / IF-nn | rows of `contradictions.md`: evidence conflicts / proposal divergences / integration fixes | project |
| T-xx, Tn, O-n, G-nn | test ids in the section files and `12-gaps.md` | project |

## Conflicts

| term | reading A | reading B | resolution |
| --- | --- | --- | --- |
| hit-stop vs freeze frame | used as synonyms in some sources | survey: hit stop is local to the bodies, freeze frame halts all game time (R-082) | the R-082 split is used; Roblox has no global time scale, so only local hit-stop exists (spec R-211, R-171; inference) |
| on twos | read as "2 fps" in loose usage | a drawing held for two frames of a stated base rate (R-112; ChatGPT 11) | base rate always stated |
| 25% (flash area) | read as 25% of the screen | 25% of a 10° field for WCAG; ITU and GAG use 25% of the screen | name the standard every time (contradictions X-43, X-44) |
| punch length | "flash 1-2 frames" vs "hit frame 0.1 s" | different layers (X-34) | brightest layer vs whole hit sprite |

## Open / test ourselves

| term | open point |
| --- | --- |
| importance rating | no mapping to parameters exists; project bands are PROPOSALs (contradictions PD-06; 12-gaps G-01) |
| floaty, mushy, cheap | no source defines them for VFX; the 05 table gives working descriptions only (05 5d) |
| closure / satisfying completion | no study found (12-gaps G-46) |
| impact frame length | no maker frame count (12-gaps G-08) |
