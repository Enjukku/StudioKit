---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer marketing · claude-opus-5-5 · high · 2026-10-22

# Review: marketing books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/marketing.md (body) + .agents/skills/marketing-design/ (SKILL.md, references/) + .agents/skills/marketing-craft/ (SKILL.md, references/ incl. image-review.md), working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer marketing (opus, high)
looked_at_first: [
  every book file read in full as it is now (role body, both SKILL.md, image-pipeline.md, image-review.md, channel-kits.md, handoffs.md) and the diffs of discovery-promise.md and channels.md; removed lines of the role and both SKILL.md walked against df13ff4; old image-pipeline.md read in full; cases.md, policy-rights.md, testing-measurement.md and evals/ without content change,
  universal-principles.md (UP-01..UP-20 with their marketing lines; UP-08 and UP-20 in full); matrix.md marketing column (135 ids, script-extracted) and the principle, apply and check of all 135 plus the 18 untagged findings the maker used, read against the books,
  my own V3 runs: both channel-kits §3 commands and all nine image-pipeline §4 commands extracted from the book text and run as written; synthetic samples: a 4 s 30 fps mp4 (two-frame white contact flash at 1000 ms, four one-frame white flashes in 2000-2433 ms, four full-screen saturated red flashes in 3000-3467 ms, a fading flash at 3667 ms), a 2 s mp4 with three quarter-screen 38->200 flashes in one second, a 48 kHz stem WAV with a hit at 1010 ms and a 500 ms short copy; a 1920x1080 scene (dark foreground frame, quiet background luma ~110 sd 4, bright hero with a thin pickaxe), traced part polygons and a coarse polygon; thumb_check.py thumbnail --mask and icon --mask on a crop with its cropped mask; vfx-craft measure.md §6 flash script on the same frame folders,
  tools/art/look_check.py and thumb_check.py --help; cv2 5.0.0, soundfile 0.14.0 installed,
  partner books: vfx-design SKILL.md:64, 68 (flash safety, sync), vfx-craft measure.md §6 (flash onsets IG-07), sound-design S-133 and review.md R-54, animation-design review.md G-04, art-direction platform-evolution-marketing.md §3, art-review feedback-briefs.md marketing row,
  roblox-creator-docs thumbnails.md:54, 220, 239; experience-icons.md:34, 80; content-maturity.md:21,
  job-card Fixed list and J018-D2..D4; stage2-brief-v2.md V1-V11; tool-modes.md,
  marketing-craft/evals/briefs.md E1 (read as the agent would at job start),
  reviews rev1 and rev2 (every finding re-checked below)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C1 (VR-26) + C3 + C8 V3, V6, V10; master UP-20 general check",
     where: ".agents/skills/marketing-craft/references/channel-kits.md:29 (frame command, flash count), :31 (what it sees), :42 ('flashes from the frame command: at most 3 in any second ... no saturated red flash at the listed times')",
     expected: "The flash line counts every large flash in any rolling second, the way the partner books count it (vfx-craft/references/measure.md §6: an onset is a frame where at least 10 % of the screen rises by 0.1 or more in relative luminance; vfx-design SKILL.md:64 'no saturated red flashes'; universal-principles UP-20 'count large-area flashes per second on the composite (at most 3)'), or says 'not verified' where it cannot",
     observed: "The command counts only frame-to-frame changes of the whole frame's mean grey of 50 levels or more. A full-screen saturated red flash on a dark frame changes the mean grey by about 38 levels, and a quarter-screen white flash by about 40, so neither is listed and the count reads low with no error. The red-flash clause then sends the agent to look 'at the listed times', which are exactly the times a red flash never appears in; with a budget of about 12 stills placed around beats and hits, a red strobe passes. The coverage row VR-26 records the same reliance on 'the listed times'",
     evidence: "my runs, command taken from the book text: (1) 4 s edit: listed changes [1000, 1067, 2000 ... 2433, 3667], 'most flashes in any 1 s 4.0'; the four red flashes at 3000-3467 ms (about 8 Hz) are absent; vfx-craft §6 on the same frames folder lists f0090_3000ms, f0094_3133ms, f0098_3267ms, f0102_3400ms as onsets. (2) quarter-screen edit: 'large changes of mean grey at ms []', 'most flashes in any 1 s 0.0'; vfx-craft §6 on the same folder: onsets at 333, 667, 1000 ms, 'most in any 1 s: 3'. Failure scenario: a creator's Short opens with a red strobe or a corner-to-corner flash burst; the marketing check records 'flashes PASS (0-1 per s)' and the edit goes to the owner as safe",
     smallest_fix: "Keep the frame command for the stills and their times. Count flashes with the partner's rule in one place: 'save the script of `vfx-craft/references/measure.md` §6 as `flash_pulse_vfx.py` in your scratch folder and run it on the frames folder the frame command wrote (same `f####_<ms>ms.jpg` names) with the edit's frame rate: at most 3 onsets in any 1 s, design for 2; look at the stills at every listed onset'; drop the flash print from the marketing command or label it 'whole-frame changes, for finding cuts'. Red: 'a saturated red flash stays not verified unless an analyser measures it; look at the stills at every onset §6 lists' (the partner's wording). If a red count is wanted in-book, this addition to the frame command ran right on both samples (red changes at 3000-3467 ms, 'most red flashes in any 1 s 4.0'): per frame also `((f[...,2].astype(int)-f[...,:2].max(2))>=100).mean()`, list the frames where that share changes by 0.25 or more, count them per second as for grey. Update coverage row VR-26 and proposals row (a) to match"}
  - {id: R1, class: recommendation, check: "C7 (practical) + kit hygiene",
     where: ".agents/skills/marketing-craft/references/channel-kits.md:29, :37 ('every frame is written'); role write scope .agents/roles/marketing.md:55 (default `knowledge/jobs/<job>/marketing/`)",
     expected: "Bulk measurement files land outside the repo; the job folder keeps only what a reviewer needs",
     observed: "The frame command writes one JPEG per frame of the whole edit into `<frames dir>`, which the book leaves open; the role's default write folder is inside the repo. A 60 s vertical Short at 60 fps is 3,600 stills per edit and per re-cut",
     evidence: ".gitignore ignores `output/`, not `knowledge/jobs/`; vfx-craft measure.md §6 keeps its script and folders in the scratch folder",
     smallest_fix: "One clause at :29: '<frames dir> in your scratch folder or under `output/` (git ignores it); copy only the stills you looked at into the job folder'"}
keep: [
  the staged key-art route written once in image-pipeline.md §1, with a check and an image budget per stage, the freeze after green light, the capped-brief rule and the new-game icon clause (rev2 R1),
  traced part masks checked on the overlay, the coarse-polygon rule, MR-07 and MR-08 naming their mask source,
  the fixed-cut squinted 3-value study that now sorts and checks its cuts and says what a cut is (rev2 F2),
  the crop command that refuses to stretch or pad; frame IoU for MR-04 and MR-28; per-variant --out-dir,
  MR-33 generation faults first; MR-04 keyword rows; MR-26 symbol square; MR-10 variant palette; MR-27 maturity line,
  the channel-kits §3 inputs: frames named with their own time, the onset command on the cutter's WAV without music, the length guard, the -17 to +40 ms window and its 'not verified' paths, the masking check on the full mix, the stills budget (all ran right in my runs),
  marketing-design §4 M-15..M-23 and §7 (all 20 principles, each with a marketing example and a named check),
  handoffs §7 (animator key pose) and §8 (named groups, magenta pass), consistent with the partner books,
  K-14 with the route a/b clause (rev2 R2) and the light-check pointers in role method 5 and K-16 (rev2 R3),
  image-review.md labels, 'I see stills', 'which lines run when', the fix order by layer, worked examples A and B,
  the proposals file (tool gaps from real runs, the video-and-audio tool row, recipe and workflow rows for G3, the animator and art-director rows adopted)
  ]
verdict: fix-first
</spec>
```

## Earlier findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev1 F1 black-fill on a coarse polygon | fixed (held) | IP §2 subject row, IP §4 parts and overlay commands ran (mask and `.overlay.png` written); coarse vs traced frame IoU 0.363 on my scene |
| rev1 F2 percentile 3-value study | fixed (held) | default cuts: dark 0.156, mid 0.834, light 0.010; the quiet background is one group |
| rev1 F3 crop stretches | fixed (held) | 900x1080 -> 512: rc 1 "never stretch"; box outside: rc 1; good box rc 0 |
| rev1 F4 generation-fault look | fixed (held) | MR-33, IP stage 3 check column |
| rev1 F5 RI-28, RI-07 checks | fixed (held) | MR-26 symbol square, MR-04 keyword rows |
| rev1 R1-R6 | fixed (held) | stage 6 and MR-29; route in one place; beat in DS §7 row 8 and CK §2-3; MR-27; capped-brief line; MR-10 |
| rev2 F1 video checks without inputs | partly fixed | frames, times, onsets, length guard, sync window, masking check and stills budget now real and right; the flash count is not (F1 above) |
| rev2 F2 3-value cuts unchecked | fixed | reversed cuts sorted to [85, 170]; one cut: rc 1 "give two cuts or none"; equal cuts: rc 1; the band-as-cut misuse prints its cuts [15, 85] and the reading rule at IP:78 names it |
| rev2 R1 icon plan | fixed | IP:10 stage 1 crop plan clause; IP:23 cap rule (8 = 1 + 3 + 3 + 1); CS K-14 |
| rev2 R2 K-14 final size | fixed | CS:64 route c / routes a/b clause |
| rev2 R3 budget written three times | fixed | role method 5 and K-16 are pointers to IR §1 |

## Results by check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | 135 rows checked, 1 failed | All 135 tagged ids have a row (script); 117 landings read against the library's principle, apply and check; the 18 rejections are sound (each names whose work it is and where marketing's side lands); the 18 untagged findings checked too. Failed: VR-26 (the flash-rate check is carried by a count that misses red and quarter-screen flashes: F1). CC-02 now passes (the sync check has real inputs and the partners' window) |
| C2 core principles | pass | `marketing-design` §7 (the skill loaded first) covers UP-01..UP-20 for marketing with an example and a named check each; no contradiction with the master (3-5 roughs meets "about 3"; tell, build, beat, peak, result); §1 says to re-read §4 and §7 after a compaction |
| C3 self-review | fail | F1: the flash line names an input that cannot show red or partial-screen flashes; every other line has a runnable input (all IP §4 commands, thumb_check and look_check modes and both CK §3 commands ran right on the real input types) |
| C4 kit rules and engine | pass | Docs claims re-read (thumbnails.md:54, 220, 239; experience-icons.md:34, 80; content-maturity.md:21); only real tool modes and flags (`--mask`, `--key`, `--compare`, `--compare-mask`, `--out-dir`, `--bottom-band` per --help); MR-27 defers to platform-policy; no rule, tool, template or workflow file changed |
| C5 nothing valuable lost | pass | Removed lines of the role and both SKILL.md walked: each kept, sharpened or moved (old generate details now live in `reference-images` §3-4; "separate icon and thumbnail briefs" is the stage 1 clause; "2-5 distinct honest concepts" in IP §3); the J016 pointer removed by the job card |
| C6 fixed rules | pass | Role frontmatter sha256 ad3a7e28... identical to df13ff4; SKILL.md 114 and 87 lines; descriptions 388 and 380 characters; no section renumbered (role "Before you hand back" unnumbered; DS §7, IP §4-5, HO §7-8 appended); J018 phrase in every changed header and the role comment; no library ids, transcript lines or "Riot" in bodies (CR- and UP- ids in channels.md, channel-kits.md and DS M-10/M-11 are the marketing paper's, unchanged; the Arcane case in cases.md is J012 text, unchanged); no tips section; evals/ unchanged; files LF in the working tree (`git ls-files --eol` w/lf; image-review.md 0 CRLF) |
| C7 better work | better, with one fix | See below |
| C8 brief v2 | fail | V3 and V10: F1. V1 inputs and budgets named (CK §3 stills budget, IR §1, IP §1 per stage); V2 real modes only; V4 MR-25 and MR-27 agree with platform-policy; V6 pass apart from F1's second flash rule (the mask-source clause appears in five places, all agreeing); V7 steps, rules and self-check before byte 13,600 in both SKILL.md; V8 brief fields, partner asks and review lines; V11 animator and art-director rows adopted, no other row targets these books |

## Better work?

Yes. On E1 (lighthouse game: titles, an icon and 3 thumbnail concepts, 8 images at most) the old books gave one generate-measure-review loop with `--box` subjects. The new books give a box-art brief (the launched thing, the sell list, the premise, the message and its symbol, the keyword table, the crop plan), a labelled warm-up, two rough rounds (thumbnail and icon, at least 3 each) under the 8-image cap, traced hero masks checked on an overlay, every rough judged at tile size, and a reasoned pick at G1 that names the goal. Every measuring path on the image side gave right answers in my runs, and the wrong-input cases stop with an error. The video side is now usable: frames named with their time, sound onsets from the cutter's WAV, the partners' sync window and honest "not verified" paths. One weak spot remains. The flash count misses the two flash types that matter most for safety, and the book tells the agent to look for red flashes at times where they never show (F1). The fix is a pointer to the partner's flash script, which already reads the same frame folder. Smaller risks: the stage 1 cell is dense and must be read slowly, and tracing a mask per rough is real work; the overlay check keeps it honest.
