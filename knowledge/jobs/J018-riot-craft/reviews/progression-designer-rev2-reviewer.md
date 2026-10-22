---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer progression-designer · claude-opus-5-5 · high · 2026-10-22

# Review: progression-designer books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/progression-designer.md (body) + .agents/skills/progression-design/ (SKILL.md, references/ incl. reward-tiers.md) + .agents/skills/progression-craft/ (SKILL.md, references/), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer progression-designer (opus, high)
looked_at_first: [
  all 12 book files read in full (role body, both SKILL.md, 10 references), then git diff df13ff4 (stat, headings, word-level removals) and the old self-check and hand-off text at df13ff4,
  knowledge/reference/craft/riot/matrix.md (progression column extracted by script: 20 IDs) and the full text of those 20 findings in the topic files; universal-principles.md (UP-01..UP-20: general checks and "applies to" lists),
  platform-policy/references/rules.md §A, game-design/references/systems-economy.md §8-§9, preproduction/references/documents.md §6, the rebuilt sound-design, ui-design and live-ops-design references that name the tier table (V10),
  tools/progression/sim.py (docstring, _event, _step, _finish_activity, trace-out handling), tool-modes.md progression rows, progression-craft/evals/briefs.md E1-E5,
  my own V3 runs (scratch .../scratchpad/pd-rev2/, files pd2_*): the three tools.md §6 python blocks and the §6c one-liner extracted from the file by script and run on fresh full, --lean, --trace-out and 10-run reports of both example models, a randomised RPG copy, an obby model with a lifetime-predicate unlock, and odds tables (exact, zero odds)
  ]   # the coverage and proposals files and the rev1 review were read after this
earlier_findings (rev1): {F1: fixed, F2: fixed, F3: fixed (limit disclosed; see R2), R1: fixed (D-21..D-28 are pointers, §6 ends at 18,380 bytes), R2: fixed, R3: fixed, R4: fixed, R5: fixed, R6: fixed, R7: fixed}
findings:
  - {id: R1, class: recommendation, check: C8 V3 + C3,
     where: ".agents/skills/progression-craft/references/tools.md:63 (step list), :76 (trace events counted), :84 ('Wrong without an error'); .agents/skills/progression-design/references/reward-tiers.md:35 (§4 step 1 event list), :13 (T3 includes 'an unlock that opens a choice, area or verb'), :74 (worked example row 'zone 2 gate opens')",
     expected: "The rates script prints every reward event the tier table tiers, or its trap line names what it cannot see; §4 step 1 lists every kind of reward event the model books",
     observed: "Model `unlocks` (predicate unlocks: zone gates, new areas) are not steps and the script reads only `activity_end` and `fight_end` from the trace, so an unlock gets no line and does not end a 'no step' stretch. The same holds for `offline_reward` events, which reward-tiers §5 says are celebrated. §4 step 1 lists ledger sources, steps, level rewards, drops and activities, not unlocks. The book's own T3 example (zone gate) therefore has no measured row from the named script",
     evidence: "Reviewer obby model pd2_obby.json (run_obby 30 s x60, unlock zone2 when lifetime coins >= 150, speed_coil requires zone2): report `unlocks` = zone2 at 450 s and trace event {'event': 'unlock', 'id': 'zone2', 't_active_s': '450'}; the script prints no unlock line and 'longest stretch with no step 1770 ... of 1800'. sim.py:1371 books the unlock event; sim.py:1026-1034 books steps only for purchase, defeat, drop, complete, level, prestige",
     smallest_fix: "In the §6a script map two more trace events: `unlock` -> 'unlock:<id>' and `offline_reward` -> 'offline:<currency>' (one more conditional on the line that builds `k`), and count them in the second stretch; add 'unlocks (zone gates, areas) and offline grants' to reward-tiers.md §4 step 1 and to tools.md §6a's list of what the trace adds"}
  - {id: R2, class: recommendation, check: C8 V3 + C7,
     where: ".agents/skills/progression-craft/references/tools.md:97-103 (§6b script and 'Reading')",
     expected: "The decision check finds the longest stretch where both policies buy the same things in the same order, which is what C-17 and timeline-genres §3 item 7 define as 'no decision'",
     observed: "The script reports only the identical prefix of each run between resets. The 'Reading' line discloses that a mid-run match is not found and says to read the lists 'by eye', which is not a realistic check on lists of 50-240 purchases. In the book's own example the missed block is longer than the reported one in every run",
     evidence: "Reviewer run on fresh greedy-roi vs cheapest-eligible full incremental reports: the script prints identical first 31 / 0 / 17 / 17 per run (as tools.md:103 quotes); difflib.SequenceMatcher(...).find_longest_match on the same lists gives 53 (run 1, greedy index 180 vs cheapest 116, 31 pot + 22 greenhouse interleaved), 25, 25, 25",
     smallest_fix: "Add three lines per run with the standard library: `m = difflib.SequenceMatcher(None, a, b, autojunk=False).find_longest_match(0, len(a), 0, len(b))`, print 'longest identical block', m.size, 'at', m.a, m.b; replace 'read the purchase lists there by eye' with 'the longest-block line finds it'; update the example numbers in Reading (53 in run 1, 25 in runs 2-4)"}
  - {id: R3, class: recommendation, check: C7,
     where: ".agents/skills/progression-design/references/reward-tiers.md:75 (worked example row 'level-up | capability (a new tool tier) | T2') against :13 (T3 'a planned spike (one hit fewer, a new tier)') and :45 ('Benefit, not amount')",
     expected: "The worked example follows the tier definitions it teaches",
     observed: "A level-up whose benefit is 'a new tool tier' reads as T3 under §2, but the example tiers it T2. The example's tier sums depend on that choice: at T3 the sums would be T2 12 and T3 13.6 per hour, an inversion above the T3 ceiling (12). An agent copying the example cannot tell why a new tool tier is T2",
     evidence: "reward-tiers.md:13, :75, :79 (T2 16 = Fox 12 + level-ups 4; T3 about 10)",
     smallest_fix: "Change the level-up benefit text to 'capability (a small stat step)' or add one sentence why a level-up is T2 here; leave the rates and sums as they are"}
  - {id: R4, class: recommendation, check: C7 + C8 V6,
     where: "reward-tiers.md:9 (§2 header 'efficient policy'), :44 (§5 'above its ceiling for the efficient policy'), :86 (§8 'inside its ceiling ... in every policy'); role :61, progression-design SKILL.md:108 (principle 3 check)",
     expected: "One scope for the rate ceiling check, stated once",
     observed: "§2 and §5 check the ceiling for the efficient policy; §8 (the check the self-review runs) checks it in every policy. A policy that repeats one activity or enemy more than the efficient one can pass under §5 and fail under §8",
     evidence: "the three lines quoted",
     smallest_fix: "Pick one (every named policy is the safer reading, since the struggling or explorer policy can repeat a reward event more often) and make §2's header and §5's line match §8"}
  - {id: R5, class: recommendation, check: C4 (tool schema),
     where: ".agents/skills/progression-craft/references/tools.md:20 ('`{\"id\", \"until\": N}`'; text unchanged since df13ff4:20)",
     expected: "The schema line matches sim.py: every number is a value object",
     observed: "A bare N is refused by sim.py ('policies.order[0].until: number 60 has no provenance label'). The error is loud, so the cost is one failed run",
     evidence: "reviewer run of pd2_obby.json with until: 60",
     smallest_fix: "Write `{\"id\", \"until\": {\"v\": N, \"src\": ...}}`"}
keep: [
  the reward and celebration tier table as an owned sheet: tiers by benefit, rates measured per named policy, tier sums compared across the game, first-time vs repeat, text names, the partner table of who gets what and when; already adopted by the rebuilt sound-design and ui-design books (V10),
  the §6a rates script after repair: steps plus `completions:` and `wins:` from the trace (inline or --trace-out), two stretches, the stop reason; re-run: RPG wins equal fights.per_enemy, obby 60 completions at 120 per h, lean and multi-run refused,
  the §6b decision check split per run between resets, with its guards and honest limits,
  the paid odds check with exact fractions (re-run: sum 1, EV 348 for 250, 230 / 459 rolls at 1 %; zero odds stop with an error, not a wrong number) and the owner-value-label / stake-and-win-back guard, which now matches platform-policy rules §A in every place a paid outcome is valued,
  the number display rule and its fixtures (rechecked 1.04M vs 1.05M, 999 vs 1.00K, 12.4M),
  luck vs skill from runs_summary with its three trap lines (re-run on a randomised RPG copy),
  the tier-table scope clause ('tier table: not in scope' when rewards do not change) in every place that asks for it,
  the role file's 'What you ask partners for, and when' and 'Before you hand back',
  §7 core principles: 17 rows with own examples and checks, 5, 9, 12 excluded with pointers, no contradiction with the master; UP-18 now has the pass budget,
  every old rule (word-level removals walked: each removed phrase is kept, sharpened or replaced by a stronger line)
  ]
verdict: pass
</spec>
```

## Results per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 36 rows checked (20 tagged, all present, matching `matrix.md` by script; 16 untagged used), 0 failed. Every landed-in location opened; each carries the rule and, where the finding has a runnable check, a self-review line. Partial rows (GD-02, SI-20, the art, VFX, sound and UI execution findings) have sound V8 reasons |
| C2 core principles | pass | `progression-design` §7 (the skill loaded first), 17 rows stated for this craft, each with an example and a check naming its input; 5, 9, 12 excluded with pointers; rows 1, 13, 19 cover the three principles the master assigns to this role; row 18 now has the pass budget (rev1 R7); no contradiction. §1 and the role file say to re-read §7 after a compaction |
| C3 self-review | pass | every checkable finding has a line the agent can run with `sim.py`, `curves.py`, the §6 scripts, partner exchange notes or the owner at the gate; rev1 F1 and F3 fixed and re-run. Weak spots: unlocks and offline grants not measured (R1); mid-run identical stretches left to "by eye" (R2) |
| C4 kit rules and engine | pass | no conflict with AGENTS.md, rules/*.md or the J018 decisions; every sim.py, curves.py and chart.py mode named exists in `tool-modes.md`; the paid random lines agree with `platform-policy` rules §A (once-only odds update, long lists behind a worded label, every outcome gives value, stake-and-win-back to the owner). Pre-existing schema slip: R5 |
| C5 nothing valuable lost | pass | every removed word run traced; old self-check lines kept with inputs named ("how the player leaves it" became "its counter"); the old vfx / sound hand-off row replaced by the stronger tier-table row; `cases.md` and `evals/` unchanged |
| C6 fixed rules | pass | outside the books only the coverage, proposals and rev1 review files; role frontmatter identical to df13ff4; SKILL.md 122 / 84 lines; descriptions 388 / 394 characters; headings only appended (§7, tools §6, data-handoff §5, two role sections; review.md title and §3 heading reworded, numbers unchanged); J018 phrase in every changed file and the role comment; no tips section; no library IDs, transcript lines or Riot names in J018-added lines; all files LF; `evals/` unchanged |
| C7 better work | yes | see the judgment below; R1-R4 |
| C8 brief v2 | pass | V1 inputs on every self-check line, the UI ask is two frames; V2 real modes only; V3 every command re-run (rates, decision, luck, odds) and right on the input types the books name, with traps written under each; the two remaining gaps are disclosed or narrow (R1, R2); V4 pass; V6 acceptable (repeats are checks that run one rule, D-21..D-28 are pointers); V7 §6 ends at 18,380 bytes, re-read line present; V8 pass (tier table, track sheet, partner asks, checklist rows 16-20); V10 pass (sound-design and ui-design already read the tier table and the display fixtures); V11 pass (the one game-designer row adopted) |

## Judgment: better work?

Read as the agent at the start of E4 ("a 25-Robux egg with a 2 % legendary needed for zone 3, plus a 2x luck pass"): the new books still make it flag essential luck and load `platform-policy`. They also make it value outcomes by owner labels and stop on any sell-back shape. It tiers the reveal by benefit and rarity, gives below-price results no celebration, gets exact odds sums and the 90 % / 99 % tails from one script, and hands VFX, sound and UI one table with triggers, measured rates and text names. On E1 (an incremental timeline) the agent now restates the problem and the target experience first. It writes each track as a game and runs a decision check. It reads reward rhythm from measured gaps, with repeated completions and wins included, and ships a display rule with fixtures. The old books had none of these. On E2, E3 and E5 the scope clause keeps the tier table out of the way. The weak spots are small and can be fixed: unlock and offline events are not measured (R1); the decision check misses its own longest stretches (R2); one worked-example row disagrees with the tier definitions (R3); the ceiling scope is stated two ways (R4). The design SKILL is still almost twice its old size, but the growth is now real new work, not restated rules.

## For the lead (not for the maker)
- D-11, D-12, `cases.md` rows 9-10 and `timeline-genres.md:70` still name LoL and TFT. These are J011 research citations from df13ff4, not J018 text. This is the same open question as before.
- `python tools/sync_harness.py --check` will show drift for the progression generated copies until the lead's sync.
