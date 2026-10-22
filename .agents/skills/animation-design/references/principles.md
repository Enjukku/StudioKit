> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. The full principle table behind SKILL.md §4. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence for each row: animation paper notes `knowledge/reference/animation/01-*.md`, `02-*.md`, `03-*.md` and the craft library `knowledge/reference/craft/riot/` (weight-timing, exaggeration, rhythm, shape-silhouette, character-design). Numbers marked PROPOSAL are starting values a check may change.

# Principles as decisions

**How to use this table.** A principle is a question to ask of the motion, with a sign you can check in a render, a capture or the sampled curves. It applies when its "applies" column fits the object; it is not a dial to turn up everywhere (the classic principles are names for diagnosis). **Method is your choice; only the result is judged:** layering from the root and pose-to-pose are both valid. Three jobs cover all of it, in this order: show the action clearly, make motion and physics believable and consistent, give it personality. "A fresh viewer" in a sign means a fresh read, run as `review.md` §8 defines it; a sign that needs motion at normal speed goes to the owner as a playable preview at the next gate (`review.md` §1 item 5).

## 1. Cause and effect
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-01.1 | Before detail, a viewer must read intent, support, force and consequence | everything | a viewer names action, force and result without text |
| P-01.2 | Energy has a source and a path: the driving part moves first (a leg powered from the core, arms thrown up to lift a jump), the rest follows, and the ends keep moving after release | anything that makes and releases force (jump, throw, strike, lever pull) | in the samples, the driver's curve leads the root's; before release shoulders, arms, hips lead; after release the ends continue |
| P-01.3 | One physics for the game: the same gravity, jump arc and impact weight in every clip, prop and code-driven motion, so players can predict results | all objects in one game | root height curves of every jump and fall match the declared language; an outlier has a recorded reason |
| P-01.4 | A mechanism moves like its mechanism (hinge, rail, gear, rope, counterweight); flex only if designed | props, machines, vehicles | a hinge never translates; speed follows the actuator |
| P-01.5 | Ask three questions of every clip: what is happening (clarity), does it feel physically right (belief), could it be any other character (personality) | every clip | the review answers all three with a yes / no and a frame |

## 2. Weight and balance
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-02.1 | Decide where the centre of mass goes first; a limb leaves support only after the weight has left it | supported limbed bodies; for flying, wheeled or floating subjects ask what carries the load | on the frame a foot lifts, the root's ground projection sits over the other support |
| P-02.2 | Show the weight moving between limbs (the most common fault in reels); a fast burst still keeps at least one frame of contact that shows where the weight went | as above | a contact, lean or catch shows where the weight went; mistake: standing on both feet, then a foot just moves |
| P-02.3 | Mass never vanishes between frames: when a big mass swings to the other side, a breakdown shows it travel; ask at every big change "where does this weight go?" | big fast moves, spins | a black-fill strip of consecutive frames shifts smoothly; no frame where a large volume pops from one side to the other |
| P-02.4 | In a still pose the centre of gravity sits over the feet unless imbalance is the point | holds, key poses | a vertical from the estimated centre of mass lands in the support (a pelvis proxy is not the true centre with a big tail, wings or a tool) |
| P-02.5 | A held object reads heavier the closer it is carried to the body; held far out it reads light; heavy loads add a counter-lean | held items, carried props | side view: the item's distance from the torso matches its weight class |
| P-02.6 | Heaviness: wider, lower stance, longer settle; check it did not go too far. Heavy is a feel, never global slow playback | heavy characters and tools | stance differs between light and heavy versions; playback speed is 1 |
| P-02.7 | Shoulders and hips belong to every action: the shoulders lift and tighten before a jump or throw (they supply its energy and range), the hips tilt on every weight shift and let a pose sink. On a standard Roblox body without collarbone joints, put that energy into the upper torso and upper arm | bodies with a shoulder girdle and pelvis | shoulder (or upper-torso) and hip channels are not constant through an action clip; mistake: arms swing up with frozen shoulders |
| P-02.8 | Landing: fast contact, then the catch; land low into a strong pose, hold the bottom a little, rise; do not sink so far it looks loose; elbows sink on landing; roll through the foot | landings | root height at landing dips clearly below standing, not past the stance limit; elbows drop on the landing frames; no scoot after contact |
| P-02.9 | A counter-effort makes a fast move believable: an arm reaching the other way, a hand touching the ground for a few frames | large fast swings, spins, swoops | in the key frames a counter-limb moves opposite the swinging limb and is visible from the game camera |
| P-02.10 | Momentum carries through poses: swing out of one pose into the next; arrive with a small overshoot and settle rather than stopping dead | action chains | arriving at a pose, the motion decelerates over several frames, not one |

## 3. Timing and spacing
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-03.1 | Frame distance between keys sets felt speed; while blocking, key the whole body on shared frames so retiming is moving keys | blocking | moving one gap changes the read without changing poses |
| P-03.2 | Spacing sells gravity: bunched near the apex, spread on the fall; even spacing on a thrown thing looks wrong | falling, bouncing, thrown things; not constant-speed machines | per-frame distance near the apex is smaller than near the ground |
| P-03.3 | A short hold of tightened energy before a spring (PROPOSAL: about 2 frames at 30 fps for the player's own move); feet stay down a frame or two longer than the root, then a sharp exit | explosive moves | feet leave 1-2 frames after the root starts rising; the root leaves the bottom steeply; mistake: a long coiled hold before the player's own push-off |
| P-03.4 | Choose interpolation per channel and segment: contacts flat or hand-set, ballistic or mechanical motion its own velocity profile, impacts hard; never ease-in-out on every joint | all keyed motion | spacing differs by channel and segment |
| P-03.5 | Contact comes fast; when a section feels weak, delete one frame at a time until it hits; then shift the feet a frame after | falls, impacts, stand-ups | frames from first contact to full weight drop between takes; the impact marker equals the contact frame |
| P-03.6 | Stylized hang time: a short hold near the apex, then a fall faster than the rise; the same logic in every jump of the game; agree it with the game-designer when the jump is gameplay | approved cartoon or heroic styles | the root height curve flattens at the apex and the descent is shorter than the ascent |
| P-03.7 | Squash on contact and stretch on speed, by a Roblox route (SKILL.md §5), keeping volume | stylized bodies and props | the contact and peak-speed frames read stronger than a take without it |
| P-03.8 | A wind-up is information. Size it by who reacts: an enemy's tell is a distinct pose held for the designer's reaction window (longer for bigger attacks; never shorter than the window); the player's own anticipation is short and tight so the move feels strong and responsive | anything that threatens or answers the player | a viewer names the attack before contact; tell frames counted at 30 fps match the window |
| P-03.9 | Holds keep an idea: freeze, breathing hold, small gaze shift are different tools; stillness is chosen | holds, idles | no motion added only to avoid stillness |
| P-03.10 | Keys tell the story, breakdowns decide how you get there: two keys and "play" is a straight blend that twists the body through itself; place every breakdown (head leads, arms follow) and accept a breakdown that looks awkward alone if the flow is right | every clip | no clip has only start and end keys; frame-stepped, no limb passes through the torso and no knee inverts |
| P-03.11 | Do not stall travel in the air: after the kick-off, horizontal travel keeps going; the feet slightly beat the body to the landing spot | jumps, leaps, dashes | the root's horizontal curves have no plateau during flight |
| P-03.12 | Lock the first pose a few frames before motion starts in showcase, emote, idle and cutscene clips (PROPOSAL: about 5 frames at 30 fps); gameplay actions keep it to what the input-response budget allows | clips the viewer must register first | the first frames have a pose change near zero |
| P-03.13 | The lengths of the wind-up and the follow-through set felt weight: a longer follow-through reads as hitting through something heavy; a longer wind-up reads as a bigger, more telegraphed attack | strikes, impacts | light and heavy versions differ in follow-through frame count; a fresh viewer ranks the longer one heavier |

## 4. Rhythm, asymmetry, arcs, line of action
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-04.1 | Uneven cadence keeps an action alive; viewers feel a predictable beat. Every offset has a cause (drag, weight, effort), never random per-channel noise | authored actions; loops and idles vary causally | the gaps between main beats differ (list them in frames); if every gap is within a frame of the others, it is a metronome: retime |
| P-04.2 | No twinning: paired limbs differ in angle and time; offset the feet on a landing for two reads (hit the ground, catch the weight) | poses, actions; not deliberately symmetric or mechanical subjects | left and right keys do not share every frame; key poses are not mirror images |
| P-04.3 | Extremities travel on arcs; a parabolic toe path keeps gravity present; a deliberate corner only at an impact; perfectly clean arcs everywhere can look floaty | leaps, kicks, swings, tool tips | tracked paths curve; a straight run of more than a few frames is a missing breakdown |
| P-04.4 | One clear line of action through a key pose; spine, limbs, weapon, hair and cloth follow it; in a held pose (hit pause, promo still: P-06.11) a few committed flow lines (hair, cloth, a trail) continue it | key poses | one curve runs through spine and limbs; no competing lines |
| P-04.5 | Every action is a short story: a beginning (the tell and build), a middle (the hit) and an end (the result and settle); none simply starts or stops | actions, reveals, mechanisms | the three beats are visible and distinct in a frame-step |
| P-04.6 | Lean into the action: tilt the body and the key shapes along the direction of travel; a static, boxy pose reads slow | dashes, attacks, runs | most diagonals of the key pose point the way the action goes |

## 5. Silhouette and camera
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-05.1 | Judge in the camera the player has, at phone size, moving, in the real place | always | the game-camera capture reads |
| P-05.2 | Move limbs to improve the end shape of a big move; no leg pointing down the lens (it foreshortens into a stub); turn feet or torso a few degrees toward profile | big extremities | both knees and the extended limb read as separate shapes in black-fill |
| P-05.3 | A signature silhouette feature (ponytail swoop, cape edge, weapon) stays visible at the held moments (key poses, hit pauses), even against left-right continuity or physical exactness | iconic characters | the feature is in the outline at every key pose and hit pause |
| P-05.4 | Keep identity across the whole set; a pose can merge an outline into a blob (weapon across the torso, mirror idle, hard twist, a drape across the arms) | sets, extremes | compare pose families as black shapes; the arm outline stays separate from the torso in idle, run and attack |
| P-05.5 | Hands and fingers change the outline even when tiny: energy flows out through the palms to the fingertips at the top of a move; fingers splay on contact and drag on falls | any distance | hand shapes change between key poses; without finger joints, use bigger hand-pose changes or a hand-mesh swap |
| P-05.6 | Give a jump apex a pose: legs tucked into a V, knees up, toes pointed; dangling legs are no pose | jumps, leaps, aerial emotes | black-fill at the apex frame shows the V |
| P-05.7 | The source of power is the primary read: the blade, the casting hand, the jaw is the clearest, least-covered part at the key pose and the contact | attacks, abilities | at the contact frame the source of power separates from the body in black-fill |
| P-05.8 | Body shape predicts movement: a heavy silhouette stomps, a slim one darts; motion and model agree | characters, creatures | a fresh read of the model's black-fill predicts the motion style the set uses |
| P-05.9 | Overlapping parts of the same colour merge in motion (red gloves in front of red hair); key poses avoid stacking them, or the art director changes a colour | key poses with overlap | in the shaded key frame, overlapping parts still separate |
| P-05.10 | A group has its own silhouette: stage group emotes and cutscene groups so the combined outline tells the beat | group emotes, cutscenes, lobbies | black-fill of the group at phone size reads as the idea (a team, a ring of threats) |

## 6. Character and intent
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-06.1 | Ask how this character does it, not how anyone does; in a stylish context flair beats practicality | characters, creatures | the clip could not be swapped onto another character unnoticed |
| P-06.2 | Personality as 2-4 adjectives, each mapped to one visible change (heavy: wider stance; proud: chin up, chest out); push, then pull back when it goes too far | poses and motion | each adjective has a visible sign; weight is still believable after the push |
| P-06.3 | Know the subtext; the same key poses can tell different stories through the in-betweens and timing | acting clips | two takes share poses and differ in mood |
| P-06.4 | Identity can live in movement: stance width, weight placement, limb rhythm, a habitual lean | generic-looking models | recognisable at camera distance as a moving silhouette |
| P-06.5 | Motion sets emotional tone and scale: an enormous creature moves slowly, with long settles and heavy contacts; a giant at human speed reads small | big creatures, bosses, set pieces | stride period and settle length exceed a normal-size character's; a fresh viewer names the intended emotion |
| P-06.6 | Act it out before keying: agents write the performance as a beat sheet (motion, time, sound word, subtext) and gather real motion reference | any body action | a beat sheet and a cited reference exist before the first key |
| P-06.7 | Comedy comes from contradiction: pose against the character's known trait, in the whole body, not only the face | comic emotes, event and promo poses | told the normal trait, a fresh viewer reads the joke from a game-distance capture |
| P-06.8 | Emotes and reactions seen for about two seconds at small size get maximum expression | emotes, reactions | shown for 2 s at real player size, a fresh viewer names the intent |
| P-06.9 | A variant may twist the tone (darker, sillier) within bounds; a darker version keeps its poise and appeal | variant clips | the pushed version still reads aspirational or likeable |
| P-06.10 | An enemy's movement pattern is its character (hop, dash-and-stop, shamble, grid steps); distinct patterns keep a crowd readable | enemy types | as plain blocks, a fresh read (`review.md` §8) tells the enemies apart by movement alone |
| P-06.11 | A promo, thumbnail, splash or cutscene still of a character starts from the brief's one-sentence premise (the moment it shows) and reuses the signature ability's key pose from the set, with its line of action and hook shapes, staged for that premise. A new generic pose with no link to play is not the character | promo, marketing and cutscene stills of a character | the still's pose, rendered black-fill at the game camera, overlaps the clip's key frame (`look_check.py silhouette --compare`, MEASURED) or the difference is recorded with its reason; a fresh read of the still names the premise |

## 7. Secondary, overlap, face
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-07.1 | Separate active from passive parts; an active tail can lead and turn the body | appendages | active parts lead with intent; passive ones settle |
| P-07.2 | Animate a chain as one mass, then offset its children (PROPOSAL: one frame per bone down the chain, two on the last); bulky masses stay springy, not flowing | hand-keyed chains: hair, tails, straps | tip lags root and settles after the body; a heavy ponytail settles fast instead of flowing like a feather duster |
| P-07.3 | Secondary parts must read at the key poses; elbows drag; the balance arm lingers | brief poses, arm moves | direction readable in the outline |
| P-07.4 | Every secondary motion has a cause; noise is not a cause; never apply it twice (a baked lag plus a runtime spring) | all | a named cause per secondary part |
| P-07.5 | Face from intention and attention: gaze and head direction are part of the pose from blocking; at gameplay distance they matter more than lips. In a look-turn the eyes lead, then the head, then the body; the face never fights the posture. In a spin or fast body turn the head can hold its world direction, then turn late and fast. Eyes close in a fast spin and on a fast head turn, widen on a fall, look from under the brows on an intense beat | faces, heads | look-turns: eye and head yaw start before the chest's; spins: head world yaw lags the chest's, then catches up fast; blinks sit on fast turns |
| P-07.6 | Secondary motion signals value: a cosmetic variant keeps the base's overlap and flourishes; removing them makes it feel cheaper | skins, variants, premium items | the variant has no fewer secondary sources than the base |

## 8. Effort and process
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-08.1 | Root cadence, poses, flow and offsets make most of the quality; hair, fingers and face are the last layer | all clips | the clip reads without hair, finger and face keys |
| P-08.2 | Spend extra time on the hardest transition; go quickly through the rest | clips with one hard section | passes concentrate there |
| P-08.3 | Expect 3-5 tries; do not marry keys; when a section misbehaves, clear its keys and re-key it | all | earlier takes replaced; the log says rebuilt, not patched |
| P-08.4 | Calibrate on basics: one simple move in several weights and moods (heavy, light, happy, sad); if they look the same, timing does no work | learning, review | a viewer tells the variants apart without labels |
| P-08.5 | Compare with the earlier take side by side, same camera | revisions | a side-by-side exists |
| P-08.6 | Judge motion in motion, never from still mock-ups: a still shows a pose, not timing | review | timing is judged from sample numbers and frame strips at a known rate; feel at normal speed by the owner on a playable preview at the gate |
| P-08.7 | One named problem per pass: look, find what feels worst, fix that, look again; a checklist backs this up but the result decides | every pass | the pass log names one problem and its before/after |
| P-08.8 | Read the curves behind the motion: per control and axis, spikes are pops, flips are gimbal, flat runs are stalls | spline and polish | sampled curves show no unintended jump, flip or plateau |
| P-08.9 | Shape eases with handles, not extra keys; fewer keys are easier to read and change | spline | key count per control stays low; no bumps from added keys |
| P-08.10 | Fix rotation flips at the source: key through them on ones, or change the rotation mode, before export | spins, arm twists | no sudden rotation jump in the samples |
| P-08.11 | Find a number by bracketing: a too-low and a too-high take, then pick between. Compare the takes in sample numbers first; render only the frames that decide, inside the plan-stage budget (`review.md` §5) | hold lengths, drop depths, overshoots | the hand-back shows the tried values and why one won |
| P-08.12 | Park a stuck part, work on another, come back with fresh eyes | any part that will not come right | the log shows the part revisited, not abandoned |
| P-08.13 | Decisive keys: a few bold pose changes, not dozens of micro-tweaks on the same frames | blocking, polish | key poses change in clear steps between takes |

## 9. Non-character objects
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-09.1 | Procedural or code motion still needs a chosen order, a readable arrival and a clear end state; drag explains travel, not ornament; the end state explains the change even with no motion | build-ups, transformations, mechanisms | pieces arrive in an order the eye can follow; a still of the end state reads |
| P-09.2 | Before a structure fails, show stress (sag, lean, wear) and give a moment to react; shell first, core last | collapses | a visible stress state before the drop |
| P-09.3 | Scale sets speed: small things move fast, big things are slowed to sell size; decide scale first | destruction, big set pieces | speed fits the size read |
| P-09.4 | Felt weight: whether something falls at all changes heaviness more than how fast | falling objects | a measured finding, not a preset |
| P-09.5 | Identical repeats lose punch fastest in the first few repeats; vary what fires often; frequent motion is shorter and quieter | ambient loops, repeated feedback | copies out of step; small variation; an every-second motion stays brief |
| P-09.6 | Physical motion should read responsive and predictable; scripted-looking falls and passing-through read fake | anything that falls, scatters or collides | owner yardstick |
| P-09.7 | Each phase of a burst gets readable time; phases connect; do not clutter the screen | multi-phase object events | phases readable and linked |
| P-09.8 | A burst reaches most of its size fast and eases into its end; linear growth reads flat | pops, opening lids, spawning props | sampled size or angle is steep at the start and flat at the end |
| P-09.9 | A build-up rises (smaller to bigger, slower to faster) and the gathering motion converges on the source before the release | charging mechanisms, power-ups, reveals | motion tracks toward the focus during the build; the release frame is shared with VFX and sound |
| P-09.10 | A prop or a place has a personality in 3-5 words, and its motion follows it ("rigid, old, grinding" vs "light, bouncy") | doors, machines, signature props | a fresh viewer describes the prop's personality from a capture |
| P-09.11 | Backdrop motion has an elegant gesture and stays calm: a plant's sway follows its curve; ambient motion is slower and smaller than anything near a sightline | plants, banners, ambient loops | ambient motion is never the fastest or brightest motion near the play space |

## 10. Exaggeration
| ID | Principle | Applies / not | Sign in the clip |
| --- | --- | --- | --- |
| P-10.1 | Game motion is larger than life: push the poses and timing that must read past real, because small, fast, glanced-at motion loses subtlety | everything the player must read | side by side with an unpushed take at game size, the pushed one changes the outline |
| P-10.2 | A believable base earns the extremes: contacts, weight shifts and arcs follow physics closely enough that one or two pushed moments (hang time, a smear, an unnatural hold) are believed | every exaggerated clip | each extreme moment is surrounded by correct contact, shift and arc; no reverse bends at elbows or knees |
| P-10.3 | Break only the joints that can take it: stretch and smear along a limb in the direction of travel for one or two frames (in Roblox, through a trail or a mesh swap, never a scaled part in a clip) | fast swings, dashes | the smear follows the motion path and is gone within a couple of frames |
| P-10.4 | A small overshoot releases energy: pass the final value once, then settle; an ease-in is the calmer alternative | stand-ups, pops, landings, code-driven pops (Back or Elastic easing) | the curve crosses its final value once, small, then settles |
| P-10.5 | Spend exaggeration on the signature moments; exaggerating everything leaves nothing believed | sets | the clip card names its one or two pushed moments |
