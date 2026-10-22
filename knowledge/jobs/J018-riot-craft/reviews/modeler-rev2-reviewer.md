---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer modeler · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: modeler books, round 2

Scope: `.agents/roles/modeler.md` (body), `.agents/skills/modeling-design/` (SKILL.md, references/), `.agents/skills/modeling-craft/` (SKILL.md, references/; evals not changed), working tree on 2026-10-22, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/modeler.md` (incl. §d repair round 1), `proposals/modeler.md`, `job-card.md`, `reviews/modeler-rev1-reviewer.md`. The new recipes were run on synthetic images in the reviewer's scratchpad; nothing in the repo was run against or changed except this file.

```text
<spec>
artifact: .agents/roles/modeler.md (body) + .agents/skills/modeling-design/** + .agents/skills/modeling-craft/** (not evals) @ working tree 2026-10-22 (repair round 1), base df13ff4
reviewer: J018 reviewer modeler (opus, high), round 2
looked_at_first: [all 14 book files read in full before the coverage table (role; design SKILL + budgets, kits-and-environment, read-and-form, reference-check, review; craft SKILL + blender-recipes, export-import, handoffs, rig-parts, textures-materials, tripo-finish); git diff -U0 df13ff4 removed lines of all 13 changed files; universal-principles.md UP-01..UP-04, UP-06, UP-14, UP-19, UP-20 re-read in full (the rest unchanged since round 1); library check lines of every covered row that names no self-review line (script over the topic files); tools/art/look_check.py header, out_path, luminance_image (sRGB-encoded grey), run_thumb (mask resample); studio-mcp SKILL C-03/C-08, references/tools.md, probes.md P-05; environment-craft audit-and-capture.md:21 (screen_capture params); docs mirror workspace/camera.md:145 (FieldOfView default 70), parts/index.md:267 (Neon glows), Camera.yaml (WorldToViewportPoint); modeling-craft/evals/briefs.md; synthetic tests: region-mask recipe (upper p50 0.791, lower p50 0.013 against a 0.216 background), mask-capture recipe (silhouette, value, thumb, palette on a sky-and-ground capture: all 'measured'), top-5 % recipe (see F2)]
findings:
  - id: F1
    class: blocking
    where: "modeling-design/references/review.md:87-164 (§5 self-review); read-and-form.md:16 (Detail spots row), :24 (archetype traits), :96 (theme nods), :101 (costume first); reference-check.md:223 (iconic-quality check); modeling-design/SKILL.md:94 (P6 check)"
    expected: "Owner (J018): 'Turn every checkable finding into a line in the role's self-review.' C3: every checkable modeler finding has a line in review.md §5 that the agent runs on its review set."
    observed: "Round 1 closed the gaps named in rev1 F3 (SL10, DT7-DT9, MO6, MO7, GR5 added; tags fixed). A full pass over every covered row that names no self-review line finds checkable findings still without one: VH-05 (detail clumped at the 1-3 detail spots with rest areas between; the read plan's 'Detail spots' row is written but never verified: no §5 line, and P6's check counts palette clusters and 4 px features only); CD-03 (the archetype is named from the black-fill of each option; SL9 checks that options differ, not that each keeps the archetype); CD-08 (at hand-off every iconic quality is at least as strong as in the image and the finish equals or exceeds it: the check exists in reference-check.md §7 but is not in §5, so it runs only before the blockout, never on the finished model); CD-19 and CD-16 (theme nods named from the props in a close render; a held prop shares at least one costume motif); partly carried: VC-12 (limbs read as cylinders, ribbon and hair ends darker: VL7 checks terminators only), SS-18 (motif integrated, not a sticker: DT6 checks scales only), LC-22 (the saturation peak sits on the focal zone: VL4 covers brightness only); untagged but used as a read-plan row: VH-09 (the reads appear in the stated read order at phone size)."
    evidence: "grep over review.md §5: 'detail spot' 0, 'rest area' 0, 'archetype' 0, 'iconic' 0, 'motif' only in DT6 (scales), 'saturat' only in CL4 (shadows keep saturation; nothing on where the saturation peak sits), 'read order' 0. Library checks: VH-05 'Downscale a capture to thumbnail size (look_check.py thumb): detail clusters sit at the focal points with clear quiet areas between ... Fail if detail density is even'; CD-03 'names the archetype from the black-fill silhouette of each option'; CD-08 'each listed iconic quality is present and at least as strong; ... the final finish equals or exceeds'; CD-19 'names the theme from the props alone in a close render'. Coverage table rows VH-05, CD-03, CD-08, CD-16, CD-19 are marked 'standard' or 'step', with no self-review line."
    smallest_fix: "Append inside the existing groups of review.md §5 (no renumbering): DT10 'Phone-size view (thumb): detail clusters sit on the read plan's 1-3 detail spots with quiet areas between; even detail density fails'; VL8 'Grey game-camera view: each part shades as its basic form (limbs as cylinders, head as a sphere, plates as planes); ribbon and hair ends darker than their middles; the most saturated cluster (palette) sits on the focal zone'; SL11 'Options and variants: the archetype (when the read plan names one) is nameable from each option's black-fill'; IM4 'Hand-off: the game-camera render next to the approved image at the same size: every iconic quality in the record is present and at least as strong; the finish equals or exceeds the image (reference-check.md §7)'; VA6 'Theme nods: the theme is named from the props in one close review_renders view, and VA1's anchor compare is unchanged; a held prop shares at least one costume motif'; add to DT6 'the motif reads as its subject in the black-fill at mid distance, integrated, not a sticker'; add to IM2 'the reads appear in the read plan's order'. Then point the five coverage rows to the new lines and add DT10 to P6's check."
  - id: F2
    class: recommendation
    where: "modeling-craft/SKILL.md:93 (Top 5 % row); modeling-design/references/review.md:114 (VL4), SKILL.md:88 (P3 check)"
    expected: "The top-5 % image marks the brightest 5 % of the model, so VL4 judges whether the extremes sit on small accents."
    observed: "On flat-region renders (the value gate, where VL4 runs first) many pixels share one grey level. 'l >= p95' then marks every pixel of the brightest large region, not 5 %. The agent sees a big torso marked as 'the extremes' while the true top value (a small accent) is also marked, and can 'fix' VL4 by darkening a region that was right."
    evidence: "Synthetic render: torso 100x170 px at sRGB 230, legs at 30, a 10x10 accent at 255. The recipe marked 17,210 px (63 % of the 27,200-px model), the whole torso plus the accent."
    smallest_fix: "In the row add: 'when the marked share is above 10 % (ties on flat regions), mark only l == the model's maximum level and record both shares'; or say that on flat-region renders VL4 reads the brightest grey level and its area instead of the top-5 % image."
  - id: F3
    class: recommendation
    where: "modeling-craft/SKILL.md:98 (Studio capture row), :99 (Mask capture row); export-import.md:188"
    expected: "IM1 measures the Studio capture 'at the game camera' and at phone size, so the capture uses the game's FOV and the phone's aspect."
    observed: "screen_capture takes only camera_position and look_at_position; the books never set Camera.FieldOfView to the game profile's FOV or say which viewport aspect the capture has. The phone-size row resamples the whole frame to the phone viewport, so a game FOV other than the editor's 70, or a Studio window wider or taller than the phone, changes the model's on-screen size in the measurement."
    evidence: "environment-craft/references/audit-and-capture.md:21 (screen_capture parameters); docs mirror workspace/camera.md:145 (FieldOfView default 70); blender-recipes.md:58 reads the game FOV for Blender cameras only."
    smallest_fix: "Studio capture row: 'before the capture set workspace.CurrentCamera.FieldOfView to the game profile FOV (execute_luau) and restore it after; if the capture's aspect differs from the phone viewport, crop it to the phone aspect around the look-at point before thumb'."
  - id: F4
    class: recommendation
    where: "modeling-design/SKILL.md:32 (step 1 check 'no field blank'); review.md:27 (§2 Read plan row: sell list and read order before the blockout); review.md:12 (value-gate row: lit grey render) vs review.md:90 (simple-model lines) and read-and-form.md:24"
    expected: "One short path for simple models (medium effort), stated the same way wherever the agent reads it."
    observed: "read-and-form §1 and review §5 let a simple model fill four read-plan rows and run 13 lines, but the design SKILL step 1 check (loaded first) says no field blank, review §2 requires sell list and read order before the blockout, and review §1 still asks every value gate for a lit grey render that only VL7 (not on the short path) uses. An agent on eval brief 1 (medium) gets two answers."
    evidence: "The cited lines."
    smallest_fix: "Step 1 check: add '(simple models: the four rows of read-and-form §1)'; review §2 Read plan row: same parenthesis; review §1 value-gate row: 'plus one lit grey render when VL7 runs'."
  - id: F5
    class: recommendation
    where: "read-and-form.md §4 (:59-66) vs textures-materials.md §8 (:130-140); read-and-form.md §6 (:82-91) vs rig-parts.md §6 (:101-111); read-and-form.md §8 (:109-115) vs kits-and-environment.md §6 (:141, :147-148); modeling-design/SKILL.md §4 M-01..M-04, M-06, M-08 vs §7 P2, P4, P5, P6, P10"
    expected: "Owner: 'better work, not longer books'; design says what and why, craft says how; a later master fix lands in one place (J018-D2 point 2)."
    observed: "Three standards blocks are written twice in near-identical words (hue shift, no flat fills with the same PROPOSAL numbers, gold, skin, extremes small, upper body brighter, judge in Studio; mass off joints, nothing over the arms, costly parts, model what the rig moves, moving parts, contact points, hook shapes; grounding, materials follow gameplay, predictable geometry). Rev1 F4 is partly open: after deleting M-17..M-28 the design SKILL is 23,665 bytes and the first ~20 KB kept after compaction end inside P11, so P12-P19 still drop out, while M-01..M-04, M-06 and M-08 repeat P2, P4, P5, P6 and P10."
    evidence: "wc -c modeling-design/SKILL.md 23665; the first 20,000 bytes end at line 104 (P11); side-by-side reading of the cited sections."
    smallest_fix: "Keep the standards in read-and-form.md; in textures-materials §8, rig-parts §6 and kits §6 keep only the how (noise mask, AO strength, overlay on the base armature, the Check column) with a pointer to the read-and-form section; in design SKILL §4 shorten M-01..M-04, M-06, M-08 to one line each with '→ §7 Pn' (evidence column kept), which brings §7 almost whole inside the window."
  - id: F6
    class: recommendation
    where: "export-import.md:188; modeling-craft/SKILL.md:34 (step 9); review.md:162 (IM1)"
    expected: "Judge a model where players meet it (UP-02); a held weapon or tool is met in the character's hand."
    observed: "The Studio capture always places the model 'on the real ground of its stage'. For eval brief 1 (the sword) and every held item, that capture shows a sword lying on the floor, not the read players get; review §2a FM36 (held prop that does not read at game view) is checked only on a Blender render."
    evidence: "modeling-craft/evals/briefs.md brief 1 check 1.4 'the blade reads from the front at the game camera'; review.md:56."
    smallest_fix: "Add to export-import §3 and IM1: 'held items: captured in the default avatar's hand (as a Tool, grip at the grip attachment) at the game camera on the real ground, back and front'."
keep: [all of round 1's keep list (read plan with the sword example, silhouette and value gates, camera rule, texture passes with a check per pass and recipes as data, design for motion, pieces that live in a place, worked examples, diagnosis by layer, icon checks at display size, what to ask each partner for and when, honest close, inbox fix, proposals file); new in round 1: the mask-capture recipe with its probe and its not-verified fallback (tested: makes a sky-and-ground capture measurable); the region-mask recipe (tested: torso and leg medians instead of the background's) and the ban on --box/--compare-subjects for renders; the unit paragraph with correct sRGB-to-luminance values (the luminance image is sRGB-encoded, look_check.py:679-682); the images-per-stage table in review §1; the simple-model short path; SL10, DT7-DT9, MO6, MO7, GR5; the texel-density recipe (formula correct); the export-origin rule for bespoke shells vs kit pieces; datamodel_type Client for the play camera; the two new proposal rows for look_check and the studio-mcp probe]
verdict: fix-first
</spec>
```

## Round 1 findings: status

| Rev1 id | Status | Evidence |
| --- | --- | --- |
| F1 Studio capture cannot be measured | fixed | craft SKILL §7 "Mask capture" row, IM1 fallback, EI §3, role step 8; synthetic test: all four modes `measured` |
| F2 box-based region numbers measure the background | fixed | §7 "Region" row (mask ∩ box), VL2, VL3, CL5, P3; synthetic test: 0.791 / 0.013 vs 0.216 background |
| F3 checkable findings without a line, dead tags | fixed for every item named; further gaps in round 2 F1 | SL10, DT7-DT9, MO6, MO7, GR5 present; tags at RF:79, BU:86, TM:126 point to lines that carry them |
| F4 SKILL bloat and compaction | partly open (round 2 F5) | M-17..M-28 deleted; P12-P19 still outside the first ~20 KB |
| F5 UP-02 motion and busy scene | fixed | P2 hands them over and lists them on the could-not-check list |
| F6 value-band units | fixed | review §5 intro and VL5; conversion values checked (0.0072, 0.0196, 0.692, 0.828) |
| F7 render count per gate | fixed | review §1 stage table; TM pass 2 "once one exists" |
| F8 no short path | fixed in review §5 and RF §1; two places still disagree (round 2 F4) | role effort paragraph, TM §7 |
| F9 bake pointer | fixed | craft SKILL step 6 |
| F10 export origin | fixed | KE §6 first row |
| F11 a-d | fixed | P13; Top 5 % row (but see round 2 F2); BR §6 Client; design step 4 |
| C1 notes LC-11, PI-13 | fixed | coverage note corrected; RC §7 item 2 |

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass with 2 row failures (in F1) | 241 rows checked (230 tagged `modeler` in `matrix.md`, all present once, script-compared; 11 untagged) plus the 20 UP rows. Every landed-in location was opened (all 14 files read in full) and carries the rule. Failed (checkable check carried nowhere): VH-05, CD-03. Partly carried: CD-08 (check only before the blockout), CD-16, CD-19, VC-12, SS-18, LC-22. The 9 full and 13 partial rejections have sound reasons (animation, rigging, art-direction or `reference-images` craft, with the modeler's share landed). |
| C2 core principles | pass | §7 in `modeling-design` (loaded first): P1-P19 cover UP-01..07 and UP-09..20, each with a model example and a check; UP-08 skipped with a sound reason. P2 now hands over motion and the busy scene; P3 uses region masks; P13 matches the master's "one radical option". No contradiction with the master. Compaction reach: see F5. |
| C3 self-review | fail (F1) | §5 is staged, runnable and now measurable on Studio captures (rev1 F1, F2 fixed and tested). Remaining: VH-05, CD-03, CD-08 at hand-off, CD-16/CD-19 and partial VC-12, SS-18, LC-22 have no line. Tool caveats: F2 (ties in the top-5 % image), F3 (capture FOV and aspect). |
| C4 kit rules and engine | pass with F3 | No conflict with AGENTS.md, rules/, J018-D2/D3/D4 or Roblox limits. No invented tool modes: the new recipes use only `look_check.py` modes and flags that exist (`--mask` on silhouette/value/thumb/palette, `--out-dir`, `contrast --sample/--fg-box/--bg-box`) plus PIL/numpy one-liners; output names (`<stem>.silhouette.png`, `<stem>.luminance.png`) match `out_path`. Engine claims checked: Neon glows (probe-first recipe is right to test it), WorldToViewportPoint, CastShadow, FieldOfView default 70, screen_capture parameters, edit camera left Scriptable (C-08, P-05). |
| C5 nothing valuable lost | pass | Removed lines walked again (git diff -U0); every one is kept, moved or sharpened, matching coverage §c. Round 1 removed only lines it had itself added (M-17..M-28). |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4; design SKILL 120 lines, craft SKILL 99; descriptions 394 and 391 characters; headings: two titles reworded, no number changed, new sections appended; J018 phrase once in each of the 13 skill files and in the role comment; no library ID, champion, artist, game or transcript line in any body (the only "Riot" is the required header phrase; RG-/TR-/FW-/TX-/BG- ids are the older modeling-paper ids); no tips section; evals unchanged. `sync_harness.py --check` reports drift for the generated `.claude/` and `.codex/` copies of these files: expected while the books are under review, the lead syncs before the gate. |
| C7 better work | yes, with weak spots | See below. |

## Will an agent with these books make better work?

Yes, clearly. Read as an agent on eval brief 1 (the sword, medium effort) and brief 2 (the Tripo hero pet), the old books said "blockout, then approve the big shapes" and "one review render set". The new books make the agent write what the model must say before it builds, gate detail behind a measured black-fill at the game camera and phone size, gate polish behind a grey value pass and the art director's check-in, texture in value-first passes, design for the rig before the final mesh, and close with a cold read and an honest weakness. Since round 1 the numbers are honest: region medians come from the body, not the background, and the Studio capture can be measured with a mask, with a `not verified` fallback when the probe fails. Weak spots: a few core standards (detail spots and rest areas, archetype per option, iconic qualities at hand-off) are still not run at hand-back (F1); the top-5 % image misleads on flat renders (F2); the Studio capture does not set the game FOV (F3); the short path for simple models is stated two ways (F4); three standards blocks are written twice, and P12-P19 still fall out after a compaction (F5); a held item is captured on the floor, not in the hand (F6). None of these makes the work worse than the old books; F1 is blocking only because the owner's rule asks for every checkable finding in the self-review.
