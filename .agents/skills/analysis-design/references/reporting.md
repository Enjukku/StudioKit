# Reporting: one finding a non-expert owner can act on

> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `analysis-design`. Sources: owner brief J013 (2026-10-21: "one main finding, the evidence, how sure it is, and one recommendation, in plain words. I am not a data expert."); owner's analyst paper (AP) §9, §10.1, Appendix D, fact-checked in `knowledge/reference/analyst/03-practice-diagnosis-reporting.md` (PR, C ids; §5 plain wording); `rules/owner-profile.md`; `ste-writing`. Tags: **V** documented · **E** reported · **O** practice.

## 1. The answer shape (every owner-facing answer)
| Part | Rule | Example shape |
| --- | --- | --- |
| **What happened** (one finding) | one sentence: which players, what changed, how much, compared with what. A decision-relevant finding, not a dashboard tour | "New phone players came back the next day less often this week: 1 in 6 instead of 1 in 5." |
| **Why we think so** (evidence) | counts, the comparison and its basis, what we ruled out. Every number traces to a pull or a calculation | "Of 4,120 new phone players (Oct 6-12), 690 returned; the week before, 870 of 4,300. Computers did not change. The new tutorial went live Oct 6." |
| **How sure we are** | High / Medium / Low + one line of reasons: are the numbers right, is the sample big enough, was it a fair test. Never a made-up percentage | "Medium: the drop is bigger than normal week-to-week movement, but we only compared weeks; we did not run a test." |
| **What we recommend** (one action) | action + who + which players + how we will know it worked + review date | "Game designer: check step 3 of the tutorial on phones. Success: D1 for phone players back above 1 in 5 for the Oct 20-26 cohort. Review Oct 29." |
| **Your decision** | the choice, or "none" | |

Part 1 stays short: about 25 lines at most; the rest goes to Part 2. **Part 1 never shows a hypothetical, example or made-up number** (not even labelled): to explain a mechanism, say it in words ("if fewer people buy, revenue can fall even when each buyer pays more") and put any worked example in Part 2, marked hypothetical in the text and in its saved file. Dates that rest on a PROPOSAL lag say "about". No tool, model or effort names in Part 1.

**Two causes stacked** (for example a player-mix change and a defect): it is still one finding. Name the bigger part first, say which part the game owns, give the split as a labelled estimate (`analytics.py stats mix`), and point the one recommendation at the part we can act on. Say what the fix will not bring back.

(O, AP:414; PR-RP01..03.) If we know where but not why: "We found where players are lost; we have not found why." Never relabel a judgment as a verified cause (O, AP:416).

### How sure: three separate questions (O, AP:416)
1. **Are the numbers right?** (measurement: finished data, stable definitions, no breaks, totals reconcile)
2. **Do we know why?** (cause: a fair test > a strong comparison > before/after > a story that fits)
3. **Is acting worth the risk?** (value: a cheap, reversible fix can be right on modest evidence; a costly redesign needs strong evidence)

| Level | Use when |
| --- | --- |
| High | numbers verified and mature; enough players that normal movement cannot explain it; a valid test or a strong design rules out the main alternatives |
| Medium | numbers verified; the change is clear, but the cause rests on a comparison, not a test, or one alternative is still open |
| Low | small numbers, immature cohorts, a measurement break, or several explanations still fit |

## 2. Plain words (owner messages also follow `ste-writing`)
| Do not write | Write |
| --- | --- |
| denominator, unit, window, population | what we counted, out of whom, which days, which players |
| statistically significant / p-value | "bigger than normal week-to-week movement" plus the range; never "the chance we are wrong" |
| confidence interval | "likely range: between X and Y" |
| causal ladder | "it happened" (we saw it) · "linked to" (we compared groups) · "caused" (only after a fair test) |
| non-completers, censoring | "we counted players who did not finish too; 'not yet' is not 'never'" |
| immature cohort | "too early to read: these players have not had 7 days yet" |
| cohort | "the group of players who first played on <date>" |
| mature | "has had its full <N> days" |
| percentage points vs percent | "from 20% to 18% = 2 points lower (a tenth fewer players)" — say both |
| theme rate | "how many people raised it, out of how many we heard from, here, these days" |
| attribution ≠ incrementality | "the source that gets credit for a player may not be what brought them" |
| exploratory segment | "a lead: we looked through many splits, so this one may be chance; we test it again before acting" |
| measurement break | "Roblox changed how it counts this on <date>; numbers before and after do not compare" |

Rates always come with counts. Small numbers as "1 in 6" plus the percentage. Units on every number (minutes, Robux, players). One rounding rule per report; keep exact values in the files (O, AP:464).

## 3. Who needs what (routing)
| Recipient | Needs | Boundary (what the analyst does not do) |
| --- | --- | --- |
| owner (creative director) | the main change, the player and business impact, how sure, one decision | no combined score that hides a trade-off |
| game-designer | the affected journey and the likely understanding or gameplay mechanism | diagnosis supports design; it never dictates a redesign |
| progression-designer | the time, attempt or affordability bottleneck and the affected cohort, with non-finishers | no global pacing change from survivors alone |
| marketing | source quality, promise match, mature cohort value by source | credit for a source is not proof it caused the players |
| live-ops-designer | event reach, use, displacement of normal play, return after the event | a launch spike is not lasting engagement |
| engineering | the logging gap, broken event or performance regression, with evidence | never writes the logging code |

(O, AP:418-424.) The analyst owns the evidence; each role owns its fix (E, Ubisoft research lead, C26).

## 4. Charts that earn their place
| Question | Chart |
| --- | --- |
| do players come back? | cohort heatmap (same age across cohorts; immature cells blank and labelled) |
| when did it change? | time series with release, event and measurement-break markers; raw points visible under any smoothing |
| which devices or sources? | small multiples on the same axes |
| where are players lost? | funnel bars showing counts and rates |
| how spread out is it? | distribution or cumulative curve (sessions, progress, spend) |
| is the economy healthy? | source/sink flows (only if they reconcile) + wallet distribution |
| did the test work? | effect with its likely range, against the smallest worthwhile effect and harm margin |

Never: two y-axes suggesting a link; an average alone for skewed data; a cumulative curve that hides a stalled daily rate; a cut axis without saying so; overlapping rolling windows read as repeated proof. Caption = the finding and its limit, not the axis names. Every chart shows counts, units, dates, maturity and missing data (O, AP:430-432). Chart craft: the `dataviz` skill. Creator Hub custom dashboards (up to 20, saved on Publish) can hold a small owner view and a diagnostic view (V RF-54).

## 5. Integrity rules for an AI analyst (O, AP:464-470; PR-AI01..05)
- **No number from writing.** Every reported number resolves to a pull record, a `analytics.py stats` output or a formula shown. Keep measured, calculated, estimated and opinion apart.
- **Check the grain before any join**: a purchase joined to many event rows multiplies revenue. Know whether each metric is a sum, mean, ratio of sums, mean of ratios, percentile or distinct count. Never average arm lifts.
- **Keep absent, zero, unfinished, filtered and not-final apart.**
- **No leakage**: explain an outcome only with facts known before it; subgroups for a causal claim use before-treatment attributes.
- **Exclusion rules** (bots, exploits) are set before seeing results; show the result with and without them when it matters. Never trim big spenders to get significance; never let one huge payer vanish inside an average.
- **Record every question tried**, not only the ones that looked good. A newly found segment is a lead.
- **Without raw data, never invent** intervals, power or sample sizes from aggregates that cannot support them.
- AI makes analysis easy for everyone, which is why a fixed review shape matters (E, Supercell, C06). The quality target is an auditable decision, not a number of reports or tests.
