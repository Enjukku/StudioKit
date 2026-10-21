---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J013-T02, Roblox_Analyst_Research_2026.txt + primary sources checked 2026-10-21"
supersedes: []
---
> Author: researcher · claude-sonnet-5-5 · high · 2026-10-21

# Statistics and experiment method for the analyst (fact-check of the analyst paper, statistics side)

Scope: the statistics and experiment-method claims of the analyst paper (AP): AP:36-59, 239-303, 305-342, 443-491, 515-583, 619-633 and the source register AP:797-829. Roblox platform facts (R1-R21) and studio-practice claims (I1-I12) are not checked here (see `01-roblox-platform-facts.md`); where a rule mixes both, only the statistics part is checked. The paper stays outside git; this note paraphrases it. AP:n = line n of the paper file.

## 1. How I checked

All reads on 2026-10-21. No verdict comes from memory or from a search summary. Quotes are 15 words or fewer. WebFetch returns an extract, so "extract" means second-hand. I had no calculator: every check value was computed by hand to 6+ digits (z = 1.959964, 0.841621, 1.281552, 1.644854). Test with tolerance: intervals 5e-4, sample sizes plus or minus 2, p-values 1e-4 relative where shown.

Verdicts: confirmed = a source I read says it, or the math reproduces it. corrected = the paper's wording needs the fix shown. unverified-kept-with-label = not proven, kept with the label. dropped = removed.

| Code | Source (publication date) and how read |
| --- | --- |
| M | Docs mirror `knowledge/external/roblox-creator-docs/` (refreshed 2026-10-20 per note 01). PE = `production/experiments.md`; RT = `production/analytics/retention.md`; CA = `cloud/guides/analytics/index.md`. Read in full for the lines cited |
| S1 | Kohavi et al., DMKD 18:140-181 (2009). PDF at exp-platform.com and ai.stanford.edu: **text layer unreadable by my tool** (4 hosts tried). Read: Springer abstract page (extract, no body; paywalled) and https://www.slideshare.net/slideshow/microsoft-guide-controlled-experiments/25991003 (extract; looks like the 2007 KDD version, see ST-11). Body of the 2009 paper: NOT read |
| S2 | https://www.microsoft.com/en-us/research/articles/diagnosing-sample-ratio-mismatch-in-a-b-testing/ (2020-09-14), live extract |
| S3 | https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-during-experiment-stage/ (2021-01-25), live extract |
| S4 | https://www.microsoft.com/en-us/research/articles/external-validity-of-online-experiments-can-we-predict-the-future/?lang=zh-cn (2024-11-20), live extract (page chrome in Chinese, text English) |
| S5 | ASA statement, Am. Stat. 2016. PDF unreadable. Read: ScienceDaily reprint of the ASA release, https://www.sciencedaily.com/releases/2016/03/160307092305.htm (2016-03-07), extract: six principles |
| S6 | Brodersen et al., Ann. Appl. Stat. 9:247-274 (2015). Read: research.google page (abstract) + full text via https://ar5iv.labs.arxiv.org/html/1506.00356 (extract, sections 1-5) |
| S7 | https://learn.microsoft.com/en-us/xbox/playfab/live-service-management/game-configuration/experiments/experimentation-keys : page metadata `updated_at` 2025-05-01 (`ms.date` 2020-03-03). Live, whole page text |
| S8 | https://arxiv.org/abs/1701.02359 (submitted 2017-01-04), abstract extract |
| E1 | Zhou, Lu, Shallah, "All about sample-size calculations for A/B testing", arXiv:2305.16459 (2023), ar5iv extract (about 97% of text) |
| E2 | Deng, Knoblich, Lu, "Applying the Delta method in metric analytics", arXiv:1803.06336 (2018), ar5iv extract |
| E3 | Johari, Pekelis, Walsh, "Always Valid Inference", arXiv:1512.04922 (2015), ar5iv extract (65% of text) |
| E4 | Deng, Lu, Chen, "Continuous Monitoring of A/B Tests without Pain", arXiv:1602.05549 (2016), ar5iv extract |
| E5 | Lakens, "Equivalence Tests: A Practical Primer", Soc. Psych. Pers. Sci. 8(4):355-362 (2017), https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/ extract |
| E6 | Microsoft ExP, Patterns of Trustworthy Experimentation: Post-Experiment Stage (2021-12-24), extract: https://www.microsoft.com/en-us/research/articles/patterns-of-trustworthy-experimentation-post-experiment-stage/ |
| E7, E8 | NIST/SEMATECH e-Handbook: 1.3.5.15 chi-square GOF (eda35f.htm); 1.3.5.3 two-sample t-test with Welch df (eda353.htm), extracts |
| E9 | Wikipedia, Binomial proportion confidence interval (Wald, Wilson, continuity-corrected Wilson), extract. Textbook formulas, used as a convenient reference |
| E10 | statsmodels source `confint_proportions_2indep` (https://raw.githubusercontent.com/statsmodels/statsmodels/main/statsmodels/stats/proportion.py), cites Newcombe 1998, Stat. Med. 17:873-890 (the paper itself not read) |
| E11 | https://sample-size.net/SampleSizeProportionsStandard02.php (cites Hulley et al., Designing Clinical Research, 4th ed., App. 6B; Fleiss, Tytun, Ury 1980), extract |
| E12, E13, E14 | Wikipedia: Difference in differences (Card-Krueger numbers); Design effect (Kish); Multiple comparisons problem, extracts |
| E15, E16 | Nie et al., arXiv:1708.01977 (2017) abstract; Bojinov, Simchi-Levi, Zhao, "Design and Analysis of Switchback Experiments", arXiv:2009.00148 abstract |
| E17 | https://confidence.spotify.com/glossary/sample-ratio-mismatch.md (vendor docs, undated), extract |
| E18 | Secondary only, not evidence for rules: Hacker News thread 2011-02-15 (https://news.ycombinator.com/item?id=2221076) quoting S1; GrowthBook blog (peeking numbers) |

Not read, so not used: Lehr 1992 (McGill PDF unreadable), Newcombe 1998 PDF, Fabijan et al. KDD 2019 body, Boos and Hughes-Oliver 2000.

**Counts (section 3):** 64 rows. Confirmed 45. Corrected 7. Unverified-kept-with-label 12. Dropped 0 (4 outside items refused, section 7).

## 2. Notes: rules to use (paraphrased; corrected where section 3 says so)

| ST | Topic | Rule | AP | Tag |
| --- | --- | --- | --- | --- |
| ST-01 | Metric contract | Before any answer write decision, universe, analysis unit, eligible population, dates, timezone, numerator, denominator, revenue basis, missing-data rule, version, source. Player, session, attempt, transaction and server are different units | 38 | OPINION |
| ST-02 | Metric contract | One player's sessions and purchases are not independent. A per-player test must be analysed per player (or with a delta-method or cluster-robust variance), never per session | 38 | OPINION [S1,S2] |
| ST-03 | Metric contract | A blank chart or missing access is not a zero. Status flags (Projected, NotStatisticallySignificant) mean an estimate, not a final fact | 40, 42 | VERIFIED [R2,R12] |
| ST-04 | Metric contract | Aggregated pulls cannot give user-level analysis, intervals, power or sample sizes; say what extra measurement is needed instead of inventing them | 44, 470 | OPINION |
| ST-05 | Ratio traps | Identities for identical populations: total playtime = sessions x mean session length; per-player playtime = sessions per player x mean length; revenue per active = payer share x revenue per payer; total revenue = actives x payer share x revenue per payer. They describe composition, not cause | 50-55 | OPINION |
| ST-06 | Ratio traps | Sum counts and amounts, then divide. Do not average daily percentages. Summed DAU is player-days. Peak CCU is an instant maximum | 55 | OPINION |
| ST-07 | Ratio traps | Retention D7 and D30 are cohort-indexed specific return days, not "returned any time in the week" | 57 | VERIFIED [R3] |
| ST-08 | Ratio traps | Label a rolling-return metric separately; D1 non-return is not churn | 59 | OPINION |
| ST-09 | Question | State the causal question with population, change, control, outcome and horizon, cost, guardrail. One primary outcome; diagnostics explain, guardrails constrain; never pick the best metric after the result | 247 | OPINION |
| ST-10 | Question | Check what exposure the assigned player really gets; an assignment label alone does not fix the treatment. Players outside the randomized rollout are not a second control | 245 | OPINION |
| ST-11 | Power | Planning approximation per variant: n = 16 sigma^2 / delta^2 (95% confidence, 80% power, equal arms) | 253, 300 | VERIFIED [S1] |
| ST-12 | Power | Replacing 16 by 21 gives 90% power (attributed to S1 by the paper) | 253 | VERIFIED [S1] |
| ST-13 | Power | Source examples: over 409,000 per variant for a 5% revenue change, under 122,000 for a 5% conversion change. E-commerce examples, not Roblox needs | 255 | VERIFIED [S1] |
| ST-14 | Power | Take variance from a comparable pre-period or A/A data at the randomization unit; set delta in absolute units from the smallest worthwhile effect | 257 | OPINION |
| ST-15 | Power | Binary outcome: use a two-proportion procedure. Revenue: zero-heavy and long-tailed, simulate at player level. Clusters: include within-cluster dependence and count independent clusters. Record method, inputs, allocation, alpha, power, target | 257 | OPINION |
| ST-16 | Power | Prefer the native MDE for native results; if MDE exceeds the smallest worthwhile effect change the question, widen reach, extend inside a valid design or go qualitative. Never lower the evidence bar to get a significant result | 259 | OPINION |
| ST-17 | Power | Count unique eligible enrollees, not DAU x days; forecast from observed unique enrollment; outcomes mature after collection ends | 261 | OPINION |
| ST-18 | Duration | Duration must cover recruitment, weekly cycles, outcome maturity and the feature cycle; pre-register decision date, enrollment cut-off and outcome cut-off separately | 265 | OPINION |
| ST-19 | Duration | Microsoft's typical test is 7 days, with day-by-day inspection for novelty; a 28% click gain on a mail button decayed | 267 | EXPERIENCE [S3] |
| ST-20 | Duration | Moving from 7-day to 14-day scorecards increased standard errors in 17% of comparisons | 267, 341 | VERIFIED [S4] |
| ST-21 | Duration | "More days always means more certainty" is unsafe when populations or effects shift; Microsoft web practice does not override Roblox duration rules | 267, 479 | OPINION |
| ST-22 | Duration | Never compare an immature D7 or D30 cohort with mature ones; compare equal follow-up | 261, 620 | VERIFIED [R3] |
| ST-23 | Integrity | Microsoft flags SRM at p below 0.0005; a quality-control cut-off, not a success threshold, not Roblox's | 271, 302 | VERIFIED [S2] |
| ST-24 | Integrity | Check allocation, counts, persistence, logging parity, exposure, joins, baseline balance. A non-significant balance test does not prove randomization. Diagnose SRM; do not reweight or delete until the alarm clears | 271, 624 | OPINION/EXPERIENCE [S2] |
| ST-25 | Integrity | PlayFab: an analysis with SRM is untrustworthy. Its "significance means not due to chance" wording is looser than the ASA definition; use the precise reading | 484, 823 | VERIFIED [S7,S5] |
| ST-26 | Early harm | Roblox early-harm screen: first 24 h, 5-minute refresh, thresholds -10% playtime, -20% ARPU and payer conversion, whole interval beyond threshold, no call below 10,000 enrolled (thresholds are tool settings, not acceptable losses) | 273, 301 | VERIFIED [R11] |
| ST-27 | Early harm | No early-harm alert is not proof of safety or an early win. Stop on a verified severe defect as an operational stop, not an efficacy win | 275, 625 | OPINION |
| ST-28 | Stopping | Repeated ordinary p-value looks are not a sequential design. Use the declared horizon or a valid sequential method | 275, 623 | OPINION [S1,S3] |
| ST-29 | Stopping | A Bayesian analysis still needs a model, prior, stopping and decision policy and calibration; the label removes neither multiplicity nor bias | 275 | OPINION |
| ST-30 | Intervals | Show effect size and interval before significance: baseline, treatment, absolute, relative (if baseline allows), N, follow-up, guardrails. Keep percentage points apart from relative percent. Never build an interval from a rounded chart lift | 277 | OPINION |
| ST-31 | Intervals | A p-value is not the chance the result is wrong or the hypothesis is false. No p-value-only shipping rule. No clear effect is not proof of no effect: interval plus practical margin | 277, 303, 491, 622 | VERIFIED [S5] |
| ST-32 | Intervals | Roblox says ignore a non-significant change; the ASA warns against cut-off-only decisions. Keep the result and judge interval, margin, cost and design | 478 | OPINION |
| ST-33 | ITT | Prefer intention-to-treat: all correctly assigned eligible players | 279 | OPINION |
| ST-34 | Triggered | A triggered analysis is legitimate only if the trigger captures potential exposure equally in both arms and treatment does not cause it | 279 | OPINION [S2,S3,S5] |
| ST-35 | Post-treatment | Buyers after seeing a shop, finishers and event participants are post-treatment or self-selected groups; keep the eligible population | 279, 626 | OPINION [S2,S3] |
| ST-36 | Multiplicity | Keep exploratory device and tenure splits apart from predeclared ones; adjust multiple primary comparisons or validate in a new test; log every question tried | 279, 470 | OPINION [S5] |
| ST-37 | Multiplicity | Do not report only favourable metrics, segments or tests; keep the declared primary and the full history | 627 | VERIFIED [S5] |
| ST-38 | Guardrails | "No significant harm" is weaker than evidence that harm is under a margin. For a critical guardrail predefine a non-inferiority margin and power for it | 289 | OPINION |
| ST-39 | Verdicts | Five verdicts: useful improvement, harmful, inconclusive, no worthwhile effect within tested bounds, invalid (conditions: section 5) | 281-287, 580-583 | OPINION |
| ST-40 | Cluster | Individual randomization suits private UI; shared combat, trade, rewards and matchmaking need party, server or market clusters or a switchback with carryover control; native tool may not support it | 293 | OPINION |
| ST-41 | Custom tests | Need durable assignment, neutral eligibility and exposure, auditable outcomes. A server split that changes on rejoin is not a player experiment. Opt-in is self-selection. Historical controls are observational. Adaptive bandits do not give unbiased fixed-test estimates | 295 | OPINION |
| ST-42 | Updates | Write an update measurement brief before release; analyse who could receive the change | 307 | OPINION |
| ST-43 | Updates | Design ladder: concurrent randomized holdout; randomized staggered or cluster rollout; difference-in-differences; interrupted time series or synthetic control; matched before/after (descriptive) | 309-317 | OPINION |
| ST-44 | Updates | Bayesian structural time series builds a counterfactual when randomization is absent; it does not remove confounding. Backtest, placebo dates, alternative controls; never use an update-affected variable as control; flat pre-trend is not proof | 319 | VERIFIED+OPINION [S6] |
| ST-45 | Updates | Difference-in-differences = treated post-minus-pre change minus comparison post-minus-pre change; record level, rate or log scale; no credible untreated group means stay descriptive | 321 | OPINION |
| ST-46 | Updates | After rollout compare with the predicted range; a selected winner's point estimate will not repeat exactly | 335 | OPINION [S4] |
| ST-47 | Updates | Before/after is descriptive unless identification is stronger; no universal update-test length | 342 | OPINION |
| ST-48 | Three clocks | Keep calendar date, player age and time since first exposure apart; new updates change who arrives and who returns | 325 | OPINION |
| ST-49 | Three clocks | Compare new cohorts at equal follow-up; event participants are interest-selected, so participant vs non-participant return is not the event effect | 327 | OPINION |
| ST-50 | Reproducibility | No business number from prose: deterministic calculation, every number traces to a cell, query or formula; keep measured, calculated, estimated and opinion apart; full precision inside, one display-rounding rule | 464, 488 | OPINION |
| ST-51 | Reproducibility | Validate grain before joins; know sum, mean, ratio of sums, mean of ratios, percentile or distinct count; do not pool by averaging arm lifts | 466 | OPINION |
| ST-52 | Reproducibility | Detect leakage; bot and exploit exclusions by an auditable rule set with sensitivity; do not trim big spenders for significance; do not hide one extreme payer in an unqualified mean | 468 | OPINION |
| ST-53 | Process | 12-step process with a gate each; invalid and inconclusive are allowed outcomes | 443-461 | OPINION |
| ST-54 | Templates | Test plan: every field before exposure, "not available" is valid; plan states unit, smallest worthwhile benefit, guardrail margins, power plan, cluster adjustment, UTC enrollment and outcome end, SRM checks, ITT, multiplicity, stopping rule | 517-552 | OPINION |
| ST-55 | Templates | Result: verdict first; "invalid" when assignment or measurement fails even with an attractive uplift; table with absolute, relative, interval and method, N per arm | 556-583 | OPINION |
| ST-56 | Platform numbers | Native duration 14-60 days; below 1,000 DAU may struggle (read for context only; owner is note 01) | 299 | VERIFIED [R10] |

## 3. Fact-check table

| ST | Claim | AP | Checked against (codes in section 1; all read 2026-10-21) | Verdict | Corrected text or reason |
| --- | --- | --- | --- | --- | --- |
| ST-01 | Contract fields and unit list | 38 | No source claim to test; a checklist | unverified-kept-with-label | OPINION policy. Consistent with E2 section 3 and E1 section 3 (unit matters) |
| ST-02 | Sessions of one player are not independent; cites S1, S2 | 38 | E2 section 3.1-3.3 (naive variance too small: SE 0.00522 vs true 0.00895); E1 section 3 (k counts randomization units) | corrected | Principle is right. S1 and S2 do not say it; cite E2 (delta method for clustered or per-unit ratio metrics) and E1 |
| ST-03 | Blank is not zero; status flags are estimates | 40, 42 | M CA:185-186 (Projected "may change"; NotStatisticallySignificant "sample size is insufficient") | confirmed | Statistics part only; R2, R12 platform wording belongs to note 01 |
| ST-04 | Aggregates cannot support user-level intervals | 44, 470 | E2 section 2.2 (variance needs per-unit variances and covariance); E1 section 3 (h needs per-user moments) | confirmed | Follows from the formulas in section 4 |
| ST-05 | Four identities | 50-53 | Algebra; check numbers in F-13 | confirmed | Hold only for identical populations and scope, as the paper says |
| ST-06 | Sum first; summed DAU = player-days | 55 | Arithmetic, F-13 | confirmed | 10/100 and 30/1000: mean of percentages 6.5%, ratio of sums 3.636% |
| ST-07 | D7, D30 are cohort-indexed return days | 57 | M RT:24-33, 126 (cohort 06/20: D7 appears 06/27, D30 appears 07/20; "8th day") | confirmed | Mirror only. R3 is owned by note 01 |
| ST-08 | Rolling-return metric separate; D1 non-return not churn | 59 | Definitional advice | unverified-kept-with-label | OPINION |
| ST-09 | Question template, one primary | 247 | M PE:320 (write a hypothesis); S7 (hypothesis template); E14 (extra metrics inflate false positives: F-10) | confirmed | Consistent. The only fact is the multiplicity arithmetic |
| ST-10 | Assignment label is not exposure; non-enrolled are not a control | 245 | S7 (variants must be statistically equivalent, else selection bias); S2 (assignment-stage causes of SRM) | confirmed | Principle |
| ST-11 | n = 16 sigma^2 / delta^2, 95%, 80% | 253, 300 | E1 section 2.1 (equal arms, equal variance, alpha .05, power .8, rule cites Kohavi 2009; extract); derivation 2(1.959964+0.841621)^2 = 15.698 (F-01). S1 body not read | confirmed | Formula and assumptions confirmed by E1 and derivation. S1's own text, section and page unread. The 2007 KDD copy (slideshare extract) has another formula, n = (4 r sigma / Delta)^2, and larger examples (1.6 million revenue, about 486,000 conversion). Use the 2009 form; do not mix versions |
| ST-12 | 21 for 90% power, attributed to S1 | 253 | Derivation 2(1.959964+1.281552)^2 = 21.015 (F-01). E1 does not mention 21 | unverified-kept-with-label | Number is correct by math. That S1 prints it is unread. Say "21 (derived; 90% power)" and cite the math |
| ST-13 | 409,000 and 122,000 examples | 255 | Arithmetic F-01: 16x30^2/(0.05x3.75)^2 = 409,600; 16x0.0475/0.0025^2 = 121,600. Inputs (sd $30, mean spend $3.75, p 5%, relative 5%) seen only in secondary text (E18 quotes 121,600, delta 0.0025) | unverified-kept-with-label | Numbers reproduce from those inputs, but I did not read the paper's own statement of them. Keep "e-commerce example". The 5% is a relative change |
| ST-14 | Variance from pre-period or A/A; absolute delta | 257 | E1 section 2.1 (sigma common to both arms); E5 (bounds from the smallest effect of interest) | confirmed | Consistent |
| ST-15 | Binary: two-proportion; revenue: simulate; clusters | 257 | E11 (two-proportion formula); E13 (Kish design effect); E2 section 3; E1 section 4.4 | confirmed | Simulation for revenue is my inference (no source read says it); keep as advice |
| ST-16 | Prefer native MDE; do not lower the bar | 259 | M PE:314-316 (MDE from DAU, rollout, duration, split; under 1,000 DAU may struggle) | confirmed | Platform part owned by note 01 |
| ST-17 | Unique enrollees, not DAU x days | 261 | Logic; F-13 example | confirmed | A returning player is counted once as an enrollee but once per day in DAU |
| ST-18 | Duration needs and separate cut-offs | 265 | S7 (comparable periods, seasonal peaks; too short or too long both cost) | unverified-kept-with-label | OPINION; S7 supports only the first half |
| ST-19 | 7-day typical; 28% mail-button example | 267 | S3 extract (Microsoft typical test 7 days; clicks fell day over day, read as novelty) | confirmed | |
| ST-20 | 17% of comparisons | 267, 341 | S4 extract: 7-day to 14-day scorecards, standard error falls 83% and rises 17% of the time; sample = one month of ExP experiments, metrics significant at 7 days (p < 0.05), cumulative metrics excluded; unit of "of the time" not defined | corrected | Write: "in 17% of metric comparisons (restricted to metrics significant at day 7, cumulative metrics excluded) the standard error was larger at 14 days". AP:341 says "extensions": wrong word. The authors read it as week 2 drawn from a different population (their inference). The 14-day estimate fell outside the 7-day 3-sigma interval 4% of the time vs 0.3% expected |
| ST-21 | More days is not always more certainty | 267, 479 | S4 (above); M PE:34 (14-60 days), PE:322 (run full duration) | confirmed | Inference supported by S4 |
| ST-22 | Compare equal follow-up only | 261, 620 | M RT:33; arithmetic F-08 | confirmed | Reporting lag after the return day is not documented; see F-08 |
| ST-23 | SRM p below 0.0005 | 271, 302 | S2 extract: threshold p < 0.0005, called conservative, article dated 2020-09-14; S7 table row 3 days shows 0.0005; M PE:285-289 (Roblox gives no cut-off) | confirmed | Others use 0.001 (E17; Kohavi talk in E18, secondary). Make the cut-off a parameter (section 6) |
| ST-24 | Diagnose, do not reweight | 271, 624 | S2 extract (causes by stage: assignment, execution, log processing, analysis; "Don't trust" results until diagnosed; "missing users are rarely just some users"); E17 (do not adjust after the fact) | confirmed | Quote verified. "Non-significant balance test proves nothing" is a logical point (absence of evidence), not from S2 |
| ST-25 | S7 SRM untrustworthy; S7 p-value wording looser than ASA | 484, 823 | S7 page: "viewed as untrustworthy" present; the same page defines the p-value correctly in one place and says significance "determines" results are not due to chance in another | confirmed | Use the correct definition: the chance of a result at least as extreme if the null were true |
| ST-26 | Early-harm numbers | 273, 301 | M PE:245-266 (24 h, 5 min, -10%, -20%, -20%, 10,000, whole interval below threshold) | confirmed | Mirror only. The 2026-10-01 post was not read by me; note 01 owns it |
| ST-27 | No alert is not safety; operational stop | 275, 625 | M PE:251 (harm-only test: interval has an upper bound only), PE:255, PE:323 | confirmed | Statistics reading: a one-sided harm screen cannot show benefit |
| ST-28 | Repeated looks are not sequential | 275, 623 | E3 section 1 (Type I error can easily rise fivefold with continuous monitoring, about 10,000 samples); S3 extract (stronger significance levels for early results); S1 sequential text unread | confirmed | Cite E3 and S3; the S1 and "Application of S1" citation is unverified |
| ST-29 | Bayesian label changes nothing | 275 | E4 sections 1, 3, 6: posterior odds stay calibrated under optional stopping if prior odds are right and the rule uses only past data; frequentist Type I error is not controlled (table 1: 0.018 to 0.06) | corrected | Write: "A Bayesian reading needs a correct prior and a rule that uses only data seen so far; it keeps the posterior calibrated but not the frequentist false-positive rate. Choosing the best of many looks, metrics or segments still biases results" |
| ST-30 | Report set; pp vs relative; no invented intervals | 277 | S5 principle 5 (a p-value does not measure effect size); M PE:279 (Roblox shows an interval on percent change, e.g. +2.37%, bounds 0.55% and 4.19%) | confirmed | The interval level used by Roblox is not stated on the page |
| ST-31 | p-value not the chance of being wrong; no p-only rule; no effect not proven | 277, 303, 491, 622 | S5 via ScienceDaily extract: principle 2 (not the probability the hypothesis is true or data arose by chance), 3 (no decisions on a threshold alone), 5; E5 (a non-significant result cannot show no effect) | confirmed | Primary ASA PDF unreadable; principles read in the ASA release reprint dated 2016-03-07 |
| ST-32 | Roblox vs ASA | 478 | M PE:325 ("If a change isn't statistically significant, ignore it"); S5 principle 3 | confirmed | Both quoted correctly |
| ST-33 | ITT = all correctly assigned eligible | 279 | E6 extract: Microsoft uses "intended-to-treat population" for the affected, triggered group | confirmed | Naming clash: in Microsoft's article it means the triggered population. Say "all assigned eligible players" |
| ST-34 | Triggered analysis rule; cites S2, S3, S5 | 279 | E6 (trigger needs 100% recall of affected users, check SRM on the triggered scorecard, triggered-complement should look like an A/A); S2 (trigger condition as an SRM cause) | corrected | Rule is right. Cite E6 and S2; S3 and S5 do not say it. Add a check: SRM on the triggered set |
| ST-35 | Post-treatment selection | 279, 626 | S3 extract (segments that move with treatment, e.g. active days, mislead; use static ones); S2 (biased conditions when segmenting) | confirmed | |
| ST-36 | Exploratory vs confirmatory; log of tries | 279, 470 | S5 principle 4 (full reporting); E14 (FWER 1-(1-a)^m, Bonferroni, Holm) | confirmed | Numbers in F-10 |
| ST-37 | Do not report only favourable results | 627 | S5 principle 4 | confirmed | |
| ST-38 | Non-inferiority for critical guardrails | 289 | E5 (equivalence bounds from the smallest effect of interest; 90% interval inside bounds for alpha .05) | confirmed | F-12 |
| ST-39 | Five verdicts | 281-287 | E5 (bounds logic); M PE:279 (Roblox calls significance "interval excludes 0") | corrected | Definitions leave gaps (positive effect of uncertain size; benefit excluded but harm not). Use the threshold rules in section 5 |
| ST-40 | Cluster or switchback | 293 | E16 abstract (switchbacks, carryover, randomization-based tests); E13 (design effect) | confirmed | Whether native Experiments supports clusters is a platform question (note 01) |
| ST-41 | Custom-experiment cautions; bandits | 295 | E15 abstract (adaptively collected sample means are biased downward); S2 (easy self-assignment as SRM cause) | confirmed | The rest is logic |
| ST-42 | Update measurement brief | 307 | none | unverified-kept-with-label | OPINION |
| ST-43 | Design ladder | 309-317 | S6 sections 1-3 (control must be unaffected; stable relationship; spillover biases); E12 (parallel trends, composition, shocks) | confirmed | Order of the ladder is the paper's judgement |
| ST-44 | BSTS description and cautions | 319 | S6 via ar5iv: control series assumed unaffected (section 2), relationship assumed stable (section 1), model structure intact (section 3), spillover biases (section 2) | confirmed | Backtest and placebo-date advice is the paper's own, not stated in S6 as far as read |
| ST-45 | DiD arithmetic | 321 | E12: (treated change) minus (control change), Card-Krueger 0.59 - (-2.16) = 2.75 | confirmed | Scale warning is correct (F-09) |
| ST-46 | Winner's point estimate will not repeat | 335 | S4 extract (winner's curse overstates effects; extrapolating past tests mostly works) | confirmed | |
| ST-47 | Before/after is descriptive | 342 | S6 abstract (counterfactual model for when randomization is unavailable) | confirmed | No source gives a universal update-test length; none is invented here |
| ST-48 | Three clocks | 325 | S3 (date segments show novelty); S4 (week 2 is another population) | unverified-kept-with-label | OPINION framework |
| ST-49 | Cohorts, event self-selection | 327 | M RT:50 (cohort tables for events); S3 (self-moving segments) | confirmed | |
| ST-50 | Deterministic numbers, traceability | 464, 488 | S5 principle 4 | unverified-kept-with-label | OPINION studio policy |
| ST-51 | Grain, metric types, no averaging lifts | 466 | F-13 numbers; E2 (ratio of means vs mean of ratios) | confirmed | |
| ST-52 | Leakage, exclusions, trimming | 468 | E6 (Twyman's law, re-run on re-randomized users) | unverified-kept-with-label | OPINION practice |
| ST-53 | 12-step process | 443-461 | none | unverified-kept-with-label | OPINION |
| ST-54 | Plan template | 517-552 | none | unverified-kept-with-label | OPINION template; fields align with section 4 |
| ST-55 | Result template | 556-583 | S2, S7 (SRM makes results untrustworthy) | confirmed | Only the "invalid beats attractive uplift" rule is testable |
| ST-56 | 14-60 days; under 1,000 DAU | 299 | M PE:34, 316 | confirmed | Mirror only |
| ST-S1 | S1 metadata and quote | 799 | Springer abstract extract (abstract: power, sample size, variance reduction); search summaries for journal data only | unverified-kept-with-label | Body unread. Online date 2008-07-30 and the quoted sentence not verified |
| ST-S2 | S2 date, quote | 803 | S2 extract | confirmed | 2020-09-14; quote present |
| ST-S3 | S3 date, quote | 807 | S3 extract | confirmed | 2021-01-25. The exact heading is not checked; the content (static segments) is present |
| ST-S4 | S4 date, quote | 811 | S4 extract | corrected | 2024-11-20 confirmed. The paper's quote was not found as written; the extract says standard error "increases 17% of the time" (7 to 14 days). Use that wording |
| ST-S5 | S5 date, quote | 815 | ScienceDaily extract | confirmed | 2016-03-07; principle 4 wording present |
| ST-S6 | S6 citation, quote | 819 | research.google abstract; ar5iv | corrected | Annals of Applied Statistics 9:247-274 (2015) confirmed. Abstract says "in a synthetic control" inside the quoted sentence; the paper's quote drops it |
| ST-S7 | S7 date, quote | 823 | S7 page | confirmed | updated_at 2025-05-01; the quote is verbatim |
| ST-S8 | S8 date, quote | 827 | arXiv abstract | confirmed | Submitted 2017-01-04; sentence verbatim |

## 4. Formulas for the stats helper

Common: alpha two-sided 0.05 unless stated; z_p is the standard normal quantile. Stdlib hint (my inference): `statistics.NormalDist().inv_cdf` gives z; `math.erfc` gives chi-square (1 df) tails; Student t quantile and chi-square tails for df of 3 or more need a coded incomplete beta or gamma (or a library).

**F-01 Kohavi sample size per variant (means; equal arms, equal variance).** n = 2 sigma^2 (z_{1-a/2} + z_{1-b})^2 / delta^2. Constants: 2(1.959964+0.841621)^2 = 15.6978 (rule: 16); 2(1.959964+1.281552)^2 = 21.0149 (rule: 21). Rule: n = 16 sigma^2/delta^2 (80%), 21 sigma^2/delta^2 (90%). Units: sigma and delta in the metric's unit; n per variant. Check A: sigma = 30, delta = 0.05 x 3.75 = 0.1875: 16 x 900 = 14,400; delta^2 = 0.03515625; n = 409,600. Check B (Bernoulli, p = 0.05, delta = 0.05 x 0.05 = 0.0025): sigma^2 = 0.0475; 16 x 0.0475 = 0.76; delta^2 = 0.00000625; n = 121,600; at 90%: 21 x 0.0475 / 0.00000625 = 159,600; exact constant: 15.697757 x 0.0475 / 0.00000625 = 119,303. Smallest detectable difference: delta = (z+z) sigma sqrt(2/n); n = 10,000, sigma = 1: 2.801585 x 0.0141421 = 0.03962 (rule 4 sigma/sqrt(n) = 0.04). Unequal split with treatment share f: n_total = (z+z)^2 sigma^2 (1/f + 1/(1-f)) / delta^2; f = 0.5: 31.3955 sigma^2/delta^2; f = 0.2: x 6.25/4 = +56.25% total (E1 section 6.1). Skewed revenue: planning only (see F-14).

**F-02 Two-proportion sample size per group.** n = [ z_{1-a/2} sqrt(2 pbar qbar) + z_{1-b} sqrt(p1 q1 + p2 q2) ]^2 / (p1 - p2)^2, pbar = (p1+p2)/2, qbar = 1 - pbar (E11, equal groups; Fleiss, Tytun, Ury 1980 adds a continuity correction, not given here). Check: p1 = 0.05, p2 = 0.0525: pbar = 0.05125; 2 pbar qbar = 0.097246875, sqrt = 0.311844; p1q1 + p2q2 = 0.0475 + 0.04974375 = 0.09724375, sqrt = 0.311839; 1.959964 x 0.311844 = 0.611204; 0.841621 x 0.311839 = 0.262451; sum 0.873654; square 0.763272; / 0.00000625 = 122,123.4, so n = 122,124 (accept 122,123-122,125). Simplified pooled form (E1 Eq. 2): 2 pbar qbar (z+z)^2 / delta^2 = 0.097246875 x 7.848879 / 0.00000625 = 122,125. Kohavi rule gives 121,600 (0.4% lower). Relative-lift form (E1 Eq. 10-11, extract): n = (1/px^2 + py^2/px^4) pbar qbar (z+z)^2 / delta_rel^2 = 841 x 0.0486234 x 7.848879 / 0.0025 = 128,384.

**F-03 Difference of two proportions, interval.** d = p1 - p2. Wald: d +/- z sqrt(p1 q1/n1 + p2 q2/n2). Wilson per group (E9): centre = (p + z^2/2n)/(1 + z^2/n); half-width = z sqrt(p q/n + z^2/4n^2)/(1 + z^2/n); gives (l, u). Newcombe hybrid score, as coded in E10: L = d - sqrt((p1 - l1)^2 + (u2 - p2)^2); U = d + sqrt((u1 - p1)^2 + (p2 - l2)^2). Check 1, 56/70 vs 48/80: d = 0.2; Wald SE = sqrt(0.0022857 + 0.003) = 0.072703, interval (0.0575, 0.3425). Wilson 56/70: centre 0.784393, half 0.092560, (0.69183, 0.87695); Wilson 48/80: centre 0.595418, half 0.104964, (0.49045, 0.70038). Newcombe L = 0.2 - sqrt(0.108166^2 + 0.100382^2) = 0.2 - 0.147569 = 0.05243; U = 0.2 + sqrt(0.076953^2 + 0.109545^2) = 0.2 + 0.133873 = 0.33387. Check 2, Wilson 10/100: (0.0552, 0.1744). Check 3, where Wald fails, 2/50 vs 0/50: d = 0.04; Wald SE = sqrt(0.0384/50 + 0) = 0.027713, interval (-0.0143, 0.0943); Newcombe: Wilson 2/50 (0.01104, 0.13460), Wilson 0/50 (0, 0.07135), interval (-0.0370, 0.1346). Wald fails with small counts, rates near 0 or 1, a zero cell (that group adds no variance) and can leave [0,1]; its real coverage can fall under nominal even for large n (E9). Use Newcombe as default; test the helper against statsmodels `confint_proportions_2indep(method="newcomb")`. Safe for yes/no outcomes (payer conversion, D1), not for money amounts.

**F-04 Difference of means, Welch.** SE = sqrt(s1^2/n1 + s2^2/n2); df = (a+b)^2 / (a^2/(n1-1) + b^2/(n2-1)) with a = s1^2/n1, b = s2^2/n2 (E8); interval d +/- t_{df,1-a/2} SE (interval is the standard inversion of the E8 test: my inference). Check: n1 = 10, s1^2 = 4, n2 = 20, s2^2 = 9, d = 2: a = 0.4, b = 0.45; SE = sqrt(0.85) = 0.921954; df = 0.7225/(0.16/9 + 0.2025/19) = 0.7225/0.0284357 = 25.408; t(0.975) is 2.0595 at 25 and 2.0555 at 26 (standard table), about 2.0578 at 25.408; interval 2 +/- 1.8972 = (0.103, 3.897), tolerance 0.002 from the t interpolation.

**F-05 Relative vs absolute; percentage points.** Absolute = p_t - p_c (x100 = percentage points); relative = (p_t - p_c)/p_c. 0.05 to 0.0525 is +0.25 pp and +5%; "5%" is never "5 pp". Relative interval, independent arms, delta method (E2 Eq. 4; equal n per arm): (Ybar/Xbar - 1) +/- z sqrt(v/n), v = s_y^2/Xbar^2 - 2 Ybar s_xy/Xbar^3 + Ybar^2 s_x^2/Xbar^4, s_xy = 0. Check: n = 100,000 per arm, Xbar = 0.05, Ybar = 0.0525, s_x^2 = 0.0475, s_y^2 = 0.04974375: v = 19.8975 + 20.9475 = 40.845; v/n = 0.00040845; SE = 0.020210; interval 0.05 +/- 0.039611 = (0.0104, 0.0896). Unequal n: Var = s_y^2/(n_y Xbar^2) + Ybar^2 s_x^2/(n_x Xbar^4) (my extension). Relative change is undefined as the control mean nears 0.

**F-06 Ratio metric with user-level randomization (ARPPU, sessions per player, any ratio of sums).** R = sum S / sum N over k units; Var(R) = (1/(k muN^2)) (sigma_S^2 - 2 R sigma_SN + R^2 sigma_N^2) = sample variance of e_i = S_i - R N_i divided by k muN^2 (E2 section 3.2). Check: N = (2,4,1,5), S = (1,2,0,3): R = 0.5; e = (0,0,-0.5,0.5), s^2 = 0.5/3 = 0.166667; muN = 3; Var = 0.166667/(4 x 9) = 0.0046296; SE = 0.068041. ARPPU = revenue / payers has a random denominator, so it needs this form; ARPU (all active players) is a plain mean.

**F-07 SRM, chi-square goodness of fit.** chi2 = sum (O_i - E_i)^2 / E_i, E_i = N w_i, df = k - 1 (no fitted parameters, E7 with c = 1); p = upper tail. 2 arms: p = erfc(sqrt(chi2/2)); 3 arms (df 2): p = exp(-chi2/2). Checks (50/50; counts from the S7 table): 105 vs 100: chi2 = 2 x 2.5^2/102.5 = 0.121951, p = 0.7269 (S7 shows 0.7269); 1,050 vs 1,000: 1.219512, p = 0.2695 (S7: 0.2695); 10,500 vs 10,000: 12.195122, p = 0.00048 (S7 shows 0.0005; below 0.0005, so flagged at the Microsoft cut-off). 3 arms, counts 3,400/3,300/3,300, weights 1/3: chi2 = (66.667^2 + 33.333^2 + 33.333^2)/3,333.33 = 2.0, p = exp(-1) = 0.3679. Critical chi2 (1 df): 12.116 at p = 0.0005, 10.828 at 0.001, 3.841 at 0.05. A 50.5/49.5 split has chi2 = 0.0001 N, flagged at N above about 121,200. E7 gives no minimum expected count (a rule of 5 is common practice, not read here; use an exact binomial test for tiny counts). Counts only, so unaffected by revenue skew. Cut-off: parameter (section 6).

**F-08 Cohort maturity.** mature(c, N, asof, L) is true when date(c) + N days + L days is on or before asof, where asof = last fully closed UTC day of the pull ("finalized through"). Roblox shows the D7 point of cohort 06/20 on 06/27 and D30 on 07/20 (M RT:33). Check: c = 2026-06-20: N = 7 gives 2026-06-27; N = 30 gives 2026-07-20; with L = 1 the cohort is readable from 06-28 and 07-21. L is not documented anywhere I read: PROPOSAL L = 1 until the pull tool measures the real lag. Compare only cohorts that are mature at equal N.

**F-09 Difference-in-differences.** DiD = (T_post - T_pre) - (C_post - C_pre). Check: 0.59 - (-2.16) = 2.75 (E12). Scale matters: rates 0.10 to 0.12 treated, 0.10 to 0.11 comparison: level DiD = 0.02 - 0.01 = 0.01 (1.0 pp); ratio scale 1.20/1.10 = 1.0909 (+9.1%). Independent cells: SE = sqrt(sum of four cell SE^2) (my inference); four SE of 0.2 give 0.4; same players in pre and post need the covariance. Needs parallel trends, no differential shocks, stable composition (E12, S6 section 1).

**F-10 Multiplicity.** Family error for m independent tests: 1 - (1-a)^m: m = 2: 0.0975; m = 3: 0.142625; m = 6: 0.264908 (E14 gives 0.2649). Bonferroni: a/m (m = 3: 0.016667). Holm thresholds (m = 3): 0.016667, 0.025, 0.05, stop at the first failure. Without independence the bound is m x a.

**F-11 Cluster design effect.** Deff = 1 + (m - 1) rho; n_eff = n / Deff (E13; m = mean cluster size, rho = intraclass correlation). Check: m = 20, rho = 0.05: Deff = 1.95; 1,000 players are worth 512.8; 10,000 independent players per arm need 19,500 players = 975 clusters of 20 per arm. Unequal cluster sizes: use F-06 form (E2 section 3.2) instead.

**F-12 Non-inferiority guardrail.** Higher-is-better metric, margin M > 0: non-inferior if the lower bound of the interval for (treatment - control) is above -M (E5; TOST at alpha .05 uses the 90% interval). Check: d = -0.4 pp, SE = 0.3 pp: 90% lower bound = -0.4 - 1.644854 x 0.3 = -0.8935 > -1.0: non-inferior at M = 1.0 pp, not at 0.8 pp. Sample size with true difference 0 (my inference, same derivation): n = 2 sigma^2 (z_{1-a} + z_{1-b})^2 / M^2 = 12.365 sigma^2/M^2 (one-sided alpha .05, 80% power).

**F-13 Identities and aggregation checks.** 2,000 actives, 5% payers = 100, $4 per payer: total $400; per active 0.05 x 4 = $0.20 = 400/2000. 500 sessions x 12 min = 6,000 min; 200 players: 2.5 sessions x 12 = 30 min = 6,000/200. Days 10/100 and 30/1000: mean of percentages 6.5%, ratio of sums 40/1100 = 3.636%. DAU: player A active 3 days, B 1 day: summed DAU 4 player-days, weekly unique 2. Averaging lifts: +10% on base 100 and +2% on base 900: average 6%, pooled (10+18)/1000 = 2.8%. Enrollment: DAU 1,000 for 14 days is up to 14,000 player-days; unique enrollees are often far fewer.

**F-14 Safe for skewed revenue? (my assessment; no source read tests it)**

| Method | Zero-heavy, long-tailed revenue | Why |
| --- | --- | --- |
| F-01 | Planning only | Needs sigma^2 from a user-level pre-period including zeros; sigma^2 is itself unstable when a few payers dominate; the approximation assumes the sample mean is near normal. Check by player-level simulation or A/A bootstrap |
| F-02, F-03 | Safe, binary only | Use for payer conversion or retention, not amounts. Newcombe preferred |
| F-04 Welch, F-05 | Approximate | Valid for large n; coverage can be poor at modest n with a heavy tail. Validate on pre-period A/A data. Pre-declare any capping and apply it to both arms |
| F-06 | Approximate | Same large-n reliance; fixes the unit, not the tail |
| F-07 | Safe | Counts only |
| F-08, F-09 arithmetic | Safe as arithmetic | Interval quality follows the variance method used |
| F-10 to F-12 | Safe as arithmetic | Inputs inherit the above |

## 5. Verdict rules (all PROPOSAL until the lead locks them; the paper's table is corrected)

Inputs: theta = treatment - control, sign flipped so higher is better; interval [L, U] at 1 - alpha (default 95%, two-sided; its bounds are used as conservative one-sided bounds); b = smallest worthwhile benefit (> 0); h = harm margin (> 0); each guardrail g has [L_g, U_g] and margin m_g; flags: integrity_ok, matured, stopping_ok. With several primary comparisons use the adjusted alpha (F-10).

Evaluate in this order; first true wins.

| Step | Verdict | Condition a script can evaluate |
| --- | --- | --- |
| 0 | no verdict yet | matured is false (outcome window not complete: F-08) |
| 1 | invalid | integrity_ok is false: SRM p below the cut-off, assignment or logging failure, contamination flag; or stopping_ok is false (ordinary-p early stop with no valid sequential method) |
| 2 | harmful | U <= -h; or any guardrail with U_g <= -m_g; or a confirmed severe operational defect (report as operational stop) |
| 3 | useful improvement | L >= b and every guardrail has L_g > -m_g |
| 4 | no worthwhile effect within tested bounds | U < b and L > -h |
| 5 | inconclusive | none of the above; attach a reason: benefit unproven (L < b <= U), harm not excluded (L <= -h), guardrail not cleared (L_g <= -m_g) |

Boundaries: L = b is useful; U = b is not "no worthwhile effect"; U = -h is harmful; L = -h is not "no worthwhile effect". Looser option (the paper's wording is silent): useful if L > 0 and point estimate >= b; Roblox's own "significant" is only that the interval excludes 0 (M PE:279). Strict is the default because the owner wants no result called real too early.

Corrections to the paper: (1) "inconclusive" is defined as permitting both benefit and harm; the real residual includes a positive effect of unknown size and a case where benefit is ruled out but harm is not. (2) It has no state for immature outcomes; use step 0. (3) A fixed-horizon or valid sequential rule must hold for steps 2 to 4 to count (ST-28).

Test vectors (b = 2.0, h = 1.0, integrity and guardrails fine unless noted):

| Interval [L, U] | Verdict |
| --- | --- |
| [2.5, 4.0] | useful improvement |
| [2.0, 3.0] | useful improvement (L = b) |
| [0.5, 3.0] | inconclusive: benefit unproven |
| [1.0, 5.0] | inconclusive strict; useful under the looser option |
| [-0.5, 1.5] | no worthwhile effect |
| [-1.5, 1.0] | inconclusive: harm not excluded |
| [-3.0, -1.0] | harmful |
| [-2.0, 3.0] | inconclusive |
| [2.5, 4.0], one guardrail [-1.2, 0.3] with m_g = 1.0 | inconclusive: guardrail not cleared |
| any interval, SRM p = 0.0001 | invalid |
| any interval, cohort not mature | no verdict yet |

## 6. Disagreements and the paper's "where sources differ" table, checked

| Item | What the sources say | Resolution |
| --- | --- | --- |
| Nonsignificant results (AP:478) | M PE:325 says ignore them; S5 principle 3 warns against cut-off-only decisions | Paper's resolution stands (ST-32). Report the interval and the margin |
| Test duration (AP:479) | S3: typical 7 days; M PE:34: 14-60 days; S4: week 2 may be another population | Paper's resolution stands (ST-21). Neither is a universal length |
| SRM cut-off | S2: p below 0.0005; E17 vendor docs: below 0.001 (Kohavi talk in E18 says 0.001, secondary); Roblox: none published; S7 table row of p = 0.0005 at 3 days is an illustration | Make `srm_p_threshold` a parameter, default 0.0005 (read in primary S2, matches the paper); always print p and the threshold; the lead may choose 0.001 |
| Kohavi formula | 2009 form 16 sigma^2/delta^2 (via E1, E18); 2007 KDD copy (slideshare extract): n = (4 r sigma/Delta)^2 and larger examples | Use the 2009 form with exact constants available (F-01) |
| ITT naming | Paper: all assigned eligible. E6: "intended-to-treat" means the triggered group | Say "all assigned eligible players" and name the triggered set apart |
| Bayesian stopping | Paper: label does not remove bias. E4: posterior stays calibrated under optional stopping with correct prior, frequentist error does not | Corrected wording at ST-29 |
| PlayFab wording | S7 defines p correctly once and loosely elsewhere | Paper's point stands (ST-25) |
| Rows AP:480-482 | Playtime vs enjoyment, telemetry vs observation, "test everything" vs restrained | Cite R19, I3, I4, I6, I8, I10, I1: outside this ticket, not checked |

## 7. Dropped claims with reasons

No AP claim is dropped outright. Items I met and refused to carry into the helper or skills:

| Item | Why |
| --- | --- |
| "Tens of thousands minimum, 200,000+ for mature programs" (a skills page I opened, not the paper) | Universal minimum sample; no scoped source |
| "n of at least 355 x skewness^2 for normal means" (my recollection) | Source not read; unverified |
| "Daily peeking for two weeks lifts 5% error to about 17%" (GrowthBook blog) | Secondary; use E3's "can easily rise fivefold" instead, sourced to the arXiv text |
| Paper-input numbers for S1 (sd $30, mean $3.75) as source facts | Seen only in secondary text; kept as arithmetic check values, not as claims about S1 |
