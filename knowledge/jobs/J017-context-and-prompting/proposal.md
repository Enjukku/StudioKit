---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J017 steps 1-3 (startup-cost.md, prompt-audit.md, knowledge/reference/studio/prompting-guide-2026-10.md)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J017 proposal (G1)

Evidence: `startup-cost.md` (measured), `prompt-audit.md` (file:line findings, per model), the cited fact sheet. Owner rules kept: self-review in every workflow book, reference images first, light checks, the gates, locked effort levels.

## A. Less start-up context (the big part)
| # | Change | Saves per agent | Decides |
| --- | --- | --- | --- |
| A1 | A `tools:` list for the 10 roles that get every tool today: the base file tools + SendMessage + only the MCP servers each uses (Studio for 9; Blender for rigger, environment, film, modeler; browser for film, modeler, ui-ux; Figma for ui-ux) — lists in `prompt-audit.md` Q4 | about 22-48 k | owner (permissions) |
| A2 | Remove the duplicate Blender MCP server (keep `blender`) | about 5-10 k for the lead and general agents | owner (your MCP settings) |
| A3 | Drop the Agent tool from roles that never start agents (no spawns in 49 role runs) | about 5 k (to verify) | owner (permissions) |
| A4 | Preload only each role's own workflow book (design + craft skill); shared skills (reference-images, platform-policy, ste-writing, studio-mcp, performance, analytics) load when their trigger fires (AGENTS.md §2 already names the triggers) | 2-7 k for 9 roles | lead |
| A5 | `explore` gets `memory: none` (it is read-only; memory added Write and Edit) | under 1 k | owner (permissions) |

Expected: a 50-agent M cutscene build starts with about a third fewer tokens.

## B. Prompts per model (small, measured changes)
| Model | Change | Why (fact sheet) |
| --- | --- | --- |
| Opus 5.5 | Remove the generic "double-check" lines duplicated in Opus role bodies; keep each skill's self-check step. Add one line naming early stops to avoid in unattended workflow runs | Opus checks its own work; extra verify lines cause over-checking (2.1.15); it may end long agent runs early (2.1.8) |
| Sonnet 5.5 | Anthropic's keep-working text for analyst and trend-scout; "Think the problem through" only for Sonnet roles; researcher: "search for specifics that may have changed, even when confident" | 2.2.2, 2.2.5, 2.2.11 |
| Haiku 5.5 | Keep Haiku briefs short; doc-keeper re-checks each file it wrote | long prompts at low effort make Haiku stop early (2.3.6); it skips checks at low effort (2.3.7) |
| All | Change behaviour with effort, not prompt text (no "think less" lines); no locked effort changes now; test medium for narrow Opus steps (exchange, sign) later, one A/B at a time | 2.4 |

## C. How we know quality holds
1. One smoke run before and after: start-up tokens per role (target: all-tools roles down by at least 25 k each).
2. The gate and the workflow tests (a tools list must not remove a tool a step uses).
3. The first real jobs: first-pass acceptance and defects you find stay the same or better (`evidence.md`); any drop reverts that change.

## To verify during the change
Per-server tool sizes, the Agent-tool roster size, the Figma connector's tool prefix, and that skills still load for a role with a tools list.
