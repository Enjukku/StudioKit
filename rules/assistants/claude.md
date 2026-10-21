# Harness profile: Claude Code

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; mechanisms and context revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016, checked on Claude Code 2.1.306)

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
| Subagent | Agent tool, role as the agent type | Nest at most 2 below the lead (platform max 3). Pin model and effort in the brief. |
| Peer message | SendMessage to an agent id | Subagents cannot list each other: ids come from the job's `crew.md` and the brief's `peers`. On 2.1.306 a message reaches a working agent at its next tool step; a message to a finished agent resumes it with its context. |
| Job workflow | Saved script per job type, `.claude/workflows/job-<type>.js` (source `.agents/workflows/jobs/`, synced) | One stage per call, `args: {job, stage}`; owner gates sit between calls (a workflow cannot pause). Every `agent()` sets `agentType`, `model`, `effort`. |
| Production chat | In the desktop app the lead starts sessions for long, independent jobs | Messages are plain text that points to files. A message to an idle chat resends its full context, so batch updates. |
| Hooks | `tools/hooks/` scripts: job pointer at subagent start, job state after compaction, hand-back shape check | The owner enables them in settings (`tools/hooks/README.md`). |
| Agent teams | OFF | Experimental, interactive only, one team per session; messaging does not need them. Keep `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` unset or `0`. Agents never edit their own settings. |

## Workflows and gate

- Slash-command workflows (`.agents/workflows/*.md`) are generated into `.claude/commands/`; job workflows (`.agents/workflows/jobs/*.js`) into `.claude/workflows/`. Never edit the generated copies.
- The gate is `python tools/verify.py`. After every Claude Code update, re-run the capability probes (`rules/knowledge.md` §8).

## Memory and context

| Item | Rule |
| --- | --- |
| Role memory | Roles use `memory: project`. MEMORY.md is an index (first 200 lines or 25 KB load); parallel instances of a role share the folder, so write dated topic files. Craft lessons only. |
| Instruction size | Keep CLAUDE.md plus all imports under 200 lines. Skill descriptions ≤ 400 characters: the skill list has a budget and drops the least-used descriptions. |
| Compaction | Each invoked skill keeps its first 5,000 tokens (25,000 in total). Steps and rules sit at the top of SKILL.md; job state lives in files; re-load `orchestration` after compaction. |
| Audit | Run `/doctor prompt-audit` weekly. It finds conflicting instructions. Fix conflicts in the canonical file. |
| Context | `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>` first, then only the cited notes. |
| Settings | The owner applies permission and environment settings. Agents propose, never edit them. |

## Commit trailers (AGENTS.md section 6)

```
Agent: <role>
Model: <exact model id>
Effort: <effort level or "default">
```

Keep the Claude Code co-author line as well.
