---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer live-ops-designer · claude-opus-5-5 · high · 2026-10-22

# Review: live-ops-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/live-ops-designer.md (body) + .agents/skills/live-ops-design/ (SKILL.md, references/) + .agents/skills/live-ops-craft/ (SKILL.md, references/ incl. new event-review.md; evals/ not reviewed), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer live-ops-designer (opus, high)
looked_at_first: [
  all book files read in full (role body, both SKILL.md, references process.md, handoffs.md, feedback-ops.md, event-review.md, and the diffs of cadence-content.md, events-offers-rules.md, evidence-feedback.md, measurement-health.md), then git diff df13ff4 of every book file,
  knowledge/reference/craft/riot/universal-principles.md (master; UP-01..UP-20 and each "applies to" list),
  knowledge/reference/craft/riot/matrix.md (live-ops column, script-extracted: 36 findings) and the full text of all 36 findings in the topic files,
  partner books read-only: game-design/references/systems-economy.md §8-§9, progression-design/references/reward-tiers.md §2, §6, §8, marketing-design SKILL §4 M-15..M-23, art-review/references/art-bible.md, game-designer and progression-designer role files, studio-mcp/references/tools.md, vfx-craft/references/measure.md §1 (frame folder), platform-policy/references/rules.md §A,
  templates/live-ops/update-plan.md and event-design.md, rules/messages.md section list,
  docs mirror: production/game-design/liveops-planning.md:45-60, content-updates.md:30-36, _api-reference/classes/GuiService.yaml (ReducedMotionEnabled), production/publishing/accessibility.md:186,
  tools/liveops/feedback_count.py (source, --help, count --help) and README.md,
  my own V3 runs on synthetic items files in the real input form (scratch: <scratchpad>/liveops-rev1/): validate (21 good lines, exit 0); count with --end 2026-10-28 and with --end 2026-10-27; a split theme spelling; an author with 4 of 4 messages; a duplicate re-export with a hand-minted item_id; anon- review rows; the eval E3 shape (60 messages, 52 from 4 authors),
  live-ops-craft/evals/briefs.md E1-E5 (E2 and E3 walked through with the new books)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C1 + C3 + C8 V5,
     where: ".agents/skills/live-ops-design/SKILL.md:74 (L-22) and references/cadence-content.md:66 carry the rule; .agents/skills/live-ops-craft/references/event-review.md:5 (scope: 'an event, a season beat, a theme, a variant line or a limited item'), references/process.md:49 (event brief lines), live-ops-craft SKILL.md:70 and :73 (self-check C); coverage live-ops-designer.md:41 (GD-33 row claims 'self-review check (self-check C post-update line)')",
     expected: "GD-33 (tagged live-ops-designer) is checkable: 'new worlds state their escape in the theme brief and differ clearly from previous ones'; check: 'compare a capture of the new world with previous worlds: palette, shapes and theme differ clearly; the backlog holds map revisits with evidence'. Owner: 'Turn every checkable finding into a line in the role's self-review'",
     observed: "Only the backlog half has a self-review line (process.md §6 keep / change row, self-check C :73). The 'new world or zone states its escape and differs clearly from the last' half is a standard only: no brief field carries the escape line (process.md §3 lists event, theme, variant and limited-item lines only), no capture is named for it, no E line checks it, and event-review.md :5 scopes the review away from a plain new world or zone update. A new world is one of the most common live updates on Roblox (pet and simulator games ship one per update), so the agent will brief it with no escape line and never compare it with the last world",
     evidence: "library game-design-fun.md GD-33 'check:' line; grep of the books for 'escape': design SKILL.md:74, cadence-content.md:66 only; event-review.md:5; process.md:49; craft SKILL.md:70-73",
     smallest_fix: "(1) process.md §3 line 49: add 'a new world or zone: the escape in one line and how it differs from the last world (palette, shapes, theme)' to the brief lines, and widen the sentence's scope to 'an event, theme, variant line, limited item or new world or zone'; (2) event-review.md:5: add 'a new world or zone' to the scope; add one capture row (C-13: the new world's first view next to the last world's first view, same camera) and one line (E-19 'The new world is an escape': pass when palette, shapes and theme differ clearly and the escape line reads from the capture; fix owner environment-designer, art-director); (3) self-check C :70 add 'the escape line (new world or zone)'; (4) correct the coverage GD-33 row"}
  - {id: F2, class: blocking, check: C1 + C8 V5 + V6,
     where: ".agents/skills/live-ops-craft/SKILL.md:70 (self-check C brief-line list) vs references/process.md:49 (the brief-line list) vs .agents/roles/live-ops-designer.md:37 (Work method 6, a third list); coverage live-ops-designer.md:33 (GD-08: 'my check is the brief line')",
     expected: "V6: one rule, one place; V5: every row whose finding has a runnable check names the self-review line that carries it. GD-08 check: 'each item in a set belongs to a named theme family with a shared visual'; SI-18 apply: 'record whether it is a new version (new palette) or the same character in a new situation'",
     observed: "The same list of event brief lines is written three times and has already drifted. process.md:49 has the reward family and, per variant, new version vs same subject in a new scene; self-check C :70 omits both; the role's Work method 6 omits the reward family, the twist line and the target experience. The agent's self-check therefore never verifies the reward-family line the coverage names as GD-08's check, nor the variant type line",
     evidence: "process.md:49 '· the reward family (event items share one named theme family and motif players can collect) · ... whether it is a new version (new palette) or the same subject in a new scene'; craft SKILL.md:70 list ends '... the anchors-kept list or its pointer, the tier rows'; role :37 '(promise, what fans want, niche, story, tone shift, anchors-kept list, tier rows)'",
     smallest_fix: "Make process.md §3 the only list. Self-check C :70 becomes '(event, theme, variant line, limited item; else \"event lines: not in scope\") The brief carries every line of `process.md` §3 for this scope, each filled or marked n/a with a reason (input: the brief and the tier table)'. Role :37 replaces its parenthesis with 'the brief lines of `live-ops-craft/references/process.md` §3'"}
  - {id: R1, class: recommendation, check: C8 V3 + V12 + V14,
     where: ".agents/skills/live-ops-craft/references/feedback-ops.md:54 and :58 (known false readings)",
     expected: "Each row's 'What I do' is correct, and the table names the false readings of the common inputs the agent will give the tool, including the role's own eval E3",
     observed: "(a) :54 'set the end one window past the last item I mean to count' is wrong: items files accumulate across weeks, so an end one window later counts the next window's items too, silently. (b) The common trap is not listed: a date-only --end is 00:00Z of that day, so a week written 'Oct 21-27' as --end 2026-10-27 drops the whole last day with no error. (c) :58 covers only 'one author with 4 or fewer messages'; the eval E3 shape (60 messages, 52 from 4 authors) gives no flag either, because no single author has half the messages. (d) Two overlapping inbox exports turned into items by hand (feedback-ops.md:14) get new item_ids, so the duplicate check passes and messages (and the loud flag) are inflated",
     evidence: "Reviewer runs: liveops-rev1-items.jsonl with --end 2026-10-28: in-game event.promise-mismatch 1 / 4, entrance 2 / 4; same file with --end 2026-10-27: promise-mismatch row gone, entrance 2 / 3, no error. liveops-rev1-e3.jsonl: 'veterans.no-goals | discord | 12 / 12 | 100.0 % | 60 |' with an empty Flags cell (code: feedback_count.py:200 needs top >= 5 and 2*top >= msgs). Duplicate d0-dup accepted: 'event.final-reward-too-long ... 9 messages ... 6 of 9' where the real count is 8 and 5",
     smallest_fix: ":54 'What I do': 'keep the end at the window boundary (end is out); an item at exactly the end belongs to the next window'. Add rows: 'a date-only --end (2026-10-27) | is 00:00Z of that day: the whole day is out | write the end as the day after the last day (Oct 21-27 → --end 2026-10-28)'; 'several loud authors, none with half the messages | no flag | compare messages with distinct authors; when messages are more than about 3 per author, read the per-author spread on the raw items and say it in words'; 'the same message in two overlapping exports | counted twice in messages, no error | take each item_id from the export's own message id, or de-duplicate overlapping exports before tagging'. Extend proposals row 5 with (e) per theme, the top three authors' message shares (no keys printed)"}
  - {id: R2, class: recommendation, check: C8 V1,
     where: ".agents/roles/live-ops-designer.md:58 ('each line names its input'); .agents/skills/live-ops-design/SKILL.md:87-89, :91-93; .agents/skills/live-ops-craft/SKILL.md:66, :68, :69, :74, :75",
     expected: "V1: every self-review line names its input",
     observed: "The new lines name their input; the kept lines do not, though the role file says every line does",
     evidence: "for example design SKILL.md:87 'Urgent harm routed first, outside the ranking.'; craft SKILL.md:68 'Plan: hypothesis per option, builder numbers, one recommendation, default stated.'",
     smallest_fix: "Add the input in parentheses to each listed line (plan file, sort file and count file, the briefs, log.md, the hand-back) or drop 'each line names its input' from role :58"}
  - {id: R3, class: recommendation, check: C7,
     where: ".agents/skills/live-ops-craft/SKILL.md:37 (step 8a), :71 (self-check C concept round); .agents/roles/live-ops-designer.md:37; references/event-review.md:76 (worked example)",
     expected: "The concept round stays inside the scope the owner's pick froze (step 7, L-12) and fits briefs where the owner already fixed the premise",
     observed: "(a) The one-pager fields (premise, promise, activity, reward shape, niche, tone shift, fans want) have no cost or scope-fit field, yet the worked example rejects option B 'on cost' and B is a new zone, which the frozen scope may not hold. (b) Eval E2 gives the premise and parts (currency, crate, countdown deal); the books make a 3-premise round and 'a reason per rejected option' mandatory for every event, so the agent either pitches against the owner's brief or fails its own self-check",
     evidence: "craft SKILL.md:37 field list; :71 'the concept round's pick is recorded with a reason per rejected option'; evals/briefs.md E2",
     smallest_fix: "Step 8a: add 'fit to the approved scope and capacity (builder rough or \"reuses X\")' to the one-pager fields; add 'when the owner's brief already fixes the premise, the round covers only what is open (theme niche, tone, reward family) or is skipped with the decision id'. Self-check C :71: 'or the decision id that fixed the premise'"}
  - {id: R4, class: recommendation, check: C2,
     where: ".agents/skills/live-ops-design/SKILL.md:113 (§7 row 13), :118 (row 18)",
     expected: "Each row's check can be run on a named input; UP-13 check: 'problem, constraints, target experience and success test before any output'; UP-18 check: 'the brief states budget and stop criteria; the hand-back states the budget used'",
     observed: "Row 13's check 'Plan fields filled before options (design §6)' points to a §6 that has no such line, and update-plan.md has no target-experience or constraints field (proposals row 2 asks for it). Row 18 has stop criteria but no budget",
     evidence: "design SKILL.md:86-94 (§6 lines); templates/live-ops/update-plan.md:35 (§C hypothesis column)",
     smallest_fix: "Row 13 check: 'Plan header and each option row carry problem, target experience, constraints (capacity, policy, age label) and success test before any option is ranked (input: plan file; template rows pending proposals row 2)'. Row 18: add 'the brief's capacity and effort budget; the review records actual vs estimate'"}
  - {id: R5, class: recommendation, check: C7 + C8 V6 + V10,
     where: ".agents/roles/live-ops-designer.md:44-55; references/handoffs.md:8-17; references/process.md:52-60; references/event-review.md:10-21; design SKILL.md:68-75 vs :103-120",
     expected: "One place per rule; 'better work, not longer books'; one 'when' per partner",
     observed: "Four 'who gets what, when' tables now exist (role, handoffs §1, process §3, event-review §1), and the timings already differ: marketing is first briefed 'after the pick' (handoffs.md:14) vs 'when the build is credible' (role :51, event-review.md:19). design SKILL.md grew from 10.2 KB to 24.2 KB; L-16..L-23 and §7 rows 3, 4, 11, 15, 19 state the same rules twice; 'grey box / config build' appears 13 times in 5 files, 'concept round' 11 times in 6",
     evidence: "byte counts df13ff4 vs now; grep -c counts across the 11 book files",
     smallest_fix: "Keep event-review.md §1 (crafts) and handoffs.md §1 (planning partners) as the two tables; make the role table one line per partner with a pointer, and use one 'when' for marketing (first brief after the pick for the calendar and fact sheet; event kit when the build is credible). In §7, let rows 3, 11, 19 point to L-18, L-17, L-19 for the rule and keep only the example and check"}
  - {id: R6, class: recommendation, check: C8 V4,
     where: ".agents/skills/live-ops-craft/references/event-review.md:57 (E-08), :36 (C-06)",
     expected: "platform-policy rules §A: 'A modifier (luck potion, pity) MUST explain its numeric effect before purchase AND the shown odds MUST change while it is active'; event luck boosts are common live-ops content",
     observed: "E-08 checks one windup, odds before the buy button and the restricted path, but not a boost; the coverage V4 line says E-08 matches 'shown odds change while a modifier is active'. The launch checklist L3 has it, so the release gate is safe; the capture review is not",
     evidence: "platform-policy/references/rules.md §A row 5; event-review.md:57; templates/live-ops/event-design.md:62 (L3)",
     smallest_fix: "E-08 input: add 'the odds screen with the event boost active (if any)'; pass: add 'the boost's numeric effect shown before purchase and the shown odds changed while it is active'"}
  - {id: R7, class: recommendation, check: C4,
     where: ".agents/skills/live-ops-craft/SKILL.md:37 ('(`rules/messages.md` §6)'), :40 ('lesson draft written'); references/process.md:98 ('lesson draft in `knowledge/inbox/`')",
     expected: "rules/messages.md §2 is the brief format; AGENTS.md §5 and role :78: the lead writes inbox drafts from the hand-back's lesson field",
     observed: "Both lines are older than J018 but sit in steps the maker rewrote: §6 is 'Review finding', and the inbox line tells the agent to write where its role says it must not",
     evidence: "rules/messages.md:40, :152; role :78 'you do not write to knowledge/inbox/'",
     smallest_fix: "craft SKILL.md:37 '§6' → '§2'; :40 and process.md:98 'lesson in the hand-back's lesson field (the lead writes the inbox draft)'"}
keep: [
  the event-review.md file as a whole: the craft-ask table with what, when and the capture each craft is judged on; the named capture set with conditions and an image budget; E-01..E-18 each with input, pass condition and fix owner; the status labels and could-not-check list; review notes that say what and why, never how,
  the worked example (Halloween pet sim): concept round with an atypical option kept as the top tier, brief lines filled from counted evidence, a correct earned-only egg reading against platform-policy §A, fix notes that leave the how to the craft,
  L-16 one promise every craft keeps and the promise, tier and identity rows added to the post-update review and the failure-response table, with matching feedback themes in the codebook,
  the concept round and gate freeze (L-21, craft step 8) and 'cooler is a ticket with a cost',
  the count tool's known false readings table as a labelled screening aid (its arithmetic rows re-checked: exclusive end, split spellings, anon rows, flag threshold all as stated),
  the role file's partner table and 'Before you hand back' list, the pain-point-with-observation rule and request restated as problem,
  every old rule kept (diff walked: the removed 'Working with other agents' bullet moved into the partner table with its content; old design step 7 kept as step 8; no outside reference to the renumbered steps),
  the §7 core principles: all eight master principles that list live-ops-designer (UP-01, 07, 11, 13, 14, 16, 18, 19) plus ten more, each with a live-ops example and a check on a named input; 5 and 9 excluded with a reason; nothing contradicts the master,
  V11: the progression-designer's proposal row adopted (L-18, handoffs §3 C2); proposals for templates, recipes, a capture preset, the count tool and two library lines, each with evidence
  ]
verdict: fix-first
</spec>
```

## Results per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (2 rows) | 61 rows checked (36 tagged + 25 untagged used); every landed-in location opened. Failed: GD-33 (the new-world half has no brief line or capture check, F1), GD-08 (the claimed brief-line check is missing from self-check C, F2). Rejections and partial rows (GD-16, GD-27, GD-32, LC-23, PP-32, PP-33, RI-04, SD-21, SI-11, SI-18) point to the partner's measure with a sound reason (V8, V13) |
| C2 core principles | pass | §7 in `live-ops-design` (loaded first), 18 rows; all 8 master principles for this role present with own example and check; 5, 9 excluded with reason; no contradiction. Weak pointers: R4. Re-read line in §1, craft §1 and the role |
| C3 self-review | fail (via F1) | E-01..E-18 run on named studio-operator captures and partner measures; inputs exist in the kit (frame folders at 30 fps as in vfx-craft measure.md §1; reduced-motion stills as ui-design asks). New-world check missing (F1) |
| C4 kit rules and engine | pass | no conflict with AGENTS.md, rules/*.md or J018-D2..D4; docs claims checked (liveops-planning.md:53-55, content-updates.md:34); only real feedback_count modes named. Two old pointers in rewritten steps: R7 |
| C5 nothing valuable lost | pass | every removed or changed line traced to its new place; coverage table c matches the diff |
| C6 fixed rules | pass | role frontmatter byte-identical to df13ff4; SKILL.md 120 / 77 lines; descriptions 351 / 390 characters; J018 phrase in every changed file and the role comment; no tips section; no library ids, transcript lines or Riot names in J018 text; evals/ unchanged; only the books and the two job files from this maker |
| C7 better work | yes, with weak spots | see below; R3, R5 |
| C8 brief v2 / v3 | fail (via F2) | V1 partial (R2); V2 pass; V3 pass with gaps in the limits (R1); V4 pass, one line short (R6); V6 fail (F2), weak (R5); V7 pass (§1-§6 end at 17.4 KB, §7 after with a re-read line); V8 pass (brief lines, craft-ask table, capture review; template fields as proposals); V10 pass (tier names, attempt cue / confirmed result, flat-key captures match partners; timing drift R5); V11 pass; V12 partial (R1); V13 pass (no measuring code; partner measures pointed to); V14 pass (label and eye check present) |

## Judgment: better work?

Walked E2 (Halloween event with a crate and a countdown deal) and E3 ("Discord is screaming for PvP") with the new books. For E2 the old books gave a policy-correct event design but nothing on what the event looks, sounds and feels like, or on how its parts agree. The new agent writes one promise sentence that every craft brief quotes. It asks the progression designer to place each reward in the game's tier table, it asks each craft for its part at the cheapest stage, and before release it judges the build on twelve named captures with eighteen checks: entrance in the first view, rarer looks bigger, nothing celebrates a rejected purchase, variants keep their anchors, one brand property changes, the event reads in grayscale. These checks find real event failures that no single craft's own review finds, so the output is clearly better. For E3 the new false-readings table helps, but it misses the exact E3 shape: four loud authors, none with half the messages, so the flag stays silent (R1). Weak spots: new-world updates get no escape line and no capture check (F1); the brief-line list is written three times and has already drifted (F2); the concept round has no scope or cost field, and it does not fit a brief that already fixes the premise (R3); the design SKILL more than doubled, with rules and principles that restate each other (R5).

## For the lead (not for the maker)
- `live-ops-design/references/cases.md:14-15, :24` name League of Legends, TFT and Riot. These lines are J014 research-paper case rows that were present at df13ff4 and are unchanged. They are not J018 material.
- `python tools/sync_harness.py --check` was not run here. The generated copies will be out of date until the lead syncs them.
