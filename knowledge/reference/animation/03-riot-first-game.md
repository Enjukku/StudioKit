---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J006-T01, Riot ep4 transcript A:1-1100; Riot core series animation part R:2896-3420; J016 Riot extracts; VFX research folder 2026-10-12; first-game animator files (read-only)
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Animation principles from Riot and the first game: decision rules, workflow order, mistakes, collaboration, rig needs

Paraphrased notes for the lead, who writes the animator skills from them. Every row names its source line. Nothing here was fact-checked against the web; Roblox and Blender facts are out of scope (notes 01 and 02 hold those). The Riot animator teaches by showing one three-hour live piece, so the reasons she gives are the evidence; her frame counts are not (she states no frame rate, A:1-1100). Where a source is silent the row says so; (inf.) marks the extractor's own reading.

## 0. How to read

| Key | Meaning |
| --- | --- |
| A:n, R:n | Line n of the Riot ep4 transcript, or of the Riot core transcript (paths in section 1) |
| E:n, AC:n, RX:n | Lines of the J016 extracts (E-anim-vfx-sound.md, A-core.md, riot-extracts.md) |
| PT, HS, TD, DF, P4, P1, P5, RE, GR | Files of `knowledge/external/vfx-research-2026-10-12/` (section 1) |
| FA, FS, FX, FD, FT, FR, FW | First-game files (section 1). Read-only. Game-specific parts are stripped except in the owner-words rows |
| N1 xx, N2 xx | Row id in notes 01 and 02 of this folder (OR, GA, PR, GT, SY, SL, CT, FS, CS, RG, BL, RV, TL, LM) |
| strength | stated principle = the speaker says it as a rule or gives the reason; example = shown in her demo; passing remark = said in one line |
| (inf.) | extractor reading, not a source claim |

## 1. Sources table

| Key | What | Lines | Date | Trust |
| --- | --- | --- | --- | --- |
| A | Riot "Super Art Power Hour" ep4, character and gameplay animation: senior animator Lana Bachynski shows a weight and pose shift between two key poses of a bold-but-sweet character, in Maya, about 3 h (A:56, A:976); at least a day normally (A:1082-1083). Teaching demo; the rig is to be released as a free educational resource (A:1070-1074) | `C:\Users\Firew\Downloads\charcter and gameplay animations ep4.txt`, A:1-1100 | undated; supplied 2026-10-21 | Principles high (stated reasons). Numbers low: no frame rate, compressed demo. One person, one game camera (top-down style game, A:760-764) |
| R | Riot core series, character animation part: three goals, poses, ball bounce, state machines, advice from animators | `C:\Users\Firew\Downloads\Riot Core fundemental Ideas.txt`, R:2896-3420; also R:1478-1492 (anatomy), R:1538-1566 (design blocks motion), R:2403-2437 (controls), R:3826-3836, R:3886-3912, R:4210-4220 (VFX and sound timing ideas) | undated; first game dates its copy 2026-10-15 (FS:8) | High for principles and order; light, comic tone; no sign-off chain |
| E | J016 extract of A (A1-A10) | `knowledge/jobs/J016-orchestration/riot/E-anim-vfx-sound.md` E:24-156 | 2026-10-21 | Derived. Cites checked in section 10 |
| AC | J016 extract of R, section 3.5 and animation rows | `riot/A-core.md` AC:228-269, AC:124, 139, 154-155, 201, 210, 435-438, 454, 461-462, 478, 563-589, 633-645 | 2026-10-21 | Derived. Checked against R in section 10 |
| RX | Per-role rows, timing spine | `knowledge/jobs/J016-orchestration/riot-extracts.md` RX:38-46, 85, 95 | 2026-10-21 | Derived. States that no Riot source names a sign-off chain (RX:13) |
| PT | Gap fill: VFX phase timing (Riot VFX artist 0.1 s hit frame; telegraph set by design; exit order) | `vfx-research-2026-10-12/gap-phase-timing.md` PT:47-66 | research 2026-10-12 | Tier B and C artist statements; no tier A number per phase (PT:7) |
| HS | Gap fill: hit-stop, shake, flash | `gap-hitstop-shake-flash.md` HS:42-53 | 2026-10-12 | Tier D fan wikis plus first-party code; one lab study. Mixed |
| TD | Gap fill: telegraphs, reaction time, danger zones | `gap-telegraphs-danger.md` TD:46-71 | 2026-10-12 | Riot 2021 post is tier A; reaction time from a peer-reviewed study |
| DF | Gap fill: destruction feel and perceived weight | `gap-destruction-feel.md` DF:126-139 | 2026-10-12 | Lab perception studies; forum rule for miniatures; mostly "no number found" |
| P4 | Destruction VFX table | `p4-destruction.md` P4:67, 73, 83, 86, 92, 107 | 2026-10-12 | Studio posts tier A and B; collapse timing from one internal clip |
| P1 | Gameplay-shape table (windup, arcs, squash) | `p1-gameplay-shape.md` P1:70-75, 107-118 | 2026-10-12 | Cooper 2019 excerpt (tier B) and Riot posts (tier A) |
| P5 | Juice, repeats, sync | `p5-p6-p7-juice-repeat-sound.md` P5:42-68 | 2026-10-12 | Preprints and studies; repeats have no tier A number (P5:6) |
| RE | Gap fill: repetition | `gap-repetition-escalation.md` RE:109-110 | 2026-10-12 | One neuroscience paper; transfer to games is inference |
| GR | Gap fill: Riot guide and talks | `gap-riot-guide-talks.md` GR:21, 56-58, 122 | 2026-10-12 | Riot 2021 tier A; style guide itself unread |
| FA | First-game animator agent file | `DestructionSimulator\.claude\agents\animator.md` FA:13-30 | 2026-10-15 (D-281) | Owner-used; game-specific paths stripped |
| FS | First-game `animation` skill | `DestructionSimulator\.agents\skills\animation\SKILL.md` FS:1-81 | 2026-10-15 | Owner-used; itself a paraphrase of R |
| FX | First-game `references/expert-workflows.md` | `...\animation\references\expert-workflows.md` FX:1-8 | 2026-10-15 | Empty table: no lesson was ever filed |
| FD | First-game decision ledger (owner words) | `DestructionSimulator\knowledge\design\decisions.md` | 2026-09-30 to 2026-10-20 | Owner words verbatim in the ledger |
| FT | First-game tried-and-failed | `...\knowledge\design\tried-and-failed.md` FT:10, FT:25 | 2026-10-02, 2026-10-10 | Evidence from play-tests |
| FR | First-game rig prompt with the animator control layer | `...\knowledge\pipelines\rig-for-animation-prompt.md` FR:59-121 | 2026-10-12 | Rig side; used in section 7 |
| FW | First-game VFX workflow proposal | `...\knowledge\design\vfx-workflow-proposal.md` FW:13-14, 28, 114 | 2026-10-16 | Motion blueprint idea |
| F, B (pointers) | Riot 2XKO and concept extracts naming the animator | `riot/F-tcg-2xko.md` F:346-383 (silhouette in motion, separable parts, cloth cost); `riot/B-concept-keyart-splash.md` B:417, 422 (secondary motion on variants) | 2026-10-21 | Second-hand: read as extracts only, raw transcripts not re-read here |

## 2. Principles as decision rules

### 2.1 Weight and balance

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| WB1 | On a big move, decide where the centre of mass goes first; a limb can leave its support only after weight has left it. | Supported, limbed bodies (stand, step, leap, kneel). Source silent for flying, wheeled, floating or mechanical subjects; (inf.) ask what carries the load there. | Freeze before a lift: root already shifted or sunk over the remaining support. | A:92-100, A:456-468 | stated principle |
| WB2 | Show weight moving from one limb to another. She names a missing transfer as the most frequent fault in demo reels she reviews (the other is still shoulders, WB8). | Same as WB1. A fast "bursty" move may jump between near frames, but a hint of contact should remain. | Step through: a contact, lean or catch shows where weight went, even in a fast move. | A:456-474, A:490-492 | stated principle; burst case passing remark |
| WB3 | Mass must not vanish from a place between frames; energy has to go somewhere, so a part counters or catches it. | Large fast moves (spin, kick, leap). Not needed for slow, low-energy moves (inf.). | A broad swing is made believable by another part countering it (arm out, hand touching ground, root leaning). | A:244-264, A:476-492 | stated principle |
| WB4 | In a still pose the centre of gravity falls over the feet, unless imbalance is the point. | Holds and key poses; deliberate imbalance for a hit, a kick to the head, a fall. | Drop a vertical from the pelvis: it lands in the support, or the story explains why not. | R:3105-3119 | stated principle |
| WB5 | A held object looks heavier the closer it is carried to the holder's centre of gravity; held far out it looks light. | Held items (swords, tools, shields) and carried props. Source silent on recoil or tool momentum (N1 RV-F06 covers that). | Same prop, two poses: only arm distance and stance differ, yet weight reads differently. | R:3121-3133 | example |
| WB6 | Heaviness can be added with a wider, lower stance, because armor and weapon weigh the character down. Apply, then check it did not go too far. | Heavy characters. Wrong for light or nimble ones. | Stance width and height differ between a light and a heavy variant of one action. | R:3147-3161 | example |
| WB7 | Energy has a source and a path. The leg is driven from the core and root lean; arms add leverage to a jump; energy runs out through palms and fingertips. | Any action that makes and then releases force (jump, kick, throw, strike). | Before release, the pushing parts move first (shoulders, arms, hips). After release, the ends keep moving the same way. | A:258-266, A:554-558, A:892-904 | stated principle (her reasoning) |
| WB8 | Shoulders (clavicles) and hips belong to the pose. She calls the clavicles the eyebrows of the body; frozen shoulders leave a jump's energy without a source. | Bodies with a shoulder girdle and pelvis. Source silent for other forms. | Shoulders lift and tighten before a jump or landing; pelvis sinks into the pose; arms do not just swing on fixed shoulders. | A:390-410, A:652-654 | stated principle |
| WB9 | A strong landing: fast contact, then the body catches the weight; a deeper pose reads stronger than landing straight up; a loose sink reads weak. | Powerful or agile characters. A soft landing can be a character choice. | Feet touch quickly, body sinks and tightens, elbows sink with the weight; no slow scooting after contact. | A:358-372, A:438-446, A:656-660, A:930-938 | stated principle; examples |
| WB10 | Roll through the foot on a landing: weight to the toe, heel comes down as weight returns, weight moves forward to finish balanced. | Bipeds. (inf.) similar for other plantigrade feet. | Visible foot roll; final pose balanced over the foot. | A:674-684 | example |

### 2.2 Timing and spacing

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| TS1 | Spacing sells gravity. Even spacing on a bouncing or thrown thing looks wrong; positions bunch near the top and spread on the way down. An "ease" is a slow-down before a stop. | Falling, bouncing, thrown, jumping things. (inf.) not for constant-speed machines. | Plot the position per frame: gaps shrink toward the apex. | R:3197-3217, A:342-352 | stated principle |
| TS2 | The frame distance between keys sets felt speed: fewer frames between keys feels faster. While blocking, key the whole body on the same frames and slide keys to feel the rhythm. | Blocking stage. Per-part offsets come later (TS3). | Moving one gap changes how fast the move reads without changing the poses. | A:354-356, A:434-438, A:446-448 | example; stated reason |
| TS3 | Before a spring, hold a short moment of tightened energy; keep the feet planted a frame or two longer and use less ease-out so the push shows force. Then give the air more time. | Explosive moves. Soft moves do not need it (inf.). "A frame or two" is her demo value with no frame rate. | Feet stay down while the body compresses; the pop off the ground is sharp. | A:448-456, A:594-606 | example |
| TS4 | Stylised hang time: stretch the top of a jump, then pull the body down fast. A "tabletop" arc is acceptable if some life stays in it. | Cartoon or heroic worlds with approved exaggeration (N1 SY02). Not realistic bodies. | Slow top, quick fall, same logic in every jump of the game (R:2977-2983). | A:342-352 | example |
| TS5 | If a fall feels weak or slow, delete one key before or after the contact until it feels right, then repair the feet. | Falls and impacts during polish. Not a general rule. | The same fall with one frame fewer reads punchier. | A:808-816 | example |
| TS6 | A small overshoot on standing up releases the energy of the move. She calls her version cheap and says an ease-in might suit better. | Stylised moves with a release. | Slight overextension at the top, then a settle. | A:376-384 | passing remark |
| TS7 | Squash and stretch show inertia and impact: stretch when moving fast, squash when stopped by a force. | Stylised bodies. N1 SY03 says only where the rig and asset contract allow it. | Shape change follows speed and contact. | R:3219-3227 | stated principle |
| TS8 | The wind-up before an attack is information the player needs. Show it clearly. | Anything that threatens or affects the player. The wind-up length belongs to design (section 5). Cooper (2019) adds: an enemy's telegraph runs longer than a player's own anticipation, and bigger attacks get longer anticipation. | A viewer can name the attack before contact. | R:2957-2971, P1:75 | stated principle |
| TS9 | Impact freeze (hit-stop) separates light from heavy hits. Its values differ by genre: fighting-game frame data on fan wikis (tier D) lists roughly 9 to 15 frames; one platformer's first-party code freezes 10 to 100 ms; a lab study found players' favourite near-freeze about 0.4 s in its one game. Source gives no Roblox method and no shared standard. | Melee, heavy hits, big reveals. The animator supplies the held pose and the contact; design owns the value (N1 CT05, LM19). | Contact frame holds; heavier hit holds longer; the next motion starts clean. | HS:42-53, P5:42, P4:83 | industry practice, mixed tiers |
| TS10 | Shared with VFX: a Riot VFX artist prefers about 0.1 s for a hit frame, with the main glow leaving first, then flare, sparks, bokeh last. Anticipation then impact then room to process is one idea across animation, sound and VFX. | Impact events. The animator needs the contact time on the shared event list. | Flash, motion and sound land on the same contact. | PT:51, PT:56, P5:47, R:3826-3834, R:4210-4220 | industry practice |
| TS11 | A cheap way to read a hold: duplicate the key (a "copied pair") rather than step the curve, so the pause reads as a pause and its timing stays visible. | Blocking holds. Stepped keys are the other camp; she finds them hard to read. | A flat segment you can lengthen or shorten. | A:268-284 | stated reason |
| TS12 | Eases come from curve handles. She uses weighted tangents because they cut the number of keys to inspect, and says other animators dislike them. | Maya practice. Blender equivalent not checked here. | Tool preference, not a principle. | A:558-590 | passing remark |

### 2.3 Rhythm and asymmetry

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| RA1 | Avoid an even cadence; a "jazzier", uneven rhythm keeps the clip exciting. Viewers feel a predictable beat. | Authored actions. For idles and loops the paper adds: vary causally, not randomly (N1 SY06, N2 RV-F04). Source silent on loops. | Tap the main events: the gaps differ. | A:360-366 | stated principle |
| RA2 | Avoid "twinning": limbs doing the same thing at the same time. Asymmetry adds interest. The only reason she gives for matching arms is that it is easy. | Poses and actions. (inf.) not for deliberately symmetrical or mechanical subjects. | Left and right differ in angle and timing. | A:540-552, A:696-700 | stated principle |
| RA3 | Offset the two feet on a landing so the eye gets two reads: the ground hit, then the catch. | Landings, steps. | One foot lands first; the other keeps travelling. | A:716-724 | example |
| RA4 | Let arms end in different states (one ready, the other following through to relaxed). | Poses with two arms. | Arms differ at the end. | A:694-700 | example |

### 2.4 Arcs

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| AR1 | Give extremities a curved path. A toe path with some parabola helps viewers accept an extreme feat because gravity still seems present. | Leaps, kicks, swings. | Track the toe or hand: a curve, not a flat slide. | A:748-758 | example |
| AR2 | Use one simple, clear line of action through a pose; broken or complex lines hide the action. | Key poses. | One curve runs through spine and limbs; parts follow it. | R:3085-3103 | stated principle |
| AR3 | Reverse the arm's curve between the top and the landing so the arm does not look hunched throughout; sinking elbows sell the landing. | Landings. | Arm curve flips; elbows drop. | A:930-938 | example |
| AR4 | Cooper (2019): most motion follows arcs; breaking an arc can add realism; perfectly clean arcs can look floaty. | Game animation in general. | Paths are curved with some irregularity. | P1:112 | industry practice |
| AR5 | Read each channel in the graph editor as a curve: the up-down channel shows the shape of a jump and exposes broken curves. | Any tool with a curve editor. | A polish aid, not a design rule. | A:192-212 | stated (tool use) |

### 2.5 Silhouette and camera

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| SC1 | Judge motion in the camera the audience gets (scene camera, game camera), not only the working view. | Always. Her game camera sees from a side-top angle. | Capture from the game camera; the action reads. | A:158-162, A:384-388, A:760-766 | stated principle (practice) |
| SC2 | Move limbs to improve the silhouette at the end of a big move. | Big extremities (kick, sweep). | The end shape of the kick is a clear shape, not a bunch. | A:158-162 | example |
| SC3 | Turn the feet so both knees show a shape; a leg pointing straight down the camera is foreshortened and boring. | A mostly fixed side view (inf.). | Both legs read as shapes. | A:760-768 | example |
| SC4 | Keep a character's signature silhouette feature visible even if it breaks left-right continuity. She says this matters more than the correct side, and admits a concept artist might disagree. | Characters with an iconic feature. | The feature is in the outline in every key pose. | A:702-710 | stated principle (hedged) |
| SC5 | Hands matter even where they are tiny: finger splay and a dragging finger pose change the visual profile. | Any camera distance; she says even a top-down game. | Finger shapes change between poses and drag after the hand. | A:916-928 | stated principle |
| SC6 | In motion, players see silhouette, not detail; make parts separable and extremities trackable. | Real-time characters. Second-hand from the 2XKO extract. | Silhouette test passes while moving. | F:346-383 (pointer) | stated principle (second-hand) |

### 2.6 Character and intent

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| CI1 | Game animation has three goals: show the action clearly, make motion and physics believable, give the character personality. | Everything that moves (inf. beyond characters). | A viewer can answer: what happened, does it obey a consistent physics, who did it. | R:2941-2949 | stated principle |
| CI2 | Ask how this specific character does it (a run, a cast), not how anyone does it. | Characters and creatures. | The clip could not be swapped onto another character unnoticed. | R:2993-3009, A:102-104 | stated principle |
| CI3 | Turn personality into two to four adjectives and map each to a visible change (heavy: wider stance; proud: chin up and chest out; noble: wind in the scarf). Pull back when it goes too far. | Pose and motion. | Each adjective has one visible change. | R:3147-3181 | example |
| CI4 | Know the subtext before posing. Choose poses that show the character's two sides; her piece blends a tough kneel with a sweet finger heart. | Acting-heavy clips. | The pose pair reads as one person with two moods. | A:42-52, A:620-622 | stated principle |
| CI5 | Where the character's fantasy is style and flair, choose the cooler move over the practical one. | Stylised heroes. Not for neutral or functional motion. | Pose language matches the character brief. | A:102-106, A:536-540 | example |
| CI6 | Attitude lives in how a body part moves: a determined walk shown through jolting hips; a landing must read confident, not afraid. | Walks, landings, entrances. | Hips, chest and head show the attitude in the main beats. | A:866-878, A:712-716 | example |
| CI7 | The same two key poses can tell different stories; the chosen story drives the in-betweens. A cheap way to offer variants. | Clips with approved poses. | Two takes differ in mood but share the end poses. | A:1052-1068 | example |
| CI8 | Motion sets emotional tone: a very large character's movement can inspire fear, wonder and scale. Consistent physics lets players predict results. | Big creatures, set pieces. | Weight and speed fit the intended emotion and stay consistent across clips. | R:2977-2991 | stated principle |
| CI9 | Act it out (or film yourself, even with stick props weighted like the weapon) before keying. | Any action with a body. For non-body subjects source is silent. | A reference clip or sketch exists and is cited. | A:632-646, R:3012-3046, R:3338-3352 | stated principle |

### 2.7 Secondary motion and overlap

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| SO1 | Animate hair or a tail as one mass first, then offset the child bones by a frame or so, the last one a little more. A cheap way to get life. | Chain parts keyed by hand. N1 FS04-FS06: key, procedural or hybrid is a choice; hand keys are allowed. | Tip lags root; settles after the body stops. | A:984-1024 | example |
| SO2 | A heavy, bulky mass stays springy, like a feather duster, not flowing like hair. | Masses with real bulk. | Bounce, not whip. | A:998-1002 | example |
| SO3 | Secondary parts must read at the key poses (e.g. the ponytail points clearly down at the jump pose), because they are seen only briefly. | Brief poses. | Outline at each key pose shows the part's direction. | A:1004-1010 | example |
| SO4 | Elbows drag behind the motion, and the arm that holds balance stays out a little longer. | Arm-driven moves. | Elbow lags the hand; balance arm lingers. | A:904-908 | example |
| SO5 | Keep secondary motion on variants; removing it lowers perceived value of premium variants. Second-hand. | Skins and variants. | Variant keeps the base's overlap. | B:422 (pointer) | stated principle (second-hand) |

### 2.8 Face and eyes

| id | principle | applies / does not apply | sign in a clip | source | strength |
| --- | --- | --- | --- | --- | --- |
| FE1 | In a fast turn, let the gaze lead: zero the eyes toward where the character should look, then follow with head and body. | Turns and spins. | Eyes arrive before the head. | A:1028-1034 | example |
| FE2 | She closes the eyes through a fast spin because people blink when turning the head, and opens them wide on the way down as a character moment. She calls the first choice counterintuitive. | Her character and camera. Not a universal rule (N1 FS03: at game distance gaze and head can matter more than fine face motion). | Eyelids track the move's effort. | A:1034-1046 | passing remark |
| FE3 | Raise the eyes under the brows for intensity in a ready pose. | Ready and combat poses. | Eyeline lifted under brow. | A:690-694 | example |
| FE4 | Keep the head steady through a turn, as a ballerina spots a point, for balance and stability. | Spins. | Head stays on the target while the body rotates, then snaps round. | A:944-948 | example |

### 2.9 Workflow order and priority of effort

| id | principle | applies / does not apply | sign | source | strength |
| --- | --- | --- | --- | --- | --- |
| WF1 | Quality comes mostly from the root's cadence, good poses, flow and offset. Hair and face are the cherry that lifts a good piece. She quotes a folk saying that good and great differ by about 10%. | Priority of effort. | The clip reads without hair and face; they add appeal, not rescue. | A:970-982, A:1024-1028 | stated principle; the 10% is hearsay she repeats |
| WF2 | Spend the extra time on the hardest transition (the big spin) and go quickly through the rest. | Clips with one hard section. | Notes and passes concentrate on the hard section. | A:222-230 | example |
| WF3 | Do not marry your keys. Layering helps: no polished poses exist yet, so deleting and restarting is cheap. | Stuck sections. | Sections were redone without loss. | A:420-432 | stated principle |
| WF4 | There is no single right method. Principle-by-principle passes (arcs, then eases) are valid but did not work for her. Only the end product matters. | Method choice. This supports "principles, not a recipe". | The reviewer judges the result, not the route. | A:726-748 | stated principle |
| WF5 | Expect three to five tries at one animation; drop precious ideas. | All clips. | Earlier takes exist and a later one replaced them. | R:3314-3336 | stated principle |
| WF6 | Simple, strong basics beat showy moves. Practise one exercise in many moods (heavy, light, happy, sad) to find weak spots. | Learning and review. | Variants of one exercise differ visibly. | R:3364-3390 | stated principle |
| WF7 | A producer, not the animator, ends polishing: work is never finished, only abandoned. | Schedule. | The clip ships at the agreed stop. | A:846-856 | stated principle |
| WF8 | Save often: turn on autosave. | Any DCC session. | A saved file exists. | A:6-12 | stated principle |
| WF9 | The ugly middle is normal: even after many years she doubts it will come together halfway. Cleaning wiggles and knee pops may need a key on every frame. | Mid-production. | The final polish pass follows the ugly middle. | A:1084-1090 | passing remark |
| WF10 | Compare the new take with the earlier version to see what changed. | Revisions. | Side-by-side exists. | R:3229-3233 | stated principle |

## 3. Workflow order (with reasons)

| Step | What | Why (her reason) | Source |
| --- | --- | --- | --- |
| 1 | Prepare: sketch, research, act it out or film yourself; brainstorm with other animators and give notes | Fastest accurate reference; acting shows how the action feels | R:3012-3072, A:632-636 |
| 2 | Pick poses that show the character's subtext | Poses carry personality | A:42-52, A:620-622 |
| 3 | Block the key poses; reuse an existing pose as a start (copy it, flip it, keep its place in the world) | Saves time; keeps ground contact | A:78-82, A:112-122 |
| 4 | Choose a method. Layering: root first, whole body keyed on the same frames, ugly for a long time, then the pieces fall into place. Pose-to-pose: build each full pose, then smooth. The core series teaches key storytelling poses plotted on the timeline | Layering keeps timing easy to move and avoids attachment. Pose-to-pose gives control early. She says either is valid (WF4) | A:84-90, A:434-438, R:3354-3362 |
| 5 | Root and weight first; hold the first pose a little before moving | The root decides where weight goes; a hold prevents an instant departure | A:92-108 |
| 6 | Set the landing target by copying root and feet to the landing frame | Moving those two moves the whole body near where it should land | A:316-322 |
| 7 | Rough the big move, then key time for the whole body together | Timing stays easy to retime | A:132-156, A:434-438 |
| 8 | Make holds as copied pairs | The pause reads as a pause | A:268-284 |
| 9 | Break up the keys so actions start at different times (feet down longer, harder push) | A jump needs a push-off, not a blend | A:590-606 |
| 10 | Replace rough rests with real poses from concept art and the character's actions; add the breakdown ("storytelling") poses | Keyframes are the main beats; breakdowns are how you get between them and may look odd alone | A:520-536, A:950-968 |
| 11 | Polish loop: play, find what feels wrong, fix, play again ("noodly") | Principle-by-principle passes did not suit her | A:726-748 |
| 12 | Details: arms, fingers, head, balance arm, foot offsets | Gives the energy a visible source | A:892-948 |
| 13 | Finish: hair and face | Raises appeal at the end | A:978-1046 |
| 14 | Check in the scene camera, ask peers ("your eyes"), compare with the previous take, let the producer call done | You cannot see your own work; polish never ends | A:384-388, A:782-796, R:3229-3233, A:848-856 |
| 15 | In the game build, a state machine blends and interrupts the clips by game conditions (speed, distance, aim, climbing) | You cannot predict which clip plays; a character is hundreds of interacting clips | R:3237-3301 |

## 4. Mistakes and fixes

| Symptom | Cause | Fix | Source |
| --- | --- | --- | --- |
| Two poses played back twist the body through itself | Plain interpolation between controls in different spaces | Take over the path; add in-betweens by hand | A:64-76 |
| A foot lifts while both feet carry weight | No weight transfer | Shift the root first; show contact | A:456-474, A:662-666 |
| A jump has no visible power | Shoulders and arms static | Move clavicles; push arms up in advance | A:390-404, A:892-904 |
| Body mass pops out of one place | No transfer of energy | Add a counter-arm, catch or lean | A:244-264 |
| Clip feels predictable | Even cadence, twinned limbs | Uneven rhythm; offset limbs | A:360-366, A:540-552 |
| Soft landing, feet scoot | Slow contact, long sink | Faster contact, tighter catch | A:438-446, A:656-660 |
| Flat travel in the air | Toes slide on a line | Give the toe path an arc | A:748-758 |
| Twisted arms | Rotation problems (gimbal) | Key every frame until fixed, or delete and redo | A:420-424, A:906-912 |
| Leg looks dull | Pointing at camera | Turn the feet, show both knees | A:760-768 |
| Fall lacks impact | One or two frames too many | Delete a key before or after contact | A:808-816 |
| Landing looks afraid | Earlier pose carried into the landing | Hold the used controls through the pose, then blend; confident arms and delayed foot | A:710-724 |
| Jump arms look like random flapping | No push before the lift | Pre-push the arms; bend the elbow ahead | A:892-904 |
| Wiggly arm poses, knee pops | Cleanup missing | Key on every frame to flatten wiggles | A:1088-1090 |
| Showy flips before basics | Wish to impress | Slow down, simple basics, mood variants | R:3364-3390 |
| Clinging to a favourite idea | Attachment | Let go; expect three to five tries | R:3314-3336 |
| Bounce feels wrong | Even spacing | Tighten spacing toward the apex | R:3197-3217 |
| Pose action unclear | Broken line of action | One clear curve | R:3099-3103 |
| Awkward balance by accident | Centre off the feet | Move the centre over the support | R:3113-3115 |
| Straight-ahead posing drifts | No planned key poses | Plot key storytelling poses first | R:3354-3362 |
| Hours of work lost | No autosave | Save and autosave | A:6-12 |
| Endless polish | No stop | The producer calls it | A:848-856 |

## 5. Collaboration and timing spine

| Topic | What the material says | Source | Strength |
| --- | --- | --- | --- |
| Design owns length | Animation talks with design so required clips and the right frame lengths are made; (inf.) the animator fits beats inside the length, never the reverse. N1 LM19: the animator never retimes gameplay to fit a clip | A:172-174, E:104 | stated principle |
| VFX runs partnered but staggered behind animation | Effects often lift animation past what animation alone can do | A:166-168, A:174-178 | stated principle |
| Audio comes after animation and must hear about changes | When animation changes, work with audio to get the impact | A:164-166, A:178-180 | stated principle |
| Engineering | Get clips into the engine; needs tools | A:170-172 | stated principle |
| Feasibility early | Animators should join early to say what can and cannot be done, and what more is possible | A:184-190 | stated principle |
| Animation as hub | It sits between tech art and audio, glues other departments; ideally everyone works in the same room | A:162-168, A:180-186 | stated principle |
| Tech art gives controls | Controls move bones intuitively, like puppet strings; they handle planted feet and follow switches | R:2403-2437 | stated principle |
| Model must allow motion | Collars, scarves or armor can block animation, e.g. an arm raise; model, tech art and animator adjust | R:1538-1566 | stated principle |
| State machines are built with engineering | Blends and interrupts depend on game conditions; (inf.) builders must join at the start | R:3237-3301, AC:645 | stated principle |
| Concept art vs silhouette | The animator may differ from the concept on a feature's side for the sake of the silhouette | A:702-710 | passing remark |
| Peer notes | Animators share ideas and give notes while brainstorming | R:3058-3072 | example |
| Producers | They end polishing | A:848-856 | passing remark |
| Telegraphs must tell the truth | Riot 2021: audio cue ahead of time, audio wind-up, hitbox must match the visible effect, a big ground circle can promise more dodging than exists | TD:46, TD:55 | industry practice |
| Minimum lengths are gameplay rules | Riot sets a minimum length for recall animations (the post says at least two seconds); that is a gameplay rule, not an animation choice | GR:21, P1:70 | industry practice |
| Reaction floor | Lab simple reaction about 0.23 s; the games rule of thumb of 0.25 s is a floor for the simplest case, not a target (inference in source) | TD:64, TD:70-71 | study; inference |
| Not stated anywhere | Frame markers, hand-off formats, review stages, sign-off chain and round counts (RX:13, E:116, E:122). From extracts: sound places frame-accurate markers on picture events (RX:41, not re-read) | | silent |

## 6. Non-character motion

The Riot animation material is silent on props, mechanisms, doors, levers, drawbridges, vehicles, mounts, buildings, ambient decoration and loops. Lana's piece is one character action in one camera; the core series is characters and state machines. What can be used comes from neighbouring material.

| Topic | What the material says | Source | Strength |
| --- | --- | --- | --- |
| Held items | Weight reads from how close the prop is to the body's centre of gravity; test with stick props weighted like the weapon. Swing, grip, follow-through and recovery are not covered | R:3121-3133, A:632-636 | example |
| Objects obey consistent physics | Players predict results when physics is consistent; do not break it per effect or clip | R:2977-2983 | stated principle |
| Telegraph before a structure fails | Surface wear, sag, lean and "a moment to react" before a section drops; give a stress state the player can see | P4:67 | industry practice (A tier posts) |
| Collapse silhouette | Shell goes first and a core remains; weight shows as lean before the fall | P4:73 | industry practice |
| Collapse timing | No maker gives crack, hold, fall or settle times. One internal clip of a skyscraper: stands about 3 s, tips as a whole, about 6 s to fall (single clip) | P4:107 | internal note, one clip |
| Check orphans after destruction | Floating leftovers are a repeating bug class | P4:92 | industry practice |
| Scale sets speed | Toy-scale effects run fast; large-scale ones are slowed to sell size; decide scale first | P4:86 | industry practice (film) |
| Perceived weight | People expect heavy things to fall faster and light ones slower; whether an object falls at all changes felt heaviness more than how fast; naive viewers did not clearly prefer true 1 g over constant speed | DF:132-135 | lab studies, not VFX studies |
| Miniature rule | Filming rule for small models: shoot faster by the square root of the scale so motion reads full size (forum, no derivation); at default Roblox gravity everything reads small (inference, untested) | DF:138-139 | tier D, single source |
| Repetition | The first few repeats of an identical effect lose the most punch (inference from one neuroscience paper). Random variety of feedback gave only a small enjoyment gain. No source gives a variant count for effects that fire every second | RE:109-110, P5:61, P5:62, P5:68 | study; gap |
| Too many layers | Redundant feedback helps until it overwhelms; the layer count in the source is the VFX researcher's suggestion | P5:50 | industry practice |
| State machine of a non-character | The core series lists a door-closing beat among its state-machine examples as a joke | R:3301 | passing remark |
| Mechanisms, vehicles, buildings, ambient loops | Silent in all Riot material. (inf.) rely on N1 SL06, SL07 and the paper's phone-cost rows | | silent |
| Server-owned motion vs cosmetic motion | First game: a planned timed-motion system for physical falls looked like phasing and was replaced by engine physics with a body cap | FT:25, FD:92 | tried and failed |

## 7. Rig needs implied (for the rigger)

| Need | Why | Source |
| --- | --- | --- |
| A root or centre-of-gravity control that moves the body while feet stay planted | Weight and root come first | A:92-100, FR:63-73 |
| Head and shoulder controls with a world-space follow option (and a body-follow option) | Keeps balance during spins for free, but makes spins harder; chosen per move | A:132-146, FR:67 |
| Clavicle controls on each side | Shoulders carry energy; frozen shoulders break jumps | A:390-410 |
| Hip control that can sink and tilt | Poses sink into support | A:652-654 |
| Foot roll with heel, ball and toe pivots; knee pole controls | Landings roll through the foot; knees "go crazy" otherwise | A:118-122, A:124-132, A:674-684, FR:69 |
| Finger controls, at least a few shapes | Splay and drag read even when small | A:916-928 |
| Eye bones with a look target or zero position, plus lids | Gaze leads a turn; eyes close and widen | A:1028-1046, FR:52, FR:73 |
| A hair or tail chain with a root-level control and per-bone offset | Animate as one mass, then offset the children | A:984-1024 |
| IK/FK choice per hand with the option to stay FK so a hand does not stick | She stays FK to avoid ground stick | A:912-916, FR:68 |
| Rotation setup that avoids twisting arms (gimbal) | Gimbal problems cost her time | A:906-912, FR:81 |
| Controls grouped; deform bones not keyed; reset to rest exactly | Easy to find, easy to return | FR:61, FR:76-82 |
| Parent switch for held props (hand follows body, world or prop) | Hand-offs between grips | FR:70 |
| Parts that can lag (chains, accessories) | Overlap needs a chain | A:984-1024 |
| Design must leave room for motion (collars, scarves, armor) | Blocks an arm raise | R:1538-1566 |
| Planted foot and "whole leg follows" switches | Tech art controls | R:2403-2437 |
| Animator test of the rig: block a short walk and wave using only the controls, log each friction point | First game: before showing anyone | FR:104-105 |
| Silent | Rig requirements for non-character subjects, mechanisms and vehicles | |

## 8. First-game lessons (universal) and owner words

Universal lessons, stripped of game content:

| Lesson | Source |
| --- | --- |
| Restate the brief before keying: what must the player read, the object's size and material, its personality in two or three adjectives, camera and device, how often it plays, what it interrupts | FA:16 |
| Gameplay timing comes from config and design; the animator never sets it | FA:17 |
| Check that the rig reaches every key pose; report rig changes upstream instead of working around them | FA:21 |
| One card per clip or event: purpose, trigger, key poses with timings, easing, anticipation and follow-through, priority, fade, loop, markers and what each fires, interrupts, adjectives, reference, how to test | FS:62-64 |
| A review checklist of eight: reads at game distance as a silhouette; anticipation before anything that affects the player; weight fits size and material; easing never linear by accident; personality; clean transitions and interrupts; gameplay, sound and VFX fire on markers; motion matches UI, VFX and camera | FS:66-75 |
| Hook gameplay to animation events (the contact frame), not guessed delays | FS:47 |
| A design that blocks motion goes back to the modeller early | FS:48 |
| Test with variants of one move (heavy, light, happy, sad): if they all look the same, timing does no work | FS:38 |
| Judge motion in motion, against a reference clip, not from stills; draw a timing lane per phase before building | FW:13-14, FW:28, FW:114 |
| The `expert-workflows` slot was created for lessons from long expert talks and never filled, so the lessons stayed only in the skill body | FX:1-8 |
| A planned-trajectory motion system for physical falls read as phasing and unpredictable; physics-driven motion read right at the cost of caps | FT:25 |
| Motion that crosses from the world to the screen must read as one connected movement; two disconnected halves failed a play-test | FT:10 |
| An animator-side rig test (block a walk and a wave using only controls) finds control friction before the animator starts | FR:104-105 |

Owner words (verbatim fragments, each kept short; ids from the first game's ledger `decisions.md`):

| Id | Date | Words | Reading for the animator | Line |
| --- | --- | --- | --- | --- |
| D-079 | 2026-10-02 | "it's almost like they phase through each other"; "I wouldn't say things are falling super realistically" | Scripted-looking falls and passing-through read as fake | FD:89 |
| D-082 | 2026-10-02 | "I just know from the real world how physics should act"; "responsive and predictable" | Owner's yardstick for physical motion is predictability | FD:92 |
| D-127 | 2026-10-09 | "I wanted this effect like from 3D to 2D on their screen"; "it just doesn't play the animation" | A hand-off between spaces is wanted; skip it when it adds nothing | FD:137 |
| D-142 | 2026-10-10 | "it looked like they were real parts like scattering out"; "now we recall them too quickly"; "carrying the velocity that it was flying outwards"; "we don't want to clutter the player's screen" | Bursts need believable scatter, the follow-up must not be instant, speed should carry over, avoid clutter | FD:152 |
| D-144 | 2026-10-10 | "fly outward for like a decent amount of time"; "it doesn't feel like they're that connected"; "missing like a lot of polish" | Give each phase readable time; connect the phases | FD:154 |
| D-145 | 2026-10-10 | "we also need some sort of engaging animation"; "juicy animation" | A conversion event deserves a satisfying motion | FD:155 |
| D-184 | 2026-10-12 | "It fits his character really well"; "so that we can animate where the eyes are looking" | Preserve a liked look and test new eye setups side by side; eyes need separate parts to move | FD:194 |
| D-281 | 2026-10-15 | "our sounds, our motion, our art, our UI in cohesion"; "Do we make the player's eyes go to the correct location?" | Motion is reviewed with the other crafts, and the question is where the eye goes | FD:218 |
| D-284 | 2026-10-19 | "I no longer need some sort of mock-up like 2D mock-up" | Judge motion in motion, not from still mock-ups | FD:221 |

## 9. Agreements and conflicts with notes 01 and 02 (spot-check)

| Topic | Riot / this note | Paper note id | Verdict |
| --- | --- | --- | --- |
| Show contacts and weight shifts, do not hide them | A:456-474 | N1 OR06, SL08 | Agrees. Riot adds the burst exception |
| Rhythm, twinning | A:360-366, A:540-552 | N1 SY06; N2 RV-F04 | Partly agrees. Lana treats unpredictability as a goal; the paper warns that random per-channel offsets read as robotic. (inf.) resolve by giving each offset a cause (drag, weight, effort) |
| Blocking method | A:84-90, A:268-284 (no stepped keys) | N2 BL22 (block with stepped poses, render real holds); N1 PR04 | Conflict on stepped blocking; agreement on real, visible holds. She says why: stepped keys hide timing from her. Method is the animator's |
| Silhouette in the game camera | A:158-162, A:760-766 | N1 OR07, GA01, CA04, SL01 | Agrees |
| Anticipation vs responsiveness | R:2957-2971, P1:75 | N1 PR02, GT01; N2 RV-F02 | Agrees. Cooper's longer enemy telegraph is extra; the paper adds the input-response caveat |
| Stylised hang time, overshoot | A:342-352, A:376-384 | N1 SY02, SY03 | Agrees if the style is approved |
| Face and gaze | A:1028-1046 | N1 FS02, FS03 | Agrees. Her eyes-closed spin is a character choice, not a rule |
| Secondary motion | A:984-1024 | N1 PR05, FS04-FS06, RG12 | Agrees; hand keys with offsets are the cheap end of key / procedural / hybrid |
| Gameplay timing authority | A:172-174 | N1 OR08, CT02, LM19 | Agrees |
| State machines | R:3237-3301 | N1 SL02 | Agrees; paper adds entry/exit pose, blend ownership and interrupts |
| Hit-stop | HS:42-53 | N1 CT05, LM19, LM27 | Agrees: a time manipulation with no shared value; Riot-side numbers are tier D or C |
| Numbers | A has no frame counts | N1 LM17-LM20 | Agrees: do not invent |
| Anatomy | A:286-312 | N1 OR03, BO01 | Agrees |
| Weighted tangents | A:558-590 | not in notes | Maya-specific; Blender equivalent for the fact-checker |

## 10. Gap read: what E section A missed

I read all of A (1,100 lines) and R:2896-3420. E's cites held on about twenty spot-checks (within a line or two). Items missing or thin in E:

| Item | Line | Why it matters |
| --- | --- | --- |
| Autosave tip | A:6-12 | Workflow safety; opens the video |
| Her reason for layering: no polished poses means no attachment, so restarting is cheap | A:420-432 | E has "delete and redo" but not the link to the method |
| "No right way; only the end product matters" and principle-checklist passes did not suit her | A:726-748 | Supports principles over a recipe (WF4) |
| Spend more time on the hardest transition, rush the rest | A:222-230 | Effort allocation |
| Set the landing target first: copy root and feet to the landing frame | A:316-322 | Planning step |
| Reuse an existing pose: copy, flip 180, keep world place | A:112-122 | Method detail |
| World-space head and shoulders is a trade-off: free balance but harder spins | A:132-146 | E lists only the benefit |
| Weight sink and a one or two frame hold before the first foot moves; arm out for effort | A:234-242 | Anticipation detail |
| Leg driven by core and root lean | A:258-266 | Cause-and-effect chain (WB7) |
| Land deeper than straight up; hold the bottom; cheap overshoot and the ease-in alternative | A:358-384 | E has overshoot only |
| Spine zeroed and untwisting a spin is hard | A:326-336 | Rig and key hint |
| The tucked V-shape in the air adds the feeling of height | A:530-536 | Pose purpose |
| Jump trajectory: delete flat curves; initial kick then near-linear travel; feet arrive before the body | A:608-618 | Spacing detail |
| Foot roll sequence on landing and weight forward | A:674-684 | Landing detail |
| Arms ready then relaxed at the end; eyes up under the brows | A:690-700 | Pose detail |
| Hold used controls through the new pose to avoid carrying old motion | A:710-716 | Blending fix |
| Arcane walk example: attitude through hip jolt | A:866-878 | Character via body part |
| She stays FK on the hand to avoid ground stick; finger drag pose eased the fall | A:912-928 | Rig and detail |
| Secondary parts must read at the key poses | A:1004-1010 | Overlap rule |
| Zero the eyes toward the look direction first | A:1028-1034 | Gaze leads |
| Time: about a day normally; ugly middle is normal; key every frame to clean pops | A:1082-1090 | Expectation setting |
| E states the 10% good-vs-great split as hers; she repeats it as something many say | A:974-976 | Hedge |
| Weighted tangents as a contested preference | A:558-590 | Tool note |

A-core 3.5 matched R:2896-3420 on every point I checked (three goals, Garen adjectives, ball bounce, state machine list, three to five tries). It adds nothing missing. Not found in any Riot animation material: frame counts, marker names, loops, idles, props, mechanisms, vehicles, review stages.
