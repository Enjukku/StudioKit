---
type: lesson
scope: universal
status: draft
updated: 2026-10-21
source: J013 steps 1-6 (G1 → G2 test)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Lessons: building the analyst (J013, steps 1-6)

| # | What happened | Lesson | Evidence |
| --- | --- | --- | --- |
| 1 | The paper was already tagged (VERIFIED / EXPERIENCE / OPINION) and sectioned, so extraction and fact-checking ran as one pass per part (3 agents instead of 6) | When owner material is already tagged and dated, merge extract + check per part; keep the "section 4: ready-to-lift procedures" ask so the skills can copy tables | J013-T01..T03 |
| 2 | The Roblox checker found what the paper and the J001 skill had wrong: Early Harm Detection watches only playtime, ARPU and payer conversion; Experiments need `universe:read`, not `universe.analytics:read`; no documented results endpoint | Fact-check the kit's own existing skills on the same topic in the same pass; it found 3 errors in `analytics` T-10..T-12 | RF-44, 01 §5 |
| 3 | The statistics checker had no shell and hand-computed every check value; the lead re-ran them in Python and all matched | Give research agents a check-value table to fill; re-run every formula value in code before a tool builder tests against it | 02 §4; lead run 2026-10-21 |
| 4 | Starting the tool builder before all fact-checks landed worked because the API facts were in the local docs mirror; two `SendMessage` updates (scopes, check values) reached it mid-build | A tool can start from the docs mirror; send late facts as numbered brief updates with `fixed` values, not a new brief | T04 updates 1-2 |
| 5 | No key was set, so G2 ran on a synthetic history written **through the real pull code with a fake transport**; both runs found the planted causes, and the Opus-high run also found 4 generator faults by reconciling segments to totals | For data roles, build the test set through the production tool, plant 2 causes with a known split, and check that the agent validates data before reading it. Generator faults are a free test of data checks | `g2-scenario.md` |
| 6 | The lead's brief gave a Tuesday-to-Monday "week" and the weekly agent followed it while flagging the template clash | Check weekdays with code before writing dates into a brief | `g2-scenario.md` |
| 7 | 23 gaps came back from the two runs (rates without counts, `show` mixing series, no investigation template, no mix-adjustment command, no perf-regression brief, frontmatter rule missing) | Ask every test run for "places the skills were unclear, missing or contradictory (file and section)"; it produced a fix list worth more than the scores | ledger T07 |
| 8 | A researcher wrote its role memory into the job folder because its working directory was the job folder; lint failed | Start subagents from the repo root, or check `knowledge/jobs/<job>/.claude/` after each wave and move memory to `.claude/agent-memory/<role>/` | J013 gate run |
| 9 | Three chats opened "J013" within minutes; two renamed (J014, J015) | Same as J014 lesson 1: re-list `knowledge/jobs/` right before citing an id | J014 lesson 1 |
