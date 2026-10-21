> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `modeling-design`. Paper notes: `knowledge/reference/modeling/03-*.md` (REV, CHK ids), `01-*.md` (BK10-BK13). Check budget: owner J005-D8, J007-D7.

# Reviewing a model

## 1. Light checks (owner rule, wins over the paper's heavy review)
- **Numbers for every check** (the audit tool): triangles, loose parts, open edges, flipped faces, size in studs, materials, UV sets, texture sizes, part list vs the record.
- **One review render set per hand-off**: the reference views next to matching renders, one render next to the player dummy, one at the game camera. That is the self-review the owner asked for ("renders from several angles compared with the reference image, scale against a player").
- **More images only when a number fails**, and only of the failing area. No before/after image sets unless a number failed. Report how many renders were made and looked at.
- **One full check per hand-off, by the receiver** (rig-pipeline §4a). The sender's self-check is numbers plus the one review set.

## 2. The pass/fail list (CHK01-CHK18 [O]; a pass needs stored evidence, UNKNOWN is not a pass)
| Check | Pass evidence | How (light) |
| --- | --- | --- |
| Approved reference | image id and revision in the record | record |
| Identity and silhouette | recognizable at the game camera; signature features present | review set; silhouette overlap with the reference at the same camera (`tools/art/look_check.py silhouette --compare`) |
| Proportions | landmarks match the approved image or an approved exception | review set; numbers if a ratio is named |
| Scale | size in studs matches the record; next to the player dummy | number + one render |
| Part inventory | every required part exists once; no extras | number (object list vs record) |
| Connectivity | loose-part count matches the plan; no floating or fused parts | number |
| Hidden parts | no faces fully inside other faces that ship by accident | number |
| Surface orientation | 0 flipped faces where a closed surface is required | number |
| Moving parts (if rigged) | the rigger's S4 sweep passes | receiver's check |
| UVs | one UV set, inside 0-1, no stretched islands at shipped size | number; image on fail |
| Materials | one material per mesh; maps present; look survives Roblox light | number + the Studio render |
| Budget | evaluated triangles and texture sizes within the budget and its source | number |
| Collision | chosen fidelity per part; openings stay open | Studio check |
| Reuse | shared meshes on purpose; meaningful names | number |
| Import parity | size, orientation, part count and look match Blender after import | numbers + one matched render |
| Phone cost | measured only when the brief asks; no phone → `not verified` | `performance` skill |
| Clean export | no helpers, dummies, high-poly sources or hidden objects exported | number (exported list) |
| Lineage | reference, route, Tripo version and settings, export settings recorded | record |

## 2a. What the owner rejected before (check these in the review set before any hand-off; FM87)
| Rejected | Check |
| --- | --- |
| Built without an approved reference: "it's poorly built" (FM01, owner, first game) | approved image id in the record |
| Too small, a "miniature" with cramped insides (FM15, FM32, owner, first game) | size in studs vs the record; player dummy render; doors, stairs, seats at player scale (FM31) |
| Boxy shapes where the art is organic; furniture too coarse; directional pieces facing the wrong way (FM32) | review set by eye, facing listed in the record |
| Held prop that does not read from the front at game view (FM36) | game-camera render |
| Head accessory that looks wrong from the side (FM37) | side render |
| Limb that comes off the body when it turns (FM38) | joint covers centred on pivots; rigger's S4 sweep |
| Rideable model with no seat or rider cut-out (FM39) | seated test figure, high and side views |
| Props clipping the body in key poses, props not scaling with the form (FM40) | clearance in the animator's key poses |
| Micro-detail that costs triangles but adds no read: "a lot of triangles that aren't necessarily needed" (FM18, owner, first game) | triangles spent vs silhouette change |
| Generic ornament that ignores the theme or material (FM19, FM21) | ornament comes from the subject's own theme |
| Variants that are only recolours when the owner asked for different designs (FM20, owner, first game) | variant list: what changes in shape |
| A flat blockout or procedurally painted boxes shown as the finished look (FM53: "I want details, and I want it to look really nice.") | label blockouts as blockouts; texture pass planned |
| A plain, untextured look (FM61, owner, first game) | texture pass in the plan |
| Gaps between pieces, misplaced pieces: "incredibly sloppy" (FM85, owner, first game) | assembled kit render at player scale |

Keep an approved simple placeholder when the owner likes it; do not replace it unasked (FM22).

## 3. When something fails
1. **Sort the defect** (REV02 [O]): identity (silhouette, proportion, palette, signature feature), construction (loose or fused parts, inside faces, normals, holes, duplicates, unapplied transforms), motion (collapsed joints, open cuts, grip), runtime (collision, cost, materials, missing data after import).
2. **Fix the biggest effect first**, not the most visible close-up (REV03).
3. **Find the cause before editing** (BK12 [O]): geometry, camera, pose, material, light, or a bad reference. Change one cause at a time. A head that looks small only in a perspective render is a camera question.
   - **Drift from the reference:** render every saved revision (raw, each clean-up, final) in the **same camera, projection and lens as each reference view** (orthographic front with orthographic front, the same 3/4 lens), then read counts and ratios per revision. Repair at the first revision where a difference appears; never compare revisions shot with different cameras (BK10 [O], J007 hidden test).
   - **"Does not look like our game":** compare with the approved neighbouring models axis by axis, each with a number: value grouping and palette (`tools/art/look_check.py` value and palette), silhouette (`look_check silhouette`), edge treatment (bevel size as a share of height), surface roughness (mean of the roughness map), detail scale (smallest readable feature at the game camera). The range comes from the approved models, never from an outside threshold; fix the axes that fall outside it (J007 hidden test).
4. **Re-run every check the fix can break** (REV09 [O]): retopology changes UVs, bakes and bends; an atlas changes material groups; separating a part changes pivots, collision and rigging; an export option changes scale or normals.
5. **Repair tools are not fixes by default** (REV05-REV07 [O]): one global merge distance can close eyelids or fuse clothing to the body; never fill every open edge (an intended open cloth edge differs from a hole that motion exposes).

## 4. What the owner sees (REV10, REV11 [O])
Short evidence: the reference next to the model at the same angle, the player-scale render, the game-camera render, the numbers against the budget, open trade-offs, one recommendation. Taste is judged by people; numbers inform it, never replace it with an invented score. Label every check gate-verified, MCP-verified, owner-confirmed or not verified.
