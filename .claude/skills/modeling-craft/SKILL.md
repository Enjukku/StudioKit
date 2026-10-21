---
name: modeling-craft
description: The how for building a Roblox model in Blender and importing it to Studio - blockout, hand modeling, the Tripo route, cuts and sockets for the rigger, UVs, textures, collision, FBX export, model audit. Use for "build this model", "clean up this Tripo model", "cut the arms off for the rigger", "it's the wrong size in Studio", "make icon renders". Read modeling-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal (J007). Evidence: `knowledge/reference/modeling/` (paper notes 01-03, first-game 04, fact-checks MR Roblox, MB Blender, MT Tripo), rigging fact-checks (RB, RT), J005 G2 gaps (GP). Tools: `tools/model/model_audit.py`, `tools/model/review_renders.py`, `tools/rig/roblox_fbx.py` (offline tests in `tools/tests/`). Tags: [V] verified, [E] experience, [O] studio opinion.

# Modeling craft: build it, check it, ship it

## 1. When this skill starts
After `modeling-design` produced an asset record with an approved, checked reference, a route and a budget. For a moving model, after the rigger's S2 plan (rig-pipeline). Needs Blender 5.1+ (MCP add-on running, or headless `blender.exe -b`), and Roblox Studio with Studio MCP for the import check (`studio-mcp` skill), in a test place, never the live place.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Blender version, MCP vs headless, scene setup, hand-modeling recipes, clean-up, evaluated counts | `references/blender-recipes.md` |
| The Tripo input pack, the raw-candidate check, finishing a Tripo model | `references/tripo-finish.md` |
| S3 for the rigger: cuts, caps, sockets, bend zones, checks C1-C5 | `references/rig-parts.md` |
| UVs, texture sizes, SurfaceAppearance, tint, normal maps, emissive, baking | `references/textures-materials.md` |
| Scale chain, export copy, FBX profile, importer settings, reimport, import triage | `references/export-import.md` |
| What each receiver gets; attach-point record; icon renders | `references/handoffs.md` |
| Budgets, collision choice, kits, the pass/fail list | `modeling-design` references |

## 3. Steps
1. **Set up** (blender-recipes §1-2): record Blender version; scene units (1 unit = 1 stud); a player-size dummy from the game profile (5 studs if unset, PROPOSAL); the approved reference views as image planes or a camera background. Work file in `content/models/<asset-id>/work/`. Check: version and units in the asset record.
2. **Blockout** the whole asset from primitives at the right size; flat colours; compare with the reference at matching cameras. Check: size in studs vs the record; owner or art director approval when the brief asks (blockout gate).
3. **Build** by route. Hand: named, parameterized primitives and modifiers, big shapes before small (blender-recipes §3). Tripo: write the input pack, the owner runs Tripo, then the raw-candidate check and finish (`references/tripo-finish.md`). Check: audit after each major stage (numbers only).
4. **Rig parts** (moving models): the rigger's cuts and bend zones, caps, sockets, counter-proposal if any (`references/rig-parts.md`). Check: C1-C5 numbers.
5. **Clean**: loose and degenerate geometry, normals, inside faces, duplicates, only what the audit flags; never one global merge or fill (blender-recipes §4). Check: audit PASS on construction rows.
6. **UVs and textures** to the texture plan; bake if the route needs it (`references/textures-materials.md`). Check: 1 UV map, 1 material per mesh; image sizes on plan.
7. **Collision and attach points**: collision role per part (budgets §6); attach points as named Empties (`references/handoffs.md` §3). Check: every attach point in the record.
8. **Audit and review set**: `model_audit.py` with the budget and size from the record; then `review_renders.py` once (reference views, player dummy, game camera). Images beyond the set only for a failing number. Check: audit json + renders listed with counts.
9. **Export and import**: export copy, kit FBX profile, Studio import in the test place, measure parity (`references/export-import.md`). Check: MCP-verified size, part count, materials, pivots.
10. **Hand off** to each receiver with the packet in `references/handoffs.md`; fill the asset record results and lineage; lesson draft. Check: STATUS + coverage.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | Keep the editable work file separate from the export copy; never edit raw Tripo files or the approved source; version every export | [O] HM6, FW-05, PRC18 |
| C-02 | Build from semantic parameters (blade length, grip diameter, roof overhang) and named collections so a rerun replaces, never duplicates | [O] HM6; [E] FM30 (edit the source, never the export) |
| C-03 | Count the evaluated, triangulated mesh (after modifiers), the number the exporter writes; never the viewport face count | [V] B03, B09, B10 (RU04) |
| C-04 | Modifier order matters; keep modifiers live until the export copy | [V] B03 (HM5) |
| C-05 | Name what a bevel width means (offset, width, depth, percent) and test the visible result at the game camera; add only the segments the shape needs | [V] B04 (HM9); [O] HM10 |
| C-06 | Booleans need manifold inputs; after a cut check slivers, inside faces and shading; never let a boolean cross a bending joint | [V] B05 (HM11); [O] HM12 |
| C-07 | Decimate static irregular shapes only; retopologize faces, bending limbs and mechanical contacts; voxel remesh is not animation topology | [V] B06, B07 (HM13-HM14); [O] HM15 |
| C-08 | Symmetry is a tool, not a duty: keep approved asymmetry; inspect the centre seam; never weld the whole mesh because the seam is open | [V] B08 (HM7); [O] HM8 |
| C-09 | Fix by diagnosis: one cause at a time; repair operators only on what the audit flags; an intended open edge is not a hole | [O] REV05-REV07, BK12 |
| C-10 | Roblox culls back faces: keep normals out and surfaces apart; a face visible in Blender may vanish in game | [E] FM62; [V] MR01 (watertight) |
| C-11 | Pivots where parts rotate (wheel axle, door hinge, lid); the rigger owns joint pivots; never move every origin to world zero | [O] EXP21, RG-08; [V] MR41-MR42 |
| C-12 | Attach points are named frames with orientation, parent and model revision, not "near the origin" | [O] HND11-HND12 |
| C-13 | A file that imports is not a model that works: measure size, facing, parts, pivots, materials and collision in Studio | [O] EXP12, DNT15 |
| C-14 | Light checks: audit numbers for everything, one review render set per hand-off, more images only for a failing number; report render counts | owner J005-D8, J007-D7 |
| C-15 | Owner rejections are the checklist: size at player scale, held props readable from the front, no limb leaving the body, no micro-detail that costs triangles without a read | [E] FM15-FM40, FM18 (`modeling-design/references/review.md` §2a) |

## 5. Rules (final check)
- Work on copies; raw Tripo output and approved sources are never edited.
- Hard limits: ≤ 20,000 triangles per mesh; one material and one UV map per mesh; UVs inside 0-1; ≤ 4 influences per vertex for anything skinned (MR01, MR06, MR12). Project budget from the asset record (creatures and characters under about 7,000, J007-D5).
- Export only with `tools/rig/roblox_fbx.py` (or every option named); one scale recipe, never stacked.
- Studio MCP checks imports in a test place; it never edits scripts (files mode). Nothing is uploaded without the owner's yes (FM89).
- Never call the Tripo API, log in to Tripo or ChatGPT for the owner, or spend credits outside the brief.
- Scripts, renders and outputs only inside the asset folder (GP09).

## 6. Self-check before returning
- [ ] Asset record results filled: triangles, size, loose parts, flipped/inverted, materials, UV maps, texture sizes, each with a label.
- [ ] Audit json PASS on hard limits; budget row PASS or a stated, approved exception.
- [ ] One review render set made; counts of renders made and looked at in the hand-back.
- [ ] Studio import measured (MCP-verified) or `not verified` with the reason.
- [ ] Lineage complete; lesson draft in `knowledge/inbox/`.

Project overlay: if `knowledge/overlays/modeling-craft.md` exists, read it after this file; it wins for this game.
