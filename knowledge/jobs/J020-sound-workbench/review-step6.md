---
type: job
scope: game
status: active
updated: 2026-10-23
source: J020-sound-workbench
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-23

# Review: soundbench step 6, layers, loops and variants (1cdae69), by reviewer

**Depth:** deep, round 1. The change decides what a delivered file may hold, and it reaches the paid-reveal rule D-03. I reviewed the frozen revision 1cdae69 (HEAD; the working tree has no changes under `tools/audio`). I read the code before the commit message's claims. Every run used copies of the 106 real GreatWallSim takes in the session scratchpad. The scripts are in the same folder (`e1_*.py`, `fa_render.py`, `p2.py`, `p4*.py`, `p5.py`, `p6.py`, `plant.py`). No repository file was written except this review.

**Goal questions:**
1. Can a layered, looped or variant delivery reach exit 0 when it is wrong? (G-4, G-5, §4 rows, R-26, D-03)
2. Is every `must` row in `form_checks` binding: in the exit code, in the family check and in rank's "use"? (§3 `render` exit 1, §6.4, §7)
3. Do the refactors leave behaviour unchanged? (`check_targets`, `click_steps`, `main_transient_index`, `check_params(spec)`) (G-3)
4. Are the loop readings relative to the loop's own material, do they guard both directions, and do they hold at 2-30 s? (§5 false readings, F-08)

**Verb and weight:** "deliver a loop or a set" decides this review. I weighted the loop wrap and the family/variant rows most heavily. Harm areas 1, 2 and 4-5 (saves, client gain, lifetimes, peak load) mostly do not apply to an offline tool. I walked each one; see coverage in the hand-back.

```text
<spec>
artifact: tools/audio/soundbench@1cdae69 (assemble.py, render.py, card.py, measures.py, ops.py, tables.json, fixtures.py, __main__.py; tests test_soundbench_assemble.py, test_soundbench_realtakes.py)
reviewer: reviewer
looked_at_first: [git show 1cdae69 (every code file), render.py plan/apply_steps/family_members/family_check whole, ops.py op_peak/op_mono/op_loudness/op_varispeed, export.py check_exportable/export_flac, measures.py F-08 (cue_numbers) and clicks, rank.py prove/verdict, editor-design.md §1, §4-§7, §9]
findings:
  - {id: F1, class: blocking, where: "tools/audio/soundbench/render.py:483 (loop_rows: f08_max)",
     expected: "R-26 (render.py:53): the form.loop_f08 row is must, at most 2. A card target that is only an aim (must: false) cannot relax a must guardrail; a card may tighten it, never loosen it (the same one-sided rule as D-03 families)",
     observed: "f08_max takes the card's targets.loop_seam.max whatever its `must` flag says and whatever its size. Test case: a 10 s tonal_pad bed looped by loop_bed, with the builder's own planted F-08 fault (a linear drift ending in a jump of 0.1 x peak; the delivered wrap step is 0.089 x peak). With no card target, the result is exit 1, must_failed [form.loop_f08] (F-08 3.236 > 2). With targets.loop_seam {max: 50, must: false}: exit 0, must_failed [], form.loop_f08 3.236 with max 50 'pass'. No other row catches this fault: clicks 0, wrap_hf and gap pass. A plausible aim also works: with {max: 3, must: false}, the same fault in the 2 s and 30 s tonal_pad (F-08 2.81 and 2.72) is caught only by F-08, so those loops pass at exit 0. A drift jump of 10 % of peak in a smooth pad is a clear click. The number in the report looks fine ('pass')",
     evidence: "Medium (a must guardrail is bypassed through an aim target; a wrong loop is delivered at exit 0). Runs: scratchpad fa_render.py (full render, FLAC, exit codes) and p2.py (loop_rows on 2/10/30 s beds). Label: not verified in Studio (a tool run, reproducible)",
     smallest_fix: "f08_max = min(card loop_seam max, LOOP_F08_MUST_MAX) when the card's max is given. If a looser card limit is really intended, it needs must: true and a `why`, and that is a design question for the lead, not a silent default",
     protect: "a stricter card limit still applies (max 1.0 must stay 1.0); the targets row 'loop_seam' in `targets` is unchanged (rank's proof compares it)",
     retest: "a test: the planted 0.1 x peak drift on tonal_pad 2/10/30 s with targets.loop_seam {max: 50, must: false} gives exit 1 with form.loop_f08 in must_failed; add it to the planted-fault list"}
  - {id: R1, class: recommendation, where: "tools/audio/soundbench/measures.py:180 (F-08 p95 over the whole file), :400 (click floor 1 % of the file peak), :455-456 (wrap_hf against the 99th percentile of every window)",
     expected: "loop_wrap's docstring says 'each relative to the loop's own material'; §5 asks every measure to list its false readings",
     observed: "All three readings compare the seam with the whole loop, not with the material around the seam. Every calibration bed is steady (at most a +-3 dB swell: fixtures.make_bed). Test case: a 10 s bed that loops exactly (circular wind low-passed at 400 Hz at -30 dB, with rain swelling in over the middle half), delivered as a pre-looped take (no loop step, the path test_a_loop_card_judges_the_wrap_even_without_a_loop_step covers). A jump planted at the wrap gives a wrap step 19 x (25.7 dB) the local step RMS, with energy above 2 kHz 10.8 dB over the local median. Result: exit 0, F-08 0.059, wrap_clicks 0, wrap_hf -44.66 dB, gap 0. The click row catches the jump from about +2 dB more (exit 1). So only the click floor of 1 % of peak protects the seam; F-08 and wrap_hf are blind there, 40 dB under their limits, because the loud section sets their baseline. The same happens at 4, 10 and 30 s and with the loud share at 0.3, 0.5 and 0.7",
     evidence: "Recommendation, not blocking: the remaining miss is a step of about -42 dB re peak in a quiet passage. It is the documented 'click under 1 % of the peak' reading, and the builder already accepts larger named misses (a 0.25 x peak spike in low-passed noise). Runs: e1b.py, e1c.py, e1_render.py. Label: not verified by listening",
     smallest_fix: "Either add 'beds with a loud section: F-08 and wrap_hf read the seam against the loud part; only the click floor remains' to the loop_wrap false readings and the hand-back's limits, or read F-08 and wrap_hf against a window of +-0.5 s around the seam and recalibrate on the 1,160 natural positions",
     protect: "the 1,160-position false-fail rate", retest: "e1b.py: no jump of more than +0 dB over the local step RMS passes"}
  - {id: R2, class: recommendation, where: "tools/audio/soundbench/rank.py:529-532 ('use' say text) with prove() :501",
     expected: "§6.4 'use' means the take passes every must after its fixable steps. Rank should never state more than its own proof shows",
     observed: "A minor hit card with form.variants 4 and three real-like takes: rank exits 0 with 'use: passes every must-target after its fixable steps', while proof.must_failed = ['form.variants']. The proof recipe has no variants step, so every variant card shows this, and a pre-looped loop card shows wrap misses the same way. Judged against the brief's question 2: not blocking. Rank is not a delivery. render still exits 1 until the recipe makes the variants or the loop, so no wrong file reaches exit 0, and the proof's must_failed is printed in rank's Markdown",
     evidence: "Recommendation. Run: p6.py. Label: not verified in Studio (a tool run)",
     smallest_fix: "When proof.must_failed holds only form.* rows, say so in the 'use' text ('the one-shot passes; the loop/variant rows are judged at render'). Do not change the targets or the code",
     protect: "rank's 60/60 equivalence on targets", retest: "p6.py: the say text names form.variants"}
  - {id: R3, class: recommendation, where: "tools/audio/soundbench/assemble.py:84-96 (transient_index) vs render.py:433-437 (layers[].measured)",
     expected: "'align lands within 1 sample', read the one way (`measures.main_transient_ms`)",
     observed: "Test: 27 layers from 9 real three-take sets (the second take of each set resampled to 48 kHz). 25 land on the marker within 1 sample; 2 do not. gainfly-swish-2.t1 logs measured 397.73 ms against the 400 ms marker (2.27 ms off); gainfly-swish-4.t3 (the 48 kHz layer) logs 419.84 against 407.3 (12.54 ms off). Both are slow-rising swishes whose -10 dB crossing is grazed (first crossing at exactly -10.0 dB) and which carry DC (mean up to -0.0135). transient_index removes the mean of the layer plus 2 ms of padding, but the as-placed reading removes the mean of the whole mix, so the threshold crossing moves. The audio itself is placed once and DC does not move what is heard, so the error is in the log, not in the sound. Still, the log then reports a 12.5 ms miss the agent may try to 'fix'",
     evidence: "Low; a truth-of-the-log issue. Run: p4.py, p4b.py. Label: not verified by listening",
     smallest_fix: "Name 'rising layers with DC: main_transient alignment is unstable; align them on F-01' in transient_index's false readings, or read the transient on the placed layer and correct once",
     protect: "the 25 exact cases", retest: "p4.py: every layer's measured value within 1 sample, or the log flags the unstable reading"}
keep: [
  "loop_bed/loop_music wrap: the last sample is x[s-1] and the first is x[s], exact through FLAC (read and test_loop_bed_wrap_is_sample_exact_through_flac)",
  "the edit pass after a loop step is gain only (mono, loudness, peak: op_peak is gain, never a limiter), and trim/cut/fade are refused there, so the seam survives",
  "crossfade_level guards both ways (+-2 dB) against the loop's own two parts; the curve follows the measured correlation",
  "loop readings at 0.5-1.5 s hold: good loops pass (one real_bed false fail at 1.5 s), and spikes and gaps are caught (p5.py); short loops give 'no value', which fails, never passes",
  "variants: seeded RandomState, stratified draws; SC-12 refused both in the card (form.variants) and in plan_form; every variant file and the other member's variant files enter D-03 (family_check plus delivered_files); stale files of the other form are removed before export",
  "every form_checks must row enters must_failed and the exit code (render.py must_fail over targets + form_rows)",
  "layers: one offset for every channel (place), resample_poly at the exact ratio; a planted right-channel 1-sample slip fails 4 layer tests (plant.py); check_exportable runs on the summed mix",
  "the refactors change nothing: check_targets is the moved block verbatim and now also validates layer targets; click_steps and main_transient_index return the same values; check_params(spec=None) takes the old path, and the op-specific checks run only for its own table"]
weakest_part: "Audibility. Every 'wrong' here is a screening number (a step size, energy re local material), not a listening check: the size at which a seam step is heard in a quiet bed is my estimate, so R1's ranking could move either way"
could_not_check: [
  {step: "R-26 itself: a 5 % of peak drift step in tonal_pad passes all four readings at F-08 1.1-1.7 (inside R-26)", missing_input: "a listening judgement of whether that step clicks", closes_it: "an owner or sound-designer listen at the first real loop cue", who: "sound-designer / owner"},
  {step: "Roblox's transcode at the loop point", missing_input: "an upload and a capture", closes_it: "the first real loop upload (editor-design §11)", who: "qa-lead"},
  {step: "the realtakes test module", missing_input: "3 of its tests skipped in my run (their real-take path was not set)", closes_it: "the builder's gate log with the real-take path", who: "feature-builder"},
  {step: "the full gate (1093 tests)", missing_input: "I ran only the soundbench assemble, render, rank and realtakes modules (81 tests, OK, 3 skipped), not tools/verify.py", closes_it: "the gate log on 1cdae69", who: "feature-builder / lead"}]
verdict: fix-first (F1)
</spec>
```

**Answers to the brief's four questions**

1. *Wrong delivery at exit 0.* Yes, in two ways. F1 (blocking): a card's aim `loop_seam` lifts the must F-08 ceiling. R1: a seam in the quiet part of a bed with a loud section is read against the loud part. I found no variant set that passes file by file but breaks D-03 as a set: every variant file, including the other members' variant files, enters `measures.parity`. I found no layer offset or resample that moves one channel only: `place` uses one offset for every channel, `resample_poly` runs on axis 0, and a planted 1-sample right-channel slip is caught.
2. *`form_checks` vs `targets`.* Every must row in `form_checks` goes into `must_failed` and the exit code, and the family check reads files, not rows. The one bypass is F1, where an aim target sets a must row's limit. Rank's one-shot view (R2) only gives wrong guidance; it never delivers a file, so it is not blocking.
3. *Refactors.* No behaviour change: I compared the old and new code line by line, and the render and rank test modules pass on 1cdae69.
4. *Loop calibration.* Both directions are guarded where it matters: the crossfade level ±2 dB, plus a gap and a click/HF reading. The readings hold from 0.5 to 30 s on steady beds. They are relative to the whole loop, not to the seam's own neighbourhood (R1), and the calibration beds are all steady.
