---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010 step 3 (owner J010-D1, J010-D2)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Eval runbook: new vs old engineering agents

## Arms
| Role | New arm (kit) | Old arm (DestructionSimulator HEAD 2026-10-20, read-only) | Model · effort new / old |
| --- | --- | --- | --- |
| architect | `.agents/roles/architect.md`; skills architecture, engineering-craft (+ area skills it names) | `.claude/agents/architect.md`; skill roblox-architecture | Opus high / Opus medium (as defined) |
| feature-builder | `.agents/roles/feature-builder.md`; engineering-craft, testing + area skills | `.claude/agents/feature-builder.md`; roblox-architecture, luau-code-review + lens skill (remotes-security, datastores, gameplay-systems) | Opus high / Opus high (money, saves, remotes: both briefs raise it) |
| quick-builder | `.agents/roles/quick-builder.md`; engineering-craft | `.claude/agents/quick-builder.md`; luau-code-review | Opus medium / Sonnet medium (as defined) |
| reviewer | `.agents/roles/reviewer.md`; code-review, engineering-craft + area skills | `.claude/agents/reviewer.md`; luau-code-review, remotes-security, datastores | Opus high / Opus high (the set has money and saves) |
| performance-engineer | `.agents/roles/performance-engineer.md`; performance, engineering-craft, studio-mcp | `.claude/agents/feature-builder.md` + performance-profiling, mcp-studio-workflow | Opus high / Opus high |
| qa-lead | `.agents/roles/qa-lead.md`; testing, engineering-craft, studio-mcp | `.claude/agents/feature-builder.md` (writes test suites) | Opus medium / Opus medium |

Both arms run as `general-purpose` subagents with the role text loaded from its file, so the mechanism is the same; only the role file and skills differ. Each run gets its own copy of the task (`python -I eng-sandbox/make_run.py <task> <arm>`).

## Prompt shape (same for both arms)
1. "Your role instructions are in `<role file>`; read it whole and follow it. Your project rules and skills live under `<kit root or DestructionSimulator root>` (read-only); read the files your role names."
2. "Task brief: `<run>/../brief-<arm>.md`. Your project folder is `<run>`; write only there."
3. "Do not open `C:\Users\Firew\Downloads\uterd\eng-evals-hidden\`, other run folders, or the DestructionSimulator git history."
4. The model and effort from the table.

## Rounds
1. Hand-in 1 → the lead runs `python -I eng-evals-hidden/run.py <task> <run>` (or the grader / capture for that role).
2. Fail → send the agent only the failing check names and messages (SendMessage to the same agent). Max 3 hand-ins.
3. Record per run: first hand-in result, rounds used, final result, tokens and minutes, anything blocked.

## What the lead may see
Visible task briefs and starter files, runner output lines, grader scores. Not the hidden tests, keys, mutants or rubrics (they stay in `eng-evals-hidden\`).
