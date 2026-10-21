---
type: log
scope: universal
status: active
updated: 2026-10-21
source: J005 G2 test (teddy), build-agent step 6
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# G2: where the skills and templates were unclear (fix after the test)

| id | stage | found by | gap | proposed fix | status |
| --- | --- | --- | --- | --- | --- |
| GP01 | S1 | animator stand-in | Rig sheet has no `priority` (must / should) or fallback field for animator needs | add `priority: must | should` and `fallback:` to the animator keys | open |
| GP02 | S1 | animator stand-in | No guidance for a root record (P00) | add a root record to the template (root, movement owner, in-place) | open |
| GP03 | S1 | animator stand-in | No rule for texture-only parts (painted eyes) or many loose decorations (297 stitch pieces) | rig-pipeline S1: one record per decoration group; texture-only parts get `moves: no` + note; rigger decides at S2 | open |
| GP04 | S1 | animator stand-in | Line endings: sheet copies may be CRLF on Windows; diffs need --strip-trailing-cr | note in templates/rig README or keep LF via .gitattributes | open |
| GP05 | S0 | lead | No approved reference image for a test asset that already exists; K0 assumes one | rig-pipeline K0: an existing approved model may serve as the look target (decision line) | open |
| GP06 | toolchain | lead | Blender MCP GUI server not running; headless blender.exe works and is enough for S2-S5 scripts | rigging-craft blender-mcp.md: add the headless route (path, `-b --factory-startup --python`) as the default when the GUI is closed | open |
| GP07 | S3 | lead (from S4) | rig-pipeline / modeler-handoff do not say exposed caps and roots must carry the skin's texture and a rounded rim; the S3 build used a flat swatch and a knife-edge annulus | modeler-handoff avoid + check: "exposed root/socket carries continuous texture and shading; rims rounded, no flat annulus" | open |
| GP08 | S2 | lead (from S4) | rigging-design region-routes §4 mentions the sphere identity but S2 chose crease-following elongated rings (1.8:1, 2:1) without stating the consequence (joint surface shows at extremes) | region-routes §4: elongated ring → state the visible-joint consequence at S2 and render it in the K2 package | open |
| GP09 | S3 | lead | stand-in wrote renders outside the repo (C:\work\r_v1) | modeler-handoff rule: scripts and renders only inside the asset folder | open |
| GP10 | S4/S4b | owner | Checking cost too high: 64-79 poses × 6 views rendered and inspected each round, and repeated by both the sender (modeler self-check) and the receiver (rigger); weight-variant searches added more. Owner 2026-10-21: "this takes way too much usage, way too much time" | rig-pipeline + rigging-craft: a check budget. All poses as scripted numbers; images opened only for failing poses + ≤ 8 key poses (gameplay camera + one close view); sender self-check is numbers only; the full image set once at release; fix rounds may run at medium effort | fixed 2026-10-21 (J005-D8) |
