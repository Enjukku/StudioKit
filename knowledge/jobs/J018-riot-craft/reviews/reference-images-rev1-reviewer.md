---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer reference-images · claude-opus-5-5 · high · 2026-10-22

# Review: reference-images books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/reference-images/ (SKILL.md; references/prompt-patterns.md; new references/rounds.md and references/self-review.md; no evals/, no role file: shared skill), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer reference-images (opus, high)
looked_at_first: [
  the four book files read in full; git show df13ff4 of the old SKILL.md and prompt-patterns.md; git diff df13ff4 -- .agents/skills/reference-images/,
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20: every picture/2D line and every applies list),
  matrix.md reference-images column (176 IDs, script-extracted; all 176 have a coverage row) and the principle/apply/check/roblox_fit of all 176 plus the 12 untagged findings the maker used (script-extracted from the topic files, read in full),
  templates/skill/art-bible.md (families table and every LOCK block), knowledge/jobs/J009-art-director/decisions.md (J009-D14, J009-D17),
  tools: tool-modes.md; look_check.py --help and the silhouette, thumb, value, palette sub-commands; look_check.py source :80-100, :306-330, :513-545, :883-1000, :1115-1144; thumb_check.py icon --help; art_refs.py --help, print, approve,
  V3 runs by me (scratchpad/rev/): C1 at --key-tol 16 and 40 on 110 real generated reference images (DestructionSimulator content/art/refs: model, character, creature, prop, structure); C3 value on the 38 real model, character and creature refs; C4 mirror IoU on 22 real three-quarter refs and on a symmetric synthetic figure projected at 0 and 40 degrees; C5 aligned IoU on 7 real pairs; synthetic 1024x1536 figures on flat and radially lit light-grey backdrops (C1, C2 thumb with the scale rule, C3, C5); C11 art_refs.py --bible templates/skill/art-bible.md print on a warm-up row and the book's option-row example,
  partner books: art-review/references/exploration.md §3 and §8, art-review/references/look-check.md §5 lines 1-9, art-review/references/feedback-briefs.md §6, marketing-craft/references/image-pipeline.md §4, modeling-design SKILL.md step 2 and reference-check.md, film-craft storyboards.md; every role file line that points to reference-images,
  roblox-creator-docs: production/publishing/experience-icons.md:34, :55; thumbnails.md:54,
  no evals/briefs.md exists for this skill: C7 read as the agent at the start of a typical job (a starter pet for a pet game, character for the modeler; then a paint-over note)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: "C4 + C7 (the rough round contradicts the locks and the book's own step 3 in the common case)",
     where: "SKILL.md:75 (I-11 'The game-camera angle and the read-first part are must-haves'), prompt-patterns.md:32 (§1a rough-options row 'Say: ... the game-camera angle') and :73 (§5 option row 'seen from the game camera's angle', example 'seen from behind and above'), rounds.md:86 (example A, R1 on the `character` lock); against SKILL.md:55 (step 3: 'When the identity has to contradict its lock (a back view under a three-quarter lock), stop') and self-review.md:99 (C11 false reading)",
     expected: "Every rough option can be generated without its identity fighting its family's lock (I-01, step 3), or the book says which view a rough uses under each lock",
     observed: "The CHARACTER LOCK ('Full body, front three-quarter view'), PROP LOCK ('three-quarter view') and MODEL REF LOCK ('one three-quarter view') fix the view. The option pattern makes 'seen from the game camera's angle' (behind and above for third-person, the default the brief example uses) part of every rough. So every character or prop rough round either breaks step 3 and I-01 (the identity overrides the lock) or stops at step 3. The worked example A runs R1 on the `character` lock with roughs judged 'at the 60 px viewport' from behind and above, then reports at R3 that the three-quarter lock blocked the back view: the same conflict is accepted at R1 and refused at R3",
     evidence: "My run: art_refs.py --bible templates/skill/art-bible.md print on the book's own option-row example prints 'A small round puppy with big ears; seen from behind and above' directly above 'CHARACTER LOCK: ... Full body, front three-quarter view', rc 0, no warning (the book's C11 lists this as a silent case). Template lines 39, 47, 51",
     smallest_fix: "I-11, §1a rough row and the §5 option row: 'the game-camera angle where the family's lock allows it (concept, environment, thumbnail, pose); under a three-quarter lock (character, prop, model) the rough keeps the lock's view and the game-camera read is judged at R3 on the game-camera-angle view (view family, proposals row 1) or on the modeler's game-camera render'. Make example A and the option-row example agree (drop 'seen from behind and above' from the `character` rough, or name a family whose lock allows it)"}
  - {id: F2, class: blocking, check: "C3 + C8 V3/V12 (a pass threshold that measures the generator's backdrop, used to split the pick sheet)",
     where: "self-review.md:42 (RO5 'subject/ring ratio at or above 1.5 (PROPOSAL)' with input 'C3 (flat-ground: against the backdrop)'), :48 (PK1 'options that passed RO4-RO5'), rounds.md:43 (§4 'options that failed are listed under it with their failing numbers, never shown as equals')",
     expected: "A number that decides which options reach the pick sheet measures the subject's read, not a property of the image model's backdrop (V14: a screening number is never the verdict on its own)",
     observed: "On flat-ground roughs the C3 ring is the lock's plain grey backdrop, whose grey the image model picks per image (0.42 to 0.99 luminance in real refs). The ratio is set by that backdrop: a light or mid-value subject (cream pet, gold, white fur, the typical saturated mid-tones) fails 1.5 although it separates well from the game's ground, and a dark subject always passes. Failing options are then shown below the sheet as losers. C3's false-reading column names the limit ('against the backdrop, not against the game's ground'), but RO5 still uses it as a pass line; art-review/references/look-check.md §5 line 1 lists a flat-key ratio as 'wrong with no error'",
     evidence: "My runs (look_check.py value --key-tol 16): the same approved king character 2.82 on a white backdrop (king_model) and 1.41 on grey (king_model_hp2, ring p50 0.513): pass vs fail by backdrop only; the whole king series king_model_p3..p8 sits at 1.52-1.65; golem 3.28 on white vs 2.00 on grey. Synthetic cream pet on flat light grey: 1.00 (fail); the same subject pixels pasted on a green game ground (70,120,50): 4.10",
     smallest_fix: "RO5: record the backdrop ratio as information only (no pass line on flat-ground roughs); pass = looked at on the real-size grey row: the read-first part holds the strongest value step inside the subject, and the subject's grey next to the art bible's ground value still separates. PK1 and rounds §4 split the sheet on RO4 and that looked-at RO5. Add the king numbers to C3's false readings"}
  - {id: F3, class: blocking, check: "C3 + C8 V12 (a measured pass that is true for every three-quarter image)",
     where: "self-review.md:59 (FN5 'measured: mirror IoU below 0.95 when an asymmetric element is asked'), :92 (C4)",
     expected: "The asymmetry check can fail: a design with no asymmetric element scores at or above the threshold on the input the book prescribes (finals under the three-quarter locks)",
     observed: "A three-quarter view of a fully symmetric design is not mirror-symmetric in the image, so every final under the CHARACTER, PROP and MODEL REF locks passes FN5's asymmetry number with no error, and nothing else in FN5 looks for the asymmetric element (its 'looked at' clause names only the identifying elements). C4's false readings name only the widened-box case",
     evidence: "My runs (silhouette --key-tol 16 --compare <mirror>): 22 real three-quarter refs (model, character, creature) 0.742-0.880, all below 0.95; a symmetric synthetic T-pose figure: front view 0.993, the same figure turned 40 degrees 0.834",
     smallest_fix: "FN5: the asymmetric element is 'looked at: named and visible at real size'; use C4's IoU only on front or side views and say so in C4's false readings ('a three-quarter view of a symmetric design scores 0.74-0.88'). Keep the mirror copy as a fresh-eyes look on the pick and each final (this also gives CR-09 the self-review line its coverage row claims). Fix C4's file name: the mirror command writes `<stem>.mirror.png`, not `<img>.mirror.png`"}
  - {id: F4, class: blocking, check: "C8 V10 + V11 + C2 (a partner's adopted proposal not carried; UP-14 count changed without a reason)",
     where: "SKILL.md:49 (§4 R1 row), rounds.md:33-40 (§3 items 1-2), self-review.md:38 (RO1); coverage/reference-images.md:314 ('proposals/art-director.md row 1 ... adopted'), :230 (UP-14 row)",
     expected: "The art director's adopted row: 'hooks written first (6-12, the warm-up labelled), 3-4 kept with one radical'; the partner book already rebuilt runs the same step (art-review/references/exploration.md:26 'Write 6-12 one-line hooks ... Hooks are text and cost no images'); UP-14 picture/2D: '6-12 rough options across directions [inference]'",
     observed: "R1 goes straight to 3-5 generated roughs. The cheap text step (6-12 hooks, keep the best 3-5) is missing, so other roles run a narrower search than the art director for the same kind of round, and the selection the library asks for (RI-16 roblox_fit: 'the risk is too little selection, not too little output') happens among 3-5 ideas instead of 6-12. The coverage row says 'adopted' and the UP-14 row gives no reason for 3-5",
     evidence: "exploration.md:26 vs rounds.md:35; proposals/art-director.md:25; universal-principles.md:287",
     smallest_fix: "rounds §3 item 2: 'write 6-12 one-line hooks first (text, no images), each from a different source with its fiction line; keep the 3-5 strongest for generation, one radical'; RO1: 'hooks written: 6-12; generated: 3-5'; one line in SKILL §4 R1 row; correct the coverage rows"}
  - {id: F5, class: blocking, check: "C1 (coverage rows whose landing does not carry the finding)",
     where: "coverage/reference-images.md:54 (CF-15), :181 (VC-14), :72 (LC-04); self-review.md:60 (FN6), :61 (FN7), :65 (FN11)",
     expected: "CF-15 (three depth groups: foreground frames, midground carries, background unifies; grey shows three planes), VC-14 (detail materials grouped in close values, framed by a contrasting base) and LC-04 (main, support and accent colours near 60/30/10, after the greys work) each have the rule and a check where the row says, or a rejection with a reason",
     observed: "CF-15 lands on SKILL §6's gore rule (only the gore clause of the library check) and on FN11, which has no depth-group clause. VC-14 cites FN6 'value structure; grouped detail framed'; FN6 has no grouping or framing clause. LC-04 cites FN7 'palette roles and shares'; FN7 and its pass check role swatches by ΔE and the reserved-hue share, never the role shares (C8 already reports per-cluster shares)",
     evidence: "self-review.md:60, :61, :65 text; library check lines CF-15 'Grayscale: three value planes are visible (dark FG, mid subject, low-contrast BG)', VC-14 'the detail cluster sits inside a narrow value band ... the frame's median is clearly different', LC-04 'area share of the top three colours near 60/30/10'",
     smallest_fix: "FN11 (concept, thumbnail, storyboard): 'depth reads in three planes: a darker foreground frame, the subject in the midground, a quiet background (looked at on the grey; C7 shares)'. FN6: 'the detail materials of one part sit in close values inside a contrasting frame'. FN7: 'role shares from C8 near the bible's split (starting value 60/30/10, sum clusters by hue family)'. Or reject a row with a reason; correct the three coverage rows"}
  - {id: F6, class: blocking, check: "C2 (owner spec: each principle with its own example and check)",
     where: "SKILL.md:119 (P13), :120 (P14), :121 (P15), :124 (P18), :125 (P19); the section's own line :105 'Each has an example from our work'",
     expected: "Every principle in §8 stated for image making with its own example and its check (J018-D1/D2 point 2)",
     observed: "P13, P14, P15, P18 and P19 have a check but no example; the other fifteen have both. The principles themselves agree with the master (one count differs: F4)",
     evidence: "SKILL.md:119-125",
     smallest_fix: "One example line each (for example P13: 'the pet brief names the 60 px read and the sell list before the first prompt'; P14: 'rounds §8 A: warm-up, four hooks from four sources, the radical lost on the pet read'; P15: 'the candle pup was dropped at the pick and not reproposed'; P18: 'the concept stopped once the modeler had no shape or colour questions'; P19: 'a common egg's reveal frame never wears the legendary trim')"}
  - {id: R1, class: recommendation, check: "C8 V3 (a known-limits line that is wrong for one backdrop form)",
     where: "self-review.md:89 (C1 false readings: 'a strong gradient or vignette gives invalid-mask at 16')",
     expected: "The known limits name the vignette case that stays silent",
     observed: "A radial studio falloff (lighter behind the subject, darker corners) leaves the border flat enough for the auto key, and the lighter centre becomes subject. C1 reports one component (the expected count, so FN1 never looks at it) while the mask swallows background; C2's scale, C5 and FN14 then use the wrong box. Real generated refs I measured have flat backgrounds (border vs side within about 5 grey levels on 110 images), so this is rare: add it to the limits",
     evidence: "Synthetic 1024x1536 figure, --key-tol 16, verdict 'measured', count 1 each time: centre 236 to corners 206: box 729 px wide (true 301), IoU vs the clean image 0.79; centre 240 to 200: box the whole frame 1024x1536, area_frac 0.36; centre 232 to 220: correct (IoU 1.0)",
     smallest_fix: "C1 false readings: 'a radial falloff whose centre is more than about 16 levels lighter than the border keys the centre as subject with no error (count still 1): look at the black-fill once per image before using C2, C5 or FN14; re-run at 40'"}
  - {id: R2, class: recommendation, check: "C3 (a false fail across a lock change)",
     where: "self-review.md:49 (PK2 'IoU of final vs pick at or above 0.85 ... a pose sheet or a new view is not compared')",
     expected: "The exclusion also covers a final in another family or pose than the pick",
     observed: "The `model` final (MODEL REF LOCK: T- or A-pose) is not a new view, so an agent compares it with the `character` pick (neutral pose) and gets a fail with no error; the screening rule catches it on the eye check, at the cost of a look",
     evidence: "Real same-character iterations: king_model_hp vs king_model_p8 0.75, king_model_p3 vs king_model_p4b 0.80",
     smallest_fix: "PK2: 'compare only the final in the pick's family and pose (the look target); a model reference, pose sheet or new view is not compared'"}
  - {id: R3, class: recommendation, check: "C1 + C3 (partial landings: the rule is in a pattern, the claimed check line does not carry it)",
     where: "coverage rows SS-09 and CF-09 (FN11 does not apply to the `prop` family), SS-11 (FN12 has no jump-apex clause), MD-08 (PK2 has no swatch clause), VH-09 and LC-22 (no read-order or saturation-peak clause), MD-03 (FN9 has 'muddy', not 'every edge hard')",
     expected: "Each checkable finding has its check in a line that runs on that family",
     observed: "The rules sit in prompt-patterns §5 or rounds §5 only",
     evidence: "self-review.md:63, :65, :66, :49",
     smallest_fix: "FN5: 'one clear top line (props, vehicles)'; FN12: 'a jump apex tucks the legs'; PK2 or FN9: 'a new look material had its swatch approved first'; FN11: 'the read order primary, secondary, tertiary holds on the grey at real size; saturation peaks at the focal point'"}
  - {id: R4, class: recommendation, check: "C8 V7",
     where: "SKILL.md:13 (re-read list), §6 at byte 18 008, §7 at 19 012-20 161",
     expected: "Steps, rules and self-check in about the first 18 KB, or the re-read line covers what falls past it",
     observed: "§6 rules and §7 self-check sit just past 18 KB; §1 asks to re-read §4, §7 and §8 after a compaction, not §6",
     evidence: "byte offsets measured on the file",
     smallest_fix: "Add §6 to the re-read line, or shorten the §5 Evidence column (move the long evidence to prompt-patterns §1b)"}
  - {id: R5, class: recommendation, check: "C8 V6 + C7 (one rule in many places)",
     where: "the rough-round rule (warm-up, 3-5 hooks, one radical, equal finish) at SKILL.md:42, :49, :80, :82, :99, :120; rounds.md §3; self-review.md RO1, RO3; prompt-patterns.md §1a, §5",
     expected: "One place for the rule, pointers elsewhere",
     observed: "Ten restatements; F4 will have to be fixed in each of them, which shows the drift risk",
     evidence: "the lines above",
     smallest_fix: "Keep the rule in rounds §3 and RO1; make SKILL §3 last line, I-14, I-16, §7 and P14 one-line pointers"}
  - {id: R6, class: recommendation, check: "C5",
     where: "SKILL.md:32 (§3 art-director row); old df13ff4 SKILL.md:26",
     expected: "The old row's duty 'checks that images from all roles look like one game (art-direction, art-review skills)' kept or moved",
     observed: "Dropped; FN10 covers each maker's own image only. The coverage table calls the row 'sharpened' and lists no loss",
     evidence: "git diff df13ff4 -- .agents/skills/reference-images/SKILL.md",
     smallest_fix: "Add 'checks that images from all roles look like one game (`art-review`)' back to the art-director row"}
keep: [
  the round structure R0-R3 with the pick between two image batches and the 'Who generates' pending route kept intact,
  the image brief with problem, constraints, the size players see the subject with its source, sell list, read-first, card, variant line, story facts (rounds §1),
  the two-half research board with one observed property per real entry and one outside-games source (rounds §2),
  the per-next-maker final table (modeler hand and Tripo, rigger, animator, vfx) with intent notes instead of settings (rounds §5),
  paint-overs as one-change edits of the exact capture, with the note restated as its problem and a default marked capture inside a budget (rounds §6),
  the edit forms in prompt-patterns §3 and the new §5 rows (view, material-ID, variant with slot fill, mannequin variant, colour vignette),
  prompt-patterns §8 words that make the subject specific,
  the light-check budget table and the per-batch counts (rounds §7),
  C2's scale rule from C1's box (tested: 60 px on a 1151 px box gives 53x80, sheet right panel nearest x4), C5 as 'shape change only' (real pairs: different characters 0.58-0.71, same character 0.75-0.995), the --key-tol 16 start value (on real refs 40 split single figures into 2-5 components where 16 kept 1),
  FN14's scale-free area ratio instead of area_frac,
  §6 rule 5 (maturity, culture, cruelty to a prop motif, true tiers) and FN15,
  the proposals file, including the view family, the background-clause fix and the two G3 rows
  ]
verdict: fix-first
</spec>
```

## Check results
| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail | 176 tagged rows checked, all present; 3 rows fail (CF-15, VC-14, LC-04: F5); 7 partial landings (R3); 8 rejections sound |
| C2 core principles | fail | §8 covers UP-01..UP-20 with no contradiction; 5 principles lack an example (F6); UP-14's 6-12 options narrowed to 3-5 without a reason (F4) |
| C3 self-review | fail | RO5 passes or fails on the backdrop (F2); FN5's asymmetry number passes every three-quarter image (F3); the rest runs with the kit tools on the named inputs |
| C4 kit rules and engine | fail | rough-round angle vs the three-quarter locks and step 3 (F1); tool modes all real; Roblox frame sizes match the docs; platform-policy diff agrees |
| C5 nothing valuable lost | pass | one duty dropped from the art-director row (R6); every other old rule kept, moved or sharpened |
| C6 fixed rules | pass | only the four books changed for this skill; SKILL.md 128 lines; description 392 characters; sections and I-ids not renumbered (§8 and I-14..I-19 appended); J018 phrase in all four headers; no Riot names, library IDs or transcript lines in bodies; no tips section; no evals/; LF line endings |
| C7 better work | better, after F1-F4 | see the judgment below |
| C8 brief v2 and v3 | fail | V3/V12 (F2, F3), V10/V11 (F4), V7 and V6 (R4, R5); V1 budgets named; V2 no invented modes; V4 policy diff done; V13 measures point to the partner books instead of copying them |

## Judgment (C7)
Read as the agent starting a starter-pet job for the modeler: the old books gave a brief, a manifest, one prompt check, one generation and a review against I-05. The new books make the agent write the problem, the size players see the pet and a sell list before any prompt, build a board from real things, separate a warm-up from distinct hooks, judge every rough as a black-fill and grey at 60 px, pick with a goal question and reasons, ask the modeler what it needs, and hand over separate views, a material-ID image and intent notes. That is clearly better work. The weak spots are where a number or a pattern would mislead it: every character rough asks for a view its lock forbids (F1), light pets lose at the pick on a backdrop number (F2), the asymmetry check cannot fail (F3), and the search is narrower than the art director's for the same kind of round (F4).
