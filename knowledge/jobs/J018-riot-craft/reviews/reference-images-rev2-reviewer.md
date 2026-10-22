---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer reference-images · claude-opus-5-5 · high · 2026-10-22

# Review: reference-images books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/skills/reference-images/ (SKILL.md; references/prompt-patterns.md; new references/rounds.md and references/self-review.md; no evals/, no role file: shared skill), working tree on top of 034dce9, compared with df13ff4, 2026-10-22
reviewer: J018 reviewer reference-images (opus, high), round 2
looked_at_first: [
  the four book files read in full; git show df13ff4:.agents/skills/reference-images/SKILL.md; git diff df13ff4 -- .agents/skills/reference-images/,
  reviews/reference-images-rev1-reviewer.md (F1-F6, R1-R6 re-checked one by one against the current text),
  knowledge/reference/craft/riot/universal-principles.md (UP-01..UP-20: every picture/2D line and general check), matrix.md reference-images column (script: 176 tagged IDs), the library entries of RI-06, SI-01, SI-09, CD-01, CD-22, RI-01, LC-05,
  templates/skill/art-bible.md (families table and every LOCK block: CHARACTER, PROP and MODEL REF fix a three-quarter view; CREATURE and POSE SHEET fix none; CONCEPT fixes the gameplay camera),
  art-review/references/art-bible.md:69 (Separation targets row: character 1.5:1), art-review/references/look-check.md §5 lines 1-9, art-review/references/exploration.md:26-27, :78-79, marketing-craft/references/image-pipeline.md:12, :68-69, :78, modeling-design SKILL.md:33 and reference-check.md, every role file line that points to reference-images, knowledge/jobs/J009-art-director/decisions.md J009-D17,
  tools: look_check.py --help and value, contrast, silhouette, palette, thumb --help; thumb_check.py --help; art_refs.py --help; tool-modes.md,
  V3 runs by me (scratchpad ri_rev2/): C1 silhouette --key-tol 16 on 7 real generated references (DestructionSimulator content/art/refs: character, model, prop); the full C12 recipe exactly as written (contrast --sample for the ground hex, the composite one-liner, value --mask) on 5 real references against a green, a sand and a mid-grey ground; C3 on the same 5; palette --roles on a real reference; art_refs.py --bible templates/skill/art-bible.md print on a warm-up row and the book's two option-row examples,
  no evals/briefs.md exists for this skill: C7 read as the agent at the start of a typical job (a starter pet for a pet game, for the modeler; then a key-pose round for the animator)
  ]   # the coverage and proposals files were read after the books
earlier_findings (rev1):
  - {id: F1, status: fixed, evidence: "I-11 (SKILL.md:75), rounds.md:36, prompt-patterns.md:32 and :73, rounds.md:87, self-review.md:41 now use the game-camera angle only where the lock leaves the camera open; my art_refs print of the character option row shows no camera words under 'front three-quarter view', the pose option row's angle sits under the POSE SHEET LOCK, which fixes no view"}
  - {id: F2, status: fixed, evidence: "RO5 (self-review.md:42) records C3 as information only and measures C12, the rough on the game's ground. My run of the C12 recipe as written: the same approved king character gives 1.87 (white backdrop) and 2.02 (grey backdrop) on a green ground, where C3 gave 2.82 and 1.41; the prop dh_p_camper 2.77 on green, 1.16 on sand (a true merge). The command runs, writes <id>.onground.png, its luminance image and JSON; silhouette.png is dark subject on white, so the composite polarity is right"}
  - {id: F3, status: fixed, evidence: "FN5 (self-review.md:59) looks at the asymmetric element; C4 (self-review.md:92) limits the IoU to front or side views and names <id>.mirror.png, which matches image-pipeline.md:68 (p[:-4]+'.mirror.png')"}
  - {id: F4, status: fixed, evidence: "rounds.md:35 (6-12 text hooks, 3-5 generated, cut ones with a reason), RO1, SKILL §4 R1 row, rounds §7, example A; agrees with exploration.md:26; coverage UP-14 row gives the reason for 3-5 generated"}
  - {id: F5, status: fixed, evidence: "FN11 three planes (self-review.md:65), FN6 grouped detail in a contrasting frame (:60), FN7 role shares summed by hue family (:61)"}
  - {id: F6, status: fixed, evidence: "P13, P14, P15, P18, P19 each carry an 'Example:' (SKILL.md:119-125)"}
  - {id: R1, status: fixed, evidence: "C1 false readings name the radial falloff with numbers (self-review.md:89)"}
  - {id: R2, status: fixed, evidence: "PK2 compares only the final in the pick's family and pose (self-review.md:49)"}
  - {id: R3, status: fixed, evidence: "FN5 top line, FN12 jump apex, FN9 swatch and edges, FN11 read order and saturation peak"}
  - {id: R4, status: accepted as is, evidence: "§6 starts at 18 245 bytes, §7 at 19 249, §8 at 20 300; SKILL.md:13 now asks to re-read §4, §6, §7 and §8 after a compaction; the maker kept the evidence column for its decision ids. Inside the V7 'roughly' with the re-read line"}
  - {id: R5, status: mostly fixed, evidence: "I-14, I-16, §7 and SKILL §3's last line point to rounds §3; the counts 6-12 / 3-5 sit in SKILL §4 R1 row, rounds §3 item 2, rounds §7 and RO1, all identical today"}
  - {id: R6, status: fixed, evidence: "SKILL.md:32 art-director row: 'checks that images from all roles look like one game (`art-review`)'"}
findings:
  - {id: R7, class: recommendation, check: "C3 + C8 V1 (a pass line whose input is often missing, with no rule for what happens then)",
     where: "self-review.md:42 (RO5 measured pass on C12), :48 (PK1 'options that passed RO4 and RO5'), :100 (C12 'no ground capture yet: the bible's ground swatch, else NOT REVIEWED'), rounds.md:43",
     expected: "When C12 cannot run, the book says how RO5 and the pick sheet proceed; every input C12 names exists in the kit",
     observed: "Neither templates/skill/art-bible.md nor art-review/references/art-bible.md has a ground swatch, so for a game's first characters (no capture yet) the fallback input does not exist; C12 is then NOT REVIEWED, RO5's measured half cannot pass, and PK1 admits only options that 'passed RO4 and RO5'. An agent may drop every option or silently skip the line",
     evidence: "grep -i ground: no swatch row in either bible file; art-review/references/art-bible.md:69 defines only ratios",
     smallest_fix: "C12: 'no ground capture yet: sample the ground from the approved concept key art (the game-designer's `concept` image), else NOT REVIEWED'. RO5: 'C12 NOT REVIEWED: the option goes on the sheet with \"separation not measured\" under it, and the looked-at grey half decides'"}
  - {id: R8, class: recommendation, check: "C7 + C8 V12 (a worked example in a form the round's own rules and checks do not cover)",
     where: "rounds.md:95 (example C: 'One `pose` row: exactly 3 options of the contact moment, left to right'); against rounds.md:36 (item 3 'one chat each (I-12)'), prompt-patterns.md:73 (pose option example 'Exactly 1 key pose'), self-review.md:39-40 (RO2 'C5 aligned IoU' between option images; RO3 'one chat each')",
     expected: "Pose options are made one way in the book, and RO2 runs on that form",
     observed: "Example C puts three options in one image; the option row and rounds §3 item 3 make one image per option. On the one-sheet form C5 has no second image, so RO2's measured pass cannot run as written. The one-sheet form is cheaper and gives equal finish by construction, so it is a fair choice; the book just does not say so",
     evidence: "rounds.md:95 vs :36; look_check.py silhouette --help: --component N measures one listed component on its crop",
     smallest_fix: "rounds §3 item 6: 'a signature move's 2-3 readings may share one `pose` image (exactly N, one per reading); RO2 then compares the C1 components (silhouette --component N) or is looked at'. Or make example C three rows"}
  - {id: R9, class: recommendation, check: "C8 V3 (a known-limits line missing for the input form the book prescribes)",
     where: "self-review.md:100 (C12 false readings)",
     expected: "The known limits name the hole fill: C1 fills key-coloured regions inside the outline by default, and the composite keeps those pixels",
     observed: "Enclosed backdrop gaps (between an arm and the body, inside a handle loop) are mask-black after C1's hole fill, so the composite keeps them in the backdrop grey and value counts them as subject. On real references the filled area was 0.5-7.4 % of the subject (villain_soft_a 7.4 %, dh_p_camper 5.7 %). Small for a median, but it moves a borderline ratio toward the backdrop's value with no error",
     evidence: "silhouette --key-tol 16 key_estimate.filled_area_px / area_px on 7 real references; look_check.py value --help (--keep-holes)",
     smallest_fix: "C12 false readings: 'C1's hole fill keeps enclosed backdrop gaps in the copy as subject (up to about 7 % of the subject on real references); for a borderline ratio re-run C1 with --keep-holes before the composite and look at the copy'"}
keep: [
  the R0-R3 rounds with the pick between two batches and 'Who generates' intact,
  the image brief fields with the size players see the subject and its source, the card, the variant line and the keep / try lists (rounds §1),
  6-12 text hooks before 3-5 generated roughs, with cut hooks given a reason (now the same step as the art director's exploration),
  the camera-words rule per family (rounds §3 item 3), which removes the lock conflict and still checks the game-camera read at R3 (FN13) on named inputs or NOT REVIEWED,
  C12: separation measured on the game's ground with existing tool modes, tested by me on real references (backdrop-independent where C3 was not),
  FN5's looked-at asymmetry and the mirror copy as fresh eyes; C4's IoU limited to front and side views,
  FN7 role shares summed by hue family, FN6 grouped detail, FN11 three planes and read order,
  the per-next-maker final table, paint-overs as one-change edits of the exact capture, the edit forms and the new prompt-pattern rows,
  every command with its silent thresholds and tested false readings (V14 labels, the eye check before any fix),
  §6 rule 5 and FN15 against platform-policy; the proposals file (view family, background clause, tool modes, the two G3 rows, the J009-D17 reading for the owner)
  ]
verdict: pass
</spec>
```

## Check results
| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass | 176 tagged IDs, all with a row (script); 8 rejections, each sound (lock or bible content, modeler's painting or mesh steps, motion captures). Landings re-opened for the 16 rows repaired in round 1 and 20 sampled rows: all carry the rule, and the checkable ones carry the check. 0 rows fail |
| C2 core principles | pass | §8 P1-P20 cover UP-01..UP-20, each stated for image making with an example and a check line; nothing contradicts the master (UP-07 and UP-11 'prompts carry' = the lock carries, which every prompt includes); UP-14's 3-5 generated has its reason |
| C3 self-review | pass | Every line names its input and runs with the kit tools; RO5 now measures the right thing (C12, tested); R7 asks for the missing-input rule |
| C4 kit rules and engine | pass | Rough-round camera words agree with the template locks and step 3; tool modes all real (help and tool-modes.md); Roblox frame sizes as checked in round 1; J009-D17 reading flagged for the owner at G3 |
| C5 nothing valuable lost | pass | The art-director 'one game' duty is back; every other old rule kept, moved or sharpened |
| C6 fixed rules | pass | Only the four books and the two job files for this skill; SKILL.md 128 lines; description 392 characters; no section or I-id renumbered (§8, I-14..I-19, prompt-patterns §8 appended); J018 phrase in all four headers; no library IDs, transcript lines or Riot names in bodies; no tips section; no evals/; LF only; templates/ and tools/ unchanged |
| C7 better work | better | See the judgment below |
| C8 brief v2 and v3 | pass | V3/V12 C12 re-run by me on real inputs; V14 labels on every command; V1 budgets per round; V2 real modes; V6 pointers (counts identical in four places); V7 re-read line; V10 hooks and counts agree with exploration.md and the modeler's views; V11 every partner row adopted or answered. Recommendations R7-R9 |

## Judgment (C7)
Read as the agent on a starter-pet job for the modeler, then a key-pose round for the animator: the old books gave a brief, a manifest, a prompt check, one image and a review against one list. The new books make the agent write the problem, the size players see the pet and a sell list first, build a board from real things, write 6-12 hooks and generate only the best 3-5 beside a labelled warm-up, judge each rough as a black-fill and grey at 60 px in the lock's own view, measure separation against the place the pet lives in rather than the generator's backdrop, pick with a goal question and reasons, ask the modeler what it needs, and hand over separate views, a material-ID image and intent notes. Round 1's misleading parts (a camera the lock forbids, a backdrop number deciding the pick, an asymmetry number that could not fail, a narrow search) are gone. The remaining weak spots are small: what to do when no ground sample exists yet (R7), pose options on one sheet versus one per image (R8), and one silent limit of the ground composite (R9).
