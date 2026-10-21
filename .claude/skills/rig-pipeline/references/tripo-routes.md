> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `rig-pipeline`. Facts: `knowledge/reference/rigging/fact-check-tools.md` (RT ids, Tripo developer pages read 2026-10-21). Policy: rigging paper RP:213-251 [O]; owner J005-D2; first-game FG01-FG06 [E].

# Tripo models: one merged mesh → a rig

## 1. What arrives and what to do first
A Tripo model usually arrives as one object with head, body, arms and legs merged. **One object is not one connected surface** (rule 06): count connected parts, open edges, intersecting shells, UV islands and materials before anyone cuts (`tools/rig/rig_audit.py` `audit_mesh`). Save the untouched source and record every Tripo version id (§3).

## 2. Route per region (rigger, S2)
Studio rule (J005-D9): choose per joint. **R-cut** where a natural cover hides the cut (collar, bandage, cuff, crease, armour); **R-skin** where there is no cover and the surface must bend continuously (rebuild the bend zone first); **R-reject** when neither keeps the design. Most characters mix both. Full table: `rigging-design/references/region-routes.md`.

Why [E]: skinned merged limbs webbed to the torso (FG01) and wrinkled at the elbow (FG04); a bridge neck creased (FG02); deleting faces to close shells opened holes, tuck-and-cap worked (FG05); one shared atlas across cut parts failed (FG06).

## 3. Tripo's own tools are candidates, never acceptance (rules 10-12)
| Tool (endpoint) | Facts (RT, read 2026-10-21) | Who runs it | Accept only if |
| --- | --- | --- | --- |
| Rig check `POST /v3/animations/rig-check` | returns `riggable` and a recommended `rig_type`; a riggability screen, not a deformation check (RT12) | rigger, before any auto-rig | — (screen only) |
| Auto Rigging `POST /v3/animations/rig` | field `model`: **default `v1.0-20240301` is biped only**; `v2.5-20260210` for non-humanoids; `v3.0-20260909` recommended by Tripo for humanoids (vendor claim, no benchmark) and must be requested by name (RT01-RT04, RT07). `rig_type`: biped (default), quadruped, hexapod, octopod, avian, serpentine, aquatic, others (`others` needs v3.0) (RT08). `out_format` glb (default) or fbx; input GLB, FBX, OBJ, STL ≤ 150 MB (RT09-RT10). `spec` naming (biped only): tripo, mixamo, actorcore, unity, unreal, vrm — **no Roblox / R15 preset** (RT11). `task_id` input only from a generation task; an edited or segmented model goes in by URL or `file_token` | rigger, as a candidate | it passes the same audit as a hand rig: joint positions and axes, weights (≤ 4, no Root), names and roots against the export schema, every §B extreme, Roblox round trip (rigging-craft tests) |
| Mesh Segmentation `POST /v3/mesh/segment` | default `v1.0-20250506` (geometry); `v2.0-20260430` Beta adds semantic labels; v2 fields `segmentation_granularity` simple / balanced / detailed, `split_by_connectivity`, `ref_image` (when given, the other two are ignored); ≤ 150 MB (RT13-RT17) | modeler, when the cut list says its boundaries fit | rigger compares boundaries and pivots with the cut list; a semantic label is not a joint seam (do-not 8) |
| Smart Segmentation `POST /v3/mesh/smartsegment` | **includes modeling** (parts are re-generated); model input must be GLB with a 16-float column-major 4×4 `transform`; `granularity` coarse / medium / fine; optional `hint` (RT18-RT20) | modeler | plus silhouette, proportion, UV and material check against the approved reference |
| Retopology `POST /v3/mesh/decimate` | `model=v3.0` must be requested (default `v2.0`); `face_limit` 500-20,000 triangles or 500-10,000 quads (RT23-RT24) | modeler | quad output is not proof of good joint flow (RP:190); bend zones still checked at S4 |
| Smart UV `POST /v3/mesh/uv` | input ≤ 80,000 equivalent triangles (a quad = 2); says it remaps textures, rigging and animation (RT25) | modeler | re-check UVs and the rig after it runs (not tested by us) |

- Record every version id used: geometry model, segmentation, rigging, retopology, texture, Smart UV are separate (RT29).
- No polygon cap is documented for rig, rig-check, segment or smart-segment (RT28). Write "none documented as of 2026-10-21"; Tripo Studio UI limits: not found.
- Quality of v3.0 rigs or v2 segmentation: no independent evidence (RT48). Never state a success rate or repair time.
- Never call the Tripo API, create accounts or spend credits without an owner-approved brief that says so.

## 4. When Tripo's output is good enough (RP:233 [O])
Good enough only if it meets this asset's rig sheet: needed regions separated correctly, no missing surfaces, correct joints and axes, usable motion through every §B extreme, ≤ 4 influences and no Root weight, silhouette kept, textures kept, and it plays in Roblox. Otherwise:
| Failure | Fix route |
| --- | --- |
| wrong boundaries or pivots | manual segmentation (modeler) + manual pivots (rigger) |
| fused or poorly bending surfaces | retopology of the bend zone (modeler) |
| right geometry, wrong motion | manual bone and weight repair (rigger) |
| repair changes the approved design beyond scope | regenerate or remodel → lead → owner |

## 5. Other auto-riggers (RT30-RT44)
| Tool | Fit | Note |
| --- | --- | --- |
| Mixamo | bipedal humanoids only (Adobe FAQ, last updated 2021-09-14, re-checked 2026-10-21) | poor default for split toy parts, birds, quadrupeds, mechanisms (RP:239 [O]) |
| AccuRIG (free) | bipedal humanoids, hands with 0-5 fingers, no facial bones (CC Advanced adds them) | check the exact edition's export before use |
| Auto-Rig Pro | Humanoid and Universal export skeletons; custom bones export only when tagged | Blender add-on; Preserve Volume off to preview engine skinning |
| Rigify | builds a control rig from a metarig (FK/IK); does not bind the mesh | use after the skeleton is right |
| UniRig, Puppeteer, Skin Tokens / TokenRig | research; public repos (MIT, Apache-2.0, MIT); author-reported metrics; no Roblox exporter | local benchmark only, on the same mesh and acceptance set |
