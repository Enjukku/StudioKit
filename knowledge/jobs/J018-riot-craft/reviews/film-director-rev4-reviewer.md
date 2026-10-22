---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer film-director · claude-opus-5-5 · high · 2026-10-22

# Review: film-director books, round 4 (J018 stage 3, focused round)

```text
<spec>
artifact: .agents/roles/film-director.md (body) + .agents/skills/film-direction/ + .agents/skills/film-craft/ (evals/ not part of the work), working tree after repair round 3, 2026-10-22; the shared flash counter .agents/skills/vfx-craft/references/measure.md §6 as it is now
reviewer: J018 reviewer film-director (opus, high), round 4
looked_at_first: [
  reviews/film-director-rev3-reviewer.md (F1, R1-R3),
  the books as they are now: role body (fixed list: lines 1-10 cmp against df13ff4), film-craft/SKILL.md, references/blender-previs.md §6-§7, references/review.md §6-§7, film-direction/SKILL.md §2 and §7, references/game-cinematics.md §2, references/scene-studies.md; vfx-craft/references/measure.md §6 (script and note),
  grep of every film book for flash, the counter name, measure.md, and for a stale copy of the script (STEP, AREAS, flash_count_film),
  my own runs (scratchpad fdrev4/): the §6 script extracted from measure.md by script and run as printed (flash_shared.py); the same script without the round-3 line 119 (flash_prefix.py); the old film-book script (fdrev3/flash_from_book.py); on all 49 rev3 folders (fdrev3/, 24, 30 and 60 fps), plus new folders: camera pans and tracking moves with no flash (gen_pan.py: dark trunks over a bright backdrop, 15 % and 30 % cover, 4 and 8 px per 1/30 s; gen_col.py: dark columns over a lit hall, 25 % and 21 % cover, half and a quarter frame width per second; gen_real.py: a forest of dark trunks and crowns against a bright sky over a textured ground, pans at 10 % and 25 % of the frame width per second, and a 6 px camera shake), rain (gen_rain.py: dark streaks over 5 % and 15 % of the frame, alone, over the rev3 E case and over the FF case), and the maker's other case types (gen_extra.py: a lasting dim then three flashes over 4 % and 8 % of the frame, two eased pulses 500 ms apart, a hard cut); a variant harness (harness.py) and the candidate one-line fix as a patched script (flash_few.py)
  ]   # coverage/film-director.md "Repair round 3" was read after this
findings:
  - {id: F1, class: blocking, check: "C8 V3, C3, C2 (#20)",
     where: ".agents/skills/vfx-craft/references/measure.md:119 (the round-3 line `elif not r[4] and net >= 0: lo = x`) and its note :133 ('pans over stripes and over a textured scene -> 0 and 0'; 'a camera pan ... reads 2-4 in a second on the 3 % count (1 on the 10 % count)'); used by film-craft/references/blender-previs.md:80 ('Read the count over 10 % of the frame (cuts and pans over-read the 3 % count)'; 'a count over it is a fault in the edit or the effect marks'), review.md:128 (R-10), film-direction/SKILL.md:146 (§7 #20), game-cinematics.md:29, roles/film-director.md:47",
     expected: "The repair fixes rev3 F1 and breaks nothing else: a shot with no flash reads 0 (at most the documented 1 for a pan into a bright area) on the 10 % count, the same at 24, 30 and 60 fps, so R-10 can say 'within the vfx-design flash rule'",
     observed: "Rev3 F1 is fixed: the counter is right on every rev3 case. But the new line breaks camera moves that pass dark shapes in front of a bright backdrop (trees against the sky, columns in a lit hall, a fence, a crowd against a bright set). While a region waits, its trough follows the frame whenever the rises are at least the falls; the falls still count from the highest value since the flash. In such a pan, the pixels a dark shape has covered since the last onset fall, and the rises count only from the last frame, so the net goes below -10 % and the region re-arms; then the uncovered pixels rise from the new trough and count a flash. This repeats several times a second. The count is too high with no error, and it changes with the render rate. The film book tells the director to trust the 10 % count on pans, and to treat a count over the rule as a fault in the edit or the effect marks. Before the round-3 line the same folders read 1",
     evidence: "measure.md §6 script extracted and run as printed (fdrev4/flash_shared.py), 'most in any 1 s' at 10 % / 3 %, no flash in any of these folders: dark columns (21-25 % cover) over a lit hall, tracking at half a frame width per second: 3/4-5 at 24, 30 and 60 fps (the same script without line 119: 1/1); a quarter frame width per second: 1-2/2-3 (without: 1/1); dark trunks against a bright sky (30 % cover), 4 px per 1/30 s: 5/5, 4/5, 5/7 at 24, 30, 60 fps; 8 px: 2/7, 7/8, 8/10 (without: 1/1 everywhere); trunks at 15 % cover, 4 px: 1, 3, 4 at 24, 30, 60 fps (the rate claim fails); forest silhouette (trunks and crowns against the sky, textured ground) panned at 25 % of the frame width per second: 2/4-5 (without: 1/1). The 3 % count also goes high on rain alone at 60 fps (15 % streaks: 1/14, without line 119: 1/1); the film book reads the 10 % count, so this part matters for the vfx and marketing users of §6. Dark-scene pans with bright windows, the camera shake, pans over 50/50 stripes and the rev3 pan folders stay at 0, as the note says",
     smallest_fix: "In measure.md §6 (the vfx-designer's book; the lead routes it, the film books need no new text) change line 119 to `elif not r[4] and ((hi - x) >= STEP).mean() < r[1] / 2: lo = x  # waiting after a flash and almost nothing falls: the trough follows the frame`, and in the note say 'while it waits and almost nothing falls (under half the region's share)'. Tested (fdrev4/flash_few.py as a patched script, and harness.py): the same counts as the current script on all 49 rev3 folders (L 5/5/5, TL 5/5, E 4/4/4, FF 5/5/5 at 24/30/60 fps; every other rev3 case unchanged) and on the maker's case types (lasting dim then three 8 % flashes 0/3; two eased pulses 2; hard cut 1); 1/1 on every column, trunk and forest pan above (the documented 1 for a pan); rain over E and FF right at every rate (4, 5), and rain alone 1/1 at 60 fps. Add the column-tracking and trunk-pan folders (expected at most 1 at 10 %) to §6's tested list and to the test set in the flash-tool proposals rows (proposals/vfx-designer.md :18, proposals/film-director.md :25)"}
keep: [
  every rev1-rev3 keep item, still intact,
  the repair-3 work: one counter in one place (blender-previs.md §7 keeps no copy: no STEP, AREAS or flash_count_film line in any film book; every film pointer names measure.md §6: role :47, film-craft/SKILL.md :19, blender-previs.md :77, review.md :128, film-direction/SKILL.md :146, game-cinematics.md :29); the export recipe for the counter (one pass, shot-list rate, frame_step 1, new empty folder, 8-bit RGB PNG, #### names, view transform recorded, the first printed line checked) with its three tested traps (frame_step 2, interleaved shots, luminance images in the folder); the value-strip warning; R1 (the cut order reaches a cap of 8 on E1, every cut line 'not verified (image budget)', what a cap counts); R2 (B-06 spread from the same --mask run; the planned-silhouette alternative still passes on its own conditions); R3 (scene-studies.md:24 neutral)
  ]
verdict: fix-first
</spec>
```

## Earlier findings: fixed or open

| Id | State now | Evidence |
| --- | --- | --- |
| rev3 F1 flicker after an eased rise or a fade-up counts once | fixed in the shared counter (measure.md:119), and the film copy removed | fdrev4 runs of the §6 script: L 5/5/5, TL 5/5, E 4/4/4, FF 5/5/5 at 24/30/60 fps (the rev3 false passes); the 38 other rev3 folders unchanged and right |
| rev3 F1, the same kind (export traps) | fixed | blender-previs.md:78-81 |
| rev3 R1 cut order and cap | fixed | review.md §7 second and third bullets |
| rev3 R2 B-06 spread | fixed | review.md:102 |
| rev3 R3 studio name | fixed | scene-studies.md:24 |
| new: the round-3 line over-counts camera moves past dark shapes on a bright backdrop | open (F1 above) | fdrev4 pan, column and forest folders |

## Result per check

| Check | Result | Notes |
| --- | --- | --- |
| Fix in every listed place | pass | All six film pointers name `vfx-craft/references/measure.md` §6; no copy of the script or its constants remains in any film book (grep); the proposals rows second the vfx tool row and withdraw the landed row |
| Own runs | fail on F1 | The fix is right on every rev3 case and the maker's case types; the same line makes a no-flash tracking or panning shot past dark shapes read 2-8 per second on the 10 % count, rate-dependent. A one-line change (tested) keeps every right count and removes the over-count |
| Fixed list | pass | Role frontmatter lines 1-10 byte-identical to df13ff4 (cmp); film-direction/SKILL.md 146 lines, film-craft/SKILL.md 96; descriptions 379 and 388 characters; no section renumbered; no CRLF; Riot and studio names only in author headers and the role's build comment; files changed after rev3 for this role: the six film book files above plus coverage and proposals (other roles' files changed in their own rounds, measure.md by the vfx-designer) |
| Nothing else broken | pass apart from F1 | R1-R3 edits read in place; the B-06 planned-silhouette clause still reads as a full alternative ('passes instead' with its own conditions), so a dark, flat silhouette does not fail the new spread clause |

## Better work (C7)
Unchanged from rev3 apart from the count: the books still make a clearly better cinematic agent than the old ones. With F1 fixed in the shared counter, R-10 gives the right flash number on the director's real inputs (Blender PNG renders of an animatic with cuts, pans and tracking moves) and the books can pass.
