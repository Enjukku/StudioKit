> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Facts: `knowledge/reference/environment/fact-check-performance-import.md` (**PI**, **PX** rows) and the rigging fact-checks it reuses; method from the environment paper notes `03-pipeline-performance-review.md` (§2, §8: H, BW rows). Docs paths are relative to `knowledge/external/roblox-creator-docs/`. Method rows marked **method** are the studio's procedure, not Roblox or Blender guidance (PI49, PI51, PI65). Revised by J018 maker environment-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§7, snapping art to the blockout; kit packages).

# Blender ↔ Studio: what is built where, and moving it across

## 1. Built where (choose per element, record in the blueprint §G)
| Element | Where | Why | Notes |
| --- | --- | --- | --- |
| Route blockout | Studio | iterate against the real avatar, camera and collision | keep named anchors and route sizes through the art pass (BW02, BW25) |
| Broad landform, ground, water | Studio Terrain | native sculpting, smooth material blends, water | see `terrain-and-water.md` |
| Sculpted cliff, hero rock, cave shell, overhang, stylized strata (one-off for this place) | Blender, then Studio | silhouette, topology, UVs, baked detail | the environment designer builds these one-off pieces (J008-D4); their form, texture and finish follow the modeler's standards (`modeling-design`: planes and edges, baked AO and curvature, wear with a reason, texel density matching the kit, detail in textures); seams to terrain checked in Studio |
| Reusable kit pieces, props, vegetation meshes, hero buildings, anything rigged | modeler (Blender) | reuse and asset craft | request in the `rules/messages.md` brief format; place them in Studio |
| Assembling kit pieces into streets and buildings | Studio (or a Blender layout that exports positions only) | game context, instancing | import each asset once, duplicate in Studio (§4); kit pieces as packages so a fix updates every copy |
| Bespoke shells for an irregular layout (no kit fits) | Blender, then Studio | the layout is gameplay-driven, so a forced kit would bend it | unique shells sharing one trim sheet; built on the imported greybox (§7) |
| Lighting, atmosphere, sky, post effects | Studio | Studio is the final renderer and owns the quality tiers; the importer brings no lights or cameras (PI49) | Blender lighting is only for renders of Blender-built parts |
| Ambience zones and source anchors | Studio | real listener, scale and streaming | `ambience-in-place.md` |
| Distant skyline | either | silhouette and depth, not near detail | check level of detail and streaming behavior (§5) |

## 2. Scale chain (set once per project; record in the scene scale record)
| Setting | Value | Source |
| --- | --- | --- |
| Blender scene | Units > Unit System **None**, Rotation Degrees: 1 Blender unit = 1 stud | `art/blender.md:25-31` (PX05) |
| Roblox convention | 1 stud ≈ 28 cm "in general"; the physics engine converts nothing, so the project keeps one reading | `physics/units.md:36-39` (PI53) |
| FBX export | Apply Scaling = **FBX Unit Scale** (the recommended recipe); every other scale value left at 1.0 | `art/blender.md:149-152`; `art/modeling/export-requirements.md:38` (PI42, PI44) |
| Other FBX export options | Path Mode Copy with embedded textures; Add Leaf Bones off; Bake Animation off unless the asset animates | `art/modeling/export-requirements.md:30-42` (PI42) |
| Axes | Forward and Up set explicitly in the export script and recorded; the Roblox page says Z Forward, Y Up, which differs from the add-on default (-Z forward). Measure with the calibration object | `art/blender.md:122-124` (PX04) |
| Importer | Scale Unit = Stud; record "Insert Using Scene Position" (default off), "Set Pivot to Scene Origin" (default on), "Use Imported Pivot" (default on) | `studio/importer.md:234-243, 319, 354` (PI47, PI53) |
| glTF | needs no FBX scale fix, but its hierarchy differs: each mesh becomes a Model with one MeshPart per primitive, and a `_Node` suffix appears when a node and its mesh share a name | `art/blender.md:131` (PX06); live importer page (PI46) |
**Never stack recipes.** Transform Scale .01 and Scene Unit Scale .01 are documented alternatives; using one of them together with FBX Unit Scale gives a model 100 times off (PI44). If scale is wrong, find the faulty layer in this order: scene units, object transforms, export conversion, importer scaling; do not resize descendants first (**method**, PI51).

## 3. One round trip before bulk work (**method**)
1. Make a calibration object of known size (for example a 4 × 8 × 2 stud block with a marked front face) and a player-size dummy taken from the scale sheet.
2. Export it with the project recipe, import it into the test place, and measure it (`Model:GetExtentsSize()`, `ref/Model.yaml:358-380`; GetBoundingBox is oriented to the PrimaryPart or WorldPivot, not the world axes, PI55).
3. Check size, front direction, pivot, hierarchy, materials and normals; compare with the dummy. Write the result in the scale record. Only then build in bulk.

## 4. Blender work through the Blender MCP
| Rule | Detail |
| --- | --- |
| Inspect first | `get_objects_summary`, `get_blendfile_summary_*`; confirm Blender version and file before writing (the MCP's bundled docs are 5.1; the Blender LTS checked by the fact-check is 5.2.2, PI38) |
| Run code | `execute_blender_code` (assign a JSON-able dict to `result`); no MCP tool exports FBX, so export with `bpy.ops.export_scene.fbx` inside it (fact-check MCP section) |
| Named collections only | keep export and non-export collections apart, stable names, a manifest before export; never target "the selection" or a default name (H04, BW22 **method**) |
| Count what ships | triangles and sizes from the evaluated mesh (`Object.evaluated_get(depsgraph)`, `to_mesh()` / `to_mesh_clear()`), on a copy (PI41) |
| Inspect without changing | `Mesh.validate()` fixes geometry, so run it on a copy when the job is inspection (PI40) |
| Locked blockout | keep the accepted blockout as a locked reference collection (K01-e **method**) |
| Repeatable scatter | record seed, asset set, exclusion masks and source revision (H07 **method**) |
| Renders | `render_viewport_to_path` / `render_thumbnail_to_path` for the review sheet next to the reference images |
| Never assume Studio tool names exist in Blender | the two MCP tool sets do not overlap; Blender tools take no studio_id (PI67) |

## 5. Import rules that change runtime cost
| Rule | Source |
| --- | --- |
| A single imported mesh may hold at most 20,000 triangles. That is a cap, not a target or a stage budget | `art/modeling/specifications.md:34` (PI24) |
| Instancing: meshes with the same MeshContent draw together when their SurfaceAppearance (if any) or TextureContent match; materials count when neither exists | `performance-optimization/improve.md:321-329` (PI18) |
| Importing the whole assembled scene at once gives identical meshes different asset ids and loses instancing: import each asset once, duplicate in Studio (packages are the reuse tool) | `performance-optimization/improve.md:342-352, 398-404` (PI19) |
| A Blender linked duplicate shares mesh data in Blender only; it does not guarantee runtime instancing | PI48 |
| Studio supports five PBR maps: color, normal, roughness, metalness, emissive | `art/modeling/surface-appearance.md:53-96` (PI52) |
| Collision: Box fidelity is cheapest; parts with no collision need set CanCollide, CanTouch, CanQuery false; anchor everything static | `performance-optimization/improve.md:170, 229-232` (PI20) |
| CollisionFidelity Tunable adds CollisionPrecision: 0 = hull, 1 = near-exact where possible; qualitative; stored in the place until regenerated | PI22, PI23 |
| Verify walkable surfaces and camera blockers with collision visualization, never from the render mesh | BW19 **method** |

## 6. After every import (**method**, BW11)
Dimensions, orientation, pivot, hierarchy, material resources, normals, collision, and asset permissions, against the calibration object and a known route fixture. A clean import only proves the importer took the file.

## 7. Snapping art to the approved blockout (**method**)
1. Export the approved greybox (or its route-critical parts) from Studio and import it into Blender at the same origin and scale (§2 scale chain); keep it as the locked reference collection.
2. Build one-off shells on the same snap grid; bespoke shells export at their world position (importer: "Set Pivot to Scene Origin" off, as the modeler uses it; whether "Insert Using Scene Position" must also be on is proved once with the calibration object at a known world position, then recorded in the scale record); reusable kit pieces export at their snap origin and are placed in Studio. Use the same grid the modeler uses for the kit (its interface contract).
3. After import, compare art and greybox bounding boxes part by part (`measure-captures.md` M8): differences stay under one snap step on every route edge, opening, cover piece and sight-line blocker, or go to the game designer as a proposal.
4. Shared trim-sheet SurfaceAppearances and kit pieces live as packages, so a material fix or a placeholder upgrade reaches every copy (`projects/assets/packages.md:14-19`; `tutorials/curriculums/environmental-art/assemble-an-asset-library.md:93`).
