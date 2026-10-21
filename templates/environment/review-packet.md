---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J008; environment paper notes (knowledge/reference/environment/03-pipeline-performance-review.md §7: RA01-RA03, RC01-RC15, RS01-RS07, MP01-MP08, RJ01-RJ05); first-game review practice (04-first-game-stages.md FS-V01..V09)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Review packet: <stage-id> · revision <n>

Workflow: `environment-design/references/review.md`. Copy to `content/stages/<stage-id>/review/packet.md`; images and clips beside it. The environment designer fills it **before the owner sees anything**. Every check is labelled **gate-verified / MCP-verified / owner-confirmed / not verified**. A check passes only against an approved contract or a measured project limit; with neither, it is `UNVERIFIED`, never PASS. Listening cannot be judged from images: sound checks stay "auditory acceptance pending" until someone listens.

## A. Build record
| Key | Value |
| --- | --- |
| stage revision / place file / .blend revision | |
| blueprint revision approved | |
| ambience map revision | |
| Studio instance (studio_id) and place | test place, never a live game place |
| graphics settings captured | low quality / high quality / phone Automatic |
| time of day and weather states captured | |
| what changed since the last packet | |

## B. Camera set (one named camera per risk, with position, target and FOV, so anyone can repeat it)
| Camera id | Kind (player-eye approach, decision point, reverse route, high overview, top-down layout, contact close-up, skyline, scale-with-player, stress scene) | Position / target / FOV | Image (low quality) | Image (high quality) | Compared with (reference image or blueprint sheet) |
| --- | --- | --- | --- | --- | --- |

Minimum for any stage: player-eye views along the whole route (approach, decision, after commit, return), front / sides / back / high 3/4 of every structure, one top-down of the whole stage, one scale shot with the player figure per area, and low oblique or under-roof views of stepped roofs and overhangs. Move the camera or character into the content before capturing (streaming draws only what is near).

## C. Look checks
| # | Check | Result | Evidence (camera ids, files) | Label |
| --- | --- | --- | --- | --- |
| 1 | Route guidance: at each decision point the next move reads | | | |
| 2 | Focal hierarchy: the landmark stays visible and distinct with normal UI and effects | | | |
| 3 | Scale and passage: openings pass the collision envelope; rooms and furniture make sense at player size | | | |
| 4 | Camera clearance: no bad clipping while moving or turning | | | |
| 5 | Lighting readability at low and high quality | | | |
| 6 | Atmosphere: sightlines usable; depth and mood match the reference | | | |
| 7 | Contact: nothing floating; intended overlaps recorded | | | |
| 8 | Finish: every visible face finished; every enterable room dressed; directional pieces face right | | | |
| 9 | Repetition: no unintended pattern on a long approach or a sideways pan | | | |
| 10 | Cohesion: shape, palette, material and detail match the art bible version, with characters, UI and VFX in view | | | |
| 11 | Iconic traits of each structure read at play distance | | | |

## D. Ambience checks
| # | Check | Result | Evidence | Label |
| --- | --- | --- | --- | --- |
| 1 | Map vs place: every zone and source id exists in the place, nothing unlisted (scene audit) | | | |
| 2 | Every source has a visible cause at its anchor | | | |
| 3 | Borders: approach, crossing, walking back, standing still, teleport, respawn | | | |
| 4 | Streaming: leave → return → leave, no doubled loops, no missing source | | | |
| 5 | Sound and picture agree (timestamped clip pair) | | | |
| 6 | Listening review by the sound designer or the owner | auditory acceptance pending until done | | |

## E. Structure and budget (scene audit + measurements)
| Measure | Value | Budget and its source | Verdict (PASS / FAIL only with a budget; else MEASURED) |
| --- | --- | --- | --- |
| floating parts | | 0 (contract) | |
| buried / hidden parts | | 0 (contract) | |
| parts outside the play area | | 0 (contract) | |
| parts / meshes per zone | | | |
| lights / shadow casters per zone | | | |
| audio sources / effects per zone | | | |
| phone frame time, memory (busiest overlap, gameplay on) | | | |

An editor or emulator number is never presented as a phone result.

## F. Open issues, exceptions, weakest points
| # | Issue (observed fact, kept apart from guesses) | Severity | Responsible craft | What must be kept | Evidence needed to close |
| --- | --- | --- | --- | --- | --- |

List the 3 weakest points left, even when every check passes.

## G. Owner decision
| Date | Owner's words |
| --- | --- |
