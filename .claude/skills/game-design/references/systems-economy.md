> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N3 §4 (systems, economies, balance, rewards, Roblox monetization), FR (Roblox facts, RC ids), FI. Tags as in SKILL.md. Roblox rules change: recheck with `platform-policy` before launch. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (new §8 cosmetics and variants, §9 honest paid random reveals).

# Systems, progression, economy, rewards

## 1. Resources (N3 §4.1)
Dormans models four roles: **sources** create, **drains** destroy, **converters** change one resource into another, **traders** move resources between owners, including abstract ones like health (D28 V, a method, not proof of fun). For each resource record 10 fields: unit · owner · storage or cap · creation event · destruction event · transfer · conversion · spend choice · variability of gain · exploit surface (O).
- Reconcile: closing = opening + created or incoming − destroyed or outgoing; count conversions per resource.
- A payment between players changes distribution; it is not a sink unless a fee is destroyed.
- Keep apart: wealth accumulation, currency supply, item scarcity, market price.

## 2. Model before tuning (N3 §4.2 O)
Building the numbers (curves, timelines, model-player simulation, data tables, live tuning) is the progression designer's job: `progression-design` (what to aim for) and `progression-craft` (how, with `tools/progression/`). This file judges the design; it does not repeat their math.
Spreadsheet or script with named assumptions and repeatable scenarios. Run 9 scenario groups: new vs experienced · efficient vs inefficient strategy · solo vs group · short vs long sessions · full trading vs none · lucky vs unlucky draws · return after absence · maximum-earning route · adversarial transfer loops. Judge distributions and bottlenecks, not one average income curve. Search for 6 problems: an early lead that becomes irreversible · catch-up that erases a deserved skill lead · conversion arbitrage · stale sinks · currency starvation · stockpiles that trivialise the next update. A simulated player is one strategy, not the population.

## 3. Balance (N3 §4.3)
Workflow (O): state the viable strategies and intended asymmetries → collect outcome and selection data per condition → inspect real decisions and failure points → find the mechanism → change the narrowest lever → retest the affected and the neighbouring populations. Read effectiveness by familiarity, opponent, map, team, unlock state and input. A low pick rate can mean unfamiliar, badly shown, narrow or weak. A 50 % aggregate win rate can hide polarised matchups. Riot's 2019 framework splits four audiences (Average, Skilled, Elite, Professional) and uses pick/ban "Presence" where Elite samples are small (D15 E, FI); Mega Crit combines expert testers, metrics, streamers and feedback (D16 E).

## 4. When the economy damages the core loop
Blizzard judged that the Diablo III auction house undermined the intended monster-to-loot loop and closed it on 18 March 2014 (D17 E; FI). Not a ban on markets; a warning that the fastest reward path must not replace the activity that defines the game.

## 5. Progression and rewards (N3 §4.5 O)
- Every unlock names its purpose: new verb · new tradeoff · expression option · world access · mastery test · social responsibility · a deliberately wanted convenience. A bigger number alone is not a new experience.
- Judge reward cadence by time to the next meaningful choice and by the tail of unrewarded attempts, not average payout. Keep predictable skill recognition apart from uncertain discovery.
- A reward schedule is written as a rule with 5 answers: what makes it eligible (action or elapsed time) · fixed or variable amount and timing · what the player knows · what happens after repeated failure · whether absence loses anything. Record expected outcome and the bad tail where calculable.
- Never claim variable rewards are more fun by nature; never use uncertainty to hide costs.
- Long-term goals without coercion: several understandable aspirations; goals may change; earned progress kept; explicit comeback paths; optional events separate from mandatory power. No streak loss, escalating absence penalties, fake scarcity or exhaustion loops. Success includes player-valued accomplishment and voluntary return, not only time extracted.
- Every price states its purpose: expression, access, convenience or power. Review free-play and competitive effects separately.

## 6. Roblox monetization and young players (FR, checked 2026-10-20)
| Fact | RC |
| --- | --- |
| Products include passes (one-time), developer products (repeatable) and monthly subscriptions; Roblox lists more types | RC19 (partly) |
| No false scarcity; no timers that are wrong or restart; discounts must be genuine; never mislead, confuse or pressure a purchase | RC20 |
| Paid random items: show every outcome and its odds before spend, as percentages summing to 100 % (long decimals may be rounded to 4+ places past the first non-zero digit, with a disclaimer); keys, tickets, luck boosts and pity systems count, and odds update while a boost is active; every outcome must give the buyer some benefit; random rewards earned with no Robux or paid currency need no odds | RC21-RC23 |
| Check `PolicyService` `ArePaidRandomItemsRestricted` and `IsPaidItemTradingAllowed`; restricted players get one of the allowed treatments (blocked or a compliant alternative) | RC23 |
| Ads: no personalised ads for under 18; no rewards that push under-13s to engage with ads; rewarded video is 13+, opt-in, a fixed non-random reward, never a forced progress gate; integration rules in force since 2026-05-04; the standards page changed 2026-10-09 (recheck) | RC24-RC26 |
| Ad integrations need registration, review, labels and `GetCampaignEligibilityAsync`; immersive ads fall back for ineligible users and eligibility never guarantees an ad | RC27, RC28 |
| Platform: FY2025 average DAUs mobile 83 %, desktop 14 %, console 3 % (annual average, not a session split); Q2 2026 about 123 million DAUs (Q1 2026: 132 million); of age-checked users in the last week of June 2026, 35 % under 13, 38 % 13-17, 27 % 18+ (age-checked subset only, 57 % of DAUs) | RC01, RC04-RC07 |

Design rules from these (O): before estimating revenue, specify free play, the bought benefit, recurrence, odds, eligibility, fulfilment and fallback. Never make essential progress depend on an ad being served. When policy texts seem to conflict for a format, settle it through Roblox's current official flow, not an invented reading (the paper's "under-13 tension" in ads was not found on any page: RC56, OPINION).

## 7. Systems check (10 items, N3 §4.7 O)
Run every applicable item; "not applicable" needs a reason. Pass / Fail / Unproven.
| # | Item | Pass when | Why |
| --- | --- | --- | --- |
| 1 | Progression | each unlock changes capability, strategy, expression or access, stated | a bigger number alone is not a new experience |
| 2 | Power | old and new players compared in every competitive or cooperative interaction | progression can lock one group out of meaningful play |
| 3 | Economy | all sources, sinks, transfers, caps, losses, refunds and persistence listed | prices alone do not explain balances |
| 4 | Exploit | repeated, concurrent, interrupted and replayed transactions tested | the rule must survive edge cases in code |
| 5 | Reward | the behaviour that earns it and what players know are stated | unclear or coercive schedules break the intended experience |
| 6 | Paid randomness | current Roblox rules, disclosures and per-player eligibility verified (§6) | a design preference cannot waive platform policy |
| 7 | Balance | population, context, competing goals and unwanted dominance defined | averages hide extreme subgroups |
| 8 | Tuning | every value has units, rationale, revision and a test | unexplained constants cannot be changed safely |
| 9 | Interactions | cross-system effects and feedback loops simulated or tested | locally fine rewards can add up to a runaway |
| 10 | Cadence | new content told apart from repeatable variation; production dependency stated | an update plan beyond the team's capacity is not a design |

## 8. Cosmetics and variants (skins, pets, trails, auras, tower and building tiers)
Gameplay comes first. Cosmetics refresh repeated play (the same routine in a new look) without changing balance; players must never pay for a disadvantage.
- **The role read stays.** A cosmetic keeps the unit reading as the role it plays (a fragile ranged unit stays slim and sharp, never armoured and tanky), keeps the base proportions and height, takes no extra screen room and never hides combat information. Each class has a silhouette rule (mass and shape) every variant is checked against.
- **No stats.** Cosmetic items change no value in the data tables. A skin that changes reach, hitbox size, visibility or sound loudness changes gameplay and is reviewed as a balance change.
- **Footprint limit.** Every cosmetic brief sets a screen-footprint limit; cosmetic effects stay below combat-effect brightness and never pulse like a threat or pickup.
- **Identity anchors.** A variant keeps the 2-5 features players know the original by (its anchors, held in the art bible) and changes theme, material, colour and costume; for a held item, its recognition features and contact points. A remake or update lists what players love (kept, brought forward) and what feels dated (trimmed, or kept with a reason), so it never becomes a parody of the original.
- **A variant is a story.** The brief has a short narrative (the character's role in the new theme), one line "keep core X, swap item Y for Z because of W" when an iconic item changes, and a re-theme of each ability's effect and sound, not only the costume (players feel the theme through what they do).
- **Each theme has its niche.** Before a new theme or event line, list existing themes and write the new one's differentiator in one line; pick themes from player data and say which proven themes it combines and at what maturity (young audience: lower maturity is the default). Refresh a tired line by one extreme pass and one pass pulled back to the brand; the owner picks.
- **Tiers.** Standard items follow the art bible; the top rarity tier may break the mould only by a documented decision (art director proposes, owner decides). Premium items keep at least the base's secondary motion; richer motion and separate finishes signal value.
- **Sensitive themes** (captivity, violence, real cultures) move onto a prop motif instead of an act or scene; culture and ethnicity are represented accurately; `platform-policy` for anything that could read badly.
- Checks: black-fill area and width-to-height ratio of variant vs base, on flat-key captures at the game camera at the same distance (`review.md` §7: an in-scene capture gives no mask), stay in the class band (PROPOSAL default: within about 10 % of base area; `python tools/art/look_check.py silhouette <flat-key capture>` on each gives area and bbox, or `--mask` when no flat key is possible; `--compare <base capture>` adds the aligned shape IoU); phone-size captures with and without the cosmetic: covered screen area compared and combat cues still visible; the data diff of a cosmetic shows no gameplay value; every anchor present (at most one hidden by a pose); a fresh reader names the base character or item from the variant's silhouette and also names the new theme.

## 9. Honest paid random reveals
When players pay (Robux or bought currency) for a random result, the reveal must not mislead. This is a design rule and a platform rule; `platform-policy` holds the current wording and PolicyService checks.
- Odds for every outcome are visible before the buy button and sum to 100 %; effects never cover or animate them; they update for the player while a boost is active or after a once-only outcome is won; a long list may open in a pop-up from a visible worded "Info" or "Details" label, never a bare icon.
- **One windup for every result.** The same beats and length up to the result frame for the lowest and the highest tier; rarity colour, escalation and tier layers start only after the result is shown.
- **No near-miss.** A lower result never shows a higher tier's layers ("so close" animations are banned); a result worth less than its price is not celebrated; luck boosts never look like better odds than the numbers.
- **Tiers read without colour alone.** Each tier adds layers with rarity (ring, rays, a crescendo, a unique motif; pure white only for the top tiers) and is named in text and frame shape.
- After the result is confirmed, a tap skips to it; in batch opens only the best result gets the full ceremony.
- The restricted-player path (paid random items not allowed in the player's region) exists and is tested.
- Checks: frame-compare the lowest and highest tier captures up to the result frame (a short Python image diff of the two frame sequences): identical; no higher-tier layer on any lower result; each tier nameable in a grayscale capture; odds visible before the buy button, and changed in a capture with a boost active; the restricted path captured.
