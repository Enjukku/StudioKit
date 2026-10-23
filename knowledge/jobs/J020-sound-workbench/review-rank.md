---
type: job
scope: game
status: active
updated: 2026-10-23
source: J020-sound-workbench
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-23

# Review: soundbench step 5, `rank` (b12e82e), by reviewer

**Depth:** deep. `rank` decides which take is used and when the cue goes to the owner (J020-D7), and it sits in front of a paid-reveal rule (D-03). This is round 1. The review is against the frozen revision b12e82e. The working tree has no changes under `tools/` relative to it. All runs used copies of the 62 real takes in the session scratchpad (`rv/`). No repository file was written except this review.

**Goal questions:**
1. Does every "use" match a real render that passes, and is every "regenerate" free of a fix that `render` would accept? (§6.3-4, J020-D7)
2. Is the level/headroom rule right for every level measure a card can name (F-09, F-13a, LUFS-I)? (§6.3, §7, review-1 #9)
3. Is a clipped-at-source take rejected on real (MP3-decoded) material? (§6.1)
4. Can `rank` weaken D-03, and is `render` unchanged by the refactor and the measure changes? (§7, D-03)

```text
<spec>
artifact: tools/audio/soundbench@b12e82e (rank.py, render.py, measures.py, tables.json, __main__.py)
reviewer: reviewer
looked_at_first: [git show b12e82e (all code files), rank.py whole, render.py whole, ops.py edit ops, measures.py level_db/true_peak_db/onset/sound_end, fixtures.py "clipped", editor-design.md §3-§7, test_soundbench_rank.py clip and MP3 tests]
findings:
  - {id: F1, class: blocking, where: "tools/audio/soundbench/rank.py:104-116 (clip_reading), CLIP_TOP_DB/CLIP_TOP_MS at :71-72",
     expected: "§6.1: a take clipped at the source is rejected outright",
     observed: "Real takes were hard-clipped at full scale (+3, +6 and +12 dB into a 1.0 clip), then encoded to MP3 (libmp3lame 128k) and decoded with intake.decode_take. This is the only form rank ever sees. All 36 clipped versions read clipped: False. Examples: gainfly-whoosh-1.t2 +12 dB had 111.6 ms flat at 0 dBFS before the encode and 0.11 ms 'within 0.5 dB of its own peak' after it (decoded peak +2.56 dBFS). gainfly-swish-2.t1 +12 dB: 96.4 ms before, 1.47 ms after. gainfly-note-speed-1.t2 +12 dB: 91.9 ms before, 0.02 ms after. The MP3 decoder overshoots above the clipped plateau. That overshoot becomes the 'own peak', and the plateau's ripple then falls more than 0.5 dB under it. So the relative band measures the overshoot, not the clipped run. Such a take goes on to be scored, and peak's gain-down cannot repair clipping, so a distorted take can get 'use'. The test that says 'clipping survives the MP3 round trip' (test_soundbench_rank.py:353-369) uses fixtures.make('clipped'), a pure 220 Hz sine. Its plateau survives the encode, but real broadband material does not",
     evidence: "High (a §6.1 rejection that does not fire on real material; distorted audio can be chosen). Run: scratchpad rv/e3.py on copies of 6 real takes. Label: not verified in Studio (a tool run, reproducible)",
     smallest_fix: "Read 'clipped at the source' against full scale, not the decoded overshoot. For example, count the time at or above -1 dBFS. On the decoded clipped versions this read 12.7-102 ms for clipped sustained takes; the 62 real clean takes read at most 7.23 ms (swish-2.t1). Then set the limit from that MP3-decoded data, not from array fixtures",
     protect: "the 62 clean real takes (at most 7.23 ms at or above -1 dBFS; the 8 ms limit leaves 0.8 ms margin: say so in the constant) and quiet takes, which never reach full scale",
     retest: "a test that clips a broadband real-like fixture (fx.make_real) at +6 and +12 dB, encodes to MP3, decodes, and expects 'clipped at the source'; plus the 62-real-take sweep with no rejection"}
  - {id: F2, class: blocking, where: "tools/audio/soundbench/rank.py:227-249 (simulate: derived level), formula in the docstring :30-34",
     expected: "§6.3: 'too quiet is fixable only when the gain needed fits inside the true-peak headroom', computed for the card's level measure (§7: F-09, F-13a, LUFS-I)",
     observed: "The formula takes gain = target - level_in and true peak after loudness = tp_in + gain. That holds for F-09 (all its thresholds are relative). It does not hold for F-13a or LUFS-I on a quiet take: the -70 LUFS absolute gate moves blocks in or out as the gain changes. On gainfly-thump-1.t1 (peak -33.7 dBFS, not near-silent), F-13a reads -57.712 at gain 0 but -59.351 + gain at every gain of 10 dB or more. op_loudness iterates, so it applies 39.35 dB, not the 37.71 dB the formula assumes. The predicted peak cut is then 1.64 dB too small: derived -25.557, simulated -27.2. Rank raises 'a soundbench bug, refused' from inside take_entry, so the WHOLE round exits 2 and nothing is ranked. Running the 20 real rounds with an F-13a card (target -20): 19 ranked, gainfly-thump-1 refused. F-13a is the level measure §7 names for a family of siblings, so paid-reveal families with a quiet take hit this. The builder's 20 real rounds used F-09 cards only",
     evidence: "High (rank cannot rank a real round for the family level measure; the guard fails safe, but on a valid card and a valid take). Runs: scratchpad rv/e2.py <takes> F-13a -20, plus the gain sweep in the review log. Label: not verified in Studio (a tool run)",
     smallest_fix: "Use the gain loudness actually applied (the op's logged total, or the level measured on the audio after the loudness step) for the true peak after loudness and for the predicted level. Do not use target - level_in",
     protect: "the F-09 path (exactly linear: the 20 F-09 rounds must still agree within 0.1 dB) and the 0.1 dB agreement guard itself",
     retest: "the 20 real rounds with F-09, F-13a and LUFS-I cards: no refusal, and derived equals simulated within 0.1 dB on every take"}
  - {id: F3, class: blocking, where: "tools/audio/soundbench/rank.py:171-192 (fix_plan: every step on any miss; loudness and peak whenever any step runs) and :316 (passes judged only on the all-steps plan)",
     expected: "§6.4: 'regenerate' only when no take passes after the fixable steps. A take that passes every must-target with no step at all passes",
     observed: "gainfly-thump-4.t2 with a card of F-09 target -22.87 tol 1, true_peak_dbtp max -1.0 (must), edge_clicks max 0 (AIM). Raw: level -23.775 pass, true peak -1.16 pass, edge clicks 2 (aim miss). The aim miss starts the plan trim + fade + loudness + peak. Loudness raises the level to the target, then peak cuts 1.41 dB to its -1.5 limit, so the level lands at -24.276 (must miss, listed under 'introduced'). Rank exits 1 'regenerate'. render of the same take with edit [] exits 0 with every must-target passing. Rank never checks the take with fewer steps (only the must-driven steps, or none), so an aim fix that breaks a must turns a usable take into a regenerate. The window is a raw true peak between the peak limit (-1.5) and the card's max: the only case where loudness + peak can lower a level that already passes",
     evidence: "High (a wrong verdict and exit code: a spent ElevenLabs round and one of the 3 rounds before the owner, J020-D7). Run: scratchpad rv/e1.py takes gainfly-thump-4.t2.mp3 -22.87 -1.0. Label: not verified in Studio (a tool run)",
     smallest_fix: "When the all-steps plan adds a must miss, also score the plan built from the must misses only (no steps when the raw take has none), and keep whichever has fewer must misses. Report the dropped aim fixes",
     protect: "the proof render must still be of the plan rank reports; and the real rounds where peak is needed anyway (raw true peak over the max: hit-speed-2.t2/t3, thump-1.t2, thump-4.t1, whoosh-1.t3), whose introduced level misses are honest",
     retest: "the e1 case returns exit 0 with steps [] (or the must-only plan), and its proof render agrees"}
  - {id: F4, class: blocking, where: "tools/audio/soundbench/rank.py:190-191, 231-233 (the peak limit comes from true_peak_dbtp only); render.py:281-282 (apply_steps maps only the true-peak max to the ceiling); STEP_FOR at rank.py:81 says sample_peak_dbfs is fixed by 'loudness and peak'",
     expected: "§6.3: a level is fixable when the gain fits inside the peak headroom. A card's sample_peak_dbfs max is a peak limit the fix must respect",
     observed: "gainfly-thump-3.t2 with a card of F-09 target -22.5 tol 1 and sample_peak_dbfs max -3.0 (must), no true-peak target. Rank plans loudness + peak at the default -1.5 limit. The sample peak then reads above -3, so rank says must miss sample_peak_dbfs and exits 1 'regenerate'. render with edit [loudness, peak ceiling_dbtp -3.0] exits 0: sample peak -3.51 pass, level -23.423 pass. A fix exists, and rank never sets peak's ceiling from the card",
     evidence: "Medium (a wrong 'regenerate' for any card that names a sample-peak max under -1.5 dBFS). Run: scratchpad rv/e4.py. Label: not verified in Studio (a tool run)",
     smallest_fix: "Set peak's ceiling (and the formula's limit) to min(-1.0, true_peak max, sample_peak max). The sample peak is never above the true peak, so a true-peak ceiling at the sample max is enough",
     protect: "render's own behaviour for recipes that set ceiling_dbtp; the F2 formula agreement",
     retest: "the e4 case: rank plans peak with ceiling -3, the level is fixed, exit 0, and the proof agrees"}
  - {id: F5, class: blocking, where: "tools/audio/soundbench/rank.py:303-316 (a refused fix sets fix None, passes False, but must_after is taken from the raw rows) and :329 (rank_key has no 'passes' term)",
     expected: "§6.2-4: a take's place and the verdict follow whether it passes. A non-passing take never sits above a passing one",
     observed: "When simulate raises an ordinary refusal, the take gets passes_after_fix False but is ordered by its RAW must and aim counts. A take with no raw must misses (it passes untouched) then reads 'passes: no', and its key [0, 0, aim count, ...] can sort above a passing take that has more aim misses. It becomes the top take, and the verdict is 'regenerate' even though the second take passes. The refusal does happen on real takes: with a LUFS-I card (valid: the takes are 480 ms), the aim sound_ms max 400 adds a cut to 399 ms (or trim shortens the file to 308-394 ms), then LUFS-I refuses ('needs 0.4 s or more'). That happened on 28 takes across 16 of the 20 real rounds. Example: gainfly-thump-4 take 2 has fix_error and must_after ['edge_clicks'], which trim + fade alone would fix. I did not reproduce a refused take sorting above a passing take on real takes; that part is shown by the code",
     evidence: "Medium (a wrong verdict through ordering; the code path is proven, and the refusal is shown on 28 real takes). Run: scratchpad rv/e2.py <takes> LUFS-I -20; code read rank.py:303-329. Label: not verified in Studio",
     smallest_fix: "Put passes_after_fix (or 'fix refused') into rank_key right after 'rejected'. Combined with F3, retry a refused plan as the must-only plan before giving up",
     protect: "the order of takes that already have a fix (the 20 real F-09 rounds must not change order)",
     retest: "a unit test with two entries: a refused fix with no raw must miss and 0 aim misses, and a passing take with 2 aim misses. The passing take is top and the verdict is 'use'"}
keep:
  - "render refactor: context() and apply_steps() are the old lines moved unchanged (same ctx keys, same peak-ceiling clamp, same snapshot order); render's order of work is identical"
  - "measures.f09_rms by cumulative sum: same windows as np.convolve 'valid'; float64 accumulation; on 7-minute files (full-scale noise, -40 dB with a -60 dB end, -60 dB with a -40 dB end) the worst window error against math.fsum was 9e-10 dB, and 6e-11 dB on the loudest window; the max(.., 0) clamp guards a negative difference"
  - "measures.clicks edges from the stored samples: this is what playback starts and stops on. It removes the false edge clicks the mean removal made on zero-start takes, and it flags a DC-offset file whose ends sit at the offset (a real step from 0). It changes render's edge_clicks only for files with DC at an edge, and that change is the correct direction"
  - "the proof render: the top take's plan rendered for real in a temp copy, every row compared by value and result, the row count compared; a mismatch refuses (exit 2). No 'use' goes out without it"
  - "D-03: rank calls render.family_members first (the same refusals), writes no family state (the proof's family.json lands in the temp root), and says that render checks parity. Rank cannot weaken render's family check"
  - "'near' = inside the target and within the tables.json margin of a limit. That is the reading the design needs: §5 'a picture only when a number fails or is near its limit', §6.2 lists near apart from missed, and render counts these values as passes. The other reading (just outside) would let rank call 'near' a value that render fails"
  - "the order key: a must miss after the fix always sorts below a pass, except through F5"
  - "find_takes: round 4 or more refused, --round 0 refused, a missing round named"
weakest_part: "F1's alternative limit comes from libmp3lame 128k at one setting; ElevenLabs' own encoder may overshoot differently, and the clean-take margin at -1 dBFS is thin (7.23 vs 8 ms)"
could_not_check:
  - {step: "planted faults 11/11", missing_input: "the planted-fault log on b12e82e (only the 52 rank and measures tests were rerun here: OK)", closes_it: "qa-lead's planted-fault result, which should include an MP3-decoded broadband clip", who: "qa-lead or feature-builder"}
  - {step: "full gate (1054 tests)", missing_input: "a verify.py run on b12e82e by me", closes_it: "the builder's gate log on the candidate", who: "feature-builder"}
  - {step: "F1 on ElevenLabs' encoder", missing_input: "a take ElevenLabs returned clipped", closes_it: "one deliberately hot ElevenLabs request decoded and measured", who: "feature-builder"}
  - {step: "F5 ordering on real takes", missing_input: "a real round where a refused take sorts above a passing one", closes_it: "the unit test in F5's retest", who: "feature-builder"}
  - {step: "proof tolerance near a limit", missing_input: "a take whose simulated value sits within 0.02 of a limit (a FLAC rounding flip would refuse)", closes_it: "a test with a value on the limit", who: "feature-builder"}
verdict: fix-first
</spec>
```

## Answers to the brief's questions
- **"Use" when the real render would fail:** No. The proof render compares every row, so a top-take "use" always matches a real render, and the family check stays in `render`.
- **"Regenerate" when a fix exists:** Yes, three ways:
  - **F3:** an aim fix plus the level reset breaks a must-target on a take that passes untouched;
  - **F4:** a sample-peak max is never used as the peak ceiling;
  - **F5:** a refused fix is ordered by raw counts.
- **Level and headroom formula:** right for F-09. Wrong for F-13a and LUFS-I on quiet takes, where the absolute gate makes the gain non-linear (F2). It also ignores a sample-peak max (F4).
- **Order key:** a must miss after the fix never sorts above a pass, except a take whose fix was refused (F5).
- **Clip check:** relative to the take's own peak is the wrong reference. On MP3-decoded takes the decoder's overshoot sets that peak, so 96-112 ms of clipping reads as 0.1-1.5 ms (F1). "Clipped at the source" is a full-scale event, so here an absolute reference is the right one. The quiet-take lesson (absolute thresholds fail on quiet takes) does not apply, because a quiet take is never at full scale.
- **"Near":** inside the target and close to a limit, as the builder made it (keep list).
- **D-03:** rank cannot weaken render's checks (keep list).
- **render refactor:** behaviour unchanged. The clicks change alters render's edge reading only for files with DC at an edge, in the correct direction (keep list).
