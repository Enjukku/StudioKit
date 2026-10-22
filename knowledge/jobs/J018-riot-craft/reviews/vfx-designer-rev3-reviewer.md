---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer vfx-designer · claude-opus-5-5 · high · 2026-10-22

# Review: vfx-designer books, rebuild round 3 (J018 stage 3, after repair round 2)

```text
<spec>
artifact: .agents/roles/vfx-designer.md (body) + .agents/skills/vfx-design/ (SKILL.md, references/) + .agents/skills/vfx-craft/ (SKILL.md, references/); working tree on top of df13ff4 after repair round 2, 2026-10-22
reviewer: J018 reviewer vfx-designer (opus, high)
looked_at_first: [
  role file read in full (frontmatter lines 1-10 byte-identical to df13ff4: same md5, same bytes); vfx-design SKILL.md, read-card.md, review.md (§A-§I) read in full; vfx-craft SKILL.md and measure.md read in full; file times: only measure.md, vfx-design SKILL.md, read-card.md and review.md changed after the rev2 review, the other references are as rev1 and rev2 walked them (flipbooks-and-kitbash, roblox-vfx, juice-repetition-sync: status-only, no content diff),
  knowledge/reference/craft/riot/universal-principles.md (UP-03, UP-09, UP-20 effect lines and general checks), matrix.md vfx column (214 IDs, script-extracted),
  partner books: film-craft/references/blender-previs.md §7 flash count (:77-100), animation-design/references/game-timing.md:36, :42 (event names),
  tools: tools/vfx/clip_metrics.py source; look_check.py value, silhouette (--keep-holes, --compare/--compare-mask), thumb, contrast (--min-ratio, --tolerance-source) run; docs mirror ParticleEmitter.yaml:962-968 (TimeScale 0 "freezes"),
  earlier reviews rev1 and rev2 (every finding re-checked), stage2-brief-v2.md, job-card.md fixed list and decisions, vfx-design/evals/briefs.md briefs 2 and 3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
v3_runs (scratchpad rev3/: my own synthetic 1280x720 JPEG folders, sky gradient + noisy ground + a character block, frames f###_<ms>ms.jpg; the §6 script extracted byte-for-byte from measure.md:88-119):
  - A three 1-frame full-screen flashes in 1 s: 3 and 3 (right). B two eased full-screen pulses 500 ms apart: 2 and 2 at 30 fps and at 60 fps (right). C a 5 % flash inside one block 3/s: 0 at 10 %, 3 at 3 % (right). D the same flash on a block corner: 0 and 3 (right). J 40 small sparks totalling about 4 % 3/s: 0 and 3 (right). H three 4 % orange flashes during a slowly brightening sky: 3 at 3 % (right; the sky counts once at 10 %, conservative). Q a pan over light and dark stripes: 0 and 0 (right). G a 4 % red zone at 2 Hz, box reading: 2.0 Hz (right)
  - P a lasting dim grade (whole screen x0.6 from frame 10, a bright stage) and three 8 % white flashes in 1 s: 0 and 0, no error (truth: 3 at 3 %). L the same dim with three 15 % flashes: 0 at 10 % (truth 3), 3 at 3 % only through the centre block. K three 3.5 % flashes over a dark smoke cloud that rolled in over a bright sky: 0 and 0 (truth 3). N a 20 % smoke cloud elsewhere, three 5 % flashes: 3 at 3 % (the blocks rescue it). The cause and the one-token fix: F1
  - BL-04 width one-liner (measure.md:39) on clip_metrics output of a ring folder: the C-21 ring (0.38 -> 0.72 at t 0.25) PASS (1200 vs 1217 ms), `linear grow` FAIL (1467), `ease-out grow` PASS (1167): right
  - mask one-liner, cover one-liner (a ring around the character 0 px; a box over the ring 2941 px), look_check value / silhouette --keep-holes / thumb --size / contrast --min-ratio 3 --tolerance-source / silhouette --compare --compare-mask (iou, area_frac keys present), curve one-liner on content/vfx/curves.json: all run and write the files measure.md names
findings:
  - {id: F1, class: blocking, check: C8 V3 + C3 (IG-07, the flash-safety count gives 0 with no error in a common busiest scene),
     where: ".agents/skills/vfx-craft/references/measure.md:107 (`elif not r[4] and -net >= r[1]: lo, hi, r[4] = x, x, True`), :121 (the Flash bullet's 'wrong with no error' list); .agents/skills/vfx-design/references/review.md:288 (IG-07)",
     expected: "The composite flash count sees every flash over its area in the busiest scene, or the book names, next to the command, each case where it gives a low number with no error (C8 V3: 'ask what makes it give a wrong number with no error')",
     observed: "While a region is armed (waiting for a flash), its baseline (lo, hi) is reset only by a flash. A net fall does not reset it, because the re-arm branch runs only when the region is not armed. So any area that darkened by 0.1 or more since the folder start and stays dark (a dim grade during a boss phase or an egg windup, dark smoke over a bright sky, a shadow that falls) is counted as a 'falling share' in every later frame, and it cancels every later flash smaller than itself in that region. The listed traps (two overlapping flashes; a pulsing layer) do not cover this one",
     evidence: "my runs: P (lasting dim + three 8 % flashes in 1 s) 0 and 0; K (three 3.5 % flashes over smoke that rolled in) 0 and 0; L (lasting dim + three 15 % flashes) 0 at 10 %. With the one-token change below: P 3 at 3 %, L 3 and 3, K 2 (the flash on the same frame as the smoke's arrival is still cancelled); A, B30, B60, C, D, F, H, J, M, N, Q, G give the same counts as before (B: 2 and 2 at 30 and 60 fps; pan Q: 0). The film director's script (film-craft/references/blender-previs.md:95) has the same line, so both books under-count in the same way",
     smallest_fix: "measure.md:107: `elif -net >= r[1]: lo, hi, r[4] = x, x, True` (a net fall re-arms and resets the baseline, armed or not). Add to the :121 'wrong with no error' list: 'a flash on the same frame as a larger darkening in its region (smoke arriving, a grade dimming) is cancelled'. Re-run table d with a lasting-dim and a smoke-over-sky sample and record them. Add a proposals row for film-craft/references/blender-previs.md §7 line 95 (the same change) so the two books keep the same count (measure.md:86 says they do)"}
  - {id: R1, class: recommendation, check: C2 / C7 (one cap, two wordings),
     where: ".agents/skills/vfx-design/references/review.md:288 (IG-07 'at most 2 per rolling second by design, never 3'); .agents/skills/vfx-craft/references/measure.md:121 ('at most 2 in any 1 s by design, never 3')",
     expected: "The hard cap reads the same in every place: master UP-20 'at most 3 per second (design target 2)'; vfx-design/SKILL.md:64 'design ≤2 ..., never >3'; §9 #20 'flashes ≤3 per second (design 2)'; RV-T06 hard cap 3/s",
     observed: "IG-07 and measure.md §6 make 3 the hard fail; the SKILL, §9 and RV-T06 make 3 the hard cap (allowed, design fail). The pass mark (≤ 2) is the same, so the verdict does not change, but a reviewer reading a count of 3 gets two labels (design miss or release block)",
     evidence: "universal-principles.md:402, :410; vfx-design/SKILL.md:64, :136; review.md:80",
     smallest_fix: "IG-07 and measure.md:121: 'at most 2 by design, never more than 3'"}
rev2_findings_rechecked: [
  F1 (flash count over-counts eased flashes, disagrees with the film count, misses 3-10 % flashes): fixed. The trough and peak test with nine blocks is the film director's (same thresholds, same rule); eased flashes count once at 30 and 60 fps; a 3 % count catches 3-10 % flashes (my runs B, C, D, J). One new trap found in the shared algorithm (F1 above),
  F2 (BL-04 reads area): fixed. BL-04 and measure.md read the box width; the C-21 ring passes, linear fails (my run); the smoke trap, upward shapes and a start ms on a flash are written next to the one-liner,
  R1 (§9 #9 cited CP-15): fixed (BL-12), R2 (busiest folder for pulse rates): fixed (measure.md:11, IG-08), R3 (readings the tool lacks): fixed (VS-02, BL-06), R4 (`windup_start`): fixed (`tell_start`, read-card.md:40, matches game-timing.md:36), R5 (stale records): fixed (S-133 row marked done; line count 136; V11 line numbers)
  ]
keep: [
  every rev1 and rev2 finding fixed and verified by my own runs,
  the read card with its loudness tiers, sources per field and two worked cards; the short route for T1-T2 effects and fixes,
  the build order: blocking with placeholder sprites -> check-in -> grey and black-fill gates -> colour -> polish -> in-game, decisions frozen after the check-in,
  review.md §I: self-review lines per pass with their input codes, the image budget under J005-D8, the fresh-read protocol,
  measure.md: every command runs as written on its real input type, with an honest 'wrong with no error' list next to each; the BL-04 width reading; the shape vs footprint split; the cover test on masks; today's capture route,
  craft rows C-17 to C-31 and the spec lines SP-01 to SP-13,
  the partner table in the role file (what to ask whom, and when); all seven partner proposal rows answered in the V11 block,
  §9 core principles: all 20, each with its own example and a runnable check that names the right line
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass (214 rows checked, 0 failed) | 214 / 214 tagged IDs have a row; the 13 extra rows are untagged findings the maker used. By script, all 114 line ids and 12 reference files the rows cite exist in the books. I read again the rows that repair round 2 touched (UP-09, IG-07 and IG-08 flash and pulse rows, BL-04 fast in, CD-04 variants, V11 rows), and their content carries the rule and the check. The rejections are sound (as in rev1 and rev2) |
| C2 core principles | pass | §9 covers UP-01 to UP-20, each with its own example and check. The #9 check now names BL-12. No contradiction with the master: the UP-03 white exception is a filed proposal, and UP-20 has a wording difference only (R1) |
| C3 self-review | fail (F1) | every checkable finding has a line with its input. The IG-07 count gives 0 with no error after a lasting darkening (F1) |
| C4 kit rules and engine | pass | TimeScale 0 "freezes" (ParticleEmitter.yaml:967), Model:ScaleTo, Highlight 255 and Rate 400/100 agree with the docs mirror. Every tool mode is real (I ran them). Nothing conflicts with AGENTS.md, rules/ or J018-D2 to D4. The fix stays in a book script, not in tools/ |
| C5 nothing valuable lost | pass | only four files changed after rev2. Each edit keeps or sharpens what it replaces (the old onset loop was shown wrong in rev2, and the area reading of BL-04 was shown wrong in rev2) |
| C6 fixed rules | pass | only the vfx books and the two job files changed for this role. Frontmatter is byte-identical. SKILL.md has 136 and 113 lines. Descriptions are 377 and 353 characters. No section is renumbered. The J018 phrase is in every changed header and in the role comment. The bodies have no Riot, games, champions or library IDs (the CD-01 to CD-17 ids in effect-card-and-presets.md are the old book's own card ids). There is no tips section, and evals/ is unchanged |
| C7 better work | yes, with one silent safety miss | see below |
| C8 brief v2 | fail on V3 (F1) | V1: inputs and image budgets are named. V2: only real modes. V3: every command runs, and the flash count has the untold trap in F1. V4: the paid-random lines agree with platform-policy. V6: one place per rule. V7: the steps, rules and self-checks are in the first part of each SKILL.md. V8: n/a. V10: the event names, the sync window and the freeze frame agree with the animator and sound books. The flash test agrees with the film book, which has the same flaw (F1 fix keeps them equal). V11: all partner rows are answered |

**C7 judgement (eval briefs 2 and 3, read as the agent would).** For the magnet coin pickup (brief 2), the old books gave a layer plan and one capture. The new books take the short route. The agent fills a read card like the worked coin card: tier T2, merge window 100 ms, at most 8 live copies, the world-to-HUD split with UI on one beat list, and the refused pickup. It blocks the pickup, checks it, and runs the 100-trigger and burst repeat (IG-09) with the builder's rate hook, which it asks for at the wiring step.

For the paid legendary egg reveal (brief 3), the read card, the identical-windup row check (IG-14), and the honest-reveal lines (with disclosure handed to platform-policy) prevent a near-miss or a rarity hint before the result. The grey and black-fill gates name the tier without colour. The agent will make clearly better and more honest work than with df13ff4.

One weak spot is left, and it is in brief 3's own moment. A reveal that dims the world during the windup and then fires its bursts is the case where the flash count reads 0 with no error (F1, run P), so a strobing reveal could pass the safety line. The fix is one token in the script plus one trap line. No other part needs a rebuild.
