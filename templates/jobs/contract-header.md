---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
revision: 1
---
> Author: <decision owner role> · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (consumers table = the dependency map; code file owners). Put this header on any shared contract that has no template of its own (route graph, state map, feature contract, event timeline); name the file contract-<name>.md so the context packet lists it. The beat sheet (templates/jobs/beat-sheet.md) carries its own revision, consumers and change table; the rig sheet (templates/rig/rig-sheet.md) carries a revision and a change log (§H). Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design): code file owners come from the direction stage. -->

# Contract: <job-id> <name>

| Field | Value |
| --- | --- |
| Owner (one writer) | <role>; the one exception is the Code file owners section below, written from the architect's limits table at the direction merge (`rules/company.md` §4 step 2) |
| Ids | <the stable ids it defines; new ones also go to knowledge/design/vocabulary.md at close> |

## Consumers (the job's dependency map for this contract)
One row per role that builds on it. A change to an id in a row makes that row's outputs stale (`rules/messages.md` §5); a selective recheck reads this table.

| Consumer (role) | Ids it builds on | Its outputs built on this contract (path) |
| --- | --- | --- |
| | | |

## Code file owners (code contracts only)
Set by the architect in its direction limits table and merged at the direction merge (file owners are the architect's decision, `rules/company.md` §3): the architect writes this section and adds a change-table row. A builder writes only the files in its row; a needed change elsewhere goes back as the lines it needs.

| Builder (role) | Owns (files or folders) |
| --- | --- |
| | |

<the contract body>

## Change table
| Revision | Date | What changed | Consumers to recheck | Acknowledged by |
| --- | --- | --- | --- | --- |
