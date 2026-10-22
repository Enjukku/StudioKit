---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer modeler · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: modeler books, round 3

Scope: `.agents/roles/modeler.md` (body), `.agents/skills/modeling-design/` (SKILL.md, references/), `.agents/skills/modeling-craft/` (SKILL.md, references/; evals unchanged), working tree on 2026-10-22 after repair round 2, against git `df13ff4`. Inputs: `knowledge/reference/craft/riot/` (README, `universal-principles.md` = master, topic files, `matrix.md`), `coverage/modeler.md` (incl. §d and §e), `proposals/modeler.md`, `job-card.md`, `reviews/modeler-rev1-reviewer.md`, `reviews/modeler-rev2-reviewer.md`. Every command line in `modeling-craft/references/read-commands.md` was run on synthetic images in the reviewer's scratchpad; nothing in the repo was run against or changed except this file.

```text
<spec>
artifact: .agents/roles/modeler.md (body) + .agents/skills/modeling-design/** + .agents/skills/modeling-craft/** (not evals) @ working tree 2026-10-22 (repair round 2), base df13ff4
reviewer: J018 reviewer modeler (opus, high), round 3
looked_at_first: [all 15 book files read in full before the coverage table (role; design SKILL + budgets, kits-and-environment, read-and-form, reference-check, review; craft SKILL + blender-recipes, export-import, handoffs, read-commands (new), rig-parts, textures-materials, tripo-finish); git diff -U0 df13ff4 removed lines of all 13 changed files; headings diffed against df13ff4; universal-principles.md UP-01..UP-20 principle, model line, general check and applies-to (unchanged since the G1 commit); check line of all 230 modeler-tagged library findings (script over the topic files); look_check.py --help for every mode, thumb's fit_size (aspect kept, padded); review_renders.py camera and resolution code; Camera.yaml FieldOfView (vertical, default 70); players/tools.md (Handle, Grip); Humanoid.yaml EquipTool; studio-mcp tools.md (datamodel_type, screen_capture time-out) and SKILL C-03/C-08; modeling-craft/evals/briefs.md; synthetic runs: region mask (works), top 5 % L and S, detail density on a square render and on a 1600x720 game-camera frame, phone-aspect crop + thumb on a 1000x700 capture, thumb at the model's WxH on a full frame, palette --mask on a flat fill (k_effective 1: CL5 works)]
findings:
  - id: F1
    class: blocking
    where: "modeling-craft/references/read-commands.md:20-27 (§3 detail density, command at :22); modeling-craft/SKILL.md:99 (Detail density row); modeling-design/references/review.md:140 (DT10); modeling-design/SKILL.md:94 (P6 check)"
    expected: "C3: DT10 (the line that closed rev2 F1 for VH-05) can be run as written: the command writes the detail-density image that DT10 and the §3 'Read' line tell the agent to look at, and it works on the files the books name as its input (the game-camera render and its black-fill at the model's phone-size WxH)."
    observed: "(a) The one-liner builds the cell image H but never saves it: sys.argv[4] (<checks>/<name>.detail.png) is never used, so the only output is 'cells N busy share X'; where the busy cells sit, which is what DT10 judges, cannot be seen. (b) It resizes the whole frame, background included, to the model's on-screen WxH without keeping the aspect, so on a game-camera frame the model shrinks to a few pixels and no cell qualifies. The coverage file (§e) says the test showed 'busy cells at the top', so the tested version differs from the written one."
    evidence: "Run on a 400x400 render: prints 'cells 14 busy share 0.43', no .detail.png written (ls of the output folder); same line plus ';Image.fromarray(H).save(sys.argv[4])' writes it. Run on a 1600x720 frame with a 60x200 px model at WxH 20x67 (the model's phone size at one third): 'cells 0 busy share nan' with numpy 'Mean of empty slice' warnings. grep 'save' read-commands.md:22: none."
    smallest_fix: "In §3: first crop the render and its black-fill to the black-fill's bbox (`look_check.py silhouette` JSON bbox_px, 2 px margin), resize both to the model's phone-size height keeping the aspect, and append ';Image.fromarray(H).save(sys.argv[4])' to the command; say in the craft SKILL §7 Detail density row 'on the crop to the black-fill bbox'. Re-run once on a real game-camera render and keep the output image in the test note."
  - id: F2
    class: blocking
    where: "modeling-craft/references/read-commands.md:14 (top 5 % command, channel S = PIL HSV S), :16; modeling-craft/SKILL.md:94 (Top 5 % row); modeling-design/references/review.md:128 (CL7); modeling-design/SKILL.md:88 (P3 check)"
    expected: "CL7 (LC-22: the saturation peak sits on the focal zone) measures how colourful a pixel looks, so the most saturated image marks the focal zone's strong colours and not near-black pixels."
    observed: "Channel S uses HSV saturation, (max-min)/max, which is high on very dark pixels with any tint. The books' own VL2 makes the lower body darker, and Studio captures carry tinted near-black shadows, so CL7 marks the boots and shadows as the saturation peak, fails, and tells the agent to change a lower body that is right (grey it out, against CL4's 'no grey, muddy shadows')."
    evidence: "Synthetic render: red focal torso sRGB (210,90,90) and near-black brown boots (25,14,8). HSV S = 145 vs 173, chroma (max-min) = 120 vs 17. The written S line marked 0 torso pixels and 1,827 boot pixels; the same line with chroma (a.max(2)-a.min(2)) marked the torso (14,140 px) and 20 boot pixels."
    smallest_fix: "In the §2 command replace `n.asarray(i.convert('HSV'))[...,1]` with chroma: `(lambda a:a.max(2)-a.min(2))(n.asarray(i.convert('RGB')).astype(int))` (or CIELAB chroma), and call channel S 'chroma (how colourful, not HSV saturation)' in §2, the craft §7 row and CL7."
  - id: F3
    class: blocking
    where: "modeling-craft/references/read-commands.md:29-33 (§4 phone-aspect crop); modeling-craft/SKILL.md:100 (Studio capture row: 'crop the capture and its mask capture to the phone aspect ... before thumb'), :91 (Phone size row, first option); modeling-design/references/review.md:167 (IM1 'measured at phone size')"
    expected: "C4/C3: the phone-size view shows the model at the size a phone shows it. Roblox's FieldOfView is vertical (Camera.yaml: 'how many degrees in the vertical direction'), so a capture at the game FOV keeps its vertical scale at any aspect, and `look_check.py thumb` already keeps the aspect and pads (fit_size)."
    observed: "(a) The crop removes height whenever the capture is narrower than the phone (the usual case: a Studio window near 16:9 against a phone near 19.5:9), so the model is enlarged before thumb and IM1's SL1, SL2 and DT2 at phone size pass too easily; the books' own example (1000x700 to 1000x450 for 800x360) enlarges the model 1.56 times. (b) The Phone size row's first option ('WxH = the model's on-screen size') applied to a whole render or capture shrinks the whole frame, background included, to the model's size, so the model ends far below its real size and the check fails or reports invalid-mask."
    evidence: "1000x700 capture, model 101 px tall (true phone height at 360 px = 52 px): thumb --size 800x360 without the crop gives bbox h 52 (scale 0.514, correct); after the §4 crop it gives h 81 (scale 0.8, area 2.4 times). thumb --size 20x67 on a 1600x720 frame with a 200 px model: scale 0.0125, verdict invalid-mask."
    smallest_fix: "§4 and the Studio capture row: 'crop only the width, and only when the capture is wider than the phone aspect (FieldOfView is vertical: keep the full height); a narrower capture goes to thumb uncropped (thumb keeps the aspect)'. Phone size row: the first option only on a crop to the black-fill bbox; on a whole render or capture use the second option (the whole frame resampled to the phone viewport)."
  - id: F4
    class: recommendation
    where: "modeling-design/SKILL.md:82 (§7 intro: 'a check you run on your own review set'), :90 (P4 check), :102 (P10 check), :110 (P14 check), :114 (P16 check); :77 (§6 self-check names only review.md §5); review.md:88-90 (§5 intro); role .agents/roles/modeler.md:57 (hand-back fields); read-and-form.md:43 (posed models), :44 (expression faces), :101 (darker variant keeps appeal), :103 (remakes); modeling-design/SKILL.md:108 (P13 'the first option is a warm-up')"
    expected: "One self-review list the agent runs at hand-off holds every checkable finding (owner J018). The 'same game' check (SI-06, SI-07, UP-11 general check: 'next to 2-3 approved anchors at the same size: it reads as the same game') guards the studio's most common visual failure, the generic image-model or Tripo look."
    observed: "The §5 list, the §6 self-check and the hand-back fields never send the agent to the §7 principle checks, and four of them have no §5 line: P4 (no region more finished than its equals), P10 (beside 2-3 approved anchor models it reads as one game), P14 (no proportion change after the gate without a decision line), P16 (each receiver's packet answers its brief keys). SL8 checks that a model differs from its neighbours, not that it belongs with them. Smaller conditional gaps with a checkable library check and no line: posed models' line of action (CF-02, SS-10), expression faces read in about two seconds (EX-04), a darker variant still reads appealing (CD-13), remake trait list (SI-11), first option labelled a warm-up (RI-21)."
    evidence: "grep review.md §5: 'one game' 0, 'anchor model' 0, 'line of action' 0, 'warm-up' 0, 'remake' 0. Library checks: SI-06 'Place the new render next to 2-3 approved anchors at the same size: it looks like the same game'; CF-02 'black-fill of each key pose shows both knees and the extended limb as separate shapes'; EX-04 'Show the emote or icon for 2 s at the real player size: a fresh agent names the intent'."
    smallest_fix: "Append IM5 to review §5: 'Beside 2-3 approved anchor models at the same game camera and size it reads as one game (value grouping, palette, edge treatment, detail scale); a miss goes to §3 \"does not look like our game\"'. Add to the §5 intro: 'The core-principle checks in modeling-design §7 are covered by these lines; P4, P14 and P16 are recorded here too' and give each a short line (or one IM6 line for the three). Append the five conditional items to SL10 (expression faces), VA (darker variant, remake list), SL9 (warm-up labelled) and a 'Posed models' clause to SL5."
  - id: F5
    class: recommendation
    where: "modeling-design/SKILL.md:35 (step 4: Tripo input pack at the route step); role .agents/roles/modeler.md:36 (step 4) vs :37 (step 5 silhouette gate); modeling-craft/SKILL.md:28-29 (step 2 blockout, then step 3 'Tripo: write the input pack'); tripo-finish.md:36 ('matches the frozen blockout or beats it'); reference-check.md:63 ('The route may change at blockout')"
    expected: "One order for the Tripo route, so the raw candidate can be compared with a frozen blockout (eval brief 2, the hero pet)."
    observed: "The design skill and the role write the input pack at step 4, before the silhouette gate (step 7); the craft skill builds the blockout first and writes the pack in step 3; tripo-finish §3 compares the finished mesh with 'the frozen blockout'. An agent on brief 2 cannot tell whether the owner runs Tripo before or after the gate. The order was already split in df13ff4; the new gate makes it matter."
    evidence: "The cited lines."
    smallest_fix: "Design step 4 and role step 4: 'Tripo: write the input pack after the silhouette gate (step 7) froze the proportions; the raw candidate is then checked against the frozen blockout' (or state the opposite once, everywhere)."
  - id: F6
    class: recommendation
    where: "knowledge/jobs/J018-riot-craft/proposals/modeler.md:13 ('Rows 1-3 are job workflow or job recipe changes') vs row 4 (`.agents/workflows/jobs/job-stage.js`)"
    expected: "Every proposal that touches a saved job workflow or a job recipe is named as one, so the lead shows it to the owner at G3 (J018-D2 point 4)."
    observed: "Row 4 changes `job-stage.js` (a saved job workflow) but the intro names only rows 1-3."
    evidence: "The cited lines."
    smallest_fix: "'Rows 1-4 are job workflow or job recipe changes'."
keep: [all of round 1's and round 2's keep lists; new in round 2 and checked here: the region-mask recipe (run again: mask ∩ box, value --mask measures the body); the top 5 % tie rule (prints both shares); FieldOfView set and restored for captures (vertical FOV, default 70, correct); the in-hand Tool capture for held items (one Handle, Tool.Grip, EquipTool on Server, Client camera for the front view, time-out fallback to not verified, probe-first); SL11, VL8, CL7's intent, DT10's intent, VA6, IM4 and the DT6/IM2 additions; the simple-model path stated the same way in design step 1, review §1, §2 and §5; the dedup (TM §8, RPA §6, KE §6 keep the how and point to read-and-form for the standards) with nothing lost; M rows as one-line pointers to §7 (design SKILL now 22.5 KB, about 3,700 words); the proposals for a look_check detail mode and the studio-mcp capture probes]
verdict: fix-first
</spec>
```

## Earlier findings: status

| Id | Status | Evidence |
| --- | --- | --- |
| rev1 F1 Studio capture cannot be measured | fixed | craft SKILL §7 Mask capture row; IM1 fallback; EI §3 |
| rev1 F2 box-based region numbers | fixed | read-commands §1 run again: region medians of the body |
| rev1 F3 checkable findings without a line | fixed | SL10, DT7-DT9, MO6, MO7, GR5 present; tags point to lines that carry them |
| rev1 F4 SKILL bloat | fixed (round 2) | M rows one line each; 22,518 bytes, about 3,700 words |
| rev1 F5 UP-02 motion and busy scene | fixed | P2 hand-over line |
| rev1 F6 value-band units | fixed | review §5 intro and VL5; conversions re-computed (0.0072, 0.0194, 0.692, 0.828) |
| rev1 F7 render count per gate | fixed | review §1 stage table |
| rev1 F8 short path | fixed | review §5 Simple models; RF §1; design step 1; role effort paragraph |
| rev1 F9 bake pointer | fixed | craft SKILL step 6 |
| rev1 F10 export origin | fixed | KE §6 first row |
| rev1 F11 a-d | fixed | P13; top 5 % row; BR §6 Client; design step 4 |
| rev1 C1 notes LC-11, PI-13 | fixed | coverage note; RC §7 item 2 |
| rev2 F1 checkable findings without a line | lines fixed; two of the new lines' commands are broken (F1 DT10, F2 CL7) | SL11, VL8, CL7, DT10, VA6, IM4 present; DT6 and IM2 extended; P3 and P6 checks name CL7 and DT10 |
| rev2 F2 top 5 % ties | fixed | read-commands §2 tie rule; both shares printed |
| rev2 F3 capture FOV and aspect | FOV fixed; the aspect fix measures wrong (F3) | craft SKILL §7 Studio capture row; read-commands §4 |
| rev2 F4 short path stated two ways | fixed | design SKILL:32, review:12, review:27 |
| rev2 F5 standards written twice; compaction | fixed | TM §8, RPA §6, KE §6 point to read-and-form; standards kept there |
| rev2 F6 held item captured on the floor | fixed (probe-first) | EI §3 Held items; IM1; §2a FM36; P2; role step 8 |

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass with 2 row failures (in F1, F2) | 261 rows checked: 230 tagged `modeler` in `matrix.md` (script-compared: all present once, none missing), 11 untagged, 20 UP rows. All 15 files read in full; every landed-in location carries the rule. Failed on the check part: VH-05 (DT10's command writes no image and gives 0 cells on a game-camera frame), LC-22 (CL7 measures HSV saturation, which marks near-black pixels). The 9 full and 13 partial rejections have sound reasons (animation, rigging, art direction, `reference-images`, level and environment design, each with the modeler's share landed). |
| C2 core principles | pass | §7 in `modeling-design` (the skill loaded first): P1-P19 state UP-01..07 and UP-09..20 for a model, each with its own example and check; UP-08 skipped with a sound reason (master does not list the modeler). No contradiction with the master (unchanged since G1). The checks of P4, P10, P14 and P16 are not in the hand-off list (F4). |
| C3 self-review | fail (F1, F2, F3) | Every other checkable modeler finding has a runnable line; region masks, mask capture, tie rule, contrast samples and palette --mask work as written (run). DT10 cannot run (F1); CL7 gives the wrong answer on dark lower bodies (F2); the phone-size view of captures is too large and the model-size option too small (F3). Minor gaps: F4. |
| C4 kit rules and engine | fail (F3) | No conflict with AGENTS.md, rules/, J018-D2/D3/D4 or Roblox limits; no invented tool modes (all look_check modes and flags exist; output names match). Engine claims checked: FieldOfView vertical and default 70, Tool Handle and Grip, Humanoid:EquipTool, datamodel_type Server and Client, screen_capture time-out in Play. The phone-aspect crop contradicts the vertical FieldOfView (F3). |
| C5 nothing valuable lost | pass | Removed lines of df13ff4 walked again: every one is kept, moved or sharpened (coverage §c matches); the round-2 dedup moved standards into read-and-form §3-§4, §6, §8 without loss (gold, skin, hue and value ranges, below-waist paint, hair at the nape, buried base all present). |
| C6 fixed rules | pass | Only the modeler books plus `coverage/modeler.md` and `proposals/modeler.md` changed for this role (other modified paths belong to the other wave-1 makers and the lead); role frontmatter byte-identical to df13ff4; design SKILL 120 lines, craft SKILL 101; descriptions 394 and 391 characters; headings: two titles reworded, no number changed, new sections appended; J018 phrase once in each of the 15 files (14 skill files incl. 2 new, plus the role comment); no library ID, Riot game, champion, artist or transcript line in any body ('Riot' only in the required header phrase); no tips section; evals unchanged; tools/, rules/ and job workflows unchanged. `sync_harness.py --check` drift in `.claude/` and `.codex/` copies is expected until the lead syncs. |
| C7 better work | yes, with weak spots | See below. |

## Will an agent with these books make better work?

Yes. Read as an agent on eval brief 1 (the starter sword, medium effort) and brief 2 (the Tripo hero pet), the old books said "blockout, then approve the big shapes" and "one review render set". The new books make the agent write a read plan (sell list, anchors, read order, on-screen size on the smallest phone) before building, pass a measured silhouette gate at the game camera and phone size before detail, pass a grey value gate and the art director's check-in before polish, texture in value-first passes with a check per pass, design for the rig before the final mesh, capture a held sword in the avatar's hand in Studio, and close with a cold read, an iconic-quality check against the image and an honest weakness. The short path keeps a medium sword proportionate. Weak spots: three of the round-2 measuring recipes give wrong numbers (F1 detail density writes no image and fails on game-camera frames; F2 the saturation image marks dark boots instead of the focal colour; F3 the phone-size view of a Studio capture is up to about 1.6 times too large). An agent that trusts F2 would grey out a correct dark lower body, so these are blocking, but each fix is one line. The core-principle checks for "reads as one game with the anchors" and three others are outside the hand-off list (F4), and the Tripo route has two orders (F5).
