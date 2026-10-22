---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer film-director · claude-opus-5-5 · high · 2026-10-22

# Review: film-director books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/film-director.md (body) + .agents/skills/film-direction/ (SKILL.md, references/) + .agents/skills/film-craft/ (SKILL.md, references/; evals/ not part of the work), working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer film-director (opus, high), round 3
looked_at_first: [
  all 15 book files read in full as they are now (role body, both SKILL.md, 7 + 6 references), then git diff df13ff4 (role body removed lines walked; section headings of every changed file compared with df13ff4),
  reviews/film-director-rev1-reviewer.md and rev2 (every finding re-checked in the books),
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20, cinematic lines), matrix.md (film-direc column, 76 ids, extracted by script), principle and check of all 76 from the topic files (extracted by script),
  job-card.md (fixed list, J018-D2..D4), stage2-brief-v2.md (V1-V11), tools/art/look_check.py (value --help; value_stats, compare_subjects, MASK_MIN_FRAC / MASK_MAX_FRAC),
  partner books read-only: vfx-design/SKILL.md:64 (flash rule), vfx-craft/references/measure.md §6, sound-design/SKILL.md:107 (S-133), vfx-design/SKILL.md:68, animation-design/references/game-timing.md:44; all proposals files grepped for rows against the film books,
  film-craft/evals/briefs.md (E1 and E2 for the C7 read),
  my own runs (scratchpad fdrev3/): the flash script extracted from blender-previs.md §7 by script and run as printed (flash_from_book.py) on 44 synthetic frame folders at 24, 30 and 60 fps (gen.py, gen2.py, gen3.py, gen4.py), and one candidate one-line fix (flash_fix5.py) on the same folders
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3, C3, C2 (#20)",
     where: ".agents/skills/film-craft/references/blender-previs.md:77-100 (Flash count script and its note, 'the same footage gives the same count at 30 and 60 fps'); used by review.md:128 (R-10), film-direction/SKILL.md:146 (§7 #20 check), game-cinematics.md:29, roles/film-director.md:47; the same definition in proposals/film-director.md (flash tool row and the vfx-craft measure.md §6 row)",
     expected: "The large-area flash count per rolling second gives the right number for the footage, the same at any render rate, so R-10 can say 'within the vfx-design flash rule' (design <= 2, never > 3, never above 3 Hz at full contrast; vfx-design/SKILL.md:64)",
     observed: "After an onset the region is disarmed with its trough set to the onset frame. If the light keeps rising after that frame (an eased rise that crosses STEP part way up, or a slow fade-up), the trough stays at the onset level; a flicker that then runs above that level is both a rise from the trough and a fall from the peak for every pixel, the two shares cancel (net 0), the region never re-arms, and the whole flicker counts as one flash. Verdict-free output, no error. The rate independence the note claims holds only when the rise is hard: at 60 fps more of an eased rise lies after the onset frame than at 30 fps, so the same footage reads differently",
     evidence: "script extracted from blender-previs.md §7 and run as printed (fdrev3/flash_from_book.py), 'most in any 1 s': (L) dark sky, lightning rising over 1/15 s to 0.80 linear, then a 5 Hz flicker 0.80/0.50 for 2 s: 5 at 24 and 30 fps, 1 at 60 fps; (TL) the same lightning (0.1 s rise, then 5 Hz +0.6/+0.3) over a static textured 640x360 colour scene: 5 at 30 fps, 1 at 60 fps; (E) an eased 0.2 s rise to 0.60, then a 4 Hz flicker 0.60/0.35: 4 at 24 fps, 1 at 30 and 60 fps; (FF) a 2 s fade-up (fire swelling, portal opening) then a 5 Hz flicker 0.62/0.40: 1 at 24, 30 and 60 fps. Every one is a false PASS of a flicker above 3 per second. The script is right on the maker's own case types, re-run here: full-frame 4 Hz pulse 4/4, 3 Hz pulse 3, sine 4 Hz 4/4, hard rise then 6 Hz flicker 6, pans over stripes 0, flashes over a pan 4, opposed halves 5, local 15 % flicker 5, fade-in alone 1, cave-to-exterior pan 1, spark ignored",
     smallest_fix: "Add one line after the re-arm line of the loop: `elif not r[4] and net >= 0: lo = x  # after a flash, while nothing falls: later rises count from this frame`. Tested (fdrev3/flash_fix5.py): identical to the printed script on all 37 folders where it was right, and right where it was wrong: L 5 / 5 / 5 at 24 / 30 / 60 fps, TL 5 / 5, E 4 / 4 / 4, FF 5 / 5 / 5. In the note, add: 'while a region waits after a flash and nothing falls, its trough follows the frame, so a flicker after an eased rise or a fade-up is counted'; keep the rate claim only after the re-run. Carry the same clause into the two proposals rows (flash tool, vfx-craft measure.md §6) so the shared tool does not inherit the gap"}
  - {id: R1, class: recommendation, check: "C8 V1, C7",
     where: ".agents/skills/film-craft/references/review.md:136 (§7 'the brief's image cap wins ... Cut in this order until it fits')",
     expected: "The cut order can reach a brief's real cap, or says what to do after the last cut",
     observed: "After all four cuts a 5-shot sequence still needs about 14-15 checking images (reveal black-fill 1, cast still 1, board contact sheet 1, one capture per shot 5, handoff 1, finish and skip 2, access 4). The eval brief E1 (a 5-shot reveal) caps the job at 8 images. The rule then gives no next step, and it does not say whether a brief's cap counts generated images (boards), images looked at, or both, while 'plan-stage images are counted separately'",
     evidence: "review.md §7 maxima and cut order; film-craft/evals/briefs.md:6 ('Max 8 images'); R-09 input 'one capture per shot'",
     smallest_fix: "Append to the cut-order line: 'then the per-shot captures become numbers only (R-09 boxes from the MCP projection), keeping the reveal and the handoff frame as images; each line whose image was cut is \"not verified (image budget)\"'. Add: 'a cap in a brief counts the images you look at; generated boards and plan-stage renders are reported beside it unless the brief says otherwise'"}
  - {id: R2, class: recommendation, check: "C3",
     where: ".agents/skills/film-craft/references/review.md:102 (B-06); film-direction/references/shot-language.md:58 ('the subject owns the widest value range')",
     expected: "VC-04's check (the focal item has the widest p5-p95 spread and its ring a clearly narrower one) has a self-review line; the standard is in shot-language §5",
     observed: "B-06 reads the subject/ring median ratio and the p95 rank, not the spread; the standard 'the subject owns the widest value range' has no line, although `value --mask` already reports both distributions",
     evidence: "look_check.py value_stats (subject and ring distributions with p5 and p95); library VC-04 check",
     smallest_fix: "B-06: add 'and the subject's p5-p95 spread is wider than its ring's (from the same --mask run)'"}
  - {id: R3, class: recommendation, check: "C6",
     where: ".agents/skills/film-direction/references/scene-studies.md:24 ('Boards matched one-to-one ... (Fortiche, Season 1)')",
     expected: "If the C6 list is read literally, as the lead did for row 10 in repair 2: no studio or season name tied to the transcripts' series",
     observed: "The disagreement line still names the studio of the animated series whose name was removed from row 10 in repair 2. Unchanged since df13ff4; its source is the J015 paper (N3 BP-01), not the transcripts",
     evidence: "git show df13ff4:.agents/skills/film-direction/references/scene-studies.md:24 (same text)",
     smallest_fix: "Lead's call, for consistency with row 10: '(an animated series' first season)'"}
keep: [
  every rev1 and rev2 keep item, still intact: the stage order options -> shot list with picture plan -> blocking strip -> value pass -> boards on the blocking stills -> timed animatic -> briefs -> animator blocking check -> Roblox; the per-stage self-review lines with inputs and image budgets; beats-and-timing.md; shot-language §5 and §7; the performance sheet and value plan; the partner table and hand-off rows; the trap notes; the five worked examples; §7 core principles; the p95 ranking with exact masks and tight boxes; B-12's id check; the four passes mapped to §6 lines; one sync rule in one place and the flash rule left to vfx-design; log ids as in the shot list,
  the repair-2 work: the net rise-minus-fall flash test with nine blocks (pans and opposed halves right, see F1 for the one gap), the planned-silhouette clause in B-06 with its box arithmetic, R-04's locked-cue pairing with planned leads in the cue note, the sizing paragraph for small camera moments with worked example 3 naming its passes, the sky mask recipe, B-07 'read whole with no bars', the options line for every experience choice in film-direction §6
  ]
verdict: fix-first
</spec>
```

## Earlier findings: fixed or open

| Id | State now | Evidence |
| --- | --- | --- |
| rev1 F1 box-median rank | fixed (kept) | blender-previs.md:74-76; review.md B-06, B-18, R-09 |
| rev1 F2 cast by silhouette IoU | fixed (kept) | review.md B-12, B-14; film-direction §7 #11 |
| rev1 R1-R10 | fixed (kept) | as listed in rev2; re-checked: beats-and-timing.md:33, review.md:13, role :60, game-cinematics.md:8 and :33, shot-language.md:50, acting-light-sound.md:49, review.md:136, roblox-assembly.md:35, R-09, B-18, §7 #15 |
| rev2 F1 flash count rate- and easing-dependent | partly fixed: hard and eased single flashes, pulses and pans now right at every rate; a flicker after an eased rise or a fade-up still reads as one flash (new F1) | fdrev3 runs |
| rev2 R1 step pointer | fixed | review.md:18 'until step 11' |
| rev2 R2 two edit takes | fixed | review.md:112 B-16; film-craft/SKILL.md:90 |
| rev2 R3 planned silhouette | fixed | review.md:102; acting-light-sound.md:40; §7 #3; role :45; worked-examples.md:9 |
| rev2 R4 planned lead or delay | fixed | review.md:122 R-04 (cue `note`, a format field: shot-list-format.md:18); shot-list-format.md:41; role :46 |
| rev2 R5 alternatives for every experience choice | fixed | film-direction/SKILL.md:112 |
| rev2 R6 sizing small moments | fixed | film-craft/SKILL.md:32 (no renumbering); role :35; worked-examples.md:25 |
| rev2 R7 sky mask, no-bars spread | fixed | blender-previs.md:75; review.md:103 |
| rev2 R8 row 10 names | fixed | scene-studies.md:18; line 24 left (R3) |

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 76 of 76 tagged findings have a row (script against matrix.md); every review id, D-id and file named in table a exists (script); principle and check of all 76 compared with their landed-in locations; 75 landed, 1 rejection (SD-29, the sound-designer's craft) and 2 partials (GD-25, WT-05) with sound reasons. 76 rows checked, 0 failed. VR-23's flash part runs through R-10 and inherits F1; VC-04's spread check: R2 |
| C2 core principles | pass with F1 | film-direction §7 (the skill loaded first; re-read note in §1) states all 20 UPs for directing, each with its own example and a check with its input; no contradiction with the master's statements or cinematic lines. #20's flash check inherits F1 |
| C3 self-review | fail on F1 | Every checkable finding has a §6 line with its input; R-10's flash count gives a false PASS on a flicker after an eased rise or fade-up (F1); VC-04 spread: R2 |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules/, J018-D2..D4 or the cutscene recipe (recipe changes stay G3 proposals rows); engine claims unchanged since rev2's checks; every tool mode named exists (`value --help`, source); the planned-silhouette clause reads fields `value` writes (subject and ring p50) |
| C5 nothing valuable lost | pass | Role body removed lines walked; rev1 and rev2 restorations still in place; headings changed only by rename or append (film-direction §6 title, acting-light-sound §2 title) |
| C6 fixed rules | pass | Only the film books plus the coverage, proposals and review files of this role changed; role frontmatter lines 1-10 byte-identical to df13ff4 (cmp); SKILL.md 146 and 96 lines; descriptions 379 and 388 characters; no section renumbered; the J018 phrase in all 15 file headers and the role comment; no tips section; evals/ unchanged; LF endings (byte count of CRLF = 0 in every file). Pre-existing studio name: R3 |
| C7 better work | better, one safety-count gap | See below |
| C8 brief v2 | fail on V3 (F1) | V1 pass with R1 (cut order cannot reach an 8-image cap); V2 pass; V3 fail (F1); V4 pass (paid random reveal, confirmed outcome agree with game-design, platform-policy, vfx-design); V6 pass; V7 pass (film-craft steps, rules and self-check end at 17.8 KB; film-direction §6 ends at 19.7 KB, §7 named in the compaction note); V8 pass; V10 pass (sync window as in sound-design S-133 and vfx-design :68; flash rule pointed to vfx-design; the vfx-craft count differs and is a proposals row); V11 pass (no new row against the film books in any proposals file, re-grepped after the last edits) |

## Better work (C7)
Read as the agent at the start of E1 (the flooded observatory reveal, 8-image cap) and E2 ("the boss entrance feels flat"). The old books gave a strong runtime, continuity and exits spine but almost no picture craft: no premise, hook or sell list, no options, no value plan, no timing grammar, and a review that asked the agent to watch clips it cannot watch. The new books make the agent pitch the moment as an experience, compare 2-3 greybox approaches at equal finish, plan a first-second read, read order and value key per shot, block and value-check on proxies before boards, time each key beat as tell, build, beat, peak and result on one marker list, ask each partner for what it needs and when, size the passes to the moment, and check each stage with named inputs, numbers first. On E2 the agent now names metronomic cuts, even light and effects-before-layout beside the old defects and proposes contrast and timing fixes with shot ids and a static alternative. Two repair rounds removed every measuring trap the earlier reviews found, and the measuring notes are honest about what each command cannot see. What is still weak: the flash count, a safety line, still passes a lightning or fire flicker that follows an eased rise or a fade-up (F1, one line to fix); on a tight image cap such as E1's the agent runs out of cuts with no next step (R1). Fix F1 and the agent clearly makes better cinematics than with the old books.
