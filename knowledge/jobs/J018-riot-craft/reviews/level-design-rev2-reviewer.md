---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer level-design · claude-opus-5-5 · high · 2026-10-22

# Review: level-design books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/level-design/ (SKILL.md 103 lines; references/review-artifact.md 147; references/plan-and-blockout.md 78; references/worked-examples.md 18; no evals/, no role file: shared skill), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer level-design (opus, high)
looked_at_first: [
  the four book files read in full; git show df13ff4 of the old SKILL.md and review-artifact.md; git diff --stat df13ff4 and git status,
  reviews/level-design-rev1-reviewer.md (F1-F3, R1-R11: each re-checked in the books),
  matrix.md level-design column (96 IDs, script-extracted; all 96 have a coverage row, no extra rows) and the principle/apply/check of all 96 (script-extracted from the topic files); universal-principles.md UP-01..UP-20 space/level lines (unchanged since 2c54520),
  tools: look_check.py --help, value and silhouette --help, source of compare_subjects (:574-597: one shared ring around the union of all boxes), value_stats (:556-571), contrast_ratio (:152-155), aligned_iou,
  V3 runs by me (scratchpad/ldrev2/): the §6.2 route-table script extracted verbatim on a 4-node route JSON with a via point, a climb in y, an edge with no limit and ledges on both margin boundaries; look_check silhouette once per landmark (tower, dome, lighthouse on a 512x512 magenta key) and --compare; the §6.4 sheet one-liner and the §6.7 markup one-liner extracted verbatim; look_check value --compare-subjects (M1 form) on an in-scene 1280x720 first view (light sky, mid ground, HUD bar, two stalls against the sky, a goal sign on a wall) in two variants (goal invisible on its wall; goal clearly darker than a light wall), then value with each box alone,
  partner books: game-design/references/spaces.md (full), game-design/references/review.md §7 (flat-key definition :59), environment-design/references/review.md §7 (RD2 :77, RD5, RD7, RD9, RD12, RD13 :88, VB5, VB9, VB13, FL1, FL7, FL9, FL11), environment-design SKILL.md :13, :27, :34, environment-craft/references/measure-captures.md M1 :16, M5, M8, M9, M10-M12, environment-craft/references/handoffs.md :89, modeling-design/references/review.md GR3 :162, art-review/references/self-review.md RD7 :70, studio-mcp probes.md P-05, preproduction/references/handoffs.md :23, roles game-designer.md :21 and environment-designer.md :21,
  PhysicsSettings.yaml (collision view exists), .agents/workflows/jobs/job-stage.js :267-591 (read only),
  stage2-brief-v2.md (V1-V14 and the review severity rule), job-card.md fixed list, rules/company.md:105 (light checks, J005-D8),
  game-concept/evals/briefs.md §5 (level review eval, read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V12 + V3 (a pass rule gives a wrong verdict with no error in a common case the book prescribes); C3 (the measure behind LD13, LD16)",
     where: "review-artifact.md:103 (§6.3 pass rule 'or has the highest ratio_to_ring among the goal and its 2-3 competitors'); used by :43 (C2), :48 (C7), :60 (C19, measured only: 'a cue box whose ratio_to_ring falls toward 1.0'), :141 (LD13); plan-and-blockout.md:50 (grey read pass 'The first view'); SKILL.md:83 (§7 #3 check)",
     expected: "V12: the contrast route of the first-read rule is run on its real input form (an in-scene first view, competitors often standing against the sky) and tells a goal that stands out from one that does not; its silent false readings are listed",
     observed: "--compare-subjects measures every box against ONE ring around the union of all boxes (look_check.py:578-597). When the competitors stand against the sky, that shared ring's median is the sky, so the darkest subject gets the highest ratio_to_ring whatever its own surroundings are. The book adopted 'highest ratio_to_ring' as a pass route in repair round 1 (wider than rev1 R3 asked) and lists three false readings (dark goal by rank, sky in the box, box inside the object), not this one. C2 and C7 also need the grey image to agree, which limits the harm there; C19 uses the same shared ratio as its only screen and is measured only, so no eye check follows",
     evidence: "My run, fv_shared.png 1280x720, value --box goal --box stallA --box stallB --compare-subjects: shared ring p50 0.786 (sky); goal (a sign on a wall of the same value) ratio_to_ring 3.62, the highest (stallA 2.35, stallB 2.08); rank_by_median [stallB, stallA, goal]; verdict measured, no error. The same goal with value --box alone: subject_ring_ratio 1.09 (no local contrast: invisible). Variant fv_shared2.png, the goal clearly darker than a light wall: shared ratio_to_ring again 3.62 (identical), alone 2.71. The shared ratio cannot tell the two cases apart; each subject's own ring can (goal 1.09 vs 2.71; stalls alone 2.35, 2.08). The book's J018 dark-tower case still passes with own rings (12.1, coverage table d)",
     smallest_fix: "§6.3: keep the shared --compare-subjects run for rank_by_median only; the contrast route reads each subject against its own surroundings: one `value --box <subject>` run per subject (goal and its 2-3 competitors), compare `subject_ring_ratio` with `brighter_than_ring` direction from the shared run; the goal is the first read when it is first by median or has the highest own subject_ring_ratio, and the grey image agrees. Add to the 'wrong number with no error' list: 'the shared ring is one ring around all boxes: when competitors stand against the sky the darkest box wins ratio_to_ring whatever its own surroundings (review run: a goal invisible on its wall, own ratio 1.09, shared 3.62, the highest)'. C19: screen each cue by its own subject_ring_ratio at both settings (one run per cue box). Correct coverage table d row 'RA §6.3 false reading (repair round 1)'"}
  - {id: R1, class: recommendation, check: "V1 + V6 (a check whose input is not in the capture set)",
     where: "review-artifact.md:57 (C16 'items are named by type when 30-50 % hidden behind a box'; input 'captures + numbers'); §6.1 :68-83",
     expected: "Every check names an input that the capture set or a partner provides",
     observed: "No capture in §6.1 shows an item partly hidden, and the looked-at budget in SKILL.md:29 has none; the agent either asks for an unbudgeted image or rates C16 Unproven. The modeler already makes exactly this image (modeling-design review.md GR3: 'one occlusion render, only for item types') and art-review RD7 checks it",
     evidence: "modeling-design/references/review.md:162; art-review/references/self-review.md:70",
     smallest_fix: "C16 input: 'numbers (environment FL1) + the modeler's GR3 occlusion render per item type (partner)'; no new capture row"}
  - {id: R2, class: recommendation, check: "V1 (a pass condition its input cannot measure)",
     where: "review-artifact.md:56 (C15 'near zero seconds outside them in a normal-round frame sequence'); :79 (§6.1 normal-round stills 'at most 6 · looked at'); SKILL.md:29",
     expected: "The pass condition says what at most 6 stills can show",
     observed: "Six stills cannot count seconds of eye draw over a normal round; motion is not visible on a single still. The agent will either invent a seconds figure or over-ask for frames",
     evidence: "§6.1 row text; game-design spaces.md:8 has the same seconds wording for the designer's own check",
     smallest_fix: "C15 pass: 'outside the planned moments, no still shows the mechanic as the brightest or most saturated thing in view, and consecutive stills show no motion of it near a decision; seconds of eye draw at speed come from the owner's play-test at the gate (§6.8)'"}
  - {id: R3, class: recommendation, check: "V10 (a conflict with a rebuilt partner book has no proposal row)",
     where: "proposals/level-design.md (no row); environment-design/references/review.md:77 (RD2 'top median or widest spread'), :88 (RD13 'visible from each fork ... key forks only')",
     expected: "Where the level book changed a shared pass rule, a proposal row carries the change to the partner who measures the same view (SKILL.md:13 says the environment designer measures the place's reads with review.md §7)",
     observed: "The level book now reads the first view by median or contrast to the ring and calls the widest spread support only (with its own run showing a false pass on spread); environment RD2, on the same M1 numbers, still passes on the widest spread. Under environment's box rule (no sky in a box) this gives an eye-checked false fail on a dark landmark rather than a silent pass, so the harm is a contradictory verdict between the two books. RD13 checks key forks only, the level book every fork in each approach direction; that difference is defensible (each role's scope) but unstated",
     evidence: "review-artifact.md:103 vs environment review.md:77; coverage table d, row 'RA §6.3 false reading' (spread 0.46-0.57 from the sky edge)",
     smallest_fix: "Add one proposal row for environment-design review.md RD2 and measure-captures.md M1: the first-read rule of level §6.3 as fixed under F1 (median, or the highest own subject_ring_ratio, spread as support only); note in the same row that RD13's key forks are a subset of the level review's fork set"}
keep: [
  every rev1 finding repaired and verified in the books: F1 (flat-key captures with shadows off, probe first, pointer to the game-design definition, cast-shadow false readings with numbers, the black-fill sheet looked at once for every landmark), F2 (every approach direction, return trips included, in L-02, step 5, C4, §6.1, LD13, PB §4), F3 (identity symbol from each zone's entry in C4 and LD13; same tell in LD8), R1 (pacing example sums to 81 s, gaps 15 s and 27 s end to start, climax after 54 s; gap defined in PB §6), R2 (looked-at vs measured-only split with a count per capture), R4 (heights and collision in C10 for every map), R5-R11,
  the level job card, the layout options pass (diagrams from route JSON on a blank canvas), the blockout order in player metrics and the blockout brief that now matches the environment designer's intake (environment-design SKILL.md:34),
  the jump correction and the jump ladder probe; engine facts match the mirror,
  the route JSON and route-table recipe: my verbatim run matched hand checks (96, 121, 243, 178 studs; ledges 5.0 ok / 5.1 CHECK climb, 7.0 ok / 6.9 CHECK block at jump 6.0, margin 1),
  the silhouette recipe and the sheet one-liner: my runs wrote <landmark>.silhouette.png next to each input and a 768x256 sheet; IoU tower vs dome 0.24, tower vs lighthouse 0.66; alignment scales to one height (shape, not size) as the book says; the markup one-liner runs verbatim,
  the teaching sheet and pacing map; 19 fixed checks with an input each, Unproven when missing, re-rated every round; the screening-aid rule; worked example 1 (the problem behind the arrow note, contrast before detail),
  the core principles table (all 20, two 'in part' with reasons, no contradiction with the master),
  the proposals file (job-stage deliverables and the 14-to-C1-C19 rows, studio-mcp probes, flat-key shadow rule, route tool, template, look_check warnings, library WL-29 jump fix)
  ]
verdict: fix-first
</spec>
```

## Result per check
| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (113 rows checked, 0 failed) | 96 tagged rows plus 17 untagged; I opened every landed-in location against each finding's check. The four rows rev1 failed or half-landed (WL-23, GD-13, CD-26, GD-25) now carry rule and check. The 18 rejections name an owner whose book carries the check (FL4, VB1, VB7, E-12, E-19, PR-38, light-and-air, ambience). The §6.3 measure behind LC-12, CF-12 and VC-04 is faulty (F1, counted under C8) |
| C2 core principles | pass | §7 has all 20, each with a level example and a check with its input; UP-09 and UP-19 marked 'in part' with reasons; the space/level lines of the master (floors clean, fog never hides a hazard, collision unchanged without sign-off, lighting after the last route change) are carried here or in L-rows and step 7 |
| C3 self-review | pass, with F1 | LD1-LD18 and C1-C19 run on named captures, numbers and partners. F1 is a fault in the measure behind LD13, LD16 (C7) and C19, not a missing line. C16's input is missing from the capture set (R1); C15's 'seconds' cannot be measured from its stills (R2) |
| C4 kit rules and engine | pass | Engine claims match the mirror (WalkSpeed 16, JumpPower 50 with CharacterUseJumpPower true, JumpHeight 7.2 only when false, Gravity 196.2, greybox 5 studs, GlobalShadows, PhysicsSettings collision view). Tool modes real (look_check value/silhouette/thumb and their output keys ratio_to_ring, brighter_than_ring, rank_by_median, subject_ring_ratio; scene_audit.load_probe; screen_capture, character_navigation, inspect_instance). Proposals only, no stage edits, PROPOSAL labels, light-check split per J005-D8 |
| C5 nothing valuable lost | pass | Every old row kept, moved or sharpened; the approach-direction rule restored; only the 7.2-stud default jump removed, correctly |
| C6 fixed rules | pass | Only the four book files plus this role's coverage and proposals files changed for level-design; no role file (shared skill); SKILL.md 103 lines; description 394 characters; sections not renumbered (C1-C14 keep the old order, §6-§7 appended); J018 phrase in all four headers; "Riot" only in headers, no library IDs or transcript lines in bodies; no tips section; LF endings; no evals/. `sync_harness.py --check` shows the generated copies out of date for all wave-3 books: the lead's sync at commit |
| C7 better work | yes, clearly | See below |
| C8 brief v2 and v3 | fail (F1) | V12/V3: F1. V1: R1, R2; the budget split is otherwise clear. V2: only real modes. V6: R7 of rev1 repaired; measures pointed to (M1, M5, M8, M9, M10). V7: steps, rules and self-check end at about 16.2 KB; §1 says to re-read §7 after a compaction. V8: sheets, a brief and review checklists. V10: R3; the blockout brief now matches the environment intake; spaces.md agrees (jump, walk limits, reads). V11: all five partner rows adopted with locations. V13: the 9-line route script is borderline, with a tool proposal; the sheet and markup are one-liners. V14: every recipe is a labelled screening aid with its false readings |

## C7: will the agent make better work?
I read the books as the game designer would for eval brief 5 ("our lobby, top-down and part coordinates; new players don't find the shop"). The old books gave 14 bare checks, "measure walk times" and a wrong jump number. With the new books the agent writes the job card, builds the route JSON and gets edge times and OVER flags from a tested script. Worked example 1 makes it look for the cause behind the "add an arrow" note. It asks the studio operator for a budgeted capture set and rates C2 as Unproven until the first view arrives. For a new stage, the options pass, teaching sheet, pacing map and blockout brief give the environment designer and the progression designer real inputs that did not exist before. The landmark checks now cover every approach direction and are protected against cast shadows. The output will be clearly better.

Weak spots:
- The first-read measure can call a goal that is invisible on its wall "the first read" when the sky dominates the shared ring (F1). In C2 and C7 the grey image must also agree, which limits the harm. C19 has no such eye check.
- C16 and C15 name inputs the capture set does not give (R1, R2). The agent will either ask for images outside the budget or rate these checks Unproven.
- The two books that judge the same first view give different verdicts on a dark landmark (R3).
- The book is dense (18 L-rows, 19 checks, 18 self-review lines, 20 principles), but each layer has its own job, and the scope line in §7 keeps a review-only job small.
