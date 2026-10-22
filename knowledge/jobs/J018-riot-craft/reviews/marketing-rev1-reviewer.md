---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer marketing · claude-opus-5-5 · high · 2026-10-22

# Review: marketing books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/marketing.md (body) + .agents/skills/marketing-design/ (SKILL.md, references/) + .agents/skills/marketing-craft/ (SKILL.md, references/, new image-review.md), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer marketing (opus, high)
looked_at_first: [
  all changed book files read in full (role body, both SKILL.md, image-pipeline.md, image-review.md, handoffs.md, channel-kits.md, discovery-promise.md and channels.md diffs),
  git diff df13ff4 on every book file (removed lines walked one by one; old image-pipeline.md read in full),
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20 and their marketing lines),
  matrix.md marketing column (135 findings, script-extracted) and the principle / apply / check of all 135 from the topic files,
  tools/art/thumb_check.py and look_check.py --help; templates/marketing/thumbnail-icon-checklist.md; templates/skill/art-bible.md THUMBNAIL LOCK,
  reference-images SKILL.md §4-§7; animation-design/references/game-timing.md §6-§7; modeling-craft handoffs (magenta pass); art-review R-14,
  roblox-creator-docs production/publishing/experience-icons.md:34,80,105 and thumbnails.md:54,150,220,239,277,
  my own V3 runs (synthetic 1920x1080 scene: dark foreground frame, quiet mid background with noise sd 4, bright hero with pickaxe; 8-point hero polygon): polygon-mask, mirror/grey, 3-value, frame IoU, crop, grid and profile commands as written in image-pipeline.md §4; thumb_check.py thumbnail --mask and icon --mask; look_check.py silhouette --mask --compare-mask,
  marketing-craft/evals/briefs.md E1 (read as the agent would at the start of the job)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C3 + C8 V3 (SS-02, UP-05),
     where: ".agents/skills/marketing-craft/references/image-review.md:25 (MR-08) with image-pipeline.md:35 (subject row: 'a coarse polygon ... 8-20 points; coarse is fine at tile size') and :64 (polygon command)",
     expected: "MR-08 judges the image's real silhouette in black-fill (SS-02: 'fill the figure with one dark value'; master UP-05 marketing line: 'the icon reads in black-fill at 150x150'): the signature item and headgear break the outline, nothing is a sliver",
     observed: "On routes a and b (every ChatGPT image, the usual case) the only mask the book makes is the agent's own coarse 8-20 point polygon, and MR-08 reads 'the sheet's mask panel'. That panel shows the agent's drawing, not the image: whether the pickaxe is a sliver or the plume breaks the outline depends on how the agent drew the polygon. The check passes or fails by construction, with no error",
     evidence: "my run: 8-point polygon round a hero with a round head, a thin body and a thin pickaxe; thumb_check thumbnail --mask -> sheet mask panel is one wedge-shaped blob (round head and thin handle gone), component_count 1, largest share 1.0; the true outline would show a thin diagonal sliver for the pickaxe. Only route c (magenta hero pass) gives a real black-fill",
     smallest_fix: "In MR-08 (and one clause in image-pipeline.md:35): 'A coarse polygon mask serves MR-07 and MR-12 only; its panel is my drawing, not a black-fill. For MR-08 on a generated image, trace a tight outline mask (follows the head, every limb, the signature item and headgear) and check it on a 50 % overlay on the master before judging; or judge MR-08 on route c's magenta pass. Label the line with the mask source.' Add the overlay as one short command in §4 (Image.blend of master and mask). The existing proposal for a flat-rough family stays the long-term fix"}
  - {id: F2, class: blocking, check: C8 V3 (VC-02, VC-04, VC-17, WL-25),
     where: ".agents/skills/marketing-craft/references/image-pipeline.md:66 (3-value command), used by image-review.md:34 (MR-13) and the green-light stage image-pipeline.md:14",
     expected: "A 3-value study shows the image's real value groups: a quiet, close-valued background reads as one group; a calm image shows a narrow range, a dramatic one a wide range (M-19, MR-12 tone)",
     observed: "The command cuts at the 33rd and 66th percentiles of the image's own values, so every study has three equal-area groups whatever the picture does. A quiet background that covers more than a third of the frame is split into dark, mid and light bands, so MR-13's 'quiet close-valued background' fails on a good image, and a flat image looks as structured as a dramatic one. No error",
     evidence: "my run: background sd 4 around value 100 (60 % of the frame); whole-image p33/p66 = 96/101; inside that background the study gives 40 -> 16 %, 128 -> 44 %, 220 (the 'light' group, the hero's value) -> 40 %. The quiet background reads as noisy and as bright as the hero",
     smallest_fix: "Fixed cuts on luminance, not percentiles: dark below 85, mid below 170, light above (or the art bible's value ladder when it has one), and print the share of each group; in MR-13 read the shares against the plan. Re-run worked example A after the change"}
  - {id: F3, class: blocking, check: C5 + C8 V3,
     where: ".agents/skills/marketing-craft/references/image-pipeline.md:68 (crop command), stage 10 :19, image-review.md:47 (MR-22); old rule df13ff4 image-pipeline.md:13 ('never stretch (Roblox stretches non-16:9 uploads)')",
     expected: "Crops keep the master's proportions; the old 'never stretch' rule is kept or replaced by something at least as good",
     observed: "The only crop command crops a box and resizes it to W x H with no aspect check, so a box whose ratio differs from the destination is silently squashed. 'Never stretch' is gone from the new route. thumb_check cannot catch it: the stretched result is square and >= 512, so every master check passes",
     evidence: "my run: box 700,200,1500,900 (800x700) -> 512 512: rc 0; thumb_check icon --mask on it: master square true, min_512 true, all_met true; the hero is squashed by 1.14 with no warning",
     smallest_fix: "In the crop command, exit with an error when (X1-X0)*H != (Y1-Y0)*W (one assert); add 'never stretch: the crop box has the destination's aspect' to stage 10 and MR-22"}
  - {id: F4, class: blocking, check: C5,
     where: ".agents/skills/marketing-craft/references/image-review.md (no line); old rule df13ff4 image-pipeline.md:12 ('Your own look first: hands, object count, identity vs anchors, scale, fake UI, invented rewards, stray text, anything the game does not have')",
     expected: "The old first look for image-model failures is kept as a self-review line",
     observed: "Identity (MR-10), scale (MR-11), fake UI and rewards (MR-25) survive; hands, object count and stray text or glyphs survive only as examples in 'Regeneration vs a new option' (image-pipeline.md:25), with no step or MR line that looks for them. reference-images' own review (I-05) is written for model sheets and does not name them. Coverage table c says the old look was 'kept, split' but these three items were not",
     evidence: "grep of the books for hands / object count / stray text: only image-pipeline.md:17 (detail stage) and :25 (examples); checklist template I1-I14 has no item for them",
     smallest_fix: "Add one line before MR-06 (or a clause in MR-25): 'Generation faults on the full-size master, once per image: hands and fingers, object and character counts against the brief, stray letters, numbers or glyphs, merged or missing parts; a fault is a regeneration (max 2)'. Input: the master, 1 look"}
  - {id: F5, class: blocking, check: C1 + C3 (RI-28, RI-07),
     where: ".agents/skills/marketing-craft/references/image-review.md:14 (MR-01) and the coverage rows RI-28, RI-07",
     expected: "Each landed finding carries its runnable check. RI-28: 'the motif drawn as a one-colour black icon still reads at icon size (thumb_check.py icon on a black-fill motif)'. RI-07: 'every element in the first rough maps to a row of the keyword table, and no row is missing from the image'",
     observed: "Both land only as brief fields (MR-01: the brief names the symbol and has a keyword table). Nothing checks that the symbol reads as a one-colour icon at 150x150 or that the roughs carry the keyword rows",
     evidence: "coverage rows RI-28 and RI-07 point to DS §4 M-18, IP §1 stage 1, MR-01; MR-01's input is 'the brief file (0 images)'",
     smallest_fix: "MR-05 or MR-06 gains: 'each rough's elements map to keyword-table rows, none missing'; MR-26 (or a new MR line) gains: 'the message's symbol drawn as a one-colour black shape reads at 150x150 (thumb_check.py icon --key auto on the black-fill symbol)'"}
  - {id: R1, class: recommendation, check: C4 (tool reality),
     where: "image-pipeline.md:15 (stage 6, routes a/b: 'generate the final ... at final size (no small image upscaled later)') vs image-review.md:62 (MR-29: 'any upscale is recorded')",
     expected: "A rule the agent can keep on route a/b: the art bible's THUMBNAIL LOCK asks for a 'wide landscape composition made for a 16:9 crop', so the 16:9 master is a crop of the model's output and may be smaller than the 1920x1080 ideal (the docs say 'ideally', thumbnails.md:54)",
     observed: "Stage 6 forbids any upscale and says 'at final size' without defining it; MR-29 allows a recorded upscale. The old book said it honestly: record the final px size and whether it reaches 1920x1080; an upscale is recorded as one",
     evidence: "templates/skill/art-bible.md:75; df13ff4 image-pipeline.md:13",
     smallest_fix: "Stage 6: 'routes a/b: the largest 16:9 crop of the model's output, its px size recorded against the 1920x1080 ideal; an upscale only as a recorded pass with a 1:1 look (MR-29)'"}
  - {id: R2, class: recommendation, check: C8 V6 + C7 (length),
     where: "the stage list in .agents/roles/marketing.md:26 and :34, marketing-craft/SKILL.md:37 (step 5 a-k) and :62 (K-12), marketing-design/SKILL.md:96 and :107 (§7 rows 4, 15), image-pipeline.md §1; marketing-craft/SKILL.md:79 ('Every image and crop: MR-01..MR-32 run')",
     expected: "One rule, one place; the self-check scoped as image-review.md §1 scopes it (lines per stage, extra images only for the recommended option)",
     observed: "The eleven-stage route is spelled out in full in three places and summarised in three more; they agree today but will drift. SKILL §6 asks for all 32 MR lines on every image and every crop, while MR-01/MR-05 are per brief and per round and MR-28 only applies to the render",
     evidence: "line refs above",
     smallest_fix: "Keep the full list in image-pipeline.md §1; make craft step 5 and role method 3 one-line pointers ('big to small through the stages of image-pipeline.md §1; each stage frozen before the next'); SKILL §6: 'the MR lines of each stage on every candidate and crop, the full list on the recommended final'"}
  - {id: R3, class: recommendation, check: C2 + C8 V10,
     where: "marketing-design/SKILL.md:100 (§7 row 8) and marketing-craft/references/channel-kits.md:25 (opening-beat check)",
     expected: "The master's and the animator's grammar: tell, build, beat (held tension), peak or hit, result (universal-principles UP-08; animation-design/references/game-timing.md §7)",
     observed: "'tell, build, peak, result': the held beat is missing, so a re-cut that trims the beat before the hit passes the opening-beat check",
     evidence: "universal-principles.md:177; game-timing.md:68-70",
     smallest_fix: "Use 'tell, build, beat, peak, result' in both lines and list the beat's start time in the opening-beat check"}
  - {id: R4, class: recommendation, check: C1 (record accuracy),
     where: "coverage/marketing.md:297 (V4 paragraph) and :83 (MD-02 row)",
     expected: "The coverage file says only what the books hold",
     observed: "V4 says CD-01 (non-sexualised designs for a young audience) and CF-15 (gore in foreground elements) reached the books; neither appears (MR-27 covers sensitive acts through a prop motif only). MD-02 row says stage 8 states 'marketing art may carry more detail than the game model, never at the cost of the read'; image-pipeline.md:17 does not say it",
     evidence: "grep 'sexual|gore|more detail than' over the books: no hit",
     smallest_fix: "Add to MR-27: 'no sexualised pose or costume; no gore on any foreground element'; and either add the MD-02 clause to stage 8 or correct the row"}
  - {id: R5, class: recommendation, check: C7 (eval E1),
     where: "image-pipeline.md §1 image budgets; marketing-craft/SKILL.md §6",
     expected: "A rule for a brief whose image cap is smaller than the stage budgets (E1: 'Images allowed (max 8)' for an icon and 3 thumbnail concepts)",
     observed: "Stages 3-7 can spend 1-2 + 3-5 + 2-3 + 1-3 + 2-3 images; the book does not say what to cut when the brief caps them",
     evidence: "marketing-craft/evals/briefs.md E1",
     smallest_fix: "One line under the stage table: 'When the brief caps images below the stage budgets, spend them on the earliest open stage and stop at its gate; never thin the round below 3 roughs to reach a later stage'"}
  - {id: R6, class: recommendation, check: C1 (SI-18),
     where: "image-review.md:27 (MR-10)",
     expected: "A skin or event version is the launched thing with its own palette; the same character in a new scene keeps the base palette",
     observed: "MR-10 asks the hero's colours to match the approved anchor images, which fails a skin variant whose new palette is the point",
     evidence: "SI-18 check: palette change matches the recorded type",
     smallest_fix: "MR-10: '... match the approved anchors of the version shown (a skin: its own anchors and palette; the base character: the base palette)'"}
keep: [
  the staged route in image-pipeline.md §1 with checks and image budgets per stage, and the freeze after green light,
  hero masks instead of --box, the subject_share_of_frame-first reading and the inverted-mask warning,
  frame IoU (not aligned IoU) for MR-28 and the layout half of MR-04,
  per-variant --out-dir, the crop-mask rule, the real-layout mock and the grid,
  image-review.md labels (measured / looked / art-director / game-designer / owner-confirmed / not verified) and the honest 'I see stills' line,
  marketing-design §4 M-15..M-23 and §7 (all 20 principles, each with a marketing example and a named check),
  handoffs §7 animator key pose (consistent with game-timing.md §6) and §8 staged render with named groups and magenta pass,
  worked examples A and B, channel-kits §3 video checks, the 'problem behind the note' rule (role method 8),
  the proposals file (tool gaps found by real runs, recipe and workflow rows for G3)
  ]
verdict: fix-first
</spec>
```

## Results by check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (3 of 135 rows) | All 135 tagged findings have a row; 117 landings opened and read. Rows failed: SS-02 (F1: the black-fill check is circular on polygon masks), RI-28 and RI-07 (F5: check not carried). The 18 rejections have sound reasons. Record errors in R4 |
| C2 core principles | pass | `marketing-design` §7 covers UP-01..UP-20 for marketing with example and check; no contradiction with the master; the beat is missing from row 8 (R3) |
| C3 self-review | fail | MR-08 cannot do its job on routes a/b (F1); RI-28 and RI-07 checks missing (F5); every other checkable finding has an MR line or a channel-kits §3 check with a named input |
| C4 kit rules and engine | pass | Docs lines cited in discovery-promise.md checked (experience-icons.md:80, 105; thumbnails.md:239, 277); every thumb_check / look_check flag the books name exists (--help); no rule, tool or workflow file changed; final-size wording (R1) |
| C5 nothing valuable lost | fail | 'never stretch' (F3) and the first look for hands, counts and stray text (F4) lost; everything else kept, sharpened or moved; the J016 pointer removal follows the job card |
| C6 fixed rules | pass | Frontmatter sha256 identical (ad3a7e28...); SKILL.md 114 and 87 lines; descriptions 388 and 380 chars; no renumbered sections; J018 phrase in every changed header and the role comment; no library ids, transcript lines or Riot names in bodies (CR-01..08 and UP-10 in channels.md are the marketing paper's ids, unchanged; cases.md unchanged); no tips section; evals/, cases.md, policy-rights.md, testing-measurement.md unchanged. `sync_harness.py --check` shows generated copies out of date: expected before the lead's sync |
| C7 better work | better, with fixes | See the judgment below |
| C8 brief v2 | fail | V3: 3-value command (F2) and crop command (F3) give wrong answers with no error; mask panel used as black-fill (F1). V1 inputs and budgets named; V2 real modes only; V4 MR-25 agrees with platform-policy; V6 duplication (R2); V7 steps, rules and self-check before §7 with a compaction pointer; V8 brief asks in handoffs; V10 animator and staged-render hand-offs consistent (beat wording R3); V11 animator row adopted, no other rows target these books |

## Better work?

Yes, clearly. With the old books an agent ran one generate-measure-review loop: no warm-up, no rough round from different hooks, no green light content, no value or light study, no crop family or layered master, and `--box` subjects that give silently wrong component counts. With the new books the agent briefs like box art (hero, sell list, premise, symbol, fans want, crop plan), makes a labelled warm-up and 3-5 distinct roughs judged at tile size, freezes the big shapes at green light, measures with real hero masks, and hands back every line labelled by what proved it. The weak spots are in the measuring layer, which the agent will trust: the black-fill panel on a polygon mask (F1), the percentile 3-value study (F2) and the stretching crop (F3) each give a confident wrong answer, and the image-model fault look was dropped (F4). All five blocking fixes are a few lines each. After them, length is the main risk (R2): the route is written out in three places.
