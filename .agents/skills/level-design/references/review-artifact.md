> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `level-design`. Sources: N4 §1 (level review artifact, encounters, 9-item checklist, O), DS (10-item review, reasons). The merged 14-item list and the node-field definitions are J003 additions (the paper names the fields without defining them, N4 §1.2).

# Level review artifact

## 1. Route graph
An annotated route graph, not only a beauty image. Show sightlines and scale from the real gameplay camera; mark where players may lose orientation and how they recover. Where routes cross, they must differ in something meaningful: timing, information, exposure, resource use, skill demand, exploration or expression.

Per node, 10 fields:
| # | Field | Holds |
| --- | --- | --- |
| 1 | Entry view | what the camera shows on arrival |
| 2 | Visible and hidden goals | what the player can see to aim for; what is there to find |
| 3 | Action choices | what the player can do here |
| 4 | Information | what the player learns or must know |
| 5 | Commitment | what is hard to undo once chosen |
| 6 | Risk | what can go wrong |
| 7 | Reward | what the player gains |
| 8 | Recovery | how the player gets back after failure |
| 9 | Exit | where the player can go next, and how they know |
| 10 | Optional content | side content and how it is signalled |

## 2. Walk-throughs and traces
Walk the route as 5 players: uninformed · returning · expert · grouped · one who missed an optional clue. Trace 4 events: a wrong turn · a death · a disconnect · an empty resource. Checkpoints keep what the player learned, not only transit. Test boundaries with the real movement tools; a visible obstacle explains its rule and stays consistent when abilities change.

## 3. Encounters
- State the behaviour each enemy or hazard asks of the player. Two enemies that differ only in health need a reason to both exist.
- Check 6 combinations: overlapping attacks · escape routes · camera occlusion · running out of safe space · resource recovery · simultaneous demands. An enemy fair alone can be unfair in a group.
- Telegraphs work at the moment of decision, at real speed, on a phone.

## 4. Review (14 checks; Pass / Fail / Unproven; no point totals)
| # | Check | Pass when | Why |
| --- | --- | --- | --- |
| 1 | Job | the layout serves the stated target experience and goal | a beautiful level that serves another fun hurts the game (DS) |
| 2 | First view | spawn view shows place, action and next goal | the first seconds decide orientation (DS) |
| 3 | Routes | intended destinations and optional alternatives are found without rescue; no dead end without a reason | intended exploration and accidental disorientation need different fixes (N4) |
| 4 | Landmarks | each zone has a unique, visible landmark; cues distinguishable from the real approach directions and camera | a unique decoration nobody perceives does not orient (N4, DS) |
| 5 | Teaching | the player meets a clear use of the mechanic before a demanding variation (unless confusion is the approved aim) | a test must tell learning from luck (N4) |
| 6 | Escalation | more challenge names the changed demand and the skill tested | hazards without a learning reason feel arbitrary (N4) |
| 7 | Readability | goals win the squint test; geometry, actors and hazard edges are clear on target screens, with effects and full player count | a clean grey box can fail in the production scene (N4, DS) |
| 8 | Pacing | intensity, recovery, anticipation and discovery alternate with a purpose; a climax exists; no long empty walk (measured) | constant maximum intensity removes contrast (N4, DS) |
| 9 | Progress | the player sees how close they are to the goal | invisible progress feels like no progress (DS) |
| 10 | Boundaries | collision, fall and reset rules, closed areas and recovery match the visible world; edges are on theme | mismatched affordances teach rules players cannot trust (N4, DS) |
| 11 | Scale | touch points fit a player in the real camera | wrong scale breaks belief (DS) |
| 12 | Story and theme | the 3-5 expected things are present and easy to find; props show how the place is used | players come for the place they were promised (DS) |
| 13 | Social | group flow, late join, separation and regrouping handled where they apply | a solo route can exclude party members (N4) |
| 14 | Failure | failure cost, retry route and information gained match the intended challenge | retry should test the skill, not add waiting (N4) |

## 5. Output
Ranked findings table (check #, what is wrong, where: node, coordinate or zone, why it matters to the player, fix proposal, cost small / medium / large); a marked-up top-down image when an image of the layout exists (route arrows, numbered problem circles matching the table, Python + Pillow is fine); "keep: what works"; "could not check" (e.g. walk times not measured in Studio). Proposals labelled PROPOSAL.
