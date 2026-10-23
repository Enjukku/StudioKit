---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J019 P6 (G3-P6, J018-D7); level-design books `plan-and-blockout.md` §1, §5, §6 and `review-artifact.md` §1, §6.2; contract named by `.agents/workflows/jobs/job-stage.js` (P1-route-graph)
supersedes: []
---
> Author: J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Route graph: <stage-id> · revision <n>

Workflow: `level-design` §3 steps 1-3. Copy to `knowledge/jobs/<job>/route-graph.md` (a copy in a job folder sets `type: job`, `rules/knowledge.md` §5); the route data goes beside it as `route.json`, started from `templates/level/route.example.json` and read by the §6.2 command in `level-design/references/review-artifact.md`; the top-down diagram beside them (§1, §6.7). The game designer owns this file; others propose changes (a change is a new revision with a row in §F). Every field is defined in the book section named in its heading: fill it there, never copy the rules here. Every value has a source (owner D-id, game profile, brief, measurement) or is `PROPOSAL`.

## A. Level job card (`level-design/references/plan-and-blockout.md` §1)
| Field | Value | Source |
| --- | --- | --- |
| target experience | | |
| four parts (goal, opposition, decisions, rules) | | |
| progress | | |
| conflict and story reason | | |
| teaches | | |
| session shape (first visit, return visit, phone session) | | |
| camera, device, group | | |
| movement metrics (walk speed, jump: measured, `review-artifact.md` §6.6) | | |
| personality and expectations | | |
| smallest gameplay object, and its floor types | | |
| stop criteria, budget | | |

## B. Nodes (`level-design/references/review-artifact.md` §1; one record per node, ids never change)
```yaml
- node: <id>                     # same id as route.json "nodes"
  fields:                        # the 10 node fields
    entry_view: ""               # 1, with read rank 1-3
    goals_visible_hidden: ""     # 2
    action_choices: ""           # 3, with the tool or ability each needs
    information: ""              # 4, critical facts and the cue that carries each
    commitment: ""               # 5
    risk: ""                     # 6
    reward: ""                   # 7
    recovery_s: UNKNOWN          # 8, seconds
    exit: ""                     # 9
    optional_content: ""         # 10
  geometry:                      # node geometry (the blockout brief and the measures read it)
    floor_position: [x, y, z]    # studs, Studio floor position; must match route.json
    stop_or_pass: ""
    sight_lines_clear: []        # from → to
    key_positions: []
    floor_types_smallest_object: ""
    events_heard: []             # event and its source
```

## C. Route table (`review-artifact.md` §1 edge row; numbers from §6.2 on `route.json`)
| From → to | Distance (studs) | Seconds at walk speed | Limit (s, from the brief) | Sees or does on the way | Timed seconds (walk test) | Source |
| --- | --- | --- | --- | --- | --- | --- |

## D. Teaching sheet (`plan-and-blockout.md` §5; one per mechanic taught, or "not required" with the reason)
| Beat | Arrangement | Failure cost | The player infers | The action that shows it | Capture |
| --- | --- | --- | --- | --- | --- |
| 1 Safe exposure | | | | | |
| 2 Required | | | | | |
| 3 Twist | | | | | |
| 4 Independent use | | | | | |

## E. Pacing map (`plan-and-blockout.md` §6; one row per route segment, in route order)
| Segment (from → to) | Seconds | Intensity 0-3 | Kind | What the player sees or does |
| --- | --- | --- | --- | --- |

## F. Changes
| Revision | Date | Change | Who proposed / who accepted | Reason and evidence |
| --- | --- | --- | --- | --- |
| 1 | | first revision | | |
