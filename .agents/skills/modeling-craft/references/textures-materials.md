> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Facts: `knowledge/reference/modeling/fact-check-roblox.md` (MR), `fact-check-blender.md` (MB). Paper notes: `02-*.md` §11 (TX ids), `01-*.md` (HM16-HM17). Sizes are starting points: `modeling-design/references/budgets.md` §4. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): texture passes (§7), colour and light in the maps (§8), UV and projection craft (§9).

# UVs, textures and materials for Roblox

## 1. Platform facts (checked 2026-10-21)
| Fact | Source |
| --- | --- |
| One material per mesh; one UV set; UVs inside 0-1; overlapping UVs allowed | MR12 |
| SurfaceAppearance maps: colour, normal, roughness, metalness, emissive mask (five) | MR17 (`surface-appearance.md:53`; the meshes page still says "four": outdated) |
| A MeshPart uses TextureID or a SurfaceAppearance; a SurfaceAppearance hides a TextureID; with a MaterialVariant, the SurfaceAppearance gives the maps and the variant still gives physical settings | MR13, MR14 |
| SurfaceAppearance.Color multiplies the colour map (not MeshPart.Color); TintMask alpha says where tint applies; tinting has no extra cost per the docs | MR16 |
| Normal maps: OpenGL tangent space only (not object or world space); export tangents; if bumps look like dents, flip the green channel | MR19 |
| Emissive mask: only the red channel of an RGB image is read; hue comes from colour data and EmissiveTint | MR17 |
| Textures render up to 4096²; 8K uploads run at 4K at most; 4K is disabled on low-end Android under 3.5 GB | MR08, MR10 |
| The importer supports vertex colours (FBX, glTF) | MR21 |
| One report (2026-10-19): a ColorMap looks slightly darker than the same image as TextureID; unresolved. Do not auto-brighten every texture; compare in Studio | MR20 [E], DNT11 |

## 2. Pick the cheapest representation that keeps the approved look (TX-13 [O])
| Surface | Use |
| --- | --- |
| Identity-critical forms (faces, emblems, a hero weapon's head) | unique painted map |
| Repeating surfaces (walls, floors, rock) | tiling material or MaterialVariant, trim sheet |
| Palette variants of one model | one grey-scale colour map + tint (MR16), not a texture per colour |
| Many small props of one family | shared atlas (cuts texture count; not draw calls, budgets §5) |
| Flat stylized colours | material colour or vertex colours (check the look in Studio), no texture |
| Glow | emissive mask (red channel) + EmissiveTint; glow is not scene light (TX-17 [O]) |
| Hero finish tiers | separate parts or regions that each take their own finish (gloss against matte, an emissive inlay on a small area); a higher tier gets more finishes only when it ranks higher |

## 3. UV steps
1. UVs **after** structure is stable: retopology, cuts and caps first (FW-09 [O]).
2. One UV map per mesh, all islands inside 0-1. Seams where the camera rarely looks or along material borders; UV seams are not mesh cuts (TX-02 [O]; UVs live per face corner, MB rows).
3. Texel density: keep more pixels on the face, hands and focal parts on purpose; equal density everywhere is not the goal. Set the target only after camera distance and texture size are known; no universal pixels-per-stud number exists (TX-02 [O]).
4. Leave padding between islands for the smallest mip that will show (TX-43 [O]).
5. Check at the shipped size, not the paint file size (PRC13 [O]).

## 4. Baking (HM16-HM17; MB rows for the exact API)
1. Low-poly first: retopology done, triangulation and normals fixed, UVs final.
2. Bake high → low (Selected to Active) with a cage or ray distance; tangent-space normals; margin set for the mip chain.
3. Inspect cavities, contacts and close parallel surfaces for projection errors. A finished bake is not a pass.
4. Never bake a lit beauty render into the colour map; painted gradients are the art director's choice, cast shadows on a moving model are not.

## 5. Tripo textures
- Tripo's textures arrive with baked lighting and its own UV layout. Re-check palette and material separation against the art bible; repaint or re-bake when the light direction is baked in (TX-45 [O]).
- After any retopology or cut, the old UVs and textures no longer fit: re-unwrap and re-bake from the untouched raw model (`references/tripo-finish.md`).

## 6. Checks (numbers)
UV map count = 1 per mesh; islands inside 0-1; material count = 1 per mesh; each image's size within the texture plan; maps present for each SurfaceAppearance slot used. One Studio render under the game's lighting next to the Blender render (import parity).

## 7. Texture passes (step 6 of the skill): over the whole model, in this order
| Pass | Do | Check before the next pass |
| --- | --- | --- |
| 1 Regions | one flat colour per material, the unlit local colour from the reference's mid-tone; clean boundaries decided once | material slot (or ID colour) count = the material list; the value-gate renders show each region as one colour |
| 2 Value gate | grey view of the flat regions at the game camera (`modeling-design/references/review.md` §1 value-gate row), and in a Studio capture once one exists | `modeling-design/references/review.md` §5 VL1-VL5 |
| 3 Form | bake AO (and a short-radius AO for contact seams) and multiply it softly into the colour map; add plane-following light and shadow along the art bible's key light (lighter up- and light-facing planes, darker undersides), one clear terminator per major form | VL7 on the one flat unlit render at the main game camera: it reads as 3D without rotating |
| 4 Colour and edges | hue-shifted shadows and highlights (§8); crisp edge highlights from a curvature mask on hard materials, varied so part of the edges stay dim; soft transitions on organic materials; small, sharp, higher-contrast accents last, on top of the big value groups | CL4, DT3; the big value groups unchanged at phone size |
| 5 Story and wear | wear at touch points, grime where dirt gathers, chips and dents, theme nods, a few glints on light-facing edges, cracks that taper | DT5, DT7, DT8 |
| 6 Material read | maps tuned at the game camera under the game's Lighting in Studio; push a map until it is too much, then pull back | every material reads as itself at game size (stop criteria) |
Simple models (medium effort) may run passes 3-5 as one pass; each pass's check still runs. Before a new kind of material, finish a small test patch (one block) to find the method; get it approved before the full pass. Keep each material class's recipe (AO strength, curvature strength, noise scale, colour shifts) as data in `scripts/`, and reuse it for every asset of that class so a set matches.

## 8. Colour and light in the maps
The standards (values first, hue shift, no flat fills, gold and skin, extremes small, upper body brighter, judge in Studio) and their starting values live in `modeling-design/references/read-and-form.md` §3-§4. How to put them into the maps:
- **After every colour change** re-run the grey view; a colour that changes the approved value structure is a wrong colour.
- **Hue shift:** shadow = the local colour moved toward a darker hue, highlight = toward a brighter hue, saturation kept; temperatures as the art bible sets; a little of the main environment colour may tint shadows when the bible asks.
- **No flat fills:** mix 2-4 near hues by a noise mask inside each material.
- **Soft light that follows the key light:** bake AO at reduced strength; never bake a lit beauty render or a cast shadow into the colour map; heavy painted highlights fight Roblox's live light and any day-night cycle.
- **Contact shadows:** a thin dark seam where one part rests on another (strap on chest, plate on plate, prop on ground), from the short-radius AO bake or painted.
- **Glow** is an emissive mask on a small area, never a whole surface; a lasting glow reads as an active or empowered state, so objects that do not show that state get none.
- **Light placement** on hair, cloth and metal follows the art bible's painted anchors, not another 3D model.
- **Characters:** light colours below the waist painted a step darker and cooler.
- **Studio shift:** compare the Studio capture with the Blender render and correct in the map, never by brightening every texture.

## 9. UV and projection craft
- **Mirrored or unique.** Overlap mirrored UV halves on symmetric parts to halve texture space; give unique UV space to asymmetric story detail (cracks, badges, text, scars) on the sides the camera sees; never paint text or a crack on mirrored UVs.
- **Even density in a set; more on the focal zone.** Assets seen together share one texel density; the face, hands and emblems may get more on purpose (`modeling-design/references/review.md` §5 DT9).
- **Trim sheets for repeating structure.** One trim sheet with a normal map dresses walls, beams and frames by mapping faces to strips; a dull strip is remapped, not remodelled.
- **Project the concept as a base.** Align a camera to the approved view and project the image onto the model as a rough first texture; then fill gaps and repaint; check other angles for stretching.
- **Re-project when geometry changes.** Bake the old texture onto the new UVs (selected to active) instead of repainting; after the layout is locked, move silhouette vertices to follow major painted details (chips, carvings) only.
- **Paint against the real surface.** Check painted forms over a wireframe or matcap render so painted tufts and carvings sit on actual geometry.
- **Stylised and hand-painted assets** can skip the high-poly bake: the low-poly mesh is the source, a shape change is a re-export and a Studio reimport.
- **One mesh, one paint layer.** An object and its own base that ship as one mesh are painted across the join so it disappears; a part added later gets its own UV islands. Separate MeshParts cannot share a paint layer: leave the blend to the environment designer's decals or ground paint.
