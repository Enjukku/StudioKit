> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Tool: `tools/env/scene_audit.py` + `tools/env/scene_probe.luau` (J008-T08; offline tests `tools/tests/test_scene_audit.py`). MCP facts: `knowledge/reference/environment/fact-check-performance-import.md` (PI59-PI67, tool-name table). Review rules: `environment-design/references/review.md`. Packet: `templates/environment/review-packet.md`.

# Scene audit, captures and the review packet

## 1. Scene audit (structure a screenshot hides)
The probe only reads the scene and prints JSON; the Python part checks it.
1. Print the probe with its settings: `python tools/env/scene_audit.py probe --root Workspace/<StageFolder>` (large stages: `--chunk-size 60000 --chunk 1`, then `--chunk 2..n`).
2. Run it in Studio: `mcp__Roblox_Studio__execute_luau` with `studio_id` (from `list_roblox_studios`), `datamodel_type: "Edit"`, `code`: the printed source. Save the output (all slices) to `content/stages/<stage>/review/probe-*.txt`.
3. Audit: `python tools/env/scene_audit.py audit --probe <files> --map content/stages/<stage>/ambience-map.md [--budgets <json>] [--floating-tol X --buried-tol Y --oob-tol Z] --out content/stages/<stage>/review/audit.json` (writes JSON and a Markdown table; exits 1 on FAIL).
| Check | What it reports | Limits (state them in the packet) |
| --- | --- | --- |
| floating | visible anchored parts with nothing under them within the tolerance, with the gap | bounding-box contact; the lowest part of a stack or a baseplate lists as floating |
| buried | parts whose top is under the terrain surface at their centre, or fully inside another opaque part's box | caves and overhangs read as buried; water ignored |
| out of bounds | parts outside the `PlayArea` parts' union | `NOT_CHECKED` without a PlayArea |
| per-zone counts | parts, MeshParts, lights by class, lights with shadows, CastShadow parts, audio by class, effects, particle emitters; plus unzoned and unpositioned | membership by centre point |
| triangles | `UNKNOWN`: no documented API | count in Blender on the evaluated mesh instead |
| map vs place | map zones or sources missing in the place, place ids missing in the map, unlisted audio under the stage root, kind mismatches, duplicate source ids: **FAIL** | music and UI audio outside the stage root are listed as global audio, not a failure |
Verdicts: `MEASURED` unless a tolerance or budget is passed; `PASS` / `FAIL` against it; `UNVERIFIED` when a field is unknown. Never invent a tolerance: budgets come from the owner or a phone measurement. Not yet verified in Studio until the first real run (J008 G2): output size limits of `execute_luau`, rays that start inside terrain.

## 2. The camera set in Studio
- `mcp__Roblox_Studio__screen_capture` takes `studio_id`, a `capture_id` (for example `"ScreenCapture_1"`) and optional `camera_position` and `look_at_position` as `[x, y, z]` (PI63). It captures the edit-time screen.
- Write the camera list first (packet §B): id, kind, position, target, FOV. Use the same list for every round so before / after compare.
- Player-eye views: camera at the avatar's eye height on the route (from the scale sheet), looking at the next cue. Top-down: high above the stage centre looking straight down. Scale shots: the player dummy in frame.
- Low and high quality: Studio's Editor Quality Level changes what post effects show (LD159); the quality level itself is not scriptable (LD131), so set it by hand or ask the owner, and record which level each capture used.
- Streaming: move the camera or character into the content before capturing (FS-V09). Restore the owner's edit camera afterwards (FS-V03).
- Play-mode checks (walks, borders, streaming): `start_stop_play`, then `character_navigation` / `user_keyboard_input` (datamodel_type Client); `get_console_output` for errors. One Studio driver at a time.

## 3. Blender renders
`render_viewport_to_path` or `render_thumbnail_to_path` from named cameras that match the reference image angles; place each render beside its reference on one labelled sheet (FS-V02). Renders prove look and silhouette of Blender-built pieces only; Studio decides the final look. Preview lighting can shift colours (white reads grey, pastel reads olive). Check the render set-up first, ambient fill and exposure before anything else: put a white / grey / palette test card in the render scene, store the render recipe (lights, ambient, exposure, colour management) with the renders, and judge final colour in Studio under the game's lighting before touching any palette value.

## 4. Packet assembly
Fill `review-packet.md`: build record, camera table with both quality levels, look checks, ambience checks (listening stays pending until someone listens), audit numbers with their limits, budgets with sources, open issues with the responsible craft, the 3 weakest points. Then hand to the owner (or the art director / studio operator first, as the brief says).
