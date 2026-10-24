# Jobs

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: direction sheet, contract, crew, exchange, reviews, evidence; active list); revised by feature-builder · claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit D R5, R16; lead decisions LD8, LD12); revised by J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6: decisions.md layout with the Closed doors table, gate packets)

M and L jobs get a folder `knowledge/jobs/<job-id>/`, copied from `templates/jobs/`. Open jobs are listed in `active.md` (the lead keeps it current; the hooks in `tools/hooks/` read it; `context_packet.py --job` takes the folder name, not this list). How a job runs: `rules/company.md` §4 and the `orchestration` skill.

| File | From template | Writer | Holds |
| --- | --- | --- | --- |
| job-card.md | job-card.md | lead | the owner's words verbatim, the four lines and goal word, size, recipe, crew, stop criteria and budget per stage (tokens), gates with approved revisions and doors closed, close-out |
| direction/proposal-<role>.md | (the recipe's D1 brief) | each direction lead | its independent first proposal. Never in the context packet or the area indexes (`rules/knowledge.md` §3): the job lead reads them through its synthesis brief |
| direction.md | direction-sheet.md | job lead | target experience, G1 options and goal question, dropped options (CD ids in `decisions.md`), non-negotiables, known limits, stop criteria and budget, decision records, conflicts with owner, resolution and confirmations (J023) |
| contract (beat-sheet.md, rig sheet, contract-<name>.md) | beat-sheet.md, `templates/rig/`, contract-header.md | the decision owner | the shared plan crafts build against, with a revision and a change table. Its **Consumers** table is the job's dependency map for that contract (no separate file) |
| decisions.md | (layout below) | lead | gate answers and other owner decisions with the owner's words and the revision approved; the job's one Closed doors table |
| gate-<G1\|G2\|G3>.md | gate-packet.md | lead | the packet the owner answers at that gate |
| crew.md | crew.md | lead | role → agent id for direct messages |
| exchange/ | exchange-note.md | each craft | one note per craft per round: agree / conflict / missing evidence |
| reviews/ | review.md | each reviewer | findings per artifact revision |
| evidence.md | evidence.md | integrator, reviewers; lead at readiness | checks with evidence, protected list, defects with causes, metrics at close |
| ledger.md | ledger.md | lead | tickets for new work |
| digest.md | decision-digest.md | lead | open owner questions |
| `<role>/` | | that role | each craft's output files |

Held-out evaluation keys (any file or folder with `hidden` in its name) are never opened, listed or quoted by agents or tools (`rules/knowledge.md` §3). A visibly named note that repeats held-out cases, keys, rubrics or answers (a grade file, eval answers, a grader brief) carries `held_out: true` in its frontmatter: the packet and the area indexes withhold it the same way.

Job id: `J<nn>` plus a short slug. Re-list this folder right before creating a job: parallel chats take numbers.


## decisions.md layout
No template file: the lead starts `decisions.md` with these two tables. Owner decisions: `orchestration` SKILL §8; closed doors: `orchestration/references/gates-and-feedback.md` §4 (when to write a row, `avoid`, re-proposal). The Closed doors table is the job's only closed-doors record: direction sheets, pre-production documents and gate packets point to its CD ids.

| ID | Date | Gate or step | Decision | Owner's words (verbatim) | Revision approved |
| --- | --- | --- | --- | --- | --- |

### Closed doors
| ID | Date | Gate | Closed option or direction | Owner's words | Reason (goal, cost, tone, policy) | May return only if |
| --- | --- | --- | --- | --- | --- | --- |
