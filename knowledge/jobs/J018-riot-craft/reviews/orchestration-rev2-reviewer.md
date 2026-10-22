---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer orchestration · claude-opus-5-5 · high · 2026-10-22

# Review: orchestration books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/orchestration/SKILL.md (183 lines, 28,848 bytes) + references/gates-and-feedback.md (GF) + references/briefs-and-handoffs.md (BH), working tree on top of df13ff4, after repair round 1, 2026-10-22. Not in scope: references/job-types.md (proposal-only, J018-D2 point 4), evals/.
reviewer: J018 reviewer orchestration (opus, high), round 2
looked_at_first: [
  the three book files read in full, then git show df13ff4:.agents/skills/orchestration/SKILL.md and git diff df13ff4 (SKILL.md only file changed; the two references are new; job-types.md and evals/ have no diff),
  binding context: AGENTS.md, rules/company.md (all), rules/messages.md §2 and §9, rules/owner-profile.md:16, rules/assistants/claude.md (Peer message row), knowledge/design/game-profile.md, knowledge/jobs/README.md:13, templates/jobs/ listing, J005-D8 (company.md §7, J005 decisions.md:22),
  partner books (V10): reference-images SKILL.md §3-§4 and references/rounds.md §7, animation-design SKILL.md §3 step 6 and references/game-timing.md §4, sound-design S-133, game-design G-19, art-review/references/feedback-briefs.md §6, preproduction/references/handoffs.md §2, progression-design SKILL.md step 8 and row 14, progression-craft SKILL.md C-11, .agents/roles/progression-designer.md,
  knowledge/reference/craft/riot/universal-principles.md UP-13..UP-20 in full (applies-to lists), matrix.md (orchestrator column by script: 79 IDs, all have a coverage row) and the principle/apply/check text of all 79 findings (script extract), the 11 untagged rows,
  tools: tools/hooks/handback_check.py (source and docstring), J018 tool-modes.md, stage2-brief-v2.md V1-V14,
  my own V3 runs (scratch C:/Users/Firew/AppData/Local/Temp/claude/C--Users-Firew--claude-spares-spare-5bnXLW/15d0fbc0-e7e9-4bea-af68-9ddb5da374ba/scratchpad/rev2_orch/): GF §2 Shown-line count and ceiling grep on p_good.md (true 1), p_example.md (the GF §8.1 form), p_two.md (two questions, 1 + 6 images), p_crlf.md (CRLF, .PNG, .jpeg); GF §1 taste grep on t_bad.md (9 taste wordings), t_good.md and the real g1-packet.md; BH §6 hook on h_ok, h_bad, h_code (coverage only in a code block) and h_empty (0-byte file); a per-line awk alternative for the Shown count,
  evals/briefs.md E-01..E-05 read as the lead at the start of a job,
  rev1 findings F1-F3, R1-R13 each re-checked against the current text
  ]   # coverage/orchestration.md and proposals/orchestration.md were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V10 (partner books) + C4 (rules/owner-profile.md:16 scope)",
     where: ".agents/skills/orchestration/SKILL.md:47 (§4.1 last sentence, added in repair round 1)",
     expected: "The no-option-menu rule covers only technical choices (owner-profile.md:16, row 'Engineering choices'). The progression-designer's rebuilt books give the owner options: progression-design SKILL.md:37 step 8 'returns options with trade-offs. The owner chooses between concrete experiences'; :116 row 14 'options bracket the key number; one recommendation'; progression-craft SKILL.md:52 C-11 'the owner picks between concrete experiences with charts'. A hand-off conflict is a proposal row, never a silent change (V10)",
     observed: "'A constraint owner (architect, performance-engineer, progression-designer) returns limits and needs, never an option menu.' A lead following this briefs the progression-designer at D1 to return no options, against its own books; the receiver must either break its book or return needs-decision (AGENTS.md §4), and the owner loses the choice between concrete progression experiences that design numbers need (AGENTS.md §0: numbers are proposals until the owner confirms). Coverage repair-round row R1 justifies it with the owner-profile line, which is about engineering",
     evidence: "SKILL.md:47; owner-profile.md:16; progression-design/SKILL.md:37, :116; progression-craft/SKILL.md:52; coverage/orchestration.md:217",
     smallest_fix: "SKILL.md:47 last sentence: 'A constraint owner (architect, performance-engineer) returns limits and needs, never an option menu for a technical choice; the progression-designer returns its targets the way its books shape them (options that bracket the key number, one recommendation).' Update coverage row R1 to match."}
  - {id: R1, class: recommendation, check: "C7 (worked example vs rule) + C8 V12",
     where: "gates-and-feedback.md:92 (§8.1 packet (1)) vs :21 ('in one line under the goal question') and :23 (grep '^Shown:')",
     expected: "The worked example writes the Shown line the way the rule and the screening grep need it: its own line, starting with 'Shown:', under the goal question",
     observed: "§8.1 puts `Shown: option-sheet.png` inline inside item (1), in backticks, before the goal question (2). A lead that copies the example gets 0 from the count and the book's own verdict 'the packet is not ready'",
     evidence: "Reviewer run p_example.md (the §8.1 form): Shown count 0, ceiling 2",
     smallest_fix: "§8.1: end item (1) at the option sheet and add after (2) a line 'Shown: option-sheet.png'."}
  - {id: R2, class: recommendation, check: "C8 V3/V12/V14 (screening aid with eye check and listed limits: not blocking under the lead's severity rule)",
     where: "gates-and-feedback.md:23 (`grep -m1 \"^Shown:\" ...`)",
     expected: "The budget is per question ('G1, one option sheet per question', GF:21), so a packet or digest with two questions has two Shown lines; the count reads each, or the known limits say it does not",
     observed: "`-m1` reads only the first Shown line; the known limits do not mention it. The eye check in SKILL §14 line 3 still catches it",
     evidence: "Reviewer run p_two.md (Q1 Shown: 1 image; Q2 Shown: 6 images): prints 1, no error. Per-line alternative `grep -n \"^Shown:\" <packet.md> | awk -F: '{l=tolower($0); n=gsub(/\\.(png|jpe?g|webp)/,\"\",l); print \"line \" $1 \": \" n \" images\"}'` prints 'line 3: 1 images' and 'line 5: 6 images'; on p_good.md, p_crlf.md it gives 1 and 3 (true); on p_example.md it prints nothing (not ready)",
     smallest_fix: "Either replace the command with the per-line form above ('one line per question; each line inside its budget') or add to the known limits: 'reads only the first Shown line; a packet with several questions: count each Shown line'."}
  - {id: R3, class: recommendation, check: "C7 (example vs rule) + C8 V1/V10",
     where: "briefs-and-handoffs.md:61-103 (§7 direction brief example)",
     expected: "The one worked brief carries what the same file's §1 and SKILL §14 lines 7-8 require for visual work: stop criteria, display sizes, budget; and the Roblox docs pointer SKILL §10 requires of every brief (SKILL.md:97). An image cap above the partner's default states its reason (reference-images SKILL.md:49 and references/rounds.md:77: R1 rough round 'at most 6 including regenerations'; owner light-check rule J005-D8)",
     observed: "No stop criteria line (refs say 'take: the four lines, sell list, budget'); no display sizes; no docs-map rows; `image_cap: 9 per round, 2 rounds` with no reason. A lead copying the example fails its own §14 line 7 and line 8 and raises the image-model batch by half",
     evidence: "BH:16-17 (rows), :76-84 (example refs and fixed); SKILL.md:97, :137-138; reference-images/SKILL.md:49; rounds.md:77",
     smallest_fix: "In the example: refs comment 'take: the four lines, sell list, stop criteria, budget'; fixed: `display_sizes: game camera on a phone, inventory icon, shop card   # game profile`, `stop: the success test reads in the grey and colour roughs at phone size; notes repeat   # job card`, `image_cap: 6 per round incl. regenerations, 2 rounds   # reference-images rounds §7`; refs: `knowledge/reference/roblox/docs-map.md   # take: art-director rows`."}
  - {id: R4, class: recommendation, check: "C8 V7 (rev1 R2, partly declined with a reason)",
     where: "SKILL.md:129 (§14 starts at byte 20,186; §15 at 23,293; total 28,848)",
     expected: "Steps, rules and self-check inside roughly the first 18 KB",
     observed: "§14 still sits about 2 KB past the window. Mitigated by SKILL.md:10 (re-read §8, §14, §15 after a compaction) and the harness re-load. The maker's reason covers only moving §9; text inside §1-§13 can move to the references with every heading and number kept, which renumbers nothing",
     evidence: "byte offsets of the ## headings (script); coverage/orchestration.md:218",
     smallest_fix: "Move about 2.2 KB of detail behind pointers, keeping each heading: the Mixed-request and Unclear rows' detail of §2 (about 0.9 KB) and the code-brief and effort bullets of §10 (about 0.6 KB) to BH; the §11 helper table (about 0.8 KB) to a references/models.md row in 'Read this file when'."}
  - {id: R5, class: recommendation, check: "C8 V3/V14 (known limits of screening aids)",
     where: "briefs-and-handoffs.md:58 (hook known false passes); gates-and-feedback.md:12 (taste grep)",
     expected: "Every silent pass of a screening aid is listed",
     observed: "(a) A 0-byte payload file (for example a failed `json.dumps` redirect) gives no stdout, no stderr, exit 0: a silent pass, not in the list (the hook treats empty stdin as 'nothing to judge', handback_check.py:59-61). (b) `prefer\\?` misses the common 'Which do you prefer, A or B?'",
     evidence: "Reviewer runs: h_empty.json → no output, exit 0; t_bad.md: 7 of 9 wordings hit; the misses are 'Happy with this?' (already listed) and 'Which do you prefer, A or B?' (not listed)",
     smallest_fix: "BH:58 known false passes: add 'an empty payload file (check the file is not empty)'. GF:12: use `prefer` instead of `prefer\\?`, or add 'Which do you prefer, A or B?' to the misses."}
  - {id: R6, class: recommendation, check: "C1 (row wording) + C7",
     where: "coverage/orchestration.md:68 (PI-06) and :52 (GD-22); SKILL.md:13 (constraints of the four lines), BH:10",
     expected: "A coverage row quotes text the book carries; GD-22's parameter list (camera, screen size, player count, session pace, input) reaches the constraints line",
     observed: "PI-06 cites 'S §5.3 (the proof is the whole job at rough finish)': that text is not in SKILL.md (§5.3 says 'cheap ... nothing polished'); the substance holds through §5.3, §6 rough-first and §15 row 4, so the row passes. GD-22: the constraints line names camera, device, budget, platform rules, locks; player count and input are missing, and the game profile has no field for them",
     evidence: "SKILL.md:13, :56, :153; BH:10; game-profile.md:15-30",
     smallest_fix: "Coverage PI-06: quote the real text. SKILL.md:13 constraints: '(camera, device and input, player count, budget, platform rules, locks)'."}
  - {id: R7, class: recommendation, check: "C8 V6 + C3",
     where: "SKILL.md:62 and BH:32 (retime rule); SKILL.md:138 (§14 line 8) vs BH:44 (Effect row)",
     expected: "One rule, one place; the per-type self-check line names every row of BH §4",
     observed: "'A retime is a contract change ... VFX and sound ... the same turn' is written in both SKILL §6 and BH §3 (consistent now, will drift). §14 line 8 lists every BH §4 row except Effect (importance tier, play rate and worst-case count, marker names)",
     evidence: "the lines named",
     smallest_fix: "SKILL.md:62: 'A retime is a contract change (`references/briefs-and-handoffs.md` §3).' §14 line 8: add 'the importance tier, play rate and marker names (effect)'."}
keep: [
  every rev1 keep item is unchanged: the four lines (SKILL §1.1, §10, BH §1), the ordered one-screen packet (SKILL §8) and the per-gate table (GF §2), the input-proof table and owner-confirmed feel and listening lines, closed doors with 'may return only if', the owner-note steps (GF §5), one marker list pointed to game-timing §4, done on evidence, the two-round restart, nothing from df13ff4 dropped,
  the rev1 F2 fix (GF §5 step 8): the owner's note stands; agents never overrule it; reviewer-vs-reviewer ties stay with the decision owner except gate picks; matches AGENTS.md §0 and company.md §3,
  the rev1 F3 fix: one runnable §14 line 8 for the per-type card and brief items, with ledger dates as input,
  the Shown line as the thing the image budget counts, with the whole-file grep labelled a ceiling and an eye check before sending (GF §2),
  the weakest part of the recommendation in every packet (SKILL §8 item 4, §15 row 16),
  the D1 split between look-owning leads (options package) and constraint owners (fix only F1's list),
  the closed-door reading rule (history vs files after the gate; avoid lists one item per line),
  the hook payload built with json.dumps and the stderr line read as 'not read'
  ]
verdict: fix-first
</spec>
```

One blocking finding (F1), a one-sentence fix. Everything else is a recommendation.

## Check results
| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass | 79 of 79 orchestrator-tagged findings have a row (script vs matrix.md); every landed-in location opened against the extracted principle/apply/check text; all 79 rules and their lead-runnable checks are carried (§14 line numbers in the table match the file); 4 rejections (PP-06, PP-08, SD-29, SD-31) sound: craft method the lead must not prescribe; 11 untagged rows correct. Wording notes in R6 (PI-06 quote, GD-22 parameters) do not fail a row. Rows checked 79, failed 0 |
| C2 core principles | pass | SKILL §15 in the skill the lead loads first; UP-13..UP-18 (the master's orchestrator rows) present with example and check; UP-1-4, 6-8, 10, 11, 19, 20 in lead terms; 5, 9, 12 routed with a reason; row 16 now has 'say our own weak spots'; row 20 flash rate (over 3 per second blocks) matches UP-20; no contradiction |
| C3 self-review | pass | rev1 F3 closed (§14 line 8); every line names its input; the image count is by eye on the Shown line. R7 (Effect row missing from line 8) is minor |
| C4 kit rules and engine | fail | F1 (progression-designer under the engineering no-menu rule). F2 of rev1 fixed (AGENTS.md §0, company.md §3). Owner-asked gate (GF:78), extra-gate rule, G1 counts (company.md §2) consistent. No engine claims added. All cross-references resolve (reference-images §4 step text at SKILL.md:56 of that skill, animation-design §3 step 6, game-timing §4, S-133, G-19, feedback-briefs §6, preproduction handoffs §2, templates/anim/timing-list.md, J005-D8 in company.md §7, claude.md Peer message row) |
| C5 nothing valuable lost | pass | Every df13ff4 line kept, sharpened or moved; the 2.1.306 message fact moved to rules/assistants/claude.md, which holds it with the resend cost; matches coverage table c and its round-1 addendum |
| C6 fixed rules | pass | Only SKILL.md modified plus the two new references in this skill; job-types.md and evals/ no diff; no orchestrator role file; frontmatter byte-identical to df13ff4 (description 277 chars); 183 lines; §1-§14 and their numbered steps not renumbered, §15 appended; J018 phrase in all three headers; no Riot, library IDs, transcript lines or game names in bodies (scan); no tips section |
| C7 better work | better, with fixes | see below; F1, R1, R3 |
| C8 brief v2/v3 | fail | V10: F1. V3/V12/V14: R1, R2, R5 (aids with eye checks; my runs reproduce the maker's numbers on the cases the book names). V1: R3 (example cap). V2: hook mode real (docstring); no other tool mode named. V4: only the rejected-request capture, consistent with game-design G-19 and networking-security. V6: R7. V7: R4. V8: findings became card items, brief asks, packet lines and §14 checks. V11: no other role's row targets SKILL, GF or BH (grep of proposals/); job-types and workflow rows collected for G3 in coverage d. V13: no measure longer than one command line |

## Earlier findings (rev1)
| Rev1 id | Now |
| --- | --- |
| F1 image count on evidence paths | fixed: Shown line counted; ceiling grep labelled; eye check (GF:21-23, SKILL:133). New edge cases R1, R2 |
| F2 conflicting notes vs owner | fixed (GF:72, SKILL:79) |
| F3 per-type items unchecked | fixed (SKILL:138); R7 minor gap |
| R1 uniform D1 demands | fixed (SKILL:47, GF:17), but the constraint-owner list introduced F1 |
| R2 V7 window | open, partly declined (R4) |
| R3 duplication | fixed for the named rules; retime rule left in two places (R7) |
| R4 taste grep | fixed; one miss left (R5) |
| R5 closed-door reading | fixed (GF:62) |
| R6 hook stderr | fixed (BH:58); empty file left (R5) |
| R7 naming rule prerequisite | fixed (SKILL:40, proposal row) |
| R8 previews in budget | fixed (GF:21) |
| R9 G1 example | fixed (GF:92); Shown placement R1 |
| R10 retime example | fixed (GF:98) |
| R11 owner-asked gate | fixed (GF:78) |
| R12 one closed-doors table | fixed (proposals:17) |
| R13 weakest part | fixed (SKILL:77, :132, :162) |

## Better work (C7)
Read as the lead at the start of eval E-01 (sound brief for the fireball hit) and a pet-companion character job (L). Against df13ff4 the lead now opens with problem, constraints, target experience and success test; sizes multi-form characters correctly; sends look-owning leads for research, a warm-up set aside, one radical and equal-finish options, and constraint owners for limits; asks one goal question with the card's goal word; names its weakest part; counts only the images the owner must look at; closes doors and keeps them out of later briefs; turns owner notes into one-problem repair briefs by layer; treats a retime as a contract change; and says "done" only with evidence. For E-01 the brief also carries the marker name and points to the one sync rule. That is clearly better work and fewer wasted rounds. Weak spots: the D1 rule as written takes the option choice away from the progression-designer (F1); the only worked brief lacks stop criteria, display sizes and a docs pointer, so copying it fails the book's own check (R3); the worked G1 example writes the Shown line in a form its own count rejects (R1); the self-check still sits past the compaction window (R4).
