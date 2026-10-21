---
name: analysis-craft
description: The analyst's how for a Roblox game's player data - pull with tools/analytics, check the math, answer the owner plainly; weekly page, A/B test plan and reading, what a feature should log. Use for "pull the numbers", "write the weekly page", "plan an A/B test", "read this test", "what should this feature log". Read analysis-design first (what and why).
---

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Kit skill: universal. Built in J013 (owner's analyst paper + fact-checks `knowledge/reference/analyst/01..03`; tool `tools/analytics/` J013-T04). Owner decisions: J013-D1 (Sonnet medium; Opus high for deep investigations), D3 (analyst plans events, `analytics` owns code), D4 (Open Cloud tool, key in the owner's environment), D5 (weekly page routing), D6 (defaults).

# Analysis craft: from question to a decision the owner can trust

## 1. When this skill starts
After `analysis-design` (the reading rules). Inputs: the question or task, the game's universe id (`knowledge/design/game-profile.md` or the brief), `knowledge/design/telemetry.md` (events and versions), the release, event and marketing calendars, the last weekly page, the game's overlay (`knowledge/overlays/analysis-craft.md`: settled API unknowns, lag, funnel names).

## 2. Read this file when
| You need | Open |
| --- | --- |
| Tool commands, the key rule, which command answers which question, unknowns to settle | `references/data-tools.md` (and `tools/analytics/README.md`) |
| What a new feature must log; the measurement spec; the split with the `analytics` skill | `references/event-planning.md` |
| Briefs to game designer, progression designer, marketing, live-ops designer, engineering; what you receive | `references/handoffs.md` |
| Answer or investigation file | `templates/analytics/finding.md` |
| Weekly page | `templates/analytics/weekly-report.md` |
| A/B test plan / result | `templates/analytics/ab-test-plan.md`, `templates/analytics/ab-test-result.md` |
| The reading rules (metrics, diagnosis, experiments, reporting) | `analysis-design` |
| Logging code, limits, Configs | `analytics` |
| Eval briefs | `evals/briefs.md` |

## 3. Steps per task type
Every task starts the same: **(a)** `status` (history fresh? >21 days → warn) · **(b)** write the metric contract · **(c)** pull what the contract needs · **(d)** check point status, maturity (`stats maturity`), breaks (2026-10-12, event versions) · **(e)** compute with `stats` and save outputs · then the task's own steps. Files go in the brief's folder (default `knowledge/jobs/<job>/analyst/`), named by content or date, never `report*` / `summary*` / `findings*` / `analysis*`; `show` and `stats` outputs in `calc/` next to the file.

**Every .md file you write** (finding, weekly page, briefs, calc notes) starts with the kit frontmatter (`rules/knowledge.md` §5): `type: job`, `scope: game` (`universal` only for kit tests), `status`, `updated`, `source`, `supersedes`, then the `> Author:` line.

**Urgent problems** (a crash or stability regression, broken purchases, lost saves, an invalid running test): finish the minimum evidence, then hand back with the first line `STATUS: done. URGENT: <one sentence>`; the lead tells the owner in the same turn. Do not wait for the weekly page.

**Missing game files** (`telemetry.md`, an empty `game-profile.md`): the rows that need them say UNAVAILABLE, and the hand-back lists creating them as a lead action.

### 3.1 Answer a question ("did the update help?", "where do players quit?")
1. Turn it into the symptom (`analysis-design/references/diagnosis.md` §1) and the decision it serves; if the brief does not say the decision, ask it in Part 1 ("what will you decide with this?") and answer anyway.

| Question type | Always check (and say so in the answer) |
| --- | --- |
| "is our number good / below average?" | no public genre table exists; give the game's own peer band with its pool and read date (or ask the owner to read it and tell you the date), and the game's own trend (`metrics-roblox.md` §4); Part 1 asks what the owner will decide with the answer |
| a price or offer change | payer count, payer conversion, ARPDAU and total revenue (not ARPPU alone); Robux scope and period; a running managed price-optimization test; a retention guardrail on all eligible players (`diagnosis.md` §8) |
| an event or update "worked" | eligible players, not joiners vs non-joiners; displacement; return after it; route to the live-ops designer (`experiments-updates.md` §7) |
| a test result or early harm signal | maturity, planned end date, SRM; Early Harm Detection only stops tests and never supports a launch (`experiments-updates.md` §1, §6) |
| a sudden drop in DN | `stats maturity` for the cohorts compared before anything else |

2. Locate in time and segment; check the player mix before blaming the game.
3. Competing-explanations table (≥ 2 rows) with evidence for and against each.
4. Pick the claim strength the design allows (causal ladder; update designs in `experiments-updates.md` §7).
5. Write the answer file from `templates/analytics/finding.md`: Part 1 in the owner shape (`reporting.md` §1), Part 2 with pulls, calculations and explanations checked. Hand-off brief to the role that owns the fix.

### 3.2 Deep investigation (big retention or revenue drop; conflicting evidence) — Opus, high effort
1. If you run on Sonnet: frame, pull, and return `needs-decision` to the lead asking for an Opus-high rerun, with the pull ids (owner J013-D1).
2. Run the full diagnosis checklist (`diagnosis.md` §10), every row with PASS/FAIL and its evidence.
3. Add a timeline of everything that changed (builds, configs, events, marketing, measurement) against the first break.
4. Ask for observed play from the affected players when telemetry cannot say why (playtest request via the lead).
5. Same answer shape; "how sure" names which checklist rows are still FAIL.

### 3.3 Weekly player-data page (on demand, J013-D6)
1. `pull --set weekly`, `pull --set performance`, `pull-funnel` per funnel in the telemetry plan; `experiments list` if tests run. The week is 7 full UTC days (default Monday to Sunday; the brief's dates win); compare with the same weekdays.
2. Fill `templates/analytics/weekly-report.md`. Part 1: exactly one finding (a quiet week: "no real change" is a finding), one recommendation, decision or "none".
3. Only mature cohorts get numbers; immature cells say when they become readable.
4. Rank funnel problems by players affected × severity, not by percentage drop.
5. Routing table: one line per role with a ticket when it needs action. Check `.agents/roles/` for each recipient: a role file that exists gets its brief directly (live-ops-designer exists since J014); only a role with no file goes through the lead.

### 3.4 A/B test plan (before anything goes live)
1. Fill `templates/analytics/ab-test-plan.md` completely: one primary outcome, smallest worthwhile effect in absolute units, guardrails with harm margins.
2. `stats samplesize` (or `samplesize-mean`) with the baseline from a pull; convert to days from **unique eligible players per day**, not DAU × days; add the outcome window and lag to get the outcome end.
3. Compare with Roblox's 14-60 days and the MDE shown at setup (the owner reads it in Creator Hub). If the game cannot detect the smallest worthwhile effect: say so plainly and propose a bigger change, a playtest or an honest descriptive before/after.
4. Owner actions: create the experiment with these settings; nothing else. The analyst never creates, starts or stops a test.

### 3.5 A/B test reading (at the planned outcome end, or an operational stop)
1. `experiments get` and `experiments stats` (SRM flag); arm counts → `stats srm` yourself too.
2. Results from the Creator Hub results page or the owner's export (no documented results endpoint); compute differences and intervals with `stats diff` / `stats welch` when counts are available; never rebuild an interval from a rounded chart.
3. `stats verdict` with the plan's benefit and harm margins → fill `templates/analytics/ab-test-result.md`. Early harm silence, early peeks and exploratory splits never make a winner.
4. Record the prediction vs the result in the plan's archive; nulls are kept.

### 3.6 Event planning for a new feature
Follow `references/event-planning.md` §2; deliver the measurement spec and the engineering brief (`handoffs.md` §5); write no code.

## 4. Craft core
| ID | Practice | Evidence |
| --- | --- | --- |
| K-01 | **Pull before you think.** `status` then the pull; the first number in your head is a guess until a file holds it | O, AP:464 |
| K-02 | **Every number cites its file**: pull id or `stats` output path. Shown arithmetic only for trivial sums of pulled counts | O, AP:464 |
| K-03 | **Save the calculation.** `stats` outputs as JSON next to the finding; the reader can rerun them | O, AP:451 |
| K-04 | **Missing is not zero; Projected is not final.** Carry the tool's flags into every table | V RF-04, RF-09 |
| K-05 | **Maturity by the tool, not by eye.** `stats maturity` for every D7/D30 cell you show | F-08 |
| K-06 | **SRM before effect.** A failed split check ends the reading: verdict Invalid | V S2 (ST-23) |
| K-07 | **The verdict comes from the rule, not from the mood.** `stats verdict` with the plan's own margins; the rule is labelled PROPOSAL until the owner decides strict vs default | 02 §5 |
| K-08 | **Settle API unknowns once per game** (retention date, lag, empty days, experiment stats) and record them in the overlay | 01 §4 |
| K-09 | **Part 1 is for a non-expert.** One page, plain words (`ste-writing`), every statistics word translated (`reporting.md` §2) | owner J013 brief |
| K-10 | **Route, do not fix.** Each role gets the evidence in its brief format; the analyst never prescribes the design | O, AP:440; E C26 |

## 5. Rules (final check, short)
- The API key is never seen, asked for, printed, stored or sent anywhere by the analyst.
- Read-only: no Creator Hub change, no experiment or config action, no write scope.
- No real player data in kit files; game data stays in the tool's data folder or the game's own repo.
- No number without a source file; no D7/D30 from an immature cohort; no winner without the planned players and time.
- Event plans: the analyst writes meaning and decisions; engineering writes code through `analytics`.

## 6. Self-check before returning
- [ ] `status` run; staleness warning passed on if >21 days.
- [ ] Every number in Part 1 and Part 2 cites a pull id or a saved `stats` output.
- [ ] Maturity, point status and measurement breaks shown where they apply.
- [ ] The template for the task type is used and complete; Part 1 has one finding and one recommendation.
- [ ] Hand-off briefs written for every role that must act (role files checked in `.agents/roles/`).
- [ ] Part 1 holds no hypothetical, example or made-up number; question-type checks (§3.1 table) applied.
- [ ] Owner actions listed; nothing changed in Creator Hub.

Project overlay: if `knowledge/overlays/analysis-craft.md` exists, read it after this file; it wins for this game.
