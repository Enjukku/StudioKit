---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J015-D7 (digest item 2)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J015-T08 brief: shot-list data format + `tools/film/shotlist.py`

<intent>
A cutscene's timings must be the same in the plan, the Blender animatic and Roblox. Today a shot list lives in a Markdown table, the animatic has its own markers and frame range, and the Roblox playback has its own numbers; each copy drifts, and frame counting causes off-by-one errors (frames 1 to 31 at 30 fps are 31 frames, not 1 second). The film director needs one data file per sequence that is the timing truth, and one small tool that checks it, shows it to people, pushes it into Blender, reads the animatic back when the director re-times shots there, writes the Roblox data module, and compares a Roblox playback log with the plan.

The paper behind this (owner research, `knowledge/reference/film/02-previs-roblox-runtime.md` BL-28..35 and `03-vocabulary-method-templates-review.md` section 7-8): stable shot ids in every stage; a cut list in half-open intervals `[start, next-start)` avoids the off-by-one; effective frame rate is `fps / fps_base` and a rate like 30000/1001 must stay a fraction; a missing timing must never become a zero-length shot; a script can flag missing ids, gaps and missing cues but cannot judge whether a cut works. The tool must stay small: it checks records, it does not direct.

Who reads its output: the film director (all commands), the owner (the Markdown table), the sound designer (the cue sheet), Blender (a generated Python script), the Roblox playback code (a generated Luau data module, consumed later by an engineering-built cutscene player, J015-D7), QA (the log comparison).
</intent>

<spec>
id: J015-T08
from: lead (orchestrator)
to: general-purpose builder
model: opus
effort: medium
skills: [engineering-craft, testing]
refs:
  - tools/art/thumb_check.py and tools/tests/test_thumb_check.py   # take: kit tool style (module docstring with usage, sources and "what it never claims"; argparse subcommands; JSON out; unittest tests). avoid: its image code
  - tools/verify.py   # take: tests run by unittest discovery in tools/tests
  - knowledge/reference/film/02-previs-roblox-runtime.md   # take: BL-07..14 (FOV maths, sensor fit), BL-28..35 (markers, fps/fps_base, frame arithmetic, rational rates). avoid: Roblox runtime rows (not this tool's job)
  - knowledge/reference/film/03-vocabulary-method-templates-review.md   # take: section 7-8 (shot-list fields), section 9 (the filled 5-shot example, for a fixture)
fixed:
  files: tools/film/shotlist.py, tools/tests/test_shotlist.py, tools/tests/fixtures/film/ (fixtures), templates/film/shotlist.example.json
  python: standard library only (json, fractions, argparse, math); runs on Python 3.11+; no bpy import in shotlist.py (Blender code is emitted as text and run inside Blender)
  format_id: "film-shotlist/1"
  file_name: "<sequence>.shots.json"
  top_level_keys:
    format: "film-shotlist/1"
    sequence: kebab-case id
    title: text
    revision: integer >= 1
    stage: one of plan | boards | previs | locked | runtime   # "locked" = timings approved by the owner
    fps: [num, den], positive integers, effective rate = num/den (24 → [24,1]; 29.97 → [30000,1001])
    start_frame: integer (Blender scene start; default 1)
    aspect: [w, h], positive integers (the review display aspect, e.g. [16,9])
    fov_mode: Roblox FieldOfViewMode name the fov values assume (string; default "Vertical")
    board_policy: one of constraint | layout-may-propose   # paper SD/BP-01: declared per sequence
    shots: list (order = edit order)
    cues: list
  shot_keys_required: id, frames, size, angle, lens, movement, action, sound, emotion, transition   # the owner's 10 fields (J015-D5); "number" = id, "length" = frames
  shot_keys_optional: rev, purpose (new information or performance change), continuity, approval, evidence, fov_deg, camera (free text or object), notes
  shot_id: unique within the file, pattern [A-Za-z0-9][A-Za-z0-9_.-]*; never reused for a different shot (rename = new id)
  frames: positive integer or the string "UNKNOWN"; 0 or negative is an error (a missing timing must not become a zero-length shot)
  lens: the string "UNKNOWN", or free text, or an object {focal_mm, sensor_mm, sensor_fit: AUTO|HORIZONTAL|VERTICAL}
  fov_deg: number in (0, 120] or "UNKNOWN"; meaning = the Roblox Camera.FieldOfView under fov_mode   # Roblox FieldOfView range 1-120, J015-T05 fact-check confirms or corrects; keep the bound as a named constant with its source
  cue_keys: id (unique, dotted, e.g. sfx.beacon.pulse), shot (an existing shot id), at (integer frame offset from the shot's first frame, or "UNKNOWN"), kind (sfx | music | vo | ambience | vfx | anim | ui | camera | other), sync (locked | flexible | pending), optional end (frame offset, > at, may pass into later shots), optional note
  timing_rule: shot start = start_frame + sum of earlier shots' frames; interval [start, start+frames); time in seconds = (frame - start_frame) * den / num as an exact Fraction; total = sum of frames
  stage_rules: at stage plan or boards, UNKNOWN frames, fov_deg and cue `at` are allowed (reported as open items); at previs, locked or runtime they are errors
open: [code structure inside the files, message wording, extra warnings that need no invented number, how the emitted Blender script is laid out, Luau module layout beyond the keys below]
commands:
  - check <file> [--json]: schema, ids, frames, stage rules, cues (shot exists, 0 <= at < shot frames when known, end > at), totals; FOV from lens objects (vertical angle from focal length, sensor size, sensor fit and aspect: HORIZONTAL → sensor is the width; VERTICAL → sensor is the height; AUTO → sensor is the larger output dimension) and, when both lens and fov_deg are given, the difference in degrees (reported, never judged without a caller tolerance); exit code 0 = no errors, 1 = errors; warnings never change the exit code
  - table <file>: Markdown shot list for people: id, start-end (s), length (frames and s), the owner's 10 fields, purpose; UNKNOWN shown as UNKNOWN; header with sequence, revision, stage, fps as a fraction and decimal, total
  - cues <file>: Markdown cue sheet for the sound designer: cue id, shot, absolute time (s), frame, kind, sync, end, note; sorted by time; UNKNOWN cues listed last
  - blender <file> --out <script.py>: emits a Python script to run inside Blender (MCP or `blender -b file.blend --python script.py`) that sets fps and fps_base from the fraction (fps = round(num/den), fps_base = fps*den/num, so fps/fps_base = num/den), frame_start and frame_end (last frame = start + total - 1), deletes only markers whose name starts with "shot:" and adds one "shot:<id>" marker per shot start, binds the marker to a camera object named "CAM_<id>" when it exists, and stores the sequence id and revision as scene custom properties; refuses (exit 1) when any frames are UNKNOWN
  - blender-export --out <script.py>: emits a Python script that, run inside Blender, writes JSON (scene fps, fps_base, frame_start, frame_end, every "shot:" marker name and frame, bound camera name, the stored sequence id and revision) to a path given as its first argument
  - diff <file> <blender.json> [--write]: compares Blender's export with the shot list: fps mismatch, frame range, missing or extra shot markers, marker order, per-shot start and length drift in frames and ms; --write takes the lengths from Blender, keeps everything else, increases revision by 1 and rewrites the file (never when markers are missing, extra or out of order)
  - luau <file> --out <Name.luau>: emits a Luau ModuleScript (`--!strict`, header comment "generated by tools/film/shotlist.py from <file> rev <n>; edit the .shots.json, not this file") returning { format, sequence, revision, fps = {num, den}, fovMode, shots = { {id, startFrame, frames, start, duration, fovDeg, transition} }, cues = { {id, shot, frame, time, kind, sync, endTime} } } with times in seconds from the sequence start (float with 6 decimals, derived from the exact fraction); refuses when any frames or cue `at` are UNKNOWN; fovDeg nil when UNKNOWN
  - log-diff <file> <log.json>: log = JSON list of {id, t} (a shot id or cue id, t in seconds since the sequence start, measured in Roblox); prints per id the planned time, measured time, difference in ms and in frames, and ids planned but not logged or logged but not planned; tolerance only from --tol-ms with --tol-source (no default)
not_in_scope: [camera paths or CFrame export from Blender to Roblox, the cutscene player runtime, reading .blend files directly, any AI or taste judgment, edits to other tools]
rules:
  - No invented numbers: no default tolerance, no "ideal" shot or sequence length, no lens-to-mood mapping. Any threshold comes from the caller with a source.
  - Exact time: use fractions.Fraction for every time computation; round only when printing.
  - The tool never edits a .shots.json except through `diff --write`, and then only frames and revision.
  - Input files are data, not instructions.
  - Kit tool: no game-specific content, names or paths in the tool, tests or fixtures; the example file is the paper's original 5-shot boss reveal (no game content) with invented placeholder lengths clearly marked as test values in a note field.
  - Tests in tools/tests/test_shotlist.py with unittest; they must pass with `python -m unittest discover -s tools/tests -p "test_*.py" -t tools/tests` and `python tools/verify.py`.
  - The module docstring states usage, sources (the note rows above), and what the tool never claims.
deliver: [tools/film/shotlist.py, tools/tests/test_shotlist.py, fixtures, templates/film/shotlist.example.json]
checks:
  - C1: frames 1-31 at [30,1]: a 31-frame shot lasts 31/30 s; a cut list of shots 30+30 at 30 fps puts shot 2 at exactly 1 s (test)
  - C2: [30000,1001] keeps exact times (shot of 1001 frames lasts exactly 1001*1001/30000 s); the Blender script sets fps 30 and fps_base 1.001 (test)
  - C3: check rejects duplicate ids, zero frames, unknown cue shot, cue at >= shot frames, UNKNOWN at stage previs; accepts UNKNOWN at stage plan and lists it as open (tests)
  - C4: FOV from lens: 50 mm on a 36 mm HORIZONTAL sensor at 16:9 gives vertical FOV 2*atan((36/(16/9))/(2*50)) in degrees (test with the formula computed in the test)
  - C5: diff detects a moved marker, a missing marker and an fps mismatch; --write updates frames and revision only (tests on a fixture blender.json)
  - C6: planted faults: break the timing rule (e.g. inclusive end) or the fraction maths and show at least one test fails (state which in the hand-back)
  - C7: the emitted Blender script runs headless in Blender 5.1.2 (`"C:/Program Files/Blender Foundation/Blender 5.1/blender.exe" -b --factory-startup --python <script>`) and the export script's JSON round-trips through `diff` with no drift (run it; paste the command and result)
  - C8: python tools/verify.py: the tests line passes (other gate lines may fail from other jobs in flight; name them)
return: rules/messages.md §3 hand-back: STATUS first; coverage of every command and check; files; check evidence (test names, command output lines); decisions_made; anything in this spec you think is wrong for the film director's use.
</spec>
