---
name: audio-tool-reviews
description: How to review soundbench / audio DSP tools: run real ElevenLabs takes (quiet, hot-start), check level-dependent ops and one-sided declarations
metadata:
  type: feedback
---

Review audio tools (tools/audio/soundbench) by running real takes, not only the builder's synthetic fixtures. Real
GreatWallSim ElevenLabs takes (GreatWallSim worktree audio/_raw/sfx, read-only; copy to scratch) peak anywhere from
-36 to 0 dBFS, start mid-waveform (first sample -1 to -20 dB re peak), and 0.5 s requests decode to 480 ms.

**Why:** in J020 steps 3-4 (2026-10-23) every synthetic test passed, but real takes showed: saturate (tanh normalised
to full scale) is a pure gain on quiet takes; afftdn `nf` in absolute dBFS ate a quiet hit's body (-14 dB, 480 -> 176
ms, channel balance changed) and the attack guard passed it; stretch refused on its own probe at ratios inside its
allowed range; a paid-reveal family declared on one card only let the other sibling be re-rendered 8 LU louder at exit 0.

**How to apply:** for each op ask "what does it do to a take at -35 dBFS peak?" (absolute thresholds, drives, noise
floors); for each guard ask "does it check only a drop, so a rise or a loss of body passes?"; for every two-sided rule
(families, siblings) ask "what if only one side declares it?"; sweep each allowed parameter range, not the tested
points; check malformed-input exit codes against the documented 0/1/2 contract.

Round 2 (2026-10-23) lessons: a group rule keyed by an id (paid family "egg") must also gather every card carrying
that id, not only the cards that list each other: two disjoint pairs with one id both passed at exit 0, 5 LU apart.
An automatic fix inside an op (trim's 0.5 ms edge fade) can bypass a rule another op enforces (fade-in keeps 90 %
of attack share or needs a why): sweep the real takes for the protected measure. Whole-file summary numbers
(saturate residual_db) are dominated by the transient on hits: compare with the body-only number before trusting.
Real GreatWallSim takes include no sustained kind: stretch/pitch need synthetic sustained material (slow: ~10 min).

Step 5 `rank` (2026-10-23) lessons: (1) a clip check relative to the take's own peak fails after MP3: the decoder
overshoots above the clipped plateau, so 100 ms of clipping reads ~0.1 ms "within 0.5 dB of peak"; always test clip
detectors on clipped-then-MP3-encoded broadband real takes, not a sine fixture. (2) LUFS measures (F-13a, LUFS-I) are
not linear in gain on quiet takes (-70 LUFS absolute gate): any formula "gain = target - level_in" breaks; run real
rounds with every level measure the card can name, not only F-09. (3) A ranker that judges only the "fix every miss"
plan can turn a must-passing take into a regenerate (aim fixes + loudness/peak); always compare against "no steps".
(4) A refused fix that keeps raw counts in a sort key can outrank a passing entry: check the key has a "passes" term.
