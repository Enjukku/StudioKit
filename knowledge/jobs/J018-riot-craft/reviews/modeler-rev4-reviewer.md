---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer modeler · claude-opus-5-5 · high · 2026-10-22

# J018 stage 3 review: modeler books, round 4 (focused: rev3 F1-F3 and every measuring command)

Scope: `.agents/roles/modeler.md`, `.agents/skills/modeling-design/**`, `.agents/skills/modeling-craft/**`, working tree on 2026-10-22 after repair round 3, against `reviews/modeler-rev3-reviewer.md`. I read the books first and the `coverage/modeler.md` §f note after them. I ran every command line in `modeling-craft/references/read-commands.md` verbatim: I took the lines from the file by script, ran them in Git Bash, and ran §2-§4 again in Windows PowerShell 5.1. I also ran each `look_check.py` call in craft SKILL §7, blender-recipes §6 and handoffs §4 on synthetic inputs in the reviewer's scratchpad. Nothing in the repo was run against or changed except this file.

```text
<spec>
artifact: .agents/roles/modeler.md + .agents/skills/modeling-design/** + .agents/skills/modeling-craft/** @ working tree 2026-10-22 (repair round 3)
reviewer: J018 reviewer modeler (opus, high), round 4
looked_at_first: [rev3 F1-F3 and smallest fixes; read-commands.md in full; craft SKILL in full (§7 every row); design SKILL P2, P3, P6; review.md §1, §5 (SL, VL, CL, DT, IM); export-import §3; blender-recipes §6; handoffs §4; grep of every thumb, crop, HSV, saturation, detail-density, phone-size mention in the 15 files; look_check.py --help (all modes), run_thumb and fit_size, out_path naming, DEFAULT_KEY_TOL 40; review_renders.py camera code (game view PERSP, sensor_fit VERTICAL; dummy only in the scale view); synthetic inputs, all with role-prefixed names (modeler_rev4-*): a 1024 flat sRGB 128 render (skin head, red torso 210,90,90, bright accent, light and dark shoulder studs, near-black brown legs 25,14,8; supersampled and box-filtered, so edges are anti-aliased with no ringing), a 1600x720 game frame with the same model 190 px tall, captures at 1000x700 and 1920x700 with a sky gradient, noisy ground, a tinted near-black shadow, a dark rock, and magenta mask captures, an even-stripe model, a two-leg frame with a 4 px gap, a noisy white-background reference, two magenta icons touching the frame edge]
findings:
  - id: F1
    class: recommendation
    where: "modeling-craft/references/read-commands.md:22 (§3 command), :24 (Input bullet); modeling-craft/SKILL.md:99-100 (Detail density row 'or capture'; Studio capture row makes a width-cropped mask capture)"
    expected: "A detail-density run on a mismatched pair (a capture and a mask of a different size) stops with an error, as every other measuring line does."
    observed: "On a wide capture the agent holds two masks: the full-width one from the Mask capture row and the width-cropped one from §4. The §3 line takes the model's box from the mask and crops the image with it, then resizes both to the same (w, h). Thus an uncropped capture with the cropped mask crops a background area beside the model and gives no error. The printed phone size is right (it comes from the mask), so the read-plan size check does not catch it. The result is 'busy share 0.0', which DT10 reads as even density: a false fail."
    evidence: "1920x700 capture + its §4-cropped 1556x700 mask: 'model at phone size 19 x 52 px; cells 23 busy share 0.0 busy rows []'. The same capture cropped by §4 with that mask: 'busy share 0.39 busy rows [24, 34, 53]'. The same mismatch in §2: numpy IndexError. In look_check.py value --mask: 'ValueError: mask size (1556, 700) differs from image size (1920, 700)'."
    smallest_fix: "In the §3 line, after k is opened, add `assert g.size==k.size,'image and mask differ in size'`. Or, in the Input bullet, write 'same size as the image: both uncropped, or both cropped by §4'."
  - id: F2
    class: recommendation
    where: "modeling-design/references/review.md:115 (VL4) vs modeling-craft/references/read-commands.md:18 (§2 tie rule, refined in round 3)"
    expected: "VL4 describes what the §2 line marks when ties exist."
    observed: "VL4 says that when ties mark more than 10 %, the line marks 'only the brightest grey level'. The round-3 line instead marks every pixel above the tied level, which is often several levels. In the test, both the light studs and the accent were marked. An agent that reads VL4 expects one level, so it takes the second marked group to be an error of the tool or a failure."
    evidence: "Flat render, L: 'p95 share 0.461 marked share 0.026'; marked rows 313-448 hold the studs (250,200,200) and the accent (245,225,120), two grey levels above the tied torso level."
    smallest_fix: "VL4: '... where ties mark more than 10 %, only the pixels above the tied level (`modeling-craft/references/read-commands.md` §2): record both shares'."
keep: [rev3 F1 fix: the §3 line crops to the black-fill box, box-averages by phone height ÷ frame height, counts edges only 2 px or more inside the outline, pads 2 px against PIL's border copy, writes <name>.detail.png and prints phone size, busy share and busy rows. Run results: 34x95 phone model on the 1600x720 frame with busy rows 14, 24, 33, 52 (head-torso line and studs, studs, accent, waist); even stripes give busy share 0.0; 19x52 on both the 1000x700 and the uncropped 1920x700 capture, which is correct for a vertical FOV; a close 1024 render prints 102x281, so the read-plan size check catches the wrong input. rev3 F2 fix: chroma channel; flat render S marks the accent only (2,400 px, rows 400-448, no leg pixel); game frame and both captures with tinted near-black shadow and dark rock mark the accent only (48 px). rev3 F3 fix: §4 crops only a capture wider than the phone and only in width; 1000x700 'not cropped', thumb scale 0.514 = 360/700, model 52 px; 1920x700 cropped to 1556x700, scale 0.5141, model 52 px; the scale check works; the model-size option is gone from the Phone size row and IM1. --key-tol 4 rule: default 40 drops the skin head (bbox top 304 vs 160), 4 keeps it. --compare-mask IoU 0.999 vs a noisy white-background reference. Icons: --key FF00FF measured (scale 0.293), auto key invalid-mask, family compare IoU 0.91. Region mask §1 (upper p50 0.218, lower 0.0054), contrast --sample 4.83, palette --roles, mirror: all run as written. All lines run unchanged in PowerShell 5.1.]
verdict: pass
</spec>
```

## Round-3 findings: status

| Id | Status | Where fixed (every place it appeared) | Run result |
| --- | --- | --- | --- |
| rev3 F1 detail density: writes no image; 0 cells on a game frame | fixed | read-commands §3 (line, input, output, read, PROPOSAL values); craft SKILL §7 Detail density row; review DT10; design SKILL P6 | `.detail.png` written in all 5 runs; right phone size and busy rows on the game frame and the captures; even stripes give 0 (fails as it should); a close render shows its wrong size in the print. A mismatched image-mask pair gives a silent wrong answer (F1 above, recommendation) |
| rev3 F2 HSV saturation marks near-black | fixed | read-commands §2 (chroma, 2 px mask shrink, thin-part note); craft §7 Top 5 % row; review CL7 (CL4 now says why it keeps HSV-style saturation); design SKILL P3 | Flat render, game frame and both captures: the S image marks the accent only, with no leg, shadow or rock pixel. VL4's tie wording is behind the refined rule (F2 above, recommendation) |
| rev3 F3 crop enlarges the model; the model-size option shrinks the frame | fixed | read-commands §4; craft §7 Phone size and Studio capture rows; review IM1 | 1000x700 not cropped, scale 0.514; 1920x700 cropped in width, scale 0.5141; both give 52 px (true value 52). 1600x720 frame: 0.5 (95-96 px vs true 95) |
| rev3 F4 (rec.) self-review misses P4, P10, P14, P16 and 5 conditional items | open, outside this round's brief (coverage §f) | — | — |
| rev3 F5 (rec.) Tripo route order stated two ways | open, outside this round's brief | — | — |
| rev3 F6 (rec.) proposals intro | fixed | `proposals/modeler.md:13` 'Rows 1-4' | — |

## Commands run (check 2)

| Line | Inputs | Runs | Files written | Right answer | Wrong number with no error when |
| --- | --- | --- | --- | --- | --- |
| RCM §1 region mask + `value --mask` | flat render black-fill, waist at y 600 | yes | `upper.mask.png`, `lower.mask.png`, luminance per region | yes: lower p50 0.0054 vs upper 0.218 | box edges taken by eye (the book forbids this) |
| RCM §2 L / S | luminance image or colour render + black-fill or capture mask | yes (Bash and PowerShell) | `.top5.png`, `.sat5.png` | yes (see keep) | none found: a size mismatch raises an error; thin parts under about 5 px drop out (the book says so and sends the agent to a close view) |
| RCM §3 detail density | game frame, capture with mask, close render, stripes | yes | `.detail.png` | yes | image and mask of different sizes (F1) |
| RCM §4 crop | 1000x700, 1920x700 capture and mask capture | yes | cropped pair; printed 'cropped' / 'not cropped' | yes | none: the thumb `scale` check catches an uncropped wide frame |
| RCM §5 mirror | flat render | yes | `.mirror.png` | yes | — |
| craft §7 silhouette, value, thumb, palette with `--key-tol 4`; `--compare --compare-mask`; contrast `--sample` | flat render, game frame, reference | yes | `.silhouette.png`, `.luminance.png`, `.thumb800x360*.png` | yes | `--key-tol 4` + LANCZOS thumb makes the phone fill about 1 px fuller (a 2 px leg gap became 1 px; area +2 %). This is too small to change SL1-SL3, so it is not a finding |
| handoffs §4 icon `thumb` / `silhouette --compare` with `--key FF00FF` | two magenta icons cut by the frame edge | yes | thumb and sheet | yes; without `--key` it is invalid-mask, as the book says | — |
| Studio lines (`execute_luau` FOV, `screen_capture`, Neon mask capture, `WorldToViewportPoint`, in-hand Tool) | — | not run (no Studio in this review) | — | not verified; the books keep them probe-first | — |

## Fixed list (check 3)

Pass. Files changed since the round-3 review: the modeler books (craft SKILL, blender-recipes, handoffs, read-commands; design SKILL, review) and the role's two job files (`coverage/modeler.md`, `proposals/modeler.md`). The other changed paths (`crew.md`, `stage2-brief-v2.md`, `tool-modes.md`, `reference/craft/riot/game-design-fun.md`) are not modeler books and are not claimed in the §f note. The role frontmatter is byte-identical to df13ff4. The skill descriptions are unchanged since round 3 (394 and 391 characters, the same as in round 3). Design SKILL has 120 lines and craft SKILL has 101. No section number changed: the only heading changes since df13ff4 are the ones round 3 recorded, plus the read-commands headings, which were already present and are unchanged. The bodies contain no library ID, no Riot game, champion or artist name and no transcript line ('Riot' appears only in the required header phrase, once per file).

## Will an agent make better work with these books?

Yes. The three measurements that could send an agent the wrong way now give the right answer on the inputs the books name:
- Detail density shows where the busy cells sit at the model's real phone size.
- The colour peak follows the focal colour, not dark boots or shadows.
- The phone-size view of a Studio capture has the phone's true scale.

Each line prints a number the agent can check against the read plan: the phone size, both tie shares, or `scale`. The two findings above are one-line clean-ups. Rev3 F4 (the "reads as one game with the anchors" check is not in the hand-off list) and F5 (the two Tripo orders) remain the most useful open improvements.
