---
type: template
scope: universal
status: active
updated: 2026-10-22
source: J008; environment paper notes (knowledge/reference/environment/03-pipeline-performance-review.md §7: RA01-RA03, RC01-RC15, RS01-RS07, MP01-MP08, RJ01-RJ05); first-game review practice (04-first-game-stages.md FS-V01..V09)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21; revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6)

# Review packet: <stage-id> · revision <n>

Workflow: `environment-design/references/review.md`. Copy to `content/stages/<stage-id>/review/packet.md`; images and clips beside it. The environment designer fills it **before the owner sees anything**. Every check is labelled **gate-verified / MCP-verified / owner-confirmed / not verified**. A check passes only against an approved contract or a measured project limit; with neither, it is `UNVERIFIED`, never PASS. Listening cannot be judged from images: sound checks stay "auditory acceptance pending" until someone listens.

## A. Build record
| Key | Value |
| --- | --- |
| stage revision / place file / .blend revision | |
| blueprint revision approved | |
| ambience map revision | |
| Studio instance (studio_id) and place | test place, never a live game place |
| graphics settings captured | lowest / highest graphics setting (`environment-design/references/review.md` §3; how: `environment-craft/references/measure-captures.md` M9) / phone Automatic |
| time of day and weather states captured | |
| what changed since the last packet | |

## B. Camera set (one named camera per risk, with position, target and FOV, so anyone can repeat it)
| Camera id | Kind (player-eye approach, decision point, reverse route, high overview, top-down layout, contact close-up, skyline, scale-with-player, stress scene) | Position / target / FOV | Image (lowest setting) | Image (highest setting) | Compared with (reference image or blueprint sheet) |
| --- | --- | --- | --- | --- | --- |

Pick the cameras by the stage's risks from the kinds in `environment-design/references/review.md` §3, not by a fixed count. Every stage has the key views of that section: the first view after spawn, the busiest moment, one decision view per zone, the top-down and one view per hazard. Move the camera or character into the content before capturing (streaming draws only what is near).

## C. Look checks (`environment-design/references/review.md` §7)
One row per §7 line; the line, its input and its numbers recipe are defined there (never copied here). Every line is re-rated every round, not only the failed ones (`review.md` §4). A fix job runs the §7 fix-job lines and marks the others `n/a (fix job)`. A line that cannot run is `not verified` and goes to the could-not-check list in §F.
| Line | Result (numbers, PASS / FAIL against a target with its source, or MEASURED) | Input used (captures, numbers files) | Label | Previous round result |
| --- | --- | --- | --- | --- |
| RD1 | | | | |
| RD2 | | | | |
| RD3 | | | | |
| RD4 | | | | |
| RD5 | | | | |
| RD6 | | | | |
| RD7 | | | | |
| RD8 | | | | |
| RD9 | | | | |
| RD10 | | | | |
| RD11 | | | | |
| RD12 | | | | |
| RD13 | | | | |
| VB1 | | | | |
| VB2 | | | | |
| VB3 | | | | |
| VB4 | | | | |
| VB5 | | | | |
| VB6 | | | | |
| VB7 | | | | |
| VB8 | | | | |
| VB9 | | | | |
| VB10 | | | | |
| VB11 | | | | |
| VB12 | | | | |
| VB13 | | | | |
| FL1 | | | | |
| FL2 | | | | |
| FL3 | | | | |
| FL4 | | | | |
| FL5 | | | | |
| FL6 | | | | |
| FL7 | | | | |
| FL8 | | | | |
| FL9 | | | | |
| FL10 | | | | |
| FL11 | | | | |
| FL12 | | | | |
| FL13 | | | | |
| AM1 | | | | |
| AM2 | | | | |
| AM3 | | | | |
| QV1 | | | | |
| QV2 | | | | |
| QV3 | | | | |
| QV4 | | | | |
| PS1 | | | | |
| PS2 | | | | |
| PS3 | | | | |
| PS4 | | | | |
| PS5 | | | | |

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

**Could-not-check list** (`review.md` §7 PS5)
| Step or §7 line | Missing input | What would close it |
| --- | --- | --- |

**Captures used against the image budget** (`review.md` §3; pass budget from the read plan, blueprint §L)
| Pass | Captures taken | Captures looked at | Budget for this pass | Over budget: why |
| --- | --- | --- | --- | --- |

## G. Owner decision
| Date | Owner's words |
| --- | --- |
