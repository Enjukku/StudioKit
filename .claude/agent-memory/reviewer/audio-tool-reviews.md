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
