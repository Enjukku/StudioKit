---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "kit phase 1"
supersedes: []
---
> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

# Context research, October 2026

Evidence behind `rules/knowledge.md`. Related: [[reference/studio/orchestration-research-2026-10]].

| Finding | Source | Date | What it means for us |
| --- | --- | --- | --- |
| One routing level (index → note) is enough; a second level never helped and sometimes hurt. Progressive disclosure helps when the corpus is too large to browse | arXiv 2607.17598 | 2026-07-20 | Index points straight to notes. No index of indexes. Keep the index small. |
| Context files did not measurably change coding-agent correctness (bound ≤10-15 pp; 17 tasks, 288 runs). Failures were implementation skill | arXiv 2607.27250 | 2026-07-28 | Keep always-loaded files short. Put craft in skills and checks, not in long context files. Do not expect notes to fix weak work. |
| No retrieval family dominates. Agents' own trajectories missed every gold file in 27-35% of samples. A retrieval-derived seed context gave higher file F1 with less exploration. RepoMap gave the best budgeted yield at 8K tokens | arXiv 2607.24882 | 2026-07-27 | Run the context packet at the start of every task. Score it with `eval_context.py`. Budget the packet near 8K tokens. |
| Claude Code: CLAUDE.md under 200 lines; first 200 lines / 25 KB of MEMORY.md load; skills load descriptions only until used; SKILL.md under 500 lines; `/doctor prompt-audit` finds conflicts; subagent `memory: project` stores in `.claude/agent-memory/<agent>/` | code.claude.com docs: memory, skills, sub-agents (v2.1.296) | read 2026-10-20 | Size rules in `rules/knowledge.md` §2. Weekly prompt audit. Roles use project memory. |
| Anthropic Managed Agents "dreaming": a scheduled pass reviews sessions and memory stores, surfaces recurring mistakes and converged workflows, restructures memory; can auto-apply or let humans review. "Outcomes" rubric with a separate grader: up to +10 points task success | claude.com/blog/new-in-claude-managed-agents | 2026-05-19 | `/improve` consolidation is our dreaming pass, owner-reviewed. Acceptance checks are a rubric; a separate context grades them. |
| Memory helps mainly when context is insufficient or tasks are hard. No single memory form wins | EvoMemBench, arXiv 2605.18421 | 2026-05-18 | Capture lessons cheaply, promote only repeated or owner-confirmed ones. Mix forms (ledger, lessons, overlays). |
| The often-quoted 84% (context editing, 2025-09) and 85% (tool search, 2025-11) reductions are older than six months and measure tool results and tool definitions, not knowledge notes. No 2026 source found for an "80%" figure | Anthropic engineering posts | 2025-09 / 2025-11 | Do not quote these as gains for notes. Claim no percentage for our knowledge base without a measurement. |
| No 2026 controlled study shows wiki-links help agents retrieve | none found | read 2026-10-20 | Keep `[[links]]` for humans and one-hop neighbours. Put needed facts in the note itself. |

## Gaps

- No measured effect of our own notes on output quality. Track with job ledgers and the retrieval eval.
