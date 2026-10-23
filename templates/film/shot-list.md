<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J015). Kit template: the field guide for a shot list. The data lives in `<sequence>.shots.json` (start from `templates/film/shotlist.example.json`); people read the table `python tools/film/shotlist.py table <file>` prints. Fields: the owner's 10 (J015-D5) plus the paper's record (N3 ST-01..13, ST-P01..12, CL-01..07; OPINION, 2026-10-21). Format and commands: `film-craft/references/shot-list-format.md`. Revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): picture plan and conventions tables. -->
# Shot list: <sequence> rev <n>

One record per shot. A shot boundary is an edit boundary; a change of staging inside one continuous take is a beat inside the same shot (N3 ST-00).

## Per-shot fields (JSON key → what to write)
| Owner field | JSON key | Write | Never |
| --- | --- | --- | --- |
| Shot number | `id` (+ `rev`) | stable id; a different shot gets a new id | reuse an id for a changed shot |
| Length | `frames` | measured frames from the animatic, or `"UNKNOWN"` (event that ends it in `notes`) | 0, or a number borrowed from a film or a mood |
| Shot size | `size` | subject scale and the context that must be visible | "cinematic" |
| Angle | `angle` | relation to the subject, eyeline, dramatic purpose | "low = power" as a rule |
| Lens | `lens` (+ `fov_deg`) | `{focal_mm, sensor_mm, sensor_fit}` or UNKNOWN; Roblox vertical FOV separately | a focal length without its sensor and fit |
| Movement | `movement` | type, start and end targets, the motivating event, what it reveals; speed UNKNOWN until measured | a move without a reason |
| Action | `action` | the visible character or world change and its continuity state | a pose name only |
| Sound | `sound` (+ `cues[]`) | exact approved line or cue id, perspective, sync intent | "epic music" |
| Emotion | `emotion` | the intended change ("curiosity becomes intention"), not a promised audience response | a single adjective |
| Transition | `transition` | cut or other transition and what motivates it | "cut on a timer" |
| (paper) Purpose | `purpose` | the new information or performance change this shot adds | |
| (paper) Continuity | `continuity` | eyeline, screen direction, prop state, action phase at the cut | |
| (paper) Approval question | `approval` | the observable criterion and the owner decision needed | |
| (paper) Evidence | `evidence` | source for borrowed facts; `OPINION` for original choices | |

## Before / after state (one line per shot)
These tables live with the printed shot list in one file, `content/film/<sequence>/shot-table.md`: the `shotlist.py table` output first, then the before/after table, the picture plan, the conventions table, then the continuity ledger.
| Shot | Player knows before | Player knows after | Subject | Screen position of the subject |
| --- | --- | --- | --- | --- |
| A | | | | left / middle / right |

## Picture plan (one line per shot)
What each column holds: `film-direction` §3 step 5 and `film-craft` §3 step 4; checked by `film-craft/references/review.md` P-03, B-03 (overlay zones) and B-06 (brightest area, planned silhouette).
| Shot | First-second read | Read order (primary / secondary / third) | Value key | Brightest area | Light direction | Overlay zones (bars, subtitles, skip, HUD at handoff) |
| --- | --- | --- | --- | --- | --- | --- |
| A | | | | | | |

## Conventions (one table per sequence)
Must match earlier cutscenes of the game and the art bible: `film-craft/references/review.md` P-09; `film-direction` §7 principle 7.
| Convention | Meaning in this game | Source (earlier cutscene, art bible row) |
| --- | --- | --- |
| Story colours | | |
| Light directions | | |
| Camera grammar | | |
| Motion material of title cards and graphic transitions | | |

## Continuity ledger (update at every cut)
| Shot | Character positions (map) | Travel direction (screen) | Eyeline target | Dominant light direction | Costume and prop state (which hand) | Entry / exit positions | Action phase at the cut |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | | | | | | | |

Every generated board and previs render carries the same shot id and revision. When an image contradicts the ledger, fix the image or revise the plan openly; never leave the contradiction for the animator (N3 CL, PM-03).
