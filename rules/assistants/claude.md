# Harness profile: Claude Code

> Author: kit-writer · claude-sonnet-5-5 · medium · 2026-10-20; mechanisms and context revised by orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016, checked on Claude Code 2.1.306); revised by orchestrator-fixer W1 · claude-opus-5-5 · high · 2026-10-21 (J016 G3); context and usage rows by orchestrator · claude-opus-5-5 · high · 2026-10-24 (J022); gate pause line revised by J024 writer · claude-opus-5-5 · default · 2026-10-24 (J024 design)

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
| Peer message | SendMessage to an agent id | Who can send and where ids come from: `rules/company.md` §5 item 3 (capability check C22: a `tools:` list without `SendMessage` cannot send). On 2.1.306 a message reaches a working agent at its next tool step; a message to a finished agent resumes it with its context and resends that whole context (J016 `pilot-plan.md` R6: 105 k tokens for a small probe). |
| Job workflow | Saved script per job type, `.claude/workflows/job-<type>.js` (source `.agents/workflows/jobs/`, synced) | One stage per call; the args (`job`, `stage`, `size`, `gate`, `studioId`, `change` and the type's flags) are in `.agents/workflows/jobs/README.md`. Owner gates sit between calls (a workflow cannot pause). Every `agent()` sets `agentType`, `model`, `effort`. Workflow agents have no ids: sideways work goes through files (`rules/company.md` §5). |
| Production chat | In the desktop app the lead starts sessions for long, independent jobs | Messages are plain text that points to files (C13). Batch updates into one message; pure news waits for the next status report (`rules/company.md` §5 item 6). |
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
| Audit | The owner runs `/doctor` weekly (a built-in command: agents cannot run it); `/improve` reminds the owner in its tips. Fix conflicts it shows in the canonical file. |
| Context | `python tools/context_packet.py packet "<task>" --role <role> --job <job-id>` first, then only the cited notes. |
| Session size (J022) | Every call re-reads the whole context, so cost is calls × context. One session per stage or task: when it ends, start a new session or `/clear`; job state lives in files and the hooks reload it. Past 500 k context (owner J023-D1), finish the step, write its state to the job files, and go on in a fresh session. **Gate pause (J024):** the lead cannot run `/compact` or `/clear`; before it sends a gate packet (G1, G3) or a digest it must wait on, it writes the stage state to the job files, and the packet's last line asks the owner to answer in a fresh session (or to run `/compact` first) when this chat is past the session size. |
| Images (J022) | An image stays in context and is re-read on every call until Claude Code drops the oldest at its image limit. The lead's chat takes only images the owner must see and failing-number diagnostics; makers and helpers view captures and hand back numbers and paths (`rules/company.md` §7 light checks). Never re-open an image to look again. |
| Tool calls (J022) | Batch: one call does several reads, greps or commands (a script, `&&`, `browser_batch`, `multi_edit`); no loops of one-line probes; cut long output at the source (`tail`, `grep`, `--json` with fields). |
| Helper models (J022) | Every `Agent` call names `model` and `effort`. Built-in helpers (general-purpose, Explore, Plan) otherwise inherit the main model: use the kit `explore` role or Sonnet for search and reading; Opus only for craft judgment. |
| Usage report (J022) | `python tools/usage_report.py --root <repo>`: context per session and subagent, with flags. `/improve` runs it weekly. |
| Settings | The owner applies permission and environment settings. Agents propose, never edit them. |

## Commit trailers (AGENTS.md section 6)

```
Agent: <role>
Model: <exact model id>
Effort: <effort level or "default">
```

Keep the Claude Code co-author line as well.
