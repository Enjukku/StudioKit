---
type: job
scope: game
status: active
updated: 2026-10-23
source: J020-sound-workbench
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-23

# Review: soundbench steps 3-4, repair round 2 (364ab54), by reviewer

Depth: deep (it guards a paid-reveal rule, D-03). This is round 2 on these findings. The review is against the frozen revision 364ab54; the working tree has no changes under `tools/audio/soundbench` relative to it. All runs used copies of the 62 real takes and synthetic audio, in the session scratchpad. No repository file was written except this review.

Goal questions:
1. Can a paid-reveal family still pass D-03 (F-13 b within 1 LU, peaks within 1 dB) when its members differ in level? (F2, LD-a)
2. Does any guard or log that this round added show a correct-looking number for a wrong result? (F1, F3, F7)
3. Does any op still refuse in-range parameters on its own probe? (F4, F5)

```text
<spec>
artifact: tools/audio/soundbench@364ab54
reviewer: reviewer
looked_at_first: [git show 364ab54 (fxops, ops, render, intake, ffmpeg, measures, card, __main__), editor-design.md family rows, test_soundbench_render.py family tests, test_soundbench_realtakes.py]
findings:
  - {id: R2-1, class: blocking, where: "tools/audio/soundbench/render.py:157-190 (family_members: neighbours are collected only when they list this cue, line 164)",
     expected: "D-03 / F2: every member of a paid-reveal family is held to one level; a family cannot pass with a member left out",
     observed: "Four cue cards declare family id 'egg', paid_reveal true. COMMON and RARE list only each other; EPIC and LEGEND list only each other and are rendered 5 dB hotter (level target -15 vs -20). Renders: COMMON exit 3, RARE exit 0 pass, EPIC exit 3, LEGEND exit 0 pass. egg.family.json now says result pass, members [EPIC, LEGEND]: the other pair's pass was overwritten. The real F-13 b spread across the four 'egg' members is 5.0 LU (limit 1). Each pair is internally consistent, and no card lists a cue outside its own pair, so neither the member-set check nor the stranger check fires",
     evidence: "High (a paid-reveal guard bypassed at exit 0). Run: scratchpad r2/fam2.py with the test module's make_cue fixtures. Label: not verified in Studio (a tool run, reproducible)",
     smallest_fix: "In the neighbour scan, also collect every card whose family.id equals this card's id, and refuse (exit 2) when that card is not in `members`. The scan already loads every card, so this is about 2 lines",
     protect: "the existing one-sided, mismatched-declaration and stranger refusals; LD-a exit 3",
     retest: "the four-card case above: every render exits 2 until the cards declare one member set; then add a test for it next to test_a_card_listing_a_stranger_is_refused"}
  - {id: R2-2, class: recommendation, where: "tools/audio/soundbench/ops.py:559-564 (op_trim edge fade) vs ops.py:613 (FADE_IN_KEEP_SHARE)",
     expected: "a fade-in that leaves under 90 % of the attack share needs a `why` (ops.py:46, :613)",
     observed: "trim's new automatic 0.5 ms edge fade (F7 fix) changes the attack with no check and no `why`. Real takes with an attack (share >= 0.02) whose first sample is hot: thump-2.t2 attack share 0.081 -> 0.062 (76 %), hit-speed-1.t1 0.073 -> 0.065 (89 %), note-strength-1.t4 0.079 -> 0.070 (89 %). The trim log records the first-sample level but not the attack share, so the loss is silent",
     evidence: "Medium. Run: scratchpad r2/tr.py over all 62 real takes (8 edge-faded takes lose more than 10 % of their share; 3 of these have an attack). Not verified by ear",
     smallest_fix: "log attack_share before and after in op_trim, and apply the same 90 % / `why` rule to the edge fade (or shorten the fade until the rule holds)",
     protect: "F7: the delivered file still starts at 0 (the real-take test assertion)",
     retest: "thump-2.t2 through trim: refused without a `why` or under 10 % loss; the real-take test still passes"}
  - {id: R2-3, class: recommendation, where: "tools/audio/soundbench/fxops.py:257-260 (chorus full graph forced to timing=\"probe\") with ffmpeg.py:291-303",
     expected: "F4/F5: an op does not refuse in-range parameters on its own probe, whatever the audio",
     observed: "chorus with in_gain 1, out_gain 1, delay 100, decay 1, depth 0.1 (all inside SPEC) is refused on every real take with 'timing cannot be proven on the probe (second peak 0.9967)'. decay 0.9 with in_gain 0.5 is refused on thump-1.t2 (second peak 0.81). The dry path (decay 0) has already proven the timing on the audio, but the full graph's probe sees wet and dry copies of near-equal size and refuses. Settings with a weaker wet copy (decay 1 with in_gain 0.7, decay 0.8 with in_gain 0.7, delay 5 with depth 10) all passed",
     evidence: "Medium (a loud refusal, not a silent pass; it is the same class as F4). Runs: scratchpad r2/ch.py (3 parameter sets x 62 takes: the strong-wet set was refused on 62 of 62. Of the other two sets, one had no refusals and the other had 1, a balance-guard refusal on whoosh-1.t3, -2.44 dB, which is the guard reading the audio) and r2/ch2.py (decay sweep). Before this commit the same settings went to the probe too, because the audio gave no clear reading, so this is partly pre-existing; this round made the probe the only judge for chorus",
     smallest_fix: "either accept the dry-path timing as the proof for the full graph (they are the same filter), or refuse decay >= 0.9 x in_gain in check_params with a message that says why",
     protect: "the dry-path timing proof; the 2 dB balance guard",
     retest: "the strong-wet set on 5 real takes: accepted, or refused at parameter check with the reason"}
  - {id: R2-4, class: recommendation, where: "tools/audio/soundbench/ops.py:532 (saturate residual_db over the whole file)",
     expected: "a logged number tells the agent what the op did to the sound (F3: saturate must act on the body of a quiet take)",
     observed: "On 19 of 62 real takes (drive 12 dB) the logged residual reads -6 to -10 dB (heavy saturation), but outside +-10 ms of the peak the residual is -17 to -48 dB (thump-3.t2: logged -8.3, body -47.7). The relative-to-peak drive saturates the transient only; the body gets a nearly clean gain. A synthetic click on a quiet body (swish-3.t1 + one sample at 10x peak) shows the same: logged -8.4 dB, body -43 dB. The number is correct as defined, but it is the wrong number for the question 'did the body saturate?'",
     evidence: "Low. Runs: scratchpad r2/sat.py and r2/click.py. compress is not affected: its log (threshold_dbfs, deepest_gain_reduction_db 0.0 on the click take) tells the truth",
     smallest_fix: "also log the residual outside the transient region (from F-01 to 10 ms after the main transient, as LIMIT_TRANSIENT uses), or name residual_db 'whole file' in the README",
     protect: "the scale invariance that the real-take test checks",
     retest: "thump-3.t2: both numbers logged and they differ"}
keep:
  - "F1 denoise: default nf = the take's tail floor; nf above floor + 3 dB is refused. With nf left at its default on all 62 real takes, including the 13 whose 'floor' is the sound's own tail (sound_reaches_end), nr 12 and nr 60 both pass with a worst 10 ms window -1.5 dB and 0.0 dB on the last third of the sound. nf = floor + 3 at nr 60 is the same. The level, length and balance guards hold"
  - "F1 on added noise: white noise at -60 / -50 dBFS is lowered 4-8 dB at the default nf; one run, thump-4.t1 + -50 dBFS noise, was refused by the length guard (140 -> 100 ms). That is a guard firing, not a silent loss"
  - "F2: one-sided, mismatched id / paid_reveal / member-set and stranger cases are refused before any audio; the re-render-louder sequence fails exit 1 from either member"
  - "LD-a exit 3 and its precedence (1 over 3); LD-b intake on stated vs decoded length with the requested length only logged (62 takes decode within tolerance)"
  - "F3: compress and saturate are scale-invariant; compress logs the truth on a click-dominated take"
  - "F4: stretch at 0.8-1.25 accepted at 0 and -30 dB on a noise bed (ambience) and the sustained stand-in; the refusals seen on a tone pad (0.95, an event moved 5.1 ms on the audio) and on rough_tone (roughness rise) are guards reading the audio, not the probe"
  - "F6: the catch-all in __main__.py returns 2 for any unexpected error; card.targets and family.id are now type-checked"
  - "F7: every real take renders starting at 0 (the lead's run)"
weakest_part: "The family check has to scan the cue folders to find all members; R2-1 shows the scan is keyed on who lists whom, not on the family id"
could_not_check:
  - {step: "stretch / pitch on real sustained takes", missing_input: "the real set has no sustained, ambience or loop kind; synthetic material only", closes_it: "2-3 real ElevenLabs ambience or bed takes run through the stretch sweep", who: "sound-designer"}
  - {step: "audibility of the R2-2 attack loss and the R2-4 body saturation", missing_input: "listening (the AI cannot hear)", closes_it: "owner A/B at G3", who: "owner"}
  - {step: "planted-fault result 142/144", missing_input: "the qa-lead's run log", closes_it: "the log, or one planted fault in a scratch copy", who: "qa-lead"}
verdict: fix-first
</spec>
```

Non-blocking one-line note: the denoise refusal text rounds the floor (fxops.py:203). On hit-speed-1.t2 it reads "nf -64.2 dBFS is above the take's measured tail floor -67.2 dBFS (+3 dB allowed)", which looks like it is inside the limit; the unrounded floor is -67.23. Print the floor to 2 decimals or print the limit itself.
