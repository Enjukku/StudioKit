> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-design`. Sources: 02:H01-H12, W1-W9, E1-E6 (studies checked in FC-M: designs, populations and sample sizes confirmed); 03:EA1, EI1-EI3, RP1-RP4, RC1-RC20 (Roblox rules checked in FC-R against the docs mirror rev 7400643 and live pages, 2026-10-21). Roblox rules move: `platform-policy` is the current rule book; recheck before launch. Not legal advice. Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (clocks mapped to tiers, luck placed on purpose, odds updates after a once-only win, long-list display, paid results honest).

# Rewards, randomness, ethics, premium fairness, Roblox rules

## 1. What the reward research can and cannot say (02:H01-H12, E1-E6)
| Source (date) | Design and population (FC-M) | What it supports | What it does not |
| --- | --- | --- | --- |
| Ryan, Rigby, Przybylski (2006) | 4 studies: lab samples 89, 50, 58 (Studies 1-3, "largely experimental"), online MMO survey 730, ages 16-44 | felt autonomy and competence go with enjoyment; relatedness too in the MMO survey | that a given progression tree causes retention |
| Deci, Koestner, Ryan (1999) | meta-analysis, 128 experiments, children and students | expected tangible and several contingent rewards lowered free-choice intrinsic motivation; positive feedback raised it; worse for children | that virtual loot equals the tested rewards |
| Cameron, Banko, Pierce (2001) | competing meta-analysis | effects depend on task interest, reward expectation and link to performance | a blanket "rewards always harm" or "always help" (01:R10) |
| Mekler et al. (2017) | 2×4 online experiment, image annotation | points, levels, leaderboards raised output, not intrinsic motivation or competence | anything about entertainment games; this is the only source for "numbers alone need not motivate" (FC-M #7) |
| Fong, Zaleski, Leach (2015) | meta-analysis of 28 studies (abstract only) | challenge-skill balance relates to flow, less to intrinsic motivation; clear goals and control matter | an optimal difficulty ratio; equal stats ≠ flow |
| Cook (2007), Koster (2005) | designer frameworks (E) | progression as learning chains; boredom after mastery; renewable challenges | proven psychology; comfort and social play matter too |
| Schreiber (2010) | course lessons (E) | XP→level→upgrade and time→XP must be read together | measured pacing |
| Woolley & Fishbach (2018); Liu et al. (2022) | randomized experiments; adults; Liu ages 17-26, n = 87/58/58/144 | earlier or immediate rewards raised intrinsic motivation in those tasks | a seconds-per-reward rule |
| Montiel et al. (2022) | scoping review, 16 cross-sectional studies, 6 with adolescents | loot-box engagement associated with problem gaming/gambling | cause, or that every free random drop is the same as a paid loot box |
| Ballou et al. (2025) | 703 US adults, 150 first-party Nintendo titles, cross-sectional | playtime did not predict well-being; perceived gaming-life fit did | safety of every design, or anything about children or Roblox |

Use (O): report the disagreement, not a slogan; test timing and usefulness locally (02:W1, E6).

## 2. Four reward clocks (02:W2-W4, O)
Keep apart and test each on its own: (1) **feedback** right after an action, (2) **completion** of a small objective, (3) a **consequential upgrade**, (4) **new content or mastery**. Make feedback readable, but not every feedback event pays currency or unlocks a system. Neither "a reward every 30 seconds" nor "always delay rewards" is supported as a universal rule. The clocks map onto the celebration tiers (`reward-tiers.md`): feedback is T1, a completed small objective T2, a consequential upgrade T3, new content or mastery T3 or a track's T4 capstone; each tier is checked against its measured rate.

Spacing (01:K7, D-08): judge a track by the gaps between usable rewards and the tail of long unrewarded stretches, not by its total; the simulator reports the gaps.

## 3. Randomness (02:W5-W8, O)
- Use surprise for routes, combinations, presentation and optional discoveries; keep cost and basic entitlement understandable. Randomness does not replace authored interesting results.
- Essential progress: a deterministic path or a visible bounded fallback (pity) instead of unbounded luck. A guarantee states what advances its counter, whether it persists, and what resets it. Test the unlucky tail, not only the mean (`progression-craft` math §4).
- **Place luck on purpose.** Per track, write where randomness sits (start, drops, crafting, matchmaking) and where skill decides, for the target audience. Luck keeps outcomes open; skill makes wins feel earned. Check with skill profiles over many seeds (`progression-craft/references/tools.md` §6c): a skilled profile recovers from an unlucky start; a struggling one sometimes reaches what the row meant for everyone. Randomness placed by accident is a finding.
- A random amount never decides how big a reward feels; size follows rarity or difficulty the player can learn (`reward-tiers.md` §5).
- Transparency and pity are safeguards, not proof a paid random system is harmless.

## 4. Ethical pacing (02:W7, W9, O; owner-approvable studio policy)
Never: tailor bad luck or friction to push a purchase · imply a near miss improves the next independent chance · take earned progress for a missed day · trigger purchases with invented emergencies · sell paid power as the escape from deliberately slowed pacing.
Always: natural finish points, reliable saves, a clear next goal, leaving without losing earned rewards. A session the player chose to end is not a retention failure; measure enjoyment and felt freedom next to return rates, never optimize for inability to stop.

## 5. Premium fairness (03:RP4, EI1-EI3, O)
- What payment may bypass is an owner decision, per item: cosmetic expression, convenience, content access, waiting, or competitive power. Show the real price and the grant; keep a viable non-paying route; measure non-payer completion and competitive outcomes apart. "Legal", "possible with the API" and "fair" are different claims.
- Rebalance the bundle, not one number: Clash of Clans' 2025-10-06 update removed Town Hall weapon upgrade levels at TH12-TH15 (weapons start maxed; ongoing upgrades cancelled without refund), moved 15 hero levels from TH15 to TH14 and cut Loot Cart recovery 20 % → 10 %, alongside loot changes (E, FC-R FO01-FO03). Model the combined effect; never copy the percentages.
- Regional prices: Roblox Managed Pricing sets eligible item prices from economic-location signals within 30 %-100 % of the creator's default; `MarketplaceService:GetUsersPriceLevelsAsync` (levels 1-1000; call at join, do not cache; test the return shape, the guide and the reference differ) lets you restrict transfers between price levels (V, FC-R FB03-FB05). UI labels read prices at runtime (`platform-policy` P-05).

## 6. Roblox rules the progression designer must design around (V, FC-R; details and code patterns: `platform-policy`)
| Area | Rule (as checked 2026-10-21) |
| --- | --- |
| What is a paid random item | anything random bought with Robux directly, or with currency, keys, tickets or re-roll tokens bought with Robux; luck passes and boosts; pity systems; bundles containing a random item; contents unknown at purchase; previewed "next outcome" systems. Not covered: skill-based variance, cosmetic-only random visuals, random rewards earned without Robux or paid currency (FB06, FB09) |
| Mixed earned + bought currency | no page decides it; the studio treats it as paid (stricter reading, ours) (FB09) |
| Odds display | before purchase, every possible outcome with its numeric probability, percentages totalling 100 %; long decimals may round to 4 or more places below the first non-zero digit, with a disclaimer that displayed odds are rounded and may not total 100 % (FB07b) |
| Luck boosts | explain the numeric effect and show updated odds while active (FB08) |
| Once-only outcomes | when an outcome can be won only once, the shown odds update for that player after it is won (`platform-policy` rules A) |
| Long lists | may open in a pop-up from a visible worded "Info" or "Details" label, never a bare icon; equal odds may share one line (`platform-policy` rules A) |
| How the result is revealed | one windup for every result, no near-miss, no celebration of a result worth less than its price: `game-design/references/systems-economy.md` §9; my side is the tier and value-vs-price columns of `reward-tiers.md` |
| Every outcome | must give the buyer some benefit (Community Standards; DF 4654622) (FB06) |
| Eligibility | `PolicyService:GetPolicyInfoForPlayerAsync` → `ArePaidRandomItemsRestricted`, `IsPaidItemTradingAllowed` (the trading flag covers all paid items, random or not) per player; never guess from age or country; fail closed (FB10-FB11; `platform-policy` P-02) |
| Restricted players | six documented treatments: (1) an unpaid earnable path, (2) a predetermined order disclosed before purchase, (3) a guaranteed direct purchase priced on expected value, (4) remove or hide the item, (5) block the purchase with an error message, (6) move the player out of those areas. Hiding is best; a buy button that refuses is "technically compliant" but confusing (FB12) |
| Price of a guarantee | Roblox's example: a 10-Robux draw at 5 % next to a 200-Robux guaranteed item, priced from expected value; 200 Robux of 10-Robux tries succeeds only 64.15 % of the time (FB13) |
| Younger players | PolicyService integration is required; avoiding urgent or pushy sales wording is a named best practice; Kids accounts (age-checked 5-8) and Select (9-15) since 2026-06-16, by region; linked parents can limit spending and screen time until 13. Never assume a young player can buy, chat, trade or play long sessions (FB14-FB17) |
| Ads | no personalized ads to under-18s; rewarded video only through Roblox's product, 13+, opt-in, fixed (not random) reward, delivered immediately; never a forced progression gate; under-13s never rewarded for ad engagement (Advertising Standards, last updated 2026-10-09; these rules predate that update) (FB18-FB22) |
| Economy guidance | Roblox's tip that net sources minus sinks should be close to zero is a reading tip for the dashboard, not a law; growth can be intended (FB01; 03:EA6) |

Design consequence (O): progression must have a complete route for a player who cannot buy, cannot roll paid random items, cannot trade and plays short sessions.
