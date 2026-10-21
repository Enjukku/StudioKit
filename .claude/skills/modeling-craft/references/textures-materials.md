> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-craft`. Facts: `knowledge/reference/modeling/fact-check-roblox.md` (MR), `fact-check-blender.md` (MB). Paper notes: `02-*.md` §11 (TX ids), `01-*.md` (HM16-HM17). Sizes are starting points: `modeling-design/references/budgets.md` §4.

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
