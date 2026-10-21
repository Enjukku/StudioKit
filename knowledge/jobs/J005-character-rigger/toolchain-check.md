---
type: log
scope: universal
status: active
updated: 2026-10-21
source: J005 lead, 2026-10-21
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Toolchain check before G2

| Check | Result | Evidence |
| --- | --- | --- |
| Blender MCP GUI server (localhost:9876) | not running (Blender closed) | MCP error 2026-10-21 |
| Blender MCP CLI tool | needs BLENDER_PATH env var (owner applies settings); not used | MCP error |
| Blender headless | Blender 5.1.2 at C:\Program Files\Blender Foundation\Blender 5.1\blender.exe (4.3 also installed) | probe script output |
| FBX add-on | 5.15.0; `roblox_fbx.check_exporter()` = [] (every option name exists) | probe |
| rig_audit Blender layer | clean two-part rig PASS (body delta 0.0 at head yaw ±60, pitch 30); planted chest weight leak FAIL (0.6042 at yaw 60); FBX rest export ran | self-test script |
| Teddy source (Tripo) | 1 mesh, 9,403 triangles, 1,301 open edges, 298 connected parts, 1 material, 1 UV map, no vertex groups | peek script (rig_audit.audit_mesh) |
| Roblox Studio MCP | 1 instance: the owner's live game place; not used for tests (needs a separate test place) | list_roblox_studios |
| Rig test place | owner opened a new place 2026-10-21; Studio MCP lists one instance "Place2" (id dd6838e7-c6d6-412f-b3ee-6e0fdfb46dde); used as the rig lab | list_roblox_studios |
| Studio import route | digest item 2 unanswered → default: the owner clicks File > Import when the rig is ready | owner chat 2026-10-21 |
