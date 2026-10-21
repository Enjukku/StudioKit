---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J011-T02, Progression_Designer_Research_2026.txt lines 230-439"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Progression paper part 2: incremental math, RPG math, reward timing and ethics (lines 230-439)

Paraphrased notes. The paper (PP) stays outside git. Every row cites `PP:<line>`. Nothing here is fact-checked: claims are the paper's, listed in section 5 for the fact-check pass. The one thing I did check is arithmetic: I recomputed the Lemonade table, the T_K form, the incomes, the M05 table, the RPG table, the 5-HP example and 0.416 with exact fractions (section 4). I had no web access, so no source was opened.

## 0. How to read

| Key | Meaning |
| --- | --- |
| PP:n | Line n of `Progression_Designer_Research_2026.txt`. One paragraph = one line. Source register = PP:728-1310. |
| Tag | VERIFIED (a source publishes it, or a study measured it in its population and method), EXPERIENCE (a studio or designer's own account), OPINION (the paper's own proposal, source O00, dated 2026-10-21, "not an external empirical source"). Tags are copied from the paper. Where a paragraph carries two tags, both are kept. "tag not stated" = the paper gives no tag word for that sentence. |
| "VERIFIED derivation" | The paper uses VERIFIED also for its own algebra (source "this paper, 2026-10-21", i.e. O00). That is a calculation, not an external source. Section 9 lists it; section 4 shows my recomputation. |
| Src | Paper source id with its date. M01-M06 and H01-H12 resolve in section 7. M02 sits in the register as `C01 aliases M02`; H08 is an alias of M04. |
| Units | The paper gives no units for most symbols. Units, domains and index origins marked "(extractor)" are my reading of the paper's definitions, added so each formula is complete. They are not paper text. |
| Row IDs | I fact row, FM formula card, L Lemonade row, G generator-chain row, RP RPG row, H study, W design choice, E evidence difference, T rule-table row (TI, TR, TW), FC claim, FR formula test, S source, LM limit, XI possible issue. |
| Plain text | All formulas are plain text. `·` = multiply, `^` = power, `Σ(a…b)` = sum from a to b, `⌈ ⌉` = ceil, `⌊ ⌋` = floor. |

## 1. Section 4: incremental and simulator progression (PP:230-283)

### 1.1 What the sources report

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| I1 | 232 | M01 reports exponential prices, linear generator output with milestone multipliers, and closed-form bulk purchases. | EXPERIENCE | M01, 2016-10-04 |
| I2 | 232 | Lemonade example inputs: price growth 1.07, output 1.67 per second, first generator free, second generator costs 4, x2 boosts stacking at 25 and at 50 owned. | EXPERIENCE | M01, 2016-10-04 |
| I3 | 232 | Boundary: the printed base 3.738 and the example value 7.87 are rounded in the source. Do not promote them to exact game constants. (The paper does not say what 7.87 measures.) | EXPERIENCE | M01, 2016-10-04 |
| I4 | 232 | Boundary: the author simplifies timed payouts into continuous per-second income. | EXPERIENCE | M01, 2016-10-04 |
| I5 | 242 | M02 separates three prestige inputs: lifetime, maximum-earned and since-reset. It corrects an earlier statement that treated roots as logarithms. | EXPERIENCE | M02, 2017-01-12 |

### 1.2 Formula cards (bulk buying, waits, payback, prestige, offline)

Model for FM1-FM6 (PP:234): b>0 base price, w>=0 current wallet, P current fixed production per second, k a nonnegative integer owned count. Conditional on this abstract model only. The model does not cover a player who spends on something else at the same time.

| ID | PP | Formula (plain text) | Variables, unit, domain, index origin | Boundaries stated | Tag | Src, date |
| --- | --- | --- | --- | --- | --- | --- |
| FM1 | 234 | C(k) = b·r^k | C = next purchase price, currency (extractor). k = owned count, integer >= 0; k = 0 gives the first price C(0) = b. r = price growth factor per owned unit, r > 1 (r = 1 in FM3). | Next cost of the very next unit. | VERIFIED derivation, conditional on the stated model | M01 bulk form 2016-10-04; edge conditions derived 2026-10-21 |
| FM2 | 234, 236 | B(k, n) = b·r^k·(r^n − 1)/(r − 1) | B = total price of n units bought in one batch while k are owned, currency (extractor). n = batch size, n >= 0 (integer is my reading). r > 1. | Valid only while prices stay unchanged exponential. If prices round, discounts change or milestones change prices, sum the actual prices instead. | VERIFIED derivation, conditional | M01 bulk form 2016-10-04; edge conditions derived 2026-10-21 |
| FM3 | 234 | r = 1: B = b·n, and max affordable n = ⌊w/b⌋ | Same symbols. | Special case. | VERIFIED derivation, conditional | derived 2026-10-21 |
| FM4 | 234 | n_max = ⌊log_r(1 + w·(r − 1)/(b·r^k))⌋, then confirm B(k, n) <= w < B(k, n + 1) | w = wallet, currency (extractor), w >= 0. r > 1. n_max integer >= 0. | The log is a floating-point estimate. The inequality, evaluated with the game's authoritative cost arithmetic, decides affordability. | VERIFIED derivation, conditional | derived 2026-10-21 |
| FM5 | 234 | T = max(0, C − w)/P | T = time to next purchase, seconds (extractor). C = next price. P = current fixed production per second, P > 0. | If P = 0 and C > w the purchase is unreachable without another income source. Does not model simultaneous spending elsewhere. | VERIFIED derivation, conditional | derived 2026-10-21 |
| FM6 | 240 | simple payback = C/ΔP | C >= 0 upgrade price. ΔP > 0 fixed incremental output per second the upgrade adds. Result in seconds (extractor). | Not proof that buying it maximizes progress. A payback ranking ignores future unlocks, competing purchases and the chosen terminal objective. | definition: tag not stated; recommendation below OPINION | derivation and recommendation 2026-10-21 |
| FM6a | 240 | Compare explicit policies (immediate purchase, saving for the next tier, milestone pursuit). Do not name a globally optimal policy without stating the objective. | policy comparison | Recommendation. | OPINION | O00, 2026-10-21 |
| FM7 | 242 | Total-entitlement rule: award = max(0, ⌊F(L)⌋ − already_awarded) | F = declared entitlement function of input L (lifetime, maximum or since-reset input, as the design declares). already_awarded = prestige already granted. Units: prestige points (extractor). | Spent prestige is a different variable from already-awarded prestige. | VERIFIED derivation; OPINION accounting recommendation | O00, 2026-10-21 |
| FM8 | 242 | Per-run rule: award = ⌊G(R)⌋ | G = declared per-run function of run input R. | FM7 and FM8 are alternative model definitions, not universal game rules. | VERIFIED derivation; OPINION accounting recommendation | O00, 2026-10-21 |
| FM9 | 242 | If F(x) = A·x^α with A > 0, α > 0, x > 0: reaching z times the entitlement needs z^(1/α) times the input, before rounding | A = scale constant. α = exponent. x = input. z = target ratio of entitlement (z > 0 is my reading; the paper gives no domain). | Do not take A, α or the reset threshold from another game's feel. Rounding (floor) comes after. | VERIFIED derivation | O00, 2026-10-21 |
| FM10 | 244 | Offline: earned = η·P_saved·min(Δt, T_cap) | η = offline efficiency (no domain given; dimensionless in my reading). P_saved = production per second at the chosen snapshot. Δt = time away, seconds. T_cap = offline cap, seconds. | Constant-rate snapshot only. Uncapped: drop the min. Changing output: integrate P(t) over the allowed interval. | OPINION model contract; VERIFIED integration conditional on contract | O00, 2026-10-21 |
| FM11 | 244 | Offline policy inputs the approved design must supply: η, the cap, whether upgrades auto-buy, whether generators generate other generators, whether buffs expire. | design inputs | The paper invents no cap and no efficiency. Offline production is a policy input, not a law. | OPINION | O00, 2026-10-21 |

### 1.3 Worked incremental model: Lemonade (PP:246-261)

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| L1 | 248 | Analysis condition: one owned free generator, empty wallet, no other purchases, immediate sequential reinvestment. This selects a state and a policy, not new tuning constants. It is a reindexed reading of M01's simplified Lemonade model, not a reconstruction of current AdVenture Capitalist. The source's 1.67 is used as an exact input to this simplified model only; the real timer behavior and any hidden precision stay outside the model. | EXPERIENCE inputs; conditional analysis, VERIFIED arithmetic | M01, 2016-10-04; analysis 2026-10-21 |
| L2 | 248, 250 | C(k) = 4·(107/100)^(k − 1) and P(k) = (167/100)·k for k < 25. k = owned count, integer, k >= 1 (k = 1 is the free generator) (extractor). C(k) = price in currency of the next generator while k are owned (C(1) = 4, the published second-generator price). P(k) = income per second while k are owned. Domain here: 1 <= k <= 24. | EXPERIENCE inputs; VERIFIED arithmetic | M01, 2016-10-04; 2026-10-21 |

Paper table (PP:252-257), exact values, copied as numbers:

| ID | PP | Owned before → after | Exact price | Income/second before | Exact wait, seconds | Exact cumulative time, seconds |
| --- | --- | --- | --- | --- | --- | --- |
| L3 | 253 | 1→2 | 4 | 167/100 | 400/167 | 400/167 |
| L4 | 254 | 2→3 | 4.28 | 3.34 | 214/167 | 614/167 |
| L5 | 255 | 3→4 | 4.5796 | 5.01 | 11449/12525 | 57499/12525 |
| L6 | 256 | 4→5 | 4.900172 | 6.68 | 1225043/1670000 | 26674729/5010000 |
| L7 | 257 | 5→6 | 5.24318404 | 8.35 | 131079601/208750000 | 465947491/78281250 |

Table tag: VERIFIED arithmetic on EXPERIENCE inputs (M01, 2016-10-04; 2026-10-21). Hand check of all five rows: section 4.

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| L8 | 259 | Compact exact form with r = 107/100: T_K = (400/167)·Σ(j=1…K−1) r^(j−1)/j, for K <= 25. T_K = elapsed seconds on owning K generators (K integer, 2 <= K <= 25; (extractor) range). The x2 gained at 25 changes production after that purchase, not the wait to buy it. The factored form may replace the large fractions without rounding. | VERIFIED derivation | 2026-10-21 |
| L9 | 261 | On this early route waits shrink although prices grow exponentially, because the first proportional output gain is larger than the price growth. Not a guarantee that waits shrink forever. | VERIFIED derived interpretation | M01 inputs; 2026-10-21 |
| L10 | 261 | Incomes: 40.08 at 24 owned, 83.5 at 25, 163.66 at 49, 334 at 50. Exact finite decimals from the published parameters, not recommended Roblox targets. Source milestones plus count growth make the jump. | VERIFIED exact arithmetic | M01 inputs; 2026-10-21 |
| L11 | 261 | No prestige timeline is claimed: the one-generator excerpt gives no complete prestige configuration. | VERIFIED (scope statement) | 2026-10-21 |
| L12 | 232, 250, 261 | (extractor) The paper writes P(k) only for k < 25. Its incomes at 25, 49 and 50 equal 2·(167/100)·25, 2·(167/100)·49 and 4·(167/100)·50, i.e. x2 for 25 <= k < 50 and x4 (stacked) from 50. The paper does not write this piecewise form. | (extractor) | derived from PP:232, 261 |
| L13 | 250, 261 | (extractor) From the paper's own C and P, the wait w_k = 4·r^(k−1)/((167/100)·k) falls until k = 15 (0.41174 s) and rises after that, until the k = 24 purchase. This agrees with L9's caveat; "waits shrink" holds only for early rows. | (extractor) | recomputed, not paper text |

### 1.4 Continuous generator chain (M05) (PP:263-277)

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| G1 | 265 | Setup: one fixed second-tier generator; zero first-tier generators; zero currency. Second tier makes first-tier generators at 1 per second. Each first-tier generator makes currency at 1 per second. | EXPERIENCE teaching model; VERIFIED derivation | M05, 2016-10-28 |
| G2 | 265, 267 | Continuous equations: G_1(t) = t and C(t) = t^2/2. t = time in seconds, t >= 0 (extractor). G_1 = number of first-tier generators (fractional allowed). C = currency. | same | M05, 2016-10-28 |
| G3 | 269-275 | Table, t (s) → G_1 → C exact: 0→0→0; 1→1→1/2; 2→2→2; 3→3→9/2; 4→4→8; 5→5→25/2. | VERIFIED derivation | M05 2016-10-28; 2026-10-21 |
| G4 | 277 | Model boundary: the published model allows fractional in-progress production. A simulator that makes integer generators only at tick boundaries is a different model; it must state whether a new generator produces during its creation tick. A difference from t^2/2 is not automatically a bug. | VERIFIED model distinction (M05 itself describes continuous vs discrete) | derived 2026-10-21; M05 2016-10-28 |

### 1.5 Rule-table rows (PP:279-283)

| ID | PP | Rule | Formula or number | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| TI1 | 280 | Batch only unchanged exponential prices | B(k, n) = b·r^k·(r^n − 1)/(r − 1) | VERIFIED derivation | M01, 2016-10-04 |
| TI2 | 281 | Derive actual waits, not merely costs | max(0, C − w)/P | VERIFIED conditional | this paper, 2026-10-21 |
| TI3 | 282 | Specify the prestige accounting base | lifetime, maximum and run are different | EXPERIENCE | M02, 2017-01-12 |
| TI4 | 283 | Declare offline policy rather than copying a cap | η, P_saved, T_cap remain inputs | OPINION | this paper, 2026-10-21 |

## 2. Section 5: RPG and action progression (PP:285-329)

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| RP1 | 287 | M04 reports Baldur's Gate: Dark Alliance XP needs: 1000 for level 1→2, 2000 for 2→3, 3000 for 3→4, "continuing". Level-up points gained: 1, 2, 3. M04 also has a separate teaching example (enemies with 5 HP, damage changing 4 to 5). The two examples must not be merged into one game's combat setup. | EXPERIENCE | M04, 2010-07-14 |
| RP2 | 291 | Model from M04's reported relation: XP needed from level l to l+1 = 1000·l. Cumulative threshold X_l = 500·l·(l − 1). Cumulative ability points A_l = l·(l − 1)/2. So X_l = 1000·A_l exactly at thresholds. l = level, integer >= 1 (extractor). X_l = cumulative XP to reach level l (X_1 = 0). A_l = cumulative points at level l (A_1 = 0). | VERIFIED derivation from EXPERIENCE source | M04, 2010-07-14 |

Level table (PP:295-301), header: Level, Cumulative XP, Cumulative points, XP to next level, Time at fixed q XP/second.

| ID | PP | Level | Cumulative XP | Cumulative points | XP to next level | Time at fixed q (XP/s) |
| --- | --- | --- | --- | --- | --- | --- |
| RP3a | 296 | 1 | 0 | 0 | 1000 | 0 |
| RP3b | 297 | 2 | 1000 | 1 | 2000 | 1000/q |
| RP3c | 298 | 3 | 3000 | 3 | 3000 | 3000/q |
| RP3d | 299 | 4 | 6000 | 6 | 4000 | 6000/q |
| RP3e | 300 | 5 | 10000 | 10 | 5000 | 10000/q |
| RP3f | 301 | 6 | 15000 | 15 | 6000 | 15000/q |

Table tag: VERIFIED conditional derivation (PP:291, 303). Hand check: section 4.

| ID | PP | Item | Tag | Src, date |
| --- | --- | --- | --- | --- |
| RP4 | 303 | The source gives no acquisition rate q, no encounter schedule and no combat stats for this table. A minutes timeline, a first-day target or a coupled combat simulation would invent inputs. The exact timeline stays symbolic: with segment rates q_l > 0, reaching level L takes Σ(l=1…L−1) 1000·l/q_l seconds (q_l in XP per second, extractor). Real runs with XP bursts and downtime need the measured event stream, not a constant-segment simplification. Do not read Schreiber's general examples as a current studio spec. | VERIFIED conditional derivation / evidence limitation | 2026-10-21 |
| RP5 | 307, 309 | N = ⌈H/d⌉ hits and TTK = t0 + (N − 1)·τ. H > 0 enemy health. d > 0 fixed effective damage per successful hit. τ > 0 attack spacing in seconds (extractor). t0 = time of first hit: t0 = 0 if starting immediately, t0 = τ if windup is a full attack period. N integer >= 1. H/(d/τ) is a continuous approximation and can differ from either discrete convention. Same rule gives TTD (player health vs incoming damage), but TTD against an enemy assumed to live forever is not the duel result: a killed enemy may never land its next strike. | VERIFIED mathematical derivation | this paper, 2026-10-21; breakpoint motivation M04, 2010-07-14 |
| RP6 | 311 | M04's separate 5-HP example: damage 4 needs 2 hits, damage 5 needs 1. With t0 = 0 kill times are τ and 0. With t0 = τ they are 2τ and τ. No attack speed is invented. 4→5 is a 25% damage gain but halves the hit count. A smoothly fitted damage curve does not give smooth encounter length. | VERIFIED derived from M04's example; not Dark Alliance combat data | M04, 2010-07-14 |
| RP7 | 313 | Explicit deterministic duel: list event times for both sides; apply attack, cast and recovery timing, mitigation, invulnerability, shield and healing; stop at the real death event; define simultaneous-hit priority. Stochastic damage: sample the process or solve its distribution. ⌈H/E[D]⌉ is generally not the expected hit count when per-hit damage is random; expected DPS is not expected TTK. Variable attack sequence d_i: hits-to-kill = the smallest n with Σ(i=1…n) d_i >= H. | VERIFIED derivation; OPINION implementation recommendation | this paper, 2026-10-21 |
| RP8 | 317 | Versioned studio formula: Blizzard's Season of Blood article combines an 18% additive Vulnerable bonus with a 20% multiplicative base as (1.18)(1.2) − 1 = 0.416, a 41.6% bonus. It states monsters were rebalanced around the changed player damage. A 2023 historical change, not the 2026 Diablo damage spec. | VERIFIED | M06, 2023-10-10 |
| RP9 | 319, 321 | For damage reduction fraction ρ with 0 <= ρ < 1: effective health against that damage type = H/(1 − ρ). Keep additive and multiplicative stacking separate in the table schema; label damage type and conditional uptime. Expected DPS can rise while the kill breakpoint stays. A defensive item can be irrelevant against a bypassing attack. | VERIFIED generic derivation | model definition 2026-10-21; studio motivation M06, 2023-10-10 |
| RP10 | 323 | M03 describes a practitioner pattern: more challenge on entering an area, small player gains, a boss challenge, then a power rise after the boss. M03 denies that it is universal. | EXPERIENCE | M03, 2010-08-18 |
| RP11 | 323 | Define each difficulty band as a named encounter/build pairing, not a universal level multiplier. For each approved player build and enemy archetype export: HP, effective hit damage, attack timing, hit-count breakpoints, TTK, TTD, recovery cost. Label boss mechanics apart from stats (a multiplier table cannot hold an invulnerability phase or a positioning demand). The creative director approves the intended encounter feel; players then test that hypothesis. | OPINION | this paper, 2026-10-21 |

Rule-table rows (PP:325-329):

| ID | PP | Rule | Formula or number | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| TR1 | 326 | Use discrete kill breakpoints | N = ceil(H/d) | VERIFIED derivation | M04 motivation; this paper, 2026-10-21 |
| TR2 | 327 | State first-hit timing | TTK = t0 + (N − 1)·τ | VERIFIED derivation | this paper, 2026-10-21 |
| TR3 | 328 | Tune enemies together with player formula changes | 18% additive and 20% multiplicative yield 41.6% | VERIFIED published arithmetic / EXPERIENCE intent | M06, 2023-10-10 |
| TR4 | 329 | Do not manufacture minutes from XP thresholds | t = Σ e_l/q_l | VERIFIED conditional | M04 plus derivation 2026-10-21 |

(extractor) In TR4, e_l is not defined in PP:230-439 (X_l = Σ e_j is at PP:226, outside my range). By PP:303 it reads e_l = 1000·l, l = 1…L−1, matching RP4.

## 3. Section 6: reward timing and ethical pacing (PP:331-438)

### 3.1 The twelve studies (H01-H12)

Each row: finding as the paper states it, design, population and sample sizes, limits the paper states, tag, date, and what the paper says it read (last word of each paragraph). Where the paper gives no size or age, the cell says "paper gives none"; I supply nothing.

| ID | PP | Finding (paraphrase) | Design | Population and sizes | Paper's stated limits | Tag | Date; what was read |
| --- | --- | --- | --- | --- | --- | --- | --- |
| H01 | 335-339 | Ryan, Rigby, Przybylski: perceived autonomy and competence are associated with enjoyment across game studies. Relatedness also predicted enjoyment in the MMO survey. | Four studies; Studies 1-3 laboratory, Study 4 online survey. Study 2 randomized game order, not autonomy. | Undergraduate laboratory samples of 89, 50 and 58 (Studies 1-3). Study 4: 730 online-community members aged 16-44, mostly male. | Need/enjoyment links are largely correlational. It is not an experiment showing that a particular progression tree causes retention. | VERIFIED | 2006; "Paper" |
| H02 | 341-345 | Deci, Koestner, Ryan: expected tangible rewards and several contingent reward categories lowered free-choice intrinsic motivation; positive feedback raised it. | Meta-analysis of 128 experiments. | Includes children and college students. Tangible-reward effects worse for children. Paper gives no other sizes. | Experimental evidence; results depend heavily on how reward and outcome are defined. Mostly controlled tasks, not persistent commercial games. Virtual loot, feedback and real-money incentives are not interchangeable treatments. | VERIFIED | November 1999; "Abstract" |
| H03 | 347-351 | Cameron, Banko, Pierce: rejects the claim that rewards have pervasive negative effects; effects depend on initial task interest, reward expectation and link to performance. | Competing meta-analysis (re-analysis of experimental literature). | Paper gives none. | Not an independent live-game replication. Real methodological disagreement with H02. Neither supports "all rewards help" nor "all rewards harm". | VERIFIED | spring 2001; "Article" |
| H04 | 353-357 | Mekler et al.: points, levels and leaderboards raised the number of annotations without a significant gain in intrinsic motivation or competence. | 2×4 online experiment; image-annotation task. | Paper gives none (the accessible abstract states no sample size or age; none supplied). | Not entertainment gameplay. Task output is not a measure of enjoyment. | VERIFIED | 1 June 2017; "Institutional record" |
| H05 | 359-363 | Fong, Zaleski, Leach: moderate link between challenge-skill balance and flow, smaller link to intrinsic motivation. Clear goals and control also contributed. | Meta-analysis of 28 studies. | Several domains; no age breakdown; no numeric effect size claimed. | Abstract supports associations only, with contextual moderators; no universally best difficulty ratio. Full publisher page was not reachable; only the publisher abstract was checked. | VERIFIED | 2015 issue; "Publisher abstract" |
| H06 | 365-369 | Daniel Cook: skill-atom model links decision, action, simulation, feedback and mental-model revision into learning chains. "Burnout" = mastering a skill without finding a further interesting use. | Designer framework (not a controlled study). | Not applicable; paper gives none. | Not a controlled study nor a clinical definition. Useful for mapping prerequisites and uses; do not repeat its neuroscience explanations as established evidence. | EXPERIENCE | 19 July 2007, repost 13 March 2021; "Author's repost" |
| H07 | 371-375 | Raph Koster: fun as learning patterns; boredom follows mastery; advocates increasingly readable, renewable challenges. | Designer op-ed. | Not applicable; paper gives none. | Not comprehensive psychology; no proof that all enjoyment is learning. Do not exclude comfort, socializing, expression by treating this lens as law. | EXPERIENCE | 15 May 2005, page updated 28 March 2014; "Author's essay" |
| H08 | 377-381 | Ian Schreiber: linked XP→level→upgrade and time→XP relations must be studied together; a rising XP threshold alone does not describe real reward pacing. | Educational worked examples (course lesson). | Not applicable; paper gives none. | Not measured player experience; not a present-day balance audit of the example game. | EXPERIENCE | 14 July 2010; "Course lesson" |
| H09 | 383-387 | Woolley, Fishbach: in their studies, earlier rewards could raise intrinsic motivation. | Experiments comparing earlier vs delayed rewards. PubMed classes it a randomized controlled trial. | News-viewing and experimental tasks; adult participants per PubMed; the checked abstract gives no full ages or sample sizes. | Not Roblox progression. Supports testing timing, not a seconds-per-reward rule. | VERIFIED | June 2018; "Abstract" |
| H10 | 389-393 | Liu et al.: immediate bonuses gave higher reported intrinsic motivation than delayed ones. | Randomized groups; reading tasks; immediate vs delayed bonus. | South China Normal University participants aged 17-26. Analyzed samples 87 (1a), 58 (1b), 58 (2), 144 (3). | Short, monetary-bonus experiments; no claim about long-term game enjoyment or a universal reward size. | VERIFIED | 16 May 2022; "Full article" |
| H11 | 395-399 | Montiel et al.: 16 empirical loot-box studies, all cross-sectional, mostly convenience samples; engagement was generally linked to problematic gaming/gambling. | Scoping review of primary studies. | Only six of the 16 included adolescents. | Definitions, samples and engagement types differed. Associations do not show direction of cause, and do not show that every random free drop equals a paid loot box. | VERIFIED | 27 January 2022; "Review" |
| H12 | 401-405 | Ballou et al.: playtime did not predict measured well-being; perceived fit of gaming with life was linked to it. | Analysis of an adult sample; the paper does not name the design type. Authors call the findings non-causal; equivalence tests inconclusive. | 703 casually engaged US adults; 150 Switch games. | Adults and one hardware ecosystem. Not evidence for children, Roblox, every intensive player, or zero harm. Does not measure an optimal progression schedule. | VERIFIED | 12 March 2025; "Article record" |

(The last column's "what was read" words are the paper's own labels. H12's design type is not named in the paper.)

### 3.2 The paper's design choices

| ID | PP | Statement (paraphrase) | Tag | Src, date |
| --- | --- | --- | --- | --- |
| W1 | 409 | Reward research is not unanimous and timing can change results. Earlier bonuses helped in specific experiments while other reward arrangements lowered free-choice motivation in meta-analyses. These are not clean contradictions: tasks, contingencies, comparison conditions and measurement windows differ. | VERIFIED | H02, H03, H09, H10 (dates in 3.1) |
| W2 | 411 | Four clocks, kept apart: (1) feedback after an action; (2) completion of a small objective; (3) a consequential upgrade; (4) new content or mastery. | OPINION | H02-H04, H09, H10; O00 2026-10-21 |
| W3 | 411 | Make feedback understandable, but not every feedback event should grant currency or unlock a system. Test each layer's timing and usefulness on its own. | OPINION | same |
| W4 | 411 | These sources support neither "reward every 30 seconds" nor "always delay rewards" as a universal rule. | OPINION | same |
| W5 | 413 | Use surprise to vary routes, combinations, presentation or optional discoveries; keep the cost and the basic entitlement understandable. Randomness does not replace authored interesting results. | OPINION | H01, H06, H11; O00 2026-10-21 |
| W6 | 413 | Essential progression: prefer a deterministic path or a visible bounded fallback over an unbounded luck requirement. If a guarantee exists, state what advances its counter, whether it persists, what resets it; test unlucky paths, not only the average. | OPINION | same |
| W7 | 415 | Ethical policy (motivated by H11, not proven by it): do not tailor bad luck or friction to push purchases; do not imply a near miss improves the next independent chance; avoid losing earned progress for missing a day; avoid purchases triggered by invented emergencies; avoid paid power needed to escape deliberately slowed pacing. | OPINION | H11; O00 2026-10-21 |
| W8 | 415 | Transparency and a pity counter are safeguards, not evidence that a paid random system is harmless. Roblox eligibility, odds and purchase rules are in a separate policy section (outside this range). | OPINION | H11; O00 2026-10-21 |
| W9 | 417 | Stopping freedom: give goals natural finish points, save reliably, show a clear next goal, let a player leave without losing earned rewards. A voluntarily finished session is not automatically a retention failure. Measure enjoyment and perceived freedom next to return behavior; do not optimize for inability to stop. These are value choices, not causal claims that shorter sessions improve health. | OPINION | H01, H12; O00 2026-10-21 |

### 3.3 Where the evidence differs (PP:419-431)

| ID | PP | Item | Tag | Src |
| --- | --- | --- | --- | --- |
| E1 | 421 | H02 and H03 disagree on how widely rewards undermine intrinsic motivation. Report the task-interest and reward-contingency distinction; choose no slogan. | VERIFIED | H02 (1999), H03 (2001) |
| E2 | 423 | Challenge-skill balance relates to flow, but strength varies by context and measure. Setting enemy stats equal to player stats does not guarantee flow. | VERIFIED | H05 (2015) |
| E3 | 425 | Mastery models (H06, H07) are design lenses. Experimental gamification evidence shows numeric progress markers alone need not raise intrinsic motivation. The sources ask different questions and are not replications of each other. | EXPERIENCE vs VERIFIED | H06, H07 vs H01, H04 |
| E4 | 427 | Loot-box associations justify caution; the reviewed cross-sectional work cannot show cause or cover every unpaid reward mechanic. | VERIFIED | H11 (2022) |
| E5 | 429 | A non-causal adult study with no playtime link does not prove every design safe; longer playtime alone is not shown to be harm. | VERIFIED | H12 (2025) |
| E6 | 431 | Unknowns to test locally: wanted reward intervals, acceptable repetition, difficulty transitions, felt fairness, stopping freedom, how long novelty lasts. No evidence here gives a Roblox-wide answer. The paper does not assume all Roblox players are children. | OPINION | synthesis, O00 2026-10-21 |

### 3.4 Rule-table rows (PP:433-438)

| ID | PP | Rule | Formula or number | Tag | Src, date |
| --- | --- | --- | --- | --- | --- |
| TW1 | 434 | Do not equate task output with intrinsic motivation | Points, levels and leaderboards raised output without the same motivational gain | VERIFIED within study | H04, 2017-06-01 |
| TW2 | 435 | Preserve disagreement about contingent rewards | Different reward definitions and outcomes matter | VERIFIED review findings | H02, 1999; H03, 2001 |
| TW3 | 436 | Avoid universal reward intervals | No verified Roblox-wide seconds-per-reward target | OPINION synthesis | O00, 2026-10-21 |
| TW4 | 437 | Keep paid random risk evidence qualified | Reviewed studies were cross-sectional | VERIFIED review scope | H11, 2022-01-27 |
| TW5 | 438 | Test meaningful progression and voluntary stopping | Engagement alone is not proof of enjoyment | OPINION | O00, 2026-10-21 |

## 4. Hand check record (check C5)

Done by me with exact fractions (Python `fractions`), not by reading the paper's text. All values below match the paper.

Lemonade, r = 107/100, wait(k) = C(k)/P(k) = 4·r^(k−1)/((167/100)·k):

| Step | Price C(k) | P(k) | Wait (paper) | Wait (recomputed) | Cumulative (paper) | Cumulative (recomputed sum) |
| --- | --- | --- | --- | --- | --- | --- |
| 1→2 | 4 | 167/100 | 400/167 | 400/167 = 2.39521 | 400/167 | 400/167 |
| 2→3 | 107/25 = 4.28 | 167/50 = 3.34 | 214/167 | 214/167 = 1.28144 | 614/167 | 400/167 + 214/167 = 614/167 |
| 3→4 | 11449/2500 = 4.5796 | 501/100 = 5.01 | 11449/12525 | 11449/12525 = 0.91409 | 57499/12525 | 614/167 = 46050/12525; + 11449/12525 = 57499/12525 |
| 4→5 | 1225043/250000 = 4.900172 | 167/25 = 6.68 | 1225043/1670000 | equal = 0.73356 | 26674729/5010000 | equal (= 5.32430) |
| 5→6 | 131079601/25000000 = 5.24318404 | 167/20 = 8.35 | 131079601/208750000 | equal = 0.62793 | 465947491/78281250 | equal (= 5.95222) |

Result: all five waits and all five cumulative times match. All fractions are in lowest terms. The closed form T_K = (400/167)·Σ(j=1…K−1) r^(j−1)/j gives the same five cumulative values for K = 2…6. Incomes: P(24) = 1002/25 = 40.08; 2·P(25) = 167/2 = 83.5; 2·P(49) = 8183/50 = 163.66; 4·P(50) = 334. All match. Also: 4/1.07 = 3.7383, consistent with a rounded printed "3.738" being b with k counted from the free generator (my observation only; the paper does not say so).

M05: G_1(t) = t and C(t) = t^2/2 give 0, 1/2, 2, 9/2, 8, 25/2 at t = 0…5. Match.

RPG: for l = 1…6, X_l = 500·l·(l−1) gives 0, 1000, 3000, 6000, 10000, 15000; A_l = l(l−1)/2 gives 0, 1, 3, 6, 10, 15; X_l = 1000·A_l holds in all six rows; XP to next = 1000·l gives 1000…6000; Σ(l=1…5) 1000·l = 15000 = X_6, so Σ 1000·l/q with constant q equals X_L/q. All match.

Other: ⌈5/4⌉ = 2, ⌈5/5⌉ = 1; (1.18)(1.2) − 1 = 0.416 (floating point prints 0.4159999…; exact decimal is 0.416); 25% gain 4→5 true. Geometric sum: Σ(i=0…n−1) b·r^(k+i) = b·r^k·(r^n − 1)/(r − 1). B(k, n) <= w is equivalent to r^n <= 1 + w(r−1)/(b·r^k), which gives FM4. A(s·x)^α = s^α·A·x^α gives s = z^(1/α) in FM9.

## 5. Claims to fact-check (a)

Every VERIFIED or EXPERIENCE claim with a number, formula, version, date, sample size or effect. "Check" says what the fact-checker should open. Derived items marked "derived" are the paper's own math (already recomputed in section 4); a source check is still needed for the inputs.

| ID | Claim | PP | Src | Source date | Tag |
| --- | --- | --- | --- | --- | --- |
| FC01 | M01 Lemonade inputs: growth 1.07, output 1.67/s, first generator free, second costs 4, x2 boosts at 25 and 50 | 232 | M01 | 2016-10-04 | EXPERIENCE |
| FC02 | M01 printed base 3.738 and example 7.87 are rounded numbers | 232 | M01 | 2016-10-04 | EXPERIENCE |
| FC03 | M01 simplifies timed payouts to continuous per-second income | 232 | M01 | 2016-10-04 | EXPERIENCE |
| FC04 | M01 presents exponential prices, linear output with milestone multipliers, closed-form bulk purchase (check the bulk form B(k, n) is in M01 as FM2) | 232, 234, 236 | M01 | 2016-10-04 | EXPERIENCE; bulk form VERIFIED |
| FC05 | M01 date 2016-10-04 (Kongregate republication 2021-07-30; provenance sirpinski.com) | 232; register | M01 | 2016-10-04 | EXPERIENCE |
| FC06 | M02 separates lifetime, maximum-earned, since-reset prestige inputs; corrects roots-vs-logarithms | 242, 282 | M02 (C01 alias) | 2017-01-12 | EXPERIENCE |
| FC07 | Lemonade table: prices 4, 4.28, 4.5796, 4.900172, 5.24318404 and incomes 1.67, 3.34, 5.01, 6.68, 8.35 (derived from FC01 inputs) | 253-257 | M01 inputs | 2016-10-04 | VERIFIED arithmetic |
| FC08 | Lemonade exact waits 400/167, 214/167, 11449/12525, 1225043/1670000, 131079601/208750000 (derived) | 253-257 | M01 inputs | 2016-10-04 | VERIFIED arithmetic |
| FC09 | Lemonade cumulative times 400/167, 614/167, 57499/12525, 26674729/5010000, 465947491/78281250 (derived) | 253-257 | M01 inputs | 2016-10-04 | VERIFIED arithmetic |
| FC10 | T_K = (400/167)·Σ(j=1…K−1) r^(j−1)/j for K <= 25, r = 107/100 (derived) | 259 | M01 inputs | 2016-10-04 | VERIFIED derivation |
| FC11 | Incomes 40.08 (24 owned), 83.5 (25), 163.66 (49), 334 (50) (derived) | 261 | M01 inputs | 2016-10-04 | VERIFIED arithmetic |
| FC12 | M05 setup (one second-tier generator, rates 1 per second at each tier) and result G_1(t) = t, C(t) = t^2/2 | 265, 267 | M05 | 2016-10-28 | EXPERIENCE teaching model; VERIFIED derivation |
| FC13 | M05 table: C = 0, 1/2, 2, 9/2, 8, 25/2 at t = 0…5 (derived) | 269-275 | M05 | 2016-10-28 | VERIFIED derivation |
| FC14 | M05 itself describes the continuous vs discrete boundary | 277 | M05 | 2016-10-28 | VERIFIED model distinction |
| FC15 | M04: Dark Alliance XP 1000, 2000, 3000 for 1→2, 2→3, 3→4, "continuing"; level-up points 1, 2, 3 (check that M04 supports the extension to every level, see XI3) | 287, 291 | M04 | 2010-07-14 | EXPERIENCE |
| FC16 | M04 separate example: 5-HP enemies, damage from 4 to 5 (check that M04's example is about 4 vs 5 damage against 5-HP enemies) | 287, 311 | M04 | 2010-07-14 | EXPERIENCE |
| FC17 | RPG model: 1000·l per level, X_l = 500·l·(l−1), A_l = l(l−1)/2, X_l = 1000·A_l (derived) | 291 | M04 | 2010-07-14 | VERIFIED derivation |
| FC18 | RPG level table rows 1…6 (derived) | 296-301 | M04 | 2010-07-14 | VERIFIED derivation |
| FC19 | M04 gives no acquisition rate q, encounter schedule or combat stats for the XP table | 303 | M04 | 2010-07-14 | VERIFIED limitation |
| FC20 | N = ceil(H/d), TTK = t0 + (N−1)τ (derived) | 307, 309, 326, 327 | this paper | 2026-10-21 | VERIFIED derivation |
| FC21 | 5-HP example: 4 damage → 2 hits, 5 damage → 1 hit; TTK τ and 0 (t0 = 0), 2τ and τ (t0 = τ); +25% damage, hit count halved (derived) | 311 | M04 | 2010-07-14 | VERIFIED derived |
| FC22 | M06: 18% additive Vulnerable bonus and 20% multiplicative base give (1.18)(1.2) − 1 = 0.416 (41.6%); monsters rebalanced around new player power; Season of Blood article 2023-10-10 | 317, 328 | M06 | 2023-10-10 | VERIFIED; intent EXPERIENCE |
| FC23 | Effective health = H/(1 − ρ), 0 <= ρ < 1 (derived) | 319, 321 | this paper; M06 motivation | 2026-10-21 | VERIFIED derivation |
| FC24 | M03 describes the entry-challenge / incremental gain / boss / post-boss power pattern and denies universality | 323 | M03 | 2010-08-18 | EXPERIENCE |
| FC25 | H01: associations of perceived autonomy and competence with enjoyment; relatedness predicted enjoyment in the MMO survey; samples 89, 50, 58 (undergraduates) and 730 (age 16-44); Study 2 randomized game order | 337, 339 | H01 | 2006 | VERIFIED |
| FC26 | H02: 128 experiments; expected tangible and several contingent rewards lowered free-choice intrinsic motivation; positive feedback raised it; tangible-reward effects worse for children | 343, 345 | H02 | 1999-11 | VERIFIED |
| FC27 | H03: competing meta-analysis; no pervasive negative effect; depends on task interest, reward expectation, link to performance | 349 | H03 | 2001 spring | VERIFIED |
| FC28 | H04: 2×4 online experiment; points, levels and leaderboards raised annotation quantity with no significant gain in intrinsic motivation or competence; no sample size in abstract | 355, 357 | H04 | 2017-06-01 | VERIFIED |
| FC29 | H05: meta-analysis of 28 studies; moderate challenge-skill/flow relation, smaller for intrinsic motivation; clear goals and control contributed; issue year 2015 (DOI first published 2014) | 361, 363 | H05 | 2015 issue | VERIFIED |
| FC30 | H06: skill-atom model; burnout meaning; original 2007-07-19, repost 2021-03-13 | 367, 369 | H06 | 2007-07-19 / 2021-03-13 | EXPERIENCE |
| FC31 | H07: fun as learning patterns; boredom after mastery; essay 2005-05-15, page updated 2014-03-28 | 373, 375 | H07 | 2005-05-15 / 2014-03-28 | EXPERIENCE |
| FC32 | H08/M04: linked XP, level, upgrade and time-to-XP relations; a rising threshold alone does not describe pacing; 2010-07-14 | 379, 381 | M04 (alias H08) | 2010-07-14 | EXPERIENCE |
| FC33 | H09: earlier vs delayed rewards; earlier could raise intrinsic motivation; PubMed lists it as an RCT with adults; June 2018 | 385, 387 | H09 | 2018-06 | VERIFIED |
| FC34 | H10: immediate vs delayed bonuses, randomized groups, reading tasks, higher reported intrinsic motivation with immediate bonuses; participants 17-26; analyzed samples 87, 58, 58, 144 (1a, 1b, 2, 3) | 391, 393 | H10 | 2022-05-16 | VERIFIED |
| FC35 | H11: 16 empirical loot-box studies, all cross-sectional, mostly convenience samples, generally linking engagement to problematic gaming/gambling; only six included adolescents | 397, 399 | H11 | 2022-01-27 | VERIFIED |
| FC36 | H12: 703 casually engaged US adults, 150 Switch games; playtime did not predict well-being; perceived fit did; non-causal; equivalence tests inconclusive | 403, 405 | H12 | 2025-03-12 | VERIFIED |
| FC37 | Reward research is not unanimous; timing can change outcomes; earlier bonuses helped in specific experiments (H02/H03/H09/H10) | 409 | H02, H03, H09, H10 | see FC26, 27, 33, 34 | VERIFIED |
| FC38 | E3: experimental gamification evidence shows numeric progress markers alone need not raise intrinsic motivation, cited to H01 and H04 (see XI9) | 425 | H01, H04 | 2006 / 2017-06-01 | EXPERIENCE vs VERIFIED |
| FC39 | Rule row: H04 points, levels and leaderboards raised output without the same motivational gain | 434 | H04 | 2017-06-01 | VERIFIED within study |
| FC40 | Rule row: H11 reviewed studies were cross-sectional | 437 | H11 | 2022-01-27 | VERIFIED review scope |

## 6. Formulas to reproduce, with expected values (b)

Values marked "paper" are stated in the paper. Values marked "(extractor test vector)" are computed by me from the paper's own inputs so a tool test has a number; they are not paper text.

| ID | PP | Formula (plain text) | Expected value |
| --- | --- | --- | --- |
| FR1 | 236 | B(k, n) = b·r^k·(r^n − 1)/(r − 1), r > 1 | Paper gives no numeric example. (extractor test vector) b = 4/1.07, r = 1.07, k = 1, n = 2 → 8.28 (= 4 + 4.28, the two published Lemonade prices); n = 1 → 4. |
| FR2 | 234 | r = 1: B = b·n; n_max = ⌊w/b⌋ | No numeric example in the paper. |
| FR3 | 234 | n_max = ⌊log_r(1 + w(r−1)/(b·r^k))⌋, then check B(n) <= w < B(n+1) | No example in the paper. (extractor test vector) the FR1 inputs with w = 8.28 must return n = 2 although a float log may give 1.9999…; the inequality decides. |
| FR4 | 234, 238 | T = max(0, C − w)/P | No example. Edge values (paper): C <= w → 0; P = 0 and C > w → unreachable. |
| FR5 | 240 | payback = C/ΔP | No example in the paper. |
| FR6 | 242 | award = max(0, ⌊F(L)⌋ − already_awarded); per-run: ⌊G(R)⌋ | No example in the paper. |
| FR7 | 242 | F(x) = A·x^α: input ratio for entitlement ratio z is z^(1/α) | No example. (extractor test vector) α = 1/2, z = 4 → 16. |
| FR8 | 244 | earned = η·P_saved·min(Δt, T_cap) | No example; paper invents no η or cap. (extractor test vector) η = 0.5, P_saved = 10, Δt = 7200, T_cap = 3600 → 18000. |
| FR9 | 250 | C(k) = 4·(107/100)^(k−1), P(k) = (167/100)·k, k < 25 | C(1..5) = 4, 4.28, 4.5796, 4.900172, 5.24318404 (paper). P(1..5) = 1.67, 3.34, 5.01, 6.68, 8.35 (paper). |
| FR10 | 253-257 | wait(k) = C(k)/P(k) | 400/167; 214/167; 11449/12525; 1225043/1670000; 131079601/208750000 (paper, exact). |
| FR11 | 253-257, 259 | cumulative T_K = (400/167)·Σ(j=1…K−1) r^(j−1)/j | K = 2…6: 400/167; 614/167; 57499/12525; 26674729/5010000; 465947491/78281250 (paper). |
| FR12 | 261 | Income with x2 at 25 and x2 again at 50 | 24 owned 40.08; 25 owned 83.5; 49 owned 163.66; 50 owned 334 (paper). |
| FR13 | 267, 269-275 | G_1(t) = t; C(t) = t^2/2 | t = 0…5: G_1 = 0…5; C = 0, 1/2, 2, 9/2, 8, 25/2 (paper). |
| FR14 | 291, 293, 296-301 | X_l = 500·l·(l−1); A_l = l(l−1)/2; XP to next = 1000·l | l = 1…6: X = 0, 1000, 3000, 6000, 10000, 15000; A = 0, 1, 3, 6, 10, 15; next = 1000…6000 (paper). X_l = 1000·A_l for every row. |
| FR15 | 303 | time to reach L = Σ(l=1…L−1) 1000·l/q_l | Constant q: X_L/q, e.g. L = 6 → 15000/q (paper table). |
| FR16 | 309 | N = ⌈H/d⌉; TTK = t0 + (N − 1)·τ | H = 5: d = 4 → N = 2; d = 5 → N = 1. t0 = 0 → TTK τ and 0; t0 = τ → TTK 2τ and τ (paper). |
| FR17 | 313 | hits-to-kill = smallest n with Σ(i=1…n) d_i >= H | No example in the paper. |
| FR18 | 317 | (1.18)(1.2) − 1 | 0.416, i.e. 41.6% (paper). |
| FR19 | 321 | effective health = H/(1 − ρ), 0 <= ρ < 1 | No example. (extractor test vector) ρ = 0.5 → 2H; ρ = 0 → H. |

## 7. Source table (c)

Resolved from the paper's register (PP:728-1310). "Reg" = register line. Evidence type is the register's wording. No key quotations copied.

| Id | Reg | Title | Author or org | Date | Evidence type | URL |
| --- | --- | --- | --- | --- | --- | --- |
| O00 | 730 | Original recommendations and mathematical analysis prepared for this paper | the paper (not an external source) | 2026-10-21 | OPINION (not an external empirical source) | none |
| M01 | 870 | The Math of Idle Games, Part I | Anthony Pecorella (Kongregate) | 2016-10-04; author republication 2021-07-30 | EXPERIENCE for game model; VERIFIED for explicitly derived arithmetic | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i ; date provenance https://www.sirpinski.com/the-math-of-idle-games-part-i/ |
| M02 (register id C01, alias) | 732 | The Math of Idle Games, Part III | Anthony Pecorella / Kongregate | 2017-01-12; author republication 2021-07-30 | VERIFIED published historical formulas; EXPERIENCE analysis | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii |
| M03 | 884 | Level 7: Advancement, Progression and Pacing | Ian Schreiber | 2010-08-18 | EXPERIENCE | https://gamebalanceconcepts.wordpress.com/2010/08/18/level-7-advancement-progression-and-pacing/ |
| M04 (alias H08) | 896 | Level 2: Numeric Relationships | Ian Schreiber | 2010-07-14 | EXPERIENCE for reported game rules; VERIFIED for derivations | https://gamebalanceconcepts.wordpress.com/2010/07/14/level-2-numeric-relationships/ |
| M05 | 908 | The Math of Idle Games, Part II | Anthony Pecorella | 2016-10-28; author republication 2021-07-30 | EXPERIENCE for teaching construction; VERIFIED for calculus | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii ; date provenance https://www.sirpinski.com/the-math-of-idle-games-part-ii/ |
| M06 | 922 | Master your Power in Season of Blood | Blizzard Entertainment | 2023-10-10 | VERIFIED for published versioned rules; EXPERIENCE for intended effect | https://news.blizzard.com/en-gb/article/24014289/master-your-power-in-season-of-blood ; date provenance https://us.forums.blizzard.com/en/d4/t/master-your-power-in-season-of-blood/128095 |
| H01 | 936 | The Motivational Pull of Video Games | Ryan, Rigby, Przybylski | 2006 | VERIFIED | https://selfdeterminationtheory.org/SDT/documents/2006_RyanRigbyPrzybylski_MandE.pdf |
| H02 | 946 | A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation | Deci, Koestner, Ryan | 1999-11 | VERIFIED | https://pubmed.ncbi.nlm.nih.gov/10589297/ |
| H03 | 956 | Pervasive negative effects of rewards on intrinsic motivation: The myth continues | Cameron, Banko, Pierce | 2001 spring | VERIFIED | https://pmc.ncbi.nlm.nih.gov/articles/PMC2731358/ |
| H04 | 966 | Towards understanding the effects of individual gamification elements on intrinsic motivation and performance | Mekler et al. | 2017-06-01 | VERIFIED | https://research.aalto.fi/en/publications/towards-understanding-the-effects-of-individual-gamification-elem/ |
| H05 | 976 | The challenge-skill balance and antecedents of flow: A meta-analytic investigation | Fong, Zaleski, Leach | 2015 journal issue; DOI first published 2014 | VERIFIED | https://www.tandfonline.com/doi/abs/10.1080/17439760.2014.967799?journalCode=rpos20&src=recsys |
| H06 | 986 | The Chemistry of Game Design | Daniel Cook | 2007-07-19 original; 2021-03-13 author repost | EXPERIENCE | https://lostgarden.com/2021/03/13/the-chemistry-of-game-design-2/ |
| H07 | 996 | Geek Fun Isn't Frivolous | Raph Koster | 2005-05-15 original; 2014-03-28 page update | EXPERIENCE | https://www.raphkoster.com/games/essays/geek-fun-isnt-frivolous/ |
| H08 | (none; alias of M04, reg 896) | see M04 | Ian Schreiber | 2010-07-14 | EXPERIENCE | see M04 |
| H09 | 1006 | It's about time: Earlier rewards increase intrinsic motivation | Woolley, Fishbach | 2018-06 | VERIFIED | https://pubmed.ncbi.nlm.nih.gov/29771568/ |
| H10 | 1016 | Do Immediate External Rewards Really Enhance Intrinsic Motivation? | Liu et al. | 2022-05-16 | VERIFIED | https://pmc.ncbi.nlm.nih.gov/articles/PMC9150741/ |
| H11 | 1026 | Loot box engagement: A scoping review of primary studies on prevalence and association with problematic gaming and gambling | Montiel et al. | 2022-01-27 | VERIFIED | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263177 |
| H12 | 1036 | Perceived value of video games, but not hours played, predicts mental well-being in casual adult Nintendo players | Ballou et al. | 2025-03-12 | VERIFIED | https://pubmed.ncbi.nlm.nih.gov/40078920/ |

The register for H01-H05, H09-H12 gives no separate author line; authors above come from the titles the paper uses. First names, journals and DOIs are not in the paper's register for these.

## 8. Limits the paper states (d)

| ID | PP | Limit |
| --- | --- | --- |
| LM1 | 232 | M01's printed base 3.738 and example 7.87 are rounded; not exact game constants. Timed payouts are simplified to continuous income. |
| LM2 | 234 | Bulk, wait and payback formulas hold only in the stated abstract model; they ignore simultaneous spending elsewhere. Changed prices (rounding, discounts, milestones) must be summed from actual prices. |
| LM3 | 240 | Payback C/ΔP is not an optimality proof; no policy is globally optimal without a named objective. |
| LM4 | 242 | Prestige accounting rules are alternative model definitions, not universal game rules. A, α and the reset threshold must not come from another game's feel. |
| LM5 | 244 | Offline efficiency, cap, auto-buy, generator chaining and buff expiry are design inputs; none is invented. |
| LM6 | 248, 261 | Lemonade is a reindexed teaching model, not current AdVenture Capitalist; 1.67 is exact only inside the model; incomes are not Roblox targets; no prestige timeline is claimed. |
| LM7 | 259, 261 | Waits are not guaranteed to shrink indefinitely. |
| LM8 | 277 | M05 is continuous; a tick-based integer model is a different model and needs its own stated rule. |
| LM9 | 287 | M04's XP example and its 5-HP example are different examples; do not combine. |
| LM10 | 303 | No q, encounter schedule or combat stats in the source; the timeline stays symbolic; minutes, day-one targets or coupled combat sims would invent inputs. Schreiber's examples are not a current studio spec. |
| LM11 | 307, 313 | H/(d/τ) is only an approximation; one-sided TTD is not a duel result; expected DPS is not expected TTK for random damage; ceil(H/E[D]) is not generally the expected hit count. |
| LM12 | 311 | The 5-HP example is not Dark Alliance combat data. |
| LM13 | 317 | The M06 formula is a 2023 historical design change, not the 2026 Diablo spec. |
| LM14 | 323 | M03 denies universality of its pattern. |
| LM15 | 339 | H01 is largely correlational. |
| LM16 | 345, 351 | H02/H03: tasks mostly controlled, not commercial games; reward types are not interchangeable; H03 is a re-analysis. |
| LM17 | 357 | H04: annotation task; no sample size in the checked abstract; task output is not enjoyment. |
| LM18 | 363 | H05: only the publisher abstract was verified; no numeric effect size or age breakdown claimed; no universal ideal difficulty ratio. |
| LM19 | 369, 375, 381 | H06, H07, H08 are designer frameworks, an op-ed and a course lesson; no controlled evidence. |
| LM20 | 387, 393 | H09, H10: lab or reading/news tasks, adults or 17-26; no seconds-per-reward rule; no long-term game enjoyment claim; the H09 abstract gives no ages or sizes. |
| LM21 | 399 | H11: cross-sectional, convenience samples, only six studies with adolescents; no causation; free drops are not shown equal to paid loot boxes. |
| LM22 | 405 | H12: adults, one ecosystem, non-causal, equivalence inconclusive. |
| LM23 | 411, 431, 436 | No source gives a Roblox-wide reward interval; "every 30 seconds" and "always delay" are both unsupported as universal rules. |
| LM24 | 415, 417 | Ethical policy (W7-W9) is value choice, not proven by H11 or H12; pity counter and transparency are not proof of harmlessness. |
| LM25 | 431 | The paper assumes nothing about all Roblox players being children. Roblox eligibility, odds and purchase rules are not in this range. |

## 9. Possible issues (e)

Marked as the paper says; nothing fixed. Hand-check results are in section 4: the Lemonade table and the RPG table are internally consistent, so none of the issues below is an arithmetic error.

| ID | PP | (extractor) possible issue |
| --- | --- | --- |
| XI1 | 234, 236, 291, 307, 317, 321 | Tag stretch: "VERIFIED derivation" labels the paper's own algebra (source "this paper"). By the paper's own definition (PP:15, outside range) VERIFIED needs a published rule or a measured result. I recomputed the Lemonade, M05, RPG, 5-HP and 0.416 numbers and checked FM2, FM4, FM9 algebraically; FM5, FM7, FM8, FM10 are definitions with no numbers to recheck. Keep the tag as written; the lead may choose to call them "derived". |
| XI2 | 232, 248, 250 | Index origin differs between FM1 (k >= 0, C(0) = b) and Lemonade (k >= 1, C(1) = 4). They agree only if b = 4/1.07 = 3.738… (the "printed base 3.738" may be this b, but the paper does not say). Tests must fix which origin they use. |
| XI3 | 287, 291 | M04 reports three XP values (1000, 2000, 3000) and three point values (1, 2, 3). The paper extends them to every level (1000·l, A_l = l(l−1)/2, table to level 6) by reading "continuing". Rows for levels 5 and 6, and the formula X_l, rest on that extension; fact-check should confirm M04 states the general rule. |
| XI4 | 261, 232 | The paper writes P(k) only for k < 25. Incomes at 25, 49, 50 imply x2 from 25 and x4 total from 50 (see L12), a piecewise form the paper never writes. |
| XI5 | 261 | "Waits shrink" is true only for early rows; my recomputation (L13) shows the minimum wait at k = 15 and growth after. Consistent with the paper's own caveat, but a tool test over k = 1…24 will not show monotone decrease. |
| XI6 | 232 | The paper does not say what the rounded "7.87" is; fact-check should open M01. |
| XI7 | 329, 226 | e_l and X_l = Σ e_j are not defined in lines 230-439; the sum range of t = Σ e_l/q_l is not given in TR4. Resolved only by reading PP:303. |
| XI8 | 311 | Spacing typos in the paper ("areτ", "atτ"); the math is correct. |
| XI9 | 425 | E3 cites H01 with H04 for the claim that numeric progress markers alone need not raise intrinsic motivation. H01 (self-determination, mostly correlational per PP:339) did not test progress markers; only H04 did. Attribution looks loose. |
| XI10 | 409 | The sentence tagged VERIFIED also says the cases are "not clean contradictions" because tasks and windows differ. That explanation is the paper's interpretation, not a finding. |
| XI11 | 339 | "MMO survey" is not tied to a study number in the paper; Study 4 (online community) is the only survey described, so Study 4 = MMO survey is my inference. |
| XI12 | 363, 976 | H05 date is "2015 issue" in the text and "2015 journal issue; DOI first published 2014" in the register. The fact-checker should settle the citation year. |
| XI13 | 393 | H10: four analyzed sample sizes (1a, 1b, 2, 3) and the register's key phrase talks about "three groups" for one experiment; consistent, but group sizes are not given. |
| XI14 | 436, 411 | "No verified Roblox-wide seconds-per-reward target" is an absence claim; it is tagged OPINION and cannot be proven by checking one source. |
| XI15 | 317 | The paper does not say which M06 sentence gives the 18% and 20% figures or what the 18% is additive to; fact-check must read M06. |
| XI16 | 732 | M02 appears in the register under id C01 ("C01 aliases M02"). Look-ups by M02 miss it unless the alias is known. H08 has no entry of its own (alias of M04). |

## 10. Coverage map

| Paper part | Where |
| --- | --- |
| Section 4 incremental (PP:230-283): M01 facts, bulk/wait/payback, M02, offline, Lemonade, M05, rule table | 1.1-1.5, 4, 6 |
| Section 5 RPG (PP:285-329): XP table, time axis, hits and TTK, stacking, effective health, difficulty bands, rule table | 2, 4, 6 |
| Section 6 rewards (PP:331-438): H01-H12, design choices, differences, rule table | 3.1-3.4 |
| Claims, formula tests, sources, limits, issues | 5, 6, 7, 8, 9 |
