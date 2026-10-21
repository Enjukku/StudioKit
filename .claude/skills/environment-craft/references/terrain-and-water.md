> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit reference: universal. J008. Facts: `knowledge/reference/environment/fact-check-lighting.md` (LF40-LF43, LX03, LX08), `fact-check-performance-import.md` (PI25, PI50), `05-roblox-look-dev.md` (LD51-LD53). Design rules: `environment-design/references/place-reading.md` §5 and SKILL E-05. Docs paths relative to `knowledge/external/roblox-creator-docs/`.

# Terrain and water

## 1. Facts
| Fact | Source |
| --- | --- |
| Terrain is a grid of 4×4×4-stud cells; each cell has an occupancy 0-1 and a material; occupancy morphs neighbouring cells into a smooth surface | `_api-reference/classes/Terrain.yaml:11-16`; `parts/terrain.md:13` (LF40, PI25) |
| Heightmap and colormap import: 1 pixel = 4 studs, JPG or PNG, at most 4096 × 4096 px (a cap on import size, not a world size); height follows the selection region's Y size | `parts/terrain.md:291, 468` (LF41, PI50) |
| Scriptable operations: FillBlock, FillBall, FillCylinder, FillWedge, FillRegion, ReadVoxels, WriteVoxels, CopyRegion | `Terrain.yaml:424, 472, 506, 542, 579, 614, 844, 1232` (PI50) |
| `MaterialColors` recolours any material except water; `Decoration` turns on animated grass on the Grass material; `GrassLength` 0.1-1. All three are NotScriptable: set them in Studio Properties | `parts/terrain.md:189, 213-221`; `Terrain.yaml:27-61, 95-108` (LF42-LF43, LX03) |
| Water: WaterColor, WaterReflectance (0-1, default 1), WaterTransparency (0-1, default 0.3), WaterWaveSize (0-1), WaterWaveSpeed (0-100); some show only while playtesting | `Terrain.yaml:145-235`; `parts/terrain.md:122-166` (LD52) |
| Custom materials: MaterialVariant works only under MaterialService; terrain looks change only through material overrides, which are global per place (at most the built-in materials, override names not scriptable); StudsPerTile larger = bigger, less repeated texture | `MaterialVariant.yaml:10-18, 471-476`; `parts/materials.md:109-114` (LX08, LD51) |
| GlobalWind moves terrain grass; Reduce Motion slows it | LF32, LF34 |

## 2. How the environment designer uses terrain
1. **Every area gets ground with height changes and visible layers** that fit the theme (lawns round houses, plazas in a city, rock strata on a cliff). No buildings on a flat plane (FS-T01, owner D-106).
2. **Block the big forms first** with fills from the blockout coordinates (Luau through `execute_luau`, Edit context, bounded regions); sculpt by hand only where the shape needs it. Keep the route's walkable surfaces exactly where the blueprint puts them.
3. **Terrain for big continuous forms, meshes for designed silhouettes** (cliff faces, overhangs, cave shells, stylized strata): sink meshes into the terrain so the join reads as construction; check every seam from eye height and from the ends of the route, from both sides, with collision visualization (PR-23; BW04).
4. **Paths join a network,** every door meets a path, the main walkway is never cut by water or scenery, and every pit, river and high place has a way out (FS-T03-T05).
5. **Boundaries look like the world** (cliffs, water, walls on theme) and are backed by a real barrier; collision, fall and reset rules match what players see (FS-T07; `level-design` L-09).
6. **Water is several jobs:** the surface look (water properties), how players move in it, its sound sources (ambience map), mist (VFX request) and shoreline dressing. Check water levels against floors and walkways (FS-T08; PR-25).
7. **Material look:** recolour with MaterialColors and wet or dry variants through MaterialService overrides (Duvall Drive used about 10 wet terrain overrides for a rain-soaked place, LD88); these are place-wide choices, so record them in the look sheet. Grass decoration and GrassLength are manual Studio steps.
8. **Do not pay detail for ground nobody walks or sees** (FS-T09). Measure one representative area's cost before budgeting a whole stage (FS-T10).

## 3. Where ground meets buildings and landforms
- **One base per structure.** Each building sits on a pad at its floor height; the ground round it blends into that pad over a ring; no grass above a floor, no gap below it.
- **Smooth, not flat.** The owner wants relief, not a flat map, but height changes must blend: limit the step between neighbouring ground samples (the limit is a project value from the game designer's walkable step or the owner; `PROPOSAL` until set), keep fixed anchors (walkways, floors and their rings, water, cave cuts) and blend between them. Stairs and lanes rise in small steps; a step the player cannot walk is a wall.
- **Landforms share the ground's base.** A placed rock, cliff or hill mesh starts below the surrounding surface so it never looks sunk or floating.
- **Measure before and after.** Sample the ground height on a grid round each structure and along the route (rays down through `execute_luau`, or `Terrain:ReadVoxels` occupancy), list steps larger than the walkable step and floors that differ from the ground at their edge, and sort each step by its source (designed relief, generated noise or outcrops, building pad edge, landform foot, tool error). Switch off the sources that only add artifacts, keep the designed relief, lower or raise a floor where its ring cannot blend (list each floor change for the owner), and measure again (first-game case: `environment-design/references/diagnosis.md`). The scene audit does not check this yet.
- Terrain fills whole 4-stud cells with partial occupancy at the surface; write heights with occupancy, not only full cells, or the ground steps in blocks (LF40).
