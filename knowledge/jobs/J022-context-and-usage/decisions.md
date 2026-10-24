---
type: decision
scope: universal
status: active
updated: 2026-10-24
source: owner chat 2026-10-24
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# J022 decisions (owner's words)

| ID | Date | Decision | Owner's words | Approves |
| --- | --- | --- | --- | --- |
| J022-D1 | 2026-10-24 | Kit job for the context and usage fixes: session per stage, image hygiene, batched tool calls, helper models, a usage report in `/improve`; settings proposed, applied by the owner | "Open a kit job for the context and usage fixes: session-per-stage rule, image hygiene, batched tool calls, model defaults for helper agents, and a usage-report tool for /improve. Propose the settings changes for me to apply." | job-card.md scope 1-6 |

## Lead decisions
| ID | Decision | Reason |
| --- | --- | --- |
| J022-LD1 | Thresholds 200 k median, 400 k peak, 20 images, 400 calls are PROPOSAL defaults of the report, not limits | No owner number; they match the Session size row and S1 |
| J022-LD2 | The rules go in `rules/assistants/claude.md` (harness specifics) plus one sentence in `rules/company.md` §7 and one in `orchestration` §1 step 5; no new section | Instruction size stays under 200 lines; no renumbering |
| J022-LD3 | `usage_report.py` reuses `improve_scan.py` readers and counts one call per message id | One reader for transcripts; the first hand tally double-counted streamed records |
