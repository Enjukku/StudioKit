---
name: film-direction
description: Decide what a Roblox cinematic moment must make the player know and feel, and how each shot does it, before anything is boarded, animated or built - opening films, story cutscenes, boss introductions, reveals, endings and short in-game camera moments. Covers the beat contract, authored vs player-directed vs hybrid camera, beats as state changes, shot jobs, size, angle, lens and what the frame leaves out, camera moves with a reason, staging, eyelines and screen direction, where to cut and why, setup and payoff, light and colour as attention, directing acting, sound and silence against picture, the player's role and every exit back to play (skip, replay, comfort, multiplayer), and how to judge the result. Use when the owner says "make an intro", "the boss entrance feels flat", "players don't get what happened", "the cutscene is too long", "the camera moves for no reason", "make the reveal hit". Read by the film director first; animator, VFX, sound, UI and environment roles read it for the shared rules. Pair with film-craft for the build.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J015 from the owner's research paper (`knowledge/reference/film/01..03`, paper read 2026-10-21) and the first game's opening-film records (`04`); craft sources fact-checked live 2026-10-21 (`fact-check-craft-sources.md`). Evidence tags: V = VERIFIED (documented fact), E = EXPERIENCE (a practitioner's account), O = OPINION (studio method). Note ids: N1 = `01-craft-scenes-game-cinematics.md`, N2 = `02-previs-roblox-runtime.md`, N3 = `03-vocabulary-method-templates-review.md`, N4 = `04-earlier-game-opening-film-lessons.md`.

# Film direction: what each shot must do, and why

The main rule: **direct attention and decisions before polish** (N1 EM-03). Say what the player must understand, which image shows it, what changes inside the shot, why the next cut is needed, and how the player gets back to play. A prettier frame does not fix a sequence the player cannot follow.

## 1. When this skill starts
A game needs a cinematic moment, or an existing one does not work. The skill answers, in this order:
1. Does this moment need an authored camera at all, or should the player stay in control (§4 D-02)?
2. What must change in the player's knowledge and feeling, and what state are they in after?
3. Which beats, which shots, in what order, and what is each shot's job?
4. For each shot: size, angle, lens/FOV, move, length rule, cut, staging, acting, light, sound. Each with a reason.
5. How does every ending return the player to a clear first action?
6. How do we judge the captured result?

The build (boards, Blender previs, the data file, Roblox assembly, review captures) is in `film-craft`.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Shot sizes, angles, lenses, moves, composition, cut types: what each can do and what it hides | `references/shot-language.md` |
| How great scenes worked (reveals, a way out, a broken visual contract, light as relationship, boss intro, player-owned camera), as mechanisms you can transfer | `references/scene-studies.md` |
| Acting briefs, light and colour plans, sound and silence against picture | `references/acting-light-sound.md` |
| Authored vs player camera, skip / replay / pause / comfort / handoff, multiplayer and phones, the first game's lessons | `references/game-cinematics.md` |
| The full source rows and limits | `knowledge/reference/film/01..04` |
| The build and the templates | `film-craft` skill |
| Paid items, romance, gore, horror, franchise themes in a story | `platform-policy` skill |
| Effect feel, flash safety, shake | `vfx-design` skill |

## 3. Steps
1. **Beat contract, owner-approved first** (N3 BC-01..05). Write: the player's situation before; the change in knowledge or feeling; the consequential character action; the state after; the gameplay reason to interrupt or redirect attention. Split essential information (needed to act) from optional atmosphere. *Check: five items written; owner approved.*
2. **Pick the camera mode** (D-02): authored, player-directed or hybrid. *Check: one line saying why this moment earns taking control away.*
3. **Beats as state changes** (N3 BC-06..09). Per beat: what the player knows before, the visible or audible event that changes it, whose intention is active, what question carries into the next beat. A beat that changes neither understanding nor feeling is cut or merged. Write the gameplay state sheet beside it (when control stops, what the avatar does, what keeps running elsewhere, what can interrupt, the state after each exit). *Check: every beat has an event and a question.*
4. **Design the shots** (§4). Every shot gets a job no other shot does. Choose size, angle and lens by what the frame must show and must leave out; move only with a reason; keep geography readable; cut on a change; give acting a cause; give light and sound a job. Where two approaches give different experiences, write both with their trade-off (attention, readability, cost, interruption) and recommend one. *Check: every shot row has purpose, emotion change and transition reason.*
5. **Design every ending** (D-24..D-27): finish, skip, repeated skip, failure or missing asset, death or respawn, disconnect, late join for shared scenes. Each lands on a stated view, state and first safe action. *Check: one row per ending.*
6. **Hand over to `film-craft`** to board, previs, brief the crafts, assemble and review. Bring the shot list back here whenever a change touches meaning.
7. **Judge the result** from captures with §6. A finding names the shot, what the player should get, what they get instead, and a revision hypothesis ("move the reveal later so the reaction comes before identification"), never "make it more cinematic" (N3 PM-05).

## 4. Craft core (what separates great work from weak work)
| ID | Practice | Evidence |
| --- | --- | --- |
| D-01 | **Feeling and information before coverage.** Name the emotional change and the information gain first; only then choose shots. "Looks cinematic" is not a goal | O: N1 RU-01, EM-03; N3 RV-01 |
| D-02 | **Earn the camera.** Authored camera when a precise reveal, a spatial deception or a performance relationship needs it and the interruption is worth it. Player-directed staging when discovering or acting is the point. Hybrid: a short authored cue, then the meaningful action goes back to the player. A long camera move is no substitute for giving the player something to do. "No cuts" does not mean freedom | O: N1 GC-02, GC-03, MM-10 |
| D-03 | **Every shot has a job** another shot is not doing: new information, a performance change or a deliberate contrast. Same size and centred subject on every shot is the most common weak sequence | O: N1 RU-02; N3 DF-01, DF-05 |
| D-04 | **Effects are conditional.** A low angle *can* show size or obstruction; a close-up *can* clarify a face and hide who approaches behind it; a wide *can* be intimate if shared action carries it. No angle, size or lens guarantees a feeling. Ask what the frame leaves out before naming an adjective | O: N1 RU-03, SH-04..07; N3 SV-01..27, DN-03 |
| D-05 | **Lens: viewpoint, not millimetres, sets perspective.** From one position a focal-length change only magnifies; matching subject size from farther away with a longer lens changes perspective. A focal length means nothing without its gate (sensor) and fit; Roblox takes an angle, not a lens (`film-craft` converts). Never label a focal length heroic or intimate | V: N1 SH-01, SH-08 (F05); E: SH-02 (1917: mostly 40 mm, reported in interviews; a production example, FC-03) |
| D-06 | **Move only when the changing view adds to the beat.** Per move write: starting information, the event that motivates the motion, what it newly reveals, the end composition. Test the static version; if both read equally, choose by style and cost, not by "motion is better". A move hurts when it hides acting, loses a landmark or fights a subtitle | O: N1 RU-04, MV-02..04 |
| D-07 | **Set a visual contract, then break it at the turn.** Hold a repeated framing (fixed camera, one subject centred) and move the camera or the subject only when the character's attention changes. If the camera already moves all the time, the turn has no contrast | E: N1 SC4-1..4 (Feast) |
| D-08 | **Reveal order: geography, then someone's alarm, then the object, then the consequential reaction.** Starting on the gruesome insert kills anticipation. A short reveal can run expectation, contradiction, comprehension, then choice or control return | E: N1 SC1-2 (Jaws); O: ED-04 |
| D-09 | **Show a way out without words: perception, then the useful detail, then the spatial solution** (an eye widens, the open lock, the wider view that makes the hiding place legible) | E: N1 SC2-2 (Yojimbo) |
| D-10 | **Keep geography readable.** Draw an overhead map (entrances, exits, threats, camera half-plane). Keep coverage on one side of the action axis (a convention, not a law); track eyeline target and screen direction per shot in a continuity ledger. Cross the line only on purpose: with a visible reposition, a re-establishing frame or a deliberately disorienting cut, and give gameplay a route back to readable space | V: N1 ST-01 (F08); E: ST-02 (Murch); O: ST-03, ST-06; N3 CL-01..07 |
| D-11 | **Stage relationships through space.** Who controls the doorway, who blocks a route, who turns away, who must move to keep eye contact. These beat "make him look powerful". One room, two characters, a doorway and two light zones can carry a scene before expensive faces exist | O: N1 ST-05; E: SC6-3 (God of War) |
| D-12 | **Cut for a change**, never on a timer: new information, a changed allegiance, a completed action or a chosen contrast. Name the relation (match on action, graphic match, eyeline, montage). Hold a reaction only while something visibly develops; a hold with nothing developing is delay, not suspense. Rhythm is the spread of new information, not the cut count. Priority when they conflict: emotion, then story, then rhythm, then continuity (a priority, not a measured weight) | O: N1 RU-06, ED-03, ED-05, ED-06; E: ED-01 (Murch) |
| D-13 | **Length is event-bounded until the animatic measures it** ("until the player recognizes the blocked exit"). No source gives an ideal cutscene length, shot length per mood, skip delay or cuts per minute. Lengths come from our own animatic, labelled design choices; lengths from analysed films stay UNKNOWN. In the animatic, cuts sit on events and what geometry decides is measured (contact, arrival, line of sight); acting durations stay PROPOSALS until the owner directs timing | O: N1 SU-05, SU-06, U-02, U-06, U-08; N3 DN-01, DN-02 |
| D-14 | **Setup earns its place by changing a later meaning**, and the payoff a player must use is actionable, not only surprising. Write the causal chain in verbs (wants, tries, meets resistance, notices, chooses, changes). Montage compresses time but must keep the choice that explains the next action. Show through behaviour where it reads; use a line of dialogue or UI where silent staging would hide essential information | O: N1 SU-02, SU-04 |
| D-15 | **Light is a change in visibility and attention**, not a mood word: name the motivated source, subject/background separation, the brightest area, silhouette and what stays hidden. Colour meanings are local conventions of this sequence, never universal ("red = anger" is not supported). Plan the concealment image and the reveal image; "brighter" is not an instruction. Judge light before composition is locked | O: N1 LC-02, LC-05; E: LC-03, LC-04 (Fortiche, Deakins/DeBlois), SC6-2 |
| D-16 | **Direct the cause, not the face.** Acting brief: what the character believes before the shot, the new stimulus, the tactic toward another character, the visible decision, the end pose the next shot needs. "Look scared, then happy" leaves out the thought that changes the action. Choreograph relationships (for example out of sync, then aligned, then a shared glance). Match expression size to the shot and the phone: a micro-expression lost at delivery size is not screen acting | E: N1 AC-01, AC-03 (Barillaro; Wanneroy, his own faces); O: AC-02, AC-04, AC-05, SC5-2 (Spider-Verse beat order unverified, FC) |
| D-17 | **Give sound a relationship to the picture.** Per cue: onset, offset, narrative role, whose perspective, allowed overlap, priority against dialogue. Silence is removing a named layer, not zero audio. Environmental sound can do the score's work. Compare warning before, exact sync and delayed sound at a reveal. Bring music in early; label temp tracks temp | E: N1 SN-01, SN-03, SN-04; O: SN-02, SN-06; V: ED-02 (J and L cuts) |
| D-18 | **A boss intro ends in an actionable arrangement**: identifiable enemy, readable threat, usable ground, a visible next action. It does not need to show every attack. A closer camera and the world reacting can sell scale. Test the return after a failed attempt as seriously as the first entrance | E: N1 SC7-2..4 (God of War); O: SK-06 |
| D-19 | **When the player owns the camera, direct the order of opportunities**, not identical frames. Separate "see the landmark", "learn the controls" and "hear the mission" when they compete; a landmark can be introduced by sound with a safe viewing spot | E: N1 SC8-2..4 (Half-Life: Alyx; VR, so test on phones) |
| D-20 | **Know the player's role in the scene** (observer, the hero, one of a group) and land on the player's own avatar when the scene ends in play. Avatars vary in height, accessories and costume: the gesture and focal point must survive the supported range | O: N1 RU-10, MM-08, GC-07; N4 V-02 (owner decision) |
| D-21 | **Plan only acting the cast can show.** Before a beat locks, check it against the rig and face kit in a render: the first game's owner cut a planned moment because the character's proportions could not show it; side characters need their own faces, eyes that can look, mouths for every spoken line | owner decisions: N4 R-04, R-05, R-09; proposal: R-06 |
| D-22 | **Phone first for readability.** A shot that needs a desktop-sized eyebrow to explain the objective fails. Check silhouette, gesture and key object at phone size; crucial storytelling never depends only on depth-of-field blur or an expensive effect | O: N1 SC6-3; N2 RT-37 |
| D-23 | **Transfer the mechanism, not the imagery.** Use famous scenes to generate testable alternatives, never to copy shots, a director's look or mature content. Choose age-appropriate stakes; put platform limits (romance, gore, horror, franchise) at the top of the beat list (`platform-policy`) | O: N1 SC-06; N3 DN-04, AR; N4 P-08 (owner decision) |
| D-24 | **Every ending is its own design**: skip (reach the correct story state without the performance), replay (no repeated rewards, damage or irreversible choices), pause (local only; do not pretend a shared world stopped), comfort (a calmer camera that keeps the information), handoff (view, movement, UI and audio restored, with a clear first action) | E: N1 SK-01, SK-02 (shipped precedents); O: SK-04, RU-14 |
| D-25 | **Skipping never punishes with confusion.** The essential objective survives in a short readable form outside the skippable part; progression never hangs on a visual cue | O: N1 SK-05; N3 DN-07 |
| D-26 | **Shared scenes need a contract** before approval: audience and late joiners, what the world does meanwhile, who decides completion, indispensable assets and their fallback, skip policy (shown to players), return path, accessibility, avatar range. Never freeze an uninvolved player; never tie a group reward to everyone finishing a camera track | O: N1 MM-01..09 |
| D-27 | **Comfort and access**: offer a reduced-camera-motion version that keeps the information; captions with speaker identity; not every big moment shakes the camera (owner, first game) | E: N1 SK-02 (cinematic smoothing precedent); O: MM-07; N4 A-05 (owner decision) |
| D-28 | **Label every reference** as shipped interactive event, shipped non-interactive real-time cinematic, pre-rendered film or marketing. "In-engine" does not prove it ran live on a phone with the player's avatar | O: N1 GC-06; E: GC-04, GC-05 |
| D-29 | **Give the owner alternatives and evidence**; options each carry a recommendation (the first game's owner answered best in that shape). Never let a proposal become approval silently; approval belongs to one revision | O: N1 RU-15; N3 PM-01c, CC-01..04, RV-18; N4 P-06 |

## 5. Rules (final check)
- No invented numbers: no ideal cutscene or shot length, skip delay, camera speed, lens mood or phone budget. UNKNOWN stays UNKNOWN until our own previs or capture measures it.
- Effects of angles, lenses, moves and colours are written as conditional ("can", "when"), with the context.
- A cinematic never decides a reward, a boss defeat, a teleport or a trade: the server does (`AGENTS.md` §2; N3 DN-08).
- Story, names, feel and lengths are PROPOSALS until the owner confirms; the owner chooses between alternatives.
- Mature, romantic, violent, horror or franchise content: `platform-policy` at design time and at review.
- Flash and shake: `vfx-design` safety rules; a reduced-motion version exists for every authored move that shakes, rolls or whips.
- The director briefs and reviews the crafts; it never silently replaces their execution or the owner's approval (N3 DN-09).

## 6. Self-check before returning
- [ ] Beat contract has five items and the owner's approval; essential vs optional information split.
- [ ] Camera mode chosen with a one-line reason.
- [ ] Every beat: event that changes knowledge, active intention, question carried forward.
- [ ] Every shot: a job, an emotion change, what it shows and leaves out, a move reason (or static), a cut reason.
- [ ] Continuity ledger: positions, travel direction, eyelines, light direction, props, action phase at each cut.
- [ ] Acting written as cause and decision, checked against what the rig and face kit can show.
- [ ] Every cue has a relationship to picture; silence named where used.
- [ ] Every ending specified with its first safe action; skip keeps the essential information; shared-scene contract answered.
- [ ] No number without our own measurement or an owner decision; effects written conditionally.
- [ ] Alternatives with a recommendation for every choice that changes the player's experience.

Project overlay: if `knowledge/overlays/film-direction.md` exists, read it after this file; it wins for this game.
