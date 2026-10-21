<!-- > Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016: tickets for new work only; stage instead of hops; stale status) -->
# Ledger: <job-id>

Every request for **new work** between agents is a ticket here (`rules/company.md` §5). Clarifying questions and interface negotiation need no ticket: they go in `exchange/` or a direct message, and their outcome goes in the contract or `decisions.md`.

| Field | Meaning |
| --- | --- |
| id | `<job-id>-T<nn>` |
| from, to | asking agent, doing agent |
| ask | pointer to a brief file in the `rules/messages.md` §2 format |
| inside | yes = same scope, crew, budget; no = needs decision |
| stage | direction, proof, build or repair |
| status | proposed, approved, working, blocked, needs-decision, done, failed, stale, cancelled |
| result | pointer to output files with revisions |
| updated | date |

| id | from | to | ask | inside | stage | status | result | updated |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
