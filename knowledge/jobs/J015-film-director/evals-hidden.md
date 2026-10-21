---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J015 brief (hidden test set); fact-checks FR FC-20..49, FB corrections 1-14; N4 owner corrections
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J015 hidden eval cases (grader only; not given to the agent)

The agent gets only the **symptom brief**. The grader scores the hand-back and files against **expected**.

## H1 — "Use a 35 mm lens for intimacy and an 85 mm for the villain, like real films"
Symptom brief: "Make the confession scene intimate with a 35 mm lens and make the villain scary with a long lens. Put those lenses in Roblox."
| Expected | Points |
| --- | --- |
| No lens-to-emotion rule; effects are conditional and come from distance, framing and staging | 3 |
| Roblox has no focal length: converts lens + sensor + fit + aspect to a vertical `FieldOfView`; notes the `angle_y` trap or computes the angle correctly | 3 |
| Perspective depends on camera position, not focal length | 2 |
| Checks framing at the narrowest supported display | 2 |

## H2 — "Make the animatic at 29.97 like TV"
Symptom brief: "Set the animatic to 29.97 fps and give me the exact cut times in seconds."
| Expected | Points |
| --- | --- |
| Keeps 30000/1001 as a fraction; Blender `fps=30000, fps_base=1001.0` (not 30 / 1.001) | 3 |
| Cut times from `[start, next-start)` with exact seconds; no rounding to 33 ms frames | 3 |
| Asks or states why 29.97 (a project decision); notes Roblox playback times come from the data module | 2 |
| Uses `shotlist.py` rather than hand arithmetic | 2 |

## H3 — "Our side characters are recolours, just animate them crying"
Symptom brief: "Board and animate the villagers crying when the hero falls; they are the same model in different colours."
| Expected | Points |
| --- | --- |
| Readiness: each speaking or emoting character needs its own face kit, eyes that can look, mouth shapes; recolours read as one character | 3 |
| Tests the acting against the rig in a render before locking the beat; offers a beat change that keeps the story outcome if the rig cannot show it | 3 |
| Tickets to the character rigger / modeler, not a workaround in animation | 2 |
| Platform check on grief and injury imagery | 2 |

## H4 — "Skip should just hide the bars"
Symptom brief: "Add a skip button: when pressed, hide the letterbox and subtitles and let the cutscene keep running behind the game."
| Expected | Points |
| --- | --- |
| Rejects: skip must reach the resulting story state and end the scene (teardown), not hide UI while it acts | 3 |
| Cancels scheduled audio (`AudioPlayer:Cancel`), clears or lets finish scene effects, releases foci, restores camera and input | 3 |
| Essential information survives the skip; repeated presses = one result; skip has its own input context on touch, gamepad, keyboard | 2 |
| Shared scenes: per-player vs group skip policy stated | 2 |
