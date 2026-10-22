---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer modeler · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: modeler books, round 1

Scope: `.agents/roles/modeler.md` (body), `.agents/skills/modeling-design/` (SKILL.md, references/), `.agents/skills/modeling-craft/` (SKILL.md, references/; evals not changed), as in the working tree on 2026-10-22, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/modeler.md`, `proposals/modeler.md`, `job-card.md`. Tool behaviour was tested on synthetic images in the reviewer's scratchpad (nothing in the repo was run against or changed).

```text
<spec>
artifact: .agents/roles/modeler.md (body) + .agents/skills/modeling-design/** + .agents/skills/modeling-craft/** (not evals) @ working tree 2026-10-22, base df13ff4
reviewer: J018 reviewer modeler (opus, high)
looked_at_first: [all 14 book files read in full before the coverage table (role, design SKILL + 5 references incl. new read-and-form.md, craft SKILL + 6 references); git show df13ff4 of role, both SKILL.md files and the removed lines of every reference (git diff -U0); universal-principles.md UP-01..UP-20 in full; principle and check of all 230 modeler-tagged library findings (matrix.md modeler column, extracted from the topic files); tools/art/look_check.py --help for every mode and its source; tools/model/review_renders.py source; studio-mcp SKILL C-03/C-08 and environment-craft audit-and-capture.md (screen_capture params, quality level); fact-check-blender MB16 (BLENDER_EEVEE on 5.1.2); roblox-creator-docs art/characters/creating/modeling-best-practices.md (mouth and eye rows); J005-D8 and J007-D7 (light checks)]
findings:
  - id: F1
    class: blocking
    where: "modeling-design/references/review.md:141 (IM1); modeling-design/SKILL.md:98 (P2 check); modeling-craft/SKILL.md:96 (Studio capture row of §7); modeling-craft/references/export-import.md:30"
    expected: "C3: every self-review line can be run with our tools. IM1 asks that SL1, SL2 and VL2 hold on the Studio capture at the game camera on the real ground, measured at phone size; P2 asks the same capture to be measured with look_check.py thumb."
    observed: "look_check.py finds the subject only from --mask, alpha, --box or a flat border key. A game-camera capture on the real ground has sky above and ground below, so the border is not flat. The books give no way to get a subject mask for a Studio capture (grep 'mask' over the 14 files: only the magenta-world hint for Blender renders, blender-recipes.md:66)."
    evidence: "Synthetic capture (sky top half, ground bottom half, subject in the middle): 'look_check.py silhouette' -> verdict invalid-mask, 'no subject mask found (no --mask, no alpha, no flat key-colour border)'; 'look_check.py thumb --size 200x150' -> invalid-mask, 'thumbnail value subject/ring and silhouette not measured'. art-review/references/look-check.md:36 already says game captures need --mask (object-ID or a hand mask from Studio); the modeler books do not."
    smallest_fix: "Add one row to modeling-craft SKILL §7 and point IM1 to it: 'Mask for a Studio capture: take a second capture from the same camera position with a flat backdrop (a large magenta #FF00FF Neon part placed behind and under the model, or the ground and sky parts hidden), run look_check.py silhouette on it, and pass its black-on-white image as --mask to silhouette, value and thumb on the real-ground capture; restore the place afterwards. VL2 on the capture uses boxes inside the body (F2).' If the second capture is not possible, IM1 records SL1/SL2 on the capture as not verified."
  - id: F2
    class: blocking
    where: "modeling-design/references/review.md:97 (VL2), :109 (CL5); modeling-design/SKILL.md:100 (P3 check); modeling-craft/SKILL.md:91 (Grey row: '--box ... --name upper --box ... --name lower --compare-subjects')"
    expected: "C3/C4: the value-gate check 'upper vs lower body medians (--compare-subjects) show the lower body quieter (15-20 % lower)' measures the body parts. The focal-zone spread (P3, VL2) and the per-region palette check (CL5) measure the region, not the background."
    observed: "--compare-subjects takes boxes; every pixel in a box counts, including the flat grey Workbench background around a limb or head. The books do not say to draw boxes inside the part. --box-key (drop the box's border colour) fails when the box edge crosses the body, which is always the case at a waist split. So the books' command returns background statistics without any warning."
    evidence: "Synthetic Workbench-like render (grey sRGB 128 background, bright torso, dark legs), boxes 120,30,280,210 'upper' and 120,210,280,380 'lower' with --compare-subjects: upper p50 = 0.216 and lower p50 = 0.216 (both equal the background luminance; the torso is about 0.72 and the legs about 0.03). With --box-key: verdict invalid-mask, 'box 1 border is not flat (0.849 within --key-tol, need 0.9)'."
    smallest_fix: "In modeling-craft SKILL §7 Grey row and in VL2/CL5, add: 'boxes lie fully inside the part (no background pixels); for a whole region use a mask split from the silhouette image (one PIL line: crop the black-fill at the waist line into two masks) and run value --mask once per region; record both medians.' Same note for P3's focal-zone spread."
  - id: F3
    class: blocking
    where: "modeling-design/references/review.md:77-143 (§5 self-review); read-and-form.md:44 (Faces), :76 (accents), :79 (cracks, glints, tagged DT6), :83 (real source per part), :91 ('(MO6)'), :100 (same character); budgets.md:84-86 (texel density, 'Check: review.md §5 DT2'); textures-materials.md:56 (pass 5 'DT5, DT6'); kits-and-environment.md:46-63 (§6 Check column)"
    expected: "Owner (J018): 'Turn every checkable finding into a line in the role's self-review (what to look for in its own render or capture).' C3: each checkable modeler finding has a self-review line; a tag in the standards names a line that carries it."
    observed: "Checkable findings with no line in review.md §5: CD-22 (eye placeholders at the blockout; face at anchor quality before a review), CD-23 (head silhouette and brows read at game size), CD-06 (face, posture, proportions match the anchor images), CD-20 / SI-17 (2-4 personality accents visible at the game camera; story detail invisible at phone size, findable close up), CD-11 (each creature part has a named real source), PP-04 (texel density equal across a set; budgets.md §8 points to DT2, which has no density check), MD-15 / MD-16 (read-and-form.md:79 tags cracks and glints as DT6; DT6 checks trims, patterns, motif and vocabulary only; textures-materials pass 5 also points to DT5/DT6 for them), SS-15 (read-and-form.md:91 tags '(MO6)'; §5 has MO1-MO5 only, so the tag points to nothing). The kit and environment checks (SI-04 theme cues, WL-05 hazards, WL-13 head-height line, WL-22 story, WL-23 landmark, PP-24 no visible duplicates, MD-17 trim-sheet count, SS-06 set silhouette sheet, SS-20 backdrop gesture, PP-27/GD-31 art inside the blockout) live only in the kits-and-environment §6 Check column, which the self-review, role step 7, craft step 8 and the hand-back never send the agent to."
    evidence: "grep over review.md lines 77-143: 'crack' 0, 'glint' 0, 'story' 0, 'texel|density' 0, 'trim sheet' 0, 'duplicate' 0, 'hazard' 0, 'head-height' 0, 'anatomy|real source' 0; 'MO6' appears only at read-and-form.md:91. Library checks: CD-22 'Early review render has placed eyes'; MD-15 'width varies along each crack and ends taper'; MD-16 'Glints are visible at the game camera and few in number'; PP-04 'no asset visibly sharper or blurrier than its neighbours at the game camera'."
    smallest_fix: "Append to review.md §5 (no renumbering): SL10 'Faces: eye placeholders in the blockout render; the face (or focal feature) at anchor quality before each review; head silhouette and brows read at phone size; face, posture and proportions match the anchor images at the same size'; DT7 'Personality accents (2-4) visible at the game camera; story details invisible at phone size and findable in one close render'; DT8 'Cracks vary in width and taper; glints few and only on light-facing edges'; DT9 'Texel density of assets seen together within one range (focal zone higher on purpose); none visibly sharper or blurrier at the game camera'; MO6 'Hook shapes face the camera in the animator's key poses (rigger's posed captures when they exist, else not verified)'; MO7 'Each creature part names its real-animal source in the record'; GR5 'Kit, prop and environment pieces: every row of kits-and-environment.md §6 Check column, results in the record'. Then fix the tags at read-and-form.md:79 (DT8), budgets.md:86 (DT9)."
  - id: F4
    class: recommendation
    where: "modeling-design/SKILL.md:61-72 (M-17..M-28) against §7 P1-P19 (:96-132) and read-and-form.md §2-§8"
    expected: "Owner: 'The goal is agents that make better work, not longer books.' rules/assistants/claude.md: after compaction each invoked skill keeps its first 5,000 tokens; steps and rules sit at the top."
    observed: "The design SKILL grew from 9,018 to 25,657 bytes. M-17..M-28 restate the same standards a third time (M-17 = P5/P8 + read-and-form §2; M-18 = review §3 step 2; M-19 = P3 + read-and-form §3; M-22 = P6; M-25 = P11; M-26 = P18/P19; M-27 = read-and-form §8; M-28 = P5 + read-and-form §5). The first ~20 KB that survive compaction end inside P7, so P8-P19 drop out after a compaction while the duplicated M rows stay."
    evidence: "wc -c modeling-design/SKILL.md: 25657 (df13ff4: 9018); head -c 20000 ends in the P7 check text."
    smallest_fix: "Delete rows M-17..M-28 (each has its home in §7 and read-and-form.md); the file drops to about 21 KB and §7 stays almost whole inside the compaction window."
  - id: F5
    class: recommendation
    where: "modeling-design/SKILL.md:98 (P2)"
    expected: "C2: nothing important from UP-02 missing. The master says 'game camera, phone size, real place, moving, busy' and its check asks for captures 'with effects and UI on'."
    observed: "P2 drops 'moving' and 'busy' without saying who covers them. The modeler only makes stills, so the right form is a hand-over line, not a new check."
    evidence: "universal-principles.md UP-02 principle and general check; coverage row VH-04 says the in-motion check goes on the could-not-check list, but P2 itself does not say so."
    smallest_fix: "Add to P2: 'A still proves one moment: the read in motion and in the busiest scene with effects and UI on is judged by the rigger, animator and art director; list it on your could-not-check list.'"
  - id: F6
    class: recommendation
    where: "modeling-design/references/review.md:100 (VL5); read-and-form.md:53 (band starting values); kits-and-environment.md:49"
    expected: "C4: a band compared with a tool output uses the tool's unit."
    observed: "VL5 compares look_check.py value p5-p95 with 'character band 8-92 %, environment 15-85 %'. look_check value reports WCAG relative luminance (linear 0-1). The bands come from painters' value (perceived lightness). A mid-dark sRGB grey of about 31 % (79/255) is already 0.08 luminance, so a character with dark boots or a dark grip fails '8 %' while it looks fine; the check will raise false findings on the lower body that VL2 asks to be darker."
    evidence: "look_check.py header: 'value: WCAG 2.x relative luminance per pixel ... distribution (p5/25/50/75/95)'; test run reports p5 0.034 for an sRGB 50 grey. Library VC-05 has the same unit gap (its check uses look_check p5/p95 with '% value'), so the fix belongs in the master first."
    smallest_fix: "State the bands as relative luminance (8 % value ~ 0.007, 15 % ~ 0.019, 85 % ~ 0.69, 92 % ~ 0.83 by the sRGB curve) or say 'convert p5/p95 to sRGB value before comparing'; raise the same fix for VC-05 to the lead (master first)."
  - id: F7
    class: recommendation
    where: "modeling-design/references/review.md:7 (the one review set) vs :102 (VL7 'a lit grey render' and 'the unlit flat render'); textures-materials.md:52-53 (pass 1 'flat (unlit) render', pass 2 'grey view ... and in a Studio capture'); modeling-design/SKILL.md:39 (step 8: 'on the real ground once a Studio capture exists (re-checked after import when it does not)')"
    expected: "Owner J005-D8 / J007-D7: scripted numbers for every check; images only when a number fails, plus the one review render set per hand-off. The set is defined once."
    observed: "The one-set list in review §1 does not include the lit grey (EEVEE) render or the flat unlit render that VL7 and texture passes 1 and 3 need each time, so their count is open. Pass 2 asks for a Studio capture at the value gate while design step 8 allows the value gate before any import. Read together, a character can get a blockout set, a value-gate set with a mid-build import, a lit grey and a flat render, and the final set: the agent cannot tell which are 'the one set'."
    evidence: "review.md:7 lists reference views, dummy render, front and back game-camera views, one Studio capture; blender-recipes.md:69 says the extra views are 'part of the one review set when the read plan needs it'."
    smallest_fix: "In review.md §1 list the set per gate in one line each (blockout gate: front and back game-camera renders; value gate: the same two plus one lit grey; hand-off: the review_renders set + back view + one Studio capture; flat unlit only when VL1 or VL7 fails) and change textures-materials pass 2 to 'and in a Studio capture once one exists' to match design step 8."
  - id: F8
    class: recommendation
    where: "modeling-design/references/review.md:78; read-and-form.md §1 (13 rows); role .agents/roles/modeler.md:16 (effort rule)"
    expected: "C7: a simple model at medium effort (a plain prop, a kit variant, a fix) gets a proportionate process."
    observed: "There is no short path: every model gets the 13-row read plan, about 50 self-review lines and six texture passes. 'Run the lines for the stage you are in' does not say which lines a simple prop may skip. Eval brief 4 (fix the lantern) or a crate variant would spend most of its effort on paperwork."
    evidence: "modeling-craft/evals/briefs.md briefs 1 and 4 are medium-effort or fixes; review.md §5 has 47 lines."
    smallest_fix: "Add one sentence after review.md:78: 'Simple models (medium effort): read plan rows Job, Identity anchors, Viewing conditions, Stop criteria; self-review RP1, SL1-SL3, VL1, VL4, DT2, GR1-GR2, IM1-IM3; the rest only when the brief or a failing number calls for it.'"
  - id: F9
    class: recommendation
    where: "modeling-craft/SKILL.md:31 (step 6)"
    expected: "C5: nothing valuable lost. Old step 6 said 'bake if the route needs it (references/textures-materials.md)'."
    observed: "New step 6 points to textures-materials §3 and §7 only; the high-to-low bake (§4) that organic hero and Tripo routes need is no longer reached from the steps (the §2 table still lists baking)."
    evidence: "git show df13ff4:.agents/skills/modeling-craft/SKILL.md line 30 vs the working tree line 31."
    smallest_fix: "In step 6 after 'UVs after structure is final', add '→ high-to-low bake when the route has a high source (§4)'."
  - id: F10
    class: recommendation
    where: "modeling-design/references/kits-and-environment.md:48 vs :12 (§2 snap origin); modeling-craft/references/export-import.md:24 (Set Pivot to Scene Origin)"
    expected: "C4: one consistent rule for where a piece's origin sits on export."
    observed: "§6 says build on the imported greybox and 'export back to the same position'. That is right for a bespoke shell snapped to its blockout, but a reusable kit piece has its snap origin at a corner or base (§2), and the importer's default 'Set Pivot to Scene Origin: on' would put a world-positioned piece's pivot far from its geometry."
    evidence: "kits-and-environment.md:12 'Snap origin: corner or base anchor for grid pieces'; export-import.md:24."
    smallest_fix: "Change the §6 first row to: 'bespoke shells export at their world position; reusable kit pieces export at their snap origin (§2) and are placed by the environment designer'."
  - id: F11
    class: recommendation
    where: "modeling-design/SKILL.md:120 (P13) vs read-and-form.md:42 and review.md:93 (SL9); review.md:99 (VL4) and SKILL.md:100 (P3); blender-recipes.md:58; modeling-design/SKILL.md:35-37 (steps 4 and 6)"
    expected: "C7: one wording per rule; every check has a command; steps in an order the inputs allow."
    observed: "(a) P13 says '2-3 distinct rough options and one radical one' (3-4 in all); read-and-form and SL9 say 2-3 options of which one is radical. (b) VL4 and P3 ask where the brightest 5 % of pixels sit; no tool mode reports that and §7 gives no command (the mirror row shows the one-line style that would fit). (c) blender-recipes §6 reads the play camera with execute_luau during play but does not name datamodel_type Client (studio-mcp C-03); the server's CurrentCamera is not the player's. (d) Step 4 writes the Tripo input pack, whose polycount target comes from the budget, before step 6 sets the budget (order kept from df13ff4)."
    evidence: "the cited lines; tripo-finish.md:13 'target ≈ the asset's triangle budget minus room'."
    smallest_fix: "(a) P13: '2-3 distinct rough options, one of them radical'. (b) Add a §7 row: python -c that loads the luminance image, thresholds it at its p95 and saves '<name>.top5.png' to view against the accents. (c) Add 'datamodel_type Client'. (d) In step 4 add 'Tripo: set the budget (step 6) first'."
keep: [the read plan in the asset record (read-and-form §1) with the sword example row by row; the silhouette gate and value gate as real gates before detail and polish; the camera rule for Roblox (identity on the back, shoulders, head, top and held item's profile); the texture passes table with a check per pass and recipes kept as data; design for motion (mass off joints, nothing in front of the arms, costly parts with a fallback, contact points fixed); kits-and-environment §6 'pieces that live in a place'; the five worked examples; review §3 diagnosis by layer with 'a note names a solution', paint-overs and conflicting notes; the icon checks at display size; 'what to ask each partner for, and when'; the honest close (IM2 cold read before the colour render, IM3 weakness and could-not-check list); the fix of the old inbox line that contradicted rules/messages.md; the proposals file (tool, template and workflow changes kept as proposals)]
verdict: fix-first
</spec>
```

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass with 4 row failures folded into F3 | 241 rows checked (230 tagged modeler in `matrix.md`, all present, no duplicates; 11 untagged). Every landed-in location carries the rule; the 9 full and 13 partial rejections have sound reasons (craft owned by the animator, art director, `reference-images` or rigger, with the modeler's share landed). Failed: SS-15 (tag `MO6` points to no line), MD-15 and MD-16 (tagged DT6 / pass-5 'DT5, DT6', which do not check them), PP-04 (budgets §8 'Check: DT2', which has no density check). Overstated landing notes, not failures: LC-11 ("at the blockout" is not in blender-recipes §6), PI-13 ("ask only for the views the build needs" is not in reference-check §7). |
| C2 core principles | pass with F4, F5 | §7 "Core principles for this craft" in `modeling-design` (loaded first): P1-P19 cover UP-01..07 and UP-09..20 with a model example and a check each; UP-08 skipped with a sound reason (the modeler owns no timing; master does not list modeler). No contradiction with the master. Missing: UP-02's "moving, busy" (F5). After compaction P8-P19 fall outside the kept 5,000 tokens (F4). |
| C3 self-review | fail (F1, F2, F3) | review.md §5 is a real, staged self-review (47 lines). But the Studio-capture lines cannot run without a mask recipe (F1), the box-based value and palette commands measure the background (F2), and several checkable findings have no line or a tag to a line that does not carry them (F3). |
| C4 kit rules and engine | pass with F6, F7, F10 | No conflict with AGENTS.md, rules/, J018-D2/D3/D4 or Roblox limits. Tool modes and flags exist (`look_check.py` value/contrast/silhouette/palette/thumb with --compare, --keep-holes, --box/--name/--compare-subjects, --sample/--fg-box/--bg-box, --roles, --size, --mask, --tolerance-source; `review_renders.py --game-cam`, `look_at`, -Y facing). Engine claims checked: BLENDER_EEVEE on 5.1.2 (MB16), screen_capture camera_position/look_at_position, quality level not scriptable, Lighting.ClockTime/GeographicLatitude, mouth/eye topology rows in the docs mirror. Unit gap in value bands (F6, library has it too); render count per gate not fixed (F7); export origin rule (F10). |
| C5 nothing valuable lost | pass with F9 | Every removed old line is kept, moved or sharpened (diff walked line by line); the coverage "old book changes" table matches the diff. Old studio names in M-row evidence were dropped (the IDs stay). Only the pointer to high-to-low baking left the steps (F9). |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4; design SKILL 132 lines, craft SKILL 96; descriptions 394 and 391 characters; no section renumbered (headings diffed; only appended §7/§8/§6/§9 sections); J018 header phrase in all 13 changed or new files and in the role comment; no Riot, Riot game, champion, artist, library ID or transcript line in any body (grep); no tips section; evals unchanged; modeler work touches only its books plus `coverage/modeler.md` and `proposals/modeler.md` (other modified files in `git status` belong to the other wave-1 makers and the lead). |
| C7 better work | yes, with weak spots | See the judgment below. |

## Will an agent with these books make better work?

Yes. Read as an agent starting eval brief 1 (the starter sword) and brief 2 (the Tripo hero pet), the old books stopped at "blockout, then approve the big shapes" and "one review render set". The new books make the agent decide what the model must say before it builds (sell list, identity anchors, read order, on-screen size on the smallest phone). They then gate detail behind a measured black-fill at the game camera and phone size, and polish behind a grey value pass and the art director's check-in. They texture in value-first passes, design for the rig before the final mesh, judge kit pieces in their set, and close with a cold read and an honest weakness. The worked sword and pet examples show exactly that path. Weak spots: the Studio-capture and box-based measurements will not give honest numbers as written (F1, F2); faces, accents, cracks, glints, texel density and the kit checks are standards without a self-review line (F3); the design SKILL repeats itself and loses its principles after compaction (F4); value bands and tool output use different units (F6); and a simple prop at medium effort carries the full process (F8).
