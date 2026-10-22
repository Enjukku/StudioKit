---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer art-director · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: art-director books, round 3

Scope: `.agents/roles/art-director.md` (body), `.agents/skills/art-direction/` (SKILL.md, references), `.agents/skills/art-review/` (SKILL.md, references; not evals), working tree on 2026-10-22 (books saved 05:56-05:58, coverage 06:00), against df13ff4 and against rounds 1 and 2 (`reviews/art-director-rev1-reviewer.md`, `reviews/art-director-rev2-reviewer.md`). I read all 14 book files in full before the coverage table, then the diff against df13ff4 (headings, frontmatter, descriptions), `coverage/art-director.md` (all sections, with the repair-round-2 table), `proposals/art-director.md`, every other role's proposal row that names these books, the partner lines that point into them, the library lines of the findings I opened, `matrix.md` (by script) and the eval briefs. I ran every command line and tool mode the books name on synthetic inputs in my scratchpad (`ad-rev3/`, script `make_samples_adrev3.py`). I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/art-director.md (body) + .agents/skills/art-direction/** + .agents/skills/art-review/** (not evals) @ working tree 2026-10-22 (after repair round 2)
reviewer: J018 reviewer art-director (opus, high), round 3
looked_at_first: [all 14 book files in full (role body; art-direction SKILL, clarity-cohesion, identity-variants, worked-examples, platform-evolution-marketing, precedents unchanged; art-review SKILL, self-review, look-check, exploration, art-bible, feedback-briefs); look_check.py value -h and the value / compare_subjects / contrast JSON layout; thumb_check.py thumbnail and icon -h; art_refs.py -h; synthetic inputs: a 1600x720 environment-only frame (saturated sky and a clipped sun above row 200, a far band, saturated decoration above head height, a calm player band, a varied near floor), the same with a busy far band, with a 30x30 pure-black patch, with a reserved-red patch, with a red enemy and its black-fill; a UI-off cut (a character, a 10x10 white accent and its black-fill) and the same with a 200x100 white sign; a busiest frame with a white HUD bar and a red health bar; in-scene hero frames (legs the ground's colour; dark legs) with magenta mask captures; 600x900 magenta flat-key renders (dark legs, equal legs, a little darker legs); a slam frame with a core, a banner and a torch; a 1920x1080 thumbnail with a hero mask]
findings:
  - id: R1
    class: recommendation
    where: "art-review/references/self-review.md:39 (Direction round row: RD1-RD5, CL1-CL3); art-direction/SKILL.md:42 (§3 step 5 'the layers keep their bands'); art-review/references/exploration.md:29 (§3 item 4 'layers keep their bands')"
    expected: "Every line the direction-round row names can run on what a direction round has: generated roughs (no layer cuts, no environment-only capture) and, at step 9, the greybox captures."
    observed: "After repair round 2, RD3 and CL1 take only the environment-only capture and RD5's clipped half only the UI-off cut. A generated rough has neither, so on every direction round these lines are NOT REVIEWED, and the 'layers keep their bands' claim in step 5 and EXP §3 item 4 has no named measure. The agent fails safe (NOT REVIEWED, no wrong number), but the band and reserved-hue read of the options, which the lock asks for ('no reserved hue on decoration'), is left to eye."
    evidence: "Self-review §1 'a line whose input is missing is NOT REVIEWED'; RD3 input (line 66), CL1 input (line 102: 'never a frame with characters, effects or the HUD'); LK §2 'A box is safe only when every pixel in it belongs to what you measure' (look-check.md:53) already gives the route: a box fully inside one layer of the rough."
    smallest_fix: "Direction-round row: 'on roughs, RD3 and CL1 as diagnostics on sample boxes fully inside the environment (LK §2 safe box); the environment-only versions run on the DR11 greybox captures'; step 5 and EXP §3 item 4 name the same."
  - id: R2
    class: recommendation
    where: "art-review/references/self-review.md:76 (RD13 pass 'lower p50 ÷ upper p50 at or below the bible's ratio'); look-check.md:107 ('0.078 on a dark-legged render (pass at about 0.7)'); art-bible.md:68; against clarity-cohesion.md:52 ('the lower body a little darker and cooler')"
    expected: "The check matches the standard it proves: the lower body 'a little darker' (about 0.6-0.7 of the upper body's luminance median, the modeler's VL2 and the library's 15-20 % default), and the upper body 'more contrasted' as the RD13 look-for column says."
    observed: "'At or below' makes the target a ceiling: a near-black lower body passes, and the tested note teaches 0.078 as a pass. The 'more contrasted' half has no pass value. Not a regression (round 2 passed any difference) and the ground half still catches dark legs on dark ground, so this is a sharpening, not a fault."
    evidence: "My run (line 1 region masks + value --mask): flat render with legs (60,60,80): lower ÷ upper 0.083 → pass; legs equal to the upper body: 1.0 → fail; legs (170,150,125): 0.553 → pass. CC §3 Character value and VC-08 principle both say 'a little darker'."
    smallest_fix: "RD13 pass: 'lower ÷ upper about 0.6-0.7 (the bible's value); far lower (starting value below 0.4, PROPOSAL) is a finding unless the bible's character card asks for it; upper p5-p95 spread wider than lower'; line 1's tested note calls 0.078 'darker than the band', not 'pass'."
  - id: R3
    class: recommendation
    where: "art-review/references/look-check.md:107, :119, :124, :135 ('repair round 2', 'Tested (repair round 2)'); self-review.md:65 (RD2 'lines 2'); self-review.md:17 (DR2 list); feedback-briefs.md:112 (C2 JSON path)"
    expected: "Book bodies speak to a future job, not to this one; small references resolve exactly."
    observed: "(a) Four tested notes say 'repair round 2', a J018 process term a later agent cannot place (the header already records the round). (b) RD2 'lines 2'. (c) DR2's pass list omits 'one named unexpected element' that EXP §7 requires (RI-23's check). (d) C2 says 'read subjects.<name>.luminance.p95'; the JSON path is `measurements.compare_subjects.subjects.<name>.luminance.p95` (found and correct in my run, so only a pointer slip)."
    evidence: "grep of the lines; slam-c2.json from my run: core p95 0.639 highest, rank_by_median core, torch, banner."
    smallest_fix: "Replace 'repair round 2' with 'Tested:'; 'line 2'; DR2 adds 'one named unexpected element'; C2 path 'measurements.compare_subjects.subjects.<name>.luminance.p95'."
keep: [Every round-2 finding is fixed and checked (table below): every environment measure (band, near-black, depth contrast, saturation field, reserved hues) now names the environment-only capture in the capture-kinds table, the self-review lines, K19-K20, §5 lines 4, 5, 8 and 9, P3 and the worked example, each line listing the frame that still holds characters, effects or the HUD as its 'wrong with no error' case; clipped white runs on the UI-off cut below the horizon with the accents excluded, so the HUD and the sun no longer fail a clean frame; the bible's §7 Separation targets row (1.5:1, 3:1) is the one place RD6, RD13 and CL15 read; the lower-body ratio has a real value; MK2 and LK §2 carry --size-source; the direction packet answers the game designer's six concept-art questions (EXP §3 item 5, DR5, role file, WE §1); one image cap per round including regenerations; one anchor count (BIB §7); headers DR1-DR11 and FB1-FB8; the C2 brightness check reads p95 of named boxes. Kept from rounds 1-2: the direction stages (research board, hooks with the warm-up, 3-4 equal-finish roughs with one radical, grey and black-fill before colour, owner sheet of the 2-3 that passed, cheap proof in the engine), the bible §7 standards, the partner ask table with what the art director gives first, the cold read and the fixed big-to-small order, the job-type table at the top of self-review §3, the paint-over budget, LK §2 mask rules, identity-variants.md, core principles P1-P20 without P8 and P19.]
verdict: pass
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass | 307 rows: all 277 findings tagged art-director in `matrix.md` have a row (script: none missing; 30 extra = 10 untagged + 20 UP rows); 22 rejections, each with a sound owner or duplicate reason (unchanged from round 2). Opened in depth this round: 39 finding rows (every row repair round 2 touched: VC-05, VC-07, VC-08, WL-25, LC-01, LC-17, LC-18, CD-04, RI-19, RI-21, plus 29 others, 22 of them drawn at random) and 2 UP rows, against the library's principle, apply and check lines; plus the 21 other rejection reasons = 62 rows checked, 0 failed. Partial but acceptable: VC-08 (R2), RI-23 (DR2 list, R3), LC-17 ("small share on focal spots" has no measure), WL-20 (high setting not noisier). |
| C2 core principles | pass | `art-direction` §7 (the skill the role file loads first) covers UP-01..07, 09..18, 20 with an example and a check each; UP-08 and UP-19 correctly not the art director's, their picture lines kept as EVT1 and IV §5 / ID6. P3's check now names the environment-only and mask captures (round-2 F1 closed). No contradiction with `universal-principles.md` (unchanged since round 2). |
| C3 self-review | pass | Every line names its input; the job-type table maps each recipe to K rows and lines. RD3, RD5, RD9, RD13, CL1, CL9 now give the right answer on their named inputs (runs below). The direction-round row names three lines whose inputs a rough cannot have: they fall to NOT REVIEWED, safe but thin (R1). |
| C4 kit rules and engine | pass | No conflict with AGENTS.md, rules, or the job card's decisions; recipe and workflow changes stay proposal rows (G3); no recipe, workflow, template or tool file changed (git status). Engine claims unchanged since round 2 and still hold (one sun per place, post effects under Lighting or the Camera, thumbnail bottom band, badge and pass circles). Every tool mode and flag exists (`value --exclude --min-ratio --tolerance-source --compare-subjects --name`, `thumb_check thumbnail --size-source --bottom-band`, `art_refs print/run/approve`). |
| C5 nothing valuable lost | pass | Round-2 edits replace weaker lines with stronger ones (RD13 any-difference → a ratio; RD10, CL1, CL9, RD9 → the inputs that can prove them; anchor counts → one pointer). The coverage file's §c and repair tables match the diff. Earlier small losses accepted in round 2 stand. |
| C6 fixed rules | pass | Only the role body, the two skills and the two job files are this maker's (other modified files are other makers' and the lead's `crew.md`, `job-card.md`); frontmatter byte-identical to df13ff4; SKILL.md 137 and 86 lines; descriptions 389 and 383 characters; LF; no section renumbered (headings only appended); the J018 header phrase in every changed file and the role comment; no library IDs, transcript lines, Riot names or "tips" section in bodies (the one "transcripts" hit, CC:85, is the first game's source note); evals and precedents.md unchanged. |
| C7 better work | yes | See below. |
| C8 brief v2 | pass | V1 inputs named; image budgets per round (regenerations inside the cap) and for paint-overs. V2 real modes only. V3: every command line and mode ran and wrote its files; each right on its named input; the wrong-with-no-error cases are written into the lines. V4 paid random tiers defer to `platform-policy`. V6 bands, ΔE, separation targets and the anchor count each in one place (BIB §7). V7 §5-§7 re-read named at AD:21 (§5 starts at 17.2 KB, §7 at 19.7 KB). V8 findings became the bible §7 sheet, the partner ask table, K19-K25 and the self-review. V10 consistent with the environment designer (VB-a 1.5:1 and 3:1 and the bible pointer, near-black 0.004 = 5 %, VB4 reserved share with the bible's distance), the modeler (VL2 0.6-0.7), VFX, marketing and UI pointers to BIB §7 (all six outside pointers resolve). V11 every other role's row against these books adopted or supported with a reason, including the environment designer's late rows 27, 28, 35, 36. |

## Commands run (C8 V3)

| Line or mode | Input | Runs | Files written | Right answer | Wrong number with no error when |
| --- | --- | --- | --- | --- | --- |
| `silhouette` → §5 line 1 region masks → `value --mask` (RD13 upper vs lower) | three flat-key renders | yes | `.silhouette.png`, region masks, JSON | dark legs 0.083, equal legs 1.0, a little darker 0.553 | the pass is a ceiling (R2) |
| §5 line 1 "Lower body against the ground": `value <scene> --mask lower --exclude upper --min-ratio 1.5 --tolerance-source` | in-scene frames + mask captures | yes | JSON with verdict | ground-coloured legs 1.0 fail; dark legs 2.14 pass | a flat-key render (the book says so) |
| §5 line 4 reserved share | environment-only; with a red patch; with a red enemy, excluded and not | yes | `.reserved.png` | 0; 900 px (0.00078); 0 with the enemy excluded; 4000 px without | characters, effects or HUD in the frame (the line says so) |
| §5 line 5 chroma bands (boxes) | environment-only | yes | stdout JSON | above 140.0, player 0.0 | sky in the upper box (the line says so) |
| §5 line 8 band and depth bands | environment-only, calm and busy far band | yes | JSON | calm far spread 0.038 < near 0.216 (pass); busy far 0.784 > near 0.213 (fail) | characters in the near rows (the line says so) |
| §5 line 9 near-black on environment-only; clipped on the UI-off cut below the horizon, accent excluded | env with black patch; UI-off cut; with a white sign; busiest whole frame | yes | `.extremes.png` | 900 px near-black; 0 clipped; 20 000 px (0.024) with the sign; the busiest whole frame 0.0156 (the false fail the line now avoids) | HUD or sky in the box (the line says so) |
| §5 line 2 squint + `contrast --sample` | slam frame | yes | `.squint.png`, JSON | blur 6 px, core 3.77 | a box crossing an edge (the line says so) |
| §5 lines 3, 6 (mirror, contact sheet) | slam, env, busy | yes | `.mirror.png`, `sheet.png` 2400x720 | yes | — |
| §5 line 7 `thumb --mask --size 800x360` | in-scene frame + black-fill | yes | thumb, sheet, JSON | scale 0.5 | — |
| FBK §5 C2 `value --compare-subjects --box --name` | slam frame | yes | JSON | core p95 0.639 highest | path wording only (R3) |
| `thumb_check.py thumbnail --size --size-source --bottom-band 20 --mask` (MK2) | 1920x1080 + mask | yes | sheet, JSON | measured, bottom_band present | — |

## Round-2 findings

| Round 2 | Status now | Evidence |
| --- | --- | --- |
| F1 environment measures on composed or single-cut captures (blocking) | fixed | LK §1 Environment-only row names RD3, RD9, CL1, CL9, K19-K20, lines 4-5, 8-9; SR RD9, CL1, CL9 inputs `env`; K19, K20; lines 4, 5, 8 list the contaminated frame as the no-error trap with numbers; AD §7 P3 check; WE §2 step 2 CL1 on the environment-only capture; my runs above |
| F2 clipped white counts HUD and sky (blocking) | fixed | SR RD5 (UI-off, below the horizon, accents excluded); LK §5 line 9 input split; K19; WE §2 step 2; my run: 0 on the clean UI-off cut, 0.024 with the sign |
| F3 separation targets row (V11) | fixed | BIB §7 Separation targets; RD6, RD13, CL15 point to it; coverage V11 round 2 |
| F4 RD13 upper-vs-lower bar | fixed (sharpening left: R2) | RD13 ratio, BIB §7 Value bands |
| F5 MK2 missing --size-source | fixed | SR MK2, LK §2; my run |
| F6 six concept-art questions | fixed | EXP §3 item 5, DR5, role file game-designer row, WE §1 step 6 |
| F7 regeneration budget wording | fixed | EXP §8, AD §3 step 4, DR9 |
| F8 anchor counts | fixed | BIB §7 Identity anchors only; C-07, IV §3, CC §3, SH2 point to it |
| F9 header ranges, C2 measure | fixed | EXP and FBK headers; FBK §5 C2 (path wording, R3) |

Round-1 findings: all were fixed by round 2 and stay fixed (RD13 can fail, environment-only capture kind, line 9, paint-over budget, owner sheet count, band numbers in one place, R-02/R-03/R-05/WO8, compaction line, studio names, icon rounding, one-sun scope, job-type map, contrast form).

## Better work (C7)

I read the books as the agent would for eval E2 (cross-craft review: quiet, busiest, lowest-quality and phone captures, a manifest with a missing field, a VFX spec and clip list without clips) and E1 (2-3 directions for the lantern courier, max 9 images). For E2 the agent now writes a cold read first, takes its lines from the job-type row, asks the studio operator for the environment-only, UI-off and mask captures by name (role file studio-operator row), marks the band, depth, reserved-hue and clipped lines NOT REVIEWED until they arrive instead of measuring them on the busiest frame, and every number it does take comes from a tested command that gives the right answer on that input. That removes the four wrong briefs round 2 predicted. For E1 the new books give a success test before images, a research board, hooks with the warm-up set aside, equal-finish roughs inside one 9-image cap, a grey and black-fill pass before colour, an owner sheet of the 2-3 that passed with the six concept-art answers and a goal question, and a bible whose §7 gives every craft measurable bands, separation targets, reserved colours, key light and shape code. With df13ff4 the agent wrote packets with a grey and a thumbnail, no hooks or board, no gate on colour and no numbers the crafts could measure. The new books make clearly better work. Weak spots left: on roughs the band and reserved-hue lines have no runnable input and fall to NOT REVIEWED (R1); the lower-body check passes legs that are far too dark (R2); the 213-line self-review is long, though the job-type table keeps each review to its row; sample boxes on generated roughs are still placed by eye.
