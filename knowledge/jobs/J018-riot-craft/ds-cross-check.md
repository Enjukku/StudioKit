---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J018 stage 1c"
supersedes: []
---
> Author: J018 cross-checker · claude-opus-5-5 · high · 2026-10-21

# J018 stage 1c: DestructionSimulator skills vs the Riot craft library

Owner instruction (J018-D2 point 3): compare the library with the 2026-10-15 DestructionSimulator (DS) skills built from the same transcripts and add anything they got right that the library lacks.

**Inputs read in full:** DS `.agents/skills/` art-fundamentals (SKILL.md, references/expert-workflows.md), animation (same), level-design (same), gui-ui (SKILL.md, references/ui-effects.md), vfx-design (SKILL.md, references/ camera-and-screen, effect-card-and-presets, elements, juice-repetition-sync, moment-recipes, review, scene-and-clutter, evidence/README.md, evals/briefs.md). Library: `knowledge/reference/craft/riot/` (README index, universal-principles.md, all topic findings opened where a DS item mapped to them). Transcript tracing through `extracts/` where a DS item claimed Riot origin. Roblox claims re-checked in `knowledge/external/roblox-creator-docs/`.

**What DS is:** art-fundamentals, animation, level-design and the gui-ui flow section paraphrase the same Riot series (mostly R00a-R00d); the library already covers almost all of it, usually with stronger, tool-backed checks. vfx-design (and gui-ui's ui-effects) come mostly from DS's own research base (studies, standards, studio practice, R-ids in DS `knowledge/reference/vfx/`, not re-read here); that is where the real gaps were: per-viewer effects, the true danger area, camera punches, hit-stop, comfort and flash safety, repetition, randomness that keeps meaning, pulse rates, outcome-tied feedback, honest paid reveals, UI timing, truthful counters, review inputs.

**Paths** in the table are relative to `DestructionSimulator/.agents/skills/` (sibling of the StudioKit folder); library findings cite them as `DS:<skill>/<file>:<line>`.

**How judged:** one row per DS rule, check, number, step or example (table rows count as items; the four genre-preset rows combine both preset tables; the seven reveal-tier rows are one item). "Got right" = sound craft for any Roblox game made by this studio, consistent with the transcripts and the docs. Verdicts: covered (pre-existing IDs; "(new)" marks an ID added in this stage that also covers it) · library-stronger · adds (a new finding was needed) · sharpens (a "(DS)" line added to an existing finding) · rejected, with a reason code: DS-only (one game, its paths, owner decisions or house style), scope (engine or code detail that belongs to a kit engineering or craft skill, not this library), weak (untested or second-hand evidence, or not checkable with kit tools), unsupported, or DS open item / no content.

## Totals

| DS file | items | covered | library-stronger | adds | sharpens | rejected |
| --- | --- | --- | --- | --- | --- | --- |
| art-fundamentals (SKILL.md, references/expert-workflows.md) | 49 | 41 | 2 | 0 | 1 | 5 |
| animation (SKILL.md, references/expert-workflows.md) | 43 | 36 | 1 | 0 | 2 | 4 |
| level-design (SKILL.md, references/expert-workflows.md) | 48 | 31 | 0 | 9 | 5 | 3 |
| gui-ui/SKILL.md | 25 | 6 | 0 | 2 | 5 | 12 |
| gui-ui/references/ui-effects.md | 18 | 3 | 0 | 11 | 1 | 3 |
| vfx-design/SKILL.md | 43 | 11 | 0 | 16 | 8 | 8 |
| vfx-design/references/camera-and-screen.md | 73 | 11 | 0 | 49 | 7 | 6 |
| vfx-design/references/elements.md | 109 | 46 | 0 | 22 | 30 | 11 |
| vfx-design/references/effect-card-and-presets.md | 46 | 12 | 0 | 16 | 5 | 13 |
| vfx-design/references/juice-repetition-sync.md | 86 | 17 | 0 | 50 | 11 | 8 |
| vfx-design/references/moment-recipes.md | 107 | 26 | 0 | 55 | 14 | 12 |
| vfx-design/references/review.md | 122 | 32 | 0 | 45 | 38 | 7 |
| vfx-design/references/scene-and-clutter.md | 104 | 43 | 0 | 35 | 19 | 7 |
| vfx-design/evidence/README.md | 4 | 1 | 0 | 0 | 0 | 3 |
| vfx-design/evals/briefs.md | 52 | 9 | 0 | 25 | 12 | 6 |
| **all** | **929** | **325** | **3** | **335** | **158** | **108** |

## What changed in the library

| Change | IDs |
| --- | --- |
| New findings (16) | VR-19 per-viewer effects · VR-20 drawn danger area = real hit area · VR-21 camera and screen punches · VR-22 hit-stop · VR-23 off paths that keep information · VR-24 frequent effects merged and capped · VR-25 randomise decoration only · VR-26 pulse rates · GD-34 feedback follows the confirmed outcome · GD-35 honest paid random reveals · UI-17 motion-table durations · UI-18 errors say the fix · UI-19 truthful counters · WL-29 routes in seconds, ledges vs jump height · WL-30 scored ten-check level review · CR-17 what each input can prove |
| New principles (2) | UP-19 Feedback follows the real outcome · UP-20 Every player can read it (never one channel; every intense channel can be reduced) |
| (DS) lines in existing findings (32) | WT-01, WT-02, WT-11 · EX-06 · VR-01 (2), VR-03, VR-04, VR-05, VR-06, VR-07, VR-08 (2), VR-09 (2), VR-11, VR-13 · CC-02 · VH-02 · VC-02, VC-04, VC-06, VC-07 · LC-01, LC-19 · UI-03, UI-05, UI-10 · WL-23 · GD-11 · CF-13 · CR-04 |
| Rests-on lists extended | UP-01 (+VR-19, VR-20), UP-02 (+VR-24, CR-17), UP-03 (+VR-19), UP-06 (+VR-24), UP-07 (+VR-25, VR-26), UP-08 (+VR-22, UI-17), UP-12 (+VR-25), UP-16 (+CR-17, WL-30), UP-17 (+VR-20) |
| README | DS row in the source table, topic counts, index rows, stage 1c note |

Numbers DS tagged [P] (untested start values) are kept as [inference] with "DS start values"; study results are cited "per DS" (second-hand, not re-read). Roblox facts newly verified in the mirror: StarterPlayer WalkSpeed 16 and JumpHeight 7.2 (`_api-reference/classes/StarterPlayer.yaml:243-249, 358-364`), GuiService.ReducedMotionEnabled and the docs' tween-time-0 pattern (`GuiService.yaml:262-268`; `production/publishing/accessibility.md:186-188`), LocalTransparencyModifier local-only on ParticleEmitter, Beam, Trail (`ParticleEmitter.yaml:502-511`; `Beam.yaml:325-335`; `Trail.yaml:278-291`), FieldOfView clamp 1-120 (`Camera.yaml:268-270`), AdjustSpeed(0) pauses (`AnimationTrack.yaml:320-324`), TimeScale 0 freezes (`ParticleEmitter.yaml:962-968`), FlipbookStartRandom (`ParticleEmitter.yaml:396-401`), ColorCorrectionEffect parenting and Saturation -1 (`ColorCorrectionEffect.yaml:24-26, 78-84`), BlurEffect.Size (`BlurEffect.yaml:31-36`), BloomEffect.Threshold (`BloomEffect.yaml:75-80`), NumberSequence linear interpolation (`_api-reference/datatypes/NumberSequenceKeypoint.yaml:96, 109`), Brightness only with LightInfluence 0 (`effects/particle-emitters.md:466-467`), mobile reserved control zones (`ui/position-and-size.md:131-139`), PolicyService ArePaidRandomItemsRestricted (`PolicyService.yaml:91`; `production/monetization/index.md:156-161`), Camera:WorldToViewportPoint ignores the GUI inset (`Camera.yaml:1308-1312`).

## Cross-check table

### art-fundamentals (SKILL.md, references/expert-workflows.md) (49 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 1 | art-fundamentals/SKILL.md:10 | Base skill; specialist skill wins in its medium | rejected | - | DS-only: DS skill-precedence rule; StudioKit sets precedence in AGENTS.md §0 |
| 2 | art-fundamentals/SKILL.md:16 | Clarity job: read in under a second where to go, threat, own, breakable, own state | covered | GD-01, UP-01, VH-07 | Same three jobs and the one-second read |
| 3 | art-fundamentals/SKILL.md:16 | Clarity fails when two things look alike but act differently | covered | UP-07, GD-13 | One code for meaning; consistent behaviour |
| 4 | art-fundamentals/SKILL.md:17 | Satisfaction: instant answer, good on success, bad on failure; change in the same frame | covered | GD-02, UI-12 | Library adds frame-count checks |
| 5 | art-fundamentals/SKILL.md:18 | Style: one look sets the emotion; tone must not contradict play | covered | GD-01, SI-01, GD-07 | - |
| 6 | art-fundamentals/SKILL.md:20 | Style is a tool for emotion (colour, proportion, realism) | covered | SI-01 | - |
| 7 | art-fundamentals/SKILL.md:24 | Most important information easiest to see; every tool is contrast | covered | VH-01, VC-01 | - |
| 8 | art-fundamentals/SKILL.md:26 | Rank items for the moment; only top 1-2 get high contrast | covered | VH-09, UP-03 | - |
| 9 | art-fundamentals/SKILL.md:27 | Lower everything else's contrast (checkerboard) | covered | VC-04 | - |
| 10 | art-fundamentals/SKILL.md:28 | Contrast channels ranked strongest first: value, saturation, hue, shape, size... | rejected | VC-01 | Unsupported order: transcripts list channels without a ranking; DS's own vfx evidence marks value-first order unresolved (SC:69, X-30) |
| 11 | art-fundamentals/SKILL.md:28 | More than one channel for critical items (colour blindness, bright sun on phones) | covered | LC-01, UP-20 (new) | LC-01 pairs reserved colour with shape; UP-20 states it as a principle |
| 12 | art-fundamentals/SKILL.md:29 | Detail is a contrast channel; calm vs busy areas | covered | VH-05 | - |
| 13 | art-fundamentals/SKILL.md:30 | Distance reads simpler (atmospheric perspective) | covered | WL-25 | - |
| 14 | art-fundamentals/SKILL.md:31 | Light is a pointer; a bright focal point can distract from a surprise | covered | LC-12, CF-13 | - |
| 15 | art-fundamentals/SKILL.md:32 | Shapes point; spiky danger, round safe, square stable | covered | SS-05, SS-08, CF-08 | - |
| 16 | art-fundamentals/SKILL.md:33 | If everything is loud nothing is; save the biggest for the biggest moment | covered | VH-02 | - |
| 17 | art-fundamentals/SKILL.md:35 | Squint test at about 25 %, then grayscale | library-stronger | VH-09, WL-28, VC-02 | Library checks run look_check.py and thumb views |
| 18 | art-fundamentals/SKILL.md:39 | 2-3 iconic elements; simplify to them when small | covered | SS-04, CD-04 | - |
| 19 | art-fundamentals/SKILL.md:40 | Black silhouette at the real camera distance; no shared silhouettes | covered | SS-02, VH-07 | - |
| 20 | art-fundamentals/SKILL.md:41 | Size ranks importance | covered | VH-10 | - |
| 21 | art-fundamentals/SKILL.md:42 | Start every model as a proxy; check in game before detail | covered | PI-04 | - |
| 22 | art-fundamentals/SKILL.md:43 | Neutral pose may fail in motion; test extreme poses | covered | CD-12, PP-18 | - |
| 23 | art-fundamentals/SKILL.md:47 | Scale cues are touch points; build next to a player-sized reference | library-stronger | WL-21 | WL-21 adds stud measurements per prop |
| 24 | art-fundamentals/SKILL.md:48 | Story in the space; wear where hands and feet go; dirt in low corners | covered | WL-22, MD-09 | - |
| 25 | art-fundamentals/SKILL.md:49 | Modular kits that look new when rotated or recoloured | covered | PP-24 | - |
| 26 | art-fundamentals/SKILL.md:50 | Art and rules agree (soft must not stop a truck) | covered | GD-07, WL-18 | - |
| 27 | art-fundamentals/SKILL.md:58 | Colour meaning consistent across world, VFX, UI, icons | covered | UP-07, LC-02, UI-06 | - |
| 28 | art-fundamentals/SKILL.md:59 | Shape meaning consistent (plus heal, circle shield, spikes damage, arrow go) | covered | VR-05, SS-06 | - |
| 29 | art-fundamentals/SKILL.md:60 | Motion personality consistent across animation, UI motion, VFX timing, camera | sharpens | WT-02 | Added a (DS) check comparing motion table, clip and effect timings |
| 30 | art-fundamentals/SKILL.md:61 | Sound personality and loudness ranking consistent | covered | VH-02, SD-21 | - |
| 31 | art-fundamentals/SKILL.md:62 | Material and age language consistent across structures, props, terrain, UI frames | covered | UP-11, SI-01 | - |
| 32 | art-fundamentals/SKILL.md:64 | Effect or sound tied to the source's colour or material tells who caused it | covered | LC-20, SD-23, WL-18 | - |
| 33 | art-fundamentals/SKILL.md:68 | Show work early and often; no grand reveals | covered | CR-07 | - |
| 34 | art-fundamentals/SKILL.md:69 | Ask goal questions, not taste questions | covered | CR-02 | - |
| 35 | art-fundamentals/SKILL.md:70 | Find the problem behind a proposed fix | covered | CR-03 | - |
| 36 | art-fundamentals/SKILL.md:71 | Broad to narrow; do not reopen a closed direction | covered | PI-03 | - |
| 37 | art-fundamentals/SKILL.md:72 | Present work as if you care: what it is for and why | covered | CR-14, RI-19 | - |
| 38 | art-fundamentals/SKILL.md:76 | Review 1: top items win squint and grayscale | covered | VH-09, VC-02 | - |
| 39 | art-fundamentals/SKILL.md:77 | Review 2: calm areas; detail where the eye should land | covered | VH-05 | - |
| 40 | art-fundamentals/SKILL.md:78 | Review 3: silhouette and traits at game distance on a phone | covered | SS-02, UP-02 | - |
| 41 | art-fundamentals/SKILL.md:79 | Review 4: player-sized reference; touch points at scale | covered | WL-21 | - |
| 42 | art-fundamentals/SKILL.md:80 | Review 5: story of use, age or place; wear at contact | covered | WL-22, MD-09 | - |
| 43 | art-fundamentals/SKILL.md:81 | Review 6: colour, shape, motion meanings match the game | covered | UP-07 | - |
| 44 | art-fundamentals/SKILL.md:82 | Review 7: looks match behaviour | covered | GD-07 | - |
| 45 | art-fundamentals/SKILL.md:83 | Review 8: nothing important signalled only by colour | covered | LC-01, UP-20 (new) | - |
| 46 | art-fundamentals/SKILL.md:87 | Style source: DS art bible and owner taste table | rejected | - | DS-only: project paths |
| 47 | art-fundamentals/SKILL.md:88 | DS 5-angle Studio review; art-director owns cohesion | rejected | - | DS-only: DS process |
| 48 | art-fundamentals/SKILL.md:89 | Breakability is clarity: what breaks, what is worth more, what is a boundary | covered | WL-03, WL-18 | Generalised as "what you can do here" |
| 49 | art-fundamentals/references/expert-workflows.md:5 | Expert-workflows ledger (empty table) | rejected | - | No content |

### animation (SKILL.md, references/expert-workflows.md) (43 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 50 | animation/SKILL.md:12 | Three jobs: show the action, believable weight, personality | covered | GD-01 | - |
| 51 | animation/SKILL.md:14 | Each action readable at game distance; attacks have a clear windup | covered | WT-01, GD-21 | - |
| 52 | animation/SKILL.md:15 | Consistent physics; big things slower and land harder; motion sets tone | covered | WT-02, WT-03 | - |
| 53 | animation/SKILL.md:16 | Personality: how does this character do it | covered | CD-09 | - |
| 54 | animation/SKILL.md:20 | Act it out or use motion reference; key storytelling poses first (pose to pose) | covered | RI-24, RI-25, WT-04 | - |
| 55 | animation/SKILL.md:21 | Expect 3-5 tries; drop a precious idea | covered | PI-09 | Same source (R00b:2255-2277) |
| 56 | animation/SKILL.md:22 | Keep it simple: a clean bounce beats a sloppy flip | covered | CR-16 | Same source (R00b:3364-3390) |
| 57 | animation/SKILL.md:26 | Line of action | covered | SS-10 | - |
| 58 | animation/SKILL.md:27 | Balance: centre of gravity over the feet unless off balance on purpose | covered | WT-07 | - |
| 59 | animation/SKILL.md:28 | Heavy prop close to the centre of gravity with a wide low stance | covered | WT-08 | - |
| 60 | animation/SKILL.md:29 | 2-3 personality adjectives pushed into the pose, then check | covered | EX-02 | - |
| 61 | animation/SKILL.md:30 | Read the pose as a black silhouette | covered | SS-02, GD-21, SS-15 | - |
| 62 | animation/SKILL.md:34 | Spacing and easing; slow at the top of an arc | covered | WT-09, WT-10 | - |
| 63 | animation/SKILL.md:35 | Squash and stretch; keep the volume constant | sharpens | EX-06 | Added the volume rule as a (DS) apply line |
| 64 | animation/SKILL.md:36 | Anticipation, action, follow-through; loose parts settle | covered | WT-01, WT-24, WT-25 | - |
| 65 | animation/SKILL.md:37 | Timing sells mass: fast to peak = energy, slow start and hard stop = heavy | covered | WT-11, WT-23, WT-03 | - |
| 66 | animation/SKILL.md:38 | Practise variants of one move (heavy, light, happy, sad) | covered | CR-16 | - |
| 67 | animation/SKILL.md:42 | Design the animation set, not single clips | covered | PP-20 | - |
| 68 | animation/SKILL.md:44 | List states and transitions including interrupts | covered | PP-20 | - |
| 69 | animation/SKILL.md:45 | Blend locomotion by speed; layer upper body over lower body | covered | PP-20 | - |
| 70 | animation/SKILL.md:46 | Decide clip priority and fade time per transition | covered | PP-20 | PP-20 roblox_fit cites priorities and fadeTime in the docs |
| 71 | animation/SKILL.md:47 | Gameplay timing on animation events, not guessed delays | covered | CC-02 | - |
| 72 | animation/SKILL.md:48 | Design must allow the motion (collar blocking an arm); agree early with the modeller | covered | CD-12, CC-03 | - |
| 73 | animation/SKILL.md:54 | Animator:LoadAnimation and Play(fade, weight, speed) | covered | PP-20 | - |
| 74 | animation/SKILL.md:55 | AnimationTrack.Priority order Core to Action4 | library-stronger | PP-20 | Library cites the docs lines; enum names re-checked in AnimationPriority.yaml:38-77 |
| 75 | animation/SKILL.md:56 | Named markers and GetMarkerReachedSignal for sync | covered | CC-02 | - |
| 76 | animation/SKILL.md:57 | Animation Graph Editor for blend trees and state machines | covered | PP-20 | - |
| 77 | animation/SKILL.md:58 | IKControl for feet, aim and reach | covered | PP-19 | pipeline-production.md:269 notes runtime IKControl |
| 78 | animation/SKILL.md:59 | TweenService easing matching the motion personality for props and UI | covered | WT-09, EX-08 | - |
| 79 | animation/SKILL.md:60 | AnimationController with Animator for rigs without a Humanoid | rejected | - | Scope: engine API fact for the animation-craft and rigging skills, not a craft finding |
| 80 | animation/SKILL.md:64 | Animation card per clip (purpose, trigger, timings, easing, priority, markers, interrupts, adjectives, test) | covered | UP-13, PP-20, CC-02, EX-02 | Fields are spread over these findings; the card itself is a DS template |
| 81 | animation/SKILL.md:68 | Review 1: reads at game distance on a phone as a silhouette | covered | GD-21, UP-02 | - |
| 82 | animation/SKILL.md:69 | Review 2: anticipation before anything that threatens the player | covered | WT-01 | - |
| 83 | animation/SKILL.md:70 | Review 3: weight consistent with size and material | covered | WT-02, WT-03 | - |
| 84 | animation/SKILL.md:71 | Review 4: easing never linear by accident | covered | WT-09, WT-04 | - |
| 85 | animation/SKILL.md:72 | Review 5: the motion could not be swapped onto another character | covered | CD-09 | - |
| 86 | animation/SKILL.md:73 | Review 6: clean transitions and interrupts, no pops | covered | PP-20 | - |
| 87 | animation/SKILL.md:74 | Review 7: gameplay, sound and VFX fire on markers | covered | CC-02 | - |
| 88 | animation/SKILL.md:75 | Review 8: motion personality matches UI, VFX and camera | sharpens | WT-02 | Same (DS) line as AF:60 |
| 89 | animation/SKILL.md:79 | DS rig rules and film plans | rejected | - | DS-only: project paths |
| 90 | animation/SKILL.md:80 | Destruction motion is physics, judged by predictable cause and effect | rejected | WT-02 | DS-only paths; the principle is WT-02 |
| 91 | animation/SKILL.md:81 | UI motion follows gui-ui and the game's motion personality | covered | UI-16, WT-02 | - |
| 92 | animation/references/expert-workflows.md:5 | Expert-workflows ledger (empty table) | rejected | - | No content |

### level-design (SKILL.md, references/expert-workflows.md) (48 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 93 | level-design/SKILL.md:10 | Level serves the target experience, guides without words, believable; owner decides | covered | GD-04, WL-01, UP-13 | Owner decisions: AGENTS.md §0 |
| 94 | level-design/SKILL.md:18 | Job field: target experience (one type of fun) | covered | GD-04 | - |
| 95 | level-design/SKILL.md:19 | Job field: player goal and how progress shows | covered | GD-03, GD-10 | - |
| 96 | level-design/SKILL.md:20 | Job field: opposition or challenge | covered | GD-03, GD-12 | - |
| 97 | level-design/SKILL.md:21 | Job field: session shape (first visit, return visit, 5-minute phone session) | adds | WL-29 (new) | Library had no session-length constraint for levels |
| 98 | level-design/SKILL.md:22 | Job field: camera and device | covered | UP-13, UI-03 | - |
| 99 | level-design/SKILL.md:23 | Job field: theme and the 3-5 things players expect | covered | SI-05, SI-04 | - |
| 100 | level-design/SKILL.md:27 | Blockout first; walk it at player speed | covered | PI-04, PP-26 | - |
| 101 | level-design/SKILL.md:28 | Review the blockout; fix route and pacing now | covered | PI-04, WL-16, WL-30 (new) | - |
| 102 | level-design/SKILL.md:29 | Art roughs keep blockout constraints; boundary as wall, cliff or river | covered | GD-31, WL-04 | - |
| 103 | level-design/SKILL.md:30 | Detail, story, light and polish after the layout works | covered | PP-26 | - |
| 104 | level-design/SKILL.md:31 | Play-test, iterate; no reopening without new evidence | covered | PI-03, GD-15 | - |
| 105 | level-design/SKILL.md:35 | First view shows place, actions, next goal | covered | WL-07 | - |
| 106 | level-design/SKILL.md:36 | One big landmark per zone visible from anywhere; smaller at decision points; unique silhouettes | sharpens | WL-23 | Added a (DS) check: a landmark from every route fork, unique black-fill |
| 107 | level-design/SKILL.md:37 | Leading shapes point to the next goal; remove lines into dead ends | covered | CF-08, WL-13 | - |
| 108 | level-design/SKILL.md:38 | Light and colour as pointers; side areas calmer | covered | LC-12, LC-17 | - |
| 109 | level-design/SKILL.md:39 | Alternate calm and busy areas | covered | VH-05 | - |
| 110 | level-design/SKILL.md:40 | Reveal: hide the next big thing behind a turn or rise, then frame it | sharpens | CF-13 | Added a (DS) apply line for levels; bright-light distraction part already in CF-13 |
| 111 | level-design/SKILL.md:41 | Affordances look the same everywhere | covered | WL-03, UP-07 | - |
| 112 | level-design/SKILL.md:45 | Interest curve: easy near spawn, harder and richer further in, climax near the end | sharpens | GD-11 | Added a (DS) apply line laying the arc out in space |
| 113 | level-design/SKILL.md:46 | Player always sees how close the goal is | covered | GD-10 | - |
| 114 | level-design/SKILL.md:47 | Measure walk times at 16 studs/s; long empty walks are dead time | adds | WL-29 (new) | WalkSpeed verified in StarterPlayer.yaml:358-364 (GD-26 had it [unverified]) |
| 115 | level-design/SKILL.md:48 | Return trips short or interesting | adds | WL-29 (new) | - |
| 116 | level-design/SKILL.md:49 | A reward or new view at each natural pause | adds | WL-29 (new) | - |
| 117 | level-design/SKILL.md:53 | Boundaries look like the world, never invisible walls; look and act impassable | covered | WL-04, GD-07 | - |
| 118 | level-design/SKILL.md:54 | Scale cues at touch points; jump height 7.2 studs, a higher ledge is a wall | adds | WL-21, WL-29 (new) | Scale covered by WL-21; jump-height metric new (StarterPlayer.yaml:243-249) |
| 119 | level-design/SKILL.md:55 | Story in the space; lived-in is more fun to wreck | covered | WL-22 | - |
| 120 | level-design/SKILL.md:56 | Art and rules agree (doorway walkable, glass weak) | covered | GD-07, WL-18 | - |
| 121 | level-design/SKILL.md:58 | Review scored 0-2 per check, total out of 20 | adds | WL-30 (new) | Library had the checks scattered, not a fixed scored review |
| 122 | level-design/SKILL.md:62 | Check 1 Job | covered | GD-04, WL-30 (new) | - |
| 123 | level-design/SKILL.md:63 | Check 2 First view | covered | WL-07 | - |
| 124 | level-design/SKILL.md:64 | Check 3 Route found without text; no unexplained dead ends | covered | WL-09, WL-16 | - |
| 125 | level-design/SKILL.md:65 | Check 4 Landmarks per zone; decision points marked | sharpens | WL-23, WL-12 | See LD:36 |
| 126 | level-design/SKILL.md:66 | Check 5 Hierarchy: squint test, calm and busy alternate | covered | VH-05 | - |
| 127 | level-design/SKILL.md:67 | Check 6 Pacing: ramp, climax, no walk over about 15 s | adds | GD-11, WL-29 (new) | 15 s limit kept as [inference] |
| 128 | level-design/SKILL.md:68 | Check 7 Progress visible | covered | GD-10 | - |
| 129 | level-design/SKILL.md:69 | Check 8 Boundaries believable, on theme, impassable | covered | WL-04, GD-07 | - |
| 130 | level-design/SKILL.md:70 | Check 9 Scale of touch points | covered | WL-21 | - |
| 131 | level-design/SKILL.md:71 | Check 10 Story and theme expectations present | covered | SI-05, WL-22 | - |
| 132 | level-design/SKILL.md:75 | Output: ranked findings table with where, why, fix, cost | adds | WL-30 (new), PI-07 | - |
| 133 | level-design/SKILL.md:76 | Output: marked-up top-down image numbered to the table | covered | CR-05, WL-30 (new) | Paint-over on a capture |
| 134 | level-design/SKILL.md:77 | Output: a could-not-check list | adds | CR-17 (new) | - |
| 135 | level-design/SKILL.md:78 | Proposals labelled PROPOSAL; the owner decides | covered | README §4, AGENTS.md §0 | - |
| 136 | level-design/SKILL.md:82 | DS stage files and plans | rejected | - | DS-only: project paths |
| 137 | level-design/SKILL.md:83 | Owner taste: full terrain, buildings 1.5x scale, windows on every face | rejected | - | DS-only: one owner's taste for one game |
| 138 | level-design/SKILL.md:84 | Breakable targets ramp in value along the route; iconic structure is the climax | sharpens | GD-11 | Generalised into the GD-11 (DS) line |
| 139 | level-design/SKILL.md:85 | Studio walk tests through studio-operator; one driver | covered | AGENTS.md §3 | Kit rule (one driver per Studio) |
| 140 | level-design/references/expert-workflows.md:5 | Expert-workflows ledger (empty table) | rejected | - | No content |

### gui-ui/SKILL.md (25 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 141 | gui-ui/SKILL.md:3 | UI built with standard Instances, Charm, Networker, Janitor; no React | rejected | - | DS-only: DS stack |
| 142 | gui-ui/SKILL.md:8 | Guide, rules and template paths | rejected | - | DS-only: project paths |
| 143 | gui-ui/SKILL.md:12 | Every screen from an owner-approved Blender-rendered mockup (D-129) | rejected | - | DS-only owner decision; StudioKit routes UI through Figma style skills; "start from an approved reference" is AGENTS.md §3.5 |
| 144 | gui-ui/SKILL.md:13 | No raw Frame or TextButton visible; every surface a kit image | rejected | - | DS-only: one game's look |
| 145 | gui-ui/SKILL.md:14 | One hero element; rarity and context colours from the style guide | covered | UI-13, VH-09, UI-06 | - |
| 146 | gui-ui/SKILL.md:15 | Snap motion, press-sink, click sound, count-up numbers with abbreviation | adds | UI-12, UI-17 (new), UI-19 (new) | Press feedback covered; durations and truthful abbreviated counters new |
| 147 | gui-ui/SKILL.md:16 | Screenshots at 1920x1080, 800x360, 1024x768 beside the mockup | sharpens | UI-03 | Added the three sizes as a (DS) line [inference on sizes] |
| 148 | gui-ui/SKILL.md:20 | Player task: where am I, what can I do, what happened, what next | covered | UP-01, UI-02 | - |
| 149 | gui-ui/SKILL.md:21 | Layout order: header, main, details, one primary action, secondary, close | sharpens | UI-10 | Added as a (DS) apply line |
| 150 | gui-ui/SKILL.md:22 | Code authoring; controller owns behaviour | rejected | - | DS-only: DS code structure |
| 151 | gui-ui/SKILL.md:23 | State in locals and Charm atoms | rejected | - | DS-only: DS stack |
| 152 | gui-ui/SKILL.md:24 | Buttons use Activated and fire requests; UI updates from server-confirmed data | adds | GD-34 (new) | Confirmed-result rule new; DS request library is DS-only |
| 153 | gui-ui/SKILL.md:25 | States: idle, pressed, disabled with reason, loading, cooldown, error | sharpens | UI-05, UI-18 (new) | Button state list added to UI-05; disabled-with-reason in UI-18 |
| 154 | gui-ui/SKILL.md:26 | Touch: 44 px targets, 12 px gaps, primary bigger, nothing in thumbstick or jump zone, no hover-only | sharpens | UI-03 | Added; reserved zones verified in ui/position-and-size.md:131-139; 44 is practice, Roblox gives no number |
| 155 | gui-ui/SKILL.md:27 | Scaling: design canvas plus UIScale; edge HUD anchors; safe insets | rejected | UI-03 | Scope: UI engineering (kit ui-basics); safe area already in UI-03 |
| 156 | gui-ui/SKILL.md:28 | Cleanup in the Janitor | rejected | - | DS-only: DS library |
| 157 | gui-ui/SKILL.md:29 | Test three sizes; young kids on iPads, check 1024x768 first (D-115) | sharpens | UI-03 | Sizes added; the iPad-first audience is DS-only |
| 158 | gui-ui/SKILL.md:33 | UX first: map information and fewest steps per audience and device | covered | UI-01, UI-03 | - |
| 159 | gui-ui/SKILL.md:34 | UI on the flow; proximity; one rule set; polish cannot rescue flow | covered | UI-01, UI-06, UI-09 | - |
| 160 | gui-ui/SKILL.md:35 | Five motion goals; UI motion personality matches animation and VFX | covered | UI-12, UI-13, UI-14, UI-15, UI-16, WT-02 | Same Riot source (R00d); cross-craft match added as a WT-02 (DS) line |
| 161 | gui-ui/SKILL.md:39 | No React, Roact, Fusion, Vide | rejected | - | DS-only: stack choice |
| 162 | gui-ui/SKILL.md:40 | No LocalScripts scattered inside ScreenGuis | rejected | - | Scope: code architecture (kit architecture skill) |
| 163 | gui-ui/SKILL.md:41 | Buttons never grant items or currency client-side | covered | GD-34 (new) | Server-authoritative outcomes; detail in the kit networking-security skill |
| 164 | gui-ui/SKILL.md:42 | No UIScale inside an overflowing container as a fit fix | rejected | - | Scope: UI engineering (kit ui-basics) |
| 165 | gui-ui/SKILL.md:43 | Pool and update lists in place, never rebuild | rejected | - | Scope: performance engineering (kit performance, ui-basics) |

### gui-ui/references/ui-effects.md (18 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 166 | gui-ui/references/ui-effects.md:5 | World-to-HUD hand-overs on one shared beat list; VFX owns 3D, UI owns landing and counter | covered | CC-02, CC-06, UI-14 | - |
| 167 | gui-ui/references/ui-effects.md:10 | Button press: sink 50 ms, release 120-150 ms overshoot, accepted on press, same delay everywhere | adds | UI-17 (new) | Values [inference] (DS practice sources) |
| 168 | gui-ui/references/ui-effects.md:10 | Leave out: bounce delaying the next tap; over 100 ms before any change | adds | UI-17 (new) | In UI-17 mistake and check |
| 169 | gui-ui/references/ui-effects.md:11 | Purchase success only on server confirm; pending state if confirm over 100 ms | adds | GD-34 (new), UI-17 (new) | - |
| 170 | gui-ui/references/ui-effects.md:12 | Error: control shake, message stays 2 s, red + icon + text, shows the fix, rate-limited sound | adds | UI-18 (new) | - |
| 171 | gui-ui/references/ui-effects.md:13 | Toast timings, at most 3 stacked, outside the combat focus, no reward spectacle | adds | UI-17 (new) | - |
| 172 | gui-ui/references/ui-effects.md:14 | Currency change: +N pop, count-up 600 ms, true balance for affordability, signed labels | adds | UI-19 (new) | - |
| 173 | gui-ui/references/ui-effects.md:15 | Anchors: 100 ms instant; enter 225 / exit 195; 200-300 major; 500 drags | adds | UI-17 (new) | - |
| 174 | gui-ui/references/ui-effects.md:20 | Pop via UIScale tween with Back easing | covered | EX-08 | Overshoot; Back easing named in EX-08 roblox_fit |
| 175 | gui-ui/references/ui-effects.md:21 | Shine sweep with UIGradient offset | rejected | - | Scope: UI build recipe (kit ui-basics) |
| 176 | gui-ui/references/ui-effects.md:22 | Glow or outline pulse with UIStroke, at most 1 Hz for lasting states | covered | VR-26 (new) | Rate rule in VR-26; build detail is ui-basics |
| 177 | gui-ui/references/ui-effects.md:23 | Number roll via NumberValue; abbreviate; true balance | adds | UI-19 (new) | - |
| 178 | gui-ui/references/ui-effects.md:24 | Shake via Position offsets, never the whole screen | adds | UI-18 (new) | - |
| 179 | gui-ui/references/ui-effects.md:25 | Fly-to-HUD from Camera:WorldToViewportPoint; landing bumps the counter | adds | UI-19 (new), UI-14 | WorldToViewportPoint verified (Camera.yaml:1308-1312) |
| 180 | gui-ui/references/ui-effects.md:26 | Burst of bits via pooled ImageLabels or ViewportFrame; cap counts | rejected | - | Scope: UI build recipe (kit ui-basics); "no native UI particles" [unverified] |
| 181 | gui-ui/references/ui-effects.md:27 | UI flash at most 80 % white, 125 ms, counts toward flash safety | sharpens | VR-13 | Composite count includes UI flashes (VR-13 (DS) line) |
| 182 | gui-ui/references/ui-effects.md:28 | Reduced motion: tween time 0 or fade; keep all information | adds | VR-23 (new) | Verified in accessibility.md:186-188 |
| 183 | gui-ui/references/ui-effects.md:29 | Tweens and pooled instances in a Janitor | rejected | - | DS-only: DS library |

### vfx-design/SKILL.md (43 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 184 | vfx-design/SKILL.md:11 | Design skill answers what and why; target picture is a written frame script | covered | WT-13, RH-03 | Timeline in data with stage times |
| 185 | vfx-design/SKILL.md:11 | No 2D mock-ups (D-284) | rejected | - | DS-only owner decision; StudioKit starts visual work from reference images (AGENTS.md §3.5) |
| 186 | vfx-design/SKILL.md:13 | Order: plan, build, check, capture, owner's final look | covered | UP-13, UP-15 | - |
| 187 | vfx-design/SKILL.md:14 | Who reads which skill | rejected | - | DS-only: skill routing |
| 188 | vfx-design/SKILL.md:17 | Frame the job: what, does, how big; importance 1-10 per viewer; rate; device mix | adds | VR-01, VR-19 (new) | Three answers covered by VR-01; per-viewer rating new |
| 189 | vfx-design/SKILL.md:17 | Read gameplay truth (area, speed, fuse, radius) from config; never set or invent it | adds | VR-20 (new) | - |
| 190 | vfx-design/SKILL.md:18 | Pick context and technique; name joining crafts; one shared beat list | sharpens | VR-01, CC-02 | Chooser added as a VR-01 (DS) line |
| 191 | vfx-design/SKILL.md:19 | Open 1-3 pro frame scripts of the same type; note peak, timing, tail, layers | covered | RI-05, RI-10, UP-14 | DS library path is DS-only |
| 192 | vfx-design/SKILL.md:20 | Our frame script at the game camera: 6-10 moments in ms with screen %; compare and fix the plan | covered | WT-13, VR-06, RH-03 | - |
| 193 | vfx-design/SKILL.md:24 | Context table: gameplay moment, world event, object change, cutscene, UI set budget and freedom | sharpens | VR-01 | In the VR-01 (DS) chooser line |
| 194 | vfx-design/SKILL.md:33 | Tool by shape the eye reads: particles, mesh plus particles, beam/trail, object change plus flash, fake debris, camera/post | sharpens | VR-01, VR-18 | Added as the VR-01 (DS) chooser line |
| 195 | vfx-design/SKILL.md:41 | Under about 10 studs prefer particles to meshes for rings, slashes, streaks | sharpens | VR-01 | In the VR-01 (DS) line [inference] |
| 196 | vfx-design/SKILL.md:44 | VFX is visuals only; never changes gameplay or touches real game parts | adds | VR-20 (new) | "Reads truth, never sets it"; separation of simulation and presentation |
| 197 | vfx-design/SKILL.md:44 | Fake destruction with the effect's own cosmetic parts is encouraged | rejected | VR-15 | DS-only owner decision (D-290); spawning own cosmetic pieces is already VR-15 craft |
| 198 | vfx-design/SKILL.md:45 | Drawn area matches the system (edge ±5 %); no invented radius rings; accuracy > readability > theme | adds | VR-20 (new), UP-01 | - |
| 199 | vfx-design/SKILL.md:45 | The big layer fires only on a confirmed success | adds | GD-34 (new) | - |
| 200 | vfx-design/SKILL.md:46 | Importance drives size, brightness, saturation, sharpness, lifetime; brightest pixel to the top priority; threat > own > pickups > others > ambient | sharpens | VH-02, VR-02 | Prominence order added to VH-02 as a (DS) line |
| 201 | vfx-design/SKILL.md:47 | Weight is not intensity: fix outcome link, truth, readability, timing before making it bigger | adds | GD-34 (new) | - |
| 202 | vfx-design/SKILL.md:48 | Sharp/down = threat, round = safe; outward burst, aimed streak, inward gathering; one focus, one shape, one hue + accent | covered | SS-05, VR-05, VR-02, VR-09, LC-19 | - |
| 203 | vfx-design/SKILL.md:49 | Anticipation, 1-3 frame punch, soft tail | covered | UP-08, VR-09 | - |
| 204 | vfx-design/SKILL.md:49 | Frequent effects shorter and quieter | adds | VR-24 (new) | - |
| 205 | vfx-design/SKILL.md:49 | Telegraphs lead by 600-1000 ms and end on the damage frame | sharpens | WT-01 | Lead values added as a (DS) line [inference] |
| 206 | vfx-design/SKILL.md:50 | Camera shake occasional; none on frequent or others' effects; off under reduced motion | adds | VR-21 (new), VR-23 (new) | - |
| 207 | vfx-design/SKILL.md:50 | Hit-stop never on explosions | adds | VR-22 (new) | - |
| 208 | vfx-design/SKILL.md:51 | Flash safety on the composite: design at most 2 large flashes per second, never over 3; no saturated red; Bloom and colour pulses count | sharpens | VR-13 | VR-13 had only [inference]/[unverified]; (DS) check added |
| 209 | vfx-design/SKILL.md:52 | Colour never the only channel; reduced variants keep all information | adds | LC-01, VR-23 (new), UP-20 (new) | - |
| 210 | vfx-design/SKILL.md:53 | Repetition: merge window, live-copy cap, variants | adds | VR-24 (new), VR-25 (new) | - |
| 211 | vfx-design/SKILL.md:54 | Paid random: odds first, identical windup, no near-miss, no celebration below cost | adds | GD-35 (new) | - |
| 212 | vfx-design/SKILL.md:55 | Sound brief says what is on screen and when; sound designer chooses; punch and transient share one trigger | sharpens | CC-02, CC-04 | One-trigger rule in the CC-02 (DS) line |
| 213 | vfx-design/SKILL.md:56 | Never claim seen or measured without a capture; never invent ids or limits; label checks | covered | CR-17 (new), AGENTS.md §3 | - |
| 214 | vfx-design/SKILL.md:59 | Read-this-file table | rejected | - | DS-only: file routing |
| 215 | vfx-design/SKILL.md:71 | Older numbers superseded by vfx-craft | rejected | - | DS-only |
| 216 | vfx-design/SKILL.md:74 | Self-check: three answers, ratings per viewer, rate, truth from config | adds | VR-01, VR-19 (new), VR-20 (new) | - |
| 217 | vfx-design/SKILL.md:75 | Self-check: context and tool per part; joining crafts; one beat list | covered | VR-01, CC-02 | - |
| 218 | vfx-design/SKILL.md:76 | Self-check: frame script with screen-size math vs a pro frame script | covered | WT-13, RI-05 | - |
| 219 | vfx-design/SKILL.md:77 | Self-check: camera channels allowed; sound brief as "what is there" | adds | VR-21 (new), CC-04 | - |
| 220 | vfx-design/SKILL.md:78 | Self-check: flash count, colour backup, reduced-motion variant, paid-random rules | adds | VR-13, VR-23 (new), GD-35 (new), LC-01 | - |
| 221 | vfx-design/SKILL.md:79 | Self-check: build matches the frame script; one capture | covered | CR-01, UP-16 | - |
| 222 | vfx-design/SKILL.md:84 | v2: storyboard replaced by written frame script | rejected | - | DS-only (D-284) |
| 223 | vfx-design/SKILL.md:85 | v2: shake occasional instead of from rating 3 | adds | VR-21 (new) | - |
| 224 | vfx-design/SKILL.md:86 | v2: layer caps replaced by the vfx-craft budget | rejected | - | DS-only budget system |
| 225 | vfx-design/SKILL.md:87 | v2: judge in a dark test place | covered | VC-06, LC-19 | Test on bright and dark backgrounds; the dark lab place itself is DS-only (D-287) |
| 226 | vfx-design/SKILL.md:90 | This project: game, style, lab place, decisions, file layout | rejected | - | DS-only |

### vfx-design/references/camera-and-screen.md (73 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 227 | vfx-design/references/camera-and-screen.md:11 | Frames without a frame rate are never converted to ms | adds | CR-17 (new) | - |
| 228 | vfx-design/references/camera-and-screen.md:17 | Importance 1-2: no camera or screen channel | adds | VR-21 (new) | Bands [inference]; DS notes no source maps ratings to parameters (X-27) |
| 229 | vfx-design/references/camera-and-screen.md:18 | Importance 3-7: trauma shake, camera kick, melee hit-stop | adds | VR-21 (new), VR-22 (new) | - |
| 230 | vfx-design/references/camera-and-screen.md:19 | Importance 8-10: FOV punch, post flash, slow motion, camera moves, white core | adds | VR-21 (new) | - |
| 231 | vfx-design/references/camera-and-screen.md:31 | Trauma added per event (+0.2 small, +0.5 big), clamps at 1 | adds | VR-21 (new) | - |
| 232 | vfx-design/references/camera-and-screen.md:32 | Shake = trauma^2-3 | adds | VR-21 (new) | - |
| 233 | vfx-design/references/camera-and-screen.md:33 | Max rotation about 3° per axis; test 1/3/6° | adds | VR-21 (new) | - |
| 234 | vfx-design/references/camera-and-screen.md:34 | No translation in 3D; rotation only | adds | VR-21 (new) | - |
| 235 | vfx-design/references/camera-and-screen.md:35 | Decay about 1 trauma per second | adds | VR-21 (new) | - |
| 236 | vfx-design/references/camera-and-screen.md:36 | Noise speed 15-20 | rejected | - | Scope: build tuning for vfx-craft; untested [P] |
| 237 | vfx-design/references/camera-and-screen.md:37 | Smoothed noise per axis; never per-frame random | adds | VR-21 (new) | - |
| 238 | vfx-design/references/camera-and-screen.md:38 | Distance falloff (0 at 3x radius), delayed to the shockwave | adds | VR-21 (new) | - |
| 239 | vfx-design/references/camera-and-screen.md:40 | Per-event trauma start values (light hit 0 ... collapse +0.6) | adds | VR-21 (new) | Used as the example; destruction rows are DS-specific [P] |
| 240 | vfx-design/references/camera-and-screen.md:49 | Melee hit-stop 50/100/150 ms; stays below the 0.54 s discomfort boundary | adds | VR-22 (new) | - |
| 241 | vfx-design/references/camera-and-screen.md:50 | Explosions and charges: 0 ms | adds | VR-22 (new) | - |
| 242 | vfx-design/references/camera-and-screen.md:51 | Projectile thrower: 0 ms | adds | VR-22 (new) | - |
| 243 | vfx-design/references/camera-and-screen.md:52 | Blocked hit about 0.67x | adds | VR-22 (new) | - |
| 244 | vfx-design/references/camera-and-screen.md:53 | Multi-hit, rapid fire, crowds: shorter or none | adds | VR-22 (new) | - |
| 245 | vfx-design/references/camera-and-screen.md:55 | Hit-stop never pauses server damage or physics; no global time scale | adds | VR-22 (new) | - |
| 246 | vfx-design/references/camera-and-screen.md:61 | Camera kick against the shot 0.5-1° | rejected | - | Weak: [P] from practice leads, shooter-specific; not needed beyond VR-21 gating |
| 247 | vfx-design/references/camera-and-screen.md:62 | Kick recovery 0.15-0.2 s | rejected | - | Weak: [P], shooter-specific |
| 248 | vfx-design/references/camera-and-screen.md:63 | FOV punch about -4° in 80 ms, top tier only; FOV clamp 1-120 | adds | VR-21 (new) | Clamp verified (Camera.yaml:268-270) |
| 249 | vfx-design/references/camera-and-screen.md:64 | FOV return 0.2-0.3 s | adds | VR-21 (new) | - |
| 250 | vfx-design/references/camera-and-screen.md:65 | Speed-boost FOV +5° as a state, gated by the motion setting | covered | VR-23 (new) | Reduced motion removes FOV changes; the value stays out [P] |
| 251 | vfx-design/references/camera-and-screen.md:66 | Slow motion 0.3x for 400 ms, local only, never global, skipped with other players near | adds | VR-21 (new) | - |
| 252 | vfx-design/references/camera-and-screen.md:72 | Brightest punch peak 2 frames at 60 fps in a 0.05-0.1 s sprite | covered | VR-09, VC-07 | One peak frame; value [P] kept out |
| 253 | vfx-design/references/camera-and-screen.md:73 | Full-screen flash at most 2 frames, top tier only; WCAG limits | sharpens | VR-13, VR-21 (new) | - |
| 254 | vfx-design/references/camera-and-screen.md:74 | Target flash is a brightness jump, 1-2 frames | sharpens | VR-09 | (DS) grayscale check added |
| 255 | vfx-design/references/camera-and-screen.md:75 | Anime impact card, local, top tier; reduce-flashes swaps it for a steady shape | covered | VR-21 (new), VR-23 (new) | - |
| 256 | vfx-design/references/camera-and-screen.md:76 | Grade pulse (ColorCorrection) counts as one flash | sharpens | VR-13 | Post pulses count in the (DS) line |
| 257 | vfx-design/references/camera-and-screen.md:77 | Darken, tint, desaturate: no number | covered | VR-13 | - |
| 258 | vfx-design/references/camera-and-screen.md:78 | Vignette pulse at most 40 %, 1 Hz; red edge counts as red flash | adds | VR-26 (new) | Low-health edge pulse |
| 259 | vfx-design/references/camera-and-screen.md:79 | Chromatic aberration off; short overlay at top tier | rejected | - | Weak: no number found; a style option |
| 260 | vfx-design/references/camera-and-screen.md:80 | No full-screen blur in play; speed lines only briefly at top tier | covered | VR-21 (new), VR-23 (new) | - |
| 261 | vfx-design/references/camera-and-screen.md:86 | CA-01 each channel names its rating; a channel above its band fails | adds | VR-21 (new) | - |
| 262 | vfx-design/references/camera-and-screen.md:87 | CA-02 trauma model on smoothed noise | adds | VR-21 (new) | - |
| 263 | vfx-design/references/camera-and-screen.md:88 | CA-03 3D shake rotation only | adds | VR-21 (new) | - |
| 264 | vfx-design/references/camera-and-screen.md:89 | CA-04 rating 1-2 adds no trauma; a single brick never moves the camera | adds | VR-21 (new) | - |
| 265 | vfx-design/references/camera-and-screen.md:90 | CA-05 blast trauma falls off and is delayed to the shockwave | adds | VR-21 (new) | - |
| 266 | vfx-design/references/camera-and-screen.md:91 | CA-06 cut shake when the camera is far back; carry weight in sound and animation | adds | VR-21 (new) | - |
| 267 | vfx-design/references/camera-and-screen.md:92 | CA-07 hit-stop is local; physics and server keep running | adds | VR-22 (new) | - |
| 268 | vfx-design/references/camera-and-screen.md:93 | CA-08 hit-stop length rises with strength | adds | VR-22 (new) | - |
| 269 | vfx-design/references/camera-and-screen.md:94 | CA-09 no hit-stop for throwers, rapid fire, chains, crowds | adds | VR-22 (new) | - |
| 270 | vfx-design/references/camera-and-screen.md:95 | CA-10 camera kick against the action, recovers | rejected | - | Weak, shooter-specific (see CS:61) |
| 271 | vfx-design/references/camera-and-screen.md:96 | CA-11 FOV punch only at the top tier, small and short, off under reduced motion | adds | VR-21 (new) | - |
| 272 | vfx-design/references/camera-and-screen.md:97 | CA-12 slow motion local, rare, skipped near a live threat | adds | VR-21 (new) | - |
| 273 | vfx-design/references/camera-and-screen.md:98 | CA-13 composite flashes at most 2 by design, 3 by governor; post pulses count | sharpens | VR-13 | - |
| 274 | vfx-design/references/camera-and-screen.md:99 | CA-14 must-notice target flash is a brightness jump | sharpens | VR-09 | - |
| 275 | vfx-design/references/camera-and-screen.md:100 | CA-15 brightest layer at most 2 frames; longer full-scale flashes only top tier | covered | VR-09, VC-07 | - |
| 276 | vfx-design/references/camera-and-screen.md:101 | CA-16 impact frames bound to the contact frame, local; reduce-flashes swap | covered | VR-09, VR-23 (new) | - |
| 277 | vfx-design/references/camera-and-screen.md:102 | CA-17 per-player grades via ColorCorrectionEffect under the Camera; ColorGradingEffect only in Lighting | adds | VR-21 (new) | ColorCorrection parenting verified (ColorCorrectionEffect.yaml:24-26); ColorGrading claim not re-checked |
| 278 | vfx-design/references/camera-and-screen.md:103 | CA-18 vignette, CA, speed lines as ScreenGui overlays; edge never the only hazard cue | adds | VR-21 (new) | Post-effects-skip-GUI kept [unverified] |
| 279 | vfx-design/references/camera-and-screen.md:104 | CA-19 pulse rates by meaning; never above 3 Hz | adds | VR-26 (new) | - |
| 280 | vfx-design/references/camera-and-screen.md:105 | CA-20 other players' effects never shake, flash or grade your screen | adds | VR-19 (new), VR-21 (new) | - |
| 281 | vfx-design/references/camera-and-screen.md:106 | CA-21 camera punch from the same confirmed event as the sound | sharpens | CC-02, GD-34 (new) | - |
| 282 | vfx-design/references/camera-and-screen.md:107 | CA-22 every channel ships with its off path | adds | VR-23 (new) | - |
| 283 | vfx-design/references/camera-and-screen.md:113 | Shake via BindToRenderStep after the camera, math.noise, never accumulate offsets | adds | VR-21 (new) | RenderPriority enum verified; exact offset [unverified] |
| 284 | vfx-design/references/camera-and-screen.md:114 | FOV tween relative to the current base, clamped | adds | VR-21 (new) | - |
| 285 | vfx-design/references/camera-and-screen.md:115 | Hit-stop via AdjustSpeed(0) and ParticleEmitter.TimeScale 0 | adds | VR-22 (new) | Verified (AnimationTrack.yaml:320-324; ParticleEmitter.yaml:962-968) |
| 286 | vfx-design/references/camera-and-screen.md:116 | Slow motion via AdjustSpeed(0.3) and TimeScale 0.3, server untouched | covered | VR-21 (new), VR-22 (new) | Same tools |
| 287 | vfx-design/references/camera-and-screen.md:117 | Flash or grade pulse via ColorCorrectionEffect under CurrentCamera | adds | VR-21 (new) | - |
| 288 | vfx-design/references/camera-and-screen.md:118 | Overlays as ScreenGui ImageLabels | adds | VR-21 (new) | [unverified] |
| 289 | vfx-design/references/camera-and-screen.md:119 | BlurEffect is full-screen Gaussian; no radial blur, CA or vignette built in | covered | VC-02 | Blur used for the squint view in the VC-02 (DS) line; the rest is scope |
| 290 | vfx-design/references/camera-and-screen.md:120 | Post effects can change at low quality; keep meaning in a non-post channel | covered | VC-02, WL-20 | VC-02 already fails a read that needs Bloom or ColorCorrection |
| 291 | vfx-design/references/camera-and-screen.md:126 | Option: shake strength slider including off | adds | VR-23 (new) | - |
| 292 | vfx-design/references/camera-and-screen.md:127 | Option: reduce flashes turns screen flashes into a steady local shape | adds | VR-23 (new) | - |
| 293 | vfx-design/references/camera-and-screen.md:128 | Option: reduced motion removes FOV, speed lines, pushes | adds | VR-23 (new) | - |
| 294 | vfx-design/references/camera-and-screen.md:129 | Option: reduce screen effects; hazard info stays in world shapes | adds | VR-23 (new) | - |
| 295 | vfx-design/references/camera-and-screen.md:135 | T-CAM test grid (trauma, exponent, max angle, FOV, kick) | adds | VR-21 (new) | In the check and apply |
| 296 | vfx-design/references/camera-and-screen.md:136 | T-HS test grid 0-400 ms, 20 repeats, 30 and 60 fps | adds | VR-22 (new) | - |
| 297 | vfx-design/references/camera-and-screen.md:137 | T-SLOW test | covered | VR-21 (new), PI-08 | - |
| 298 | vfx-design/references/camera-and-screen.md:138 | T-SAFE composite capture through an analyser | sharpens | VR-13 | - |
| 299 | vfx-design/references/camera-and-screen.md:144 | Open conflicts (final-blow tier, kick recovery, collapse decay, frame counts) | rejected | - | DS open items, not rules |

### vfx-design/references/elements.md (109 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 300 | vfx-design/references/elements.md:17 | Heading table: what gameplay, shape, value, colour, timing, composition each move | covered | UP-01, SS-05, VC-07, LC-02, UP-08, VH-05 | Overview only |
| 301 | vfx-design/references/elements.md:30 | EL-01 three answers before any look: what it is, what it does, how much impact | covered | VR-01, UP-13 | - |
| 302 | vfx-design/references/elements.md:31 | EL-02 conflicts settled by rank: accuracy, readability, theme | covered | UP-01, GD-01 | - |
| 303 | vfx-design/references/elements.md:32 | EL-03 rate 1-10 per player, ally, enemy; prominence rises with rating | adds | VR-19 (new), VH-02 | - |
| 304 | vfx-design/references/elements.md:33 | EL-04 drawn danger shape = server hit shape on every skin | adds | VR-20 (new) | - |
| 305 | vfx-design/references/elements.md:34 | EL-05 predicted cosmetic next frame; confirmed hit waits for the server and looks different | adds | GD-34 (new) | - |
| 306 | vfx-design/references/elements.md:35 | EL-06 one colour or silhouette per rule category; never reuse a rule colour for decoration | covered | LC-01, LC-02, UP-07 | - |
| 307 | vfx-design/references/elements.md:36 | EL-07 tone other players' non-threat effects; no shake, flash or post from others | adds | VR-19 (new) | - |
| 308 | vfx-design/references/elements.md:37 | EL-08 own-weapon feedback below enemy cues; muzzle-flash memory test | sharpens | VH-02 | In the VH-02 (DS) line |
| 309 | vfx-design/references/elements.md:38 | EL-09 quality tiers remove decoration only; information survives the lowest tier | sharpens | VR-08, WL-20 | VR-08 (DS) line |
| 310 | vfx-design/references/elements.md:39 | EL-10 no near-permanent glow outside active states | sharpens | VR-05 | VR-05 (DS) line |
| 311 | vfx-design/references/elements.md:40 | EL-11 every telegraph uses at least 2 channels | sharpens | WT-01 | WT-01 (DS) line |
| 312 | vfx-design/references/elements.md:41 | EL-12 block in over-strong, then dial back | covered | PI-08, SI-13, MD-06 | - |
| 313 | vfx-design/references/elements.md:45 | Dial: importance bands and their channel rights | adds | VR-21 (new) | [inference] |
| 314 | vfx-design/references/elements.md:46 | Dial: others' non-threat effects at LocalTransparencyModifier 0.5 | adds | VR-19 (new) | LocalTransparencyModifier verified (ParticleEmitter.yaml:502-511) |
| 315 | vfx-design/references/elements.md:47 | Dial: telegraph-to-hitbox tolerance, no number | adds | VR-20 (new) | Tolerance kept as [inference] |
| 316 | vfx-design/references/elements.md:53 | EL-13 one primary shape carries the purpose; secondaries carry theme | covered | VR-02 | - |
| 317 | vfx-design/references/elements.md:54 | EL-14 sharpness tracks threat | covered | SS-05, VR-05 | - |
| 318 | vfx-design/references/elements.md:55 | EL-15 outward burst, aimed streak, inward gathering | covered | VR-09, WT-12, CF-10 | - |
| 319 | vfx-design/references/elements.md:56 | EL-16 ground areas: circle or cone; vertical border against oval flattening; decals follow slopes | adds | VR-20 (new) | - |
| 320 | vfx-design/references/elements.md:57 | EL-17 hard edge where the boundary carries information, soft for atmosphere | adds | VR-20 (new) | - |
| 321 | vfx-design/references/elements.md:58 | EL-18 one signature silhouette per weapon; success and fail differ in silhouette | covered | VR-05, UP-05, GD-02 | - |
| 322 | vfx-design/references/elements.md:59 | EL-19 direction reads in a paused frame; VelocityParallel; Trail length | covered | SS-08, VR-02 | Engine settings are vfx-craft scope |
| 323 | vfx-design/references/elements.md:60 | EL-20 low-frequency shape first; bake breakup into flipbooks; coarser variants for small sizes | covered | UP-04, MD-02 | Flipbook detail is vfx-craft scope |
| 324 | vfx-design/references/elements.md:61 | EL-21 one exaggeration level per project; squash and stretch | covered | SI-07, EX-06 | - |
| 325 | vfx-design/references/elements.md:62 | EL-22 visual scale apart from collision, never falsifying the danger border | adds | VR-20 (new) | - |
| 326 | vfx-design/references/elements.md:66 | Dial: silhouette test frame at 64-128 px grayscale | covered | SS-02, VH-07 | thumb_check.py |
| 327 | vfx-design/references/elements.md:67 | Dial: flipbook 4x4 on a 1024 sheet | rejected | - | Scope: vfx-craft build detail |
| 328 | vfx-design/references/elements.md:68 | Dial: Trail Lifetime default 2 s | rejected | - | Scope: engine default |
| 329 | vfx-design/references/elements.md:69 | Dial: one primary shape per effect | covered | VR-02 | - |
| 330 | vfx-design/references/elements.md:75 | EL-23 focus owns peak contrast, saturation and detail | covered | VC-04, VC-07, VH-05 | - |
| 331 | vfx-design/references/elements.md:76 | EL-24 supporting layers mid-value; near-white only on top-tier focus | covered | VC-07, VC-05 | - |
| 332 | vfx-design/references/elements.md:77 | EL-25 check value twice: grayscale plus a timed find test | covered | VC-02, VH-07 | - |
| 333 | vfx-design/references/elements.md:78 | EL-26 brightest pixel belongs to the top-priority element; effects above characters, below UI | sharpens | VH-02, VH-01, VC-05 | - |
| 334 | vfx-design/references/elements.md:79 | EL-27 additive for hot cores, normal for smoke; LightEmission turns darks transparent; Brightness only with LightInfluence 0 | sharpens | VR-04 | Brightness rule verified (particle-emitters.md:466-467) |
| 335 | vfx-design/references/elements.md:80 | EL-28 judge boldness at game speed and distance before polish | covered | UP-02, VH-04, EX-01 | - |
| 336 | vfx-design/references/elements.md:81 | EL-29 climax gets the biggest contrast, dissipation the least | covered | VC-17, VR-09 | - |
| 337 | vfx-design/references/elements.md:82 | EL-30 heavy impact gets a brief light pulse at the impact point, not a wash | sharpens | VR-03 | VR-03 (DS) line |
| 338 | vfx-design/references/elements.md:86 | Dial: supporting-layer value 20-80 % | covered | VC-05 | Value [P] kept out |
| 339 | vfx-design/references/elements.md:87 | Dial: focus peak 90-100 % only at the top tier | covered | VC-07 | - |
| 340 | vfx-design/references/elements.md:88 | Dial: focus contrast at least 3:1 against the local background | sharpens | VC-06 | VC-06 (DS) line |
| 341 | vfx-design/references/elements.md:89 | Dial: peak at most about 2 stops above stage diffuse white | rejected | - | Weak: broadcast HDR transfer, [P], not measurable with kit tools |
| 342 | vfx-design/references/elements.md:90 | Dial: Bloom Threshold 0.9, only focus pixels bloom | sharpens | VC-07 | Threshold semantics verified (BloomEffect.yaml:75-80) |
| 343 | vfx-design/references/elements.md:91 | Dial: blast light Range 2-3x radius, hold 2 frames, fade 0.3 s, Shadows off | sharpens | VR-03 | - |
| 344 | vfx-design/references/elements.md:92 | Dial: LightInfluence 0 on emissive cores | sharpens | VR-04 | - |
| 345 | vfx-design/references/elements.md:98 | EL-31 one dominant hue plus one accent | covered | LC-19, LC-04 | - |
| 346 | vfx-design/references/elements.md:99 | EL-32 saturation is relative; reserve strong colour | covered | LC-17, LC-01 | - |
| 347 | vfx-design/references/elements.md:100 | EL-33 clash test on a same-hue stage area; add a contrasting secondary | sharpens | LC-19 | LC-19 (DS) line |
| 348 | vfx-design/references/elements.md:101 | EL-34 recolour layers by function; the edge gets the peak when the border is the message | adds | LC-03, VR-20 (new) | - |
| 349 | vfx-design/references/elements.md:102 | EL-35 hue conventions (heal green, frost blue) | covered | LC-02 | - |
| 350 | vfx-design/references/elements.md:103 | EL-36 team colour follows the viewer's relation, paired with shape | adds | VR-19 (new) | - |
| 351 | vfx-design/references/elements.md:104 | EL-37 never colour alone; red looks darker to CVD players | sharpens | LC-01 | LC-01 (DS) line |
| 352 | vfx-design/references/elements.md:105 | EL-38 palette tone sets aggression | covered | LC-03, SI-01 | - |
| 353 | vfx-design/references/elements.md:109 | Dial: hues per effect 1 + 1 | covered | LC-19 | - |
| 354 | vfx-design/references/elements.md:110 | Dial: blast colour-over-life ramp | rejected | - | Scope: recipe value [P] for vfx-craft |
| 355 | vfx-design/references/elements.md:111 | Dial: about 8 % of male players have CVD | sharpens | LC-01 | - |
| 356 | vfx-design/references/elements.md:112 | Dial: saturated-red flash test | sharpens | VR-13 | Red flashes counted separately in the (DS) line |
| 357 | vfx-design/references/elements.md:118 | EL-39 name the phases: windup, crescendo, punch, follow-through, dissipation | covered | UP-08, RH-03 | - |
| 358 | vfx-design/references/elements.md:119 | EL-40 telegraph at least reaction + choice + motor + render; cosmetic windup never delays a control | sharpens | WT-01 | - |
| 359 | vfx-design/references/elements.md:120 | EL-41 punch: 1-2 frame bulge, brightest layer shortest; consequence on the gameplay event | covered | VR-09, WT-13 | - |
| 360 | vfx-design/references/elements.md:121 | EL-42 one shared event marker drives flash, sound, camera; steady delay beats jitter | sharpens | CC-02 | - |
| 361 | vfx-design/references/elements.md:122 | EL-43 stagger exits | sharpens | WT-11 | WT-11 (DS) line |
| 362 | vfx-design/references/elements.md:123 | EL-44 impacts front-load within the first 25 % of lifetime | covered | WT-11 | WT-11 already has 70-80 % size in the first 20-25 % |
| 363 | vfx-design/references/elements.md:124 | EL-45 no linear curves; NumberSequence interpolates linearly, add keypoints | sharpens | WT-11, WT-09 | Verified (NumberSequenceKeypoint.yaml:96, 109) |
| 364 | vfx-design/references/elements.md:125 | EL-46 active signal retires visibly when gameplay ends; fade to avoid pops | adds | VR-20 (new), VR-11 | - |
| 365 | vfx-design/references/elements.md:126 | EL-47 faster than a heartbeat reads danger, slower safe | adds | VR-26 (new) | - |
| 366 | vfx-design/references/elements.md:127 | EL-48 one cadence per element; stepped cadence reads punchy | covered | RH-01, SI-01 | Stepped cadence is a style choice |
| 367 | vfx-design/references/elements.md:128 | EL-49 length signals significance; anything hiding a target clears by its clear-by time | sharpens | VH-02, VR-07 | VR-07 (DS) line |
| 368 | vfx-design/references/elements.md:132 | Dial: telegraph lead 0.6 / 1.0 s | sharpens | WT-01 | [inference] |
| 369 | vfx-design/references/elements.md:133 | Dial: brightest punch layer 2 frames | covered | VR-09 | - |
| 370 | vfx-design/references/elements.md:134 | Dial: full shape at size by about 80 ms | covered | WT-11 | - |
| 371 | vfx-design/references/elements.md:135 | Dial: sound 0 to +40 ms late, never over 1 frame early | sharpens | CC-02 | CC-02 (DS) line; contradicts CC-02's older [inference] |
| 372 | vfx-design/references/elements.md:136 | Dial: main action done by 25 % of lifetime | covered | WT-11 | - |
| 373 | vfx-design/references/elements.md:137 | Dial: whole-effect life for brick hits and charge blasts | rejected | - | DS-only values [P] |
| 374 | vfx-design/references/elements.md:138 | Dial: dust and smoke clear-by times | sharpens | VR-07 | - |
| 375 | vfx-design/references/elements.md:139 | Dial: scorch decals until regeneration; at most 30 live | rejected | - | DS-only budget [P] |
| 376 | vfx-design/references/elements.md:140 | Dial: FlipbookFramerate 15 | rejected | - | Scope: vfx-craft build detail |
| 377 | vfx-design/references/elements.md:141 | Dial: danger pulse rates 1 to 2 to 3 Hz | adds | VR-26 (new) | - |
| 378 | vfx-design/references/elements.md:142 | Dial: heal pulse below 60 per minute | adds | VR-26 (new) | [inference]; DS marks it single-source |
| 379 | vfx-design/references/elements.md:143 | Dial: micro windup 1-2 frame inward bulge | covered | WT-01, VR-09 | - |
| 380 | vfx-design/references/elements.md:149 | EL-50 poster test: freeze the punch frame, one focus | covered | VR-09, VH-09 | - |
| 381 | vfx-design/references/elements.md:150 | EL-51 one job per layer; removable by quality tier; add a layer only if the blur test still reads | covered | VR-02, UP-06, VR-08 | Tier removal in the VR-08 (DS) line |
| 382 | vfx-design/references/elements.md:151 | EL-52 one hero per beat; the lower-rated effect dims | sharpens | VH-02 | - |
| 383 | vfx-design/references/elements.md:152 | EL-53 emit in clumped cones, not a uniform sphere; ground blasts about 45° | sharpens | WT-11 | [inference] |
| 384 | vfx-design/references/elements.md:153 | EL-54 rapid multi-hits: own onset each, or fuse | sharpens | VR-09 | - |
| 385 | vfx-design/references/elements.md:154 | EL-55 tie intensity to the outcome; reward beat after the action | adds | GD-34 (new) | - |
| 386 | vfx-design/references/elements.md:155 | EL-56 keep peaks rare; alternate with quiet stretches | covered | VH-02, RH-01, GD-11 | - |
| 387 | vfx-design/references/elements.md:156 | EL-57 muted cool background, bright warm gameplay | covered | VC-05, CF-15, LC-17 | - |
| 388 | vfx-design/references/elements.md:157 | EL-58 aftermath ground edge equals the true blast radius | adds | VR-20 (new) | - |
| 389 | vfx-design/references/elements.md:158 | EL-59 prefer a cue on another channel over more particles | covered | VC-01, UP-06 | - |
| 390 | vfx-design/references/elements.md:162 | Dial: layers per normal effect (superseded) | rejected | - | DS-only budget system |
| 391 | vfx-design/references/elements.md:163 | Dial: full-detail blasts per client at most 4 | adds | VR-24 (new) | Full-detail cap [inference] |
| 392 | vfx-design/references/elements.md:164 | Dial: at most 4 effects needing attention per view | adds | VR-19 (new) | - |
| 393 | vfx-design/references/elements.md:165 | Dial: particles per impact; Rate caps are ceilings | sharpens | VR-08, VR-24 (new) | - |
| 394 | vfx-design/references/elements.md:166 | Dial: at most 40 live particles per continuous emitter on phones | covered | VR-08 | Value [P] kept out |
| 395 | vfx-design/references/elements.md:167 | Dial: multi-hit spacing (separate at about 8 frames at 30 fps, merge under 5) | sharpens | VR-09 | - |
| 396 | vfx-design/references/elements.md:168 | Dial: peak 3-5 s, relax 30-45 s (spawn pacing) | covered | GD-11, RH-01 | Transfer from a spawn model is [inference] in DS too |
| 397 | vfx-design/references/elements.md:169 | Dial: feedback amount matches the outcome | adds | GD-34 (new) | - |
| 398 | vfx-design/references/elements.md:177 | EL-60 must-see layer starts with an abrupt onset | sharpens | VR-11 | VR-11 (DS) exception line |
| 399 | vfx-design/references/elements.md:178 | EL-61 hit flash is a brightness jump, not hue alone | sharpens | VR-09 | - |
| 400 | vfx-design/references/elements.md:179 | EL-62 motion onsets capture attention, ongoing drift does not | covered | VR-16, VR-11 | - |
| 401 | vfx-design/references/elements.md:180 | EL-63 never rely on looming alone | rejected | - | Weak: DS's own evidence is non-significant (X-35) |
| 402 | vfx-design/references/elements.md:181 | EL-64 key element differs from neighbours in some feature | covered | VC-01, VH-07 | - |
| 403 | vfx-design/references/elements.md:182 | EL-65 crowding: offset look-alike layers about 150 ms | covered | VR-02, RH-02 | Number not adopted (single lab study) |
| 404 | vfx-design/references/elements.md:183 | EL-66 repeated identical cues lose pull | adds | VR-24 (new) | - |
| 405 | vfx-design/references/elements.md:184 | EL-67 design for pop-out, not scanning | covered | VC-01, VH-07 | - |
| 406 | vfx-design/references/elements.md:185 | EL-68 score clutter with Feature Congestion | rejected | VH-05, VR-06 | Not runnable with kit tools; clutter is checked by VH-05 and VR-06 |
| 407 | vfx-design/references/elements.md:186 | EL-69 contact, then reaction reads as cause | covered | WT-13 | - |
| 408 | vfx-design/references/elements.md:190 | Conflicts and gaps table | rejected | - | DS open items, not rules |

### vfx-design/references/effect-card-and-presets.md (46 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 409 | vfx-design/references/effect-card-and-presets.md:14 | CD-01 job and rating before any asset id; card order | covered | VR-01, UP-13 | Card order is a DS template |
| 410 | vfx-design/references/effect-card-and-presets.md:15 | CD-02 null for not chosen; "no number found" instead of 0 | covered | README §4 | Library marks [inference] and never invents values |
| 411 | vfx-design/references/effect-card-and-presets.md:16 | CD-03 every number tagged; status draft until the owner confirms | covered | README §4, AGENTS.md §0 | - |
| 412 | vfx-design/references/effect-card-and-presets.md:17 | CD-04 gameplay truth read from config; the card never sets it | adds | VR-20 (new) | - |
| 413 | vfx-design/references/effect-card-and-presets.md:18 | CD-05 drawn area = server area in every tier and variant; debug sphere test | adds | VR-20 (new) | - |
| 414 | vfx-design/references/effect-card-and-presets.md:19 | CD-06 one job per layer; full-detail blast cap | adds | VR-02, VR-24 (new) | - |
| 415 | vfx-design/references/effect-card-and-presets.md:20 | CD-07 over budget, merge only non-truth layers | sharpens | VR-08 | - |
| 416 | vfx-design/references/effect-card-and-presets.md:21 | CD-08 rate per viewer; top-tier rights only at 8+ | adds | VR-19 (new), VR-21 (new) | - |
| 417 | vfx-design/references/effect-card-and-presets.md:22 | CD-09 big feedback only on a confirmed outcome; action cue never covers the impact point | adds | GD-34 (new) | - |
| 418 | vfx-design/references/effect-card-and-presets.md:23 | CD-10 phase times in ms; frames stay frames without a frame rate | adds | CR-17 (new) | - |
| 419 | vfx-design/references/effect-card-and-presets.md:24 | CD-11 one sound event per visual landmark; sync window | sharpens | CC-02, SD-05 | - |
| 420 | vfx-design/references/effect-card-and-presets.md:25 | CD-12 others' non-threat effects toned; nothing from others shakes or flashes | adds | VR-19 (new) | - |
| 421 | vfx-design/references/effect-card-and-presets.md:26 | CD-13 reduced variant keeps footprint, contact, outcome, pickups | adds | VR-23 (new) | - |
| 422 | vfx-design/references/effect-card-and-presets.md:27 | CD-14 lights Shadows off; 1024 flipbooks with a static fallback; pool reset list | rejected | VR-08 | Scope: vfx-craft build details; the information-survives-lowest-tier part is in the VR-08 (DS) line |
| 423 | vfx-design/references/effect-card-and-presets.md:28 | CD-15 short card only for minor effects | rejected | - | DS-only card process |
| 424 | vfx-design/references/effect-card-and-presets.md:29 | CD-16 name the genre preset and departures | rejected | GD-22 | DS-only preset system; genre demands are GD-22 |
| 425 | vfx-design/references/effect-card-and-presets.md:30 | CD-17 blend the two nearest presets | rejected | - | DS-only |
| 426 | vfx-design/references/effect-card-and-presets.md:34 | Full effect-card template | rejected | VR-01, VR-19 to VR-26 | DS-only template; its rule fields map to these findings |
| 427 | vfx-design/references/effect-card-and-presets.md:99 | Short card fields | rejected | - | DS-only template |
| 428 | vfx-design/references/effect-card-and-presets.md:106 | Worked example: heavy C4 on a brick wall | adds | VR-23 (new), VR-25 (new) | Two example lines reused; game-specific values stay out |
| 429 | vfx-design/references/effect-card-and-presets.md:147 | C.1 fuse contact 1500 ms | rejected | WT-01 | DS-only value |
| 430 | vfx-design/references/effect-card-and-presets.md:148 | C.1 fuse blink 1 to 2 to 3 Hz | adds | VR-26 (new) | - |
| 431 | vfx-design/references/effect-card-and-presets.md:149 | C.1 crescendo 400 ms | rejected | WT-12 | DS-only single-source value |
| 432 | vfx-design/references/effect-card-and-presets.md:150 | C.1 flash lifetime 0.05 s, peak 2 frames | covered | VR-09 | - |
| 433 | vfx-design/references/effect-card-and-presets.md:151 | C.1 core lifetime 0.45-0.55 s | rejected | - | DS-only value |
| 434 | vfx-design/references/effect-card-and-presets.md:152 | C.1 dust lifetime 2-3 s; see-through by 2 s | sharpens | VR-07 | - |
| 435 | vfx-design/references/effect-card-and-presets.md:153 | C.1 dust TimeScale 0.6 (toy vs building) | rejected | WT-03 | DS-only owner call (X-55) |
| 436 | vfx-design/references/effect-card-and-presets.md:154 | C.1 chip and ring counts 16 / 24 | rejected | - | DS-only values |
| 437 | vfx-design/references/effect-card-and-presets.md:155 | C.1 shake max rotation 3° | adds | VR-21 (new) | - |
| 438 | vfx-design/references/effect-card-and-presets.md:156 | C.1 shake decay 1.0/s | adds | VR-21 (new) | - |
| 439 | vfx-design/references/effect-card-and-presets.md:157 | C.1 blast hit-stop 0 ms | adds | VR-22 (new) | - |
| 440 | vfx-design/references/effect-card-and-presets.md:158 | C.1 FOV kick -4° in 0.15 s | adds | VR-21 (new) | - |
| 441 | vfx-design/references/effect-card-and-presets.md:159 | C.1 blast light Range 2.5x core | sharpens | VR-03 | - |
| 442 | vfx-design/references/effect-card-and-presets.md:160 | C.1 sound offset 0, window 0 to +40 ms | sharpens | CC-02 | - |
| 443 | vfx-design/references/effect-card-and-presets.md:161 | C.1 others' LocalTransparencyModifier 0.5 | adds | VR-19 (new) | - |
| 444 | vfx-design/references/effect-card-and-presets.md:162 | C.1 size spread ±15 %, never on the footprint | adds | VR-25 (new) | - |
| 445 | vfx-design/references/effect-card-and-presets.md:166 | Preset shared baseline (truth, confirmed outcome, medium build, flash cap, colour backup, others reduced, sliders) | covered | VR-20, GD-34, VR-13, LC-01, VR-19, VR-23 (all post-1c) | Every baseline rule now has a finding |
| 446 | vfx-design/references/effect-card-and-presets.md:173 | Preset Simulator (reward gold only on rewards; no celebration before confirm; odds first) | covered | LC-01, GD-34 (new), GD-35 (new) | Preset values [P] stay in vfx-design |
| 447 | vfx-design/references/effect-card-and-presets.md:174 | Preset Destruction (chunk : bits : dust; no shake per brick) | rejected | VR-21 | DS-only genre values [P]; shake rule in VR-21 |
| 448 | vfx-design/references/effect-card-and-presets.md:175 | Preset Battlegrounds (hit-stop by tier; telegraph leads; review from target camera) | covered | VR-22 (new), WT-01, VH-02 | - |
| 449 | vfx-design/references/effect-card-and-presets.md:176 | Preset Horror (no disorienting camera; fog never hides hazards; no sound-only warnings) | covered | VR-21 (new), UP-20 (new) | - |
| 450 | vfx-design/references/effect-card-and-presets.md:177 | Preset Obby (no shake on movement; trails never cover edges; first response 100 ms) | covered | VR-21 (new), VR-07, UI-17 (new) | - |
| 451 | vfx-design/references/effect-card-and-presets.md:178 | Preset Tycoon (one colour per resource; no max spectacle per purchase; true balance) | covered | LC-02, VR-24 (new), UI-19 (new) | - |
| 452 | vfx-design/references/effect-card-and-presets.md:179 | Preset Disaster survival (one hazard language; spectacle never hides the safe route) | covered | UP-07, VR-07 | - |
| 453 | vfx-design/references/effect-card-and-presets.md:180 | Preset Anime-style (impact frame top tier only; stepped holds) | covered | VR-21 (new), VR-09 | Style values are a game's art-bible choice (SI-01) |
| 454 | vfx-design/references/effect-card-and-presets.md:195 | Untested items list | rejected | - | DS open items |

### vfx-design/references/juice-repetition-sync.md (86 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 455 | vfx-design/references/juice-repetition-sync.md:13 | Procedure: name the confirmed outcome; no outcome, no big layer | adds | GD-34 (new) | - |
| 456 | vfx-design/references/juice-repetition-sync.md:14 | Procedure: importance tier and channel count | adds | VR-19 (new), VR-24 (new) | - |
| 457 | vfx-design/references/juice-repetition-sync.md:15 | Procedure: windup, punch on contact, follow-through, dissipation | covered | UP-08, RH-03 | - |
| 458 | vfx-design/references/juice-repetition-sync.md:16 | Procedure: estimate rate; frequent effects get repetition plan and caps | adds | VR-24 (new) | - |
| 459 | vfx-design/references/juice-repetition-sync.md:17 | Procedure: amplification check before any escalation | adds | GD-34 (new) | - |
| 460 | vfx-design/references/juice-repetition-sync.md:18 | Procedure: punch and sound from one event; write the sync target | sharpens | CC-02 | - |
| 461 | vfx-design/references/juice-repetition-sync.md:19 | Procedure: failure-mode review, then tests | covered | UP-16, PI-07 | - |
| 462 | vfx-design/references/juice-repetition-sync.md:25 | Study: success-dependent feedback raises competence (n=1,699) | adds | GD-34 (new) | Cited per DS; not re-read |
| 463 | vfx-design/references/juice-repetition-sync.md:26 | Study: amplified feedback not tied to success lowers competence (n=678) | adds | GD-34 (new) | - |
| 464 | vfx-design/references/juice-repetition-sync.md:27 | Study: random variety gives only a small enjoyment gain | adds | VR-25 (new) | - |
| 465 | vfx-design/references/juice-repetition-sync.md:28 | Study: curiosity predicts enjoyment and playtime | rejected | - | No design rule follows; DS itself forbids quoting playtime numbers |
| 466 | vfx-design/references/juice-repetition-sync.md:29 | Study: medium beats extreme feedback | adds | GD-34 (new) | - |
| 467 | vfx-design/references/juice-repetition-sync.md:30 | Study: raising intensity alone changed nothing | adds | GD-34 (new) | - |
| 468 | vfx-design/references/juice-repetition-sync.md:31 | Study: juicy UI raises engagement and aesthetics | covered | GD-02, UI-11 | - |
| 469 | vfx-design/references/juice-repetition-sync.md:32 | Study: feedback after the action helps; more phases help | covered | UP-08, RH-03, GD-34 (new) | - |
| 470 | vfx-design/references/juice-repetition-sync.md:33 | Study: text labels carry graded progress better than particles | adds | GD-34 (new) | Tier labels readable with particles off |
| 471 | vfx-design/references/juice-repetition-sync.md:34 | Study: juicy rated higher, played worse (abstract only) | rejected | CR-02 | Weak: abstract only; "judge on the goal, not liking" is already CR-02 |
| 472 | vfx-design/references/juice-repetition-sync.md:35 | Study: hand-tuned juice beats generated sets | covered | PI-08, UP-16 | Tune by testing in game |
| 473 | vfx-design/references/juice-repetition-sync.md:36 | Study: haptics, low and high both beat none (abstract only) | rejected | - | Weak: abstract only |
| 474 | vfx-design/references/juice-repetition-sync.md:37 | Study: shake on hit raises felt agency (abstract only) | covered | VR-21 (new) | Shake allowed on rare big successes |
| 475 | vfx-design/references/juice-repetition-sync.md:38 | Study: games without hit-stop rank near the bottom for impact | adds | VR-22 (new) | Correlational |
| 476 | vfx-design/references/juice-repetition-sync.md:39 | Study: long hit-stop turns uncomfortable (boundary about 0.54 s, VR) | adds | VR-22 (new) | - |
| 477 | vfx-design/references/juice-repetition-sync.md:40 | Caveat: the studies are not one dose curve for Roblox | covered | README §4 | Kept as "per DS" wording and [inference] values |
| 478 | vfx-design/references/juice-repetition-sync.md:46 | JU-01 big layer only on confirmed success; hierarchy action < success < big success | adds | GD-34 (new) | - |
| 479 | vfx-design/references/juice-repetition-sync.md:47 | JU-02 do not raise intensity to fix a flat effect | adds | GD-34 (new) | - |
| 480 | vfx-design/references/juice-repetition-sync.md:48 | JU-03 medium build for frequent effects; amplification only on top tiers and success | adds | VR-24 (new), GD-34 (new) | - |
| 481 | vfx-design/references/juice-repetition-sync.md:49 | JU-04 grade feedback by a learnable real cause, never at random | adds | GD-34 (new) | - |
| 482 | vfx-design/references/juice-repetition-sync.md:50 | JU-05 windup and swing layers never cover the impact point | adds | GD-34 (new), VR-07 | - |
| 483 | vfx-design/references/juice-repetition-sync.md:51 | JU-06 reward beat on or after the confirmed result; surprise only on rare tiers | adds | GD-34 (new), WT-13 | - |
| 484 | vfx-design/references/juice-repetition-sync.md:52 | JU-07 graded progress uses a text label plus particles | adds | GD-34 (new) | - |
| 485 | vfx-design/references/juice-repetition-sync.md:53 | JU-08 one job per channel; few channels on a normal hit | covered | VR-02, VR-24 (new) | - |
| 486 | vfx-design/references/juice-repetition-sync.md:54 | JU-09 hit flash is a brightness jump | sharpens | VR-09 | - |
| 487 | vfx-design/references/juice-repetition-sync.md:55 | JU-10 local weapon hit-stop by tier; none on physics, explosions, chains, crowds, throwers | adds | VR-22 (new) | - |
| 488 | vfx-design/references/juice-repetition-sync.md:56 | JU-11 shake only on success events, scaled by size; none on frequent events | adds | VR-21 (new) | - |
| 489 | vfx-design/references/juice-repetition-sync.md:57 | JU-12 one short haptic pulse on success tiers | rejected | - | Weak: abstract-only evidence; haptics API not checked |
| 490 | vfx-design/references/juice-repetition-sync.md:58 | JU-13 judge on readability and competence; compare complete builds; keep a fewer-effects build | covered | CR-02, UP-16 | - |
| 491 | vfx-design/references/juice-repetition-sync.md:59 | JU-14 each event ends in a stable readable state | covered | RH-03 | - |
| 492 | vfx-design/references/juice-repetition-sync.md:61 | Checklist of what satisfying effects share | covered | GD-34, VH-02, CC-02, UP-08, VR-24, UI-17, WT-09, RH-03 | Covered after stage 1c |
| 493 | vfx-design/references/juice-repetition-sync.md:71 | Failure: mushy (no contact concentration) | adds | VR-22 (new), VR-09 | - |
| 494 | vfx-design/references/juice-repetition-sync.md:72 | Failure: floaty (heavy pieces move like dust) | covered | WT-02, WT-09, WT-10 | - |
| 495 | vfx-design/references/juice-repetition-sync.md:73 | Failure: cheap or disconnected; mute test | adds | GD-34 (new), VR-01 | Mute test in the VR-01 (DS) line |
| 496 | vfx-design/references/juice-repetition-sync.md:74 | Failure: noisy; trim ordinary peaks, never enlarge the top | covered | VH-02, VR-02, VR-24 (new) | - |
| 497 | vfx-design/references/juice-repetition-sync.md:75 | Failure: delayed; constant delay across devices | sharpens | CC-02, UI-12 | - |
| 498 | vfx-design/references/juice-repetition-sync.md:76 | Failure: annoying or fatiguing (long freezes, slow counters, repeats, flashes) | adds | VR-24 (new), VR-22 (new), UI-19 (new) | - |
| 499 | vfx-design/references/juice-repetition-sync.md:82 | Amplification check 1: tied to the outcome | adds | GD-34 (new) | - |
| 500 | vfx-design/references/juice-repetition-sync.md:83 | Amplification check 2: impact point visible | adds | GD-34 (new) | - |
| 501 | vfx-design/references/juice-repetition-sync.md:84 | Amplification check 3: miss, hit, blocked, break, big break distinct | adds | GD-34 (new) | - |
| 502 | vfx-design/references/juice-repetition-sync.md:85 | Amplification check 4: measured on readability, not liking | covered | CR-02 | - |
| 503 | vfx-design/references/juice-repetition-sync.md:86 | Amplification check 5: frequent effects stay below the extreme build | adds | VR-24 (new) | - |
| 504 | vfx-design/references/juice-repetition-sync.md:92 | JU-15 variants hide repetition; they do not add satisfaction | adds | VR-25 (new) | - |
| 505 | vfx-design/references/juice-repetition-sync.md:93 | JU-16 randomise decoration only; lock meaning | adds | VR-25 (new) | - |
| 506 | vfx-design/references/juice-repetition-sync.md:94 | JU-17 variants by recombining layers plus one tinted grey texture | adds | VR-25 (new) | - |
| 507 | vfx-design/references/juice-repetition-sync.md:95 | JU-18 engine randomisation: FlipbookStartRandom, rotation only on symmetric sprites | adds | VR-25 (new) | FlipbookStartRandom verified (ParticleEmitter.yaml:396-401) |
| 508 | vfx-design/references/juice-repetition-sync.md:96 | JU-19 more frequent = shorter and subtler; tails under 0.5 s | adds | VR-24 (new) | - |
| 509 | vfx-design/references/juice-repetition-sync.md:97 | JU-20 merge same-kind events in a window | adds | VR-24 (new) | - |
| 510 | vfx-design/references/juice-repetition-sync.md:98 | JU-21 cap live copies, cull oldest; extras play primary only | adds | VR-24 (new) | - |
| 511 | vfx-design/references/juice-repetition-sync.md:99 | JU-22 culling priority: essential, supporting, environment; fade, never pop | sharpens | VR-08 | VR-08 (DS) line |
| 512 | vfx-design/references/juice-repetition-sync.md:100 | JU-23 live count = Rate x Lifetime + bursts; budget by copies at once | adds | VR-24 (new) | - |
| 513 | vfx-design/references/juice-repetition-sync.md:101 | JU-24 punch fades with repeats; test over hundreds of shots | adds | VR-24 (new) | - |
| 514 | vfx-design/references/juice-repetition-sync.md:103 | No VFX retrigger number found | rejected | - | No rule |
| 515 | vfx-design/references/juice-repetition-sync.md:109 | JU-25 escalation tiers gated by real outcome thresholds | adds | GD-34 (new) | - |
| 516 | vfx-design/references/juice-repetition-sync.md:110 | JU-26 each step adds one layer at the impact point, never covers it | adds | GD-34 (new) | - |
| 517 | vfx-design/references/juice-repetition-sync.md:111 | JU-27 tier named by a text label; visible reset | adds | GD-34 (new) | - |
| 518 | vfx-design/references/juice-repetition-sync.md:113 | No escalation step numbers found | rejected | - | No rule |
| 519 | vfx-design/references/juice-repetition-sync.md:121 | JU-28 one trigger schedules visual punch and sound | sharpens | CC-02 | - |
| 520 | vfx-design/references/juice-repetition-sync.md:122 | JU-29 sound 0 to +40 ms late, never over 1 frame early | sharpens | CC-02 | Contradicts CC-02's older [inference] "1 early is safer"; the DS line is evidence-based |
| 521 | vfx-design/references/juice-repetition-sync.md:123 | JU-30 brightest flash on the transient frame; swap the mesh at the flash peak; delay shake by distance | sharpens | VR-09, VR-21 (new) | - |
| 522 | vfx-design/references/juice-repetition-sync.md:124 | JU-31 intended offsets labelled on the card | covered | CC-02 | Timing changes go through the marker contract |
| 523 | vfx-design/references/juice-repetition-sync.md:125 | JU-32 constant latency; measure output on the device | sharpens | CC-02 | - |
| 524 | vfx-design/references/juice-repetition-sync.md:126 | JU-33 sound carries weight, picture carries shape; compensate when shake is cut | adds | VR-21 (new) | - |
| 525 | vfx-design/references/juice-repetition-sync.md:128 | Sync tolerance references (broadcast, studies) | sharpens | CC-02 | Evidence for the CC-02 (DS) line |
| 526 | vfx-design/references/juice-repetition-sync.md:138 | T-01 hit-stop 50/100/150 ms; explosions 0 | adds | VR-22 (new) | - |
| 527 | vfx-design/references/juice-repetition-sync.md:139 | T-02 channels per normal hit (superseded) | rejected | - | DS-only budget system |
| 528 | vfx-design/references/juice-repetition-sync.md:140 | T-03 tails under 0.5 s for every-second effects | adds | VR-24 (new) | - |
| 529 | vfx-design/references/juice-repetition-sync.md:141 | T-04 first response within 100 ms | covered | UI-12, GD-02, UI-17 (new) | - |
| 530 | vfx-design/references/juice-repetition-sync.md:142 | T-05 merge window 100 ms | adds | VR-24 (new) | - |
| 531 | vfx-design/references/juice-repetition-sync.md:143 | T-06 3 variants by recombination | adds | VR-25 (new) | - |
| 532 | vfx-design/references/juice-repetition-sync.md:144 | T-07 at most 8 live copies, cull oldest | adds | VR-24 (new) | - |
| 533 | vfx-design/references/juice-repetition-sync.md:145 | T-08 at most 10 particles per frequent copy | adds | VR-24 (new) | - |
| 534 | vfx-design/references/juice-repetition-sync.md:146 | T-09 sound offset window | sharpens | CC-02 | - |
| 535 | vfx-design/references/juice-repetition-sync.md:147 | T-10 large flashes 2 per second by design | sharpens | VR-13 | - |
| 536 | vfx-design/references/juice-repetition-sync.md:148 | T-11 coin flight 0.5 s, count-up at most 0.6 s | adds | UI-19 (new) | - |
| 537 | vfx-design/references/juice-repetition-sync.md:149 | T-12 reward layer stagger 0 / +80 / +140 ms | covered | WT-11, UI-19 (new) | Stagger in the WT-11 (DS) line; offsets as the UI-19 example |
| 538 | vfx-design/references/juice-repetition-sync.md:150 | T-13 random spread on decorative layers | adds | VR-25 (new) | - |
| 539 | vfx-design/references/juice-repetition-sync.md:151 | T-14 escalation tiers 3, reset 3 s | adds | GD-34 (new) | Visible reset adopted; numbers from tier-D leads not adopted |
| 540 | vfx-design/references/juice-repetition-sync.md:157 | Unsettled evidence and tests table | rejected | - | DS open items |

### vfx-design/references/moment-recipes.md (107 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 541 | vfx-design/references/moment-recipes.md:19 | MO-01 rate every moment per viewer; prominence rises with rating | adds | VR-19 (new), VH-02 | - |
| 542 | vfx-design/references/moment-recipes.md:20 | MO-02 screen-level channels only at 8+; shake from 3 | adds | VR-21 (new) | - |
| 543 | vfx-design/references/moment-recipes.md:21 | MO-03 final blow 8 vs ordinary kill 7 | rejected | VR-21 | DS-only tier settlement [P] |
| 544 | vfx-design/references/moment-recipes.md:22 | MO-04 gameplay information first; brightest pixel to the top priority | sharpens | UP-01, VH-02 | - |
| 545 | vfx-design/references/moment-recipes.md:23 | MO-05 punch on the server-confirmed change; pending state over 100 ms | adds | GD-34 (new) | - |
| 546 | vfx-design/references/moment-recipes.md:24 | MO-06 amplify only what is tied to the outcome | adds | GD-34 (new) | - |
| 547 | vfx-design/references/moment-recipes.md:25 | MO-07 sound transient from the same event; sync window | sharpens | CC-02 | - |
| 548 | vfx-design/references/moment-recipes.md:26 | MO-08 composite flash governor | sharpens | VR-13 | - |
| 549 | vfx-design/references/moment-recipes.md:27 | MO-09 hit-stop only on weapon contact, local | adds | VR-22 (new) | - |
| 550 | vfx-design/references/moment-recipes.md:28 | MO-10 trauma shake, rotation only; none on light hits, warnings, per brick, dashes; slider | adds | VR-21 (new), VR-23 (new) | - |
| 551 | vfx-design/references/moment-recipes.md:29 | MO-11 telegraph equals the real area and timing; removed on the damage frame | adds | VR-20 (new), WT-01 | - |
| 552 | vfx-design/references/moment-recipes.md:30 | MO-12 colour never alone; greyscale and CVD filter | covered | LC-01, UP-20 (new) | - |
| 553 | vfx-design/references/moment-recipes.md:31 | MO-13 sight blockers see-through by 2 s | sharpens | VR-07 | - |
| 554 | vfx-design/references/moment-recipes.md:32 | MO-14 debris fades, never pops; no floating leftovers | covered | VR-11 | - |
| 555 | vfx-design/references/moment-recipes.md:33 | MO-15 pulse rates by meaning | adds | VR-26 (new) | - |
| 556 | vfx-design/references/moment-recipes.md:34 | MO-16 reveal windup identical for every tier | adds | GD-35 (new) | - |
| 557 | vfx-design/references/moment-recipes.md:35 | MO-17 no near-miss | adds | GD-35 (new) | - |
| 558 | vfx-design/references/moment-recipes.md:36 | MO-18 odds visible before purchase | adds | GD-35 (new) | - |
| 559 | vfx-design/references/moment-recipes.md:37 | MO-19 others' reward and movement effects toned | adds | VR-19 (new) | - |
| 560 | vfx-design/references/moment-recipes.md:38 | MO-20 reduced motion; separate controls | adds | VR-23 (new) | - |
| 561 | vfx-design/references/moment-recipes.md:39 | MO-21 toy-brick vocabulary | rejected | UP-11 | DS-only style; "effects match the art bible" is UP-11 |
| 562 | vfx-design/references/moment-recipes.md:40 | MO-22 frequent moments shorter; exits shorter than entrances | adds | VR-24 (new), UI-17 (new) | - |
| 563 | vfx-design/references/moment-recipes.md:41 | MO-23 full-detail blast cap; extras play primary only | adds | VR-24 (new) | - |
| 564 | vfx-design/references/moment-recipes.md:42 | MO-24 never random-start a meaningful one-shot | adds | VR-25 (new) | - |
| 565 | vfx-design/references/moment-recipes.md:43 | MO-25 rapid impacts each get their own onset (170 / 340 ms) | sharpens | VR-09 | - |
| 566 | vfx-design/references/moment-recipes.md:44 | MO-26 projectile head brighter than trail; charge never brighter than release | covered | VR-02, WT-12 | - |
| 567 | vfx-design/references/moment-recipes.md:45 | MO-27 deterministic fuses; countdown tracks the server | adds | VR-20 (new) | - |
| 568 | vfx-design/references/moment-recipes.md:46 | MO-28 every primary flipbook has a static fallback | sharpens | VR-08 | Information survives the lowest tier |
| 569 | vfx-design/references/moment-recipes.md:52 | Tunable: brightest flash peak 2 frames | covered | VR-09 | - |
| 570 | vfx-design/references/moment-recipes.md:53 | Tunable: hit-stop light / heavy / crit | adds | VR-22 (new) | - |
| 571 | vfx-design/references/moment-recipes.md:54 | Tunable: blocked hit-stop 0.67x | adds | VR-22 (new) | - |
| 572 | vfx-design/references/moment-recipes.md:55 | Tunable: trauma per event | adds | VR-21 (new) | - |
| 573 | vfx-design/references/moment-recipes.md:56 | Tunable: shake max angle | adds | VR-21 (new) | - |
| 574 | vfx-design/references/moment-recipes.md:57 | Tunable: trauma decay | adds | VR-21 (new) | - |
| 575 | vfx-design/references/moment-recipes.md:58 | Tunable: FOV kick at 8+ | adds | VR-21 (new) | - |
| 576 | vfx-design/references/moment-recipes.md:59 | Tunable: final-blow slow motion, local | adds | VR-21 (new) | - |
| 577 | vfx-design/references/moment-recipes.md:60 | Tunable: telegraph lead 600 / 1000 ms | sharpens | WT-01 | - |
| 578 | vfx-design/references/moment-recipes.md:61 | Tunable: countdown blink 1 / 2 / 3 Hz | adds | VR-26 (new) | - |
| 579 | vfx-design/references/moment-recipes.md:62 | Tunable: zone fill 0.75 with an opaque outline, at most 1 Hz | adds | VR-20 (new), VR-26 (new) | - |
| 580 | vfx-design/references/moment-recipes.md:63 | Tunable: chain link spacing | sharpens | VR-09 | - |
| 581 | vfx-design/references/moment-recipes.md:64 | Tunable: dust clear-by | sharpens | VR-07 | - |
| 582 | vfx-design/references/moment-recipes.md:65 | Tunable: building dust TimeScale 0.6 | rejected | - | DS-only owner call |
| 583 | vfx-design/references/moment-recipes.md:66 | Tunable: collapse windup 1.5 s creak, trickle, lean | rejected | WT-01, WL-05 | DS-only value; the tell principle is WT-01 |
| 584 | vfx-design/references/moment-recipes.md:67 | Tunable: blast light | sharpens | VR-03 | - |
| 585 | vfx-design/references/moment-recipes.md:68 | Tunable: trail lifetimes | rejected | VR-02 | Scope: vfx-craft values [P]; tail shorter than head is VR-02 |
| 586 | vfx-design/references/moment-recipes.md:69 | Tunable: spark start values | rejected | - | Scope: vfx-craft tutorial values |
| 587 | vfx-design/references/moment-recipes.md:70 | Tunable: sound offset | sharpens | CC-02 | - |
| 588 | vfx-design/references/moment-recipes.md:71 | Tunable: others' effects at 0.5 | adds | VR-19 (new) | - |
| 589 | vfx-design/references/moment-recipes.md:72 | Tunable: continuous emitter at most 40 live | covered | VR-08 | Value [P] kept out |
| 590 | vfx-design/references/moment-recipes.md:73 | Tunable: live Highlights at most 20 | rejected | LC-01 | Weak: untested [P]; the engine cap 255 is already in LC-01 roblox_fit |
| 591 | vfx-design/references/moment-recipes.md:74 | Tunable: scorch decals at most 30 | rejected | - | DS-only |
| 592 | vfx-design/references/moment-recipes.md:85 | Recipe light hit: small flash, no shake, no hit-stop on rapid fire; vary samples, never timing | adds | VR-09, VR-21 (new), VR-22 (new), VR-25 (new) | - |
| 593 | vfx-design/references/moment-recipes.md:86 | Recipe heavy hit: dense core, hit-stop 100 ms, small shake, no FOV | adds | VR-22 (new), VR-21 (new), WT-11 | - |
| 594 | vfx-design/references/moment-recipes.md:87 | Recipe critical hit: distinct accent shape, no full-screen flash per crit | adds | VR-05, VR-21 (new), VR-13 | - |
| 595 | vfx-design/references/moment-recipes.md:88 | Recipe final blow: local slow motion, FOV kick, no victory before confirm | adds | VR-21 (new), GD-34 (new) | - |
| 596 | vfx-design/references/moment-recipes.md:89 | Recipe ordinary kill: no FOV, no slow motion | adds | VR-21 (new) | - |
| 597 | vfx-design/references/moment-recipes.md:90 | Recipe blocked hit: shows why, never silent | adds | UI-18 (new), VR-22 (new) | - |
| 598 | vfx-design/references/moment-recipes.md:96 | Recipe small explosion: clumped cones, ring never wider than the damage radius | adds | WT-11, VR-20 (new) | - |
| 599 | vfx-design/references/moment-recipes.md:97 | Recipe medium explosion: swap to the destroyed mesh at the flash peak; smoke see-through by 2 s | sharpens | VR-09, VR-07 | - |
| 600 | vfx-design/references/moment-recipes.md:98 | Recipe huge explosion: distance-delayed shake, FOV punch, grade pulse counts as a flash | adds | VR-21 (new), VR-13 | - |
| 601 | vfx-design/references/moment-recipes.md:99 | Recipe chain: per-link onset, escalate only with real outcome | adds | VR-09, GD-34 (new) | - |
| 602 | vfx-design/references/moment-recipes.md:100 | Recipe delayed charge: blink 1/2/3 Hz from the server fuse; no random fuse | adds | VR-26 (new), VR-20 (new) | - |
| 603 | vfx-design/references/moment-recipes.md:106 | Recipe wood break | covered | WL-18, SD-23 | Material drives effect and sound; recipe values [P] stay in vfx-design |
| 604 | vfx-design/references/moment-recipes.md:107 | Recipe stone break; dust never hides the new opening | covered | WL-18, VR-07 | - |
| 605 | vfx-design/references/moment-recipes.md:108 | Recipe glass break; no sustained glitter (reads as reward) | covered | WL-18, UP-07 | - |
| 606 | vfx-design/references/moment-recipes.md:109 | Recipe metal; distinct response per material | covered | WL-18, SD-23 | - |
| 607 | vfx-design/references/moment-recipes.md:110 | Recipe toy brick | rejected | - | DS-only |
| 608 | vfx-design/references/moment-recipes.md:111 | Recipe building collapse: stress tell, tip as one, dust never hides escape routes | covered | WT-01, WL-05, VR-07 | Values DS-only |
| 609 | vfx-design/references/moment-recipes.md:117 | Recipe windup / charge: brightness rises, peak saved for release, cancel collapse | covered | WT-12, VR-09 | - |
| 610 | vfx-design/references/moment-recipes.md:118 | Recipe projectile: head brightest; impact on the authoritative collision | covered | VR-02, GD-34 (new) | - |
| 611 | vfx-design/references/moment-recipes.md:119 | Recipe swing trail: sharp leading edge, never masking the next swing | covered | VR-02, SS-08 | Trail:Clear across teleports is vfx-craft scope |
| 612 | vfx-design/references/moment-recipes.md:120 | Recipe muzzle flash: next rendered frame client-side; never hides the aim target | covered | VH-02, UI-12 | - |
| 613 | vfx-design/references/moment-recipes.md:121 | Recipe weapon impact: per material; confirmed hits wait for the server | covered | WL-18, GD-34 (new) | - |
| 614 | vfx-design/references/moment-recipes.md:122 | Recipe area attack: true boundary is primary; vertical border rings; removed on the last tick | adds | VR-20 (new) | - |
| 615 | vfx-design/references/moment-recipes.md:128 | Recipe telegraph: geometrically true, progress ends on the damage frame, at least 2 channels | adds | VR-20 (new), WT-01 | - |
| 616 | vfx-design/references/moment-recipes.md:129 | Recipe danger zone: steady or 1 Hz, hard true edge, fade ends on expiry | adds | VR-20 (new), VR-26 (new) | - |
| 617 | vfx-design/references/moment-recipes.md:130 | Recipe timer: monotonic, at most 3 Hz | adds | VR-26 (new) | - |
| 618 | vfx-design/references/moment-recipes.md:131 | Recipe low health: edge pulse 1 Hz, centre clear, no red wash, no control loss | adds | VR-26 (new) | - |
| 619 | vfx-design/references/moment-recipes.md:137 | Recipe pickup: local pop, merged within 100 ms, whole effect under 300 ms, no shake | adds | VR-24 (new) | - |
| 620 | vfx-design/references/moment-recipes.md:138 | Recipe coins to counter: representative sprites, true final number | adds | UI-19 (new) | - |
| 621 | vfx-design/references/moment-recipes.md:139 | Recipe backpack full: state + label + icon; rate-limited deny cue | adds | UI-18 (new), UI-13 | - |
| 622 | vfx-design/references/moment-recipes.md:140 | Recipe sell: nothing before confirm; burst steps by sale size | adds | GD-34 (new) | - |
| 623 | vfx-design/references/moment-recipes.md:141 | Recipe level-up: short, never blocks input; no aura that looks like a buff | covered | GD-02, VR-05 | - |
| 624 | vfx-design/references/moment-recipes.md:142 | Recipe unlock: settles into a usable state; beacon until visited; no ownership before confirm | covered | UI-14, WL-12, GD-34 (new) | - |
| 625 | vfx-design/references/moment-recipes.md:146 | Reveal windup V1 identical for every tier; no rarity tint before the result | adds | GD-35 (new) | - |
| 626 | vfx-design/references/moment-recipes.md:153 | Reveal tier ladder Common to Secret (seven rows) | adds | GD-35 (new) | Ladder principle adopted; per-tier values DS-only |
| 627 | vfx-design/references/moment-recipes.md:161 | Ladder basis; push-ins and white off under reduced motion; tier nameable without colour | adds | GD-35 (new), VR-23 (new), UP-20 (new) | - |
| 628 | vfx-design/references/moment-recipes.md:166 | Quick-open and skip after confirm; batch rules | adds | GD-35 (new) | Numbers DS-only |
| 629 | vfx-design/references/moment-recipes.md:175 | Recipe dash: no cloud over the destination; no shake per dash in multiplayer | covered | VR-07, VR-21 (new) | - |
| 630 | vfx-design/references/moment-recipes.md:176 | Recipe jump: no radial burst that reads as an attack | covered | VR-05 | - |
| 631 | vfx-design/references/moment-recipes.md:177 | Recipe landing: dust sized by fall height | covered | WT-22, WT-02 | - |
| 632 | vfx-design/references/moment-recipes.md:178 | Recipe speed lines: only with real speed; off under reduced motion | covered | VR-23 (new), GD-07 | - |
| 633 | vfx-design/references/moment-recipes.md:179 | Recipe teleport: departure and arrival as two cues; no fake path | covered | UP-08, UI-14 | - |
| 634 | vfx-design/references/moment-recipes.md:185 | Ambient dust in light: sparse, faded in and out | covered | VR-16, VR-11 | - |
| 635 | vfx-design/references/moment-recipes.md:186 | Ambient fireflies: never gold (reserved reward colour) | covered | VR-16, LC-01 | - |
| 636 | vfx-design/references/moment-recipes.md:187 | Ambient fog: Atmosphere first; never hides hazards or pickups | covered | WL-25, VR-16, UP-20 (new) | - |
| 637 | vfx-design/references/moment-recipes.md:188 | Ambient embers: from a source, never a collectible look | covered | VR-16, LC-01 | - |
| 638 | vfx-design/references/moment-recipes.md:189 | Ambient weather: lightning gets a flash review | sharpens | VR-13 | - |
| 639 | vfx-design/references/moment-recipes.md:190 | Stage atmosphere: muted background, high Bloom threshold | sharpens | VC-05, VC-07 | - |
| 640 | vfx-design/references/moment-recipes.md:201 | Paid random 1: every outcome and % before purchase | adds | GD-35 (new) | Policy page not in the mirror: [unverified] |
| 641 | vfx-design/references/moment-recipes.md:202 | Paid random 2: a worded Details control | adds | GD-35 (new) | - |
| 642 | vfx-design/references/moment-recipes.md:203 | Paid random 3: luck boosts explained with numbers; luck VFX never suggest more | adds | GD-35 (new) | - |
| 643 | vfx-design/references/moment-recipes.md:204 | Paid random 4: one-per-user outcomes update the odds | rejected | - | Scope: policy detail for the kit platform-policy skill; [unverified] here |
| 644 | vfx-design/references/moment-recipes.md:205 | Paid random 5: restricted-user path via PolicyService | adds | GD-35 (new) | Verified (PolicyService.yaml:91) |
| 645 | vfx-design/references/moment-recipes.md:206 | Paid random 6: static odds panel, nothing covers it, no near-miss, no urgency | adds | GD-35 (new) | - |
| 646 | vfx-design/references/moment-recipes.md:207 | Paid random 7: earned rewards need no disclosure; DS owner questions | rejected | - | Scope / DS-only open questions |
| 647 | vfx-design/references/moment-recipes.md:213 | Unsettled evidence table | rejected | - | DS open items |

### vfx-design/references/review.md (122 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 648 | vfx-design/references/review.md:13 | Label each check checked / inferred / not checkable; never pass what the input cannot show; list what was not checked | adds | CR-17 (new) | - |
| 649 | vfx-design/references/review.md:18 | Input: config, code and card values (what they can and cannot show) | adds | CR-17 (new) | - |
| 650 | vfx-design/references/review.md:19 | Input: one screenshot (one moment; name the phase) | adds | CR-17 (new) | - |
| 651 | vfx-design/references/review.md:20 | Input: frame sequence with known fps (timing; no sound) | adds | CR-17 (new) | - |
| 652 | vfx-design/references/review.md:21 | Input: video with audio (sync; device latency not shown) | adds | CR-17 (new) | - |
| 653 | vfx-design/references/review.md:22 | Any input: player tests, owner ratings, real-device perf need a test plan | adds | CR-17 (new) | - |
| 654 | vfx-design/references/review.md:28 | R0 card facts before art notes | covered | UP-13, UP-16 | - |
| 655 | vfx-design/references/review.md:29 | R1 block-in in grey shapes at real timing | covered | UP-04, PI-04 | - |
| 656 | vfx-design/references/review.md:30 | R2 truth overlay of the server area for every viewer and tier | adds | VR-20 (new) | - |
| 657 | vfx-design/references/review.md:31 | R3 frame by frame; contact cell on the contact frame; punch in the first 5 frames | covered | UP-08, CC-02 | - |
| 658 | vfx-design/references/review.md:32 | R4 slow playback at TimeScale 0.25, solo each layer | adds | CR-17 (new), VR-02 | Slow playback never proves feel |
| 659 | vfx-design/references/review.md:33 | R5 grayscale via ColorCorrectionEffect Saturation -1 | sharpens | VC-02 | Verified (ColorCorrectionEffect.yaml:78-84) |
| 660 | vfx-design/references/review.md:34 | R6 squint via BlurEffect Size | sharpens | VC-02 | Verified (BlurEffect.yaml:31-36) |
| 661 | vfx-design/references/review.md:35 | R7 real phone at intended distance; lowest and highest quality | covered | UP-02, WL-20 | - |
| 662 | vfx-design/references/review.md:36 | R8 worst plausible concurrency with pickups, players, UI | covered | VR-06, VR-19 (new) | - |
| 663 | vfx-design/references/review.md:37 | R9 brightest, darkest, most saturated stage; inside dust | covered | VC-06, LC-19 | - |
| 664 | vfx-design/references/review.md:38 | R10 muted read first, then measured sync | sharpens | VR-01, CC-02 | - |
| 665 | vfx-design/references/review.md:39 | R11 100 triggers at 1 per second | adds | VR-24 (new) | - |
| 666 | vfx-design/references/review.md:40 | R12 comfort and safety: reduced mode, composite flash count | adds | VR-23 (new), VR-13 | - |
| 667 | vfx-design/references/review.md:41 | R13 performance on a low-end phone, 10-15 min | sharpens | VR-08 | - |
| 668 | vfx-design/references/review.md:42 | R14 before/after with the same seed, camera and competing effects | adds | CR-17 (new) | - |
| 669 | vfx-design/references/review.md:48 | RV-01 R0 before any art note; stop and ask for facts | covered | UP-13, UP-16 | - |
| 670 | vfx-design/references/review.md:49 | RV-02 label every check | covered | CR-17 (new), AGENTS.md §3 | - |
| 671 | vfx-design/references/review.md:50 | RV-03 end with a could-not-check list | adds | CR-17 (new) | - |
| 672 | vfx-design/references/review.md:51 | RV-04 truth judged against server numbers or an overlay, never by eye | adds | VR-20 (new) | - |
| 673 | vfx-design/references/review.md:52 | RV-05 fix in rank order; no rank 3-4 notes while rank 1 is open | covered | PI-07, VH-11, UP-01 | - |
| 674 | vfx-design/references/review.md:53 | RV-06 slow playback never proves feel; re-check at 1x | adds | CR-17 (new) | - |
| 675 | vfx-design/references/review.md:54 | RV-07 frames stay frames unless the capture fps is known | adds | CR-17 (new) | - |
| 676 | vfx-design/references/review.md:55 | RV-08 never fix a flat hit by raising intensity first | adds | GD-34 (new) | - |
| 677 | vfx-design/references/review.md:56 | RV-09 randomness touches ornament only | adds | VR-25 (new) | - |
| 678 | vfx-design/references/review.md:57 | RV-10 review muted first; needing sound is a readability fault | sharpens | VR-01 | - |
| 679 | vfx-design/references/review.md:58 | RV-11 safety and performance block release; a warning label is not a fix | adds | VR-23 (new) | - |
| 680 | vfx-design/references/review.md:59 | RV-12 flashes tested on the composite; record tool and version | sharpens | VR-13 | - |
| 681 | vfx-design/references/review.md:60 | RV-13 judge in context (stage, distance, other players, UI) | covered | UP-02, CR-01 | - |
| 682 | vfx-design/references/review.md:61 | RV-14 perf on a real low-end phone; emulator is not verified | sharpens | VR-08 | - |
| 683 | vfx-design/references/review.md:62 | RV-15 note format: moment, symptom, concrete change, protects, retest | sharpens | CR-04 | - |
| 684 | vfx-design/references/review.md:63 | RV-16 give a direction; builder picks the value ("raise until the check passes") | sharpens | CR-04, CR-06 | - |
| 685 | vfx-design/references/review.md:64 | RV-17 change one phase at a time; replay at 1x | covered | PI-07 | - |
| 686 | vfx-design/references/review.md:65 | RV-18 lab numbers stay evidence; project values are tagged proposals | covered | README §4 | - |
| 687 | vfx-design/references/review.md:66 | RV-19 check ParticleFlipbookTextureCompatible after load | rejected | - | Scope: vfx-craft engine check |
| 688 | vfx-design/references/review.md:67 | RV-20 before/after share seed, camera, competing effects | adds | CR-17 (new) | - |
| 689 | vfx-design/references/review.md:73 | RV-T01 capture fps logged | adds | CR-17 (new) | - |
| 690 | vfx-design/references/review.md:74 | RV-T02 slow-playback TimeScale 0.25 | covered | CR-17 (new) | Value is a tool setting |
| 691 | vfx-design/references/review.md:75 | RV-T03 punch window: first 5 frames | covered | VR-09, WT-21 | - |
| 692 | vfx-design/references/review.md:76 | RV-T04 flash sprite peak 2 frames | covered | VR-09 | - |
| 693 | vfx-design/references/review.md:77 | RV-T05 sound offset window | sharpens | CC-02 | - |
| 694 | vfx-design/references/review.md:78 | RV-T06 large-area flashes 2 per second by design, 3 cap; leading edges 334 ms apart | sharpens | VR-13 | - |
| 695 | vfx-design/references/review.md:79 | RV-T07 red and danger pulse rates | adds | VR-26 (new) | - |
| 696 | vfx-design/references/review.md:80 | RV-T08 telegraph lead | sharpens | WT-01 | - |
| 697 | vfx-design/references/review.md:81 | RV-T09 see-through time of dust | sharpens | VR-07 | - |
| 698 | vfx-design/references/review.md:82 | RV-T10 at most 4 simultaneously relevant effects | adds | VR-19 (new) | - |
| 699 | vfx-design/references/review.md:83 | RV-T11 others' non-threat effects toned | adds | VR-19 (new) | - |
| 700 | vfx-design/references/review.md:84 | RV-T12 full-detail blasts per client | adds | VR-24 (new) | - |
| 701 | vfx-design/references/review.md:85 | RV-T13 live Highlights at most 20 | rejected | LC-01 | Weak: untested [P]; engine cap already in LC-01 |
| 702 | vfx-design/references/review.md:86 | RV-T14 repetition run: 100 triggers at 1 per second | adds | VR-24 (new) | - |
| 703 | vfx-design/references/review.md:87 | RV-T15 perf session 10-15 min on an Android under 2 GB | sharpens | VR-08 | - |
| 704 | vfx-design/references/review.md:88 | RV-T16 squint blur size: record the value | sharpens | VC-02 | - |
| 705 | vfx-design/references/review.md:89 | RV-T17 hit-stop tiers | adds | VR-22 (new) | - |
| 706 | vfx-design/references/review.md:90 | RV-T18 shake: rotation only, trauma model | adds | VR-21 (new) | - |
| 707 | vfx-design/references/review.md:96 | Fix rank 1: truth of area and timing | adds | VR-20 (new), UP-01 | - |
| 708 | vfx-design/references/review.md:97 | Fix rank 2: right message at the right importance | covered | VH-02, VR-19 (new) | - |
| 709 | vfx-design/references/review.md:98 | Fix rank 3: visibility, clutter, brightness | covered | VH-05, VR-06, VC-07 | - |
| 710 | vfx-design/references/review.md:99 | Fix rank 4: theme and polish | covered | UP-01, GD-01 | - |
| 711 | vfx-design/references/review.md:100 | Gate: safety and performance block release at any rank | adds | VR-23 (new), VR-08 | - |
| 712 | vfx-design/references/review.md:102 | Riot publishes 3 tiers; the rank 2/3 split is DS's | covered | UP-01, GD-01 | - |
| 713 | vfx-design/references/review.md:108 | Release gate: truth | adds | VR-20 (new) | - |
| 714 | vfx-design/references/review.md:109 | Release gate: importance order = prominence order | covered | VH-02, VR-19 (new) | - |
| 715 | vfx-design/references/review.md:110 | Release gate: readability (grayscale, squint, phone, bright and dark) | covered | VC-02, UP-02, VC-06 | - |
| 716 | vfx-design/references/review.md:111 | Release gate: sound (muted read; measured offset) | sharpens | VR-01, CC-02 | - |
| 717 | vfx-design/references/review.md:112 | Release gate: safety on the composite; reduced mode keeps essentials | adds | VR-13, VR-23 (new) | - |
| 718 | vfx-design/references/review.md:113 | Release gate: performance on a low-end phone | sharpens | VR-08 | - |
| 719 | vfx-design/references/review.md:114 | Release gate: every proposal listed; owner confirmation | covered | AGENTS.md §0, README §4 | - |
| 720 | vfx-design/references/review.md:118 | Note format: one moment, one symptom, one change; builder answers with a new capture | sharpens | CR-04 | - |
| 721 | vfx-design/references/review.md:126 | Example notes table (C4 card) | sharpens | CR-04 | Format adopted; content DS-specific |
| 722 | vfx-design/references/review.md:132 | Work order one note at a time; "make it pop" is a bad note | sharpens | CR-04, PI-07 | - |
| 723 | vfx-design/references/review.md:138 | Mistake: ring or flash edge differs from the server area | adds | VR-20 (new) | - |
| 724 | vfx-design/references/review.md:139 | Mistake: hit reads late; peak not on the contact frame | covered | VR-09, CC-02 | - |
| 725 | vfx-design/references/review.md:140 | Mistake: hazard look outlives the active end; fuse not server-driven | adds | VR-20 (new) | - |
| 726 | vfx-design/references/review.md:141 | Mistake: unavoidable hit, telegraph too short | sharpens | WT-01 | - |
| 727 | vfx-design/references/review.md:142 | Mistake: hit drawn in the wrong place from latency | covered | CC-02 | CC-02 roblox_fit: trigger on the client that sees the hit |
| 728 | vfx-design/references/review.md:143 | Mistake: dust hides the hole; a break with no sound record | sharpens | VR-07, SD-06 | - |
| 729 | vfx-design/references/review.md:144 | Mistake: everything looks top-tier | covered | VH-02, VR-02 | - |
| 730 | vfx-design/references/review.md:145 | Mistake: eye follows the trail; own launch outshines threats | covered | VR-02, VH-02 | - |
| 731 | vfx-design/references/review.md:146 | Mistake: big swing, weak result; miss looks like hit | adds | GD-34 (new) | - |
| 732 | vfx-design/references/review.md:147 | Mistake: fine in preview, lost in play; blinds others | covered | UP-02, VH-04, VR-19 (new) | - |
| 733 | vfx-design/references/review.md:148 | Mistake: value sinks or blows out; same value as the stage | covered | VC-05, VC-06, VC-07 | - |
| 734 | vfx-design/references/review.md:149 | Mistake: glow wash from low Bloom threshold; additive smoke vanishes | sharpens | VC-07, VR-04 | - |
| 735 | vfx-design/references/review.md:150 | Mistake: covers UI; black on a dark stage from LightInfluence default | sharpens | VR-07, VR-04 | - |
| 736 | vfx-design/references/review.md:151 | Mistake: competing hues; one hue with two meanings | covered | LC-19, LC-02 | - |
| 737 | vfx-design/references/review.md:152 | Mistake: colour-blind players miss it; simulator as proof | sharpens | LC-01 | - |
| 738 | vfx-design/references/review.md:153 | Mistake: lost in a same-hue scene; saturated orange light | sharpens | LC-19, VR-03 | - |
| 739 | vfx-design/references/review.md:154 | Mistake: mechanical timing; linear curves; dim long flash | covered | WT-09, WT-11, VR-09 | - |
| 740 | vfx-design/references/review.md:155 | Mistake: lingers and blocks the next effect | adds | VR-24 (new), VR-07 | - |
| 741 | vfx-design/references/review.md:156 | Mistake: one mass, all layers start and end together | sharpens | WT-11 | - |
| 742 | vfx-design/references/review.md:157 | Mistake: object vanishes before the blast reads | sharpens | VR-09 | - |
| 743 | vfx-design/references/review.md:158 | Mistake: lag feel from long or uniform hit-stop; hits merge | adds | VR-22 (new), VR-09 | - |
| 744 | vfx-design/references/review.md:159 | Mistake: toy vs building scale wrong | rejected | WT-03 | DS-only owner call (X-55) |
| 745 | vfx-design/references/review.md:160 | Mistake: muddy layers; spherical spawn; blob sparks | sharpens | VR-02, WT-11 | - |
| 746 | vfx-design/references/review.md:161 | Mistake: eye in the wrong place; card switched off by a plain fade | covered | CF-10, VR-11 | - |
| 747 | vfx-design/references/review.md:162 | Mistake: jittery shake; view through walls; numb shake | adds | VR-21 (new) | - |
| 748 | vfx-design/references/review.md:163 | Mistake: effect steals control or sight | adds | VR-21 (new), VR-23 (new) | - |
| 749 | vfx-design/references/review.md:164 | Mistake: threat or pickup not found; others at full strength | adds | VR-19 (new) | - |
| 750 | vfx-design/references/review.md:165 | Mistake: targets hidden by lingering dust; saturated ambient | sharpens | VR-07, VH-05, LC-17 | - |
| 751 | vfx-design/references/review.md:166 | Mistake: pickups lost in debris; outline them | adds | VR-19 (new) | - |
| 752 | vfx-design/references/review.md:167 | Mistake: repeat noticed; meaning shifts with randomness | adds | VR-25 (new) | - |
| 753 | vfx-design/references/review.md:168 | Mistake: frame overload; escalation over contact; frequent flourish drags (100 ms / 500 ms) | adds | VR-24 (new), GD-34 (new), UI-17 (new) | - |
| 754 | vfx-design/references/review.md:169 | Mistake: sound early; gap on device | sharpens | CC-02 | - |
| 755 | vfx-design/references/review.md:170 | Mistake: meaning lost when muted | sharpens | VR-01 | - |
| 756 | vfx-design/references/review.md:171 | Mistake: blurry or shimmering flipbook sprite | rejected | - | Scope: vfx-craft flipbook craft |
| 757 | vfx-design/references/review.md:172 | Mistake: seam, pop, hard line at geometry | covered | VR-11 | Fades covered; flipbook mode and ZOffset are vfx-craft scope |
| 758 | vfx-design/references/review.md:173 | Mistake: static texture or bleeding from a bad sheet | rejected | - | Scope: vfx-craft flipbook craft |
| 759 | vfx-design/references/review.md:174 | Mistake: ghosting; random start skips the onset | adds | VR-25 (new) | Random start off for one-shots; blend frames are scope |
| 760 | vfx-design/references/review.md:175 | Mistake: effect disappears on old phones; reuse sheets, static fallback | sharpens | VR-08 | - |
| 761 | vfx-design/references/review.md:176 | Mistake: GPU spikes; cap used as budget; overdraw | sharpens | VR-08, VR-10 | - |
| 762 | vfx-design/references/review.md:177 | Mistake: draw calls; Emit not scaled by quality; stale pooled bits | rejected | - | Scope: vfx-craft and performance build detail |
| 763 | vfx-design/references/review.md:178 | Mistake: shadowed effect lights; uncapped debris; emulator pass | sharpens | VR-08, VR-03 | - |
| 764 | vfx-design/references/review.md:179 | Mistake: seizure risk from flash rate, red pulses, area | sharpens | VR-13, VR-26 (new) | - |
| 765 | vfx-design/references/review.md:180 | Mistake: label instead of a fix; no off switch; reduced mode deletes warnings | adds | VR-23 (new) | - |
| 766 | vfx-design/references/review.md:181 | Mistake: false confidence from one analyser pass | sharpens | VR-13 | - |
| 767 | vfx-design/references/review.md:182 | Mistake: polish before block-in; intensity first | adds | UP-04, GD-34 (new) | - |
| 768 | vfx-design/references/review.md:183 | Mistake: lab number as default; vague notes | sharpens | README §4, CR-04 | - |
| 769 | vfx-design/references/review.md:189 | Unsettled evidence table | rejected | - | DS open items |

### vfx-design/references/scene-and-clutter.md (104 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 770 | vfx-design/references/scene-and-clutter.md:16 | Procedure 1: rate every effect per viewer | adds | VR-19 (new) | - |
| 771 | vfx-design/references/scene-and-clutter.md:17 | Procedure 2: name each effect's focus and the decision it supports | covered | VR-02, VH-09 | - |
| 772 | vfx-design/references/scene-and-clutter.md:18 | Procedure 3: give each effect only its band's channels | adds | VR-21 (new) | - |
| 773 | vfx-design/references/scene-and-clutter.md:19 | Procedure 4: build per viewer relation | adds | VR-19 (new) | - |
| 774 | vfx-design/references/scene-and-clutter.md:20 | Procedure 5: check the effect on the stage's extreme surfaces | sharpens | LC-19, VC-06 | - |
| 775 | vfx-design/references/scene-and-clutter.md:21 | Procedure 6: stage big moments in order and space them in time | covered | GD-11, RH-01, VC-04 | - |
| 776 | vfx-design/references/scene-and-clutter.md:22 | Procedure 7: composite stress test at max cadence and player count | covered | VR-06 | - |
| 777 | vfx-design/references/scene-and-clutter.md:23 | Procedure 8: label each check with its context | covered | CR-17 (new) | - |
| 778 | vfx-design/references/scene-and-clutter.md:29 | Budget: at most 4 attention-needing effects per viewer | adds | VR-19 (new) | - |
| 779 | vfx-design/references/scene-and-clutter.md:30 | Budget: Feature Congestion rise at most +30 % | rejected | VH-05 | Not runnable with kit tools |
| 780 | vfx-design/references/scene-and-clutter.md:31 | Budget: screen pixels changed by effects (20 % routine, 50 % peak) | sharpens | VR-06 | - |
| 781 | vfx-design/references/scene-and-clutter.md:32 | Budget: pixels above stage diffuse white at most 14 % | rejected | - | Weak: broadcast HDR transfer, [P] |
| 782 | vfx-design/references/scene-and-clutter.md:33 | Budget: world 99th percentile at least 1 stop below the focus peak | rejected | VC-07 | Weak transfer; the principle is VC-07 |
| 783 | vfx-design/references/scene-and-clutter.md:34 | Budget: overdraw view targets | rejected | VR-08, VR-10 | Scope: performance tooling; principle covered |
| 784 | vfx-design/references/scene-and-clutter.md:35 | Budget: at most 10 live particles per routine impact with 8+ players | adds | VR-24 (new) | - |
| 785 | vfx-design/references/scene-and-clutter.md:36 | Budget: full-detail blasts per client | adds | VR-24 (new) | - |
| 786 | vfx-design/references/scene-and-clutter.md:37 | Budget: at most 20 active Highlights | rejected | LC-01 | Weak: untested [P]; engine cap in LC-01 |
| 787 | vfx-design/references/scene-and-clutter.md:38 | Budget: others' non-threat effects at 50 % opacity | adds | VR-19 (new) | - |
| 788 | vfx-design/references/scene-and-clutter.md:39 | Budget: danger edge within ±5 % of the true radius, never inside | adds | VR-20 (new) | - |
| 789 | vfx-design/references/scene-and-clutter.md:40 | Budget: focus onset leads look-alike debris by 150 ms | covered | VR-02, RH-02 | Number not adopted |
| 790 | vfx-design/references/scene-and-clutter.md:41 | Budget: telegraph lead | sharpens | WT-01 | - |
| 791 | vfx-design/references/scene-and-clutter.md:42 | Budget: main action done by 25 % of lifetime | covered | WT-11 | - |
| 792 | vfx-design/references/scene-and-clutter.md:43 | Budget: top-band moments at most 1 per 30 s | covered | VH-02, GD-11 | Value [P] kept out |
| 793 | vfx-design/references/scene-and-clutter.md:44 | Budget: flash spacing and area | sharpens | VR-13 | - |
| 794 | vfx-design/references/scene-and-clutter.md:45 | Budget: looping pulse rates | adds | VR-26 (new) | - |
| 795 | vfx-design/references/scene-and-clutter.md:46 | Budget: critical markers at least 3:1 contrast | sharpens | VC-06 | - |
| 796 | vfx-design/references/scene-and-clutter.md:47 | Budget: FOV kick only at 8+ | adds | VR-21 (new) | - |
| 797 | vfx-design/references/scene-and-clutter.md:48 | Budget: vision-blocking dust clear-by | sharpens | VR-07 | - |
| 798 | vfx-design/references/scene-and-clutter.md:56 | Band map: rating to blend, value and screen channels | adds | VR-21 (new) | [inference] |
| 799 | vfx-design/references/scene-and-clutter.md:67 | SC-01 one focus per effect | covered | VR-02, VR-09 | - |
| 800 | vfx-design/references/scene-and-clutter.md:68 | SC-02 focus owns the extremes; pure white only top tier; overlapping additive copies must not clip | covered | VC-07 | - |
| 801 | vfx-design/references/scene-and-clutter.md:69 | SC-03 steer the eye by value, then colour, then shape; confirm with a timed find | covered | VC-02, VH-07 | The order is unresolved even in DS (X-30); the checks are covered |
| 802 | vfx-design/references/scene-and-clutter.md:70 | SC-04 brightest pixels on the top-priority element in every phase | sharpens | VH-02 | - |
| 803 | vfx-design/references/scene-and-clutter.md:71 | SC-05 calm rest areas around the focus | covered | VH-05 | - |
| 804 | vfx-design/references/scene-and-clutter.md:72 | SC-06 direction reads in a still | covered | SS-08, VR-02 | - |
| 805 | vfx-design/references/scene-and-clutter.md:73 | SC-07 windup cue sits on the screen spot of the later punch | covered | VR-09, CF-10 | - |
| 806 | vfx-design/references/scene-and-clutter.md:74 | SC-08 must-notice layers at full strength on the first frame; ambient fades in | sharpens | VR-11 | - |
| 807 | vfx-design/references/scene-and-clutter.md:75 | SC-09 looming only for top-band punches, with a brightness onset | rejected | - | Weak: non-significant evidence (X-35) |
| 808 | vfx-design/references/scene-and-clutter.md:76 | SC-10 focus differs from neighbours or leads them | covered | VC-01 | - |
| 809 | vfx-design/references/scene-and-clutter.md:77 | SC-11 warnings detectable in peripheral vision at phone size | covered | WT-01 | At least 2 channels per tell (WT-01 (DS) line) |
| 810 | vfx-design/references/scene-and-clutter.md:83 | SC-12 rate per viewer group | adds | VR-19 (new) | - |
| 811 | vfx-design/references/scene-and-clutter.md:84 | SC-13 attention follows rating | covered | VH-02 | - |
| 812 | vfx-design/references/scene-and-clutter.md:85 | SC-14 only the band's channels | adds | VR-21 (new) | - |
| 813 | vfx-design/references/scene-and-clutter.md:86 | SC-15 conflict order: information, readability, theme | covered | UP-01 | - |
| 814 | vfx-design/references/scene-and-clutter.md:87 | SC-16 prominence order threat > own > pickups > others > ambient | sharpens | VH-02 | - |
| 815 | vfx-design/references/scene-and-clutter.md:88 | SC-17 value bands UI > effect focus > characters > world | covered | VH-01, VC-05 | - |
| 816 | vfx-design/references/scene-and-clutter.md:89 | SC-18 must-find actors win by outline first | adds | VR-19 (new) | Deleting retired Highlights is engine scope |
| 817 | vfx-design/references/scene-and-clutter.md:90 | SC-19 pulse rate carries meaning | adds | VR-26 (new) | - |
| 818 | vfx-design/references/scene-and-clutter.md:96 | SC-20 cut detail with no gameplay; strip decoration from often-checked cues | covered | UP-06, VR-02 | - |
| 819 | vfx-design/references/scene-and-clutter.md:97 | SC-21 one dominant hue plus a complement | covered | LC-19 | - |
| 820 | vfx-design/references/scene-and-clutter.md:98 | SC-22 short effects; dissipate once done; a new threat in the aftermath is found first | covered | WT-11, VR-07 | - |
| 821 | vfx-design/references/scene-and-clutter.md:99 | SC-23 no danger look after the last damage tick | adds | VR-20 (new) | - |
| 822 | vfx-design/references/scene-and-clutter.md:100 | SC-24 strong saturation only for gameplay classes | covered | LC-01, LC-17 | - |
| 823 | vfx-design/references/scene-and-clutter.md:101 | SC-25 prefer a cheap non-particle cue; keep a cheap confirmation when capping | covered | VC-01, UP-06, GD-34 (new) | - |
| 824 | vfx-design/references/scene-and-clutter.md:102 | SC-26 noise budget per rating; attention count; pickup hues differ from nearby effects | adds | VR-19 (new) | - |
| 825 | vfx-design/references/scene-and-clutter.md:103 | SC-27 engine caps are ceilings; fewer larger particles | sharpens | VR-08, VR-10 | - |
| 826 | vfx-design/references/scene-and-clutter.md:104 | SC-28 thin by screen coverage | covered | VR-06 | - |
| 827 | vfx-design/references/scene-and-clutter.md:105 | SC-29 stress-test the full composite | covered | VR-06 | - |
| 828 | vfx-design/references/scene-and-clutter.md:106 | SC-30 every number names device, resolution, quality, FOV, distance, fps | adds | CR-17 (new) | - |
| 829 | vfx-design/references/scene-and-clutter.md:112 | SC-31 danger edge equals gameplay geometry; marks never overstate | adds | VR-20 (new) | - |
| 830 | vfx-design/references/scene-and-clutter.md:113 | SC-32 ground zones: outline + fill, follow slopes, vertical edge | adds | VR-20 (new) | - |
| 831 | vfx-design/references/scene-and-clutter.md:114 | SC-33 effects never cover HUD-critical UI; text over play gets a backing | covered | VR-07 | - |
| 832 | vfx-design/references/scene-and-clutter.md:115 | SC-34 critical markers meet the contrast floor on every stage | sharpens | VC-06 | - |
| 833 | vfx-design/references/scene-and-clutter.md:116 | SC-35 colour never alone; orange vs blue; plan for 8 % | sharpens | LC-01 | - |
| 834 | vfx-design/references/scene-and-clutter.md:117 | SC-36 decorative contrast out of path and target regions | covered | LC-18, LC-16 | - |
| 835 | vfx-design/references/scene-and-clutter.md:118 | SC-37 telegraph lead plus a sound cue ahead | sharpens | WT-01 | - |
| 836 | vfx-design/references/scene-and-clutter.md:119 | SC-38 hit confirmation only for server-confirmed outcomes; attempts look different | adds | GD-34 (new) | - |
| 837 | vfx-design/references/scene-and-clutter.md:120 | SC-39 identity and indicator size survive every skin | covered | CD-04, GD-16, VR-20 (new) | - |
| 838 | vfx-design/references/scene-and-clutter.md:121 | SC-40 nonessential shake, head bob, blur, auto camera have an off setting | adds | VR-23 (new) | - |
| 839 | vfx-design/references/scene-and-clutter.md:122 | SC-41 flashes counted on the composite against the strictest standard; a toggle is not the fix | sharpens | VR-13, VR-23 (new) | - |
| 840 | vfx-design/references/scene-and-clutter.md:123 | SC-42 more players, fewer and quieter effects; no cinematic zooms | adds | VR-19 (new) | - |
| 841 | vfx-design/references/scene-and-clutter.md:124 | SC-43 depth layers; no depth of field in active play | covered | CF-15, VR-21 (new) | - |
| 842 | vfx-design/references/scene-and-clutter.md:130 | SC-44 build per viewer relation; ranges only for those who can act | adds | VR-19 (new) | - |
| 843 | vfx-design/references/scene-and-clutter.md:131 | SC-45 tone by relation, not by caster | adds | VR-19 (new) | - |
| 844 | vfx-design/references/scene-and-clutter.md:132 | SC-46 local clarity setting | adds | VR-19 (new) | - |
| 845 | vfx-design/references/scene-and-clutter.md:133 | SC-47 one ally/enemy colour pair by relation, carried by outlines | adds | VR-19 (new), LC-02 | - |
| 846 | vfx-design/references/scene-and-clutter.md:134 | SC-48 allied spectacle only with identical hostile-facing indicators | covered | GD-16, VR-20 (new) | - |
| 847 | vfx-design/references/scene-and-clutter.md:135 | SC-49 server sends, each client draws per relation; local grades under the Camera | adds | VR-19 (new), VR-21 (new) | - |
| 848 | vfx-design/references/scene-and-clutter.md:141 | SC-50 muted stage backgrounds; the world never uses an effect colour at its value | covered | VC-05, LC-01 | - |
| 849 | vfx-design/references/scene-and-clutter.md:142 | SC-51 keep value headroom | covered | VC-05, VC-07 | - |
| 850 | vfx-design/references/scene-and-clutter.md:143 | SC-52 test on extreme surfaces; fix the stage before boosting the effect | sharpens | LC-19, VC-04 | - |
| 851 | vfx-design/references/scene-and-clutter.md:144 | SC-53 adapt brightness per stage with one multiplier in data | covered | VR-17, UP-17 | - |
| 852 | vfx-design/references/scene-and-clutter.md:145 | SC-54 Bloom only on focus pixels; additive for focus, normal for smoke | sharpens | VC-07, VR-04 | - |
| 853 | vfx-design/references/scene-and-clutter.md:146 | SC-55 faint wispy effects fail on busy stages; reads with polish off | covered | VC-02, EX-01 | - |
| 854 | vfx-design/references/scene-and-clutter.md:152 | SC-56 build-up, short peak, fade, quiet stretch | covered | UP-08, GD-11, RH-01 | - |
| 855 | vfx-design/references/scene-and-clutter.md:153 | SC-57 top-band channels only for peaks | adds | VR-21 (new), VH-02 | - |
| 856 | vfx-design/references/scene-and-clutter.md:154 | SC-58 scale intensity with outcome and rarity; tie to success | adds | GD-34 (new) | - |
| 857 | vfx-design/references/scene-and-clutter.md:155 | SC-59 space same-type onsets; overshoot then dial back | covered | VR-24 (new), PI-08 | - |
| 858 | vfx-design/references/scene-and-clutter.md:161 | SC-60 order: setup, beat before, payoff, aftermath, time to process | covered | UP-08, RH-03, CF-11 | - |
| 859 | vfx-design/references/scene-and-clutter.md:162 | SC-61 setup dims competing effects before the peak | sharpens | VC-04 | - |
| 860 | vfx-design/references/scene-and-clutter.md:163 | SC-62 beat before at object and gameplay scale; camera push, hold, pull | covered | VR-09, WT-13, VR-21 (new) | - |
| 861 | vfx-design/references/scene-and-clutter.md:164 | SC-63 one peak per effect package | covered | VR-09 | - |
| 862 | vfx-design/references/scene-and-clutter.md:165 | SC-64 hit-stop scales by weight; none in crowds | adds | VR-22 (new) | - |
| 863 | vfx-design/references/scene-and-clutter.md:166 | SC-65 aftermath shows true radius and the changed space; a player-scale anchor | adds | VR-20 (new), VR-07, WL-21 | - |
| 864 | vfx-design/references/scene-and-clutter.md:167 | SC-66 exit order glow, flare, sparks, bokeh | sharpens | WT-11 | - |
| 865 | vfx-design/references/scene-and-clutter.md:168 | SC-67 no film cuts, zooms or slow motion while control and threats are live | adds | VR-21 (new) | - |
| 866 | vfx-design/references/scene-and-clutter.md:169 | SC-68 one event for punch and sound; measure per device | sharpens | CC-02 | - |
| 867 | vfx-design/references/scene-and-clutter.md:175 | Studio method: Riot (goal order, per-viewer rating, two colours, white for ultimates) | covered | UP-01, VR-19 (new), LC-19, VC-07 | - |
| 868 | vfx-design/references/scene-and-clutter.md:176 | Studio method: WoW spell density for other party members | adds | VR-19 (new) | - |
| 869 | vfx-design/references/scene-and-clutter.md:177 | Studio method: Marvel Rivals local VFX toggles | adds | VR-19 (new) | - |
| 870 | vfx-design/references/scene-and-clutter.md:178 | Studio method: Destiny opacity by coverage; thin costliest systems | covered | VR-06, VR-08 | - |
| 871 | vfx-design/references/scene-and-clutter.md:179 | Studio method: Azur fewer larger particles, cap by concurrency | covered | VR-10, VR-24 (new) | - |
| 872 | vfx-design/references/scene-and-clutter.md:180 | Studio method: Valve pacing (peak 3-5 s, relax 30-45 s) | covered | GD-11 | - |
| 873 | vfx-design/references/scene-and-clutter.md:186 | Open items and tests table | rejected | - | DS open items |

### vfx-design/evidence/README.md (4 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 874 | vfx-design/evidence/README.md:5 | Evidence lives outside the skill; open only to check a source | rejected | - | DS-only evidence routing |
| 875 | vfx-design/evidence/README.md:12 | Evidence file map | rejected | - | DS-only |
| 876 | vfx-design/evidence/README.md:26 | Raw research location; engine truth in the docs mirror | covered | AGENTS.md §0 | - |
| 877 | vfx-design/evidence/README.md:30 | How to add evidence (tiers, contradictions, one fact in one file, re-run evals) | rejected | README §2, §4 | DS-only process; the library's own source and tag rules hold |

### vfx-design/evals/briefs.md (52 items)

| # | DS path:line | item (short) | verdict | library ID(s) or new ID | reason |
| --- | --- | --- | --- | --- | --- |
| 878 | vfx-design/evals/briefs.md:5 | Grading rule: 80 % of checks, no must failed | rejected | - | DS-only eval harness |
| 879 | vfx-design/evals/briefs.md:10 | C1 provenance tags; no claims of seen or measured | covered | README §4, CR-17 (new) | - |
| 880 | vfx-design/evals/briefs.md:11 | C2 no invented asset ids or engine limits | covered | CR-17 (new), AGENTS.md §0 | - |
| 881 | vfx-design/evals/briefs.md:12 | C3 rule IDs cited | rejected | - | DS-only |
| 882 | vfx-design/evals/briefs.md:13 | C4 deliverable format | rejected | - | DS-only |
| 883 | vfx-design/evals/briefs.md:14 | C6 frame script, pro defaults, LightInfluence 0 everywhere | rejected | VR-04 | DS-only v2 rule; the library asks for LightInfluence set on purpose (VR-04 (DS)) |
| 884 | vfx-design/evals/briefs.md:15 | C5 composite flash count, colour backup, reduced variant, budget with static fallback | adds | VR-13, LC-01, VR-23 (new), VR-08 | - |
| 885 | vfx-design/evals/briefs.md:23 | 1.1 rated per viewer about 5; no FOV, slow motion or white at this band | adds | VR-19 (new), VR-21 (new) | - |
| 886 | vfx-design/evals/briefs.md:24 | 1.2 weight from outcome link and truth; drawn edge = server radius | adds | GD-34 (new), VR-20 (new) | - |
| 887 | vfx-design/evals/briefs.md:25 | 1.3 punch 2 frames; swap at the flash peak; staggered exits | sharpens | VR-09, WT-11 | - |
| 888 | vfx-design/evals/briefs.md:26 | 1.4 no hit-stop on explosions; trauma shake rules | adds | VR-22 (new), VR-21 (new) | - |
| 889 | vfx-design/evals/briefs.md:27 | 1.5 toy vocabulary; debris fades; dust see-through by 2 s | sharpens | VR-11, VR-07 | Toy vocabulary is DS-only |
| 890 | vfx-design/evals/briefs.md:28 | 1.6 v2 budget recipe | rejected | - | DS-only budget system |
| 891 | vfx-design/evals/briefs.md:29 | 1.7 LightEmission 1 on core and sparks, 0 on dust; LightInfluence set | sharpens | VR-04 | - |
| 892 | vfx-design/evals/briefs.md:30 | 1.8 one trigger; sync window | sharpens | CC-02 | - |
| 893 | vfx-design/evals/briefs.md:31 | 1.9 test on a low-end phone 10-15 min; compare complete builds | sharpens | VR-08, CR-02 | - |
| 894 | vfx-design/evals/briefs.md:39 | 2.1 importance about 2; no shake, flash, FOV or post | adds | VR-19 (new), VR-21 (new) | - |
| 895 | vfx-design/evals/briefs.md:40 | 2.2 merge within 100 ms; exact counter | adds | VR-24 (new), UI-19 (new) | - |
| 896 | vfx-design/evals/briefs.md:41 | 2.3 caps on copies, particles, coin sprites | adds | VR-24 (new) | - |
| 897 | vfx-design/evals/briefs.md:42 | 2.4 short and subtle; coin flight 0.5 s; count-up 0.6 s | adds | VR-24 (new), UI-19 (new) | - |
| 898 | vfx-design/evals/briefs.md:43 | 2.5 plays on the confirmed credit; response within 100 ms; pending state | adds | GD-34 (new), UI-17 (new) | - |
| 899 | vfx-design/evals/briefs.md:44 | 2.6 3 variants by recombination; decoration-only randomness | adds | VR-25 (new) | - |
| 900 | vfx-design/evals/briefs.md:45 | 2.7 never brighter than a threat; reward gold only on rewards; others toned | sharpens | VH-02, LC-01, VR-19 (new) | - |
| 901 | vfx-design/evals/briefs.md:46 | 2.8 repetition test at 20 per second and over hundreds | adds | VR-24 (new) | - |
| 902 | vfx-design/evals/briefs.md:54 | 3.1 identical windup; no rarity tint before the punch | adds | GD-35 (new) | - |
| 903 | vfx-design/evals/briefs.md:55 | 3.2 no near-miss; no celebration below cost | adds | GD-35 (new), GD-34 (new) | - |
| 904 | vfx-design/evals/briefs.md:56 | 3.3 odds before purchase; Details control; PolicyService path; no urgency | adds | GD-35 (new) | - |
| 905 | vfx-design/evals/briefs.md:57 | 3.4 Legendary at 8, toast for others; skip and quick-open | adds | GD-35 (new), VR-21 (new) | Tier values DS-only |
| 906 | vfx-design/evals/briefs.md:58 | 3.5 tier nameable without colour | adds | GD-35 (new), UP-20 (new) | - |
| 907 | vfx-design/evals/briefs.md:59 | 3.6 push-in and shake off under reduced motion; flash count | adds | VR-23 (new), VR-13 | - |
| 908 | vfx-design/evals/briefs.md:60 | 3.7 push back on "make it exciting" for a paid pull | adds | GD-35 (new), GD-34 (new) | - |
| 909 | vfx-design/evals/briefs.md:68 | 4.1 drawn circle = server area in every tier and variant | adds | VR-20 (new) | - |
| 910 | vfx-design/evals/briefs.md:69 | 4.2 lead 600 / 1000 ms; 2+ channels; removed on the damage frame | sharpens | WT-01, VR-20 (new) | - |
| 911 | vfx-design/evals/briefs.md:70 | 4.3 telegraph rated 9 for the threatened player; owns the brightest pixel | adds | VR-19 (new), VH-02 | - |
| 912 | vfx-design/evals/briefs.md:71 | 4.4 colour plus pattern; sharp downward shapes; source cue not via post effects | covered | LC-01, SS-05, VR-19 (new) | - |
| 913 | vfx-design/evals/briefs.md:72 | 4.5 monotonic progress; at most 3 Hz; no random start | adds | VR-26 (new), VR-25 (new) | - |
| 914 | vfx-design/evals/briefs.md:73 | 4.6 trauma by distance; hit-stop by contact tier; composite flash count | adds | VR-21 (new), VR-22 (new), VR-13 | - |
| 915 | vfx-design/evals/briefs.md:74 | 4.7 dodge test on a 30 fps phone and a PC | covered | WT-01 | - |
| 916 | vfx-design/evals/briefs.md:82 | 5.1 start at R0: job, importance, server radius before art notes | covered | UP-13, UP-16 | - |
| 917 | vfx-design/evals/briefs.md:83 | 5.2 3 full-screen flashes in 0.5 s blocks release; a toggle is not a fix | sharpens | VR-13, VR-23 (new) | - |
| 918 | vfx-design/evals/briefs.md:84 | 5.3 0.8 s pure white core fails | covered | VC-07, VR-09 | - |
| 919 | vfx-design/evals/briefs.md:85 | 5.4 translation shake fails; rotation only | adds | VR-21 (new) | - |
| 920 | vfx-design/evals/briefs.md:86 | 5.5 6 emitters over budget; merge non-truth layers | sharpens | VR-08 | Emitter counts DS-only |
| 921 | vfx-design/evals/briefs.md:87 | 5.6 ranked findings; safety and performance block release | sharpens | CR-04, VR-23 (new) | - |
| 922 | vfx-design/evals/briefs.md:88 | 5.7 fixed cards plus a could-not-check list | adds | CR-17 (new) | - |
| 923 | vfx-design/evals/briefs.md:96 | 6.1 ambient at importance 1; never the brightest; no pickup or hazard hue | covered | VR-16, LC-01 | - |
| 924 | vfx-design/evals/briefs.md:97 | 6.2 fades, no abrupt onsets; nothing above 1 Hz | adds | VR-11, VR-26 (new) | - |
| 925 | vfx-design/evals/briefs.md:98 | 6.3 ambient values (motes lifetime, speed, rate) | rejected | VR-16 | DS-only values [P] |
| 926 | vfx-design/evals/briefs.md:99 | 6.4 muted background; high Bloom threshold; ColorGradingEffect Lighting-only | sharpens | VC-05, VC-07 | - |
| 927 | vfx-design/evals/briefs.md:100 | 6.5 palette from the art bible; test on extreme surfaces; fog never hides | covered | UP-11, LC-19, UP-20 (new) | - |
| 928 | vfx-design/evals/briefs.md:101 | 6.6 continuous emitters at most 40 live; LightEmission 0 on dust | sharpens | VR-04, VR-08 | - |
| 929 | vfx-design/evals/briefs.md:102 | 6.7 test on the real stage with gameplay effects on top | covered | UP-02, VR-19 (new) | - |

## Notes for the lead

| # | Note |
| --- | --- |
| 1 | **Conflict, CC-02:** its check says "1 early is safer than late [inference]" for sound vs the contact frame. DS's sync evidence (broadcast standards, studies; per DS) says the opposite: an early sound is noticed sooner, so target sound 0 to about 40 ms after the first lit frame and never more than 1 frame early. Per the append-only rule the old line stays; the (DS) line under it states the evidence-based target. Stage 2 makers should follow the (DS) line; the lead may retire the old inference with an owner-visible note. |
| 2 | **UP-01's engineering line** ("feedback fires on the client at once") is refined by UP-19 and GD-34: the attempt cue fires at once; the big outcome layer waits for the server's confirmation. Not a contradiction, but role books should state both halves together. |
| 3 | **GD-02 roblox_fit** says hit-stop by pausing tracks is [unverified]; VR-22 now cites the verified docs lines. **GD-26 roblox_fit** says WalkSpeed 16 is [unverified]; WL-29 cites the verified line. The old tags stay (append-only). |
| 4 | **Sources outside the transcripts:** the new findings rest on DS lines, and through them on DS's research base, which this check did not re-read. The UP-19 and UP-20 principles are therefore less directly sourced than UP-01 to UP-18; the master's note says so. |
| 5 | **Not adopted on purpose:** DS's numeric importance-to-channel map is kept only as an [inference] band (DS itself records that no source maps a rating to parameters, X-27); genre presets, material break recipes, reveal-tier timings and destruction values stay in DS as game-specific [P] values; engine build recipes (flipbook sheets, overdraw targets, pooled UI bursts, gradient shine sweeps) belong to the kit's vfx-craft, ui-basics and performance skills, which already hold most of them. |
| 6 | **Kit overlap:** the kit's own `vfx-design` and `ui-basics` skills already carry ported DS content (trauma shake, LocalTransparencyModifier, merge windows, reduced motion, thumb zones). Adding the general rules to the library keeps them alive when stage 2 rebuilds those books from the library. |
