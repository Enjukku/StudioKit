---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J011-T03, Progression_Designer_Research_2026.txt lines 440-727"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Progression paper part 3: economy accounting, Roblox platform rules, tools and simulation, player-data diagnosis, hand-off, process, checklist (lines 440-727)

Paraphrased notes. The paper (PP) stays outside git. Every row cites `PP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 11 for the fact-check pass. The only checks I ran are arithmetic hand checks (section 10, marked extractor). I had no web access. The paper's research cut-off is 2026-10-21 (PP:5, lookup). Paper section numbers: 7 Economy and Roblox platform constraints (PP:440), 8 Tools and reproducible simulations (PP:488), 9 Diagnose progression with player data (PP:539), 10 Hand approved data to engineering (PP:603), 11 The progression designer process (PP:620). Parts 1 and 2 of this series are `01-cases-shapes-curves.md` and `02-incremental-rpg-rewards.md`.

## 0. How to read

| Key | Meaning |
| --- | --- |
| PP:n | Line n of `Progression_Designer_Research_2026.txt`. One paragraph = one line. Source register = PP:728-1310. Heading lines count as lines. |
| Tag | VERIFIED (a source publishes the rule or number; for the paper's own algebra it means "derived", see Z01). EXPERIENCE (a studio or designer's account). OPINION (the paper's own proposal, source O00, 2026-10-21, "not an external empirical source": PP:730). Tags are the paper's, copied unchanged. Paragraphs the paper leaves untagged say "untagged". Where one paragraph mixes tags, each part is split and marked. |
| Src | Paper source id with date. "acc. 2026-10-21" = undated living documentation, accessed 2026-10-21 (register wording, PP:1048 and others). Access is not a publication date. |
| (extractor) | Anything I added: a variable definition, unit, domain, hand calculation, cross-reference or issue. Not paper text. |
| Row IDs | EA accounting, EI industry case, RP regional pricing, RC Roblox compliance, ET section 7 rule-table row, TL tools, SM simulator spec, NP numeric precision, TT section 8 rule-table row, DB behaviour interpretation, DR retention and benchmarks, DI instrumentation, DM diagnostic-matrix row, DX experiments, DT section 9 rule-table row, HO hand-off, HT section 10 rule-table row, PS process step, PC check or pass, PT section 11 rule-table row, CK checklist row, DN don't, OQ open question, MB math boundary, EB evidence boundary, FM formula card, HC hand check, RB Roblox claim, OT other claim, S source, X limit, Z possible issue. |
| Formulas | Plain text. `×` multiply, `^` power, `ceil()` round up, `floor()` round down, `log` natural or any one base (a ratio of logs is base-free), `max`, `min`. Every variable is defined in section 9. |
| Quotes | At most a few, each under 15 words, only in sections 13 and 14, attributed to the register line. |

Coverage map

| Paper part | Where here |
| --- | --- |
| 7 Economy and Roblox platform constraints PP:440-486 | section 1 |
| 8 Tools and reproducible simulations PP:488-537 | section 2 |
| 9 Diagnose progression with player data PP:539-601 | section 3 |
| 10 Hand approved data to engineering PP:603-618 | section 4 |
| 11 Process, conservation check, passes PP:620-651 | section 5 |
| Review checklist PP:653-672 | section 6 |
| Do not do PP:674-694 | section 7 |
| Open questions, math boundaries, tool evidence boundaries PP:696-726 | section 8 |
| Formula cards, hand checks (extractor) | sections 9, 10 |
| Claims to fact-check (a), sources (b), limits (c), possible issues (d) | sections 11-14 |

## 1. Economy and Roblox platform constraints (paper section 7, PP:440-486)

### 1.1 Accounting: ledger, identity, price index, affordability (PP:442-450)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| EA1 | 444 | OPINION | Treat a currency as a ledger with a purpose, not a number that must rise. Specify per currency: earning activities, recurring and one-time expenditures, transfer rules, storage restrictions, premium conversions, intended purchasing power at each progression tier. In analysis, keep earned currency, premium-purchased currency and promotional grants separate even if the player's wallet merges them. Analytical recommendation only; not evidence that several visible currencies improve a game. | R01, acc. 2026-10-21; R02, acc. 2026-10-21 |
| EA2 | 446 | VERIFIED: accounting identity | For a closed population and a currency with no omitted adjustment: B(t+1) = B(t) + S(t) − K(t) (FM1). Player-to-player transfers cancel in the population total. A transaction tax does not cancel. If the observed population changes, add balances entering or leaving it and explicit administrative corrections. Derived bookkeeping, not an empirically optimal economy. | Author derivation, 2026-10-21 (O00); implementation categories R01 |
| EA3 | 448 | OPINION | Keep currency inflation apart from item abundance, intentional exponential progression and rising nominal rewards. Fixed-basket price index P(t) (FM2): same items, same quality, same base quantities in both periods. Analyst-defined, not a Roblox metric. Track executed trade prices, volumes and availability; seller listings alone can reflect unsold or manipulative offers. | Author analytical proposal and derivation, 2026-10-21 (O00) |
| EA4 | 448 | OPINION | If prices are designer-fixed, watch affordability instead: required active earning time T = max(0, C − B) / r (FM3) for a constant net earning rate r > 0. If earning changes over time, solve the cumulative-earnings integral; do not divide by a misleading average. | Author, 2026-10-21 (O00) |
| EA5 | 450 | VERIFIED / disagreement (first part) | Roblox economy documentation recommends net sources minus sinks near zero, and adding sinks when balances rise. Its dashboard exposes source/sink categories and average wallet balances. | R01, acc. 2026-10-21 |
| EA6 | 450 | OPINION (second part) | Do not raise that recommendation to an accounting law or a universal progression target. In a growing population, or an incremental game that deliberately accumulates wealth, positive net flow can be intended. A stable aggregate can hide poor newcomers and very rich veterans. Before tightening rewards, inspect wallet percentiles, tenure, progression tier and attainable purchase times. The paper says the disagreement is about the scope of a heuristic, not about the ledger identity. | O00 (no id cited in the paragraph) |

### 1.2 Industry evidence and premium fairness (PP:452-462)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| EI1 | 454 | EXPERIENCE | Supercell's Clash of Clans update of 6 October 2025: removed Town Hall weapon upgrade levels at TH12-TH15 (stated reason: they slowed midgame progression); moved 15 hero levels from TH15 to TH14 (five each for three heroes); changed loot incentives; reduced Loot Cart recovery from 20% to 10%. Documented interventions, not published causal retention gains. | R03, 2025-10-06 |
| EI2 | 456 | OPINION | Warning against reading one reward cut as the whole change. Model the combined effect of costs, reward rates, available activities, storage and unlock prerequisites. Removing grind at one gate can coexist with a smaller recovery source elsewhere. Do not copy the percentages into a Roblox project: they describe one game's economy and its accompanying changes. | R03, 2025-10-06 |
| EI3 | 458 | EXPERIENCE | Supercell extended Clash of Clans local-cost pricing to more than 100 countries and restricted lower-price-region donations to higher-price regions. Described by Supercell as accessibility and fairness choices; no controlled fairness or retention result published. | R04, 2025-08-21 |
| RP1 | 460 | VERIFIED | Roblox Managed Pricing adjusts eligible item prices using economic-location signals, not simply account location. | R05, acc. 2026-10-21 |
| RP2 | 460 | VERIFIED | Documented regional bounds: 30%-100% of the creator's default price (FM14). | R05, acc. 2026-10-21 |
| RP3 | 460 | VERIFIED | GetUsersPriceLevelsAsync supports checks on item transfers between price levels. The documentation gives gift and trade restrictions as examples, not one compulsory universal transfer design. | R05, acc. 2026-10-21 |
| RP4 | 462 | OPINION | Premium fairness needs a creative-director decision on what payment may bypass: cosmetic expression, convenience, content access, waiting or competitive power are different propositions. Show the real purchase price and the grant. Keep a viable intended nonpaying route. Measure nonpayer completion and competitive outcomes separately. "Legal", "available through the API" and "fair" are not synonyms. A higher ARPPU does not show the remaining audience has a better game. | Author recommendation, 2026-10-21 (O00); contrasting pricing practices R04-R05 |

### 1.3 Roblox compliance boundary (PP:464-478). Section heading says: not legal advice

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| RC1 | 466 | VERIFIED | Paid random items = rewards bought directly with Robux, or indirectly through currency bought with Robux. | R06, acc. 2026-10-21 |
| RC2 | 466 | VERIFIED | Current policy: before purchase, show all possible final outcomes and the actual numerical probability percentages. Outcome probabilities total 100%, "subject to its stated rounding-display treatment" (the paper does not state that treatment: Z08). | R06, acc. 2026-10-21 |
| RC3 | 466 | VERIFIED | A paid luck modifier must explain its numerical effect and show the updated odds while it is active. | R06, acc. 2026-10-21 |
| RC4 | 466 | VERIFIED | A free, gameplay-earned random reward is treated differently (the paper does not say how). | R06, acc. 2026-10-21 |
| RC5 | 468 | VERIFIED | PolicyService:GetPolicyInfoForPlayerAsync returns ArePaidRandomItemsRestricted and IsPaidItemTradingAllowed. | R06, acc. 2026-10-21 |
| RC6 | 468 | VERIFIED | A restricted user cannot use the paid random generator. A user not allowed paid-item trading must not reach trading of the relevant paid items. | R06, acc. 2026-10-21 |
| RC7 | 468 | VERIFIED | Documented alternatives: earnable access, disclosed deterministic sequences, guaranteed direct purchases, or removal/blocking. | R06, acc. 2026-10-21 |
| RC8 | 470 | OPINION | Use the returned eligibility; do not infer it from a guessed age or a static country list. Keep origin metadata when paid currency, free currency and paid-item rewards interact. Renaming the intermediary token does not make a paid random outcome free. If the eligibility call fails, treat restricted features conservatively until handled; never grant by default. | R06-R07, acc. 2026-10-21; engineering recommendation |
| RC9 | 472 | VERIFIED (first sentence only; paragraph tagged "VERIFIED / OPINION distinction") | Roblox illustrates a 10-Robux draw with 5% odds by showing a 200-Robux guaranteed alternative. A policy example, not proof of fair intrinsic value. | R06, acc. 2026-10-21 |
| RC10 | 472 | Author mathematical derivation and interpretation (paragraph tag as RC9; derivation source is the paper) | Independent constant-probability trials, no pity: expected spend to first success is c/p (FM4); chance of success within n tries is 1 − (1 − p)^n (FM5). Spending the expected amount is no guarantee. Calling c/p the uniquely fair direct price is unsupported. For fixed 0 < p < 1 and target 0 < q < 1, the least attempt count is n_q = ceil(log(1 − q) / log(1 − p)) (FM6). Not valid unchanged for pity or changing probabilities: model the actual conditional failure probabilities and their product. | Author, 2026-10-21 (O00) |
| RC11 | 474 | VERIFIED | Roblox younger-audience guidance requires PolicyService checks and discourages urgent or pushy sales language aimed at minors. Eligibility depends on location, age and platform. | R07, acc. 2026-10-21 |
| RC12 | 474 | VERIFIED | The June 16 global Kids/Select launch introduced further game reviews for under-16 access. | R08, 2026-06-16 |
| RC13 | 474 | VERIFIED | Age-checked users aged 5-8 generally have Kids accounts; users aged 9-15 have Select; regional variation exists. | R08, 2026-06-16 |
| RC14 | 474 | VERIFIED | Linked parents can set spending and screen-time limits until age 13. | R08, 2026-06-16 |
| RC15 | 474 | OPINION | A progression route must not assume every young player can buy, chat, trade or play a long continuous session. Kids/Select membership is not a substitute for individual purchase and trading policy checks. | R06-R08 |
| RC16 | 476 | VERIFIED | Advertising Standards, updated October 9, 2026, prohibit personalized ads to under-18s. | R09, 2026-10-09 |
| RC17 | 476 | VERIFIED | Rewarded video must use Roblox's product and is for users 13+. Rewards must be predetermined, not chance-based; clear disclosure; affirmative opt-in; immediate delivery after completion. | R09, 2026-10-09 |
| RC18 | 476 | VERIFIED | Video must not be forced as a progression gate. | R09, 2026-10-09 |
| RC19 | 476 | VERIFIED | Users under 13 must not be rewarded for engaging with advertising. | R09, 2026-10-09 |
| RC20 | 478 | OPINION | Do not merge "no paid-random restriction returned" with "rewarded random ad prize permitted": different policies. Do not describe every ad format as uniformly forbidden to under-13s: the standards separate ad integrations and age-restricted categories. These are platform requirements, not country-by-country legal advice or assurance of compliance. Recheck the official pages before launch. | R06-R09 (R09 2026-10-09; others acc. 2026-10-21) |

### 1.4 Section 7 rule table (PP:480-486; columns: rule, formula or number, evidence mark, source and date)

| ID | PP | Rule | Formula or number | Evidence mark | Source and date |
| --- | --- | --- | --- | --- | --- |
| ET1 | 481 | Reconcile currency flows before balancing | B′ = B + S − K, plus boundary adjustments | VERIFIED derivation | Author, 2026-10-21; R01 |
| ET2 | 482 | Diagnose affordability, not only wealth | T = max(0, C − B) / r when r is constant | OPINION metric; VERIFIED algebra | Author, 2026-10-21 |
| ET3 | 483 | Do not copy one economy's intervention | Loot Cart 20% → 10% amid broader changes | EXPERIENCE | R03, 2025-10-06 |
| ET4 | 484 | Separate regional price accessibility from arbitrage | Documented price range 0.30P to P | VERIFIED | R05, acc. 2026-10-21 |
| ET5 | 485 | Disclose paid-random outcomes and use eligibility | Outcome probabilities total 100%; two policy flags | VERIFIED | R06, acc. 2026-10-21 |
| ET6 | 486 | Never force a rewarded ad as a progression gate | 13+; predetermined reward | VERIFIED | R09, 2026-10-09 |

## 2. Tools and reproducible simulation (paper section 8, PP:488-537)

### 2.1 Spreadsheets versus simulators; smallest model; statistics (PP:490-504)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| TL1 | 490 | EXPERIENCE | Spreadsheets are a documented professional tool, not a beginner workaround. The GDC 2025 spreadsheet microtalks describe: Lauren Scott's shared progression scheme for Psychonauts 2; Guillaume Pierre's time/space/money/progression model for Cityscapes: Sim Builder; Retora's spreadsheet content pipeline for Merchant Guilds. Reported project practice, not comparative proof that one tool makes better games. | W01, 2025 (GDC event year; session date not established) |
| TL2 | 492 | EXPERIENCE | David Morris of Spryfox described detailed metagame simulation and analysis before the final metagame was built. Supports simulating interacting systems when a static curve is not enough; the public abstract gives no audited accuracy benchmark. | W02, 2019 (GDC event year) |
| TL3 | 494 | OPINION, recommended workflow | Use Excel or Google Sheets for parameters, inspectable formulas, charts and stakeholder comparison. Use a small deterministic Python or Luau simulator for branching purchases, unlocks, caps, resets and player strategies. Export CSV for flat tables and a structured format such as JSON for nested rules. Proposed tool choices, not a claim that the cited studios used this stack. Keep one explicit balance-data revision in every tool. The creative director approves goals and trade-offs, not thousands of cells. | Basis W01-W02 (2025; 2019) |
| TL4 | 498 | EXPERIENCE | Schreiber separates exhaustive enumeration (exact answer for a finite modeled outcome space) from Monte Carlo sampling (estimate from repeated random trials). His introductory article uses Excel as one sampling tool. | W03, 2010-07-28 |
| TL5 | 500 | OPINION, proposed decision rule | Order: algebra for deterministic formulas; enumerate a small finite state space when feasible; state-transition or event simulator when action order matters; Monte Carlo only for real stochastic inputs. One seeded path is a reproducible example, not a distribution. A strategy simulator with no random inputs needs no random repetition. | Basis W03 (2010-07-28), W02 (2019) |
| TL6 | 502 | VERIFIED, statistics | NIST gives Wilson and exact binomial confidence-interval methods and warns that normal approximations can be inadequate with very few failures or small samples. | W05, undated; acc. 2026-10-21 |
| TL7 | 504 | OPINION, reporting requirement | For a simulated failure proportion, declare before choosing the run budget: the trial, the independence assumption, the sample size, the interval method and the decision precision wanted. Use a fixed predeclared analysis point or a justified sequential method; do not stop whenever a conventional interval looks favorable. Report uncertainty separately from sensitivity to the behavior model. No justified universal count such as 1,000 or 10,000 players. No number of replications shows the assumed purchasing policy describes real people. | Statistics W05 (acc. 2026-10-21); model choice author recommendation (O00) |

### 2.2 Minimum simulator specification, policies, contracts (PP:506-514)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| SM1 | 508 | OPINION, original specification | State kept explicitly: currency balances; owned production; equipment; unlocked content; quest state; inventory and storage limits; prestige state; lifetime-earned counters; active elapsed time; calendar time. | Informed by W02, 2019 |
| SM2 | 508 | OPINION | Declare event order, e.g. produce → receive rewards → apply caps → purchase → unlock → reset, or whatever the design needs. That order is illustrative, not prescribed. The requirement: spreadsheet, simulator and shipped implementation agree. | W02, 2019 |
| SM3 | 510 | OPINION | Each virtual-player policy gets a name and assumptions. Listed policies (8): (1) cheapest eligible purchase; (2) greatest immediate production gain per cost; (3) save for a named unlock; (4) hoard; (5) spend on cosmetics; (6) explore rather than optimize; (7) struggle in combat; (8) return after an absence. | W02, 2019; W04, 2010-08-25 |
| SM4 | 510 | OPINION | Do not call a greedy return-on-investment heuristic "optimal" without proof it reaches the chosen objective fastest. Simulate paid and unpaid routes separately when both exist, without treating spending as necessary to progress. Policies are stress scenarios until observed behavior supports their frequencies. | W02, 2019; W04, 2010-08-25 |
| SM5 | 512 | OPINION, dimensional contract | Every formula needs units and a time basis. currency / (currency / active-second) gives active seconds only while the earning rate stays constant. If a purchase changes production, integrate the separate intervals or advance to each event. Calendar time also needs a session/absence model. Missing amount D > 0 with zero earning rate: the wait is unreachable under that state, not zero and not a division-error value. A cap below the requirement with no reachable cap upgrade: report a blocked path. The formulas are definitions and deductions under stated assumptions, not measured player pacing. | W02, 2019 |
| SM6 | 514 | OPINION, offline contract | Specify: eligible elapsed time, cap, production snapshot, active boosts, storage capacity, automatic purchases, daily-reset timezone, claim conditions, clock source. Tests: claim before, at and after the cap; a reset at a day boundary; an absence spanning a balance update. Illustrative frozen-rate rule offlineReward = rateAtExit × min(max(elapsed, 0), offlineCap) (FM7), then a documented capacity rule. Invalid when production, boosts or automated purchases change during the absence. An original implementation contract, not a universal idle-game mechanic. | W02, 2019 |

### 2.3 Numeric precision and rounding (PP:516-524)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| NP1 | 518 | VERIFIED | Luau's documented number type is a 64-bit IEEE 754 double. All integers through 2^53 = 9,007,199,254,740,992 are exactly representable (FM9); larger integer literals can lose precision. This does not mean arbitrary decimal arithmetic below that boundary is exact. Roblox's API reference may call an argument int64, but that does not create a separate exact-integer Luau number type. | W06, W07, undated; acc. 2026-10-21 |
| NP2 | 520 | OPINION | Choose the smallest meaningful currency unit, maximum balance and representation together. Test that adding or spending that unit still changes the stored balance at the maximum planned magnitude. A suffix such as "Qa" changes presentation, not precision. Beyond the chosen safe domain, require an explicit big-number representation with defined arithmetic, comparison, serialization and rounding; do not widen the design because the UI can print more digits. | W06-W07, acc. 2026-10-21 |
| NP3 | 522 | VERIFIED, mathematical distinction | In general floor(xy) need not equal floor(x)floor(y) (FM10), so rounding intermediate values can differ from rounding the final product. Algebraic observation, not a published economy configuration. Roblox documents math.floor as rounding downward. | W07, acc. 2026-10-21 |
| NP4 | 524 | OPINION | Specify whether a bulk purchase costs the sum of individually rounded prices or the rounded geometric-sum price. Specify when modifiers, taxes, discounts, caps and floors apply. For each transaction, compare spreadsheet, reference simulator and runtime on the same starting state and operation sequence. Treat display rounding as separate from balance changes. | W06-W07, acc. 2026-10-21 |

### 2.4 Arithmetic executed for the paper (PP:526-530)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| TL8 | 528 | VERIFIED execution | Calculations ran in an exact rational-arithmetic script using Python fractions.Fraction, so source decimals and table results are exact rationals with no hidden rounding. It checks 2550 direct-sum/bulk-formula equalities, RPG XP-to-point identities and both combat hit thresholds, then emits the displayed timelines. Verifies arithmetic only: does not run Roblox, measure a live game, validate fun, prove a purchase policy globally optimal or infer missing source parameters. The script is not in the paper range and not in this repo. | Paper, 2026-10-21 (no source id; execution) |
| TL9 | 530 | OPINION workflow | Input sheets separate quoted source values, approved studio tuning, derived values and observed telemetry. Export canonical parameter data and rerun the same calculation code the game uses. Per player policy keep: policy name, starting state, enabled content, offline conditions, exact event log, termination condition, balance-data version. Check milestone boundaries and before/after gear breakpoints explicitly; aggregate totals can hide them. Do not demand universal daily or weekly durations: ask the director for intended pacing, then give forecast ranges conditional on measured play rates. | This paper, 2026-10-21 (O00) |

### 2.5 Section 8 rule table (PP:532-537)

| ID | PP | Rule | Formula or number | Evidence mark | Source and date |
| --- | --- | --- | --- | --- | --- |
| TT1 | 533 | Keep a visible model; add state simulation when interactions require it | No universal run count | EXPERIENCE plus OPINION tool choice | W01, 2025; W02, 2019 |
| TT2 | 534 | Prefer exact answers when the modeled problem permits them | Enumeration versus sampled estimate | EXPERIENCE | W03, 2010-07-28 |
| TT3 | 535 | Set statistical precision before a simulation budget | Interval method and independence must be declared | VERIFIED method; OPINION procedure | W05, undated/accessed 2026-10-21 |
| TT4 | 536 | Check meaningful currency increments at maximum magnitude | All integers through 2^53 exactly representable | VERIFIED fact; OPINION check | W06, undated/accessed 2026-10-21 |
| TT5 | 537 | Freeze operation order and rounding policy | floor(xy) need not equal floor(x)floor(y) | VERIFIED mathematical distinction | W07, undated/accessed 2026-10-21 |

## 3. Diagnose progression with player data (paper section 9, PP:539-601)

### 3.1 Interpreting behavior (PP:541-549)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| DB1 | 543 | EXPERIENCE | Schreiber: statistics can show a pattern without establishing its cause; playtime and return behavior are imperfect proxies for fun. A low-use item may be weak, unappealing or hard to learn. Cautions, not a claim that one metric diagnoses motivation. | W04, 2010-08-25 |
| DB2 | 545 | OPINION, progression dashboard | Per milestone and balance revision report: exposure, entry state, attempted and achieved counts, active time, calendar time, attempts or deaths, currency earned and spent, balance just before purchase, available alternatives, exit state. Split by new vs returning players, route/build, device/control constraints and relevant session behavior; do not present small slices as reliable populations. Measure resource bottlenecks separately: currency but no material; material but no unlock; power but unclear objective. | W04, 2010-08-25; W02, 2019 |
| DB3 | 547 | OPINION, non-completer rule | Never compute "time to milestone" only for achievers and present it as the whole population. Report who was eligible, who has not achieved it, and each player's observation window. A new cohort has had less time to reach late content; a missing milestone event may be a telemetry fault. Keep active-time and elapsed-calendar-time charts separate. Proposed safeguard, not a sourced claim about any game. | W04, 2010-08-25 |
| DB4 | 549 | OPINION, tuning loop | If players leave before an unlock, compare explanations: unaffordable cost, confusing objective, uninteresting activity, combat failure, too little session time left. Change the smallest justified lever, then compare a clearly identified cohort and revision. Inspect distributions and individual paths, not only averages. No causation from an uncontrolled before/after, especially when acquisition, events or content also changed. | W04, 2010-08-25 |

### 3.2 Denominators, retention and engagement definitions, benchmarks (PP:551-559)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| DR1 | 553 | VERIFIED | Roblox D1/D7/D30 retention cohorts are indexed by the new user's first play date. D7 means return seven days later, not "at least once during the first week". An immature cohort's missing D7/D30 value is not zero. (The paper defines only D7 in words; the general Dk form is in DT1, FM11. D1 and D30 are not separately defined in the paper text.) | R10, acc. 2026-10-21 |
| DR2 | 553 | VERIFIED | Average session time = total playtime divided by number of sessions (FM12). The first-session retention chart measures the share of new users still present X minutes into their first session. | R11, acc. 2026-10-21 |
| DR3 | 555 | OPINION | Record for every chart: eligibility population, numerator, denominator, observation window, acquisition source, cohort entry rule, build/balance version. Total playtime/DAU and total playtime/session answer different questions. A tutorial improvement can shorten sessions by removing waiting while raising completion. A long session may hold inactivity or confusion and cannot alone certify enjoyable progression. | Author recommendations, 2026-10-21 (O00); definitions R10-R11 |
| DR4 | 557 | VERIFIED | Roblox benchmark source order: similar-player games where available, then genre, then all experiences. Similar-game benchmarks update daily, use comparison games with at least 100 DAU, and show the 50th-90th percentile range. The documentation's 12.11%-18.73% D1 example is an illustration, not a platform target. | R12, acc. 2026-10-21 |
| DR5 | 557 | VERIFIED | Overall-success benchmark pools are different: top 1,000 games by rolling 30-day total playtime, excluding games under 30 days old. | R12, acc. 2026-10-21 |
| DR6 | 559 | OPINION | A benchmark is descriptive and depends on how it is selected. Its stronger games are survivors; a changing comparison pool can move the displayed benchmark with no change in your game. No universal D1, D7 or minutes-per-session ideal is justified. Compare appropriate cohorts including players who left; set creative objectives before picking optimization metrics. Recommendation-ranking signals must not be reused as causal progression rules. | R12, acc. 2026-10-21; analytical interpretation |

### 3.3 Instrumentation and current caveats (PP:561-569)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| DI1 | 563 | VERIFIED | LogEconomyEvent records: player, Source/Sink (flow direction), currency, positive amount, ending balance, transaction type, optional item SKU, custom fields. (Paper gives these as prose; no parameter names, types or enum names.) Roblox's current economy, funnel and custom events need server calls in published games, not Studio or client sends. | R01; R13, acc. 2026-10-21 |
| DI2 | 563 | OPINION | Log after the authoritative award or purchase succeeds, not on button press. Keep purchase attempts as a separate event. | R14, acc. 2026-10-21 |
| DI3 | 565 | VERIFIED | LogOnboardingFunnelStepEvent and LogFunnelStepEvent power funnels. Repeated steps count only the first instance. Skipped later steps automatically complete earlier ones. Funnel attribution and filters use entry-time values, not necessarily the player's later device. A recurring funnel uses funnelSessionId to tell attempts apart. | R15, acc. 2026-10-21 |
| DI4 | 565 | OPINION | A free-form RPG should not encode optional branches as one compulsory ordered funnel. Use separate paths or custom events; otherwise auto-completed steps can manufacture apparent participation. | Paper (cites no id for this sentence); basis R15 |
| DI5 | 567 | VERIFIED | LogProgressionEvent accepts Start, Complete or Fail and path/level information, with a convenience method per state. Its reference states these events do not currently display in any Roblox-provided chart. Do not promise a finished progression dashboard because the API exists. | R13, acc. 2026-10-21 |
| DI6 | 567 | VERIFIED | Custom events can carry durations or other numeric values. Built-in aggregations: counts, distinct users, mean, sum, min, max. No promised percentile or survival-analysis pipeline. | R16, acc. 2026-10-21 |
| DI7 | 569 | VERIFIED / unresolved documentation disagreement | Event-types documentation lists 10 resource types; Economy-events documentation and the AnalyticsService reference say 5. The paper leaves this unresolved. | R01; R13-R14, acc. 2026-10-21 (10 = Event types page per paper text; 5 = Economy events and AnalyticsService reference) |
| DI8 | 569 | OPINION | Design the first schema around no more than 5 resource types; confirm real acceptance before relying on the larger limit. | R14 and others, acc. 2026-10-21 |
| DI9 | 569 | VERIFIED | Event-types page also gives: 3 custom fields; 100 funnel steps; 100 custom event names; global requests per minute 120 + 20 × CCU (FM13). These are transport and cardinality limits, not targets for useful events. Charts usually take about 24 hours. View Events gives a near-real-time list for validation. | R14, acc. 2026-10-21 |

### 3.4 Diagnostic matrix (PP:571-582). Paper heading: signals are questions, not automatic verdicts

All seven rows are OPINION, proposed diagnostics dated 2026-10-21 (PP:573), grounded in the platform measurements R01 and R10-R16. Thresholds must come from the game's intended pacing and observed uncertainty, not from invented universal benchmarks (PP:573).

| ID | PP | Suspicion | Numbers and denominator | Confounds to rule out | Appropriate next test |
| --- | --- | --- | --- | --- | --- |
| DM1 | 576 | First reward is too late | Time from entry to first meaningful reward; distribution of active time over all entrants, with unfinished players kept as censored observations | Loading failures, device performance, acquisition mismatch, omitted events | Change reward access or onboarding, not the whole XP curve |
| DM2 | 577 | Level is a grind wall | Conversion from eligible entrants to the next unlock; active earned currency per minute; net remaining price; failure count | Optional detours, session interruption, returning veterans, trading gifts | Test cost and earning activity separately; keep the intended skill test |
| DM3 | 578 | Content is exhausted too fast | Time to the last meaningful unlock, then return rate and activity mix | Experts self-selecting, exploit farming, limited alpha content | Add strategic breadth or later goals before slowing new players globally |
| DM4 | 579 | Apparent inflation | Wallet percentiles by tenure; executed fixed-basket price index; new currency per person-hour; sink uptake | New-player inflow, balance transfers, deliberate scaling, rare-item supply shock | Repair the dominant unwanted source or add wanted expenditure, not a blanket tax |
| DM5 | 580 | Premium creates a wall | Completion and time-to-unlock by spender cohort defined before treatment; payer conversion and nonpayer return | Payers were more engaged before paying; regional price and tenure mix | Randomized offer or interface tests plus qualitative fairness review; never infer that payment caused retention |
| DM6 | 581 | A reward route dominates | Reward per hour and selection share by route and stage, plus failure and enjoyment feedback | The best route may also be the most fun; class and device bias | Improve the alternatives; measure diversity without penalizing competence |
| DM7 | 582 | Retention fell after update | Mature first-play cohorts split by device, region, acquisition and version | Weekend or holiday shifts, paid-acquisition burst, crashes, changed eligibility | Verify operations first, then isolate the progression change |

### 3.5 Survivor bias and experiments (PP:584-592)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| DB5 | 584 | OPINION | Time-to-level among completers alone suffers survivor bias: a harsher gate can make surviving experts' mean look faster while everyone else quits. Report completion probability and unfinished exposure next to duration; separate active playtime from wall-clock return delay. A player not back at the observation cutoff is unobserved future behavior, not proof of permanent churn. | Author, 2026-10-21 (O00) |
| DX1 | 588 | VERIFIED | Native in-game Experiments use configs, allow planned durations of 14-60 days, and up to two variants plus control. Code must call ConfigService:GetConfigForPlayerAsync and then GetValue for the key; GetConfigAsync alone does not apply experiments. Calling GetValue enrolls the player, so early calls can enroll users who never meet the changed feature. | R17, acc. 2026-10-21 |
| DX2 | 590 | VERIFIED | Roblox warns that under 1,000 DAU may make useful results hard; a power warning, not a hard universal minimum. Targeting reduces sample size. The UI estimates minimum detectable effect and exposes sample-ratio mismatch. Early-harm checks do not justify naming an early winner. | R17, acc. 2026-10-21 |
| DX3 | 592 | OPINION | Predeclare a practical win criterion and guardrails, e.g. more eligible players reach the next interesting decision without hurting later return, competitive fairness or nonpayer progress. The numeric effect size comes from the team's goals and feasible sample, not the paper. Persist experiment exposure and version when a multi-session path needs continuity; audit changed eligibility before comparing cohorts. Non-significance is not equivalence. Small teams should combine instrumented playtests, player explanations and longer observation instead of a fabricated confident A/B result. | R17; author interpretation, 2026-10-21 |

### 3.6 Section 9 rule table (PP:594-601)

| ID | PP | Rule | Formula or number | Evidence mark | Source and date |
| --- | --- | --- | --- | --- | --- |
| DT1 | 595 | Use mature first-play cohorts | Dk returns on day k / original new cohort | VERIFIED | R10, acc. 2026-10-21 |
| DT2 | 596 | Distinguish session and user averages | Session time = playtime / sessions | VERIFIED | R11, acc. 2026-10-21 |
| DT3 | 597 | Never turn example benchmarks into targets | 50th-90th percentile band; pool changes | VERIFIED description; OPINION rule | R12, acc. 2026-10-21 |
| DT4 | 598 | Include people who did not finish | Completion rate plus censored duration | OPINION analytical method | Author, 2026-10-21 |
| DT5 | 599 | Avoid imaginary progression charts | LogProgressionEvent currently has no provided chart | VERIFIED | R13, acc. 2026-10-21 |
| DT6 | 600 | Validate instrumentation before curve changes | View Events now; charts about 24 hours | VERIFIED | R14, acc. 2026-10-21 |
| DT7 | 601 | Power experiments, not confidence theater | 14-60 days; up to 2 variants + control | VERIFIED | R17, acc. 2026-10-21 |

## 4. Hand approved data to engineering (paper section 10, PP:603-618)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| HO1 | 605 | EXPERIENCE | GDC's 2025 overview reports that the Merchant Guilds team used Apps Scripts to deploy spreadsheet-authored content. A real spreadsheet-to-game workflow; it does not show that direct deployment without review is safe. | W01, 2025 |
| HO2 | 607 | OPINION, handoff package | Deliver an approved data snapshot with these 13 fields: (1) stable item/upgrade/milestone IDs; (2) schema version; (3) balance revision; (4) currency and time units; (5) formula ID and parameters; (6) input domain; (7) caps; (8) rounding and modifier order; (9) prerequisites; (10) costs and rewards; (11) reset behavior; (12) expected fixture outputs; (13) the creative rationale for deliberate exceptions. Include generated engineering tables and readable charts from the same snapshot. Never make an engineer or a second AI infer values from a chart or prose. The paper's proposed contract. | Informed by W01 (2025); W06-W07 (acc. 2026-10-21) |
| HO3 | 609 | OPINION, synchronization rule | Pick one editable authority (reviewed spreadsheet or structured source data) and generate the other views. Put an explicit revision or content hash in exports and reports. Fail the export if: required IDs are missing or duplicated; references are unresolved; formulas give nonfinite values; generated values differ from approved fixtures. Keep a semantic change report: old/new values, changed milestone times under named policies, changed reset and rounding rules. Never repair one stale copy by silently changing another. | W01, 2025; original release contract (O00) |
| HO4 | 611 | OPINION, narrow example schema | An upgrade row could hold 10 fields: upgradeId, tier, costCurrencyId, baseCost, growthFactor, costRounding, productionPerActiveSecond, requiredUpgradeId, maxOwned, balanceRevision. Illustrative only; an RPG reward table needs other fields. Store a reason and a source or assumption label with exceptional values so later agents do not flatten intentional power spikes into a smooth curve. | W01, 2025; W02, 2019 |
| HO5 | 613 | OPINION, existing-player handoff | Include representative existing save states and the expected interpretation after the balance change: spent currency, unlock eligibility, equipped items, prestige awards, lifetime counters. Do not assume recalculating today's curve preserves yesterday's earned state. Flag any migration or compensation decision for the creative director and the engineering owner. A progression-data requirement, not a full deployment architecture. | W02, 2019; original recommendation |

Section 10 rule table (PP:615-618; columns: rule, formula or number, evidence mark, source and date)

| ID | PP | Rule | Formula or number | Evidence mark | Source and date |
| --- | --- | --- | --- | --- | --- |
| HT1 | 616 | Generate runtime data from the approved authority | One named revision per artifact | EXPERIENCE precedent; OPINION contract | W01, 2025 |
| HT2 | 617 | Make units, caps and rounding explicit | Meaningful currency unit + active/calendar time | OPINION contract grounded in numeric facts | W06-W07, undated/accessed 2026-10-21 |
| HT3 | 618 | Diff outcomes, not just parameters | Milestone times under the same policies | OPINION | W02, 2019 |

## 5. The progression designer process (paper section 11, PP:620-651)

### 5.1 Ten steps (PP:622-642)

PP:622 (OPINION, original process): a proposed studio workflow, not a published industry standard; it combines documented spreadsheet practice, metagame simulation, probability analysis and cautious reading of player metrics. Basis W01 (2025), W02 (2019), W03 (2010-07-28), W04 (2010-08-25).

| ID | PP | Step (paraphrase) |
| --- | --- | --- |
| PS1 | 624 | Get the creative director's desired experience: what gets easier, what stays hard, which choices open, what can never be bought away. |
| PS2 | 626 | Build the feeling timeline (the paper's section 2, outside this range). Every target stays a hypothesis until a person has played and reported the intended feeling. |
| PS3 | 628 | Draw the resource and unlock graph. Define state, clocks, sources, sinks, caps, resets and event order before tuning coefficients. |
| PS4 | 630 | Choose the simplest curve that gives the intended relationship. Declare units, domain, parameters, breakpoints, examples. Do not pick exponential growth only because the genre uses big numbers. |
| PS5 | 632 | Compute deterministic examples independently. Trace a full purchase/level/reset sequence, not one row. Compare cumulative cost with per-step cost, and cumulative XP with XP-to-next-level. |
| PS6 | 634 | Simulate the named policies and session assumptions. Keep an event trace that explains each milestone and blocked path. Add stochastic sampling only where the mechanic or behavior model is random. |
| PS7 | 636 | Review failure modes (7): exploding waits; flattened meaningful rewards; unreachable prerequisites; dominant shortcuts; capped resources that cannot pay required costs; reset loops that create unintended value; nonfinite or precision-lost numbers. |
| PS8 | 638 | Give the creative director alternative parameter sets with trade-offs and uncertainty. Ask them to choose among concrete experiences, not to approve unexplained coefficients. |
| PS9 | 640 | Export the approved revision, run cross-tool fixture comparisons, hand engineering the data contract and expected results. |
| PS10 | 642 | Observe play and telemetry. Explain mismatches between prediction and behavior; revise behavior assumptions as well as numbers. A passing arithmetic check is not evidence of fun. |

### 5.2 Conservation check, model pass versus design pass, rule table (PP:644-651)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| PC1 | 644 | OPINION, conservation check | For each currency and simulated interval, require endingBalance = startingBalance + grantedSources + transfersIn − spentSinks − transfersOut (FM8), with cap loss, conversion and rounding recorded as named adjustments. An accounting identity under those definitions, not an empirical economy target. An unexplained residual is a model or instrumentation problem; a positive net source is not automatically a balance problem. | W08, 2010-09-08 (resource generation, destruction, trading distinctions); proposed check (O00) |
| PC2 | 646 | OPINION, model pass | A model passes arithmetic review only if: required paths are reachable; forbidden paths stay blocked; transaction ledgers reconcile; generated tables match fixtures; expected numeric boundaries hold. | W02, 2019; W04, 2010-08-25; W06, acc. 2026-10-21 |
| PC3 | 646 | OPINION, design pass | A design passes creative review only when its trade-offs and experienced pacing meet the director's brief. Neither a model pass nor high retention alone certifies ethical or enjoyable progression. | W02, 2019; W04, 2010-08-25; W06, acc. 2026-10-21 |

Section 11 rule table (PP:648-651; same columns)

| ID | PP | Rule | Formula or number | Evidence mark | Source and date |
| --- | --- | --- | --- | --- | --- |
| PT1 | 649 | Keep arithmetic acceptance separate from creative acceptance | Model pass ≠ fun proof | OPINION synthesis | W02, 2019; W04, 2010-08-25 |
| PT2 | 650 | Explain every currency change | End = start + sources − sinks + net transfers + named adjustments | OPINION check; accounting identity | W08, 2010-09-08 |
| PT3 | 651 | Approve the experience before exporting coefficients | No universal pacing constants | OPINION workflow | W01, 2025; W02, 2019 |

## 6. Progression review checklist (PP:653-672)

PP:655 (OPINION O00, 2026-10-21): these release-review gates are proposed studio practice, not empirically established universal quality thresholds. The owner may reject a model that passes every arithmetic gate because it is not the desired game. A blank evidence field is not a pass. Table columns as the paper: pass/fail item, evidence required to pass, failure response. All 15 rows:

| ID | PP | Item | Evidence required to pass | Failure response |
| --- | --- | --- | --- | --- |
| CK1 | 658 | Player experience is specified | Owner-approved target feelings and meaningful changes, not only larger values | Return to game designer and owner |
| CK2 | 659 | Every numeric input has provenance | Dated source, measured dataset or explicit approved design decision | Remove the unsupported number or get the missing decision |
| CK3 | 660 | Units and index origins are explicit | Currency, XP, seconds, levels and ownership states defined | Correct dimensions and off-by-one errors |
| CK4 | 661 | Formula and exported data agree | Regenerated table matches the exact versioned model | Block export; find the divergent inputs |
| CK5 | 662 | Progression is reachable | Required dependencies and reachable states shown for each supported path | Repair the inaccessible state or missing acquisition path |
| CK6 | 663 | Time estimates include strategy | Starting state, earning process, purchase policy and player path recorded | Relabel the timeline as conditional and rerun |
| CK7 | 664 | Power spikes are intentional | Breakpoint changes and the content they affect reviewed | Change power, enemy thresholds or encounter context |
| CK8 | 665 | Prestige improves an approved objective | Reset losses, retained assets and recovery path compared explicitly | Rework the reset, or explain its non-efficiency purpose |
| CK9 | 666 | Rewards carry meaning | Each unlock changes capability, choice, information or an owner-approved goal | Remove the empty milestone or add meaningful content |
| CK10 | 667 | Economy accounting closes | Source and sink events reconcile with wallet changes under a defined scope | Investigate missing events, duplication or classification |
| CK11 | 668 | Premium rules are independently checked | Current platform-policy review and fairness decision recorded | Disable the noncompliant offer; get a policy review |
| CK12 | 669 | Simulated paths are disclosed | Supported policies, uncertainty, caps and missing human behavior listed | Stop presenting the model as a population prediction |
| CK13 | 670 | Mathematical tests passed | Reproducible report for boundaries, sums, threshold transitions and exports | Fix the model and rerun dependent checks |
| CK14 | 671 | Gameplay was actually tested | Observation record from the relevant build and participants | Mark gameplay validation pending; never infer it from arithmetic |
| CK15 | 672 | Owner approved release values | Exact data version and scope of approval recorded | Do not ship automatically |

## 7. Do not do (PP:674-694)

All ten are OPINION O00, 2026-10-21.

| ID | PP | Don't (paraphrase) |
| --- | --- | --- |
| DN1 | 676 | Do not invent an XP earning rate, combat cadence or session benchmark to finish a table. Keep the unknown symbolic and name the measurement needed. |
| DN2 | 678 | Do not call a higher nominal reward a power increase before checking what it buys or changes. Compare the resulting state against the same content and time cost. |
| DN3 | 680 | Do not turn a designer's recollection or an observational psychology result into a universal causal law. Keep source type and population. |
| DN4 | 682 | Do not optimize predicted player behavior with knowledge the real player does not yet have, unless the path is labeled omniscient. |
| DN5 | 684 | Do not pass a formula that is dimensionally right but operationally impossible (the player must spend the same currency twice, or hold a locked prerequisite). |
| DN6 | 686 | Do not use continuous DPS in place of discrete hit thresholds, or continuous income as a claim about an unmodeled production cycle. |
| DN7 | 688 | Do not publish the worked examples as proposed values for the studio's game. They compute from historical source parameters; they are not tested tuning recommendations. |
| DN8 | 690 | Do not describe arithmetic execution as playtesting, or a cohort simulation as measured player telemetry. |
| DN9 | 692 | Do not silently change rounding, indexing, caps or reset rules between the spreadsheet and the shipped table. |
| DN10 | 694 | Do not let an agent approve its own creative decision, monetization-policy exception or production release. |

## 8. Open questions, math boundaries, tool evidence boundaries (PP:696-726)

### 8.1 Open questions and limits (PP:696-706; all OPINION O00, 2026-10-21)

| ID | PP | Open question or limit (paraphrase) |
| --- | --- | --- |
| OQ1 | 698 | No established universal number for how many seconds a Roblox player should wait for the next upgrade, how many rewards make a session satisfying, or how fast every genre should advance. Sources describe particular systems, selected populations and platform measurements. A studio picks its audience and intended experience, then measures its own build. An exact formula does not remove that uncertainty. |
| OQ2 | 700 | The worked RPG source gives no XP earning process, so no measured calendar timeline. The unresolved quantity is the path-dependent XP acquisition rate, including encounter outcomes and travel or downtime. The incremental reconstruction also does not fix the commercial game's real onboarding duration: the published inputs and the model's continuous-income assumptions bound the claim. |
| OQ3 | 702 | Open design questions: is a plateau useful anticipation, a needed mastery interval or an unwanted wall for this audience? Does a numerical reset support a wanted replay experience or only repeat familiar labor? These need player observations linked to state history, not a coefficient chosen by an agent. |
| OQ4 | 704 | Distribution: a curve right for an efficient route can fail exploration, low skill, interrupted play or accessibility needs. Published examples rarely give those distributions. Treat the gap as missing evidence; use several explicitly defined player paths, not the mean path for everyone. |
| OQ5 | 706 | The paper's validation shows arithmetic consistency for the listed models. It does not show an enjoyable game, a compliant live monetization implementation or a tested Roblox experience. Those are separate owner and studio review duties. |

### 8.2 Additional mathematical boundaries (PP:708-718; five items; the paragraph and items carry no tag: untagged)

| ID | PP | Boundary (paraphrase) | Src id named |
| --- | --- | --- | --- |
| MB1 | 710 | M02 corrects "the author's" earlier root-versus-log explanation. Use the actual function, not the loose phrase "logarithmic prestige". (Whose "author": Z27.) | M02 (= C01), 2017-01-12 |
| MB2 | 712 | M01's rounded demonstration prices and free-first-item indexing cannot all be treated as exact raw game data. The reindexed model fixes the second price at 4 and does not claim engine equivalence. | M01, 2016-10-04 |
| MB3 | 714 | M05's continuous fractional-generation model and a discrete tick implementation answer different questions. State event semantics before comparing results. | M05, 2016-10-28 |
| MB4 | 716 | M03's experiential pacing pattern is not a measured optimal schedule; its author says it is not necessarily best for every game. | M03, 2010-08-18 |
| MB5 | 718 | No complete sourced combat cadence or XP acquisition data was found for the RPG example. Its time axis stays symbolic, not invented. | none |

### 8.3 Tool evidence boundaries (PP:720-726)

| ID | PP | Tag | Content (paraphrase) | Src, date |
| --- | --- | --- | --- | --- |
| EB1 | 722 | EXPERIENCE | W02's 2019 framing argues for simulation beyond spreadsheet limits; W01's 2025 examples show spreadsheets still doing real production work. A difference in problem complexity and workflow emphasis, not evidence of a universal winner. | W01, 2025; W02, 2019 |
| EB2 | 724 | EXPERIENCE plus OPINION caution | Schreiber's 2010 tutorial suggests repeating Monte Carlo runs until results look consistent. Introductory heuristic, not a precision guarantee. For a defensible probabilistic claim use a specified estimator and interval procedure such as W05, not the tutorial's illustrative trial counts. | W03, 2010-07-28; W05, acc. 2026-10-21 |
| EB3 | 726 | VERIFIED source limitation | The GDC sources are public session descriptions, not independently reviewed simulation code or a full transcript. The inspected sources do not establish a universal best first-session duration, monthly progression speed, acceptable wall length or an automatic agent that can certify fun. Proposed workflows and timeline feelings are OPINION, not disguised studio disclosures. | W01, 2025; W02, 2019 |

## 9. Formula cards (extractor assembly: every variable defined, unit and domain)

Where the paper gives a definition, it is marked "paper". Everything else is (extractor), added so each formula is complete; the paper gives no units or domains for most symbols (Z03, Z09).

| ID | PP | Formula (plain text) | Variables, unit, domain | Tag, src |
| --- | --- | --- | --- | --- |
| FM1 | 446, 481 | B(t+1) = B(t) + S(t) − K(t) (rule table writes B′ = B + S − K plus boundary adjustments) | B(t) = total balance of one currency over the closed population (paper); S(t) = newly created currency (paper); K(t) = destroyed currency (paper). (extractor) units: currency units; t = discrete step index; S and K measured over the step from t to t+1; B, S, K >= 0. Closed population, no omitted adjustment (paper). | VERIFIED: accounting identity; derivation O00 2026-10-21 |
| FM2 | 448 | P(t) = Σ[p_i(t) × q_i(0)] / Σ[p_i(0) × q_i(0)] | i = item in a fixed basket (same items, same quality, same base quantities in both periods: paper); p_i(t) = price of item i at time t (paper says to track executed trade prices); q_i(0) = base quantity of item i. (extractor) p in currency per item, q in items, P dimensionless, P(0) = 1, requires denominator > 0 and every basket item priced in both periods. | OPINION; O00 2026-10-21 |
| FM3 | 448, 482 | T = max(0, C − B) / r | C = cost (paper); B = usable balance (paper); r = constant net earning rate, r > 0 (paper). (extractor) C, B in currency units; r in currency per active second (unit from PP:512); T in active seconds; T = 0 when B >= C. Not valid when r changes: use the cumulative-earnings integral (not written in the paper). | OPINION metric; VERIFIED algebra; O00 |
| FM4 | 472 | Expected spend to first success = c / p | p = per-trial success probability, constant, 0 < p < 1 (paper); trials independent, no pity (paper). c = price per trial: not defined in the paper (Z09); (extractor) c in currency units per try. | Author derivation; O00 |
| FM5 | 472 | P(success within n tries) = 1 − (1 − p)^n | n = number of tries (paper); (extractor) n a positive integer. | Author derivation; O00 |
| FM6 | 472 | n_q = ceil(log(1 − q) / log(1 − p)) | q = desired success probability, 0 < q < 1; p fixed, 0 < p < 1 (paper); independent trials; n_q = least try count reaching q. Not valid for pity or changing probabilities (paper). | Author derivation; O00 |
| FM7 | 514 | offlineReward = rateAtExit × min(max(elapsed, 0), offlineCap) | Paper gives no definitions. (extractor) rateAtExit = production rate in the exit snapshot, currency per second; elapsed = eligible elapsed time in seconds; offlineCap = cap on credited time in seconds. A capacity rule follows. Invalid if production, boosts or auto-purchases change during the absence (paper). | OPINION, illustrative; W02 basis |
| FM8 | 644, 650 | endingBalance = startingBalance + grantedSources + transfersIn − spentSinks − transfersOut; named adjustments (cap loss, conversion, rounding) recorded (PP:650 adds "+ named adjustments" in the equation) | Per currency, per simulated interval (paper). (extractor) all terms currency units; adjustment sign convention not given (Z02). | OPINION check; accounting identity; W08 |
| FM9 | 518, 536 | 2^53 = 9,007,199,254,740,992; every integer from 0 through 2^53 is exact | Luau number = 64-bit IEEE 754 double (paper). | VERIFIED; W06, W07 |
| FM10 | 522, 537 | floor(x × y) need not equal floor(x) × floor(y) | x, y real numbers (extractor); math.floor rounds downward (paper). | VERIFIED mathematical distinction; W07 |
| FM11 | 595, 553 | Dk retention = (new users who return on day k) / (original new cohort) | Cohort indexed by first play date; D7 = return seven days later (paper). (extractor) k = days after first play; ratio in [0, 1]; undefined (not zero) while the cohort is immature. | VERIFIED; R10 |
| FM12 | 596, 553 | Average session time = total playtime / number of sessions | (extractor) playtime in minutes or seconds, sessions a count. Different from total playtime / DAU (PP:555). | VERIFIED; R11 |
| FM13 | 569 | Global requests per minute = 120 + 20 × CCU | Paper does not define CCU or scope. (extractor) CCU = concurrent users; scope of "global" unstated (Z17). | VERIFIED; R14 |
| FM14 | 460, 484 | Regional price in [0.30 × P, P] | P = the creator's default price (paper: "default price"). (extractor) same currency as P (Robux). | VERIFIED; R05 |

## 10. Hand checks (extractor; arithmetic only)

Computed with Python 3 on 2026-10-21. These check the paper's algebra and examples; they are not fact checks of any source.

| ID | Check | Result |
| --- | --- | --- |
| HC1 | 2^53 | 9007199254740992 matches PP:518. 2^53 + 1 converted to a double equals 2^53 (precision lost), consistent with "larger integer literals can lose precision". |
| HC2 | c/p with c = 10 Robux, p = 0.05 | 200 Robux. Equals the 200-Robux guaranteed alternative that PP:472 attributes to Roblox's example. The paper does not say the example price is set to c/p (Z09). |
| HC3 | 1 − (1 − p)^n at p = 0.05, n = 20 (expected spend 200 Robux at 10 per try) | 0.6415 (64.15%). So spending the expected amount succeeds about 64% of the time, consistent with PP:472 "no guarantee". |
| HC4 | n_q at p = 0.05 | q = 0.5: 14 (13 gives 0.4867, 14 gives 0.5123). q = 0.9: 45 (0.9006). q = 0.95: 59 (58 gives 0.9490, 59 gives 0.9515). q = 0.99: 90 (0.9901). |
| HC5 | floor(xy) versus floor(x)floor(y), x = y = 1.5 | floor(2.25) = 2; floor(1.5) × floor(1.5) = 1. Also x = y = 2.5: 6 versus 4. Confirms PP:522 in general. |
| HC6 | T = max(0, C − B) / r | C = 100, B = 40, r = 3 gives 20 active seconds. C = 100, B = 120 gives 0. r = 0 with C > B is unreachable (SM5), not a number. |
| HC7 | Regional bounds | 30% of default price floor = at most 70% discount. Matches the R05 register quotation (section 14, Z07). |

## 11. Claims to fact-check (a)

Every VERIFIED or EXPERIENCE claim in lines 440-727 with a number, API, formula, date or rule. "Src date" is from the register (section 12). Fact-check: does the source say this, in the version dated? The paper's quoted register quotations are not repeated here. Roblox documentation is living and undated; "accessed 2026-10-21" means the page as the paper's author saw it.

### 11.1 Roblox claims (sources R01-R17, W06, W07)

| # | Claim (paraphrase, exact names and numbers) | PP | Src | Src date | Tag |
| --- | --- | --- | --- | --- | --- |
| RB01 | Roblox economy docs recommend net sources minus sinks near zero, and adding sinks when balances rise | 450 | R01 | undated; accessed 2026-10-21 | VERIFIED / disagreement |
| RB02 | Roblox dashboard exposes source/sink categories and average wallet balances (paper cites R01, not R12) | 450 | R01 | undated; accessed 2026-10-21 | VERIFIED / disagreement |
| RB03 | Managed Pricing adjusts eligible item prices using economic-location signals, not simply account location | 460 | R05 | undated; accessed 2026-10-21 | VERIFIED |
| RB04 | Regional price bounds: 30%-100% of the creator's default price | 460, 484 | R05 | undated; accessed 2026-10-21 | VERIFIED |
| RB05 | GetUsersPriceLevelsAsync supports checks on item transfers between price levels; gift/trade restrictions are examples, not a compulsory design | 460 | R05 | undated; accessed 2026-10-21 | VERIFIED |
| RB06 | Paid random items = rewards bought with Robux directly, or through currency bought with Robux | 466 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB07 | Policy requires all possible final outcomes and actual numerical probability percentages before purchase; probabilities total 100% subject to a stated rounding-display treatment | 466, 485 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB08 | Paid luck modifier must explain its numerical effect and show updated odds while active | 466 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB09 | A free gameplay-earned random reward is treated differently | 466 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB10 | PolicyService:GetPolicyInfoForPlayerAsync returns ArePaidRandomItemsRestricted and IsPaidItemTradingAllowed | 468, 485 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB11 | A restricted user cannot use the paid random generator; a user not allowed paid-item trading must not access trading of the relevant paid items | 468 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB12 | Documented alternatives: earnable access, disclosed deterministic sequences, guaranteed direct purchases, removal/blocking | 468 | R06 | undated; accessed 2026-10-21 | VERIFIED |
| RB13 | Roblox example: 10-Robux draw, 5% odds, 200-Robux guaranteed alternative | 472 | R06 | undated; accessed 2026-10-21 | VERIFIED (first sentence of a mixed paragraph) |
| RB14 | Younger-audience guidance requires PolicyService checks and discourages urgent/pushy sales language aimed at minors; eligibility depends on location, age, platform | 474 | R07 | undated; accessed 2026-10-21 | VERIFIED |
| RB15 | June 16 global Kids/Select launch added further game reviews for under-16 access | 474 | R08 | 2026-06-16 | VERIFIED |
| RB16 | Age-checked 5-8 generally Kids accounts; 9-15 Select; regional variation | 474 | R08 | 2026-06-16 | VERIFIED |
| RB17 | Linked parents can set spending and screen-time limits until age 13 | 474 | R08 | 2026-06-16 | VERIFIED |
| RB18 | Advertising Standards updated October 9, 2026 prohibit personalized ads to under-18s | 476 | R09 | updated 2026-10-09; accessed 2026-10-21 | VERIFIED |
| RB19 | Rewarded video must use Roblox's product; 13+; predetermined, not chance-based rewards; clear disclosure; affirmative opt-in; immediate delivery after completion | 476, 486 | R09 | updated 2026-10-09; accessed 2026-10-21 | VERIFIED |
| RB20 | Video must not be forced as a progression gate | 476, 486 | R09 | updated 2026-10-09; accessed 2026-10-21 | VERIFIED |
| RB21 | Under-13 users must not be rewarded for engaging with advertising | 476 | R09 | updated 2026-10-09; accessed 2026-10-21 | VERIFIED |
| RB22 | The standards separate ad integrations and age-restricted categories (stated inside an OPINION paragraph, depends on R09) | 478 | R09 | updated 2026-10-09; accessed 2026-10-21 | OPINION resting on R09 |
| RB23 | R02 is cited as a basis for the currency-ledger recommendation; the paper states no specific R02 fact | 444 | R02 | undated; accessed 2026-10-21 | OPINION basis |
| RB24 | D1/D7/D30 cohorts indexed by first play date; D7 = return seven days later; immature cohort missing result is not zero; Dk = returns on day k / original new cohort | 553, 595 | R10 | undated; accessed 2026-10-21 | VERIFIED |
| RB25 | Average session time = total playtime / sessions; first-session retention chart = share of new users still present X minutes into the first session | 553, 596 | R11 | undated; accessed 2026-10-21 | VERIFIED |
| RB26 | Benchmarks: similar-player games, fallback genre then all experiences; similar-game benchmarks update daily; comparison games at least 100 DAU; 50th-90th percentile range; example D1 12.11%-18.73% is an illustration | 557, 597 | R12 | undated; accessed 2026-10-21 | VERIFIED |
| RB27 | Overall-success benchmark pools: top 1,000 games by rolling 30-day total playtime, excluding games under 30 days old | 557 | R12 | undated; accessed 2026-10-21 | VERIFIED |
| RB28 | LogEconomyEvent records player, Source/Sink, currency, positive amount, ending balance, transaction type, optional item SKU, custom fields | 563 | R01; R13 | undated; accessed 2026-10-21 | VERIFIED |
| RB29 | Economy, funnel and custom events need server calls in published games, not Studio or client | 563 | R01; R13 | undated; accessed 2026-10-21 | VERIFIED |
| RB30 | LogOnboardingFunnelStepEvent and LogFunnelStepEvent power funnels; repeated steps count only the first instance; skipped later steps auto-complete earlier ones | 565 | R15 | undated; accessed 2026-10-21 | VERIFIED |
| RB31 | Funnel attribution and filters use entry-time values, not necessarily later device | 565 | R15 | undated; accessed 2026-10-21 | VERIFIED |
| RB32 | A recurring funnel uses funnelSessionId to distinguish attempts | 565 | R15 | undated; accessed 2026-10-21 | VERIFIED |
| RB33 | LogProgressionEvent accepts Start, Complete, Fail and path/level information; convenience method per state | 567 | R13 | undated; accessed 2026-10-21 | VERIFIED |
| RB34 | LogProgressionEvent events do not currently display in Roblox-provided charts | 567, 599 | R13 | undated; accessed 2026-10-21 | VERIFIED |
| RB35 | Custom events can carry durations or numeric values; built-in aggregations: counts, distinct users, mean, sum, min, max; no promised percentile or survival analysis | 567 | R16 | undated; accessed 2026-10-21 | VERIFIED |
| RB36 | Event-types documentation lists 10 resource types; Economy-events documentation and AnalyticsService reference say 5 | 569 | R01; R13; R14 | undated; accessed 2026-10-21 | VERIFIED / unresolved disagreement |
| RB37 | Event-types page: 3 custom fields; 100 funnel steps; 100 custom event names; global requests/minute 120 + 20 × CCU | 569 | R14 | undated; accessed 2026-10-21 | VERIFIED |
| RB38 | Charts usually take about 24 hours; View Events gives a near-real-time list | 569, 600 | R14 | undated; accessed 2026-10-21 | VERIFIED |
| RB39 | Experiments use configs; planned duration 14-60 days; up to two variants plus control | 588, 601 | R17 | undated; accessed 2026-10-21 | VERIFIED |
| RB40 | Code needs ConfigService:GetConfigForPlayerAsync then GetValue; GetConfigAsync alone does not apply experiments; calling GetValue enrolls the player | 588 | R17 | undated; accessed 2026-10-21 | VERIFIED |
| RB41 | Roblox warns under 1,000 DAU may make results difficult (power warning, not hard minimum); targeting reduces sample size; UI estimates minimum detectable effect and exposes sample-ratio mismatch | 590 | R17 | undated; accessed 2026-10-21 | VERIFIED |
| RB42 | Luau number = 64-bit IEEE 754 double; integers through 2^53 = 9,007,199,254,740,992 exactly representable; larger integer literals can lose precision; API reference may say int64 without a separate Luau type | 518, 536 | W06; W07 | undated; accessed 2026-10-21 | VERIFIED |
| RB43 | Roblox documents math.floor as rounding downward | 522 | W07 | undated; accessed 2026-10-21 | VERIFIED |

### 11.2 Other claims (R03-R04 industry, W01-W05, W08, and the paper's own derivations)

R05 is a Roblox document and sits in 11.1 (RB03-RB05); the lead's spec grouped "R03-R05" as industry (see Z29).

| # | Claim (paraphrase, exact names and numbers) | PP | Src | Src date | Tag |
| --- | --- | --- | --- | --- | --- |
| OT01 | Supercell removed Clash of Clans Town Hall weapon upgrade levels at TH12-TH15, saying they slowed midgame progression | 454 | R03 | 2025-10-06 | EXPERIENCE |
| OT02 | Same update moved 15 hero levels from TH15 to TH14 (five each for three heroes) | 454 | R03 | 2025-10-06 | EXPERIENCE |
| OT03 | Same update changed loot incentives and cut Loot Cart recovery from 20% to 10% | 454, 483 | R03 | 2025-10-06 | EXPERIENCE |
| OT04 | Supercell expanded Clash of Clans local-cost pricing to more than 100 countries (register title says "Global Pricing": Z06) | 458 | R04 | 2025-08-21 | EXPERIENCE |
| OT05 | Supercell restricted lower-price-region donations to higher-price regions, described as accessibility and fairness choices; no controlled result published | 458 | R04 | 2025-08-21 | EXPERIENCE |
| OT06 | GDC 2025 microtalks: Lauren Scott shared progression scheme for Psychonauts 2; Guillaume Pierre time/space/money/progression model for Cityscapes: Sim Builder; Retora spreadsheet content pipeline for Merchant Guilds | 490 | W01 | 2025 (GDC year) | EXPERIENCE |
| OT07 | Merchant Guilds team used Apps Scripts to deploy spreadsheet-authored content | 605 | W01 | 2025 (GDC year) | EXPERIENCE |
| OT08 | David Morris (Spryfox) described detailed metagame simulation and analysis before the final metagame was built; no audited accuracy benchmark in the abstract | 492 | W02 | 2019 (GDC year) | EXPERIENCE |
| OT09 | Schreiber separates exhaustive enumeration (exact for finite modeled outcome space) from Monte Carlo sampling; article uses Excel | 498 | W03 | 2010-07-28 | EXPERIENCE |
| OT10 | Schreiber's tutorial suggests repeated Monte Carlo runs until results appear consistent | 724 | W03 | 2010-07-28 | EXPERIENCE plus OPINION |
| OT11 | Schreiber: statistics show a pattern without cause; playtime and return are imperfect proxies for fun; a low-use item may be weak, unappealing or hard to learn | 543 | W04 | 2010-08-25 | EXPERIENCE |
| OT12 | NIST gives Wilson and exact binomial confidence-interval methods and warns that normal approximations can fail with few failures or small samples | 502 | W05 | undated; accessed 2026-10-21 | VERIFIED |
| OT13 | Resource generation, destruction and trading distinctions (basis for the conservation check) | 644, 650 | W08 | 2010-09-08 | OPINION basis; register EXPERIENCE |
| OT14 | Accounting identity B(t+1) = B(t) + S(t) − K(t); transfers cancel in the population total, a transaction tax does not | 446, 481 | O00 derivation | 2026-10-21 | VERIFIED: accounting identity |
| OT15 | T = max(0, C − B) / r for constant r > 0 | 448, 482 | O00 derivation | 2026-10-21 | OPINION metric; VERIFIED algebra |
| OT16 | P(t) = Σ[p_i(t)q_i(0)] / Σ[p_i(0)q_i(0)] | 448 | O00 | 2026-10-21 | OPINION |
| OT17 | Expected spend to first success c/p; success within n tries 1 − (1 − p)^n; n_q = ceil(log(1 − q) / log(1 − p)) (see HC2-HC4) | 472 | O00 derivation | 2026-10-21 | Derivation in a mixed-tag paragraph |
| OT18 | floor(xy) need not equal floor(x)floor(y) (see HC5) | 522, 537 | W07 (as cited) | undated; accessed 2026-10-21 | VERIFIED mathematical distinction |
| OT19 | Exact-rational script (Python fractions.Fraction) checked 2550 direct-sum/bulk-formula equalities, RPG XP-to-point identities and both combat hit thresholds; arithmetic only | 528 | none (paper's own execution) | 2026-10-21 | VERIFIED execution |
| OT20 | GDC sources are public session descriptions, not reviewed code or full transcripts | 726 | W01; W02 | 2025; 2019 | VERIFIED source limitation |
| OT21 | M-source boundaries: M01 rounded demo prices and free-first-item indexing; M05 continuous vs discrete tick; M03 pacing pattern not a measured optimum; M02 root-vs-log correction | 710-716 | M02 (= C01); M01; M05; M03 | 2017-01-12; 2016-10-04; 2016-10-28; 2010-08-18 | untagged |

## 12. Source table (b): every source id cited in lines 440-727

Register lines are PP:730 and the lines shown. "Evidence type" is the register's wording. URLs are copied from the register; no web access. Register quotations are at the register line; a few short ones (under 15 words) are used in section 14. The register gives no author for R01-R17; hosts suggest Roblox (extractor).

| Id | Title | Author / org | Date (register) | Evidence type | URL | Register line |
| --- | --- | --- | --- | --- | --- | --- |
| O00 | Original recommendations and mathematical analysis prepared for this paper | the paper | 2026-10-21 | not an external empirical source | none | 730 |
| R01 | Economy events | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/economy-events | 1046 |
| R02 | Monetization foundations | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/game-design/monetization-foundations | 1056 |
| R03 | Get Ready for Ranked! - Update | Supercell (host supercell.com; author not in register) | 2025-10-06 | EXPERIENCE | https://supercell.com/en/games/clashofclans/blog/release-notes/get-ready-for-ranked-update/ | 1066 |
| R04 | Upgrading Global Pricing for Clash of Clans | Supercell (host supercell.com; author not in register) | 2025-08-21 | EXPERIENCE | https://supercell.com/en/news/clash-global-pricing-upgrade/ | 1076 |
| R05 | Regional pricing | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/monetization/regional-pricing | 1086 |
| R06 | Paid random items policy guidelines | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/monetization/paid-random-items | 1096 |
| R07 | Promoting Items to Younger Audiences | not stated (en.help.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://en.help.roblox.com/hc/en-us/articles/47965190783892-Promoting-Items-to-Younger-Audiences | 1106 |
| R08 | Age-Based Roblox Kids and Select Accounts Now Globally Available | not stated (about.roblox.com newsroom) | 2026-06-16 | VERIFIED | https://about.roblox.com/newsroom/2026/06/age-based-roblox-kids-and-select-accounts-now-globally-available | 1116 |
| R09 | Advertising Standards | not stated (en.help.roblox.com) | updated 2026-10-09; accessed 2026-10-21 | VERIFIED | https://en.help.roblox.com/hc/en-us/articles/13722260778260-Advertising-Standards | 1126 |
| R10 | Retention | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/retention | 1136 |
| R11 | Engagement | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/engagement | 1146 |
| R12 | Analytics dashboard | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/analytics-dashboard | 1156 |
| R13 | AnalyticsService API reference | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/reference/engine/classes/AnalyticsService | 1166 |
| R14 | Event types | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/event-types | 1176 |
| R15 | Funnel events | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/funnel-events | 1186 |
| R16 | Custom events | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/analytics/custom-events | 1196 |
| R17 | Experiments | not stated (create.roblox.com) | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/production/experiments | 1206 |
| W01 | Tools Summit: A Series of Microtalks About Spreadsheets | Tyler Coleman, Russ Fan, Nathan Harling, Tomo Moriwaki, Guillaume Pierre and Lauren Scott; GDC Vault session overview | 2025 (GDC event year; exact session date not established) | EXPERIENCE | https://gdcvault.com/play/1035550/Tools-Summit-A-Series-of | 1216 |
| W02 | Beyond Spreadsheets: Building a Metagame Simulator for Balance and Prototyping | David Morris, Spryfox; GDC Vault session overview | 2019 (GDC event year; exact session date not established) | EXPERIENCE | https://gdcvault.com/play/1026489/Beyond-Spreadsheets-Building-a-Metagame | 1228 |
| W03 | Level 4: Probability and Randomness | Ian Schreiber, Game Balance Concepts | 2010-07-28 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/07/28/level-4-probability-and-randomness/ | 1240 |
| W04 | Level 8: Metrics and Statistics | Ian Schreiber, Game Balance Concepts | 2010-08-25 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/08/25/level-8-metrics-and-statistics/ | 1252 |
| W05 | 7.2.4.1. Confidence intervals | NIST/SEMATECH e-Handbook of Statistical Methods | undated; accessed 2026-10-21 | VERIFIED | https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm | 1264 |
| W06 | Luau syntax by example: Number literals | Luau documentation | undated living documentation; accessed 2026-10-21 | VERIFIED | https://luau.org/syntax/ | 1276 |
| W07 | Numbers | Roblox Creator Hub | undated living documentation; accessed 2026-10-21 | VERIFIED | https://create.roblox.com/docs/luau/numbers | 1288 |
| W08 | Level 10: Final Boss | Ian Schreiber, Game Balance Concepts | 2010-09-08 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/09/08/level-10-final-boss/ | 1300 |
| C01 (= M02) | The Math of Idle Games, Part III (register line: "C01 aliases M02") | Anthony Pecorella / Kongregate | 2017-01-12; author republication 2021-07-30 | VERIFIED published historical formulas; EXPERIENCE analysis | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii (date provenance https://www.sirpinski.com/the-math-of-idle-games-part-iii/) | 732 |
| M01 | The Math of Idle Games, Part I | Anthony Pecorella | 2016-10-04; author republication 2021-07-30 | EXPERIENCE for game model; VERIFIED for explicitly derived arithmetic | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i (date provenance https://www.sirpinski.com/the-math-of-idle-games-part-i/) | 870 |
| M03 | Level 7: Advancement, Progression and Pacing | Ian Schreiber | 2010-08-18 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/08/18/level-7-advancement-progression-and-pacing/ | 884 |
| M05 | The Math of Idle Games, Part II | Anthony Pecorella | 2016-10-28; author republication 2021-07-30 | EXPERIENCE for teaching construction; VERIFIED for calculus | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii (date provenance https://www.sirpinski.com/the-math-of-idle-games-part-ii/) | 908 |

M02 has no register entry of its own: the paper's register line PP:732 is "C01 aliases M02", so the C01 row serves both ids. M04 (alias of H08) and M06 are not cited in this range.

## 13. Limits the paper states (c)

| ID | PP | Limit (paraphrase) | Handling for the skill writer |
| --- | --- | --- | --- |
| X01 | 444 | The ledger recommendation is analytic, not evidence that several visible currencies improve a game. | Do not cite it as a design finding. |
| X02 | 446 | The identity is bookkeeping, not an optimal economy. Taxes do not cancel; population changes need boundary terms. | State boundary terms in every ledger. |
| X03 | 448 | The price index is analyst-defined, not a Roblox metric. Seller listings can mislead. An average rate misleads when earning changes. | Use executed trades; use the integral for changing rates. |
| X04 | 450 | Roblox's "net near zero" is a heuristic. The paper's view: positive net flow can be intended; a stable aggregate can hide newcomers and veterans. The disagreement is over scope, not the identity. | Present both; never call it a law. |
| X05 | 454, 456 | Clash of Clans changes are documented interventions, not causal retention gains. Do not copy 20% to 10% or the other numbers. | Use as a warning to model the whole bundle. |
| X06 | 458 | No controlled fairness or retention result published for the regional pricing change. | Label as practice, not proof. |
| X07 | 460 | Gift and trade restrictions are examples, not a compulsory transfer design. | Do not state them as required. |
| X08 | 462 | "Legal", "available" and "fair" differ; higher ARPPU does not show a better game for the rest. | Keep nonpayer metrics. |
| X09 | 464, 478 | Not legal advice; not country-by-country; no assurance of compliance. Recheck official pages before launch. | Add the recheck step to every monetization review. |
| X10 | 472 | The 10 Robux / 5% / 200 Robux example is a policy example, not proof of fair value. c/p as the unique fair price is unsupported. n_q does not apply to pity or changing probabilities. | Use conditional failure probabilities for pity. |
| X11 | 474 | Eligibility depends on location, age and platform; Kids/Select membership does not replace per-purchase and per-trade checks. | Check PolicyService per feature. |
| X12 | 478 | "No paid-random restriction" and "rewarded random ad prize allowed" are different policies. Not every ad format is uniformly forbidden to under-13s. | Check each policy separately. |
| X13 | 490, 492, 494 | Spreadsheet practice is reported, not comparative proof. The Spryfox abstract has no audited accuracy. The workflow stack is proposed. | Keep tool advice as OPINION. |
| X14 | 500, 504, 510 | No universal run count; a seeded path is not a distribution; replications do not validate the purchasing policy; policies are stress scenarios. | Declare estimator and precision first. |
| X15 | 512, 514 | The formulas are definitions, not measured pacing. The frozen-rate offline rule fails when production, boosts or auto-purchases change. Not a universal idle mechanic. | Test boundaries before using. |
| X16 | 518, 520, 522 | 2^53 does not make all decimal arithmetic exact; int64 in an API name is not a Luau type; suffixes change display only; floor of product is not product of floors. | Test the smallest unit at maximum balance. |
| X17 | 528 | Arithmetic only: not Roblox, not a live game, not fun, not a global optimum. | Never call it playtesting. |
| X18 | 543, 547, 549 | Statistics show patterns, not causes. Achiever-only time is biased. No causation from an uncontrolled before/after. | Keep denominators and windows. |
| X19 | 553, 557, 559 | Missing immature D7/D30 is not zero. The 12.11%-18.73% value is an illustration. Benchmarks are descriptive and survivor-biased; the pool can change; no universal D1, D7 or minutes ideal; ranking signals are not causal rules. | Never set a benchmark as a target. |
| X20 | 565, 567, 569 | LogProgressionEvent has no provided chart; no percentile or survival tooling promised; 5 vs 10 resource types unresolved; limits are transport limits, not targets; charts take about 24 hours. | Verify with View Events; schema at 5 or fewer. |
| X21 | 573, 584 | Matrix signals are questions; thresholds come from intended pacing, not universal benchmarks. Completer-only time suffers survivor bias; an unreturned player is not permanently churned. | Report completion plus censored duration. |
| X22 | 590, 592 | Under 1,000 DAU is a power warning, not a hard minimum. Early-harm checks do not name a winner. Non-significance is not equivalence. | Combine playtests and longer observation for small teams. |
| X23 | 605, 611, 613 | Spreadsheet-to-game deployment is not shown safe without review; the schema is illustrative; the handoff is not a deployment architecture. | Keep review gates. |
| X24 | 622, 644, 646, 655 | The process is a proposal, not an industry standard; the identity is not an economy target; model pass is not design pass; the checklist is not an empirical threshold set. | Owner may reject a passing model. |
| X25 | 698-706 | No universal wait time, reward count or pace; worked RPG source has no XP rate; plateau and reset value are open; distributions are missing; validation is arithmetic only. | Keep unknowns symbolic. |
| X26 | 710-718 | Five math boundaries (MB1-MB5). | See section 8.2. |
| X27 | 722-726 | GDC sources are session descriptions; tool differences reflect problem complexity; no universal best first-session duration, monthly speed, wall length or fun-certifying agent. | See section 8.3. |

## 14. Possible issues (extractor), not fixed (d)

All are "(extractor) possible issue". I did not change or resolve any of them.

| ID | PP | Item | Why it looks off |
| --- | --- | --- | --- |
| Z01 | 446, 481, 482 | The paper tags its own derivations VERIFIED (accounting identity, "VERIFIED derivation", "VERIFIED algebra") with source "Author derivation". PP:15 (lookup) defines VERIFIED as a source publishing the rule. | Same pattern as part 1 issue Z04. Treat these as derived, not externally sourced. |
| Z02 | 446, 481, 644, 650 | Three forms of the identity. PP:446: population total, no transfers, no adjustment term, plus a prose list of boundary additions. PP:481: B′ = B + S − K plus boundary adjustments. PP:644: per currency per interval with transfersIn and transfersOut and no adjustment term in the equation, though cap loss, conversion and rounding are "recorded as named adjustments". PP:650 adds "+ named adjustments" and "net transfers" in the equation. | The sign convention of the adjustments is not given, and the paper does not say whether cap loss counts as destroyed currency K. Fact-check and decide a single form before the skill is written. |
| Z03 | 446, 448 | Symbol B means total population balance in PP:446 and a single player's usable balance in PP:448. C, r, t have no stated units or domains; r's unit appears only at PP:512. | Variable reuse. Definitions in section 9 are (extractor). |
| Z04 | 448 | "Solve the cumulative-earnings integral" is named, but no integral or rate function is written. | Gap: the paper gives no formula for variable r(t). |
| Z05 | 450 | The statement that Roblox's dashboard exposes source/sink categories and average wallet balances cites R01 (Economy events); the dashboard page is R12. | Check which Roblox page says it. |
| Z06 | 458 | Paper says "local-cost pricing" in "more than 100 countries"; the R04 register title and quotation use the words "global pricing" (register: "we're rolling out global pricing across more than 100 countries"). The register quotation does not mention the donation restriction. | Terminology differs; the donation claim is not covered by the register quotation. Check R04. |
| Z07 | 460, 484 | The paper says "Managed Pricing"; the R05 register title is "Regional pricing" (quotation: "never be discounted by more than 70%"). The class that owns GetUsersPriceLevelsAsync, and its parameters and return, are not stated. The rule-table title (PP:484) mentions arbitrage; the body paragraph (PP:460) never does. | Check names and the API owner in R05. 30%-100% is consistent with a 70% maximum discount (HC7). |
| Z08 | 466 | "Subject to its stated rounding-display treatment": the treatment is never stated. | Fact-check against R06 what the rounding rule is; the skill must not paraphrase a rule the paper omits. |
| Z09 | 472 | c is used but not defined (paper defines p, n, q). HC2 shows 10 / 0.05 = 200 equals the Roblox alternative, but the paper does not say so; it says the 200 is not proof of fair value. n is not said to be an integer. | (extractor) read c as price per trial. |
| Z10 | 474 | "June 16" has no year (R08 date gives 2026-06-16). "Requires PolicyService checks" is attributed to R07, a help article whose register quotation is about pushy messages. "Linked parents ... until age 13" and "5-8 / 9-15" are given with no more detail. | Fact-check each part against R07 and R08. |
| Z11 | 476, 478 | Thresholds differ and could be confused: personalized ads under 18; rewarded video 13+; no rewards for engaging with ads under 13. PP:478 warns against calling every ad format forbidden to under-13s. Not contradictory but easy to merge. | Keep as three separate rules. Check R09. |
| Z12 | 553 | Only D7 is defined in words. D1 and D30 definitions, and the unit of X in "X minutes", are not given in the text. | The spec asked for D1/D7/D30 definitions; the paper supplies the D7 wording and the general Dk rule (PP:595). |
| Z13 | 557 | The paper does not say which retention metric the 12.11%-18.73% example describes beyond "D1 example", or how fallback to genre and all experiences is triggered. | Check R12. |
| Z14 | 563 | The server-only rule for "economy/funnel/custom events" cites R01 and R13 (economy events and the API reference); funnel (R15) and custom events (R16) are not cited for it. LogEconomyEvent is described in prose; no parameter names, enum names or types. | Open R13 for the exact signature before writing code. |
| Z15 | 565 | The R15 register quotation says filters apply only to the first funnel step; the paper says attribution and filters use entry-time values and gives the device example. The paper does not say which method takes funnelSessionId. | Check R15 for both statements. |
| Z16 | 567 | "Convenience methods for each state" are not named. R16's register quotation ("Events are aggregated daily") is not reflected in the paper text. | Check R13 and R16. |
| Z17 | 569 | The paper says event types lists 10 resource types and R01/R13 say 5, but cites "R01; R13-R14" together. What "resource types" means is not defined. "3 custom fields" is not said to be per event. CCU and the scope of "global" requests per minute are not defined. | Check R14 against R01 and R13; resolve before relying on either limit. |
| Z18 | 573 | The matrix says it is grounded in R01 and R10-R16 and omits R17, though DM5 and DM7 point to randomized tests. | Low risk. |
| Z19 | 522 | The math.floor documentation claim cites W07 (Numbers page); the rounding function may be documented in the math library reference instead. | Check W07. |
| Z20 | 502 | W05 is cited for both Wilson and exact binomial methods; the register quotation names only the exact binomial method. | Check W05 for the Wilson method and the small-sample warning. |
| Z21 | 490, 605 | W01's register author list has six names; the paper never says who presented Merchant Guilds or what "Retora" is, and writes "Apps Scripts". W01's session date is not established. | Check W01; do not credit a person. |
| Z22 | 528 | The 2550-equality script is the paper's own execution, tagged VERIFIED with no source id, and the script and its output are not in the range or repo. It also mentions "displayed timelines" while PP:17 (lookup) says timelines stay symbolic. | Not checkable from this range. Treat as unverified. |
| Z23 | 569, 590 | Section 9's experiment limits (14-60 days, 2 variants + control, under 1,000 DAU) all rest on one page (R17); limits like 3 custom fields rest on one page (R14) that conflicts with two others on resource types. | Single-source Roblox claims: fact-check against the live page. |
| Z24 | 626 | Step PS2 points to "Section 2" (feeling timeline), the paper's own section 2, outside this range. | Cross-reference only; part 1 holds section 2. |
| Z25 | 644 vs 646 | PC1 cites W08 for the conservation check, but the paper does not say W08 gives the check itself, only "distinctions". | Check W08. |
| Z26 | 650 vs 595 | Rule-table row PT2 writes "net transfers" as one term; PP:644 splits into transfersIn and transfersOut. | Same as Z02; cosmetic. |
| Z27 | 710 | "The author's earlier root-versus-log explanation" is ambiguous: the paper's author or the M02 author (Pecorella). Part 2 (I5) reads it as an M02 self-correction. | Check M02 and part 2. |
| Z28 | 710-718 | The additional boundaries paragraph and its items are untagged; the surrounding sections tag every paragraph. M01-M05 are named as source ids with no dates in the paragraph. | Tags are blank by the paper, not omitted by me. |
| Z29 | spec | The lead's spec groups "R03-R05 industry". R03 and R04 are Supercell pages; R05 is a Roblox page (regional pricing) and is listed in 11.1. | Confirm grouping with the lead. |
