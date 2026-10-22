---
name: modeling-craft
description: The how for building a Roblox model in Blender and importing it to Studio - blockout as the silhouette gate, hand modeling, Tripo finish, cuts and sockets for the rigger, UVs, texture passes, collision, FBX export, audit, read checks. Use for "build this model", "clean up this Tripo model", "cut the parts for the rigger", "wrong size in Studio", "icon renders". Read modeling-design first.
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal (J007). Evidence: `knowledge/reference/modeling/` (paper notes 01-03, first-game 04, fact-checks MR Roblox, MB Blender, MT Tripo), rigging fact-checks (RB, RT), J005 G2 gaps (GP). Tools: `tools/model/model_audit.py`, `tools/model/review_renders.py`, `tools/rig/roblox_fbx.py`, `tools/art/look_check.py` (offline tests in `tools/tests/`). Tags: [V] verified, [E] experience, [O] studio opinion. Rebuilt by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the gates in the steps, texture passes, measuring the read (§7).

# Modeling craft: build it, check it, ship it

## 1. When this skill starts
After `modeling-design` produced an asset record with an approved, checked reference, a read plan, a route and a budget. For a moving model, after the rigger's S2 plan (rig-pipeline). Needs Blender 5.1+ (MCP add-on running, or headless `blender.exe -b`), and Roblox Studio with Studio MCP for the import check and the game-camera capture (`studio-mcp` skill), in a test place, never the live place.

## 2. Read this file when
| You need | Open |
| --- | --- |
| Blender version, MCP vs headless, scene setup, the game camera and key light, hand-modeling recipes, clean-up, evaluated counts, extra review views | `references/blender-recipes.md` |
| The Tripo input pack, the raw-candidate check, finishing a Tripo model | `references/tripo-finish.md` |
| S3 for the rigger: cuts, caps, sockets, bend zones, checks C1-C5 | `references/rig-parts.md` |
| UVs, texture sizes, SurfaceAppearance, tint, normal maps, emissive, baking, the texture passes, colour and light in the maps, trim sheets | `references/textures-materials.md` |
| Scale chain, export copy, FBX profile, importer settings, reimport, import triage | `references/export-import.md` |
| What each receiver gets and what to ask each partner for; attach-point record; icon renders | `references/handoffs.md` |
| The exact command lines for region masks, top 5 %, detail density, phone-aspect crop, mirror | `references/read-commands.md` |
| The read plan, silhouette, value, colour, detail and motion standards | `modeling-design/references/read-and-form.md` |
| Budgets, collision choice, kits, the pass/fail list, the self-review | `modeling-design` references |

## 3. Steps
1. **Set up** (blender-recipes §1-2): record Blender version; scene units (1 unit = 1 stud); a player-size dummy from the game profile (5 studs if unset, PROPOSAL); the approved reference views as image planes or a camera background; the game camera(s) from the game profile and the art bible's key light direction (blender-recipes §6). Work file in `content/models/<asset-id>/work/`. Check: version, units, camera and light source in the asset record.
2. **Blockout: the silhouette gate.** The whole asset from primitives at the right size; one flat colour per material region; the main top and bottom lines before anything else; compare with the reference at matching cameras; render the front and back game-camera views and measure their black-fill and phone-size versions (§7); when the blockout is itself a hand-off (a proof), the full review set is its one set. Options when the design is open (2-3, equal finish, one radical). Characters and large props with no proof capture planned: import the blockout into the test place and capture it next to the default avatar at the game camera. Check: size in studs vs the record; `modeling-design/references/review.md` §5 SL lines pass; blockout revision frozen; owner or art director approval when the brief asks (blockout gate).
3. **Build** by route, in passes over the whole model (big shapes, then medium, then small; never finish one part while the rest is blank). Hand: named, parameterized primitives and modifiers (blender-recipes §3); organic hero forms: rich form first, then a budgeted game mesh with loops where it bends. Tripo: write the input pack, the owner runs Tripo, then the raw-candidate check and finish, restoring the iconic qualities it softened (`references/tripo-finish.md`). Check: audit after each major stage (numbers only); silhouette still matches the frozen blockout.
4. **Rig parts** (moving models): the rigger's cuts and bend zones, caps, sockets, counter-proposal if any (`references/rig-parts.md`); no mass across a joint or cut. Check: C1-C5 numbers; MO lines of the self-review.
5. **Clean**: loose and degenerate geometry, normals, inside faces, duplicates, only what the audit flags; never one global merge or fill (blender-recipes §4). Check: audit PASS on construction rows.
6. **UVs and textures in passes** (`references/textures-materials.md` §3, §7): UVs after structure is final → high-to-low bake when the route has a high source (§4 of that file) → flat material regions → **value gate** (grey view at the game camera) → AO and curvature bake, form shading along the key light → hue-shifted shadows and highlights, crisp edges and accents → wear and story → material read under Roblox light in Studio. Stop before texture polish for the art director's check-in (captures at the game camera on the real background). Check: 1 UV map, 1 material per mesh; image sizes on plan; VL and CL lines pass before polish; DT lines after.
7. **Collision and attach points**: collision role per part (budgets §6), simple and predictable; attach points as named Empties (`references/handoffs.md` §3). Check: every attach point in the record.
8. **Audit and review set**: `model_audit.py` with the budget and size from the record; then `review_renders.py` once (reference views, player dummy, game camera) plus the back game-camera view (blender-recipes §6); the images per stage are listed once in `modeling-design/references/review.md` §1; run the read measurements (§7) on those files and the self-review (`modeling-design/references/review.md` §5). Images beyond the set only for a failing number. Check: audit json + renders listed with counts + self-review results in the record.
9. **Export and import**: export copy, kit FBX profile, Studio import in the test place, measure parity (`references/export-import.md`); capture at the game camera on the real ground (held items in the avatar's hand) plus its mask capture, and measure it at phone size (§7). Check: MCP-verified size, part count, materials, pivots; IM1 passes.
10. **Hand off** to each receiver with the packet in `references/handoffs.md`; fill the asset record results and lineage; honest recap and lesson in the hand-back. Check: STATUS + coverage.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| C-01 | Keep the editable work file separate from the export copy; never edit raw Tripo files or the approved source; version every export | [O] HM6, FW-05, PRC18 |
| C-02 | Build from semantic parameters (blade length, grip diameter, roof overhang) and named collections so a rerun replaces, never duplicates | [O] HM6; [E] FM30 (edit the source, never the export) |
| C-03 | Count the evaluated, triangulated mesh (after modifiers), the number the exporter writes; never the viewport face count | [V] B03, B09, B10 (RU04) |
| C-04 | Modifier order matters; keep modifiers live until the export copy | [V] B03 (HM5) |
| C-05 | Name what a bevel width means (offset, width, depth, percent) and test the visible result at the game camera; add only the segments the shape needs; hard materials get crisp edges, organic ones soft transitions | [V] B04 (HM9); [O] HM10 |
| C-06 | Booleans need manifold inputs; after a cut check slivers, inside faces and shading; never let a boolean cross a bending joint | [V] B05 (HM11); [O] HM12 |
| C-07 | Decimate static irregular shapes only; retopologize faces, bending limbs and mechanical contacts; voxel remesh is not animation topology | [V] B06, B07 (HM13-HM14); [O] HM15 |
| C-08 | Symmetry is a tool, not a duty: keep approved asymmetry; inspect the centre seam; never weld the whole mesh because the seam is open | [V] B08 (HM7); [O] HM8 |
| C-09 | Fix by diagnosis: one cause at a time; repair operators only on what the audit flags; an intended open edge is not a hole | [O] REV05-REV07, BK12 |
| C-10 | Roblox culls back faces: keep normals out and surfaces apart; a face visible in Blender may vanish in game | [E] FM62; [V] MR01 (watertight) |
| C-11 | Pivots where parts rotate (wheel axle, door hinge, lid); the rigger owns joint pivots; never move every origin to world zero | [O] EXP21, RG-08; [V] MR41-MR42 |
| C-12 | Attach points are named frames with orientation, parent and model revision, not "near the origin" | [O] HND11-HND12 |
| C-13 | A file that imports is not a model that works: measure size, facing, parts, pivots, materials and collision in Studio, and judge the look in a Studio capture at the game camera | [O] EXP12, DNT15 |
| C-14 | Light checks: audit numbers for everything, one review set per hand-off (its black-fill, grey, phone-size and mirror views are measurements, not new renders), more images only for a failing number; report render counts | owner J005-D8, J007-D7 |
| C-15 | Owner rejections and the self-review are the checklist: size at player scale, held props readable from the front, no limb leaving the body, no micro-detail that costs triangles without a read | [E] FM15-FM40, FM18 (`modeling-design/references/review.md` §2a, §5) |
| C-16 | Every work file carries the game camera(s), the key light and the player dummy from the first session; every judging render comes from them | [O] |
| C-17 | Rich form first, then the game mesh: organic hero forms are blocked and refined (or the Tripo mesh is the high), then retopologized to the budget with loops at elbows, knees, shoulders, mouth and eyes | [O] |
| C-18 | Material regions before shading: one material slot or ID colour per material before any texture work; later passes change value only inside a region | [O] |
| C-19 | Detail goes into textures, not polygons, unless it changes the silhouette, a bend or a material edge; painted forms are checked against a wireframe or matcap render so they sit on real geometry | [O] |
| C-20 | Mirrored UVs on symmetric parts; unique UV space where story detail goes (cracks, badges, text); asymmetric details in geometry or a separate part | [O] |
| C-21 | When texturing exposes a geometry problem, change the mesh and re-project the existing texture (selected-to-active bake); at the end, pull silhouette vertices to follow the major painted details only after the texture layout is locked | [O] |
| C-22 | Project the approved image onto the model from a matching camera as a rough first texture, then fill the gaps and repaint; a base, never the finish | [O] |
| C-23 | Stylised hand-painted assets start low-poly (no high-poly bake), so a shape change is a re-export and a Studio reimport, not a re-bake | [O] |
| C-24 | Keep separable parts separate and clearly named (garments, props, plants, base); judge them combined; keep quads where later edits are planned and UV islands laid out so another agent can pick the file up | [O] |
| C-25 | Decisive edits: one deliberate shape change and a re-render, not dozens of micro tweaks; a section that keeps failing is rebuilt from the frozen blockout or the raw source | [O] |
| C-26 | A step repeated across assets becomes a script in the asset folder (texture recipes per material class, the read measurements); one repeated three times or more becomes a tool ticket (PROPOSAL count) | [O] |

## 5. Rules (final check)
- Work on copies; raw Tripo output and approved sources are never edited.
- Hard limits: ≤ 20,000 triangles per mesh; one material and one UV map per mesh; UVs inside 0-1; ≤ 4 influences per vertex for anything skinned (MR01, MR06, MR12). Project budget from the asset record (creatures and characters under about 7,000, J007-D5).
- No detail pass before the silhouette gate; no texture polish before the value gate and the art director's check-in.
- Export only with `tools/rig/roblox_fbx.py` (or every option named); one scale recipe, never stacked.
- Studio MCP checks imports and takes captures in a test place; it never edits scripts (files mode); restore the edit camera after captures. Nothing is uploaded without the owner's yes (FM89).
- Never call the Tripo API, log in to Tripo or ChatGPT for the owner, or spend credits outside the brief.
- Scripts, renders and outputs only inside the asset folder (GP09).

## 6. Self-check before returning
- [ ] Asset record results filled: triangles, size, loose parts, flipped/inverted, materials, UV maps, texture sizes, each with a label.
- [ ] Audit json PASS on hard limits; budget row PASS or a stated, approved exception.
- [ ] One review set made (with the back game-camera view); read measurements run on it; self-review lines (`modeling-design/references/review.md` §5) recorded; counts of renders made and looked at in the hand-back.
- [ ] Studio import measured and the game-camera capture taken (MCP-verified), or `not verified` with the reason.
- [ ] Lineage complete; honest recap and lesson in the hand-back (the lead writes the inbox draft; you do not write to `knowledge/inbox/`).

Project overlay: if `knowledge/overlays/modeling-craft.md` exists, read it after this file; it wins for this game.

## 7. Measuring the read (on the files of the one review set)
Inputs: the `review_renders.py` set, the back game-camera render (blender-recipes §6), and the Studio game-camera capture. Outputs go to `content/models/<asset-id>/renders/checks/`. Tolerances come from the brief, art bible or owner (`--tolerance-source`); without one the verdict is MEASURED. On a review-set render (flat sRGB 128 grey background) add `--key-tol 4` to every `look_check.py` call that finds the model by its background (`silhouette`, `value`, `thumb`, `palette`): the default 40 drops every model pixel within 40 levels of that grey (in the test, a lit skin-tone head vanished from the black-fill with no error). Open the black-fill once per set: every part black. On a capture, use `--mask`.
| View | Command | Read |
| --- | --- | --- |
| Black-fill | `python tools/art/look_check.py silhouette <render> --key-tol 4 --out-dir <checks>` (for the aligned IoU add `--compare <other image> --compare-mask <its black-fill>`: `--compare` alone keys the other image with this call's tolerance, so make a reference image's black-fill first with its own `silhouette` call and open it; `--keep-holes` when the model has enclosed gaps) | the black-on-white image; area and bbox; IoU against the reference or a neighbour |
| Phone size | `python tools/art/look_check.py thumb <game-camera render> --key-tol 4 --size <phone viewport WxH> --out-dir <checks>` (a capture: `--mask` instead of `--key-tol`): the whole frame resampled to the smallest phone viewport from the game profile. FieldOfView is vertical, so this is the phone's scale at any frame aspect up to the phone's; a wider capture is first cropped in width (`references/read-commands.md` §4). Never `--size` at the model's own on-screen size on a whole frame (it shrinks the frame to the model's size); not for orthographic or close views | value and silhouette re-run small; anchors still visible; `scale` = phone height ÷ frame height |
| Grey | `python tools/art/look_check.py value <render> --key-tol 4 --out-dir <checks>` | the luminance image (`<name>.luminance.png`); p5-p95 luminance (linear: bands converted in `modeling-design/references/review.md` §5); subject/ring ratio against the ground |
| Region (upper vs lower body, focal zone, one material) | cut a region mask from the black-fill (`references/read-commands.md` §1), then `look_check.py value <render> --mask <region>.mask.png --out-dir <checks>/<region>` (or `palette --mask` for CL5). Box edges from the projection recipe or, on a capture, `WorldToViewportPoint`, never by eye. Never use `--box` or `--compare-subjects` on a render: every background pixel in the box counts | each region's subject p50 and p5-p95; record both medians |
| Top 5 % (value or colour) | `references/read-commands.md` §2 on the luminance image (L) or the colour render (S: chroma, how colourful, not HSV saturation, which peaks on tinted near-black), inside the black-fill or the capture's mask; ties on flat-region renders follow the §2 rule: record both shares | black = the brightest (L) or most colourful (S) pixels; they sit on the named accents (VL4, P3) or the focal zone (CL7) |
| Joint and overlap steps | `python tools/art/look_check.py contrast --sample <render> --fg-box <part A> --bg-box <part B>`; each box lies fully inside its part (no background pixels), edges from the projection recipe | the ratio between two neighbouring parts (record it; the WCAG rules are for UI only) |
| Palette | `python tools/art/look_check.py palette <render> --key-tol 4 --roles <bible roles json>` | clusters, area shares, distance to each role swatch |
| Mirror | `references/read-commands.md` §5 | lopsided shapes, the asymmetric element |
| Small features | the projection recipe (blender-recipes §6): every named part's projected height in px at the game camera on the phone | parts under the starting value of about 4 px |
| Detail density | `references/read-commands.md` §3 on a game-camera render (or capture), its black-fill (or mask) and the phone viewport height: it crops to the model and scales it by phone height ÷ frame height (edge threshold and cell size are PROPOSAL) | `<name>.detail.png`: busy cells sit on the read plan's detail spots with quiet cells between (DT10); no busy cells, or busy cells everywhere, is even density; part lines also show as busy rows |
| Studio capture | before the capture set `workspace.CurrentCamera.FieldOfView` to the game profile's FOV (`execute_luau`; note the old value; the editor default is 70); `screen_capture` with `camera_position` and `look_at_position` from the game camera, on the real ground; restore the FOV and the camera after (`studio-mcp` P-05); record the graphics quality level. First time in a place: check the FOV took (the model's size in frame differs from a 70° capture), else record the FOV used. A capture wider than the phone viewport: crop its width only, and the mask capture's, to the phone aspect before `thumb` (`references/read-commands.md` §4; FieldOfView is vertical, so keep the full height); a narrower capture goes to `thumb` uncropped. Held items: in the avatar's hand (`references/export-import.md` §3) | the same checks on the capture with `--mask` from its mask capture: Studio decides the final look |
| Mask capture (for every Studio capture) | a real-ground capture has no flat border, so `look_check.py` cannot find the model alone (`invalid-mask`). From the same camera: put a temporary large `#FF00FF` Neon part behind the model and one under it, set the model's CastShadow off, capture, run `look_check.py silhouette` on that capture, and pass its `<name>.silhouette.png` as `--mask` to `silhouette`, `value`, `thumb` and `palette` on the real-ground capture. Then delete the parts, restore every property you changed and the camera. Probe once per place: open the black-fill and check it matches the model; if it gives `invalid-mask` or a wrong outline, the capture's SL1, SL2 and VL2 are `not verified` | the mask that makes the capture measurable |
