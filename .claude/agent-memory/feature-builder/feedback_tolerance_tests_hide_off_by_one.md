---
name: tolerance-tests-hide-off-by-one
description: Measure tests with +-tolerances let off-by-one and offset faults survive; add one exact-answer fixture per measure; check survivors for equivalent mutants
metadata:
  type: feedback
---

Every numeric measure needs at least one fixture whose answer is exact by construction (a DC-free square wave for energy shares, a steady tone for an onset), asserted tightly, next to the realistic tolerance tests.

**Why:** J020 soundbench step 1-2 (2026-10-23): planted faults "attack-share window +1 sample" and "main-transient window-centre offset dropped (0.5 ms)" survived suites whose tests used +-1 ms or range checks on noisy hit fixtures. Golden JSON (rounded to 0.01) caught every off-by-one in the moved measures, but only because the old tool's numbers were frozen. Also: one survivor ("pad each file to its own length + 0.4 s" for F-13a) was an equivalent mutant: digital-silence padding sits under the -70 LUFS absolute gate. Reason it through before adding a test, and plant the real fault (no padding) instead.

**Repair round 1 (same job):** the reviewer showed two guards that could not fail: lag measured on the mono sum (one channel shifted 30 ms passed) and compensation by the reading, re-checked with the same estimator (0 by construction). Rule: every compensation verifies against a declared value, every multichannel time check runs per channel, and a re-check that uses the same estimator on its own output is not a guard. Also remove DC before any correlation.

**Steps 3-4 (same job):** a compressor test computed its expected values with the function under test (`static_curve_db`), so a knee-formula fault survived; a family test's "too loud" case also failed a second check (peak spread), hiding the LU limit. Rule: expected values are hand-worked literals or an independent library, and each boundary case must be able to fail on one check only.

**How to apply:** for each measure, list the faults that move the number by less than the test tolerance and add an exact case. Report equivalent mutants by name with the reason, never as a caught fault. Related: [[planted-faults-unequal-parts]], [[bash-heredoc-escapes]] (the heredoc rewrote `\n` in a fault list again).
