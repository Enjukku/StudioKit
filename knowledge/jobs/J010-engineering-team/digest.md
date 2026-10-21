---
type: job
scope: universal
status: active
updated: 2026-10-21
source: J010 G1
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# Decision digest: 2026-10-21 (J010 G1)

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 1 | Research paper. The attached path is `Environment_Designer_Research_2026.txt` (environment designer). `Engineering_Agents_Research_2026.txt` is in the same folder, saved 01:28 today, and covers the 6 roles | use the engineering paper / you send another file | use the engineering paper | use the engineering paper |
| 2 | Offline Luau test tool. Without it, every test runs in Studio, one at a time | (a) download `luau-windows.zip`, 3.2 MB, from github.com/luau-lang/luau, release 0.743 (2026-10-16), made by Roblox's Luau team; (b) Studio only | (a): fast tests for logic code; Studio stays for engine and performance tests | (b) |
| 3 | Baseline for performance-engineer and qa-lead (no old agent exists) | old feature-builder + old `performance-profiling` skill; old feature-builder writing tests | as listed | as listed |
| 4 | Old quick-builder ran on Sonnet | run it as defined (Sonnet) / run it on Opus | as defined: that is the real old agent. The score page names the model difference | as defined |
| 5 | Test size per role | (a) 3 tasks (about 70 agent runs in total); (b) 2 tasks (about 50) | (a): 2 tasks is too few to see a difference. One run per task is still noisy; scores show direction, not proof | (a) |
| 6 | Phone numbers | agents measure in Studio on this PC; real phone numbers need you to play on your phone | Studio numbers for approval; a phone check in the first real game | Studio numbers |
| 7 | Skill books | (a) 2 new books per role (12 books); (b) the shared J001 books + new books only where no home exists (likely Luau craft and testing) + small additions to J001 books, each shown as a diff | (b): smaller, one place per fact (`rules/anti-overengineering.md`) | (b) |
| 8 | Slot. J002, J003, J005 and J008 are open L jobs; the company limit is 2 at a time | (a) start step 1 now (study + paper, Sonnet only) and show you the causes; (b) wait for a slot | (a): step 1 is cheap reading and you asked to see the causes first | (a) |

# Decision digest: 2026-10-21 (J010 G1b: rework causes + test targets)

Study: `knowledge/reference/engineering/rework-study.md`.

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 9 | Accept the cause table as the basis for the agents | accept / change | accept | accept |
| 10 | Performance targets for the performance-engineer tests (PROPOSAL) | (a) frame p95 at or under 16.7 ms and worst frame at or under 50 ms after the stress, server and client, same recipe 3 runs, in Studio on this PC; behaviour tests still pass; replicated bytes and Part counts reported. The 50 ms worst frame is DestructionSimulator's own lag budget (8b13cfec); (b) your numbers | (a) | (a) |
| 11 | Past tasks as tests | rebuilt as small stand-alone tasks with the same trap (study §5); the full DestructionSimulator code is too big and too game-specific to replay fairly | rebuilt tasks | rebuilt tasks |
| 12 | Old-agent version for the baseline | HEAD (2026-10-20, includes the 10-09 fixes) / the first version | HEAD: it is the best the old agents ever were | HEAD |
| 2 (again) | Download the official Luau test tool `luau-windows.zip`, 3.2 MB, github.com/luau-lang/luau release 0.743 (2026-10-16), Roblox's Luau team | yes / no (Studio only) | yes | no download: hidden tests run in Studio only, one at a time |
| 13 | Studio for the engine and performance tests | open one Studio with an empty Baseplate when the test step starts | yes | the performance tests wait |

# Decision digest: 2026-10-21 (J010 G3 architect)

Scores: `scores-architect.md`.

| # | Decision | Options | Recommendation | Default if no answer |
| --- | --- | --- | --- | --- |
| 14 | Architect | (a) fix the new role (only real design choices to the owner, budgets are the architect's call, shorter plans) and rerun the 3 tasks once (about 0.45 M tokens with the grader; the fix is informed by this grading, so the rerun is labelled "task seen"); (b) approve the new architect as it is; (c) keep the old architect's text as the kit architect | (a) | (a) |
| 15 | Remaining test plan (asked before) | cut (one run per agent per role, max 2 fix rounds, one grader per role, about 4-5 M tokens) / pause | cut | cut |
