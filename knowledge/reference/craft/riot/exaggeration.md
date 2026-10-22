---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [animator, modeler, art-director, reference-images, vfx-designer, sound-designer, marketing, film-director, character-rigger, ui-ux-designer, game-designer, reviewer]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Exaggeration

Pushing forms, poses and motion past real so they read at game size and speed, without breaking belief.
EX-01 to EX-04 push shapes and poses (larger than life, adjectives, contradiction, emotes). EX-05 is the limit that makes extremes believable. EX-06 to EX-10 are motion exaggeration tools (squash and stretch, hang time, overshoot, shoulders and hips, energy to the fingertips).
Related: timing in `weight-timing.md`, silhouette pushes in `shape-silhouette.md` (SS-03, SS-04), build-ups in `weight-timing.md` (WT-12), sound transients in `sound.md`.
The line marked (DS) in EX-06 was added in stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`).

### EX-01 Larger than life: extend and sharpen what must read
- principle: Game characters are larger than life ("double the size, double the muscle mass, double the personality"). A soft feature that does not stick out from the body is weak: extend it, sharpen it and increase its area until it changes the outline. Push proportions, hook shapes and pose energy past realistic.
- why: At game scale and speed only features that change the outline read, and exaggeration sells the fantasy.
- apply: Modelers exaggerate key features (shoulder pieces, hat brims, weapons) beyond the reference until they break the silhouette; reference-images prompts ask for heroic, stylised proportions; animators and sound match the push.
- check: Black-fill at the game camera before and after: each pushed feature visibly changes the outline. Side by side with a realistic-proportion figure, the design is clearly exaggerated in the hook areas.
- mistake: The soft epaulet that "doesn't stick out too far from her body" (R01:202-210); realistic proportions that vanish at game size.
- examples:
  - R01: the epaulet extended and sharpened becomes much more visible (R01:202-210).
  - R11: the 2XKO cast "have all gotten into protein", leaping out of the screen (R11:195-197, 210).
- roblox_fit: Phone cameras show characters smaller than League's, so exaggerate more; stylised proportions read better at small sizes [inference].
- roles: modeler, art-director, reference-images, vfx-designer, animator, marketing, sound-designer, reviewer
- also: shape-silhouette, character-design
- sources: R01-F12 (R01:202-210); R11-F16 (R11:195-197, 210)

### EX-02 Make a pose specific by layering adjectives, then pull back if too far
- principle: Turn a generic pose into one only this character would do by layering character adjectives, each mapped to a pose change. Push, then check whether it went too far and pull back.
- why: Adjectives make a pose specific; checking "too far" keeps weight believable.
- apply: List 2-4 adjectives per character and map each to a pose change (heavy = wider, lower stance; defiant or proud = chin up, chest out; majestic = wind in the cape or scarf). Use the same list in reference-image prompts and key-art poses.
- check: Compare before and after poses: a reviewer names the adjectives from the after pose without being told; the weight is still believable (centre of gravity over the feet, WT-07).
- mistake: Generic poses; going "a little bit too far".
- examples:
  - R00b: Garen: wider stance for weight, raised chin and puffed chest for confidence, heroic wind in his scarf (R00b:3135-3181).
- roblox_fit: A scarf or cape needs its own bones or code-driven motion on Roblox [inference].
- roles: animator, reference-images, marketing, art-director, film-director
- also: character-design, weight-timing
- sources: R00b-F36 (R00b:3135-3181)

### EX-03 For comedy, pose against the character's known trait
- principle: Comedy comes from contradiction: a known tough guy running away "with fear in his eyes".
- why: The viewer knows the character's normal attitude, so the opposite reads as a joke and a story.
- apply: For comic emotes, event poses and promo art, write the character's known trait and choose a pose that clearly contradicts it; the contradiction reads in the whole body (running, looking back), not only the face.
- check: Without text, a fresh agent who is told the character's normal trait reads the joke from a game-distance capture.
- mistake: The joke carried only by a tiny facial expression [inference].
- examples:
  - R05: Brimstone running from zombies (R05:217-225).
- roblox_fit: At phone size faces are tiny; the contradiction must read through body pose [inference].
- roles: animator, film-director, marketing, art-director
- also: character-design, composition-focus
- sources: R05-F09 (R05:217-225)

### EX-04 Emotes and reactions: maximum expression for a two-second read
- principle: Art that is visible for about two seconds (emotes, reactions, expression icons) must be as stylised and expressive as possible so the intent reads in that time.
- why: Short visibility and small size leave no room for subtlety.
- apply: Push emote and expression key poses and icons to the extreme; source number: about 2 seconds visible (R01:307-317). Act or collect reference of the expression first (RI act it out).
- check: Show the emote or icon for 2 s at the real player size: a fresh agent names the intent.
- mistake: Subtle expressions that do not communicate.
- examples:
  - R01: he made faces at his desk to match the emote expressions (R01:307-317).
- roblox_fit: Emotes and reaction icons are tiny on phones; same rule [inference].
- roles: animator, art-director, modeler, ui-ux-designer, sound-designer
- also: weight-timing, ui-ux
- sources: R01-F20 (R01:307-317)

### EX-05 A believable base earns the extremes; break only the joints that can take it
- principle: Animation must follow physics "to a degree enough" that the extreme moments (hanging in the air, smears) are believed. Know from anatomy which joints can be stretched, held unnaturally long or smeared without looking broken; spend exaggeration on one or two signature moments.
- why: Grounded basics (contacts, weight shifts, arcs) earn trust; smears on believable joints read as speed, elsewhere as a broken rig.
- apply: Keep contacts, weight shifts and arcs correct across the clip; choose 1-2 signature moments to exaggerate. Smear or stretch only along limbs in the direction of travel for 1-2 frames [inference]; when a motion is hard, think about it at a bare anatomical level (the wind-up before a throw).
- check: Reviewer asks: is each extreme moment surrounded by correct weight cues (contact, shift, arc)? Step the smear frames: the stretched part follows the motion path and returns within 1-2 frames; no reverse bends at elbows or knees.
- mistake: Breaking the character "in ways that look weird" (R04:296); exaggerating everything so nothing is believed [inference].
- examples:
  - R04: smear frames have "a couple things that are unnaturally stretched, held unnaturally long" (R04:294-300, 306-312); the hold in the air works because the rest obeys energy (R04:472-480).
- roblox_fit: Standard Motor6D clips cannot stretch limbs (a Pose stores only a CFrame: knowledge/external/roblox-creator-docs/_api-reference/classes/Pose.yaml:54-68); smears come from Trails, Beams or extra smear meshes [inference].
- roles: animator, modeler, character-rigger, vfx-designer, game-designer
- also: weight-timing
- sources: R04-F13 (R04:294-300, 306-312); R04-F22 (R04:472-480)

### EX-06 Squash on contact, stretch on speed, by a Roblox-safe route
- principle: Stretch a moving object when it moves fast to show inertia and elasticity; squash it when it hits to show the force stopping it. Compare with a version without it to see the gain.
- why: Shape change shows speed and impact force.
- apply: Use stretch on fast frames and squash on contact frames for cartoon styles, scaled to the art bible. In Roblox, character clips cannot scale parts, so take another route: a VFX impact ring or dust on contact, a camera nudge, a code-driven scale tween on a separate mesh or prop, or swapping a squashed mesh for a frame or two [inference]. Bone scale on skinned meshes is [unverified].
- apply (DS): Keep the volume: when one axis stretches, the other two shrink so the product of the scale factors stays near 1 (the classic Illusion of Life rule; DS:animation/SKILL.md:8, 35).
- check: Frame captures at the contact and peak-speed frames, before and after side by side: the impact and speed read more strongly in the after version.
- mistake: Rigid shapes on impacts; trying to scale Motor6D parts in a KeyframeSequence.
- examples:
  - R00b: Teemo stretched when fast, squashed on landing (R00b:3219-3233).
- roblox_fit: A KeyframeSequence Pose stores only a CFrame (knowledge/external/roblox-creator-docs/_api-reference/classes/Pose.yaml:54-68), so squash and stretch needs the routes above; UI can scale freely with TweenService [inference].
- roles: animator, vfx-designer, ui-ux-designer, character-rigger
- also: weight-timing, vfx-reads-timing
- sources: R00b-F38 (R00b:3219-3233)

### EX-07 Cartoony hang time: hold near the apex, then fall fast
- principle: For a heroic jump, flatten the top of the arc with a small hold ("tabletop") and then let gravity take over quickly so the body is "vacuumed" down.
- why: Hang time sells strength and style; the fast fall keeps it from looking floaty.
- apply: Real jump: fast rise, gradual slowdown, fall. Toony jump: rise, flattened top with a short hold, then a faster fall than the rise. Agree the hang with the game designer when the jump is gameplay.
- check: Root Y curve from `clip_check.py` samples: a flat or near-flat section at the apex, then a descent shorter than the ascent [inference on ratio]; watch at 30 fps: no floaty fall.
- mistake: Falling too slowly or too quickly ("she's falling a little quick", R04:354).
- examples:
  - R04: Akali leaps "higher than people can normally jump" and hangs before landing (R04:336-352).
- roblox_fit: Gameplay jumps are driven by Humanoid physics; hang time applies to animation layered over it, to scripted moves and to cutscenes [unverified].
- roles: animator, vfx-designer, sound-designer, game-designer
- also: weight-timing
- sources: R04-F14 (R04:336-352)

### EX-08 A small overshoot releases energy
- principle: A slight overextension at the top of a rise (a small overshoot, then settle) makes the motion feel energetic; an ease-in is the calmer alternative.
- why: Overshoot shows energy leaving the body.
- apply: Key the root slightly past the final height, then settle. Same for UI pop-ins and VFX scale: pass the target size once, then settle.
- check: The curve crosses its final value once, then settles; the overshoot is visible but small (in `clip_check.py` samples or the tween curve).
- mistake: Every motion arriving dead on its end value [inference].
- examples:
  - R04: "a little overextension at the top so that it feels like ... that energy of her sort of standing up is coming out" (R04:374-384).
- roblox_fit: PoseEasingStyle Elastic exists for clips (knowledge/external/roblox-creator-docs/_api-reference/enums/PoseEasingStyle.yaml:35-38); TweenService Back or Elastic easing gives UI overshoot [unverified].
- roles: animator, ui-ux-designer, vfx-designer
- also: weight-timing, ui-ux
- sources: R04-F17 (R04:374-384)

### EX-09 Always animate the shoulders and hips
- principle: Always animate the clavicles (the shrug) and the hips. Clavicles are "the eyebrows of the body"; without them wind-ups have no energy source and poses look dead; hips let poses sink comfortably.
- why: Full range of motion and body tightening create the wanted exaggeration.
- apply: Riggers expose shoulder and hip controls; every jump, landing or throw keys a shoulder raise and drop and a hip tilt. On a standard R15 rig without clavicles, exaggerate UpperTorso and upper-arm rotation instead.
- check: In `clip_check.py` samples, shoulder (or clavicle) and hip channels are not constant through action clips; hip rotation changes on every weight shift.
- mistake: Named as a top beginner mistake with weight transfer (R04:394-400, 490-492); "I also haven't used her hips at all" (R04:652).
- examples:
  - R04: arms swinging up for a jump without shoulder motion give no energy (R04:388-410, 490-492, 648-654).
- roblox_fit: Standard R15 has 15 joints and no clavicle; LeftClavicle and RightClavicle exist only as optional advanced R15 joints (knowledge/external/roblox-creator-docs/characters/index.md:87-95).
- roles: animator, character-rigger, modeler
- also: weight-timing, pipeline-production
- sources: R04-F18 (R04:388-410, 490-492, 648-654)

### EX-10 Energy flows out to the fingertips; hands matter even when tiny
- principle: At the top of a move the arms carry the remaining energy out through the palms and fingertips. Hand and finger shapes (splay on contact, drag on falls) add a lot even when hands are tiny on screen.
- why: Following energy through the extremities completes the motion line, and a hand-shape change alters the profile and connects the motion.
- apply: At the apex, extend the arm follow-through to the fingertips; key splay on contact and drag on falls; VFX trails can follow the same line. Without finger joints, use bigger hand-pose changes or swap hand meshes [inference].
- check: At the apex frame the arm line continues the body's motion direction to the fingertips; hand pose changes at key moments are visible at the game camera.
- mistake: "don't forget the fingers" (R04:928).
- examples:
  - R04: energy "would probably kind of flow all the way through her palms and out her fingertips" (R04:552-557); one dragging finger pose made the fall easier to read (R04:912-928).
- roblox_fit: Finger joints exist only on advanced R15 rigs, up to 15 per hand (knowledge/external/roblox-creator-docs/characters/index.md:87-95); on phones use bigger hand shapes [inference].
- roles: animator, vfx-designer, character-rigger, modeler, reviewer
- also: weight-timing, character-design
- sources: R04-F26 (R04:552-557); R04-F37 (R04:912-928)
