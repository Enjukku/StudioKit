---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: J005-T06 (lead); DestructionSimulator (read-only) rules/character-rigs.md, knowledge/reference/character-part-rigging.md (2026-10-12), knowledge/design/decisions.md D-160, D-161, D-184, D-185, D-186, knowledge/design/tried-and-failed.md F-020, .claude/agents/animator.md, .agents/skills/animation/SKILL.md (2026-10-15)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# First-game experience with Tripo rigs and the earlier animator (kit-neutral lessons)

The first game (a destruction simulator with a stylized plush/toy story cast built from Tripo image-to-3D meshes, filmed in Blender, some also live in Roblox) is the owner's only hands-on rig evidence. Owner decisions are game-specific; the lessons below are EXPERIENCE for the kit. Game names, characters and file paths stay out of skills.

## 1. What failed (owner-observed)
| id | what was tried | what the owner saw | lesson | source |
| --- | --- | --- | --- | --- |
| FG01 | One merged Tripo mesh skinned as one piece | inner arms fused to the torso "webbed" on every arm raise | Fused bridges cannot be fixed by weights; separate or rebuild the bridge (agrees with rigging paper RP:186) | D-160, 2026-10-11 |
| FG02 | A new neck mesh joining a separated head to the body | the neck creased | Do not invent a bridge mesh to hide a head joint on a no-neck body; bury the head root in the body instead | D-185, 2026-10-12 |
| FG03 | Variants made by reshaping (bending) a finished rigged body | "their bodies become deformed after you shape them differently"; shoulder lumps | Variants come from one cut base with re-seated sockets, never from bending the rigged body | D-185, 2026-10-12 |
| FG04 | Skinned Tripo arms | "the arms have always been like an area where it gets messed up when it moves. It becomes like wrinkly" | Candy-wrapper / collapse at skinned joints on generated topology; owner asked for shoulder, arm and hand as separate pieces | D-186, 2026-10-12 |
| FG05 | Closing Tripo open shells by pushing along normals, deleting faces, hole fill, Laplacian membrane, membrane with nearest UVs | shards, see-through holes, only 3 of the new loops closed (body had 487 open edges), dark sheet, stretched stripes | Inspect open edges first; a tuck-and-cap (radial tuck to the first inner shell hit) worked; deleting faces into a body opens holes | F-020, 2026-10-11 |
| FG06 | One Tripo texture atlas shared by all cut parts | failed (cause not recorded) | Give each cut part its own UVs and re-baked texture | character-part-rigging.md §g |
| FG07 | Tail model passing through a cape | clipping | Clearance between moving parts and cloth is a rig-sheet item; owner chose to reshape the cape (look change → owner) | D-161, 2026-10-11 |

## 2. What the owner approved as the method (first game)
| id | method | owner words | kit status |
| --- | --- | --- | --- |
| FG10 | Every moving part its own closed mesh (body, head, ears, upper/lower limbs, hands, feet, tail sections), each skinned only to its own bones; the body never moves when a limb, head or tail moves (measured body delta 0) | "making the arms and stuff their own model. Um, same with maybe the feet and tail. So you can um, rig it properly" (D-160); "separate the head, um, just like we did with everything else" (D-185) | becomes route R-cut, first try for stylized merged characters (J005-D2 item 3); not a universal rule |
| FG11 | Joints hidden by overlap: a rounded root dome buried in a socket of the neighbour; the visible join is an intersection line in a natural crease, tuft or collar | D-185 via the research note | seam-hiding option "socket / overlap" |
| FG12 | Bone-only for anything live in Roblox; film extras (cloth sim, Preserve Volume, corrective shape keys) sit on top and are never required | rule 8 of the first game's rig rule | agrees with rigging paper rule 12 / do-not 12 |
| FG13 | Faces as a kit of separate parts (eyeballs with a look-at target and limits, lids or lashes, nose, mouth, brows); keep a face the owner likes exactly unless a side-by-side test matches it | D-184, D-186 | face route option; "owner-liked look is locked" is a general habit |
| FG14 | Own-face per character so a cast does not look like one character recoloured | D-186 | design point for the art director, not rigging |

## 3. Numbers from the first game's research note (all UNVERIFIED there; never defaults)
| item | value | status |
| --- | --- | --- |
| buried head root depth | 25-35% of head radius | UNVERIFIED, no pose test was run |
| root dome radius | 1.15-1.2 x limb section at the cut | UNVERIFIED |
| example ROM: head yaw ±25, pitch -15/+20, roll ±10; arm swing ±70, raise 80; leg swing ±40, spread 25; ear root ±35; tail root ±45 (degrees) | starting values | UNVERIFIED; the animator states ROM per asset in §B |
| rigid vs skinned elbow threshold | limb shorter than about 2.5 widths → rigid pair | UNVERIFIED threshold |
| loops at a skinned joint | "3 tight loops" | sources disagree (2-3, 3-4, 5-7); rigging paper: no universal loop count (RP:188). Drop as a rule |
| sphere-dome geometry check | dome of radius r at depth d meets a flat surface in a circle of radius sqrt(r^2 - d^2); limb radius at the surface must be smaller | geometry identity (true); useful as a socket check |

## 4. The earlier animator (2026-10-15) — what still holds
| keep | drop |
| --- | --- |
| Three jobs: show what happens, believable weight, personality | Game-specific rig paths and film plans (§9 of the old skill) |
| Prepare from reference; pose-to-pose; 3-5 tries | "Never set gameplay timing yourself" stays, reworded: gameplay owner sets windows |
| Line of action, balance, prop weight, 2-3 personality adjectives, silhouette test | Old effort setting (medium): owner now sets animator to Opus high |
| Animation sets as states + transitions + interrupts; priorities; markers for gameplay, sound, VFX sync | "Destruction motion is physics" (game-specific) |
| Check the rig can reach every key pose; report rig changes instead of working around them (now: rig note, rig-pipeline §4) | Riot-transcript-only claims without dates where the new paper is stronger |
| Animation card per clip; review checklist (read at game distance, anticipation before threat, consistent weight, no accidental linear easing, personality, clean transitions, marker sync, cohesion with UI/VFX/camera) | — |

## 5. Cross-check with the rigging paper
- FG01, FG04 agree with RP:186-192 (false bridges; topology before weights) and the region table (plush or toy → cut where design hides a break; bare skin → skin).
- FG10's "body delta 0" is the rigging paper's head-isolation / protected-region test (RP:273, RP:486) with tolerance 0 for rigid pieces: measurable by `tools/rig/rig_audit.py`.
- FG12 agrees with RP:281 (Preserve Volume preview only; Roblox result is authoritative).
