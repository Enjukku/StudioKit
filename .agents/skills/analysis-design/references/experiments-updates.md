# Experiments and updates: enough players, enough time, honest verdicts

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-design`. Owner J013: "It runs and reads A/B tests correctly (Roblox Experiments), and never calls a result real without enough players and time." Sources: owner's analyst paper (AP) §5, §6, Appendices B-C, fact-checked in `knowledge/reference/analyst/02-statistics-experiments.md` (ST, F ids; primary sources read 2026-10-21) and `01-roblox-platform-facts.md` (RF ids). Tags: **V** documented · **E** reported · **O** practice. Formulas run in `tools/analytics` (`analysis-craft/references/data-tools.md`), never by hand in prose.

## 1. What Roblox Experiments can and cannot do (V)
| Fact | Src |
| --- | --- |
| In-game tests (config values) and matchmaking tests; 14-60 days | RF-40 |
| In-game: control + up to 2 variants; matchmaking: up to 3 variants, equal split, one running matchmaking test per universe. Roblox recommends a simple 50/50 | RF-40 |
| The MDE shown at setup comes from the goal metric and players per arm (DAU, rollout, duration, split); MDE above 100% means significance is unlikely; under ~1,000 DAU useful results may be hard | RF-41 |
| Tracked: D1, D7, playtime, ARPU, ARPPU, payer conversion, session time; playtime, ARPU, payer conversion, ARPPU and session time are **cumulative over the experiment** (not the daily dashboard numbers). Goal metric = one of seven; **no D30, no custom metric** | RF-42 |
| Targeting is re-checked each session; a player who stops matching stays attributed to their arm but stops getting the value | RF-43 |
| A config key is locked while its test runs; one active test per key; in-game tests auto-complete 14 days after the decision date | RF-50 |
| Roblox calls a change significant when its interval does not overlap 0%, and says to ignore non-significant changes | RF-49 |
| Sample-ratio mismatch (SRM) is checked every 5 min for 24 h, then daily; a banner appears; Roblox says stop and restart. Roblox publishes no SRM p-value cut-off | RF-48 |
| **Early Harm Detection (EHD)**: first 24 h (or until daily results), every 5 min, **only playtime (−10%), ARPU (−20%), payer conversion (−20%)**; flags only if the whole interval is past the threshold; **no harm call under 10,000 enrolled across variant and control**; for stopping, never for launch | RF-44..47 |
| Experiments API: list, get, stats (documented field: SRM flag) with key scope `universe:read`; a per-metric results endpoint is **not documented**: read results from the Creator Hub dashboard or export unless a real-key test proves otherwise | 01 §4.3 |

So: no EHD flag says nothing about D1, D7, ARPPU or session time, and nothing at all under 10,000 enrolled. Silence is "not checked", not "safe".

## 2. Before the test: the plan (fill `templates/analytics/ab-test-plan.md` before any player sees it)
- **The question** (O, AP:247): among <eligible players>, does <change>, compared with <control>, improve <outcome over a defined horizon> by enough to justify <cost>, without more than <harm> on <guardrails>?
- **One primary outcome.** Diagnostics explain; guardrails constrain. Never pick the best-looking metric afterwards (ST-09).
- **Smallest worthwhile effect** in absolute units (percentage points, minutes), from player, design or business value — not the hoped-for lift (ST-14).
- **Guardrails with harm margins.** "No significant harm" is weaker than "harm ruled out beyond the margin"; for a critical guardrail (retention) set a non-inferiority margin and size the test for it (ST-38).
- **Exposure is what the player really gets** (ST-10): a tenure-targeted onboarding test may give a temporary treatment followed by normal play; audit with engineering. Players outside the rollout are not a second control.
- **Unit and spillover** (ST-40..41): per-player randomization suits private UI. Shared combat, trading, rewards, matchmaking or a server economy let one player's arm change another's game; say so, and consider party, server or cluster designs (often not possible natively). A server split that changes on rejoin is not a player experiment; an opt-in "new mode" is self-selection; a bandit optimizes allocation but does not give a fair fixed-test estimate.
- **Fairness is a constraint, never a variable**: paid random item odds, policy rules and purchase delivery are never tested (`diagnosis.md` §9).

## 3. Enough players: the power plan
| Rule | Src |
| --- | --- |
| No universal "enough players". Size from the outcome's spread and the smallest worthwhile effect | V S1 (ST-11) |
| Yes/no outcome (D1, payer conversion): two-proportion sample size (normal approximation, two-sided α, power) → `analytics.py stats samplesize` | F-02 |
| Mean outcome: n per arm ≈ 16 σ² / δ² at 95% confidence and 80% power (21 for 90%); assumes well-behaved means — revenue is zero-heavy and long-tailed, so treat it as rough and prefer player-level data | V S1 (ST-11..12), F-01 |
| Kohavi's examples (409,000 per arm for a 5% revenue change; under 122,000 for a 5% relative conversion change) are e-commerce examples, not Roblox needs | ST-13 |
| Count **unique eligible players** enrolling per day, not DAU × days: returning players repeat | O ST-17 |
| Prefer Roblox's MDE at setup for native tests. If MDE > smallest worthwhile effect: change the question, test a bigger change, reach more eligible players safely, run longer within the 60-day limit, or diagnose qualitatively. **Never lower the bar until a preferred result becomes significant** | O ST-16 |
| A small game can still find a severe usability failure (watch a playtest); it cannot reliably prove a tiny retention lift | O AP:259, 653 |

## 4. Enough time
- Duration covers recruitment, whole weekly cycles, outcome maturity and the feature's own cycle (learning, economy). Fix three dates before the start: enrollment end, **outcome end** (enrollment end + the longest outcome window, e.g. + 7 days for D7, + reporting lag), decision date (ST-18).
- Roblox's 14-60 days is the platform rule. Microsoft's typical 7-day tests are a different context (E, ST-19), and a second week does not always narrow the uncertainty: in one Microsoft study, for metrics already significant at day 7, standard errors grew at day 14 in 17% of comparisons (V S4, scoped, ST-20). "Longer is always surer" is unsafe when the population shifts.
- A price offer can pull purchases forward; a short session lift does not prove lasting retention (O, AP:265).
- Cohort maturity: a D*N* value for first-play date *d* is readable only after *d* + *N* days plus the reporting lag (lag undocumented; default 1 day, PROPOSAL) → `analytics.py stats maturity` (F-08).

## 5. Integrity and stopping
- **Sample-ratio check first** (ST-23..24): compare observed arm counts with the planned split (chi-square, `analytics.py stats srm`). Default alarm p < 0.0005 (Microsoft ExP; others use 0.001; Roblox publishes none) — always print p and the cut-off. A failed check = **Invalid**: diagnose (assignment, eligibility, logging, joins), never reweight or delete players until it passes. Also check persistence, logging parity, exposure and baseline balance; a passing balance test does not prove randomization worked.
- **Stopping** (ST-27..29): fixed end date, or a properly built sequential method. Repeated peeking at ordinary p-values is not a sequential design. Stop early only for a verified severe defect or service harm — an **operational stop**, never a win. A Bayesian analysis still needs a stated model, prior and decision rule; it is not a free pass for peeking.
- **Analysis** (ST-33..37): all correctly assigned eligible players (intention to treat). A triggered subset is fair only if the trigger is equally possible in both arms and not caused by the treatment ("bought after seeing the new shop" is not). Exploratory splits stay labelled and get confirmed in a new test; adjust for several primary comparisons. Keep the declared primary outcome and every test in the archive, nulls included.
- **Effect before significance** (ST-30..31): report control and treatment values, absolute difference, relative difference if the baseline allows, the interval and method, players per arm, follow-up and guardrails. Percentage points are not percent. A p-value is not "the chance we are wrong"; significance is not size or importance. Never build an interval from a rounded chart lift. Default interval for two rates: Newcombe (Wald fails at small counts, rates near 0 or 1, zero cells) (F-03).

## 6. Verdicts (first true wins; `analytics.py stats verdict` evaluates them)
Inputs: effect θ (higher = better), interval [L, U], smallest worthwhile effect *b* > 0, harm margin *h* > 0, guardrail intervals and margins, integrity, maturity (02 §5).

| # | Verdict | Condition | Owner sentence |
| --- | --- | --- | --- |
| 0 | **No verdict yet** | outcome window not finished | "Too early: the players in this test have not had <N> days yet. We read it on <date>." |
| 1 | **Invalid** | SRM alarm, broken assignment or logging, contamination, or an early stop on ordinary p-values | "The test setup failed, so it cannot tell us if the change helped. Fix <problem> first." |
| 2 | **Harmful** | U ≤ −h, or a guardrail's upper bound ≤ −its margin, or a confirmed severe defect | "This version hurt <outcome>. Keep or go back to the current version." |
| 3 | **Useful improvement** | default: L > 0 **and** point estimate ≥ b, and every guardrail's lower bound > −its margin. Strict option: L ≥ b | "The test supports <benefit> for <players>. We recommend <action> and keep watching <guardrail>." |
| 4 | **No worthwhile effect** | U < b and L > −h | "Any gain is too small to be worth it. Do not make this change for this reason." |
| 5 | **Inconclusive** | anything else; name the reason: benefit unproven, harm not excluded, guardrail not cleared | "We do not know yet whether this helped. Keep the current version while we <one next action>." |

The default rule for step 3 is a PROPOSAL awaiting the owner (J013 G3): the strict option needs far more players, which small games rarely have; the default still requires a real positive effect whose best estimate is worth it. Roblox's own "significant" (interval excludes 0) is weaker than both.

## 7. Measuring updates and events (no test possible)
Write an update measurement brief before release: intended players and mechanism, eligible population, version and config ids, rollout schedule, outcome windows, concurrent events and marketing, decision rule (ST-42). Analyse players who could get the change (old servers on old versions are not treated).

| Design (best first, if feasible) | Can show | Watch out for | Src |
| --- | --- | --- | --- |
| concurrent randomized holdout | a causal effect in the assigned group | contamination, spillover, exposure, maturity | ST-43 |
| randomized staggered or cluster rollout | a causal effect under its assignment | enough independent clusters; carry-over; shared worlds | ST-43 |
| difference-in-differences | a conditional causal estimate with a credible untreated group | parallel trends, no other shock, no spillover; treated (post − pre) − comparison (post − pre) (F-09; `stats did`: without standard errors it gives a point estimate only — add a placebo period, e.g. the same check one week earlier) | ST-45 |
| interrupted time series / synthetic control (BSTS) | a modelled counterfactual | backtest, placebo dates, alternative controls; never use a variable the update changed as a control; a flat pre-trend proves nothing | V S6, ST-44 |
| matched before/after (same weekdays, horizons, source mix) | a **description** only | everything else that changed | ST-47 |

- A game-wide release with no credible untreated group stays descriptive; never invent a control from another genre or game. An honest description beats a falsely precise causal number (O, AP:321).
- **Three clocks** (ST-48): calendar date (weekends, holidays, outside events), player age (progress, selection), time since first exposure (learning, novelty). An update can bring different new players, bring back veterans and change incumbents differently: report each, not one blended "update lift".
- **Events** (ST-49): event joiners chose to join; joiner vs non-joiner return is not the event's effect. Track reach among eligible players, completion, reward redemption, repeat play, return after the event, and displacement of normal play and spending.
- **After rollout** (ST-46): check delivery, performance and definitions match the test; compare the measured result with the predicted range (a selected winner's estimate usually shrinks); a long-term holdout where justified; end with one decision: continue, revert, revise, or get the missing evidence.
- 2026-10-12 discovery recording change: any window across it says so; never attribute it to a thumbnail or update (V RF-55).
