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
Rank round 2 (2026-10-23): a "do nothing" plan added as a fix candidate must pass the export's own refusals (a
master over full scale cannot be written at 24-bit); proof-render every take's kept plan, not just the top. A clip
or level reading that is a total time (ms over a threshold) grows with take length: calibrate on long takes too.
Step 6 loops/layers/variants (2026-10-23): (1) a card target with must:false must never set the limit of a must
guardrail row: grep every `.get("max", CONST)` that reads a card target into a must row (loop_seam lifted R-26's F-08 2.0
to the card's aim 50: exit 0 on a 0.1 x peak drift click). (2) Loop seam readings built on whole-file percentiles
(F-08 p95, HF p99, click floor 1 % of peak) go blind when the seam sits in a quiet part of a bed with a loud section:
build a circular (FFT-filtered) bed so the base loop is exact, then plant jumps re the LOCAL step RMS. (3) Alignment by
a threshold crossing (main transient -10 dB) moves with DC removal context on slow-rising takes: compare the align
reading with the as-placed reading on real swishes.
Step 6 round 2: a repair that adds an automatic `dc` (whole-take mean subtraction) to a layer leaves a step at the
layer's edges inside the mix (a take ending at ~0 now ends at -mean): 0 -> 2 clicks on a real swish at exit 0. When a
fix is "remove X so the reading is stable", check it changes only the reading, never the placed audio: diff the click
count and edge steps against a mocked no-fix baseline.
Step 7 `generate` (paid API client, 2026-10-24): (1) urllib raises http.client.IncompleteRead (HTTPException, not
OSError) when a 200 body is cut: a "catch network errors as possibly spent" handler misses it; patch urlopen to prove.
(2) Run logs written only on the happy path lose every attempt on any late exception: ask for a finally. (3) Existence
checks at plan time + mode 'x' at write time = a concurrent run loses a PAID take (FileExistsError after the charge).
(4) Count 5xx-without-cost-header like a timeout. (5) Preflight every local dependency (ffmpeg) before the first paid
call. (6) A cap keyed on a name the input file chooses (layer names) is bypassed by renaming. (7) Default urllib opener
forwards custom auth headers on cross-host redirects: prove with two loopback servers.
Rank on layered rounds (2026-10-24): when a judge READS an existing recipe (placement, targets) but simulates and
proves a stripped copy (design: [], no loop), "every use proven by a real render" proves the wrong recipe. Test: add one
ordinary design step (highpass 60) to recipe.json, then render recipe.json with the judge's choice: 5 of 6 real cases
flipped use -> exit 1. Also cross-check every round count against generate.cue_rounds (counts takes/rejected/ too).
Hand-check level verdicts with crest = F-09 - TP vs target - (ceiling - margin): gain-only reachability in one line.
Layered rank round 2 (2026-10-24): when a fix makes the proof recipe the real recipe, every old exemption that existed
because the proof was partial (form./variants. rows filtered from must_failed) becomes a false `use`: grep the filters.
Variant spread failures need a level target with headroom (-24): at -18 the peak cap hides the spread.
