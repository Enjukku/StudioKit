---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 2
supersedes: []
---
> Author: J018 maker animator · claude-opus-5-5 · high · 2026-10-22

# J018 coverage: animator

Books rebuilt: `.agents/roles/animator.md` (body), `.agents/skills/animation-design/` (SKILL.md + references), `.agents/skills/animation-craft/` (SKILL.md + references; evals untouched). Paths below are relative to `.agents/skills/` unless they start with `roles/`. Tagged findings: 139; untagged findings used: 16; rejected: 2 (CF-18, CF-19; CD-21 is a partial landing).

## a. Findings

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| CD-01 | Know the character, then decide on their behalf | animation-design/SKILL.md §3 step 1 (feel words, subtext), step 5; animation-design/references/principles.md §6 P-06.1-P-06.3 | step / standard | |
| CD-04 | Variants hold the identity anchors and change the rest | animation-design/references/sets-and-states.md §1 (variants keep the base); animation-design/references/review.md §8c G-08; animation-design/SKILL.md §9 #11 | standard / self-review check / core principle | |
| CD-06 | Keep the likeness the same in every product | animation-design/references/sets-and-states.md §1 (identity across the set and variants); animation-design/references/review.md §8c G-08 | standard / self-review check | |
| CD-07 | The fantasy must survive every real view | animation-design/SKILL.md §3 step 1-2 (camera, phone size, side the camera sees); animation-design/references/review.md §8c G-01, G-10 | step / self-review check | |
| CD-09 | Every action shows who this character is | animation-design/references/principles.md §6 P-06.1; animation-design/SKILL.md §4 P-08; animation-design/references/review.md §8a B-14; animation-design/references/worked-examples.md §1 | standard / self-review check / example | |
| CD-10 | Believable anatomy and plausible construction | animation-design/references/body-and-species.md §1 (anatomy first) | standard | |
| CD-11 | Invent creatures from real anatomy | animation-design/references/body-and-species.md §3 (hybrid and invented creatures) | standard | |
| CD-12 | Design for motion: test extreme poses, keep mass off the joints | animation-design/SKILL.md §3 step 3 (stress poses test costume near joints); animation-design/references/body-and-species.md §1; roles/animator.md work method step 2 | step | |
| CD-13 | Twist the tone within bounds; darker still keeps the appeal | animation-design/references/principles.md §6 P-06.9 | standard | |
| CD-15 | Re-theme the abilities, not only the costume | animation-design/references/sets-and-states.md §1 (a variant may re-theme an ability's flourish, never the tell) | standard | |
| CD-21 | Explore costumes on varied poses and body types | animation-design/SKILL.md §3 step 6 (2-3 key-pose options, one pushed further) | step (partial) | partial: costume exploration on varied body types belongs to the art director and reference-images (costume sheets); the animator takes only the pose variety |
| CD-22 | Put the eyes and face in early | animation-design/references/body-and-species.md §2 neck and head row (gaze direction is part of the pose from blocking); animation-craft/SKILL.md §3 step 4 | step | |
| CD-23 | Brows, face structure and nose carry identity | animation-design/references/body-and-species.md §2 eyes and face row (brows carry identity, pushed to read) | standard | |
| CD-24 | Eyes act in fast turns | animation-design/references/principles.md §7 P-07.5; animation-design/references/body-and-species.md §2 neck and head row, §4; animation-design/references/review.md §8b S-15, S-17; animation-craft/SKILL.md §4 C-26 | standard / self-review check | |
| CD-25 | Start promo and story art from a premise and the signature ability pose | animation-design/references/principles.md §6 P-06.11 (premise in one sentence; reuse the signature key pose from the set; black-fill compare with the clip's key frame), §4 P-04.4 (flow lines in a held promo pose); animation-design/references/review.md §8a B-17; animation-design/references/game-timing.md §6 marketing / film-director row; animation-design/references/worked-examples.md §1 promo still; animation-design/SKILL.md §6 characters row; animation-craft/references/blender-keying.md §7 promo still; roles/animator.md partner table (marketing row) | standard / self-review check / hand-off / example / step | |
| CD-27 | Hard cases: scary creature-humanoids and multi-form characters | animation-design/references/body-and-species.md §3 (scale; scary creatures turn silly); animation-design/references/sets-and-states.md §1 (several forms = several sets) | standard | |
| CF-01 | Big to small: composition first, detail and effects last | animation-design/SKILL.md §1 governing idea (big before small); animation-design/SKILL.md §9 #4; animation-craft/SKILL.md §3 steps 4-7 | core principle / stage order | |
| CF-02 | Design and pose for the side the game camera shows | animation-design/SKILL.md §3 step 2 (side the camera sees); animation-design/references/principles.md §5 P-05.2; animation-design/references/review.md §8a B-04 | step / self-review check | |
| CF-09 | Lines on an object lead somewhere and agree with each other | animation-design/references/principles.md §4 P-04.4 (one line of action; hair, cloth, trail follow it) | standard | |
| CF-10 | Converging motion pulls the eye to the focus | animation-design/references/principles.md §9 P-09.9 (gathering motion converges on the source before the release) | standard | |
| CF-18 | Camera height states status | — | — | rejected: camera height is the film-director's and marketing's choice; the animator states status through pose and feel words (P-06.2) |
| CF-19 | Small secondary elements carry movement and colour pops along the eye path | — | — | rejected: small accent elements along the eye path are VFX and environment placement; animator secondary motion is ranked by cause (P-07.4) instead |
| CR-01 | Judge in the game, at the game camera, in the real place, moving | animation-design/SKILL.md §3 step 10; animation-design/references/review.md §1, §8c G-01; animation-craft/SKILL.md §3 step 11; animation-craft/references/roblox-playback.md §10 | step / self-review check | |
| CR-03 | Solve the problem behind the note; separate goals from tactics | animation-design/references/review.md §4 (problem behind the note; goal vs tactic) | standard | |
| CR-05 | Give and solve visual notes as paint-overs on a capture | animation-design/references/review.md §4 (a marked capture or posed proxy as the visual note) | standard | |
| CR-07 | No grand reveals: show early and often, partner crafts first | animation-craft/SKILL.md §3 step 4 (blocking check-in before spline); roles/animator.md work method step 7 | stage | |
| CR-16 | Calibrate on simple basics in many moods | animation-design/references/principles.md §8 P-08.4 | standard | |
| CR-17 | Say what each input can prove; end with a could-not-check list | animation-design/references/review.md §5 (what each input can prove; could-not-check list); animation-craft/references/roblox-playback.md §10; animation-design/references/review.md §8c G-04 | quality bar / self-review check | |
| CC-01 | One target experience, signed by every craft | animation-design/references/game-timing.md §6 hand-offs (art director, gameplay rows); roles/animator.md partner table | step | |
| CC-02 | One marker list is the timing contract for animation, VFX and sound | animation-design/SKILL.md §3 step 8; animation-design/references/game-timing.md §4 (stage names, sync rule); animation-design/references/review.md §8c G-03, G-04; animation-design/SKILL.md §9 #17 | standard / self-review check / core principle | |
| CC-03 | Build for the next craft: ask what they need first | animation-design/references/game-timing.md §6; roles/animator.md 'What you ask for, and when' | step | |
| CC-04 | The concept leaves room for the next crafts' decisions | animation-design/references/game-timing.md §6 (join at concept time; supply feasibility); roles/animator.md reference-images bullet | standard | |
| EX-01 | Larger than life: extend and sharpen what must read | animation-design/references/principles.md §10 P-10.1; animation-design/SKILL.md §4 P-12 | standard | |
| EX-02 | Make a pose specific by layering adjectives, then pull back if too far | animation-design/references/principles.md §6 P-06.2; animation-design/SKILL.md §3 step 1 (feel words mapped to visible change) | standard / step | |
| EX-03 | For comedy, pose against the character's known trait | animation-design/references/principles.md §6 P-06.7; animation-design/SKILL.md §3 step 6 (comic contradiction option); animation-design/references/review.md §8a B-13 | standard / self-review check | |
| EX-04 | Emotes and reactions: maximum expression for a two-second read | animation-design/references/principles.md §6 P-06.8; animation-design/references/review.md §8a B-13; animation-design/references/worked-examples.md §1 | standard / self-review check / example | |
| EX-05 | A believable base earns the extremes; break only the joints that can take it | animation-design/references/principles.md §10 P-10.2, P-10.3, P-10.5; animation-design/SKILL.md §4 P-12; animation-design/references/review.md §8a B-11 | standard / self-review check | |
| EX-06 | Squash on contact, stretch on speed, by a Roblox-safe route | animation-design/SKILL.md §5 (squash and stretch need a Roblox route; volume); animation-craft/SKILL.md §4 C-22; animation-design/references/principles.md §3 P-03.7 | standard / engine fact | |
| EX-07 | Cartoony hang time: hold near the apex, then fall fast | animation-design/references/principles.md §3 P-03.6; animation-design/references/review.md §8b S-09; animation-design/references/worked-examples.md §1/§4 | standard / self-review check | |
| EX-08 | A small overshoot releases energy | animation-design/references/principles.md §10 P-10.4; animation-design/references/review.md §8b S-12; animation-craft/references/motion-specs.md §2 item 10 | standard / self-review check | |
| EX-09 | Always animate the shoulders and hips | animation-design/references/principles.md §2 P-02.7; animation-design/references/body-and-species.md §2 shoulders row; animation-craft/SKILL.md §4 C-24; animation-design/references/review.md §8b S-13; animation-design/SKILL.md §3 step 9 (K2) | standard / self-review check / engine fact | |
| EX-10 | Energy flows out to the fingertips; hands matter even when tiny | animation-design/references/principles.md §5 P-05.5; animation-design/references/body-and-species.md §2 hands row; animation-design/references/review.md §8b S-17 | standard / self-review check | |
| GD-01 | Every asset has jobs: clarity first, then feel, then style | animation-design/SKILL.md §1 (three jobs, in order; three questions); animation-design/references/principles.md §1 P-01.5; animation-design/references/review.md §1 | standard | |
| GD-02 | Every action gets immediate feedback; reached goals get a short celebration | animation-design/references/game-timing.md §2 (player's own move answers the input at once); animation-design/references/game-timing.md §4 attempt vs outcome | standard | |
| GD-06 | Movement patterns give enemies character | animation-design/references/principles.md §6 P-06.10; animation-design/SKILL.md §6 creatures row | standard | |
| GD-09 | Mechanics and numbers are design constraints for art | roles/animator.md partner table (game-designer: mechanics, numbers, windows); animation-design/SKILL.md §3 step 1 | step | |
| GD-13 | Fairness comes from clear expectations and consistency | animation-design/SKILL.md §9 #7 (same attack, same tell); animation-design/references/game-timing.md §7; animation-design/references/review.md §8c G-09; animation-design/references/worked-examples.md §4 | core principle / self-review check | |
| GD-21 | Low mental load on the player's own character | animation-design/references/review.md §8c G-10 (own move identifiable from silhouette in the busiest moment); animation-design/SKILL.md §3 step 1 (who must react) | self-review check | |
| GD-34 | Feedback follows the real outcome: a small cue on input, the big layer on confirmed success | animation-design/references/game-timing.md §4 attempt vs outcome; animation-design/SKILL.md §7 rule; animation-design/references/review.md §8c G-05; animation-design/SKILL.md §9 #19; animation-design/references/worked-examples.md §2 | standard / rule / self-review check / core principle | |
| LC-21 | Test colours where parts overlap | animation-design/references/principles.md §5 P-05.9; animation-design/references/review.md §8b S-21 | standard / self-review check | |
| PP-02 | Rich form first, then a budgeted game mesh with loops where it bends | animation-design/SKILL.md §3 step 3 (stress poses reveal bend zones for the rigger) | step | |
| PP-12 | Build to the shared rig: reuse its joints, match it, model what it moves | animation-design/references/sets-and-states.md §1 (shared clips replayed on a variant mesh) | standard | |
| PP-13 | Keep the contact points fixed in every variant | animation-design/references/sets-and-states.md §1 (contact points fixed across variants); roles/animator.md partner table (modeler) | standard | |
| PP-14 | Design moving parts with room to move | animation-design/references/sets-and-states.md §2 weapon row (inspect: moving parts slide without clipping); animation-design/references/review.md §8b S-20 | standard / self-review check | |
| PP-15 | Spend expensive features only where they earn it | animation-design/SKILL.md §3 step 3 (flag costly parts with a cheap fallback); roles/animator.md partner table (rigger) | step | |
| PP-18 | Rigs are tested in extreme poses before animation | animation-craft/SKILL.md §3 step 2 (S6 stress poses on the real rig) | step (kept from old book) | |
| PP-19 | Controls are puppet strings with planted feet | animation-craft/SKILL.md §3 step 2 (key controls only, contacts held); animation-design/references/review.md §8b S-01 | step / self-review check | |
| PP-20 | A character is many clips that interrupt and blend: plan the states first | animation-design/references/sets-and-states.md §1 (plan the state machine before keying; clips made to blend), §3; animation-design/references/review.md §8c G-07 | standard / self-review check | |
| PP-21 | Read the curves behind the motion | animation-design/references/principles.md §8 P-08.8; animation-design/references/review.md §1 item 6, §8b S-18; animation-craft/references/blender-keying.md §8 | standard / self-review check | |
| PP-22 | Shape eases with tangents, not extra keys | animation-design/references/principles.md §8 P-08.9; animation-craft/references/blender-keying.md §3; animation-craft/SKILL.md §3 step 6 | standard / step | |
| PP-23 | Fix gimbal flips at the source | animation-design/references/principles.md §8 P-08.10; animation-design/references/review.md §3 (gimbal row); animation-design/references/review.md §8b S-18 | standard / self-review check | |
| PI-01 | The cheapest stage goes first; expect big changes while it is rough | animation-design/SKILL.md §9 #15; animation-craft/SKILL.md §3 step 4 | core principle / stage | |
| PI-06 | Work in passes over the whole; big things before small | animation-craft/SKILL.md §3 steps 4-7 (passes over the whole clip); animation-design/references/principles.md §8 P-08.1 | stage | |
| PI-07 | One named problem per pass; fix the worst first | animation-design/references/principles.md §8 P-08.7; animation-craft/SKILL.md §3 step 7; animation-design/references/review.md §4 | standard / step | |
| PI-08 | Find the right number by bracketing | animation-design/references/principles.md §8 P-08.11 (numbers first, renders inside the plan budget); animation-design/references/review.md §5 (plan-stage budget), §8 intro; animation-design/references/game-timing.md §5 (the gameplay owner and VFX bracket the hit-stop; the animator supplies freeze-frame takes) | standard | |
| PI-09 | Not precious: most attempts fail, so delete, redo and let go | animation-design/references/principles.md §8 P-08.3; animation-craft/SKILL.md §3 step 7; animation-design/SKILL.md §9 #15 | standard | |
| PI-10 | Park a stuck part and come back | animation-design/references/principles.md §8 P-08.12 | standard | |
| PI-11 | A time box forces the readable choice | animation-design/references/review.md §6 (pass budget in the brief); roles/animator.md work method step 1 (stop criteria) | quality bar | |
| PI-12 | Know when it is done: written stop criteria, repeating notes | animation-design/references/review.md §6; animation-design/SKILL.md §9 #18 | quality bar / core principle | |
| PI-15 | Decisive marks: few bold decisions, not many small tweaks | animation-design/references/principles.md §8 P-08.13 | standard | |
| RI-08 | Reference order: our game first, then the real world, then mix; take ideas, never copy | animation-design/references/body-and-species.md §6 (reference order, take ideas never copy); animation-design/SKILL.md §3 step 5 | step | |
| RI-09 | When a brief fuses two ideas, reference the overlap | animation-design/references/body-and-species.md §6 (reference the overlap of fused ideas) | standard | |
| RI-10 | Study the real thing closely for the details invention misses | animation-design/references/body-and-species.md §6 (real observation adds what invention misses) | standard | |
| RI-12 | Get enough reference; make the missing one | animation-design/references/body-and-species.md §6 (make the missing reference: mannequin, test pose, pose image); animation-design/SKILL.md §3 step 5 | step | |
| RI-15 | Learn by recreating work you love, then twist it | animation-design/references/body-and-species.md §6 (a new motion style: study 2-3 successful clips structurally in numbers, then change toward our feel words; never copy a clip) | standard | |
| RI-24 | Act it out: agents write the performance beat by beat | animation-design/SKILL.md §3 step 5 (beat sheet: motion, time, sound word, subtext); animation-design/references/principles.md §6 P-06.6; animation-design/references/body-and-species.md §6; animation-design/references/review.md §8a B-12 | stage / standard | |
| RI-25 | Pose to pose from motion reference | animation-design/references/body-and-species.md §6 (pose to pose from reference; key poses reviewed as stills) | standard | |
| RI-26 | The same key poses can tell different stories: try two | animation-design/SKILL.md §3 step 6 (two timing takes on key clips); animation-design/references/principles.md §6 P-06.3 | stage | |
| RH-01 | Vary the cadence: fast and slow beats, never metronomic | animation-design/references/principles.md §4 P-04.1 (beat gaps listed in frames); animation-design/references/game-timing.md §7; animation-design/references/review.md §8a B-07 | standard / self-review check | |
| RH-02 | No twinning: offset paired parts for two reads | animation-design/references/principles.md §4 P-04.2; animation-design/references/review.md §8b S-14; animation-design/SKILL.md §9 #12; animation-craft/references/blender-keying.md §8 twinning | standard / self-review check / core principle | |
| RH-03 | Every effect tells a beginning, a middle and an end | animation-design/references/principles.md §4 P-04.5; animation-design/references/game-timing.md §7 | standard | |
| RH-04 | Block holds as copied key pairs, not stepped keys | animation-craft/references/blender-keying.md §3 (holds as copied key pairs; stepped only for a quick pose review); animation-craft/SKILL.md §3 step 4; animation-design/references/review.md §8a B-09 | standard / self-review check | |
| RH-05 | Put motion into a still with a few committed flow lines | animation-design/references/principles.md §4 P-04.4 (flow lines continue the line of action in a held pose) | standard | |
| SS-01 | Silhouette first, then light that shows form, detail last | animation-craft/SKILL.md §3 step 4 (root, then poses; black-fill before detail); animation-design/SKILL.md §9 #4 | stage | |
| SS-02 | Judge the silhouette filled solid, small and squinted | animation-craft/references/blender-keying.md §7 (black-fill renders); animation-design/references/review.md §8a B-02; animation-design/SKILL.md §3 step 6 | stage / self-review check | |
| SS-04 | Keep the few identifying elements, make them chunky, cut the rest | animation-design/SKILL.md §3 step 2 (identity anchors and hook shapes listed); animation-design/references/review.md §8a B-03 | step / self-review check | |
| SS-05 | Shape language carries meaning: sharp is danger, round is friendly | animation-design/SKILL.md §9 #5 (sharp, angular timing for aggressive subjects; soft arcs for friendly) | core principle | |
| SS-06 | One shape vocabulary for the whole game, down to the small shapes | animation-design/SKILL.md §9 #7 (one motion language, the art bible's motion line) | core principle | |
| SS-08 | Slopes make direction; tilt shapes along the action | animation-design/references/principles.md §4 P-04.6 | standard | |
| SS-10 | Line of action and gesture before detail | animation-design/references/principles.md §4 P-04.4; animation-design/SKILL.md §4 P-07; animation-design/references/review.md §8a B-02 | standard / self-review check | |
| SS-11 | Give the jump apex a pose: legs tucked into a V | animation-design/references/principles.md §5 P-05.6; animation-design/references/worked-examples.md §1 | standard / example | |
| SS-12 | Body shape predicts movement | animation-design/references/principles.md §5 P-05.8; animation-design/references/body-and-species.md §1; animation-design/SKILL.md §3 step 2 | standard / step | |
| SS-13 | Players must track hands, head and feet | animation-design/references/review.md §8a B-03 (hands, head, feet separate) | self-review check | |
| SS-14 | Nothing hangs in front of the shoulders and arms | animation-design/references/principles.md §5 P-05.4 (a drape across the arms) | standard | |
| SS-15 | Show the hook shapes at the held moments of motion | animation-design/references/principles.md §5 P-05.3; animation-design/references/game-timing.md §5 (freeze frame faces the camera); animation-design/references/review.md §8a B-03, §8c G-06 | standard / self-review check | |
| SS-19 | Design the group silhouette | animation-design/references/principles.md §5 P-05.10; animation-design/references/review.md §8a B-15 | standard / self-review check | |
| SS-20 | Backdrop pieces: simple surfaces, elegant gesture | animation-design/references/principles.md §9 P-09.11; animation-craft/references/ambient-at-scale.md §3 (sway follows the gesture) | standard | |
| SD-03 | Ambience, foley and one signature element put the player in the world | animation-design/references/game-timing.md §6 sound row (contact events for footsteps per surface) | step | |
| SD-04 | The sound theme comes from what the thing does in play | animation-design/references/game-timing.md §4 (an ability moves like its mechanic verb, the same verb as the VFX frame script and sound cue card); animation-design/SKILL.md §3 step 5 (verb in the beat sheet), step 8; animation-design/references/review.md §8a B-16; animation-design/SKILL.md §9 #8 | standard / step / self-review check | |
| SD-05 | Stage the action: one sound per named stage | animation-design/references/game-timing.md §4 (use the same stage names: load, charge, release, travel, impact, tail) | standard | |
| SD-07 | Shape the envelope: the attack and transient make the hit land | animation-design/references/principles.md §3 P-03.13 (wind-up and follow-through as attack and release); animation-design/references/game-timing.md §4 sync rule | standard | |
| SD-22 | Characters sound like who they are, and sound telegraphs their state | animation-design/references/game-timing.md §4 (a state with a timer or a breaking point gets a building tell before it ends, as a named event); animation-design/SKILL.md §3 step 8, §6 creatures row; animation-design/references/review.md §8a B-16; animation-design/references/principles.md §9 P-09.2 (stress before a structure fails) | standard / step / self-review check | |
| SI-05 | Make it for a specific audience, and give fans what they want | animation-design/SKILL.md §3 step 1 (one line on what the target players want) | step | |
| UI-11 | The static state explains; motion and sound make it felt | animation-design/references/principles.md §9 P-09.1 (the end state explains the change with no motion); animation-craft/references/motion-specs.md §2 item 10 | standard | |
| UI-16 | Motion goal: a physical material that carries the brand | animation-design/SKILL.md §9 #7 (the art bible's motion line); animation-design/references/game-timing.md §7 | core principle | |
| VR-01 | Specify the read (shape, colour, timing), then pick the cheapest technique | animation-design/SKILL.md §5 technique choice (read first, cheapest technique) | standard (kept) | |
| VR-02 | Rank every effect's layers: primary, secondary, tertiary | animation-design/SKILL.md §9 #3 (rank what reads first); animation-design/references/principles.md §7 P-07.3 | core principle | |
| VR-09 | The hit is one peak frame between cause and result | animation-design/references/game-timing.md §7 (one peak per action) | standard | |
| VR-21 | Camera and screen punches are rare, local, rotation-only and gated by importance | animation-design/references/game-timing.md §1 (never bake camera motion into a gameplay clip), §5 (weight in pose when the camera is far or shake is off) | standard | |
| VR-22 | Hit-stop is local, short and scaled by hit strength | animation-design/references/game-timing.md §5; animation-craft/SKILL.md §4 C-25; animation-craft/references/roblox-playback.md §9; animation-design/references/review.md §8c G-06 | standard / engine fact / self-review check | |
| VR-23 | Every intense channel has an off path that keeps the information | animation-design/references/game-timing.md §8; animation-craft/SKILL.md §4 C-27; animation-design/references/review.md §8c G-02; animation-craft/references/motion-specs.md §2 item 11 | standard / self-review check | |
| VR-25 | Randomise decoration only; lock what carries meaning | animation-craft/references/ambient-at-scale.md §3; animation-design/references/sets-and-states.md §4 ambient row; animation-design/SKILL.md §9 #12 | standard / core principle | |
| VH-06 | The source of power is the primary read | animation-design/SKILL.md §4 P-18; animation-design/references/principles.md §5 P-05.7; animation-design/references/review.md §8a B-03 | standard / self-review check | |
| VH-08 | Silhouette is the first read, the face the second | animation-design/SKILL.md §3 step 2 (anchors in the outline); animation-design/SKILL.md §9 #5 | step / core principle | |
| WT-01 | Anticipation must read: long enough to react to, tight enough to feel strong | animation-design/SKILL.md §4 P-17; animation-design/references/principles.md §3 P-03.8; animation-design/references/game-timing.md §2; animation-design/references/review.md §8a B-06; animation-design/references/worked-examples.md §2, §4 | standard / self-review check / example | |
| WT-02 | One consistent physics lets players predict | animation-design/references/principles.md §1 P-01.3; animation-design/SKILL.md §9 #7; animation-design/references/review.md §8c G-09 | standard / self-review check | |
| WT-03 | Motion sets the emotional tone; giants move slowly | animation-design/references/principles.md §6 P-06.5; animation-design/references/game-timing.md §7; animation-design/references/review.md §8c G-15 | standard / self-review check | |
| WT-04 | Keys tell the story; place every breakdown on purpose | animation-design/references/principles.md §3 P-03.10; animation-design/SKILL.md §7 rule; animation-design/references/review.md §3; animation-craft/SKILL.md §3 step 5 | standard / rule / step | |
| WT-05 | Root first, then poses, then offsets, then details | animation-craft/SKILL.md §3 step 4 (pass 1 root and feet, pass 2 poses on shared frames); animation-design/references/review.md §8a B-01 | stage / self-review check | |
| WT-06 | Shift the weight before a foot moves | animation-design/references/principles.md §2 P-02.1, P-02.2; animation-design/references/review.md §8b S-01; animation-design/references/sets-and-states.md §3 | standard / self-review check | |
| WT-07 | Centre of gravity over the feet, unless off-balance is the point | animation-design/references/principles.md §2 P-02.4; animation-design/references/review.md §8a B-05 | standard / self-review check | |
| WT-08 | Held objects show weight by distance from the body | animation-design/references/principles.md §2 P-02.5; animation-design/references/review.md §8b S-20; animation-design/references/worked-examples.md §3 | standard / self-review check | |
| WT-09 | Uneven spacing and eases sell gravity | animation-design/references/principles.md §3 P-03.2; animation-design/references/review.md §8b S-07; animation-craft/references/blender-keying.md §8 | standard / self-review check | |
| WT-10 | Moving parts travel on arcs | animation-design/references/principles.md §4 P-04.3; animation-design/references/review.md §8b S-08; animation-craft/references/blender-keying.md §8 | standard / self-review check | |
| WT-11 | Bursts reach size fast and ease out slowly | animation-design/references/principles.md §9 P-09.8; animation-design/references/worked-examples.md §10 | standard | |
| WT-12 | Build-ups rise: smaller to bigger, dim to bright, low to high | animation-design/references/principles.md §9 P-09.9 | standard | |
| WT-13 | Cause first, then effect: a short beat between them, timed in tenths | animation-design/references/game-timing.md §7 (result after its cause, tenths of a second); animation-design/references/review.md §8a B-07 | standard / self-review check | |
| WT-14 | Mass cannot vanish | animation-design/references/principles.md §2 P-02.3; animation-design/references/review.md §8b S-02 | standard / self-review check | |
| WT-15 | Counterbalance makes fast moves believable | animation-design/references/principles.md §2 P-02.9; animation-design/references/review.md §8b S-03 | standard / self-review check | |
| WT-16 | The driving limb leads; momentum carries through the poses | animation-design/references/principles.md §1 P-01.2, §2 P-02.10; animation-design/references/review.md §8b S-04 | standard / self-review check | |
| WT-17 | Hold the first pose before moving (showcase clips) | animation-design/references/principles.md §3 P-03.12; animation-design/references/review.md §8a B-10 | standard / self-review check | |
| WT-18 | Keep the head stable in world space; turn it late and fast | animation-design/references/principles.md §7 P-07.5; animation-design/references/body-and-species.md §2 neck row; animation-design/references/review.md §8b S-15; animation-design/SKILL.md §3 step 9 (K2 head orient) | standard / self-review check | |
| WT-19 | Push off with force: feet stay down, then a sharp exit | animation-design/references/principles.md §3 P-03.3; animation-design/references/review.md §8b S-05 | standard / self-review check | |
| WT-20 | Do not stall travel mid-air | animation-design/references/principles.md §3 P-03.11; animation-design/references/review.md §8b S-06; animation-design/references/review.md §3 | standard / self-review check | |
| WT-21 | Fast contact; delete frames until the hit lands | animation-design/references/principles.md §3 P-03.5; animation-design/references/review.md §8b S-10 | standard / self-review check | |
| WT-22 | Land low and strong, with tension; elbows sink | animation-design/references/principles.md §2 P-02.8; animation-design/references/review.md §8b S-11 | standard / self-review check | |
| WT-23 | Small changes in attack and release change the felt weight | animation-design/references/principles.md §3 P-03.13 | standard | |
| WT-24 | Secondary motion adds perceived value | animation-design/references/principles.md §7 P-07.6; animation-design/references/sets-and-states.md §1 | standard | |
| WT-25 | Animate hair as one mass, then offset down the chain | animation-design/references/principles.md §7 P-07.2 (one-frame offsets PROPOSAL); animation-design/references/review.md §8b S-16 | standard / self-review check | |

Untagged findings used (tagged for other roles, valuable for animation):

| ID | Title | Landed in (file § section) | As | Rejected: reason |
| --- | --- | --- | --- | --- |
| GD-35 | Paid random reveals are honest | animation-design/references/game-timing.md §9; animation-design/SKILL.md §7 rule; animation-design/references/worked-examples.md §8 egg row; animation-design/references/review.md §8c G-13; animation-design/SKILL.md §9 #19 | rule / self-review check / example / core principle | |
| VR-24 | Frequent effects are shorter, quieter, merged and capped | animation-design/references/game-timing.md §2 (frequency sets length); animation-design/references/review.md §8c G-11; animation-design/references/review.md §7 | standard / self-review check | |
| VR-26 | Pulse and blink rates carry meaning: slow is safe, fast is urgent, never above 3 Hz | animation-design/references/game-timing.md §8 (pulses at most 3 per second, slow safe, fast urgent); animation-craft/references/motion-specs.md §2 item 11; animation-design/references/review.md §8c G-12 | standard / self-review check | |
| VR-20 | The drawn danger area is the real hit area, from warning to last tick | animation-design/SKILL.md §5 (the picture tells the truth: reach, danger pose ends with danger); animation-design/references/review.md §8c G-14; animation-craft/references/motion-specs.md §2 item 12 | standard / self-review check | |
| VH-02 | Rank loudness across a set: if everything is loud, nothing is | animation-design/references/sets-and-states.md §2 (hit reactions by strength); animation-design/references/game-timing.md §4 (outcome layer scaled by strength) | standard | |
| VR-16 | Ambient environment effects: tiny, slow, partly hidden | animation-craft/references/ambient-at-scale.md §3 (ambient slower and smaller, partly hidden); animation-design/references/principles.md §9 P-09.11 | standard | |
| LC-01 | Reserve the gameplay colours; keep them, and fast motion, out of decoration | animation-craft/references/ambient-at-scale.md §3 (no fast motion in the play space); animation-design/references/review.md §8c G-12 | standard / self-review check | |
| CD-26 | Design a prop or a place as a character | animation-design/references/principles.md §9 P-09.10; animation-craft/references/motion-specs.md §2 item 10; animation-design/references/worked-examples.md §6 | standard / example | |
| CR-02 | Ask a goal question, never "do you like it?" | animation-design/SKILL.md §3 step 6 (goal question for the pick); animation-design/references/review.md §4 | step | |
| CR-13 | Close with an honest recap of your own result | animation-design/references/review.md §4 (honest weakness); roles/animator.md hand-back | quality bar | |
| PI-14 | "It would be cooler" is new scope: log it | animation-design/SKILL.md §7 rule; roles/animator.md working with other agents | rule | |
| SD-26 | Review the key event solo, then in the full mix | animation-design/references/review.md §1 item 4 (with and without effects); animation-design/references/review.md §8c G-01, G-02 | self-review check | |
| VH-04 | Judge noise in motion, with lighting and effects on | animation-design/references/review.md §8c G-01 (moving, with effects, other players and HUD on) | self-review check | |
| WL-21 | Scale: a player-sized reference in every blockout and scene | animation-design/SKILL.md §3 step 2 (player-sized reference in the study renders); animation-craft/references/blender-keying.md §7 | step | |
| WL-28 | Work from far away; zoom out every round | animation-design/references/review.md §1 (game camera at phone size first, close views after) | standard | |
| UI-12 | Motion goal: responsiveness | animation-design/references/game-timing.md §2 (the player's own move answers the input on the press frame or the next) | standard | |

## b. Universal principles

All 20 apply to animation. Section: `animation-design/SKILL.md` §9 "Core principles for this craft" (each row: standard, example, check, where).

| UP-ID | Applies (yes/no + reason) | Where in "Core principles for this craft" |
| --- | --- | --- |
| UP-01 | yes: every clip's first job is the gameplay read | §9 #1 |
| UP-02 | yes: clips are judged at the game camera, phone size, in the real place | §9 #2 |
| UP-03 | yes: the biggest pose change and fastest spacing go to the tell and contact | §9 #3 |
| UP-04 | yes: root, poses, offsets, then detail | §9 #4 |
| UP-05 | yes: line of action, signature shape, source of power, shape-language timing | §9 #5 |
| UP-06 | yes: few poses and chosen holds; secondary only where it adds value | §9 #6 |
| UP-07 | yes: one physics and one tell per attack class; the art bible's motion line | §9 #7 |
| UP-08 | yes: the timing grammar and the marker contract are the animator's core | §9 #8 |
| UP-09 | yes: pushed signature moments on a believable base; Roblox routes for squash and stretch | §9 #9 |
| UP-10 | yes: feel words and subtext drive the motion | §9 #10 |
| UP-11 | yes: variants keep tells, timing, anchors and secondary motion | §9 #11 |
| UP-12 | yes: no twinning, copies out of step, meaning locked | §9 #12 |
| UP-13 | yes: windows, markers, camera, rate, rig limits before keys | §9 #13 |
| UP-14 | yes: beat sheet, references, key-pose options, timing takes | §9 #14 |
| UP-15 | yes: blocking check-in before spline; re-key, do not patch | §9 #15 |
| UP-16 | yes: one named problem per pass; curves; honest weakness | §9 #16 |
| UP-17 | yes: markers, blendable clips, in-place locomotion, exact rig notes | §9 #17 |
| UP-18 | yes: stop criteria and pass budget; face and hair last; pops logged | §9 #18 |
| UP-19 | yes: attempt vs confirmed outcome; paid reveals share one windup | §9 #19 |
| UP-20 | yes: tells in pose and silhouette; reduced-motion path keeps the pose; pulse rate cap | §9 #20 |

## c. Old book changes (old = git revision df13ff4)

| Old text (file:line at df13ff4) | Kept / sharpened / replaced by / moved / removed | Why |
| --- | --- | --- |
| animation-design/SKILL.md:6 (header: evidence keys AP:/A:/R: lines) | replaced by a header that points to `knowledge/reference/animation/` and the craft library | J018 body rule: no citations or transcript lines in the body; evidence stays reachable from the header |
| animation-design/SKILL.md:13 governing idea (AP:9, AP:21) | sharpened (§1: three jobs in order + governing idea + big before small) | the three jobs give the order of judgement (clarity, belief, personality) |
| animation-design/SKILL.md:15 'There is no single recipe ... UNKNOWN, never a default' | kept; sharpened (method open, result judged; starting values are PROPOSALs) | library demo numbers enter only as PROPOSAL starting values |
| animation-design/SKILL.md:31-38 §3 steps 1-8 | replaced by §3 steps 1-10 (who reacts, rate, anchors and hook shapes, act it out, thumbnail key poses, sync rule) | new plan stages; old steps kept inside the new ones (1→1, 2→2, 3→3, 4→4, 5→7, 6→8, 7→9, 8→10) |
| animation-design/SKILL.md:43-60 §4 table 'Evidence' column | removed (column); every row kept and sharpened; P-17 and P-18 added | J018 body rule; the evidence lives in the reference notes |
| animation-design/SKILL.md:51 P-07 'iconic shape beats physical correctness' | sharpened (§4 P-07: one line of action, signature shape at held moments) | silhouette at the game camera made checkable with black-fill |
| animation-design/SKILL.md:56 P-12 'Exaggerate the read, not every amplitude' | sharpened as 'Push the read on a believable base' (§4 P-12, principles §10) | names the one or two signature moments and the believable base around them |
| animation-design/SKILL.md:72 'Visual motion is never physics or gameplay authority' | kept; extended (§5: the picture still tells the truth about reach and danger) | a pose implying more reach than the hit area misleads |
| animation-design/SKILL.md:87-93 §7 rules | kept; added rules on breakdowns, reads in pose not effects, confirmed outcome, paid reveals, new scope | library rules that guard fairness and quality |
| animation-design/SKILL.md:96-101 §8 self-check | sharpened (§8: who reacts, anchors, beat sheet, key-pose pick, tell sizing, sync rule) | covers the new plan stages |
| animation-design/references/principles.md:1-96 Source column and inline A:/R:/AP: refs | removed (column and refs); all rows kept | J018 body rule; evidence in the header pointers |
| animation-design/references/principles.md:36 P-03.7 'Squash and stretch ... only where the rig and asset contract allow it' | replaced by P-03.7 + SKILL §5 Roblox route (no scale in clips) | a keyframe pose stores only a CFrame: squash needs another route |
| animation-design/references/principles.md:37 P-03.8 wind-up as information | sharpened (anticipation sized by who reacts) | enemy tells vs the player's own tight anticipation |
| animation-design/references/principles.md:85 P-08.6 owner quote D-284 | quote removed; principle kept | body carries no citations |
| animation-design/references/principles.md:95-96 P-09.6, P-09.7 owner quotes | quotes removed; principles kept | body carries no citations |
| animation-design/references/review.md:1-62 inline AP:/A: refs | removed; content kept | J018 body rule |
| animation-design/references/review.md:12-29 §2 R-01..R-15 | kept; R-11 sharpened (tells fit the window, reach truth); R-16, R-17 added | silhouette and every-player reads become pass/fail rows |
| animation-design/references/review.md:52-56 §5 light checks | sharpened (black-fill from the same render pass, could-not-check list, what each input proves) | silhouette checks stay inside the owner's light-check budget (J005-D8) |
| animation-design/references/game-timing.md:5-13 §1 table | kept; rows added (reaction window, hit-stop length, camera shake) | who owns the new timing values |
| animation-design/references/game-timing.md:19 'Anticipation is information ... not automatically input delay' | sharpened (§2 anticipation sized by who reacts) | player's own move vs enemy tell |
| animation-design/references/game-timing.md:40-42 §5 'No general hit-stop ... value exists: it is a proposal per game' | sharpened (§5: still a game value; PROPOSAL starting values and bracketing; freeze frame supplied by the animator) | the library and vfx-design give start values; the rule that it is a game value stays |
| animation-design/references/worked-examples.md:7-15 §1 (a named Riot champion demo) | replaced by §1 a Roblox brawler emote with beat sheet, options and pick | no Riot names in the body; shows the new plan stages |
| animation-design/references/worked-examples.md:68-74 §8 table | kept; egg / paid crate row added; title now includes egg reveal | paid random reveals need one windup |
| animation-design/references/body-and-species.md:15 shoulders row ('the eyebrows of the body' [E] A:394-410) | sharpened (standard R15 has no collarbone joints: upper torso and upper arm) | verified Roblox joint fact |
| animation-design/references/body-and-species.md:18 hands row | sharpened (fingers only on advanced R15; hand-pose changes or mesh swap) | verified Roblox joint fact |
| animation-design/references/body-and-species.md:52 act it out with weighted sticks | replaced by a written beat sheet + made reference (Blender mannequin, test pose, pose image) | agents cannot film themselves |
| animation-design/references/sets-and-states.md:9 state machine bullet | sharpened (plan before keying; clips made to blend) | transitions are what players see most |
| animation-craft/SKILL.md:6 header | kept; J018 phrase and docs paths for new facts added | header rule |
| animation-craft/SKILL.md:28 step 4 'stepped (CONSTANT) keys or copied-pair holds, as you prefer' | replaced (§3 step 4: holds as copied pairs; CONSTANT only for quick pose review; root pass then pose pass; check-in) | stepped keys hide the in-between timing |
| animation-craft/SKILL.md:29 step 5 'Breakdowns, spline, polish' (one step) | replaced by steps 5 (breakdowns and offsets), 6 (spline), 7 (polish, one named problem per pass) | separate passes with their own self-review lines |
| animation-craft/SKILL.md:33 step 9 'Play on the intended Animator' | sharpened (step 11: also capture at the game camera, effects hidden, grayscale, §8c lines) | in-game judgement made part of the build |
| animation-craft/SKILL.md:44-59 C-03, C-08, C-09, C-11, C-13, C-14 AP:/[O] refs | paper-line refs removed; engine fact ids kept | J018 body rule; engine facts keep their verification ids |
| animation-craft/SKILL.md:87-94 §8 self-check | sharpened (check-in, §8a-c lines, captures with effects hidden, could-not-check list, freeze frame and sync rule) | matches the new passes |
| animation-craft/references/blender-keying.md:21 'Stepped blocking ... both show real holds' (03 TS11) | replaced (holds as copied key pairs; CONSTANT only for pose review) | copied pairs keep the real timing visible |
| animation-craft/references/blender-keying.md:24 '(a Maya habit, 03 TS12)' | ref removed; content kept | no Riot note refs in the body |
| animation-craft/references/ambient-at-scale.md:20 '(03 §6, RE:109-110 ...)' | ref removed; content kept | no Riot note refs in the body |
| animation-craft/references/ambient-at-scale.md:22 'Keep it calm' | sharpened (slower than sightline motion, decorative-only variation, sway follows gesture) | ambient motion must not compete with play |
| roles/animator.md:33 'Craft practice from Riot's artists ... riot-extracts.md §4' | removed | job card: role files point to their own books, not to the J016 card; the craft now lives in the books |
| roles/animator.md:35-43 Work method steps 1-8 | replaced by steps 1-11 (act it out and pick poses, time it, block then check in, passes, judge in game) | the new stage order |
| roles/animator.md:45-49 Working with other agents | kept; partner table 'what you ask for, and when' added | owner spec: what it asks partners for and when |
| roles/animator.md:55 Hand-back list | kept; beat sheets, key-pose pick, self-review lines, could-not-check list, one named weakness added | evidence for the new stages |
| animation-design/references/principles.md:74 P-07.5 'gaze can lead a turn ... eyes arrive first; face does not fight posture' | removed in stage 2 by mistake; restored in repair round 1 and split: look-turns (eyes, then head, then body; the face never fights the posture) vs spins and fast body turns (head holds its world direction, then turns late and fast); same split in body-and-species §2 neck row and §4, review S-15 | the stage 2 text applied the spin rule to every turn, which is wrong for an ordinary look-turn |
| animation-design/references/principles.md P-08.6 'Judge motion in motion ... review uses playback' | kept; sharpened (repair 1): timing from sample numbers and frame strips, feel at normal speed on a playable preview by the reviewer or owner | the agent sees stills only |
| animation-design/references/body-and-species.md:40 'Blinks have a reason: people blink when the head turns fast' | kept (§4 'eyes close ... on a fast head turn') | |
| animation-design/SKILL.md §4 'Sign in the clip' column (stage 2 / repair 1 text) | moved (repair round 2): the column is removed from SKILL §4; every sign sits in `principles.md` (P-01.1-P-10.5) and the checks in `review.md` §8; the §4 heading points to both | compaction: §8 of the SKILL must sit inside the part kept after compaction (review round 2 R3) |
| animation-design/SKILL.md §3 step 5 reference order and how to make a missing reference | moved (repair round 2) to a pointer to `body-and-species.md` §6, which holds the same text | duplication between SKILL and reference; compaction |

Citation policy (repair round 1): bodies carry no craft citations. Evidence ids that verify an engine, pipeline or tool fact stay where they sit (RA, RR, RB, KB, TC, SD and the paper's engine-section AP lines in the craft references and the C-rows). Paper lines that backed a craft opinion were removed: the design references in stage 2, `animation-craft/references/ambient-at-scale.md` (AP:432, AP:460) in repair round 1.

Nothing else was removed: every old rule, step, principle row, review row, failure row, worked example and engine fact is still in the books (some reworded). The one loss found by the stage 3 review (P-07.5 look-turn rule) is restored above.

## Repair round 1 (review `reviews/animator-rev1-reviewer.md`, 2026-10-22)

All three blocking findings and all six recommendations fixed; none declined. Keep list untouched (the plan stages, passes, compute table, attempt vs outcome, every-player rules, C-22..C-27, variants, worked example §1, §9 all 20 rows, proposals).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (SD-04, SD-22 landed as keywords) | `animation-design/references/game-timing.md` §4: two new bullets (an ability moves like its mechanic verb, the same verb as the VFX frame script and sound cue card; a state with a timer or breaking point gets a building end-of-state tell as a named timing-list event). Check: `review.md` §8a B-16 (new, appended). Steps: SKILL §3 step 5 (verb in the beat sheet), step 8 (verb, end-of-state tells); SKILL §6 creatures row; §9 #8 check. Role file work method step 4 and the "Contract" hand-back line. Coverage rows SD-04, SD-22 corrected |
| F2 (look-turn face rule lost; head-lag sign too broad) | `principles.md` P-07.5 rewritten: look-turn order (eyes, head, body; the face never fights the posture) restored and the spin case qualified; sign column split. `body-and-species.md` §2 neck and head row and §4 same split. `review.md` S-15 split into look-turn and spin. Coverage section c row added; CD-24 row updated |
| F3 (image budget of the new plan stages) | `review.md` §5 new bullet: plan-stage images are making, with their own budget (one black-fill contact sheet per key clip; takes, pre-push frames and brackets judged by numbers first and rendered only where they decide; playable previews are for the reviewer or owner); counts reported. SKILL §3 step 6 (one contact sheet per clip), §7 rule, §8 last line; §9 #6 check made number-first (cause named on the clip card, S-16; render only when the read is in doubt), §9 #9 (B-11 against the pre-push frame), §9 #10 (B-14 on existing renders). `review.md` B-11, B-12, B-14 rewritten to fit; `principles.md` P-08.11 numbers first; `game-timing.md` §5 bracket moved to its owners. Craft: `blender-keying.md` §7 contact-sheet bullet; craft SKILL §7 light-check rule; role file steps 3 and 11 |
| F4 ("fresh viewer" / "tester" with no method; mirror missing) | `review.md` §8 intro: definition of a fresh read (write the read before opening the brief, clip name or notes; the reviewer repeats it blind at the check-in) and a mirrored second look. `principles.md` "How to use" points every "fresh viewer" sign to it; P-06.10 "tester" replaced. SKILL §9 #16 check adds the fresh read and the mirrored look |
| F5 (timing picks from stills; bracket outside the decision right) | `review.md` §1 item 5: you see stills; timing from sample numbers and frame strips at a known rate; takes and feel go to the reviewer or owner as a playable preview. `blender-keying.md` §7: how to render the playable preview (Workbench, `image_settings.media_type = 'VIDEO'`, checked in the Blender API docs). `game-timing.md` §5: the gameplay owner and VFX bracket the hit-stop; the animator supplies freeze-frame takes. SKILL §3 steps 6 and 10; `principles.md` P-04.1 (beat gaps in frames instead of tapping along), P-08.6; `review.md` G-11 (pile-up from the Output log; "tires" is the reviewer's or owner's call). Role file step 3 |
| F6 (SKILL.md doubled; §8 and §9 lost after compaction) | `animation-design/SKILL.md` cut from 30,481 to about 25,800 characters without renumbering: §4 sign column shortened (full signs stay in `principles.md`), §5, §6, §7 tightened, §9 rows cut to principle, short example, check, where. §8 now ends at about 19,150 characters (about 4,800 tokens at the reviewer's 4 chars/token), inside the 5,000 kept after compaction. Details moved, not dropped: underside study and measured lengths to `body-and-species.md` §1; "a tween is quick to author, not proven cheaper" to craft SKILL §6 |
| F7 (check-in rule with no named reviewer) | `animation-craft/SKILL.md` §3 step 4: with no named reviewer, the check-in is the §8a record plus black-fills and root-only preview in the job folder, said in the hand-back; §7 rule points to it; role file step 7 |
| F8 (sync window differs from sound-design S-133) | `game-timing.md` §4 sync rule: sound-design's window is wider; until aligned (proposal), the sound-designer's book governs the sound side and the offset is MEASURED. `review.md` G-04 reports MEASURED until then. Proposal row kept |
| F9 (tables and headers) | (a) CD-21 reason moved to the rejected column; (b) SD-04 now matches the book (F1); (c) SKILL §4 heading no longer promises a mistakes column; (d) `roblox-playback.md` §10 defines the phone viewport (capture resampled to the floor phone's screen size, Pillow resize or `look_check.py thumb --size` with `--box`); (e) one citation policy, written above in section c: engine, pipeline and tool fact ids stay, craft-opinion paper lines removed (`ambient-at-scale.md` AP:432, AP:460). Line endings normalized to LF (`.gitattributes` eol=lf) |

## Repair round 2 (review `reviews/animator-rev2-reviewer.md`, 2026-10-22)

The blocking finding and all seven recommendations fixed; none declined. Keep list untouched (plan stages, passes, plan-stage image budget, fresh-read definition, playable preview and "you see stills", hit-stop bracket with its owners, the round 1 repairs, §9 with all 20 rows).

| Review finding id | Fixed where / declined: why |
| --- | --- |
| F1 (CD-25 landed as a keyword) | `principles.md` §6 new row P-06.11: a promo, thumbnail, splash or cutscene still starts from a one-sentence premise and reuses the signature key pose from the set; sign: black-fill at the game camera compared with the clip's key frame (`look_check.py silhouette --compare`, MEASURED) or the difference recorded; a fresh read names the premise. P-04.4 points to it. Self-review: `review.md` §8a B-17 (appended). Hand-off: `game-timing.md` §6 new row (marketing, film-director). Example: `worked-examples.md` §1 promo still bullet. Craft: `blender-keying.md` §7 promo still bullet (set the clip's key frame, never re-pose). SKILL §6 characters row; role file partner table (marketing row). Proposal row for `marketing-craft` and `film-craft` (they ask the animator for the pose). Coverage row CD-25 corrected |
| R1 (worked emote used the spin rule on a look-turn) | `worked-examples.md` §1 Drivers: in the glance the eyes reach the camera first, then the head, then the chest; the head holds its world direction only if the hop turns the body. Secondary: a blink on the fast head turn |
| R2 (no one can watch a timing preview during the job) | `review.md` §1 item 5: an agent reviewer judges takes by the same beat-gap numbers and strips; until the owner watches the previews at the next gate, the take with the better recorded reasons is used, marked PROPOSAL, and both previews go into the gate packet. Same wording carried to SKILL §3 steps 6 and 10, `review.md` §5 and B-12, G-11, `principles.md` "How to use" and P-08.6, `blender-keying.md` §7 playable preview, role file work method step 3 |
| R3 (§8 at the compaction edge; §9 past it) | SKILL §1 new line: after a compaction, re-read §8 and §9 before handing on a plan. SKILL trimmed without renumbering: §4 'Sign' column removed (signs in `principles.md`, checks in `review.md` §8), §5 and §6 cells tightened, step 5 reference detail replaced by its pointer, header shortened. §8 now ends at about 17,950 characters (was 19,152 after round 1 plus this round's additions), about 4,850 tokens at 3.7 characters per token |
| R4 (`thumb --box` does not re-measure silhouette) | `roblox-playback.md` §10: `--box` re-measures value against the surroundings only; silhouette numbers come from the black-fill renders or a `--mask` drawn from the effects-hidden capture. This also corrects the repair round 1 F9(d) wording above |
| R5 (G-11, G-14 hooks have no supplier) | Role file partner table, feature-builder row: in the test place a hit-reject hook, a rate trigger for frequent clips that logs the playing-track count, and a debug overlay of the hit area. `review.md` G-11 and G-14 now name the builder's rate trigger and debug overlay |
| R6 (eval A6 would count plan-stage images against the cap) | `proposals/animator.md` evals row: A6 counts plan-stage images (one contact sheet per key clip, previews) separately, as `review.md` §5 says |
| R7 (RI-15 rejection reason unsound) | RI-15 now landed: `body-and-species.md` §6 new bullet (a new motion style: structural study of 2-3 successful clips in numbers, then changed toward our feel words and anchors; never copy a clip). Header count of rejections corrected to 2 |
