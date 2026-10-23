---
type: job
scope: game
status: draft
updated: <date>
source: <job-id>
supersedes: []
revision: 1
---
> Author: film-director · <model id> · <effort> · <date>
<!-- Template: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; beat contract, state-change columns and gameplay state sheet added by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J015, film-direction skill §3); frontmatter, beat ids, consumers and change table added by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3. Used for cutscenes, key moments and effects; it is the cutscene contract (one writer: the film-director). Copy to the job folder or `knowledge/design/moments/<moment-id>.md`. Shots, exact timings and cues live in the shot list (`templates/film/shotlist.example.json`), not here. Revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): problem-to-budget contract rows, intensity and resistance columns, options and pick. -->

# Beat sheet: <job-id or moment-id>

> Status: PROPOSAL until the owner approves the beat contract (decision id: <>). The revision is in the frontmatter; every change adds a row to the change table at the end.

## Beat contract (owner approves this first)
What each row must hold: `film-direction` §3 step 1; checked by `film-craft/references/review.md` P-01.

| Field | Value |
| --- | --- |
| Problem and constraints | <the problem the moment solves; devices, play camera, cast and rig limits, sets, platform limits> |
| Premise | <one sentence> |
| Hook | <one line: what makes this moment compelling> |
| Target experience | <the job card's line: kind of fun + the sentence of what the player must feel or believe; the game profile's target when the card has none> |
| Sell list (2-4) | <1 …, 2 …: what the player must feel or know after it> |
| Budget and stop criteria | <options, passes, images; floor: the success test; bar: the signs a top director needs to see before shipping (`rules/messages.md` §2)> |
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
One row per beat (`film-direction` §3 step 3; checked by P-05). A beat that changes neither understanding nor feeling is cut or merged. Beat ids (`B01`, `B02`, ...) are stable: never renumber; a new beat takes the next free id. Times are filled from the shot list after previs; before that write the event that ends the beat. Event ids are the shot list's cue ids (`cues[].id`, e.g. `sfx.beacon.pulse`) that VFX, sound and the animator key to.

| Beat | Shots | Event ids (shot list `cues`) | Start-end (s) or ending event | Player knows before | Event that changes it (seen or heard) | Whose intention is active | Question carried into the next beat | What resists | Intensity (calm / rising / climax) | What the player sees / feels | Fixed (value + source) | Open per craft (camera / anim / vfx / sound / environment / UI / model) | Owner notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B01 | <A, B> | <sfx.beacon.pulse> | <until the player notices the beacon> | | | | | | | | | | |

## Options and pick (key beat)
How the options are made, shown and picked: `film-direction` §3 step 4 and `film-craft` §3 step 3; checked by P-04.

Research board: <path> · Key beat: <B0n>

| Approach | Hook (one line) | Non-obvious | Contact sheet (path) | Why it lost (or "picked") |
| --- | --- | --- | --- | --- |
| A | | yes / no | | |

| Item | Value |
| --- | --- |
| Goal question (against the sell list) | <"which makes the threat read first at phone size?"> |
| Pick | <approach; owner decision id> |

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

## Consumers (the job's dependency map for this contract)
| Consumer (role) | Beats and event ids it builds on | Its outputs built on this sheet (path) |
| --- | --- | --- |
| animator | | |
| vfx-designer | | |
| sound-designer | | |
| environment-designer | | |
| ui-ux-designer | | |
| feature-builder | | |

## Change table
A change to a beat or event id that a consumer builds on is a contract change (`rules/messages.md` §5): add the row, notify each consumer, mark their outputs stale.

| Revision | Date | What changed | Consumers to recheck | Acknowledged by |
| --- | --- | --- | --- | --- |
