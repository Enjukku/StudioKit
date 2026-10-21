# Lantern Woods: worked example of an RPG

> Author: progression-designer · claude-opus-5-5 · high · 2026-10-21 (J011-T08, refreshed in J011-T12 on sim and chart 1.1.0). Model `example-rpg-r2`, SHA-256 `f839924ee5e5b2ad…` (the full hash is in every run file).

**For learning, not tuning.** This is a teaching example. Only the XP table uses a published rule (source M04, a 2010 article that reports 1,000 x level XP per level for its first levels and "continuing"; this model continues it to level 15). Every other number is an `EXAMPLE ASSUMPTION`, and none of it is data from any real game. A "pass" below means that the simulator measured a time inside a window that I chose. It does not show that the game is fun.

**How to read the codes.** `TL-05` is row 5 of the feeling timeline; the same id is the goal id in `model.json` and in every run file. `G-07` is a row in the skill-gap list (`knowledge/jobs/J011-progression-designer/skill-gaps-T08.md`).

## 1. The game in short

- **What the player does.** Fights slimes and wolves in Lantern Woods, beats a crypt guard for a key, beats the Hollow King, and enters the Ember Marsh (trolls). The Ember Drake is the final, optional fight.
- **Power.** Each level adds 10 HP and 1 damage. Gear adds more: iron sword +3 damage, leather armour 40 % less damage taken, sunsteel edge +6 damage (after the king), dragonscale 20 % more protection (after the king). All gear stacks; there are no equipment slots (a model limit).
- **Gates.** The king needs the crypt key. The marsh opens when the king falls. The guard needs level 4; the drake needs level 12.
- **Fights.** Each fight is a duel computed hit by hit. The player hits first. If both sides would die at the same moment, the player wins (the tie rule `player_first`). After each fight the player walks to the next enemy (`overhead_s`).
- **Boss attempts.** The model player tries a boss when the preview says the boss would be left with 25 % HP or less, and walks back 30 s after a loss. It does not retry with the same level and gear. So lost boss fights now appear in the results.
- **Sessions** (`EXAMPLE ASSUMPTION`). One 30-minute session a day. A second player plays days 1 and 2 and returns on day 10.
- **Luck.** None: the key always drops. Essential progress should never wait on luck.
- **Monetization.** None. A real game that sells gear or chests must load the `platform-policy` skill.

## 2. The feeling timeline

All wording is a proposal; all windows are `EXAMPLE ASSUMPTION`s. Appendix A has the full rows.

| Row | When | What the player should feel | Shape | Window |
| --- | --- | --- | --- | --- |
| TL-01 | first minute | "I hit it, it pops, my XP bar moves." | fast start | first kill ≤ 10 s |
| TL-02 | first level-up | "I am stronger now." | power spike | level 2 ≤ 6 min |
| TL-03 | first session | "The sword changes everything." | power spike | first one-hit-fewer spike on wolves ≤ 10 min |
| TL-04 | first session | "There is a key to find." | hard wall (level 4) | guard beaten ≤ 30 min |
| TL-05 | the Hollow King | "The king beat me; now I beat him." | soft wall, then the marsh's hard wall opens | a soft wall before the king in 40-75 min; king beaten in 40-75 min |
| TL-06 | first day | "Coming back gives me a new place." | — | marsh open by day 2 |
| TL-07 | first week | "The marsh is slower, but I prepare for the drake." | soft wall | a soft wall in the marsh in 60-90 min; level 12 by day 7 |
| TL-08 | first month | "I finished it." | — | drake beaten between day 5 and day 21 |

**Thresholds** (in `model.json` → `analysis`). A **soft wall** is 15 min or more of play with no visible step (half a session). A **power spike** is one hit fewer on a reference enemy (wolf for the woods, troll for the marsh), the wolf needing a third more hits to down the player (armour), or the king falling 20 % faster. The troll is measured only after the marsh opens, and the king only while the player holds the key and has not beaten him. A **hard wall** is the simulator's definition: an enemy the player could beat, or an item they could afford, that is still locked.

## 3. The exact trace first

`curves.py` and the simulator's duel give the breakpoints before any run (Appendix B). Three facts drive this example:

1. **The sword is a real spike.** Wolves (36 HP) go from 8 hits to 5 at level 1.
2. **The marsh cancels the level-ups.** With sword and sunsteel, the troll (90 HP) takes 5 hits at levels 6-9 and 4 hits at levels 10-15. Ten level-ups give one breakpoint. At 4 hits, the next breakpoint (3 hits) needs 30 damage, which +1 per level reaches only at level 17.
3. **The king is a knife edge.** At level 6 with sword and armour, the player and the king both die at 16 s, and the tie rule gives the win to the player. At level 5 the player loses. The struggling player can never beat the drake: at level 15 with all gear they need 57 s and die at 37.5 s.

## 4. The model players

Each run is one named strategy, not the player population. All runs are exact mode and `--lean`.

| Run file | Who | Play time simulated |
| --- | --- | --- |
| `runs/efficient.json` | Efficient: buys what it can, fights a beatable boss first, else the enemy with the most XP per second | 5 h; done at 3.1 h |
| `runs/careful.json` | Careful: skips every boss (also the crypt guard) until level 9 | 5 h; done at 3.6 h |
| `runs/struggling.json` | Struggling: 0.5 s slower per swing, 75 % damage | 6 h |
| `runs/daily.json` | Efficient, 30 min a day | up to 30 sessions; done on day 6 |
| `runs/returning.json` | Efficient, away from day 3 to day 9 | up to 30 sessions; done on day 13 |

The T08 "door-check" run is gone: the new simulator finds the hard walls in the normal runs.

## 5. Results

Each verdict comes from the simulator's goal with the same id.

| Row | Verdict | Evidence |
| --- | --- | --- |
| TL-01 | pass; **fail** for struggling | efficient 8 s (2 s fight + 6 s walk); struggling 10.5 s |
| TL-02 | pass; **fail** for struggling | efficient 300 s; struggling 390 s |
| TL-03 | pass | efficient 240 s: the sword takes wolves from 8 hits to 5 (`spikes`, `wolf_hits`) |
| TL-04 | pass; **fail** for careful and struggling | efficient 1317 s. Hard wall: the guard is beatable from 588 s but locked until level 4 (711 s, `walls.hard`). Careful 6739 s; struggling 1823 s. |
| TL-05 | pass; **fail** for careful and struggling | efficient: soft wall before the king at 2948 s (level 6 after a 947 s wait, TL-05b); king beaten at 2979 s on the 2nd attempt (lost at level 5). Struggling: 3rd attempt, 3.55 h, level 11. Careful: 112.8 min. |
| TL-06 | pass | `daily.json` 87,579 s (day 2). Hard wall: trolls are beatable from 588 s (9.8 min) but the marsh stays locked for 2391 s (40 min) until the king falls. |
| TL-07 | pass; **fail** for returning | soft wall in the marsh at 4361 s (level 8, TL-07a); level 12 on day 5.00 (daily); returning day 12.00 (away in week 1) |
| TL-08 | pass, with a finding | daily day 6.00 (518,813 s); returning day 13.00 |

The careful run also shows the king's own gate: the king is beatable from 2988 s but locked for 3751 s, because this player skipped the guard that drops the key. Ledgers close with residual 0 in every run; no precision flag.

## 6. Walls and spikes: planned or found

| What the simulator found | Where | Planned? |
| --- | --- | --- |
| Spikes on wolves: sword 8 → 5 hits (240 s), level 2 → 4 hits, level 5 → 3 hits | all runs | yes (TL-02, TL-03) |
| Armour spike: wolves need 7 hits to down the player instead of 5 (588 s) | all runs | yes: the armour makes the king beatable |
| Hard walls: guard locked by level (588-1299 s); marsh locked behind the king (588-2979 s) | efficient, daily | yes (TL-04, TL-05/06) |
| Lost king fight at level 5, then a soft wall to level 6 | efficient | yes: "the king beat me; now I beat him" |
| Soft walls at levels 8-13 (16-25 min each) | efficient, daily | yes (TL-07): the marsh slowdown |
| Only one troll spike in the whole marsh (level 10, 5 → 4 hits) | all runs that reach the marsh | **found**: see finding 2 |
| Soft walls from level 5 onwards and 3 king attempts | struggling | **found**: see finding 1 |

## 7. Findings I did not plan

1. **The king is a much bigger wall for the struggling player.** Efficient: 2 attempts, king at 49.7 min, level 6. Struggling: 3 attempts, king at 3.55 h, level 11 (4.3 times later), and the drake is impossible even at level 15 with all gear. A stat wall for one player is a skill wall for another: the fix is an assist or another route, not a lower price.
2. **The marsh cancels the level-ups.** The troll has 2.5 times the wolf's HP. During the slowest part of the game (16-25 min per level), nine of ten level-ups change nothing the player can feel on the enemy they fight. This is breakpoint math, not a bug.
3. **The tie rule decides the king.** At level 6 the player wins only because simultaneous hits go to the player. With the opposite rule the king needs level 7 (about 7 min more). Engineering must copy the tie rule exactly.
4. **The content ends on day 6.** The daily player beats the drake on day 6 (3.1 h of play). TL-08 passes as "completion", but weeks 2-4 have no goals.

## 8. Options for the owner

| Option | What changes | What the player feels, and when | Evidence | Trade-off |
| --- | --- | --- | --- | --- |
| A. As is | — | Efficient: king at 50 min, drake on day 6. Struggling: stuck at the king for 3.5 h, never finishes. | `runs/efficient.json`, `runs/struggling.json` | The struggling player has no way through. |
| B. Late assist | Lantern Ward: +15 % protection, 300 gold, in the shop after 50 min of play (`options/model-B.json`) | Struggling: king at 2.49 h, level 9 (one hour sooner); drake at 5.64 h on the 3rd attempt. Efficient: king unchanged; drake at 3.04 h on the 2nd attempt. | `options/runs/B-struggling.json`, `B-efficient.json` | One more shop item. The struggling path is still long. |
| C. Assist + marsh weapon | B, plus Ember Edge (+6 damage, 4,000 gold, level 11) and drake HP 800 → 900 (`options/model-C.json`) | Efficient: at 2.2 h trolls fall in 3 hits, not 4 (a spike in the slow marsh). But the drake falls at level 12 at 2.57 h without the dragonscale, so the last savings goal disappears. Struggling: drake at 5.99 h. | `options/runs/C-efficient.json`, `C-struggling.json` | Fixes finding 2 but makes the dragonscale useless and the game shorter. |

Uncertainty: how many real players fight like the struggling profile is unknown; the 50-min timer is a guess at "has tried and failed".

**Recommendation: B now.** It gives the struggling player a way through and barely changes the efficient path. Do C after one more re-tune (for example a stronger drake hit), so the marsh gets its spike and the dragonscale keeps its job. (Same as T08. The new boss attempts add the lost fights but do not change the order of the options.)

**Owner decision needed:** which option this example presents as its fix. **Default if no answer: B**, with the note that nothing here ships to a game.

## 9. What the charts show

- `chart.html`, **Timeline**: one row per player. Purple triangles near 4-10 min: the sword, the first level-up and the armour. Hatched red blocks from 9.8 min: the locked guard and the locked marsh. Orange blocks after 49 min: the king's level check and the marsh slowdown. The struggling row has orange blocks from 45 min and the king only at 3.5 h.
- `chart.html`, **Reference metrics over time**: the troll line starts when the marsh opens (5 hits) and steps down only once. The wolf line steps down four times.
- `chart.html`, **Curves**, "Hits to kill per level": flat stretches are level-ups that change nothing on that enemy.
- `options/chart.html`: rows A, B, C for the efficient and the struggling player (each row title names its model).

## 10. Hand-off, playtest, limits

- **UI**: show damage numbers so the sword spike is visible; show "needs the crypt key" on the king's door; show what the next level changes.
- **Analyst**: one event per fight (enemy, win or loss, time), per level-up and per purchase; for the king, attempts per player. Keep players who never finish in the denominator.
- **A playtest must check**: does the player feel the sword (TL-03)? How many attempts do real players need for the king (TL-05)? Does the marsh feel like preparation or like grind (TL-07)? Do players want more after the drake?
- **Limits**: one strategy per run; the model player attempts a boss only by its preview rule; every attack lands; no measured player data. Every result depends on all 94 `EXAMPLE ASSUMPTION` inputs (listed in each chart's assumptions panel).

Files: `model.json`, `runs/*.json`, `chart.html`, `options/model-B.json`, `options/model-C.json`, `options/runs/*.json`, `options/chart.html`. Re-run commands: `../README.md`.

## Appendix A: full timeline rows

| Row | Sign to watch | Intended state | Purpose | Model check | Playtest question |
| --- | --- | --- | --- | --- | --- |
| TL-01 | first kill in 10 s | 1 slime down | show cause and effect | goal TL-01 | Does the player see the XP bar move and attack again? |
| TL-02 | level 2 before 6 min | level 2 | first proof that XP means power | goal TL-02 | Does the player notice the level-up? |
| TL-03 | wolves fall in 5 hits, not 8 | iron sword | a gear spike on an unchanged enemy | goal TL-03 (`spikes` wolf_hits ≥ 1) | Does the player feel the sword without a tooltip? |
| TL-04 | guard beaten in 30 min | crypt key | give the boss door a clear prerequisite | goal TL-04; `walls.hard` | Does the player know where the key comes from? |
| TL-05 | loses once, levels up, wins | level 6, sword, armour | a fair boss test with a visible reason to grow | goals TL-05b (`soft_walls` ≥ 1 before the king), TL-05; `fights.per_enemy.hollow_king` | Is the king a fair test or a wall of numbers? |
| TL-06 | the marsh opens in the day-2 session | marsh open | reward the first return | goal TL-06; `walls.hard` (bog_troll) | Does the player go to the marsh on their own? |
| TL-07 | level-ups slow to one per 15-25 min | level 12, sunsteel | make the final fight a goal to prepare for | goals TL-07a (`soft_walls` ≥ 2 after the marsh opens), TL-07 | Preparation or grind? |
| TL-08 | drake beaten between day 5 and 21 | drake down | a satisfying end | goal TL-08 | Did the ending feel earned? |

## Appendix B: breakpoints (exact)

Hits to kill = HP / damage, rounded up.

| Player | Wolf (36 HP) | Troll (90 HP) |
| --- | --- | --- |
| Level 1, no gear (5 damage) | 8 | 18 |
| Level 1 + sword (8) | 5 | 12 |
| Levels 2-4 + sword (9-11) | 4 | 10, 9, 9 |
| Levels 5-7 + sword (12-14) | 3 | 8, 7, 7 |
| Levels 6-9 + sword + sunsteel (19-22) | 2 | 5 |
| Levels 10-15 + sword + sunsteel (23-28) | 2 | 4 |
| Levels 11-15 + option C's ember edge (30-34) | 2 | 3 |

Duels (commands in `../README.md`): level 6 with sword and armour against the king: win at 16 s (17 hits; the king needs 8). Level 5: loss at 14 s. Struggling player at level 15 with all gear against the drake: loss at 37.5 s (would need 39 hits, 57 s).
