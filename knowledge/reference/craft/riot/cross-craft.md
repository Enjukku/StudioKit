---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1b: synthesis of knowledge/jobs/J018-riot-craft/extracts (owner-supplied Riot transcripts, 14 videos)"
supersedes: []
roles: [orchestrator, art-director, game-designer, animator, vfx-designer, sound-designer, film-director, modeler, character-rigger, ui-ux-designer, environment-designer, marketing, reference-images, feature-builder, architect, reviewer, qa-lead]
---
> Author: J018 synthesizer · claude-opus-5-5 · high · 2026-10-21

# Cross-craft work

ADDED TOPIC (prefix CC). How crafts work as one team: one target, one timing contract, building for the next maker, leaving room for the next maker, sharing motifs, and splitting big jobs. Folds in the extract topics cross-craft handoff, cross-craft cohesion and crew split. In our studio this maps to the direction sheet, contracts, sideways exchange notes and the integrator role (`rules/company.md`).
Related: blockout ownership in `game-design-fun.md` (GD-31), feedback order in `critique-feedback.md`, rig-ready building in `pipeline-production.md` (PP-12).
The line marked (DS) in CC-02 was added in stage 1c from the DestructionSimulator cross-check; it gives measured sync targets that differ from the older [inference] in the same check field.

### CC-01 One target experience, signed by every craft
- principle: Art, design, engineering, sound and VFX are interdependent; the best results come when all push toward one target and set each other up for easy wins. A release feels cohesive and immersive only when every craft serves one vision.
- why: Crafts that only follow each other cannot support each other's strengths; mismatched crafts break immersion.
- apply: The leads write one shared target experience before work splits (the kit's direction sheet, which every craft signs); each craft's brief cites that line and names how it helps the others; reviews check every craft against the direction sheet.
- check: Every craft brief quotes the same target-experience line; the review checks each craft's output against the direction sheet and lists mismatches.
- mistake: Designers make the rules and artists "just make it look pretty" (R00d:5290-5296).
- examples:
  - R00d: a target experience so "art and design are aiming in the same direction" (R00d:5280-5308).
  - R03: a skin feels cohesive when SFX, VFX and art collaborate on one vision (R03:1072-1080).
- roblox_fit: No change.
- roles: orchestrator, art-director, game-designer, architect, feature-builder, sound-designer, vfx-designer, animator, modeler
- also: game-design-fun, style-identity
- sources: R00d-F24 (R00d:5280-5308); R03-F46 (R03:1072-1080)

### CC-02 One marker list is the timing contract for animation, VFX and sound
- principle: Animation is the hub between design, tech, VFX and audio: it agrees frame lengths with design and joins early. The first step of syncing is a frame-accurate marker at every synced event (contact, release, impact, scene cut); VFX and sound key from those markers, and a sound's transient sits exactly on its contact frame.
- why: Sound or flash one frame off reads loose or late; late involvement means infeasible requests or wasted potential; a timing change that does not reach VFX and sound breaks the hit.
- apply: The animator joins at design time and returns the frame count and named markers (contact, release, impact) in the contract; VFX and sound cue cards reference those marker names; any timing change goes to VFX and sound in the same hand-back. Sound files are trimmed so they start at their transient; cutscenes mark every cut.
- check: Each gameplay clip has a frame length agreed with the game designer and named markers in the contract; `clip_check.py events` finds no missing marker; frame-stepping the capture shows the transient peak on the contact frame, inside the window in the next line (the earlier [inference] "1 frame early is safer than late" is retired by the lead, J018 G1 prep: it contradicts the sync evidence); no sound file has leading silence.
- check (DS): DS's sync evidence (broadcast standards and studies) differs from the [inference] above: an early sound is noticed sooner than a late one, so target the sound onset 0 to about 40 ms after the first lit punch frame and never more than 1 frame (16.7 ms at 60 fps) early; schedule picture punch and sound transient from one trigger event; a steady small delay beats a jittering one; measure on the target device (phone speaker and Bluetooth), since code-simultaneous is not output-simultaneous (DS:vfx-design/references/juice-repetition-sync.md:121-125, 128-132).
- mistake: Animations done without confirming "the right frame lengths" (R04:172-174); placing sounds by ear across a scene without sync points (R07:211-213).
- examples:
  - R04: animation as "a bit of a hub" and a "go-between" (R04:162-190).
  - R07: a frame-accurate marker on each gauntlet hit as the sync point (R07:211-215, 365, 502).
- roblox_fit: Animation markers fire through AnimationTrack:GetMarkerReachedSignal (knowledge/external/roblox-creator-docs/animation/events.md:12, 47-72); network and play-start latency move sounds later on clients, so trigger hit sounds and flashes on the client that sees the hit [inference, unverified].
- roles: animator, game-designer, vfx-designer, sound-designer, film-director, feature-builder, orchestrator, qa-lead
- also: weight-timing, sound, vfx-reads-timing, rhythm
- sources: R04-F07 (R04:162-190); R07-F05 (R07:211-215, 365, 502)

### CC-03 Build for the next craft: ask what they need first
- principle: Work must not be a pain for the next maker: a model must fold right for the rigger and animator; a concept must answer the questions the 3D maker will have, not create new ones. Ask the next craft its needs before building.
- why: A model that deforms badly breaks every animation and is expensive to fix after rigging; gaps in a concept become guesses.
- apply: Before modelling, read the rig sheet (`rig-pipeline`) and ask the rigger for joint positions, cut points and moving parts; record the agreed points in the contract. Reference-images output includes the views and notes modelers and riggers need (back view, moving parts, joint use); the art director stays reviewer through the build.
- check: Extreme-pose tests (full elbow bend, knee bend, arm raised) with a test rig show no spikes, collapses or interpenetration; the downstream hand-back lists zero unanswered design questions.
- mistake: Working only for your own craft's look (R03:266-268); creating "extra questions for a character artist to solve" (R01).
- examples:
  - R03: elbows folding "like a box with many loops"; ask the next people their needs (R03:248-270, 276-286).
  - R01: coattails planned on existing bones "without worry of making an animator or a tech artist mad at us" (R01:244-256, 398-407).
- roblox_fit: Roblox characters use skinned Bones or Motor6D rigid parts (see `rigging-design`).
- roles: modeler, character-rigger, animator, art-director, reference-images, vfx-designer, orchestrator
- also: pipeline-production, character-design
- sources: R03-F12 (R03:248-270, 276-286); R01-F14 (R01:244-256, 398-407)

### CC-04 The concept leaves room for the next crafts' decisions
- principle: The concept fixes the idea and invites the specialists: motion and effect sketches show the feeling to inspire, not to dictate timing or technique.
- why: Downstream crafts own their decisions; over-specified concepts block better solutions.
- apply: Reference images and concept briefs fix the idea, silhouette and colour roles and mark animation and VFX opportunities as intent notes (what should move, what should glow); timing and technique are left to the animator and VFX designer.
- check: The concept hand-off names where motion and effects go without fixing frame timings or particle settings; each downstream craft gets an open question, not a fixed answer.
- mistake: The concept dictating rules for the whole team.
- examples:
  - R12: "I'm creating a canvas for the rest of the team"; sketches of a knife opening and a sword sliding to inspire VFX and animation (R12:35-39, 360-364).
- roblox_fit: Same in our pipeline: reference-images sets the target, specialists build in Blender and Studio.
- roles: art-director, reference-images, modeler, animator, vfx-designer, orchestrator
- also: references-ideation, process-iteration
- sources: R12-F02 (R12:35-39, 360-364)

### CC-05 Share strong motifs across crafts; seek input from several roles
- principle: Any craft can change another's direction: a motif found in an illustration can become the shape language of a whole release, and a design idea can change the art's palette. A pitch that feels derivative becomes unique when diverse people add ideas.
- why: A motif that runs through art, design, UI and story makes a release feel like one thing; different perspectives find angles one author misses.
- apply: When one craft finds a strong motif, record it in the contract or art bible so UI, VFX, environment and marketing reuse it. New theme or concept proposals get independent proposals from several roles before G1 ("the right leads agree first").
- check: The motif appears in each craft's output for the release (UI frame, VFX shape, key art); the proposal record shows input from more than one role.
- mistake: A single author shipping a derivative idea; a motif that stays in one craft's file [inference].
- examples:
  - R05: circular line work from the illustration became an episode's shape language; attacker red and defender green changed the art's palette (R05:401-423).
  - R01: the skins team as "one of the most diverse teams" he has worked on (R01:813-822).
- roblox_fit: No change.
- roles: art-director, orchestrator, ui-ux-designer, marketing, vfx-designer, environment-designer, game-designer, reviewer
- also: style-identity, critique-feedback
- sources: R05-F13 (R05:401-423); R01-F46 (R01:813-822)

### CC-06 Split a big craft job by category, with one integrator and a shared library
- principle: Two makers can split a large job by category (tonal and magic, ice, mechanisms, environment), work in parallel, hand building blocks across through a shared library, then merge and review together under one integrator.
- why: Parallel specialisation is fast; a shared library makes hand-off easy; one integrator keeps it one design.
- apply: For large sound (or VFX) jobs, the orchestrator splits by category with one owner per category and one integrator; hand-off is through library files (SD-30); the integration review is done together.
- check: Each category has one owner; the integration review is logged; the parts used come from the shared library.
- mistake: Parallel makers with no integrator, producing parts that do not fit [inference].
- examples:
  - R07: tonal material and a shot passed through the shared library; the other designer integrates (R07:50-53, 139-141, 316-317, 345, 564-574).
- roblox_fit: No change.
- roles: orchestrator, sound-designer, vfx-designer
- also: pipeline-production, sound
- sources: R07-F31 (R07:50-53, 139-141, 316-317, 345, 564-574)
