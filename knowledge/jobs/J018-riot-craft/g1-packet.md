---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J018 stage 1 (1a readers, 1b synthesizer, 1c cross-check)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# G1 packet: the Riot craft library

**Decision asked:** approve the library at its current state (443 findings, 20 universal principles) as the source for stage 2, so the first wave (animator, modeler, game-designer) can start.

## What was built
| Stage | Result |
| --- | --- |
| 1a readers (17, Opus medium) | 649 findings, each with principle, why, apply, check, mistake, example, Roblox fit, roles, topic, transcript lines (`extracts/`) |
| 1b synthesizer (Opus high) | 427 library findings in 21 topic files + `universal-principles.md` UP-01..UP-18 (the master, J018-D1/D2); all 649 extract findings merged, 0 dropped (`synth/merge-plan.md`) |
| 1c cross-check (Opus high) | 929 DestructionSimulator items judged: 325 covered, 16 new findings, 32 sharper checks added to existing findings, UP-19 and UP-20 added, 108 rejected with a reason (`ds-cross-check.md`) |
| Lead | script check: every finding has all fields, roles use the fixed list, all 649 extract IDs covered; `matrix.md` generated; 3 conflicts fixed (CC-02 sound sync: sound 0 to 40 ms late, never more than 1 frame early; UP-01 engineering line; 2 stale [unverified] tags) |

## Universal principles (the master)
| ID | Principle (short) | Applies to |
| --- | --- | --- |
| UP-01 | The gameplay read comes first; beauty never costs it | all makers, design, engineering, review |
| UP-02 | Judge it where players meet it: game camera, phone size, real place, moving, busy | all makers, review, qa |
| UP-03 | Decide what is read first; spend contrast only there | all visual and audio makers, UI, design |
| UP-04 | Big before small: silhouette, value and composition before colour and detail | all visual makers, motion, sound, UI |
| UP-05 | Shape and silhouette carry identity and meaning | visual makers, motion, sound (by analogy) |
| UP-06 | Less is more: few elements, rest areas, indicate instead of spelling out | all makers |
| UP-07 | One code for meaning across the whole game | all makers, design, engineering |
| UP-08 | Timing tells cause and effect: tell, build, beat, hit, result | motion, effect, sound, UI, cinematic, design, engineering |
| UP-09 | Push what must read past real, on a believable base | visual makers, motion, effect, sound |
| UP-10 | The subject's character drives every choice | all makers, design |
| UP-11 | One world, one style; identity survives every variant | all makers, design, live-ops |
| UP-12 | Controlled variation and life, never exact repetition | visual makers, motion, effect, sound, space |
| UP-13 | Problem, constraints and target before making anything | everyone |
| UP-14 | Research, then many distinct options, then a reasoned pick | all makers, design, lead |
| UP-15 | Cheap stages first; gates freeze decisions; do not be precious | everyone |
| UP-16 | Critique against the goal, one named problem at a time | everyone, review |
| UP-17 | Build for the next craft and for the engine | all makers, engineering, lead |
| UP-18 | Know when it is done | everyone |
| UP-19 | Feedback follows the real outcome | motion, effect, sound, UI, cinematic, marketing, design, engineering, review, qa |
| UP-20 | Every player can read it: never one channel, and every intense channel can be reduced | all makers, design, engineering, review, qa |

## Library index
| File | Prefix | Topic | Findings |
| --- | --- | --- | --- |
| [character-design.md](../../reference/craft/riot/character-design.md) | CD | Character design | 29 |
| [composition-focus.md](../../reference/craft/riot/composition-focus.md) | CF | Composition and focus | 20 |
| [critique-feedback.md](../../reference/craft/riot/critique-feedback.md) | CR | Critique and feedback | 17 |
| [cross-craft.md](../../reference/craft/riot/cross-craft.md) | CC | Cross-craft work | 6 |
| [exaggeration.md](../../reference/craft/riot/exaggeration.md) | EX | Exaggeration | 10 |
| [game-design-fun.md](../../reference/craft/riot/game-design-fun.md) | GD | Game design and fun | 35 |
| [light-colour.md](../../reference/craft/riot/light-colour.md) | LC | Light and colour | 25 |
| [materials-detail.md](../../reference/craft/riot/materials-detail.md) | MD | Materials and detail | 17 |
| [pipeline-production.md](../../reference/craft/riot/pipeline-production.md) | PP | Pipeline and production | 33 |
| [process-iteration.md](../../reference/craft/riot/process-iteration.md) | PI | Process and iteration | 15 |
| [references-ideation.md](../../reference/craft/riot/references-ideation.md) | RI | References and ideation | 30 |
| [rhythm.md](../../reference/craft/riot/rhythm.md) | RH | Rhythm | 5 |
| [shape-silhouette.md](../../reference/craft/riot/shape-silhouette.md) | SS | Shape and silhouette | 20 |
| [sound.md](../../reference/craft/riot/sound.md) | SD | Sound | 33 |
| [style-identity.md](../../reference/craft/riot/style-identity.md) | SI | Style and identity | 20 |
| [ui-ux.md](../../reference/craft/riot/ui-ux.md) | UI | UI and UX | 19 |
| [value-contrast.md](../../reference/craft/riot/value-contrast.md) | VC | Value and contrast | 17 |
| [vfx-reads-timing.md](../../reference/craft/riot/vfx-reads-timing.md) | VR | VFX reads and timing | 26 |
| [visual-hierarchy.md](../../reference/craft/riot/visual-hierarchy.md) | VH | Visual hierarchy | 11 |
| [weight-timing.md](../../reference/craft/riot/weight-timing.md) | WT | Weight and timing | 25 |
| [world-level-readability.md](../../reference/craft/riot/world-level-readability.md) | WL | World and level readability | 30 |

Full finding index: [README.md](../../reference/craft/riot/README.md). Finding x role matrix: [matrix.md](../../reference/craft/riot/matrix.md).

## Findings per role
| Role | Findings |
| --- | --- |
| animator | 139 |
| modeler | 230 |
| character-rigger | 63 |
| art-director | 277 |
| environment-designer | 195 |
| film-director | 76 |
| vfx-designer | 214 |
| sound-designer | 96 |
| ui-ux-designer | 144 |
| marketing | 135 |
| game-designer | 145 |
| progression-designer | 20 |
| live-ops-designer | 36 |
| architect | 24 |
| feature-builder | 52 |
| qa-lead | 77 |
| reviewer | 137 |
| orchestrator | 79 |
| reference-images | 176 |
| level-design | 96 |

## 10 sample findings

<!-- from value-contrast.md -->
### VC-05 Give each screen layer its own value and saturation band
- principle: Keep each layer in its own value and colour range. Environment avoids the darkest darks and lightest lights and sits in one controlled saturation band; characters get a little more range; UI and VFX own the extremes. No pure black in the environment.
- why: The layer with the widest value range wins attention, so UI and VFX read over characters, and characters over the environment. An uncontrolled environment palette raises noise everywhere and hides "a character coming out" (R09:634-635).
- apply: The art bible sets the bands per game. PROPOSAL defaults [inference; the sources give no numbers]: environment 15-85 % value, characters 8-92 %, UI and VFX 0-100 %; environment saturation clearly below character saturation. Environment designers build a material zoo (one sample block per material in one Studio place) and check every material against the band before use. Tune Lighting, materials and textures so the environment never reaches pure black or white.
- check: `look_check.py value` on game-camera captures with masks per layer (environment vs characters vs effects): environment p5/p95 inside its band, VFX and UI own the extremes. `look_check.py palette` on a capture of the material zoo: every material inside the set saturation range. Fail on any pure black in the environment.
- mistake: An environment that uses the full value range and competes, so players "just look at a mess" (R13:760); "if I start using black ... can't do that" (R02:818-820).
- examples:
  - R02: a hard Riot rule: VFX highest whites, then characters, then environment clamped, no pure black (R02:804-828).
  - R13: dozens of units, VFX, UI and cards scream for attention; environment keeps a "buttery, creamy" mid range (R13:749-790).
  - R09: one saturation and value band for all environment materials, checked in an asset zoo of material cubes (R09:624-635).
- roblox_fit: Tone mapping and ColorCorrection Contrast and Saturation change final values (knowledge/external/roblox-creator-docs/environment/post-processing-effects.md:83-84, 124), so measure in-game captures. MaterialVariant lets the zoo hold custom materials (knowledge/external/roblox-creator-docs/_api-reference/classes/MaterialVariant.yaml:5). Phone screens and outdoor glare compress contrast, so keep margin between bands [inference].
- roles: art-director, environment-designer, vfx-designer, modeler, character-rigger, ui-ux-designer, game-designer, level-design, reference-images, reviewer, qa-lead
- also: visual-hierarchy, light-colour, world-level-readability
- sources: R02-F34 (R02:804-828); R13-F31 (R13:749-790); R09-F32 (R09:624-635)

<!-- from shape-silhouette.md -->
### SS-04 Keep the few identifying elements, make them chunky, cut the rest
- principle: A small on-screen character or item survives as 3-4 identifying elements. Choose the right ones (the danger is choosing wrong ones), make them big and clear, push the convex and concave form beyond realism, and remove or reduce every small thing that does not improve the read (rivets, buttons, buckles).
- why: At small size only a few big elements survive; they must be the ones that identify the character. Chunky shapes survive motion and let players track a limb; removing noise organises visual importance.
- apply: The brief lists 3-4 identifying elements per character or item, agreed with the art director before modelling. Modelers scale hook details up to silhouette size (thin spikes become chunky spikes) and drop small details or keep them in texture at low contrast. Review tests each small detail by removal: if the read stays, it goes. Same rule for props, UI icons and VFX shapes.
- check: Thumbnail-size and game-camera captures (`thumb_check.py`, `look_check.py thumb`): every listed element is visible; black-fill identifies the character; before/after captures with a detail removed show no lost read (then keep it removed); convex parts carry light, concave parts shadow.
- mistake: Reducing Garen to "his boots, hands, and hair" (R00a); form-fitting plates with thin spikes that vanish (R11); buttons that "added a lot of unnecessary noise" (R01).
- examples:
  - R00a: Garen simplified to sword, pauldrons and scarf for League's small size (R00a:1146-1176).
  - R11: Katarina's gauntlet spikes chunked up so the "dramatic metal shape" lets you track her arm (R11:187-195).
  - R01: buttons removed from the blouse; concept art relays visual information (R01:940-946).
  - R03: Caitlyn's identifying points are the hat, giant rifle, long legs and collar; over-emphasise what pops out and what is concave (R03:208-217).
- roblox_fit: Phone screens make this stronger; small details also cost triangles (knowledge/external/roblox-creator-docs/art/characters/specifications.md:378). Keep identifying elements readable from behind for third-person cameras [inference].
- roles: modeler, art-director, character-rigger, animator, ui-ux-designer, marketing, reference-images, environment-designer, vfx-designer, reviewer
- also: character-design, visual-hierarchy, materials-detail, exaggeration
- sources: R00a-F32 (R00a:1146-1176); R11-F15 (R11:187-195); R01-F52 (R01:940-946); R03-F09 (R03:208-217)

<!-- from character-design.md -->
### CD-12 Design for motion: test extreme poses, keep mass off the joints
- principle: Parts that look great in a neutral pose may fail in motion. Collars, scarves, armour and long hair near a joint block poses or clip; static (unjointed) hair must not extend into areas that deform; long coattails and billowing sleeves need their own cloth rig. Fix the design with the rigger and animator before the final model.
- why: Players see the character moving almost all the time; dramatic motion collides with or deforms costume near joints, and every extra cloth chain costs rig time and performance.
- apply: Before the final model, pose-test extremes in Blender (arms up, head turn, crouch, attack). Leave clearance around neck, shoulders and wrists; bundle hair into one unit set away from the nape; keep unjointed hair off bending shoulders and chest; flag long cloth in concept as a cost and ask the rigger before keeping it (easy fix: shorter or removed).
- check: Pose renders at extreme poses and a fast clip (walk, attack, head turn): no intersection with face, body, legs or collar in frame captures; `clip_check.py` sampled frames reviewed at the extremes.
- mistake: Approving designs in neutral pose only (a character who cannot raise its arms without stabbing its face); long hair "right against the nape"; static hair extended into costume.
- examples:
  - R00a: collars, scarves and armour can limit animation (R00a:1530-1562).
  - R11: Katarina's hair moved to a ponytail away from the neck; Ahri's condensed braid (R11:305-314).
  - R01: a wavy strand on the temple joint; static hair over the shoulder kept short (R01:541-553).
  - R03: Caitlyn's coattails need their own cloth rig (R03:910-929).
- roblox_fit: R15 has a Neck joint between Head and UpperTorso and separate body meshes (knowledge/external/roblox-creator-docs/art/characters/specifications.md:29, 535); mass across that cut breaks, and rigid part rigs make clipping more visible.
- roles: modeler, character-rigger, animator, art-director, reference-images, reviewer
- also: pipeline-production, shape-silhouette
- sources: R00a-F39 (R00a:1530-1562); R11-F25 (R11:305-314); R01-F33 (R01:541-553); R03-F39 (R03:910-929)

<!-- from weight-timing.md -->
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

<!-- from light-colour.md -->
### LC-01 Reserve the gameplay colours; keep them, and fast motion, out of decoration
- principle: Some colours carry gameplay meaning (red = enemy, danger, "you can shoot this"; the route colour; the team colours). Reserve them: decoration and environment do not use them, and environments also avoid fast motion near sightlines. Pair every reserved colour with a shape or outline cue for colour-blind players, and check saturation numerically, not by eye.
- why: A hue no other object uses becomes a code the player learns instantly; red or moving set dressing competes with the danger signal, and a player shot by someone they could not see loses unfairly. An artist's own eye can oversaturate.
- apply: The art bible holds a reserved-colour table (enemy, danger, team, interactable, route) with the hues and the saturation limit allowed in set dressing. Environment and modeling keep large surfaces neutral; reference-images prompts state "neutral environment, no red accents" when red is reserved. A bright hazard that must be red is tamed (LC-18).
- apply (DS): For two sides, pair orange with blue, not red with green; plan for about 8 % of male players with a colour-vision deficiency, to whom red often looks darker (DS:vfx-design/references/scene-and-clutter.md:116; DS:vfx-design/references/elements.md:104, 111).
- check: `look_check.py palette` on game-camera captures: share of pixels in each reserved hue band outside gameplay objects (target near 0; the owner sets the number); saturation of environment greens and reds measured against the bible. View a capture in a deuteranopia and protanopia simulation [inference]: the danger still reads by shape. Watch a 10 s capture for moving set pieces near sightlines [inference].
- mistake: The signal colour on decoration so it loses meaning; "red is normally a color we try to avoid, and then fast movement is also something we wanna avoid" (R09:60-62); "when I get shot by someone I can't see, that can be rough" (R02:212-214).
- examples:
  - R00a: red enemies in Superhot, red jump spots in Mirror's Edge (R00a:326-336).
  - R02: red is reserved for enemies; he measures how far out his greens are in saturation and tones them back; advocate colour-blind settings (R02:192-216, 438-444).
  - R09: lava is "bright red and it's on fire which is really fast", the hardest element to fit into a VALORANT site (R09:59-63, 820-829).
- roblox_fit: Whatever colour the game uses for enemy or danger Highlights is a reserved hue (Highlight is limited to 255 instances per client: knowledge/external/roblox-creator-docs/effects/highlighting.md:37). No global colour-blind filter was confirmed [unverified], so build paired cues (shape plus colour). Small phone screens give reserved signals fewer pixels, so clashes cost more [inference].
- roles: art-director, environment-designer, vfx-designer, ui-ux-designer, game-designer, modeler, reference-images, level-design, reviewer, qa-lead
- also: world-level-readability, ui-ux, game-design-fun
- sources: R02-F11 (R02:192-216, 438-444); R09-F03 (R09:59-63, 820-829); R00a-F10 (R00a:326-336)

<!-- from vfx-reads-timing.md -->
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

<!-- from sound.md -->
### SD-07 Shape the envelope: the attack and transient make the hit land
- principle: A sound's envelope (attack, decay, sustain, release) is its dynamics and decides whether it feels sharp, soft, sustained or lingering. For impacts, boost the very start (the transient) so the hit has punch; add a separate transient layer when the main layer is soft.
- why: The ear judges impact from the attack; a sharp onset reads as contact and weight.
- apply: Cue cards give a target envelope in milliseconds [inference: the sources give no numbers]; a punch: very short attack, quick decay, little sustain, short release. Every hit and shot cue has a defined transient layer or boost, and the transient frame is marked for sync with the VFX flash and the animation contact.
- check: Waveform of the generated file: peak position and length match the card; the onset peaks within the first few milliseconds [inference]; the audio transient frame equals the visual contact frame.
- mistake: Soft, slow onsets on impacts [inference].
- examples:
  - R00c: a punch broken into attack, decay, sustain, release (R00c:4164-4201).
  - R07: a transient shaper to "squeeze a little bit more life out of the beginning"; a rattly mech layer kept for the gunshot transient (R07:52, 81, 241-242, 405, 413).
- roblox_fit: No live transient shaper in Roblox's audio effects (knowledge/external/roblox-creator-docs/audio/effects.md:33-228), so bake it into the file. The same envelope idea maps to animation (anticipation, impact, settle) and VFX (build, peak, fade) [inference].
- roles: sound-designer, animator, vfx-designer
- also: weight-timing, exaggeration
- sources: R00c-F21 (R00c:4164-4201); R07-F13 (R07:52, 81, 241-242, 405, 413)

<!-- from ui-ux.md -->
### UI-18 Errors and denials say what is wrong and how to fix it, at the control
- principle: A refused action answers on the control that was pressed: what went wrong and what the player needs ("need 40 more gold"), in text with an icon and the danger colour, never colour alone and never a joke that hides the fix. Disabled controls show their reason.
- why: A silent or vague "no" makes players retry and blame the game; a whole-screen reaction to a small error punishes the wrong thing.
- apply: On an error, shake only the control (PROPOSAL about ±4 px, 3 cycles in about 280 ms [inference]); the message appears near it and stays at least about 2 s or until the next tap; a soft, rate-limited "no" sound plays. Every disabled button states why (cost, level, cooldown) and what unlocks it. Refusals in the world (a blocked hit, a full backpack) show a "why" cue too (an icon or a short label) and a distinct, rate-limited sound, not silence.
- check: Trigger each refusal in a capture: the message names the cause and the fix; it reads in grayscale; the screen does not shake; spamming the action plays the sound at most about once per 0.5 s [inference].
- mistake: A red flash only; a whole-screen shake for a UI error; a disabled button with no reason; silent refusals.
- examples:
  - DS: a blocked hit shows a "too strong" icon and a clink, never silence; a full backpack shows FULL plus an icon and a soft, rate-limited thud per refused item (DS:vfx-design/references/moment-recipes.md:90, 139).
- roblox_fit: Tween the control's Position offset for the shake so the layout stays untouched [inference]; colour roles come from the UI rule sheet (UI-06).
- roles: ui-ux-designer, feature-builder, sound-designer, game-designer, reviewer, qa-lead
- also: game-design-fun, light-colour
- sources: DS:gui-ui/references/ui-effects.md:12, 24; DS:gui-ui/SKILL.md:25; DS:vfx-design/references/moment-recipes.md:90, 139

<!-- from world-level-readability.md -->
### WL-29 Plan routes in player metrics: seconds at walk speed, ledges against jump height
- principle: Distances mean nothing to the player; time does. Measure every route in seconds at the real walk speed, keep walks between goals short (shorter still for short phone sessions), make the loop's return trips short or worth taking, and put a reward or a new view at each natural pause. Any ledge higher than the jump height is a wall.
- why: Long empty walks are dead time that ends phone sessions; a return trip walked many times per session multiplies every wasted second; a ledge that looks climbable but is not reads as a bug.
- apply: The level brief states the session shape (first visit, return visit, short phone session) and the movement metrics. Keep a route table per stage: distance, seconds at walk speed, what the player sees or does on the way. PROPOSAL default [inference, DS]: no walk over about 15 s without something to do or see; return trips (sell, restock, respawn to goal) get shortcuts, new views or things to do on the way. Ledges meant to be climbed stay under the jump height; ledges meant to block stay clearly above it.
- check: For each route, distance divided by walk speed stays under the brief's limit; a walk capture at the default speed shows something to do or see within each limit; every ledge on the main route is measured against the jump height in Studio.
- mistake: Judging routes from a top-down view in studs only; a decorative ledge just under jump height that lets players climb out of the map; a 40-second walk back to sell.
- examples:
  - DS: at 16 studs per second, 160 studs is 10 s (DS:level-design/SKILL.md:47).
- roblox_fit: Default WalkSpeed is 16 studs per second (knowledge/external/roblox-creator-docs/_api-reference/classes/StarterPlayer.yaml:358-364) and default JumpHeight is 7.2 studs (StarterPlayer.yaml:243-249); a game that changes them uses its own values from the game profile.
- roles: level-design, environment-designer, game-designer, progression-designer, feature-builder, reviewer, qa-lead
- also: game-design-fun, process-iteration
- sources: DS:level-design/SKILL.md:21-22, 47-49, 54, 67

<!-- from references-ideation.md -->
### RI-21 The first output is a warm-up; reject the typical idea
- principle: The first drawing of a day and the first thumbnail of a task are usually the weakest: they default to the expected idea. Get them out of the way, make more, and look for the surprising option, even a tiny sketch in the corner.
- why: First attempts sit "in the range of expectation"; understanding the theme speeds up later options; the unusual idea is memorable.
- apply: Never stop at the first image result: the first batch is a warm-up and further variants use changed prompts; every concept brief asks for one deliberately atypical option; plan at least two option rounds, with a slow first one.
- check: The record shows how many options were made before the pick (a pick from one fails); the set holds at least one non-obvious idea; the first option is labelled warm-up.
- mistake: "We'll just draw one thing" (R08); going with "what we think Alune would do"; treating the first concept as the answer.
- examples:
  - R08: "our first thumbnail is never going to be the best one" (R08:220-232, 620-634).
  - R12: one sketch on day one, six on day two (R12:202-207, 451-455).
  - R08: Alune riding the moon like a swing won over weapon variants (R08:854-875).
- roblox_fit: Roblox discovery rewards distinct ideas, but the twist must still read at icon size [inference].
- roles: reference-images, art-director, marketing, game-designer, modeler, vfx-designer, orchestrator, reviewer
- also: process-iteration, critique-feedback
- sources: R08-F08 (R08:220-232, 620-634); R12-F18 (R12:202-207, 451-455); R08-F32 (R08:854-875)

## Open points (no answer needed; defaults stated)
- Numbers marked [inference] (for example value bands 15-85 % environment and 8-92 % characters, UI tweens 0.1-0.25 s) are starting defaults, not rules. Default: makers write them as starting values that a check can change; real games correct them.
- Some Roblox claims stay [unverified] (bone scale on skinned meshes, particle collision, a global colour-blind filter). Default: makers keep them as "probe in Studio before relying on it".
- Rules from League's high top-down camera were restated for Roblox's third-person camera (VC-08, LC-10, CF-02). Default: the first real capture checks them.

## Usage (record only, J018-D4)
| Stage | Tokens |
| --- | --- |
| 1a readers | 2.08 M |
| 1b synthesizer | 0.77 M |
| 1c cross-check | 0.50 M |
| Stage 1 total | 3.35 M |
