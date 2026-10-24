---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: orchestrator · <model id> · <effort> · <date>
<!-- Template: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: recipe, direction leads, usage in tokens, gates bound to revisions, close-out metrics); revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (frontmatter, Studio id, code file owners pointer); revised by orchestrator · claude-opus-5-5 · high · 2026-10-22, J019 (Risks row for the recipes' risk-gated slots); revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6): four lines and goal word, stop criteria and budget per stage, doors closed per gate; revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021: target-experience sentence, belief check, floor and bar); revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design: no proof stage and no G2, `performance` risk token) -->

# Job card: <job-id> <title>

## The owner's words (verbatim, first)
> <paste the owner's request word for word>

| Field | Value |
| --- | --- |
| Job id | |
| Title | |
| Size | S / M / L |
| Type (recipe) | cutscene / character / stage / ui-screen / feature / effect / marketing-art / other: <why> |
| Job lead (agent) | |
| Needs and limits writers | <the recipe's needs and limits rows for this job, conditional crafts marked> |
| Integrator | |
| Studio place (`studio_id`) | <the test place the Studio driver uses; none = Blender or files only> |
| Code file owners | the `owns` column of the contract header (`contract-<name>.md`), set by the architect in its direction limits table and merged into the plan (`rules/company.md` §4 step 2) |
| Linked jobs | <job-id: which shared interface it owns (saved fields, ids, who grants, who checks)>; none = a single job |
| Risks (review slots) | the risks this job carries, which switch on the recipe's *(risk: …)* rows (`orchestration/references/job-types.md`): tokens (the saved workflow's `risks` arg: `.agents/workflows/jobs/README.md`): `money`, `saves`, `remotes`, `trades`, `paid-random` (paid random items), `server-result` (the server confirms the result), `rewards`, `frequent-effect`, `danger-area`, `sold-variant`, `new-enemy` (with gameplay behaviour), `performance` (the performance-engineer gives limits and reviews), `shop-screen` (shop, odds or progress screen), `event` (from a live-ops update brief); none = "none" |
| Status | proposed |

## Four lines (goal)
What each line holds: `orchestration` SKILL §1 step 1; written before the first brief (SKILL §3 step 3).
| Line | Value |
| --- | --- |
| Problem | |
| Constraints | |
| Target experience | <one or two named kinds of fun>: <what the work must make the player feel, do or believe, one sentence, no number (the number goes in the success test)> |
| Success test | |
| Goal word | <the word every goal question carries (`orchestration/references/gates-and-feedback.md` §1)> |
| Belief check | <the player belief the problem rests on, word for word> → <analyst result path and verdict, or "not run: no player data (reason)", or "none"> (`orchestration` SKILL §1 step 1) |

## References
<owner-approved links and files>

## Scope
| In | Out |
| --- | --- |
| | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| | | | |

Agent ids: `crew.md`.

## Mechanism
<saved workflow `job-<type>` stage by stage / subagents by hand / production chat, and why>

## Stop criteria and budget per stage
What they hold: `orchestration` SKILL §3 step 3 (token estimate source) and `orchestration/references/gates-and-feedback.md` §7. Write stop criteria as `floor: <the success test> · bar: <observable signs a top professional needs>` (`rules/messages.md` §2).
| Stage | Stop criteria | Passes | Image cap | Tokens estimate | Tokens actual |
| --- | --- | --- | --- | --- | --- |
| direction | | | | | |
| build | | | | | |

## Acceptance checks
- [ ] <measurable pass rule>

## Gates
| Gate | Date | Revision approved | Owner's words | Doors closed (CD ids in `decisions.md`) |
| --- | --- | --- | --- | --- |
| G1 direction | | | | |
| G3 final | | | | |

## Close-out
Metrics in `evidence.md` §4. Filed into the vault (`orchestration` skill §9): [ ] decisions [ ] precedents [ ] vocabulary [ ] systems [ ] tried-and-failed [ ] taste log [ ] catalogs [ ] lesson drafts [ ] removed from `knowledge/jobs/active.md`
