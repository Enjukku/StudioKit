---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer sound-designer · claude-opus-5-5 · high · 2026-10-22

# Review: sound-designer books, rebuild round 3 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/sound-designer.md (body) + .agents/skills/sound-design/ (SKILL.md, references/), working tree on top of df13ff4 after repair round 2, 2026-10-22 (files changed after rev2: SKILL.md, craft-process.md, emotion-recipes.md, review.md, roblox-audio.md, worked-examples.md)
reviewer: J018 reviewer sound-designer (opus, high)
looked_at_first: [
  role file body, SKILL.md, review.md, craft-process.md, worked-examples.md, roblox-audio.md read in full; F-13 uses grepped in every book file,
  my round-1 and round-2 reviews, every finding re-checked against the files,
  roblox-creator-docs: Instance.yaml:2329-2345 (DescendantAdded: "parenting an object to the Instance will fire the event"),
  universal-principles.md sound lines (UP-01..UP-20), matrix.md sound column (96 IDs, script), animation-design game-timing.md:44 and review.md:139,
  tools: clip_check.py --help, shotlist.py log-diff --help and the drill fixture run (signed column +12.000 ms); Studio: list_roblox_studios returned no instance,
  V3 runs of F-13 b exactly as review.md:131 writes it (scratchpad sound-rev3/f13b.py, f13b2.py, f13b3.py; pyloudnorm, numpy 2.4.6, scipy 1.17.1, soundfile 0.14.0),
  sound-design/evals/briefs.md brief 5 (obby checkpoint and fail; read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: B1, class: blocking, check: C8 V3 + C3 (the paid-reveal guardrail measure fails a correct design with no error),
     where: ".agents/skills/sound-design/references/review.md:131 (F-13 b 'window = 400 ms, or the shortest compared file's length if shorter'); used by review.md:75 (R-31), SKILL.md:122 (D-03), worked-examples.md:51, :53",
     expected: "F-13 b compares the results' sound, so trailing silence in a delivered file does not change the verdict. The maker's own round-2 run showed why the window must follow the shortest result: a fixed 400 ms window reads an honest longer result about 3 LU louder and pushes the agent to quieten the rarer result",
     observed: "The window is set from the file length. Nothing in the books removes trailing silence: R-20 checks only the onset, R-22 passes a file that ends below -40 dB and then carries silence, and F-12 itself says 'silence padding counts'. Generated and exported files often carry trailing silence. With padded files the window grows back toward 400 ms and the hole the maker closed opens again. R-31 is a guardrail line (D-03; SC-16 never bends it), so the owner cannot pass it at check-in, and the agent is pushed to make the rare result quieter than the common one",
     evidence: "V3 (f13b2.py): honest pair, common 120 ms note, rare 240 ms two notes (same level): unpadded F-13 b diff 1.09 LU (the higher note's K-weighting); both files with 100 ms trailing silence: window 0.22 s, diff 3.29 LU (FAIL); with 300 ms: window 0.4 s, diff 3.59 LU (FAIL). Honest egg-style pair (click + 300 ms body vs + extra note + tail): 0.50 LU unpadded, 1.59 LU (FAIL) with 250 ms trailing silence on both. After trimming each file to its sound (f13b3.py) the padded pair reads 1.09 LU again, the same as unpadded. The round-2 trap (3 dB louder body + 600 ms tail) still fails at 2.99 LU (unpadded) and 3.12 LU (padded): B1 of round 2 stays fixed",
     smallest_fix: "review.md:131 F-13 b Compute: start with 'trim each result to its sound (F-01 onset to the F-04 end point) before measuring; ' and change the window to 'the shortest trimmed result's length'. Wrong-number cell (b): add 'trailing silence makes the window longer and fails an honest longer result by up to about 3 LU: trim first'"}
  - {id: R1, class: recommendation, check: C8 V3 (an error on some lengths),
     where: ".agents/skills/sound-design/references/review.md:131 (F-13 b `Meter(rate, block_size=window)` with window = the shortest file's length)",
     expected: "The measure runs on every length",
     observed: "When the window equals a file's length, pyloudnorm's length check (`data.shape[0] < block_size * rate`) fails for some sample counts because of float rounding, and it raises 'Audio must have length greater than the block size'. This is an error, not a wrong number, but the agent may mark R-31 NOT RUN or patch the code itself",
     evidence: "f13b.py / f13b3.py: 33 of 492 lengths between 1,000 and 19,200 samples raise ValueError with block_size = n/rate (for example n = 1,629, 1,777, 3,294); with block_size = (n - 1)/rate there are no errors, and where both ran the results differ by at most 0.014 LU",
     smallest_fix: "F-13 b Compute: 'block_size = (window samples - 1) / rate (float rounding otherwise raises on some lengths)'"}
  - {id: R2, class: recommendation, check: C8 V3 + C4 (the pooling counter can fail correct pool code),
     where: ".agents/skills/sound-design/references/roblox-audio.md:107 (§G 'Pooling (creation counter)'); review.md:84 (R-40)",
     expected: "The counter counts AudioPlayers created during the burst, not pooled players re-used",
     observed: "The counter counts game.DescendantAdded events. The docs say the event fires whenever an object is parented into the instance, so a pool that parks idle players at nil and parents them again on use fires it on every play. S-224 lists 'parent' among the fields a pooled player resets, so the book allows that pattern. Then the count is above 0 for correct code (a false FAIL with no error). The same counter also counts the default character Sounds that the engine creates when a character spawns during the burst",
     evidence: "Instance.yaml:2333-2337 ('parenting an object to the Instance will fire the event for this object and all of its descendants'); roblox-audio.md:46 (S-224 'parent'). Not run: no Studio connected (list_roblox_studios returned an empty list)",
     smallest_fix: "§G pooling row: 'count only new instances: keep a weak-keyed set of every AudioPlayer and Sound seen during warm-up and count the ones not in it; ignore Sounds under a character model'. R-40 needs no change"}
  - {id: R3, class: recommendation, check: C8 V10 (for the lead; carried from round 1 R6),
     where: ".agents/skills/animation-design/references/game-timing.md:44; animation-design/references/review.md:139 (G-04)",
     expected: "Partner books agree now that the sound window is aligned",
     observed: "Both lines still say that the sound book's window is wider and that the offset is reported as MEASURED until it is aligned. The sound book is aligned (SKILL.md:107 S-133)",
     evidence: "the two lines; proposals/sound-designer.md:33 (the row for the lead is present)",
     smallest_fix: "The lead deletes the 'until it is aligned' clause in both animator lines (not the sound maker's files)"}
keep: [
  "round-2 fixes that hold: F-13 split into (a) integrated, padded to one length, for options and siblings, and (b) momentary maximum for paid results, with the tail hole, the fixed-window hole and the short-burst residual named in the wrong-number cell; R-31, D-03 and worked example §4 all use F-13 b",
  "R-34 scoped to threat hits and attacks against friendly one-shots; tells, warnings, charges and build-ups excluded (agrees with S-76, R-09, R-28; SC-11 and §7 #5 say the same)",
  "pooling check rebuilt as a creation counter plus a grep for Instance.new outside the pool module, with a probe clause for the first use; the before/after count is gone",
  "worked example §2: the T2 bag-full event gets a 150-300 ms confirm (S-194 tier B), and the R-15 check compares against it",
  "earlier keep items: the 'You cannot hear' frame with input codes on every line; check-ins A/B/C with goal questions and budgets; stage sheets on event ids; attempt/outcome split; the F table with a 'wrong number with no error' column found by real runs; R-43 log-diff read from the signed column without --tol-ms; the identity sheet and the partner table; Doppler and distance-curve lines that match the docs mirror"
  ]
verdict: fix-first
</spec>
```

## Earlier findings: fixed or open

| Id | Now |
| --- | --- |
| rev1 F1 R-31 measured RMS | fixed (rev2 B1 then rev3 check: F-13 b) |
| rev1 F2a Doppler, F2b distance curve | fixed (roblox-audio.md:52, :108; SKILL.md:93; R-16) |
| rev1 F3 five missing checks | fixed (R-22, R-33, R-34, R-35, R-62, check-in B reference) |
| rev1 R1 D-07 wording | fixed (SKILL.md:126) |
| rev1 R2 DC offset, F-10 band | fixed (review.md:113-115, :128) |
| rev1 R3 sync copies | fixed (numbers only in S-133; R-43, R-54 keep the signed bounds) |
| rev1 R4 wiring self-check | fixed (R-40) |
| rev1 R5 same-wave rows | fixed (coverage V11 tables) |
| rev1 R6 animator books | open for the lead: R3 above |
| rev1 R7 SKILL size | fixed (§1-§5 end at 19,157 bytes) |
| rev1 R8 evals 3.5 | proposals evals row (d) present |
| rev2 B1 F-13 tail hole | fixed: the trap fails at 2.99 LU and honest results pass when unpadded. The new window rule has a padding hole: B1 above |
| rev2 B2 pooling count before/after | fixed (creation counter + grep); the counter needs a re-parent clause: R2 above |
| rev2 B3 R-34 scope | fixed (review.md:78) |
| rev2 R1 bag-full sized like a milestone | fixed (worked-examples.md:27, :29, :35) |
| rev2 R2 evals 4.2, 4.3 | proposals evals row (e) present |
| rev2 R3 coverage citation | fixed (coverage :276 cites :450) |

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | pass (96 rows checked, 0 failed this round) | Script: all 96 tagged IDs have a row; 22 untagged rows and the 5 rejections keep sound reasons. Rounds 1-2 opened every landing. This round I re-opened the landings changed after rev2 (GD-35, SS-05, GD-02, VR-24, SD-21, SD-28, WT-02, SD-18): each carries its rule and its check. GD-35's check has the B1 hole, which I count under C3 and C8, not as a missing landing |
| C2 core principles | pass | §7 has 20 rows, each stated for sound with an example and a check. #5 now says "threat hits", which agrees with UP-05's sound line. No contradiction with the master |
| C3 self-review | fail | B1: R-31 fails honest paid results when the files carry trailing silence |
| C4 kit rules and engine | pass (one rec.) | Doppler, distance curves, DescendantAdded, execute_luau on the Client data model match the docs; clip_check --timing and shotlist log-diff are real modes; R2 is a counter detail |
| C5 nothing valuable lost | pass | All 48 S- and D- ids of the old SKILL.md are still defined (script). The old self-check items (wiring, device matrix, A/B pairs) are kept in R-25, R-40, R-65 and the check-ins |
| C6 fixed rules | pass | Frontmatter byte-identical to df13ff4. SKILL.md has 205 lines; the description has 328 characters. Headings: only the §3 retitle and the appended §7 and roblox-audio §G. The J018 phrase is in every book file. No Riot names, library ids or transcript lines in the bodies; no tips section; evals/ and evidence/ unchanged |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 | V1 pass. V2 pass. V3: B1 (padding), R1 (pyloudnorm error on some lengths), R2 (re-parenting). V4 pass (D-03, D-07, S-165, S-166, S-172 defer to platform-policy; S-228 keeps asset ids and gains off client requests). V6 pass. V7 pass (19.2 KB to §6; re-read rule after compaction). V8 n/a (craft role; brief asks and partner table present). V10 pass, except the animator lines the lead owns (R3). V11 pass (the marketing and art-director rows are recorded or do not touch these books) |

## Will an agent make better work with these books?

Yes. I read eval brief 5 (obby checkpoint and fall sounds, retried dozens of times) as the agent would.

With the old books the agent had a rule table, a genre preset and a cue card. It would pick sounds from rules and write a "listening-test plan" it could not run. With the new books it does these things:
- It frames both cues by job, emotion and rate.
- It keys the checkpoint chime to the confirmed checkpoint event and locks its sound (meaning never varies).
- It gives the fall cue variants, jitter and a contact cooldown, and checks that the cue decays fast (R-22).
- It keeps the fall cue below the reward tier and makes success and fail differ.
- It measures every file and asks the owner goal questions at check-ins instead of claiming it listened.

Weak spots:
- The paid-reveal parity line fails honest results when the files carry trailing silence (B1). The fix is one clause.
- The workflow has eleven steps and three check-ins for every job. A two-cue job like brief 5 gets lighter only through the short card and "minor cues picked by numbers". The maker declined to change this in round 2, with a reason. I agree it is not a defect.
- The always-loaded text (role file + SKILL.md) is about 38 KB.

The only blocking fix is one clause in review.md:131.
