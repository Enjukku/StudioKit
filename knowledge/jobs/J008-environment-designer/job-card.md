---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent environment-designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J008 — Build the environment-designer agent

| Field | Value |
| --- | --- |
| Job id | J008-environment-designer (J006 is kept for the animator, roster) |
| Size | L (new role that replaces content-builder, 2 skill books, a 1,469-line paper to extract and fact-check, first-game stage history, a scene audit tool, a real test stage in Blender + Studio) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J008-D4..D6). Steps 2-5 done 2026-10-21 (5 notes + 3 fact-checks + look-dev research in `knowledge/reference/environment/`; skills environment-design, environment-craft; templates/environment/; role environment-designer; tools/env/ scene audit with 19 tests; evals). Step 6: Studio/Blender G2 test moved to the owner's later full-workflow project (J008-D8); hidden test run once (T10) and graded (T11), gaps fixed. Waiting for G3 |
| Depends on | `level-design` (J003, exists), `reference-images` (exists), `sound-design` and `vfx-design` (exist, pointer lines only), J007 modeler (G1 pending) for the asset-request brief |

## Owner's words (2026-10-21, excerpts)
- "It builds stages, levels and worlds: the space, terrain, set dressing, lighting, atmosphere and ambience, so every place looks great, sounds right, reads clearly and plays well on phones."
- "It builds in Blender (through Python and the Blender MCP), in Roblox Studio (through the Studio MCP), or both ... It decides what is built where."
- "For each stage it writes an ambience map (zones, what you hear, what moves, point sources, how zones blend). The sound designer makes the sounds and the VFX designer makes the effects from that map."
- "It follows the game designer's layout (routes, pacing, what the player does) and the art director's art bible. Key places start from reference images made with the kit's reference-images skill (concept and environment families)."
- "It places assets the modeler makes, and asks the modeler for new ones in the brief format."
- "It reviews its own work before anyone sees it: screenshots from many cameras (player eye level, high views, top-down), scale against a player, focal points, lighting, ambience, floating or hidden parts, and performance budgets."
- "This agent replaces content-builder in the roster."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially numbers, Roblox lighting, atmosphere and audio settings, and performance budgets, and drop what you cannot back up."
- "Keep the lessons that hold for any game ... blueprints and approval before building, real scale with terrain everywhere, windows on every face, renders reviewed before Studio, and the agent's own multi-angle review. Remove anything specific to that game, such as the brick style."
- "Model: Opus. Effort: high for new stages and big environments, medium for small changes and fixes."

## Goal
One `environment-designer` agent that turns the game designer's layout and the art bible into a finished place: it reads clearly from the player camera, it sounds and moves like a real place (written down as an ambience map the sound and VFX designers build from), and it stays inside measured phone budgets. It decides what is built in Blender and what in Studio and records why, places the modeler's assets, and shows the owner only reviewed work.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Environment_Designer_Research_2026.txt` (outside git) | 15 rules; 10 cases from shipped games; guiding the player; scale; lighting; atmosphere and lighting recipes; ambience zones and soundscapes; ambient life; set dressing; terrain and nature; cohesion with the art director; workflow and kits; Blender ↔ Studio hybrid; performance and measured budgets (7-step method); review; 15-step process; AI-built defects; "do not do"; open questions; dated source register (C, B, P, A, E ids) | 1,469 lines, 137 KB | high: VERIFIED / EXPERIENCE / OPINION tags, dated sources, quoted. The paper states no stage was built, heard, play-tested or benchmarked. Roblox facts dated 2026-10 are near or after the model cutoff → live check |
| DestructionSimulator `.claude/agents/content-builder.md`, `.agents/skills/brick-builder/`, `.agents/skills/art-fundamentals/`, `knowledge/design/stages/*` (15 files), `knowledge/logs/*stage*` (21 logs), stage rows in `knowledge/design/decisions.md` and `tried-and-failed.md`, `rules/owner-profile.md` taste table (read-only) | First-game builder role, stage briefs, build logs, owner rejections and approvals | ~3,000 lines | medium-high: owner practice and owner words; brick style, brick budgets, destruction rules and game names are game-specific → drop |

## Scope
| In | Out |
| --- | --- |
| Reference notes in `knowledge/reference/environment/` + fact-check tables (Roblox lighting / atmosphere / terrain / post effects; Roblox audio and ambience; performance, streaming, scale and import). Reuse J005 / J007 tables where a claim is already checked | Routes, interactions, pacing, encounter design (game designer, `level-design`) |
| Skills `environment-design` and `environment-craft` (brief.md) | Making sounds or effects (sound designer, VFX designer) |
| Shared templates `templates/environment/`: stage blueprint, ambience map, review packet | Making reusable models and kit pieces (modeler, J007) |
| Scene audit tool `tools/env/` (Studio probe through MCP + ambience-map check; pure parts tested offline): floating and buried parts, parts outside the playable area, lights and shadow casters per zone, sound sources against the ambience map, part / mesh / triangle counts per zone | Game code, runtime scripts beyond what a place needs to hold its ambience zones (that belongs to a builder, digest item 4) |
| Role file `environment-designer`; roster row replaces content-builder; pointer renames in `level-design`, `preproduction` refs, `game-designer` role | Building the art-director, modeler or studio-operator agents |
| Pointer line in `sound-design` and `vfx-design` to the ambience map template | Rewriting those skills |
| Hand-off briefs to game designer, art director (planned), modeler, sound designer, VFX designer, studio operator (planned), `rules/messages.md` format | |
| Eval briefs + hidden cases; one real test stage slice + one small fix (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extractors ×4 (paper §1-5, §6-10, §11-15 + defects + don'ts; first-game sources) | Sonnet | high (J004-D2, J005-D4 precedent; digest item 6) | dense notes per part |
| fact-checkers ×3 (lighting, atmosphere, terrain, post; audio and ambience; performance, streaming, scale, import) | Sonnet | high | fact-check tables: claim, source, checked against, verdict |
| tool builder (scene audit + ambience-map check + offline tests) | Opus | medium | `tools/env/` + `tools/tests/` |
| lead (merge, skills, templates, role, hand-offs, evals, review) | Opus | high | 2 skills, 3 templates, role, hand-offs, evals, roster |
| environment-designer test A: new stage slice | Opus | high (owner: new stages) | blueprint, ambience map, reference images, Blender + Studio build, review packet |
| environment-designer test B: a fix on test A | Opus | medium (owner: small changes and fixes) | fix, before/after captures |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time (company limit). Wave 1: 3 paper extractors. Wave 2: first-game extractor + 2 fact-checkers. Wave 3: third fact-checker + tool builder. The lead writes the skills and templates (it needs the paper, the first-game history and the existing level, sound and VFX skills together). The new agent runs the tests as a subagent with Blender MCP and Studio MCP in a separate test place.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | 1 |
| Agents | 4 extract + 3 fact-check + 1 tool + 2 tests + 1 grader = 11 | 4 extract + 3 fact-check + 1 look-dev research (J008-D7) + 1 tool (+1 follow-up) + 1 hidden test + 1 grader = 11 runs; Studio test not run (J008-D8) |
| Models / effort | Sonnet high ×8; Opus medium ×2; Opus high ×1 + lead | Sonnet high ×9; Opus medium ×1; Opus high ×1 (environment-designer) + lead |
| Image generations | 3-6 ChatGPT images (concept + environment families for the test slice, retries) | 0 (test moved, J008-D8) |

## Acceptance checks
- [ ] Every number and every Roblox lighting, atmosphere, terrain, audio and performance claim in a skill has a source and a fact-check verdict (confirmed / corrected / unverified-kept-as-OPINION / dropped); dropped claims listed with the reason.
- [ ] No invented budgets: stage budgets (parts, triangles, lights, sound sources, particles) stay PROPOSAL or UNKNOWN until the owner sets them or a phone measurement exists; platform limits are stated as limits, not targets.
- [ ] Nothing specific to DestructionSimulator in kit files (grep for brick terms, game names, D-ids = 0 hits outside source tables).
- [ ] First-game lessons kept as universal rules: blueprint approved before building; real scale against a player; terrain everywhere (no flat plane); finished on every face players can see (windows on every face); renders reviewed before Studio; own multi-angle review.
- [ ] Ambience map template: zones, what you hear, what moves, point sources, how zones blend, states; the sound and VFX designers can each build from it without asking (checked by their evals reading it).
- [ ] Built-where rule: Blender vs Studio vs split, with reasons, recorded per stage.
- [ ] Self-review set: eye-level along the route, high views, top-down, scale shots next to a player, focal-point shots; floating / hidden parts = 0 by audit; budgets checked; each check labelled gate-verified / MCP-verified / owner-confirmed / not verified.
- [ ] Scene audit tool: offline tests pass; it runs in Studio through MCP on the test stage.
- [ ] Hand-off briefs follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.
- [ ] G2: test stage shown with its reference image, blueprint, ambience map and review captures next to the best first-game stage.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "Just make sure you run the agents. All right, yeah, looks good." |
| G2 first real test (stage slice + fix) | 2026-10-21 | not run here: "we're going to do a test by making doing a project that goes through the entire workflow" (J008-D8) |
| G3 final approval | | |
