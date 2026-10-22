> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-design`. Facts: `knowledge/reference/modeling/fact-check-roblox.md` (MR ids, read 2026-10-21). Paper notes: `knowledge/reference/modeling/02-*.md` (BG, TX, CK ids). Owner: J007-D5. Revised by J018 maker modeler · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018): the detail budget by display size (§8).

# Budgets: ceilings, project budgets and measurement

## 1. Three numbers that are not the same
| Kind | What it is | Where it comes from | May the modeler use it as a target? |
| --- | --- | --- | --- |
| **Ceiling** | The most Roblox (or Tripo) accepts | platform docs (§2) | No. Passing a ceiling proves upload, not phone cost |
| **Project budget** | What this game spends per model kind | the owner, the game profile, or a measured phone scene (§3, §5) | Yes. This is the target |
| **Comparison** | Another production's number (a Dota slot, a Roblox sample place) | case studies | No. Context only (MP:637 [O]) |

Never promote a ceiling or a comparison into a budget. Never split a heavy model into several meshes only to pass the per-mesh ceiling (BG-02 [O]).

## 2. Roblox ceilings (checked 2026-10-21)
| Asset category | Ceiling | Source |
| --- | --- | --- |
| Any imported mesh (generic MeshPart) | ≤ 20,000 triangles; watertight; real thickness; quads where possible | MR01, `art/modeling/specifications.md:34-37` |
| Avatar body (Marketplace) | head 4,000, torso 1,750, each limb asset 1,248, total 10,742 triangles; 15 named meshes | MR03 |
| Rigid or layered accessory (Marketplace) | one mesh, ≤ 4,000 triangles | MR04 |
| Marketplace textures | ≤ 2048 × 2048 | MR05 |
| Skinned vertex | ≤ 4 bone influences; no Root influence | MR06 |
| Material and UVs | one material per mesh; one UV set; UVs inside 0-1; overlap allowed | MR12 |
| Texture rendering | up to 4096 × 4096; 8K uploads are stored but run at 4K at most | MR08 |
| 4K on phones | not guaranteed: texture streaming disables 4K on low-end Android under 3.5 GB (status 2026-03-23) | MR10 |

Name the asset category first: avatar limits apply only to platform avatar items, never to a custom NPC, pet or creature (MR02).

## 3. Project triangle budgets (whole model, all parts together, evaluated and triangulated)
| Model kind | Budget | Status |
| --- | --- | --- |
| Character, NPC, creature (incl. hero pets) | **under about 7,000** | owner J007-D5: "Even for like things like creatures, we should probably keep it like under 7k or whatever." |
| Small pet (many on screen at once) | ≤ 3,000 | PROPOSAL (owner confirms at J007 G2) |
| Vehicle | ≤ 7,000 | PROPOSAL, matched to the character budget |
| Held weapon or tool | ≤ 2,000 | PROPOSAL |
| Small prop (fits in a 5 × 5 stud box) | ≤ 1,000 | PROPOSAL |
| Large prop | ≤ 3,000 | PROPOSAL |
| Building (whole, exterior) | ≤ 7,000 | PROPOSAL |
| Modular kit piece, rock, plant | ≤ 2,000 per piece | PROPOSAL |

- The game profile or a game overlay may set other numbers; they win for that game.
- "Under about 7,000" is read as the whole model (all meshes of one character together). A rigid-piece rig splits the same budget across its pieces. If the owner means per mesh, the overlay says so.
- Spend triangles where they change the silhouette at the game camera, a bend the animator needs, or a material edge. Never spend them because the budget has room (CS5-c [O]).
- Count the evaluated, triangulated mesh after modifiers, the number the exporter writes, not the viewport face count (RU04 [V] B03, B09, B10; `modeling-craft`).

## 4. Textures and materials (starting points, not budgets)
| Rule | Value | Status |
| --- | --- | --- |
| Roblox size guidance | 256² for a 5 × 5 stud object, 512² for 10 × 10, 1024² for 20 × 20 | [V] MR11 |
| Roblox PBR guidance | 256² per 2 × 2 × 2 stud volume, 1024² stated maximum | [V] MR11 (the page also says 4096 elsewhere: MR09, so state "4K supported, not a target") |
| Character or creature | one 1024² set | PROPOSAL |
| Weapon, tool, small pet | one 512² set | PROPOSAL |
| Small prop | 256², or a shared atlas or tint | PROPOSAL |
| Maps may differ in size | e.g. normal 1024, colour 512, roughness 256, no metalness in one Roblox sample | [E] MR15, not a budget |
| Palette variants | one grey-scale colour map + SurfaceAppearance tint instead of one texture per colour | [V] MR16 (tint costs nothing extra per the docs) |

## 5. Reuse and draw calls
- Meshes with the same MeshContent share a draw call only when their SurfaceAppearances match (or TextureContents, or materials) [V] MR24. Upload each mesh once and duplicate it in Studio; the importer does not de-duplicate.
- An atlas cuts texture count; it does not merge different meshes into one draw call (DNT10 [O]).
- A Blender linked duplicate is not a shared Roblox asset after import (ENV07 [O]).
- Build kits from a few canonical pieces with planned variants; a variant must change silhouette, function or story, otherwise it is a tint (ENV19 [O]).
- Reuse before making new: search the game's asset library and approved asset ids (Studio MCP `search_game_tree`, the asset records) for a mesh, material or trim that already does the job; reuse, recolour, then make new. The hand-back names what was reused and what is new.

## 6. Collision and distance
- CollisionFidelity has five options: Default, Hull, Box, PreciseConvexDecomposition, Tunable (Tunable adds CollisionPrecision 0-1, set in Studio). Tunable did not replace the others [V] MR25.
- Choose collision for gameplay, not looks (BG-41 [O]):
  - **Walkable or stood-on meshes keep Default** (or PreciseConvexDecomposition for merged multi-piece meshes). Box or Hull on walkable meshes made players float in the second game; the owner had it reverted (FM71, owner, first game: "make these ones have more accurate collisions"). Test with foot-height checks, not surface tops only.
  - Box or Hull only on parts nobody stands on or brushes against closely (small anchored props, distant pieces); a few simple proxy parts for blockers; no collision (CanCollide, CanQuery, CanTouch off) for pure decoration.
  - Doorways and walk paths stay open at real player size.
- Mesh streaming (`Workspace.MeshStreamingAndImprovedLoDs`), when enabled, ignores `MeshPart.RenderFidelity` and makes cloud LoDs; it does not support skinned meshes and does not change collision [V] MR26, MR29. Default-on was forecast for about July 2026 and is not confirmed: read the place's setting. Without it, the legacy Automatic bands apply (< 250 studs highest, 250-500 medium, ≥ 500 lowest) [V] MR28.
- A skinned creature gets no cloud LoD: it must meet its budget as authored.

## 7. Turning a PROPOSAL into a measured budget (when the owner asks, or a scene is slow)
Follow the `performance` skill. Minimum record (MP:647-657 [O]): asset kind and revision; scene, camera and visible count; named device; the ceiling and its source; proposed limits; before and after captures of the same scene; frame time and memory result; the accepted envelope and its conditions; who approved. Scene Analysis shows triangles and draw calls by render pass on the local machine only [V] MR32; MicroProfiler splits frame time (33.33 ms = 30 FPS, 16.67 ms = 60 FPS) [V] MR34. No phone, no phone verdict: write `not verified`.

## 8. Detail budget by display size (set with the triangle budget, step 6)
Triangles and texture pixels are spent where the player sees them, at the size they see them.
| Rule | How |
| --- | --- |
| Name the display sizes | on-screen height in px at the game camera on the smallest phone (from a Studio capture or from distance and FOV), plus the icon or shop-card size; in the read plan |
| Tier per size | in-game model: macro forms, the identity anchors and 1-3 detail spots; icon and shop close-up: the anchors bigger and cleaner; marketing renders may carry more detail than the game model, never the reverse |
| Sides | finish every side an orbiting or player-controlled camera reaches; skip a side only when the camera is locked and the record says which |
| Small features | a feature under about 4 px at phone size does not read (starting value, PROPOSAL): remove it, merge it into a larger shape, or paint it into the texture at low contrast |
| Detail in texture, not polygons | fur tufts, carvings, seams and small bolts are painted or baked (normal and colour) unless they change the silhouette, a bend or a material edge |
| Even texel density in a set | assets seen together share one pixel density on purpose; one sharper or blurrier asset looks out of place; the focal zone (face, hands, emblem) may carry more on purpose |
| Bigger is not better | a 1024² map uses four times the memory of a 512² map; the smallest size that holds at the game camera wins |
Check: `review.md` §5 DT2 (small features), DT9 (texel density); texture sizes against §4 and the record.
