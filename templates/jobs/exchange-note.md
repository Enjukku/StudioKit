<!-- > Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016). One file per craft per round in the job's exchange/ folder: exchange/r<round>-<role>.md. Format: rules/messages.md §4. -->
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
