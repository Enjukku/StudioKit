---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer level-design · claude-opus-5-5 · high · 2026-10-22

# Review: level-design books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/level-design/ (SKILL.md 103 lines; references/review-artifact.md 151; references/plan-and-blockout.md 78; references/worked-examples.md 18; no evals/, no role file: shared skill), working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer level-design (opus, high)
looked_at_first: [
  the four book files read in full; git show df13ff4 of the old SKILL.md and review-artifact.md (every old line compared with the new text); git status and git diff --stat df13ff4,
  reviews/level-design-rev1-reviewer.md (F1-F3, R1-R11) and reviews/level-design-rev2-reviewer.md (F1, R1-R3): each re-checked in the books,
  matrix.md level-design column (96 IDs, script-extracted; all 96 have a coverage row; 17 untagged rows extra) and the apply/check text of all 113 findings (script-extracted from the topic files); universal-principles.md space/level lines (UP-01..UP-20; unchanged in the working tree),
  tools: look_check.py value/thumb/silhouette --help; source of value_stats (:555-571), compare_subjects (:574-597), run_value (:802-834), the thumb record (:1007-1016),
  V3 runs by me (scratchpad/ldrev3/): the §6.3 rank run, the three own-contrast runs with --exclude-box and the printer one-liner, all extracted verbatim from the book, on three in-scene 1280x720 first views (light sky, mid ground, HUD bar, mid wall; a goal portal as a hollow arch, as a solid light panel, and as an orange panel of the wall's value; a light fountain and a dark stall as competitors); the §6.3 phone-size thumb command (844x390); the §6.2 route-table script extracted verbatim on a 4-node route JSON with a via point and ledges on both margin boundaries,
  partner books: environment-design/references/review.md RD2 :77, RD5, RD9 :84, RD12 :87, RD13 :88, VB5, VB9, VB10, VB13, FL1 :106, FL7, FL11; environment-craft/references/measure-captures.md M1 :16, M5, M8, M9, M10; modeling-design/references/review.md GR3 :162; game-design/references/review.md §7 :59; game-design/references/spaces.md section list; art-review/references/art-bible.md §7 :69 (marker 3:1); studio-mcp/references/probes.md P-05 :72,
  roblox-creator-docs Camera.yaml:263-270 (FieldOfView vertical, default 70),
  stage2-brief-v2.md (V1-V14 and the review severity rule), job-card.md fixed list, other roles' proposal rows against level-design (environment-designer :32, game-designer :21-22, :34, progression-designer :28),
  game-concept/evals/briefs.md §5 (the level review eval, read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C5 (an old pass condition dropped; the coverage table says 'kept')",
     where: "review-artifact.md:44 (C3 Routes); coverage/level-design.md table c, row 'review-artifact.md:34-47 checks 1-14' ('kept as C1-C14 ... sharpened')",
     expected: "The old check 3 is kept or replaced by something at least as good: df13ff4 review-artifact.md:37 'intended destinations and optional alternatives are found without rescue; no dead end without a reason'",
     observed: "The new C3 says 'intended destinations are found without rescue in the played walk' and drops 'and optional alternatives'. No other check or LD line takes it over: the books still plan optional content (node field 10 'Optional content | side content and how it is signalled', review-artifact.md:20; L-08 shortcuts for return trips; the 'one who missed an optional clue' walk-through, :27), but no review line asks whether a player finds the shortcuts, side routes and side areas the route graph signals. C3's own 'Why' column ('intended exploration and accidental disorientation need different fixes') still points at that half. The coverage table records the check as kept",
     evidence: "git show df13ff4:.agents/skills/level-design/references/review-artifact.md line 37; grep 'optional' in the four books: only review-artifact.md:27 (the walk-through persona); C3 text :44; LD3-LD18 :132-151 name no optional route or side content",
     smallest_fix: "C3 Pass when: 'intended destinations, and the optional alternatives the route graph signals (node field 10: shortcuts, side routes, side areas), are found without rescue in the played walk; hidden secrets excepted'. Correct the coverage table c row"}
  - {id: R1, class: recommendation, check: "C3 + C7 (two pass rules for the same view disagree)",
     where: "plan-and-blockout.md:50 (grey read pass, row 'The first view', 'Pass when')",
     expected: "The same pass rule as review-artifact.md §6.3 (:106) and C2 (:43): the goal's own contrast reaches the marker target, and it is first by median or by own contrast",
     observed: "'the first read: lightest, or strongest in contrast against its own surroundings, tallest, and where the lines lead'. 'Lightest' alone passes here; §6.3 fails a lightest goal whose own ratio is under the target (the maker's own run: a light tower on a light sky, first by median, own 1.04). The measure column points to §6.3, so an agent that runs it is safe; an agent that reads only the Pass column is not",
     evidence: "coverage table d, row 'RA §6.3 median false reading (repair round 2)'; review-artifact.md:106",
     smallest_fix: "Pass when: 'the goal or main landmark is in frame, its own contrast reaches the marker target, it is the lightest or the strongest in contrast among its competitors (§6.3), it is the tallest, and the lines lead to it'"}
  - {id: R2, class: recommendation, check: "C7 (the eval brief: first view from coordinates only)",
     where: "SKILL.md:63 (rule: no pass/fail on reads without a capture); review-artifact.md:43 (C2 input '1 capture + numbers'); worked-examples.md §1 (uses a capture)",
     expected: "When the input is a top-down image and part coordinates only (eval brief 5: 'New players don't find the shop'; must 5.1 'first view from spawn checked'), the agent has an analytic screen for the first view that it can run before the capture arrives",
     observed: "The books give no way to check the first view without a capture, so C2 goes Unproven with a request. The core of this eval's problem (is the shop in the first frame at all?) can be screened from the spawn's facing and the coordinates",
     evidence: "Camera.yaml:263-270: FieldOfView is the vertical angle, default 70; at 16:9 the horizontal view is about 102 degrees, at a 844x390 phone about 113 degrees (2·atan(tan 35° · aspect), an inference); game-concept/evals/briefs.md:57-65",
     smallest_fix: "One line in review-artifact.md §6.2 or §6.3: 'With coordinates only: the bearing from the spawn facing to the goal and to each competitor, against half the horizontal field of view (about 51° at 16:9, about 56° on a wide phone); a subject outside it is not in the first frame. Labelled analytic; C2 stays Unproven until the capture'"}
  - {id: R3, class: recommendation, check: "V1 (an input count the agent cannot compute)",
     where: "review-artifact.md:60 (C19 'key views'), :83 (§6.1 'Lowest and highest graphics setting | key views at both | 2 per key view')",
     expected: "The views C19 needs at both settings are named, so the capture request and the image budget have a count",
     observed: "'Key views' is defined nowhere in the four books; the agent will either ask for every view at both settings or pick some without a rule",
     evidence: "grep 'key view': SKILL.md:83, :101; review-artifact.md:60, :83 only",
     smallest_fix: "§6.1 row: 'key views = the first view, the fork views, the zone entry views and one view per hazard (the looked-at set without the busiest moment and the stills)'"}
  - {id: R4, class: recommendation, check: "C8 V3/V14 (known limits of a screening aid: rare to medium cases, the eye check covers C2 and C7)",
     where: "review-artifact.md:109 (§6.3 'Gives a wrong number with no error when'); used measured-only by :60 (C19)",
     expected: "The known limits name the subject shapes common in Roblox levels that a rectangle box reads wrongly",
     observed: "Two cases are missing. (a) A hollow or thin subject (an arch or ring portal, a gate frame): the box median reads what shows through the gap. My runs: a hollow arch whose bright legs fill just over half its box gave own 3.8, the same as a solid panel; with thinner legs the median flips to the wall behind and the ratio falls toward 1.0 (a false fail, looked at on C2 and C7). (b) For C19, a thin cue (a hazard rim, a path edge line narrower than the 8 px ring) boxed loosely: the box median is the surface around the cue, so a rim that the lowest setting removes can keep its ratio and pass with no look, because C19 is measured only. The book's 'a few pixels big ... judged on the still' covers goals, not C19 cues",
     evidence: "scratchpad/ldrev3 runs: s1 (hollow arch) own 3.80, s2 (solid) own 3.80, s3 (orange, wall's value) own 1.10 and rank c1 first: the screen fails and the still is looked at, as the book says; the maker's C19 run (coverage table d) boxed the rim tightly (4.09 to 1.10)",
     smallest_fix: "Add to §6.3's limits: 'a hollow or thin subject (arch, ring, frame): box its solid part or judge it on the still'; in C19's input: 'a cue thinner than the ring (rim, edge line) is boxed tight to the cue or looked at on the lowest-setting still'"}
  - {id: R5, class: recommendation, check: "C7 (bloat; V6 run history in the body)",
     where: "review-artifact.md:109 (one line of about 1,600 characters), :112-114",
     expected: "The limits list states each false reading and its fix in one clause; the run history lives in the coverage file",
     observed: "The §6.3 limits line carries the J018 run numbers for every case (1.09, 3.62, 1.0, 8.7, 1.04, 14.2, 0.46-0.57, 1.05, 770 px ...). The agent reads all of it on every first-view check; the numbers prove the limit to a reviewer, not to the agent",
     evidence: "coverage/level-design.md table d already holds every run",
     smallest_fix: "Keep one example number per false reading at most; point to 'coverage table d (J018)' only in the file header, not in the body"}
  - {id: R6, class: recommendation, check: "C1 (VC-01: the rule landed, its check only in part)",
     where: "SKILL.md:68 (rule), review-artifact.md:150 (LD17 'contrast before detail'), :109 ('a goal that stands out by hue alone ... is judged on the still')",
     expected: "When a read fails or the screen cannot measure it, the finding says which contrast wins or loses against the surroundings (value, hue, saturation, shape, size, position, motion), so the fix changes a contrast and not the detail",
     observed: "The value screen measures value only; the hue-only and few-pixel cases are judged on the still with no list of what to judge. LD17 checks that the fix is not detail, not which contrast to change",
     evidence: "library check of the finding behind 'contrast before detail': a contrast list per focal item, at least one type clearly wins; my s3 run (an orange goal at the wall's value) fails the value screen although it reads by hue",
     smallest_fix: "LD17: add 'for a failing or unmeasured read, a contrast list for the goal (value, hue, saturation, shape, size, position, motion: wins, ties or loses); the fix changes one that loses'"}
keep: [
  rev2 F1 repaired and verified by my runs: §6.3 reads rank_by_median from the shared run only and each subject's own subject_ring_ratio from its own run, with the target and the grey image; the shared-ring and median-first false readings are listed with numbers; the printer one-liner globs itself and runs (my run: three files printed with ratio and direction); the thumb step writes the thumbnail and sheet and gives invalid-mask without a box, as written,
  rev2 R1 (C16 reads the modeler's GR3 occlusion render, which exists at modeling-design review.md:162), R2 (C15 says what stills can show; seconds come from the owner's play-test), R3 (proposal row for environment RD2 and M1, which still pass on the widest spread: the conflict is recorded, not silent),
  every rev1 repair still in place: shadow-free flat-key captures and the black-fill sheet, every approach direction at each fork, identity symbol from each zone's entry, same tell in LD8, the pacing example (segments sum to 81 s, gaps 15 s and 27 s, climax at 67 s), the looked-at vs measured-only budget, heights and collision in C10 for every map, R5-R11,
  the level job card, the layout options pass, the blockout order in player metrics and the blockout brief, the teaching sheet, the pacing map, the 19 fixed checks each with an input, re-rated every round, the screening-aid rule,
  the jump correction and the jump-ladder probe; the route-table script (my verbatim run: 96 studs 6.0 s, 204 studs 12.8 s OVER 10, ledges 5.4 ok / 5.5 CHECK climb, 7.4 ok / 7.3 CHECK block at jump 6.4, margin 1),
  worked example 1 (the problem behind the arrow note; contrast before detail),
  the core principles table: all 20, each with a level example and a check with its input, two marked 'in part' with reasons, nothing contradicting the master,
  the proposals file (recipe and workflow rows marked for G3; tool, template, probe, library and partner rows)
  ]
verdict: fix-first
</spec>
```

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (113 rows checked, 0 failed) | All 96 tagged IDs have a row, plus 17 untagged rows. I opened every landed-in location against each finding's apply and check text. The rows that rev2 touched (LC-12, CF-12, VC-04, VH-01 through §6.3; WL-02 and WL-19 through C16; GD-23 and UI-13 through C15; WL-20, VR-16 and LC-18 through C19) now carry rule and check. The 18 rejections each name the owner whose book carries the check. VC-01's contrast list is carried only in part (R6), so I count that row as a pass with a recommendation |
| C2 core principles | pass | §7 has all 20 principles, each with a level example and a check with its input. UP-09 and UP-19 are marked "in part", with reasons. No line contradicts the master. The master's space/level lines are all carried here or in the L-rows and step 7: floors clean, lighting after the last route change, collision unchanged without sign-off, fog never hides a hazard |
| C3 self-review | pass, with R1 and R3 | LD1-LD18 and C1-C19 run on named captures, numbers and partner inputs. Two weak spots: the grey-pass "Pass when" wording is looser than §6.3 (R1), and "key views" has no count (R3) |
| C4 kit rules and engine | pass | Engine claims match the mirror: WalkSpeed 16, JumpPower 50 with CharacterUseJumpPower true, Gravity 196.2, greybox 5 studs, GlobalShadows, FieldOfView 70 vertical. The tool modes are real: `look_check value --box/--exclude-box/--compare-subjects`, `thumb --size`, `silhouette --compare`, `scene_audit.load_probe`, and the Studio MCP `screen_capture`, `character_navigation` and `inspect_instance`. The books make proposals only, label values PROPOSAL and keep the light-check split |
| C5 nothing valuable lost | fail (F1) | Every old row is kept, moved or sharpened, except one: old check 3's "optional alternatives are found without rescue" was dropped without a record. The 7.2-stud default jump was removed correctly |
| C6 fixed rules | pass | For level-design, only the four book files plus this role's coverage and proposals files changed. There is no role file (shared skill). SKILL.md has 103 lines, and the description has 394 characters. Sections are not renumbered: C1-C14 keep their order, and §6-§7 are appended. All four headers have the J018 phrase. "Riot" appears only in the old SKILL header; the bodies have no library IDs or transcript lines and no tips section. Line endings are LF, and there is no evals/ folder. The "J018" tag in the L-row evidence column matches the other rebuilt books. `sync_harness.py --check` shows the generated copies of wave-3 books out of date; the lead syncs them at commit |
| C7 better work | yes, clearly | See below. Weak spots: R2, R4, R5, R6 |
| C8 brief v2 and v3 | pass | V12/V3: I ran every §6.3 command verbatim on in-scene first views. The own-contrast screen separates a visible goal (3.8) from a goal of the wall's value (1.1). The rank run and the thumb step behave as written, and the route-table script re-runs correctly. The limits for hollow subjects and thin C19 cues are missing (R4, a recommendation under the severity rule). V1: R3. V2: only real modes. V4: no money, policy, save or remote lines. V6/V13: the measures point to environment M1, M5, M8, M9 and M10, and the per-subject run has a tool proposal. V7: steps, rules and self-check end at about 15.5 KB; §7 starts at 16.3 KB, and §1 says to re-read it after compaction. V8: sheets, a blockout brief and review checklists. V10: the RD2 difference is recorded as a proposal row. V11: all five partner rows are adopted, with their locations. V14: every recipe is labelled as a screening aid, with its limits |

## C7: will the agent make better work?
I read the books as the game designer would for eval brief 5 ("our lobby, top-down and part coordinates; new players don't find the shop").

The old books gave 14 bare checks, "measure walk times" and a wrong jump number. With the new books, the agent:
- writes the job card;
- builds the route JSON from the coordinates and gets edge times and OVER flags from a tested script;
- follows worked example 1 to look for the cause behind an "add an arrow" note, and calms the surroundings before it raises the goal;
- draws the numbered top-down markup with a tested one-liner;
- asks the studio operator for a budgeted capture set.

When the first view arrives, the screen now reads each subject against its own surroundings, so the round-2 false pass is gone. For a new stage, the options pass, the teaching sheet, the pacing map and the blockout brief give the environment designer and the progression designer inputs that did not exist before. The output will be clearly better than with the old books.

Weak spots that remain:
- **First view from coordinates only (R2).** With coordinates and no capture, the agent has no first-view screen, so it rates C2 Unproven. This eval's main question (is the shop in the first frame at all?) can be screened from the spawn facing and the camera's field of view.
- **Optional routes (F1).** The review no longer asks whether players find the optional routes and shortcuts that the plan signals.
- **Hard cases for the value screen (R4, R6).** Hollow portals, thin hazard rims at the lowest setting and hue-only goals need a known limit or a contrast list.
- **Long limits line (R5).** The §6.3 limits line is long because it carries the run history.
- **Book size.** The book is dense: 18 L-rows, 19 checks, 18 self-review lines and 20 principles. Each layer has its own job, and the scope line in §7 keeps a review-only job small.
