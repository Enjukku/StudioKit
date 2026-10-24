---
type: job
scope: game
status: active
updated: <date>
source: <job-id>
supersedes: []
---
> Author: <role> · <model id> · <effort> · <date>
<!-- Template: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); frontmatter added by role-fixer W4 · claude-opus-5-5 · high · 2026-10-21, J016 G3. One file per craft per round in the job's exchange/ folder: exchange/r<round>-<role>.md. Format: rules/messages.md §4. Roles whose tools cannot send messages, and every agent inside a saved workflow, do all sideways work through these notes. Revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design): the direction stage's needs and limits rounds (N1, N2) use templates/jobs/needs-table.md, not this note; this note stays for contract questions outside those rounds and for contract-change acknowledgements. -->

# Exchange note: <role>, round <n>

```text
<spec>
round: <n>
contract: <path>@rev<n>
from: <role>
items:
  - {about: <beat / part / state id>, verdict: agree}
  - {about: <id>, verdict: conflict, why: "<what breaks, with evidence>", needs: "<decision owner decides | test: ...>"}
  - {about: <id>, verdict: missing evidence, why: "<what is not known>", needs: "<who provides what>"}
</spec>
```
