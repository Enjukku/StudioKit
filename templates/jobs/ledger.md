<!-- > Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20 -->
# Ledger: <job-id>

Every request between agents is a ticket here (`rules/company.md` section 3).

| Field | Meaning |
| --- | --- |
| id | `<job-id>-T<nn>` |
| from, to | asking agent, doing agent |
| ask | pointer to brief section, or 1-3 line intent brief |
| inside | yes = same scope, crew, budget; no = needs decision |
| status | proposed, approved, working, blocked, needs-decision, done, failed, cancelled |
| hops | agents the request chain has passed (max 3) |
| result | pointer to output files |
| updated | date |

| id | from | to | ask | inside | status | hops | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
