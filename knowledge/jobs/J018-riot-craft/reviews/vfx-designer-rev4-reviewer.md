---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer vfx-designer · claude-opus-5-5 · high · 2026-10-22

# Review: vfx-designer books, round 4 (J018 stage 3, after repair round 3; focused on the flash counter)

```text
<spec>
artifact: .agents/roles/vfx-designer.md (body) + .agents/skills/vfx-design/ (SKILL.md, references/) + .agents/skills/vfx-craft/ (SKILL.md, references/); working tree on top of df13ff4 after repair round 3, 2026-10-22 07:10
reviewer: J018 reviewer vfx-designer (opus, high), round 4
looked_at_first: [
  reviews/vfx-designer-rev3-reviewer.md and reviews/film-director-rev3-reviewer.md (both F1 cases),
  vfx-craft/references/measure.md read in full (§6 script :88-132, Flash bullet :133, Pulse bullet :134); vfx-design/references/review.md IG-07 :288, IG-08 :289, RV-T06 :80; vfx-design/SKILL.md :64, :136,
  file times: after the rev3 review only measure.md and review.md changed in the books (role file, both SKILL.md and the other references are older; evals/ dated 2026-10-20),
  partner pointers (read only): film-craft/references/review.md:128 R-10 and marketing-craft/references/channel-kits.md:32 now send their flash count to measure.md §6 and read "the over-10 % count"; film-craft/references/blender-previs.md §7 still holds its own copy (the film round is in progress; proposals row 19 covers it),
  my own runs (scratchpad rev4/): the §6 script extracted from measure.md by script (flash_pulse_vfx.py, 43 lines); the rev3 reviewer's folders (rev3/A-Q, G); the film reviewer's 48 folders (fdrev3/*, PNG at 24, 30, 60 fps); my generators gen4.py, gen4b.py, gen4c.py, gen4d.py (640x360 JPEG f###_<ms>ms.jpg, textured sky and ground, 24/30/60 fps); old_loop.py = the same script with the round-2 loop, to see what round 3 changed
  ]   # the maker's coverage note "Repair round 3" and proposals file were read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3 + C3 (IG-07, the flash count gives a low number with no error in a common scene)",
     where: ".agents/skills/vfx-craft/references/measure.md:116 (net = rising share minus falling share), :133 (Flash bullet, 'Wrong with no error' list); .agents/skills/vfx-design/references/review.md:288 (IG-07 parenthesis)",
     expected: "The one flash counter of three books names, next to the command, every common case in which it reads low with no error (the rev3 standard), or counts it",
     observed: "Two lights or areas that flash in turn inside one region cancel: on each frame one light rises while the other falls by the same share, so the net is 0 in the whole frame, and the nine blocks catch it only when one light fills 90 % (10 % count) or 27 % (3 % count) of a block. A siren bar, alarm lights left and right in a corridor, two-tone warning lights: each light flashes 4 times a second, the count reads 0 or 1. Not in the list (the listed overlap case is the opposite: flashes at the same time). Film and marketing read only the 10 % count (film-craft review.md:128, channel-kits.md:32); in vfx the spec route of IG-07 catches it only when the lights are in this effect's own spec, not other lights in the busiest scene. Present since round 2 (old_loop.py gives the same numbers), not caused by the round-3 lines",
     evidence: "U2 (two amber lights, 11.8 % of the frame each, alternating at 4 Hz for 2 s): 1 at 10 %, 4 at 3 %, at 24, 30 and 60 fps; one of them alone: 4 and 4. U1 (two 3.1 % lights side by side in the centre block, 4 Hz): 0 and 1 at 24, 30 and 60 fps; one alone (T3c): 0 and 4. The box reading on one light's box: 3.96 Hz (U1 0.37,0.40,0.48,0.60; U2 0.10,0.40,0.45,0.62)",
     smallest_fix: "Add to the too-low list in measure.md:133: 'lights or areas that flash in turn inside one region (a siren, alarm lights left and right) cancel each other: a 4 Hz pair of 12 % lights reads 1 at 10 %, a pair of 3 % lights in one block 0 and 1 (24, 30 and 60 fps). Time each light with its own tight box (the box rate) and count it as flashes at that rate when it covers more than the count's share of the frame (10 % for cinematics and marketing, 3 % for effects).' In IG-07's parenthesis add 'or lights flash in turn'"}
  - {id: F2, class: blocking, check: "C8 V3 (rev3 F1 fixed only in part; the bullet claims more than the script does)",
     where: ".agents/skills/vfx-craft/references/measure.md:118 (re-arm only when the net fall reaches the region's share), :133 ('so a lasting dim, smoke that rolled in or a shadow cannot hide later flashes')",
     expected: "The claim holds, or the case it misses is in the list",
     observed: "A net fall re-arms a region only when the falling share reaches the region's share (10 % or 3 % of the frame, or 90 % or 27 % of a block). A lasting darkening smaller than that stays a falling share, and it still cancels the first flash after it when the flash covers less than the share plus the darkening. The flash's own fall then re-arms the region, so the later flashes count: one too few. That changes the verdict when the flashes fit in one second: a 4-flash burst (a hard fail) reads 3 at 10 %, which the film and marketing pointers pass ('at most 3'); in vfx a 3-flash burst reads 2 (a design pass). The round-3 line fixed every darkening larger than the share (rev3 P, L, K now right)",
     evidence: "U3 (a lasting shadow, 7.6 % of the frame falling, then four 15.3 % band flashes in 1 s): 3 at 10 % (truth 4), 4 at 3 %, at 24, 30 and 60 fps (round-2 loop: 0 and 4). T2 (dark smoke 1.5 % beside the spot, then three 4.3 % flashes in 1 s): 0 and 2 (truth 0 and 3; round-2 loop 0 and 0). S1 (a 6.1 % shadow, three 15.3 % flashes): 2 and 3 (truth 3 and 3). S6 (the same shadow, a 5 Hz flicker for 1.4 s): 5 and 5, right, because later windows hold all five",
     smallest_fix: "measure.md:133: replace 'so a lasting dim, smoke that rolled in or a shadow cannot hide later flashes' with 'so a lasting dim, smoke or a shadow over more than the count's share cannot hide later flashes'; add to the too-low list: 'a smaller lasting darkening in the region cancels the first flash after it when the flash covers less than the share plus the darkening: one too few in a short burst (a 7.6 % shadow, then four 15 % flashes in 1 s: 3 at 10 %; 1.5 % smoke beside three 4.3 % flashes: 2 at 3 %)'. IG-07's parenthesis: 'or after a smaller lasting darkening'"}
  - {id: R1, class: recommendation, check: "C3 (a new too-high case from the round-3 lines)",
     where: ".agents/skills/vfx-craft/references/measure.md:118-119, :133 (too-high list)",
     expected: "The too-high list names what a fixed camera can over-count",
     observed: "A large dark shape crossing a bright area (a boss or a cloud shadow over the sky) now reads 2 at 3 % (round-2 loop: 1). With one real flash in the same second the busiest-scene count reads 3, a design miss that is not there",
     evidence: "V1 (a dark 14 % shape crossing the sky at 8, 20 and 40 px per frame, fixed camera): 1 at 10 % and 2 at 3 % at each speed; V2 (a bright 12 % shape crossing): 1 and 1, as before",
     smallest_fix: "Add to the too-high list: 'a large dark shape crossing a bright area reads 1 at 10 % and 2 at 3 %: look at the frame of every listed onset'"}
rev3_findings_rechecked: [
  vfx rev3 F1 (a lasting fall cancels later flashes): fixed in every listed place for darkenings over the share: measure.md:118 (net fall re-arms, armed or not), the same-frame case in the :133 list, review.md:288 points to the list, coverage table d re-run, proposals row 19 for film-craft. My runs on the rev3 folders: P 0/3, L 3/3, K 0/2 (the same-frame flash, listed), A 3/3, B30 2/2, B60 2/2, C 0/3, D 0/3, J 0/3, H 1/3, N 0/3, Q 0/0, G box 2.0 Hz: as the rev3 reviewer predicted for the fix. The smaller-darkening residue: F2,
  film rev3 F1 (a flicker after an eased rise or a fade-up counts once, and the count changes with the rate): fixed (measure.md:119). My runs on the film reviewer's folders: L 5/5/5, TL 5/5, E 4/4/4, FF 5/5/5 at 24/30/60 fps; every other folder gives the same count at each rate (DK, D 6; H3 3; M 4; P, QL, n 5; S, a, k 4; F, J 1; QN, TN, i, i4 0),
  vfx rev3 R1 (two wordings of the cap): fixed, IG-07 and measure.md:133 'at most 2 by design, never more than 3', as SKILL.md:64 and RV-T06,
  input handling for three books: PNG renders `0000.png` and JPEG `f###_<ms>ms.jpg` both read; empty folder, mixed types, times that do not rise, 16-bit grey frames and boxes in pixels or swapped each stop with a message (my runs)
  ]
fixed_list: [only measure.md and review.md changed in the books after the rev3 review (file times); role frontmatter lines 1-10 identical to df13ff4; both SKILL.md frontmatter identical, 136 and 113 lines, descriptions 377 and 353 characters; measure.md §1-§6 and review.md §A-§I in order, nothing renumbered; no Riot, game or library names in the changed bodies (header lines only); LF endings]
keep: [
  the round-3 loop (lines 118 and 119): right on every rev3 and film rev3 case at every rate, and it removed the all-flashes-lost failure of rev3 F1,
  one counter for three books with loud stops on wrong input; the 10 % and 3 % counts and the box rate; the honest too-low and too-high lists with a tested number for each,
  everything in the rev3 keep list (read card, build order, §I lines and image budget, measure.md traps and footprint method, C-17 to C-31, SP-01 to SP-13, partner table, §9)
  ]
verdict: fix-first
</spec>
```

## Check results

| Check | Result | Note |
| --- | --- | --- |
| Rev3 F1 fixed in every listed place | yes, for darkenings over the share | measure.md:118 and :133, review.md:288, coverage table d, proposals row 19. The smaller darkening still costs one flash, and the bullet says it cannot (F2) |
| Film rev3 F1 on the one counter | fixed | L, TL, E, FF right at 24, 30 and 60 fps; all 48 film folders give one count at every rate |
| My own runs on the real input types | two unlisted low readings | JPEG captures and PNG renders. Alternating lights cancel (F1, present since round 2). A smaller lasting darkening hides the first flash of a burst (F2). One new over-count (R1) |
| Nothing else broken | pass | Every rev3 folder gives the count the rev3 reviewer predicted for the fix. Input stops work. Only the two book files changed |
| Fixed list | pass | See `fixed_list` |

**What to change.** Both blocking findings are text fixes in the Flash bullet (measure.md:133) and in IG-07's parenthesis; the script can stay as it is. F1 also routes alternating lights to the box rate, which already works on them (3.96 Hz for a 4 Hz light). After those lines are in, the counter is honest about every case I could make give a low number.
