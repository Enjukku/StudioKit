---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer ui-ux-designer · claude-opus-5-5 · high · 2026-10-22

# Review: ui-ux-designer books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/ui-ux-designer.md (body) + .agents/skills/ui-design/ (SKILL.md, references/ incl. worked-examples.md) + .agents/skills/ui-figma/ (SKILL.md, references/) + .agents/skills/ui-style-cartoon|anime|pixel|stud/SKILL.md, working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer ui-ux-designer (opus, high)
looked_at_first: [
  the rev1 and rev2 reviews (F1-F3, R1-R12), to know what to re-check,
  role file and ui-design SKILL.md, review.md, screen-contract.md, motion.md, shops-rewards-onboarding.md, style-choice.md, worked-examples.md, ui-figma SKILL.md, all read in full as they are now; git diff df13ff4 of the four style books and the four ui-figma references; removed role-file lines walked,
  tools/vfx/clip_metrics.py source; my own V3 runs in the reviewer scratchpad r3/: eight 30 fps press folders (300 x 160 crops over a static noisy sky; press frame 400 ms): A small sink then a bigger outcome change, B cue on the press frame, C changed majority, D cloud drifting through the margin, E press under 40 levels, F cue 267 ms late, G cue after the last frame, H sink then 'Buying...'; the lag line (review.md:79), the hit-target line (:82) and the reveal line (:81) extracted from the book file with sed and run as written,
  the Figma export_video tool schema (MP4 behind a presigned URL, fps 5-60); `which ffmpeg` on this machine (not found); cv2 5.0.0 present,
  partner books for V10: vfx-craft/references/measure.md §1 ('no kit tool records a frame folder yet'), vfx-design read-card.md and moment-recipes.md (world-to-HUD, low-health pulse), sound-design SKILL.md S-133 and craft-process.md §2 (UI cue list), art-review/references/art-bible.md §7 rows, marketing-craft/references/channel-kits.md:29 (cv2 frame command),
  roblox-creator-docs: ui/styling/editor.md:321-333 (@ViewportDisplaySizeSmall built-in query), production/publishing/accessibility.md:100-130 and :180-190,
  universal-principles.md UI lines of UP-01..UP-20; matrix.md ui-ux column (script compare),
  ui-design/evals/briefs.md brief 3 (anime summon) for C7
  ]   # the maker's coverage and proposals files were read after this
previous_findings:
  - {id: F3, status: fixed,
     note: "review.md:79 lag line + :92 note + S-33 (:148) + §7 (:170) + worked example step 10 + figma-mcp §6 + motion §5 all agree. My verbatim runs: A cue 433 lag 33 with pre-press max 0 (summary.onset_ms not used); B lag 0; H lag 33; F lag 267 = FAIL; C pre-press max 11.1 (flagged by the 'must be 0' rule); D pre-press max 1.45 (flagged); E and G cue None = UNVERIFIED. No wrong number reaches a PASS"}
  - {id: R9, status: fixed, note: "review.md:94 kind comes from the flow sheet's How often column, close/back/tabs/HUD are frequent, minor needs a written reason; screen-contract.md:84; worked example close 150 x 150 frequent"}
  - {id: R10, status: fixed, note: "'phone layout frame' (1920 x 1080 canvas, the @ViewportDisplaySizeSmall arrangement, never a resampled copy) in ui-design SKILL.md:31, ui-figma SKILL.md:23 and :77, review.md:112, ui-style-stud:99; 'phone-fit view' stays the 565 x 318 resample (screen-contract.md:51). The built-in query name exists (editor.md:333)"}
  - {id: R11, status: fixed, note: "S-33 '<= 67 ms at 30 fps (the press frame or the next, plus one frame of capture jitter; PROPOSAL)'; release check 24 points to S-33"}
  - {id: R12, status: fixed, note: "S-44 (:159), its note (:93), §7 (:170), shops §5 (:54), ui-style-anime §10, worked example (common vs rare and vs legendary). My run: a 10 px tell on a middle tier gives 149-158 changed pixels against a floor of 0"}
findings:
  - {id: R13, class: recommendation, check: C3 / C8 V2-V3 / V10 (frame-folder routes),
     where: ".agents/skills/ui-figma/references/figma-mcp.md:86 ('extract frames with ffmpeg, named f###_<ms>ms.jpg'); .agents/skills/ui-design/references/motion.md:39 ('from the studio-operator's Studio capture rig through the lead'); review.md:92 (pre-press remedies) and §7 :170",
     expected: "Every route the S-33 / S-40 / S-43 / S-44 checks need can be run with our tools as written, and the book says what happens when a route does not exist yet (as the rebuilt vfx-craft/references/measure.md §1 does)",
     observed: "(1) The only route the designer can run before a build is the Figma prototype: export_video returns an MP4 behind a presigned URL, then 'ffmpeg' splits it. ffmpeg is not installed on this machine (`which ffmpeg`: not found), and ffmpeg's numbered output cannot name frames by ms anyway, so the agent must improvise the split and the renaming. A tested command already exists in the kit: marketing-craft/references/channel-kits.md:29 (cv2, which is installed; it writes f####_<ms>ms.jpg, which clip_metrics.py reads). (2) motion.md:39 names a Studio 'capture rig' as if it exists. vfx-craft measure.md §1 says no kit tool records a frame folder yet, and this maker's own studio-mcp proposal row says nobody has probed it. The UI books never say that without a folder the build's S-33/S-40/S-43/S-44 go on the could-not-check list, so the agent may wait for a capture nobody can make. (3) A PC capture where the cursor moves onto the button before the click shows the hover look (AutoButtonColor) before the press. The pre-press maximum rises above 0, and neither listed remedy (more idle frames, crop inside the face) removes it. Not a wrong number: the rule flags it. But the agent has no fix",
     evidence: "`which ffmpeg` → not found; `python -c 'import cv2'` → 5.0.0; export_video schema (MP4, presigned URL, fps 5-60); vfx-craft/references/measure.md:18; proposals/ui-ux-designer.md studio-mcp row; my run D shows how a pre-press change is flagged",
     smallest_fix: "figma-mcp.md §6: 'download the MP4 (export at fps 30) and split it with the frame command in marketing-craft/references/channel-kits.md §3 (it names frames f####_<ms>ms.jpg)' in place of ffmpeg. motion.md §5 and review.md §7: 'No kit tool records a Studio frame folder yet; ask the lead for the route; without a folder these lines are not verified and go on the could-not-check list.' review.md:92: add 'a hover look before the press (PC capture): start the capture with the cursor already resting on the control, or capture with touch emulation'"}
  - {id: R14, class: recommendation, check: C1 (check precision of two rows),
     where: "coverage rows LC-05 (S-19) and WL-28 (S-23 'every round'); review.md:130 (S-19), :134 (S-23)",
     expected: "The library check is carried. LC-05: no palette cluster far from every role swatch. WL-28: the small-size view is measured each round",
     observed: "S-19 checks that each role swatch is found and that nothing sits near the danger hue. It does not flag a stray colour far from every role, so a new hue not taken from the palette passes. S-23 does not say 'every round' (only F-21, a technique row, says 'look again'). The coverage cell claims more than the S-line holds. The rules are carried (style-choice §6, F-21); only the checks are weaker",
     evidence: "light-colour.md:81 (LC-05 check); world-level-readability.md:384 (WL-28 check); review.md:130, :134",
     smallest_fix: "S-19: add 'no cluster with share >= 5 % sits beyond the tolerance from every role swatch (a new colour is taken from the palette)'. S-23: add 'run at each style round, not only at hand-back'"}
  - {id: R15, class: recommendation, check: C8 V10 (one unit for the sync limit),
     where: ".agents/skills/ui-design/references/motion.md:36 ('never more than one frame before it'); role file partners row sound-designer",
     expected: "The same early limit as the sound designer's S-133: one frame at 60 fps = 16.7 ms",
     observed: "The UI line says 'one frame' with no rate. At the 30 fps the UI captures use, that reads as 33 ms early, twice the sound book's limit. The marketing reviewer met the same trap and fixed it in ms",
     evidence: "sound-design/SKILL.md:107; coverage/marketing.md table g (window in ms, not one 30 fps frame)",
     smallest_fix: "motion.md:36 and the role-file row: 'never more than about 17 ms (one 60 fps frame) before it'"}
keep: [
  every fix of rounds 1 and 2: S-49 with its runnable hit-target line and the frequent/minor rule; the S-33 lag line, which reads the per-frame coverage against the pre-press maximum and never trusts summary.onset_ms; the boxed reveal difference with a changed-pixel count, a noise floor and a per-tier comparison,
  the stage order flow → structure study → 2-3 wireframes (one atypical) → grey value pass → rule sheet → target images → Figma → motion, both gates, and the scale-down line for changes inside an approved screen,
  review.md §6 staged S-lines, each naming its input, plus the command block and the honest 'wrong without an error' notes,
  the rule sheet naming the art bible §7 rows (checked: the rows exist in art-review/references/art-bible.md:69-76), one motion table per game seeded from ui-basics §A, attempt cue vs confirmed outcome with pending after about 100 ms,
  the partners table and the review slot with return paths (a read-order failure goes back to the grey pass),
  §7 core principles: 20 rows, each with its own example and S-id check, no contradiction with the master,
  the two worked examples (now consistent with every changed check), the proposals file (recipe and workflow rows with reasons; tool rows that would retire the three one-liners)
  ]
verdict: pass
</spec>
```

## Check results

| Check | Result | Notes |
| --- | --- | --- |
| C1 coverage | pass (144 rows checked, 0 failed; 2 weak, R14) | Script compare with matrix.md (`ui-ux` column): 144 tagged IDs = 144 rows, none missing, no duplicates; the 15 extra rows are the declared untagged findings. Every S-id cited exists in review.md §6. I opened the landed-in content of UI-01..UI-19, the S-33 / S-44 / S-49 rows (UI-03, UI-12, GD-02, WT-01, GD-35) and about 25 others (LC, RI, VH, EX, SI, MD, PP, WL, VR-26). Rejections CR-10, PI-10, RH-05, SS-08, VR-04 and the CR-16 proposal-only row have sound reasons (VR-04: additive wash-out does not arise with Roblox's Normal-blend UI) |
| C2 core principles | pass | ui-design SKILL.md §7 (the skill loaded first): UP-01..UP-20 stated for UI, each with its own example and check; row 12 keeps the master's limit (UP-07 wins); rows 8, 19, 20 match the master's UI lines (S-33's 67 ms sits inside the master's 100 ms); §1 says to re-read §7 after a compaction |
| C3 self-review | pass (one route weak, R13) | Every checkable UI finding has an S-line with a named input (Figma metadata and screenshots, look_check modes, clip_metrics + lag line, hit-target and reveal one-liners, studio-operator captures, the owner at a playable preview). The prototype frame-split step names ffmpeg, which is not installed here (R13) |
| C4 kit rules and engine | pass | No change to rules/, tools/, templates/, workflows, orchestration, ui-basics, platform-policy, evals, tools line, model or effort (git status clean). Engine claims re-checked: @ViewportDisplaySizeSmall (styling/editor.md:333), PreferredTransparency 1 = default / 0 = opaque, multiplied into BackgroundTransparency (accessibility.md:104-110), reduced motion tween time 0 (:184-188). Recipe and workflow changes are proposals only |
| C5 nothing valuable lost | pass | Removed role-file lines walked again: the old steps are carried by SKILL §3 (focus map step 10, size math step 5 + S-49, side-by-side S-25, device set review §5). The J016 riot-extracts pointer is replaced by the books themselves. Style-book and ui-figma reference edits only add to old lines; the target count went from 2-4 to 2-3, inside the brief's image budget |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4; SKILL.md lines 118/85/110/107/102/103; descriptions 372-383 characters, unchanged; the J018 phrase in all 16 changed or new skill files and in the role comment; sections appended, none renumbered; no library IDs or Riot names added to bodies (VALORANT, Hearthstone, the ready-check video are pre-existing J002 evidence); no tips section; evals/ unchanged; LF endings |
| C8 brief v2 | pass (recommendations R13, R15) | V1: inputs per S-group, image budget review.md §5. V2: every kit tool mode named is real; the external ffmpeg is the weak route (R13). V3: lag, hit-target and reveal lines run verbatim from the file and give the right answer on 8 + 2 + 2 samples; the wrong-without-error cases are written down, and each is caught by the pre-press rule or reads as UNVERIFIED. V4: paid-random, purchase and ads lines point to platform-policy §A-§D. V6: one place per rule (the rule sheet names bible rows; motion numbers in motion §7-§8 and ui-basics §A). V7: ui-design §6 ends at 17.5 KB; ui-figma §6 at 18.6-19.9 KB with the compaction note. V8: partners table, review slot, rule sheet and motion table as sheets. V10: world-to-HUD split, attempt/outcome, low-health 1 Hz and art-bible rows agree with the rebuilt partner books; the sync unit differs (R15). V11: game-designer, art-director, progression and sound rows adopted with reasons; no new rows from later waves (grep of every proposals file) |
| C7 better work | better | See below |

## Judgment (C7)

I read the books as the agent would at the start of eval brief 3: an anime summon screen paid with gems bought with Robux, "make it hype". The old books would give a styled banner and a reveal with a "same anticipation for every rarity" note. The agent could not check that note, and it had no flow or read-order proof.

With the new books the agent:
- loads platform-policy §A first and puts the odds behind a worded label before the buy button. A pity count inside a ×10 is stated at review, and restricted players get an alternative screen, not a dead button.
- counts the taps, proves in grey that the summon button and the hero rank first, then styles from an approved target image with glow on those two only (S-17).
- measures the windup of every tier against the lowest tier, frame by frame inside the reveal box, so a tint on a single Epic tier is caught. The 10x summon ends on a sorted summary, and only the best result gets the full ceremony.
- specifies a press answer within two frames, a pending state and no success before the server confirms.

All of that is checkable, and the round-3 fixes closed every remaining wrong-verdict case I could build.

Weak spots that remain, all recommendations:
- The prototype frame-split route names a program that is not installed, and the books do not say that no Studio frame recorder exists yet (R13).
- Two coverage cells claim slightly more than their S-lines check (R14).
- The sync limit is given in frames with no rate (R15).
- The books are about twice as long as the old ones. The staged S-lines and the scale-down line justify most of that length.

No blocking problem remains. This role is ready for G3.
