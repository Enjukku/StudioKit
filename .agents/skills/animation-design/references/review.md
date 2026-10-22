> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Sources: animation paper AP:994-1034 (review, RV, 15-row checklist RV-T01..T15, failure list RV-F01..F08), AP:1036-1100 (gates), AP:1070-1088 (do not do); Riot ep4 A:158-160, A:246-254, A:384-386, A:420-432, A:456-468, A:540-552, A:760-764, A:818-856 (self-review, mistakes). Owner rule J005-D8 (light checks). Tags as in SKILL.md.

# Review: judge the read, then the defects

## 1. Order (AP:998-1000)
1. **Read first:** can a viewer name the subject, goal, direction, key contact, force and result without text? Is it the approved character?
2. **Then defects** (§2). Separate approved exaggeration from accidents; record disagreement instead of a false consensus.
3. **Views:** the game camera at phone size first; then side and front diagnostics; a silhouette pass; with and without effects; the final context.
4. **Speeds:** normal speed first (a clumsy still can be a good transition; a handsome contact sheet can hide a dull rhythm, AP:533), then slow, then frame by frame at events.
5. **Delivered asset:** judge the imported Roblox result, not only the Blender preview (AP:996).

## 2. Pass / fail checklist (AP:1004-1021)
| ID | Test | Pass | Fail |
| --- | --- | --- | --- |
| R-01 | Intent and personality | viewer names the action and the approved character quality | gesture contradicts the brief or needs explaining |
| R-02 | Part identity | every animated part has a label and a driver | an unknown part moved by generic noise |
| R-03 | Contact | planted or gripped parts stay attached within the approved tolerance | foot slide, grip separation, unexplained penetration |
| R-04 | Support and weight | support and force explain acceleration and recovery | weightless launch, unsupported stop, no reaction |
| R-05 | Arcs and spacing | paths and spacing serve anatomy, force and style | accidental corners, one ease everywhere, pops |
| R-06 | Joint and mesh integrity | within verified range; deformation acceptable | knee or elbow inversion, collapsing volume, broken fold |
| R-07 | Secondary causality | lag, correction and settle have causes | all parts in phase, or a generic delayed wave |
| R-08 | Tools and props | grip, pivot, collision, path and consequence agree | tool feels detached, hinge translates, impact has no response |
| R-09 | Loop seam | pose and velocity continuous, or an approved break | pause, pop or drift at the repeat |
| R-10 | Transition and interruption | required paths keep contacts and clean up | residue, stale trails, stuck grips, no recovery |
| R-11 | Gameplay timing | visible threat and result agree with the windows | the picture implies a range or damage that is not there |
| R-12 | Export fidelity | imported poses, events and length match the approved preview | lost action, changed scale, retimed contact, missing channel |
| R-13 | Runtime | priority, blending, authority and replication as designed | other clients disagree; unrelated joints overridden |
| R-14 | Cost | the agreed phone scene passes measured frame and memory goals | only a desktop or single-asset test passes |
| R-15 | Owner approval | the current revision is approved, open issues disclosed | approval of an older revision |

**Tolerances first** (AP:1023): a numeric check passes or fails only against a tolerance set in units, camera and method. With no tolerance, report the measurement as MEASURED, never PASS.

## 3. Common failures: first check (AP:1025-1027; Riot A:456-474, A:390-404, A:540-552)
| Symptom | Check first |
| --- | --- |
| Floaty, linear | spacing, support, contact and braking before adding keys; computer in-betweens left alone twist the body [E] A:64-76 |
| No anticipation | does a responsiveness rule explain it? If not, add a readable cue inside the approved timing |
| Foot moves without a weight shift (the most common reel fault) | add the weight shift or a contact [E] A:456-474 |
| Jump has no energy source | clavicles and shoulders still; add the shrug and the arm push [E] A:390-404, A:892-904 |
| Robotic timing, twinning | spacing and accents of events; offset limbs; uneven cadence, not random per-channel offsets [E] A:360-366, A:540-552 |
| Soft, scooting landing | make the contact faster; tighten a landing that sinks too far [E] A:438-446, A:656-660 |
| Bad arcs | plot world-space landmarks; check the reference and the camera |
| Weightless tool | grip, support shift, tool acceleration, body reaction after impact |
| Stiff tails or wings | rethink the anatomy and which part drives which |
| Gimbal-twisted arm | key it through, or delete and redo [E] A:906-912, A:420-424 |
| Too many keys or bones | reduce only after measuring what the removal does |
| Leg pointing down the camera | turn it so the knee shows; foreshortening reads as boring [E] A:760-766 |

## 4. Writing a finding (AP:1002)
Tie every remark to a time and visible evidence ("left foot drifts 0.3 studs during declared support, frames 12-18, side view"). No "add life". A proposed change names the channel or body group, the event interval, the intended result for the viewer and the regression to check.

## 5. Light checks (owner J005-D8; `rig-pipeline` §4a)
- Numbers for every clip (`tools/anim/clip_check.py`: loop seam, contact slide, length against the window, events against the timing list, ROM against the control manifest).
- Images only when a number fails, plus at most 8 key frames per action: the accent pose, the extremes, the loop seam, from the game camera and one close view.
- One full check per hand-off, by the receiver; the full image set once, at release.
- Report how many renders were made and how many images were looked at.

## 6. When to stop polishing
The approved revision is done when R-01 to R-15 pass or carry owner-approved exceptions. Small pops most viewers will not see are logged, not chased; the producer (here the lead and the owner) calls it done [E] A:818-856. When a part will not fix, delete the keys and redo it [E] A:420-432.

## 7. Do not do (AP:1070-1088)
Deduce species or mass from bones · paste a bird wing cycle on a bat · invent timing or budget values · equate more keys, bones, simulation or AI output with better animation · let effects cover a missing contact · overwrite an approved clip without keeping the old revision and its event contract · treat a preview render as proof of import, replication or phone cost · ship unreviewed generated motion · replace owner approval with a score.
