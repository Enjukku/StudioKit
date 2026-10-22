---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer progression-designer · claude-opus-5-5 · high · 2026-10-22

# Review: progression-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/progression-designer.md (body) + .agents/skills/progression-design/ (SKILL.md, references/ incl. new reward-tiers.md) + .agents/skills/progression-craft/ (SKILL.md, references/), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer progression-designer (opus, high)
looked_at_first: [
  all 12 book files read in full (role body, both SKILL.md, 9 references), then git diff df13ff4 and a word-level diff of every removed word,
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20, incl. each "applies to" list),
  knowledge/reference/craft/riot/matrix.md (progression column: 20 findings, script-extracted) and the full text of those 20 findings in the topic files,
  platform-policy/references/rules.md §A-§D, game-design/references/systems-economy.md §8-§9, game-design/references/principles.md §5 §7, preproduction/references/documents.md §6,
  tools/progression/sim.py (--help, schema docstring, _finish_activity, _summary_runs), curves.py (expected_spend, attempts_for_quantile), chart.py --help,
  progression-craft/evals/briefs.md (E1-E5),
  my own V3 runs (scratch folder .../scratchpad/pd-reviewer/): the four tools.md §6 snippets extracted from the file by script and run on fresh sim.py reports of both example models, a lean report, a 40-run randomised RPG copy, an odds table with exact, float and zero odds, and a new obby model with a repeated paid activity
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C8 V3 + C3,
     where: ".agents/skills/progression-craft/references/tools.md:63 (§6a: 'Steps are ... first completions') and :64-80 (rates script and its 'Wrong without an error' line)",
     expected: "V3: the command gives the right answer on every input type the agent will really give it, and the book names what makes it give a wrong number with no error. The books support obbies and tycoon tasks through `activities` (tools.md:13 'this is how obbies and tycoon tasks fit'); for those games the reward event players repeat is the activity completion, and its rate is what the tier table needs",
     observed: "The script counts only steps. sim.py books a step only for the first completion of an activity (sim.py:1185-1188); repeated completions pay their rewards but are not steps and are not in `fights.per_enemy`. The trap line warns only about repeated kills. An obby or tycoon model therefore gets a rate of one completion per run and a false 'longest stretch with no step', with no error",
     evidence: "Reviewer run: obby.json (activity run_obby 30 s, 10 coins, policy order run_obby until 20 then speed_coil 100 coins), full single-run report, rates script prints 'complete:run_obby 1 per h 6.0' and 'longest stretch with no step 570 of 600'; the same report's inline `trace` holds 20 `activity_end` events with success true (120 per active hour)",
     smallest_fix: "In the §6a script add a completions count from the full report's `trace`: per id, `activity_end` events with `success` true, printed as 'completions:<id> n per h' (refuse when `trace` is a path object from --trace-out, or load that file). Add to the 'Wrong without an error' line: 'repeated activity completions (obby runs, tycoon tasks) are not steps: read the completions lines'. Extend the existing sim.py reward-rate proposal row with per-activity completion counts"}
  - {id: F2, class: blocking, check: C8 V4 + C4,
     where: ".agents/skills/progression-design/references/reward-tiers.md:29 (column 'value vs price': 'the model's sell value or the owner's value label'), :65-73 (worked example), .agents/skills/progression-craft/references/tools.md:103 and :109 (odds check: 'value in the price currency', prints 'expected value per roll ... for <price>')",
     expected: "platform-policy/references/rules.md:17 (§A, binding shared skill, wins): a paid roll whose prize is the currency it was paid with, or converts into it, is the stake-and-win-back shape: treat it as simulated gambling and do not build it; unclear cases go to the owner. V4: every paid-random line that lands is diffed against this skill",
     observed: "The tier table tells the agent to value paid random outcomes by their sell value in the price currency, and the odds check prints expected value per roll against the price. The worked example is a 250-coin egg where coins are sold for Robux, with outcomes valued 100 / 300 / 1,200 / 9,000 coins: expected value 348 coins per 250-coin roll. If those values are sell-back values (the column's first option), the example is a positive-value wager on a Robux-bought currency, and no line in the books names the rule. The coverage V4 row (table d) diffed only the odds display rows",
     evidence: "rules.md:17 vs reward-tiers.md:29, :65, :70-73; reviewer run of the §6d snippet on the example's own odds table: 'odds sum 1 ... expected value per roll 348.0 for 250'",
     smallest_fix: "reward-tiers.md:29: replace '(the model's sell value or the owner's value label)' with '(the owner's value label; if an outcome can be sold or converted back into the price currency, the roll is the stake-and-win-back shape in `platform-policy` rules §A: stop and raise it to the owner)'. One sentence in §7: the values are owner value labels; pets do not sell for coins. The same clause in tools.md §6d's input line. Self-check D line 95 (progression-design SKILL.md:95): add 'no paid random outcome sells back into its price currency'"}
  - {id: F3, class: blocking, check: C8 V3 + C3,
     where: ".agents/skills/progression-craft/references/tools.md:82-93 (§6b decision check), used by progression-design SKILL.md:86 and progression-craft SKILL.md:75 ('each identical stretch')",
     expected: "The self-check asks for every identical stretch (on purpose or reopened); the script must find them, or the book must say which stretches it cannot see",
     observed: "The script compares the two purchase lists by position and stops at the first difference, so it reports only the identical prefix of the whole report. After each prestige both policies start again from the same state and can buy the same things in the same order; those stretches are never reported, and the 'Reading' line does not say so",
     evidence: "Reviewer run, incremental example, greedy-roi vs cheapest-eligible full reports: the script prints 'identical first 31 of 464 purchases'. Split at each prestige step: run 1 identical 31 of 233, run 2 0 of 89, run 3 17 of 88, run 4 17 of 54. Two identical stretches after resets are missing from the answer",
     smallest_fix: "In the §6b script split both purchase lists at each `prestige` step and print the identical prefix per run (three lines). Add to 'Reading': 'a stretch that matches again in the middle of a run (not at a run start) is not found; read the purchase lists there by eye'"}
  - {id: R1, class: recommendation, check: C7 + C8 V6 V7,
     where: ".agents/skills/progression-design/SKILL.md:64-71 (D-21..D-28), :77 (rules line), §6 ending at byte 19,212",
     expected: "One rule, one place (V6); steps, rules and self-check inside roughly the first 18 KB (V7); 'better work, not longer books'",
     observed: "SKILL.md grew from 12.8 KB to 24.7 KB. D-21..D-28 restate §3 steps 2, 4, 5, 7, 9 and reward-tiers.md §5 almost word for word; :77 restates D-22. The celebrate-on-confirmed rule is stated in 8 places, below-price in 5. §6 ends at 19.2 KB, so its last lines (platform-policy written out, every number labelled) are the first to fall out after a compaction",
     evidence: "grep counts over the 12 files ('confirmed' 22 hits in 9 files; 'below price' 10 hits in 5); byte offsets: §4 7.7 KB, §6 16.1-19.2 KB",
     smallest_fix: "Cut D-21..D-28 to one line each that points to its §3 step or to reward-tiers.md §5 (or fold them into the steps), and drop the duplicate rules line :77. This alone brings §6 under about 17 KB"}
  - {id: R2, class: recommendation, check: C7,
     where: ".agents/roles/progression-designer.md:34, :61, :75; progression-design SKILL.md:38, :91-92; progression-craft SKILL.md:35, :80",
     expected: "The tier table is built when the task adds or changes rewards (the role's own :38 says so for the proof stage)",
     observed: "Work method step 4, 'Before you hand back' and both self-checks require a filled tier table from full single-run reports on every task. Eval briefs E2 (the sword breakpoint), E3 (players quit at level 12) and E5 (prestige feels pointless) add no rewards; an agent following the role file would spend runs on a table nobody asked for",
     evidence: "progression-craft/evals/briefs.md E2, E3, E5 must-pass lists name no reward tiers",
     smallest_fix: "Add 'when the task adds or changes rewards; otherwise write \"tier table: not in scope\"' to role :34 and :61 and to the two self-check lines"}
  - {id: R3, class: recommendation, check: C7 + C3,
     where: "reward-tiers.md:51, :87; timeline-genres.md:61; progression-design SKILL.md:91, :113 (principle 8 check)",
     expected: "The capstone rule is consistent with D-09 (SKILL.md:52: exponential costs belong in voluntary infinite sinks) and the uncapped-track cases, and its check can be run",
     observed: "'Each track ends on its capstone: its last step is its highest tier' has no answer for an infinite voluntary sink, which has no last step. The check reads 'the report's steps', but a report's last step is wherever the horizon or 'all goals reached' cut the run (reviewer runs: incremental stops at 'horizon reached', RPG at 'all goals reached'), not the track's end",
     evidence: "rpg-best report stop reason 'all goals reached' at 11,213 s; inc-greedy 'horizon reached' at 3,600 s",
     smallest_fix: "Reword to 'each finite track (and each run of a repeating track) ends on its capstone; an infinite voluntary sink has none', and check it on the timeline's planned finish row and the report time of that row, not on the report's last step"}
  - {id: R4, class: recommendation, check: C7,
     where: "reward-tiers.md:43 ('In every track and every policy, a tier's median gap is longer than the tier below it') and :75-77 (worked example)",
     expected: "One clear scope for 'rarer is bigger' and a worked example that follows it",
     observed: "The rule says 'in every track', but the example flags Lucky Find for being 'more frequent than level-ups', a different track. Under that cross-track reading, later rebirths (T3, 6 per hour) are also more frequent than level-ups (T2, 4 per hour) and are not flagged. An agent copying the example cannot tell which reading the self-check 'higher tiers rarer' (SKILL.md:91) means",
     evidence: "reward-tiers.md:75 level-up T2 4 per hour; :76 later rebirths T3 6 per hour; :77 Lucky Find compared with level-ups",
     smallest_fix: "State the scope once in §5 (the player feels all tiers together, so across the game per policy is the stronger reading) and make §7 follow it: flag the rebirth / level-up pair and say how it is resolved, or limit the Lucky Find note to its ceiling"}
  - {id: R5, class: recommendation, check: C8 V3,
     where: ".agents/skills/progression-craft/references/tools.md:99-101 (§6c one-liner and 'Reading')",
     expected: "The trap list names every way the printed numbers mislead",
     observed: "'Compare ... the median time across profiles'. `active_s_median` is the median over the runs that reached the goal only (sim.py:2029-2035), so a profile that reaches a goal in 2 of 40 runs shows a median from those 2",
     evidence: "Reviewer run, randomised RPG copy, 40 runs steady: TL-05 '2 / 40 ... 1806.0'",
     smallest_fix: "Add to 'Wrong without an error': 'the median is over the runs that reached the goal; read it only next to reached_runs'"}
  - {id: R6, class: recommendation, check: C8 V1,
     where: "progression-design SKILL.md:94, :95, :96 (self-check lines); :86 '(track sheet + two reports)'",
     expected: "§6 header: 'Each line names its input'",
     observed: "Three lines have no input in parentheses; 'track sheet' is named only here and is defined nowhere (§3 step 4 says 'one line each' without a place)",
     evidence: "SKILL.md:82 header vs :94-96; grep 'track sheet' finds :86 only",
     smallest_fix: "Prefix :94 '(reward ledger + full report)', :95 '(odds table + platform-policy rules §A)', :96 '(old vs new model)'; in §3 step 4 say 'in the working file's track sheet'"}
  - {id: R7, class: recommendation, check: C2,
     where: "progression-design SKILL.md:121 (principle 18)",
     expected: "Master UP-18 general check: the brief states budget and stop criteria before starting; the hand-back states the budget used",
     observed: "Row 18 has the stop criteria but no budget set before starting",
     evidence: "universal-principles.md UP-18 'general check'",
     smallest_fix: "Add to row 18: 'a pass budget (tuning rounds before the owner sees options) written in the restated brief; the hand-back states the rounds used'"}
keep: [
  the reward and celebration tier table as a sheet the agent owns (tiers by benefit, rates measured per named policy, rate ceilings as PROPOSAL, first-time vs repeat, text names, partner table of who gets what and when),
  the number display rule with fixtures (rechecked: 1,049,999 floors to 1.04M against a price ceiled to 1.05M; half-up would show both as 1.05M),
  the paid odds check (exact fractions; reran: 230 and 459 rolls for 90 % and 99 % at 1 %; float odds visibly miss 1),
  the guards that refuse --lean and multi-run reports in §6a and §6b,
  luck vs skill by skill profiles over seeds, read from runs_summary, and the multi-run timeline trap,
  the role file's 'What you ask partners for, and when' table and the 'Before you hand back' list,
  every old rule kept (word-level diff walked; nothing lost, steps renumbered only inside §3 and the role's work method, no outside reference to the old numbers),
  the core principles section: progression-specific examples and checks, no contradiction with the master,
  the GD-35 lines in rewards-ethics.md §6, which match platform-policy rules §A rows 2-5
  ]
verdict: fix-first
</spec>
```

## Results per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 36 rows checked (20 tagged + 16 untagged used), 0 failed. Every landed-in location opened; each carries the rule and, where checkable, a check. Rejections and partial rows (GD-02, SI-20 hand-off only; art, VFX, sound and UI execution findings) have sound reasons (V8). Weak check on GD-11: R3 |
| C2 core principles | pass | §7 in `progression-design` (loaded first), 17 rows with own examples and checks; 5, 9, 12 excluded with pointers; no contradiction found. Minor gap: R7. Re-read-after-compaction line present (§1, role file) |
| C3 self-review | fail | rates line and decision-check line rest on scripts that miss repeated activities and post-reset stretches (F1, F3); capstone check cannot be run as written (R3) |
| C4 kit rules and engine | fail (via F2) | no conflict with AGENTS.md, rules/*.md or the J018 decisions; no new engine claims; every sim.py, curves.py and chart.py mode named exists. F2: the value-vs-price column steers toward a shape `platform-policy` says not to build |
| C5 nothing valuable lost | pass | every removed word traced; old self-check lines all kept (split or sharpened); the old vfx / sound hand-off row replaced by a stronger one |
| C6 fixed rules | pass | role frontmatter identical to df13ff4 (md5); SKILL.md 123 / 84 lines; descriptions 388 / 394 characters, unchanged; J018 phrase in every changed file and the role comment; no tips section; no library IDs, transcript lines or Riot names in J018 text; `evals/` unchanged; files LF; outside the books only the two job files |
| C7 better work | yes, with weak spots | see judgment below; R1-R4 |
| C8 brief v2 | fail | V1 minor (R6); V2 pass; V3 fail (F1, F3; R5); V4 fail (F2); V6 and V7 weak (R1); V8 pass; V10 pass (game-designer vocabulary matches; conflicts filed as proposals); V11 pass (the one game-designer row adopted) |

## Judgment: better work?

E4 ("a 25-Robux egg with a 2 % legendary needed for zone 3, plus a 2x luck pass") with the new books: the agent still flags essential luck and loads `platform-policy` as before, and now also tiers the reveal by benefit and rarity, leaves below-price results without a celebration, gets exact odds sums and the 90 % / 99 % tails from one script, and hands VFX, sound and UI a table with triggers, rates and text names. E1 (incremental timeline) gains a decision check, measured reward rates and a display rule. These are real gains the old books did not have. The weak spots: the rate and decision scripts silently miss repeated activities and post-reset stretches (F1, F3), the value-vs-price column needs the stake-and-win-back guard (F2), and the design SKILL nearly doubled with restated rules (R1).

## For the lead (not for the maker)
- D-11, D-12, `cases.md` rows 9-10 and `timeline-genres.md:70` name LoL and TFT. They are J011 research-paper citations present at df13ff4, not J018 material. This is the same open question as the game-designer reviews' J003 citations.
- Coverage line 19 calls the tier rate ceilings "library numbers marked [inference]". They are the maker's own values. The books label them PROPOSAL correctly, so only the coverage wording is off.
- `python tools/sync_harness.py --check` reports DRIFT for the progression generated copies, as expected before the lead's sync.
