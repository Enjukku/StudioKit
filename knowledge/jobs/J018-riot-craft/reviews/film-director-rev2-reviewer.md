---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer film-director · claude-opus-5-5 · high · 2026-10-22

# Review: film-director books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/film-director.md (body) + .agents/skills/film-direction/ (SKILL.md, references/) + .agents/skills/film-craft/ (SKILL.md, references/; evals/ not part of the work), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer film-director (opus, high), round 2
looked_at_first: [
  all 14 book files read in full as they are now (role body, both SKILL.md, 7 + 6 references), then git diff df13ff4 (removed lines walked for film-craft SKILL.md and all references; old film-direction §5-§6 and the old role body re-read),
  reviews/film-director-rev1-reviewer.md (F1, F2, R1-R10 each re-checked in the books),
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20: principle, cinematic line, general check), matrix.md (film-direc column, 76 ids, extracted by script) and principle / apply / check of all 76 from the topic files,
  job-card.md (fixed list, J018-D2..D4), stage2-brief-v2.md (V1-V11), tool-modes.md, orchestration/references/job-types.md §1 Cutscene,
  tools/art/look_check.py (--help of value / silhouette / thumb / palette; source: MASK_MIN_FRAC 0.001, MASK_MAX_FRAC 0.98, compare_subjects :574-597, run_value), tools/film/shotlist.py (--help of every command),
  partner books read-only: vfx-design SKILL.md:62 (flash rule), vfx-craft/references/measure.md §6, animation-design references/game-timing.md:44 and :64, roles/animator.md :68-69, vfx-design and sound-design sync windows, game-design systems-economy.md:73, ui-design shops-rewards-onboarding.md:49,
  roblox-creator-docs _api-reference/classes/Camera.yaml:1308-1333 (WorldToViewportPoint, no GUI inset),
  film-craft/evals/briefs.md (E1 and E2 used for the C7 read),
  my own runs (scratchpad fdrev2/): the flash script extracted from blender-previs.md §7 and run as printed on 9 synthetic frame folders; look_check silhouette on small and border-touching region masks; thumb --mask --size 667x375; value --box on a frame without bars; a Blender 5.1 headless probe of the §7 black-fill and object-colour mask recipe under the default AgX view transform, keyed by look_check
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3, C3",
     where: ".agents/skills/film-craft/references/blender-previs.md:77-89 (Flash count script and its note); used by review.md:128 (R-10), film-direction/SKILL.md:146 (§7 #20 check), roles/film-director.md:47",
     expected: "The flash count gives the number of large-area flashes per rolling second on the animatic frame folder, the same for the same footage at any render rate, so R-10 can say 'within the vfx-design flash rule' (design <= 2, never > 3, vfx-design/SKILL.md:62)",
     observed: "The script counts frames whose per-pixel rise from the previous frame is >= 0.1 on >= 10 % of the frame. A flash that rises over several frames is counted once per rising frame; a flash whose per-frame rise is under 0.1 is not counted at all, however large its total change. The count therefore depends on the render rate and on easing, with verdict-free output and no error. The book's note names only the small-area limit; the ramp limit the maker found (coverage table d, repair-1 R-10 row) is not in the book",
     evidence: "script extracted from blender-previs.md §7 and run as printed (fdrev2/flash_book.py): (a) a whole-frame 4 Hz pulse 0.05-0.50 linear luminance, 2 s: 10 per second when rendered at 30 fps, 0 per second at 60 fps (false PASS of a 4 Hz full-frame pulse; vfx-design: 'never above 3 Hz at full contrast'); (b) a 5 Hz pulse 0.10-0.26 at 30 fps: 0 (WCAG general-flash pair of opposing changes >= 0.1, 5 per second); (c) two eased flashes in one second (3 rising frames each): 6, a false FAIL against 'never > 3'; (d) four hard 2-frame flashes: 4 (right). A corrected count that registers a flash as a rise of >= 0.1 from the running trough and re-arms only after an opposing fall of >= 0.1 from the running peak (fdrev2/flash_fix.py) gives (a) 5 and 5, (b) 5, (c) 2, (d) 4",
     smallest_fix: "Replace the loop in blender-previs.md §7 with the tested trough/peak form: `lo = hi = None; armed, on = True, []` then per frame `if lo is None: lo = hi = L; continue`; `lo, hi = np.minimum(lo, L), np.maximum(hi, L)`; `if armed and ((L - lo) >= STEP).mean() >= AREA: on.append(i); armed, hi = False, L` `elif not armed and ((hi - L) >= STEP).mean() >= AREA: armed, lo = True, L` (same print line). Change the note to: 'a flash = a rise of STEP from the lowest value since the last flash, counted again only after an opposing fall of STEP; rate- and easing-independent; a flash smaller than AREA, and saturated red, are not counted'. Update the proposals row for a flash tool with the same definition"}
  - {id: R1, class: recommendation, check: "C6, C5",
     where: ".agents/skills/film-craft/references/review.md:18 ('held: needs Roblox' until step 7)",
     expected: "Step references follow the reordered film-craft §3 (Roblox assembly is now step 11)",
     observed: "'until step 7' still points to the old numbering; step 7 is now Storyboards, so the line says runtime rows wait for the boards",
     evidence: "film-craft/SKILL.md:42 (step 11 Assemble in Roblox), :38 (step 7 Storyboards); git show df13ff4:.agents/skills/film-craft/SKILL.md (old step 7 Assemble in Roblox). The other step pointers (role :35 'steps 3-8', film-direction SKILL.md:42 'step 3', acting-light-sound.md:48 'step 6') are right; templates/film/storyboard-brief.md:24 is stale too and is already a proposals row",
     smallest_fix: "review.md:18: 'until step 11 (`film-craft` §3)'"}
  - {id: R2, class: recommendation, check: "C3, C1",
     where: ".agents/skills/film-craft/references/review.md:112 (B-16); film-craft/SKILL.md:88 (self-check 'Animatic timed'); coverage table a row RI-26",
     expected: "RI-26's check ('two alternatives exist with a recorded choice') has a self-review line, as the coverage row claims for B-16",
     observed: "The rule lands (film-craft step 8 'two edit takes on the same shots', D-31, acting-light-sound §1), but B-16 checks drift, the manifest, temp marks and the owner's timing only; no line asks for the two takes and the owner's recorded pick",
     evidence: "review.md:112 text; film-craft/SKILL.md:39 (step 8) and :88",
     smallest_fix: "B-16: add '; the key beat has two edit takes on the same shots and the owner's pick is recorded'; the same clause in the film-craft self-check line 'Animatic timed'"}
  - {id: R3, class: recommendation, check: "C7, C3",
     where: ".agents/skills/film-craft/references/review.md:102 (B-06 'the subject first when the named regions are ranked by each region's p95'); film-direction/references/acting-light-sound.md:40 (brightest-area row)",
     expected: "The value check judges the read the shot planned, including a planned silhouette (the boss dark in a fire-lit gate, the hero against the dawn), where the contrast is the subject's darkness against the brightest area",
     observed: "B-06 fails every shot whose subject is not the brightest named region, so a deliberate backlit silhouette reveal reads as FAIL and step 12 says to fix every FAIL before the owner sees it; the agent is pushed toward front-lit reveals. The subject/ring ratio the line also reads is symmetric and already measures such a shot correctly",
     evidence: "look_check.py contrast_ratio of the subject and ring medians (symmetric WCAG ratio, run_value); B-06 text; the library has no finding against backlit silhouettes (grep of knowledge/reference/craft/riot/ for backlit / silhouetted: none apart from SS-19's group example)",
     smallest_fix: "B-06: add 'a shot whose value key plans a silhouette (subject dark against the brightest area) passes on the subject/ring ratio and the bright area sitting directly behind the subject; write the silhouette in the picture plan'; one clause in the acting-light-sound §2 brightest-area row ('or directly behind it, for a planned silhouette')"}
  - {id: R4, class: recommendation, check: "C7, C8 V3",
     where: ".agents/skills/film-craft/references/review.md:122 (R-04 'each sound cue minus its picture event ... against the sync rule'); film-direction/references/acting-light-sound.md:66 (three versions incl. 'warning before'); shot-language.md:91 (J cut)",
     expected: "The sync rule is applied to cues that are meant to be in sync; a planned lead (a J cut, a warning before the reveal) is judged against its own planned offset",
     observed: "R-04 reads every sound cue against the one-sided sync rule, so a deliberate warning-before cue or J cut, which the books recommend trying at a reveal, reads as a sync FAIL",
     evidence: "shot-list-format.md:18 (cues carry sync: locked / flexible / pending); review.md §3 defect row 'fix cue timing or document an intended offset'",
     smallest_fix: "R-04: 'the sync rule applies to cues with sync: locked paired with their picture event; a planned lead or delay (J cut, warning before) is checked against its note in the shot list'"}
  - {id: R5, class: recommendation, check: C5,
     where: ".agents/skills/film-direction/SKILL.md:107-118 (§6 self-check)",
     expected: "The old self-check line 'Alternatives with a recommendation for every choice that changes the player's experience' is kept or replaced",
     observed: "The new §6 keeps alternatives only for the key beat (options at equal finish); the wider line is gone from the self-check, although §3 step 5 and §5 still state the rule. Choices such as skip policy, camera mode or the shared-scene policy now have no self-check line",
     evidence: "git show df13ff4:.agents/skills/film-direction/SKILL.md:96",
     smallest_fix: "§6: extend the options line with '; every other choice that changes the player's experience shows its alternatives with one recommendation'"}
  - {id: R6, class: recommendation, check: "C7, C4 (rules/anti-overengineering.md)",
     where: ".agents/skills/film-craft/SKILL.md:31-44 (§3 steps 1-13); roles/film-director.md:31-40",
     expected: "The stages are sized to the job: a 3-second in-play camera moment does not need the same passes as a 9-shot boss entrance",
     observed: "Thirteen steps with an options pass, blocking strip, value strip, light variants, boards and two edit takes, with no line on what a small moment may skip. Worked example 3 (door reveal in an obby) shows a small case but not which steps it ran. An agent can over-build small jobs, and the light-check rule only caps images, not passes",
     evidence: "film-craft/SKILL.md §3; worked-examples.md:21-25; old books had no sizing line either, but they had 9 lighter steps",
     smallest_fix: "One line at the top of film-craft §3: 'Size the passes at step 1 and record them with the budget: a short in-play camera moment runs text options, one blocking key frame with its B-03/B-04/B-06 numbers, the animatic and the Roblox lines; options sheets, the value strip, light variants and boards are for moments with a key beat worth them'; worked example 3 names the steps it ran"}
  - {id: R7, class: recommendation, check: "C8 V3",
     where: ".agents/skills/film-craft/references/blender-previs.md:75 (region masks); review.md:103 (B-07 'a box on the picture, bars excluded')",
     expected: "Each measuring recipe covers the inputs the line names",
     observed: "(a) The region list names 'sky patch', but the Blender recipe renders one object-colour mask per region; the sky is the world, not an object, and the book does not say how to mask it. (b) B-07 on a frame without bars: a picture-area box covers 100 % of the frame and look_check refuses it ('invalid-mask', >= 98 %); the line does not say to read the whole distribution then. Both fail visibly, not silently",
     evidence: "my runs: value frame.png --box 0,0,1280,720 -> verdict invalid-mask, subject None, whole p5/p95 given; --box 0,8,1280,712 -> measured. A border-touching 600x150 region mask in silhouette -> invalid-mask (no flat border), so a big sky region must go through value --mask, which accepts it",
     smallest_fix: "blender-previs §7 rank bullet: 'the sky region: world black, every object white, in the same pass'; B-07: 'with no bars, read the whole distribution (a box over 98 % of the frame is refused)'"}
  - {id: R8, class: recommendation, check: C6,
     where: ".agents/skills/film-direction/references/scene-studies.md:18 (row 10)",
     expected: "No Riot games or artists named in the book bodies (C6 list)",
     observed: "Row 10 names 'Arcane Season 2' and the artist 'Maunoury'. The file is unchanged since df13ff4 and the row comes from the J015 research paper (N3 AR), not from the transcripts, so it is not a J018 regression; the coverage itself calls it 'the animated-series memory sequence'",
     evidence: "git diff df13ff4 -- scene-studies.md: empty; grep -i arcane over the 14 book files: this row only",
     smallest_fix: "Lead's call. If the C6 list is read literally: 'An animated series, a memory sequence (E; supporting)' with the mechanism and N3 AR source unchanged"}
keep: [
  every rev1 keep item, still intact: the stage order options -> shot list with picture plan -> blocking strip -> value pass (light variants, grayscale strip, then colour) -> boards on the blocking stills -> timed animatic -> briefs -> animator blocking check -> Roblox; the per-stage self-review lines with inputs and image budgets; beats-and-timing.md; shot-language §5 and §7; the performance sheet and value plan; the partner table and hand-off rows; the 'do not judge' and trap notes; the five worked examples; §7 core principles; the proposals file,
  the repair-1 work: the p95 ranking with exact region masks in Blender and tight, checked boxes on captures (blender-previs §7 'Rank the bright regions'), which also catches the two extra traps the maker found (under 5 % fill, a brighter patch inside a loose box),
  B-12's cast check by model and rig ids with a pose-matched silhouette compare only,
  the four review passes mapped to their §6 lines (review.md §1, film-craft step 12),
  one sync rule in one place (beats-and-timing.md §4) and the flash rule left to vfx-design, every other line pointing there,
  'the brief's image cap wins' with a cut order (review.md §7),
  log ids exactly as in the shot list, written into roblox-assembly §3, shot-list-format §2 and the engineering hand-off row
  ]
verdict: fix-first
</spec>
```

## Earlier findings (rev1): fixed or open

| Rev1 id | State now | Evidence |
| --- | --- | --- |
| F1 box-median rank | fixed | blender-previs.md:74-76 (p95, region masks, tight boxes, fill and brighter-patch rules); review.md B-06, B-18, R-09; film-craft C-20, step 6; film-direction §7 #3; role :45 |
| F2 cast by silhouette IoU | fixed | review.md B-12 (ids against the asset record and rig sheet; pose-matched compare only), B-14 (both from the still's camera); §7 #11; modeler partner row asks for the asset records |
| R1 stale sync clause | fixed | beats-and-timing.md:33 (clause gone); proposals S-133 row withdrawn |
| R2 four passes | fixed | review.md:13, film-craft step 12 and self-check, role step 8 |
| R3 modeler ask | fixed | role :60 |
| R4 four lost clauses | fixed | game-cinematics.md:8 and :33, shot-language.md:50, acting-light-sound.md:49 |
| R5 repeated numbers | fixed | sync numbers only at beats-and-timing.md:33; flash numbers only in vfx-design |
| R6 flash count runnable | fixed as a script, but the script miscounts (new F1) | blender-previs.md:77-89 |
| R7 image cap | fixed | review.md:136 |
| R8 job ids in bodies | fixed | D-29, C-20 'O', shot-list-format.md:38 |
| R9 log ids | fixed | roblox-assembly.md:35, shot-list-format.md:42, handoff-briefs engineering row |
| R10 sell list, convergence, not precious | fixed | R-09, B-18, §7 #15 |

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 76 of 76 tagged findings have a row (script against matrix.md); every landed-in location opened against the finding's principle, apply and check; 75 landed, 1 rejection (SD-29, sound-designer's craft: sound) and 2 partials (GD-25, WT-05) with sound reasons. 76 rows checked, 0 failed. One row overstates its check location (RI-26 -> B-16): R2 |
| C2 core principles | pass | film-direction §7 (the skill loaded first) states all 20 UPs for directing, each with its own example and a check with its input; no contradiction with the master; UP-15 'not precious' now present. #20's check inherits F1 |
| C3 self-review | fail on F1 | Every checkable finding has a §6 line with its input; R-10's flash count gives a rate-dependent wrong number (F1); RI-26's check has no line (R2) |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules/, J018-D2..D4 or the cutscene recipe (the added pre-board passes are G3 proposals rows); `WorldToViewportPoint` claim matches Camera.yaml:1308-1333; every tool mode named exists; the Blender black-fill and mask recipe works and is keyed by look_check under the default AgX view transform too (magenta reads #CA75CA, auto-key still finds it). Sizing note: R6 |
| C5 nothing valuable lost | pass with recommendations | Removed lines of film-craft SKILL.md and all references walked; rev1's four lost clauses and the modeler ask are back; one old self-check line lost (R5); one step pointer broken by the reorder (R1) |
| C6 fixed rules | pass | Only the film books plus the coverage, proposals and review files changed (git status); role frontmatter lines 1-10 byte-identical to df13ff4; SKILL.md 146 and 94 lines; descriptions 379 and 388 characters; no section renumbered (§7 appended; review §6-7, blender-previs §7, shot-language §7 appended; steps inside §3 reordered as the owner allowed); J018 phrase in every changed file's header and the role comment; no Riot names, library ids or transcript lines added; no tips section; evals/ unchanged. Pre-existing Arcane row: R8 |
| C7 better work | better, one measuring fault | See below |
| C8 brief v2 | fail on V3 (F1) | V1 pass (inputs and image budgets per line; the cap rule); V2 pass; V3 fail (F1; R4, R7 small); V4 pass (paid random reveal matches game-design, vfx-design, ui-design); V6 pass (one sync rule, flash rule delegated); V7 pass (steps, rules and self-check in the first ~19 KB of film-direction, ~17 KB of film-craft; compaction note names §7); V8 pass (performance sheet, value plan, picture plan, partner asks); V10 pass (animator, VFX, sound windows and still asks agree); V11 pass (the animator's still row adopted; no other row targets the film books) |

## Better work (C7)
Read as the agent at the start of E1 (the flooded observatory reveal, 8-image cap) and E2 ("the boss entrance feels flat"). The old books gave a strong runtime, continuity and exits spine but almost no picture craft: no premise or sell list, no options, no value plan, no timing grammar, and a review that asked the agent to watch clips it cannot watch. The new books make the agent pitch a premise, hook and sell list; compare 2-3 greybox approaches at equal finish; plan a first-second read, read order and value key per shot; block and value-check on proxies before boards; time key beats as tell, build, beat, peak, result on one marker list; ask each partner for what it needs and when; and check each stage with named inputs, numbers first and images only where the cap allows. On E2 the agent now names metronomic cuts, even light and effects-before-layout beside the old defects and proposes contrast and timing fixes with shot ids. The repair round removed both measuring traps and every rev1 recommendation. What is still weak: the flash count gives a different answer for the same footage at 30 and 60 fps and misses eased pulses (F1, a safety line); the p95 rule would fail a deliberate silhouette reveal (R3); the sync rule would fail a planned J cut (R4); and nothing tells the agent to run fewer passes on a 3-second camera moment (R6). Fix F1 and the agent clearly makes better cinematics than with the old books.
