---
name: rigging-craft
description: The how for building and testing a Roblox rig in Blender and proving it in Studio - inspection, posed proxy at the game camera, skeleton, weights, the controls the read needs, control manifest, test clips, FBX export, Studio import. Use at rig-pipeline S2 (posed plan), S4, S5, for "the export looks wrong in Studio", "bones are missing after import", "weights are broken". Read rigging-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Rebuilt by J018 maker character-rigger · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (posed proxy at the game camera, the controls the read needs, numbers-first S4 and S5 lines, measuring recipes run on Blender 5.1.2 headless). Evidence: `knowledge/reference/rigging/` (notes 01-03; fact-checks RR Roblox, RB Blender, RT tools), `knowledge/reference/animation/02-*.md`. Tools: `tools/rig/rig_audit.py`, `tools/rig/roblox_fbx.py` (offline tests in `tools/tests/`), `tools/anim/clip_check.py`, `tools/art/look_check.py`. Tags: [V] verified, [E] experience, [O] studio opinion.

# Rigging craft: build, test and ship the rig

## 1. When this skill starts
After `rigging-design` produced the rig plan and the animator signed K2 (rig-pipeline S2); for the posed plan of `rigging-design` §3 step 10 (the proxy pose at the character proof), step 3 below. Needs: the rig sheet, the source snapshot or blockout, Blender running with the MCP add-on (or headless Blender), Roblox Studio for S5 (`studio-mcp` skill), the game profile (camera, distance, field of view, devices).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Blender version rules, MCP rules, exact API calls, stage scripts, the measuring recipes (overlaps, cap exposure, head drift, scale channels) | `references/blender-mcp.md` |
| Weight cleanup order, locality, deformation that Roblox runs, chains and hook parts | `references/weights.md` |
| Export skeleton, controls (the read controls), control manifest, FBX profile, Studio import, runtime facts | `references/controls-export-import.md` |
| S4 proxy sweep, measurements, the test clips, the 22-item release checklist, **the S4 and S5 self-review lines and image budget** | `references/tests.md` |
| Game-camera and black-fill renders (the one recipe the animator and rigger share) | `animation-craft/references/blender-keying.md` §7 |
| Fix-note format | `templates/rig/fix-note.md` |
| Tripo endpoints, model ids, when Tripo output is good enough | `rig-pipeline/references/tripo-routes.md` |
| A symptom you need to trace | `rigging-design/references/diagnosis.md` |

## 3. Steps
1. **Version and scene.** Record Blender version, FBX add-on version, `roblox_fbx.check_exporter() == []` in the build manifest. Inspect the scene before changing anything. Check: manifest written.
2. **Inventory (S2 support).** Per mesh: triangles, open edges, connected parts (`rig_audit.audit_mesh`), materials, UV maps, size in studs; 6 orthographic renders, wireframe over shaded, back included. Check: defect map in `tests/s2_inventory.json`.
3. **Plan renders and the posed plan (S2).** Draw the cut lines and bend zones from §C over the model, 6 views plus the game camera, for the modeler brief. Then pose the plan (`rigging-design/references/design-for-motion.md` §4): a proxy (one bone per part at the §C pivots, parts 100% on their bone) on the blockout or source, posed at the hardest 2-3 stress poses and the signature pose; numbers for every pose (overlaps, cap exposure, black-fill components and box: `references/blender-mcp.md` §6), then the black-fill and shaded images within line P-11's budget. At the character proof, import the posed proxy into the test place and capture it at the game camera against the game's background. Check: plan renders tie to part ids; P-11 recorded.
4. **S4 geometry acceptance.** When the modeler hands back: scripted checks (watertight, triangles, part count matches the plan, a `cap_<cut id>` group for every §C cut of every part, sampling above 0; a socket only where the child covers it, or n/a on a closed parent face), then the proxy sweep through every §B extreme and stress pose with the numbers of `references/tests.md` §3; images only for failing numbers plus ≤ 8 key poses (G-lines, `references/tests.md` §6). Fail, confirmed by eye on its still → **one** fix note with every failed item; max 2 rounds. Check: §G rows + §H sign-off.
5. **Skeleton.** Export bones by allowlist + parent map; pivots from §C (landmarks, not bounding boxes); rest orientation and roll kept; Root without weights; sockets for VFX / grips / hitboxes as non-deforming bones, named by the game's convention. Authoring controls on top: FK, IK + poles, switches, and the read controls the plan kept (clavicles and hips with their ranges, the head world-orient switch holding the head's rest world frame, hand shapes, one control per hook-shape part, chains driven as one mass with per-bone offsets), left and right independent, quaternion rotation for spin-heavy controls (`references/controls-export-import.md` §2). Check: rotation preview per joint; hierarchy dump; switches toggled at rest move nothing.
6. **Weights.** Rigid parts: one bone at 1.0. Skinned zones: localized weights; chains weighted so each bone bends its own segment; then the cleanup order (remove accidental non-deform groups, keeping the `cap_*` and protected groups that R-02 and R-03 need → fill gaps → remove cross-body support → limit 4 → normalize, all with `group_select_mode='BONE_DEFORM'`). Check: `rig_audit.audit_weights` PASS.
7. **Control manifest.** One record per control (`references/controls-export-import.md` §3), ranges from §B, the read need each control serves, quaternion channels named by index with `quat` ranges (±sin(θ/2)). Check: every §B ROM appears as a min/max on a control; every kept read control is in it.
8. **Tests in Blender.** The clips the asset needs from `references/tests.md` §4 as named Actions with their slots assigned; `rig_audit.audit_scene` with protected groups that reach the start of each transition, sweeps, tolerances from §F (MEASURED if none); combined stress poses with the S4 numbers; `clip_check.py` rom, contact_slide and pops on the wind-up, contact-hold and spin clips; head drift on the spin clip. Check: R-lines R-01 to R-09 filled; any FAIL goes back to step 4-6, not to polish.
9. **Export and round trip.** Bake the export skeleton with visual keying on a copy; `roblox_fbx.export` rest + one file per clip; re-import into a fresh Blender scene; compare hierarchy, weights, sizes, and the spin clip's head drift by clip frame. Check: `tests/roundtrip.json`.
10. **Roblox import.** File > Import, Rig Type Custom (R15 only for avatar bodies), Keep Zero Influence Bones on when sockets or a weightless Root must survive; read every warning; check MeshParts, Bones, attachments, controller, Animator; play each test clip on the intended Animator; capture the key poses at the game camera in the real place (R-10). Check: MCP-verified evidence in §G.
11. **Release.** All 22 checklist items and the R-lines PASS, MEASURED (no sheet tolerance), n/a, or BLOCKED / not verified with the reason; hand the rig, manifest, test record, the sweep and contact-hold clips, and the limits to the animator (S6). Then handle rig notes: restate the problem behind each note, triage it to rig fix / geometry note to the modeler / design question to the lead.

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
| C-11 | Contacts and end effectors are checked after bake and after import: error accumulates down the hierarchy | [V] (RP:484) |
| C-12 | One file per test clip (traceable); the Animation Clip Editor also takes multi-clip files | [O] RP:382; [V] RR37 |
| C-13 | A world-orient switch is authoring-only: it holds the head's rest world frame, moves nothing at rest, and reaches Roblox only through a visual-key bake; a default bake drops it with no error | [V] studio test 2026-10-22, Blender 5.1.2 (`references/blender-mcp.md` §6) |
| C-14 | Assign the Action **and its slot** on every object that should play it (a copy, an export skeleton): an Action without a slot plays nothing, and a bake then records a frozen pose with no error | [V] studio test 2026-10-22, Blender 5.1.2 |
| C-15 | Numbers before images at S2, S4 and S5: overlap pairs, cap exposure on points over every cap face (recipe 1), black-fill component count and box, rom, contact slide, pops, head drift; images only where a number fails plus the key poses; every number is a screening aid with known false readings (`references/blender-mcp.md` §6): a failing or borderline one is checked by eye on the still before a fix note | [O] owner J005-D8; recipes `references/blender-mcp.md` §6 |
| C-16 | No scale in clips: a pose stores only a CFrame; squash, stretch and smears ship as swap meshes, code-scaled separate parts or VFX; scan every export clip for scale keys other than 1 (a bake's constant-1 scale channels are harmless) | [V] `_api-reference/classes/Pose.yaml`, `Bone.yaml` |
| C-17 | Quaternion rotation for spin-heavy controls; an Euler wrap pops in one frame, found by `clip_check.py` pops only with a landmark off the spin axis | [V] studio test 2026-10-22; `animation/curve-editor.md` (KeyframeSequences use quaternions) |
| C-18 | A step you repeat by hand on a third asset becomes a script in `content/rigs/<id>/scripts/` and a tool ticket for `tools/rig/` | [O] `rules/anti-overengineering.md` |

## 5. Rules (final check)
- Max 4 influences, no Root weight, ≤ 20,000 triangles per mesh, watertight (RR01-RR05); `rig_audit.py` hard-fails these.
- Never edit the source snapshot; never apply the Armature modifier on the only source.
- Never call the Tripo API, create accounts or upload assets without an owner-approved brief that says so.
- Never write scripts through Studio MCP in `files` source mode (`AGENTS.md` §3); Studio MCP is for import checks, play-tests and captures.
- Never claim a Blender or Studio test without an evidence file from this task (rigging paper do-not 20).
- The rigger never cuts or remodels when a modeler or stand-in exists (rig-pipeline §3).
- Never key scale in an export clip (C-16); never ship a switch or constraint the export depends on without a visual-key bake (C-13).
- Checks are light (owner J005-D8): numbers for every pose and clip; images only on a failing number plus the key poses (`references/tests.md` §6 budget).

## 6. Self-check before release (K5)
- [ ] Build manifest: Blender + FBX add-on versions, exporter check `[]`, export options used.
- [ ] `audit_s5.json`: weights PASS, geometry PASS, sweeps PASS or MEASURED with the sheet's tolerance named.
- [ ] Every test clip the asset needs exists as a named Action (slot assigned) and as an export file.
- [ ] Fresh-scene round trip and Studio import done; hierarchy, scale, axes, sockets, controller, Animator match §A and §C.
- [ ] Control manifest covers every §B ROM and every kept read control.
- [ ] The S4 G-lines and S5 R-lines of `references/tests.md` §6 each PASS, MEASURED, not verified or n/a with evidence; renders made and images looked at counted.
- [ ] All 22 release items recorded with evidence and labels; BLOCKED items say why; the could-not-check list and one honest weakness written.

Project overlay: if `knowledge/overlays/rigging-craft.md` exists, read it after this file; it wins for this game.
