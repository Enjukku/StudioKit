---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: orchestrator · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); revised by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3 (frontmatter; saved-workflow and tool limits). Kept by the lead. Subagents cannot list each other: this file is how they find a peer's id for SendMessage. -->

# Crew: <job-id>

| Role | Agent id | Stage | Started | Status | Owns |
| --- | --- | --- | --- | --- | --- |
| | | | | working / done / stopped | |

Rules:
- This file lists agents the lead (or a production chat's job lead) spawns by hand. Add a row when such an agent starts; give each brief the `peers` ids it needs; a message to a finished agent resumes it with its context (Claude Code 2.1.306); never use an id from another job.
- Inside a saved workflow there are no agent ids: sideways work goes through `exchange/` files in the order the stage sets, and repairs are fresh calls with the review files.
- Only roles whose `tools:` line includes SendMessage (or that have no `tools:` line) can send a message: since J016-D6 every working role can; the helpers (doc-keeper, explore, researcher) answer in `exchange/` notes or their hand-back.
