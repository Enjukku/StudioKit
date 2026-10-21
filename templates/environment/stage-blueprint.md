---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J008; first-game stage practice (knowledge/reference/environment/04-first-game-stages.md FS-P01..P14, FS-S, FS-T, FS-B); environment paper notes (route contract G01, scale sheet SC02/SC08, built-where BW01-BW08, annotated reference CO02)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Stage blueprint: <stage-id> · revision <n>

Workflow: `environment-design` §3 steps 1-6. Copy to `content/stages/<stage-id>/blueprint.md`, with the sheet images in `content/stages/<stage-id>/blueprint/`. **The owner approves this blueprint before any building starts** (owner rule from the first game: a stage built without one was thrown away). Every sheet image shows a player figure at true size. Every number has a unit (studs) and a source (game designer's layout, owner D-id, measurement, or `PROPOSAL`).

## A. Stage card
| Key | Value |
| --- | --- |
| stage_id / revision | |
| hook (one sentence a player would repeat) | |
| feeling along the route | one line per area, in route order |
| layout source | game designer's route graph: path + revision (the route is theirs; changes are proposals in §J) |
| art bible version | path + version; this stage's dominant, secondary and accent colour |
| key-place reference images | approved image paths (reference-images skill, concept and environment families) |
| camera and player | camera mode, avatar envelope, walk speed, jump, other abilities, held items (source: game designer / runtime config) |
| scale convention | 1 stud = 28 cm unless the game profile says otherwise; any exaggeration listed in §D |
| target devices | named low-end phone(s); budgets come from the owner or a phone measurement, else `UNKNOWN` |
| players at once | |

## B. Set list (what players expect to find here)
| Item | Role in the stage (landmark / route cue / encounter / dressing / ambience cause) | Iconic traits that must read at play distance (2-3) | Source (modeler asset id, new request, or built here) |
| --- | --- | --- | --- |

Iconic, expected things before trivia. Plan every decoration, furniture type and outdoor prop here, so the layout and budget already know them.

## C. Site plan (top-down sheet + table)
| Zone / area | Footprint (studs) | Ground height range | Terrain type and layers | Paths in / out | Landmark seen from here | Ambience zone id |
| --- | --- | --- | --- | --- | --- | --- |

Sheet shows: zones, the route graph overlaid, the path network (every path joins the network or ends at a destination; every door meets a path), height bands, water, the play-area boundary and what it looks like, spawn, exits and climb-outs from every pit, river and high place. **Terrain with height changes in every area: no flat plane.**

## D. Scale sheet
| Measure | Value (studs) | Why (motion, envelope, margin) | Source |
| --- | --- | --- | --- |
| standard door / opening | | | |
| main path width | | | |
| ceiling / overhead clearance | | | |
| stair / ramp / climb | | | |
| exaggerated relations (what bends and why) | | | |

## E. Structures (one per building or landform; plan per floor, elevations, one section)
| Structure | Sheets (plan per floor, front, side, back, section) | Faces players can see (all must be finished: windows or equal detail) | Rooms players can enter (all furnished and dressed) | Facing (main face toward the route) |
| --- | --- | --- | --- | --- |

Before approval, compare **each elevation with the reference silhouette**: a boxy blueprint makes a boxy build. Read every sheet image yourself: labels readable, nothing floating, nothing inside walls, directional pieces facing the right way.

## F. Guidance per decision point
| Node | Approach | Intended next move | Cue (landmark, framed opening, light, material, sound) | Views to capture (approach, decision, after commit, return) |
| --- | --- | --- | --- | --- |

## G. Built where
| Element | Blender / Studio / split | Why | How it moves between them | Owner (environment designer or modeler request) |
| --- | --- | --- | --- | --- |

## H. Light, air and ambience plan (summary; details in the ambience map)
| Area | Time / weather state | Mood words from the art target | Readability that must survive low quality | Ambience zone and main causes |
| --- | --- | --- | --- | --- |

## I. Estimate and checks
| Item | Estimate | Budget and its source (or `UNKNOWN`) |
| --- | --- | --- |
| parts / meshes per zone | | |
| lights, shadow casters per zone | | |
| sound sources, effects per zone | | |
| new modeler requests | | |

Plan checks (script where possible, never by eye only): no overlaps; one connected path network; heights and exits; water levels against floors and walkways; the main walkway never interrupted by scenery; budget fit.

## J. Proposals to other owners, open questions, kept and cut
| # | To (game designer / art director / modeler / owner) | Proposal or question | Why | Default if no answer |
| --- | --- | --- | --- | --- |

## K. Approval
| Gate | Date | Owner's words |
| --- | --- | --- |
| blueprint approved | | |
