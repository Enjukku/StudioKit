---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer ui-ux-designer · claude-opus-5-5 · high · 2026-10-22

# Review: ui-ux-designer books, rebuild round 2 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/ui-ux-designer.md (body) + .agents/skills/ui-design/ (SKILL.md, references/ incl. worked-examples.md) + .agents/skills/ui-figma/ (SKILL.md, references/) + .agents/skills/ui-style-cartoon|anime|pixel|stud/SKILL.md, working tree on top of df13ff4 after repair round 1, 2026-10-22
reviewer: J018 reviewer ui-ux-designer (opus, high)
looked_at_first: [
  the round-1 review (F1, F2, R1-R8) to know what to re-check,
  all 17 book files read in full as they are now; git diff df13ff4 on every one, removed lines of the role file and ui-design SKILL.md walked one by one; diff of the four style books and four ui-figma references,
  tools/vfx/clip_metrics.py source (median background, DIFF_THRESHOLD 40, UI_MASK, onset = first frame with coverage >= max(0.2, 10 % of peak)), look_check.py value/contrast/palette/thumb/silhouette -h,
  my own V3 runs in the reviewer scratchpad r2/: press folders (300 x 160 crops of a button over a noisy sky, 30 fps JPEG) for the worked example, a press followed by the confirmed outcome inside the window, a HUD button with a drifting cloud in the margin; the S-49 hit-target one-liner and the S-44 reveal one-liner extracted verbatim from review.md lines 80-81 and run on my own CSVs and reveal folders,
  knowledge/reference/craft/riot/universal-principles.md UI lines of UP-01..UP-20; matrix.md ui-ux column (144 IDs, script compare with the coverage table: none missing, none extra; the 35 other rows are the UP table and untagged findings),
  partner anchors: preproduction/references/documents.md §6/§7/§9, game-design/references/review.md §7, progression-craft/references/data-handoff.md §5, animation-design game-timing §4, vfx-design juice-repetition-sync T-05/T-09, sound-design reward-and-juice S-194,
  orchestration/references/job-types.md §4 (UI screen), ui-design/evals/briefs.md (common checks, briefs 1 and 2)
  ]   # the maker's coverage and proposals files were read after this
previous_findings:
  - {id: F1, status: fixed, note: "S-49 added (review.md:111) with the hit-target one-liner (:81) and its wrong-without-error notes (:93); SKILL §3 step 5 and §6 lines 2 and 5 restored; ui-figma F-24 and §6; screen-contract §5; four style books; role file S-01..S-49. My verbatim runs: a passing layout gives no FAIL and the primary as biggest; a 128 px Buy, an 80 px close, a 10 px gap and a target in the thumbstick zone each FAIL; a container row is flagged as the note says"}
  - {id: F2, status: "fixed (capture rule); one remaining wrong-number case found: F3",
     note: "Capture rules (idle majority, ms from capture start, press ms noted), metrics.json onset_ms, pre-press coverage 0, null = UNVERIFIED are all in review.md:91 and S-33; worked example corrected. My run of the worked example's own folder (13 idle, press 400 ms, 7 changed) gives onset_ms 433 with every pre-press frame at 0: right"}
  - {id: R1, status: fixed, note: "Reveal one-liner crops one box and counts pixels changed by > 40; my run: noise pair 0 changed pixels, a 6 x 6 px glint 60-71 changed pixels from its frame on, detected even on the whole frame by the count"}
  - {id: R2, status: fixed, note: "ui-figma §1 compaction note (re-read §3, §5, §6)"}
  - {id: R3, status: "adopted for the named items, declined for the rest with a sound reason", note: "rule sheet names the art bible §7 rows, never re-typed (style-choice.md:194); §7 check cells cite S-ids; the remaining repeats are one-line pointers at the step where the agent acts, no drift found"}
  - {id: R4, status: fixed, note: "screen-contract.md:81-82, 2 taps + a reasoned extra tap row"}
  - {id: R5, status: fixed, note: "SKILL.md:47 and :58"}
  - {id: R6, status: fixed, note: "SKILL.md:26; role file work method step 1"}
  - {id: R7, status: fixed, note: "style-choice.md:187; SKILL step 4 points to it"}
  - {id: R8, status: fixed, note: "coverage header corrected; clip_metrics proposal row names the 'stays pressed or Buying…' case"}
findings:
  - {id: F3, class: blocking, check: C8 V3 (+ C1 row UI-12, C3),
     where: ".agents/skills/ui-design/references/review.md:91 (clip_metrics note: 'the lag is onset_ms − press ms') and :147 (S-33); worked-examples.md:25; §7 capture list :169",
     expected: "V3: on the real input the command gives the right answer, and the book names what makes it give a wrong number with no error. The real input for S-33 in the review slot (§7) is a Studio frame folder of a press on a build; in a Studio play-test the server answers within a frame or two, so the confirmed outcome (popup closes, reveal starts, Roblox prompt opens, '+1' lands) normally falls inside the 7 post-press frames the capture rule asks for",
     observed: "summary.onset_ms is the first frame whose coverage reaches max(0.2 %, 10 % of the clip's peak) (clip_metrics.py:82-83). When a bigger change follows the press inside the folder, a small attempt cue under 10 % of that peak is skipped and onset_ms lands on the outcome. The book tells the agent to compute the lag from summary.onset_ms, so a correct button reads as a laggy one: a false FAIL with no error, sent back to the builder from the review slot. Not in the note's wrong-without-error list. Second, smaller case: a HUD button over a moving world (clouds, players) gives pre-press coverage above 0; the note says 're-capture with more idle frames', which cannot fix it, so the check can never pass",
     evidence: "My runs (scratchpad r2/, 30 fps, 13 idle frames, press frame 400 ms, cue on the next frame = true lag 33 ms): (I) small sink (coverage 7.3 %) then the popup closes at 567 ms (99 %): onset_ms 567, lag 167 = FAIL, pre-press frames all 0, no error; (G) sink 9.4 % then 'Hatching…' 11.4 % then the popup closes: onset_ms 467 (one frame late); (H) the worked example's own case without an outcome: 433, right; (J) a cloud drifting through the crop margin: pre-press coverage 0.32-3.15 %, onset_ms 67",
     smallest_fix: "In the review.md §6 clip_metrics note and S-33: 'The lag is the ms of the first frame after the press whose coverage_pct rises above the highest pre-press value (read it from frames in metrics.json), minus the press ms; summary.onset_ms is only a cross-check: it uses 10 % of the clip's peak, so a bigger change later in the folder (the popup closing, the reveal, a Roblox prompt) hides a small press cue. For a control over a moving world, crop inside the control's face or capture over a still backdrop; more idle frames do not fix a moving margin.' Keep pre-press coverage 0 as the rule for still backdrops. Add the case to the clip_metrics proposal row (an idle-frame background or --region also removes it)"}
  - {id: R9, class: recommendation, check: C7 (the check is only as good as its kind column),
     where: "review.md:93 (S-49 kinds primary / frequent / minor), :111; screen-contract.md:56-67; worked-examples.md:25 ('close 110 × 110 (minor)')",
     expected: "A rule that says which tap targets are frequent (44 pt) and which are minor (28 pt), so the agent cannot pass S-49 by labelling a control minor",
     observed: "No book defines frequent vs minor. The worked example classes the popup's close X, which the player uses on most visits, as minor at 110 px (about 32 pt); eval brief 1.5 checks exactly the close button on a kids' phone game. An agent copies the example",
     evidence: "grep 'minor' over ui-design and ui-figma: only the Apple 44 / 28 numbers and the S-49 kinds; worked-examples.md:25",
     smallest_fix: "One clause in the S-49 note: 'kind comes from the flow sheet's How often column: a target the player uses on most visits of the screen (buy, close, back, tabs, HUD buttons) is frequent; minor only for rare controls (info, a settings toggle)'; make the example's close 150 × 150 or give the reason it is minor"}
  - {id: R10, class: recommendation, check: C7 (term clash),
     where: "ui-figma/SKILL.md:23 ('a phone-fit frame'), ui-design/SKILL.md:31 ('a phone-fit frame and a PC frame'), review.md:111 ('the phone layout frame'), screen-contract.md:51 ('phone-fit view' = the canvas resampled to 565 × 318)",
     expected: "One name for the phone layout frame, with its size, so S-49's canvas-px thresholds apply to it",
     observed: "'Phone-fit' means the 565 × 318 resample in screen-contract §5 and also the phone layout frame in ui-figma §3. An agent that builds the phone frame at 565 × 318 (or 667 × 375 pt) and runs S-49 with 150 / 96 / 27 gets a FAIL on every target; the worked example's numbers (Hatch 420 × 170) show the frame is meant to be 1920 × 1080 canvas",
     evidence: "the four lines above",
     smallest_fix: "ui-figma §3 step 1 and ui-design §3 step 5: 'a phone layout frame (1920 × 1080 canvas, the arrangement of the @ViewportDisplaySizeSmall variant; never a resampled copy)'; keep 'phone-fit view' for the 565 × 318 resample"}
  - {id: R11, class: recommendation, check: C7 (one-frame contradiction),
     where: "review.md:147 (S-33 '≤ 67 at 30 fps (the press frame or the next, PROPOSAL)'); review.md:41 check 24; motion.md:21",
     expected: "The number and its words agree",
     observed: "'The press frame or the next' is a lag of 0 or 33 ms; ≤ 67 allows the frame after next. The worked example measures from the last idle frame (lag 33 = 'the next'), so the 67 ms margin is one extra frame the words do not mention",
     evidence: "the three lines",
     smallest_fix: "Either '≤ 67 ms (within two frames at 30 fps, allowing one frame of capture jitter; PROPOSAL)' or '≤ 33 ms'; the master's 100 ms holds for both"}
  - {id: R12, class: recommendation, check: C7 (honest reveals: middle tiers unchecked),
     where: "review.md:158 (S-44 'the lowest vs the highest tier'), :169 (§7 asks for lowest and highest tier captures); shops-rewards-onboarding.md:111",
     expected: "The rule is 'no tier differs before the result'; the check should catch a tell on any tier",
     observed: "S-44 compares only the lowest with the highest tier, so a tell on a middle tier (only Epic shakes, only Rare tints) passes",
     evidence: "S-44 cell; shops §5 one-windup rule",
     smallest_fix: "S-44 and §7: 'the lowest tier against every tier that adds a layer after the result (one folder per tier; numbers only)'"}
keep: [
  the fixes of round 1: S-49 with a runnable hit-target check and honest notes, the S-33 capture rules with the pre-press coverage check, the boxed reveal difference with a changed-pixel count and a noise floor that rejects bad captures,
  the stage order flow → structure study → 2-3 wireframes (one atypical) → grey value pass → rule sheet → target images → Figma → motion, both gates, and the new scale-down line for changes inside an approved screen (SKILL §3 intro),
  review.md §6 staged S-lines with inputs, the command block and the wrong-without-error notes (value, contrast, palette, thumb, silhouette re-checked: options real),
  the rule sheet that names the art bible rows instead of copying them, the motion table seeded from ui-basics §A, attempt cue vs confirmed outcome with pending at about 100 ms,
  the partners table and review slot, the flow-sheet template that now obeys its own 2-tap rule, the two worked examples,
  §7 core principles (20 rows, each with an example and an S-id check; no contradiction with the master),
  the proposals file (recipe and workflow rows with reasons; tool rows for clip_metrics, seq_compare and hit_targets that would remove the manual one-liners)
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (1 of 144 rows) | 144 tagged IDs = 144 rows (script compare with matrix.md: none missing, none extra, no duplicates); every S-id and file named in a landed-in cell exists (script); landed-in content re-read in the books. UI-12 fails through F3 (S-33 gives a false FAIL on the normal Studio input); GD-02 and WT-01 also cite S-33 but are carried by S-43 and S-41. Rejections CR-10, PI-10, RH-05, SS-08, VR-04 and the CR-16 proposal-only row are sound. The round-1 record errors (R8) are corrected |
| C2 core principles | pass | `ui-design/SKILL.md` §7: 20 rows, each stated for UI with its own example and an S-id check; row 12 keeps the master's limit; rows 8, 19, 20 match the master's UI lines; §1 says to re-read §7 after a compaction |
| C3 self-review | fail (1 line) | Every checkable UI finding has an S-line with a runnable input (Figma metadata and screenshots, look_check modes, clip_metrics, the two one-liners, studio-operator captures, the owner at a named preview). S-33's lag reading is wrong when the outcome lands inside the capture (F3) |
| C4 kit rules and engine | pass | No change to rules/, tools/, workflows, evals, tools line, model or effort; recipe and workflow changes are proposals only; G1 additions (grey pass beside the wireframe) sit inside the recipe's 'grey-box wireframe'. Engine claims as verified in round 1 (PreferredTransparency, reduced motion, easing); all look_check options the books name exist (`-h`) |
| C5 nothing valuable lost | pass | Round-1 losses restored (touch rubric self-check, safe-area marking now S-49, D-05 and D-16 caveats). Removed old lines walked again: each is kept, moved (odds, ads and discounts to the platform-policy pointer and shops §3; 'disabled says why' to D-27; celebrate-after-confirm to D-26) or replaced by something stronger |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4; SKILL.md lines 118/85/110/107/102/103; descriptions 372-383 characters and unchanged; the J018 phrase in all 17 changed or new files; section numbers kept (new sections appended); no citations, library IDs or Riot names added (VALORANT, Hearthstone and the ready-check video are pre-existing J002 evidence); no tips section; evals/ unchanged; LF endings. Other modified files in the tree (sound-design, vfx-design) belong to other makers. Note for the lead: `sync_harness.py --check` shows the generated copies stale (expected before the lead's sync) |
| C8 brief v2 | fail (V3) | V1 pass (inputs per S-group; image budget review.md §5). V2 pass. V3: hit-target and reveal one-liners run verbatim and correct; clip_metrics right on the worked example's folder but wrong when the outcome follows inside the folder or the margin moves (F3). V4 pass. V6 pass (R3 resolved or reasoned). V7 pass (ui-design §6 ends at 17.4 KB; ui-figma §6 at 18.4-19.7 KB with the compaction note). V8 pass. V10 pass (sync rule, merge window, feedback-stack names, display rule anchors exist in the partner books). V11 pass |
| C7 better work | better; one check to fix | See below |

## Judgment (C7)

I read the books as the agent would at the start of eval brief 2 (stud HUD for an obby, mostly phones). The old books would give a styled HUD with a decision record and a phone-size note. The new books first make the agent list the HUD needs and give each a zone. Then the agent draws 2-3 layouts and checks the hit targets against the thumbstick and jump zones by numbers (S-49: the "must" checks 2.1 and 2.2 now have a runnable test). It proves the read order in grey before the stud texture goes on, and it specifies the skip-stage purchase as attempt, pending and confirmed states. The round-1 gaps are closed.

Weak spots that remain:
- The press-timing check can still give a wrong verdict on a real Studio build: a false FAIL when the outcome arrives inside the capture (F3; a one-sentence fix).
- Nothing defines which targets are "frequent", and the worked example classes a close X as minor (R9).
- "Phone-fit frame" has two meanings (R10).
- The books are about twice as long as before. That is the price of the staged S-lines, and the scale-down line now keeps small jobs small.

Fix F3 and this role is ready.
