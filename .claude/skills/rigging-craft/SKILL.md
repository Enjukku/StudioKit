---
name: rigging-craft
description: Build and test a Roblox rig in Blender through Python and the Blender MCP, then prove it in Roblox Studio - inspect a model (connected parts, fused bridges, open edges, triangles), render the cut plan for the modeler, run the S4 proxy sweep and write one exact fix note, build the export skeleton and authoring controls, paint and clean weights (prune then normalize, max 4 influences, no Root weight), write the control manifest the animator uses, run the 12 test clips and the rig audit tool, export FBX with every option set by name (Blender's defaults are wrong for Roblox), import into Studio with the right rig type and Keep Zero Influence Bones, and record a test record with evidence. Use at rig-pipeline S4 and S5, when "the export looks wrong in Studio", "bones are missing after import", "the weights are broken", or when an animator reports a rig problem. Read rigging-design first (what and why); this is how.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Evidence: `knowledge/reference/rigging/` (notes 01-03; fact-checks RR Roblox, RB Blender, RT tools), `knowledge/reference/animation/02-*.md`. Tools: `tools/rig/rig_audit.py`, `tools/rig/roblox_fbx.py` (offline tests in `tools/tests/`). Tags: [V] verified, [E] experience, [O] studio opinion.

# Rigging craft: build, test and ship the rig

## 1. When this skill starts
After `rigging-design` produced the rig plan and the animator signed K2 (rig-pipeline S2). Needs: the rig sheet, the source snapshot, Blender running with the MCP add-on, Roblox Studio for S5 (`studio-mcp` skill).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Blender version rules, MCP rules, exact API calls, stage scripts | `references/blender-mcp.md` |
| Weight cleanup order, locality, deformation that Roblox runs | `references/weights.md` |
| Export skeleton, controls, control manifest, FBX profile, Studio import, runtime facts | `references/controls-export-import.md` |
| S4 proxy sweep, measurements, the 12 test clips, the 22-item release checklist | `references/tests.md` |
| Fix-note format | `templates/rig/fix-note.md` |
| Tripo endpoints, model ids, when Tripo output is good enough | `rig-pipeline/references/tripo-routes.md` |
| A symptom you need to trace | `rigging-design/references/diagnosis.md` |

## 3. Steps
1. **Version and scene.** Record Blender version, FBX add-on version, `roblox_fbx.check_exporter() == []` in the build manifest. Inspect the scene before changing anything. Check: manifest written.
2. **Inventory (S2 support).** Per mesh: triangles, open edges, connected parts (`rig_audit.audit_mesh`), materials, UV maps, size in studs; 6 orthographic renders, wireframe over shaded. Check: defect map in `tests/s2_inventory.json`.
3. **Plan renders.** Draw the cut lines and bend zones from §C over the model, 6 views, for the modeler brief. Check: each mark ties to a part id.
4. **S4 geometry acceptance.** When the modeler hands back: scripted checks (watertight, triangles, part count matches the plan), then the proxy sweep through every §B extreme from the 6 review views. Fail → **one** fix note with every failed item; max 2 rounds. Check: §G rows + §H sign-off.
5. **Skeleton.** Export bones by allowlist + parent map; pivots from §C (landmarks, not bounding boxes); rest orientation and roll kept; Root without weights; sockets for VFX / grips / hitboxes as non-deforming bones. Authoring controls (FK, IK + poles, switches) on top, only what the clip list needs. Check: rotation preview per joint; hierarchy dump.
6. **Weights.** Rigid parts: one bone at 1.0. Skinned zones: localized weights; then the cleanup order (remove non-deform groups → fill gaps → remove cross-body support → limit 4 → normalize, all with `group_select_mode='BONE_DEFORM'`). Check: `rig_audit.audit_weights` PASS.
7. **Control manifest.** One record per control (`references/controls-export-import.md` §3), ranges from §B. Check: every §B ROM appears as a min/max on a control.
8. **Tests in Blender.** The clips the asset needs from the 12 (`references/tests.md` §4) as named Actions; `rig_audit.audit_scene` with protected groups and sweeps, tolerances from §F (MEASURED if none). Combined stress poses. Check: §G filled; any FAIL goes back to step 4-6, not to polish.
9. **Export and round trip.** `roblox_fbx.export` rest + one file per clip; re-import into a fresh Blender scene; compare hierarchy, weights, sizes. Check: `tests/roundtrip.json`.
10. **Roblox import.** File > Import, Rig Type Custom (R15 only for avatar bodies), Keep Zero Influence Bones on when sockets or a weightless Root must survive; read every warning; check MeshParts, Bones, attachments, controller, Animator; play each test clip on the intended Animator; capture. Check: MCP-verified evidence in §G.
11. **Release.** All 22 checklist items PASS or BLOCKED with reason; hand the rig, manifest, test record and limits to the animator (S6). Then handle rig notes: triage each item to rig fix / geometry note to the modeler / design question to the lead.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | Never export with Blender's FBX defaults: they add leaf bones, bake every Action, simplify curves and skip the unit-scale option. Use `tools/rig/roblox_fbx.py` | [V] RB rule 4; RR18-RR19 |
| C-02 | `group_select_mode='BONE_DEFORM'` on every weight operator; the default counts control groups | [V] RB rule 13 |
| C-03 | Prune to 4, then normalize; Blender normalizes at deform time, so measure exported weights, not the viewport | [V] RB rules 13-14; [O] RP:271 |
| C-04 | Export bones by allowlist, not "Only Deform Bones" (it drops non-deforming sockets) | [V] RB26 |
| C-05 | FBX carries baked samples, never constraints, IK or drivers; bake the export skeleton with visual keying | [V] RB rules 6, 20 |
| C-06 | Keep Zero Influence Bones on in the importer for sockets and a weightless Root; never add Root weights to keep it | [V] RR22; [O] RP:417 |
| C-07 | A pass needs Blender and Roblox evidence for the same revision; an untested item is BLOCKED | [O] RP:431 |
| C-08 | No tolerance in the sheet → the measurement is reported as MEASURED, never PASS | [O] RP:486; `rig_audit.judge` |
| C-09 | Idempotent MCP stages with checkpoints; a rerun replaces its own output | [O] RP:367, 548 |
| C-10 | Bisect planes are in world space for the operator; transform per part, never one world plane through every limb | [V] RB rule 16; [O] RP:174 |
| C-11 | Contacts and end effectors are checked after bake and after import: error accumulates down the hierarchy | [V] Riot compression article (RP:484) |
| C-12 | One file per test clip (traceable); the Animation Clip Editor also takes multi-clip files | [O] RP:382; [V] RR37 |

## 5. Rules (final check)
- Max 4 influences, no Root weight, ≤ 20,000 triangles per mesh, watertight (RR01-RR05); `rig_audit.py` hard-fails these.
- Never edit the source snapshot; never apply the Armature modifier on the only source.
- Never call the Tripo API, create accounts or upload assets without an owner-approved brief that says so.
- Never write scripts through Studio MCP in `files` source mode (`AGENTS.md` §3); Studio MCP is for import checks, play-tests and captures.
- Never claim a Blender or Studio test without an evidence file from this task (rigging paper do-not 20).
- The rigger never cuts or remodels when a modeler or stand-in exists (rig-pipeline §3).

## 6. Self-check before release (K5)
- [ ] Build manifest: Blender + FBX add-on versions, exporter check `[]`, export options used.
- [ ] `audit_s5.json`: weights PASS, geometry PASS, sweeps PASS or MEASURED with the sheet's tolerance named.
- [ ] Every test clip the asset needs exists as a named Action and as an export file.
- [ ] Fresh-scene round trip and Studio import done; hierarchy, scale, axes, sockets, controller, Animator match §A and §C.
- [ ] Control manifest covers every §B ROM.
- [ ] All 22 release items recorded with evidence and labels; BLOCKED items say why.

Project overlay: if `knowledge/overlays/rigging-craft.md` exists, read it after this file; it wins for this game.
