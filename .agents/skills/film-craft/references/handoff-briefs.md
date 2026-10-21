> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Source: N3 HO-01..09 (hand-off table, OPINION, 2026-10-21), N1 AC-04, SN-06, `rules/messages.md`. Format of every brief: `rules/messages.md` §2 (intent + spec, sent whole, every rule restated, skills named).

# Hand-offs: what each craft gets from the film director

The director delegates execution, not accountability: animation the camera hides is a directing problem even if the animation is correct (N3 HO-00). The director states the readable result it needs; it never writes rig, code or mix implementation.

## 1. Who gets what
| Recipient (role) | Director provides | Recipient decides | Director reviews | Skills to name |
| --- | --- | --- | --- | --- |
| game-designer | beat contract, proposed interruption, gameplay state sheet | gameplay requirements and progression consequences | player purpose and exit state | `game-design` |
| art-director | mood references, contrast intent, colour strip | approved style and visual language | consistency of the sequence with the game | `art-direction` |
| animator (planned role; the lead holds briefs until it exists, J015-D7) | per shot: acting brief (belief, stimulus, tactic, decision, end pose), action beats, eyelines, framing and occlusion limits, frame window from the shot list | poses, motion, implementation | readable performance in the final framing | `film-direction` (acting), the animator's craft skill |
| character-rigger | what must move and how far for the planned acting (face kit, eye target, mouth shapes, limb range) | rig method | the rig can show the beat (render test) | `rigging-design` |
| environment-designer | visible geography, staging lanes, landmarks per shot and their side of frame, light intent per beat (source, brightest area, what stays hidden), sets the shot list needs | set construction, lighting execution | attention, silhouettes, spatial continuity from the shot cameras | `environment-design` |
| vfx-designer | cue id and time, narrative function, attention priority, occlusion limits ("must not hide the route or the boss silhouette"), the shot camera | effect construction, runtime behaviour | the effect clarifies the beat | `vfx-design`, `vfx-craft` |
| sound-designer | cue sheet (`shotlist.py cues`), each cue's role, perspective, sync type, silence intent, dialogue priority | recording, synthesis, mix, playback | timing, intelligibility, relationship to picture | `sound-design` |
| ui-ux-designer | letterbox, subtitle and skip requirements, protected areas per shot, speaker identity, reduced-motion and large-text cases | layout, interaction, accessible presentation | readability, nothing essential covered | `ui-design` |
| engineering (architect → feature-builder) | the `.luau` scene data, input and audience policy, every ending with its resulting state, readiness list, server transitions allowed | camera system, authority, cleanup, instrumentation | captured behaviour and reproducible defects | `architecture`, `engineering-craft` |
| owner | alternatives, evidence, the captured sequence, unresolved risks | creative approval and priority | approval recorded with the owner's words | `ste-writing` |

## 2. Fixed vs open (precision rule, `rules/messages.md` §1)
| Fixed (with a source) | Open (the craft decides) |
| --- | --- |
| shot ids, frame windows and cue times from the shot list (`<file>.shots.json rev n`) | poses, timing inside the window, secondary motion |
| landmarks that must be visible and their side of frame (approved board) | how the set is built and dressed |
| cue ids and sync type (locked / flexible / pending) | the sound itself, layers, processing |
| what must not be covered (route, boss silhouette, subtitle area) | effect technique, textures, curves |
| owner decisions (ids) and platform limits | everything without a source |

A feeling gets a target and an observable sign: "the player must recognise the statue is alive; sign: in the shot D capture the head turn reads before the water burst covers it", not "add a 0.3 s head turn".

## 3. Example (animator, shot C of the original boss-reveal example)
```text
<intent>
Shot C is where curiosity turns into recognition: the player must see the explorer realise, before the statue moves, that something is wrong. The reaction comes before the threat is shown (approved reveal order: geography, alarm, object, reaction). Medium close, eye level, static camera: the change of attention carries the beat, so the body must show it.
</intent>
<spec>
id: J0xx-T05
from: film-director
to: animator
skills: [film-direction, <animator craft skill>]
refs:
  - content/film/<sequence>/boards/C.png   # take: framing, the eyeline target off right; avoid: the hand pose (superseded by shot B's end pose)
  - content/film/<sequence>/previs/animatic_v3.mp4   # take: timing and camera; the explorer is a proxy
fixed:
  frames: 54 to 101 at 30/1 fps        # boss-reveal.shots.json rev 3, shot C
  start_pose: shot B end pose (right hand raised, weight forward)   # continuity ledger
  end_pose: weight on the back foot, head toward the statue (screen right)   # needed by shot D
  eyeline: from the beacon (middle) to past it (right)   # continuity ledger
  camera: static medium close, eye level   # shot list
open: [beats of the realisation, holds, secondary motion, hand action]
avoid: [a facial-only reaction (lost at phone size), looking at the camera]
acting: {belief: "the beacon is a prize", stimulus: "it went dark and something moved behind it", tactic: none, decision: "stop reaching, move away"}
owns: [content/film/<sequence>/anim/C/]
not_in_scope: [shot D, the statue, camera changes]
rules: [Body and head angle must read at phone size. Avatars vary in height: keep the gesture readable for the supported range. No change to frame window without a ticket.]
deliver: content/film/<sequence>/anim/C/
checks:
  - C1: in a 30 fps capture from the shot camera, the stop and the weight shift both read before frame 101
  - C2: end pose matches the fixed end_pose (side-by-side with shot D's first frame)
return: hand-back to film-director (rules/messages.md §3); key poses first (G2 sample)
</spec>
```
