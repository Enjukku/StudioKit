---
type: job
scope: universal
status: active
updated: 2026-10-20
source: owner chat 2026-10-20 (/build-agent character-rigger, then animator)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# J005 intent brief — rig workflow + character-rigger

<intent>
The owner wants motion that never breaks the model: no seams, stretching or body skew when the head or a limb moves. The way there is a workflow where each role does what it knows best. The animator says what must move, how far and how; the rigger turns that into a joint and bone plan and says which parts must be separate, where the cuts go and why; the modeler cuts, cleans seams and re-models, and may push back with a better cut; the rigger checks that result, rigs it and tests it, and sends problems back as one exact note; the animator animates on a tested rig and reports rig problems back. This loop matters most for Tripo models, which arrive as one merged mesh. The first game showed why: skinned fused limbs webbed and wrinkled, and a neck mesh creased; separate pieces with hidden roots fixed it. The papers are strong evidence, not gospel: numbers, Blender facts, Roblox facts and Tripo facts get checked, and what cannot be backed up is dropped or kept only as OPINION.
</intent>

<spec>
id: J005
from: owner
to: lead
skills: [orchestration, ste-writing, reference-images, performance, studio-mcp]
refs:
  - C:\Users\Firew\Downloads\uterd\NewGame\Roblox_Character_Rigger_Research.txt   # take: all; avoid: vendor capability claims as quality proof
  - C:\Users\Firew\Downloads\Animator_Research_Paper.txt   # take: §2 body inventory, §9 rig manifest + export, §10 Roblox runtime, §12 hand-off; avoid: timing numbers (J006)
  - ..\DestructionSimulator\rules\character-rigs.md, ..\DestructionSimulator\knowledge\reference\character-part-rigging.md   # take: owner experience, seam methods, checklist ideas; avoid: game-specific decisions as kit rules, UNVERIFIED angles as defaults
  - knowledge/jobs/J005-character-rigger/workflow.md   # the approved workflow (after owner review)
fixed:
  role_name: character-rigger            # owner 2026-10-20; roster row exists
  tier: craft → opus, effort high        # owner 2026-10-20 "Opus, high effort for both agents"
  tools_in_use: Blender (Python + Blender MCP), Roblox Studio (Studio MCP)   # owner 2026-10-20
  messages_format: rules/messages.md     # owner 2026-10-20
  new_roster_row: modeler (planned)      # owner 2026-10-20
open: [book structure inside the skills below, recipes, script design, eval wording]
not_in_scope: [modeler role build, animator skills and role (J006), game code]
rules:
  - Paraphrase sources; papers stay outside git.
  - Every number, Blender, Roblox and Tripo fact cites its source and fact-check verdict.
  - Keep evidence tags; never invent budgets, joint angles, loop counts or bone caps.
  - No DestructionSimulator specifics in kit files; owner history is cited as EXPERIENCE only.
  - Skills ≤ 500 lines, kit template, project-overlay line.
deliver: knowledge/reference/rigging/*, .agents/skills/{rig-pipeline,rigging-design,rigging-craft}/*, templates/rig/*, tools/rig/*, .agents/roles/character-rigger.md, roster rows, evals
checks: see job-card.md acceptance checks
return: step 1 review + G1 to owner now; G2 first real test; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `rig-pipeline` | shared | Stages S0-S8, who decides what, checks between stages, rig sheet, fix note, Tripo route table, change control, modeler hand-off, timing-list pointer | animator, character-rigger, modeler, lead |
| `rigging-design` | design | What makes a game rig great; rigid vs skinned vs mixed per region; joint placement from motion; what animation needs from a rig (from the animation paper: active vs passive parts, contacts, held tools, wings, tails, multi-legs); Tripo decision; seam-hiding choices; faces; mechanical rigs; Roblox runtime choices; failure diagnosis | character-rigger, animator, modeler |
| `rigging-craft` | craft | How in Blender 5.x + MCP: inspect, cut-plan renders, proxy sweep, skeleton, weights (prune then normalize), controls and manifest, export profile, Studio import, test clips, audit script, failure table, self-check | character-rigger |

## First real test (G2), proposed
One raw merged Tripo character from the first game's sources (default: `DestructionSimulator/content/art/story/models_src/teddy/teddy+bear+3d+model.fbx`, read-only copy) goes through S2-S5 with the stand-in modeler, at least one real fix-note round, Blender tests and a Studio import with test clips. Shown next to the first game's final rig (`golem_v3_roblox.fbx`).
