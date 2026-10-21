---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J008 (owner 2026-10-21 "zones, what you hear, what moves, point sources, how zones blend"); environment paper fields AF01-AF32 (knowledge/reference/environment/02-ambience-life-dressing-terrain.md §6)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Ambience map: <stage-id> · revision <n>

Workflow: `environment-design` §ambience (what and why), `environment-craft` (placing zones and points in the place). Copy to `content/stages/<stage-id>/ambience-map.md`. The environment designer writes it; the sound designer and the VFX designer build from it and fill only their own keys (`sound:` / `vfx:`); others comment in §H, never edit.

**Number rule.** Every number has a unit (studs, seconds, 0-1) and a source: the approved blockout (exported coordinates), a measured capture, an owner D-id, or `PROPOSAL`. A value nobody has measured is `UNKNOWN`, never 0 and never a guess. No source gives a universal range, gain or crossfade time for any ambient sound (environment paper EP:318, EP:755): those numbers come from this stage, measured.

## A. Stage (environment designer)
| Key | Value |
| --- | --- |
| stage_id / revision | |
| blockout revision the numbers come from | path + date |
| art bible version | |
| listener | camera / avatar / other, and why (third-person cameras can pass a wall while the avatar is still inside) |
| player feeling per area, in order of the route | one line each, from the game designer's layout |
| acoustic approach per enclosed space | authored reverb / acoustic simulation / none; one choice per space, recorded (never both by accident) |
| shared environment state | the state every craft reads: time of day, weather, wind, water, event, current zone (§D) |
| muted play | supported? If yes, every gameplay-critical sound also has a visual cue |

## B. Zones (one record per zone; zone IDs never change)
```yaml
- zone: Z-FALLS                  # stable id, used by sound, VFX, code and review
  env:                           # environment designer
    feeling: loud water landmark; the reward for the climb   # what the player should feel or work out here
    bounds: {shape: box, center: UNKNOWN, half_extents: UNKNOWN, y_range: UNKNOWN, units: studs, source: blockout rev 3}
    priority: 2                  # wins over lower numbers where zones overlap
    neighbors: [Z-SWAMP, Z-CAVE]
    what_you_hear:               # plain words; the sound designer decides how it sounds
      continuous: none needed; the falls carry the zone
      intermittent: []           # one-shots with when they may play (time, weather, state)
      point_sources: [FALL-MAIN, RIVER-OUT]   # ids in §C
    what_moves: [falling water, spray at the basin, wet rocks shine]   # visible causes; VFX ids in §C
    quiet_space: route lane on the left bank stays free of spray and props   # what must stay readable
    fallback: keep FALL-MAIN; drop spray detail first   # low-detail behavior, in drop order
    checkpoints: [approach before the reveal, basin edge, cave mouth looking back]   # named listening and camera points
  sound:                         # sound designer
    layers: ""                   # clips, variation, eligibility
    mix_revision: ""             # the approved mix that set the levels
  vfx:                           # VFX designer
    effects: ""                  # effect ids, spec files
  approval: {owner: environment-designer, state: draft}   # draft / sound-reviewed / vfx-reviewed / owner-approved
```

## C. Point sources and moving things (one record per source; ids never change)
```yaml
- id: FALL-MAIN
  kind: sound                    # sound / effect / sound+effect / moving prop
  env:
    anchor: the visible impact point at the foot of the falls   # a part or attachment that is really there
    position_source: UNKNOWN     # world position from the blockout; studs
    visible_cause: the falls themselves   # what the player sees that explains it (never a sound with no cause)
    heard_from: the approach checkpoint, before the falls are seen   # the job, not a distance
    directional: yes             # should the player be able to point at it?
    streaming: keep              # keep (persistent anchor) / rebuild once on return / may stop; and why
    degrade_rank: 1              # 1 = last to drop
  sound:
    range_and_curve: UNKNOWN     # set by the sound designer from the checkpoints; end of curve at gain 0
    gain: UNKNOWN
  vfx: {}
```

## D. Shared environment state
| State key | Values | Who changes it | Who reads it (sound, VFX, lighting, plants, code) |
| --- | --- | --- | --- |
| time_of_day | | | |
| weather | e.g. clear / rain / storm | | |
| wind | strength and direction, plus local shelter per zone | | |
| exposure | open / sheltered / enclosed, per zone (not height alone) | | |
| event | stage events that change the sound or motion | | |

Wind sound, moving plants and blowing particles read the same wind state. A flag that whips over a perfectly still soundscape is a defect unless the brief says otherwise.

## E. Blends (one row per border the player can cross)
| From → to | Where the change happens | How it changes | Edge cases written down | Source |
| --- | --- | --- | --- | --- |
| Z-FALLS → Z-SWAMP | along the outflow, not at a line | outdoor water fades as the reeds come in | walk back, stand on the edge, teleport in, respawn in, camera passes the wall | PROPOSAL |

Never switch the whole mix at once at a border. Width and time of a blend are `UNKNOWN` until a route capture exists.

## F. Lifecycle and streaming
| Source or zone | Anchor that does not stream out (or rebuild rule) | On leave | On return | Tested leave → return → leave |
| --- | --- | --- | --- | --- |
| | | stop events, free the source | rebuild once, never a second loop | yes / no |

## G. Checks before hand-off (environment designer)
- [ ] Every zone on the route has a feeling, bounds (or `UNKNOWN` with the blockout revision that will set it), neighbors and a fallback.
- [ ] Every point source has a visible cause and a real anchor. No prop is audible without a reason.
- [ ] Every border the player can cross has a blend row with its edge cases.
- [ ] One acoustic approach per enclosed space, recorded.
- [ ] Gameplay-critical cues are never masked by ambience and never depend on sound alone when muted play is supported.
- [ ] No number without a unit and a source; nothing invented; `UNKNOWN` where not measured.
- [ ] Listening is not judged from screenshots: the sound check stays "auditory acceptance pending" until someone listens.

## H. Comments and changes
| Date | Who | Section / id | Comment or change request | Status |
| --- | --- | --- | --- | --- |
