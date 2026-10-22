> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-craft`. Sources: 03:HO1-HO5, HT1-HT3, PS9, TL3, TL9 (paper, O contract; W01 GDC 2025 spreadsheet-to-game practice, E); `architecture` R-07 (definitions vs runtime vs saved); `rules/messages.md` (brief format). Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (readable requirements, tier ids on rewards, the tier table in the briefs, new §5 number display).

# Data tables, the engineering contract, and the hand-offs

## 1. One authority, generated views (03:HO3, TL3)
- The **reviewed progression model** (the JSON the simulator reads, `tools/progression/sim.py`) is the one editable authority for every progression number. Charts, timeline reports and the game's definition tables are generated from the same revision. Never edit a generated copy; never repair a stale copy by changing another (03:HO3, DN9).
- Every export carries the model revision (and content hash). An export fails when: an id is missing or duplicated; a reference does not resolve; a formula gives a non-finite value; a generated value differs from an approved fixture.
- Where the definition tables live in the game and how code reads them is engineering's call (architect / feature-builder; `architecture` R-07: definitions are read-only data that pick among supported behaviours, never a second programming language). You deliver the values, the contract and the fixtures.

## 2. The data contract (03:HO2, HO4, O; 13 fields)
| # | Field | Holds |
| --- | --- | --- |
| 1 | Stable ids | item, upgrade, level, enemy, milestone ids that never change meaning (saves refer to them) |
| 2 | Schema version | which table shape this is |
| 3 | Balance revision | the model revision the values came from |
| 4 | Units | currency ids, time unit (active s / calendar day), per-second vs per-action |
| 5 | Formula id + parameters | e.g. `exponential(b, r)`, with index origin; or an explicit value list |
| 6 | Domain | valid index range (levels 1-60, owned 0-500) |
| 7 | Caps | balance caps, owned caps, level caps |
| 8 | Rounding + modifier order | where rounding happens, additive vs multiplicative groups, bulk = sum of rounded units or rounded closed form |
| 9 | Prerequisites | unlock predicates, each with a player-readable requirement ("need level 12", "beat the Crypt Guard") the UI shows on the locked thing |
| 10 | Costs and rewards | per row, with currency; each reward with its tier id from the reward tier table |
| 11 | Reset behaviour | what a prestige/rebirth removes, keeps, merges, grants |
| 12 | Expected fixture outputs | rows engineering's tests must reproduce exactly (cost at n, cumulative XP at l, hits-to-kill per build × enemy, prestige award at L) |
| 13 | Rationale for exceptions | per deliberate spike or irregular value: why, and its source label, so nobody smooths it away |

Example row shape (03:HO4, illustrative; an RPG table has other fields): `upgradeId, tier, costCurrencyId, baseCost, growthFactor, costRounding, productionPerActiveSecond, requiredUpgradeId, maxOwned, balanceRevision`.

## 3. Changing live numbers (03:HO5, HT3)
- Diff **outcomes**, not only parameters: the change report lists old/new values AND old/new milestone times under the same named policies, plus changed reset or rounding rules.
- Existing players: give representative saved states and how each must read after the change (spent currency, unlock eligibility, equipped items, prestige awards, lifetime counters). Recomputing today's curve does not preserve yesterday's earned state. Migration or compensation is an owner + engineering decision (`data-saving`); flag it, never decide it.

## 4. Hand-off briefs (`rules/messages.md` §2: `<intent>` prose + `<spec>`; every rule restated; skills named)
| To | You send | They decide | `fixed` usually holds | Typical checks |
| --- | --- | --- | --- | --- |
| game-designer (goals in, curves out) | the feeling timeline draft, options with trade-offs, the simulator charts, the reward tier table (tier, trigger, rate per event) for the feedback stack's Celebration and Frequency fields; luck vs skill runs when asked | loop and content changes; the feedback stack; with the owner, which experience | owner decision ids, timeline rows, tier ids | each option shows what the player feels differently and when; the feedback stack quotes the table's tiers |
| engineering (architect, feature-builder, quick-builder) | the model revision, the exported definition tables, the data contract, fixtures, the change report | file layout, runtime format, code structure, save migration with the owner | ids, values, units, rounding order, caps, fixtures (source: model revision + owner decision) | engineering's tests reproduce every fixture exactly; server is the authority for currency (`networking-security`) |
| ui-ux-designer (how progress is shown) | what the player must see at each timeline point: current value, next goal and its cost/requirement, time or attempts to it, what a milestone unlocks, odds for any random reward, what a reset keeps; the readable requirement of every locked thing; the tier, text name and counter of each reward; the number display rule and its fixtures (§5) | layout, style, motion | numbers shown, rounding for display (display only, §5), odds tables from the same data (`platform-policy` P-01); logic and affordability use the true value at once, count-ups are decoration ending on the exact number | the next goal and its benefit are readable on a phone in the first minute; I ask for a phone-size frame of the shop or progress screen at two timeline points and compare every shown number with the fixtures |
| analyst (`analysis-design`) | the events each timeline target needs (milestone reached, attempt/fail, economy source/sink with balance), the denominators and cohorts, the predicted values per policy | event code and dashboards | event names, fields, revision tags (`analytics`) | each target can be measured with its denominator; non-completers kept |
| live-ops designer | sinks and sources an event may add, caps, what must never be bought, the model to re-simulate event changes | event content and calendar | economy limits from the model, owner decisions | event changes re-simulated; normal route never balanced around events (01:K7.O) |
| vfx-designer, sound-designer (every reward moment) | the reward tier table: event name, tier (first / repeat), measured rate, confirmed trigger, text name | the effect and the sound, caps per tier, merge windows | event names, tiers, triggers | each restates the tiers and rates it built to in its exchange note; no reward moment plays before its trigger |
| art-director (item families and rarity ladders) | families with rank 1-N per item, the rows allowed a style break (top tier, by owner decision), premium rows | how rank shows (size, complexity, finish, secondary motion) | family and rank ids | the art director restates the rank order it drew to; a stronger or rarer item never looks lower |

Live-ops side of this hand-off: `live-ops-craft/references/handoffs.md` §3.

## 5. Number display (what the UI shows; the true value never changes)
- Logic, affordability and saves use the exact value. A displayed number is rounded for reading only.
- **Balances round down, prices and requirements round up,** at the shown digits, so a shown balance never looks affordable when it is not. Same suffix table everywhere (K, M, B, T; one place in the data), the same significant digits for a balance and the price next to it.
- Count-ups and flying coins are decoration over the true value: they end on the exact number; the buy button checks the true balance at once.
- Gains read as gains; spending is neutral (danger colours stay for danger).
- The fixtures come from the tool, never by hand: `curves.display_round(x, sig, "floor" | "ceil")` in `tools/progression/curves.py` (the suffix table is `DISPLAY_SUFFIXES`, one place).
- Fixtures I send with the rule (3 significant digits): balance 1,049,999 shows 1.04M next to a price of 1,050,000 shown as 1.05M (half-up would show both as 1.05M); balance 999.5 shows 999 next to a price of 1,000 shown as 1.00K (half-up would show 1000); price 12,350,000 shows 12.4M.
- Odds have their own display rule (rounding digits and disclaimer): `platform-policy`.
