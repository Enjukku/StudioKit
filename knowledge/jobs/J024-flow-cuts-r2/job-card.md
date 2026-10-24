---
type: job
scope: universal
status: active
updated: 2026-10-24
source: owner chat 2026-10-24 (J023-D6, J023-D7)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# Job card: J024-flow-cuts-r2 — the second, heavy cut of the job flow

## The owner's words (verbatim, first)
Copied from `knowledge/jobs/J023-flow-speed/decisions.md` rows J023-D6 and J023-D7:
- J023-D6: "I think we completely get rid of making these like roughs or these like sketches, and we just build the real thing every single time." · "I feel like we can more efficiently get through the directions what the crafts need without spending so many rounds and transferring so much data from model to model." · "I don't think we necessarily need all 7 of these reviewers for every single task."
- J023-D7: "We don't need to keep the cutscene animatic. We just try to create drop it along with all the other roughs. We just try to create the final product the first time around."
- Goal, from the owner (relayed by the J023 lead): "keep our same results but just cut down by like 75%".

| Field | Value |
| --- | --- |
| Job id | J024-flow-cuts-r2 |
| Title | Second cut of the job flow: no roughs, direction and needs in one step, fewer reviewers |
| Size | L (kit job: all 7 job workflows, rules, recipes, skill, templates, tests) |
| Type (recipe) | other: kit job (no recipe fits; same shape as J023) |
| Job lead (agent) | orchestrator (this chat), started from the J023 lead chat |
| Direction leads | none (the owner set the direction in J023-D6, D7; the brief from the J023 lead names the three cuts) |
| Integrator | orchestrator |
| Studio place (`studio_id`) | none (files, fake-agent harness) |
| Code file owners | see `design.md` §10 (one builder per script group, one writer, one test updater) |
| Linked jobs | J023-flow-speed (the uncommitted baseline this job builds on; committed separately) |
| Risks (review slots) | none |
| Status | built; gate pending owner review (see Status) |

## Four lines (goal)
| Line | Value |
| --- | --- |
| Problem | After J023 a job still takes many agent runs: minimum L/M runs cutscene 48/36, character 43/35, stage 41/33, effect 29/20 (original: 56, 46, 48, 35). Most come from rough passes, proof stages, check-ins between a rough and a final, separate needs rounds and 5-7 reviewers |
| Constraints | Same results (J023-D3); every quality check with measured evidence stays (`J023-flow-speed/research/lead-and-evidence.md`); no owner gate removed except G2; the crafts agree together before production (J023-D2); never renumber sections; LF; other chats' files untouched; commit nothing until the owner says so |
| Target experience | mastery: game work moves fast, and the owner does not see a drop in quality |
| Success test | Minimum agent runs per job type about 75 % below the original flow (targets for L: cutscene 16-20, effect about 10, character about 20, UI about 12), measured with `tools/workflows/wf_harness.mjs`; new tests fail on the J023 scripts; gate `RESULT: PASS`; later: no rise in repair rounds or owner-found defects on real jobs |
| Goal word | fast |
| Belief check | none (kit job; the claim is about our own run counts, measured by the harness) |

## Scope
| In | Out |
| --- | --- |
| The 7 scripts `.agents/workflows/jobs/*.js`; recipes and skill (`orchestration`); `rules/company.md`, `rules/messages.md`, `rules/assistants/claude.md`; templates; role "place in the job flow" lines that name a removed step; tests | H (shorter books, J023-D5); other chats' files (`tools/audio/**`, `tools/tests/test_soundbench_*`, `tools/art/art_refs.py`, `tools/tests/test_art_refs.py`, `.agents/skills/reference-images/**`, `.agents/skills/ui-figma/**`, `knowledge/inbox/2026-10-23-orchestrator-chatgpt-work-mode-effort.md`, `knowledge/reference/studio/juku-studios-*`); commits |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| builder A (general-purpose stand-in) | opus | default | `job-cutscene.js`, `job-effect.js`, `tools/tests/test_j024_cutscene_effect.py` |
| builder B (general-purpose stand-in) | opus | default | `job-character.js`, `job-stage.js`, `tools/tests/test_j024_character_stage.py` |
| builder C (general-purpose stand-in) | opus | default | `job-feature.js`, `job-ui-screen.js`, `job-marketing-art.js`, `tools/tests/test_j024_feature_ui_marketing.py` |
| writer (general-purpose stand-in) | opus | default | recipes, rules, skill, templates, workflows README, role lines |
| test updater (general-purpose stand-in) | opus | default | older tests that assert a removed step |

## Stop criteria
- Floor: the success test above.
- Bar: every removed step is named with the check that replaces it or the risk it leaves; recipes, `rules/company.md`, README and scripts say the same thing; each new test fails on the J023 scripts; old tests keep their strength on the new flow.

## Budget
5 Opus builder/writer runs + 1 test updater run; no images. Usage estimate: about 1.5-3 M tokens (J023 used 3 builders + 1 writer + 1 updater; per-run size not recorded there).

## Status
Opened and built 2026-10-24 per `design.md` (LD1-LD7). Not committed (owner's word needed; J023 and J024 go in separate commits, other chats' files left out).

Minimum agent runs (direction + proof + build, clean fakes, `risks: []`; `tools/workflows/wf_harness.mjs` through the lead's `measure_runs.py`):

| Type | Original L / M | J023 L / M | J024 L / M | Cut vs original (L) |
| --- | --- | --- | --- | --- |
| Cutscene | 56 / 56 | 48 / 36 | 17 / 17 | -70 % |
| Character (playable) | 46 (49) / 46 (49) | 43 (46) / 35 (38) | 16 (20) / 16 (20) | -65 % (-59 %) |
| Stage | 48 / 48 | 41 / 33 | 12 / 12 | -75 % |
| UI screen (shop) | 35 (41) / 31 (37) | 26 (30) / 21 (25) | 11 (13) / 11 (13) | -69 % (-68 %) |
| Feature (money + numbers) | 37 (43) / 37 (43) | 32 (36) / 24 (28) | 9 (11) / 9 (11) | -76 % (-74 %) |
| Effect (animated) | 35 (40) / 35 (40) | 29 (34) / 20 (26) | 10 (12) / 10 (12) | -71 % (-70 %) |
| Marketing art | 22 / 22 | 17 / 13 | 4 / 4 | -82 % |
| All seven, L min | 279 | 236 | 79 | -72 % |

Built by builders A-C (scripts + `tools/tests/test_j024_*.py`: 30 + 19 + 18 tests, each shown failing on the J023 snapshot), the writer (rules, recipes, skill, templates, README, 21 role lines, 3 craft hand-off files), the test updater (11 older test files retargeted, notes in the shared notes folder `j024-test-updater.md`). Lead fixes after the updater flagged them: the cutscene D1 brief lost the options method (restored); the `event` live-ops review ran beside the integrated review in feature, UI and marketing (now after it). Lead edits outside the writer's files: `film-craft` and `film-direction` (strips, boards and the animatic are passes only on the owner's ask), `templates/role.md` step 3, `templates/rig/rig-sheet.md` G3 row.

Open (other books, not changed; H waits): `templates/film/*` and `art-review` describe boards and the animatic as passes; `animation-design` §3 step 6 timing takes at G2; `preproduction/references/handoffs.md` lines 101, 139 ("first sample (G2)"); `live-ops-craft` hand-offs mention the grey-box verdict. No independent review of the J024 build yet.
