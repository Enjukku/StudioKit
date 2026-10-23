---
name: simulate-steps-in-sequence
description: When computing "can a pipeline step fix this", choose each later step from the measures after the earlier steps, and model playback on stored samples; real takes broke both raw-input shortcuts (J020 rank, 2026-10-23)
metadata:
  type: feedback
---

Plan each fix step from the state the earlier steps leave, never from the raw input, and read any "what playback hits" measure on the stored samples, not on a normalised copy.

**Why:** in J020 step 5 (`soundbench rank`) the first plan chose steps from the raw take's misses. A smoke run on real ElevenLabs rounds showed `trim` moving the F-09 level out of range (-17.1 to -14.9) and the sound length past its max (280 to 309 ms) with no `loudness` or `cut` planned. All 18 synthetic tests had passed. The same run found that `clicks.edges` read the mean-removed audio: a real low thump that started and ended at exactly 0 read 2 edge clicks, and that turned a passing round into "regenerate".

**How to apply:** for any "simulate the fix" tool, run the real step loop stage by stage and re-measure between stages. Make the final steps (level, peak) always close the pass. Run the tool on the real inputs before trusting a green suite ([[fixtures-like-real-inputs]]). Add a planted fault for each ordering shortcut ([[planted-faults-unequal]]).
