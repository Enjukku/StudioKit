---
type: job
scope: universal
status: active
updated: 2026-10-24
source: owner chat 2026-10-23/24 (usage and speed in the games)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-24

# Job card: J022-context-and-usage — keep contexts small so the studio costs less and moves faster

## Owner's words (verbatim)
- "I'm testing out the workflows now inside of games, and it takes too much usage, and the progress is way too slow."
- "It's also important to note that I've been doing it using the workflow without ever doing /improve yet."
- "Open a kit job for the context and usage fixes: session-per-stage rule, image hygiene, batched tool calls, model defaults for helper agents, and a usage-report tool for /improve. Propose the settings changes for me to apply."

## Four lines
| Line | Value |
| --- | --- |
| Problem | Game sessions re-read very large contexts on every call: start 76-97 k, median 300-580 k, peak to 948 k; no auto-compaction before the window filled (GreatWallSim UI session: two manual compactions at 948 k and 883 k); 500-2,800 calls per session; up to 302 images in one chat; helper agents on Opus |
| Constraints | Quality first (owner: "best result over usage"); no cut of a fact, rule or check (`rules/messages.md`); settings are the owner's (agents propose, never edit); AGENTS.md + imports under 200 lines; the measuring tool is read-only and standard library only |
| Target experience | mastery: the owner sees game work move at a steady pace without hitting usage limits |
| Success test | `tools/usage_report.py` runs on the game projects and flags each oversized session; the next week's report shows median context per call and calls per session falling, with no rise in repair rounds |

## Scope (owner's list)
1. Session per stage rule. 2. Image hygiene. 3. Batched tool calls. 4. Model defaults for helper agents. 5. A usage-report tool run by `/improve`. 6. A settings proposal for the owner (not applied by agents).

## Status
Built 2026-10-24: `tools/usage_report.py` + 6 offline tests; rows Session size, Images, Tool calls, Helper models, Usage report in `rules/assistants/claude.md`; `rules/company.md` §7 light checks (images stay out of the lead's chat); `orchestration` §1 step 5 (fresh session per stage); `/improve` step 1 item 2b and the "Oversized context" row; `settings-proposal.md` (S1 `autoCompactWindow` 200000, S2 `CLAUDE_CODE_SUBAGENT_MODEL` sonnet) for the owner. Checks: own tests, workflow-free process tests, lint and sync PASS; full gate FAIL only on J020's uncommitted `test_soundbench_generate.py` (another chat's step 7 in progress). Not committed. Baseline (deduplicated), 2026-10-22..24: Reverse 7 sessions, median context 150-462 k, 3 helper-on-Opus agents; GreatWallSim 6 sessions, median 90-421 k, 12 big-context flags. Open: the owner applies S1 and S2; re-run the report after a week, then close.
