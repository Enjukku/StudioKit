---
name: film-direction
description: What and why of a Roblox cinematic moment - intros, cutscenes, boss entrances, reveals, endings, stills; premise, beats, options, shot jobs, read order, value, timing, sound, every exit. Use for "make an intro", "the boss entrance feels flat", "players don't get what happened", "the cutscene is too long", "make the reveal hit". Film director reads first; film-craft is the how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J015 from the owner's research paper (`knowledge/reference/film/01..03`) and the first game's opening-film records (`04`); craft sources fact-checked live 2026-10-21 (`fact-check-craft-sources.md`). Rebuilt by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence stays out of the body: the film notes above (row ids N1..N4, cited in the references) and the craft library `knowledge/reference/craft/riot/` (§7 follows its `universal-principles.md`). Tags: V verified fact, E practitioner experience, O studio opinion.

# Film direction: what each shot must do, and why

The main rule: **direct attention and decisions before polish.** Say what the player must understand, which image shows it in its first second, what changes inside the shot, why the next cut is needed, and how the player gets back to play. A prettier frame does not fix a sequence the player cannot follow, and more detail does not fix a weak read: more contrast in the right place does.

## 1. When this skill starts
A game needs a cinematic moment (an intro, a story cutscene, a boss entrance, a reveal, an ending, a short in-game camera moment, a still taken from a cinematic), or an existing one does not work. Answer, in this order:
1. Does this moment need an authored camera at all, or should the player stay in control (D-02)?
2. What is the premise in one sentence, which target experience does it serve, what must change in the player's knowledge and feeling, and what state are they in after?
3. Which beats; which options for the key beat and which pick; which shots in what order; what is each shot's job and its first-second read?
4. For each shot: blocking, size, angle, lens/FOV, move, length rule, cut, read order, value and light, acting, sound. Each with a reason.
5. How does every ending return the player to a clear first action?
6. How do we judge the result, and when is it done?

The build (options, blocking, value pass, boards, Blender previs, the data file, Roblox assembly, review captures) is in `film-craft`. **After a context compaction**, re-read §3, §5, §6 and §7 of this file before you hand on a plan: only the start of a skill survives compaction.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Shot sizes, angles, lenses, moves, cuts; composition inside the frame, read order, flow lines, depth, scale and groups; stills from a cinematic | `references/shot-language.md` |
| Timing a beat (tell, build, beat, peak, result), rhythm, the climax, the marker contract and sync rule, confirmed outcomes | `references/beats-and-timing.md` |
| Acting briefs (cause, subtext, the performance sheet, pushed moments), the value and light plan per beat, sound and silence against picture | `references/acting-light-sound.md` |
| How great scenes worked (reveals, a way out, a broken visual contract, light as relationship, boss intro, player-owned camera), as mechanisms to transfer | `references/scene-studies.md` |
| Authored vs player camera, skip / replay / pause / comfort / handoff, shared scenes, phones, the first game's lessons | `references/game-cinematics.md` |
| Worked Roblox examples: a boss entrance, a new-world intro, a door reveal in play, a victory after a confirmed win, a promo still from a cutscene | `references/worked-examples.md` |
| The full source rows and their limits | `knowledge/reference/film/01..04` |
| The build, its stages, the image budget and the self-review lines | `film-craft` skill; review lines: `film-craft/references/review.md` §6 |
| Paid items, romance, gore, horror, franchise themes in a story; a reveal of a paid random result | `platform-policy` skill (and the game-designer's reveal rules) |
| Effect feel, flash safety, camera shake and punches in play | `vfx-design` skill |
| A character's signature key pose and the clip timing list | `animation-design` skill (`references/game-timing.md`) |

## 3. Steps
1. **Problem, premise and beat contract, owner-approved first.** Write the problem the moment solves and its constraints (devices, the play camera, cast and rig limits, sets, budget, platform limits); the premise in one sentence; the hook (one line on what makes this moment compelling); the target experience it serves, from the game profile ("cinematic" and "fun" are not targets); the sell list (2-4 things the player must feel or know after it). Then the five contract items: the player's situation before; the change in knowledge or feeling; the consequential character action; the state after; the gameplay reason to interrupt or redirect attention. Split essential information (needed to act) from optional atmosphere. State the budget (options, passes, images) and the stop criteria. *Check: problem, premise, hook, target experience, sell list, five items, budget and stop criteria written; owner approved.*
2. **Pick the camera mode** (D-02): authored, player-directed or hybrid. *Check: one line saying why this moment earns taking control away.*
3. **Beats as state changes** (D-37). Per beat: what the player knows before, the visible or audible event that changes it, whose intention is active, the question carried into the next beat; each beat is a short cause-and-effect story, and the intensity rises to one climax. A beat that changes neither understanding nor feeling is cut or merged. Write the gameplay state sheet beside it (when control stops, what the avatar does, what keeps running, what can interrupt, the state after each exit). *Check: every beat has an event and a question; the intensity line rises to one climax.*
4. **Research, then options for the key beat** (D-31). Our game's approved images and anchors first, then real-world reference for what invention misses, plus one source from outside games. Then 2-3 clearly different approaches for the beat that carries the moment (a different reveal order, staging or camera mode), each with its own one-line hook and one of them non-obvious, made as rough greybox thumbnails at equal low finish (`film-craft` §3 step 3). Pick with a goal question against the sell list ("which makes the threat read first at phone size?"), record why each other option lost, and show the owner the options with one recommendation. *Check: the options differ in layout or order, not only colour; the pick and its reasons are recorded.*
5. **Design the shots** (§4). Every shot gets a job no other shot does and one first-second read (D-30); its read order is planned (primary, secondary, at most a third) and light, framing, value and motion converge on the primary (D-34, D-35); it is composed inside the delivery frame (D-33); blocking comes first, then camera, then value and light, then colour, effects last (D-32). Choose size, angle and lens by what the frame must show and leave out; move only with a reason; keep geography readable; cut on a change; give acting a cause; give light and sound a job. Where two approaches give different experiences, write both with their trade-off (attention, readability, cost, interruption) and recommend one. *Check: every shot row has purpose, first-second read, read order, value key, emotion change and transition reason.*
6. **Design every ending** (D-24..D-27, D-40): finish, skip, repeated skip, failure or missing asset, death or respawn, disconnect, late join for shared scenes. Each lands on a stated view, state and first safe action; a reward or victory beat plays only on the confirmed result. *Check: one row per ending.*
7. **Hand over to `film-craft`** to block, value-check, board, previs, brief the crafts, assemble and review. Bring the shot list back here whenever a change touches meaning.
8. **Judge the result against the goal** (D-44; the lines in `film-craft/references/review.md` §6). A finding names the shot, what the player should get in its first second, what they get instead, the layer at fault (blocking, composition, value, timing, acting, sound, runtime) and one revision hypothesis ("move the reveal later so the reaction comes before identification"), never "make it more cinematic". One named problem per pass, the worst first; re-check the other layers after a fix. Stop when the stop criteria hold or a round brings no new notes.

## 4. Craft core (what separates great work from weak work)
One line each. Effects of choices are possibilities in context, never guarantees. Depth: SL `shot-language`, BT `beats-and-timing`, AL `acting-light-sound`, SS `scene-studies`, GC `game-cinematics`, WE `worked-examples` (all in `references/`).

| ID | Practice | Depth |
| --- | --- | --- |
| D-01 | **Feeling and information before coverage** [O]: name the emotional change and the information gain, then choose shots; "looks cinematic" is not a goal | SL |
| D-02 | **Earn the camera** [O]: authored when a precise reveal, a spatial deception or a performance relationship is worth the interruption; player-directed when discovering or acting is the point; hybrid = a short authored cue, then the action back to the player. A long move never replaces something to do | GC §1 |
| D-03 | **Every shot has a job** no other shot does [O]: new information, a performance change or a chosen contrast; same size and centred subject on every shot is the commonest weak sequence | SL |
| D-04 | **Effects are conditional** [O]: a low angle *can* show size, a close-up *can* hide who approaches, light from below *can* read as threat, camera height *can* state status; ask what the frame leaves out, then test the read | SL §1-2 |
| D-05 | **Viewpoint, not millimetres, sets perspective** [V]: a focal length means nothing without sensor and fit; Roblox takes a vertical angle; never call a focal length heroic | SL §3 |
| D-06 | **Move only when the changing view adds to the beat** [O]: start information, motivating event, what it reveals, end composition; test the static version first | SL §4 |
| D-07 | **Set a visual contract, then break it at the turn** [E] | SS |
| D-08 | **Reveal order** [E]: geography, someone's alarm, the object, the consequential reaction | SS |
| D-09 | **A way out without words** [E]: perception, the useful detail, the spatial solution | SS |
| D-10 | **Keep geography readable** [V/E/O]: overhead map, one side of the axis by convention, a continuity ledger; cross the line only on purpose, with a route back | SL §5 |
| D-11 | **Stage relationships through space** [O]: doorways, blocked routes, turned backs and light zones carry a scene before expensive faces | SL §5 |
| D-12 | **Cut for a change, never on a timer** [O/E]: name the relation; hold a reaction only while something develops; emotion, then story, then rhythm, then continuity | SL §6 |
| D-13 | **Length is event-bounded until the animatic measures it** [O]: cuts on events, geometry measured, acting durations PROPOSALS until the owner times them | BT §1 |
| D-14 | **Setup earns its place by changing a later meaning** [O]: the causal chain in verbs; a montage keeps the choice | BT §1 |
| D-15 | **Light is a change in visibility and attention** [O/E]: motivated source, separation, the brightest area, what stays hidden; colour meanings are this sequence's conventions; plan concealment and reveal images | AL §2 |
| D-16 | **Direct the cause, not the face** [E/O]: belief, stimulus, tactic, decision, end pose, subtext; expression sized to the shot and the phone | AL §1 |
| D-17 | **Sound has a relationship to the picture** [E/O/V]: per cue its job, emotion, onset, offset, perspective, priority; silence removes a named layer; music and effects planned together | AL §3 |
| D-18 | **A boss intro ends in an actionable arrangement** [E/O]: identifiable enemy with its source of power read first, usable ground, a visible next action; the return after a failure tested too | GC §2 |
| D-19 | **A player-owned camera gets an order of opportunities** [E], not identical frames | GC §1 |
| D-20 | **Know the player's role** [O] and land on the player's own avatar; gesture and focus survive the avatar range | GC §3 |
| D-21 | **Plan only acting the cast can show** [owner decisions]: test each physical beat on the rig and face kit in a render; cut what cannot show, keep its story outcome | AL §1 |
| D-22 | **Phone first** [O]: silhouette, gesture and key object read at phone size; nothing essential rides on blur or an expensive effect | GC §4 |
| D-23 | **Transfer the mechanism, not the imagery** [O]; age-appropriate stakes; platform limits at the top of the beat list | SS |
| D-24 | **Every ending is its own design** [E/O]: skip, replay, pause, comfort, handoff, failure, disconnect | GC §2 |
| D-25 | **Skipping never punishes with confusion** [O]: the essential objective survives outside the skippable part | GC §2 |
| D-26 | **Shared scenes need a contract before approval** [O] | GC §3 |
| D-27 | **Comfort and access** [E/O]: a reduced-motion version keeps the information; captions with speaker; not every big moment shakes | GC §2 |
| D-28 | **Label every reference** [O]: shipped interactive, real-time cinematic, pre-rendered or marketing | GC §1 |
| D-29 | **Alternatives and evidence for the owner** [O]: one recommendation per option set; pitch the moment as the experience the player will have (what they see, hear and feel, in one or two concrete sentences), never as an asset list; approval belongs to one revision | GC §5 |
| D-30 | **Premise and first-second read** [O]: a one-sentence premise and a hook per moment; per shot, the story beat and the hero read in its first second at phone size | SL §5 |
| D-31 | **Options before a pick** [O]: research first; 2-3 different approaches for the key beat at equal finish (full images at the highest quality), each its own hook, one non-obvious; the first idea is a warm-up; two edit takes on key beats, timed by the owner | WE |
| D-32 | **Big before small** [O]: beats and blocking, camera, value and light, colour, then effects; the clean frame passes before any effect is added | BT §5 |
| D-33 | **Compose inside the real frame** [O]: bars, subtitles, skip, the narrowest display and the handoff HUD from the first thumbnail; in a small frame the identifying parts fill it | SL §5 |
| D-34 | **One subject, one read order** [O]: primary, secondary, at most a third; flow lines and converging motion lead to the primary; accents never outshine it; fix a weak read with contrast, not detail | SL §5 |
| D-35 | **Value plan per beat** [O]: calm the surround first; the brightest area on the subject; contrast rises with intensity; dark foreground, lit midground, quiet background; light can hide a surprise | AL §2 |
| D-36 | **Scale, status and groups** [O]: a group has its own silhouette; a giant behind small heroes sells threat and moves slowly; push scale on a believable base | SL §5 |
| D-37 | **Timing tells cause and effect** [O]: tell, build, a small beat, one peak, result; the eye moves on after the peak; uneven gaps; one climax | BT §1-3 |
| D-38 | **Act it out on paper** [O]: motion, driver, time, sound word and subtext per beat; adjectives become pose changes; one or two pushed moments on a believable base; eyes act | AL §1 |
| D-39 | **The marker list is the timing contract** [O]: a marker at every cut and synced event; same names for VFX and sound; picture and sound from one trigger, sound inside the sync rule | BT §4 |
| D-40 | **Feedback follows the real outcome** [O]: victory, reward or defeat plays after the server confirms, at its size, skippable; a paid random reveal follows the game-designer's rules and `platform-policy` | BT §4 |
| D-41 | **Every player can read it** [O]: the beat play needs reads with sound off and in grayscale; flashes keep the `vfx-design` flash rule; every intense camera channel has a reduced version | GC §2 |
| D-42 | **Stills from a cinematic** [O]: big to small inside the final crop; the featured thing is the hero; the signature key pose from the set; switchable layers | SL §7 |
| D-43 | **One world on screen** [O]: cast, palette and light match the game; places show who lives there; crowds vary in pose and timing, never in meaning | SL §5 |
| D-44 | **Critique against the goal** [O]: goal questions; the problem behind a note; one named problem per pass; fresh eyes; say what each input proves; an honest recap | `film-craft` review |

## 5. Rules (final check)
- No invented numbers: no ideal cutscene or shot length, skip delay, camera speed, lens mood or phone budget. UNKNOWN stays UNKNOWN until our own previs or capture measures it; a starting value in this book is a PROPOSAL a check may change.
- Effects of angles, lenses, moves, light and colours are written as conditional ("can", "when"), with the context.
- A cinematic never decides a reward, a boss defeat, a teleport or a trade: the server does (`AGENTS.md` §2). A celebration plays only after the confirmed result.
- Story, names, feel and lengths are PROPOSALS until the owner confirms; the owner chooses between options, and each option set carries one recommendation.
- Mature, romantic, violent, horror or franchise content, and any reveal of a paid random result: `platform-policy` at design time and at review; it wins over this book.
- Flash and shake: the `vfx-design` flash and camera rules, counted on the whole frame with every effect on; a reduced-motion version exists for every authored move that shakes, rolls or whips, and it keeps the information.
- The director briefs and reviews the crafts; it never silently replaces their execution or the owner's approval. "It would be cooler" mid-job is new scope: a ticket with its cost.

## 6. Self-check before handing on the plan
Runnable lines with their inputs are in `film-craft/references/review.md` §6 (P = plan lines); each is PASS, MEASURED, not verified or n/a, with evidence.
- [ ] Problem, premise, hook, target experience, sell list and the five contract items are written; the owner approved; essential vs optional information split; budget and stop criteria stated.
- [ ] Camera mode chosen with a one-line reason.
- [ ] Every beat: the event that changes knowledge, the active intention, the question carried forward; one climax.
- [ ] The key beat had 2-3 different options at equal finish; the pick and the reasons each other lost are recorded; every other choice that changes the player's experience (camera mode, skip policy, the shared-scene policy) shows its alternatives with one recommendation.
- [ ] Every shot: a job, a first-second read, a read order, a value key, an emotion change, what it shows and leaves out, a move reason (or static), a cut reason.
- [ ] Continuity ledger: positions, travel direction, eyelines, light direction, props, action phase at each cut.
- [ ] Acting written as cause, decision and subtext, with the pushed moments named, and checked against what the rig and face kit can show.
- [ ] Every cue has a job and a relationship to picture; silence named where used; the marker list and the sync rule are in the contract.
- [ ] Every ending specified with its first safe action; skip keeps the essential information; rewards wait for the confirmed result; the shared-scene contract answered.
- [ ] No number without our own measurement, an owner decision or a PROPOSAL label; effects written conditionally.

Project overlay: if `knowledge/overlays/film-direction.md` exists, read it after this file; it wins for this game.

## 7. Core principles for this craft
The studio's universal principles, stated for directing a cinematic moment: the standard, an example from our work, a check you can run with its input, and where the depth sits. Check ids (P-, B-, R-) are the lines in `film-craft/references/review.md` §6.

| # | Principle, for my work | Example | Check (input) | Where |
| --- | --- | --- | --- | --- |
| 1 | **The gameplay read comes first:** the story beat and the hero read in each shot's first second; the handoff frame shows the threat, the goal and the first safe action before any beauty. | A boss entrance ends on the boss's glowing fist, the open arena floor and the exit gate, not on a dramatic sky. | R-07 and P-03: first-second read written per shot; the handoff capture at the game camera on the phone viewport names threat, goal and first action (Studio MCP capture). | D-18, D-30 |
| 2 | **Judge it where players meet it:** the target device size, the narrowest display, the bars, subtitles and skip on, in Roblox, with the real HUD on the handoff frame. | A wide establishing shot that read in Blender loses the tiny exit sign at 667x375; the exit moves closer to the camera. | B-04 `look_check.py thumb` subject height at phone size; R-01 captures in Studio, phone claims from a device. | D-22, D-33 |
| 3 | **Decide what is read first; spend contrast only there:** light, framing, value and motion converge on the subject; everything else is calmer. | The hero child stands in the only lit doorway; the crowd behind stays mid-grey. | B-06 `look_check.py value` subject/ring ratio, and the subject first when every named bright region is ranked by its p95 on masks or tight boxes, or for a planned silhouette the backdrop first with the subject dark inside it (key-frame numbers). | D-34, D-35 |
| 4 | **Big before small:** beats and blocking, then camera, then value and light, then colour, then effects. | The reveal is approved as a grey proxy strip before the lava glow is added. | P-07: blocking strip and value strip dated before the colour strip, boards and effects (job folder dates). | D-32 |
| 5 | **Shape and silhouette carry the beat:** group silhouettes and scale contrast tell the story; the line of action reads in black-fill. | Three heroes back to back, ringed by small shadow creatures, read as "surrounded" with no faces visible. | B-05 `look_check.py silhouette` on per-group masks: the group outline and the giant-to-hero height ratio (key-frame numbers). | D-36 |
| 6 | **Less is more:** one subject per shot; a few strong reads; the layout is clean before smoke and sparks. | A busy market shot loses its background stalls' bright banners so the thief reads. | B-08: the clean frame (effects off) passes B-05 and B-06 on its own; count reads per shot (at most three) from the shot table. | D-32, D-34 |
| 7 | **One code for meaning:** story colours, light directions and camera grammar mean the same thing every time in the game. | Warm light always marks home; the villain is always underlit; the same push-in always marks a decision. | P-09: the sequence's colour and light conventions table is consistent across shots and with earlier cutscenes of the game (shot table vs art bible). | D-15, D-43 |
| 8 | **Timing tells cause and effect:** tell, build, a small beat, one peak, result; the result after its cause; uneven rhythm; one marker list keeps picture, VFX and sound together. | The gate cracks (tell), dust trickles (build), a held breath of silence (beat), the gate bursts (peak), the boss steps through (result). | B-10 `shotlist.py check` lengths and beat gaps are not all equal; R-04 `shotlist.py log-diff` cue and cut times against the plan (numbers). | D-37, D-39 |
| 9 | **Push what must read past real, on a believable base:** scale, pose and contrast pushed on one or two moments; balance, contact and geography true around them. | The guardian is three times the hero's height in the reveal shot; its steps still land with weight. | B-05 height ratio; R-08 at the animator's blocking check-in: the pushed pose keeps its centre of gravity over its support (key-frame stills). | D-36, D-38 |
| 10 | **The subject's character drives every choice:** each shot has a premise and the character's subtext; how *this* character enters, not how a boss enters. | A greedy merchant boss counts coins while the hero walks in: the subtext is "you are not worth looking at". | P-01 premise and hook written; P-10 every acting row has subtext; the owner names the intended adjectives at G1 from the thumbnail strip. | D-30, D-38 |
| 11 | **One world, one style:** the cast looks like its in-game models, the light follows the art bible, the palette matches the game. | The cutscene uses the in-game rig and its approved face kit, not a prettier stand-in. | B-12: each cast member's model and rig ids equal its asset record and rig sheet (doc, MCP read-back); a silhouette compare only of the rig posed as the anchor at the anchor's camera; R-09 palette against the art bible roles (`look_check.py palette --roles`). | D-43 |
| 12 | **Controlled variation and life:** crowds, extras and backgrounds vary in pose and timing; meaning never varies. | Six villagers cheer on different frames with three poses, not one clip copied six times. | B-13: in the key frame, no two neighbouring extras share pose and frame (frame-stepped stills of the crowd shot). | D-43 |
| 13 | **Problem, constraints and target before shots:** premise, beats and the player's role come before any board. | A tycoon's "new floor unlocked" moment is checked against the target experience before anyone boards it; it becomes a 3-second camera move, not a cutscene. | P-01: the beat contract with problem, constraints, target experience and sell list is dated before the first image. | §3 step 1 |
| 14 | **Research, options, a reasoned pick:** 2-3 distinct thumbnails of the key beat before the animatic. | Option A reveals the boss by its shadow, B by the crowd fleeing, C by a quiet empty arena: B wins at phone size. | P-04: the options contact sheets, at equal finish, and the recorded pick with reasons (job folder). | D-31 |
| 15 | **Cheap stages first; gates freeze; I am not precious:** thumbnails, blocking, value, boards, animatic, then Roblox; after the owner times the animatic, timing changes only by a new revision. A better option replaces mine without a fight; a closed door reopens only by a new owner decision. | A late "add a slow-motion beat" note becomes a new shot-list revision with its affected cues listed; the sound designer's quieter reveal beats my drum hit, so the drum goes. | P-07 stage dates; P-04 rejection reasons say why each option lost, mine included; R-11 `shotlist.py diff` shows no drift after `stage: locked` unless a revision is logged. | `film-craft` §3 |
| 16 | **Critique against the goal, one problem at a time:** notes name the beat and what the player should understand there. | "Shot D: players should know the statue is alive; the water burst covers the head turn" leads to one fix: the burst starts 6 frames later. | R-12: every finding names shot, intended read, observed read, layer and one fix; one problem per pass in the log. | D-44 |
| 17 | **Build for the next craft and the engine:** shot ids, cue ids, markers, the sync rule, layered stills and the Luau data module; budgets respected. | The animator gets frame windows and end poses; sound gets the cue sheet; marketing gets the key frame with switchable layers. | P-11 every brief has fixed values with sources and checks; R-04 no planned cue missing from the playback log. | D-39, D-42 |
| 18 | **Know when it is done:** stop when the beats read at target size and the cues hit their markers; stop criteria and a pass budget set first. | After the second note round only repeats, the lead calls done; the small pops go to the follow-up list. | R-13: the hand-back lists each stop criterion with its evidence and the budget used. | §3 step 8 |
| 19 | **Feedback follows the real outcome:** a victory or reward sequence plays only after the server confirms the result, matches its size and is skippable. | The trophy cutscene starts on the server's "round won" event, never on the client's guess. | R-14: a test build where the server rejects the win: no victory cinematic plays (feature-builder's hook, Output log). | D-40 |
| 20 | **Every player can read it:** the beat play depends on reads with sound off and in grayscale; no strobing; every intense camera channel has a reduced version. | The "door is open" beat shows the open door, not only a creak; the whip pan becomes a cut under reduced motion. | R-10: grayscale and reduced-motion captures of the reveal and handoff frames name every essential fact; the animatic's large-area flash count per rolling second (the studio's counter, `vfx-craft/references/measure.md` §6) within the `vfx-design` flash rule (frame-folder numbers). | D-41, D-27 |
