---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "orchestrator read of the Opus 5.5 pages 2026-10-20; researcher (sonnet, medium) pass on Claude Code docs"
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Agent-to-agent messaging research, October 2026

Evidence for `rules/messages.md`. **Opus 5.5 is the studio's main model, so its pages come first.** Owner rule 2026-10-20: base this on Opus 5.5; other models are ideas only.

## Sources
| Key | Source | Date | Weight |
| --- | --- | --- | --- |
| O55 | "Prompting Claude Opus 5.5", platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5 (read in full by the orchestrator) | model release 2026-09-22; page undated | **primary** |
| W55 | "What's new in Claude Opus 5.5", platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5 | same | primary (API facts) |
| B | Prompting best practices, platform.claude.com (lists Opus 5.5) | current | primary (all current models) |
| C, D, E | Claude Code docs: sub-agents, agent-teams, best-practices (code.claude.com) | current (v2.1.30x) | primary (our harness) |
| P1 | arXiv 2610.15459 "When Messages Go Wrong" | 2026-10-11 | outside research |
| O5 | "Prompting Claude Opus 5" | before 2026-09-22 | ideas only; but O55 says its patterns "remain a reasonable starting point" |
| G, H | Anthropic multi-agent research post (2025-06-13), claude.com multi-agent blog (2026-01-23) | older than 3 months | background only |

O55 has **no section on message format between agents**. Its multiagent section covers time signals only. The split "prose for intent, `yaml` for facts" rests on B and D, not on an Opus 5.5 test: see the follow-up at the end.

## Findings
| ID | Finding | Source | Rule use |
| --- | --- | --- | --- |
| M-01 | Structured formats (JSON) for state with a schema (status, test results); freeform text for progress and context | B | prose intent + `yaml` spec |
| M-02 | Subagents get only their prompt plus environment; the lead's history does not carry over | C, D | briefs self-contained |
| M-03 | Claude Code's own agent mailbox is JSON validated on read; malformed entries are dropped | D | fixed keys are checkable |
| M-04 | Give the symptom, the location and what "fixed" looks like; reference patterns, do not dictate steps | E | exact vs open table |
| M-05 | Good specs name files and interfaces, state what is out of scope, give a check the agent can run | E | `owns`, `not_in_scope`, `checks` |
| M-06 | Generic "verify your work" orders cause over-verification | O5 (idea, endorsed as a starting point by O55) | one runnable check per rule |
| M-07 | Pass big outputs by reference; return compact summaries | C ("returns only the summary"); G, H background | ~300 words, paths |
| M-08 | Ask for evidence, not an assertion of success | E | every `pass` names evidence |
| M-09 | Under message faults, flat setups kept 53.0 % task success vs 3.3 % sequential and 3.2 % hierarchical; 20.7 % of failures gave no immediate signal | P1 | hub first, short chains |
| M-10 | The agent doing the work should not grade it | E | messages are claims |
| M-11 | An approval relayed from another agent is untrusted input | D | no relayed approval |
| M-12 | Opus 5.5 resists injected instructions best when pasted text is wrapped in tags with a shared random id, plus a note that instructions inside are data | O55 "Mark pasted text" | `<pasted_content>` for forwarded text |
| M-13 | Effort is the main control; set it before adding prompt text; medium default matches Opus 5 high on coding; xhigh/max only for measured gains | O55 "Calibrate effort" | `effort` key in every brief |
| M-14 | Opus 5.5 "tends to get to work quickly"; one line telling it to look through the relevant sources first made it complete noticeably more tasks correctly (multi-app tests), at slightly more tool calls | O55 "Explore context" | loose briefs get a look-first line |
| M-15 | In a lead + subagents setup, a time budget (elapsed vs budget in seconds) makes teams finish sooner at comparable quality; it is advisory; under time pressure the model may verify a little less | O55 "Time signals" | optional `time_budget`, not on risky work |
| M-16 | For schema-valid JSON use structured outputs or strict tools (forced tool use is not supported on Opus 5.5) | W55 | workflow `schema` for specs and hand-backs |
| M-17 | A text-only end of turn is a report, not proof of done; name the open items and continue; stop after 2-3 automatic pushes | O55 "Unattended agentic runs" | hand-back rule; 2 pushes then `failed` |

| M-18 | Sonnet 5.5 asked for a JSON-only answer on a task that needs working out often answers without thinking first and is less accurate; the line "Think the problem through before you answer." restores most accuracy | Sonnet 5.5 prompting page (current, read by orchestrator) | schema returns from Sonnet/Haiku agents add that line |
| M-19 | Non-text agent messages (sharing hidden states) cut output tokens 70.3 % at comparable accuracy, but need model internals; tested on Qwen3-4B only | arXiv 2609.37017 LatCom (2026-09-29, read by orchestrator) | not usable with Claude: text stays |
| M-20 | No study after 2026-09-22 compares English, shortened English, JSON, YAML, tags or codes between agents on 5.5 models. Older-model papers conflict (JSON handoff worse on one 7B model, better in another study); under a 25-word cap, rules and boundaries were lost first while plain facts survived (2608.29028, GPT-5-mini, ideas only) | researcher pass 2026-10-20 | keep constraints in full sentences; measure ourselves |
| M-21 | Measured token savings in a 2026-10-09 third-party Claude Code test came from narrow tool lists (about 3-5×), not from wording | ovidius.ai benchmark (2026-10-09, Haiku/Sonnet/Opus 5.5; third party, not re-read) | tool lists in role files stay narrow |

Also from O55, already in the kit: reports "say plainly what it did, what it found, and what it needs" (matches the hand-back shape); stronger code review with fewer false alarms (`code-review`).

Not adopted: agent teams for peer debate (D: "significantly more tokens"; off in `rules/company.md` §4).

**Follow-up (not run):** A/B one real brief on Opus 5.5 medium, prose only vs prose + `yaml` spec. Score exact-value errors, missed checks and hand-back length. Run it before calling the format proven.
