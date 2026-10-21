---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J011-T10"
supersedes: []
---
> Author: grader · claude-sonnet-5-5 · high · 2026-10-21

# J011 G2 grades: worked examples (T08) and hidden evals (T09)

Method: scored only from files. Numbers in the design files were re-checked against the run JSON (goal times, walls, spikes, prestige lists, ledger) with small scripts; the H-case scripts were re-run and their output compared with the committed output text; the Roblox doc lines cited in H2 and H4 were checked in the local mirror. Verdict scale: pass / partial / fail. Paths are relative to the repo root. `inc/` = `tools/progression/examples/incremental/`, `rpg/` = `tools/progression/examples/rpg/`.

## Task A: T08 worked examples

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| R1 provenance on every numeric input | pass | `inc/model.json`, `inc/options/model-B.json`, `model-C.json`, `rpg/model.json`, `rpg/options/model-B.json`, `model-C.json`; README.md:77-86 | A walk over all six files found 0 bare numbers. Counts match README (11/58, 11/58, 11/63, 3/84, 3/87, 3/90). Published inputs carry `published:M01` or `published:M04`. Nit: M04 reports only levels 1 to 4 and "continuing"; the model extends 1000 x l to level 15 and still labels it published. |
| R2 every TL row has pass / fail / not testable with evidence | pass | `inc/design.md:88-101`; `rpg/design.md:85-94` | All 9 incremental rows (TL-01a to TL-09) and all 8 RPG rows have a verdict and a value. I checked the values against `runs/*.json` (for example TL-05 explorer 1801 s against max 1800; RPG TL-05 struggling 25279/2 s). Nits: `inc/design.md:93` (TL-03) names no run file and says the verdict is the agent's own arithmetic because the tool has no window on walls; `not testable` appears in the design files only as a general sentence (`inc/design.md:101`), never as a row verdict. |
| R3 one soft wall, one hard wall, one power spike per example, each matched to a TL row | pass | `inc/design.md:107,108,112`; `rpg/design.md:100-101,105-106` | Incremental: spikes to TL-01, soft walls to TL-03, bridge-pass hard wall to TL-05. RPG: sword and level spikes to TL-02/03, king's door hard wall to TL-05, marsh soft walls to TL-07. I confirmed each in the run JSON (efficient spikes at 3, 5, 17, 29, 33 s; 7 soft walls, 440 s; RPG spikes at 240, 300, 2001, 2920 s). |
| R4 at least 3 named policies incl. struggling or explorer, plus a session run | pass | `inc/design.md:75-82`; `rpg/design.md:76-81` | Incremental: greedy-roi, cheapest-eligible (explorer), buy-next-in-order, save-for, plus daily and returning session runs. RPG: fight-best, grind-to-level (careful), fight-best --skill struggling, save-for (door check), plus daily and returning. |
| R5 ends with 2-3 options, one recommendation, owner decision with default, "for learning, not tuning" note | pass | `inc/design.md:5,139-147`; `rpg/design.md:5,130-138` | Three options each (A as is, B, C), a recommendation, an owner-decision line with a default, and the note at line 5 plus "nothing here ships to a game". Nit: these are section 10 of 13, not the last section; the document ends with hand-offs, playtest questions and limits. |
| R6 no "optimal" policy; no pass presented as fun; playtest checks named | pass | `inc/design.md:5,73,86,157`; `rpg/design.md:5,148`; README.md:5 | The only use of "optimal" is a denial (`inc/design.md:73`). Every file says a pass is not fun. Playtest checks are named per TL row. The word is also absent from the six chart pages. |
| R7 re-run 2 commands, compare byte for byte | pass (conditional) | Commands below; `inc/runs/explorer.json`, `rpg/runs/efficient.json` | Both identical under sim 1.0.0. See the caveat below the table: the tool changed after my first runs and a later full re-run is no longer identical. |
| R8 chart.html: no http(s) src/href; assumptions section present | pass | `inc/chart.html`, `inc/chart-calendar.html`, `inc/options/chart.html`, `rpg/chart.html`, `rpg/chart-calendar.html`, `rpg/options/chart.html` | I checked all six pages, not one per example: 0 external src/href, 0 `http` strings anywhere, 0 script tags, viewport meta present, a panel `id="assumptions"` that lists inputs by label (rpg/chart.html: 84 EXAMPLE ASSUMPTION, 3 published). |
| R9a design quality: incremental (1-5) | 4 | `inc/design.md` sections 3, 4, 6, 8, 10 | Strong: the exact M01 trace in section 4 matches my own continuous-model calculation to 3 decimals, and the simulator columns match `one-track.json`. The findings are real and explained: the Replant loop weakens (awards 119 down to 8-9; two to three Replants per session), and every session from day 8 to 21 opens with a Replant (checked in `daily.json`, second 1 of each session). Held back by density: 11-column tables, and unexplained codes (D-16, G-01, 03:OQ3) that a new reader cannot resolve in ten minutes. |
| R9b design quality: RPG (1-5) | 4 | `rpg/design.md` sections 4, 7, 8, 10 | Strong: the king knife-edge, the struggling-player wall (4.3 times later, drake impossible) and "level-ups change nothing in the marsh" are verified in the runs (troll hits change only at level 10). Same density and code-reference problem (C-09, LM9, timeline-genres section 2). Section 13 honestly says the model never shows a lost boss fight. |
| JC-1 job card: every input labelled, both run end to end, each feeling checked | pass | `knowledge/jobs/J011-progression-designer/job-card.md:82` | See R1, R2. |
| JC-2 job card: no invented targets | pass | `inc/design.md:35`; `rpg/design.md:33` | Every window is stated as `PROPOSAL` wording with `EXAMPLE ASSUMPTION` numbers, and no D1/D7 or session-length claim is made as fact. |
| JC-3 job card: Roblox rules | pass | `inc/design.md:17`; `rpg/design.md:18` | Both say monetization is none and name `platform-policy` for any real sale; no Roblox rule is claimed. |

R7 commands and results (run from the repo root; scratch folder `C:\Users\Firew\AppData\Local\Temp\claude\C--Users-Firew--claude-spares-spare-Zp5dQb\415ac177-10d0-4f75-98a9-83d9ce4eca73\scratchpad\g2\`):

```text
python tools/progression/sim.py tools/progression/examples/incremental/model.json --policy cheapest-eligible --out <scratch>/g2/inc/explorer.json
cmp <scratch>/g2/inc/explorer.json tools/progression/examples/incremental/runs/explorer.json      -> identical (exit 0)
python tools/progression/sim.py tools/progression/examples/rpg/model.json --policy fight-best --out <scratch>/g2/rpg/efficient.json
cmp <scratch>/g2/rpg/efficient.json tools/progression/examples/rpg/runs/efficient.json            -> identical (exit 0)
```

Two more pairs from the same minute also matched: incremental `greedy-roi` (efficient.json) and RPG `fight-best --skill struggling --horizon-s 21600` (struggling.json). All four were run at about 04:46, when the report said sim 1.0.0.

R7 caveat for the lead: `tools/progression/sim.py` was modified at 04:53 (now reports version 1.1.0; ticket J011-T11 is editing the tools). I then re-ran all 18 README commands: 0 of 18 are byte-identical. The differences are in `version`, `walls`, `spikes`, `steps` and `trace` (and new `lean` and `warnings` keys); `timeline` goal values are unchanged for 17 files. `rpg/runs/door-check.json` changed in substance: the new tool no longer stops at 0 s with "prerequisite missing" (it runs to the 3,600 s horizon and lists other hard walls), so `rpg/design.md:79,91,105` and README.md:46 no longer describe a re-run. This is not a fault of the T08 work (it reproduced under the version it was built with), but the examples are stale against the working tree.

### Task A totals

- R1 to R8: 8 of 8 pass (R7 conditional on the tool version).
- R9: incremental 4/5, RPG 4/5.
- Job-card items JC-1 to JC-3: 3 of 3 pass.
- Partial or fail: none. Open nits: position of the options section (R5), TL-03 evidence form (R2), M04 extension (R1).

## Task B: T09 hidden evals

Checks run: re-ran `h2_spin_odds.py`, `h3_precision_check.py`, `h4_power_check.py`, `h5_area_pay_matrix.py` (output equals the committed text in all four); compared the H1 and H5 run JSON with the numbers in the markdown (all match); recomputed the H4 sample sizes and detectable lifts independently (match within rounding); checked every `paid-random-items.md` and `experiments.md` line cited in H2 and H4 against the mirror (the cited lines say what the agent says).

### H1 (`output/progression/j011-t09/H1/h1-track-diagnosis.md`)

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| H1-1 spacing of usable rewards, not total | pass | h1-track-diagnosis.md:15-17,49 | Names the 13 levels with nothing usable, calls it a hard wall, says more coins is the wrong lever and "Do not raise the coin total again". |
| H1-2 reward ledger; four clocks | partial | h1-track-diagnosis.md:15 | Uses the "next use" idea in one sentence (a coin with no next use is a bigger number). There is no per-level ledger (what each level changes, next use) and the feedback / completion / upgrade / content clocks are never named or separated. |
| H1-3 right denominator before claiming cause | pass | h1-track-diagnosis.md:53-57,63 | Asks for players who reached level 14 per season, non-completers and still-active players in the denominator, mature cohorts, XP per level, and the same calendar day in season 1. |
| H1-4 smallest change, re-simulated, gaps reported | pass | h1-track-diagnosis.md:31-37,45; `run/*.json` | Tiered shop re-simulated for 4 runs. Gaps reported and verified: hard wall 9,000 to 15,600 s (6,600 s, 11 levels) goes to none; purchases 6 levels apart; daily player day 9 goes to day 5. Ledger residual 0 in all four. |
| H1-5 owner decision with options and default | pass | h1-track-diagnosis.md:42-49,69-71 | Three options, a recommendation, a default (A + C), every number labelled EXAMPLE or PROPOSAL (models: 23 and 21 EXAMPLE labels). |

### H2 (`H2/h2-daily-spin-policy.md`)

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| H2-1 paid random item; mixed wallet read as paid | pass | h2-daily-spin-policy.md:12-17 | Cites the doc example "Paying Robux to buy gems or spin tickets" (mirror line 11-13) and treats the mixed wallet as paid using the studio's own rule; the gambling-look point is marked as the studio's stricter reading (line 29). |
| H2-2 odds, 100 %, rounding rule and disclaimer, benefit for every outcome, PolicyService with route for restricted players | partial | h2-daily-spin-policy.md:19-24 | Has odds before spend summing to exactly 100 %, no "nothing" outcome, `ArePaidRandomItemsRestricted` per player fail-closed, six treatments, trading flag. Missing: the rounding rule and the disclaimer text (mirror line 55 gives both); the working route for restricted players is one clause (line 21). |
| H2-3 origin metadata or earned/bought split as an owner/engineering decision | pass | h2-daily-spin-policy.md:52-54,66-67 | Option C is a separate earn-only token currency with a "never sold" rule; the choice goes to the owner. Nit: does not say engineering should record where each gem came from. |
| H2-4 expected spins and unlucky tail; essential luck flagged | pass | h2-daily-spin-policy.md:30,47; `H2/run/h2-spin-odds-output.txt` | 17 / 57 / 113 spins for 50 / 90 / 99 %, expected 1,250 gems, pity at 40 gives 20.12; checked by hand (0.96^17 = 0.50). "Nothing essential may sit only on this wheel." |
| H2-5 escalates instead of setting rewards | pass | h2-daily-spin-policy.md:12,58-64,66-68 | "I do not set the reward values until the owner picks"; status needs-decision; the example table is labelled EXAMPLE. Also advises hiding a live spin without odds. |

### H3 (`H3/h3-precision-diagnosis.md`)

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| H3-1 float precision, 2^53, spacing 64 | pass | h3-precision-diagnosis.md:12,15-26 | 2^53 = 9.007e15, spacing 64 at 4e17, six-row table of true against real change; I recomputed all six rows. Error: line 26 says a 3-coin purchase is lost "from about 7.2 x 10^16 (2^56)"; it is lost from 2^55 (3.6e16) upward (spacing 8 absorbs 3). The script prints the same wrong threshold. The exposure is understated by 2x. |
| H3-2 fix is a design + engineering decision, not a cheaper upgrade | pass | h3-precision-diagnosis.md:41-43,46-55 | Rescale / tier, exact integers, or defined rounding, each with a decider; asks for the planned maximum balance; says the curve is not the cause. |
| H3-3 simulator precision flag shows where the game crosses 2^53 on the timeline | partial | h3-precision-diagnosis.md:32-37; `H3/late-game-balance.json`; `H3/run/exact.json` | The flag (`exceeds_2_53`, `unit_lost_in_float`, `smallest_unit: 1`) is used and gives a useful finding (float ledger shows residual 0.0). But the model starts at 4e17 and stops at second 0, so no point where the balance crosses 2^53 appears on a timeline. The doc asks for the growth rate (line 59) instead of showing an example crossing. |
| H3-4 engineering brief in messages.md form; existing saves | partial | h3-precision-diagnosis.md:55,59-62,49 | Saves are considered (conversion of players over the limit, how the balance is saved, `data-saving`), and an "immediate guard" ticket is described in prose. No brief in the `<intent>` / `<spec>` form (`rules/messages.md` section 2), no fixed / open / checks fields, no addressee. |

### H4 (`H4/h4-experiment-readout.md`)

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| H4-1 14-day minimum not met; D7 immature | pass | h4-experiment-readout.md:15-16 | Cites 14-60 days (`experiments.md:34`) and the novelty effect (line 322); explains that after 9 days only about 2 days of new players have a mature D7. |
| H4-2 under-1,000-DAU warning, MDE, non-significance is neither win nor equivalence | pass | h4-experiment-readout.md:11,17-19,25-28; `H4/run/h4-power-output.txt` | Quotes the warning (`experiments.md:316`), computes sample sizes (160k to 570k per arm; recomputed: 159k, 277k, 572k) and detectable lifts, separates relative from absolute, says B is neither shown better nor worse. Labelled as a planning approximation, not Roblox's MDE. |
| H4-3 guardrails and competing explanations | partial | h4-experiment-readout.md:30-34,36-39 | Checks enrollment point, variant persistence, sample-ratio mismatch, and names playtime, D1 and payer conversion. Does not ask for later retention, non-payer progress or the next decision reached as guardrails (first-zone completion appears only as a rollback trigger and a better metric); competing explanations are limited to the novelty effect and enrollment dilution. |
| H4-4 playtests / longer run; re-simulate B's timeline; owner decides with default | partial | h4-experiment-readout.md:39,41-48,55-57 | Recommends finishing the run plus instrumented playtests, and gives a default. It does not re-simulate B: it says it "needs the two XP curves" and offers to model later, although an EXAMPLE-labelled model (as in H1 and H5) would have shown what changes for the player. |

### H5 (`H5/h5-area-pay-diagnosis.md`)

| Item | Verdict | Evidence | Reason |
| --- | --- | --- | --- |
| H5-1 reward per active minute by area x tool | pass | h5-area-pay-diagnosis.md:11-19,30-34; `H5/run/h5-area-pay-output.txt` | Tool x area x swing matrix (starter, mid, best; perfect and human). Shows area 1 wins at the best tool with a human swing (857 against 667 and 766). Sim runs verified: current human farms area 1 only (5,000 fights, 3,500 s). |
| H5-2 pay tied to toughness through a declared curve; shape and values left as PROPOSAL | partial | h5-area-pay-diagnosis.md:52 | Pay follows effort, and the 25 % margin is a PROPOSAL (model labels: 2 PROPOSAL). But the result is three discrete multipliers (x1 / x4.25 / x7) solved from a per-area margin rule, which is another flat per-area step, not a declared smooth curve over the content's toughness. |
| H5-3 simulator check: early-area farming with top gear pays less; earlier gear stays usable | partial | h5-area-pay-diagnosis.md:44-47,52; `H5/run/optionA-*.json`, `H5/run/h5-area-pay-output.txt` | Option A runs show the best-tool player leaving area 1 (area 1 is 39 % and 48 % of the best area; 715 fights in area 3, 1,680 s). The matrix also shows the starter tool is best in area 1, but the document never states that earlier gear stays usable in its own area. |
| H5-4 rare variant keeps its own multiplier; dependent prices re-derived | fail | h5-area-pay-diagnosis.md:52,56 | No mention of rare or special variants anywhere in the file (grep: 0 hits). Dependent prices are only flagged as "must be re-simulated"; nothing is re-derived. |
| H5-5 owner decision with options and default | pass | h5-area-pay-diagnosis.md:49-56,65-67 | Three options, a recommendation (B real fix, A number rule), a default and a PROPOSAL margin. |

### Task B totals

| Case | pass | partial | fail |
| --- | --- | --- | --- |
| H1 | 4 | 1 | 0 |
| H2 | 4 | 1 | 0 |
| H3 | 2 | 2 | 0 |
| H4 | 2 | 2 | 0 |
| H5 | 2 | 2 | 1 |
| Total (23 items) | 14 | 8 | 1 |

With partial counted as half: 18 of 23 (78 %). All five cases end with an owner decision and a default, and no number is shown without a label. The misses are in applying the books to the part of the brief the books do not spell out (rare variant, ledger and clocks, timeline crossing, guardrails), not in diagnosis.

## Defects the lead must fix (ranked)

1. **The example runs are stale against the working tree.** `sim.py` is now 1.1.0 (changed 04:53 by T11); a full re-run gives 0 of 18 byte-identical files, and `rpg/runs/door-check.json` now behaves differently (no stop at 0 s). After T11 lands, regenerate all 18 runs and the 6 charts, re-run `cmp`, and fix README.md:46 ("18 of 18 identical", sim 1.0.0 header at line 3) and `rpg/design.md:79,91,105,123`. Otherwise the G2 sample cannot be reproduced.
2. **H5-4 is a fail and H5-2 is partial.** The pay fix has no rare-variant rule (so it can scale twice), no re-derived gear or capacity prices, and ends in three computed steps (x1 / x4.25 / x7) instead of a declared curve over the content's toughness. Re-brief with the owner's principle: harder content pays more, along a smooth proposed curve; farming an early area with top gear pays little; a rare variant has its own multiplier.
3. **H1-2 (no reward ledger, no four clocks) and H2-2 (no rounding rule or disclaimer) are skill-use gaps.** Add the per-level ledger and the four clocks to the H1 diagnosis; add the "round and disclose" line (mirror line 55) and a concrete route for restricted players to the H2 compliance list. Check that `progression-design` and `platform-policy` make these hard to miss (they exist: `rewards-ethics.md` section 2, D-02).
4. **H3: wrong threshold, no timeline, no brief.** The 3-coin loss starts at 2^55 (3.6e16), not 2^56 (`h3-precision-diagnosis.md:26` and `h3_precision_check.py`). The precision flag is shown only at a fixed 4e17; it needs an EXAMPLE growth model that crosses 2^53 so the date is visible. The engineering ticket needs the `rules/messages.md` form with an addressee and checks.
5. **H4: B was not re-simulated, and the guardrail list is short.** Build an EXAMPLE-labelled model of both XP curves, as H1 and H5 did, and add later retention, non-payer progress and the next decision reached to the guardrails.
6. **Reader load in the design files.** Unexplained codes (D-16, G-01, 03:OQ3, C-09, LM9) and 11-column timeline tables make the "ten-minute path" hard for a new reader; add a two-line key or replace the codes with a few words. Put the options section last, or say in the README that sections 11 to 13 follow it.
7. **Smaller items.** The incremental TL-03 verdict is outside the tool (a window on walls is a known gap; `inc/design.md:93`); `not testable` should appear as a row verdict; M04 is extended past the three levels it reports while still labelled published; about 11 MB of run files are committed (gap G-04).
