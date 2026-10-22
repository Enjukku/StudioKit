---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [animator, vfx-designer, sound-designer, game-designer, ui-ux-designer, film-director, feature-builder, character-rigger, reference-images, marketing, modeler, art-director, live-ops-designer, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Weight and timing

How timing, spacing and balance make motion feel heavy, fast, fair and alive, in clips, effects, sound and UI.
WT-01 to WT-03 are the gameplay jobs of timing (readable anticipation, consistent physics, emotional tone). WT-04 to WT-06 are the working method (keys and breakdowns, root first, weight shift). WT-07 to WT-10 are balance and gravity (centre of gravity, held weight, spacing, arcs). WT-11 to WT-13 time bursts and build-ups. WT-14 to WT-22 are body mechanics for action clips. WT-23 to WT-25 are dynamics and secondary motion.
Related: `exaggeration.md` for pushing past real, `rhythm.md` for cadence and offsets, the timing contract between crafts in `cross-craft.md`.
Lines marked (DS) in WT-01, WT-02 and WT-11 were added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### WT-01 Anticipation must read: long enough to react to, tight enough to feel strong
- principle: Anticipation tells the player an action is coming; for an attack it is often the most important thing the player must know. Its length depends on who must react: an enemy attack's wind-up is held long enough for the player to react; a player's own action uses a short, tight anticipation (a couple of frames of tightening) so it feels powerful and responsive.
- why: Without a readable wind-up, hits feel unfair; a long hold on the player's own move reads as waiting and kills the push-off.
- apply: Every enemy and boss attack has a distinct anticipation pose with a clear silhouette, held for a reaction window the game designer sets (PROPOSAL default for dodgeable attacks: at least 0.3-0.5 s [inference]); VFX and sound add a tell on the same frames. Player moves: about 2 frames of tight hold before a spring (R04 demo value, R04:448-454), then more time in the air or on the action.
- apply (DS): Telegraph lead start values for dodgeable attacks: about 0.6 s with one known dodge direction, about 1.0 s with 2-4 safe spots [inference, DS PROPOSAL]; never below visual reaction time (about 0.23 s, a study DS cites) plus choice, touch and render time; bigger attacks get longer windups; the tell uses at least 2 channels (VFX plus sound or animation) and ends, and is removed, on the damage frame (DS:vfx-design/references/elements.md:40, 132; DS:vfx-design/references/moment-recipes.md:29, 60).
- check: Frame-by-frame capture at the game camera: the anticipation pose has a clear black-fill silhouette; count its frames at 30 fps and compare with the designer's reaction window (enemy) or input-response budget (player); VFX and sound tells start on the same frame (`clip_check.py events`).
- mistake: Attacks with no wind-up, impossible to read; holding the coiled pose "for quite so long" before a player's push-off (R04:450).
- examples:
  - R00b: anticipation of a punch, "about to punch you in the face", is one of the most important things a player needs to know (R00b:2953-2971).
  - R04: "just a couple frames of her holding this pose, a tightening of the energy before the spring" (R04:448-454).
- roblox_fit: Network latency shortens the effective reaction window for enemy tells, so err longer for dodgeable attacks [inference]; short player anticipations suit phone gameplay where responsiveness matters [inference].
- roles: animator, vfx-designer, sound-designer, game-designer, ui-ux-designer, qa-lead
- also: game-design-fun, vfx-reads-timing, exaggeration
- sources: R00b-F28 (R00b:2953-2971); R04-F21 (R04:448-454)

### WT-02 One consistent physics lets players predict
- principle: Realistic or fantastical, motion and physics must be consistent so players can predict how objects and actions will affect the world.
- why: Prediction makes the player feel in control.
- apply: Declare one gravity, jump arc and impact-weight language per game (game profile or art bible) and keep every clip, effect and code-driven motion consistent with it.
- check: Compare jump and fall timing across characters, props and effects against the declared values (root Y curves from `clip_check.py`, measured fall times); flag outliers.
- check (DS): Motion personality is one across crafts: UI tween easing and durations, VFX timing and camera moves match the art bible's motion line (snappy, heavy, floaty, bouncy); compare the motion table (UI-15) with clip and effect timings and flag any craft that moves differently (DS:art-fundamentals/SKILL.md:60; DS:animation/SKILL.md:75; DS:gui-ui/SKILL.md:35).
- mistake: Each asset moving by its own rules.
- examples:
  - R00b: consistent physics "allows the player to predict how objects and actions will affect the world" (R00b:2973-2983).
- roblox_fit: Workspace.Gravity and Humanoid jump settings set the base physics [unverified]; animations, VFX and tweens should match them.
- roles: animator, game-designer, vfx-designer, feature-builder, sound-designer
- also: game-design-fun
- sources: R00b-F29 (R00b:2973-2983)

### WT-03 Motion sets the emotional tone; giants move slowly
- principle: How something moves sets the emotion: the slow, heavy movement of an enormous character instils fear, wonder and epic scale.
- why: Slow, heavy motion reads as size and power; human-speed motion makes a giant read small.
- apply: For big creatures and bosses: slower timing, longer settles, ground impacts, supporting VFX and low sound. State the intended emotion in the brief.
- check: Show the clip to a fresh agent and ask which emotion it gives; compare its timing (stride period, settle length) with a normal-size character's.
- mistake: Giant characters animated at human speed.
- examples:
  - R00b: "the movement of an enormous character can instill a sense of fear, wonder, and epic scale" (R00b:2985-2991).
- roblox_fit: No change.
- roles: animator, film-director, sound-designer, vfx-designer, game-designer
- also: exaggeration, game-design-fun
- sources: R00b-F30 (R00b:2985-2991)

### WT-04 Keys tell the story; place every breakdown on purpose
- principle: Two key poses plus "play" is a linear blend that twists the body through itself; interpolation is not animation. Keys are the storytelling beats; breakdowns are how you get there, placed on purpose to direct the flow (head leads, arms follow). A breakdown can look awkward on its own if the flow is good.
- why: A linear blend has no weight, arcs or intent; limbs take the shortest path through the body and it reads mechanical. The eye reads flow between keys, not single in-betweens.
- apply: Never ship a clip with only start and end keys. In Blender, after key poses, add breakdowns for root, feet and arms and scrub every frame for parts passing through each other. In Roblox KeyframeSequences give each Pose an explicit easing; do not rely on Linear between far-apart poses.
- check: Render at 30 fps from the game camera and step frame by frame: no limb passes through the torso, knees do not invert, feet do not drift. `clip_check.py` root and foot samples: a straight-line path between two keys over more than about 6 frames flags a missing breakdown [inference]. At speed, breakdowns are not noticeable.
- mistake: "If you just press play after you put the poses in, things should look good theoretically" (R04:66-68); the body "twisting inside of herself" (R04:70); over-polishing single in-betweens.
- examples:
  - R04: Akali's kneel and finger-heart poses blended directly twist her body into a mess; the leg swoop happens only when the foot is moved by hand (R04:64-82, 148-156).
  - R04: "keyframes are like what it is and breakdowns are how you get there" (R04:948-972).
- roblox_fit: KeyframeSequence poses interpolate per PoseEasingStyle (Linear, Constant, Elastic, CubicV2 and others: knowledge/external/roblox-creator-docs/_api-reference/enums/PoseEasingStyle.yaml:22-60); there is no automatic arc, so arcs must be keyed.
- roles: animator, character-rigger, film-director, reviewer
- also: pipeline-production
- sources: R04-F01 (R04:64-82, 148-156); R04-F39 (R04:948-972)

### WT-05 Root first, then poses, then offsets, then details
- principle: Work in layers: first the root (centre of gravity) with the whole body keyed on shared frames so timing is easy to change, then poses at the key moments, then offsets, then details.
- why: The centre of mass carries the weight story; if the root path and timing are right, the rest follows, and shared keys keep retiming cheap.
- apply: In Blender by Python: pass 1 keys only root or hips (position and rotation) plus feet; pass 2 full-body poses on the same frames; pass 3 limb offsets; pass 4 secondary (hair, fingers, face). Retime in passes 1-2 by moving whole-body keys. Expect it to look "weird and bad for a long time" first (R04:90).
- check: After pass 1, render the root-only version from the game camera: the root path alone reads as the action (rise, hang, fall, settle); `clip_check.py` root Y curve shows one clear rise and fall with holds where intended.
- mistake: Polishing a pretty pose before the root timing works.
- examples:
  - R04: the whole move built with the root alone before "there's no pose in the air where we've just animated the root"; "I keep everything keyed on like the whole body ... so that I can easily adjust the timing" (R04:84-96, 434-437, 520-526).
- roblox_fit: The root becomes HumanoidRootPart or LowerTorso motion in the exported clip; root translation in a clip moves the visual, not the physics body [unverified].
- roles: animator, film-director
- also: process-iteration, pipeline-production
- sources: R04-F02 (R04:84-96, 434-437, 520-526)

### WT-06 Shift the weight before a foot moves
- principle: A character on two feet cannot lift or slide a foot until its weight has moved onto the other support. Show at least a little contact and where the weight went, even in a fast move.
- why: Viewers know from their own bodies that lifting a loaded foot means falling; skipping the shift breaks belief in the whole move. It is the most frequent demo-reel note (R04:456-460).
- apply: Before any foot lifts, key the root moving over the planted foot (lean or sink) for at least a few frames; for snappy gameplay moves keep at least one frame that shows contact and weight direction.
- check: Step the clip: on the frame a foot leaves the ground, the root's ground projection sits over the other support; `clip_check.py contact_slide` on the planted foot stays within the rig sheet's tolerance.
- mistake: Characters "standing there on both feet and then they will just move a foot" (R04:456-460).
- examples:
  - R04: to swoop Akali's back leg she first has to "pull her weight off of that foot somehow"; the shift started "a little earlier" so the other foot can move (R04:96-100, 456-474, 660-666).
- roblox_fit: Gameplay clips are short and blend with AnimationTrack fadeTime (knowledge/external/roblox-creator-docs/_api-reference/classes/AnimationTrack.yaml:251); the shift can live in the first frames of the next clip, but it must exist.
- roles: animator, reviewer, qa-lead
- also: exaggeration
- sources: R04-F03 (R04:96-100, 456-474, 660-666)

### WT-07 Centre of gravity over the feet, unless off-balance is the point
- principle: A pose shows weight distribution: the centre of gravity falls over the feet, or the character looks awkward, unless that is the intent (just kicked in the head).
- why: Viewers sense balance instantly.
- apply: In each key pose (animation, key art, reference images), place hips and mass so their vertical projection lands in the support area of the feet; break this only on purpose.
- check: Front and side renders of the key pose: drop a vertical line from the estimated centre of mass; it lands between or over the feet, or the brief says why not.
- mistake: Accidentally off-balance poses.
- examples:
  - R00b: off-balance is right only for being kicked in the head (R00b:3104-3119).
- roblox_fit: No change.
- roles: animator, reference-images, marketing, film-director
- also: shape-silhouette
- sources: R00b-F34 (R00b:3104-3119)

### WT-08 Held objects show weight by distance from the body
- principle: The closer a character holds an object to its own centre of gravity, the heavier it looks; held far out, it looks light.
- why: People pull heavy loads close to balance them.
- apply: Pose held items by their intended weight: heavy weapons and loot close to the body with a counter-lean; light items held out. State the weight class in the prop brief.
- check: Side render of the pose: the item's distance from the torso matches its weight class; heavy items show a counter-lean.
- mistake: Heavy objects held at arm's length with no strain.
- examples:
  - R00b: the same sphere looks like a balloon held out, or a bowling ball held close (R00b:3121-3133).
- roblox_fit: Tool grips fix the hold position; set the grip and the hold pose to match weight [unverified].
- roles: animator, reference-images, modeler, marketing
- also: character-design
- sources: R00b-F35 (R00b:3121-3133)

### WT-09 Uneven spacing and eases sell gravity
- principle: Even spacing feels wrong. Spacing that shrinks as an object rises shows gravity pulling it down; an object slows down before it stops (an ease).
- why: Real objects accelerate and decelerate; constant speed looks mechanical.
- apply: Use eased curves for arcs and stops (Blender interpolation, PoseEasingStyle in clips, TweenService easing for code-driven motion and UI). For bounces and jumps, spacing shrinks near the top and widens near the ground.
- check: Per-frame positions from `clip_check.py` samples: frame-to-frame distance near the apex is smaller than near the ground; flag constant per-frame spacing.
- mistake: Even, linear spacing.
- examples:
  - R00b: Teemo as a bouncing ball (R00b:3193-3217).
- roblox_fit: Same in clips and tweens; check exact easing names in the docs before use [unverified].
- roles: animator, vfx-designer, ui-ux-designer, feature-builder, film-director
- also: rhythm, exaggeration
- sources: R00b-F37 (R00b:3193-3217)

### WT-10 Moving parts travel on arcs
- principle: Moving parts travel on arcs; a flat horizontal toe or hand path looks unreal, a slightly parabolic path keeps gravity present.
- why: Gravity curves trajectories; arcs make extreme action believable.
- apply: Track toe, hand and weapon-tip paths and adjust keys until they form arcs or parabolas. VFX projectiles and debris follow the same rule.
- check: Plot sampled world positions of feet, hands or the weapon tip: the path curves; flag straight segments longer than a few frames.
- mistake: "she feels really, really flat ... traveling kind of horizontally" (R04:750-752).
- examples:
  - R04: a more parabolic toe path (R04:748-758).
- roblox_fit: No change.
- roles: animator, vfx-designer
- also: exaggeration
- sources: R04-F34 (R04:748-758)

### WT-11 Bursts reach size fast and ease out slowly
- principle: An explosion is a circle growing to full size; linear growth feels flat. Reach most of the size very fast at the start, then slow down toward the maximum.
- why: Fast-out then ease gives energy and impact; linear motion feels mechanical.
- apply: Particle Size NumberSequence that jumps most of the way in the first part of the lifetime and eases at the end, or an ease-out tween on a MeshPart. PROPOSAL default: about 70-80 % of max size within the first 20-25 % of the duration [inference]. Same curve for UI pop-ins and reward bursts.
- apply (DS): Stagger the exit: the main glow leaves first, the flare almost as fast, sparks later, embers last; offset secondary layer starts by 2-3 frames so the effect is not one mass; ParticleEmitter NumberSequences interpolate linearly between keypoints (knowledge/external/roblox-creator-docs/_api-reference/datatypes/NumberSequenceKeypoint.yaml:96, 109), so add keypoints to ease; bursts throw in a few clumped directional cones, not an even sphere (ground blasts about a 45° cone [inference]) (DS:vfx-design/references/elements.md:122, 124, 152; DS:vfx-design/references/review.md:156).
- check: Sample size per frame at 30 fps: the curve is steep at the start and flat at the end, not a straight line.
- mistake: Linear growth (the "if it was linear" demo, R00c:3812).
- examples:
  - R00c: an explosion as an expanding circle, linear versus eased (R00c:3790-3828).
- roblox_fit: ParticleEmitter Size takes a NumberSequence over lifetime (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:130-167).
- roles: vfx-designer, animator, ui-ux-designer, sound-designer
- also: vfx-reads-timing
- sources: R00c-F13 (R00c:3790-3828)

### WT-12 Build-ups rise: smaller to bigger, dim to bright, low to high
- principle: Show power being gathered before the release: a core that starts small and dim and grows and brightens, a spawn rate ramping up, a sound that rises in pitch or swells (a reversed sound swells into the release). Time the build-up as carefully as the hit; it is also a strong sound moment.
- why: Rising size, brightness and pitch read as charging energy and make the release feel bigger; sound and picture peaking on the same frame strengthen it.
- apply: The effect spec gives every large effect a wind-up phase and names the release frame shared by VFX, animation and sound. VFX: Size growing over the lifetime (source: scale up to 2, settled at 1.5, R06:158-160); a Lifetime long enough to see the build; spawn rate ramp from 0 to 100 over the build, cut to 75 when 100 was too much (R06:258, 265); start the build early (lightning moved from 1.5 s to 0.5 s, R06:255-257). Sound: rising pitch, a second charge higher than the first, or a reversed copy of the impact or tonal layer, loudest at the release. UI meters filling follow the same rising pattern [inference].
- check: Frame captures of the build: size and brightness rise monotonically and the build lasts long enough to notice (measure seconds); pitch rises across the charge with the loudest point at the release frame; the release frames of VFX, animation and sound match within 1-2 frames at 30 fps [inference].
- mistake: A core that pops in at full size and "fades out way too soon" (R06:155); an explosion with no lead-in.
- examples:
  - R06: the centre dot "getting bigger, it's getting brighter"; lightning ramping "zero to like a bajillion" (R06:155-161, 255-261).
  - R07: a second charge pitched up "so it's kind of a charge sound"; reversed sais "for the charge up" (R07:366-371, 511-513, 572-574).
  - R00c: the build-up before an explosion can be timed for interest and is "a good sound example" (R00c:3830-3834).
- roblox_fit: Particle Rate caps at 400 per second per emitter and 100 on mobile (knowledge/external/roblox-creator-docs/effects/particle-emitters.md:212); Rate can be tweened from code. No reverse-play property was found, so play a pre-reversed file; for variable-length charges tween Sound.PlaybackSpeed upward (knowledge/external/roblox-creator-docs/sound/objects.md:170-172) [inference]. Trigger VFX and sound from the same client event so latency does not split them [inference].
- roles: vfx-designer, sound-designer, animator, film-director, ui-ux-designer
- also: exaggeration, vfx-reads-timing, sound, rhythm
- sources: R06-F14 (R06:155-161, 255-261); R07-F19 (R07:366-371, 511-513, 572-574); R00c-F14 (R00c:3830-3834)

### WT-13 Cause first, then effect: a short beat between them, timed in tenths
- principle: A result starts after its cause, not with it. Like a rock thrown into a still lake (a moment before it hits, then the splash), every impact has a short hold or delay, then the release. Tune these gaps in 0.1-0.2 s steps.
- why: Starting together reads as no cause; a small delay reads as consequence, and the short hold builds expectation so the release lands harder.
- apply: Write the effect as a timeline in data with start times per stage. Source timeline: hit delayed 0.1 s to start at 1.6 s (R06:232-233); rain tried at 2.0 s, set to 1.8 s (R06:277-278); floor candy at 2.2 s, after the falling candy (R06:325-326); clouds spawn 1-2 s and stop at the hit (R06:270). PROPOSAL default hold before a burst: a few frames for small hits, longer for big ones [inference]. At 30 fps 0.1 s = 3 frames.
- check: Frame-by-frame capture at 30 fps: list each stage's start frame; each follows its cause by a few frames; a visible hold precedes the peak burst frame.
- mistake: "if they spawn at the same time, it's gonna be a little bit too soon" (R06:326).
- examples:
  - R00c: the rock in the lake: delay, then release, is the timing all explosions use (R00c:3890-3910).
  - R06: rain "off by a small amount", moved 0.2 s earlier; candy on the floor after the falling candy (R06:232-233, 268-271, 276-279, 324-326).
- roblox_fit: Drive stages from a timeline table (content as data) with task.delay; frame rate varies on phones, so time in seconds, not frames.
- roles: vfx-designer, animator, sound-designer, film-director
- also: rhythm, vfx-reads-timing
- sources: R00c-F15 (R00c:3890-3910); R06-F24 (R06:232-233, 268-271, 276-279, 324-326)

### WT-14 Mass cannot vanish
- principle: When mass is on one side and the character suddenly faces the other, show the transfer; "a very sudden absence of space where something once was" reads wrong. Ask at every big change: where does this weight go?
- why: Newtonian intuition: carried mass and energy have to go somewhere; a pop breaks belief.
- apply: Between two poses with a big mass change, add a breakdown where the mass visibly moves (lean, arm out, step). Same for VFX bursts and props that change direction [inference].
- check: Black-fill strip of consecutive frames: the silhouette's mass shifts smoothly; no single frame where a large body volume disappears from one side; root or mass-centre path is continuous.
- mistake: The body that "just pops in this other direction" (R04:250).
- examples:
  - R04: Akali's tight spin must not pop to the other direction (R04:244-254).
- roblox_fit: No change.
- roles: animator, vfx-designer, reviewer
- also: exaggeration
- sources: R04-F09 (R04:244-254)

### WT-15 Counterbalance makes fast moves believable
- principle: Other body parts counter a broad move (an arm out to catch balance, a hand touching the ground); that visible counter-effort lets a very fast move feel possible.
- why: The viewer accepts speed when the body clearly braces against it.
- apply: For each large swing, add an opposite reaching limb or a hand support for 2-4 frames [inference on count].
- check: In the swing's key frames, a counter limb moves opposite to the swinging limb and is visible from the game camera.
- mistake: A swoop done "super quick" without counter, "not super believable" (R04:482).
- examples:
  - R04: an arm out to counterbalance during the swoop; a hand touching the ground makes the quick swoop believable (R04:238-242, 254-260, 480-488).
- roblox_fit: No change.
- roles: animator, reviewer
- also: exaggeration
- sources: R04-F10 (R04:238-242, 254-260, 480-488)

### WT-16 The driving limb leads; momentum carries through the poses
- principle: Find what drives the motion (a leg powered by the obliques, arms throwing the body up) and let the rest follow it; do not stop dead in each pose but swing out of one and into the next. A balancing arm drags at the elbow.
- why: Force has a visible source; momentum flowing through poses feels alive, hard stops feel robotic.
- apply: Key the driver first and let the root follow a frame or two later [inference]; arms rise ahead of a jump to throw the body up; delay the elbow of a balancing arm by a frame; slightly overshoot a pose and settle instead of arriving dead on.
- check: In `clip_check.py` samples the driver's curve leads the root's; arm motion precedes root lift on jumps; arriving at a pose, motion decelerates over several frames, not one.
- mistake: Sticking "so hard to this last pose" (R04:262); arms flailing like "Wakko and Yakko and Dot" (R04:896).
- examples:
  - R04: "the leg is what should really be driving that motion"; "she's carrying the momentum into the squat" (R04:258-264).
  - R04: arms push up so "that force is coming through" (R04:890-906).
- roblox_fit: No change.
- roles: animator
- also: exaggeration, rhythm
- sources: R04-F11 (R04:258-264); R04-F36 (R04:890-906)

### WT-17 Hold the first pose before moving (showcase clips)
- principle: Lock the starting pose for a few frames so the character does not move immediately.
- why: The viewer needs to register the start pose before change begins; an instant move from frame 0 reads as a pop.
- apply: Key the full rig unchanged at frame 0 and about frame 5 (her demo value, R04:106-108) before the first motion key, for emotes, idles, showcase and cutscene clips. Gameplay actions keep this to the minimum the input-response budget allows [inference].
- check: `clip_check.py` samples: frames 0-5 identical (pose delta near zero) for showcase clips; for gameplay clips the hold fits the game designer's response budget.
- mistake: Moving "immediately from this pose" (R04:106).
- examples:
  - R04: "pop the frame five and just lock her down so she doesn't move there for a little bit" (R04:106-108).
- roblox_fit: Network and input latency on phones may forbid long starting holds in gameplay clips [inference].
- roles: animator, vfx-designer, sound-designer
- also: rhythm
- sources: R04-F04 (R04:106-108)

### WT-18 Keep the head stable in world space; turn it late and fast
- principle: Keep the head (and shoulders) holding their world orientation while the body turns under them, then turn the head late and fast, like a dancer spotting.
- why: A stable head gives balance and "interesting motion ... for free".
- apply: In the Blender rig give the head (optionally the shoulders) a world-space orient option, or key the head to counter body rotation; in a spin keep the head facing the old direction, then snap it to the new one in a few frames.
- check: During a body turn the head's world yaw changes less and later than the chest's: compare head and torso yaw curves from `clip_check.py` samples; the head curve lags, then catches up quickly.
- mistake: The head rotating rigidly with the body; note that world space makes spins harder to key (R04:142-144).
- examples:
  - R04: Akali's head keeps its rotation as the body turns, then turns "quickly, like a ballerina" (R04:134-146, 940-948).
- roblox_fit: The exported clip stores local joint transforms (Neck under UpperTorso), so the world-space behaviour must be baked into keys in Blender [unverified].
- roles: animator, character-rigger
- also: character-design
- sources: R04-F05 (R04:134-146, 940-948)

### WT-19 Push off with force: feet stay down, then a sharp exit
- principle: To feel a push-off, keep the feet on the ground 1-2 frames longer than the root and make the ease-out from the crouch sharp, not slow.
- why: Delayed foot release shows the legs doing the work; a fast exit shows force.
- apply: Offset foot keys 1-2 frames after the root starts rising; reduce the ease-out on the root.
- check: Feet leave the ground 1-2 frames after root lift starts; the root Y curve leaves the bottom steeply.
- mistake: Blending between two keys so "she doesn't feel like she's pushing off" (R04:592-594).
- examples:
  - R04: "feet actually staying on the ground for at least one, maybe even two more frames" (R04:588-606).
- roblox_fit: No change.
- roles: animator, sound-designer, vfx-designer
- also: exaggeration
- sources: R04-F28 (R04:588-606)

### WT-20 Do not stall travel mid-air
- principle: Horizontal travel must not stop flat during a jump: an initial kick, then near-linear travel, with the feet slightly "beating her to her location".
- why: Stalled travel looks like hitting an invisible wall.
- apply: Remove keys that flatten X or Z travel during flight; let the feet arrive slightly before the body.
- check: Root X and Z curves during flight have no plateau.
- mistake: "She's like hitting this wall here. You can see it flattens out" (R04:608).
- examples:
  - R04: deleting the flat curves so she travels through space (R04:606-618).
- roblox_fit: No change.
- roles: animator
- also: none
- sources: R04-F29 (R04:606-618)

### WT-21 Fast contact; delete frames until the hit lands
- principle: Contact should come fast: less time between keys feels faster, and a slow touch-then-scoot reads soft. When a section feels weak, remove one frame at a time until it hits.
- why: Quick contact shows the body catching its weight; too many frames dilute impact.
- apply: Move landing and impact keys closer together; feet contact within 1-2 frames of the fall [inference]; then delete single frames in a weak range and re-check; shift the feet by a frame after. Sound and VFX impact markers sit on the contact frame.
- check: Count frames from first contact to full weight before and after; the after version is shorter and reads zippier; the impact marker equals the contact frame (`clip_check.py events`).
- mistake: "the feet sort of touch and then really slowly scooch out" (R04:438-440); "there's like a couple too many frames ... not impactful" (R04:810).
- examples:
  - R04: "the less time there is between the keys, the faster it will feel" (R04:436-448); "I just delete one of the frames out until it feels more right" (R04:806-816).
- roblox_fit: Shorter clips also feel more responsive in gameplay [inference].
- roles: animator, sound-designer, vfx-designer, game-designer
- also: rhythm, vfx-reads-timing
- sources: R04-F20 (R04:436-448); R04-F35 (R04:806-816)

### WT-22 Land low and strong, with tension; elbows sink
- principle: Landing straight up is not impactful: land lower into a strong pose, hold the bottom a little, then rise. But do not sink too far: the muscles visibly catch the weight. On landing the arm curve reverses and the elbows sink, pulling the character into the ground. Posture carries emotion: a forward lean coming in reads as fear.
- why: Absorbing the fall shows weight and power; controlled deceleration reads strong, over-sinking reads loose.
- apply: Key the root below standing height with bent knees at landing, hold the bottom a few frames, rise to the end pose; limit the depth and shorten the absorb; elbows go down at landing; keep the torso upright for confident characters.
- check: Root Y minimum at landing is clearly below standing height but not excessively deep (compare with the character's stance in the rig sheet); elbow height drops on landing frames; the landing frame is a strong black-fill pose; a reviewer reads the intended emotion from it.
- mistake: "it's not super impactful just to land straight up like that" (R04:358); "sinking too far ... a little loose" (R04:656-658); "she looks kind of afraid as she comes in" (R04:714).
- examples:
  - R04: "strike a cool pose" instead of landing straight up (R04:354-358, 366-372).
  - R04: Akali must "stick the landing" to feel powerful (R04:652-660, 710-716).
  - R04: "the elbows are sinking down ... makes her a little bit more grounded" (R04:928-938).
- roblox_fit: No change.
- roles: animator, game-designer, reviewer
- also: exaggeration, character-design
- sources: R04-F16 (R04:354-358, 366-372); R04-F31 (R04:652-660, 710-716); R04-F38 (R04:928-938)

### WT-23 Small changes in attack and release change the felt weight
- principle: Small changes in dynamics change the feeling: a longer attack gives a punch lead-up and anticipation; a longer release makes it feel like punching through a brick wall. The same holds for motion: wind-up length is the attack, follow-through the release.
- why: The senses read the onset as approach and the tail as mass and aftermath.
- apply: For heavier hits, lengthen the release (sound tail, animation follow-through, VFX linger); for telegraphed attacks, lengthen the attack or add a pre-sound and a longer wind-up [inference for the animation mapping].
- check: Compare light and heavy hit cues: the heavy one has the longer tail (waveform) and the longer follow-through (frame count); a listening test and a fresh agent both rank it heavier.
- mistake: Light and heavy hits with the same envelope [inference].
- examples:
  - R00c: a punch with a longer attack and a longer release feels like a brick wall (R00c:4202-4222).
- roblox_fit: No change.
- roles: sound-designer, animator, vfx-designer
- also: sound, exaggeration
- sources: R00c-F22 (R00c:4202-4222)

### WT-24 Secondary motion adds perceived value
- principle: Secondary animation (an idle hat tip, hair motion, coattails) signals care; removing it makes a cosmetic feel less valuable than its siblings.
- why: Extra motion reads as premium quality.
- apply: Premium cosmetics keep or add secondary motion (dangling parts on existing joints, idle flourishes); map richness to the price tier [inference].
- check: Count secondary-motion sources per cosmetic against the base and same-tier siblings: a premium item never has fewer than the base.
- mistake: "If we ever completely remove the hat animations, remove the hair animation, the skin itself might feel a little less valuable" (R01:688-696).
- examples:
  - R01: base Caitlyn tips her hat when idle after an ultimate kill (R01:688-696).
- roblox_fit: Each extra animated bone or joint costs rig and animation work and runtime [unverified for cost].
- roles: animator, art-director, game-designer, live-ops-designer, marketing, character-rigger
- also: style-identity, game-design-fun
- sources: R01-F43 (R01:688-696)

### WT-25 Animate hair as one mass, then offset down the chain
- principle: Animate hair as one chunk first; heavy hair (a ball ponytail) is springy, not fluid. Then offset each bone down the chain by one frame (the last by two).
- why: A cheap, controllable follow-through that keeps the mass right.
- apply: In Blender key the hair root; offset each child bone's curve by 1 frame, the end bone by 2.
- check: `clip_check.py` samples: hair bones lag the root by the set frames; heavy hair settles quickly instead of flowing.
- mistake: Making a heavy mass too fluid, "like a feather duster" (R04:1002).
- examples:
  - R04: the ponytail as one springy mass with offsets (R04:982-1022).
- roblox_fit: Skinned meshes with Bones support this; rigid Motor6D accessories may not [unverified].
- roles: animator, character-rigger, modeler, vfx-designer
- also: rhythm
- sources: R04-F41 (R04:982-1022)
