---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent modeler)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J007 intent brief — modeler agent

<intent>
The studio needs one agent that makes every 3D model a Roblox game uses: characters, creatures, pets, weapons, tools, props, vehicles, buildings and environment pieces. A model is done only when three things are true: it reads as the approved design from the game camera, it moves the way the animator and rigger need, and it stays cheap on low-end phones. A good reference image, a good Tripo result or a clean upload alone does not prove any of these.

Every model starts from a ChatGPT reference image made with the reference-images skill and the game's art bible. The modeler checks the image before it builds (part count, views that agree, geometry that can exist) and attaches an approved image when the subject has one, so the design does not drift. Most models are built by hand in Blender through Python and the Blender MCP. Models that must look especially good are generated with Tripo from the reference, then cleaned and finished in Blender. Both routes end at the same checks.

For anything that moves, the modeler works inside the rig pipeline the rigger and animator designed (J005): the animator says what moves, the rigger says which parts are separate and where the cuts go, and the modeler makes the cuts, cleans the seams and rebuilds what needs it. It may propose a better cut or a better way to build a part, once, with the rig sheet rows it still meets.

The owner sees only reviewed work: renders from several angles next to the reference, scale next to a player, no floating or hidden parts, budgets met. The research paper is strong evidence but not gospel. Numbers, Blender facts, Tripo facts and Roblox limits are checked, and claims that cannot be backed up are dropped.
</intent>

<spec>
id: J007
from: owner
to: lead
skills: [orchestration, ste-writing, reference-images, rig-pipeline, performance, studio-mcp]
refs:
  - C:\Users\Firew\Downloads\Modeler_Research_Paper.txt   # take: 15 rules, asset record, reference checks, route choice (hand vs Tripo), Tripo 13-step finishing, articulation choice (skin / rigid / hybrid), texture and material rules, Roblox limits list (§8 items 1-10), collision and streaming, environment kits, export/import, review table, 22-step process, failure diagnosis, don'ts; avoid: treating OPINION recipes as tested, vendor demos as success rates, generator maxima or other games' limits as phone budgets
  - .agents/skills/rig-pipeline/ + templates/rig/   # take: S0-S8, rig sheet §D modeler keys, fix note, Tripo route table
  - knowledge/jobs/J005-character-rigger/modeler-handoff.md   # take: the S3 brief and checks C1-C5, adopted as-is
  - knowledge/reference/rigging/fact-check-*.md   # take: claims already checked; do not check them twice
  - .agents/skills/reference-images/ + tools/art/art_refs.py   # take: families, art bible, anchors; avoid: changing the skill (pointers only)
  - DestructionSimulator content-builder, brick-builder, art-fundamentals (read-only)   # take: universal build and art lessons; avoid: brick style, game names
  - GreatWallSim model work (read-only, list in job-card.md)   # take: model list format, hero import, modular kit, hook-up audit lessons; avoid: game names and themes
fixed:
  role_name: modeler                                    # roster; owner 2026-10-21
  model: opus                                           # owner 2026-10-21
  effort: high for hero models and new kinds of models; medium for simple models   # owner decision 2026-10-20, roster
  every_model_starts_from: approved ChatGPT reference (reference-images skill)    # owner 2026-10-21
  main_route: hand modeling in Blender (Python + Blender MCP)                     # owner 2026-10-21
  hero_route: Tripo from the reference, then Blender clean-up and finish          # owner 2026-10-21
  rig_split: animator - what moves; rigger - which parts, where the cuts go; modeler - cutting, seam clean-up, re-modelling, counter-proposals   # owner 2026-10-20 and 2026-10-21; J005-D1
  s3_brief: knowledge/jobs/J005-character-rigger/modeler-handoff.md, as-is      # J005-D1
  upload_ceiling_triangles_per_mesh: 20000               # knowledge/external/roblox-creator-docs/art/modeling/specifications.md:34 (ceiling, not a target, J007-D5)
  creature_and_character_triangles: under about 7000     # owner J007-D5
  tripo_operator: the owner (modeler writes the input pack)   # owner J007-D4
  checks: light - numbers for every check, images only on failure plus one review set per hand-off   # J005-D8, J007-D7
  hand_offs: rigger, animator, animator, art director, environment designer, VFX (attach points), UI (icon renders); rules/messages.md format   # owner 2026-10-21
open: [book structure inside the two skills, audit script structure, recipe choice per model kind, hand-off wording]
not_in_scope: [rigging, weights, animation, level placement, game code, art-director agent, Tripo API tool (J007-D4)]
rules:
  - Paraphrase sources; never copy paper text; the paper stays outside git.
  - Evidence tags kept. A number without a checked source is PROPOSAL or UNKNOWN, never a rule. Project budgets come from the owner or a phone measurement.
  - Nothing specific to DestructionSimulator or GreatWallSim in kit files.
  - The source snapshot (raw Tripo output, approved .blend) stays untouched; work on a copy.
  - Code and models live on disk (files mode); Studio MCP only checks imports, never edits scripts.
  - API keys (Tripo, OpenAI) only in environment variables, never in the repo, notes or chat.
  - Self-review from several angles before any render reaches the owner; label each check gate-verified, MCP-verified, owner-confirmed or not verified.
  - Skills ≤ 500 lines, kit template, "Read this file when" table, project-overlay line.
deliver: knowledge/reference/modeling/*, .agents/skills/modeling-design/*, .agents/skills/modeling-craft/* (evals/briefs.md included), .agents/roles/modeler.md, tools/model/*, tools/tests/test_model_*.py, knowledge/jobs/J007-modeler/handoffs.md
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 two real test models; G3 approval
</spec>

## Proposed skill books
| Skill | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `modeling-design` | design | What makes a game model read (shape hierarchy, silhouette at the game camera, material grouping); the asset record; checking a reference before building; route choice (hand vs Tripo) with reasons; skin vs rigid vs hybrid with the rigger; budget thinking (per-mesh limits vs scene budgets vs phone measurement); reuse and modular kits; review rules and failure diagnosis | modeler, rigger, art director, content-builder, lead |
| `modeling-craft` | craft | Blender through Python and MCP: scene units and player-scale dummy, blockout, bevels and normals, booleans and cleanup, cuts, caps and sockets for rig parts; Tripo route (inputs, settings to record, raw-candidate check, retopology vs decimation, re-bake); UVs and textures (sizes, one material per mesh, atlases); collisions; attachments for VFX and tools; export and Roblox import; audit script; self-review render set; hand-off packets | modeler |

## Known risks (to resolve in step 2)
1. Tripo facts change fast (P2 preview vs stable, Studio vs API features). Every Tripo fact gets a dated check; the skill names the version it was checked on.
2. Phone budgets: the paper says scene budgets are UNKNOWN. The skill gives per-mesh platform limits as facts and project budgets as owner decisions with a measurement method.
3. Blender version: the owner's installer is Blender 5.1.2; API calls are checked against the Blender MCP docs for that version.
4. J005 overlap: J005 is writing the Blender and Tripo fact-check tables now. J007 reads them first and checks only new claims.
5. Test B uses the character-rigger (built in J005) for the S2 rig sheet and the S4 check.

## Hidden test set (evals)
Held out of the skills: the paper's AI-model failure cases (lines 913-926, "Common AI made model failures"); the extractors skip them. The eval gives the agent a symptom and asks for the diagnosis and the fix order. A separate grader scores it.

## First real tests (G2), proposed
- **Test A (medium, hand-built):** one simple model with attach points, for example a sword or a pickaxe. Reference image → Blender by hand → audit → renders → Studio import → VFX attach-point note and UI icon renders.
- **Test B (high, Tripo):** one hero pet or creature. Reference image → Tripo → raw-candidate check → rig-sheet cuts (S3) → finish in Blender → audit → renders → Studio import → hand-back to the rigger.
- Both are shown next to their reference images and next to the best first-game model.
