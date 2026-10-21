> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-craft`. Sources: 03:HO1-HO5, HT1-HT3, PS9, TL3, TL9 (paper, O contract; W01 GDC 2025 spreadsheet-to-game practice, E); `architecture` R-07 (definitions vs runtime vs saved); `rules/messages.md` (brief format).

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
| 9 | Prerequisites | unlock predicates |
| 10 | Costs and rewards | per row, with currency |
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
| game-designer (goals in, curves out) | the feeling timeline draft, options with trade-offs, the simulator charts | loop and content changes; with the owner, which experience | owner decision ids, timeline rows | each option shows what the player feels differently and when |
| engineering (architect, feature-builder, quick-builder) | the model revision, the exported definition tables, the data contract, fixtures, the change report | file layout, runtime format, code structure, save migration with the owner | ids, values, units, rounding order, caps, fixtures (source: model revision + owner decision) | engineering's tests reproduce every fixture exactly; server is the authority for currency (`networking-security`) |
| ui-ux-designer (how progress is shown) | what the player must see at each timeline point: current value, next goal and its cost/requirement, time or attempts to it, what a milestone unlocks, odds for any random reward, what a reset keeps | layout, style, motion | numbers shown, rounding for display (display only), odds tables from the same data (`platform-policy` P-01) | the next goal and its benefit are readable on a phone in the first minute |
| analyst (`analysis-design`) | the events each timeline target needs (milestone reached, attempt/fail, economy source/sink with balance), the denominators and cohorts, the predicted values per policy | event code and dashboards | event names, fields, revision tags (`analytics`) | each target can be measured with its denominator; non-completers kept |
| live-ops designer | sinks and sources an event may add, caps, what must never be bought, the model to re-simulate event changes | event content and calendar | economy limits from the model, owner decisions | event changes re-simulated; normal route never balanced around events (01:K7.O) |
| vfx / sound designer (when a milestone needs celebration) | which milestones are spikes the player must feel, and their importance rank | the effect and the sound | milestone ids, rank | — |

Live-ops side of this hand-off: `live-ops-craft/references/handoffs.md` §3.
