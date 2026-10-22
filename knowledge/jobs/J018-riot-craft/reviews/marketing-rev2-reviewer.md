---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer marketing · claude-opus-5-5 · high · 2026-10-22

# Review: marketing books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/marketing.md (body) + .agents/skills/marketing-design/ (SKILL.md, references/) + .agents/skills/marketing-craft/ (SKILL.md, references/ incl. image-review.md), working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer marketing (opus, high)
looked_at_first: [
  every book file read in full as it is now (role body, both SKILL.md, image-pipeline.md, image-review.md) and the diffs of handoffs.md, channel-kits.md, discovery-promise.md, channels.md against df13ff4; old image-pipeline.md read in full; evals/, cases.md, policy-rights.md unchanged, testing-measurement.md changed only in line endings,
  universal-principles.md (UP-01..UP-20 and each marketing line); matrix.md marketing column (135 ids, script-extracted); the principle, the marketing apply sentences and the check of all 135 findings plus the 12 untagged ones the maker used,
  my own V3 runs on a synthetic 1920x1080 scene (dark foreground frame, quiet background luma ~110 sd 4, bright hero: round head, body, thin pickaxe): every IP §4 command extracted from the book text and run as written (traced-parts mask, overlay, mirror/grey, 3-value with default, moved, reversed and bible-band cuts, frame IoU, crop good/stretched/outside, grid, real-layout mock, profile with and without sRGB ICC); thumb_check.py thumbnail --mask and icon --mask on a crop with its cropped mask; MR-26 symbol square with --key auto; look_check.py silhouette --mask --compare (key-pose black-fill) and --compare-mask; palette --mask --roles,
  a 30-frame synthetic mp4 to test whether the CK §3 video checks can be run with what is installed (cv2 yes; ffmpeg, imageio, av no; tools/vfx/clip_metrics.py reads frame folders only),
  tools/art/*.py --help, tool-modes.md, stage2-brief-v2.md V1-V11, job-card Fixed list and J018-D1..D5,
  partner books: animation-design game-timing.md §6-§7, sound-design S-133, vfx-design SKILL sync and flash rows, art-review art-bible.md §7, modeling-craft handoffs (magenta pass), art-review feedback-briefs.md marketing row,
  roblox-creator-docs production/promotion/content-maturity.md:21 (uploaded images moderated whatever the label),
  marketing-craft/evals/briefs.md E1 (read as the agent would at job start),
  review rev1 (every finding re-checked below)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C3 + C8 V1, V2 (CC-02, VR-26; also the frame checks for UP-08, CD-09, CD-15, WT-24, UI-16, SD-21)",
     where: ".agents/skills/marketing-craft/references/channel-kits.md:25 (opening-beat check), :27 (sound stays in sync), :28 (flash count)",
     expected: "Every self-review line names an input the agent can produce with our tools and its stills budget (V1); a measure the tools lack is a manual check with a 'not verified' path plus a proposal row (V2). Partner books state the same sync check with its fallback: 'measured on the target device, else not verified' (vfx-design SKILL.md:66, animation-design game-timing.md:44, sound-design review.md R-54)",
     observed: "The three checks run on 'the edit's frames, stepped at its frame rate' and 'stepped frames ... with its audio waveform', but no book says how to get those frames or that waveform, gives no stills budget, and the sync line has no 'not verified' path. No kit tool reads a video or its audio (tool-modes.md has none; clip_metrics.py needs a frame folder and a fixed camera); ffmpeg is not installed, so no installed library can read an mp4's audio. No proposal row asks for the tool. The coverage V3 table runs none of the CK §3 checks",
     evidence: "my run: cv2 (installed) steps a synthetic 30 fps mp4 into f###_<ms>.jpg frames and per-frame mean luma ([38 x10, 248, 248, 38 ..., 248, ...]: the two flashes are plain), so frames and the flash count are reachable with one short command the book does not give; audio: `which ffmpeg` none, imageio/av not installed, cv2 has no audio path; soundfile (installed) reads WAV only. Failure scenario: the owner hands over a creator's 20 s Short; the agent cannot produce the frames the check names, or looks at a few screenshots and writes 'sync PASS' with no audio evidence",
     smallest_fix: "In channel-kits.md §3 add one short command (run and checked by me): `python -c \"import sys,os,cv2;v,o=sys.argv[1:3];os.makedirs(o,exist_ok=True);c=cv2.VideoCapture(v);r=c.get(cv2.CAP_PROP_FPS);L=[(cv2.imwrite(os.path.join(o,'f%03d_%dms.jpg'%(i,round(i*1000/r))),f),int(cv2.cvtColor(f,cv2.COLOR_BGR2GRAY).mean()))[1] for i,(k,f) in enumerate(iter(c.read,(False,None)))];print('fps',r,'frames',len(L),'mean luma per frame',L)\" <edit.mp4> <frames dir>` (frames named with their ms; a full-screen flash is a rise and fall of the mean luma: count them per second). Add a budget: at most about 12 stills looked at (2-3 around each beat of the opening action and each checked hit). Sync line: input = the edit's audio exported as WAV by whoever cut it (onset read with soundfile next to the contact frame's ms); without it, or for device sync, 'not verified' (the sound designer's window). Add a proposal row for a video-and-audio mode in the kit tools"}
  - {id: F2, class: blocking, check: "C8 V3 (VC-02, VC-17, WL-25)",
     where: ".agents/skills/marketing-craft/references/image-pipeline.md:69 (3-value command, its 'or the art bible's value ladder as CUT1 CUT2') and :78 (reading rule), used by image-review.md:36 (MR-13)",
     expected: "Every input path the book names gives the right study or stops with an error",
     observed: "The default cuts work (round-1 F2 is fixed). But the book offers 'the art bible's value ladder as CUT1 CUT2', and the bible has no ladder of cut points: its §7 'Value bands' row gives per-layer ranges in percent grey-view value and linear luminance (environment 15-85 % (0.020-0.69)). The command takes any two integers as 0-255 grey levels, does not sort them and does not check units, so following the book gives a wrong study with no error and no near-cut warning",
     evidence: "my runs on the scene (quiet background luma ~110, 82 % of the frame): default cuts -> dark 0.156, mid 0.827, light 0.017 (right); cuts '15 85' (the bible's environment band as written) -> dark 0.0, mid 0.156, light 0.844, near-cut 0.0: the quiet background reads as the light group, as bright as the hero; cuts '170 85' (reversed) -> dark 0.017, light 0.156: the dark frame is reported as light and the .3value.png is inverted; one cut '100' -> light 0.0 with no error. art-review/references/art-bible.md §7 'Value bands' row",
     smallest_fix: "In the command: `c=sorted(int(v) for v in sys.argv[2:4]) or [85,170]` and stop unless two cuts are given; in the text: 'cuts in grey levels 0-255 of the luminance image; use the defaults unless the art bible names 3-value cut points in grey levels (its value bands are per-layer ranges in percent, not cuts)'"}
  - {id: R1, class: recommendation, check: "C7 + C5 (old craft step 5 'separate icon and thumbnail briefs')",
     where: "image-pipeline.md:10 (stage 1 crop plan), :19 (stage 10), :86 (example A: icon square cut from the thumbnail master) vs :90 (example B: a new game's icon designed on its own); marketing-craft/SKILL.md:64 (K-14 'one master feeds the whole kit'); marketing-design/SKILL.md:51 (M-04 icon = identity, thumbnail = one moment)",
     expected: "The agent knows when the icon gets its own brief and thumbnail round (identity: a new game, example B) and when it is a crop of the key-art master (an update or event), so E1 ('icon and 3 thumbnail concepts', max 8 images) has a clear plan",
     observed: "The route plans the icon as one crop of the master; example B designs it separately; nothing says which applies. On E1 the cap rule stops at the thumbnail round's gate, so an agent following K-14 reports the icon 'not done', while the template (`thumbnail-brief.md` header '<icon | thumbnail>') still implies one brief per type",
     evidence: "marketing-craft/evals/briefs.md E1; templates/marketing/thumbnail-brief.md:11",
     smallest_fix: "One clause in stage 1: 'A new game's icon (identity, M-04) is its own brief and joins the thumbnail round as its own roughs; an update or event icon is a crop of the master, still judged for identity at 150x150 (MR-22)'"}
  - {id: R2, class: recommendation, check: "C7 (residual of rev1 R1)",
     where: "marketing-craft/SKILL.md:64 (K-14 '... make finals at final size')",
     expected: "The same rule as stage 6 and MR-29 (routes a/b: the largest crop of the model's output, its size recorded against the ideal; an upscale only as a recorded pass)",
     observed: "K-14 still says 'make finals at final size' without the route a/b clause that stage 6 (image-pipeline.md:15) and MR-29 now carry",
     evidence: "image-pipeline.md:15; image-review.md:64",
     smallest_fix: "K-14: '... finals at final size (route c) or the largest crop of the model's output with its size recorded (routes a/b, `image-pipeline.md` §1 stage 6)'"}
  - {id: R3, class: recommendation, check: "C8 V6",
     where: ".agents/roles/marketing.md:36 (method 5), marketing-craft/SKILL.md:66 (K-16), image-review.md:6 (§1 first bullet)",
     expected: "One rule, one place",
     observed: "The light-check budget (numbers for every candidate, one sheet each, extra images only for the recommended option and failures) is written out three times; they agree today",
     evidence: "line refs above",
     smallest_fix: "Keep it in image-review.md §1; role method 5 and K-16 become pointers ('light checks and budgets: `image-review.md` §1 and `image-pipeline.md` §1')"}
keep: [
  the staged route written once in image-pipeline.md §1 with checks and budgets per stage, the freeze after green light and the capped-brief rule,
  traced part masks checked on the new overlay, the coarse-polygon warning, MR-08 judged only on a real outline,
  the fixed-cut, squinted 3-value study with its near-cut share; the crop command that refuses to stretch or pad,
  MR-33 generation faults first; MR-04 keyword rows; MR-26 symbol square; MR-10 variant palette; MR-27 maturity line (agrees with content-maturity.md:21 and defers to platform-policy),
  hero masks instead of --box, subject_share_of_frame read first, frame IoU for MR-28, per-variant --out-dir,
  marketing-design §4 M-15..M-23 and §7 (all 20 principles with a marketing example and a named check; the beat now in row 8),
  handoffs §7 (animator key pose, consistent with game-timing.md §6) and §8 (named groups, magenta pass),
  image-review.md labels, 'I see stills', 'which lines run when', the fix order by layer,
  worked examples A and B (updated for masks, the value study and the symbol),
  the proposals file (tool gaps from real runs, recipe and workflow rows for G3, the art-director V11 row adopted)
  ]
verdict: fix-first
</spec>
```

## Round 1 findings: status

| Rev1 id | Status | Evidence |
| --- | --- | --- |
| F1 black-fill on a coarse polygon | fixed | IP §2 subject row, IP §4 parts and overlay commands (both run: mask and `.overlay.png` written), MR-07/MR-08 name the mask source |
| F2 percentile 3-value study | fixed (new edge in F2 above) | default cuts keep the quiet background in one group (mid 0.827) |
| F3 crop stretches | fixed | 800x700 -> 512: rc 1 "never stretch"; box outside the image: rc 1; good box rc 0; stage 10 and MR-22 say "never stretch" |
| F4 generation-fault look lost | fixed | MR-33 (image-review.md:24), stage 3 check column |
| F5 RI-28, RI-07 checks | fixed | MR-04 keyword rows; MR-26 symbol: my run, symbol square `--key auto` -> measured, `component_count` 1 |
| R1 final size | fixed in stage 6 and MR-29; residual in K-14 (R2 above) | |
| R2 route in three places | fixed | role method 3, craft step 5 and K-12 are pointers; SKILL §6 scoped by `image-review.md` §1 |
| R3 the beat | fixed | DS §7 row 8, CK §2 step 1, CK §3 opening-beat check |
| R4 coverage claims | fixed | MR-27 (sexualised, gore in every layer); stage 8 MD-02 clause (image-pipeline.md:17) |
| R5 capped briefs | fixed | image-pipeline.md:23 |
| R6 skin palette | fixed | MR-10, stage 1 brief field; `palette --mask --roles` runs |

## Results by check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | 135 rows checked, 2 failed | All 135 tagged ids have a row (script); 117 landings compared with the library principle and check against the books read in full; 18 rejections sound (each names whose work it is and where marketing's side lands). Failed: CC-02, VR-26 (rule carried, but the check's input cannot be produced: F1) |
| C2 core principles | pass | `marketing-design` §7, the skill loaded first, covers UP-01..UP-20, each with a marketing example and check; no contradiction (3-5 roughs meets the master's "about 3"); compaction pointer in §1 |
| C3 self-review | fail | F1: the video checks name frames and a waveform the agent has no route to; every image line has a runnable input (all IP §4 commands and tool modes ran on the real input type) |
| C4 kit rules and engine | pass | Only real tool modes; MR-27 agrees with content-maturity.md:21 and platform-policy; sync window and flash limit match the partner books; roster efforts in the hand-off briefs match the role files; no rule, tool or workflow file changed |
| C5 nothing valuable lost | pass | Every old line walked (table c checked against df13ff4); "never stretch", the fault look and the upscale record restored; the icon-brief point is a clarity gap (R1), the template still holds it |
| C6 fixed rules | pass | Role frontmatter identical to df13ff4; SKILL.md 114 and 87 lines; descriptions 388 and 380 characters; no section renumbered (new §7, §4-§5, §7-§8 appended); J018 phrase in every changed header and the role comment; "Riot" only in headers (and the unchanged J012 case in cases.md); CR-/UP- ids in bodies are the marketing paper's, unchanged; no tips section; evals/ unchanged; testing-measurement.md line endings only; generated copies wait for the lead's sync |
| C7 better work | better, with fixes | See below |
| C8 brief v2 | fail | V1/V2: F1; V3: F2 (all other commands right, and they stop loudly on wrong sizes); V4 pass; V6: R3; V7 pass; V8 pass (brief fields, partner asks, review lines); V10 pass; V11 pass |

## Better work?

Yes. With the old books the agent ran one generate-measure-review loop with `--box` subjects and no rough round. With these books, on E1 it writes a box-art brief (hero, sell list, premise, symbol, keyword table, crop plan), labels a warm-up, makes 3-5 roughs from different hooks, traces real hero masks and checks them on an overlay, judges at tile size, picks with reasons, and freezes the big shapes at a green light with a value study, light set-ups and safe squares. Every line is labelled by what proved it, and the measuring layer that misled in round 1 now gives right answers on the default paths. Two weak spots remain. The video checks read well but cannot be run as written (F1). The 3-value study can still be given wrong cuts in a way the book itself suggests (F2). Both are a few lines each. After them, the main risks are the unstated icon plan on a capped new-game brief (R1) and the density of the stage table, which the agent must read slowly.
