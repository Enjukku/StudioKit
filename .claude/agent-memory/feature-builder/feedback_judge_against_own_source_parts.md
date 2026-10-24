---
name: feedback-judge-against-own-source-parts
description: "Relative to the take" can still false-alarm when it is relative to the whole file's distribution; judge an edit (crossfade, splice) against its own source parts; check planted faults fail by assertion, not crash
metadata:
  type: feedback
---

A level guard relative to the whole loop's 5-95 % window range (J020 step 6, 2026-10-23) false-alarmed on 90 of 1,160
natural positions and failed 3 good loops built from real takes (+6 to +9 dB: the seam held the bed's loudest
moment). Judging the crossfade against the band between its own two source parts' levels, per window, separated
cleanly (good -1.7..+0.6 dB; wrong curves -1.7..-3.1 and +2.6..+3.0). A gap reading against the file's 5th
percentile is blind on beds that already hold near-silent lulls (0 of 9 real-take beds caught).

**Why:** real beds are peaky and gappy; any whole-file statistic treats a natural swell or lull at the seam as a
defect, or hides a real one. The reviews keep finding thresholds calibrated on steady synthetic material.

**How to apply:** for an edit operation, compare its output with the exact inputs it was made from (same windows,
same positions) before reaching for file-wide percentiles; calibrate every detector at many natural positions
(rotate a good loop) on real-take material, and report the false-alarm count. In a planted-fault test, print why
each fault fails and require FAIL (assertion), never ERROR (a patch with the wrong signature also "catches").
Related: [[feedback-fixtures-like-real-inputs]], [[feedback-planted-faults-unequal]].
