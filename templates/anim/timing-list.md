---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J006; rig-pipeline §5; animation paper AP:475-491 (event fields, shared contract), AP:17 (exact frame arithmetic), AP:986 (one canonical time); orchestration job-types effect recipe (same event ids); J019 P6 (G3-P6): slots for `animation-design/references/game-timing.md` §4, §5, §8
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Timing list: <action-id> · revision <n>

Owned by the animator (`rig-pipeline` §5). One list per action revision: `content/anim/<asset-id>/timing-<action-id>.md` (a JSON copy for scripts: `timing-<action-id>.json` with the same rows). VFX frame scripts and sound cue cards name these ids. Gameplay windows come from the gameplay owner and are copied here, never changed here. A marker is presentation, never damage authority.

| Key | Value |
| --- | --- |
| Clip id and file | |
| Source frame rate (effective = fps / fps_base) | |
| Clip length | <seconds> = <intervals> intervals at <fps> |
| Gameplay windows source | <feature contract / config path @ revision>, or none (cosmetic) |
| Revision change from last | |
| Mechanic verb (abilities; the same verb as the VFX frame script and sound cue card: `animation-design/references/game-timing.md` §4) | <verb> or n/a |
| Sync trigger: the one event picture punch and sound transient start from (window: `game-timing.md` §4 "Sync rule") | <event id>; verified on device / not verified |
| Reduced-motion note: what the clip keeps and what goes when the player reduces motion (`game-timing.md` §8) | |

## Events
Time rule: seconds = (frame − first frame) / effective fps, kept exact (fractions allowed); one canonical value per event, editor labels are derived.

| Event id | Meaning (one meaning only) | Time (s) | Source frame @ fps | Owner | Authority (presentation / gameplay) | Layer: attempt (plays on input) / outcome (starts from the confirmed event) (`game-timing.md` §4) | Consumers (VFX, sound, UI, camera, code) | Marker name in the clip (if any) | Interruption rule | Replay / loop rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| windup_start | | | | animator | presentation | attempt | | | | |
| contact_candidate | the pose reaches the target (not a confirmed hit) | | | animator | presentation | attempt | | | | |
| contact_confirmed | gameplay outcome; not in the clip | — | — | gameplay | gameplay | outcome | VFX, sound, UI | — | | |
| freeze_frame | the pose held during hit-stop (`game-timing.md` §5); its length is the gameplay owner's, copied below | | | animator | presentation | outcome | VFX, sound, code | | | |
| <state>_end_warn | building tell before a timed or breakable state ends, e.g. `shield_break_warn` (`game-timing.md` §4); n/a when the action has no such state | | | animator | presentation | | VFX, sound | | | |
| cleanup | clears trails, loops, grip overrides | | | animator | presentation | | all | | | |

## Gameplay windows (copied, read-only)
| Window | Start (s) | End (s) | Source |
| --- | --- | --- | --- |
| hit-stop length (if any) | | | gameplay owner + VFX designer (`game-timing.md` §5) |

## Change log
| Revision | Date | Events moved (old → new) | Consumers told |
| --- | --- | --- | --- |
