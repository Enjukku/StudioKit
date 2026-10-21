---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent engineering team)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J010 — Build the engineering team (architect, feature-builder, quick-builder, reviewer, performance-engineer, qa-lead)

| Field | Value |
| --- | --- |
| Job id | J010-engineering-team |
| Size | L (6 roles, a 133 KB paper to extract and fact-check, a rework study of 1,710 commits + 85 session logs, a hidden test bench, new-vs-old runs for every role) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved (J010-D1); G1b approved (J010-D2). Step 1 done except 2 fact-checks; step 2 (test bench) starting |
| Depends on | J001 skills (closed, owner-approved); `rules/anti-overengineering.md`, `rules/messages.md`; DestructionSimulator repo (read-only) |

## Owner's words (2026-10-21, excerpts)
- "engineering team: architect, feature-builder, quick-builder, reviewer, performance-engineer, qa-lead (one after the other in this chat)"
- "to understand how to build to the best of Lua's ability. You should look at the Roblox documentation."
- "A research paper I had written for these agents ... Use it as strong evidence, but not as gospel. Check claims that matter, and drop what you cannot back up."
- "The engineering skills I approved in J001 ... plus rules/anti-overengineering.md and rules/messages.md. These are the base."
- "A rework study of DestructionSimulator (read-only) ... find the tasks that needed several rounds of fixes. Sort each one by cause: hard by nature ...; process ...; agent quality ... Show me the top causes in each group before building the agents."
- "Do not assume the old agents are bad, and do not copy them either. Treat them as a baseline: keep what the evidence shows works, fix what the evidence shows does not."
- "The quality bar: professional game studio code, written the best possible way in Luau, using Roblox's built-in features instead of rebuilding them. Simple, clear code that is right the first time where possible, and a measure-change-measure loop where the problem is hard by nature (physics, performance)."
- "I am not a programmer, so I judge these agents by scores, not by reading code. Before I approve each agent, it must pass tests with right answers: hidden tests for the builders, planted bugs for the reviewer, performance targets for the performance engineer, and real past tasks from the rework study. Run the same tasks with the old DestructionSimulator agents as a baseline, and show me both scores in plain words: rounds needed, tests passed, performance numbers."
- "Write the hand-offs between them, and to the game designer, UI, VFX, sound, animator and environment designer, in the brief format (rules/messages.md)."
- "Models: Opus for all of them (code is always Opus at medium effort or higher); high effort for the architect, the performance engineer, and for money, saves and networking work."

## Goal
Six engineering agents that write professional Luau the Roblox way (engine features first, simple, right the first time where the problem allows), measure before and after where the problem is hard by nature, and prove it with scores the owner can read: tests passed, rounds needed, performance numbers, each next to the old DestructionSimulator agent's score on the same tasks.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Engineering_Agents_Research_2026.txt` (outside git). The attached path was `Environment_Designer_Research_2026.txt`; digest item 1 | 15 rules; why agents over-build; first-try success with current Claude; code craft; current Luau (new type solver, tables, strings, native); engine features first; phone performance budgets; tests and tools; review by consequence; hand-offs and task contract; rework records and cause taxonomy; protected evals; don'ts; source register (A Anthropic, C craft, L Luau, T, more) | ~1,150 lines, 133 KB | high: VERIFIED / EXPERIENCE / OPINION tags, dated sources. The paper says it executed no code, tests, Studio scenes or device benchmarks. Sources after the model cutoff → live check |
| J001 skills: data-saving, networking-security, performance, architecture, code-review (+ `references/luau-current.md`, `references/testing.md`), ui-basics, analytics, platform-policy, studio-mcp; `rules/anti-overengineering.md`, `rules/messages.md` | The base. Owner-approved 2026-10-20 | 9 skills | owner-approved |
| `knowledge/reference/architecture/strong-codebases-2026-10.md`, `roblox-operations-2026-10.md` | J001 paper digests (architecture; testing, releases, budgets, exploits) | — | owner material |
| Roblox Creator Docs local mirror `knowledge/external/roblox-creator-docs/` + `knowledge/reference/roblox/whats-new.md` | Engine truth (owner: "look at the Roblox documentation") | — | rank 1 for engine facts |
| DestructionSimulator (read-only): git history (1,710 commits, 2026-09-30 → 2026-10-20), `knowledge/logs/` (85 session logs), `knowledge/design/tried-and-failed.md`, `decisions.md` (≈290 rows), `knowledge/handoffs/`, `knowledge/research/`, old agents `.claude/agents/{architect,feature-builder,quick-builder,reviewer}.md` and their skills | Rework study source; the baseline agents; real past tasks with known final answers | 2.3 GB repo | evidence of what happened; game-specific content stays out of the kit |

## Scope
| In | Out |
| --- | --- |
| Rework study `knowledge/reference/engineering/rework-study.md`: each multi-round task, its rounds, its cause group and cause, with commit and log evidence; top causes per group shown to the owner **before any agent is built** (checkpoint G1b) | Changing DestructionSimulator in any way (read-only; snapshots go to a scratch folder) |
| Paper notes + fact-check tables in `knowledge/reference/engineering/` (Luau and engine claims against the docs mirror; Anthropic and craft claims against the web) | Rebuilding DestructionSimulator systems |
| Test bench outside both repos (`C:\Users\Firew\Downloads\uterd\eng-evals-hidden\`): hidden tests, planted-bug set, performance scenarios, answer keys; written by a separate agent; the lead never reads it while writing skills | Real-phone benchmarks by agents (digest item 6) |
| 6 role files; new or extended skill books only where the shared J001 books have no home (digest item 7); every J001 change shown as a diff | Rewriting J001 skills wholesale |
| Hand-off briefs: between the 6 roles, and to game-designer, ui-ux-designer, vfx-designer, sound-designer, animator, environment-designer (`rules/messages.md` format) | The animator and environment-designer agents themselves (J006, J008) |
| Score page per role: new vs old on the same tasks, plain words | |

## The tests (what the owner reads)
One run per task per agent. Same brief, same project snapshot, same tools for new and old. Only the role file and skills differ. A **round** is one hand-in; after a failed round the agent gets only the failing test names and messages (max 3 rounds).

| Role | Tasks (per role: 2 real past tasks from the rework study + 1 new hidden task) | Score in plain words |
| --- | --- | --- |
| feature-builder | money / save / remote / core-system tasks (effort high for money, saves, networking) | hidden tests passed on the first hand-in; rounds to pass all; tests passed at the end; serious review findings left; size of the change against the accepted fix |
| quick-builder | small, exact changes | same as feature-builder, plus "stayed in scope: yes/no" |
| reviewer | about 12 changes: about 10 with a planted bug (real past bugs where possible) + 3 clean changes | bugs found with proof (x of 10); false alarms; worst bug rated at the right severity |
| performance-engineer | 2-3 slow Studio scenarios, one from a real past performance problem | before and after numbers from the same capture (frame ms, script ms, memory MB, network KB/s, part count), target met yes/no, behaviour tests still pass |
| architect | past design problems that cost several rounds | traps from the answer key avoided (x of n), scored by a separate grader; plan size; questions it correctly sent to the owner |
| qa-lead | 2 features with a brief | planted bugs (buggy versions) its tests catch (x of n); false failures on the correct version |

Performance targets: from `performance` skill budgets where one applies (frame 16.67 ms for 60 FPS); otherwise a target set from the measured "before" number, shown to the owner at G1b as PROPOSAL. Studio on this PC runs server and client together and is not a phone (performance F-01): the numbers compare old vs new; they do not prove phone speed.

Baselines: the old agent runs as it was defined (its file, its skills, its model). No old performance-engineer or qa-lead exists → baseline = old feature-builder with the old `performance-profiling` skill, and old feature-builder writing the tests (its file lists "test suite"). Digest items 3-4.

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| paper extractors ×3 (§1-4; §5-8; §9-11 + don'ts + register) | Sonnet | high | dense notes |
| fact-checkers ×2 (Luau + engine claims vs docs mirror; Anthropic, craft and eval claims vs web) | Sonnet | high | claim, source, checked against, verdict |
| rework extractors ×4 (git history 09-30 → 10-07; 10-08 → 10-20; session logs; tried-and-failed + decisions + handoffs + old agent files) | Sonnet | high | task rows: rounds, commits, logs, cause, evidence |
| test-bench writer ×2 (builder hidden tests + qa planted versions; reviewer planted-bug set + architect answer keys), separate context | Opus | high | `eng-evals-hidden\` |
| performance scenario builder (Studio, one instance) | Opus | high | 2-3 scenarios + capture script + "before" numbers |
| lead (study merge, skills, role files, hand-offs, score pages) | Opus | high | as listed |
| new agents under test ×6 and old agents ×6 | Opus (old quick-builder: Sonnet, as defined) | per role | runs |
| grader (architect and reviewer proof, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time (company limit). Step 1: study and paper in parallel (Sonnet). Step 2: test bench (Opus, separate context). Step 3: one role at a time in the owner's order: lead writes the role and any skill it needs → new and old agents run the same tasks → score page → owner approves (G3 per role) → next role. Hidden tests run by a script; the lead sees scores and failing test names only.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one; context will compact) | |
| Agents | 9 Sonnet (study + paper) + 3 Opus (test bench) + about 36 test runs + about 15 repair rounds + 6 Sonnet grader runs ≈ 70 | |
| Models / effort | Sonnet high ×15; Opus high ×3 + feature/arch/perf runs; Opus medium for quick-builder, reviewer, qa runs; old agents at their own settings | |
| Studio time | one instance, sequential: performance scenarios and engine-bound tests | |

## Acceptance checks
- [ ] Rework study: every task row cites commits and/or log lines; every cause has one group (hard by nature / process / agent quality) and the evidence for it; top causes per group shown to the owner before step 3.
- [ ] Every paper claim used in a skill has a fact-check verdict (confirmed / corrected / kept as EXPERIENCE or OPINION / dropped); dropped claims listed with the reason; engine claims checked against the docs mirror.
- [ ] Hidden tests and answer keys written before any role file, by a separate agent; the lead's skill files contain no text from them (diff check).
- [ ] Each role: new and old scores on the same tasks in one plain-words table; one run per task stated as a limit.
- [ ] Builders: hidden tests pass by round 3 or the role is not proposed for approval.
- [ ] Performance: before and after numbers from the same capture script; behaviour tests pass after the change.
- [ ] No DestructionSimulator-specific content in kit files (brick terms, stage names, D-ids outside source tables = 0).
- [ ] Hand-off briefs to the 6 roles + 6 crafts follow `rules/messages.md` (§6 checks).
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "Okay, for this use Sonnet on high ... Opus medium where Opus medium should be used and ... Opus high where Opus high should be used." (J010-D1) |
| G1b rework causes + test targets | 2026-10-21 | "I will accept all six. Of your question." (J010-D2) |
| G3 architect | | |
| G3 feature-builder | | |
| G3 quick-builder | | |
| G3 reviewer | | |
| G3 performance-engineer | | |
| G3 qa-lead | | |
