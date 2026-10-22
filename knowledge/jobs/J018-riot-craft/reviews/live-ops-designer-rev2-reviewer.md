---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer live-ops-designer · claude-opus-5-5 · high · 2026-10-22

# Review: live-ops-designer books, round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/live-ops-designer.md (body) + .agents/skills/live-ops-design/ (SKILL.md, references/) + .agents/skills/live-ops-craft/ (SKILL.md, references/ incl. event-review.md; evals/ not reviewed), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer live-ops-designer (opus, high)
looked_at_first: [
  every book file read in full as it is now (role body, both SKILL.md, process.md, handoffs.md, feedback-ops.md, event-review.md) and git diff df13ff4 of all 10 changed files plus the old role body and old design SKILL in full,
  reviews/live-ops-designer-rev1-reviewer.md (F1, F2, R1-R7 re-checked one by one),
  knowledge/reference/craft/riot/matrix.md (live-ops column extracted by script: 36 findings) and the principle, apply, check and roblox_fit lines of all 36 in the topic files,
  universal-principles.md (UP-01..UP-20; the eight that list live-ops-designer read in full),
  partner books read-only: platform-policy/references/rules.md §A, progression-design/references/reward-tiers.md §6 and §8, game-design/references/systems-economy.md §8-§9 headings, marketing-design SKILL M-15, M-22, M-23, marketing-craft/references/ (image-review.md exists), art-review/references/art-bible.md:79, progression-designer and marketing role lines that name live-ops, templates/live-ops/event-design.md and update-plan.md,
  docs mirror: production/game-design/liveops-planning.md:53-55 and :65, content-updates.md:34, GuiService.yaml (ReducedMotionEnabled),
  tools/liveops/feedback_count.py (full source, --help, count --help, validate --help) and tools/liveops/README.md,
  my own V3 runs (scratch: <scratchpad>/lo-rev2/): validate on 31 synthetic items (exit 0); count with --end 2026-10-27 / 2026-10-28 / 2026-11-04 on a file that also holds the next week; a theme with 22 messages from 10 authors (4 authors x 4, 6 singles); anon- review rows; one urgent support item; the book's exact command form `--out sorts/counts-<date>.md` run from a copy of the repo layout,
  live-ops-craft/evals/briefs.md E1-E5 (E2 and E4 walked with the new books)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: R1, class: recommendation, check: C7 + C8 V6,
     where: ".agents/skills/live-ops-craft/SKILL.md:37 (step 8c 'the activity's grey-box verdict before any art brief'); references/event-review.md:12 (game-designer row 'before any art brief'); references/handoffs.md:114 (game-designer rule 'before any art brief')",
     expected: "One order for the art brief and the grey box. The same books brief the art director at the concept round, before the grey box: event-review.md:14 (art-director 'concept round (before any production art)'), handoffs.md:16 (art-director 'the concept round ... before any production art'), role :37 and both self-checks ('before any production art brief')",
     observed: "Three lines say 'before any art brief'; read literally they hold back the art director's concept-round brief (theme niche, anchors, theme rough) until the activity is proven, which contradicts the art-director row and step 8a",
     evidence: "grep 'before any art brief' vs 'production art brief' over the books: 3 vs 4 hits, lines as listed",
     smallest_fix: "In the three lines write 'before any production art brief' (the theme rough at the concept round is not production art)"}
  - {id: R2, class: recommendation, check: C8 V3 + V12 + V14; C4,
     where: ".agents/skills/live-ops-craft/references/feedback-ops.md:36 (step 7 command `--out <sorts/counts-<date>.md>`) with :14 (new: item_id taken from the export's own message or row id); references/event-review.md:79 (worked example count file `sorts/counts-2026-10-20.md`); feedback-ops.md:60 (several loud authors row)",
     expected: "The command, run in the exact form the book names, writes where the book says the file lives (`FEEDBACK_DATA_DIR/sorts/`, gitignored; feedback-ops.md:6 'Player text and ids never enter git')",
     observed: "(a) The tool resolves an items path that does not exist against FEEDBACK_DATA_DIR, but writes --out relative to the working directory. Run from the repo root, `--out sorts/counts-<date>.md` creates `<repo>/sorts/counts-<date>.md`, outside .gitignore, with no warning. The file holds no author keys, but its §B lists urgent item_ids, which J018's new rule (:14) makes the platform's own message ids. The command line is older than J018, but the maker re-edited this exact line under V12. (b) The new 'several loud authors' row triggers at 'about 3 messages per author'; a theme with 22 messages from 10 authors, 16 of them from 4 authors (2.2 per author), passes under it with no flag. The distinct-author count stays correct, so this is a known limit, not a wrong decision number",
     evidence: "Reviewer run in a copy of the layout: `python tools/liveops/feedback_count.py count items/week.jsonl --start 2026-10-21 --end 2026-10-28 --out sorts/counts-2026-10-28.md` read `.tools/feedback-data/items/week.jsonl` and wrote `./sorts/counts-2026-10-28.md` (§B lists the urgent id); source: feedback_count.py:128-132 (resolve for items only) and :354-356 (--out as given); .gitignore has `.tools/` and no `sorts/`. Same file, --end 2026-10-28: 'veterans.no-goals | discord | 10 / 13 | 76.9 % | 22 |' with an empty flag cell",
     smallest_fix: "(a) feedback-ops.md:36: write the out path as `--out \"$FEEDBACK_DATA_DIR/sorts/counts-<date>.md\"` (default `.tools/feedback-data/sorts/`) and add a §4 row: 'a relative --out path | written relative to the working directory, not the data dir, no warning | always give the full data-dir path; check the file landed under .tools/'. (b) Extend the §4 'several loud authors' row with 'a few heavy authors among many single posters (16 of 22 messages from 4 of 10) stays under the 3-per-author mark: read the spread on any theme whose messages exceed its authors by half or more'; add (g) '--out relative to the data dir' to proposals row 5"}
  - {id: R3, class: recommendation, check: C1 + C3,
     where: "coverage rows CD-13, SI-05, SI-12, GD-20 (coverage live-ops-designer.md:28, :53, :55, :38); books: process.md:49 (brief lines), craft SKILL.md:37 (one-pager fields), :71 (self-check C concept round), event-review.md:51 (E-01)",
     expected: "Each finding's own check, where the live-ops agent can run it on its inputs. CD-13: 'the final pose capture still reads heroic or aspirational'; SI-05: 'the output shows the fan-expected trait at its strongest'; SI-12: 'side-by-side ... the new theme and its nearest existing one: a fresh agent tells them apart'; GD-20: 'each theme pitch lists its data and source themes'",
     observed: "The rule and the brief line land for all four, and self-check C confirms the line is written. The output-level half is not checked anywhere the agent runs: no E line or concept-round check looks at tone and appeal, at the fans-want trait in the captures, or at the theme rough next to the nearest theme; the one-pager fields (craft :37) and self-check D carry 'what fans want with its counts' but not the proven themes combined and the maturity (only the ranking rule process.md:45 and L-20 say it)",
     evidence: "event-review.md:51-69 (E-01..E-19 inputs and pass conditions); craft SKILL.md:37, :71; design SKILL.md:90",
     smallest_fix: "E-01 pass: add 'the fans-want trait shows at its strongest; the tone matches the brief's tone shift and the subject keeps its appeal'. Craft :71 (concept round): add 'the picked theme rough sits next to the nearest existing theme: a cold read tells them apart'. Craft :37 one-pager fields: add 'the proven themes it combines and the maturity it keeps'"}
  - {id: R4, class: recommendation, check: C7,
     where: ".agents/skills/live-ops-craft/SKILL.md:73 (self-check C post-update review line)",
     expected: "Eval E4-4: 'Post-update review fields all filled or marked unknown'; design L-15: 'insufficient evidence is valid'",
     observed: "The line asks that the promise row, the tier row and the keep / change line are 'filled'. In E4 (and any event planned before these books) there is no promise sentence and no promise or tier theme was tagged; 'filled' invites the agent to write a verdict it has no evidence for",
     evidence: "evals/briefs.md E4 brief and E4-4; process.md:92-95 (the rows)",
     smallest_fix: ":73 'filled' → 'filled, or \"unknown: <why>\" (no promise sentence, no themes tagged)'"}
  - {id: R5, class: recommendation, check: C8 V6 + V7,
     where: ".agents/roles/live-ops-designer.md:37 and .agents/skills/live-ops-design/SKILL.md:46 (event-scope list without 'a season beat') vs event-review.md:5, craft SKILL.md:37, process.md:49 (with it); process.md:49 '(the one list; the self-checks, the role file and the templates point here)'",
     expected: "V6: the definition of event-scope work lives in one place (event-review.md top, as the coverage says) and the others point to it; a pointer claim is true",
     observed: "The scope list is written out in six places and already differs (two omit the season beat). process.md:49 says the templates point to the brief-line list; no template does yet (event-design.md:20 has only 'player promise'; proposals row 1 is pending)",
     evidence: "grep of the books for 'new world or zone'; grep of templates/live-ops/ for 'process.md' or 'event-review': no hit",
     smallest_fix: "Replace the parenthesised lists in role :37 and design :46 with 'event-scope work (`event-review.md` top)'. process.md:49: 'the self-checks and the role file point here; the templates will once proposals row 1 is approved'"}
  - {id: R6, class: recommendation, check: C7,
     where: ".agents/skills/live-ops-craft/references/event-review.md:15 (row 'environment-designer, level-design') and :67 (E-17 fix owner 'level-design, environment-designer')",
     expected: "Fix owners are roles the lead can route a note to",
     observed: "`level-design` is a shared skill, not a role (.agents/roles/ has no level-design or level-designer)",
     evidence: "ls .agents/roles/; matrix.md:488 (level-desi = level-design, a shared skill)",
     smallest_fix: "Name the role and the skill: 'environment-designer (with the level-design skill)'; for E-17 add game-designer where the secret is a hunt item"}
  - {id: R7, class: recommendation, check: C2,
     where: ".agents/skills/live-ops-design/SKILL.md:116 (§7 row 16) and .agents/skills/live-ops-craft/references/event-review.md:74 (§4 'never how to build the fix')",
     expected: "UP-16 general check: 'Every review note names the goal, the layer and a concrete fix ...; the hand-back maps each note to done or questioned'",
     observed: "Not a contradiction (a non-craft role must not prescribe the how, AGENTS.md §1), but the reconciliation is unstated: row 16's check drops the concrete fix and the done / questioned mapping. The worked example already does it right (the note states the condition the fix must meet, event-review.md:81)",
     evidence: "universal-principles.md UP-16 general check; event-review.md:81",
     smallest_fix: "Row 16 check: 'Each review note: goal, evidence, the condition the fix must meet (the E line's pass), owner; the next review maps each note to done or questioned; the hand-back names one weakness'"}
  - {id: R8, class: recommendation, check: C5,
     where: ".agents/skills/live-ops-craft/SKILL.md:3 (description)",
     expected: "Old triggers kept unless replaced by something at least as good",
     observed: "The trigger phrase 'how many players want X' (df13ff4 craft SKILL.md:3) was dropped; it is the plainest owner wording for a count request. 'sort this feedback' only partly covers it",
     evidence: "git diff df13ff4 -- .agents/skills/live-ops-craft/SKILL.md lines 3; description now 390 characters",
     smallest_fix: "Trade '(what each craft gets, when)' (29 characters) for '\"how many want X\"' in the Use-for list; stays under 400"}
  - {id: R9, class: recommendation, check: record accuracy,
     where: "knowledge/jobs/J018-riot-craft/coverage/live-ops-designer.md:15, :17, :144",
     expected: "The coverage header matches the books after repair round 1",
     observed: "Still says E-01..E-18, C-01..C-12 and '§1-§6 end at 17.4 KB'; the books have E-19, C-13 and §7 starts at 17,756 bytes",
     evidence: "byte offset of '## 7. Core' in design SKILL.md: 17756; event-review.md:42, :69",
     smallest_fix: "Update the three lines (E-01..E-19, C-01..C-13, 17.8 KB)"}
keep: [
  every rev1 fix, checked in the books: F1 (process.md:49 new-world line; event-review.md:5 scope, :15 environment row, :42 C-13, :69 E-19; L-22 points to E-19; self-check C covers E-01..E-19), F2 (process.md:49 is the one list; craft :70 and role :37 point to it; GD-08 and SI-18 rows name self-check C), R1 (feedback-ops.md:14, :36, :54-:61: rows corrected and added; my runs give the same numbers), R2 (every §6 line names its input), R3 (scope-fit field, premise-fixed skip with decision id, worked example option B), R4 (§7 rows 13 and 18), R5 (one line per partner in the role, one marketing timing in handoffs.md:14 and event-review.md:19), R6 (E-08 boost line matches platform-policy §A row 5), R7 (§2 brief format; lesson in the hand-back),
  event-review.md as a whole: the craft-ask table with what, when and the capture each craft is judged on; the named capture set with conditions and an image budget; E-01..E-19 each with input, pass and fix owner; status labels and the could-not-check list; the worked example with the earned-only egg read correctly against platform-policy §A row 1,
  the count tool's known false readings table: every arithmetic claim re-run and correct (date-only end is 00:00Z; end exclusive; a later end counts the next week; anon rows one author each; no flag under 5 messages or half),
  the concept round, scope fit and gate freeze; 'cooler' is a ticket with a cost,
  L-16..L-23 and the promise, tier, identity and keep / change rows in the post-update review and the failure-response table,
  §7: all eight master principles that list live-ops-designer (UP-01, 07, 11, 13, 14, 16, 18, 19) plus ten more, each with an event example and a check on a named input; 5 and 9 excluded with a reason; no contradiction,
  the proposals file (templates, a recipe review slot, a capture preset, the count tool, two library lines, two partner pointers), each with evidence; V11: the progression-designer's row adopted
  ]
verdict: pass
</spec>
```

## Results per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (61 rows checked, 0 failed) | 36 tagged rows (script: all 36 from matrix.md have a row) + 25 untagged; every landed-in location opened. GD-33 and GD-08 now carry their checks. Four rows carry the rule and the brief line, but only part of the finding's output check: CD-13, SI-05, SI-12, GD-20 (R3). Rejections and partner-measure rows (GD-16, GD-27, GD-32, LC-23, PP-32, PP-33, RI-04, SD-21, SI-11, SI-18) have sound reasons (V8, V13) |
| C2 core principles | pass | §7 in `live-ops-design` (loaded first; re-read line in §1, craft §1 and the role); all eight master principles for this role present with their own example and check; no contradiction; UP-16's concrete fix not stated (R7) |
| C3 self-review | pass | E-01..E-19 run on named studio-operator captures and partner measures the agent reads; the count lines run on the tool's output; the new-world check exists (C-13, E-19). Output-level checks for four brief lines missing (R3) |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules/*.md, J018-D2..D4 or platform-policy §A; docs lines re-read (liveops-planning.md:53-55, :65; content-updates.md:34); only real feedback_count modes named. Relative --out lands outside the gitignored data dir (R2a, older than J018) |
| C5 nothing valuable lost | pass | Diff walked; every removed or changed line traced; one dropped trigger phrase (R8) |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4; SKILL.md 120 / 77 lines; descriptions 351 / 390 characters; no section renumbered; J018 phrase in every changed file and the role comment; no tips section; no library ids, transcript lines or Riot names in J018 text (cases.md:14-15, :24 are unchanged J014 rows); evals/ unchanged |
| C7 better work | yes | See below; weak spots R1, R3, R4, R5 |
| C8 brief v2 / v3 | pass | V1 inputs and image budget named; V2 real modes only; V3 re-run by me, numbers correct, two silent traps not yet in the limits (R2); V4 E-08 and L-19 match platform-policy §A; V6 one list for brief lines, scope list still copied (R5); V7 §1-§6 end at 17.8 KB; V8 findings became brief lines, the craft-ask table and the capture review; V10 tier names, attempt cue / confirmed result, marketing timing and art-bible theme rows match partners; V11 adopted; V12 silent thresholds next to the command; V13 no measuring code, partner measures pointed to; V14 screening-aid label and eye check present |

## Judgment: better work?

Walked E2 (Halloween event with a Robux-gem crate and a countdown deal) and E4 ("did the event work?") with the new books. In E2 the old books gave a policy-correct event design and nothing about what the event looks, sounds and feels like. The new agent sees that the owner already fixed the premise, so it only runs the open part of the concept round. It writes one promise sentence that every craft brief quotes. It asks the progression designer to place every reward in the tier table, and asks each craft for its part at the cheapest stage. Before release it judges the build on named captures: the entrance is in the first view, the rarer reward looks bigger, nothing celebrates a declined purchase, the crate has one windup for every tier, and the boost changes the shown odds. In E4 the post-update review now also asks whether the promise held and whether the rare rewards felt rare. The checks are concrete, have named inputs, and find event failures that no single craft finds in its own review. The output is clearly better than with the old books, and repair round 1 removed both blocking gaps. Weak spots that remain: three lines still put the grey box before "any art brief", which contradicts the concept-round brief to the art director (R1). Four brief lines are checked only for being present, not in the result (R3). The post-update self-check asks for verdicts that can honestly be "unknown" (R4). The count command's relative --out path writes outside the gitignored data folder (R2).
