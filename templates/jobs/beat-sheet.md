<!-- > Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; beat contract, state-change columns and gameplay state sheet added by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J015, film-direction skill §3). Used for cutscenes, key moments and effects. Copy to the job folder or `knowledge/design/moments/<moment-id>.md`. Shots and exact timings live in the shot list (`templates/film/shotlist.example.json`), not here. -->
# Beat sheet: <job-id or moment-id>

> Revision: <n>, <date>. Status: PROPOSAL until the owner approves the beat contract (decision id: <>).

## Beat contract (owner approves this first)
| Field | Value |
| --- | --- |
| Player's situation before | <where they are, what they know, what they were doing> |
| Change in knowledge or feeling | <from → to, e.g. curiosity → recognition of danger> |
| Consequential character action | <the action that changes the situation> |
| State after | <what the player knows, where they stand, what they can do next> |
| Why interrupt or redirect attention | <the gameplay reason; for player-directed moments: why no camera takeover> |
| Camera mode | authored / player-directed / hybrid, and why (`film-direction` D-02) |
| Essential information (needed to act) | <list; must also survive a skip> |
| Optional atmosphere | <list> |
| Platform limits | <romance, injury, horror, franchise: what is excluded (`platform-policy`)> |

## Beats
One row per beat. A beat that changes neither understanding nor feeling is cut or merged. Times are filled from the shot list after previs; before that write the event that ends the beat.

| Beat | Shots | Start-end (s) or ending event | Player knows before | Event that changes it (seen or heard) | Whose intention is active | Question carried into the next beat | What the player sees / feels | Fixed (value + source) | Open per craft (camera / anim / vfx / sound / environment / UI / model) | Owner notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | <A, B> | <until the player notices the beacon> | | | | | | | | |

## Gameplay state sheet (cinematics only; agree with the game designer and engineering)
| Item | Value |
| --- | --- |
| When control stops or is limited | |
| What the player's avatar does | |
| What keeps running elsewhere (NPCs, hazards, timers, other players) | |
| What can interrupt the scene | <death, respawn, teleport, a newer scene, disconnect> |
| Audience (shared scenes) | <one player / party / everyone; what a late joiner sees> |
| Skip policy | <individual / unanimous / host / fixed shared start; shown to players how> |
| Who decides completion | <server event vs one client's playback> |

| Ending | Resulting story state | View the player gets | First safe action | Server transition requested |
| --- | --- | --- | --- | --- |
| Finish | | | | |
| Skip | | | | |
| Failure (missing asset, actor removed, camera taken) | | | | |
| Death or respawn | | | | |
| Disconnect and rejoin | | | | |
| Late join (shared) | | | | |
