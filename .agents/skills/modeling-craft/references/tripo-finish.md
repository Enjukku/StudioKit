> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Facts: `knowledge/reference/modeling/fact-check-tripo.md` (MT ids; ST01-ST22 = what the owner can set in Tripo Studio; "rule N" = line N of its "Rules a skill may state"; every page read 2026-10-21, docs only, nobody logged in). Rig-side Tripo tools: `rig-pipeline/references/tripo-routes.md`. Owner runs Tripo (J007-D4). Tripo changes fast: re-read the Studio panel before trusting a row; a control marked "unknown" may exist. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): restoring iconic qualities (§2-§3).

# Tripo route: input pack → owner run → raw check → finish in Blender

## 1. The input pack (the modeler writes it; the owner runs Tripo)
Folder `content/models/<asset-id>/tripo/input/` with the images and `run-sheet.md`:

| Item | What to write | Why / source |
| --- | --- | --- |
| Images | **single**: one clean subject, three-quarter front view, open stance (T- or A-pose for characters), subject 70-85% of the frame, plain even background and light, ≥ 1024 × 1024, no labels, no other subjects, nothing overlapping. **multiview** (2-4 images, paid plan for P2.0): the same design, pose, scale, light and background in every view, one image per view, file names `front.png`, `left.png`, `back.png`, `right.png` | Tripo advice ST03-ST04, rules 10-12; "left" is not defined in Tripo docs: name it the **subject's own left** and say so on the sheet; owner, first game (extra views in one image make extra models) |
| Family | P Series (Smart Mesh, "Clean Topology") for most rigged or game models; H Series (HD Model, "Best Quality") when the surface and texture detail are the point and the low mesh is rebuilt or baked anyway | ST01; H reaches about 2 million faces, a ceiling not a budget (rule 5) |
| Version | P2.0 (Studio "current"; API id P2-20260801 still Preview) or H3.1 (API v3.1-20260211) | rules 2, 25; record what the panel shows |
| Polycount (P) | target ≈ the asset's triangle budget minus room for caps and fixes (e.g. 6,000 triangles for a 7,000 budget); the field is a target, so count the output | ST06, rule 6; owner J007-D5 |
| Topology | Quad for P (default), export FBX so quads survive (OBJ and GLB may triangulate) | ST10, rule 8 |
| Texture | P makes geometry only: texture afterwards (Tripo Texture module or our own bake). H: 2K tier is enough for Roblox phones (runtime ≤ 4K, our budgets ≤ 1024); **Remove Lighting: On** so lighting is not baked into the colour map (default Off; it changes the base colour map only) | ST11, ST13; budgets §4 |
| Variants | 1, or 2-4 polycount variants on Pro/Max/Team for the same credits; variants are not a LoD chain | ST09 |
| Parts / segmentation | do **not** run Tripo segmentation or Auto Split unless the rig sheet's cut list says its boundaries fit; the rigger's cut list wins; Quick Cap makes flat caps (a construction result, not a hidden socket) | ST14-ST15; tripo-routes §3 |
| Auto-rig | no: Studio has no Roblox/R15 preset and its skeleton cannot be edited; the character-rigger rigs | ST19 |
| Retopo / Smart UV in Tripo | no for P output (P cannot be retopologized); Studio Smart UV **discards textures**. Do these in Blender | ST17-ST18 |
| Export | FBX, textures included, no rig, no animation; no scale, pivot or axis control is documented, so we fix those in Blender | ST20-ST21 |
| Record to return | plan, family, version as shown, every setting, task or model id, date, privacy setting, credits used | rules 22-23; asset record "Tripo record" |
| Licence | keep the model private on a paid plan; the free-tier rights conflict across Tripo pages (rule 23) | the owner decides; never promise free-tier clearance |

The owner drops the exported files in `content/models/<asset-id>/tripo/raw/`. **Raw files are never edited** (source snapshot).

## 2. Raw-candidate check (before any clean-up work; FW-04, TR-32 [O])
1. Import a copy; measure size, objects, materials, textures, UV maps; run `tools/model/model_audit.py` (triangles, open edges, loose parts, inverted parts).
2. Look in **clay** (no texture), **wireframe** and **face orientation**, from the reference angle, the back and the underside: texture can paint a feature that has no shape; backs and undersides are invented and often wrong (TR-31, TR-34 [E]).
3. Compare silhouette and landmarks with the approved reference at the same camera, and each iconic quality listed in the record (`modeling-design/references/reference-check.md` §7): note every one Tripo softened (rounded tips, mushy planes, lost proportion pushes, a generic face).
4. **Reject early** (send back to the owner with one exact note, or switch to hand modeling): wrong anatomy or part count, fused grips, missing openings, false backs, weak identity, fused repeated limbs that cannot be copied clean (FM41), a mesh far over budget with no clean way down. Max 2 regenerations, then the lead decides (route change).

## 3. Finish in Blender (FW-05..FW-13 [O]; the steps are a studio procedure, not measured results)
1. **Working copy**; scale to studs, set front and up, apply transforms.
2. **Rig parts first** (if it moves): cuts, caps, bend zones per the rig sheet (`references/rig-parts.md`). Treat any Tripo part split as a proposal; the rigger's cut list wins (X-04).
3. **Simplify by error, not by count**: decimate only static, irregular pieces where the silhouette survives; retopologize joints, silhouette turns and mechanical contacts by hand (FW-07; HM14-HM15 [V] B06, B07).
4. **Repair shape as shape**: a missing handle is modelled, never painted on (FW-08). Fix normals, thin slivers, intersections. Restore the iconic qualities the raw model softened: re-sharpen tips and planes, push the anchors back past the reference, rebuild a generic face to the anchor images; the black-fill at the game camera matches the frozen blockout or beats it.
5. **UVs after structure is final**, one map per mesh; then **re-bake** colour (and normal if the plan uses it) from the untouched raw model onto the finished mesh (FW-09; `references/textures-materials.md` §4). Repaint baked light or cast shadows the art bible does not want (TX-45).
6. **Materials to the texture plan**, not Tripo's defaults (4K or 8K maps are reduced to the plan) (FW-10).
7. **Export copy**, recount triangles, export, import, measure (`references/export-import.md`).

**Hero option to test (PROPOSAL, J007 G2 test B):** run the same images as H3.1 (high source with texture) and P2.0 (clean low mesh near budget); align them in Blender; cut and finish the P mesh; bake the H colour and normal detail onto it. Unproven: alignment between two generations may need manual fitting; record the time it takes.

## 4. Never
- Never quote a Tripo success rate, clean-up time or "production-ready" claim (rule 24; TR-35).
- Never import a maximum-detail result as the game model (DNT03).
- Never ask the owner to log in for you, share credentials or spend credits outside the approved brief.
- Never edit the raw folder.
