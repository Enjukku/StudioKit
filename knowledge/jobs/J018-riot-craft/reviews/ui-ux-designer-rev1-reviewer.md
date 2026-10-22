---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer ui-ux-designer · claude-opus-5-5 · high · 2026-10-22

# Review: ui-ux-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/ui-ux-designer.md (body) + .agents/skills/ui-design/ (SKILL.md, references/ incl. new worked-examples.md) + .agents/skills/ui-figma/ (SKILL.md, references/) + .agents/skills/ui-style-cartoon|anime|pixel|stud/SKILL.md, working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer ui-ux-designer (opus, high)
looked_at_first: [
  all 17 changed or new book files read in full, then git diff df13ff4 on every one (removed lines walked one by one, old ui-design SKILL.md and old review.md read whole),
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20), ui-ux.md (UI-01..UI-19) read whole, matrix.md (ui-ux column: 144 findings, script-extracted, compared with the coverage IDs: 144/144, no extra, no duplicate), VR-04 and SS-08 (the rejections) read,
  platform-policy/references/rules.md §A-§D, ui-basics/references/ui-effects.md §A-§B, orchestration/references/job-types.md §4, .agents/workflows/jobs/job-ui-screen.js (UI-screen stages),
  roblox-creator-docs: production/publishing/accessibility.md:100-130 and :180-190, ui/animation.md:400-415, production/game-design/ui-ux-design.md:140-178,
  tools: look_check.py value/contrast/palette/thumb/silhouette -h, tools/vfx/clip_metrics.py source, all run on my own synthetic samples (scratchpad v3/: a 1920x1080 UI shot over a noisy sky/ground backdrop; 30 fps press folders cropped to a button; 1080p reveal folders with a tint on the egg),
  partner books: game-design/references/review.md "UI screen", preproduction/references/documents.md §6/§7/§9, animation-design/references/game-timing.md §3-§4,
  ui-design/evals/briefs.md (common checks C1-C6, briefs 1 and 2)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C3 + C5 + C1 (row UI-03),
     where: ".agents/skills/ui-design/references/review.md:85-110 (§6 S-01..S-15, the only self-review groups that run on the designer's own frames before a build exists); .agents/skills/ui-design/SKILL.md:88 (§6 line 5); .agents/skills/ui-figma/SKILL.md:76-83 (§6)",
     expected: "Old ui-design SKILL.md:70 (df13ff4) self-check: 'Sizes converted to the smallest supported phone (§5 of screen-contract) and meet the declared touch and text rubric'; old step 4: 'Mark interactive vs decorative bounds and the core-UI safe area'. Library UI-03 (ui-ux.md, apply DS + check): touch targets at least about 44 pt with gaps, the primary action bigger, nothing important in the thumbstick/jump zones, 'every needed item is visible, reachable by thumb'. Eval common check C2 (must) and briefs 1.5 and 2.2 (must) test exactly this",
     observed: "No S-line checks touch-target size or that interactive elements stay out of the no-go overlay. S-13 checks only critical STATE outside the overlay; S-23 checks that labels and marks still read at phone fit; release check 05 (review.md:22) and 06 exist but run only on Studio captures of a build (§1, §7). The new SKILL §6 line 5 says only 'Sizes converted to the smallest supported phone' (the 'and meet the rubric' clause is gone). The role file tells the agent to run S-01..S-48 before hand-back, so an agent following the new books can hand back a 128 px Buy (38 pt, the J002 G2 failure screen-contract.md:65 itself records) without any check failing. The coverage row for UI-03 lands it in S-23, which does not carry this check",
     evidence: "grep '44 pt|150 canvas|touch' over review.md §6: no S-line; old SKILL.md:70 vs new SKILL.md:88; ui-design/evals/briefs.md C2, 1.5, 2.2; screen-contract.md:56-66 (the size table the check would use)",
     smallest_fix: "Append one row to the Wireframe options group in review.md §6 (new id S-49, no renumbering): 'S-49 | On the phone-fit frame, every interactive element's hit area meets the declared touch rubric (default: frequent ≥ 150 canvas px, minor ≥ 96 px at f 0.294; screen-contract §5) with a gap between targets; the primary action is the biggest target; no interactive part inside the no-go overlay (ui-figma F-24). Input: Figma node bounds (get_metadata).' Restore SKILL.md §6 line 5 to '... converted to the smallest supported phone and meet the declared touch and text rubric (S-49)', add S-49 to ui-figma §6, and point the UI-03 coverage row at S-49"}
  - {id: F2, class: blocking, check: C8 V3 (+ C1 row UI-12, C3),
     where: ".agents/skills/ui-design/references/review.md:78, :83 and :136 (S-33); motion.md:39 (§5); ui-figma/references/figma-mcp.md §6 ('0 ms on the trigger ... crop to the control first'); worked-examples.md:25 ('S-33: onset_ms 33 on a frame folder cropped to Hatch')",
     expected: "V3: the command gives the right answer on the real input, and the book names what makes it give a wrong number with no error. The real input for S-33 is a frame folder of a button press; after a press the button normally stays changed (pressed, then 'Buying…' pending, then disabled against a repeat commit: shops-rewards-onboarding.md §2 commit row)",
     observed: "clip_metrics.py takes the per-pixel median of ALL frames as the background (clip_metrics.py:100). When the control stays changed in more than half the frames, the median IS the pressed look, so the idle frames before the press count as 'effect' and onset_ms is 0 whatever the real lag: a button that answers 300 ms late still passes S-33 (≤ 67 ms). The book's fix ('crop every frame to the control first') does not help: my run was already cropped. The worked example teaches a number (33 ms on Hatch, which goes to 'Hatching…') that this tool would report as 0. Two more silent cases: a press that changes the face by less than 40 levels per channel (DIFF_THRESHOLD, clip_metrics.py:28) gives onset_ms null; and onset_ms is written only to metrics.json in the folder (stdout prints peak and visible only, clip_metrics.py:123), which the book does not say. The '0 ms on the press' naming also cannot hold once idle frames precede the press (the frame regex needs ms ≥ 0)",
     evidence: "My runs on 240x160 crops, 30 fps, 31 frames: press at 67 ms and stays sunk + 'Buying...' → onset_ms 0; press at 67 ms that returns after 4 frames → 67 (right); press that only darkens the face by 20 levels → onset_ms null; same staying press with 10 idle frames then 8 pressed (idle majority) → onset_ms 333 = the press frame (right). Folders in the reviewer scratchpad v3/press_*",
     smallest_fix: "Rewrite the clip_metrics note in review.md §6 (and the S-33 cell): 'Capture more idle frames before the press than changed frames after it (for example 10 before, 8 after) so the median is the idle look; name frames from the capture start and record the press frame's ms; read summary.onset_ms in <folder>/metrics.json (stdout does not print it) and check frame 0 has coverage_pct 0; onset − press ms ≤ 67 at 30 fps. A press that changes the control by less than about 40 levels per channel registers nothing (onset null): that is UNVERIFIED, not PASS.' Point motion.md §5 and figma-mcp.md §6 to that note instead of '0 ms on the press', correct worked-examples.md step 10, and add the pending-state case to the clip_metrics proposal row"}
  - {id: R1, class: recommendation, check: C8 V3 (S-44),
     where: "review.md:80 and :147 (manual per-frame difference), S-44 (:147); worked-examples.md:25 (noise floor 0.3)",
     expected: "The paid-reveal check detects a tier-specific layer during the windup on a real capture",
     observed: "The one-liner averages the difference over the whole frame, so a small tier tell (a gold glint on a 48 px egg corner, a faint rarity tint) is diluted below a real-capture noise floor; the worked example's own numbers (noise floor 0.3) sit inside the range my tinted sample produced on the maker's run (0.24-0.36, coverage table d). A false 'identical windups' PASS is possible with no error",
     evidence: "My run, 1080p, tint on a ~200x260 px egg: noise 0.01-0.03, tinted 0.91-1.31 (detected); the same tint on a 10x smaller area scales to ~0.1, under a 0.3 floor",
     smallest_fix: "Add to the S-44 note: 'crop both folders to the reveal object's box (same box) before diffing, and compare each frame's value with the noise floor's maximum for the same box, not the whole frame'"}
  - {id: R2, class: recommendation, check: C8 V7,
     where: ".agents/skills/ui-figma/SKILL.md:67-85 (§5 rules from byte 17,483, §6 self-check bytes 18,269-19,525)",
     expected: "Steps, rules and self-check within roughly the first 5,000 tokens (about 18 KB); otherwise §1 says what to re-read after a compaction",
     observed: "The F-table grew (F-03, F-07 longer; F-25..F-29 added) and pushed §6 past ~18 KB (old file 15.8 KB total). Borderline; §1 has no compaction note",
     evidence: "byte offsets measured with head -n | wc -c",
     smallest_fix: "Add to ui-figma §1: 'After a compaction, re-read §5 and §6 of this file.' (or move F-26..F-29 detail into a reference and keep one-line rows)"}
  - {id: R3, class: recommendation, check: C8 V6 / C7 (duplication),
     where: "'one attention motion' stated in 10 places (SKILL D-14, §5, §7 row 3; motion.md §1; review.md S-34 and §2; shops §6; effect-assets §3; stud sunburst; worked example); 'outcome only on confirmation' in 6; SKILL §7 example/check cells restate D-20..D-28; style-choice.md §5 'Colour roles: copied from the art bible's colour roles'",
     expected: "One rule, one place; others point to it",
     observed: "No drift today (I compared the numbers: pending 100 ms, pulses ≤ 1 Hz / ≤ 3 Hz, toasts ≤ 3, merge window 100 ms agree everywhere), but the rule sheet copying the art bible's colour-role rows is a second copy of binding data that will drift when the art director edits the bible",
     evidence: "grep counts; style-choice.md:71",
     smallest_fix: "Rule sheet: 'Colour roles: the art bible's rows by name (never re-typed), plus the UI-only roles with hex'. SKILL §7 check cells: cite the S-id/D-id instead of restating the rule where they already do both"}
  - {id: R4, class: recommendation, check: C7 (worked template contradicts its rule),
     where: ".agents/skills/ui-design/references/screen-contract.md:81 (flow sheet example row) vs :83",
     expected: "PROPOSAL default: frequent actions within 2 taps of the HUD (plus Roblox's prompt); every extra tap has a reason",
     observed: "The template's only example row is a frequent task ('every session, many times') at '3 + prompt' with 'Extra taps and why: none'. An agent copying the template copies the contradiction; worked example 1 does it right (2 taps)",
     evidence: "screen-contract.md:81-83",
     smallest_fix: "Change the example to 'HUD shop button → egg card → Buy → Roblox prompt | 2 + prompt' or keep 3 and write the reason in the last column"}
  - {id: R5, class: recommendation, check: C5 (small caveats lost),
     where: "SKILL.md:47 (D-05) and :58 (D-16)",
     expected: "Old D-05 '(not 2026, not playtime)' and old D-16 'pseudo-locale finds weak boxes, not translation quality' kept or moved",
     observed: "Both qualifiers were dropped in the rewrite; neither is in screen-contract §6 or review.md. They stop two known misuses (quoting the DAU split as playtime; treating a pseudo-locale pass as a translation check)",
     evidence: "git show df13ff4:.agents/skills/ui-design/SKILL.md lines 43 and 54",
     smallest_fix: "Put the two clauses back in D-05 and D-16 (a few words each)"}
  - {id: R6, class: recommendation, check: C7 (over-process on small jobs; rules/anti-overengineering.md),
     where: "ui-design SKILL.md §3 (12 steps), role file Work method and 'Before you hand back' (S-01..S-48)",
     expected: "Build what was asked at the size it needs",
     observed: "Nothing says which stages a small change runs: a one-button fix on an approved screen reads as structure study + 2-3 wireframes + grey pass + target images + 48 S-lines. A medium-effort agent will either over-process or skip arbitrarily",
     evidence: "grep 'skip|small change' over the books: none",
     smallest_fix: "One line in SKILL §3: 'A change inside an approved screen runs only the stages it touches (from its pain point down) and the S-lines of those stages; the approved wireframe, rule sheet and target image stand.'"}
  - {id: R7, class: recommendation, check: C7 (input missing),
     where: "SKILL.md:30 (step 4 structure study); style-choice.md:64",
     expected: "The study traces real screens (the brief's references or owner screenshots)",
     observed: "No line for the common case where none are given; the agent will 'trace' genre screens from memory and present them as a study",
     evidence: "style-choice.md:64 names only the brief's references or owner screenshots as inputs",
     smallest_fix: "Add: 'No screenshots given: ask the lead for 2-3, or capture them in the built-in browser and log the source; a study from memory is labelled not verified'"}
  - {id: R8, class: recommendation, check: C1 (record accuracy),
     where: "knowledge/jobs/J018-riot-craft/coverage/ui-ux-designer.md:17 and :23 (clip_metrics proposal row in proposals/ui-ux-designer.md:23)",
     expected: "The coverage record states what the books hold",
     observed: "':17' says the engine fact 'Camera:WorldToViewportPoint does not account for the GUI inset' was added to the books; no book file contains it (it is builder territory, so dropping it is fine, but the record is wrong). The clip_metrics proposal's reason names only the popup case, not the pending-state case of F2",
     evidence: "grep WorldToViewportPoint over the UI books: no match",
     smallest_fix: "Correct the coverage sentence; add the F2 case to the proposal row"}
keep: [
  the stage order flow → structure study → 2-3 wireframes (one atypical) → grey value pass → rule sheet → target images → Figma → motion, with the wireframe gate and the style gate (SKILL §3; ui-figma §3 Flow/Wireframes pages, F-25 grey frame the style keeps),
  review.md §6 as staged S-lines that each name their input, the command block, and the honest 'wrong number without an error' notes for value/contrast/palette/thumb (all four confirmed by my runs),
  the read-order measure: --compare-subjects on the grey frame and the same boxes on the styled screen (S-10, S-16),
  motion.md §7 one motion table per game seeded from ui-basics ui-effects §A (one place for starting values) and §8 refusals, true counters, frequent events, pulse classes, celebrations,
  attempt cue vs confirmed outcome with pending at ~100 ms across motion §2, the purchase state machine and S-37,
  paid-random screen side as a pointer to platform-policy §A with the label-word proposal (V4 clean),
  the partners table (what to ask whom, when) and review.md §7 (my review slot inputs and return paths),
  F-21 fixed to the measured fit (thumb 565x318, f 0.294) instead of the wrong 0.33-0.35,
  the two worked examples (egg shop, mining HUD), SKILL §7 core principles (20 rows, no contradiction with the master),
  proposals file: recipe and workflow rows with reasons, tool rows, partner rows
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | fail (2 of 144 rows) | 144 tagged findings = 144 rows (script compare with matrix.md, no gaps or extras); landed-in locations opened for all rows. Failed: UI-03 (its check has no S-line, F1); UI-12 (S-33 passes a laggy press, F2; GD-02 and WT-01 also lean on S-33). Rejections CR-10, PI-10, RH-05, SS-08, VR-04 and the CR-16 proposal-only row have sound reasons. Coverage record inaccuracy: R8 |
| C2 core principles | pass | `ui-design/SKILL.md` §7, 20 rows, each with its own example and check; row 12 keeps the master's limit (consistency wins); rows 9, 19, 20 match the master's UI lines (press feedback within 100 ms is met by S-33's 67 ms; ≤ 3 Hz; critical marks ≥ 3:1). No contradiction found; §1 says to re-read §7 after a compaction |
| C3 self-review | fail | Touch-target / no-go check missing (F1); S-33 measurement unreliable on the normal input (F2). Every other checkable UI finding has an S-line with a runnable input (Figma metadata/screenshots, look_check modes, studio-operator captures, the owner at a named preview) |
| C4 kit rules and engine | pass | Engine claims checked in the mirror (PreferredTransparency 0 = opaque, default 1 = most transparent; reduced motion tween time 0; Quad default; conventions page). No change to rules/, tools/, workflows, evals, tools line, model or effort. Recipe and workflow changes are proposals only |
| C5 nothing valuable lost | fail | The 'meet the declared touch and text rubric' self-check and the wireframe safe-area marking were dropped (F1). Two small caveats dropped (R5). Everything else removed is kept, moved (ads and paid-random rules to platform-policy pointers) or replaced by something better |
| C6 fixed rules | pass | Frontmatter byte-identical (md5 of the first 11 lines); SKILL.md lines 118/85/110/107/102/103; descriptions 372-383 characters; J018 header phrase in every changed skill file and the role comment; no section renumbered (new sections appended; ui-design review §6-§7, motion §7-§8, style-choice §5-§6, screen-contract §7-§8); no tips section; evals/ unchanged; LF line endings. The names VALORANT, Hearthstone, 'Riot's ready-check video' in D-01, motion.md §1 and style-choice §4 are pre-existing J002 research-paper evidence, not J018 additions |
| C8 brief v2 | fail | V1 pass (inputs per S-group, image budget in review.md §5). V2 pass (every named mode exists). V3 fail on S-33 (F2), weak on S-44 (R1); value, contrast, palette, thumb, silhouette re-run by me and correct. V4 pass. V6 recommendation (R3). V7 ui-design pass (self-check ends at 16.7 KB), ui-figma borderline (R2). V8 pass (partners table, review slot). V10 pass (sync rule, attempt/outcome, feedback-stack names match animation-design and game-design). V11 pass (game-designer, progression, sound rows adopted with reasons) |
| C7 better work | better, with the weak spots above | See the judgment below |

## Judgment (C7)

Read as the agent at the start of eval brief 1 (cartoon egg shop for kids on phones), the new books produce clearly better work than df13ff4. The old books had a decision record and a style pick, then went straight to Figma. The new ones make the agent count taps first. It compares 2-3 layouts and proves the read order in grey with a number before any styling. It writes the refusal ("Need 150 more coins"), the pending state and the honest reveal as checks it can run, and it asks the game designer, the sound designer and the VFX designer for the right inputs at the right step. The measured self-review replaces "looks fine in grayscale" with commands whose failure modes are written down. That fixes the J002 "B minus" causes (weak hierarchy, equal gloss everywhere, no target).

Where it is still weak:
- The one self-check the eval marks "must" for this brief is gone: touch size on the smallest phone (F1).
- The press-timing check passes any button that stays pressed or pending (F2).
- The books are about twice as long (ui-design SKILL 10.8 KB to 23.8 KB, review.md 4.5 KB to 20 KB), with rules restated in many places (R3) and no guidance that scales the 12 stages down for a small fix (R6).

Fix F1 and F2 and this role is ready.
