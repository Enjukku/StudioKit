---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer orchestration · claude-opus-5-5 · high · 2026-10-22

# Review: orchestration books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/orchestration/SKILL.md (172 lines, 27,538 bytes; §14 at byte 18,703, §15 at 21,912) + references/gates-and-feedback.md (GF, 105 lines) + references/briefs-and-handoffs.md (BH, 127 lines), working tree on top of df13ff4 after repair round 2, 2026-10-22. Not in scope: references/job-types.md (proposal-only, J018-D2 point 4), evals/.
reviewer: J018 reviewer orchestration (opus, high), round 3
looked_at_first: [
  the three book files read in full; git show df13ff4:.agents/skills/orchestration/SKILL.md read in full and walked line by line against the current text; git diff --stat df13ff4 (SKILL.md the only tracked change; GF and BH untracked new files; job-types.md and evals/ no diff, no untracked file),
  binding context: AGENTS.md, rules/company.md §2, §3, §7 (incl. :105 light checks J005-D8 and :107 repair-round limits), rules/messages.md §2 (key list, :86 time_budget) and §6, rules/owner-profile.md:16, rules/anti-overengineering.md rule 20, .agents/workflows/jobs/README.md contract table, templates/jobs/direction-sheet.md (decision-record fields), templates/jobs/evidence.md §4, job-types.md Contract rows (read-only), knowledge/reference/studio/agent-messaging-research-2026-10.md M-15,
  partner books (V10): reference-images/references/rounds.md §7, animation-design SKILL.md §3 step 6 and references/game-timing.md §4, sound-design S-133, game-design G-19 and row 19, art-review/references/feedback-briefs.md §6, preproduction/references/handoffs.md §2, progression-design SKILL.md:37 and row 14, progression-craft C-11, live-ops-craft (event-review.md §1, handoffs.md, process.md), .agents/roles/live-ops-designer.md:27, every external reference to `orchestration` § numbers (grep), tools/art/thumb_check.py (icon 150x150), engineering rework-study B08,
  library: matrix.md orchestrator column extracted by script (79 IDs) vs coverage table a (79 of 79 present, plus 11 untagged rows); principle/apply/check/mistake text of all 90 findings extracted by script and read against the landed-in text; universal-principles.md UP-13..UP-20 in full and the applies-to lists of UP-01..UP-12,
  my own V3 runs (scratch C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/rev3_orch/): GF §2 per-line Shown count and ceiling grep on p_good (true 1 → 1, ceiling 6), p_two (1 and 6 → 1 and 6), p_crlf (CRLF, .PNG → 3), p_bullet (bulleted and bold → no output = not ready), p_contact (contact sheet → 1), p_gif (gif and mp4 → 1, listed limit), p_dirdot (".png" inside a folder name → 4, rare), GF itself (line 97: 1); GF §1 taste grep on t_bad (11 wordings: 7 hit) and t_good (1 listed false hit) and on every knowledge/jobs/*/digest*.md and g1-packet.md (no hit); BH §6 hook on h_ok (pass, no output), h_bad (block line), h_case ("Art-Director", not a kit role: silent pass, listed), h_empty (0 bytes: silent pass; `test -s` catches it); python tools/verify.py --fast (SKILL size, descriptions, always-loaded, kb lint PASS; sync_harness DRIFT incl. the two new orchestration references and kb_index STALE: the lead's post-wave step),
  evals/briefs.md E-01..E-05 read as the lead at the start of a job,
  rev1 and rev2 findings each re-checked against the current text
  ]   # coverage/orchestration.md and proposals/orchestration.md were read after this
findings:
  - {id: R1, class: recommendation, check: "C4/V4 (rules/messages.md §2 time_budget, M-15) + C7 (eval E-02)",
     where: ".agents/skills/orchestration/SKILL.md:95 (§10 'Open with ... budget, stop criteria'), :126 (§14 line 7 'Every brief: ... budget and stop criteria'); references/briefs-and-handoffs.md:16 (Budget row: passes, image cap, tokens)",
     expected: "Budget pressure stays out of risky work: rules/messages.md:86 'time_budget ... not on money, saves or security work (M-15)'; the research reason is 'under time pressure the model may verify a little less' (agent-messaging-research M-15); eval E-02 (gem shop purchase) must pass 'No time_budget (money work)'",
     observed: "Every brief must carry a budget (passes, image cap, tokens), with no exemption for money, saves, remotes or security code. A lead briefing the E-02 builder writes a pass or token budget into a money brief; it does not break the literal key rule (time_budget) but carries the same pressure the rule keeps out, and its §14 line 7 marks a money brief without a budget as incomplete",
     evidence: "SKILL.md:95, :126; BH:16; rules/messages.md:86; M-15 row (agent-messaging-research-2026-10.md:45); evals/briefs.md E-02",
     smallest_fix: "BH:16 Budget row source cell, append: 'not in a brief for money, saves, remotes or security work: there the budget stays in the job card (rules/messages.md §2, time_budget)'. §14 line 7: 'budget and stop criteria (money, saves, remotes: stop criteria only)'."}
  - {id: R2, class: recommendation, check: "C4 (rules/company.md:107, rules/anti-overengineering.md rule 20)",
     where: ".agents/skills/orchestration/SKILL.md:71 (§7.3 'Two repair rounds per review gate ... an approach that failed both rounds restarts at its cheapest stage, not a third patch'); references/gates-and-feedback.md:82 ('after two repair rounds, diagnose')",
     expected: "The repair-round limit as the binding rule sets it: two per review gate, code review three (company.md:107; anti-overengineering rule 20; .agents/workflows/jobs/README.md 'code findings 3, other findings 2')",
     observed: "'Two repair rounds' is df13ff4 text (J016), but the new J018 clause 'not a third patch' now forbids the third code-review round the rule grants. In a saved workflow the stage itself stops at three for code, so harm is small; in a hand-run code stage the lead would stop at two and restart from the cheapest stage. Not blocking: the count predates J018, the binding rule wins by priority (AGENTS.md §0), and the clause keeps rule 20's intent (stop patching, rethink the approach)",
     evidence: "SKILL.md:71; GF:82; rules/company.md:107; rules/anti-overengineering.md:39; workflows README contract row 'Repair rounds'",
     smallest_fix: "SKILL.md:71: 'Repair rounds per review gate as `rules/company.md` §7 sets them (two; code review three); then ... an approach that failed every allowed round restarts at its cheapest stage, not one more patch'. GF:82: 'after the repair-round limit (SKILL §7.3), diagnose'."}
  - {id: R3, class: recommendation, check: "C8 V10 (partner book rebuilt in wave 3)",
     where: ".agents/skills/orchestration/SKILL.md:33 (§2 Live update row); references/briefs-and-handoffs.md:46 (§4 Live update row)",
     expected: "The lead's split of a live update reads the input the rebuilt live-ops books hand it: the craft-ask table (live-ops-craft/references/event-review.md §1: what each craft is asked for, at which stage, judged on which capture); .agents/roles/live-ops-designer.md:27 'Your craft-ask table tells the lead which craft each part needs, at which stage, and the capture it will be judged on'",
     observed: "Both rows name the plan and the card items (pain point, audience, themes, differentiator) but not the craft-ask table, so a lead may size and brief the linked jobs without the stage and capture each craft was promised. The live-ops proposal (proposals/live-ops-designer.md:19) targets job-types.md only; no row asks for this book line, so this is a consistency gap, not an ignored proposal",
     evidence: "SKILL.md:33; BH:46; live-ops-designer.md:27; live-ops-craft/references/event-review.md:7; live-ops-craft/references/handoffs.md:17; process.md:18, :60",
     smallest_fix: "BH:46, append: 'split into jobs by the plan's craft-ask table (`live-ops-craft/references/event-review.md` §1): each row's craft, stage and capture go into that job's card'."}
  - {id: R4, class: recommendation, check: "C8 V3/V14 (screening aid with an eye check and listed limits: not blocking under the lead's severity rule)",
     where: "references/gates-and-feedback.md:12 (taste grep and its known misses)",
     expected: "The common taste wordings are caught or listed as misses",
     observed: "'Which one looks best?', 'Does this work for you?' and 'Are you OK with B?' give no hit and are not in the listed misses ('Happy with this?', 'Good to go?'). The line still says to read the question line against the job card, so the eye check closes it",
     evidence: "Reviewer run t_bad.md: 7 of 11 wordings hit; the 4 misses are 'Happy with this?' (listed) and the three above (not listed)",
     smallest_fix: "Add `best\\?|work for you|ok with` to the pattern, or add the three wordings to the misses."}
keep: [
  every rev1 and rev2 keep item is unchanged: the four lines (SKILL §1.1, §10, BH §1 with touch input and player count), the ordered one-screen packet (§8) with the recommendation's weakest part, the per-gate table and image budget (GF §2) with the Shown line as the counted thing, the input-proof table and owner-confirmed feel and listening lines, closed doors with "may return only if" and the history-vs-later-files reading rule, the owner-note steps (GF §5) with the owner's note standing over a reviewer, one marker list pointed to game-timing §4 (retime rule only in BH §3), done on evidence, the two-round restart idea, §14 line 8 per-type items incl. the effect row,
  the rev2 F1 fix (SKILL:47): constraint owners give no technical option menu; the progression-designer returns targets as its books shape them (matches owner-profile.md:16, progression-design :37, :116, progression-craft C-11),
  the per-line Shown count (GF:23): one line per question, correct on every common form I ran, listed limits true,
  the BH §7 brief: stop criteria, display sizes, docs-map rows, image caps that match reference-images rounds §7 (round 1 at most 6 incl. regenerations, round 2 at most 3),
  the round-2 moves (§2 → BH §8, §10 → BH §9, §11 → BH §10, §4.3 → template fields, §5.1 → recipe Contract rows, §9.7 → evidence.md §4, §10 key list → rules/messages.md §2): every target holds the moved text,
  nothing from df13ff4 dropped
  ]
verdict: pass
</spec>
```

No blocking finding. Four recommendations, each a one-line fix.

## Check results
| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass | 79 of 79 orchestrator-tagged findings have a row (script: matrix.md column vs coverage table a); 11 untagged rows correct. Every landed-in location opened against the extracted principle, apply and check text: the rule is there, and each lead-runnable check is a §14 line or a GF/BH aid. 4 rejections (PP-06, PP-08, SD-29, SD-31) sound: craft method the lead must not prescribe. Rows checked 79, failed 0 |
| C2 core principles | pass | SKILL §15 in the skill the lead loads first; UP-13..UP-18 (the master's orchestrator rows) each with a lead example and a check with its input; 1-4, 6-8, 10, 11, 19, 20 in lead terms; 5, 9, 12 routed with a reason. No contradiction: row 20 "over 3 per second" blocks, matching UP-20 "at most 3"; row 16 has "say our own weak spots" (UP-16 honest weaknesses); fresh eyes (UP-16) is kept as review by another agent (§7.2) |
| C3 self-review | pass | Every §14 line names its input; line 3 counts the Shown line by eye; line 8 covers every BH §4 row. R1 touches line 7 for risky briefs |
| C4 kit rules and engine | pass, with R1-R2 | rev2 F1 fixed. No engine claim added; icon 150x150 matches thumb_check.py:16, :73. Extra-gate rule, G1 counts, light checks (J005-D8), owner-note precedence, tie rule consistent with company.md §2-§3, §7. All cross-references resolve. R1 (budget in risky briefs vs time_budget rule), R2 (repair-round count vs code review three) are recommendations |
| C5 nothing valuable lost | pass | Every df13ff4 line kept, sharpened or moved; round-2 moves land in files that hold the text (README "blocked with the list of what is needed", messages.md §2 key list, direction-sheet fields, evidence.md §4 rows, BH §8-§10); matches coverage table c and both addenda |
| C6 fixed rules | pass | Only SKILL.md plus the two new references in this skill, and coverage/proposals for orchestration; job-types.md and evals/ no diff; no lead role file; frontmatter byte-identical to df13ff4 (description 277 chars); 172 lines; §1-§14 and their steps not renumbered, §15 appended; J018 phrase in all three headers; no Riot, library IDs, transcript lines, games or champions in bodies (scan); no tips section. sync_harness drift for the new files is the lead's post-wave step |
| C7 better work | better | see below |
| C8 brief v2/v3 | pass, with R3-R4 | V3/V12: I ran every command the books name on the real input forms; outputs match the book and the listed limits (R4: three more taste wordings to list). V13: no measure longer than one command line. V1: image budgets and inputs named. V2: hook usage real (docstring, run). V4: R1. V6: retime and other rules in one place. V7: §14 starts at 18.7 KB, at about the 5,000-token edge; rest declined with a sound reason (§9 is cited by number from five files), mitigated by SKILL:10 and the harness re-load. V8: findings became card items, brief asks, packet lines, §14 checks. V10: R3. V11: no other role's row targets SKILL, GF or BH; recipe and workflow rows collected for G3 |

## Earlier findings
| Id | Now |
| --- | --- |
| rev1 F1-F3, R1, R3, R5-R13 | fixed (confirmed again) |
| rev1 R2 / rev2 R4 (V7 window) | partly fixed (§14 from 20.2 KB to 18.7 KB); rest declined with a sound reason; accepted |
| rev1 R4 / rev2 R5b (taste grep) | fixed for the named wordings; three more listed in R4 |
| rev2 F1 (progression-designer under the no-menu rule) | fixed (SKILL:47) |
| rev2 R1 (Shown line in the worked example) | fixed (GF:94-97; count reads 1) |
| rev2 R2 (only the first Shown line read) | fixed (per-line count, GF:23) |
| rev2 R3 (worked brief incomplete) | fixed (BH:76-87) |
| rev2 R5a (empty payload file) | fixed (BH:58, `test -s`) |
| rev2 R6 (PI-06 quote, GD-22 parameters) | fixed (coverage PI-06; SKILL:13, BH:10) |
| rev2 R7 (retime twice; effect row missing in §14 line 8) | fixed (SKILL:62 pointer; SKILL:127) |

## Better work (C7)
Read as the lead at the start of eval E-01 (sound brief for the fireball hit), E-02 (gem shop purchase) and a pet-companion character job (L). Against df13ff4 the lead now writes the four lines before sizing; sizes multi-form characters correctly; sends look-owning leads for research, a warm-up set aside, one radical option and equal finish, and constraint owners for limits only; asks one goal question with the card's goal word; names the recommendation's weakest part; shows only the images the owner must judge, counted on the Shown line; closes doors and keeps them out of later briefs; turns owner notes into one-problem repair briefs by layer; treats a retime as a contract change; and says "done" only with evidence. For E-01 the brief points to the marker list and the one sync rule and adds the cue list per state change. For E-03 and E-04 the hand-back and approval rules are unchanged and sharper (hook limits named). This is clearly better work with fewer wasted rounds, and the repairs made the book shorter in SKILL.md (28.8 KB to 27.5 KB) without losing rules. Weak spots: the budget line has no exemption for money, saves and remotes briefs (R1); the repair-round wording is off by one for code (R2); the live-update split does not name the live-ops craft-ask table (R3); several rules (four lines in the card, the Shown line, the closed-doors table, stop and budget keys) depend on template fields that exist only as proposals until the owner's G3 answer, so until then each lead must remember them; the self-check still sits at the edge of what a compaction keeps.
