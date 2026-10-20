# Harness profile: Claude Code

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20

Read `AGENTS.md` and `rules/company.md` first. This page holds only Claude Code specifics; CLAUDE.md imports it.

## Models and roles

| Tier | Model | Used for |
| --- | --- | --- |
| lead | opus | The lead chat; architecture; risky code review (tiers are set in `kit.json`) |
| craft | opus | Specialist craft (animation, VFX, models, UI, sound, design) and all code |
| research | sonnet | Reading docs into fact sheets, data pulls, Studio checks |
| mechanical | haiku | Search, copy, format, data entry |

- Every role file pins its model. No silent inherit.
- Roles and skills are canonical in `.agents/roles/` and `.agents/skills/`.
- `python tools/sync_harness.py` generates `.claude/agents/` and `.claude/skills/`. Never edit generated files. Run `python tools/sync_harness.py --check` in the gate.

## Mechanisms

| Mechanism | How in Claude Code | Rules |
| --- | --- | --- |
| Subagent | Agent tool with a named role | Up to 3 nested levels. Result returns as a summary. Pin model and effort in the brief. |
| Production chat | In the desktop app the lead starts sessions for long, independent jobs | Chats message each other by name with SendMessage. A message to an idle chat resends its full context, so batch updates. |
| Dynamic workflow | Saved script that calls agent() | Set model and effort on every agent() call. Run a small slice first. |
| Agent teams | OFF | Experimental, about 7x tokens, plan approvals are automatic. The owner sets `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=0`. Agents never edit their own settings. |

## Workflows and gate

- Workflows (`.agents/workflows/*.md`) are generated into `.claude/commands/` by the sync tool. Never edit the generated copies.
- The gate is `python tools/verify.py`.

## Memory and context

| Item | Rule |
| --- | --- |
| Role memory | Roles use `memory: project`. Each agent keeps its own MEMORY.md. The first 200 lines or 25 KB load. Keep it short. |
| Instruction size | Keep CLAUDE.md plus all imports under 200 lines. |
| Audit | Run `/doctor prompt-audit` weekly. It finds conflicting instructions. Fix conflicts in the canonical file. |
| Context | `python tools/context_packet.py packet "<task>"` first, then only the cited notes. |
| Settings | The owner applies permission and environment settings. Agents propose, never edit them. |

## Commit trailers (AGENTS.md section 6)

```
Agent: <role>
Model: <exact model id>
Effort: <effort level or "default">
```

Keep the Claude Code co-author line as well.
