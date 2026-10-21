---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J011-T05, web checks 2026-10-21"
supersedes: []
---
> Author: fact-checker · claude-sonnet-5-5 · high · 2026-10-21

# Fact check J011-T05: game cases, formulas, studies, tool practice

Scope: every claim in the claims lists of `01-cases-shapes-curves.md` (section 8, CL01-CL38, plus the optional OL1-OL7) and `02-incremental-rpg-rewards.md` (section 5, FC01-FC40) that cites C01-C11, M01-M06, H01-H12 or W01-W05, W08, plus the lead's 17 priority items. R-ids and W06/W07 are another ticket (J011-T06) and are not here. I did not edit the notes. Row ids below are `01:CLnn` and `02:FCnn`.

Count: claims in the lists 38 (note 01) + 40 (note 02) = 78; claims checked 78 of 78; optional OL rows checked 7 of 7. Six W rows (W01-W05, W08) are not in either claims list (they sit in paper section 8, outside both notes' ranges); I checked them from the paper's register and added them in table E. Rows with no external source (CL36, CL37, FC20, and the derived parts of FC07-FC11, FC13, FC17, FC18, FC21, FC23) are arithmetic: I recomputed them with exact fractions (Python `fractions`) and say so.

## How I checked

Read date for every row is 2026-10-21. I read raw page text, not search snippets, for every confirmed or corrected row. Tools:
- `curl` (browser User-Agent) for raw HTML of studio pages, the author's blog, PDFs (`pdftotext`) and PMC/PLOS full text. JSON-LD `datePublished` or the visible post date gave the page date.
- NCBI E-utilities (`efetch`, XML) for PubMed records of H02, H09, H12, because the PubMed HTML page returns a JavaScript challenge. These are abstract-level records.
- Wayback Machine for the retired Kongregate developer blog (`blog.kongregate.com`, captures of 2017-06-20/22), to date M01, M05 and C01 at the original host.
- OpenAlex and Crossref APIs for H05, because tandfonline.com returned HTTP 403 to curl and to WebFetch. The abstract text is a mirror of the publisher abstract; Crossref gave the issue data. H05 is abstract only.
- WebSearch once for the Game Developer syndication of C01 and once for TFT early-level XP (third-party snippet, used only as a cross-check, never as proof).
- Arithmetic: Python `fractions` for the Lemonade table, T_K, M05, RPG table, TFT sums, Clash caps, Hearthstone percentage.
- Another agent was using the same scratchpad folder during this ticket and overwrote one of my helper scripts. I moved to a private folder and re-ran the affected reads. No result below depends on the overwritten file.

Provenance labels: studio-published (studio's own page), author account (the author's own page or repost), journal record (publisher, PubMed, PMC, PLOS), third-party (not used to confirm anything).

## Verdict key

confirmed: the source says it, at the scope stated. corrected: the source says something different or narrower; the row gives the correct statement. unverified: the source is silent or the claim is the paper's synthesis; keep it as EXPERIENCE or OPINION only. dropped: the source contradicts it. No row is dropped.

## Priority items (check C1)

| # | Item | Verdict | Result in one line | Rows |
| --- | --- | --- | --- | --- |
| 1 | Three prestige formulas, inputs, "fractional exponent not logarithm" (C01/M02) | confirmed, with one correction | All three formulas match Part III exactly. Realm Grinder uses max currency, AdCap and Cookie Clicker use lifetime. The author says roots are not logs, and names Clicker Heroes as the exception that really is log-like. The paper's "three inputs" is narrower than the source (four factors, two categories). | 01:CL01-04, 02:FC06 |
| 2 | Lemonade inputs (M01) | confirmed | 1.07, 1.67/s, first free, second costs 4, x2 stacking at 25 and 50, and both rounded figures are in Part I. 7.87 = 4 x 1.07^10 (the source's own 10-owned example with base 4); 3.738 = 4/1.07. | 02:FC01-05, 07-11 |
| 3 | M05 two-tier chain | confirmed | Source states the chain, the half-existing rule and y = x^2/2; t = 0, 1, 2 values are in the text, t = 3-5 are the paper's arithmetic and are right. | 02:FC12-14 |
| 4 | M04 XP rule and 5-HP example | confirmed, scope added | Source gives XP 1000/2000/3000 "and so on" (triangular) and points 1, 2, 3, 4 "and so on", and states the net ratio 1000 XP : 1 point. The formula 1000*l is the paper's reading of "triangular", and it is a faithful one. The 5-HP example is separate and is about a cost peak, not hit counts. | 02:FC15-19, FC21 |
| 5 | M06 Vulnerable 18% x 20% = 41.6% | confirmed, scope added | Worked example in the article: the base x20% multiplicative plus an extra +18.0% from gear. 18% is an example input, not a game constant. | 02:FC22 |
| 6 | TFT 13.23 values and 228 -> 288 | confirmed; Z02 resolved by arithmetic | Patch notes list 20/36/48/80/84 and "228 => 288" verbatim. The five sum to 268. The remaining 20 XP (levels 1 to 5, unlisted) closes both totals: 228 = 20 + 24+40+60+84 and 288 = 20 + 20+36+48+80+84. The 20 is my inference; the page does not itemize it. | 01:CL24-26 |
| 7 | Diablo IV 200 -> 300, level 60, Pit tiers | confirmed | 200 -> 300 is Paragon POINTS earned by leveling (not a level cap). Levels 1-60, Paragon from 60. Beating Pit tier 20/35/50/65 unlocks Torment I/II/III/IV. | 01:CL07-11 |
| 8 | Hearthstone | confirmed | "Nearly 20%" is Blizzard's own wording next to 37,000 XP. 7 -> 5 wins, 150 -> 350, 50 gold from level 51 all in the article. Levels past 50 are the bonus levels. | 01:CL15-16 |
| 9 | Clash Royale | confirmed | 50,000 Elite Wild Cards for 14 -> 15 with nothing else. Caps match. Reward totals are cumulative, 25,000 -> 50,000 at league 10. December 4 is 2023 and is the effective date (season start); the post is dated 30 Nov 2023. | 01:CL17-20 |
| 10 | Factorio | confirmed | count_formula "1000*2^(l-6)", level 6 costs 1000, each level twice the last. | 01:CL05-06 |
| 11 | WoW Renown | confirmed | Renown 5 and 10 on two characters give Warband Renown 10 (furthest progress). "Not 15" is the paper's inference. | 01:CL12-14 |
| 12 | LoL Marks | confirmed; one wording correction | Marks 0 / 1 / 2 by level band; 4-milestone track per split plus a repeating milestone. The article is a pre-release plan with feedback invited; it never uses the word "proposal". | 01:CL21-23 |
| 13 | Overwatch | confirmed | Borders every 20 hero levels, fiery look at 60, retroactive, curve flattens at 20. | 01:CL28-30 |
| 14 | Mario Wonder | confirmed; Z10 resolved | Six worlds around the Petal Isles, "a total of seven areas": six worlds plus the Petal Isles. | 01:CL31 |
| 15 | H01-H12 | confirmed (12 of 12) | Designs, populations, sample sizes and finding directions match. Notes in table D. | 02:FC25-40 |
| 16 | C01 date | confirmed; Z03 resolved | 2017-01-12 original (Kongregate dev blog, Wayback). 2017-02-01 is the Game Developer (Gamasutra) syndication. 2021-07-30 is the author's own republication on sirpinski.com. Three events, no conflict. | 01:CL01-04, 02:FC05 |
| 17 | W05 NIST | confirmed | Wilson interval (Wilson 1927) and an exact binomial method for very few failures or small N. | table E |

## Source locations (used in the tables)

| Id | Where I read it |
| --- | --- |
| C01/M02 | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-iii (page text); author repost https://www.sirpinski.com/the-math-of-idle-games-part-iii/ ("Originally published January 12, 2017", post date Jul 30, 2021); Wayback http://blog.kongregate.com/the-math-of-idle-games-part-iii/ (capture 2017-06-20, byline date January 12, 2017); syndication https://www.gamedeveloper.com/design/the-math-of-idle-games-part-iii (datePublished 2017-02-01) |
| M01 | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-i; sirpinski repost (Originally published October 4, 2016); Wayback blog capture 2017-06-20 (byline October 04, 2016); Game Developer copy 2016-10-13 |
| M05 | https://www.kongregate.com/en/pages/the-math-of-idle-games-part-ii; sirpinski repost (Originally published October 28, 2016); Wayback blog capture 2017-06-22 (October 28, 2016); Game Developer copy 2016-12-14 |
| M03/M04/W03/W04/W08 | gamebalanceconcepts.wordpress.com pages at the register URLs; post dates from page metadata |
| M06 | https://news.blizzard.com/en-gb/article/24014289/master-your-power-in-season-of-blood (datePublished 2023-10-10) |
| C02 | https://www.factorio.com/blog/post/fff-161 ("Posted by Tomas & kovarex on 2016-10-21") |
| C03 | https://news.blizzard.com/en-gb/article/24140803/conquer-colossal-foes-in-season-of-hatred-rising (datePublished 2024-10-02) |
| C04 | https://news.blizzard.com/en-us/article/24061008/the-war-within-warbands-preview (datePublished 2024-04-17) |
| C05 | https://hearthstone.blizzard.com/en-gb/news/23585675/rewards-track-update-coming-soon (2020-12-07) |
| C06 | https://supercell.com/en/games/clashroyale/blog/release-notes/card-evolution-2/ ("18 Jun 2023") |
| C07 | https://supercell.com/en/games/clashroyale/blog/news/changes-coming-to-path-of-legends/ ("30 Nov 2023") |
| C08 | https://www.leagueoflegends.com/en-us/news/dev/dev-updating-champion-mastery/ (2024-01-05) |
| C09 | https://teamfighttactics.leagueoflegends.com/en-gb/news/game-updates/teamfight-tactics-patch-13-23-notes/ (2023-11-20), section "Leveling changes" and "Shop odds" |
| C10 | https://news.blizzard.com/en-us/article/24224138/weekly-recall-gaining-progress (2025-08-22) |
| C11 | https://www.nintendo.com/au/news-and-articles/experience-the-unexpected-in-super-mario-bros-wonder-gameplay-presentation/ ("8 September 2023") |

## A. Idle-game sources: C01/M02, M01, M05 (Kongregate dev blog, Pecorella)

Provenance for all rows: author account (the author's own series, on Kongregate's blog and on his own site). Read via curl (page text) and Wayback (original host dates).

| Row | Claim | What the source says | Where | Verdict |
| --- | --- | --- | --- | --- |
| 01:CL01 | AdCap p = 150*sqrt(cL/10^15), cL lifetime earnings | Same formula; p is total prestige currency, c_L is lifetime currency. Source adds that resetting at the same point still gains a little each time, shrinking. Doubling needs roughly 3x-4x the previous run (assumption-dependent); the pure sqrt gives 4x lifetime. | C01 Part III, section on AdVenture Capitalist | confirmed |
| 01:CL02 | Repeating the same run adds prestige, progressively less | "You can keep resetting at the same point and gain currency"; the amount diminishes each time. | C01, AdCap paragraph | confirmed |
| 01:CL03 | Cookie Clicker p = (cL/10^12)^(1/3); doubling p needs 8x lifetime earnings | Formula matches (cube root). Source words the 8x as "roughly 8 times the previous run". The paper's "8x total lifetime earnings" is the exact math of a cube root (2^3 = 8). | C01, Cookie Clicker paragraph | confirmed (math exact; source wording looser) |
| 01:CL04 | Realm Grinder p = (sqrt(1+8*cM/10^12) - 1)/2, from maximum earnings; same maximum gives no extra | Formula matches; the author derives it from c_M = 10^12 * p(p+1)/2 with the quadratic formula. "If you reset at the same point you will earn literally no more." Doubling needs 4x the previous run. | C01, Realm Grinder paragraph | confirmed |
| 02:FC06 | M02 separates lifetime, maximum-earned, since-reset inputs; corrects roots-vs-logarithms | Four factors are listed: max earnings (Realm Grinder), lifetime (Cookie Clicker, AdCap), since last reset (Egg, Inc.), upgrades bought since reset (Clicker Heroes). The author sorts them into TWO categories, "lifetime stats and since-reset"; max earnings sits with lifetime. Variables defined: c_L, c_M, c_R. The correction: "I have incorrectly called this 'taking a log' in the past"; most prestiges are a fractional exponent; Clicker Heroes really is log-like. | C01 Part III, intro and "Note:" paragraph | corrected (see changes 1-2) |
| 02:FC01 | Lemonade inputs: growth 1.07, 1.67/s, first free, second 4, x2 at 25 and 50 | rate_growth = 1.07, cost_base = 4 (footnote: technically 3.738, first one free, "the second one that costs 4"), production_base = 1.67/sec; "at 25 and 50 ... (stacking) x2". | M01 Part I, AdCap Lemonade paragraph | confirmed |
| 02:FC02 | Printed base 3.738 and example 7.87 are rounded | 7.87 is the source's result for cost_next = 4 x 1.07^10 (exact 7.8686). 3.738 is 4/1.07 = 3.7383. Both rounded. The two are not on one base: 3.738 x 1.07^10 = 7.353 (= 4 x 1.07^9). So 7.87 is the simplified-base example, not the cost at 10 owned in the paper's re-indexed model. | M01 Part I, same paragraph and footnote | confirmed (with clarification, changes 3) |
| 02:FC03 | M01 simplifies timed payouts to continuous per-second income | "This model simplifies income to be per-second instead of requiring a timer." Said about the multi-generator optimal-purchase model; the Lemonade formula is also per second. | M01 Part I, paragraph after the 5-generator graph | confirmed |
| 02:FC04 | Exponential prices, linear output with multipliers, closed-form bulk buy (B(k,n)) | "costs grow exponentially while production grows at a linear or polynomial rate"; cost = b*r^k*(r^n-1)/(r-1); max = floor(log_r(c(r-1)/(b*r^k)+1)); valid only for simple exponential growth with no shifting costs. This is FM2 and FM4 exactly. | M01 Part I, "BONUS CONTENT" | confirmed |
| 02:FC05 | M01 date 2016-10-04 (Kongregate republication 2021-07-30; provenance sirpinski.com) | Original on the Kongregate Developer's Blog, byline October 04, 2016 (Wayback capture). The 2021-07-30 republication is on the author's own site sirpinski.com, not on Kongregate. Game Developer syndicated it 2016-10-13. | M01 sources above | corrected (changes 4) |
| 02:FC07 | Lemonade prices 4, 4.28, 4.5796, 4.900172, 5.24318404; incomes 1.67 ... 8.35 | Source gives only the formula and one example. Table is the paper's arithmetic. I recomputed: 4 x 1.07^(k-1) and 1.67 x k give exactly those values. | M01 formula; my fractions run | confirmed (arithmetic) |
| 02:FC08 | Waits 400/167, 214/167, 11449/12525, 1225043/1670000, 131079601/208750000 | Recomputed price/income per step; all five equal and in lowest terms. | my fractions run | confirmed (arithmetic) |
| 02:FC09 | Cumulative 400/167, 614/167, 57499/12525, 26674729/5010000, 465947491/78281250 | Recomputed running sums: 2.3952, 3.6766, 4.5907, 5.3243, 5.9522 s; all five equal. | my fractions run | confirmed (arithmetic) |
| 02:FC10 | T_K = (400/167)*sum_{j=1..K-1} r^(j-1)/j | Gives the same five cumulative values for K = 2..6 (exact fractions). Holds for K up to 25. | my fractions run | confirmed (arithmetic) |
| 02:FC11 | Incomes 40.08 (24), 83.5 (25), 163.66 (49), 334 (50) | 1.67x24 = 40.08; 1.67x25x2 = 83.5; 1.67x49x2 = 163.66; 1.67x50x4 = 334. Right under the source's stacking x2 at 25 and at 50. The minimum wait on the paper's route is at k = 15 (0.4117 s) and rises to 0.473 s at k = 24, so "waits shrink" is true only for early rows, as the paper already says. | M01 multipliers; my run | confirmed (arithmetic) |
| 02:FC12 | M05 setup: one fixed tier-2 generator; rates 1/s per tier; G1(t) = t, C(t) = t^2/2 | One Gen 2 that never changes, produces Gen 1 at 1 per second; Gen 1 makes 1 currency per second. Currency "is in fact y = x^2/2", the integral of y = x. | M05 Part II, sections after "At time t=0" | confirmed |
| 02:FC13 | Table C = 0, 1/2, 2, 9/2, 8, 25/2 at t = 0..5 | Text gives t = 0 (zero), t = 1 (0.5 currency), t = 2 (2 currency). t = 3, 4, 5 follow from x^2/2: 4.5, 8, 12.5. | M05; my run | confirmed |
| 02:FC14 | M05 itself describes the continuous vs discrete boundary | "One oddity of looking at continuous graphs for a discrete problem": a Gen 1 created in a second yields only half a currency that second. | M05 Part II, paragraph before t=0 | confirmed |

## B. Schreiber and Blizzard formula sources: M03, M04, M06

Provenance: M03/M04 author account (teaching blog); M06 studio-published. Read via curl.

| Row | Claim | What the source says | Where | Verdict |
| --- | --- | --- | --- | --- |
| 02:FC15 | M04: XP 1000, 2000, 3000 for 1->2, 2->3, 3->4, "continuing"; points 1, 2, 3 | Dark Alliance XP-to-level is "triangular": 1000, 2000, 3000 "and so on". Upgrade points: level 2 gives 1, level 3 gives 2, next 3, then 4 "and so on". The two triangular relations "cancel" to a linear 1000 XP : 1 upgrade point on average. So the source does state a general rule, in words, and the net ratio. Only 3 XP values and 4 point values are explicit numbers. | M04, section "Interactions Between Relationships" | confirmed (formula 1000*l is the paper's reading of "triangular") |
| 02:FC16 | M04 separate 5-HP example: damage 4 to 5 | "If everything in your game has 5 hit points, there is actually a huge difference between doing 4 or 5 damage"; context is cost peaks in numeric relationships (the 5th point of damage costs more). Not an XP or Dark Alliance example. Hit counts 2 vs 1 are the paper's arithmetic (ceil(5/4) = 2, ceil(5/5) = 1). | M04, paragraph on cost peaks | confirmed (source says "everything", not "enemies") |
| 02:FC17 | 1000*l per level, X_l = 500*l*(l-1), A_l = l(l-1)/2, X_l = 1000*A_l | Derived from FC15; I recomputed. Source's own 1000:1 ratio agrees. | my run | confirmed (derivation) |
| 02:FC18 | RPG table levels 1-6 | X = 0, 1000, 3000, 6000, 10000, 15000; A = 0, 1, 3, 6, 10, 15; next = 1000..6000. All right. Levels 5 and 6 rest on the "and so on" rule. | my run | confirmed (derivation) |
| 02:FC19 | M04 gives no q, encounter schedule or combat stats | True. The source only reasons about shapes of XP rewards ("an hour per level" is a hypothetical exercise). | M04 time paragraph | confirmed |
| 02:FC20 | N = ceil(H/d), TTK = t0 + (N-1)*tau | No external source (the paper's own derivation). Standard discrete-hit logic; spot values right. | my run | confirmed (arithmetic only) |
| 02:FC21 | 5-HP: 4 dmg -> 2 hits, 5 dmg -> 1; TTK tau and 0 / 2tau and tau; +25% damage, hits halved | Arithmetic right. The source says only "a huge difference", not the numbers. | my run | confirmed (derived) |
| 02:FC22 | M06: 18% additive Vulnerable and 20% multiplicative give 41.6%; monsters rebalanced; article 2023-10-10 | Season of Blood article: bonus buckets now additive except a base multiplicative part; Vulnerable x20%, Critical x50%, Overpower x50%. Worked example: standard x20% plus +18.0% from gear gives (1.18)(1.2) - 1 = 0.416, "41.6%". Says monsters "have been rebalanced around the new player power". Dated 2023-10-10. The 18% is an example gear value. | M06, damage-bucket section and example | confirmed (18% is an example input) |
| 02:FC23 | Effective health = H/(1-rho) | No external source (paper's derivation). Consistent with M06: resistances became additive; the article says 60 -> 65% is worth more than 20 -> 25%. By H/(1-rho): x1.143 vs x1.067. | M06 resistance section; my run | confirmed (derivation) |
| 02:FC24 | M03: entry challenge, small gains, boss, post-boss power rise; denies universality | Source describes that pattern as "the most common pattern I've seen"; then "not the only pattern ... not even necessarily the best"; varies "based on genre and intended audience". | M03, power progression paragraphs | confirmed |

## C. Studio game cases: C02-C11

Provenance for all rows: studio-published (developer blog, patch notes, announcement). Read via curl, page text.

| Row | Claim | What the source says | Where | Verdict |
| --- | --- | --- | --- | --- |
| 01:CL05 | Factorio worker-robot-speed 6+, count_formula = 1000*2^(l-6); level 6 costs 1,000; doubles; 2016 development example | "count_formula = "1000*2^(l-6)"", l is the research level; "the level 6 costs 1000"; every other level "costs twice of the previous one". Posted 2016-10-21. | C02, section "Infinite research" | confirmed |
| 01:CL06 | Infinite research is an optional sink for huge factories with diminishing reward vs cost | "optional resource sinks for people that like to make huge factories"; "cost/gain ratio is going to have diminishing returns". | C02, same section | confirmed |
| 01:CL07 | Diablo IV Oct 2024: levels 1-60; Paragon begins at 60 | "Levels 1-60 representing character level ... Starting at Level 60 ... Paragon Levels". | C03, "Paragon and Character Level Split" | confirmed |
| 01:CL08 | Level-earned Paragon points raised 200 to 300 | "The number of Paragon Points that can be earned by leveling has increased from 200 to 300." These are points, not a level cap. The same section also raises the Paragon Levels you can earn, and says a build is realized at about Paragon Level 200. | C03, "Paragon Boards" | confirmed (points, not levels) |
| 01:CL09 | Paragon shared within realm and mode partition | "shared across all your characters on the same Realm (Seasonal or Eternal) and mode (Standard or Hardcore), in their respective partitions". | C03, Paragon intro | confirmed |
| 01:CL10 | Pit unlocks at 60; Pit tiers 20/35/50/65 unlock Torment I-IV | Level 60 unlocks the Pit and tiers 1-20. BEATING Pit tier 20 unlocks Torment I; tier 35 Torment II; tier 50 Torment III; tier 65 Torment IV. | C03, "Your Gateway to Hell" | confirmed (unlock needs beating the tier) |
| 01:CL11 | Blizzard: stat bloat from World Tier III / Sacred items; new characters reach endgame sooner; scaling felt weak | Developer's Note: World Tier III and Sacred items "can add a lot of stat bloat"; aim "for new characters to reach the endgame faster". Another note: feedback that level scaling led to "feeling weak". | C03, Developer's Notes | confirmed |
| 01:CL12 | WoW: shared Renown; Renown 5 and 10 become 10, not 15 | Warband reputations show "the furthest that any character ... has achieved"; example Valdrakken Accord Renown 5 and 10 gives Warband Renown 10. "Not 15" is not in the source; it is the reason given (adding would favour alt players). | C04, "Warband-Wide Reputation" | confirmed |
| 01:CL13 | Reputation on first Warband completion, a different currency on repeats | "We plan for quests to only give reputation as a first-time completion bonus"; repeats give a bonus currency, transferable across the Warband. A plan in a preview. | C04, quest-reward section | confirmed (preview wording: "plan") |
| 01:CL14 | Front-loaded campaign reputation would favour many alts if summed; goal: switch characters without losing efficiency | "if we added all the reputations ... unfair advantage for players who play many alts"; goal: play multiple characters "without losing efficiency or long-term progress". | C04, intro and reputation section | confirmed |
| 01:CL15 | Hearthstone Dec 2020: 37,000 XP ("nearly 20%"); 7 -> 5 wins; 150 -> 350; 50 gold per level from 51 | "reducing the requirements of the current rewards track by a total of 37,000 XP (nearly 20%)" (Blizzard's wording). Weekly quest "Win 7 Games of Ranked Play Mode" becomes 5. Maximum bonus level "now 350, up from 150"; each level "beginning at level 51" rewards 50 gold. Bonus levels are the levels after 50. The changes were announced for later in December. | C05, quest, XP and bonus-level sections | confirmed |
| 01:CL16 | First implementation missed goals; long gaps between bonus rewards; cadence no longer depends on event XP | "our initial implementation missed that mark"; bonus levels "took too much time to earn, leading to long play sessions between rewards"; event XP had been counted in the intended cadence and is dropped. | C05 | confirmed |
| 01:CL17 | Clash Royale June 2023: 14 -> 15 costs 50,000 Elite Wild Cards, no other requirement | "All upgrades from level 14 to 15 will require 50,000 Elite Wild Cards and nothing else"; the extra level "doesn't cost Gold". Dated 18 Jun 2023. | C06, "Level 15 / Elite Levels" | confirmed |
| 01:CL18 | Caps from December 4: 11/12/12/13/13/14/14/15/15/15 across leagues 1-10 | New table lists exactly those caps for leagues 1-10. "Dec 4" = when the next season starts and the caps go live; post dated 30 Nov 2023, so December 4, 2023. | C07 | confirmed (year 2023; effective date) |
| 01:CL19 | Cumulative seasonal Elite Wild Card rewards reach 50,000 at league 10, up from 25,000; totals not additive | New totals 0, 2,500, 2,500, 7,500, 15,000, 25,000, 25,000, 35,000, 35,000, 50,000; old totals ended at 25,000. "You will have collected a total number ... in the corresponding row." | C07, tables | confirmed |
| 01:CL20 | Stepped caps avoid an abrupt card-level rise in battles | Other leagues' caps adjusted "so there isn't such an instant increase to Card Levels in your Battles". | C07, last paragraphs | confirmed |
| 01:CL21 | LoL Jan 2024: uncapped mastery; Marks none at 1-4, one per level 5-9, two per level 10+ | "uncapping mastery levels ... keep leveling forever"; table: levels 1-4 none, 5-9 1 per level, 10+ 2 per level. | C08, "Leveling Changes" | confirmed |
| 01:CL22 | Four per-split milestones, then a repeating milestone; "proposal", not final | "Each split, every champion will have a 4-milestone reward track" plus a repeating more-difficult bonus milestone. The article is a pre-release plan: asks for feedback and promises an update "closer to release towards the start of the summer". It does not call itself a proposal and does not define "split" on the page. Marks per milestone: 1, 1, 2, 2; repeating one gives 1. | C08, "Split Mastery" and "Final Thoughts" | corrected (wording, changes 5) |
| 01:CL23 | Riot wanted mastery to show accomplishment; infinite track can feel like grind; shorter milestones | Principle "Mastery reflects real accomplishment, not just grind"; "an infinite system can sometimes feel like a grind" so they add shorter-term achievements. | C08, "Our Goals", "Split Mastery" | confirmed |
| 01:CL24 | TFT 13.23: level 10 available; XP 20/36/48/80/84 | "TFT goes to 10!"; "Level 10 is now the max level you can achieve at any point". Lines: 5-6 24=>20, 6-7 40=>36, 7-8 60=>48, 8-9 84=>80, 9-10 100=>84. | C09, "Leveling changes" | confirmed |
| 01:CL25 | Published total XP to max 228 -> 288 | Line "Total XP need to hit max: 228 => 288" is verbatim. It is not the sum of the listed lines: new listed values sum to 268 (20+36+48+80+84) and old listed values to 308 (24+40+60+84+100). Both totals reconcile with 20 unlisted XP for levels 1 to 5: 20+24+40+60+84 = 228 (old max, level 9) and 20+20+36+48+80+84 = 288 (new max, level 10). The 20 is inferred (a third-party snippet for a later set shows early steps 2/2/6/10, sum 20, but that is not this patch). | C09, same section; my run | confirmed (Z02 resolved, inference stated) |
| 01:CL26 | Level 8 odds 18/25/36/18/3; level 9 10/20/25/35/10 | "Level 8: 16/20/35/25/4 => 18/25/36/18/3%"; "Level 9: 9/15/30/30/16% => 10/20/25/35/10%". Both sum to 100. | C09, "Shop odds" | confirmed |
| 01:CL27 | Riot framed it as clearer composition identity per level | "each level has a distinct purpose for your comp"; odds changed "to sharpen each Level's identity". | C09 | confirmed |
| 01:CL28 | Overwatch 2: Ascended borders every 20 hero levels; milestone at 60 | "For every 20 levels of Hero progression ... a new Ascended portrait border"; borders gain complexity, "culminating in fiery flair at level 60". | C10 | confirmed |
| 01:CL29 | Earlier levels easier; flattens at 20; retroactive; minutes not published | "bit of an experience curve up to level 20, making earlier cosmetics (and levels) easier"; "this curve flattens at level 20 to a standard amount of time played". Levels "awarded retroactively" (Baptiste level 50 example). No minutes figure on the page. | C10 | confirmed |
| 01:CL30 | Earlier hero-based system "unnecessarily complex", did not resonate | "feels unnecessarily complex and wasn't resonating correctly". Rewards made easier to see and equip. | C10, opening | confirmed |
| 01:CL31 | Mario Wonder: six worlds around Petal Isles, seven areas; badges; examples; Invisibility; co-op shares badge | "six distinct worlds that circle the Petal Isles, giving you a total of seven areas". Badges earned "as your adventure progresses". Wall-Climb Jump, Dolphin Kick, Crouching High Jump, Grappling Vine; Invisibility is "an additional challenge". "In local multiplayer, each group of players will use the same badge." | C11 | confirmed |
| 01:CL32 | Rule 2: a published rule is evidence of that rule in its stated version only (C03, C08) | Both sources are dated and version-bound, so the dates are right (C03 2024-10-02, C08 2024-01-05). The rule itself is the paper's method principle; neither source says it. | C03, C08 dates | corrected (tag: OPINION; dates confirmed) |
| 01:CL33 | Rule 6: optional endless sink and introductory reward track solve different problems | C02 does call infinite research an optional sink; C10 does describe an introductory first-20-levels track. The contrast "solve different problems" is the paper's synthesis. | C02, C10 | corrected (C02 intent confirmed; the contrast is OPINION) |
| 01:CL34 | Rule 9: reward spacing can need correction even when the system pays a large total | C05 confirms the spacing problem. It does NOT call the payout large: Blizzard also cut the track XP by 37,000 and added gold because rewards felt slow and gold earnings low. Total and spacing were both changed. | C05 | corrected (changes 6) |
| 01:CL35 | Rule 10: no support for "all rewards help" or "all harm" (H02, H03) | See table D, FC26-27. The two meta-analyses disagree; neither supports a slogan. | H02, H03 | confirmed |

## D. Studies: H01-H12

Provenance for all rows: journal record (peer-reviewed article or its abstract) except H06/H07/H08, which are author accounts. I never upgraded a correlational result to causal. "Abstract only" is stated where that is all I read.

| Row | Study | Design, population, sizes, finding (what the source says) | Where and how read | Verdict |
| --- | --- | --- | --- | --- |
| 02:FC25 | H01 Ryan, Rigby, Przybylski 2006 | Four studies. Studies 1-3: laboratory, undergraduates, 1, 2 and 4 games. Study 1 n = 89 (23 male, 66 female); Study 2 n = 50 (36 f, 14 m), random assignment of which game came first; Study 3 n = 58 undergraduates (46 f, 12 m), game per visit by random assignment. Study 4: online survey of 730 community members with MMO experience (51 female, 679 male), aged 16 to 44, mean 22.1. Finding: perceived autonomy and competence are associated with enjoyment and preference for future play; autonomy, competence and relatedness each independently predicted enjoyment and future play in Study 4 (the MMO survey; this settles XI11). Limits: the authors call the work "largely experimental" (assignment to games), but need satisfaction was measured, not manipulated, so the need-enjoyment link is an observed association; the paper's "largely correlational" is a fair reading of that link, not the authors' wording. No point, level or leaderboard test. | Full PDF, `pdftotext`; Abstract, Methods of each study, Discussion | confirmed |
| 02:FC26 | H02 Deci, Koestner, Ryan 1999-11 | Meta-analysis. Abstract says 128 "studies" (title says "experiments"). Engagement-, completion- and performance-contingent rewards undermined free-choice intrinsic motivation (d = -0.40, -0.36, -0.28), as did all rewards, tangible rewards and expected rewards. Positive feedback enhanced it (d = 0.33). Tangible rewards more harmful for children than college students. | PubMed record via E-utilities; abstract only | confirmed |
| 02:FC27 | H03 Cameron, Banko, Pierce 2001 Spring | Meta-analysis of the same literature (>100 experimental studies), intended to resolve the differences with H02. "In general, rewards are not harmful"; low-interest tasks: rewards enhance free-choice motivation; high-interest tasks: negative effects when rewards are tangible, expected and loosely tied to performance. Concludes no "pervasive negative effects". The Behavior Analyst 24(1):1-44. | PMC full text, Abstract | confirmed |
| 02:FC28 | H04 Mekler et al. 2017-06-01 | 2x4 online experiment (points, leaderboards, levels vs control, crossed with goal causality orientation), image annotation task. No significant effect of game elements on competence or intrinsic motivation. Points, and especially levels and leaderboard, raised the number of tags. No sample size in the abstract. Computers in Human Behavior 71:525-534. | Aalto institutional record (abstract); abstract only | confirmed |
| 02:FC29 | H05 Fong, Zaleski, Leach 2015 | Meta-analysis of 28 studies. Challenge-skill balance and flow: "moderate"; smaller with intrinsic motivation. Weaker correlations for individualistic cultures, work or education contexts, experience sampling, state self-report. Clear goals and sense of control also contributed. No age breakdown. J Positive Psychology 10(5):425-446, print 2015-09-03, online 2014-10-15 (settles XI12: cite 2015, DOI first published 2014). | Abstract via OpenAlex mirror; Crossref for issue data (publisher page HTTP 403); abstract only | confirmed |
| 02:FC30 | H06 Cook | Interaction loop of decision, action, simulation, feedback, modeling; "burnout" = player masters a skill but finds no interesting use. Original Gamasutra 2007-07-19 (Game Developer page 2007-07-19; lostgarden.com 2007-07-19 URL); repost 2021-03-13. Designer framework, not a study. | lostgarden.com repost and Game Developer page | confirmed |
| 02:FC31 | H07 Koster | Fun as the reward for learning patterns; "once the player has mastered the underlying pattern, the fun erodes". Ran in the LA Times 2005-05-15; page updated March 28, 2014. The designer's goal is "self-refreshing game play" with ever more complex patterns, models "subject to interpretation". The paper's wording at PP:373 says "interpretable"; note 02's table says "readable", which the source does not say. | raphkoster.com essay page | confirmed (use "interpretable", not "readable") |
| 02:FC32 | H08/M04 | XP, level and upgrade relations chain together; XP reward growth vs triangular level cost shapes time per level; a rising threshold alone does not set time. 2010-07-14. Course lesson. | M04, time paragraphs | confirmed |
| 02:FC33 | H09 Woolley, Fishbach 2018-06 | Five studies: immediate vs delayed reward framing for a news program (Study 1) and a bonus in an experimental task (Studies 2-3) raised intrinsic motivation; mediated by activity-reward association; timing effect independent of magnitude (Study 5). PubMed type: Randomized Controlled Trial; MeSH age terms Adult, Young Adult, Middle Aged. No sample sizes in the abstract. J Pers Soc Psychol 114(6). | PubMed record via E-utilities; abstract only | confirmed |
| 02:FC34 | H10 Liu et al. 2022-05-16 | Frontiers in Psychology 13:853879. Participants from South China Normal University, all aged 17-26. Reading tasks. Study 1a: 90 took part, 87 analysed (3 excluded), randomised into three groups of 29. Study 1b: 58, randomised to two groups of 29. Study 2: 63 took part, 58 analysed. Study 3: 144 (two-factor, timing x magnitude; 5 vs 7 RMB). Immediate extra reward gave higher reported intrinsic motivation. Short monetary-bonus lab experiments. | PMC full text, Methods of each study | confirmed |
| 02:FC35 | H11 Montiel et al. 2022-01-27 | Scoping review. 16 primary empirical studies; all cross-sectional; most convenience samples; only six included adolescents. "In general" a significant positive relationship between loot-box engagement and problematic gaming and gambling, possibly depending on engagement type and sample. PLOS ONE 17(1), published January 27, 2022. | PLOS full text, Abstract | confirmed |
| 02:FC36 | H12 Ballou et al. 2025-03-12 | Royal Society Open Science 12(3):241174. 703 casually engaged US adults (recruited through Prolific), pre-registered; surveys joined to Nintendo Switch play-session data supplied by Nintendo of America, covering first-party games only (150 games, over 140,000 h). Cross-sectional. Playtime did not predict well-being; "gaming life fit" did. Authors call findings "non-causal"; equivalence tests inconclusive. | PubMed record (E-utilities) and PMC full text, Methods | confirmed (add: first-party titles only; cross-sectional) |
| 02:FC37 | W1: reward research is not unanimous; timing can change results (H02, H03, H09, H10) | H02 (undermining), H03 (no pervasive undermining), H09 and H10 (earlier bonus higher intrinsic motivation) all say what the paper says. "Not clean contradictions" is the paper's interpretation (XI10), not a finding. | see FC26, 27, 33, 34 | confirmed |
| 02:FC38 | E3: experimental gamification evidence that numeric markers alone need not raise intrinsic motivation, cited to H01 and H04 | H04 supports it, in one annotation task. H01 never tests points, levels, badges or leaderboards (I searched the full text). | H04 abstract; H01 full text | corrected (cite H04 only, changes 7) |
| 02:FC39 | H04 points, levels, leaderboards raised output, not the same motivation | Same as FC28. | H04 abstract | confirmed |
| 02:FC40 | H11 reviewed studies were cross-sectional | Same as FC35. | H11 abstract | confirmed |

Optional OL rows (does the source plausibly support the use?):

| Row | Use | Check | Verdict |
| --- | --- | --- | --- |
| 01:OL1 | Six benefits of a progression event (H01, H04, H06, H07, M04) | No source lists these six; each supports a piece (autonomy/competence, markers alone not enough, learning chains). The list is the paper's synthesis. | unverified (keep OPINION) |
| 01:OL2 | Learning vs unlocking a mechanic (H06, H07) | H06 skill chains and H07 fun-as-learning support the lens. | confirmed (as a lens) |
| 01:OL3 | Early win, challenge choice (H01, H05) | H01 and H05 support competence-enjoyment and a moderate challenge-skill/flow link. "Easy competence for relaxers, hard goals for experts" is in neither. | unverified (specific claim OPINION) |
| 01:OL4 | Empty-level audit (H04, H06) | H04 shows markers did not raise intrinsic motivation in one task; the audit idea is the paper's. | unverified |
| 01:OL5 | Grind definition (H01, H06, H08) | None of the three defines grind. C08 (not cited here) does mention grind. | unverified (definition is the paper's) |
| 01:OL6 | Timeline template method (W02, W04) | W04 says statistics show that something happens, not why; W02 is a simulator talk. Lean-support only. | confirmed (as a lean) |
| 01:OL7 | Cross-case synthesis S2 (C02, C04, C05, C10) | Each of the four statements matches its source as checked in table C; Hearthstone also changed totals (see CL34). | confirmed |

## E. Tool practice: W01-W05, W08 (outside both claims lists; from the paper's register)

| Row | Claim in the paper | What the source says | Where and how read | Verdict |
| --- | --- | --- | --- | --- |
| W01 | GDC 2025 microtalks: Scott (Psychonauts 2 shared progression scheme), Pierre (Cityscapes: Sim Builder), Coleman (Merchant Guilds with Apps Script deployment) | Session overview names exactly these talks. | gdcvault.com/play/1035550, session description; abstract only | confirmed |
| W02 | Morris, Spryfox, metagame simulator, GDC 2019 | Overview: simulating the metagame, "pre-analytics" before the metagame is built. | gdcvault.com/play/1026489; abstract only | confirmed |
| W03 | Exhaustive enumeration (exact) vs Monte Carlo (estimate); Excel as one tool | "The first way gets you an exact answer"; Monte Carlo as the fallback; Excel simulation shown. Dated 2010-07-28. | gamebalanceconcepts.wordpress.com Level 4 | confirmed |
| W04 | Level 8 (2010-08-25) | Statistics "can tell us that something is happening, but it can't tell us why". | Level 8 page | confirmed |
| W05 | NIST gives Wilson and exact binomial intervals and warns normal approximations may be inadequate | Section 7.2.4.1: Wilson interval (Wilson 1927; recommended by Agresti-Coull and Brown-Cai-DasGupta; lower limit cannot be negative). For very few failures or very small N, symmetric normal-approximation limits "may not be accurate enough"; an exact binomial method follows. Page is undated. | itl.nist.gov/div898/handbook/prc/section2/prc241.htm | confirmed |
| W08 | Resource generation, destruction, trading (basis for the paper's ledger check) | Level 10 lists resource generation, destruction (burn or convert) and trading. The accounting identity itself is the paper's, not Schreiber's. Dated 2010-09-08. | Level 10 page | confirmed |

## F. Dates and derived math

| Row | Claim | Check | Verdict |
| --- | --- | --- | --- |
| 01:CL36 | Nine curve formulas and their n = 0, 1, 2 samples are correct math | No external source. CV1-CV7 samples recomputed by substitution; CV3 F(1) = b, F(2) = 3b; CV5 at n = 0 gives a. All right. CV8 and CV9 are the extractor's conditional derivations. | confirmed (arithmetic) |
| 01:CL37 | X_l = sum e_j; constant e gives linear X, linear e gives quadratic X; time = X/q | Right (e = 1000*j gives X = 500*l*(l-1); recomputed). | confirmed (arithmetic) |
| 01:CL38 | M01 dated 2016-10-04, M04 2010-07-14 | M01: original blog byline October 04, 2016. M04: post "July 14, 2010 at 12:17 pm". | confirmed |

## Possible issues from the notes that this check settles

| Issue | Answer |
| --- | --- |
| 01:Z02 TFT 268 vs 228 -> 288 | Resolved by arithmetic: 20 unlisted XP for levels 1 to 5 in both totals (see CL25). The patch page itself does not itemize it. |
| 01:Z03 C01 later dates | Resolved: 2017-02-01 = Game Developer syndication; 2021-07-30 = author's republication on sirpinski.com; original 2017-01-12. |
| 01:Z05 Clash "December 4" | Resolved: December 4, 2023, effective date (next season start). |
| 01:Z06 Hearthstone "nearly 20%" and "level 51" | Resolved: Blizzard's own words; levels beyond 50 are the bonus levels. |
| 01:Z07 Diablo 200 -> 300 | Resolved: Paragon points earned by leveling. |
| 01:Z08 LoL milestones | Partly: 4 milestones per split plus a repeating one; marks 1, 1, 2, 2 and 1. "Split" is not defined on the page. |
| 01:Z09 Overwatch numbers | Partly: borders every 20 levels, fiery at 60, curve flat from 20; the page does not link the cadence to the flattening. |
| 01:Z10 Mario Wonder | Resolved: six worlds plus the Petal Isles area = seven. |
| 01:Z11 prestige symbols | Resolved: c is "currency" (c_L lifetime, c_M max, c_R this run); p total, delta-p gained. |
| 02:XI2, XI6 index origin, 7.87 | Resolved: the source's own footnote says the base is "technically 3.738" (= 4/1.07) with the first stand free; 7.87 = 4 x 1.07^10 uses the simplified base 4. |
| 02:XI3 M04 extension | Resolved: general rule stated in words ("triangular", "and so on") and the 1000:1 ratio. |
| 02:XI9 H01 vs H04 | Confirmed as a loose cite: H04 only. |
| 02:XI11 "MMO survey" | Resolved: Study 4. |
| 02:XI12 H05 year | Resolved: 2015 issue (10(5)), online 2014-10-15. |
| 02:XI15 M06 | Resolved: 18% is the example's gear bonus; 20% is the base Vulnerable multiplier. |

## Changes the skills must make (corrected and dropped rows)

No row is dropped. Corrections:
1. Prestige inputs (02:FC06): do not write "three prestige inputs". Write: Pecorella lists four ways to compute prestige (max earnings; lifetime earnings; earnings since last reset; upgrades bought since reset) and sorts them into two categories, lifetime-based and since-reset. Max-based sits with lifetime in his sorting. The three variables he defines are c_L, c_M, c_R.
2. Log vs root (02:FC06): keep "most prestiges are a fractional exponent, not a log", and add his exception: Clicker Heroes really has a log-like effect. Do not say all idle prestige formulas are roots.
3. 7.87 and 3.738 (02:FC02): say "M01's example 4 x 1.07^10 = 7.87 uses the simplified base 4; the author's footnote gives the technical base 3.738 (= 4/1.07, first stand free)". Do not use 7.87 as the cost at 10 owned in a model where the second stand costs 4 (that is 7.353).
4. M01 date provenance (02:FC05): original is the Kongregate developer blog 2016-10-04; the 2021-07-30 republication is the author's own site sirpinski.com, not Kongregate. Game Developer copy: 2016-10-13. Same for M05 (2016-10-28 original; Game Developer 2016-12-14) and C01 Part III (2017-01-12; Game Developer 2017-02-01).
5. LoL mastery (01:CL22): call it "Riot's January 2024 pre-release design announcement (release planned for the start of summer 2024; feedback invited)", not an explicit "proposal". Still not current rules.
6. Hearthstone (01:CL34, and K7.O/Q4 in note 01): Blizzard changed BOTH the total (37,000 XP removed, nearly 20%; gold added at levels 27 and 30) and the spacing (bonus levels 150 -> 350, 50 gold each from 51). It did not call the payout large. Do not teach "spacing fixed without changing the total".
7. Gamification cite (02:FC38): the "numeric progress markers alone need not raise intrinsic motivation" finding rests on H04 only, in one image-annotation task. Remove H01 from that sentence.
8. Rule 2, Rule 6 (01:CL32, CL33): these are the paper's method principles (OPINION), not findings of C03, C08, C02 or C10. Use the source dates only.
9. OL rows (01:OL1, OL3, OL4, OL5): the six benefits, challenge-choice reading, empty-level audit and grind definition are the paper's synthesis; no source states them. Keep them as OPINION.

Wording and scope notes (not corrections of fact, but a skill that copies the paper should keep them):
- Diablo (01:CL10): Torment tiers unlock on BEATING Pit tier 20/35/50/65. 200 -> 300 is Paragon POINTS.
- Realm Grinder, AdCap, Cookie Clicker (01:CL03): "8x" is exact for lifetime earnings under a pure cube root; the author writes "roughly 8 times the previous run".
- M06 (02:FC22): 18% is a worked-example gear value.
- H07 (02:FC31): say "interpretable" or "open to interpretation", not "readable".
- H12 (02:FC36): first-party Nintendo titles only; cross-sectional, pre-registered; Prolific US adults.
- H01 (02:FC25): the authors call Studies 1-3 "largely experimental"; the need-enjoyment link is still an association (needs were measured).
- M04 5-HP (02:FC16): the source says "everything in your game has 5 hit points" and the point is a cost peak; the hit counts (2 vs 1) are the paper's arithmetic.
- TFT totals (01:CL25): the 228 and 288 are the patch page's own figures; the extra 20 XP is inferred.

## Unreachable sources and limits

- H05 publisher page (tandfonline.com): HTTP 403 for curl and WebFetch. Abstract read through OpenAlex and issue data through Crossref. Abstract only; no full text.
- H02, H09, H12: PubMed HTML returns a JavaScript challenge; read the PubMed XML record from NCBI E-utilities (abstract level). H12 also read in full on PMC.
- H04: the Aalto institutional record only (abstract); the journal page was not opened. Abstract only.
- W01, W02: GDC Vault session descriptions only; no talk video or slides.
- Kongregate's current pages show no post date; the original dates come from the Wayback captures of the old blog and the author's repost.
- TFT early-level XP (the 20): not on the patch page; the cross-check was a third-party search snippet for a later set. Inference marked as such.
- Not checked (out of ticket): R-ids, W06, W07 (J011-T06); whether any 2026 live value of these games still matches (the paper does not claim it).
