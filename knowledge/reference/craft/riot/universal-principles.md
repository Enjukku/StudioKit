---
type: reference
scope: universal
status: active
updated: 2026-10-22
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, progression-designer, live-ops-designer, architect, feature-builder, orchestrator, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Universal principles (master)

**This file is the master (owner decision J018-D1, 2026-10-21).** It is not a skill. Every role's books get a "Core principles for this craft" section that states each principle below that applies to the role, written for that role's own work with its own examples and checks. Stage 3 reviewers check each role's section against this file: no contradiction, nothing important missing. A later fix goes into this file first, then into each role's section.

How to read it: each principle has a stable ID (UP-01 ...; never renumber, append new ones at the end), a general statement, why it works, one line per medium showing how it lands there, a general check, the roles it applies to, and the library findings it rests on (topic files in this folder; source lines live there). Mediums: picture/2D (reference images, concepts, paint-overs), model (Blender, Tripo clean-up, Studio parts and MeshParts), motion (rigs and clips), effect (ParticleEmitter, Beam, Trail, light), sound (cue cards, generated audio, Roblox mix), UI (Figma to Roblox), space/level (blockouts, environments, lighting), cinematic (shots, cutscenes), marketing art (icons, thumbnails, key art), and where it honestly applies, design (game, progression, live-ops) and engineering (architect, feature-builder).
Numbers marked [inference] are proposals, not source facts. The pipeline is ours: AI agents make everything; checks run on renders and Studio captures at the game camera, grayscale and black-fill views, thumbnail-size views, `tools/art/look_check.py`, `tools/art/thumb_check.py` and `tools/anim/clip_check.py`.

Order: UP-01 to UP-12 are the principles that most change the quality of the work itself; UP-13 to UP-18 are the process principles every maker needs.
UP-19 and UP-20 were added in J018 stage 1c from the DestructionSimulator cross-check (`knowledge/jobs/J018-riot-craft/ds-cross-check.md`); they rest mostly on findings sourced from DS, not from the 14 transcripts.

## Index

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
| UP-12 | Controlled variation and life, never exact repetition | visual makers, motion, effect, sound, UI, space (lead fix 2026-10-22: UI added; the UI line already holds) |
| UP-13 | Problem, constraints and target before making anything | everyone |
| UP-14 | Research, then many distinct options, then a reasoned pick | all makers, design, lead |
| UP-15 | Cheap stages first; gates freeze decisions; do not be precious | everyone |
| UP-16 | Critique against the goal, one named problem at a time | everyone, review |
| UP-17 | Build for the next craft and for the engine | all makers, engineering, lead |
| UP-18 | Know when it is done | everyone |
| UP-19 | Feedback follows the real outcome | motion, effect, sound, UI, cinematic, marketing, design, engineering, review, qa |
| UP-20 | Every player can read it: never one channel, and every intense channel can be reduced | all makers, design, engineering, review, qa |

### UP-01 The gameplay read comes first; beauty never costs it
- principle: Everything the player sees and hears is a carrier of game state. Its first job is clarity: the player instantly knows where to go, who is friend or enemy, what is dangerous, what just happened and what they can do. Satisfaction and style come after; a beautiful piece that weakens the read has failed.
- why: Players decide in fractions of a second on small, busy screens; information that needs study is missed, and art that hides state feels unfair.
- in each medium:
  - picture/2D: a reference image states the gameplay read it must support before its mood; pick the option a player names correctly in one second.
  - model: identifying elements, weapon and role read at game size; cosmetics never change the role read or hide combat information.
  - motion: every attack has a readable anticipation; the player's own moves read from the silhouette at the key pose.
  - effect: the gameplay core (where, what it hits) is the primary read; effects never cover players, HUD or targets.
  - sound: every gameplay state change has a cue that identifies it with the screen covered; far-carrying sounds are the ones players must act on.
  - UI: each element says one thing the player must understand and act on, readable in a glance on a phone.
  - space/level: the environment is the backdrop; routes, cover, hazards and objectives read before decoration; floors stay clean for the smallest gameplay object.
  - cinematic: the shot's story beat and the hero read in the first second.
  - marketing art: the launched thing is the hero; the promise reads at icon and tile size.
  - design: art and mechanics promise the same thing; every threat telegraphs and behaves consistently.
  - engineering: the small attempt cue (VFX, sound, UI) fires on the client at once so the read is not delayed by the network; the big outcome layer waits for the server-confirmed result (UP-19); a threat's tell is sent when its wind-up starts, never with the damage, so network delay does not eat the reaction window (lead fix 2026-10-22: WT-01's latency note needed its engineering answer).
- general check: In a capture of the busiest expected moment at the game camera on a phone-size viewport, name each critical fact (route, ally or enemy, threat, objective, own state) at a glance; ask "what is the gameplay read here, and does any element weaken it?" before any style question.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, progression-designer, live-ops-designer, feature-builder, reviewer, qa-lead
- rests on: GD-01, WL-01, WL-02, WL-03, WL-19, VH-01, VH-04, VH-07, VR-02, VR-07, WT-01, SD-01, UI-02, UI-10, GD-07, GD-13, GD-16, GD-21, RI-01, RI-04, VR-19, VR-20

### UP-02 Judge it where players meet it: game camera, phone size, real place, moving, busy
- principle: Nothing is approved from a beauty shot, an editor viewport or a close-up. Judge every piece through the real game camera, at the size players see it (often a phone), in its real surroundings, in motion, with lighting, effects, other players and UI on.
- why: Camera, scale, surroundings, motion and light change the read; detail done close up is invisible at game size; most players play on phones.
- in each medium:
  - picture/2D: compose inside the real frame and crop (icon, shop card, HUD); view every image small, mirrored and in grayscale.
  - model: review renders at the game camera on the real ground and next to roster neighbours; the back and top matter for third-person and top-down cameras.
  - motion: key poses read through the game camera, not the Blender viewport; hook shapes show at the held moments.
  - effect: test in play mode at the game camera after every change, with the worst-case number of simultaneous effects.
  - sound: judge the cue in the full mix of the game at the player's distance, on phone-like speakers as well as headphones.
  - UI: capture at phone and PC sizes in Studio device emulation, with thumbs and safe areas in mind.
  - space/level: walk the route at the game camera and speed; capture at the lowest and highest graphics settings.
  - cinematic: review the cut at the target device size with the HUD state players will have.
  - marketing art: check at 150x150 icon size and the measured tile size, on a phone, in the final layout.
  - design: play-test in the real build with the real tools, not on paper alone.
  - engineering: profile on a phone-class device with the expected player count.
- general check: The review packet contains play-mode captures at the game camera, at phone size, in the real place, with effects and UI on (plus `thumb_check.py` or `look_check.py thumb` for small views); no decision rests only on a turnaround, an editor view or a close-up.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, feature-builder, architect, reviewer, qa-lead
- rests on: CR-01, CF-02, CF-04, CF-07, WL-28, CD-07, VH-04, VC-06, SS-15, MD-02, VR-06, SD-24, LC-24, UI-03, WL-20, PP-33, VR-24, CR-17

### UP-03 Decide what is read first; spend contrast only there
- principle: Rank what must be noticed (first, second, third) and give contrast in that order. Contrast is every kind of difference (value, hue, saturation, size, shape, motion, loudness, timbre). To focus, first lower the contrast everywhere else; reserve the extremes (pure white, the most saturated colour, the loudest sound, the biggest motion) for the few things that matter.
- why: Attention goes to the strongest difference; if everything is loud, nothing is.
- in each medium:
  - picture/2D: one focal point with the full value range; background detail in values close to the background; read order planned and led by flow lines.
  - model: highest contrast and saturation on head, shoulders, hands and the source of power; the rest quieter; extremes only on small accents.
  - motion: the key pose and the hit get the clearest silhouette and the biggest change; the rest supports.
  - effect: rank effects by importance and cap size, brightness and duration per tier; inside one effect, primary over secondary over tertiary; nothing blows out: clipped white only at the single focus on the peak frames (1-2 frames), a large white core only at the top tier (VC-07) (lead fix 2026-10-22: "never blow out to white" contradicted VC-07's focus exception).
  - sound: the important cue gets the unique timbre, the space before it and the highest priority in the mix; small sounds carry only up close.
  - UI: one attention motion at a time; the critical state in a fixed, prominent position; the brightest element is the next action.
  - space/level: value bands per layer (environment narrowest, characters wider, VFX and UI the extremes); light and saturation lead to the objective.
  - cinematic: light, framing and motion converge on the subject of each shot.
  - marketing art: the hero has the highest contrast and the largest readable area; the title has calm room.
  - design: celebrations, rewards and threats are tiered so the rare and important feel bigger.
- general check: `look_check.py value` with the focal item as subject: the subject has the widest luminance spread and the ring a narrower one; in a blurred or thumbnail capture (or a solo-then-mix listen) the first thing noticed is the intended one.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, reviewer
- rests on: VC-01, VC-04, VC-05, VC-07, VC-08, VH-01, VH-02, VH-06, VH-09, LC-12, LC-17, CF-08, VR-02, SD-09, UI-10, UI-13, GD-02, VR-19

### UP-04 Big before small: silhouette, value and composition before colour and detail
- principle: Solve the big read first and lock it: silhouette and pose, then value structure and composition, then light, then colour, then detail and effects. Work in passes over the whole piece; never finish one part while the rest is blank. No detail rescues a big read that fails.
- why: Big decisions are cheap to change early and decide the read; detail done on a wrong base is wasted and hides problems.
- in each medium:
  - picture/2D: flat two-tone or grayscale roughs first; colour on top of an approved value version; glow last.
  - model: blockout and proxy at the game camera, then flat material regions, then shading, then detail; forms before prettiness.
  - motion: root and centre of gravity first, then whole-body key poses, then offsets, then hair, fingers and face.
  - effect: shape, colour role and timing first; the core read before sparks and polish.
  - sound: the main gesture and envelope of the cue first, then layers, then processing and sweetening.
  - UI: the flow and wireframe first, then layout, then style, then motion.
  - space/level: blockout and routes, then composition and kit, then set dressing, then lighting and post effects last.
  - cinematic: beats and blocking first, then camera, then light and effects.
  - marketing art: composition in the final frame first, then light, colour and effects.
  - design: the core loop proven in a greybox before any feature, system or art.
- general check: An approved blockout, rough or grayscale exists and is dated before the first detail, colour or polish pass; in each review render no region is clearly more finished than its equals; a grayscale or black-fill of the current pass still reads.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, reviewer
- rests on: SS-01, CF-01, VC-02, VC-03, VC-13, VH-11, LC-11, MD-04, WT-05, UI-01, PI-04, PI-06, PP-26, GD-15

### UP-05 Shape and silhouette carry identity and meaning
- principle: The outline is the first read. A character, item or effect is recognised by a few big identifying shapes; shape language carries meaning (sharp reads dangerous, round reads friendly, square reads stable); and one shape vocabulary runs through the whole game. Judge shapes filled solid and small.
- why: Shape survives distance, motion, colour blindness and tinted light; lines and fine detail do not.
- in each medium:
  - picture/2D: fill the silhouette to judge it; broad cuts, not notches; size steps (big, medium, small).
  - model: 3-4 identifying elements made chunky; signature proportions kept; nothing drapes in front of the arms.
  - motion: a clear line of action in every key pose; the signature shape stays visible; extremities stay trackable.
  - effect: a game-wide shape code (heal, shield, damage) readable in grayscale.
  - sound: the audio equivalent is a signature tone per weapon or character and transients that match the shape language (sharp for aggressive, soft for gentle) [inference].
  - UI: icons and frames follow the game's shape vocabulary; a motif still reads as a one-colour icon.
  - space/level: the landmark is the tallest, clearest shape; directional shapes point to the goal; collision shapes stay simple and predictable.
  - cinematic: group silhouettes and scale contrast tell the story beat.
  - marketing art: the hero's identifying shapes fill the crop; the icon reads in black-fill at 150x150.
  - design: roles and threats read from shape and size (bigger reads more important).
- general check: Black-fill at the game camera and at thumbnail size (`look_check.py silhouette`): a fresh agent names the subject, its owner or role, and its mood (dangerous or friendly) from the fill alone, and it differs from its nearest neighbours.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, reviewer
- rests on: SS-02, SS-03, SS-04, SS-05, SS-06, SS-07, SS-10, SS-13, SS-15, VH-07, VH-08, VH-10, CD-04, VR-05, SD-21, CF-14, WL-15, RI-28

### UP-06 Less is more: few elements, rest areas, indicate instead of spelling out
- principle: Use the fewest shapes, colours, layers and details that give the strongest read. Clump detail in a few chosen places and leave areas of rest. Indicate masses (hair, grass, crowds, materials) with a few strong marks instead of rendering every part. Cut what the eye does not need.
- why: Every edge, colour and layer is a signal; together, and multiplied by motion and many players, they become noise that hides the read.
- in each medium:
  - picture/2D: one message, one symbol; limited palette in roles (about 60/30/10); low-contrast background detail.
  - model: remove small details that do not change the outline or read; hair and fur as clumps; detail density follows display size.
  - motion: a few clear poses and holds instead of constant busy motion; secondary motion only where it adds value.
  - effect: one main hue per effect; few tertiary particles; small footprints; ambient effects tiny and slow.
  - sound: cut unneeded frequencies first; one layer owns the low end; small sounds stay short and close.
  - UI: the HUD only as big as the genre needs; one job per element; one attention motion per screen.
  - space/level: rest areas in the player band; floors clean; detail clusters above head height or at edges.
  - cinematic: one subject per shot; layout clean before smoke and sparks.
  - marketing art: a clean backdrop and negative space for the hero and the title.
  - design: a feature earns its place against the target experience; "it would be cooler" is new scope.
- general check: Count distinct shapes, colours (`look_check.py palette`), layers or sounds against the brief's cap; at thumbnail size or in a solo listen, remove each small element in turn: if the read does not drop, it stays removed.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, reviewer
- rests on: VH-03, VH-04, VH-05, MD-01, MD-02, SS-04, LC-04, LC-19, VR-02, VR-06, VR-16, SD-11, UI-02, UI-04, CF-16, WL-19, PI-14, VR-24

### UP-07 One code for meaning across the whole game
- principle: Every signal that carries meaning (colour, shape, motion pattern, sound, screen position, material) means one thing everywhere in the game. Gameplay colours are reserved and kept out of decoration; one hue never means both help and harm; similar things behave the same way every time.
- why: Players learn the code once and read every new piece by it; a broken code sends a false signal and feels unfair.
- in each medium:
  - picture/2D: prompts state the colour-role table and the reserved hues; no reserved hue in set dressing.
  - model: team, faction and rarity colours follow the bible; materials that play differently look different.
  - motion: the same attack always has the same tell; one physics and gravity language for the game.
  - effect: colour roles and shape codes per effect type; the effect's hue sits next to its caster's.
  - sound: each floor material has one footstep sound; each weapon keeps its signature tone in every stage.
  - UI: a written rule sheet for colour, text style and screen position; one motion table per element type.
  - space/level: one orientation convention across maps; material follows the gameplay rule (shootable, climbable).
  - cinematic: story colours and light directions (bottom light = threat) used the same way each time.
  - marketing art: brand colours, fonts and naming patterns kept; one property changes per event.
  - design: consistent rules and telegraphs make failure learnable; hazards have written rules.
  - engineering: codes live as shared data (colour roles, motion tables, sound IDs), never hard-coded per script.
- general check: Sample colours, shapes, motions and sounds across captures and data tables against the code tables: any signal used for two meanings, or one meaning shown two ways, fails; on an environment-only capture, the share of pixels within a colour distance of each reserved swatch (authored and as rendered) outside gameplay objects is near zero; a k-means `look_check.py palette` merges small accents and cannot show it (lead fix 2026-10-22: same fix as the LC-01 check).
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, live-ops-designer, feature-builder, architect, reviewer, qa-lead
- rests on: LC-01, LC-02, LC-20, VR-05, UI-06, UI-15, SS-06, WT-02, GD-07, GD-13, GD-30, SD-21, SD-23, WL-11, WL-18, SI-14, LC-14, VR-25, VR-26

### UP-08 Timing tells cause and effect: tell, build, beat, hit, result
- principle: Every event is a short story with a beginning, middle and end: a readable tell or anticipation, a build that rises, a small beat before the release, one clear peak, and a result that starts after its cause. Vary the rhythm; keep the player's own actions responsive; one marker list keeps animation, effects and sound on the same frame.
- why: Players read cause from order and timing; uneven rhythm keeps attention; a hit lands only when picture and sound peak together.
- in each medium:
  - picture/2D: a still implies the moment with flow lines and a pose at the peak or just before it.
  - motion: short tight anticipation for the player, readable wind-ups for enemies; fast contact; uneven cadence; holds at key poses.
  - effect: the build grows in size and brightness, a beat, one peak flash, then the eye moves to the result; stages timed in 0.1-0.2 s steps.
  - sound: rising charge, a transient on the contact frame, a tail that sells the weight; one sound per named stage.
  - UI: feedback on the press frame; tweens short; reward motion from the source to its destination.
  - space/level: plan the opening seconds of a round and the rhythm of rest and action along a route.
  - cinematic: beats and cuts are marked frame-accurately and sound and effects follow the markers.
  - marketing art: the chosen moment is the peak of the action, read in one glance.
  - design: tension rises toward the climax; celebrations are short and end before the next decision.
  - engineering: trigger effects and sounds from the same client event; read animation markers instead of guessing times.
- general check: Frame-by-frame capture at 30 fps: label tell, build, beat, peak and result with start frames; each result follows its cause; the peak frames of animation, VFX and sound match (`clip_check.py events`); gaps between beats are not all equal; player input feedback appears within 1-2 frames.
- applies to: animator, vfx-designer, sound-designer, ui-ux-designer, film-director, marketing, game-designer, level-design, feature-builder, architect, reviewer, qa-lead
- rests on: WT-01, WT-11, WT-12, WT-13, WT-21, WT-23, RH-01, RH-03, RH-05, VR-09, CF-11, SD-05, SD-07, CC-02, UI-12, UI-14, GD-02, GD-11, GD-26, VR-22, UI-17

### UP-09 Push what must read past real, on a believable base
- principle: Things on a game screen are small, fast and seen in a glance, so what must read is pushed past reality: bigger hook shapes, stronger poses, clearer contrast, bolder sound. Exaggeration works only on a believable base: correct weight, contacts and anatomy everywhere else.
- why: Subtle features vanish at game size and speed; grounded basics earn belief for the extreme moments.
- in each medium:
  - picture/2D: extend and sharpen the features that must read; poses specific through adjectives, pulled back if too far.
  - model: hook shapes and signature items oversized; believable anatomy and attachments underneath.
  - motion: hang time, overshoot and smears on one or two signature moments; contacts and weight shifts correct around them.
  - effect: energy reads brighter and bigger than physics, but builds and falls off in a believable order.
  - sound: transients boosted, pitch shifted for size, layers that sell weight beyond the real recording.
  - UI: pop and bounce on rewards with a small overshoot; emotes and reaction icons at maximum expression.
  - space/level: landmarks taller and scale cues clearer than real; doorways sized for the camera.
  - cinematic: scale contrast (a giant behind small heroes) and camera angle push status and threat.
  - marketing art: big heads, pushed poses and contrast for a two-second read.
- general check: Side by side with a realistic version (proportion figure, linear clip, raw recording): the pushed features clearly change the outline or read at game size; the surrounding weight cues (contact, shift, arcs, believable joints) are all present.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, film-director, marketing, reviewer
- rests on: EX-01, EX-02, EX-04, EX-05, EX-07, EX-08, SS-03, SS-04, CD-10, WT-03, SD-07, SD-08, CF-06, CF-17, WL-21

### UP-10 The subject's character drives every choice
- principle: Know who or what you are making before choosing anything: a character's core and tension, a prop's or place's personality, a mechanic's verb, the story premise of a shot. Every shape, colour, pose, motion, sound and material must trace back to it; what does not is cut.
- why: Choices that follow one personality are consistent and specific; generic choices waste the chance to build identity.
- in each medium:
  - picture/2D: a character card and a sell list before any image; options judged against them.
  - model: proportions, face and costume pieces express the tension words; a prop has a personality in 3-5 words.
  - motion: ask how this character runs, not how a character runs; motion adjectives from the card.
  - effect: the effect's shape, colour and timing express the ability's verb and the caster.
  - sound: the theme comes from the gameplay verb (slows, stuns); a character sounds like its size, age and material.
  - UI: the UI's thematic and motion material come from the game's world.
  - space/level: each place states who lives here and what happened, and shows it.
  - cinematic: each shot has a premise and the character's subtext.
  - marketing art: the premise and the signature ability pose sell who the character is.
  - design: behaviour first; tuning numbers set tone as well as balance.
- general check: Each design choice in the hand-back traces to a line of the card or brief; a fresh agent shown the result without notes gives back the intended adjectives, verb or story fact.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, reviewer
- rests on: CD-01, CD-02, CD-09, CD-25, CD-26, SD-04, SD-22, SI-02, GD-05, RI-24, RI-27, WL-22, UI-07

### UP-11 One world, one style; identity survives every variant
- principle: Everything must look and sound like one game: a deliberate style with set levers, the art bible's anchors over any maker's habit, one palette and shape vocabulary, and identity anchors that every skin, tier, update and product keeps while the rest changes.
- why: A world made by many makers (and by an image model) drifts into generic or mixed work; players recognise and love specific characters and break trust when they drift.
- in each medium:
  - picture/2D: every prompt carries the art bible's style words and the approved anchors; results are compared with the anchors.
  - model: variants keep the anchors, proportions and contact points; new parts sample the existing palette.
  - motion: the character's motion style and signature moves stay recognisable in every variant.
  - effect: effects match the game's shape language and colour roles; reused layers are recoloured to the target mood.
  - sound: the game's sound section lists signature sounds and forbidden directions; variants keep the signature tone.
  - UI: one UI ecosystem from one thematic; style books chosen once per game.
  - space/level: one shape language and palette across maps; theme cues so no place is generic.
  - cinematic: likeness and palette match the in-game character; light and colour follow the art bible.
  - marketing art: brand pattern kept with one twist per event; likeness matches the game.
  - design: themes are chosen to fit the world's tone; top tiers may break the style only by a documented decision.
- general check: Place the new piece next to 2-3 approved anchors at the same size: it reads as the same game; every listed identity anchor is present in each variant (`look_check.py silhouette --compare`, `palette --roles`).
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, live-ops-designer, reviewer
- rests on: SI-01, SI-03, SI-06, SI-07, SI-09, SI-14, SI-19, CD-04, CD-06, SS-06, LC-05, LC-03, UI-07, SD-21, CC-01

### UP-12 Controlled variation and life, never exact repetition
- principle: Real things vary: small shifts in hue and value, irregular edges, asymmetry, offset timing, used and lived-in surfaces, randomised repeats. Add controlled variation so work feels hand-made and alive, never so much that it becomes noise.
- why: Exact repetition and perfect uniformity read as machine-made and dead, a high risk for AI-made work; variation inside a system reads as life.
- in each medium:
  - picture/2D: no flat fills; hue-shifted shadows; ask for imperfection and wear in prompts.
  - model: slight bevel and shape variation, wear where hands go, one asymmetric element, no visible tiling.
  - motion: no twinning: offset paired limbs and vary angles; secondary motion with offsets.
  - effect: random rotation and size on repeats; layers blend instead of popcorning.
  - sound: several takes and small pitch variation per play; long beds from spliced takes; loops that do not repeat audibly.
  - UI: variation lives in style and secondary screens; core controls stay consistent (UP-07 wins over variation).
  - space/level: lived-in story details; kit pieces rotated so no duplicate is seen twice in one view.
  - cinematic: crowds and backgrounds vary in pose and timing.
  - marketing art: avoid the generic first output; one unexpected element.
- general check: Look for exact repeats in captures (same piece at the same angle, mirrored marks, identical limbs on the same frame, the same sample twice in a row); fail on flat or one-hue materials (chromaticity spread over small blocks on one lit side under its limit, LC-09; a k-means cluster count passes value texture in one hue) (lead fix 2026-10-22: same fix as the LC-09 check); and check variation stays inside the colour family and value band.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, reviewer (lead fix 2026-10-22: ui-ux-designer added; the UI line already holds)
- rests on: MD-09, MD-10, LC-07, LC-09, SS-16, RH-02, WT-24, WT-25, VR-11, VR-14, SD-20, SD-29, WL-22, PP-24, RI-21, RI-23, VR-25

### UP-13 Problem, constraints and target before making anything
- principle: Before the first image, clip, cue or line of a spec, write what problem it solves, the constraints (target experience, camera, device, budget, rig, mechanics and numbers, theme) and what the end should look like. A reference or prompt is intent; constraints decide what is built, and deviations are said out loud.
- why: Work without a target does not move the team; constraints narrow the search and prevent endless spinning; if the maker cannot see the end, nobody else can.
- in each medium:
  - picture/2D: the reference-images request names the problem, constraints and success test, plus the sell list.
  - model: triangle and texture budgets, rig sheet, camera and contact points are read before modelling.
  - motion: frame length, markers and gameplay window agreed with design before keying.
  - effect: shape, colour role, timing and the particle budget written before building.
  - sound: the cue card names job, story point, emotion, verb and hearing distance before generating.
  - UI: the flow, device targets and the information each element must give come before style.
  - space/level: route, objective, spawn and the gameplay read of each piece come before dressing.
  - cinematic: premise, beats and the player's role come before shots.
  - marketing art: the launched thing and the promise come before composition.
  - design: the target experience (type of fun), the genre's demands and the four game components come first.
  - engineering: the behaviour contract and the engine's limits come before code.
- general check: The brief has problem, constraints, target experience and success test before any output; the hand-back lists every deviation from the reference with its reason.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, progression-designer, live-ops-designer, architect, feature-builder, orchestrator, reviewer
- rests on: RI-03, RI-04, GD-03, GD-04, GD-09, GD-22, CD-02, PP-01, CC-01, SD-01, UI-01

### UP-14 Research, then many distinct options, then a reasoned pick
- principle: Start from research and reference (the game's own anchors, then the real world), make many quick options with distinct hooks rather than one polished guess, include one unexpected or radical option, and pick with stated reasons against the brief. The first output is a warm-up.
- why: Breadth means the chosen direction beat real alternatives; real reference adds what invention misses; reasons make the pick reviewable.
- in each medium:
  - picture/2D: a narrow moodboard with pillars; 6-12 rough options across directions [inference]; one recommended with a reason.
  - model: real references per material; ortho views; options on an in-game mannequin.
  - motion: motion reference and a written beat sheet before keying; two timing alternatives on key clips.
  - effect: observed reference of the real phenomenon; bracketed values compared at the game camera.
  - sound: several texture-based prompts and takes per layer, one odd variant, picked by listening against a reference.
  - UI: a structural study of 2-3 strong references before the new design; layout options before style.
  - space/level: reference of real places for unique details; layout options tested in play.
  - cinematic: thumbnails of distinct shot ideas before the animatic.
  - marketing art: about 3 distinct thumbnails, then variants of the pick; options at equal finish.
  - design: several concept pitches with a recommendation; ideas from outside the genre.
- general check: The job record shows the research board, the count of distinct options (black-fills or summaries differ), at least one non-obvious option, and the pick with a reason tied to the brief; no single option was polished before the pick.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, live-ops-designer, orchestrator, reviewer
- rests on: RI-05, RI-08, RI-10, RI-16, RI-17, RI-18, RI-19, RI-21, RI-23, RI-24, SD-28, SD-29, PI-08

### UP-15 Cheap stages first; gates freeze decisions; do not be precious
- principle: Do the cheapest stage first and expect big changes there; show work early and often; move through gates that freeze each level of decision (rough, approved direction, materials, polish) and never reopen a closed door without a new decision. Most attempts fail: delete, redo and let go of your own idea when a better one appears.
- why: Change costs rise at every stage; late reveals waste the most work; attachment blocks necessary change.
- in each medium:
  - picture/2D: loose roughs are disposable; the pick freezes the direction.
  - model: proxy in game before detail; after the direction gate, no proportion or layout changes.
  - motion: blocking before splines; a broken section is re-keyed, not patched.
  - effect: greybox timing with placeholder sprites before final textures.
  - sound: rough cues in the mix early; final processing after the timing locks.
  - UI: wireframe gate before visual style; style gate before motion polish.
  - space/level: blockout played before art; lighting only after the last route change.
  - cinematic: animatic gate before final shots.
  - marketing art: thumbnail gate, green light, render, polish.
  - design: the crudest playable prototype before any art; closed directions logged.
  - engineering: a behaviour contract and a spike before the full build.
- general check: The job record shows rough states shown before polish, a gate record per stage with a capture, no layout or pose change after the direction gate, and no closed direction reproposed without a new owner decision.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, architect, feature-builder, orchestrator, reviewer, qa-lead
- rests on: PI-01, PI-02, PI-03, PI-04, PI-05, PI-09, CR-07, GD-15, CF-01, UI-01

### UP-16 Critique against the goal, one named problem at a time
- principle: Judge and give notes against the stated goal, never taste ("which reads as most dangerous?", not "do you like it?"). Find the problem behind each note, name its layer, fix the worst problem first, show visual fixes as paint-overs, refresh your eyes (mirror, grayscale, another reviewer), and report your own weaknesses honestly.
- why: Goal questions make every reviewer judge the same thing; named causes give fixes; vague or literal notes cause rework.
- in each medium:
  - picture/2D: paint-over notes on a capture; flipped and grayscale self-review.
  - model: notes name the layer (silhouette, value, colour, material, detail) and keep the identity anchor.
  - motion: each pass fixes the single worst-feeling problem; the curves are read, not only the picture.
  - effect: bracketed options compared against the brief's read; the self-check list (what is covered, what is blocked).
  - sound: notes in technical terms with a direction; solo listen, then full mix.
  - UI: changes name the pain point they fix and where it was observed.
  - space/level: self-review names dead space, oversize and unreadable spots.
  - cinematic: notes name the beat and what the viewer should understand there.
  - marketing art: options judged against the brief first; ties go to the owner with a recommendation.
  - design: notes are tagged goal or tactic; the lead curates the best solution from every source.
  - engineering: review findings name the failure scenario and its evidence.
- general check: Every review note names the goal, the layer and a concrete fix (or a paint-over); the hand-back maps each note to done or questioned and lists at least one honest weakness or says why there is none.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, live-ops-designer, architect, feature-builder, orchestrator, reviewer, qa-lead
- rests on: CR-02, CR-03, CR-04, CR-05, CR-06, CR-08, CR-09, CR-11, CR-12, CR-13, CR-15, PI-07, SD-26, SD-27, PP-21, CR-17, WL-30

### UP-17 Build for the next craft and for the engine
- principle: Every piece is made to be used by the next maker and to run in the real engine: ask the next craft what it needs, deliver it (views, markers, joints, layers, data), leave room for its decisions, stay inside the budgets, reuse before making new, and keep content as data.
- why: Work that is a pain downstream breaks every later step; expensive work that does not show steals budget from what does.
- in each medium:
  - picture/2D: concept sheets give the views and notes the modeler and rigger need and mark motion and effects as intent, not settings.
  - model: built to the shared rig and budgets; moving parts with pivots; clean meshes, UVs and collision; separable parts.
  - motion: frame lengths and named markers delivered in the contract; clips made to blend.
  - effect: one root for scaling; reuse the effect library; within particle caps.
  - sound: cues keyed to animation markers; a building-block library; cue names mapped to asset IDs in data.
  - UI: shared components, tokens and a motion table in data.
  - space/level: art snapped to the approved blockout; kit and zoo reuse; collision unchanged without sign-off.
  - cinematic: switchable layers and named groups for variants.
  - marketing art: layered masters and crop-safe composition for the whole asset kit.
  - design: tuning lives in data tables; cosmetic and feature costs are written before approval.
  - engineering: export and import steps are scripts; one owner per file; repeated manual steps become tools.
- general check: The downstream hand-back lists zero unanswered questions; budgets measured within target; reused assets named; no hard-coded content IDs or numbers in logic; a repeated manual step has a tool ticket.
- applies to: art-director, reference-images, modeler, character-rigger, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, architect, feature-builder, orchestrator, reviewer
- rests on: CC-02, CC-03, CC-04, PP-01, PP-11, PP-12, PP-14, PP-15, PP-25, PP-28, PP-29, PP-32, VR-08, VR-17, SD-30, GD-31, VR-20

### UP-18 Know when it is done
- principle: Work is never finished, only stopped. Set a budget (time, passes, iterations) and written stop criteria before starting; finish each artefact only as far as its user needs; stop when the criteria hold or the notes start repeating; new ideas past the gate become follow-ups.
- why: Past the useful point extra work is invisible to players and costs time; a time box forces the choice that reads.
- in each medium:
  - picture/2D: a concept stops when shapes, values, colours and focal point are settled; it is a blueprint, not the product.
  - model: stop when every material reads at game size, the finish matches the anchors and no area looks incomplete.
  - motion: body mechanics before polish; hair and face as the last 10 %; the lead calls done.
  - effect: stop when the read, timing and budget pass at the game camera.
  - sound: stop when the solo and mix listens pass; stand-ins are named, not hidden.
  - UI: stop when the flow, states and motion table pass on phone and PC.
  - space/level: stop when the routes, reads and budgets pass at low and high settings.
  - cinematic: stop when the beats read at target size and the cues hit their markers.
  - marketing art: stop when every crop passes at real size.
  - design: a map or feature is revisited from evidence later; it is never "done forever", but each update closes.
- general check: The brief states budget and stop criteria; the hand-back states the budget used and shows each criterion passing; note rounds end when a round brings no new notes.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, live-ops-designer, orchestrator, reviewer, qa-lead
- rests on: PI-11, PI-12, PI-13, PI-14, CD-08, CR-12, GD-33, SD-28

### UP-19 Feedback follows the real outcome
- principle: The size of a response matches what really happened. Every input gets an instant small cue; the big response comes on the confirmed result, graded by causes the player can learn; frequent things stay short and quiet; nothing is amplified past the outcome, celebrated before it is confirmed, or dressed to suggest a better result than the real one.
- why: Feedback tied to real success builds the player's sense of competence; feedback louder than the outcome, early, or misleading lowers it and breaks trust (DS evidence base, GD-34).
- in each medium:
  - picture/2D: reveal and reward images show the tier the player actually gets; no rarer-looking frame on a common result.
  - model: rarity and power tiers differ in silhouette and finish by their real rank (SI-20); a cheap item does not wear the top tier's look.
  - motion: the attempt animation is small and quick; the big contact pose, hit-stop and follow-through scale with the confirmed hit's strength.
  - effect: the attempt cue plays on the input frame; the punch layer plays only on the confirmed event, sized by its tier; frequent effects are shorter, merged and capped.
  - sound: a tick on input; the reward or impact sound on confirmation, its weight by tier; one sound per merge window.
  - UI: press feedback within 100 ms; success only on server confirmation, with a pending state when slow; counters show the true value.
  - space/level: rewards and new views sit at real achievements and natural pauses.
  - cinematic: a victory or reward sequence plays only after the result is confirmed and can be skipped.
  - marketing art: no claim of rewards or rarities the game does not give.
  - design: escalation tiers step at real outcome thresholds; paid random reveals keep the same windup for every result and never fake a near-miss.
  - engineering: play the attempt cue on the client at once; play the outcome layer when the server's confirmation arrives; a rejected request never shows the success layer.
- general check: Send a request the server rejects: no success layer, sound or celebration plays; miss, hit, blocked and big-hit outcomes are distinct with sound off; a frequent event at its real rate shows one label per merge window and no tail build-up; the lowest and highest paid-random results share an identical windup.
- applies to: animator, vfx-designer, sound-designer, ui-ux-designer, film-director, marketing, game-designer, progression-designer, live-ops-designer, feature-builder, architect, reviewer, qa-lead
- rests on: GD-34, GD-35, GD-02, VH-02, UI-12, UI-19, VR-22, VR-24

### UP-20 Every player can read it: never one channel, and every intense channel can be reduced
- principle: Meaning never rides on one channel: colour pairs with shape, icon or text; sound pairs with a picture; a warning pairs with a second cue. Flashes and pulses stay within safe rates, and every intense channel (shake, flash, full-screen tint, fast motion) has a reduced version that keeps all the information.
- why: Colour-blind players (about 8 % of males, per DS), players on muted phones or in bright sun, and players sensitive to motion or flashes all miss single-channel signals; a reduced mode that drops the warning is unfair to exactly them.
- in each medium:
  - picture/2D: tiers, teams and states read in grayscale; tier names are written, not only coloured.
  - model: team and rarity differ in shape or trim, not only in tint.
  - motion: telegraphs show in pose and silhouette as well as in effects; reduced motion removes camera-driven motion, not the pose.
  - effect: danger edges are a brightness and shape cue, not hue alone; composite flashes stay at most 3 per second (design target 2); every shake, flash and screen tint has an off path.
  - sound: no gameplay meaning is sound-only; every important cue also shows on screen.
  - UI: colour plus icon plus text for status; reduced motion snaps or fades tweens; critical markers keep about 3:1 contrast against their background.
  - space/level: hazards read by shape and material with colour removed; fog and dust never hide a hazard or the route.
  - cinematic: no strobing cuts or flashes above the safe rate; the story beat reads with sound off where play depends on it.
  - marketing art: the promise reads in grayscale at icon size.
  - design: the settings list (shake, flashes, screen effects, reduced motion) is part of the feature spec; safety faults block release.
  - engineering: read GuiService.ReducedMotionEnabled; comfort settings change only the local screen.
- general check: Capture the busiest scene in grayscale, with sound off and reduced motion on: every threat, pickup, team, tier and outcome is still identified; count large-area flashes per second on the composite (at most 3); each intense channel in the spec names its off path.
- applies to: art-director, reference-images, modeler, animator, vfx-designer, sound-designer, ui-ux-designer, environment-designer, level-design, film-director, marketing, game-designer, feature-builder, reviewer, qa-lead
- rests on: LC-01, VR-05, VR-13, VR-23, VR-26, UI-11, UI-18, VC-06
