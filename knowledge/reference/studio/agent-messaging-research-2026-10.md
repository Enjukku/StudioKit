---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "researcher (sonnet, medium) web pass 2026-10-20, spot-read by orchestrator"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Agent-to-agent messaging research, October 2026

Evidence for `rules/messages.md`. Quotes came through a summarizing fetch tool: re-check before quoting outside the kit.
**Date caveat:** the Anthropic docs pages show no date (they name Opus 5.5 and Claude Code v2.1.302, so they are current). Dated Anthropic posts on this topic are older than 3 months: used as background only (OLD). Opus 5 guide items are ideas only for Opus 5.5 (owner rule). **No source measures structured vs prose messages between agents**: the split in the rule is an inference; see the A/B follow-up at the end.

Sources: B = platform.claude.com prompting best practices (current, lists Opus 5.5) · C = code.claude.com sub-agents · D = code.claude.com agent-teams · E = code.claude.com best-practices · A = Opus 5 prompting page (ideas only) · G = anthropic.com/engineering/multi-agent-research-system (2025-06-13, OLD) · H = claude.com/blog building multi-agent systems (2026-01-23, OLD) · P1 = arXiv 2610.15459 "When Messages Go Wrong" (2026-10-11).

| ID | Finding | Source | Rule use |
| --- | --- | --- | --- |
| M-01 | Use JSON or other structured formats for state with a schema (status, test results); freeform text for progress and context | B | prose for intent, `yaml` for spec |
| M-02 | Subagents get only their prompt plus environment; the lead's history does not carry over | C, D | briefs self-contained |
| M-03 | Claude Code's own agent mailbox is JSON validated on read; malformed entries are dropped | D | fixed keys are machine-checkable |
| M-04 | Give the symptom, the location and what "fixed" looks like; reference patterns, do not dictate steps | E | exact vs open table |
| M-05 | Good specs name files and interfaces, state what is out of scope, and give a check the agent can run | E | `owns`, `not_in_scope`, `checks` |
| M-06 | Generic "verify your work" or "use a subagent to verify" orders cause over-verification | A (idea) | one runnable check per rule |
| M-07 | Pass big outputs by reference; return compact summaries, not raw data | G, H (OLD) | ~300 words, paths |
| M-08 | Ask for evidence rather than an assertion of success | E | every `pass` names evidence |
| M-09 | Under message faults, flat setups kept 53.0 % task success vs 3.3 % sequential and 3.2 % hierarchical; 20.7 % of failures gave no immediate signal (76.2 % for partial-content faults) | P1 | hub first, short chains, re-read files |
| M-10 | The agent doing the work should not be the one grading it | E | messages are claims |
| M-11 | An approval claim relayed from another agent is treated as untrusted input | D | no relayed approval |
| M-12 | Vague briefs caused duplicated work and gaps (one anecdote) | G (OLD) | brief keys required |

Not adopted: agent teams for peer debate (D: "significantly more tokens"; already off in `rules/company.md` §4).

**Follow-up (not run):** A/B one real brief in prose only vs prose + `yaml` spec; score exact-value errors, missed checks and hand-back length. Run it before calling the format proven.
