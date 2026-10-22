> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Rebuilt by J018 maker animator · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Evidence: animation paper notes `knowledge/reference/animation/02-*.md` (review, gates, do-not list); the craft library `knowledge/reference/craft/riot/` (critique-feedback, weight-timing, exaggeration, rhythm, shape-silhouette, process-iteration). Owner rule J005-D8 (light checks). This is the self-review the animator runs before every hand-back: §8 holds the lines per pass.

# Review: judge the read, then the defects

## 1. Order
1. **Read first:** at the game camera, at phone size, moving, in the real place: can a viewer name the subject, goal, direction, key contact, force and result without text? Is it the approved character? Then the three questions: what is happening, does it feel physically right, could it be any other character?
2. **Silhouette:** the key frames as black-fill at the game camera: one line of action, the source of power and the hook shapes in the outline, limbs separate.
3. **Then defects** (§2, §8). Separate approved exaggeration from accidents; record disagreement instead of a false consensus.
4. **Views:** the game camera at phone size first; then side and front diagnostics; with and without effects; with reduced motion; the final context with other players and HUD.
5. **Speeds:** normal speed first (a clumsy still can be a good transition; a handsome contact sheet can hide a dull rhythm), then slow, then frame by frame at events. Slow playback finds problems but never proves feel: re-check every retime at normal speed. You see stills (Blender renders, Studio MCP captures): judge timing from the sample numbers (beat gaps, spacing, B-07, S-07) and frame strips at a known rate; a pick between timing takes, and any feel judgement at normal speed, goes to the owner as a playable preview (`animation-craft/references/blender-keying.md` §7). An agent reviewer at a check-in sees stills too: it judges takes by the same beat-gap numbers and frame strips. Until the owner watches the previews at the next gate, the take with the better recorded reasons is used and marked PROPOSAL, and both previews go into the gate packet.
6. **Curves:** read the sampled curves per control and axis, not only the picture: spikes, flips and plateaus show where the eye misses them.
7. **Delivered asset:** judge the imported Roblox result, not only the Blender preview.

## 2. Pass / fail checklist (the concrete lines are in §8)
| ID | Test | Pass | Fail |
| --- | --- | --- | --- |
| R-01 | Intent and personality | viewer names the action and the approved character quality | gesture contradicts the brief, needs explaining, or could be any character |
| R-02 | Part identity | every animated part has a label and a driver | an unknown part moved by generic noise |
| R-03 | Contact | planted or gripped parts stay attached within the approved tolerance | foot slide, grip separation, unexplained penetration |
| R-04 | Support and weight | support and force explain acceleration and recovery; weight shifts before lifts | weightless launch, unsupported stop, no reaction, a mass that pops |
| R-05 | Arcs and spacing | paths and spacing serve anatomy, force and style | accidental corners, one ease everywhere, pops, stalled travel |
| R-06 | Joint and mesh integrity | within verified range; deformation acceptable | knee or elbow inversion, collapsing volume, broken fold, a body twisting through itself |
| R-07 | Secondary causality | lag, correction and settle have causes | all parts in phase, or a generic delayed wave |
| R-08 | Tools and props | grip, pivot, collision, path and consequence agree | tool feels detached, hinge translates, impact has no response |
| R-09 | Loop seam | pose and velocity continuous, or an approved break | pause, pop or drift at the repeat |
| R-10 | Transition and interruption | required paths keep contacts and clean up | residue, stale trails, stuck grips, no recovery |
| R-11 | Gameplay timing and truth | visible threat and result agree with the windows; tells fit the reaction window; reach matches the hit area | the picture implies a range, damage or success that is not there |
| R-12 | Export fidelity | imported poses, events and length match the approved preview | lost action, changed scale, retimed contact, missing channel |
| R-13 | Runtime | priority, blending, authority and replication as designed | other clients disagree; unrelated joints overridden |
| R-14 | Cost | the agreed phone scene passes measured frame and memory goals | only a desktop or single-asset test passes |
| R-15 | Owner approval | the current revision is approved, open issues disclosed | approval of an older revision |
| R-16 | Silhouette and read | every key pose reads as a black shape at the game camera at phone size | a key pose is a blob, a stub or needs colour, effects or camera to read |
| R-17 | Every player | tells and outcomes read with effects hidden, colour removed and the reduced-motion path (no shake, flashes or camera effects) | the read lives only in an effect, a colour or the camera |

**Tolerances first:** a numeric check passes or fails only against a tolerance set in units, camera and method. With no tolerance, report the measurement as MEASURED, never PASS.

## 3. Common failures: first check
| Symptom | Check first |
| --- | --- |
| Floaty, linear | spacing, support, contact and braking before adding keys; computer in-betweens left alone twist the body |
| Body twists through itself | only two keys with a straight blend between: add breakdowns for root, feet and arms |
| No anticipation | does a responsiveness rule explain it? If not, add a readable cue inside the approved timing |
| Unfair attack | the tell is no distinct pose, or shorter than the reaction window: fix the pose and ask design for the window |
| Foot moves without a weight shift (the most common reel fault) | add the weight shift or a contact |
| Jump has no energy source | shoulders and hips still: add the shrug, the hip tilt and the arm push |
| Jump stalls in the air | flat horizontal root curves in flight: remove the plateau keys |
| Soft, scooting landing | make the contact faster; delete frames until it hits; tighten a landing that sinks too far |
| Hit feels mushy | contact not fast, no single peak frame, follow-through too short, or the freeze frame is a weak pose |
| Pose reads as a blob | black-fill it: rotate limbs off the body, turn the leg out of the lens, clear the source of power |
| Robotic timing, twinning | spacing and accents of events; offset limbs; uneven cadence, not random per-channel offsets |
| Generic, could be anyone | no visible sign of the feel words; push one change per adjective |
| Giant reads small | human-speed timing: slow the beats, lengthen settles, weight the contacts |
| Bad arcs | plot world-space landmarks; check the reference and the camera |
| Weightless tool | grip, support shift, tool acceleration, distance from the body, body reaction after impact |
| Stiff tails or wings | rethink the anatomy and which part drives which |
| Gimbal-twisted arm | key it through on ones, or delete and redo |
| Too many keys or bones | reduce only after measuring what the removal does |
| Leg pointing down the camera | turn it so the knee shows; foreshortening reads as boring |

## 4. Writing a finding
- Tie every remark to a time and visible evidence ("left foot drifts 0.3 studs during declared support, frames 12-18, side view"). No "add life". A proposed change names the channel or body group, the event interval, the intended result for the viewer and the regression to check.
- Ask a goal question, never "do you like it?": "which take reads as heavier at phone size?"
- A note that carries a solution ("make it slower") hides a problem ("it doesn't feel heavy"): restate the problem in one line and solve that; re-check the problem after the fix, not only that the suggestion was made. Say whether a note is about the goal or the tactic.
- A visual note is a marked capture or a posed proxy of the fix, before and after, not words alone.
- One named problem per pass: find the worst, fix it, look again.
- The hand-back maps each note to done or questioned, and names at least one honest weakness with its next step, or says why there is none.

## 5. Light checks (owner J005-D8; `rig-pipeline` §4a)
- Numbers for every clip (`tools/anim/clip_check.py`: loop seam, contact slide, length against the window, events against the timing list, ROM against the control manifest, pops) plus the sample-curve lines of §8 (computed from the same samples file).
- Images only when a number fails, plus at most 8 key frames per action: the tell, the accent or contact, the extremes, the loop seam, from the game camera and one close view. Render those frames once, shaded and as black-fill from the same pass (`animation-craft/references/blender-keying.md` §7); `tools/art/look_check.py silhouette` measures the black-fill, so the silhouette lines cost no extra images.
- In-game: at most 8 Studio captures per action (the same key moments), plus one with effects hidden and one in grayscale.
- One full check per hand-off, by the receiver; the full image set once, at release.
- **Plan-stage images are making, not checks, and have their own budget:** one black-fill contact sheet per key clip at phone size with all key-pose options tiled on one image; timing takes, a pre-push frame and a bracket are judged from sample numbers first and rendered only for the frames that decide; a playable preview is for the owner to watch at the gate, not frames you inspect. Report their count with the check images.
- Report how many renders were made and how many images were looked at.
- Say what each input can prove: a still shows a pose, not timing; a frame sequence at a known rate shows timing; sound sync needs a device capture with audio. A check whose input cannot show it is "not verified", never PASS; end with a could-not-check list.

## 6. When to stop polishing
The approved revision is done when R-01 to R-17 pass or carry owner-approved exceptions and the brief's stop criteria hold. The brief states a pass budget and the stop criteria before work starts. A review round that only repeats earlier notes means it is close; small pops most players will not see are logged, not chased; the lead and the owner call it done. When a part will not fix, delete its keys and redo it.

## 7. Do not do
Deduce species or mass from bones · paste a bird wing cycle on a bat · invent timing or budget values · equate more keys, bones, simulation or AI output with better animation · let effects cover a missing contact · overwrite an approved clip without keeping the old revision and its event contract · treat a preview render as proof of import, replication or phone cost · ship unreviewed generated motion · replace owner approval with a score · approve a frequent motion from a single trigger.

## 8. Self-review lines by pass
Run the lines of the pass you are at before its hand-off or check-in; write each as PASS, FAIL, MEASURED or not verified, with its evidence. **Input:** N = numbers from the samples file or `clip_check.py` (every clip); K = the ≤ 8 key frames (shaded + black-fill, game camera); C = Studio captures. Lines that do not apply to the clip are marked n/a with the reason. A starting value marked PROPOSAL may be changed by bracketing; the change is recorded. **A fresh read** ("a fresh viewer", "a tester" in these books): write what you read from the black-fill or capture before you open the brief, the clip name or your notes, then compare; at the check-in the reviewer repeats it blind. For a second look, mirror the frame (a one-line image flip) and read it again.

### 8a. Blocking pass (before the check-in, before any spline)
| ID | Look for | In |
| --- | --- | --- |
| B-01 | The root-only preview already reads the action (rise, hang, fall, settle); the root height curve shows one clear rise and fall with holds where intended | K, N |
| B-02 | Each key pose has one line of action; a fresh read of its black-fill at phone size names the action | K (`look_check.py silhouette`, `thumb --size`) |
| B-03 | The source of power and every listed hook shape are in the outline at each key pose and hit pause; hands, head and feet separate from the body | K |
| B-04 | No limb aims down the lens; both knees and the extended limb read as separate shapes | K |
| B-05 | In each still key pose the centre of gravity sits over the support, or the brief says why not (side view) | K |
| B-06 | An enemy's tell is a distinct pose held at least the designer's reaction window (frames at 30 fps vs window); the player's own tell is short and tight | N |
| B-07 | Tell, build, beat, hit and result are labelled with frames; the result starts after its cause; the gaps between main beats are not all equal | N |
| B-08 | The accent sits on the gameplay event; the clip length fits the window unchanged (`clip_check.py` length with the window) | N |
| B-09 | Holds are real holds (copied key pairs, flat between) and the preview runs with normal interpolation, not only stepped | N |
| B-10 | Showcase, emote, idle and cutscene clips hold the first pose a few frames (PROPOSAL: about 5 at 30 fps) before moving; gameplay clips stay within the response budget | N |
| B-11 | The clip card names its one or two pushed moments; each pushed frame differs from the same frame before the push (kept from blocking) in `look_check.py silhouette --compare` | K (plan budget) |
| B-12 | Key clips: 2-3 key-pose options at equal finish on one contact sheet, and two timing takes compared by their beat gaps; the pick and its reasons are recorded (the timing take used until the owner picks on the previews at the next gate is marked PROPOSAL) | job record |
| B-13 | Emotes and reactions: shown for 2 s at real player size, the intent is named; a comic pose contradicts the known trait in the whole body | K |
| B-14 | When the set has another character's run or idle: the key-frame black-fills already rendered for each are told apart by a fresh read, which names each one's feel words (no new images) | K |
| B-15 | Group poses (group emotes, cutscene groups): the combined outline reads as the idea | K |
| B-16 | Abilities and timed states: the clip card names the mechanic verb, the same as the VFX frame script and sound cue card, and how the motion carries it; a state with a timer or breaking point has a building end-of-state tell as a named event on the timing list | clip card, N |
| B-17 | Promo, thumbnail or cutscene stills of a character (when briefed): the one-sentence premise is written; the pose is the signature move's key frame from the set, its black-fill at the game camera compared with the clip's key frame (`look_check.py silhouette --compare`, MEASURED), or the difference is recorded with its reason; a fresh read of the still names the premise | K |

### 8b. Spline and polish passes
| ID | Look for | In |
| --- | --- | --- |
| S-01 | On every frame a foot lifts, the root's ground projection sits over the other support; planted feet pass `contact_slide` (tolerance from the rig sheet, else MEASURED) | N |
| S-02 | No mass pops: through the biggest change the root path is continuous and `pops` shows no outlier there; a black-fill strip only if it does | N (K on fail) |
| S-03 | Fast swings have a counter-limb moving the other way, visible from the game camera | K |
| S-04 | The driver leads: the driving limb's curve starts before the root's; arms rise before the root on a jump | N |
| S-05 | Push-off: feet leave 1-2 frames (PROPOSAL) after the root starts rising; the root leaves the bottom steeply | N |
| S-06 | No stalled travel: the root's horizontal curves have no plateau during flight | N |
| S-07 | Gravity spacing: frame-to-frame distance near an apex is smaller than near the ground; no constant spacing on falling or thrown things | N |
| S-08 | Arcs: hand, toe and tool-tip paths curve; a straight run longer than about 6 frames (PROPOSAL) is a missing breakdown | N |
| S-09 | Styled hang time: the root height flattens at the apex and the descent is shorter than the ascent | N |
| S-10 | Contact is fast: frames from first contact to full weight fall between takes; the impact marker is the contact frame | N |
| S-11 | Landing: the root dips clearly below standing but not past the stance limit, holds a little, rises; elbows drop on the landing frames; no scoot | N |
| S-12 | Overshoot: where used, the curve crosses its final value once, small, then settles | N |
| S-13 | Shoulder (or upper-torso) and hip channels are not constant through an action; the hips change on every weight shift | N |
| S-14 | No twinning: left and right keys do not share every frame; landing feet offset; key poses not mirror images | N, K |
| S-15 | Head: in a look-turn, eye and head yaw start before the chest's; in a spin or fast body turn (when the design asks for it), the head's world yaw lags the chest's, then catches up fast | N |
| S-16 | Secondary: chains lag their root by the planned offsets and settle; heavy masses settle fast; each secondary part names its cause; nothing is both baked and runtime-sprung | N, clip card |
| S-17 | Hands and eyes: hand shapes change at key moments and read at the game camera; on dynamic heads, blinks sit on fast turns and eyes widen on falls | K |
| S-18 | Curves are clean: no flip, spike or unintended plateau per control; `rom` inside the manifest; `pops` has no unexplained outlier | N |
| S-19 | Effort order held: no hair, finger or face keys dated before the blocking check-in | job record |
| S-20 | Held items: distance from the body matches the weight class, heavy ones with a counter-lean; moving parts slide without crossing the arms | K, N |
| S-21 | Overlap: where parts of the same colour overlap in a key pose, they still separate in the shaded frame, or the art director is asked | K |
| S-22 | Loops: `loop_seam` position and velocity; idle variation has a cause; tell and contact frames identical across variants and copies | N |

### 8c. Import and in-game pass (Studio, after import)
| ID | Look for | In |
| --- | --- | --- |
| G-01 | At the game camera on the phone viewport, in the real place, moving, with effects, other players and HUD on: the action, its direction and its landing frame are named | C |
| G-02 | Effects hidden, colour removed (grayscale of the capture), shake and flashes off: every tell, contact and outcome still reads from the pose | C |
| G-03 | Marker times from the Output log match the timing list (`clip_check.py` events tolerance, else MEASURED) | log |
| G-04 | Sync: the sound onset lands 0 to about 40 ms after the first lit contact frame and never more than one frame early, measured on the target device; otherwise not verified (`sound-design` uses the same window) | device capture |
| G-05 | Attempt vs outcome: a hit the server rejects (test place) plays no confirmed-hit reaction, hit-stop pose or celebration | C, log |
| G-06 | The hit-stop freeze frame is the contact pose with the source of power and hook shapes facing the camera | C |
| G-07 | Every listed transition, captured: no pop, foot slide or stuck grip; clean-up clears trails and loops | C |
| G-08 | Variants: base and variant key frames side by side (`look_check.py silhouette --compare`): same tell and contact frames, anchors visible, no fewer secondary sources | K, C |
| G-09 | One code: jump and fall root curves and tell lengths match the other clips of the same class, or the difference is recorded | N |
| G-10 | In the busiest expected moment, the player's own move is identifiable from its silhouette at its key pose | C |
| G-11 | Frequent motions at their real rate (for example 100 triggers at one per second, from the builder's rate trigger in the test place): no pile-up (the playing-track count it logs to the Output stays flat), the clip ends before the next trigger; whether it tires is the owner's call on a playable preview at the gate | log, C |
| G-12 | Ambient copies out of step; never the fastest motion near a sightline; pulses at most 3 per second; a still or slow variant exists | C, spec |
| G-13 | Paid reveals: the lowest and highest results share an identical windup, frame by frame, up to the result frame | C |
| G-14 | Truth: with the builder's debug overlay of the hit area on in the test place, the swing's visible reach does not exceed it; a danger pose ends when the danger ends | C |
| G-15 | Scale: a giant's stride period and settles are longer than a normal-size character's; a fresh read names the intended emotion | N, C |
