> Author: J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22. Part of `progression-design`; built also from the owner's Riot transcripts (J018). Rates come from `progression-craft/references/tools.md` §6; paid random rules from `platform-policy` (it wins); how a paid result is revealed from `game-design/references/systems-economy.md` §9. Every number below is a PROPOSAL starting value or an EXAMPLE ASSUMPTION. Repaired in review round 1 (rates compared per tier as a whole, capstones on finite tracks, value labels never sell-back prices).

# The reward and celebration tier table

## 1. What it is
I decide which rewards the player should feel, how big each feels next to the others, and how often each really happens. The crafts decide how it looks and sounds. One table per game (or per feature that adds rewards), in my working folder as `reward-tiers.md`, tagged with the model revision it was measured on. It feeds the game designer's feedback stack (the Celebration and Frequency fields of `preproduction/references/documents.md` §6) and the briefs to VFX, sound, UI and art. If every reward celebrates, none does: the table keeps the rare ones big by keeping the frequent ones small.

## 2. Tiers (starting definitions; the owner may rename, add or merge)
| Tier | Earned by (the benefit, `SKILL` D-02) | Rate ceiling (PROPOSAL, efficient policy, all the tier's events together) | What it may get (the crafts choose how) |
| --- | --- | --- | --- |
| T1 routine | a pickup, a kill reward, a currency tick, a repeat purchase that only raises a number | none: any rate | feedback only: small, short, merged when frequent; no celebration |
| T2 small goal | a subgoal, a quest or chain step, a cheap upgrade that moves a reference metric a little, an uncommon find | about 1 per active minute | a short confirmation that ends before the next decision |
| T3 milestone | a feeling-timeline row, a planned spike (one hit fewer, a new tier), an unlock that opens a choice, area or verb, a rare find | about 1 per 5 active minutes | a celebration in play; the reward shown at its destination |
| T4 peak | a track's capstone: first rebirth, first boss win, final season reward, the top rarity | about 1 per session (the session model's length) | the biggest moment; may break the house style only by owner decision |

A repeated event's first time may sit one tier above its repeats (first rebirth T4, later rebirths T3).
The ceilings are not pacing targets (no universal rewards-per-session number exists, `SKILL` D-14): they only stop a tier from firing so often that it no longer feels rare. Each game sets its own with the owner; a playtest may move them.

## 3. Columns (one row per reward event)
| Column | Holds |
| --- | --- |
| id, event | stable id; the event name from the feature contract and `knowledge/design/vocabulary.md` (the name VFX, sound and UI key to) |
| timeline row | `TL-nn` it serves, or "routine" |
| benefit | what the player can now do (capability, choice, understanding, expression, access, accomplishment) or "number only" |
| tier | first time / repeat |
| trigger | the confirmed source: the model's ledger source, goal or step that the server grants (never a client estimate or a timer) |
| rate | per active hour and per session, for each named policy, with the report path and model revision |
| paid path | none · bought directly · random bought with Robux or Robux-bought currency (then the paid columns are filled) |
| value vs price | paid random rows: the outcome's value on the price's scale (the owner's value label; if an outcome can be sold or converted back into the price currency, the roll is the stake-and-win-back shape in `platform-policy` rules §A: stop and raise it to the owner) against the price; below price → reveal only, no celebration tier |
| family, rank | for items: theme family and rank inside it (1 = lowest); the look must show the rank |
| text name | the tier or rarity name shown in words with the result (never colour alone) |
| counter | the counter the reward increases (UI shows the true value at once) |

## 4. How I fill it
1. List every reward event: the model's ledger sources, steps, level rewards, drops and activities, plus the feature contract's events.
2. Propose a tier from the benefit, never from the amount: a bigger number alone stays T1.
3. Measure each event's rate per named policy (efficient, explorer or struggling, returning) from full single-run reports (`progression-craft/references/tools.md` §6a), for the brief's session pattern.
4. Apply the rules in §5; each fix is a tier move or a rate change, and the owner chooses between them.
5. Rank items inside each family (power or rarity) and mark the rows allowed a style break (top tier only).
6. Show the table with the options; tiers are PROPOSAL until the owner decides. Then send it (§6).

## 5. Rules
- **Rarer is bigger.** Compared across the whole game, per named policy, each tier as a whole: the player feels every track together, so a tier's rate is the sum of its events' rates (`tools.md` §6a lines, every track). Each tier's sum is below the sum of the tier under it (T2 and up); an inversion is a finding. Two single events of different tiers are not compared: a frequent T3 event next to a rarer T2 event is fine while the sums keep their order.
- **Frequent never holds a high tier.** A tier's sum above its ceiling for the efficient policy is a finding: its most frequent event moves down a tier, or a rate changes.
- **Benefit, not amount.** Tier follows what changed for the player; the amount scales inside a tier.
- **Confirmed only.** The trigger is the server's grant; offline earnings celebrate the granted amount after the grant; the attempt cue on input belongs to the game designer's feedback stack, not to this table.
- **A learnable cause sizes it.** Rarity, difficulty, chain length; a random amount never picks the tier; escalation (streak, combo, chain) steps at thresholds the model defines and resets visibly.
- **Paid random rows are honest.** Tier by real rarity and value; below-price results get no celebration tier; odds as numbers summing to exactly 1 from the same data the server rolls; reveal rules in `game-design/references/systems-economy.md` §9; `platform-policy` wins.
- **Top tier only breaks the style,** and only by a documented owner decision (the art director proposes the break).
- **Words carry the tier.** Every tier and rarity has a text name shown with the result.
- **Each finite track ends on its capstone** (and each run of a repeating track, such as one rebirth cycle): the step at its planned finish holds its highest tier; no track ends on a routine gain. An infinite voluntary sink has no capstone; its steps keep the tier their benefit earns.

## 6. What each partner gets, and when
| Partner | Gets from the table | Their call | When |
| --- | --- | --- | --- |
| game-designer | tier, trigger and rate per event | the feedback stack (attempt cue, outcome response, celebration length, merge window) | before the feature spec's feedback stack is frozen |
| vfx-designer, sound-designer | tier (first / repeat), rate, trigger, text name | shape, length, loudness and caps per tier, merge windows | before any reward effect or cue is built |
| ui-ux-designer | tier, counter, text name, odds rows; the number display rule (`progression-craft/references/data-handoff.md` §5) | layout, motion, where the reward flies | before reward and shop screens are styled |
| art-director | family and rank ladders, style-break rows, premium rows | how rank shows (size, complexity, finish, secondary motion) | before item families are drawn |
| live-ops-designer | the tiers and their ceilings | event rewards placed in the same tiers; a new top-tier reward needs the same rarity proof | event planning |

Each partner restates the tiers and rates it uses in its exchange note; an open question there means the table is not done.

## 7. Worked example (illustrative; every value EXAMPLE ASSUMPTION)
A pet simulator: players smash breakables for coins, hatch eggs with coins (coins are also sold for Robux, so eggs are paid random), unlock zones and rebirth. Session model: 20 active minutes. Rates from full single-run reports of the efficient policy, which hatches about 40 eggs per hour at 250 coins each (odds 60 / 30 / 9 / 1 %). Pet values are the owner's value labels on the coin scale; pets never sell for coins (a sell-back would make the egg a stake-and-win-back roll).

| Event | Benefit | Tier | Rate | Note |
| --- | --- | --- | --- | --- |
| coin pickup | number only | T1 | about 900 per hour | merged by the crafts |
| egg: Common Cat (value 100, price 250) | expression | reveal only | 24 per hour | below price: no celebration |
| egg: Uncommon Fox (value 300) | expression | T2 | 12 per hour | |
| egg: Rare Owl (value 1,200) | power + expression | T3 | 3.6 per hour | |
| egg: Secret Drake (value 9,000) | power + status | T4, style break by owner decision | 0.4 per hour | odds 1 %: 230 hatches for a 90 % chance |
| zone 2 gate opens | access | T3 | first at 9 minutes | the capstone of zone 1 |
| level-up | capability (a new tool tier) | T2 | 4 per hour | |
| first rebirth / later rebirths | reset with a multiplier | T4 / T3 | 6 per hour = 2 per session | the first-time rule keeps T4 rare; later rebirths fire more often than level-ups, which is fine: T3's sum stays below T2's |
| "Lucky Find" bonus | number only | was T3 | 20 per hour | finding: its benefit is number only (T1), and at T3 it lifts T3's sum to about 30 per hour, above the T3 ceiling (12) and above T2's sum (16): moved to T1, or made rarer if the owner wants it felt |

Tier sums after the fix (efficient policy): T2 16 per hour (Fox 12 + level-ups 4; ceiling 60); T3 about 10 per hour (Owl 3.6 + later rebirths 6, plus the once-only gate; ceiling 12); T4 0.4 per hour plus the first rebirth (ceiling 3 at 20-minute sessions). Each sum is below the one under it.

What the crafts receive: a short table of event names with tier, rate and text name; the art director gets the families (Ocean, Lava) ranked 1-5 with the Secret row marked for a documented break.

## 8. Checks (the self-review lines in `SKILL` §6 run these)
| Check | Input | Pass when |
| --- | --- | --- |
| Rate ceilings and order | full single-run report per named policy (`tools.md` §6a); the rows' rates summed per tier | each tier's sum inside its ceiling and below the sum of the tier under it, in every policy |
| Confirmed triggers | the model file | every celebrated row names a ledger source, goal or step |
| Paid rows | the odds table (`tools.md` §6d) + `platform-policy` rules §A | odds sum to exactly 1; below-price rows uncelebrated; values are owner labels, no outcome sells back into the price currency; text names present |
| Capstones | the timeline's planned finish row per finite track (and per run of a repeating track) and that row's goal time in the report; never the report's last step, which is wherever the horizon or "all goals reached" stopped the run | the event at that time holds the track's highest tier; infinite voluntary sinks are exempt |
| Partners | exchange notes | each partner restated tier, rate and name with no open question |
| Feel | the owner on a playable preview at the gate | owner-confirmed, or listed as not verified |
