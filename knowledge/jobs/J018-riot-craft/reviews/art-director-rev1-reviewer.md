---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer art-director · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: art-director books, round 1

Scope: `.agents/roles/art-director.md` (body), `.agents/skills/art-direction/` (SKILL.md, references), `.agents/skills/art-review/` (SKILL.md, references; not evals), working tree on 2026-10-22, against df13ff4. I read all 14 book files in full before the coverage table. Then I read `matrix.md`, `universal-principles.md` (the master), the principle and check lines of all 277 findings tagged art-director (extracted by script from the topic files), `coverage/art-director.md`, `proposals/art-director.md`, the job card and `stage2-brief-v2.md`. I ran the book's command lines and tool modes on synthetic inputs in my scratchpad (`ad-rev/`, role-prefixed script `make_samples_adrev.py`). I changed nothing in the repo except this file.

```text
<spec>
artifact: .agents/roles/art-director.md (body) + .agents/skills/art-direction/** + .agents/skills/art-review/** (not evals) @ working tree 2026-10-22
reviewer: J018 reviewer art-director (opus, high), round 1
looked_at_first: [all 14 book files in full (role body; art-direction SKILL, clarity-cohesion, identity-variants, worked-examples, platform-evolution-marketing, precedents unchanged; art-review SKILL, self-review, look-check, exploration, art-bible, feedback-briefs); git diff df13ff4 of every changed file (all removed lines read); look_check.py -h for value, contrast, silhouette, palette, thumb; thumb_check.py icon/thumbnail -h; look_check.py ring_mask, value_stats and contrast_ratio source; synthetic inputs: a 600x900 magenta flat-key render (light head, bright upper body, near-black lower body), a 1600x720 game frame (sky, noisy ground, a hero whose lower body has the ground's colour, a bright objective, three reserved-red patches of 91 px each) with its magenta mask capture, an environment-only cut with a 30 px pure-black patch, the same cut with 10 characters and a white HUD bar left on (an effects-off cut), a shadowed copy of the reserved red, a hat variant of the flat render, a 512 magenta icon]
findings:
  - id: F1
    class: blocking
    where: "art-review/references/self-review.md:64 (RD13 pass 'lower subject/ring > 1'); look-check.md:100-104 (§5 line 1 'Tested ... lower body 0.053'); coverage §d row RD13 ('lower subject/ring 3.26: correct')"
    expected: "RD13's second half ('the lower body still separates from the ground', VC-08) fails when the lower body does not separate from the ground."
    observed: "The check cannot fail. look_check.py contrast_ratio is (max+0.05)/(min+0.05), so subject_ring_ratio is always 1 or more, and '> 1' passes any two medians that differ at all. Also, on the 'flat' input that RD13 names, the ring around the lower-body region is the magenta key plus a strip of the upper body, not the ground. So the maker's 3.26 is the contrast to magenta."
    evidence: "Game frame + mask capture, lower body painted the ground colour (78,83,68 on ground 70-90): lower subject p50 0.0822, ring p50 0.0908, ratio 1.065 → RD13 passes. Flat render: lower ring p50 0.2848 = luminance of #FF00FF (ratio 4.65), upper ring also 0.2848. A region under 0.1 % of the frame (a small hero's legs at 1600x720) gives invalid-mask (a safe error)."
    smallest_fix: "RD13: run the lower-body half only on the in-scene capture with the mask capture (never on flat renders); pass `--exclude <upper-region mask>` so the ring is ground only; set a real starting value (for example 'lower subject/ring ≥ 1.5, PROPOSAL, the bible's value wins') and note that the ratio is symmetric (always ≥ 1). Update the §5 line 1 'Tested' note and the coverage row."
  - id: F2
    class: blocking
    where: "art-review/references/look-check.md:26 (Layer cuts 'one change each'), :85 (K19), :126 (§5 line 8); art-direction/references/worked-examples.md:19, :22 (§2 inputs and step 2); proposals/art-director.md (job-stage.js row: 'layer cuts (effects off, UI off)')"
    expected: "The environment band (RD3, K19) is measured on a capture in which every pixel of the box is environment: UI, effects and characters off together. The capture-kinds table names that capture, and the worked example uses it."
    observed: "LK §1 defines layer cuts as one change each (UI off, or effects off, or characters off), so no listed capture kind is environment-only. RD3 and §5 line 8 need one ('every pixel in the box is that layer'). Worked example §2 asks only for UI-off and effects-off cuts and measures the environment band 'on the effects-off layer cut' of a busy hub, where players and the HUD are still on. The agent then reports a band that is too wide and briefs the environment designer to fix a fault that does not exist. No error is shown."
    evidence: "Same 1600x720 play-area box (0,360,1600,720): environment-only cut p5 0.0685, p95 0.1069; the effects-off cut with 10 characters and one HUD bar p5 0.0666, p95 0.8773 (above the 0.69 band). The worked example's own number (p95 0.86) is what this contamination gives."
    smallest_fix: "LK §1: add a capture kind 'Environment only: UI, effects and characters off together (for layer bands)'; K19 and RD3 name it as the input. WE §2: add that capture to the inputs and measure step 2 on it. In the proposals row for job-stage.js, add the environment-only capture (characters off too)."
  - id: F3
    class: recommendation
    where: "self-review.md:54 (RD3 'no pure black in the environment'), :56 (RD5 'no large clipped area'); look-check.md §5 (no counting line)"
    expected: "Each claim in a pass column has a measure (VC-05: 'fail on any pure black'; VC-07: 'clipped-white pixels cluster on the intended accent only'). The environment designer's VB1 already measures a near-black share."
    observed: "RD3 and RD5 read p5/p95 only. A small pure-black or clipped area does not move p5 or p95, so both pass with no error."
    evidence: "Environment-only cut with a 30 px pure-black patch: p5 0.0685, p95 0.1069 (inside the band); the black patch is not seen. `environment-design/references/review.md:90` VB1 asks for 'near-black share about zero'."
    smallest_fix: "Add one §5 line that counts pixels with luminance ≤ 0.002 and ≥ 0.98 inside a mask or box (the line 4 pattern: share plus a marked image), and point RD3 and RD5 to it."
  - id: F4
    class: recommendation
    where: "art-review/SKILL.md:59 (R-16), feedback-briefs.md:118 (§6 'A visual note is a picture'), self-review.md:189 (FB2 'one per visual note')"
    expected: "V1: every image-making stage states its image budget; generated images need the owner's yes for the batch (`reference-images` 'Who generates', role file 'imagesApproved')."
    observed: "Every visual note must carry a paint-over, and the default route is a generated edit with `reference-images`. No budget is stated, and the books do not say that a generated paint-over without the batch yes goes to `image-prompts.md` as pending. A review with 8 visual notes asks for 8 generated images."
    evidence: "Brief v2 V1; AD §5 rule 'every image-making stage states its budget (J005-D8)'; role file Reference images bullet."
    smallest_fix: "FBK §6: 'Default: a marked capture (arrows, circles, a value overlay drawn on the capture: no generation). A generated paint-over only for the 1-2 worst visual notes, inside the brief's image cap, with the batch yes; otherwise write it to image-prompts.md and list it as pending.' FB2: 'one marked capture or paint-over per visual note'."
  - id: F5
    class: recommendation
    where: "art-direction/SKILL.md:41, :43 (keep 3-4; sheet A, B, C), worked-examples.md:12-13 (owner sheet A, B, C, D); orchestration job-types.md:38-39 (character recipe: '2-3 visual directions', 'G1 shows 2-3 pictured directions'); role description '2-3 directions'"
    expected: "The number of directions at the owner gate agrees with the recipe and the role description, and options that fail the grey pass are not on the owner sheet as equals."
    observed: "The books keep 3-4 options with one radical, and the worked example puts all 4 on the owner sheet, including C (ratio 1.6) and D (1.2), which failed the grey pass. exploration.md §3 item 4 says colour is judged only on options that pass. The example also logs D as a closed door before the owner answers."
    evidence: "Lines cited; eval E1 also asks for '2-3 directions'."
    smallest_fix: "AD step 6 and EXP §3 item 6: 'the owner sheet shows the 2-3 options that passed the grey pass (the recipe's G1 count); the others are listed with their failing numbers'. WE §1 steps 6: show A and B (plus C only if it passed), and close D only after the owner's words."
  - id: F6
    class: recommendation
    where: "art-direction/SKILL.md:72 (C-19), clarity-cohesion.md:29 (§2 item 4), art-bible.md:68 (§7 Value bands), self-review.md:54 (RD3); also the ΔE 10 in art-bible.md:69, look-check.md:111, self-review.md:90"
    expected: "V6: one rule, one place; other places point to it."
    observed: "The starting band values (15-85 % = 0.020-0.69; 8-92 % = 0.007-0.83) are written in 4 places, and the reserved-hue distance 10 in 3. Each copy says the bible wins, so the harm is small now, but the library's VC-05 unit change in the proposals would need 4 edits."
    evidence: "grep '0.020-0.69' finds the four lines above plus the worked example."
    smallest_fix: "Keep the numbers only in art-bible.md §7 (the table a game's bible copies); C-19, CC §2 item 4 and RD3 say 'the bible's band (starting values: art-bible.md §7)'."
  - id: F7
    class: recommendation
    where: "art-review/SKILL.md:45 (R-02), :46 (R-03), :48 (R-05), :54 (R-11); self-review.md §3 (no completeness line)"
    expected: "C5: nothing valuable lost."
    observed: "(a) R-02 lost the practical vision limits from its old evidence column (the model sees a resized copy and is unreliable under about 200 px). This matters more now, because the cold read is done on a phone-size image and icons are 150x150. (b) R-03 lost 'raise a needs-decision for the project value' and R-05 lost 'if the spec and kit default differ, measure both and raise needs-decision'. (c) R-11 completeness (every face finished, every room furnished, every path joined, ground continuous) is the first game's most repeated owner correction. The old book said that no self-review caught it, and the new 135-line self-review still has no line for it (only the K-table footnote and the environment brief)."
    evidence: "git diff df13ff4 -- art-review/SKILL.md (old R-02 evidence, R-03, R-05, R-11 text)."
    smallest_fix: "R-02: add 'view small slots enlarged (nearest neighbour), never judge an image under about 200 px by eye'. Restore the two needs-decision clauses. Add a WO8 (or MD10) line: 'Completeness: every face finished, every room furnished, every path joined, ground continuous; input busy + orbit captures; pass none missing'; K25 cites it."
  - id: F8
    class: recommendation
    where: "art-direction/SKILL.md:21 (compaction line); byte offsets: §5 rules start at 16.7 KB, §6 self-check runs 18.0-19.2 KB"
    expected: "V7: steps, rules and self-check sit in about the first 5,000 tokens (about 18 KB), or the first section names them for re-reading."
    observed: "The self-check (§6) ends at 19.2 KB, just past the line. The re-read line names §7 only."
    evidence: "Byte count of art-direction/SKILL.md by heading (total 26.8 KB)."
    smallest_fix: "Line 21: 're-read §5-§7 of this file and art-review §6'."
  - id: F9
    class: recommendation
    where: "platform-evolution-marketing.md:54 ('Supercell's 2025 logo evolution'); AD §5 rule 'studio names appear only in references/precedents.md'"
    expected: "The book keeps its own new rule."
    observed: "One studio name is still in the body text. The maker moved the other cases to precedents.md."
    evidence: "grep of the 14 book files (headers excluded)."
    smallest_fix: "Replace with 'a studio's 2025 logo evolution, precedents.md §2 (S 01:SC-BS)' and check that precedents.md holds it."
  - id: F10
    class: recommendation
    where: "clarity-cohesion.md:108 and PEM §3 ('the icon square and its rounding'); PEM §3 new bullets"
    expected: "Engine claims checked against the docs mirror; V6 across books."
    observed: "Badge and pass circles are documented (`production/publishing/badges.md:32`, `production/monetization/passes.md:28`); icon rounding is not (`production/publishing/experience-icons.md` has no such statement). The marketing maker's proposal row (`proposals/marketing.md:31`) says the new PEM §3 bullets restate marketing-design M-15..M-23."
    evidence: "Docs grep; marketing proposal row."
    smallest_fix: "Mark icon rounding 'unverified' or drop it. Replace the restated marketing standards in PEM §3 with a pointer to marketing-design §4 and keep the art director's review duties (MK1-MK8)."
  - id: F11
    class: recommendation
    where: "clarity-cohesion.md:66, art-bible.md:71 ('One key light direction per place ... Lighting.ClockTime and GeographicLatitude')"
    expected: "The engine fact is stated with its scope."
    observed: "The Lighting service is one per Roblox place. Two areas in one place cannot have different sun directions unless a client script changes Lighting when the player moves. 'Per place' can be read as 'per area'."
    evidence: "environment/lighting.md:169-179 (ClockTime and GeographicLatitude are Lighting properties)."
    smallest_fix: "Add 'one sun per Roblox place (Lighting is global); areas inside one place differ by local lights or a client-side Lighting change the environment designer owns'."
  - id: F12
    class: recommendation
    where: "self-review.md §1 and §3 (135 lines); look-check.md §4 (K01-K25)"
    expected: "C7: the agent can pick the lines a job needs without reading all 135 or ticking boxes at random."
    observed: "Nothing maps a job type (character, stage, effect, UI screen, marketing art, direction round) to its K rows and self-review lines. The role file says 'the §3 lines the question needs', which leaves the choice open on every job."
    evidence: "Reading the books for eval E2 (cross-craft busy scene): EV, RD, CL, CP, EVT and K rows apply, but the choice comes from the agent's judgment, not from the book."
    smallest_fix: "Add a 6-row table at the top of self-review §3: recipe → K rows → line groups (for example stage: EV, RD1-RD12, CL1-CL9, CL15, WO, CP4-CP6, CP11, K09, K13, K19-K21, K25)."
  - id: F13
    class: recommendation
    where: "look-check.md:37 (§2 generic command line)"
    expected: "Each tool mode named with the flags it takes."
    observed: "`contrast` has no image argument and no `--out-dir`. With the generic form it stops with 'unrecognized arguments: --out-dir' (a safe error)."
    evidence: "Run on scene2.png."
    smallest_fix: "Add '(contrast: `contrast --sample <image> --fg-box ... --bg-box ... --out <json>`; no --out-dir)'."
keep: [The direction stages in art-direction §3 steps 3-9: research board with both halves and a keyword table, 6-12 hooks with the warm-up set aside, 3-4 rough options at equal low finish with one radical, the grey and black-fill pass before any colour pick, one sheet with a goal question, cheap proof in the engine before polish. art-bible.md §7: the standards every craft measures against (screen order, value bands in both units, reserved colours with a shape partner, key light per place, shape vocabulary and effect shape code, motion line, UI thematic, identity anchors), so partners' checks have a source. The role file's partner table (what to ask each craft for, and when). The cold read written before the hand-back is opened, the fixed review order big to small, and R-16 to R-21. look-check.md §2 mask rules and §5 command lines: all 8 ran as written and gave right answers on their stated inputs (squint pairs keep rank order; reserved-hue pixel share counted exactly 273 px of 273; chroma bands 48.5 above vs 15.2 player band; contact sheet 2400x720; thumb with mask scale 0.5; mirror written), each with its 'wrong with no error' note; the palette k=8 trap and the --key-tol 4 rule. identity-variants.md (anchors, slot filling, variant vs same character, cosmetic footprint, tiers deferring to platform-policy). Core principles §7: P1-P20 without P8 and P19, each in the art director's terms with an example and a check line; no contradiction with the master. Frontmatter byte-identical; LF; descriptions 389 and 383 characters; SKILLs 137 and 86 lines; evals and precedents.md unchanged.]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass with 2 row failures | 287 rows: all 277 tagged findings present (script against `matrix.md`, column art-director), 10 untagged; 22 rejections, each with a sound owner or duplicate reason. Every landed location was opened against the finding's principle and check. Failed: VC-08 (check cannot fail, F1), VC-05 (no environment-only capture kind; pure black not measured: F2, F3). Partial but acceptable: VC-07 (clipped area, F3), WL-13 (directional patterns), WL-20 (high setting not noisier), CD-23 (brows). |
| C2 core principles | pass | `art-direction` §7 covers UP-01..UP-07, UP-09..UP-18, UP-20 with an example and a self-review line each; UP-08 and UP-19 are correctly not the art director's (the master's applies-to lists agree) and their picture lines are kept as EVT1 and IV §5 / ID6. No contradiction found. The section sits after byte 19 KB; §1 names it for re-reading (see F8 for §5-§6). |
| C3 self-review | fail (F1) | Every self-review line names its input; 135 lines; every coverage SR id exists (script). RD13 cannot fail (F1); RD3 and RD5 claim measures they do not run (F3). |
| C4 kit rules and engine | pass with notes | No conflict with AGENTS.md or rules found; no tool mode invented (every mode and flag checked against -h). Engine claims checked: shadows scale down with quality (`environment/lighting.md:171`), badge and pass circles (docs), ClockTime and GeographicLatitude (scope note F11); icon rounding not in the docs (F10). Option count vs the character recipe (F5). |
| C5 nothing valuable lost | pass with notes | All removed lines in the diff walked. Studio names moved to precedents.md; "View every image" replaced by the light-check rule (correct). Lost: R-02 vision limits, two needs-decision clauses, and still no completeness line (F7). |
| C6 fixed rules | pass (one book-rule slip, F9) | Only the role body, the two skills and the two job files are the maker's; frontmatter byte-identical; no section renumbered (list items in exploration §3 renumbered inside a section, no outside reference broken); J018 header phrase in every changed file and the role comment; no library IDs, transcript lines, Riot names or "tips" section in bodies; evals unchanged. |
| C7 better work | yes, after F1-F2 | See below. |
| C8 brief v2 | fail (V3: F1, F2) | V1 inputs named everywhere, direction-round budget in exploration §8; paint-over budget missing (F4). V2 real modes only. V3: all 8 §5 lines and the named modes run; two wrong-with-no-error cases (F1, F2) and two unmeasured claims (F3). V4 paid random tiers defer to platform-policy (no conflict). V6 band numbers in 4 places (F6). V7 borderline (F8). V8 findings became the bible §7 standards, the partner ask table, K19-K25 and the self-review. V10 consistent with the modeler (bands, units, key-tol 4), the animator (key-pose black-fills, timing list) and the game designer (10 % footprint, variant brief). V11 wave-1 rows adopted with reasons. Same-wave rows written against these books by environment, ui-ux, marketing, sound and progression makers are not in the coverage file (they ran in parallel); the lead should pass them to the round-2 maker. |

## Commands run (C8 V3)

| Line or mode | Input | Runs | Files written | Right answer | Wrong number with no error when |
| --- | --- | --- | --- | --- | --- |
| `silhouette` | flat render; mask capture | yes | `.silhouette.png`, JSON | yes | — |
| §5 line 1 region mask + `value --mask` | flat render; game frame + mask capture | yes | `<region>.mask.png`, JSON | upper/lower medians yes; lower-vs-ground no | ring is the key colour on flat renders; '> 1' always passes (F1) |
| §5 line 2 squint + `contrast --sample` pairs | game frame | yes | `.squint.png`, JSON | yes: objective 6.64 > hero 4.63 | a sample box crossing an edge (the book says so) |
| §5 line 3 mirror | game frame | yes (Windows path inside the Python string; a Git Bash `/c/...` path fails loudly) | `.mirror.png` | yes | — |
| §5 line 4 reserved share | game frame, `-` exclusion | yes | `.reserved.png` | yes: 273 px = 3 patches x 91 px | the same paint in shadow is ΔE 16 from the swatch and is missed; the book's 'sample the rendered swatch too' covers lit drift, not shadowed copies |
| §5 line 5 chroma bands | game frame | yes | stdout JSON | yes: 48.5 above vs 15.2 player band | rows taken by eye in perspective (the book says so) |
| §5 line 6 contact sheet | 3 images | yes | `sheet.png` 2400x720 | yes | — |
| §5 line 7 `thumb --mask --size 800x360` | game frame + mask | yes | small image, JSON | scale 0.5 | — |
| §5 line 8 `value --box` layer band | environment-only cut; effects-off cut | yes | JSON | environment-only yes; effects-off no | characters and HUD in the box: p95 0.107 → 0.877 (F2); pure black invisible to p5 (F3) |
| `silhouette --compare` | flat render vs hat variant | yes | JSON | IoU 0.875; alignment recorded | IoU scales by bbox height (the book says so: footprint by area_frac and bbox_px) |
| `thumb_check.py icon --key FF00FF` | 512 magenta icon | yes | sheet, JSON | measured | — |
| generic §2 syntax on `contrast` | game frame | error 'unrecognized arguments: --out-dir' | — | safe error | — (F13) |

## Better work (C7)

I read the books as the agent would for eval E1 ("2-3 directions for a lantern courier in a flooded night city, max 9 images") and E2 (cross-craft busy scene). With the old books the agent wrote 2-3 packets with a grey and a thumbnail each, made no research board, did not set the first idea aside, did not gate colour on the grey read, and gave the bible no numbers the crafts could measure. With the new books it writes a success test first, builds a research board, writes 6-12 hooks and sets the warm-up aside, makes equal-finish roughs inside a stated budget, picks from a grey and black-fill contact sheet, and writes a bible that tells the modeler, environment, VFX and UI designers their value bands, reserved hues, key light and shape code. For E2 it writes a cold read before the hand-back, asks for named capture kinds, measures with tested commands that each list how they can mislead, and sends paint-over briefs. That is clearly better work. Where it is still weak: two measures give a wrong answer with no error (F1 lower body vs ground; F2 environment band on a cut that still has characters and HUD, taught by the worked example); some pass columns claim things no command measures (F3); paint-overs have no image budget (F4); the 135-line self-review has no map from job type to lines, so reviews can grow into box-ticking (F12); and the option count disagrees with the character recipe (F5).
