---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J006; rig-pipeline §5; animation paper AP:475-491 (event fields, shared contract), AP:17 (exact frame arithmetic), AP:986 (one canonical time); orchestration job-types effect recipe (same event ids)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Timing list: <action-id> · revision <n>

Owned by the animator (`rig-pipeline` §5). One list per action revision: `content/anim/<asset-id>/timing-<action-id>.md` (a JSON copy for scripts: `timing-<action-id>.json` with the same rows). VFX frame scripts and sound cue cards name these ids. Gameplay windows come from the gameplay owner and are copied here, never changed here. A marker is presentation, never damage authority.

| Key | Value |
| --- | --- |
| Clip id and file | |
| Source frame rate (effective = fps / fps_base) | |
| Clip length | <seconds> = <intervals> intervals at <fps> |
| Gameplay windows source | <feature contract / config path @ revision>, or none (cosmetic) |
| Revision change from last | |

## Events
Time rule: seconds = (frame − first frame) / effective fps, kept exact (fractions allowed); one canonical value per event, editor labels are derived.

| Event id | Meaning (one meaning only) | Time (s) | Source frame @ fps | Owner | Authority (presentation / gameplay) | Consumers (VFX, sound, UI, camera, code) | Marker name in the clip (if any) | Interruption rule | Replay / loop rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| windup_start | | | | animator | presentation | | | | |
| contact_candidate | the pose reaches the target (not a confirmed hit) | | | animator | presentation | | | | |
| contact_confirmed | gameplay outcome; not in the clip | — | — | gameplay | gameplay | VFX, sound, UI | — | | |
| cleanup | clears trails, loops, grip overrides | | | animator | presentation | all | | | |

## Gameplay windows (copied, read-only)
| Window | Start (s) | End (s) | Source |
| --- | --- | --- | --- |

## Change log
| Revision | Date | Events moved (old → new) | Consumers told |
| --- | --- | --- | --- |
