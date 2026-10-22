> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Reference for `film-craft`. Tool: `tools/film/shotlist.py` (J015-T08, 47 offline tests; Blender 5.1.2 round trip run 2026-10-21 with no drift). Field guide for people: `templates/film/shot-list.md`. Owner decision J015-D5 / D7: one machine-readable shot list keeps timings the same in the plan, the previs and Roblox. Revised by J018 maker film-director · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§2 what the commands do not judge, from runs on sample files).

# The shot list file: one timing truth for plan, previs and Roblox

## 1. The file
One `<sequence>.shots.json` per sequence (format `film-shotlist/1`), kept at `content/film/<sequence>/` in the game. Start from `templates/film/shotlist.example.json` (the paper's 5-shot boss reveal, all lengths UNKNOWN).

| Key | Meaning |
| --- | --- |
| `sequence`, `title`, `revision` | id (kebab-case), name, revision ≥ 1 (every change that touches timing or meaning raises it) |
| `stage` | `plan` → `boards` → `previs` → `locked` (owner approved the timings) → `runtime`. UNKNOWN lengths, FOV and cue offsets are allowed only at `plan` and `boards` |
| `fps` | `[num, den]`: 24 → `[24,1]`; 29.97 → `[30000,1001]`. The project's choice (owner decision); the first game proposed 24 for a rendered video (N4 V-03) |
| `start_frame` | Blender scene start (default 1) |
| `aspect` | review display aspect, e.g. `[16,9]` |
| `fov_mode` | the Roblox `FieldOfViewMode` the `fov_deg` values assume; `Vertical` for authored shots |
| `board_policy` | `constraint` or `layout-may-propose` (`film-direction` scene-studies, disagreements) |
| `shots[]` | edit order. Required: `id`, `frames`, `size`, `angle`, `lens`, `movement`, `action`, `sound`, `emotion`, `transition` (the owner's 10 fields; number = `id`, length = `frames`). Optional: `rev`, `purpose`, `continuity`, `approval`, `evidence`, `fov_deg`, `camera`, `notes` |
| `cues[]` | `id` (dotted: `sfx.beacon.pulse`, never equal to a shot id), `shot`, `at` (frame offset from the shot's first frame, or UNKNOWN), `kind` (sfx, music, vo, ambience, vfx, anim, ui, camera, other), `sync` (locked, flexible, pending), optional `end` (frame offset, may run into later shots), `note` |

- **Timing rule:** shot start = `start_frame` + the earlier shots' frames; a shot covers `[start, start + frames)`; seconds = `(frame - start_frame) * den / num`, exact. A missing length is `"UNKNOWN"`, never 0. Shots after an UNKNOWN shot have an UNKNOWN start.
- **Markers:** `shot:<id>` markers may be bound to `CAM_<id>`; `cue:<id>` markers stay unbound (a bound marker cuts the camera). Exports made before cue markers existed show "missing cue marker(s)" until the next full push.
- **Shot ids are stable.** A rename is a new id; `diff` then shows one missing and one extra marker and `--write` refuses: rename on purpose, then re-push.
- **Lens:** `"UNKNOWN"`, free text, or `{focal_mm, sensor_mm, sensor_fit}`; with the object, `check` computes the vertical FOV. `fov_deg` is the Roblox `Camera.FieldOfView` (vertical degrees, 1-120). A lens without its sensor and fit is not a lens spec.
- Empty text fields are errors: write UNKNOWN.

## 2. Commands
| Command | Use |
| --- | --- |
| `python tools/film/shotlist.py check <file> [--json] [--fov-tol-deg D --tol-source S]` | after every edit; exit 1 = errors; open items listed |
| `table <file>` | the Markdown shot list for the owner and the crafts |
| `cues <file>` | the cue sheet for the sound designer (sorted by time) |
| `blender <file> --out push.py [--props-only]` | full push: fps / fps_base, frame range, one `shot:<id>` marker per shot start (camera `CAM_<id>` bound if it exists), one unbound `cue:<id>` marker per cue with a known `at`, sequence and revision; deletes only `shot:` and `cue:` markers; refuses UNKNOWN lengths. `--props-only`: rate and sequence properties only, allowed while lengths are UNKNOWN (first animatic) |
| `blender-export --out export.py` | script that writes the animatic's timing JSON with `shot:` and `cue:` markers (`-- out.json` argument, or `export(path)` in Blender MCP) |
| `diff <file> <blender.json> [--write]` | drift between plan and animatic: rate, range, missing / extra / out-of-order markers, per-shot start and length drift and per-cue drift in frames and ms. A shot or cue with UNKNOWN plan timing is "not compared"; exit 0 means everything was compared and nothing differs. `--write` takes shot lengths and cue `at` from Blender (revision + 1); it first prints the Blender range and the length the last shot will get (from the scene's end frame): read it before you accept; it refuses when a cue marker lies outside its shot, on extra or duplicate markers, or when the end frame is before the last shot marker. Cue `end` is not round-tripped: edit it by hand |
| `luau <file> --out <Name>.luau` | generated `--!strict` ModuleScript for the Roblox player (shots and cues with frames and seconds). Refuses UNKNOWN lengths or cue offsets. Never edit the output |
| `log-diff <file> <log.json> [--tol-ms MS --tol-source S [--early-ms MS]]` | compare a Roblox playback log (`[{id, t}]`, seconds from sequence start) with the plan: per id planned vs measured, ms and frames; no default tolerance |

**What the commands do not judge** (found by running them on sample files):
- `check` passes a shot list whose shots all have the same length: rhythm is read by you from its per-shot output (review line B-10).
- `log-diff` without `--tol-ms` reports `measured` and exits 0 even when planned ids are missing from the log: read the "planned, not logged" line; with a tolerance, a missing id fails.
- `log-diff` compares each id with its planned time. `--tol-ms` alone is symmetric (a cue 33 ms early passes `--tol-ms 40`); add `--early-ms 16.7` for the one-sided sync window (−16.7 ms to +40 ms). It still judges against the plan, not against the picture event, so pair each `sync: locked` sound cue with its picture event from the same log and read the sign; a planned lead or delay keeps its offset in the cue's `note` (review line R-04).
- `log-diff` matches ids exactly: a log that writes `shot:A` instead of `A` lists every shot as "planned, not logged" and "logged, not planned", still with verdict `measured` and exit 0. Log ids are the shot ids and `cues[].id` as in the file (`references/roblox-assembly.md` §3).

Pushing does not save the `.blend`: save it after the push (in the MCP session, or add a save call when running headless). The push writes the rate exactly as `fps = num`, `fps_base = den` (29.97 → 30000 / 1001.0); Blender's own 30 / 1.001 is stored as a 32-bit float and is off by about 1.4e-6 fps (FB FC-08). `diff` still accepts that older form.

## 3. The round trip
1. **Plan** (`stage: plan`): write shots and cues from the beat sheet; lengths UNKNOWN or event-bounded in `notes`. `check`; `table` for the owner.
2. **Boards** (`stage: boards`): panels named by shot id (`templates/film/storyboard-brief.md`).
3. **Previs:** `blender --props-only` sets the rate and the sequence properties while lengths are UNKNOWN; block the animatic with cameras `CAM_<id>`, a `shot:<id>` marker at each cut and a `cue:<id>` marker at each cue event; time the shots (the owner may direct timing on the animatic). `blender-export` → `diff --write` fills shot lengths and cue offsets; before the first write, check the scene's end frame is the last cut you intend (the last shot's length comes from it). Then push normally. Set `stage: previs`; `check` must pass with no UNKNOWN.
4. **Locked:** after the owner approves timing, set `stage: locked`. From now on a timing change is a new revision with its affected cues listed (`references/review.md` §5).
5. **Runtime:** `luau --out` into the game's source (path from the architect); the player logs shot and cue times in a test build; `log-diff` against the plan. Set `stage: runtime` when the capture matches.

The tool never judges whether a cut, a length or a lens works; it keeps the numbers the same everywhere.
