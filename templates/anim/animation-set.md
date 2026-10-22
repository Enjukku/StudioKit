---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J006; animation paper AP:398-467 (sets, loops, transitions SL01-SL08), AP:751-763 (priority, tracks)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Animation set: <asset-id> · revision <n>

One file per animated asset: `content/anim/<asset-id>/animation-set.md`. Clips come from the implemented states (game-designer or feature contract, revision named). A state with no clip says "absent on purpose" or names its code-driven motion spec.

States source: <feature contract / spec path @ revision>

## Clips
| Clip id | State | Loop / one-shot | Entry pose → exit pose | Length (s) and source (window id / measured / PROPOSAL) | Priority intent | Layered joints (blank = whole body) | Interruption rule | Attachments | Events (timing list ids) | LOD variant | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Transitions to test
| From | To | Blend length (source) | Must keep (contacts, grip) | Clean-up | Result |
| --- | --- | --- | --- | --- | --- |

## Clip cards (one per clip)
### <clip id>
- **Read:** what the player must understand, by which event.
- **Key poses:** the story poses (frame, what each says).
- **Breakdown / storytelling pose:** what carries the motion between them.
- **Accent:** the event where the visible peak sits (timing list id).
- **Spacing:** where it snaps, where it eases, where it holds, and why.
- **Arcs to check:** landmarks (hand, tool tip, toe, tail tip, head).
- **Secondary:** what settles after, its cause.
- **Not in this clip:** VFX trails, flashes, camera (owners named).
- **Checks:** clip_check metrics to pass; key frames to render.
