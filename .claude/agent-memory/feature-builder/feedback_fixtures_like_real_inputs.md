---
name: fixtures-like-real-inputs
description: Audio (and any signal) tools must be tested on fixtures shaped like the real inputs - level, start, length, channels - not only full-scale ideal ones
metadata:
  type: feedback
---

Before calling a signal tool done, measure a handful of real inputs (level, first sample, length, channel balance, noise floor) and add fixtures that match them; run every guard on those, plus an optional env-gated test on the real files.

**Why:** J020 soundbench steps 3-4 (2026-10-23): every fixture peaked near full scale and started from silence; real ElevenLabs takes peaked at -24 to -43 dBFS, started mid-waveform and came back 480 ms for a 0.5 s request. Absolute thresholds (afftdn nf, compressor threshold, full-scale-normalised saturation) silently did nothing or ate the sound, guards checked one direction only, and the intake refused every real take. The reviewer found all of it in one run on 10 real takes; 133 passing tests had not.

**How to apply:** design-pass parameters relative to the input's own peak or measured floor; guards in both directions where both are damage; one realistic fixture per input class; `SOUNDBENCH_REAL_TAKES`-style optional test. Related: [[tolerance-tests-hide-off-by-one]].
