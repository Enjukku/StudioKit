---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J006; animation paper AP:398-467 (sets, loops, transitions SL01-SL08), AP:751-763 (priority, tracks); J019 P6 (G3-P6): columns for `animation-design/references/sets-and-states.md` §5, plan-stage lines for `animation-design/SKILL.md` §3 steps 5-6
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Animation set: <asset-id> · revision <n>

One file per animated asset: `content/anim/<asset-id>/animation-set.md`. Clips come from the implemented states (game-designer or feature contract, revision named). A state with no clip says "absent on purpose" or names its code-driven motion spec.

States source: <feature contract / spec path @ revision>

## Clips
| Clip id | State | Loop / one-shot | Entry pose → exit pose | Length (s) and source (window id / measured / PROPOSAL) | Who must react + reaction window (source) (`animation-design/references/game-timing.md` §1-§2) | Play rate (source) | Pushed moments (1-2; `animation-design/references/principles.md` P-10.5) | Priority intent | Layered joints (blank = whole body) | Interruption rule | Attachments | Events (timing list ids) | Reduced-motion variant (`game-timing.md` §8) | LOD variant | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Transitions to test
| From | To | Blend length (source) | Must keep (contacts, grip) | Clean-up | Result |
| --- | --- | --- | --- | --- | --- |

## Clip cards (one per clip)
### <clip id>
- **Read:** what the player must understand, by which event.
- **Beat sheet:** per beat: body action and driver, time (window or PROPOSAL), sound word, subtext; the mechanic verb for an ability (`animation-design/SKILL.md` §3 step 5).
- **Key-pose options and pick:** contact sheet path (2-3 black-fill options at the game camera), the pick and why each other option lost; timing takes for signature, tell and emote clips (`animation-design/SKILL.md` §3 step 6; `animation-design/references/review.md` §8a B-12).
- **Key poses:** the story poses (frame, what each says).
- **Breakdown / storytelling pose:** what carries the motion between them.
- **Accent:** the event where the visible peak sits (timing list id).
- **Spacing:** where it snaps, where it eases, where it holds, and why.
- **Arcs to check:** landmarks (hand, tool tip, toe, tail tip, head).
- **Secondary:** what settles after, its cause.
- **Not in this clip:** VFX trails, flashes, camera (owners named).
- **Checks:** clip_check metrics to pass; key frames to render.
