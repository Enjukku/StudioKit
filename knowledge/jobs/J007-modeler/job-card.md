---
type: job
scope: universal
status: draft
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent modeler)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J007 — Build the modeler agent

| Field | Value |
| --- | --- |
| Job id | J007-modeler (J006 is kept for the animator, roster) |
| Size | L (new role, 2 skill books, a 1,974-line paper to extract and fact-check, first-game sources, a model audit script, two real test models in Blender + Studio) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | proposed: G1 waits for the owner (digest.md) |
| Depends on | J005 `rig-pipeline` (exists), J005 rigger skills and role (step 2 running) for the G2 rig loop |

## Owner's words (2026-10-21, excerpts)
- "It builds characters, creatures, pets, weapons, tools, props, vehicles, buildings and environment pieces for Roblox games."
- "Every model starts from a reference image made with ChatGPT, using the kit's reference-images skill ... It checks the reference before modeling. When a subject already has an approved image, it attaches it so the design does not drift."
- "Most models are built by hand in Blender (through Python and the Blender MCP). Models that must look especially good are generated with Tripo from the reference image, then cleaned up and finished in Blender."
- "The animator says what must move, the rigger says which parts must be separate and where the cuts go, and the modeler does the cutting, seam clean-up and re-modelling, because it knows geometry best. It may push back with a better way to build a part."
- "Every model stays cheap on low-end phones: triangle and texture budgets, reuse of meshes, simple collisions, correct export and import into Roblox."
- "It reviews its own work before anyone sees it: renders from several angles compared with the reference image, scale against a player, no floating or hidden parts, budgets met."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially numbers, Blender facts, Tripo facts and Roblox limits, and drop what you cannot back up."
- "Keep what still holds for any game, and remove anything specific to those games (for example the brick style)."
- "Model: Opus. Effort: high for hero models and new kinds of models, medium for simple models (owner decision 2026-10-20)."

## Goal
One `modeler` agent that turns an approved reference image into a Roblox-ready model: it reads as the design, it moves the way the rig sheet needs, and it stays cheap on low-end phones. It chooses between hand modeling in Blender and Tripo + Blender finishing, records why, and hands each downstream role exactly what it needs.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Modeler_Research_Paper.txt` (outside git) | 15 rules; great stylized models (10 cases); ChatGPT references; blockout; hand modeling in Blender; Tripo generation + finishing (13 steps, H/P series, multiview inputs); building for rigger and animator; textures and materials; Roblox budgets (10 numbered limits); environment and buildings; export and import; hand-offs; review (pass/fail table); 22-step process; AI-model failures; "do not do" list; open questions; dated source register (P, C, I, B, T, R ids) | 1,974 lines, 176 KB | high: VERIFIED / EXPERIENCE / OPINION tags and dated sources. The paper states no modeling, Tripo run, import or device test was done. Tripo and Roblox facts dated 2026-10 are after the model cutoff → live check |
| DestructionSimulator `.claude/agents/content-builder.md`, `.agents/skills/brick-builder/`, `.agents/skills/art-fundamentals/`, `content/art/refs/model`, `content/art/anchors/model` (read-only) | First-game builder role, art fundamentals, model reference practice | ~220 lines + art folders | medium-high: owner practice; brick style is game-specific → drop |
| GreatWallSim `knowledge/design/{model-list, hero-assets-import, dam-section-kit, characters, secret-hero, asset-hookup-audit}.md`, `knowledge/logs/2026-10-1{7,8}-*`, `knowledge/logs/2026-10-20-dam-kit-swap.md`, `knowledge/systems/{dam-section-kit, environment-import}.md`, `art/style-locks.md` (read-only) | Second-game model list, hero import, modular kit, character plans, import and hook-up audit | ~1,500 lines | medium-high: owner decisions and logs; game names and themes → drop |
| J005 files (kit): `rig-pipeline` skill, `templates/rig/`, `knowledge/jobs/J005-character-rigger/modeler-handoff.md`, `knowledge/reference/rigging/*` incl. fact-check tables | The rig sheet, the S3 hand-off and the checks the modeler must adopt | — | owner-approved (J005-D1) |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/modeling/` + fact-check tables (Roblox, Blender, Tripo); reuse J005's tables where a claim is already checked | Rig, bones, weights, animation (rigger, animator) |
| Skills `modeling-design` and `modeling-craft` (brief.md) | Placing models in levels and maps (content-builder, planned) |
| Model audit script `tools/model/` (Blender side through MCP, pure parts tested offline): evaluated triangles, loose parts, non-manifold edges, size against a player, UV sets, materials per mesh, texture sizes | Game code, runtime scripts |
| Role file `modeler`; adopts `modeler-handoff.md` and the rig sheet §D keys as-is | Changing `rig-pipeline` beyond naming the new skills in the S3 brief |
| Hand-off briefs to rigger, animator, art director (planned), VFX (attach points), UI (icon renders), `rules/messages.md` format | Building the art-director agent |
| Eval briefs + hidden cases; 2 real test models (G2) | A Tripo API tool, unless the owner says yes (digest item 3) |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×4 (paper §1-4, §5-8, §9-13 + don'ts; first-game sources) | Sonnet | high (J004-D2, J005-D4 precedent; digest item 5) | dense notes per part |
| fact-checkers ×3 (Roblox limits; Blender via MCP docs + web; Tripo via web) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (model audit script + offline tests) | Opus | medium | `tools/model/` + `tools/tests/` |
| lead (merge, skills, role, hand-offs, evals, review) | Opus | high | 2 skills, role, hand-offs, evals, roster |
| modeler test A: hand-built simple model | Opus | medium (owner: simple model) | model, audit, renders, Studio import |
| modeler test B: Tripo hero model through the rig loop | Opus | high (owner: hero model) | model, cut parts, audit, renders, Studio import |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time (company limit). Wave 1: 3 paper extractors. Wave 2: first-game extractor + Roblox and Blender fact-checkers. Wave 3: Tripo fact-checker + tool builder. The lead writes the skills (it needs the paper, the first-game history and the rig pipeline together). The new modeler runs the tests as a subagent with Blender MCP and Studio MCP; test B uses the real rigger S2 sheet if J005 has built the rigger by then.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | |
| Agents | 4 extract + 3 fact-check + 1 tool + 2 tests + 1 grader = 11 | |
| Models / effort | Sonnet high ×8; Opus medium ×2; Opus high ×1 + lead | |
| Image generations | test references: about 4-8 ChatGPT images (2 subjects, front/side/back views, retries) | |
| Tripo | 1-3 generations for test B (owner's account or API, digest item 3) | |

## Acceptance checks
- [ ] Every number, Blender fact, Tripo fact and Roblox limit in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-OPINION / dropped); dropped claims listed with the reason.
- [ ] No invented budgets: project triangle, texture and scene budgets stay PROPOSAL or UNKNOWN until the owner sets them or a phone measurement exists (paper rule 14).
- [ ] Nothing specific to the first games in kit files (grep for brick style terms, game names, D-ids = 0 hits outside source tables).
- [ ] The role adopts `modeler-handoff.md` C1-C5 and the rig sheet §D keys without change; counter-proposal rule (one round) stated.
- [ ] Reference step: the modeler uses `reference-images` (families model, character, creature, prop, environment; `tools/art/art_refs.py`; the art bible) and attaches the approved image for a subject that has one.
- [ ] Self-review: renders from front, back, both sides, 3/4 and top next to the reference; one render next to a player-size dummy; audit shows 0 floating parts and 0 hidden interior parts; budgets met.
- [ ] Model audit script: offline tests pass; it runs in Blender through MCP on both test models.
- [ ] Hand-off briefs to rigger, animator, art director, VFX and UI follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.
- [ ] G2: test A and test B imported in Studio (MCP-verified), shown with renders next to their reference images and the best first-game model.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | | |
| G2 first real tests (2 models) | | |
| G3 final approval | | |
