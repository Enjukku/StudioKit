---
name: animation-design
description: What and why of motion for anything that moves in Roblox - characters, creatures, held items, props, mechanisms, vehicles, buildings, ambient loops. Read what must move; choose poses, timing, spacing and the cheapest technique; judge the read. Use for "make it feel heavy", "it looks floaty / stiff", "players can't read the attack", rig-pipeline S1/K2. Animator reads first; animation-craft is how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J006 from owner material. Evidence: animation paper notes `knowledge/reference/animation/01-*.md`, `02-*.md` (AP:<line> = paper line), Riot animation notes `03-riot-first-game.md` (A:<line> = Riot ep4 transcript, R:<line> = Riot core series), fact-checks `knowledge/reference/animation/fact-check-*.md` and `knowledge/reference/rigging/fact-check-*.md`. Tags: [V] verified source, [E] expert experience, [O] studio opinion / policy.

# Animation design: what moves, why, and how it reads

## 1. When this skill starts
Before any key is set, for anything that moves. It answers: what the player must read and feel, what drives each moving part, which technique moves it (keyed clip, code, physics, texture), which clips and states are needed, what the timing contract is, and how the result is judged. `animation-craft` answers how to build, export and play it in Blender and Roblox. `rig-pipeline` is the shared workflow when a rig is needed.

**Governing idea [O] (AP:9, AP:21):** good motion is cause and effect the viewer can follow: what is intended, what pushes, what supports, what happens, what results. More keys, bones, noise or generated clips do not build that chain. Work in this order: the motion idea, then the performance, then the runtime asset.

**There is no single recipe.** A knight, a drawbridge and a flag move for different reasons. Every choice below is a decision with a reason; write the reason down. A number that no source, owner or measurement gives is UNKNOWN, never a default (AP:15, AP:1094).

## 2. Read this file when
| You need | Open |
| --- | --- |
| The principles in full: when each applies, the sign a reviewer can check, sources | `references/principles.md` |
| A worked example for your kind of object (character action, creature, pet, sword swing, door, drawbridge, chest, lever, elevator, trap, vehicle, mount, building, flag, windmill) | `references/worked-examples.md` |
| Body parts and species (tails, wings, legs, ears, fins, long bodies, floating) and the motion profile fields | `references/body-and-species.md` |
| Animation sets, states, transitions, interruptions, loops, idles | `references/sets-and-states.md` |
| Game timing, gameplay windows, the shared event timeline, hit-stop ownership | `references/game-timing.md` |
| The review checklist, common failures and their first check | `references/review.md` |
| Templates: motion profile, animation set, timing list, motion spec | `templates/anim/` |
| How to build it (Blender keying, export, Roblox playback, code-driven specs, loops at scale) | `animation-craft` skill |
| The rig workflow (S1, K2, S6, S7), rig sheet and rig notes | `rig-pipeline` skill |

## 3. Steps
1. **Read the brief for the read.** What must the player understand, and by when? Who or what moves, its size on the phone screen, the game camera, how often it plays, what interrupts it, what gameplay window it must fit (from the gameplay owner, never invented). Write the character or object in 2-4 words of personality or behaviour ("nimble, playful", "heavy, old, grinding"). *Check: the read and the feel words are written; missing gameplay numbers are listed as UNKNOWN with their owner.*
2. **Study the whole subject before moving it** (AP:184-192). Multi-view renders (front, back, both sides, raised ¾, the gameplay camera, underside where it matters). One record per visible part: what it is, what carries it, whether it bends, active / passive / rigid / mechanical, and "does not move" where true. Names prove nothing: three similar fins can be decorative, steering and armour (AP:184). Mass is UNKNOWN unless supplied; length is measured (AP:188). *Check: every visible part has a record.*
3. **Choose the technique per moving part** (§5): keyed clip on a rig, code-driven motion, physics constraint, texture / flipbook, or a mix. Write the reason and the docs page. A rig is needed → `rig-pipeline` S1 (motion profile, ROM with units, stress poses, clip list) with the rigger. No rig (a rigid door on a hinge line) → no rigger step; write a motion spec for the builder. *Check: every moving part has a technique, a reason and a docs path.*
4. **Write the set** (`references/sets-and-states.md`, `templates/anim/animation-set.md`): clips from the implemented states and transitions, each with entry and exit pose, loop policy, interruption rule, priority intent, blend owner, attachments and events. An action the game does not need is marked absent, not filled in (AP:402). *Check: every gameplay state has a clip, a spec or a deliberate "absent".*
5. **Plan each clip's poses and timing** (§4): the key poses that tell the story, the breakdown that carries the motion, the accent at the gameplay event, holds that keep an idea, contrast in spacing. Gameplay windows are fixed inputs; you place beats inside them (A:172-174). *Check: each clip names its key poses, its accent event and the window it fits.*
6. **Draft the timing list** (`templates/anim/timing-list.md`; `rig-pipeline` §5): named events, time in seconds plus the source frame and frame rate, meaning, owner, consumers, interruption rule. VFX frame scripts and sound cue cards use the same event ids. *Check: VFX and sound can read every event they need from it.*
7. **K2 (when rigged):** check the rigger's plan answers every motion need; sign, or send one note. A "not supported" that changes the look goes to the lead for the owner.
8. **Judge it** (`references/review.md`): at the game camera, at phone size, at normal speed first, then frame by frame at events; with and without effects. *Check: the review rows have evidence.*

## 4. Principles as decisions (summary; full table with sources in `references/principles.md`)
Each is a tool to diagnose with, not a dial to turn up everywhere (AP:53, AP:59). Use the one the read needs.

| ID | Decide | Ask | Sign in the clip | Evidence |
| --- | --- | --- | --- | --- |
| P-01 | **Cause first** | What intends, pushes, supports, results? | a viewer names the action, the force and the result without text | [O] AP:9, 21 |
| P-02 | **Weight and support** | Where is the centre of gravity, what is planted, where does weight go? | weight leaves a foot before it lifts; a fast move still shows a contact; mass never vanishes between frames | [E] A:92-100, A:246-254, A:456-474; [O] AP:190 |
| P-03 | **Timing makes speed and weight** | Fewer frames = faster; where does the clip hold, where does it snap? | a short hold tightens energy before a spring (anticipation); deleting one frame can sharpen an impact | [E] A:446-454, A:808-816 |
| P-04 | **Spacing, not one ease** | Which segments ease, which snap, which keep speed? | uneven spacing per channel and segment; never ease-in-out on every joint | [O] AP:385, AP:646; [E] A:194-210 |
| P-05 | **Arcs** | What path does each landmark draw, also as projected to the camera? | smooth arcs where anatomy or force gives them; a deliberate corner only at an impact | [O] AP:68; [E] A:754-758 (parabolic toe path keeps gravity) |
| P-06 | **Rhythm and asymmetry** | Is the cadence even? Do limbs twin? | an uneven, "jazzy" cadence; feet and hands offset so the eye catches two reads | [E] A:360-366, A:540-552, A:716-724; [O] AP:389 |
| P-07 | **Silhouette at the game camera** | Does the shape read at phone size from the real camera? | the pose reads as a black shape; an iconic shape beats physical correctness; no leg pointing down the lens | [E] A:158-162, A:702-708, A:760-766; [V] TF2 shapes AP:107-113 |
| P-08 | **Character drives choices** | What would this character or object do, and why? | motion choices trace back to the 2-4 personality words and the subtext | [E] A:42-52, A:102-104, A:620-622; [E] AP:81-87 (identity can live in movement) |
| P-09 | **Active vs passive parts** | Does this part drive (steer, balance, grip, look) or follow? | active parts lead with intent; passive parts lag and settle from a named cause; no generic delayed wave | [V] gecko tails AP:228; [O] AP:230, AP:277 |
| P-10 | **Overlap and follow-through with a cause** | What settles after the main action, and why? | subordinate masses settle; secondary motion supports the main idea and never competes | [O] AP:66, AP:69, AP:648; [E] A:984-1024 |
| P-11 | **Holds keep an idea** | Freeze, breathing hold, small gaze shift? | stillness is chosen; an idle with every part in sync reads as a machine | [O] AP:389 |
| P-12 | **Exaggerate the read, not every amplitude** | Which part of the read must be stronger? | stylized breaks are listed and approved; contact truth survives | [O] AP:71, AP:381-383 |
| P-13 | **Effort order** | Is the root cadence, pose and flow right before detail? | detail (hair, face, fingers) added last; the clip already works without it | [E] A:970-982; [O] AP:642 |
| P-14 | **Gameplay timing is fixed input** | What is the window, the accent event, the cancel point? | the visible threat and result agree with the authoritative windows; anticipation is information, not delay | [E] AP:115-121, AP:349; [O] AP:473 |
| P-15 | **Mechanisms move like their mechanism** | Hinge, rail, gear, piston, rope? Actuator and hard stops? | a hinge never translates; speed follows the actuator (a winch, a counterweight, a hand); stops are hard unless flex is designed | [O] AP:200-220 (mechanical row), AP:446-454; `rigging-design` mechanisms |
| P-16 | **Method is open, the result is judged** | Layering root-first or pose-to-pose? | any route that passes the review; no fixed recipe | [E] A:726-748 (WF4) |

## 5. Technique choice (decide per moving part; facts and docs paths in `animation-craft` and `knowledge/reference/animation/fact-check-techniques.md`)
| Technique | Choose when | Avoid when | Who builds |
| --- | --- | --- | --- |
| **Keyed clip on a rig** (Bones for bending surfaces, Motor6D for rigid pieces) | the shape bends; many parts move with authored timing; acting, contact, comedy or gameplay information must come out the same every time | one rigid piece on one axis (a code or physics mover is simpler) | animator with the rigger (`rig-pipeline`) |
| **Code-driven motion** (TweenService, CFrame / PivotTo on the client) | rigid object, few axes, simple curve: doors, chests, platforms, elevators, bobbing pickups, signs | the motion bends or needs many timed parts; server-side cosmetic tweens add replication traffic (AP:771, AP:831) | animator writes the motion spec (`templates/anim/motion-spec.md`); a builder writes the code |
| **Physics constraints** (hinges, sliders, springs, motors) | the motion must react to players, weight or collisions; swinging signs, ropes, trapdoors that drop | the outcome must be the same for every client, or it decides gameplay without the physics owner | builder with the physics owner; animator writes the feel targets |
| **Texture or flipbook** | the motion is surface detail: water, scrolling belts, fire, glow, distant crowds | the silhouette must move | VFX (flipbooks) or builder (texture scroll); animator states the rhythm |
| **Procedural layer on a clip** (IK, look-at, spring) | input keeps changing (aim, look-at, uneven ground) and the result can be bounded and tested | the part carries intent (a pointing tail cannot be a free spring) | builder, from the animator's limits (AP:508-510) |

- **Cheapest that looks right wins**, measured, not assumed. Authoring cost and runtime cost are different: a tween is quick to author but not proven cheaper per frame (AP:831). Many copies (ambient decoration): cost per copy and phone budgets decide (`performance` skill; `animation-craft` §6).
- **Visual motion is never physics or gameplay authority.** Bones move the picture, not the collision shape [V] (AP:721); a marker is presentation, never damage (AP:473). Collision, occupancy and outcomes belong to the gameplay and physics owners.

## 6. Kinds of objects (detail and a worked example each: `references/worked-examples.md`)
| Kind | What usually decides the motion | Usual technique | Joins |
| --- | --- | --- | --- |
| Characters (locomotion, actions, idles, emotes, reactions, cutscene acting) | support and weight, intent, personality, gameplay windows | keyed clips on a rig | rigger, game-designer, film-director (acting per shot), VFX, sound |
| Creatures and pets | anatomy family, active vs passive appendages, gait and contacts, owner attention (pets) | keyed clips; LOD variants for crowds | rigger, environment-designer |
| Held items (swords, tools, guns, shields) | grip, the item's mass and its arc with the body; follow-through and recovery; readiness beats | keyed on the character rig with item sockets; the item's own parts keyed where they move | rigger (grip anchors), VFX (trails and flashes on the timing list), sound |
| Props and mechanisms (doors, chests, levers, drawbridges, elevators, traps, machines) | the mechanism: pivot or rail, actuator, travel, hard stops; the interaction moment | code-driven or physics for rigid one-axis parts; keyed when several linked parts move | builder, game-designer (trap windows) |
| Vehicles and mounts | suspension, wheels and steering follow the vehicle's real motion; a mount's gait carries the rider | physics or code for the body; keyed rider and mount clips | builder, physics owner, rigger |
| Buildings and large structures (build-up, transformation, collapse) | sequence and readable arrival; a clear end state; collision kept apart from the show | keyed or code sequence of pieces; physics for debris (owner decides) | environment-designer, VFX, destruction / physics owner |
| World decoration and ambient loops (flags, windmills, plants, water wheels, signs) | a calm, varied rhythm that never draws the eye; cost per copy | texture, code on the client, or a short looped clip; shared tracks | environment-designer (ambience map), performance-engineer |
| Out of scope | cutscene camera motion (film-director); UI motion (ui-ux-designer) | — | — |

## 7. Rules (final check)
- Never invent a mass, delay, anticipation length, hold length, spring constant, stretch percentage, foot-slide tolerance, phone budget or frame count; mark UNKNOWN or PROPOSAL and name the owner (AP:1076).
- Never retime a gameplay window to fit a clip; place beats inside it and report a conflict (AP:986).
- Never let VFX hide a missing contact or an unclear pose; a marker never decides damage (AP:1080).
- Never work around a missing degree of freedom (bending a tool, a wing through the body): one rig note with alternatives (`rig-pipeline` §4).
- Never ship generated motion without review, provenance and a rights check (AP:941-951, AP:1086).
- Judge at the real camera and phone size, never only in the editor or a beauty shot.
- The owner approves feel and look; a score or a famous studio's style never replaces that (AP:1088).

## 8. Self-check before handing on the plan
- [ ] The read, the feel words and the gameplay windows (or their UNKNOWN owners) are written.
- [ ] Every visible part has a record; every moving part has a technique, a reason and a docs path.
- [ ] The set covers every implemented state and transition; absences are deliberate.
- [ ] Each clip names its key poses, its accent event and its window.
- [ ] The timing list has every event VFX, sound and UI need, with seconds, source frame and frame rate.
- [ ] No number without a source, owner decision, measurement or PROPOSAL label.

Project overlay: if `knowledge/overlays/animation-design.md` exists, read it after this file; it wins for this game.
