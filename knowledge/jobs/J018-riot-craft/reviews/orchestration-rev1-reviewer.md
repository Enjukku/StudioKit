---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer orchestration · claude-opus-5-5 · high · 2026-10-22

# Review: orchestration books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/orchestration/SKILL.md (183 lines) + references/gates-and-feedback.md (new) + references/briefs-and-handoffs.md (new), working tree on top of df13ff4, 2026-10-22. Not in scope: references/job-types.md (proposal-only, J018-D2 point 4), evals/.
reviewer: J018 reviewer orchestration (opus, high)
looked_at_first: [
  the three book files read in full, then git show df13ff4:.agents/skills/orchestration/SKILL.md (143 lines, the only old file besides job-types.md and evals) and git diff df13ff4, line by line,
  binding context: AGENTS.md, rules/company.md (all), rules/messages.md (all), rules/owner-profile.md, references/job-types.md (read-only, for consistency), rig-pipeline §1, reference-images §4, animation-design §3 step 6 + references/game-timing.md §4 + references/review.md §1 item 5 and §5, sound-design SKILL S-133, game-design G-19, art-review/references/feedback-briefs.md §6, templates/jobs/, knowledge/design/game-profile.md, J005-D8,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20 incl. every "applies to" list), matrix.md (orchestrator column extracted by script: 79 IDs) and the principle/apply/check/mistake text of all 79 findings,
  tools: tools/hooks/handback_check.py (source, docstring) + tools/hooks/README.md, tools/kb_index.py --help, tools/art/thumb_check.py icon --help, J018 tool-modes.md,
  my own V3 runs (scratch .../scratchpad/rev_orch/): GF §1 taste grep on a synthetic bad packet ("What do you think?", "Any thoughts on these?", "Which one do you prefer?"), a second bad packet ("Do you like option A?", "Thoughts?") and a good packet; GF §2 image grep on a synthetic G1 packet with one shown image and five evidence or rejected-image paths, and on the real J009 direction-packets.md and J018 g1-packet.md; GF §4 closed-door grep on a synthetic job folder (decisions.md row, origin proposal, inline avoid, multi-line avoid, a re-proposal); BH §6 hook on three payloads (well-formed, no STATUS, hand-written JSON with a raw newline),
  evals/briefs.md E-01..E-05 read as the lead at the start of a job
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3/V12 + C3 (lead severity rule: wrong number, no error, common case the book prescribes, no eye check)",
     where: ".agents/skills/orchestration/references/gates-and-feedback.md:21 (image budget screening aid); used by SKILL.md:133-134 (§14 lines 2-3: 'greps: references/gates-and-feedback.md §1-2', 'image count inside the budget')",
     expected: "The count measures what the budget limits: the images the owner is asked to look at (option sheet, at most one diagnostic image per failing number, at most 6 key stills). The same line says 'Everything else goes as numbers with their file paths', so evidence paths must not count, and a reading the book feeds into a self-check needs its known false readings and an eye check (V14)",
     observed: "`grep -o -i -E \"\\.(png|jpe?g|webp)\\b\" <packet.md> | wc -l` counts every PNG/JPG/WEBP name in the file: every evidence path the book itself prescribes next to a number, every rejected-image path, every log row. Known limits list only the contact sheet and images sent outside the file; no eye check is named",
     evidence: "Reviewer run: synthetic G1 packet with one shown image (`captures/option-sheet.png`) plus four check rows naming their input capture and one rejected-image path: grep prints 6 (true count 1). Real input form: J009 direction-packets.md prints 24, but it shows one 'look first' image (`side-by-side.png`, line 15); the other 23 are evidence, grayscale, thumb and `_rejected/` paths (lines 34-109). The maker's R2 run read 24 as 'matching their links'",
     smallest_fix: "Replace the line with: 'Screening aid: `grep -n -o -i -E \"\\.(png|jpe?g|webp)\\b\" <packet.md>` lists every image name in the packet, including the evidence paths next to numbers, rejected images and log rows; it is a ceiling, not the count. Count by eye only the images the owner is asked to look at (the artifact, the option sheet, each diagnostic still) against the budget. A contact sheet counts as one; images sent outside the file are not listed.'"}
  - {id: F2, class: blocking, check: "C4 (AGENTS.md §0 priority 1; rules/company.md §1, §3)",
     where: ".agents/skills/orchestration/references/gates-and-feedback.md:73 (§5 step 8)",
     expected: "AGENTS.md §0: the owner, in chat, always wins. company.md §1: the owner owns taste and every gate answer; §3: a reviewer's dissent is information, not a veto (unless inside its authority); taste ties between options that all meet the goal: the decision owner decides; SKILL.md:50 'A tie is not by itself a reason to ask the owner'",
     observed: "'Conflicting notes (the owner and a reviewer, or two reviewers) are never averaged: the decision owner (rules/company.md §3) decides; taste goes to the owner with both readings shown at the same camera.' For an owner-vs-reviewer conflict this tells the lead that the decision owner (for a silhouette note: the art-director) decides, i.e. an agent may overrule an owner note. For a reviewer-vs-reviewer taste tie it sends the tie to the owner, against company.md §3 and SKILL §4.4",
     evidence: "AGENTS.md §0 table row 1; rules/company.md:10, :52-54; SKILL.md:50; GF:73",
     smallest_fix: "Split the sentence: 'Owner vs reviewer: the owner's note stands; when the reviewer has evidence the note breaks the goal, a safety or comfort rule or a platform rule, put both readings at the same camera in the digest and let the owner choose. Two reviewers: the decision owner decides (rules/company.md §3); a tie where every option meets the goal stays with the decision owner, unless it is a gate pick (the owner picks at gates).'"}
  - {id: F3, class: blocking, check: "C3 + C1 (check half of 17 rows)",
     where: ".agents/skills/orchestration/SKILL.md:130-143 (§14 self-check) vs references/briefs-and-handoffs.md:14-15 (sell list, display sizes) and :36-48 (§4 per-type card and brief items)",
     expected: "Every checkable finding for the lead has a self-review line it can run. These rows' library checks are file checks the lead can run itself: the art brief cites the grey-box play-test verdict (GD-15); the lighting pass is dated after the last route change (PP-26); every screen and state is listed before style (UI-05, UI-01); the brief has the sell list, the role and the display sizes (CD-02, GD-18, MD-02); every state change has a cue or a reason (SD-01); the floor-material list exists (SD-23); a mode change has a balance re-check list (GD-19); the ranked environment list exists (WL-06); the marketing kit is planned at the start and names the launched thing as hero (PP-32, RI-04); a theme library exists before character work (RI-06); a live update card names its data, audience and differentiator (GD-20, SI-05, SI-12)",
     observed: "These rules land only as rows of the BH §1 and §4 tables. No §14 line points to them: line 7 checks 'the four lines, the target-experience line, budget and stop criteria, every rule, skills, sourced fixed values, inputs with revisions, consumers' needs', not the per-type items. In a feature job the lead can send the art brief before a grey-box verdict, or the stage light brief before the last route change, and its self-check passes. The coverage file's V5 statement lists only the rows that have §14 lines",
     evidence: "SKILL.md:130-143; BH:14-15, :36-48; coverage/orchestration.md:24, 48-51, 54, 60, 64, 78, 80, 89-90, 97-100, 102 (all 'As: standard', no self-review)",
     smallest_fix: "Add one §14 line: '- [ ] The card and briefs carry the job type's items (`references/briefs-and-handoffs.md` §1, §4) before the briefs that depend on them: sell list and display sizes (visual work); grey-box verdict cited in any production art brief (feature); light brief dated after the last route change (stage); every screen and state listed before style (UI); cue list per state change (sound); data, audience and differentiator (live update) [job card, briefs, ledger dates].'"}
  - {id: R1, class: recommendation, check: "C7 + C4 (rules/owner-profile.md:16, job-types.md direction-lead rows)",
     where: "SKILL.md:47 (§4.1 'Each returns: a research board; hooks ...; 2-3 options ...'), gates-and-feedback.md:17 (G1 row 'One option sheet')",
     expected: "Each direction lead returns what its recipe row names (job-types.md:22, 38, 55, 69, 82, 95, 107: e.g. architect 'runtime choice, camera ownership ...', performance-engineer 'budget'); option demands sit with the leads that own a look or an approach; owner-profile: 'Do not offer option menus for technical choices'",
     observed: "§4.1 asks every direction lead (architect, performance-engineer, progression-designer included) for a research board, hooks with a warm-up and a radical, and 2-3 options as pictures; the G1 row assumes an option sheet, while the feature recipe's G1 shows 'the behaviour in player words, the risky claims'. Briefing the architect or the performance-engineer this way wastes a pass and invites technical option menus into the packet",
     evidence: "SKILL.md:47; GF:17; job-types.md:82-83; owner-profile.md:16",
     smallest_fix: "§4.1: 'Each returns what its recipe row names; leads that own a look or an approach (the recipe's pictured options) add a research board, hooks ..., 2-3 options ...; constraint owners return limits, needs and one recommendation.' GF:17: 'where the recipe shows pictured options'."}
  - {id: R2, class: recommendation, check: "C8 V7",
     where: "SKILL.md:130-143 (§14 self-check starts at character 19,804 of 27,309; §15 at 21,960)",
     expected: "Steps, rules and self-check inside roughly the first 5,000 tokens (about 18 KB)",
     observed: "§14 sits just past the window. Mitigated: SKILL.md:10 says to re-load the skill and re-read §8, §14, §15 after a compaction, and the harness profile re-loads `orchestration` after compaction. The duplicated text in R3 is the cheapest place to win the space back",
     evidence: "byte offsets of the ## headings (script); old SKILL.md 16,668 bytes",
     smallest_fix: "Trim the restatements listed in R3 from §6 and §8 (point to GF instead), which moves §14 under about 18 KB."}
  - {id: R3, class: recommendation, check: "C8 V6",
     where: "'No grand reveals': SKILL.md:61, :80, :135 and GF:75-79; 'additions are tickets': SKILL.md:63, BH:52, GF:84; 'one owner per file': SKILL.md:64, BH:54; the packet's check items: SKILL.md:77 item (6) and GF:23-29",
     expected: "One rule, one place; other places point to it",
     observed: "Each rule is restated in 2-4 places in slightly different words (for example SKILL §8 item (6) and GF §2 'Every packet carries' both list read-feel-look order, labels, stand-ins, could-not-check, owner-confirmed lines). Not yet contradictory, but they will drift",
     evidence: "the lines named",
     smallest_fix: "Keep the rule in SKILL (or in GF for the packet details) and replace the other copies with a one-line pointer."}
  - {id: R4, class: recommendation, check: "C8 V3/V14 (screening aid with eye check: not blocking)",
     where: "gates-and-feedback.md:12",
     expected: "The taste-question grep catches the common forms and lists them as known limits",
     observed: "`do you like|like it\\?|thoughts\\?` misses 'What do you think?' and 'Any thoughts on these?' (only a bare 'thoughts?' matches); the known-limits text names other misses but not these, the most common ones",
     evidence: "Reviewer run: packet with 'What do you think?', 'Any thoughts on these?', 'Which one do you prefer?' → no hit, exit 1; packet with 'Do you like option A?', 'Thoughts?' → 2 hits, exit 0",
     smallest_fix: "Pattern `do you like|like it\\?|thoughts|what do you think|prefer\\?`; add 'what do you think' to the known limits if kept out."}
  - {id: R5, class: recommendation, check: "C8 V3/V14",
     where: "gates-and-feedback.md:63",
     expected: "The reading rule matches what the grep lists",
     observed: "'A mention on an avoid: line is correct; any other line is a re-proposal' also flags the door's own row in decisions.md, the gate packet, the D1 proposal that first offered it, and an avoid list written one item per line",
     evidence: "Reviewer run on a synthetic job folder: 5 hits; only T05 is a re-proposal; decisions.md:4, the origin proposal and a multi-line `avoid:` item (T04.md:2) would be labelled re-proposals by the rule",
     smallest_fix: "Add: 'The door's own decisions.md row, the gate packet and the proposals written before the gate are history; read only files written after the gate; an avoid list written one item per line is also correct.'"}
  - {id: R6, class: recommendation, check: "C8 V3",
     where: "briefs-and-handoffs.md:59",
     expected: "Every way the hook reads as a pass without judging is listed",
     observed: "'no output means it passed'; a hand-written payload.json that holds the hand-back text with raw newlines is invalid JSON: the hook prints `handback_check: JSONDecodeError ...` on stderr, nothing on stdout, exit 0",
     evidence: "Reviewer run: p_raw.json → stderr line only, exit 0; with stderr hidden, no output at all",
     smallest_fix: "Add: 'A `handback_check:` line on stderr means the payload was not read: not a pass. Build the payload with `json.dumps`.'"}
  - {id: R7, class: recommendation, check: "C4 / C7",
     where: "SKILL.md:40 (§3.1 'game-profile.md filled, with naming and folder rules'), BH:55",
     expected: "A prerequisite the lead can check against a real field",
     observed: "knowledge/design/game-profile.md has no naming or folder field, so every first M or L job in a game stops on a prerequisite with no template; no proposal row asks for the field",
     evidence: "game-profile.md:15-30",
     smallest_fix: "Add a proposals/orchestration.md row: game-profile field 'Asset naming and folder rules (link)'; in §3.1 say what minimum counts (or 'for jobs that create assets')."}
  - {id: R8, class: recommendation, check: "C8 V1/V10",
     where: "gates-and-feedback.md:18 (G2 row: two timing takes as playable previews) vs :21 ('plus the playable preview')",
     expected: "The budget names every preview the packet carries; animation-design references/review.md §1 item 5 puts both previews into the gate packet",
     observed: "The budget allows one playable preview while the G2 row asks for two per signature, tell or emote clip",
     evidence: "GF:18, :21; animation-design/references/review.md §1 item 5",
     smallest_fix: "GF:21: 'plus the playable previews (one per take the owner picks between)'."}
  - {id: R9, class: recommendation, check: "C7 (worked example vs recipe)",
     where: "gates-and-feedback.md:93 (§8.1, packet (1) 'the option sheet A-C at the spawn camera' and (6) 'MCP-verified: grey captures')",
     expected: "At G1 a character job shows pictured directions (reference images); the Studio blockout at the game camera is the G2 proof (job-types.md:39, :42); company.md §2 'No expensive work before the owner's yes'",
     observed: "The example implies three Studio-captured grey pets before G1; a lead copying it would order 3D work for every option before the pick",
     evidence: "GF:93; job-types.md:39, :42; company.md:30",
     smallest_fix: "(1) 'the option sheet A-C (reference images, grey beside colour, placed on a spawn-camera capture at phone size)'; (6) 'grayscale and phone-size reads of the images; not verified at the game camera until the G2 blockout'."}
  - {id: R10, class: recommendation, check: "C7 (example vs rule)",
     where: "gates-and-feedback.md:99 (§8.3 retime in production, L job) vs SKILL.md:57 ('After G2 ... timing beats change only by a new owner decision')",
     expected: "The example says why this retime needs no owner decision",
     observed: "A wind-up change after G2 with no owner line reads as an exception to §5.4",
     evidence: "GF:99; SKILL.md:57",
     smallest_fix: "Add: 'The change stays inside the window approved at G2, so it is a tuning change, not a beat change; outside it, the digest gets the change first.'"}
  - {id: R11, class: recommendation, check: "C4 (AGENTS.md §0)",
     where: "gates-and-feedback.md:79",
     expected: "The owner can always ask for a gate",
     observed: "'When the owner wants to see more often, give status pictures, not extra gates' can be read as refusing an owner request",
     evidence: "GF:79; company.md:33",
     smallest_fix: "Append: 'unless the owner asks for a gate'."}
  - {id: R12, class: recommendation, check: "C8 V6 (proposal)",
     where: "proposals/orchestration.md:17",
     expected: "One closed-doors record per job (GF §4 puts it in decisions.md)",
     observed: "The row also adds a Closed doors table to templates/jobs/direction-sheet.md: two records of one fact",
     evidence: "proposals/orchestration.md:17; GF:52",
     smallest_fix: "Direction-sheet template: a line that points to the decisions.md table, not a second table."}
  - {id: R13, class: recommendation, check: "C2 (nothing important missing)",
     where: "SKILL.md:162 (§15 row 16), :77 (packet item 4); rows 11, 13, 16 checks have no [input]",
     expected: "UP-16 includes 'report your own weaknesses honestly'; the lead's honest recap reaches the owner at each gate, not only at close (SKILL.md:91)",
     observed: "Row 16 covers goal, one problem, layer; the packet has no 'weakest part' line, so the honest recap appears only in the close-out retrospective",
     evidence: "universal-principles.md UP-16 principle and general check; SKILL.md:77, :91, :162",
     smallest_fix: "Packet item (4): add 'the recommended option's weakest part'; add the input bracket to the checks of rows 11, 13 and 16."}
keep: [
  the four lines before sizing (SKILL §1.1) and in every brief (§10, BH §1 with its worked pet example),
  the ordered one-screen gate packet (SKILL §8) and the per-gate table with what each gate closes (GF §2),
  'what each input can prove' table and the owner-confirmed feel and listening lines (GF §2),
  closed doors with 'may return only if', carried into `avoid` (SKILL §1.5, §8; GF §4),
  owner notes: problem behind the note, goal or tactic, layer, one problem per repair brief, 'not happy may mean not done', fix accepted in the same capture (GF §5, example 8.2),
  the D1 return (research, warm-up, radical, equal finish, play value and cost, needs from other crafts) for the look-owning leads,
  one marker list as the timing contract, pointed to game-timing §4, never restated (BH §3),
  done on evidence, pending said as pending, rejected-request capture (SKILL §12-13),
  an approach that failed two rounds restarts at its cheapest stage (SKILL §7.3),
  the BH §7 direction brief example (complete against rules/messages.md §2 and §9),
  nothing from df13ff4 was dropped (C5)
  ]
verdict: fix-first
</spec>
```

## Check results
| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (check half) | 79 of 79 tagged findings have a row (script vs matrix.md); every landed-in location opened; all 79 rules are carried. 17 rows lack the lead-runnable check (F3). 4 rejections (PP-06, PP-08, SD-29, SD-31) are sound: craft method the lead must not prescribe. 11 untagged rows read: correct |
| C2 core principles | pass | SKILL §15 in the skill loaded first; UP-13..UP-18 (the master's orchestrator rows) all present, plus 1-4, 6-8, 10, 11, 19, 20 in lead terms; 5, 9, 12 routed with a reason; no contradiction found (flash rule 3 per second matches UP-20). R13 |
| C3 self-review | fail | F3 (per-type items unchecked); F1 (image count line runs on a wrong number) |
| C4 kit rules and engine | fail | F2 (conflicting-notes rule vs AGENTS §0 and company §3). No engine claims added; icon 150x150 matches thumb_check. R1, R7, R11 |
| C5 nothing valuable lost | pass | every old line of SKILL.md (df13ff4) is kept, sharpened or moved; matches coverage table c |
| C6 fixed rules | pass | only the books in scope changed (job-types.md, evals/, rules/, workflows, templates, tools unchanged since df13ff4); no orchestrator role file; 183 lines; description unchanged (277 chars); §1-§14 not renumbered, §15 appended; J018 phrase in all three headers; no "Riot", library IDs, transcript lines or game names in bodies; no tips section; LF endings |
| C7 better work | better, with fixes | see judgment below; R1, R9, R10 |
| C8 brief v2/v3 | fail | V3/V12: F1 (blocking), R4-R6 (screening aids with eye checks or listed limits). V1: R8. V2: all modes real (hook docstring, kb_index --help). V4: no money, saves or remotes rule restated beyond the rejected-request capture (matches networking-security and game-design G-19). V6: R3, R12. V7: R2. V8: findings became card items, brief asks and packet checks. V10: marker list, sync rule and attempt/outcome rule pointed to partner books, consistent. V11: other roles' rows adopted in part or declined with reasons; wave-3 rows (architect, qa-lead, level-design, live-ops, feature-builder, reviewer, reference-images) were written in parallel and target only job-types.md or other books |

## Better work (C7)
Read as the lead at the start of a pet-companion character job (L) and against eval E-01 and E-03. With the old books the lead would size the job, open a card with the owner's words and send direction briefs asking for "2-3 reference images or rough options"; the G1 packet would be "the artifact first, the decision in one sentence". With the new books the card opens with problem, constraints, target experience and success test; D1 asks for research, a set-aside warm-up, a radical option and equal finish; the G1 packet is ordered (artifact as players meet it, one goal question with the card's goal word, options with play value and cost, rejection reasons, closed doors); owner notes are turned into one-problem repair briefs by layer; retimes are contract changes; "done" waits for evidence. That is clearly better work and fewer wasted rounds. Weak spots: the image-count aid gives a wrong number on the real packet form (F1); the conflicting-notes line can let an agent overrule the owner (F2); the per-type items, which carry most of the craft-specific value, have no self-check (F3); D1 demands are uniform for constraint leads (R1); the book grew from 16.7 KB to 27.3 KB, partly through restatement (R2, R3).
