> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Facts: `knowledge/reference/modeling/fact-check-roblox.md` (MR35-MR46), `fact-check-blender.md` (MB), rigging fact-checks (RB23, RB31). The scale chain is shared with the environment designer: `environment-craft/references/blender-to-studio.md` §2-3 is the one source; this page adds what models need. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the game-camera capture after import (§3).

# Export from Blender, import into Roblox

## 1. Scale chain (once per project; record it)
- Blender: Unit System None, Rotation Degrees, 1 Blender unit = 1 stud (MR36).
- FBX: Apply Scalings = FBX Unit Scale, all other scale values 1.0 (MR36, MR38). Never stack a 0.01 export scale or a 0.01 scene unit scale on top: the model comes in 100 times off (DNT07).
- glTF: needs no scale fix; its import hierarchy differs (each mesh node becomes a Model with one MeshPart per primitive) (MR40).
- 1 stud ≈ 28 cm is the Roblox reading for physics; it is not an export setting (MR35).
- **Calibration round trip** before the first real model of a project: a block of known size with a marked front, plus the player dummy; export, import, measure. Only then build in bulk (`environment-craft/references/blender-to-studio.md` §3).

## 2. The export copy
1. Work file stays editable. Make an **export copy**: apply the agreed transforms, set names and part origins (pivots where parts rotate, never all at world origin; the rigger owns joint pivots), apply needed modifiers (FW-11 [O]).
2. Select only the approved objects: no cameras, lights, reference planes, dummies, high-poly bake sources, hidden helpers (EXP10 [O]; review "clean export").
3. Export with the kit profile: `tools/rig/roblox_fbx.py`, `export(path, kind="rest")` for static or rigid models; the rigger exports rigged files. It sets every option by name, because Blender's FBX defaults are wrong for Roblox (rigging fact-check RB23, RB31). Run `check_exporter()` first; a missing option name stops the export.
4. Recount triangles on the export copy (after triangulation) and write them in the asset record (FW-11 [O]).
5. Keep a versioned export; never overwrite the only accepted file (PRC18 [O]).

## 3. Import into Studio (in the test place, never the live place; J005-D6)
| Importer setting | Default | Use | Source |
| --- | --- | --- | --- |
| Scale Unit | Studs | Studs (matches the scale chain) | MR41 |
| World Forward / World Up | Front / Top | keep; verify with the calibration object's marked front | MR41 |
| Set Pivot to Scene Origin | on | off when part origins must be kept (hinges, wheels, doors) | MR41, MR42 |
| Merge Meshes | off | keep off for anything with moving parts | MR42 |
| Keep Zero Influence Bones | off | rigged assets only; the rigger decides | MR41 |

- Read every importer warning; a warning is evidence to resolve, not noise (PRC19 [O]).
- After import, measure: size (`Model:GetExtentsSize()`), orientation, part count and names, pivots, materials and maps, normals, collision. Compare with the Blender numbers (import parity).
- Then judge the look where players meet it: place the model on the real ground of its stage (or the closest approved place), capture it at the game camera (`screen_capture` with the camera position and target from the game profile; restore the camera after), take its mask capture from the same camera, and run the read measurements on the capture at phone size with that mask (`modeling-craft` §7). Record the graphics quality level used; when the brief names a lowest supported level, the anchors and the value read must hold there too (set by hand or by the owner: not scriptable). The Studio capture, not the Blender render, decides colour and value.
- **Held items** (weapons, tools, anything a character carries) are judged in the hand, where players meet them, not lying on the floor. Make a test copy as a `Tool` with exactly one part named `Handle` and `Tool.Grip` set from the grip pivot in the attach-point record; start a play-test on the real ground, equip it (`execute_luau`, `datamodel_type` Server: `Humanoid:EquipTool`), capture from behind at the default play camera and once from the front (Client: `CurrentCamera` Scriptable at the front game-camera position, restored after), each with its mask capture (the mask then holds avatar and item: the item must separate from the avatar's outline, SL1-SL2). `screen_capture` can time out in Play: retry once; still failing, take the edit-time capture on the ground for the numbers and put the in-hand read on the could-not-check list as `not verified`. Not yet run in this kit: the first run is a probe; record the working recipe in the asset record.
- Studio shows the asset to its uploader; that does not prove live players can load it. Set the asset's permission for the experience; never make an asset public to fix a permission error (MR43, DNT12). New accounts default to Restricted for new meshes and images since 2026-05-05 (MR43).
- Studio MCP is for checking the import (`studio-mcp`, MCP-verified label); in files mode it never edits scripts. The owner may click the import itself when the brief says so (J005-D6).

## 3a. First-game import lessons (FM ids [E])
- Roblox culls back faces: panels facing into the shape were invisible in game although Blender showed them; faces very close to another surface z-fight at distance (FM62). Check face direction (audit: inverted parts) and keep surfaces apart.
- Imported MeshParts arrive with an empty TextureID and default collision: set both on purpose (FM67).
- An uploaded texture returns a Decal asset id; `MeshPart.TextureID` needs the image id behind it (FM68).
- The first import of a project is a pilot for axes, scale, pivots and joints (FM66). Never apply an exporter fix and a place fix together: the model moved twice (FM78).
- Keep seat, pivot and effect points in one record per model, in Blender space, with the Roblox mapping beside them (FM76; `references/handoffs.md` §3).
- **Upload is an owner gate**: nothing is uploaded before the owner approves; a dry run lists exactly what would upload; keys stay outside the repo (FM89, owner, first game).
- Uploaded is not in the game: keep an id registry per asset family and mark each USED / UNUSED / STALE; track models built but not uploaded (FM91-FM93).

## 4. Reimport
Reimport keeps properties, hierarchy, CollisionFidelity, RenderFidelity, the file path and import preset; it does not version assets. A rig reimport deletes bones missing from the new file and replaces WrapTargets (MR44, MR46). Auto-Reimport is a Studio beta (MR45). So: keep the old export, reimport in the test place, then compare attachment names, part count and collision before accepting.

## 5. When the import looks wrong (TRI01-TRI07 [O])
| Symptom | Look at first |
| --- | --- |
| Wrong size or facing | scene units → object transforms → export conversion → importer scale; change one layer at a time |
| Texture missing or wrong | baked images and map slots; a SurfaceAppearance hiding a TextureID (MR13); look at a render, not file names |
| Bumps look like dents | normal map tangent space; flip green (MR19) |
| Wrong pivot or parts fused | Set Pivot to Scene Origin and Merge Meshes settings |
| Fine in Studio, broken live | asset permissions; beta-only features |
| Looks damaged far away | mesh streaming on? cloud LoDs ignore RenderFidelity (MR26) |
