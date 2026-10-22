> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. The full principle table behind SKILL.md §4. Sources: animation paper notes `knowledge/reference/animation/01-*.md` (ids OR, GA, PR, BO, SY, SL, CT, FS), `02-*.md` (BL, RV); Riot and first-game note `03-riot-first-game.md` (ids WB, TS, RA, AR, SC, CI, SO, FE, WF; A:<line> = Riot ep4, R:<line> = Riot core series). Tags: [V] verified, [E] expert experience, [O] studio opinion.

# Principles as decisions

**How to use this table.** A principle is a question to ask of the motion, with a sign a reviewer can check. It applies when its "applies" column fits the object; it is not a dial to turn up everywhere (the twelve classic principles are diagnosis names, [V] names AP:59, [O] application AP:61-75). **Method is the animator's choice; only the result is judged** [E] (WF4, A:726-748): layering root-first and pose-to-pose are both valid. Three goals cover all of it [E] (CI1, R:2941-2949): show the action clearly, make motion and physics believable and consistent, give it personality.

## 1. Cause and effect
| ID | Principle | Applies / not | Sign in the clip | Source |
| --- | --- | --- | --- | --- |
| P-01.1 | Before detail, a viewer must read intent, support, force and consequence | everything | a viewer names action, force and result without text | [O] OR01, AP:21 |
| P-01.2 | Energy has a source and a path: pushing parts move first, the ends keep moving after release | anything that makes and releases force (jump, throw, strike, lever pull) | before release, shoulders, arms, hips lead; after release, ends continue | [E] WB7, A:258-266, A:554-558 |
| P-01.3 | Consistent physics lets players predict results; never break it per clip | all objects in one game | the same fall, jump or swing logic in every clip | [E] R:2977-2983 |
| P-01.4 | A mechanism moves like its mechanism (hinge, rail, gear, rope, counterweight); flex only if designed | props, machines, vehicles | a hinge never translates; speed follows the actuator | [O] AP:200-220 mechanical row; SL06 |

## 2. Weight and balance
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-02.1 | Decide where the centre of mass goes first; a limb leaves support only after weight has left it | supported limbed bodies; for flying, wheeled or floating subjects ask what carries the load | root already shifted over the remaining support before a lift | [E] WB1, A:92-100 |
| P-02.2 | Show weight moving between limbs (the most common reel fault); a fast burst still keeps a hint of contact | as above | a contact, lean or catch shows where weight went | [E] WB2, A:456-474 |
| P-02.3 | Mass never vanishes between frames; another part counters or catches it | big fast moves | a counter-arm, a hand on the ground, a lean | [E] WB3, A:244-264 |
| P-02.4 | In a still pose the centre of gravity sits over the feet unless imbalance is the point | holds, key poses | a vertical from the pelvis lands in the support | [E] WB4, R:3105-3119; [O] BO04 (a pelvis proxy is not the true centre of mass with a big tail, wings or a tool) |
| P-02.5 | A held object reads heavier the closer it is carried to the body; far out it reads light | held items, carried props | same prop, two distances, different weight | [E] WB5, R:3121-3133 |
| P-02.6 | Heaviness: wider, lower stance; check it did not go too far. Heavy is a feel, never global slow playback | heavy characters and tools | stance differs between light and heavy versions | [E] WB6, R:3147-3161; [O] AP:323 |
| P-02.7 | Shoulders and hips belong to the pose: clavicles are "the eyebrows of the body"; hips sink | bodies with a shoulder girdle and pelvis | shoulders lift and tighten before a jump; pelvis sinks | [E] WB8, A:390-410, A:652-654 |
| P-02.8 | Landing: fast contact, then the catch; deeper reads stronger; roll through the foot | landings | no scoot after contact; foot rolls; elbows sink | [E] WB9-WB10, A:438-446, A:674-684 |

## 3. Timing and spacing
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-03.1 | Frame distance between keys sets felt speed; while blocking, key the whole body on shared frames and slide keys to feel rhythm | blocking | moving one gap changes the read without changing poses | [E] TS2, A:434-448 |
| P-03.2 | Spacing sells gravity: bunch near the apex, spread on the fall; even spacing on a thrown thing looks wrong | falling, bouncing, thrown things; not constant-speed machines | per-frame positions shrink toward the apex | [E] TS1, R:3197-3217 |
| P-03.3 | A short hold of tightened energy before a spring; feet stay down a little longer for a sharp push | explosive moves | the pop off the ground is sharp | [E] TS3, A:448-456, A:594-606 |
| P-03.4 | Choose interpolation per channel and segment: contacts flat or hand-set, ballistic or mechanical motion its own velocity profile, impacts hard; never ease-in-out every joint | all keyed motion | spacing differs by channel and segment | [O] BL24, AP:646; SY04, AP:385 |
| P-03.5 | Cut a frame at an impact if it feels weak; a small overshoot can release energy | polish of falls, impacts, stand-ups | one frame fewer reads punchier | [E] TS5-TS6, A:376-384, A:808-816 |
| P-03.6 | Stylized hang time: slow top, fast fall, same logic in every jump of the game | approved cartoon or heroic styles | consistent jump arcs across clips | [E] TS4, A:342-352; [O] SY02 |
| P-03.7 | Squash and stretch show inertia and impact, only where the rig and asset contract allow it | stylized bodies | shape follows speed and contact | [E] TS7, R:3219-3227; [O] SY03 |
| P-03.8 | A wind-up is information the player needs; enemy telegraphs can run longer than the player's own anticipation; length belongs to design | anything that threatens or affects the player | a viewer names the attack before contact | [E] TS8, R:2957-2971; [E] Cooper 2019 via P1:75 |
| P-03.9 | Holds keep an idea: freeze, breathing hold, small gaze shift are different tools; stillness is chosen | holds, idles | no motion added only to avoid stillness | [O] SY06, AP:389 |

## 4. Rhythm, asymmetry, arcs, line of action
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-04.1 | Uneven cadence keeps an action alive; viewers feel a predictable beat. Every offset has a cause (drag, weight, effort), never random per-channel noise | authored actions; loops and idles vary causally | the gaps between main events differ, each for a reason | [E] RA1, A:360-366; [O] SY06, RV-F04 (conflict resolved by "a cause per offset") |
| P-04.2 | No twinning: limbs differ in angle and timing; offset the feet on a landing for two reads | poses, actions; not deliberately symmetric or mechanical subjects | left and right differ | [E] RA2-RA4, A:540-552, A:716-724 |
| P-04.3 | Extremities travel on arcs; a parabolic toe path keeps gravity present; breaking an arc can add realism, perfectly clean arcs can look floaty | leaps, kicks, swings, tool tips | tracked paths are curves | [E] AR1, A:748-758; AR4, P1:112 |
| P-04.4 | One clear line of action through a key pose | key poses | one curve runs through spine and limbs | [E] AR2, R:3085-3103 |

## 5. Silhouette and camera
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-05.1 | Judge in the camera the player has, at phone size | always | the game-camera capture reads | [E] SC1, A:158-162, A:760-766; [O] OR07 |
| P-05.2 | Move limbs to improve the end shape of a big move; no leg pointing down the lens | big extremities | clear shapes, both knees visible | [E] SC2-SC3, A:158-162, A:760-768 |
| P-05.3 | A signature silhouette feature stays visible even against left-right continuity | iconic characters | the feature is in the outline at every key pose | [E] SC4, A:702-710 (hedged) |
| P-05.4 | Keep identity across the whole set; a pose can merge an outline into a blob (weapon across the torso, mirror idle, hard twist) | sets, extremes | compare pose families as black shapes | [V] TF2 shapes CA04, AP:107-113; [O] SL01 |
| P-05.5 | Hands and fingers change the outline even when tiny | any distance | finger shapes change between poses | [E] SC5, A:916-928 |

## 6. Character and intent
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-06.1 | Ask how this character does it, not how anyone does | characters, creatures | the clip could not be swapped onto another character unnoticed | [E] CI2, R:2993-3009, A:102-104 |
| P-06.2 | Personality as 2-4 adjectives, each mapped to one visible change; pull back when too far | poses and motion | each adjective has a visible sign | [E] CI3, R:3147-3181 |
| P-06.3 | Know the subtext; the same key poses can tell different stories through the in-betweens | acting clips | two takes share poses, differ in mood | [E] CI4, CI7, A:42-52, A:1052-1068 |
| P-06.4 | Identity can live in movement: stance width, weight placement, limb rhythm, a habitual lean | generic-looking models | recognisable at camera distance as a moving silhouette | [E] CA01, AP:81-87 |
| P-06.5 | Motion sets emotional tone and scale: a huge creature's speed and weight inspire fear and wonder | big creatures, set pieces | speed and weight fit the emotion and stay consistent | [E] CI8, R:2977-2991 |
| P-06.6 | Act it out before keying; film yourself with weighted stick props | any body action | a cited reference exists | [E] CI9, A:632-646, R:3012-3046 |

## 7. Secondary, overlap, face
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-07.1 | Separate active from passive parts; an active tail can lead and turn the body | appendages | active parts lead with intent; passive ones settle | [V] gecko AP:228; [O] OR05, FS04 |
| P-07.2 | Animate a chain as one mass, then offset children; bulky masses stay springy, not flowing | hand-keyed chains | tip lags root and settles after the body | [E] SO1-SO2, A:984-1024 |
| P-07.3 | Secondary parts must read at the key poses; elbows drag; the balance arm lingers | brief poses, arm moves | direction readable in the outline | [E] SO3-SO4, A:904-908, A:1004-1010 |
| P-07.4 | Every secondary motion has a cause; noise is not a cause; never apply it twice (baked lag + runtime spring) | all | named cause per secondary part | [O] BL25, FS06 |
| P-07.5 | Face from intention and attention; gaze can lead a turn; at gameplay distance head and gaze matter more than lips | faces | eyes arrive first; face does not fight posture | [O] FS02-FS03; [E] FE1, A:1028-1034 |
| P-07.6 | Keep secondary motion on cosmetic variants; removing it lowers perceived value | skins, variants | the variant keeps the base's overlap | [E] SO5 (second-hand) |

## 8. Effort and process
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-08.1 | Root cadence, poses, flow and offset make most of the quality; hair and face are the last layer | all clips | the clip reads without hair and face | [E] WF1, A:970-982 |
| P-08.2 | Spend extra time on the hardest transition; go quickly through the rest | clips with one hard section | passes concentrate there | [E] WF2, A:222-230 |
| P-08.3 | Expect 3-5 tries; do not marry keys; delete and redo when stuck | all | earlier takes replaced | [E] WF3, WF5, A:420-432, R:3314-3336 |
| P-08.4 | Test one move in several moods (heavy, light, happy, sad): if they look the same, timing does no work | learning, review | variants differ visibly | [E] WF6, R:3364-3390 |
| P-08.5 | Compare with the earlier take side by side | revisions | a side-by-side exists | [E] WF10, R:3229-3233 |
| P-08.6 | Judge motion in motion, never from still mock-ups | review | review uses playback | owner first game D-284 ("I no longer need some sort of mock-up like 2D mock-up") |

## 9. Non-character objects (where the Riot material is silent, 03 §6)
| ID | Principle | Applies / not | Sign | Source |
| --- | --- | --- | --- | --- |
| P-09.1 | Procedural or code motion still needs a chosen order, a readable arrival and a clear end state; drag explains travel, not ornament | build-ups, transformations, mechanisms | pieces arrive in an order the eye can follow | [V] Fortnite wall CA09, AP:147-153 |
| P-09.2 | Before a structure fails, show stress (sag, lean, wear) and give a moment to react; shell first, core last | collapses | a visible stress state before the drop | [E] P4:67, P4:73 (studio posts) |
| P-09.3 | Scale sets speed: small things move fast, big things are slowed to sell size; decide scale first | destruction, big set pieces | speed fits the size read | [E] P4:86 (film practice) |
| P-09.4 | Felt weight: whether something falls at all changes heaviness more than how fast | falling objects | lab finding, not a preset | [V] lab studies via DF:132-135 |
| P-09.5 | Identical repeats lose punch fastest in the first few repeats; vary what fires often | ambient loops, repeated feedback | copies out of step; small variation | [E] RE:109-110 (inference from one paper) |
| P-09.6 | Physical motion should read responsive and predictable; scripted-looking falls and passing-through read fake | anything that falls, scatters or collides | owner yardstick | owner first game D-079, D-082 ("I just know from the real world how physics should act"; "responsive and predictable") |
| P-09.7 | Each phase of a burst gets readable time; phases connect; do not clutter the screen | multi-phase object events | phases readable and linked | owner first game D-142, D-144 ("it doesn't feel like they're that connected") |
