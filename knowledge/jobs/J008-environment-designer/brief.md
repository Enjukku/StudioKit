---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent environment-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J008 intent brief — environment-designer agent

<intent>
The studio needs one agent that makes every place in a Roblox game: stages, levels, hubs and worlds. A place is done only when four things are true: the player can read it from the game camera (where to go, what matters, what can happen next), it feels like somewhere real to be in (light, air, sound and movement that have a cause), it keeps the game designer's routes and pacing, and it runs on low-end phones. A beautiful render alone proves none of these.

The game designer owns the layout (routes, interactions, pacing); the art director owns the art bible; the modeler makes the assets. The environment designer turns these into a place: space, terrain, set dressing, lighting, atmosphere and ambience. Key places start from reference images made with the reference-images skill. It builds in Blender, in Studio, or splits the work, and it records why for each stage.

For each stage it writes an ambience map: zones, what you hear, what moves, point sources, how zones blend. Wind high up, a waterfall that grows louder as you walk to it, frogs in a swamp, dripping water and echo in a cave. The sound designer and the VFX designer build their craft from that map; the environment designer says where and why, never how a sound or an effect is made.

First-game practice that worked stays: a blueprint the owner approves before building, real scale against a player, terrain everywhere, every face a player can see is finished, renders reviewed before Studio, and the agent's own multi-angle review before anyone sees the work. The research paper is strong evidence, not gospel. Numbers and Roblox lighting, atmosphere, audio and performance claims are checked, and claims that cannot be backed up are dropped.
</intent>

<spec>
id: J008
from: owner
to: lead
skills: [orchestration, ste-writing, level-design, reference-images, sound-design, vfx-design, performance, studio-mcp]
refs:
  - C:\Users\Firew\Downloads\Environment_Designer_Research_2026.txt   # take: 15 rules, route contract vs art pass, guidance, scale convention, light and atmosphere as composition + readability, ambience zones and source contracts, ambient life, set dressing, terrain, art-director cohesion, kits, Blender↔Studio hybrid, 7-step budget method, review packet, 15-step process, defect diagnosis, don'ts; avoid: copied tutorial settings as presets, platform caps as stage budgets, case-study layouts as rules, proposed checks described as tests
  - .agents/skills/level-design/   # take: route graph, first view, landmarks, review artifact; avoid: duplicating it (the environment skills point to it)
  - .agents/skills/sound-design/, .agents/skills/vfx-design/   # take: what each craft needs from a place; avoid: making their choices
  - .agents/skills/reference-images/ + tools/art/art_refs.py   # take: concept and environment families, art bible, anchors; avoid: changing the skill
  - knowledge/external/roblox-creator-docs/{environment,effects,audio,parts,workspace/streaming}   # take: engine truth first, web second
  - knowledge/reference/rigging/fact-check-*.md, knowledge/reference/modeling/* (J007, when it exists)   # take: claims already checked (Blender export, Roblox import); do not check them twice
  - DestructionSimulator content-builder, brick-builder, art-fundamentals, stage briefs, stage logs, stage decisions, owner taste table (read-only)   # take: universal stage lessons, owner rejections; avoid: brick style, brick budgets, destruction rules, game names
fixed:
  role_name: environment-designer                                  # owner 2026-10-21
  replaces: content-builder (roster)                               # owner 2026-10-21
  model: opus                                                      # owner 2026-10-21
  effort: high for new stages and big environments; medium for small changes and fixes   # owner 2026-10-21
  builds: space, terrain, set dressing, lighting, atmosphere, ambience   # owner 2026-10-21
  tools: Blender (Python + Blender MCP), Studio (Studio MCP), or both; the agent decides and records why   # owner 2026-10-21
  ambience_map_per_stage: zones, what you hear, what moves, point sources, how zones blend   # owner 2026-10-21
  layout_from: game designer (routes, pacing, actions)             # owner 2026-10-21
  style_from: art director's art bible                             # owner 2026-10-21
  key_places_start_from: reference images (reference-images skill, concept and environment families)   # owner 2026-10-21
  assets: placed from the modeler; new ones asked for in the brief format   # owner 2026-10-21
  kept_lessons: blueprint + approval before building; real scale, terrain everywhere; windows on every face; renders reviewed before Studio; own multi-angle review   # owner 2026-10-21
  self_review: player eye level, high views, top-down; scale against a player; focal points; lighting; ambience; floating or hidden parts; performance budgets   # owner 2026-10-21
  hand_offs: game designer, art director, modeler, sound designer, VFX designer, studio operator; rules/messages.md format   # owner 2026-10-21
  stud_scale: 1 stud = 28 cm (paper B02) — re-checked in step 2   # paper rule 4
open: [book structure inside the two skills, template fields beyond the owner's list, audit tool structure, recipe choice per place type, hand-off wording]
not_in_scope: [routes and pacing, making sounds or effects, making reusable models, game code, art-director / modeler / studio-operator agents]
rules:
  - Paraphrase sources; never copy paper text; the paper stays outside git.
  - Evidence tags kept. A number without a checked source is PROPOSAL or UNKNOWN, never a rule. Stage budgets come from the owner or a phone measurement.
  - Nothing specific to DestructionSimulator in kit files.
  - Route changes are proposals to the game designer, never hidden inside an art pass.
  - Code lives on disk (files mode); Studio MCP builds and checks place content and never edits scripts; one driver per Studio instance; tests use a separate test place, never a live game place.
  - The source copy (approved .blend, approved place) stays untouched; work on a copy.
  - API keys (OpenAI) only in environment variables, never in the repo, notes or chat.
  - Self-review from several cameras before anything reaches the owner; label each check gate-verified, MCP-verified, owner-confirmed or not verified.
  - Skills ≤ 500 lines, kit template, "Read this file when" table, project-overlay line.
deliver: knowledge/reference/environment/*, .agents/skills/environment-design/*, .agents/skills/environment-craft/* (evals/briefs.md included), templates/environment/*, .agents/roles/environment-designer.md, tools/env/*, tools/tests/test_env_*.py, knowledge/jobs/J008-environment-designer/handoffs.md
checks: see job-card.md acceptance checks
return: G1 to owner now; G2 test stage slice + fix; G3 approval
</spec>

## Proposed skill books and templates
| File | Kind | Holds | Read by |
| --- | --- | --- | --- |
| `environment-design` | design | What makes a place read and feel real; route contract vs art pass; first view, landmarks, leading shapes and light (pointing to `level-design`, not repeating it); scale and the player envelope; light and atmosphere as composition and as readability; ambience: zones, causes, point sources, blends, states; ambient life; set dressing hierarchy and quiet space; terrain and nature; cohesion with the art bible; budgets as measured project decisions; review rules and defect diagnosis | environment-designer, game designer, art director, sound designer, VFX designer, lead |
| `environment-craft` | craft | Built-where choice (Blender / Studio / split) with reasons; scale calibration and one round trip before bulk work; blockout; terrain in Studio; Blender kit assembly and import checks (pivots, dimensions, collision, instancing); Lighting, Atmosphere, Sky, post effects and local lights with checked defaults; placing the ambience map in the place (zone volumes, emitter points; the sound and VFX designers fill them); streaming; scene audit tool; review camera set and review packet; hand-off packets | environment-designer |
| `templates/environment/stage-blueprint.md` | template | Plan, elevations, player silhouette, route overlay, landmarks, built-where table | environment-designer → owner (approval before building) |
| `templates/environment/ambience-map.md` | template | Zones, what you hear, what moves, point sources, blends, states, priorities | environment-designer → sound designer, VFX designer |
| `templates/environment/review-packet.md` | template | Camera list, captures, audit numbers, budget table, labels, open issues | environment-designer → owner, studio operator |

## Built-where split with the modeler (proposal, digest item 3)
| Built by | What |
| --- | --- |
| environment-designer | Blockout, terrain, landforms, cliffs and cave shells that are one-off for this place, assembly of kit pieces into buildings and streets, lighting, atmosphere, ambience zones and points, placement |
| modeler | Every reusable asset: modular kit pieces, props, hero buildings, vegetation meshes, anything rigged |

## Known risks (to resolve in step 2)
1. Roblox lighting and audio change fast (new audio API objects, acoustic simulation, lighting technology). Every such fact gets a dated check against the local docs mirror, then the web.
2. Phone budgets: the paper says stage budgets are UNKNOWN. The skills give platform limits as facts and project budgets as owner decisions with the paper's measurement method.
3. Scale: the paper's 1 stud = 28 cm convention and the J005 / J007 export-scale recipes must agree; one round-trip test proves it.
4. Ambience in a place needs zone volumes and a small runtime that blends them. The environment designer places the zones; who writes the runtime is digest item 4.
5. The art director and studio operator are planned, not built. Until they exist, their briefs go to the lead; the environment designer runs its own Studio checks with `studio-mcp`.

## Hidden test set (evals)
Held out of the skills: the paper's "common AI-built defects" section and 2-3 first-game stage rejections from the owner (taken from the stage logs and tried-and-failed rows). The eval gives the agent a symptom and asks for the cause and the fix order. A separate grader scores it.

## First real tests (G2), proposed
- **Test A (high, new stage):** a small, game-neutral 3-zone slice that uses the owner's examples: a swamp edge (frogs, insects), a waterfall that grows louder as you approach, a cave mouth (drips, echo), with a high ridge (wind). Reference images → blueprint (owner sees it) → built-where choice → Blender + Studio build in a separate test place → ambience map → audit → review packet.
- **Test B (medium, fix):** one fix on test A from a realistic note (for example "players miss the cave entrance" or "the zone change is abrupt"), with before/after captures.
- Both shown next to the reference images and the best first-game stage.
