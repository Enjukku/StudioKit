---
type: job
scope: universal
status: active
updated: 2026-10-21
source: owner chat 2026-10-21 (/build-agent analyst)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21

# J013 — Build the analyst agent

| Field | Value |
| --- | --- |
| Job id | J013-analyst |
| Size | L (new role, 2 skill books, an 831-line paper with 41 dated sources (several after the model cutoff) to extract and fact-check, a data tool on Open Cloud with tests, a stats helper with tests, 3 templates, a real test) |
| Owner (human) | owner |
| Job owner (agent) | lead (orchestrator) |
| Status | G1 approved 2026-10-21 (J013-D6). Steps 2-6 done 2026-10-21: 3 fact-checks (192 rows) in `knowledge/reference/analyst/`; tool `tools/analytics/` (51 tests); skills analysis-design, analysis-craft; 4 templates in `templates/analytics/`; role `analyst`; evals E1-E5 + hidden H1-H5 (5/5 pass after fixes); G2 on a SYNTHETIC TEST history (`g2-scenario.md`). G3 waits: `digest-g3.md` |
| Depends on | `analytics` skill (J001, logging side, exists); Open Cloud Analytics Query API (local mirror `knowledge/external/roblox-creator-docs/cloud/guides/analytics/`); Experiments API (`cloud/guides/experiments.md`); `trend_keys.py` key pattern (J004); `networking-security` N-11 (keys); `platform-policy`, `ste-writing`, `dataviz` skills; game-designer, progression-designer, marketing roles (exist); live-ops-designer role (planned, not built) |

## Owner's words (2026-10-21, excerpts)
- "It reads each game's own player data and explains what is happening and why: where players quit, how far they get, how long they stay, whether they come back, how the economy flows, what players buy, and how the game runs on their devices."
- "It answers questions like 'why did retention drop?' and 'did the update help?' with one main finding, the evidence, how sure it is, and one recommendation, in plain words. I am not a data expert."
- "It runs and reads A/B tests correctly (Roblox Experiments), and never calls a result real without enough players and time."
- "It decides which events a new feature should log, using the approved analytics skill from J001 (that skill covers the logging code; this agent covers reading the data)."
- "It sends a weekly report to me, the game designer, the progression designer, marketing and the live-ops designer."
- "A script that pulls the game's data through Roblox's official Open Cloud analytics APIs and saves the history, so trends can be compared over time. The API key lives only in my environment, never in the repo or in chat."
- "Templates: a weekly analytics report for a non-expert owner, an A/B test plan, and an A/B test result with a plain-language verdict."
- "Use it as strong evidence, but not as gospel. Check claims that matter, especially Roblox analytics facts, benchmarks and statistics rules, and drop what you cannot back up."
- "Model: Sonnet, medium effort; Opus at high effort for a deep investigation (for example a big retention drop)."

## Goal
One `analyst` agent that reads each game's own player data and tells the owner what changed, for whom, how sure we are, and the one thing to do next, in plain words. It reads the data correctly (cohorts of equal age, right denominators, measurement breaks marked), never calls a result real without enough players and time, and never invents a benchmark. It plans and reads Roblox Experiments, decides what a new feature must log (the `analytics` skill owns the code), and writes a weekly report routed to the owner, game designer, progression designer, marketing and live-ops designer. Every number it reports comes from a saved pull or a deterministic calculation, never from prose.

## Material received
| Source | What | Size | Trust |
| --- | --- | --- | --- |
| `C:\Users\Firew\Downloads\Roblox_Analyst_Research_2026.txt` (outside git; owner wrote it) | Evidence contract; 15 rules; metric contract and metric table; benchmarks (peer band 50th-90th, no public genre matrix); diagnosis (symptom split, competing-explanations table, funnels, causal language ladder); economy and purchase analysis; experiments (native tool limits, power, duration, SRM, Early Harm Detection, 5 verdicts); updates and events (design hierarchy, 3 clocks, 2026-10-12 discovery break); feedback as data; event planning; reporting to a non-expert; 12-step process; templates (diagnosis checklist, A/B plan, A/B result, weekly report); don'ts; open questions; source register R1-R21, I1-I12, S1-S8 | 831 lines, 96 KB | high: VERIFIED / EXPERIENCE / OPINION on every claim, dated sources, no invented benchmarks. No game data was used. R11, R18, R19, R20, I1 and the 2026-08-24 API post are after the model cutoff (2026-06) → live check |
| Kit: `analytics` skill (J001), local docs mirror (`production/analytics/`, `production/experiments.md`, `cloud/guides/analytics/`, `cloud/guides/experiments.md`), `trend_keys.py` / `trend_store.py` (J004) | The logging side, the engine truth, a tested key and history pattern | — | owner-approved / engine docs |

## Scope
| In | Out |
| --- | --- |
| Reference notes + fact-check tables in `knowledge/reference/analyst/` | Logging code, AnalyticsService calls, telemetry module (the `analytics` skill and engineering own them) |
| Skills `analysis-design` (what and why, read by designers and marketing too) + `analysis-craft` (how), names in digest item 3 | Changing an experiment, a config or a price in Creator Hub (owner actions) |
| `tools/analytics/`: Open Cloud pull + history store + stats helpers, with offline tests (digest items 4-6) | Raw player-level data, scraping, undocumented endpoints |
| 3 templates in `templates/analytics/`: weekly report, A/B test plan, A/B test result | The live-ops-designer role (planned; hand-off brief only) |
| Role file `analyst` (Sonnet medium; Opus high for deep investigations); roster row from planned to built | A real diagnosis of a game before G2 |
| Hand-off briefs to game designer, progression designer, marketing, live-ops designer (planned), engineering (logging requests) | |
| One-line scope change in `analytics` description (digest item 7) | |
| Eval briefs + hidden cases; 1 real test (G2) | |

## Crew
| Role | Model | Effort | Deliverable |
| --- | --- | --- | --- |
| extract + fact-check ×3: (A) Roblox platform facts R1-R21 + the Open Cloud and Experiments APIs; (B) statistics and experiment rules S1-S8 + the paper's power, SRM, verdict and causal rules; (C) studio practice I1-I12, feedback, economy, reporting | Sonnet | high (J004, J009, J012 precedent) | one notes file + one fact-check table per part |
| tool builder (`tools/analytics/` + tests) | Opus | medium (no money or saves; read-only key handling follows N-11) | scripts + tests |
| lead (merge, skills, templates, role, hand-offs, evals, review) | Opus | high | 2 skills, 3 templates, role, hand-offs, evals, roster |
| analyst test (new agent) | Sonnet medium for the weekly report; Opus high for one deep question | per owner | G2 package |
| grader (hidden cases, separate context) | Sonnet | high | rubric scores |

## Mechanism
Subagents, max 3 at a time. Wave 1: the 3 extract+fact-check agents (the paper is already tagged and structured, so extraction and checking are one pass per part; this saves 3 agents against J012). Wave 2: the tool builder (it needs fact-check A for the API facts). The lead writes the skills and templates. The new agent runs the G2 test as a subagent.

## Budget
| | Estimate | Actual |
| --- | --- | --- |
| Sessions | 1 (this one) | 1 |
| Agents | 3 extract+check + 1 tool + 2 test runs + 1 grader = 7 | 11: 3 + 1 + 2 + 1 hidden run + 3 re-runs + 1 grader (re-runs after skill fixes; over by 4) |
| Models / effort | Sonnet high ×4; Opus medium ×1; Sonnet medium ×1 + Opus high ×1 (test); lead Opus high | Sonnet high ×4 (3 checkers + grader); Opus medium ×1 (tool); Sonnet medium ×5 (weekly, hidden, 3 re-runs); Opus high ×1 (investigation); lead Opus high |
| API calls | G2: about 20-40 Open Cloud queries with your key (read-only) | 0 (no key set; synthetic history through the real pull code) |

## Acceptance checks
- [ ] Every Roblox analytics fact, benchmark, threshold and statistics rule in a skill has a source, a date and a verdict (confirmed / corrected / unverified-kept-with-label / dropped); dropped claims listed with the reason.
- [ ] No invented numbers: no genre benchmark, no "good D1", no universal player count or test length. Platform numbers are stated as the platform's limits, with link and date read.
- [ ] Every owner-facing answer has the shape: one finding, evidence (counts + denominator + window), how sure (high / moderate / low with the reason, never an invented percentage), one recommendation with an owner and a review date.
- [ ] A/B: plan template is filled before exposure; result template has the 5 verdicts; "enough players and time" is a stated, checkable rule (native MDE vs smallest worthwhile effect, 14-60 days, matured outcomes, SRM check); early harm signals never pick a winner.
- [ ] Tool: the key is read only from an environment variable, never logged, written or echoed (planted-key test); history is append-only with pull time, query and point status (`Projected`, `NotStatisticallySignificant`) kept; offline tests pass with recorded API fixtures; no network in tests.
- [ ] Stats helpers: every formula has a test against a published value or a hand-computed case.
- [ ] Event planning: the analyst writes the decision and the observation; the `analytics` skill and engineering own the code; the hand-off brief says so.
- [ ] 3 templates exist; each one is used in the G2 test or an eval.
- [ ] Hand-off briefs to the 5 recipients follow `rules/messages.md`.
- [ ] Skills ≤ 500 lines, "Read this file when" table, overlay line; `python tools/sync_harness.py --check` and `python tools/verify.py` PASS.
- [ ] Evals: 3-5 briefs with must-pass checks; hidden cases scored by a separate grader.

## Gates
| Gate | Date | Owner's words |
| --- | --- | --- |
| G1 brief | 2026-10-21 | "You may begin." |
| G2 first real test | | |
| G3 final approval | | |
