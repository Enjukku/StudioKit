# Jobs

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: direction sheet, contract, crew, exchange, reviews, evidence; active list)

M and L jobs get a folder `knowledge/jobs/<job-id>/`, copied from `templates/jobs/`. Open jobs are listed in `active.md` (the lead keeps it current; hooks and `context_packet.py --job` read it). How a job runs: `rules/company.md` §4 and the `orchestration` skill.

| File | From template | Writer | Holds |
| --- | --- | --- | --- |
| job-card.md | job-card.md | lead | the owner's words verbatim, size, recipe, crew, budget in tokens, gates with approved revisions, close-out |
| direction.md | direction-sheet.md | job lead | target experience, G1 options, non-negotiables, known limits, decision records, signatures |
| contract (beat-sheet.md, rig sheet, contract-<name>.md) | beat-sheet.md, `templates/rig/`, contract-header.md | the decision owner | the shared plan crafts build against, with a revision and a change table |
| decisions.md | (own table) | lead | gate answers and other owner decisions with the owner's words and the revision approved |
| crew.md | crew.md | lead | role → agent id for direct messages |
| exchange/ | exchange-note.md | each craft | one note per craft per round: agree / conflict / missing evidence |
| reviews/ | review.md | each reviewer | findings per artifact revision |
| evidence.md | evidence.md | integrator, reviewers; lead at readiness | checks with evidence, protected list, defects with causes, metrics at close |
| ledger.md | ledger.md | lead | tickets for new work |
| digest.md | decision-digest.md | lead | open owner questions |
| `<role>/` | | that role | each craft's output files |

Job id: `J<nn>` plus a short slug. Re-list this folder right before creating a job: parallel chats take numbers.
