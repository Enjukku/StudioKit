---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [vfx-designer, art-director, game-designer, ui-ux-designer, environment-designer, animator, sound-designer, film-director, modeler, reference-images, level-design, feature-builder, architect, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# VFX reads and timing

How visual effects communicate gameplay first and look good second, and how they are built to read, to blend and to stay cheap.
VR-01 to VR-05 set what an effect must say (shape, colour, timing, the three reads, the energy look, shape codes). VR-06 to VR-08 protect the screen (footprint, never cover information, cost). VR-09 is the hit beat. VR-10 to VR-16 are particle craft (solid volumes, no popcorning, glow textures, strobes, variation, piles, ambient effects). VR-17 and VR-18 are build structure and tools.
Related: loudness by rank in `visual-hierarchy.md` (VH-02), white blowout in `value-contrast.md` (VC-07), effect colour in `light-colour.md` (LC-02, LC-03, LC-19, LC-20), timing in `weight-timing.md` (WT-11 to WT-13), three beats in `rhythm.md` (RH-03), eye leading in `composition-focus.md` (CF-10, CF-11).
Stage 1c (DestructionSimulator cross-check) added VR-19 to VR-26: per-viewer effects, the true danger area, camera punches, hit-stop, reduced modes, frequent effects, locked meaning, pulse rates. Lines marked (DS) in older findings come from the same check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### VR-01 Specify the read (shape, colour, timing), then pick the cheapest technique
- principle: An effect is built from three pillars: shape language (does it help or hurt you), colour (what it means), timing (cause and effect). If those are right, the tool does not matter; there is no standard recipe, and the same effect can be cards, meshes, trails or anything else. Timing is "really, really important".
- why: Players read intent from shape, meaning from colour and cause from timing in any engine; they see only the result, not the technique.
- apply: Every VFX brief and cue card states three lines before building: shape (sharp and aggressive or round and protective), colour role (from the colour-role table, LC-02), timing (stage start times in seconds). Then choose the cheapest Roblox piece per layer: ParticleEmitter (cards, flipbooks), MeshPart with a texture, Beam, Trail, light.
- apply (DS): Technique chooser by what the eye must read: many small, soft or chaotic bits (fire, smoke, sparks) need particles; one big solid shape that keeps its form while it moves or grows (wave, dome, pillar) needs a mesh with particles on top; a line between two points or a ribbon behind something needs a Beam or Trail; an existing object that changes (completes, upgrades, charges) changes itself and hides the swap under a flash; a feeling over the whole screen for a rare heavy moment uses camera and post effects (VR-21). Under about 10 studs, prefer particles to meshes for rings, slashes and streaks. Context sets the budget: frequent gameplay moments are short and cheap, rare world events may be big, cutscenes may use heavy assets (DS:vfx-design/SKILL.md:23-41).
- check: For the review capture answer three questions in one line each: does the shape say help or harm; does the colour match its role; are stage starts measured and in order (frame captures at 30 fps). Judge against the spec's read, not a technique checklist.
- check (DS): Review muted first: the effect's meaning reads with sound off; if it needs sound, that is a readability fault, not a sync fault (DS:vfx-design/references/review.md:38, 57).
- mistake: Thinking strong painting skill comes first (R06:191, 194); locking onto a familiar technique when another gives the read cheaper.
- examples:
  - R06: the whole "happy storm" planned as shape, colour, timing (R06:24, 59, 191, 367-368).
  - R00c: "I might make the same effect using camera-facing cards, meshes, trails" (R00c:3478-3502).
- roblox_fit: All three are set through ParticleEmitter Texture and Shape, Color, Lifetime, Rate and timing in code; flipbooks: knowledge/external/roblox-creator-docs/effects/particle-emitters.md:397-415; Beam: effects/beams.md; Trail: effects/trails.md.
- roles: vfx-designer, art-director, animator, sound-designer, ui-ux-designer, reviewer
- also: shape-silhouette, light-colour, weight-timing
- sources: R06-F01 (R06:24, 59, 191, 367-368); R00c-F02 (R00c:3478-3502)

### VR-02 Rank every effect's layers: primary, secondary, tertiary
- principle: An effect has a primary, a secondary and a tertiary read, and the eye follows them in that order. Primary = the gameplay core (where it is, what it hits), brightest and highest contrast; secondary = the theme (what element, "this is fire"), clearly weaker; tertiary = a few small supporting bits (sparks), which steal focus if there are many.
- why: A clear ranking delivers the gameplay meaning before the flavour; equal layers leave the eye nowhere to go, and many small bright bits create noise.
- apply: Write the three reads into every effect spec and reference-image prompt. Primary gets the highest brightness and contrast; secondary is a Trail or Beam with one tiling texture, lower in brightness and narrower than the head; tertiary emitters run at low Rate and small Size and fade with Transparency. PROPOSAL default: tertiary particles never brighter or larger than secondary [inference].
- check: Shrink and grayscale the capture (`look_check.py thumb`): the primary is the first thing seen; mask the head: the tail still reads as the theme; hide the tertiary layer: the effect still reads, and if clarity drops with tertiary on, cut its count.
- mistake: All layers equal in brightness and size; a tail as bright and wide as the head; "make sure not to add too many or they'll steal the focus and muddy up the clarity" (R00c:3606-3611).
- examples:
  - R00c: a fireball: head (primary), ribbon tail with a scrolling tiling texture (secondary), a few sparks (tertiary) (R00c:3551-3560, 3580-3598, 3600-3618).
- roblox_fit: Only the primary survives at phone size; Trail Lifetime and TextureLength (knowledge/external/roblox-creator-docs/effects/trails.md:154; _api-reference/classes/Trail.yaml:437) and Beam TextureSpeed (_api-reference/classes/Beam.yaml:500) make the secondary; fewer tertiary particles also help phones when many players cast at once.
- roles: vfx-designer, art-director, reference-images, animator, ui-ux-designer, environment-designer, reviewer
- also: visual-hierarchy
- sources: R00c-F04 (R00c:3551-3560); R00c-F06 (R00c:3580-3598); R00c-F07 (R00c:3600-3618)

### VR-03 Energy reads as a bright core, a glow and something moving
- principle: Energy and magic read as emitted light: a bright core first, a softer glow around it, and a shell or texture that moves so it does not look like a static sticker. Additive light brightens and saturates.
- why: Brightness draws the eye and reads as emitted energy; motion adds life.
- apply: Core = ParticleEmitter with a soft glow texture and LightEmission high, locked to the source; glow = a softer, larger layer; shell = a simple Blender half-sphere or ring MeshPart with an animated texture (flipbook particle, Beam TextureSpeed or a scripted offset). Blender concept renders: emissive core plus bloom. Draw the energy shape first (the lightning), then add glow.
- apply (DS): A heavy impact may add a brief light pulse at the impact point so nearby surfaces light up: a PointLight held for about 2 frames and faded within about 0.3 s, Range about 2-3 times the fireball radius, Shadows off, a desaturated warm colour [inference, DS PROPOSAL]; Range, not Brightness, widens the lit area [unverified]; never a large uniform wash that erases silhouettes (DS:vfx-design/references/elements.md:82, 91; DS:vfx-design/references/moment-recipes.md:67).
- check: Frame captures at 30 fps: the core is the brightest value in the effect; the glow halo is visible but does not swamp the core; the shell texture visibly moves between frames.
- mistake: A core no brighter than its tail; energy painted as flat colour [inference].
- examples:
  - R00c: the fireball head = glow card plus half-sphere mesh with scrolling fire (R00c:3558-3580).
  - R12: lightning inside the glass drawn first, then glow and linear-dodge highlights (R12:354-356, 384-389).
- roblox_fit: No custom shaders; LightEmission gives additive blending (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:57, 257); scrolling via flipbooks (particle-emitters.md:397-415) or Beam TextureSpeed (_api-reference/classes/Beam.yaml:500).
- roles: vfx-designer, art-director, modeler, reference-images
- also: value-contrast, light-colour
- sources: R00c-F05 (R00c:3558-3580); R12-F31 (R12:354-356, 384-389)

### VR-04 Keep an additive core coloured with a saturated halo behind it
- principle: Additive colours wash toward white. Put an alpha-blended, more saturated, darker layer behind the bright core; the surround makes the white core read as coloured.
- why: The eye judges colour from the surround.
- apply: Two emitters at the focus: a core with LightEmission near 1 and a slightly larger halo with LightEmission 0 in the saturated hue.
- apply (DS): Smoke and dust use LightEmission 0 so their dark shapes survive (above 0, dark colours turn see-through); set LightInfluence on every emitter on purpose (0 for self-lit glows, higher for smoke that should take the scene light); Brightness scales the emitted light only when LightInfluence is 0 (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:462-467; DS:vfx-design/references/elements.md:79).
- check: Zoomed capture of the core: a visible coloured ring around the bright centre, not a white disc on grey.
- mistake: Only additive layers, which lose saturation (R06:163-166).
- examples:
  - R06: a pink alpha texture behind the white dot, "faking the saturation in the additive dot" (R06:171-174).
- roblox_fit: LightEmission 0 is normal blending, 1 additive (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:257).
- roles: vfx-designer, art-director, ui-ux-designer
- also: light-colour, value-contrast
- sources: R06-F16 (R06:171-174)

### VR-05 Effects follow a game-wide shape code
- principle: Standardise shapes for meanings across the whole game (plus signs = healing, circles = shields and protection, spiky angular shapes = damage) so players read every new effect by the same code; shape matters most where colours are similar.
- why: Players learn the code once; shape survives where colour fails (colour blindness, tinted lighting).
- apply: The art bible holds an effect shape table; every effect spec and VFX reference image follows it; particle textures carry the shape.
- apply (DS): A lasting glow reads as an active or empowered state: do not leave objects glowing permanently unless that state is what they show (DS:vfx-design/references/elements.md:39).
- check: Grayscale capture of key frames: the effect type (heal, shield, damage) is identifiable by shape alone, also in black-fill.
- mistake: Effects with similar colours and no shape distinction.
- examples:
  - R00c: League's plus signs for health, protective circles for shields, spiky shapes for damage (R00c:3672-3726).
- roblox_fit: Small screens favour bold simple shapes; the particle Texture carries the shape (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:57).
- roles: vfx-designer, art-director, ui-ux-designer, game-designer, modeler, reference-images
- also: shape-silhouette, style-identity
- sources: R00c-F09 (R00c:3672-3726)

### VR-06 Budget each effect's footprint for the worst-case crowd
- principle: Keep feedback and celebration effects small (within one unit's space) and short; big effects only for rare, non-overlapping events. Seven gigantic effects at once and the player cannot tell what is happening.
- why: Clarity must hold "the entire time"; noise can "cost them a round".
- apply: The brief sets a footprint and duration per effect class. PROPOSAL default: personal feedback radius about one character width (about 4-6 studs), short duration [inference]. Test with the worst-case count on screen (every player's effect at once).
- check: Capture at the game camera with the maximum simultaneous count: every character and the thing the player must act on stay visible; count overlapping effects; measure each effect's screen area against its class cap.
- check (DS): Start caps for screen coverage [inference, DS PROPOSAL]: routine effects change at most about 20 % of the screen's pixels (difference image against effects off), a top-tier peak at most about 50 % for at most about 1 s; tune with a 5/10/20/35/50 % test grid against the time to find a pickup (DS:vfx-design/references/scene-and-clutter.md:31).
- mistake: "If I just have seven different gigantic effects going off at once, the player's not gonna know what's going on" (R06:51).
- examples:
  - R06: TFT celebrations stay within one hex; the demo goes 3x on purpose and says it would not ship (R06:49-53, 74, 77).
- roblox_fit: Many players on one server each trigger effects on a small phone screen; particle Rate caps at 400 per second per emitter and 100 on mobile (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:212).
- roles: vfx-designer, game-designer, art-director, level-design, reviewer, qa-lead
- also: visual-hierarchy, world-level-readability
- sources: R06-F05 (R06:49-53, 74, 77)

### VR-07 Never cover what the player needs to see; stay low
- principle: Effects must not cover information players use: other players and units, the HUD, targets, shop and placement areas. Avoid tall vertical effects that block the camera's view.
- why: Covering information is unfair as well as confusing: one player's effect can hide what another needs.
- apply: List the information areas seen from the game camera (other players, HUD zones, targets, shop) and keep effects below and away from them. Source heights: a cloud at 400 units was right, 600 too high, 800 far too high (R06:69-75).
- check: Capture at the game camera during the effect; mask the information areas and confirm no effect pixels cover them; run the source's self-check list: are characters, benches, gold or items blocked? (R06:354-355).
- check (DS): Anything that blocks sight is see-through by about 2 s; impact dust lives about 1.5-3 s, huge clouds at most about 5 s at falling opacity, and nothing lingers over about 8 s in play areas [inference, DS PROPOSAL]; the changed space (a hole, an opened route) reads through the dust first (DS:vfx-design/references/moment-recipes.md:31, 64; DS:vfx-design/references/scene-and-clutter.md:48, 166).
- mistake: Effects placed "super high", blocking the enemy bench and giving an unfair advantage (R06:70, 78).
- examples:
  - R06: the final candy storm "blocks gameplay clarity, the benches would be blocked, your gold mines would be blocked, the characters would be blocked" (R06:70-80, 245, 329-330, 354-355).
- roblox_fit: Third-person and top-down cameras look down at the play area, so an effect above a character hides it from others; keep effects out of phone HUD safe areas [unverified for an engine rule].
- roles: vfx-designer, game-designer, ui-ux-designer, environment-designer, level-design, reviewer, qa-lead
- also: world-level-readability, composition-focus, ui-ux
- sources: R06-F06 (R06:70-80, 245, 329-330, 354-355)

### VR-08 Real-time effects are built for cost
- principle: Game effects run every frame on every player's device, so how an effect is built needs as much thought as how it looks. Many 3D meshes spawned as particles are expensive ("do not do this ever").
- why: Each effect competes with the frame budget; an expensive effect costs frame rate for everyone who sees it.
- apply: Plan each effect with the fewest emitters, particles and textures that keep the read, and state a budget in the spec (emitter count, max live particles, textures). PROPOSAL default: one emitter per read layer, at most three layers for a common ability [inference]. Many small objects are 2D sprite particles; a few pooled MeshParts only for hero pieces.
- apply (DS): Over budget or on a low quality level, drop decoration layers first and never cut or merge a layer that carries truth (area edge, contact, outcome, threat, pickup); every information layer survives the lowest tier; distant copies fade, never pop; engine caps (Rate 400 per second, 100 on mobile) are ceilings, not budgets (DS:vfx-design/references/effect-card-and-presets.md:20; DS:vfx-design/references/elements.md:38; DS:vfx-design/references/juice-repetition-sync.md:99; DS:vfx-design/references/scene-and-clutter.md:103).
- check: Count emitters, Beams, Trails and spawned parts in the effect at peak; in a Studio play-test with the expected number of simultaneous casts, compare frame time with and without the effect (`performance` skill tools).
- check (DS): Performance passes only on a real low-end phone (about 2 GB Android) at the worst expected concurrency over a 10-15 min session, with the budget set before the test; the Studio emulator and short runs are 'not verified' (DS:vfx-design/references/review.md:41, 61).
- mistake: Building like film (many layers, high counts); "spawning a ton of meshes could be very expensive" (R06:307).
- examples:
  - R00c: real-time game VFX versus pre-rendered film effects (R00c:3457-3470).
  - R06: 400 candy meshes on the floor; the machine struggled (R06:306-308, 337-338, 347).
- roblox_fit: ParticleEmitter emits only 2D images (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:11), so mesh rain means real Parts; Rate caps at 100 per second per emitter on mobile (particle-emitters.md:212); exact per-device caps [unverified].
- roles: vfx-designer, architect, feature-builder, qa-lead, reviewer
- also: pipeline-production
- sources: R00c-F01 (R00c:3457-3470); R06-F26 (R06:306-308, 337-338, 347)

### VR-09 The hit is one peak frame between cause and result
- principle: A hit (a slash or flash) tells the viewer something was struck and a result follows. Build the energy until it becomes unstable, then hit on one chosen frame.
- why: The hit is the beat that connects the build-up to the result; without it the result has no cause.
- apply: Concentrate the build elements toward the centre (spawn shape shrunk, count increased, for example 3 to 6), then place one short flash on the hit frame, paired with the sound transient and the animation contact frame.
- apply (DS): Swap an object's state (intact to broken, base to upgraded) on the flash peak so the flash hides the swap; rapid hits closer than about 170 ms read as one, so give each its own short onset or merge them on purpose [inference, DS] (DS:vfx-design/references/juice-repetition-sync.md:123; DS:vfx-design/SKILL.md:28, 38; DS:vfx-design/references/elements.md:153, 167; DS:vfx-design/references/moment-recipes.md:43).
- check: Frame capture: exactly one brightest peak frame at the hit; the result starts after it (WT-13); the flash frame equals the marker in the timing contract.
- check (DS): The hit flash is a brightness jump that still shows in a grayscale capture; a hue change alone fails (DS:vfx-design/references/elements.md:178; DS:vfx-design/references/juice-repetition-sync.md:54).
- mistake: Several competing peaks, or a result with no hit before it [inference].
- examples:
  - R06: lightning duplicated, more spawned and pulled into the centre, a flash on the hit frame (R06:208, 211-217, 225-227, 253).
- roblox_fit: A one-frame flash is ParticleEmitter:Emit on a short-lifetime emitter, triggered from the same client event as the sound.
- roles: vfx-designer, animator, sound-designer, film-director
- also: weight-timing, rhythm, exaggeration
- sources: R06-F21 (R06:208, 211-217, 225-227, 253)

### VR-10 A volume reads solid: close the gaps between sprites
- principle: Spread-out sprites let you see through a cloud and the volume breaks into flat cards; overlap until the gaps close.
- why: Gaps reveal the cards; a closed mass reads as volume.
- apply: For clouds, smoke and mist, increase overlap with larger Size before more particles, and use a front and a back layer instead of one thin spread.
- check: Capture at the game camera: no background visible through the mass; a black-fill of the effect layer shows no holes.
- mistake: Spreading the emitter wide without adding density ("you can see through it", R06:97).
- examples:
  - R06: the spread cloud thickened with more overlapping clouds (R06:97, 105-106).
- roblox_fit: Rate caps at 100 per second on mobile (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:212), so prefer larger Size over more particles.
- roles: vfx-designer, environment-designer
- also: shape-silhouette
- sources: R06-F09 (R06:97, 105-106)

### VR-11 No popcorning: particles fade in and out and blend
- principle: "Popcorning" is seeing individual particles appear or vanish. Fix it by fading opacity in and out (not only shrinking), starting small, and keeping overlapping layers in similar colours so they blend.
- why: Visible pops break the illusion of one mass and look cheap.
- apply: Every particle gets a Transparency sequence that fades in and out (for example opaque, then fading to 1 from half its lifetime, R06:345-346); overlapping layers share colours; never use shrinking to 0 as the only exit.
- apply (DS): Exception: layers the player must notice (the punch flash, a telegraph's first frame) start at full strength on their first visible frame, because an abrupt onset draws attention; fades are for masses and ambient layers (DS:vfx-design/references/elements.md:177; DS:vfx-design/references/scene-and-clutter.md:74).
- check: Frame-by-frame capture of births and deaths: count particles that appear or vanish within one frame (target: none visible at the game camera).
- mistake: Recolouring one layer so it no longer blends (R06:113); fading only by scale (R06:342-344).
- examples:
  - R06: a pink cloud on navy back clouds popcorned; floor candy faded by shrinking until an opacity fade was added (R06:113-116, 122-124, 342-346).
- roblox_fit: Fading near the start and end of lifetime "avoids a popping in/out effect" (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:183).
- roles: vfx-designer, art-director, reviewer
- also: light-colour
- sources: R06-F11 (R06:113-116, 122-124, 342-346)

### VR-12 A glow texture is a soft dot with small irregularities
- principle: A glow is a dot blurred and blurred again, with a few small irregular artefacts, on a transparent background.
- why: A perfect radial gradient looks synthetic; small irregularities read as energy.
- apply: Make a white or grayscale dot on a transparent PNG (scripted image or reference-images), blur it, add slight noise, upload as the emitter Texture.
- check: View the texture on dark and light backgrounds: soft falloff, no hard edge, no visible square edge.
- mistake: A clean synthetic gradient or a visible card edge [inference].
- examples:
  - R06: a simple glow texture made for the centre dot (R06:137-142).
- roblox_fit: Use a .png with a transparent background; a grayscale texture with no alpha can use LightEmission 1 to hide dark regions (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:57).
- roles: vfx-designer, reference-images
- also: materials-detail
- sources: R06-F13 (R06:137-142)

### VR-13 Strobes stay low and behind; the focus never flashes
- principle: A flashing layer can add energy behind the focus, but at low opacity; the focus itself must not strobe.
- why: Full-opacity strobing is harsh, tiring and fights the focus for attention.
- apply: Put the flicker layer behind the core with high Transparency; keep the core steady. Check flash safety for any large brightness change [inference].
- check: Frame captures: the flicker layer's brightness change between frames is small; the core does not flicker; count large full-screen brightness flips per second and keep them rare [inference].
- check (DS): Count large-area flashes on the full composite of the busiest scene (all effects, post-effect pulses such as Bloom or ColorCorrection, UI flashes): at most 3 general and 3 red flashes in any 1 s (WCAG 2.3.1, per DS), design target at most 2; saturated red flashes count separately; one effect passing alone is not a pass (DS:vfx-design/references/camera-and-screen.md:73, 98; DS:vfx-design/references/moment-recipes.md:26; DS:vfx-design/references/review.md:59, 78).
- mistake: A strobing focus, or a strobe at full opacity (R06:200-203).
- examples:
  - R06: the strobe behind the dot, opacity lowered twice until "that's better" (R06:198-203).
- roblox_fit: Phone players hold the screen close; no Roblox docs rule on flash rate was found [unverified]; load `vfx-design` for flash safety.
- roles: vfx-designer, art-director, reviewer, qa-lead
- also: value-contrast
- sources: R06-F19 (R06:198-203)

### VR-14 Repeated objects: random rotation and size, no constant spin
- principle: Repeated objects need random spawn rotation and a size range so no two neighbours match, but no constant spin on objects that should be at rest.
- why: Identical orientation and size reveal the copy ("like a bunch of fish"); constant rotation reads unnatural for resting objects.
- apply: Rotation range full 360 with random sign; size range of about 1x to 3x (R06:340); RotSpeed 0 for resting objects.
- check: Capture at rest: no two neighbours look identical; few matching orientations; nothing spins once landed.
- mistake: Spawned candy all rotating and all the same scale (R06:315-316, 339).
- examples:
  - R06: spawn at 360 with a chance of +1 and -1 on both axes (R06:315-318, 339-341).
- roblox_fit: Rotation takes a min-max range and RotSpeed sets spin (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:494-498); 2D particles rotate only in the screen plane.
- roles: vfx-designer, environment-designer, modeler
- also: materials-detail, rhythm
- sources: R06-F27 (R06:315-318, 339-341)

### VR-15 Build piles from lifetime overlap, inside the play area
- principle: A pile is a copy of the falling layer with physics removed, spawned at ground level, with a long lifetime and random early death so it stacks; its spawn width stays inside the stage.
- why: Lifetime overlap makes accumulation; objects off the stage edge break belief.
- apply: Floor layer: height 0, lifetime 5 s with a 50 % chance to die early (R06:320-321), stack height kept low; spawn width cut from 1000 to 500 to stay on the stage (R06:335-336); the falling layer lives about 1-1.5 s (R06:311).
- check: Capture at peak: the pile covers only the floor area; nothing outside the play bounds; stack height believable.
- mistake: Spawning off the side of the stage (R06:334); stacking too high, "not as believable" (R06:332-333).
- examples:
  - R06: candy piles up on the floor after the rain (R06:310-314, 319-323, 331-336).
- roblox_fit: Lifetime is capped at 20 s and is a min-max range, which gives random death (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:199).
- roles: vfx-designer, environment-designer
- also: weight-timing
- sources: R06-F28 (R06:310-314, 319-323, 331-336)

### VR-16 Ambient environment effects: tiny, slow, partly hidden
- principle: Anything moving in the environment pulls the eye from players: use only a little smoke, slow bright flames down, place them where their base is partly hidden, and lower them until they only suggest.
- why: Motion and brightness compete with players (LC-01).
- apply: Ambient effects use low emission and slow particles and sit away from sightlines [inference on placement].
- check: Capture near each sightline: ambient effects are visible but are not the brightest or fastest moving thing near it.
- mistake: Bright, fast flames in the play space.
- examples:
  - R09: Haven smoke in "tiny little" amounts; flames slowed, moved to the pillar and lowered "even a little bit more" (R09:1054-1080).
- roblox_fit: ParticleEmitter.TimeScale slows a system (knowledge/external/roblox-creator-docs/_api-reference/classes/ParticleEmitter.yaml:962); Brightness (ParticleEmitter.yaml:78).
- roles: vfx-designer, environment-designer, art-director
- also: world-level-readability, light-colour
- sources: R09-F49 (R09:1054-1080)

### VR-17 Build each effect under one root so one change scales it all
- principle: Scaling or raising an effect means every emitter and layer must follow; layers that do not move together break alignment.
- why: A centre dot left below raised clouds breaks the effect.
- apply: Build every effect under one root Attachment or Part with offsets relative to it; keep sizes and heights in one data table so a global scale is one change.
- check: Change the root scale or height once and capture: all layers stay aligned.
- mistake: Raising the clouds but not the centre glow and lightning (R06:248, 254, 263).
- examples:
  - R06: everything doubled: scale 1.5 to 2, height to 500 (R06:239-250, 263).
- roblox_fit: `Model:ScaleTo` scales particle emitter sizes with the model (knowledge/external/roblox-creator-docs/_api-reference/classes/Model.yaml:716-740, "Visual properties like sizes of particle emitters" at :739); a Part or Attachment resized by hand does not rescale its emitters [inference]; keep one scale factor in data and scale through `ScaleTo` or from that factor (lead fix 2026-10-22: the docs say the opposite of the earlier [unverified] line).
- roles: vfx-designer, feature-builder, architect
- also: pipeline-production
- sources: R06-F25 (R06:239-250, 263)

### VR-18 Know the whole toolbox: still or moving particles, meshes with moving textures
- principle: Effects are mostly particle systems: an emitter can show one still image held in place or a stream that reacts to gravity. Some shapes (swirls, rings, trails) read better as simple meshes with textures that move over them.
- why: Knowing the range lets an agent use the cheapest fitting piece instead of custom code.
- apply: One ParticleEmitter with Rate 0 and a single Emit (or long Lifetime and Speed 0) for a held image [inference]; Acceleration and Drag for gravity-like motion; simple ring and swirl meshes from the modeler in Blender, textured with a Beam or Trail scroll or a scripted offset [inference].
- check: Inspect emitter properties through Studio MCP; frame captures confirm the motion matches the spec; scrolling textures move without visible seams.
- mistake: Writing custom code for what an emitter setting does [inference].
- examples:
  - R00c: a water stream with gravity and collision versus a single held image (R00c:3516-3542).
  - R06: swirls made of meshes, scrolling textures and texture painting (R06:182-183, 384-386).
- roblox_fit: Particles have Acceleration, Drag and wind (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:206, 267-269); particle collision with world geometry is not documented [unverified], so fake splashes with a second emitter at the hit point [inference]; SurfaceAppearance has no UV scroll [unverified].
- roles: vfx-designer, feature-builder, modeler
- also: pipeline-production
- sources: R00c-F03 (R00c:3516-3542); R06-F30 (R06:182-183, 384-386)

### VR-19 Rate each effect per viewer and build it for the viewer's relation
- principle: The same effect matters differently to the player who caused it, to an ally or bystander, and to the player it threatens. Rate its importance for each viewer and draw it per relation: threats and pickups stay full for whoever must act on them; other players' non-threat effects are toned down on your screen and never shake, flash or tint it. Team colour follows the viewer's relation (enemy versus ally), not the caster, and always pairs with a shape or outline.
- why: On a busy server most effects on screen belong to someone else; at full strength they bury the one threat or pickup the player must act on. People track only a few items at once (DS cites working-memory studies of about 3-5 items), so attention is rationed per viewer.
- apply: Each effect spec carries three importance ratings (self, other, threatened; 1-10) and a per-viewer variant line. PROPOSAL defaults [inference, DS start values]: other players' non-threat effects at about 50 % opacity through LocalTransparencyModifier; own effects, threats and pickups never toned; at most about 4 effects need attention per viewer at once (own action, nearest threat, one pickup, one ambient); more players on screen means fewer, smaller, quieter effects each and no cinematic zooms. Offer a local clarity setting (all, reduced, essential) that changes only the local screen and never hides threats. Must-find actors win by an outline (Highlight) before brighter particles.
- check: Two-client capture of the busiest expected moment. As the bystander: the toned effects do not hide your own threat or the nearest pickup, and your camera never moves, flashes or tints from another player's effect. As the threatened player: the threat is at full strength and is the brightest element near you. Count effects that need attention per viewer against the cap; sweep player counts (1, 8, max): the time to find the local threat stays flat.
- mistake: Every player's celebration at full strength on everyone's screen; team colour tied to the caster, so the same red means enemy to one player and ally to another; a clarity option that also hides threats.
- examples:
  - DS: WoW's spell-density option (Everything, Reduced, Essential) and Marvel Rivals' local VFX toggles reduce only other players' visuals (DS:vfx-design/references/scene-and-clutter.md:176-177).
  - DS: a per-viewer 1-10 importance rating credited to Riot practice across 750 abilities (DS:vfx-design/references/scene-and-clutter.md:175); this Riot source is outside the 14 transcripts.
- roblox_fit: LocalTransparencyModifier on ParticleEmitter, Beam and Trail is a multiplier seen only by the local client and does not replicate (knowledge/external/roblox-creator-docs/_api-reference/classes/ParticleEmitter.yaml:502-511; Beam.yaml:325-335; Trail.yaml:278-291); the server sends the event and each client draws for its relation; Highlight DepthMode AlwaysOnTop shows the outline through other objects (_api-reference/classes/Highlight.yaml:86-96), capped at 255 per client (effects/highlighting.md:37).
- roles: vfx-designer, game-designer, ui-ux-designer, feature-builder, architect, reviewer, qa-lead
- also: visual-hierarchy, light-colour, world-level-readability
- sources: DS:vfx-design/references/elements.md:36, 46, 103; DS:vfx-design/references/scene-and-clutter.md:29, 38, 89, 123, 130-136, 175-177; DS:vfx-design/references/effect-card-and-presets.md:25; DS:vfx-design/references/review.md:83

### VR-20 The drawn danger area is the real hit area, from warning to last tick
- principle: A ring, flash edge or dust stop line that shows where something hurts sits exactly on the gameplay area at warning, contact and expiry, in every quality tier, skin and viewer variant. The effect reads that truth from the gameplay data; it never sets or invents it. When the danger ends, the danger signal ends on that frame.
- why: Players stand or move by the drawn edge: a ring larger or smaller than the hit area punishes correct play, and a hazard look that outlives the hazard makes players avoid safe ground. Truth comes before readability, and readability before theme.
- apply: List each truth value (shape, radius, fuse, contact time, active end) with the data field it comes from. Draw the boundary as the primary layer, with a hard edge where the edge carries information and soft edges only for atmosphere. Ground zones get an outline plus a low fill, follow slopes and stairs, and add a thick vertical or camera-facing border, because a low camera flattens circles into ovals. Countdown visuals track the server timer; no random fuse. Telegraph progress ends, and the cue is removed, on the damage frame. Aftermath marks (scorch, cracks, dust edge) never overstate the affected area. Visual size may be tuned apart from collision size for decoration, never for the danger border; an offset indicator is an owner decision, never a default. With no gameplay attached (showcase, cosmetic), draw no radius ring.
- check: Overlay a debug shape of the server area (sphere, box, cone) at warning, contact and active end, for the self, ally and threatened views and every quality tier: ring edge, flash edge and dust stop line sit on it (PROPOSAL tolerance about ±5 %, never inside the hit area [inference]). Step to the last damage tick: nothing hazard-coloured remains after it. Run the fuse 20 times: the visual blow matches the server time.
- mistake: Sizing the ring by eye; a skin with a bigger telegraph; a danger glow that lingers after the last tick; a random fuse delay; decorative rings that read as the area.
- examples:
  - DS: a debug sphere overlay at contact; the dust ring's stop line equals the blast radius (DS:vfx-design/references/review.md:30, 128; DS:vfx-design/references/effect-card-and-presets.md:18).
- roblox_fit: Radius and timing live in the gameplay data module and the effect reads them (content as data, UP-17); a see-through debug Part sized from the same data shows the server shape in a test build [inference]; decals and SurfaceGui follow surfaces for zones on slopes [inference].
- roles: vfx-designer, game-designer, feature-builder, architect, level-design, ui-ux-designer, reviewer, qa-lead
- also: world-level-readability, game-design-fun, value-contrast
- sources: DS:vfx-design/SKILL.md:44-45; DS:vfx-design/references/elements.md:31-33, 56-57, 62, 125, 157; DS:vfx-design/references/moment-recipes.md:29, 46, 122, 128-129; DS:vfx-design/references/scene-and-clutter.md:39, 99, 112-113; DS:vfx-design/references/review.md:30, 51; DS:vfx-design/references/effect-card-and-presets.md:17-18

### VR-21 Camera and screen punches are rare, local, rotation-only and gated by importance
- principle: Camera shake, field-of-view punches, slow motion and full-screen flashes or grades are the loudest channels in the game. Use them only for rare, high-importance moments of the local player, never for frequent events and never because of another player's effect. With a third-person 3D camera, shake rotates the view; it does not move it.
- why: A camera that moves on every hit numbs the player, costs aim and causes discomfort; moving (translating) the camera pushes it into walls; another player's effect shaking your screen is noise you cannot act on.
- apply: Each effect spec names its importance and the camera channels it uses. PROPOSAL bands [inference, DS start values]: importance 1-2 uses no camera or screen channel; middle tiers use no camera channel by default, and a small shake only on a rare heavy hit when the owner allows it (lead fix 2026-10-22: the kit's shake is occasional, vfx-design §4); only the top tier (about 8-10 of 10) gets a field-of-view punch (at most about 4° in about 0.15 s, back over 0.2-0.3 s), local slow motion (eased, and only when no other live threat is near) or a full-screen grade pulse. Shake uses a trauma value: each event adds trauma (small about +0.2, big about +0.5), trauma clamps at 1 and decays (about 1 per second), and the shake angle is trauma squared or cubed times a maximum angle (about 3°, tested against 1° and 6°) on smoothed noise, never fresh random offsets per frame. Blast shake falls off with distance and starts when the shockwave reaches the viewer. When the camera is far back, cut shake and carry the weight in sound and animation. No film cuts, zooms or depth of field during active play unless control is paused.
- check: For each effect, list its camera channels against its importance band (a channel above its band fails); capture a frequent effect at its real rate: the camera never moves; two-client capture: the bystander's camera never shakes or tints; near a wall in third person, the shake causes no clipping; aim and move during a shake at the lowest setting.
- mistake: Shake on every brick, pickup or hit; translation shake in 3D; a full-screen flash on routine critical hits; slow motion while another threat is live.
- examples:
  - DS: per-event trauma start values, from a light hit (0) to a building collapse (+0.6 at ground contact) (DS:vfx-design/references/camera-and-screen.md:40-43).
- roblox_fit: Camera.FieldOfView is clamped to 1-120° and defaults to 70 (knowledge/external/roblox-creator-docs/_api-reference/classes/Camera.yaml:268-270); a ColorCorrectionEffect works when parented to Lighting or Workspace.CurrentCamera (_api-reference/classes/ColorCorrectionEffect.yaml:24-26), and under the camera it stays on that client; apply shake each frame after the default camera update (BindToRenderStep after the Camera priority, _api-reference/enums/RenderPriority.yaml:5-10; exact offset [unverified]); post effects do not affect GUI, so vignettes and speed lines are ScreenGui overlays [unverified].
- roles: vfx-designer, film-director, animator, feature-builder, game-designer, reviewer, qa-lead
- also: weight-timing, visual-hierarchy
- sources: DS:vfx-design/SKILL.md:50; DS:vfx-design/references/camera-and-screen.md:15-21, 29-43, 57-66, 84-96, 102-103, 113-118; DS:vfx-design/references/moment-recipes.md:20-21, 28; DS:vfx-design/references/juice-repetition-sync.md:56, 126; DS:vfx-design/references/scene-and-clutter.md:123, 168

### VR-22 Hit-stop is local, short and scaled by hit strength
- principle: A brief freeze at contact makes a melee hit feel solid, but it freezes only the attacker's and target's animation and the hit's own particles, and its length rises with the hit's strength. Physics, debris, other players and server results keep running.
- why: Without hit-stop, contact reads mushy (DS cites a correlational ranking where games without it placed near the bottom for impact feel); one length for every strength flattens light and heavy; long or repeated freezes read as lag and become uncomfortable (a VR study put the pleasant/unpleasant boundary near 0.54 s).
- apply: PROPOSAL start values [inference, DS start values]: light 50 ms, heavy 100 ms, critical or finishing hit 150 ms; a blocked hit about two thirds of the unblocked one; 0 ms by default on explosions and charges, for the thrower of a projectile, on rapid fire, on chain secondaries and in crowds; multi-hits get shorter stops. Freeze on the best pose; the hit sound plays on the first freeze frame. Bracket the length (0, 50, 100, 150, 250 ms) over 20 repeats at 30 and 60 fps (PI-08).
- check: Capture light, heavy and critical hits: the freeze length rises with strength and stays well below 0.5 s; during the freeze, debris, other players and physics keep moving; a 20-hit repetition test is not called laggy; no freeze on explosions or projectile throwers.
- mistake: Freezing the whole game; the same stop for every hit; hit-stop on every shot of rapid fire.
- examples:
  - DS: Celeste-style freezes of 0.05 s on a dash and 0.1 s on an explosion launch as practice references (DS:vfx-design/references/camera-and-screen.md:49).
- roblox_fit: AnimationTrack:AdjustSpeed(0) pauses a track (knowledge/external/roblox-creator-docs/_api-reference/classes/AnimationTrack.yaml:320-324); ParticleEmitter.TimeScale 0 freezes a particle system (_api-reference/classes/ParticleEmitter.yaml:962-968); after the stop restore both to the base speed the track's one owner holds, never to a value saved when the stop began, so overlapping stops cannot restore a saved 0 (lead fix 2026-10-22: two overlapping stops left a track frozen, J018 reviewer run R5); there is no global time scale, so the server never pauses [inference].
- roles: vfx-designer, animator, feature-builder, game-designer, sound-designer, reviewer, qa-lead
- also: weight-timing, game-design-fun
- sources: DS:vfx-design/references/camera-and-screen.md:45-55, 92-94, 115; DS:vfx-design/references/juice-repetition-sync.md:38-39, 55; DS:vfx-design/references/moment-recipes.md:28, 53-54, 86-88; DS:vfx-design/references/review.md:89; R00a:136-164 (hit-pause as a kind of satisfaction, via GD-02)

### VR-23 Every intense channel has an off path that keeps the information
- principle: Shake, flashes, full-screen tints, fast motion and camera pushes each have a player-facing way to reduce or remove them, and the reduced version still carries every piece of information: footprint, contact, outcome, threats and pickups. A warning label is not a fix.
- why: Motion and flashes cause discomfort and, for photosensitive players, risk; a reduced mode that deletes the warning makes the game unfair for exactly the players who need it.
- apply: Each effect and UI motion spec lists its reduced variant: a flash or blink becomes a steady shape or a steady glow with a fill countdown; shake goes to zero; field-of-view punches, push-ins, speed lines and camera dips are removed; UI tweens snap (time 0) or become fades. Where the game has these channels, give separate controls: shake strength (including off), reduce flashes, reduce screen effects; reduced motion follows the player's Roblox setting. Safety faults block release at any priority.
- check: Turn on reduced motion and reduced flashes and capture the busiest scene with sound off: the player can still say where, when and what happened, and every threat and pickup is still found; no camera motion and no large flashes remain; each channel in the spec names its off path (a channel without one fails review).
- mistake: A reduced mode that deletes the telegraph; a "may cause discomfort" label instead of a change; one global toggle that removes gameplay cues along with the uncomfortable effects.
- examples:
  - DS: the reduced variant of a fused charge turns its blink into a steady glow plus a ring-fill countdown (DS:vfx-design/references/effect-card-and-presets.md:136).
- roblox_fit: GuiService.ReducedMotionEnabled reflects the player's Reduce Motion toggle (knowledge/external/roblox-creator-docs/_api-reference/classes/GuiService.yaml:262-268); the docs set the TweenInfo time to 0, or swap to a fade, when it is true (production/publishing/accessibility.md:186-188, 208); shake, flash and screen-effect sliders are the game's own settings [inference].
- roles: vfx-designer, ui-ux-designer, film-director, animator, feature-builder, game-designer, reviewer, qa-lead
- also: ui-ux, light-colour
- sources: DS:vfx-design/SKILL.md:51-52; DS:vfx-design/references/camera-and-screen.md:107, 122-129; DS:vfx-design/references/effect-card-and-presets.md:26, 136; DS:vfx-design/references/moment-recipes.md:38; DS:vfx-design/references/review.md:40, 58; DS:gui-ui/references/ui-effects.md:28

### VR-24 Frequent effects are shorter, quieter, merged and capped
- principle: The more often an effect plays, the shorter and subtler it is. Same-kind events that arrive together merge into one burst, one sound and one count label; each frequent effect has a cap on live copies and particles; and its punch is judged over hundreds of repeats, not one view.
- why: An effect seen once a minute can be loud; one seen every second piles up tails that hide the next contact and tires the player; an identical punch loses its pull after the first few repeats.
- apply: Each effect spec states its expected rate and maximum burst. PROPOSAL defaults [inference, DS start values]: every-second effects keep tails under about 0.5 s and use few channels; same-kind events within about 100 ms merge; at most about 8 live copies of one frequent effect per client (cull the oldest) and about 10 particles per copy; above a full-detail cap, extra copies play only the primary layer. Exits are shorter than entrances.
- check: Trigger the effect at its real rate for 100 triggers (one per second) and at its burst rate (for example 20 per second): no tail build-up hides the next contact; one label and one sound per merge window; live copies and particles stay within the caps (count in Studio); the final counter is exact; the owner does not notice the repeat.
- mistake: Approving a pickup or hit effect from a single trigger; 20 pickups in a second showing 20 bursts and 20 labels; a long tail on an every-second effect.
- examples:
  - DS: coin pickups at up to 20 per second with a magnet: merged, capped, and the count stays exact (DS:vfx-design/evals/briefs.md:33-46).
- roblox_fit: Steady live particles per emitter are about Rate times mean Lifetime plus bursts; Lifetime is capped at 20 s and Rate at 400 per second (100 on mobile) (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:199, 212); pool and reuse effect instances and reset them before reuse [inference].
- roles: vfx-designer, sound-designer, ui-ux-designer, feature-builder, game-designer, reviewer, qa-lead
- also: visual-hierarchy, sound, ui-ux, rhythm
- sources: DS:vfx-design/SKILL.md:53; DS:vfx-design/references/juice-repetition-sync.md:96-101, 140-145; DS:vfx-design/references/moment-recipes.md:40-41, 137; DS:vfx-design/references/review.md:39, 86, 168; DS:vfx-design/evals/briefs.md:33-46

### VR-25 Randomise decoration only; lock what carries meaning
- principle: Variation hides repetition but must never change meaning. Randomise decorative axes (rotation of symmetric sprites, size, lifetime, start frame of chips and splinters, brightness of tertiary bits, which sample of a sound plays); lock everything that carries information: the contact frame, the footprint, team and danger colour, the warning deadline, the power rank and the start frame of meaningful one-shots (telegraph, flash, countdown). Variants are recombined layers, not unique assets, and variety alone does not add satisfaction.
- why: A random start frame on a telegraph or a jittered blast core changes what the player reads; unique assets per variant multiply cost; in DS's juice evidence, random variety gave only a small enjoyment gain, while grading by a real cause is what carried the feel (GD-34).
- apply: Mark each effect layer decorative or semantic in the spec; random ranges go only on decorative layers. PROPOSAL defaults [inference, DS start values]: size about ±15 %, brightness about ±10 %, lifetime about ±20 % on decorative layers; about 3 variants of an every-second effect, built from 3 cores and shared secondaries with one grey texture tinted by a colour ramp. Random rotation only on radially symmetric sprites, never on directional ones. In sound, vary the samples, never the timing.
- check: Capture both ends of every random range side by side: area, timing, team and tier are identical; no meaningful one-shot has a random start frame (inspect FlipbookStartRandom); a "make it more satisfying" fix is never only more variants.
- mistake: FlipbookStartRandom on a telegraph; size jitter on a blast core or danger ring; a directional streak rotated at random.
- examples:
  - DS: variation from rotation 0-360 and size ±15 %, with area, contact time, flash colour, ring colour and pattern, and onset order locked (DS:vfx-design/references/effect-card-and-presets.md:134).
- roblox_fit: FlipbookStartRandom decides whether each particle starts on a random frame (knowledge/external/roblox-creator-docs/_api-reference/classes/ParticleEmitter.yaml:396-401); Rotation and RotSpeed take min-max ranges (effects/particle-emitters.md:494-498).
- roles: vfx-designer, sound-designer, environment-designer, modeler, animator, reviewer
- also: rhythm, materials-detail
- sources: DS:vfx-design/references/juice-repetition-sync.md:27, 92-95, 150; DS:vfx-design/references/moment-recipes.md:42, 85; DS:vfx-design/references/review.md:56, 167; DS:vfx-design/references/effect-card-and-presets.md:82, 134

### VR-26 Pulse and blink rates carry meaning: slow is safe, fast is urgent, never above 3 Hz
- principle: A pulse faster than a heartbeat reads as danger; slower reads as safe. Lasting states pulse slowly or stay steady; countdowns speed up toward the event; nothing pulses above 3 times per second at full contrast.
- why: Players read urgency from tempo before they read the icon; a fast-blinking calm state is a false alarm; above about 3 flashes per second, flashing becomes a photosensitivity risk (the WCAG three-flash rule, per DS).
- apply: PROPOSAL rates [inference, DS start values]: lasting danger zones steady or at most 1 Hz; countdowns at 1 Hz, then 2 Hz in the last 2 s and 3 Hz in the last 1 s; low health as a 1 Hz edge pulse with a small brightness swing, the centre of the screen clear, no full red wash; heal and safe states slower than about 60 per minute. Timers move monotonically and the last step lands on the event frame. Rates live in the shared motion table so UI, VFX and sound tick together.
- check: Measure every looping pulse and blink in a capture (frames per cycle at a known frame rate): each matches its meaning class and none exceeds 3 Hz at full contrast; countdown ticks match the server timer.
- mistake: A fast-blinking pickup that reads as a hazard; a low-health red wash over the whole screen; a countdown that drifts from the real fuse.
- examples:
  - DS: a fuse blinks at 1 Hz when armed, 2 Hz in the last 2 s and 3 Hz in the last 1 s, with a beep on each blink (DS:vfx-design/references/moment-recipes.md:61, 100).
- roblox_fit: Drive pulses from the server's timer value replicated to clients, not a local guess [inference]; UI pulses are UIStroke or ImageLabel transparency tweens (`ui-basics`) [inference].
- roles: vfx-designer, ui-ux-designer, sound-designer, game-designer, feature-builder, reviewer, qa-lead
- also: rhythm, ui-ux, sound
- sources: DS:vfx-design/references/elements.md:126, 141-142; DS:vfx-design/references/camera-and-screen.md:104; DS:vfx-design/references/moment-recipes.md:33, 61, 100, 129-131; DS:vfx-design/references/scene-and-clutter.md:45, 90; DS:vfx-design/references/review.md:79
