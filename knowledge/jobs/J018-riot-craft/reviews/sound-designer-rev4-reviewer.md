---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer sound-designer · claude-opus-5-5 · high · 2026-10-22

# Review: sound-designer books, repair round 3 (J018 stage 3, review round 4)

```text
<spec>
artifact: .agents/roles/sound-designer.md (body) + .agents/skills/sound-design/ (SKILL.md, references/), working tree on top of df13ff4 after repair round 3, 2026-10-22 (files changed after rev3: SKILL.md, references/review.md, references/roblox-audio.md)
reviewer: J018 reviewer sound-designer (opus, high)
looked_at_first: [
  my round-3 review; review.md §4 (F-01 to F-13), R-08, R-31, R-40; SKILL.md D-03; worked-examples.md §4; roblox-audio.md §G pooling row and S-224,
  my own F-13 b, F-12 and F-09 written from the book text (scratchpad sound-rev4/f13b4.py, f13b4b.py, f13b4c.py, f09.py, hyb.py; pyloudnorm, numpy 2.4.6, scipy 1.17.1, soundfile 0.14.0), run on WAV files written and read back,
  the maker's round-2 sample files (sound-designer-r2/*.wav), the maker's recipe script for its channel handling only,
  Studio: list_roblox_studios returned no instance
  ]   # the maker's "Repair round 3" coverage note was read after this
findings:
  - {id: B1, class: blocking, check: C8 V3 + C3 (the paid-reveal guardrail measure still fails a correct design with no error),
     where: ".agents/skills/sound-design/references/review.md:131 (F-13 b: 'window = 400 ms, or the shortest trimmed result's length if shorter'); review.md:130 (F-12 sound end: 'the last sample at or above the peak minus 40 dB'); review.md:127 (F-09 uses the F-12 sound); used by review.md:75 (R-31), SKILL.md:122 (D-03), worked-examples.md:51, :53",
     expected: "The round-3 fix makes the verdict independent of what follows the result's body. The book's own wrong-number cell (b) says an honest longer result at the same level must not read about 3 LU louder",
     observed: "The trim removes digital silence only. The window still follows each result's quietest end, and low-level sound after the body sets that end: a noise floor under the trailing part (generated and recorded files) or a reverb or decay tail. Then the window grows back toward 400 ms and the honest longer result fails R-31 again, a guardrail line that SC-16 cannot bend. The maker tested a -70 dBFS floor only. The F-12 end is per sample, and Gaussian noise peaks about 12 dB over its RMS, so a floor about 50 dB under the peak already reaches the -40 dB threshold. The same end point moves F-09: a variant of one sound with a noisy tail reads 3 dB quieter, a false FAIL of R-31's +/-1 dB",
     evidence: "f13b4.py, f13b4c.py (book recipe, all channels, WAV round trip). Round-3 short honest pair (120 ms 880 Hz vs 880 + 1,320 Hz, peak -1 dBFS, 300 ms trailing part): noise floor -70 / -60 / -55 dBFS RMS: 1.09 LU (the K-weighting difference the cell names); -50 dBFS: window 400 ms, 3.59 LU (FAIL); same pair at peak -12 dBFS with a -60 dBFS floor: 3.59 (FAIL). Reverb: one pluck (150 ms) vs three equal plucks, dry: 0.00 (pass); the same reverb at -30 / -25 dB wet on both: 0.00; at -20 dB wet on both: window 244 ms, 2.80 LU (FAIL). One identical, quiet reverb flips the verdict by 2.8 LU. F-09 (f09.py): 200 ms 440 Hz variant with 300 ms trailing part, clean -4.05 dBFS, -60 dBFS floor -4.05, -50 dBFS floor -7.06 (sound length 488 ms, 3 dB lower). Every round-3 case still runs as the maker reports (egg honest 0.50, egg trap 2.99, r2 trap 2.64, short loud 2.52; padding with digital silence changes nothing). Block size (n-1)/rate: 0 errors on 1,466 lengths at 22.05, 44.1 and 48 kHz",
     smallest_fix: "F-13 b Compute: 'window = 100 ms, or the shortest trimmed result's length if shorter'; wrong-number cell (b): 'a window that follows a result's length grows with a noise floor or a reverb tail and fails an honest longer result by about 3 LU: keep it at 100 ms'. Tested on every case above (f13b4c.py, 'fixed100'): noise floor -50 dBFS 1.08, reverb -20 dB 0.00, short honest 1.08, egg honest 0.51, r2 honest -0.10, egg trap 3.00, r2 trap 2.19, short loud 2.37 (the traps still FAIL). The 30 ms square burst then reads 1.22 instead of 0.81 (the dense-burst residual gets smaller: update that clause). For F-12 and F-09: end the sound at the last 10 ms window whose RMS is within 40 dB of the loudest (as F-04), then at the last sample at or above the peak minus 40 dB inside it; tested (hyb.py): the -50 and -45 dBFS floors then give 120 / 240 ms sounds and 1.09 / 1.00 LU, and it adds no 10 ms grid error. Name the floor limit in the F-12 cell (a floor within about 42 dB of the loudest window still reaches the file end)"}
  - {id: R1, class: recommendation, check: C8 V3 + C4 (the pooling counter gives a wrong verdict for two common code shapes),
     where: ".agents/skills/sound-design/references/roblox-audio.md:107 (§G 'Pooling (creation counter)'); review.md:84 (R-40)",
     expected: "The counter reads 0 for every correct pool and above 0 for create-per-play code",
     observed: "(a) New in this round: the counter skips every instance 'under a model that holds a Humanoid'. Enemy and NPC models hold Humanoids, so per-hit Sounds or AudioPlayers created at the hit target escape the counter (false PASS). The grep half checks only Instance.new(\"AudioPlayer\"), so Instance.new(\"Sound\") at an NPC escapes both halves. (b) From before: the warm-up plays each cue once. A pool that grows on demand (take a free player, else create one) then creates players during the burst until it reaches the burst's overlap, and the counter fails correct code (false FAIL)",
     evidence: "The row text: 'not under a model that holds a Humanoid (the engine's default character Sounds)'; 'play each cue once (warm-up)'; S-149 and S-224 do not require a pre-filled pool. Not run: no Studio connected (list_roblox_studios returned an empty list)",
     smallest_fix: "§G pooling row: 'warm-up = one 10 s burst at the real top rate; count during a second burst'; replace the Humanoid clause with 'not under a player character (Players:GetPlayerFromCharacter) and created at its spawn', or 'no character spawns during the burst' and drop the clause; R-40 (G): grep Instance.new(\"AudioPlayer\") and Instance.new(\"Sound\")"}
keep: [
  "round-3 B1 fix in every listed place: F-13 b trims to the F-12 sound (review.md:131); F-12 defines file and sound length (review.md:130); R-08 uses the sound length (review.md:48); D-03 tail limit uses the shortest result's F-12 sound length (SKILL.md:122); R-31 and worked-examples.md §4 name F-13 b; digital trailing silence no longer moves F-13 b or F-09 (my runs: 1.09 / 1.09 / 1.09 for 0 / 100 / 300 ms; egg pairs equal padded and unpadded)",
  "round-3 R1 fix: block_size = (window samples - 1) / rate with its reason; no errors on any length or sample rate I ran",
  "the maker's same-kind search: F-09 on the sound, length checks on the sound, F-13 a checked and left as is (its padding to one length is right)",
  "the F-13 cell now names the K-weighting register effect as a true difference and the remaining dense-burst residual",
  "pooling row: the weak-keyed set of instances seen before the burst fixes the re-parent false FAIL of round 3",
  "earlier keep items stand (rev3 keep list)"
  ]
verdict: fix-first
</spec>
```

## Earlier findings: fixed or open

| Id | Now |
| --- | --- |
| rev3 B1 F-13 b window follows the file length | fixed for digital silence (review.md:131). Low-level sound after the body (noise floor, reverb tail) reopens the same hole: B1 above |
| rev3 R1 pyloudnorm raises on some lengths | fixed (review.md:131 block size) |
| rev3 R2 pooling counter counts re-parents | fixed (weak-keyed set). The new Humanoid clause and the one-play warm-up give wrong verdicts: R1 above |
| rev3 R3 animator lines (lead) | open for the lead: animation-design/references/game-timing.md:44 still says "until it is aligned" |
| rev1, rev2 findings | closed as listed in rev3; nothing in this round reopens them |

## Checks on this round

| Check | Result | Note |
| --- | --- | --- |
| Fix in every listed place | pass | F-13 b, F-12, F-09, R-08, D-03 changed; R-31 and worked-examples §4 point to F-13 b and inherit the trim |
| Own runs on real input types | fail (B1) | The fix holds for digital silence, WAV/OGG/MP3/FLAC (the maker's runs) and mixed sample rates (44.1 vs 48 kHz: 1.09, same as 48/48). It fails for a noise floor about 50 dB under the peak and for a quiet reverb tail on the results. Stereo: the book does not say mono or all channels; with a 0.5 ms Haas second note the mono sum reads 1.1 LU lower than the channels. The maker's recipe uses the channels, so I count it as a wording point inside B1's fix, not a finding |
| No new conflict with the fixed list | pass | Changed in this round: SKILL.md, review.md, roblox-audio.md, coverage and proposals only. Role and SKILL.md frontmatter identical to HEAD. SKILL.md 205 lines, description 328 characters. Headings unchanged, no renumbering. No Riot names, library ids or citations in the changed body lines (the J018 phrase in the author lines only). evals/ and evidence/ unchanged |

## What still gives a wrong number with no error

- A noise floor or a reverb tail after the result's body sets the F-13 b window (B1). This is the main remaining hole, and generated reward sounds often carry both.
- In F-12 and F-09, a noise floor within about 50 dB of the peak moves the sound's end to the file end (B1, second part).
- A stereo result measured as a mono sum can read up to the R-25 mono drop (3 dB) quieter than the player hears. Say "all channels" in F-13 b.
- Pooling: a pool that grows on demand fails, and per-hit sounds created under NPC models pass (R1).
