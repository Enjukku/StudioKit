# Job workflows

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016, owner approval J016-D4). Kit folder: universal.

One saved Claude Code workflow per job type. `tools/sync_harness.py` copies each `job-<type>.js` byte for byte to `.claude/workflows/`, where `meta.name` becomes the slash command `/job-<type>`. Never edit the copies. Codex runs the same stages by hand from the `orchestration` skill's `references/job-types.md`.

## Contract every job workflow keeps
| Rule | Why |
| --- | --- |
| One stage per call: `args: {job, stage, size, studioId?, gate?, change?}` plus type-specific keys, stages `direction`, `proof`, `build`, `repair`; bad args return `blocked` before any agent starts. Every stage that writes to Studio requires `studioId` (each workflow's `whenToUse` says which; marketing art never does) | a workflow cannot pause for the owner (capability check C07); gates sit between calls |
| After every repair round the candidate is recaptured and refrozen before the next review round | reviewers never judge stale captures |
| A role the workflow cannot route (a finding's maker or an affected role) returns `needs-decision` | nobody drops work silently (`rules/company.md` §8) |
| M jobs run the proof inside `build` | `rules/company.md` §2 |
| Every `agent()` call sets `agentType` (the role), `model`, `effort` and a `schema` (the hand-back schema, evidence before status) | `rules/messages.md` §2; roles README |
| Every brief is built in the `rules/messages.md` §2 shape: `<intent>`, `<spec>` with packet line, inputs, owns, rules, deliver, checks | quality: complete briefs |
| Direction proposals are independent; reviewers judge artifacts and captures before hand-backs and never edit | `rules/company.md` §4, §7 |
| One Studio writer at a time (`studioId` from the lead); the built-in browser serves one agent at a time | `rules/company.md` §9 |
| Interface rounds ≤ 2; review repair rounds ≤ 2, then `needs-decision` | `rules/company.md` §9 |
| A planned role (animator) runs as a stand-in on `general-purpose` with its brief | `orchestration` skill §2 |
| The script never reads or writes files and never uses `Date.now()` or `Math.random()` | workflow runtime limits |

## Test
`python -m unittest tools.tests.test_job_workflows` runs every script here under `tools/workflows/wf_harness.mjs` with fake agents (no tokens): bad args are refused, every stage ends `done`, briefs are well formed, repair rounds are bounded. It is part of the gate (skipped where Node.js is not installed).

## Running one (the lead)
Only after the owner has asked for the job and answered the previous gate. Example: `Workflow({name: "job-cutscene", args: {job: "J021-boss-intro", stage: "proof", size: "L", gate: "<owner's G1 words>"}})`. Report the agent count and usage at the next gate.
