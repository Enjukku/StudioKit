---
name: feedback-simulate-in-the-consumers-frame
description: A simulation that must match a later real run has to read its numbers in the same context (buffer length, channels, neighbours) the real run uses; probe what the context moves before scoring
metadata:
  type: feedback
---

J020 rank on layered rounds (2026-10-24): render reads each layer's rows on the layer placed in a buffer as long as
the whole mix; scoring a layer take alone gave other numbers (a probe with 600 ms more silence moved a real hit's
sound_ms 274.6 -> 294.1 ms, tail_snr 38.6 -> 46.0, band shares and edge clicks: the measures remove the buffer mean).
The fix: read each candidate in the mix it would make with the other layers' current choices, iterate until the
choices stay the same, then assert the chosen rows equal the real run's value for value. A first version read every
candidate in the chosen mix's frame and crashed on a longer runner-up: a candidate's frame is max(own, others').

**Why:** "one code path" is not enough when the context of the call differs; the proof render would have refused every
layered `use` as a rank/render disagreement.

**How to apply:** before scoring parts of a whole, probe which measures move with the surrounding context (length,
padding, channel count, neighbours); keep an exact-equality guard between the simulated and the real reading; make the
"read in isolation" shortcut a planted fault. Related: [[simulate-steps-in-sequence]], [[fixtures-like-real-inputs]].
