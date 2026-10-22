> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Source: N3 HO-01..09 (hand-off table, OPINION, 2026-10-21), N1 AC-04, SN-06, `rules/messages.md`. Format of every brief: `rules/messages.md` §2 (intent + spec, sent whole, every rule restated, skills named). Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (the performance sheet and pushed moments for the animator, the value plan for the environment designer, the marker list and sync rule for VFX and sound, stills for marketing, the outcome trigger for engineering).

# Hand-offs: what each craft gets from the film director

The director delegates execution, not accountability: animation the camera hides is a directing problem even if the animation is correct (N3 HO-00). The director states the readable result it needs; it never writes rig, code or mix implementation.

## 1. Who gets what
| Recipient (role) | Director provides | Recipient decides | Director reviews | Skills to name |
| --- | --- | --- | --- | --- |
| game-designer | beat contract, proposed interruption, gameplay state sheet | gameplay requirements and progression consequences | player purpose and exit state | `game-design` |
| art-director | mood references, contrast intent, colour strip | approved style and visual language | consistency of the sequence with the game | `art-direction` |
| animator | per shot: acting brief (belief, stimulus, tactic, decision, subtext, end pose) and the performance sheet (per beat motion, driver, time, sound word); 2-4 adjectives with their pose change; the one or two moments to push; action beats, eyelines, framing and occlusion limits, frame window from the shot list; for a still or key frame, the premise and the still's camera (you supply the signature key pose from the set) | poses, motion, implementation | readable performance in the final framing; the blocking reviewed at the shot cameras before polish | `film-direction` (acting), `animation-design`, `animation-craft` |
| character-rigger | what must move and how far for the planned acting (face kit, eye target, mouth shapes, limb range) | rig method | the rig can show the beat (render test) | `rigging-design` |
| environment-designer | visible geography, staging lanes, landmarks per shot and their side of frame, the value and light plan per beat (contrast key, motivated source, brightest area, separation, depth groups, what stays hidden), the approved value strip, story facts the place must show, sets the shot list needs | set construction, lighting execution | attention, silhouettes, spatial continuity and the value lines (B-06, B-07) from the shot cameras | `environment-design` |
| vfx-designer | cue id and time, narrative function, attention priority (the effect is never the primary read unless the beat is the effect), the peak marker it shares with sound and picture, occlusion limits ("must not hide the route or the boss silhouette"), the shot camera, the clean frame it is added to | effect construction, runtime behaviour, camera punches in play | the effect clarifies the beat; the subject still ranks first (B-08) | `vfx-design`, `vfx-craft` |
| sound-designer | cue sheet (`shotlist.py cues`), each cue's job and the emotion it carries, perspective, sync type, the stage names of staged actions, silence intent, dialogue priority, the sync rule (`film-direction/references/beats-and-timing.md` §4); temp sound from the first animatic | recording, synthesis, mix, playback | timing, intelligibility, relationship to picture; the key event solo, then in the full mix (owner listen at the gate) | `sound-design` |
| ui-ux-designer | letterbox, subtitle and skip requirements, protected areas per shot, speaker identity, reduced-motion and large-text cases | layout, interaction, accessible presentation | readability, nothing essential covered | `ui-design` |
| engineering (architect → feature-builder) | the `.luau` scene data, input and audience policy, every ending with its resulting state, readiness list, server transitions allowed, the server-confirmed event that starts any outcome sequence; for the test build: a playback log of shot, cue and animation-marker times on one clock (ids exactly as in the shot list: `A`, not `shot:A`; `roblox-assembly.md` §3), and a hook that rejects the result | camera system, authority, cleanup, instrumentation | captured behaviour and reproducible defects (R-04, R-14) | `architecture`, `engineering-craft` |
| marketing (stills from a cinematic) | the key frame with its premise, crop-safe composition and layers (foreground, midground, background, lights, effects) as named switchable groups; the clean frame | crops, title, the promise | the featured thing is the hero in every crop | `marketing-design` |
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
acting: {belief: "the beacon is a prize", stimulus: "it went dark and something moved behind it", tactic: none, decision: "stop reaching, move away", subtext: "she still wants the prize", adjectives: [curious (leans in), wary (weight back)], pushed: "the recoil, stronger than real; balance kept over the back foot"}
owns: [content/film/<sequence>/anim/C/]
not_in_scope: [shot D, the statue, camera changes]
rules: [Body and head angle must read at phone size. Avatars vary in height: keep the gesture readable for the supported range. No change to frame window without a ticket.]
deliver: content/film/<sequence>/anim/C/
checks:
  - C1: in a 30 fps capture from the shot camera, the stop and the weight shift both read before frame 101
  - C2: end pose matches the fixed end_pose (side-by-side with shot D's first frame)
  - C3: blocking (key poses as black-fill from the shot camera) shown to film-director before splines; the recoil reads at phone size
return: hand-back to film-director (rules/messages.md §3); key poses first (G2 sample)
</spec>
```
