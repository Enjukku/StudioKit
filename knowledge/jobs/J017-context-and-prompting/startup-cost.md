---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J017 step 1 (J016 smoke-run task outputs, 2026-10-21; file sizes at 7bd7bf1)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# What one agent loads at start (measured)

Method: the J016 smoke runs (Haiku, one-step placeholder hand-backs, at most 2 tool calls) report tokens per agent; such a run is almost all start-up context. File sizes are characters / 4. "Base" = measured minus the kit's own files (rules, role file, preloaded skills): Claude Code's system prompt plus tool definitions.

| Role | Tools line | Measured (median, k tokens) | Rules + role + preloaded skills (k) | Base (k) |
| --- | --- | --- | --- | --- |
| sound-designer | 9 tools | 30.2 | 3.5 + 1.8 + 4.3 = 9.6 | 20.6 |
| reviewer | 7 tools | 30.6 | 3.5 + 2.0 + 4.8 = 10.3 | 20.3 |
| progression-designer | 9 tools | 43.8 | 3.5 + 2.3 + 13.3 = 19.1 | 24.7 |
| vfx-designer | 10 + browser | 44.5 | 3.5 + 2.5 + 8.1 = 14.1 | 30.4 |
| art-director | 10 + browser | 46.7 | 3.5 + 2.7 + 9.3 = 15.5 | 31.2 |
| game-designer | 10 tools | 47.8 | 3.5 + 3.0 + 15.4 = 21.9 | 25.9 |
| general-purpose (no role) | all | 67.7 | 3.5 | 64.2 |
| feature-builder | all | 81.4 | 3.5 + 2.1 + 5.0 = 10.6 | 70.8 |
| architect | all | 81.7 | 3.5 + 2.5 + 5.0 = 11.0 | 70.7 |
| performance-engineer | all | 83.9 | 3.5 + 1.7 + 7.0 = 12.2 | 71.7 |
| qa-lead | all | 84.1 | 3.5 + 1.7 + 7.2 = 12.4 | 71.7 |
| film-director | all | 93.8 | 3.5 + 2.6 + 13.2 = 19.3 | 74.5 |
| environment-designer | all | 94.4 | 3.5 + 2.5 + 14.0 = 20.0 | 74.4 |
| character-rigger | all | 96.3 | 3.5 + 2.2 + 14.9 = 20.6 | 75.7 |
| ui-ux-designer | all | 96.5 | 3.5 + 3.0 + 13.6 = 20.1 | 76.4 |

## Findings
1. **Tool definitions are the largest part.** A role with no `tools:` line (10 roles: architect, character-rigger, environment-designer, feature-builder, film-director, modeler, performance-engineer, qa-lead, quick-builder, ui-ux-designer) carries every connected MCP server's tools: base about 70-76 k against about 20-25 k with a short list. The built-in browser adds about 5-10 k.
2. **Two Blender MCP servers are connected** (`blender` and `Blender`, 26 tools each): one copy is pure duplicate cost for every all-tools agent and the lead.
3. **Preloaded skills cost 2-15 k per agent.** The largest: game-designer 15.4 k (7 skills), character-rigger 14.9 k, modeler 14.2 k, environment-designer 14.0 k.
4. **The kit's always-loaded rules are small** (about 3.5 k).
5. A 50-agent M cutscene build spent 3.5 M tokens on Haiku doing no work; on Opus the same start-up cost is paid at Opus prices.

## Levers (to size in the proposal)
| Lever | Saves per agent | Who decides |
| --- | --- | --- |
| A `tools:` list per role naming only the MCP servers it uses (wildcards such as `mcp__Roblox_Studio__*`) | about 45-55 k for the 10 all-tools roles | owner (tool lists are permissions) |
| Remove the duplicate Blender server | about 5-10 k for all-tools agents and the lead (estimate) | owner (MCP config) |
| Preload only the design skill; the craft skill loads when the step needs it | about 3-8 k for the heavy roles | lead proposal, test first |
