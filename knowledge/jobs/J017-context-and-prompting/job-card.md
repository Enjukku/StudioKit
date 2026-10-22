---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (after J016)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J017 — Lower the start-up context of every agent; prompt each model the way Anthropic recommends

| Field | Value |
| --- | --- |
| Job id | J017-context-and-prompting |
| Size | M (measure and research, one proposal at G1, then changes across roles, skills and workflow briefs) |
| Job owner (agent) | lead (orchestrator) |
| Status | waiting on G3: changes made (e74719f); after-measurement done (`startup-cost.md` "After"): 6 of 8 measured roles saved 29-33 k, film-director 22 k, ui-ux-designer 16 k |

## Owner's words (2026-10-21)
"So how do we improve this further? You said we use a lot of usage just booting up skills, right? So how do we fix that?"
"First is the Claude prompting guide. Are we creating prompts properly? https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices And this is specific towards each model. So are we prompting Sonnet 5.5 properly? Are we prompting Opus 5.5 properly? Are we prompting Haiku 5.5 properly?"
"This might be helpful for lowering the amount of context we automatically boot up while still getting a similar result."

## Steps
| # | Step | Gate |
| --- | --- | --- |
| 1 | Measure what each role loads at start (rules, role file, preloaded skills, memory, tool definitions) from the smoke-run journals and the files | — |
| 2 | Fact sheet from the prompting guide, per model, with citations | — |
| 3 | Compare our briefs, role files, skills and workflow briefs with the guide | — |
| 4 | Proposal: what to cut or move, expected tokens saved, how quality is protected and measured | **G1** |
| 5 | Changes, gate, one before/after measurement | **G3** |
