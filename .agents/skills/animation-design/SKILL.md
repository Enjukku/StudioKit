---
name: animation-design
description: What and why of motion for anything that moves in Roblox - characters, creatures, held items, props, mechanisms, vehicles, buildings, ambient loops. Read what must move; choose poses, timing, spacing and the cheapest technique; judge the read. Use for "make it feel heavy", "it looks floaty / stiff", "players can't read the attack", rig-pipeline S1/K2. Animator reads first; animation-craft is how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J006 from owner material. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence stays out of the body: `knowledge/reference/animation/` (paper notes, fact-checks) and the craft library `knowledge/reference/craft/riot/` (§9 follows its `universal-principles.md`). Tags: [V] verified, [E] expert experience, [O] studio opinion.

# Animation design: what moves, why, and how it reads

## 1. When this skill starts
Before any key is set, for anything that moves: the read, who reacts, what drives each part, the technique, the clips and states, the timing contract, and how the result is judged. `animation-craft` is how to build and play it; `rig-pipeline` is the shared workflow when a rig is needed.

**Three jobs, in this order.** Game motion must (1) show the action clearly: what it is, where it goes, when it lands, whose it is; (2) make motion and physics believable and consistent, so players can predict it; (3) give the subject personality. Ask of every clip: what is happening, does it feel physically right, could it belong to any other character?

**Governing idea [O]:** good motion is cause and effect the viewer can follow: what intends, what pushes, what supports, what happens, what results. More keys, bones, noise or generated clips do not build that chain. Work in this order: the motion idea, the performance, the runtime asset; and big before small at every stage (root and poses, then offsets, then hair, fingers and face).

**There is no single recipe.** A knight, a drawbridge and a flag move for different reasons; write the reason for every choice. Method is open (pose to pose or layered from the root); only the result is judged, at the game camera, at phone size, in the real place. A number that no source, owner or measurement gives is UNKNOWN, never a default; a starting value from this skill is a PROPOSAL that a check may change.

**After a context compaction**, re-read §8 and §9 of this file before you hand on a plan: only the start of a skill survives compaction.

## 2. Read this file when
| You need | Open |
| --- | --- |
| The principles in full: when each applies and its sign in the clip | `references/principles.md` |
| A worked example per kind (emote, attack, creature, pet, sword, door, drawbridge, chest, egg, trap, vehicle, building, flag) | `references/worked-examples.md` |
| Body parts and species, faces, the motion profile, reference | `references/body-and-species.md` |
| Animation sets, states, transitions, interruptions, loops, idles, variants | `references/sets-and-states.md` |
| Game timing: who reacts, the timing grammar, windows, the shared event timeline, verbs and state tells, sync, hit-stop, attempt vs outcome, reduced motion | `references/game-timing.md` |
| The self-review lines per pass, pass/fail rows, common failures, the image budget, when to stop | `references/review.md` |
| Templates: motion profile, animation set, timing list, motion spec | `templates/anim/` |
| How to build it (Blender keying, game-camera and black-fill renders, export, Roblox playback, code-driven specs, loops at scale) | `animation-craft` skill |
| The rig workflow (S1, K2, S6, S7), rig sheet and rig notes | `rig-pipeline` skill |

## 3. Steps
1. **Read the brief for the read.** What must the player understand, and by when? **Who must react:** the player reading an enemy's or hazard's tell (it must last long enough to react to) or the player doing the action (it answers the input at once and stays tight). Also: what moves, its size on the phone screen, the game camera, how often it plays, what interrupts it, the gameplay window (from its owner, never invented), and whether the outcome is server-confirmed (the clip shows the attempt; confirmed-outcome motion is its own layer). Write 2-4 feel words, each with one visible change ("heavy: wider, lower stance, longer settle"); when the brief names the target players, add one line on what they want to see. *Check: read, who reacts, rate, windows (or UNKNOWN with owner), feel words with their visible change.*
2. **Study the whole subject before moving it.** Multi-view renders (front, back, sides, raised ¾, the game camera) with a player-sized reference. One record per visible part: what it is, what carries it, whether it bends, active / passive / rigid / mechanical, or "does not move". Names prove nothing; mass is UNKNOWN unless supplied. List the 2-5 **identity anchors and hook shapes** (signature item, headpiece, ponytail, the source of power) that must stay visible at key poses, and the sides the camera sees most. A body shape that disagrees with the wanted motion (a heavy silhouette asked to move daintily) is a question for the art director, not something to hide in keys. *Check: every part has a record; anchors listed with the side the camera sees.*
3. **Choose the technique per moving part** (§5) and write the reason and the docs page. A rig is needed → `rig-pipeline` S1 (motion profile, ROM with units, stress poses that also test costume near joints, clip list) with the rigger; flag costly parts (capes, long hair chains) with a cheap fallback. No rig (a rigid door on a hinge) → a motion spec for the builder. *Check: every moving part has a technique, a reason and a docs path.*
4. **Write the set** (`references/sets-and-states.md`, `templates/anim/animation-set.md`): clips from the implemented states and transitions, each with entry and exit pose, loop policy, interruption rule, priority intent, blend owner, attachments and events; plan the state machine with the builder who codes it, and make clips to blend. An action the game does not need is marked absent. *Check: every gameplay state has a clip, a spec or a deliberate "absent".*
5. **Act it out on paper and gather reference.** Before any key, a beat sheet per clip that carries the read: per beat, what the body does and what drives it, the time (window or PROPOSAL), a sound word ("hup... ka-THUNK") and the subtext (what the character wants). For an ability, name its mechanic verb (slows, stuns, knocks back). Reference for anatomy, action, speed and load, not looks; order, and how to make a missing one: `references/body-and-species.md` §6. Take ideas, never copy a clip. *Check: beat sheet with times, sound words, subtext (and verb); every key pose has a reference.*
6. **Thumbnail the key poses.** For each clip that carries the read (a tell and contact, a signature move, an emote, the personality idle), pose 2-3 clearly different options of its key poses fast on the real or proxy rig, at equal finish; one pushes further (a stronger line of action, or a pose against the character's known trait for comedy). Render them as black-fill at the game camera and tile them into **one contact sheet per clip** (image budget: `references/review.md` §5). Pick with a goal question ("which reads as an overhead slam at phone size?"); record the pick and why each other option lost. Signature, tell and emote clips also get two timing takes on the same poses, compared by their beat gaps; until the owner picks on the playable previews at the next gate, the take with the better recorded reasons is used as a PROPOSAL (`references/review.md` §1 item 5). *Check: one contact sheet per key clip; a recorded pick with reasons.*
7. **Plan each clip's poses and timing** (§4; `references/game-timing.md` §7): tell → build → beat → hit → result. Key poses tell the story; breakdowns are placed on purpose; the accent sits at the gameplay event; holds keep an idea; the gaps between beats differ; anticipation is sized by who reacts. Gameplay windows are fixed inputs. *Check: each clip names its key poses, its accent event and its window; its beat gaps are not all equal.*
8. **Draft the timing list** (`templates/anim/timing-list.md`; `rig-pipeline` §5): named events, seconds plus source frame and frame rate, meaning, owner, consumers, interruption rule; the same stage names and verb as the VFX frame script and sound cue card; a building end-of-state tell for any state with a timer or breaking point; the sync rule (`references/game-timing.md` §4). *Check: VFX and sound can read every event they need from it.*
9. **K2 (when rigged):** the rigger's plan answers every motion need, including shoulder and hip controls, a way to hold the head's world orientation through a spin, finger or hand-shape controls where hands must read, and control of every hook-shape part. Sign, or send one note. A "not supported" that changes the look goes to the lead for the owner.
10. **Judge it** (`references/review.md`): the read first, at the game camera, at phone size, in the real place with effects on; then the defects; the key frames in black-fill; with effects hidden and reduced motion on. You see stills: judge timing from sample numbers and frame strips at a known rate; feel at normal speed is the owner's call on a playable preview. *Check: the review lines for the pass have evidence.*

## 4. Principles as decisions (summary; when each applies and its sign in the clip: `references/principles.md`; the checks: `references/review.md` §8)
Each is a tool to diagnose with, not a dial to turn up everywhere. Use the one the read needs.

| ID | Decide | Ask |
| --- | --- | --- |
| P-01 | **Cause first** | What intends, pushes, supports, results? |
| P-02 | **Weight and support** | Where is the centre of gravity, what is planted? |
| P-03 | **Timing makes speed and weight** | Where does it hold, where does it snap? |
| P-04 | **Spacing, not one ease** | Which segments ease, snap, keep speed? |
| P-05 | **Arcs** | What path does each landmark draw from the game camera? |
| P-06 | **Rhythm and asymmetry** | Is the cadence even? Do limbs twin? |
| P-07 | **Silhouette at the game camera** | Does the black shape read at phone size? |
| P-08 | **Character drives choices** | How would this character do it, and why? |
| P-09 | **Active vs passive parts** | Does this part drive or follow? |
| P-10 | **Overlap and follow-through with a cause** | What settles after, and why? |
| P-11 | **Holds keep an idea** | Freeze, breathing hold or a gaze shift? |
| P-12 | **Push the read on a believable base** | Which one or two moments must read stronger than real? |
| P-13 | **Effort order** | Root, pose and flow right before detail? |
| P-14 | **Gameplay timing is fixed input** | Window, accent event, cancel point? |
| P-15 | **Mechanisms move like their mechanism** | Hinge, rail, gear, piston, rope? |
| P-16 | **Method is open, the result is judged** | Layered root-first or pose-to-pose? |
| P-17 | **Anticipation is sized by who reacts** | Must the player dodge this, or is it their own move? |
| P-18 | **The source of power is the primary read** | Blade, casting hand, jaw? |

## 5. Technique choice (decide per moving part; facts and docs paths in `animation-craft` and `knowledge/reference/animation/fact-check-techniques.md`)
| Technique | Choose when | Avoid when | Who builds |
| --- | --- | --- | --- |
| **Keyed clip on a rig** (Bones bend, Motor6D for rigid pieces) | the shape bends; many parts with authored timing; acting, contact or gameplay information must repeat exactly | one rigid piece on one axis | animator with the rigger (`rig-pipeline`) |
| **Code-driven** (TweenService, CFrame / PivotTo on the client) | rigid, few axes, simple curve: doors, chests, platforms, pickups | it bends or needs many timed parts; a server-side cosmetic tween replicates every frame | animator's motion spec; a builder codes it |
| **Physics constraints** (hinges, sliders, springs, motors) | it must react to players, weight or collisions | every client must see the same, or it decides gameplay without the physics owner | builder with the physics owner; animator's feel targets |
| **Texture or flipbook** | surface detail: water, belts, fire, glow, distant crowds | the silhouette must move | VFX or builder; animator states the rhythm |
| **Procedural layer on a clip** (IK, look-at, spring) | input keeps changing (aim, uneven ground) and the result can be bounded and tested | the part carries intent (a pointing tail is never a free spring) | builder, from the animator's limits |

- **Cheapest that looks right wins**, measured, not assumed; for many copies, cost per copy and phone budgets decide (`performance`; `animation-craft` §6).
- **Visual motion is never physics or gameplay authority** [V]: bones move the picture, not the collision shape; a marker is presentation, never damage. The picture still tells the truth: no swing implies more reach than the hit area; a danger pose ends with the danger.
- **Squash and stretch need a Roblox route** [V]: a clip cannot scale a part (a keyframe pose stores position and rotation only). Use a mesh swap, code-driven scale on a separate part, a VFX ring, dust or trail, or bone scale only after a Studio probe proves it; keep the volume.

## 6. Kinds of objects (detail and a worked example each: `references/worked-examples.md`)
| Kind | What usually decides the motion | Usual technique | Joins |
| --- | --- | --- | --- |
| Characters (locomotion, actions, idles, emotes, reactions, cutscene acting, promo stills) | support, weight, intent, personality, windows, who reacts; a promo or cutscene still reuses the signature key pose (P-06.11) | keyed clips on a rig | rigger, game-designer, film-director, VFX, sound, marketing |
| Creatures and pets | anatomy, active vs passive appendages, gait; giants move slowly; the movement pattern is the character; a timed or breakable state gets a building tell | keyed clips; LOD variants for crowds | rigger, game-designer |
| Held items | grip, mass and arc with the body (heavy reads close); follow-through; readiness beats; room for moving parts | keyed on the character rig with item sockets | rigger, VFX, sound |
| Props and mechanisms (doors, chests, levers, traps, reveal eggs) | pivot or rail, actuator, travel, hard stops; a personality in 3-5 words | code or physics for one axis; keyed when linked parts move | builder, game-designer |
| Vehicles and mounts | suspension and wheels follow the real motion; the gait carries the rider | physics or code body; keyed rider and mount | builder, physics owner, rigger |
| Buildings (build-up, transformation, collapse) | arrival order; a clear end state; stress before a collapse; collision kept apart | keyed or code sequence; physics debris by its owner | environment-designer, VFX, physics owner |
| Ambient loops (flags, windmills, plants) | calm, varied rhythm that never pulls the eye from play; sway follows the gesture; cost per copy | texture, client code, short looped clip | environment-designer, performance-engineer |
| Out of scope | cutscene camera (film-director); UI motion (ui-ux-designer); camera shake and screen effects (VFX) | — | — |

## 7. Rules (final check)
- Never invent a mass, delay, anticipation, hold or hit-stop length, spring constant, stretch percentage, foot-slide tolerance, phone budget or frame count; mark UNKNOWN or PROPOSAL and name the owner.
- Never retime a gameplay window to fit a clip; place beats inside it and report a conflict.
- Never let VFX, colour or the camera carry a read the pose should carry: a tell, a contact and a hit read with effects hidden and reduced motion on.
- Never ship a clip with only its start and end keys (the blend twists the body through itself); every breakdown is placed.
- Never play confirmed-outcome motion (big hit reaction, hit-stop pose, celebration) before the outcome is confirmed.
- Paid random reveals (eggs, crates, chests bought with real or bought currency): the same windup for every result, no near-miss motion, no rarity hint before the result frame (load `platform-policy`).
- Never work around a missing degree of freedom (bending a tool, a wing through the body): one rig note with alternatives (`rig-pipeline` §4).
- Never ship generated motion without review, provenance and a rights check.
- Judge at the real camera and phone size, never only in the editor or a beauty shot. Plan-stage images keep their own budget (`references/review.md` §5).
- The owner approves feel and look; a score or a famous studio's style never replaces that. "It would be cooler" mid-job is new scope: a ticket, not a silent addition.

## 8. Self-check before handing on the plan
- [ ] The read, who reacts, the rate, the feel words with their visible change, and the gameplay windows (or their UNKNOWN owners) are written.
- [ ] Every visible part has a record; anchors and hook shapes are listed with the side the camera sees; every moving part has a technique, a reason and a docs path.
- [ ] The set covers every implemented state and transition; absences are deliberate.
- [ ] Each key clip has a beat sheet with a subtext line (and a verb for abilities), references, and a recorded pick from one black-fill contact sheet at the game camera.
- [ ] Each clip names its key poses, its accent event and its window; enemy tells are sized to the reaction window, the player's own moves stay tight.
- [ ] The timing list has every event VFX, sound and UI need, with seconds, source frame and frame rate, end-of-state tells, and the sync rule.
- [ ] No number without a source, owner decision, measurement or PROPOSAL label; plan-stage image count reported.

Project overlay: if `knowledge/overlays/animation-design.md` exists, read it after this file; it wins for this game.

## 9. Core principles for this craft
The studio's universal principles, stated for animation: the standard, a short example, a check you can run, and where the depth sits.

| # | Principle, for my work | Example | Check | Where |
| --- | --- | --- | --- | --- |
| 1 | **The gameplay read comes first:** what, where, when it lands, whose, before any flourish. | A slam tell reads before the cape swirl; the swirl is cut where it covers the arms. | Frame-step the game-camera capture at phone size: action, direction and landing frame named from the pose alone. | §3.1, P-01, P-14 |
| 2 | **Judge it where players meet it:** game camera, phone size, the real place, effects, players and HUD on. | A pet's wave hidden behind the owner's body turns toward the camera. | Approval rests on Studio captures at the game camera on the phone viewport, never a Blender close-up. | §3.10, review.md §8c |
| 3 | **Spend change only where it reads first:** the biggest pose change, fastest spacing and clearest silhouette go to the tell and contact. | An idle stays small so one ear flick reads. | In the samples, the largest pose change and fastest spacing sit on the accent event. | P-03, P-04, P-18 |
| 4 | **Big before small:** root, key poses, offsets, then hair, fingers, face. | A jump approved as a root-only preview, then as black-fill poses. | Root preview and key-pose black-fills dated before splines; no secondary keys before the check-in (S-19). | P-13, craft §3 |
| 5 | **Shape and silhouette carry identity:** one line of action; signature shape and source of power in the outline; hands, head, feet trackable; sharp timing for aggressive subjects, soft arcs for friendly ones. | Blade off the torso; ponytail visible from behind. | `look_check.py silhouette` on each key-pose black-fill; action and character named; limbs separate (B-02, B-03). | P-07, P-18 |
| 6 | **Less is more:** a few clear poses and chosen holds; secondary motion only where it adds. | A shopkeeper idle: one breath, one glance per loop. | Each secondary channel names its cause on the clip card (S-16); a channel whose only cause is "life" is removed; a render without it only when the read is in doubt. | P-10, P-11 |
| 7 | **One code for meaning:** one gravity and jump language; the same attack, the same tell; the art bible's motion line. | Every enemy lunge uses one crouch-tell family. | Root curves and tell lengths of one class match, or the outlier has a reason (G-09). | P-01, game-timing §7 |
| 8 | **Timing tells cause and effect:** tell, build, beat, hit, result; fast contact; unequal gaps; one marker list for VFX and sound; an ability moves like its verb. | Hammer: coiled hold, fast swing, one-frame contact, long settle; dust on `contact_candidate`. | Beat frames labelled at 30 fps, gaps unequal (B-07); `clip_check.py` events match the timing list; verb named (B-16). | P-03, P-06, game-timing §4 |
| 9 | **Push what must read, on a believable base:** one or two signature moments past real; contacts, shifts and arcs true around them. | A hero jump hangs at the apex, legs in a V, then falls fast. | The clip card names the pushed moments; each differs from its pre-push frame (B-11); S-01 and S-08 pass around them. | P-12, §5 |
| 10 | **The subject's character drives every choice:** each feel word has a visible change; know the subtext. | A timid pet takes short strides and looks back. | A fresh read names the feel words from the key-frame black-fills; two characters' key frames tell apart (B-14). | P-08, §3.1 |
| 11 | **Identity survives every variant:** tell, timing, contact points, anchors and secondary motion kept. | A premium sword skin keeps the base tell frames and its tassel. | `silhouette --compare` base vs variant: same tell and contact frames, no fewer secondary sources (G-08). | sets-and-states §1 |
| 12 | **Controlled variation, never exact repetition:** no twinning; copies out of step; meaning never varies. | Feet land a frame apart; a row of flags waves out of phase. | S-14 and S-22 numbers; tell frames identical across variants. | P-06, craft §6 |
| 13 | **Problem, constraints and target before keys:** window, length, markers, camera, rate, rig limits, budget. | A dodge roll: window, cancel, rate and roll range written first. | The brief restatement is dated before the first key file. | §3.1 |
| 14 | **Research, options, a reasoned pick:** beat sheet, reference, 2-3 key-pose options, two timing takes on key clips. | Three slam poses on one contact sheet; the "overhead" one wins. | Reference list, contact sheet and the recorded pick in the job record (B-12). | §3.5, §3.6 |
| 15 | **Cheap stages first; gates freeze; not precious:** blocking shown before splines; after the check-in poses and timing hold; a broken section is re-keyed. | An arm that twists in a spin is deleted and re-keyed. | Check-in recorded before splines; key-pose frames after it match, or a decision is logged. | craft §3 step 4 |
| 16 | **Critique against the goal, one named problem at a time:** read the curves, refresh your eyes, name a weakness. | "Landing scoots: left foot 0.3 studs, frames 12-18" fixed with a faster contact. | Pass log: one problem per pass with before/after; a fresh read and a mirrored look at each check-in; one named weakness in the hand-back. | review.md §4, §8 |
| 17 | **Build for the next craft and the engine:** lengths and markers in the contract; clips blend; in-place locomotion; exact rig notes. | VFX starts the trail on `swing_accel`; sound on `contact_candidate`. | Consumers acknowledge the timing-list revision; `clip_check.py` events has no missing marker. | §3.8, craft §3 |
| 18 | **Know when it is done:** stop criteria and a pass budget; face and hair last; small pops logged, not chased. | After round two the notes only repeat: stop. | The hand-back states the budget used and each stop criterion with evidence. | review.md §6 |
| 19 | **Feedback follows the real outcome:** the attempt is small and immediate; the big reaction, hit-stop pose and flourish wait for the confirmed hit; paid reveals share one windup. | A punch plays on input; the stagger on server confirm. | A server-rejected hit plays no confirmed motion (G-05); the lowest and highest egg results share the windup (G-13). | game-timing §4, §9 |
| 20 | **Every player can read it:** tells in pose and silhouette, never in effects, colour or camera alone; reduced motion keeps the pose; pulses at most 3 per second. | A boss tell reads as a crouch with VFX off. | G-02 capture: VFX hidden, grayscale, shake and flashes off; every tell and outcome names itself. | game-timing §8, review.md §8c |
