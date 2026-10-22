> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `animation-design`. Sources: animation paper AP:347-375 (game vs film, GT01-GT09), AP:469-498 (combat contract, CT01-CT06), AP:967-992 (hand-offs, HC01-HC04); Riot ep4 A:162-190 (timing spine). Notes: `knowledge/reference/animation/01-*.md` §6, §9; `02-*.md` §4. Tags as in SKILL.md.

# Game timing and the shared event timeline

## 1. Who owns which time
| Time | Owner | The animator's part |
| --- | --- | --- |
| Gameplay windows (startup, active, recovery, cancel, cooldown) | gameplay owner (game-designer, feature contract, config) [E] A:172-174; [O] AP:473 | place readable beats inside them; report a conflict, never retime the window (AP:986) |
| Clip beats (anticipation, accent, follow-through, settle) | animator | inside the window |
| VFX timing | vfx-designer, partnered and "a little staggered" behind animation [E] A:166-168 | name the events VFX needs |
| Sound timing | sound-designer, after the picture; must hear about every change [E] A:164-180 | name accents and confirmed outcomes |
| Camera accents in cutscenes | film-director | act inside the shot list |
| Authoritative outcome (hit, damage, open, occupied) | server gameplay code | none: a marker is presentation (AP:473) |

## 2. Game time is not film time (AP:351-363)
- Separate five things: the visible reaction, the authoritative start, the active window, when cancel is allowed, when control returns. A recovery pose can keep playing after control returns; a blend can cover a state change; neither shows the cancel window.
- Startup / active / recovery are analysis tools, not proof of three sequential states; note buffering, hit confirmation and rate changes.
- Input delay has several clocks (input, game acceptance, network, animation scheduling, display). A long windup is not lag. No safe general value for input delay, cancel window, startup or blend length was found (AP:355): design supplies them or approves a measurement.
- Anticipation is information and perceived effort, not automatically input delay: move visible effort around protected events instead of stretching the action [E] WoW casters (AP:115-121).
- Protect readiness beats: a cosmetic variant keeps the base clip's readiness and ammunition events [E] Riot weapon skins (AP:89-97).

## 3. Frame arithmetic (exact, AP:17, AP:361)
- seconds = source intervals / source frame rate. Poses on frames 1 and 31 at 30 fps are 30 intervals = 1 s apart.
- A 30 fps interval is exactly 100/3 ms; a 60 fps interval 50/3 ms. Keep fractions; rounding is a logged decision.
- Blender's effective rate is `render.fps / render.fps_base` [V] (AP:361).
- Capture rate, animation sampling rate, simulation step, render rate and display refresh are five different things.
- A count with no stated rate ("45 frames") has no seconds equivalent (AP:1144).
- Retiming by k: recheck every dependent event at t × k; uniform scaling can still look wrong (AP:363).

## 4. The shared event timeline (format: `templates/anim/timing-list.md`)
Fields per event (AP:475): action revision, stable name, meaning, time in seconds (exact or rational), source frame and frame rate, owner, authority, replay policy, interruption behaviour, consumers.

Typical events, use only those the action has: request accepted, presentation start, anticipation complete, active start, contact candidate, active end, cancel open / close, recovery complete, attachment change, VFX trigger, audio trigger, camera accent, UI cue, clean-up.

- **One meaning per event.** Never one marker named "Hit": a trail may start before contact, a whoosh follows acceleration, a contact sound needs a confirmed surface, damage may come after prediction (AP:477).
- **Forecast vs confirmed.** `ContactCandidate` (animator, from the pose) is not `ContactConfirmed` (gameplay outcome). A miss never plays confirmed-hit feedback (AP:483-491).
- **Clean-up is an event.** Interruption clears trails, loops, grip overrides and connections.
- **One canonical time per event,** derived editor labels only; no craft keeps its own rounded frame list (AP:986).

## 5. Hit-stop and impact (AP:479-481)
- Hit-stop manipulates time; choose what freezes (attacker, victim, weapon, track, particles, camera, audio, controller) and on which clock. Without explicit time scaling, author a held pose or a local presentation pause and keep simulation running. No general hit-stop, shake or sound-offset value exists: it is a proposal per game.
- Impact reads from approach, contact geometry, force direction, allowed deformation and consequence. Check with effects hidden: if removing the flash hides the impact, the pose or timing is unclear (AP:481).

## 6. Hand-offs (AP:975-984)
| With | Animator needs | Animator supplies | Accepted when |
| --- | --- | --- | --- |
| Owner | intent, personality, readability priorities | alternatives, previews, trade-offs | decision recorded on the current revision |
| Modeler (through the rigger) | shape, parts, silhouette limits | contacts and extreme-pose envelope | multi-view deformation renders |
| Rigger | parts, axes, limits, IK/FK, export joints, sockets | motion ranges, failed poses (one rig note) | rig test clip and round trip |
| Gameplay | states, speed, windows, cancels, authority, interruption | contact timing, displacement, feasibility, events | the same event contract in runtime tests |
| VFX | origins, directions, lifetimes, cancel | named events and attachment transforms | effects align on hit, miss and interruption |
| Sound | cue meaning, intensity, surface data | accents and confirmed outcomes | no stale loop, no false hit cue |
| UI | feedback meaning and priority | action-state and result events | UI never shows a false success |

Bring the animator in at concept time: it can say what is feasible, or that more is possible [E] A:184-190.
