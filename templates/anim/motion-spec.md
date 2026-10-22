---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J006 owner brief ("Code-driven motion: the animator writes the motion spec (curves, timings, events); a builder writes the code"); animation paper AP:446-454 (props), AP:771, AP:831 (tweens, cosmetic motion local); fact-check-techniques.md
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Motion spec: <object-id> · revision <n>

For motion driven by code (TweenService, CFrame / PivotTo) or physics constraints. The animator writes what moves, how and why; a builder (feature-builder or quick-builder) writes the code. Values go into data (`AGENTS.md` §2: content is data), never into logic. Every value has a source or says PROPOSAL.

## Intent
- **Read:** what the player must understand (it is unlocked, it is about to drop, it is safe to step on).
- **Feel words:** (heavy, old, grinding / light, snappy, magical).
- **Interaction:** what starts it (player input, trigger, timer, state change), who owns that state (server, client).

## Mechanism
| Key | Value |
| --- | --- |
| Moving part(s) and what stays fixed | |
| Pivot or rail: position, axis, space (e.g. hinge line along the door's edge, not its centre) | |
| Travel: from → to (degrees or studs) | |
| Actuator (hand, motor, counterweight, gravity, magic) | |
| Hard stops and whether it rebounds | |
| Technique and reason (+ docs page) | TweenService / CFrame per frame / constraint (Hinge motor or servo, Prismatic, Spring) / keyed clip |
| Runs on (client cosmetic / server authoritative) and why | |
| Collision and occupancy owner (what physics or gameplay sees during the motion) | |

## Phases
Lengths in seconds; source = gameplay window id, owner decision, measured reference, or PROPOSAL.

| Phase | From → to (value) | Length (s) | Curve (EasingStyle + Direction, or a named custom curve with key points) | Why this curve | Event at start / end (timing list ids) |
| --- | --- | --- | --- | --- | --- |
| e.g. unlock | 0 → 3° rattle | | | the latch gives first | unlock_click |
| accelerate | | | | | |
| travel | | | | | |
| stop | | | | hard stop, small settle | door_stop |

## Variation and scale (ambient or repeated objects)
| Key | Value |
| --- | --- |
| Copies on screen (game profile or PROPOSAL) | |
| Per-copy variation (phase offset, speed range) so copies do not move in step | |
| Off-screen / far behaviour (stop, slow, skip) | |
| Streaming: what happens when the object streams in or out mid-motion | |

## Interruptions and states
| Case | Behaviour |
| --- | --- |
| Triggered again while moving | |
| Player stands in the path / on it | |
| Late joiner sees it | starts at the current state, not from the beginning |
| Reset / round restart | |

## Checks the builder and reviewer run
- [ ] Pivot and axis match the spec (rotation preview from two views).
- [ ] Each phase length and curve as listed; events fire at the listed times (Output log times).
- [ ] Cosmetic motion runs on the client; authoritative state on the server.
- [ ] Copies are out of step; off-screen behaviour as listed.
