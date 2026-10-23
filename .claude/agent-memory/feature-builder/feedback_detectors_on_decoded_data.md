---
name: detectors-on-decoded-data
description: Tune any defect detector (clipping, clicks) on the form the tool really receives (MP3-decoded, both bitrates), with broadband real takes, and state the margin; a pure-sine fixture passed a check that missed 36 of 36 real clipped takes (J020 rank review, 2026-10-23)
metadata:
  type: feedback
---

Set a detector's reference and limit from the data in the form the tool receives, not from the clean array that made it. For audio from a service, that means decoded MP3 at every bitrate the service uses, made from broadband real takes, never only from a pure-sine fixture. State the margin between the clean group and the defect group, and say plainly which defects cannot be separated.

**Why:** in J020 `rank`, the clip check read time "within 0.5 dB of the take's own peak". The MP3 decoder overshoots above a clipped plateau and becomes that peak, so all 36 real clipped takes read clean (review-rank F1). The test had passed on a pure 220 Hz sine, whose plateau survives the encode. After the fix (time at or above -1 dBFS, full scale), sustained takes separate with a 2.8 ms margin. Short hits clipped even by 12 dB do not separate from clean full-scale hits at all, by any feature I tried.

**How to apply:** before choosing a threshold, survey clean real inputs against defect copies made from them (several strengths, every codec setting). Print the clean maximum and the defect minimum. Pick the limit with a stated margin. Write the unseparable cases into the docstring and the hand-back, not into a tuned rule fitted on the same 62 takes. Related: [[fixtures-like-real-inputs]], [[simulate-steps-in-sequence]].
