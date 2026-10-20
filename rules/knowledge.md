# Knowledge rules — the context system

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Kit file: universal. Evidence: Claude Code memory/skills/sub-agents docs (read 2026-10-20, v2.1.296); arXiv 2607.17598 (2026-07-20, one routing level is enough, a second hurts); arXiv 2607.27250 (2026-07-28, short human-written context files; craft lives in skills); arXiv 2607.24882 (2026-07-27, no retrieval method dominates; agents miss needed files 27-35% of the time; a retrieved seed packet helps); Anthropic Managed Agents "dreaming" (2026-05-19, scheduled reviewed memory consolidation). Notes: `knowledge/reference/studio/context-research-2026-10.md`.

Results depend on context. These rules keep context **correct, small and findable** for every agent, in every game made with this kit.

## 1. One source of truth

- Everything the studio knows is plain markdown or data files **in this repository** (versioned, reviewable, readable by Claude, Codex and the owner). Obsidian or any other viewer is optional and never required.
- Private assistant memory is not shared with subagents or other games: anything another agent needs goes into the repository.

## 2. Load by cost

| Layer | What | Loaded | Size rule |
| --- | --- | --- | --- |
| Always | `AGENTS.md` + harness profile (+ `CLAUDE.md` imports) | every session | ≤ 200 lines total, written by humans or the lead, never auto-generated |
| Index | `knowledge/index.md` → one index per area | when a task starts | one routing level only: index → note |
| Packet | `python tools/context_packet.py packet "<task>"` | start of every task | the task's likely notes, files and decisions, with paths |
| Skills | `.agents/skills/<skill>/` (+ the game's overlay) | when the craft is needed | SKILL.md ≤ 500 lines; detail in references |
| Path rules | `.claude/rules/*.md` with `paths:` (Claude) | when matching files are touched | only area-specific rules |
| Agent memory | `.claude/agent-memory/<agent>/MEMORY.md` (`memory: project`) | when that agent starts | first 200 lines / 25 KB load; detail in topic files |
| Reference | `knowledge/reference/`, `knowledge/external/` (docs mirrors) | on lookup | agent-ready cards for big docs (dense tables), raw mirror for exact lookup |

## 3. Notes

Every note is **one topic** and starts with typed frontmatter, then the author line:

```yaml
---
type: decision | lesson | failed | system | job | reference | log | index | profile | overlay
scope: universal | game
status: draft | active | superseded
updated: 2026-10-20          # absolute dates only
source: J07 | session 2026-10-20 | url
supersedes: []               # paths of notes this one replaces
---
> Author: <role> · <model id> · <effort> · <date>
```

- **scope: universal** = true for any Roblox game made with the kit; candidate for `/kit-sync`. **scope: game** = this game only. Never mix scopes in one note.
- **Superseded, not deleted.** When a note is replaced, set `status: superseded` and link the replacement; the packet tool skips superseded notes.
- **Links:** use `[[folder/name]]` for related notes (they help humans, viewers and the packet tool's one-step neighbours). A link never replaces putting the fact in the note that needs it.
- **Dense for AI readers:** tables, fixed keys, `file:line`, numbers with units and sources.

## 4. Where things go

| Kind | Path | Type |
| --- | --- | --- |
| Owner decisions | `knowledge/design/decisions.md` (ledger rows with the owner's words) | decision |
| Open questions | `knowledge/design/open-questions.md` | — |
| Rejected approaches | `knowledge/design/tried-and-failed.md` | failed |
| What the game is, taste | `knowledge/design/game-profile.md` + design notes | profile |
| Finished systems | `knowledge/systems/<system>.md` (contract card first) | system |
| Jobs | `knowledge/jobs/<job-id>/` | job |
| Lesson drafts | `knowledge/inbox/YYYY-MM-DD-<job>-<agent>.md` | lesson (draft) |
| Accepted lessons | `knowledge/lessons/<area>/<slug>.md` | lesson (active) |
| Game overlays for kit skills | `knowledge/overlays/<skill>.md` (made by `/integrate`) | overlay |
| Session logs | `knowledge/logs/YYYY-MM-DD-<topic>.md` (≤ 40 lines) | log |
| Research and references | `knowledge/reference/<area>/` | reference |
| Generated maps and indexes | `knowledge/generated/` (tool-owned, never hand-edited) | index |

## 5. The learning loop

1. **Capture (every job, cheap):** at a gate answer or job end, each agent writes a lesson draft to `knowledge/inbox/` (template in `knowledge/inbox/README.md`): what worked, what failed, and **the owner's corrections word for word**. Haiku or Sonnet.
2. **Consolidate (weekly, inside `/improve`):** merge duplicates, convert dates, mark superseded, prune stale notes and agent memories, and **promote** a lesson into a skill, rule or overlay only when it happened twice or the owner stated or confirmed it. Every promotion links its evidence. The owner reviews the change summary before anything lands.
3. **Test:** a promotion that changes a skill is checked against that skill's eval briefs when they exist; `/doctor prompt-audit` (Claude) finds conflicts.
4. **Share:** universal lessons go to the kit with `/kit-sync`, owner-approved.

## 6. Retrieval health

- `python tools/kb_index.py` regenerates area indexes and runs the lint (missing frontmatter, dead links, superseded without replacement, notes over 300 lines, duplicate titles). Part of the gate.
- `python tools/eval_context.py` scores the packet tool on `knowledge/evals/retrieval.jsonl` (task → files the work really needed). Run it before and after any change to retrieval; keep a change only if the score holds.
