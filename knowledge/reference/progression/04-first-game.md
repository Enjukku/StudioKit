---
type: reference
scope: universal
status: active
updated: 2026-10-21
source: "J011-T04, DestructionSimulator knowledge/design + systems (read-only)"
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-21

# Progression lessons from the studio's first game (owner rulings, failures, data practice, telemetry plan)

The first game's files were read only. Nothing in that folder was changed. The lesson column of every row is written for any game and names no item, zone or number of that game. The game-specific detail sits only in the last column. The owner's words are copied exactly in the "Status and owner's words" column; they contain the game's own nouns because they are quotes. No player data exists: the game had no public test (FG:decisions.md:124), so every number below is a design number, not a measured one.

## 0. How to read

| Key | Meaning |
| --- | --- |
| FG:file:line | Line in the first game's file. File names are short; the path map is below. One cite = one line of that file. |
| Row IDs | O owner ruling. F failure, problem found or gap. S structure practice (how numbers were stored). P agent proposal shape (not decided). T telemetry practice. Q open question. |
| Kind | owner ruling, tried-and-failed, structure practice, telemetry practice, open question, problem found (found in a log or review, not in the failed-approach register). |
| DECIDED | The decision ledger holds a row. The owner's words are quoted when the ledger records them. The ledger says kickoff and review rows are "paraphrased faithfully" (FG:decisions.md:6), so those rows read "words not recorded". |
| PROPOSAL | An agent wrote it. The owner has not confirmed it. It is never a decision. |
| OPEN | A question the owner has not answered when the file was read. |
| FOUND / FIXED | A problem seen by an agent or reviewer; FIXED means the file says it was repaired. |
| (extractor) | My arithmetic or check, not the game's text. |

Path map (all under `C:\Users\Firew\Downloads\uterd\DestructionSimulator\`): decisions.md, economy.md, gear.md, pets.md, brick-strength-stages.md, telemetry.md, tried-and-failed.md, open-questions.md, 00-game-overview.md, game-framework.md = `knowledge/design/`. economy-loop.md = `knowledge/systems/`. 2026-10-12-stage-strength.md = `knowledge/logs/`. 00-roadmap.md = `knowledge/plans/`. owner-profile.md = `rules/`. economy.json, weapons.json, charges.json = `content/economy/` and `content/gear/`. specs.py = `tools/content/`. test_economy_content.py = `tools/tests/`. Amount.luau = `src/shared/Economy/`.

## 1. Owner rulings (what the owner decided)

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| O01 | Pay for clearing content in later zones follows the content's toughness through a smooth curve, not a flat per-zone multiplier. The same content is tougher in each later zone, so gear must scale with the zone. The curve shape is chosen for fun; numbers need not be round. | owner ruling | DECIDED D-174, 2026-10-12: "the same concrete on that stage is significantly tougher"; "scale it in the way that it's the most fun for the player rather than some like flat thing" | FG:decisions.md:184 | Flat "Brick mult" column (1x to 4,500x) replaced by strength S (1 to 870,000 over 14 stages) and yield = S^0.85 (FG:brick-strength-stages.md:125,140-155). |
| O02 | A rare variant of ordinary content has its own payout multiplier, not derived from the zone curve, so it does not scale twice. | owner ruling | DECIDED D-174, 2026-10-12: "a 1% chance that each concrete brick is like a diamond brick ... a multiplier that it isn't necessarily based off strength" | FG:decisions.md:184 | Variant table (stage, material, variant, chance, yield_mult) is design only, not built (FG:brick-strength-stages.md:168-180). |
| O03 | A regress guard is part of the scaling purpose: farming an early zone with top gear pays little, later zones pay more, and gear from earlier zones stays usable. | owner ruling | DECIDED D-174 (purpose sentence) and D-018; words not recorded | FG:decisions.md:184; FG:decisions.md:27 | Stage 1 farming with top gear "pays little". |
| O04 | Remove the chore step between action and reward: credit at once, show a short animation. Products sold to ease the chore lose their purpose and must be replaced. | owner ruling | DECIDED D-122, 2026-10-09: "for number four, sure. I think that's the best optimization we can have"; earlier: "maybe we don't make it so the player has to collect bricks anymore ... it just goes from animation on their screen coming from the building ... into the brick counter" | FG:decisions.md:132 | Range upgrade, auto-collect pass and one pet type lost their purpose (FG:open-questions.md:29). Replacement idea: bigger capacity or a 2x income boost. |
| O05 | Knock-on rewards (results a player caused but did not hit directly) pay the players involved, shared by their contribution. The rate is a separate number set by an agent. | owner ruling | DECIDED D-066, 2026-10-02: "a collapsed building can give credit to those involved". The 0.5x rate and the split by direct share are agent numbers (PROPOSAL). | FG:decisions.md:76 | `consequence_credit_rate` 0.5 (FG:economy.json:9; FG:economy-loop.md:50-52,145). |
| O06 | Payout follows the size of what was cleared (volume in reference units), not a flat count per piece. | owner ruling | DECIDED D-069, 2026-10-02: "I believe a brick's value should follow its size" | FG:decisions.md:79 | Reference unit = 1 x 2 x 1.2 studs; value rounded up. |
| O07 | Harder content pays more. | owner ruling | DECIDED D-075, 2026-10-02: "there might be some steel beams in your way, and those are a little bit harder to break"; "for the obsidian towers ... it doesn't take too much blast damage. And then materials like that should go for more money"; "for materials like wood, maybe it's easy for wood to snap in half if there's a heavy object" | FG:decisions.md:85 | Material value multiplier; numbers are PROPOSAL in a physics note not read here. |
| O08 | The owner accepted a price-growth curve as a starting point only, and gave the layout and multipliers at conversion points to the agents' judgement of fun. | owner ruling | DECIDED D-028, 2026-09-30: only "whatever is most fun" is recorded; the rest is paraphrased | FG:decisions.md:37 | Gate cost about x8 per zone accepted "as the starting point". |
| O09 | The owner fixes the first tier at multiplier 1 and asks an agent to propose the curve. | owner ruling | DECIDED D-014, 2026-09-30; words not recorded | FG:decisions.md:23 | Stage 1 = 1x. |
| O10 | Reward value that is not collected in time may be lost; the owner asked for it. A hard ceiling is still needed (see F04). | owner ruling | Owner request 2026-10-04: "merge even more ... get rid of ones that weren't collected in time"; the agent record says "value lost, owner-approved" | FG:open-questions.md:21; FG:economy-loop.md:149 | Floor tokens live 50 s. |
| O11 | No reset or prestige layer in this game. | owner ruling | DECIDED D-032, 2026-09-30; words not recorded | FG:decisions.md:41; FG:economy.md:104 | Locked as "No rebirth". |
| O12 | The premium list is income multipliers (item and currency), unlimited carry, an odds boost, auto-convenience, a premium-only pull and gifting. Paid random items show their odds (an agent policy note). | owner ruling | DECIDED D-039, 2026-09-30; words not recorded | FG:decisions.md:48; FG:economy.md:79-92 | Six passes, one premium egg, gifting. |
| O13 | The owner set the odds band for the rarest collectible and the odds of the rarest size variant, and made bulk-open an upgrade with exponentially rising cost. | owner ruling | DECIDED D-009, D-031, D-010, 2026-09-30; words not recorded | FG:decisions.md:18,19,40 | Top rarity 1 in 10,000 to 1 in 100,000 (agent chose 1 in 100,000, FG:pets.md:16); size variant about 1 in 200; bulk-open up to 25. |
| O14 | Upgrades cost the second currency; its source was left undecided at the time (see F09). | owner ruling | DECIDED D-011, 2026-09-30; words not recorded | FG:decisions.md:20 | Examples: speed, pickup range, odds. |
| O15 | When the audience is young children, reward rules must be explainable in one line each. | owner ruling | DECIDED D-115, 2026-10-09: "a younger audience ... maybe like four years old to maybe like fourteen ... mostly kids on like iPads ... predominantly young boys"; "it's a little bit of everything" | FG:decisions.md:125 | Agent turned this into "kid-simple" rules and printed odds (FG:pets.md:82,100-103). |
| O16 | The studio's foundations must work for any genre, not copy one game. | owner ruling | DECIDED D-136, 2026-10-10: "it's not necessarily about Roblox itself. It's about game development"; "a strong foundational game framework that we can use on literally a multitude of games. Whether it be story, survival, destruction, simulator, anything" | FG:decisions.md:146 | Applies to the progression kit: no genre assumption. |
| O17 | No early public test: real players arrive at full launch only, so there is no live data before launch. | owner ruling | DECIDED D-114, 2026-10-09: launch: "Full launch only" | FG:decisions.md:124 | Why every number stayed PROPOSAL. |

## 2. Failures, problems found and gaps

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| F01 | When a tier multiplier scales a difficulty threshold, items with a near-zero base escape it (zero times anything is zero), stay trivially easy and still pay the late-tier yield. Scale from a reference base so tier 1 returns the original value and soft items stay weaker than the reference. The first repair formula was wrong; the builder caught it. | problem found | FIXED 2026-10-12; agent work, no owner words | FG:2026-10-12-stage-strength.md:12; FG:brick-strength-stages.md:121 | t x S + max(base - t, 0) x (S - 1), base 25. Glass (0) at S 2.6 gives 40. |
| F02 | A "never zero progress" minimum for out-classed gear must pay the lowest-tier rate and give no knock-on share. The first version let a player farm a chain reward at the high-tier rate (reviewer finding, High). A farm test now pins it. | problem found | FIXED 2026-10-12; agent review, no owner words | FG:2026-10-12-stage-strength.md:13; FG:brick-strength-stages.md:127 | Farm test pays 1,600 against 21,281.7 before the fix. |
| F03 | Removing the trip between earning and converting opens a camping exploit (stand at the conversion point, convert every action). Real income also rises above the modelled rate because uncollected value no longer expires. Re-measure income per minute on the same route before and after such a change. | problem found | OPEN (Q-47, Q-48); mitigations are PROPOSAL | FG:open-questions.md:27-28 | Proposal: no instant credit within about 12 studs of a sell pad, or a short sell cooldown. |
| F04 | A lifetime that refreshes on merge turns into a bank that holds value past the carry limit. Add a hard ceiling counted from the oldest part, and keep it above the normal lifetime. | problem found | FIXED (review 2026-10-04) | FG:economy-loop.md:106,152 | 50 s lifetime, 180 s ceiling. |
| F05 | When stored reward value is compacted, never move it across tiers that pay at different rates, or value is laundered between rates. | owner ruling | DECIDED in D-056 (owner play-test and UI review, 2026-09-30); words not recorded | FG:decisions.md:66; FG:economy-loop.md:88-90 | "never across stages". |
| F06 | One number lived in three places with different values: an owner's example, a prose table and the data file. The data file ran the game; the other two stayed. Name one binding source and mark the others as example or superseded. | problem found | OPEN | FG:economy.json:4,7; FG:economy.md:51; FG:decisions.md:16; FG:telemetry.md:35 | Starter capacity 500 (owner example, prose) against 150 (data). Telemetry plans to log both. |
| F07 | When a curve is replaced, dependent tables (entry prices, capacity per tier, pull prices) are not re-derived by themselves. The old table stayed in the prose with a "superseded" note, and the dependents waited as open items. | problem found | OPEN (Q-48, Q-61) | FG:economy.md:29-42; FG:open-questions.md:28,40; FG:brick-strength-stages.md:131-133 | Yield x2.5 per stage against the old gate and egg prices. |
| F08 | The planned economy simulator ("simulates a player hour by hour") was never built. The pacing targets are unmeasured, and the economy slice is "gate-verified only". The first real numbers will come from telemetry after launch. | problem found | FOUND 2026-10-21 (extractor) | FG:economy.md:2,16-24; FG:00-roadmap.md:18; FG:economy-loop.md:22; FG:decisions.md:124 | `tools/econ/sim.py` is named; `tools/` has no `econ` folder (directory listing 2026-10-21). |
| F09 | A currency was given spend options while its source stayed undecided. A source was later designed, but the files read show no code that pays it. Design the source and the sink of a currency together. | problem found | FOUND | FG:decisions.md:20,37; FG:economy-loop.md:14; FG:telemetry.md:63 | Gem bricks are counted by the blast code and "credited by nobody". |
| F10 | Value proportional to size or material makes outlier payers: one oversized prop pays far above its neighbours; one surface pays several times the other ambient surfaces. Audit the top payers per zone before release. Give ambient surfaces a low pay tier with a test cap. | problem found | OPEN (Q-65, Q-54); the low tier is PROPOSAL | FG:open-questions.md:44,34,20 | Large fir about 2,200 units; mountain rock 5x other terrain; ground about 1/5 of earth value. |
| F11 | Check that the first content of each tier can be cleared with the gear obtainable at that point. Previous-tier starter gear could not fell a key target of the next tier. | problem found | OPEN (Q-68) | FG:open-questions.md:47 | Iron tower: threshold 56 x S 2.6 = 145.6 against starter power 100; next-tier gear needs a reach of about 2.3 studs. |
| F12 | The reward-delivery step was changed at least four times on owner play-test (flat icons, 3D items that merge, burst then recall, then no collection step). The owner judges reward feel in play. Plan iterations for it. | tried-and-failed | F-015 and F-019 rejected; owner play-test: "come from the same spot" | FG:tried-and-failed.md:10,27; FG:decisions.md:63-64,132 | Pickup motion D-138/D-142 replaced by D-144. |
| F13 | The failed-approach register holds no economy or progression row (20 rows; two touch reward delivery). Economy dead ends sat in logs and review notes. Write a row for each rejected curve or price. | problem found | FOUND (extractor) | FG:tried-and-failed.md:9-27 | Register rows F-001 to F-020. |

## 3. Structure practice (how the numbers were stored and protected)

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| S01 | Every tuning number lives in a data file with a schema version, a status field (proposal or locked) and a notes field that names the records that decided it. Logic modules hold none. | structure practice | PROPOSAL rule, in use | FG:economy.md:2; FG:economy-loop.md:40; FG:economy.json:2-4; FG:specs.py:247 | "Tuning happens in data, never in code." |
| S02 | A tool compiles the data file into two runtime copies: a full server-only table and a small replicated subset named in an allow-list. A new client read must be added to the list, and a test enforces it. | structure practice | in use | FG:specs.py:701-709; FG:economy-loop.md:38 | Five client fields. |
| S03 | Each field has a type, bounds and a unit comment. Cross-field "content rules" keep tuning consistent. A test mutates good data and asserts each bad value is rejected (zero, negative, NaN, text, missing). | structure practice | in use | FG:specs.py:255-261; FG:test_economy_content.py:77-100,229-233; FG:economy-loop.md:152,156,161 | Cap must exceed one batch; ceiling must exceed lifetime. |
| S04 | Tier scaling is one array indexed by tier number (index 1 must be 1) plus a list from zone id to tier number. A guard test fails when a content zone has no row (it would silently use the tier-1 value) or a row names no zone (typo). | structure practice | in use | FG:specs.py:395-399,411,436; FG:test_economy_content.py:272-283; FG:economy.json:11-27 | Test zones use tier 1. The array has room for 64 tiers; 14 are used. |
| S05 | A test pins the data array to the design note's table, so a drift between prose and data fails the gate. | structure practice | in use | FG:test_economy_content.py:238-247 | Message names the design table. |
| S06 | A new scaling layer must be an identity at the first tier. A regression checksum (same outcomes with and without the table) proves it, and a test proves the minimum-hit rule never fires at tier 1. | structure practice | in use, gate-verified only | FG:2026-10-12-stage-strength.md:17; FG:test_economy_content.py:249-270 | 120 blasts, 7,758 kills, same checksum. |
| S07 | One function normalises every stored, compared or sent amount: NaN, infinity, negative and fractions become safe whole numbers, and the value saturates at the largest exactly storable integer. | structure practice | in use | FG:Amount.luau:1-29 | Ceiling 2^53. |
| S08 | When the payout unit changes, calibrate the divisor so a reference object pays about its old count. A test pins the divisor. Fractions are carried per player so no rounding value is lost. | structure practice | in use | FG:economy-loop.md:46-55,144; FG:test_economy_content.py:79-80 | Divisor 5; a reference house pays 482.0 for 470 pieces. |
| S09 | Convert in a safe order: remove the carried units first, then pay the currency, so a failure can lose units but never duplicate currency. Carried value is committed at checkpoints, not on every change. | structure practice | in use | FG:economy-loop.md:114,118-119 | Commit every 3 s and before a sale. |
| S10 | Gear rows hold stats but no price; entry and pull prices exist only in prose. Pricing then cannot be simulated or tested, and the telemetry item ids wait for a shop. | problem found | FOUND (extractor) | FG:weapons.json:14-26; FG:open-questions.md:29; FG:economy.md:31-42 | Rows: power, rate, bonus, range. No `price` key. |
| S11 | The owner dictates by voice, so IDs and numbers can arrive wrong. Echo a number back when a wrong guess would change the result. | structure practice | rule in the game's owner profile | FG:owner-profile.md:9 | "Q19" meant Q-29. |

## 4. Agent proposals: shapes and ratios (PROPOSAL; none is decided)

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| P01 | Pacing targets are a table of milestone against play time: first conversion, first purchase, first gate, then a growth rate per tier and an end total. The first-gate time, the growth rate and the end total can be cross-checked as a geometric series. | structure practice | PROPOSAL | FG:economy.md:16-24 | First sell under 90 s; first buy under 4 min; first gate 15 min; later gates 25 to 35 percent longer each; tier 10 gate at 8 to 10 h. (extractor) Nine gates at 25 to 35 percent growth sum to about 6.5 to 9.9 h. |
| P02 | Split price growth by source: entry price growth equals income growth times gear and odds growth. | structure practice | PROPOSAL; the owner accepted the x8 only as a start (O08) | FG:economy.md:29 | x8 per tier = about x2.5 (curve) times about x3 (gear and companions). |
| P03 | Carry capacity is sized as seconds of play at the tier where it is bought. Capacity and price both grow by a roughly constant factor per tier, price faster than capacity. | structure practice | PROPOSAL | FG:economy.md:51-60 | Rule: 60 to 90 s of play. (extractor) 12-tier table: capacity x2.5 to x3.2 per tier; price x5 to x7.1 per tier from tier 3. Capacity must grow with yield (Q-61). |
| P04 | Income formula shape: base times tier factor times (1 plus the sum of additive boosts) times premium multipliers. | structure practice | PROPOSAL | FG:economy.md:14 | stageMult, petBoost, upgradeBoost, weaponBonus, gamepass2x. |
| P05 | Upgrade ladders use base times r^level for long ladders and an explicit list for very short ones, each with a per-level step and a level cap. | structure practice | PROPOSAL | FG:economy.md:64-73 | r between 1.5 and 1.7, e.g. 10 x 1.6^lvl; lists of up to four steps such as 150, 600, 2500. |
| P06 | An odds modifier multiplies the weights of the rarer entries, then renormalises; the commonest entries absorb the loss. The rarest entry uses a steeper exponent so stacking matters. A total cap is set. | structure practice | PROPOSAL | FG:pets.md:6-20 | Weights x (1 + L); rarest x (1 + L)^1.5; cap +500%. |
| P07 | A cross-tier scale for collectible bonuses is chosen so a later-tier common item beats an earlier-tier rare one: scale to the power of the tier gap, times the common bonus, must exceed the rare bonus. | structure practice | PROPOSAL | FG:pets.md:18 | x2.6 per stage. (extractor) 2.6^3 = 17.6, so a 10 percent common becomes 176 percent against a 40 percent rare, three stages apart. |
| P08 | A multiplier ladder uses a near-constant step ratio. The first step is guaranteed by combining duplicates; later steps are chance-based with printed odds. Size and quality modifiers multiply. | structure practice | PROPOSAL, "super down the line" | FG:pets.md:64-78,98-103 | x2.5, x6, x15, x40 (steps x2.4 to x2.7); 5 combine to 1; 20 percent success; huge x3 times shiny x1.5 = x4.5. |
| P09 | Collectibles are saved as instances (id, kind, tier, rarity, size, traits, locked), not counts. One pure function computes the bonus. New modifiers then become data and UI with no save migration. | structure practice | PROPOSAL, applied now | FG:pets.md:106-108 | `base(rarity, stage) x tierMult x sizeMult` plus trait effects. |
| P10 | Keep the conversion rate flat at every conversion point. Stacked conversion multipliers compound into runaway numbers and make older points pointless. | structure practice | PROPOSAL under the O08 delegation | FG:economy.md:47 | One sell pad per zone, all pay the same. |
| P11 | Express a power gap as a player-visible quantity and give a rule for gear tables. Toughness grows slightly faster than pay, so a new tier needs better gear and pays more, and old gear is clearly weak. The first wall is the gentlest because players meet it first. | structure practice | PROPOSAL | FG:brick-strength-stages.md:129-136,157-166 | Own tier 50 percent of reach, one tier later about 19 percent, then one chip. Tier starter power about 100 x S; best about 2.5x. |
| P12 | Retention features proposed: a multi-day reward loop where a missed day pauses and does not reset; a friend bonus with a cap; a code table with reward and expiry, one use per player; timed server events. | structure practice | PROPOSAL; contents open (Q-21, Q-22) | FG:economy.md:98-103 | 7-day loop; friend bonus +5 percent each, cap +20 percent; events every 20 to 30 min. |

## 5. Telemetry practice (what was planned to see the problems)

Status of all rows: PROPOSAL. At read time no analytics call existed in the game's source (FG:telemetry.md:2), and the owner's two open points were unanswered (Q07).

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| T01 | Start from the questions the owner must answer, then map each to the event and the dashboard page that answers it. Include the pacing targets as a question. | telemetry practice | PROPOSAL | FG:telemetry.md:10-18 | Five questions: where first-session players stop, how far by zone, what happened before a quit, is the economy flowing, does the loop match the targets. |
| T02 | The first-session funnel follows the real core loop: join, first action, first reward, first collect, first conversion, third conversion (the loop "clicked"), first purchase, first move to the next tier. Skipped steps count as done. Fields count only on step 1. Inserting a tutorial renumbers the steps. | telemetry practice | PROPOSAL | FG:telemetry.md:20-37 | 8 steps; steps 7 and 8 wait for the shop and gates. |
| T03 | A one-time progression funnel has one step per tier first entered. Field 1 buckets days since first join to line up with the platform's retention windows. | telemetry practice | PROPOSAL | FG:telemetry.md:39-50 | Buckets 0, 1, 2-7, 8-28, 29+. Limit 100 steps per funnel; 14 used. |
| T04 | Log economy events after the write succeeds, with positive amounts. Log the conversion, not each tiny gain, and tag the active multiplier so source size can be read. | telemetry practice | PROPOSAL | FG:telemetry.md:52-67 | Source and sink rows per currency; field "Pass - 2xGold or none". |
| T05 | Measure stalls and waits: time idle, time waiting at a full carry limit, seconds per earn-and-convert trip, and the gap to afford a purchase (throttled to once per minute). A session-end event carries the last action. | telemetry practice | PROPOSAL | FG:telemetry.md:71-82 | `IdleStretch` over 60 s, `FullPackWait`, `TripSeconds`, `CantAfford`, `SessionEnd`. Trip time tests the 60 to 90 s capacity rule (P03). |
| T06 | Say what is not tracked and why: per-action events break the rate limit, and a death loop cannot be measured where nothing deals damage. | telemetry practice | PROPOSAL | FG:telemetry.md:86 | Per-blast and per-pickup events. |
| T07 | Budget the events against the platform limits before shipping: requests per minute, custom fields, field value combinations, funnels, event names. | telemetry practice | PROPOSAL | FG:telemetry.md:88-99 | About 3 to 5 events per player per minute against 120 + 20 x players per server. |
| T08 | Read values you expect to tune through remote config with the content value as default, so A/B tests can change them after launch. Choose the first candidates now. | telemetry practice | PROPOSAL, after launch | FG:telemetry.md:114-116 | Onboarding reward, first gate price, start capacity, debris lifetime. |
| T09 | Plan for blocked data access: an analyst agent reads the platform's analytics API, with a manual export as the fallback when the key type is not offered. | telemetry practice | FOUND: API pull blocked 2026-10-08 | FG:telemetry.md:108-112 | The key page did not list the analytics system. |
| T10 | A telemetry plan written before the features exist leaves many events "pending". Mark each event as can ship, needs a small change or pending its feature. | telemetry practice | PROPOSAL | FG:telemetry.md:24-33,56-65 | Shop, eggs, gates, gems all pending. |

## 6. Open questions (not answered when read)

| ID | Lesson (game-neutral) | Kind | Status and owner's words | Source | Source detail |
| --- | --- | --- | --- | --- | --- |
| Q01 | Gear lineup, feel, progression and prices are left to the owner until the owner has played with a test kit. A designer must not fill them in. | open question | OPEN; owner words: "we're going to need to redesign weapons" | FG:open-questions.md:16 | Q-35, 2026-10-02. |
| Q02 | A premium product that depended on a removed friction needs a replacement decision. | open question | OPEN | FG:open-questions.md:29 | Q-49. |
| Q03 | Should the minimum-hit rule for out-classed gear exist at all, and does a thrown charge count? | open question | OPEN; PROPOSAL default yes | FG:open-questions.md:39,43 | Q-60, Q-64. |
| Q04 | Capacity per tier should grow with yield so trips stay the same length. | open question | OPEN; PROPOSAL | FG:open-questions.md:40 | Q-61. |
| Q05 | Which rare variants per tier, at what chance and multiplier. | open question | OPEN; not built | FG:open-questions.md:41 | Q-62. |
| Q06 | Reward contents and event cadence are undecided. | open question | OPEN | FG:open-questions.md:10-12 | Q-21 daily rewards, Q-22 events, Q-23 modifiers and traits. |
| Q07 | Two telemetry points are unanswered: ship the can-ship steps now, and is the idle threshold right. | open question | OPEN | FG:telemetry.md:118-121 | Section 9 of the plan. |

## 7. End lists

### (a) Taste cases: symptom to the owner's answer

Each case is rewritten without the game's nouns. The verbatim words are in the cited row and contain the game's nouns.

| # | Symptom | Owner's answer | Row |
| --- | --- | --- | --- |
| 1 | Pay is a flat step per zone and feels arbitrary; top gear farms an early zone as well as new gear does. | Make the same content tougher in each zone and let pay follow toughness through a curve picked for fun, with no round numbers. | O01, O03 |
| 2 | A rare variant would inherit the zone curve and double scale. | Give the rare variant its own multiplier, not based on the curve. | O02 |
| 3 | The player must walk to collect each reward after the action. | Remove the step: credit at once with a short animation. Then check the products sold around the old step. | O04, F03 |
| 4 | A result the player set in motion pays nothing because they did not hit it directly. | Give credit to the players involved, shared by contribution (agent set the lower rate). | O05 |
| 5 | A tiny piece and a huge piece pay the same. | Value follows size. | O06 |
| 6 | Tough content pays the same as easy content. | Harder content "should go for more money". | O07 |
| 7 | Conversion points could carry their own multipliers. | Delegated: "whatever is most fun". The agent kept all points flat (P10). | O08, P10 |
| 8 | Uncollected rewards pile up. | "get rid of ones that weren't collected in time"; add a hard ceiling (F04). | O10, F04 |
| 9 | The genre expects a reset or prestige layer. | None for this game (words not recorded). | O11 |
| 10 | The audience is young children. | Keep each reward rule one line long and show odds. | O15 |

### (b) Structure practice: how numbers were kept as data

- Where: one JSON file for economy tuning and two for gear, each with `schema` and `status` keys and a notes string (FG:economy.json:2-4; FG:weapons.json:1-4). A tool compiles them to a server-only module and a replicated subset (S02).
- Units: whole-number amounts with a safe ceiling (S07); a value unit equal to size times material divided by a divisor, calibrated to the old scale (S08); seconds, studs and per-level percentages named in field comments (FG:specs.py:252-261).
- Caps and tiers: schema bounds, cross-field rules, a hard ceiling on stored reward lifetime (S03, F04); tier curve as an array with identity at tier 1 and a guarded id list (S04).
- Revisions: no version field on the numbers. Change history sits in the decision ledger (append only, old rows struck and superseded, FG:decisions.md:5), PROPOSAL labels in file headers and a parity test between the design table and the data (S05). The checks are gate-verified only; none is play-verified.
- Problems it caused: the same number in prose, owner example and data with different values (F06); superseded prose tables left in place with dependents unretuned (F07); prices missing from gear data (S10); the planned simulator never built (F08).

### (c) Do not carry into the kit (game-specific terms found)

Grep the kit for these. Words marked (common) also have ordinary meanings, so check each hit.

- Game name: DestructionSimulator, Destruction Simulator.
- Zone names: Blockcraft, Landmarks USA, Dream House, Classic Blocky Games, North Pole, Titanic Harbor, Toy Bedroom, Dino Park, Pirate Isles, Airport, Bikini Bottom, Animal City, Zootopia, Candy Kingdoms, Nether, Disaster Island.
- Gear names: Brick Blaster, Boom Cube, Pickaxe Boomerang, Lava Bucket Lobber, Fireball Staff, Crystal Sword, Seismic Hammer, Tornado Horn, Monkey Mayhem, Thunder Cloud, Orbital Laser, Black Hole, Lucky Block C4, Minecart Bomb, Crystal Cluster, Pizza Launcher, Meteor Remote, Liberty Bell Bomb.
- Collectible names: Gold Machine, Upgrade Wheel, Trait Reroller, Itempedia, Pet index, Huge, Shiny, Quick-open, Cube Chick, Abyss Wyrm, Liberty Phoenix, Starlight Alicorn, Guest Ghost.
- Currency and loop nouns: brick, bricks, backpack, sell pad, floor pickup, token, gold (common), gems (common), egg (common), pet (common), Secret (common), stage strength, stageMult, value units (common), consequence credit, instant credit, floor rule.
- Game terms in code and data: `pickup_mode`, `stage_strength`, `value_divisor`, `consequence_credit_rate`, `threshold_base`, `PickupService`, `SellService`, `TripSeconds`, `FullPackWait`, `IdleStretch`, `CantAfford`, `PetStats`.
- Ledger ids: D-0xx, D-1xx, D-2xx, Q-xx, F-0xx (allowed only in a source column).
- Physics words from the owner's quotes: blast, collapse, crush, rubble, debris, concrete, steel, obsidian, glass, wood.
