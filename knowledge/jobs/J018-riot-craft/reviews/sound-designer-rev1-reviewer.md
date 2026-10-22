---
type: job
scope: universal
status: active
updated: 2026-10-22
source: J018 stage 3
supersedes: []
---
> Author: J018 reviewer sound-designer · claude-opus-5-5 · high · 2026-10-22

# Review: sound-designer books, rebuild round 1 (J018 stage 3)

```text
<spec>
artifact: .agents/roles/sound-designer.md (body) + .agents/skills/sound-design/ (SKILL.md, references/ incl. new craft-process.md, review.md, worked-examples.md), working tree on top of df13ff4, 2026-10-22
reviewer: J018 reviewer sound-designer (opus, high)
looked_at_first: [
  role file body, SKILL.md, review.md, craft-process.md, worked-examples.md read in full; git diff df13ff4 of every other reference (cue-card, roblox-audio, mix-and-loudness, repetition, reward-and-juice, horror-and-tension, emotion-recipes, elements, ai-generation-prompts, craft-satisfying, genre-presets, glossary); old SKILL.md §3-§5 and old role body walked line by line,
  knowledge/reference/craft/riot/universal-principles.md (master, UP-01..UP-20, every 'sound:' line),
  matrix.md sound column (96 IDs, script-extracted), sound.md SD-01..SD-33 and the principle/apply/check/roblox_fit of the 63 other tagged findings (script-extracted from the topic files),
  roblox-creator-docs: SoundService.yaml:140-200, AudioEmitter.yaml (member list, :107-200, :349-378), AudioListener.yaml (:106-134, :287), Humanoid.yaml:360-375, audio/effects.md:1-40 and section list, animation/events.md:12,47,
  platform-policy/references/rules.md §A, §D; game-design/references/principles.md §7; animation-design game-timing.md and review.md; vfx-design SKILL.md and sync rows; environment-design ambience.md; templates/environment/ambience-map.md,
  tools: tool-modes.md, tools/film/shotlist.py:1150-1200 (log-diff), tools/anim/clip_check.py (run),
  sound-design/evals/briefs.md briefs 1-3 (read as the agent would)
  ]   # the maker's coverage and proposals files were read after this
findings:
  - {id: F1, class: blocking, check: C8 V3 + C3 (the paid-reveal guardrail),
     where: ".agents/skills/sound-design/references/review.md:75 (R-31) and :123 (F-09); worked-examples.md:51, :53",
     expected: "SKILL.md:126 D-03: paid-reveal results differ 'never by peak level or short-term loudness (within 1 LU)'. The self-review line that proves it must measure loudness and peak, and must not pass a louder result",
     observed: "R-31 checks only F-09, which is plain RMS of the loudest 400 ms window (review.md:123 itself says never to call it LUFS), 'within 1 dB'. Plain RMS has no K-weighting, so a brighter result is louder by several LU at the same RMS; and no line compares the results' peaks. Worked example §4 repeats 'within 1 dB, F-09'. The wrong number comes with no error, on the one line that guards the honest-reveal rule",
     evidence: "V3 run (scratchpad sound-reviewer-v3/sound-reviewer-measure.py, soundfile 0.14.0, numpy 2.4.6, scipy 1.17.1, pyloudnorm): two 1.2 s result sounds with the same envelope, 220 Hz vs 3,520 Hz: F-09 -16.05 vs -16.05 dBFS (R-31 PASS), integrated loudness -21.28 vs -17.15 LUFS (4.1 LU apart, D-03 broken). A result with a 3 ms click added: F-09 within 0.1 dB of the plain one (PASS), sample peak -6.0 vs -10.5 dBFS (4.5 dB louder peak, D-03 broken). pyloudnorm measured a 0.40 s file without error",
     smallest_fix: "R-31 second clause: 'paid random reveal results: integrated LUFS (pyloudnorm; pad every result with silence to the same length of at least 0.4 s) within 1 LU of each other, and sample peaks (F-03) within 1 dB'. F-09 'wrong number' cell: add 'RMS has no K-weighting: two files with equal RMS can differ by 4 LU when their spectra differ; use LUFS for any loudness-parity check'. worked-examples.md:51 'all results within 1 LU and 1 dB peak'; :53 'R-31 (results within 1 LU, LUFS; peaks within 1 dB)'"}
  - {id: F2, class: blocking, check: C4 (engine claims) + C8 V3 (Studio check gives a wrong answer with no error),
     where: "(a) references/roblox-audio.md:52 Doppler row and SKILL.md:93 SC-10; (b) references/roblox-audio.md:107 (§G 'Distance curves') used by review.md:56 R-16",
     expected: "(a) Engine claims match the docs mirror. (b) A Studio inspection that marks a line MCP-verified reads the value the engine really uses",
     observed: "(a) The row says 'the docs do not say whether audio-graph emitters get Doppler' and cites SoundService.yaml:178-190. Four lines further the same entry says the opposite: DopplerScale 'does not impact the behavior of instances in the advanced audio system, such as AudioPlayer or AudioEmitter', and no AudioEmitter or AudioListener member mentions Doppler. SC-10 sends the agent to probe for something the docs already answer, and leaves the travel-loop design open in the wrong direction (a projectile on a graph emitter gets no engine pitch shift). (b) §G reads only AudioEmitter:GetDistanceAttenuation(). The docs say this returns the custom curve even when DistanceAttenuationMode is a preset, and the engine then ignores that curve and uses DistanceAttenuationBounds. An empty table means the default curve. The AudioListener has its own distance curve that also applies. A preset-mode emitter with an old custom curve therefore 'matches the card' while the real roll-off is different: a false MCP-verified pass on R-16",
     evidence: "SoundService.yaml:194-195 (Doppler note); AudioEmitter.yaml member list (no Doppler); AudioEmitter.yaml:135-160 (Bounds, preset only), :167-185 (DistanceAttenuationMode: custom curve 'is ignored' unless Custom; default Custom), :349-365 (GetDistanceAttenuation: 'always returns the custom curve ... regardless of the current DistanceAttenuationMode'; empty table = default curve); AudioListener.yaml:106-120, :287 (listener curve). Not run in Studio: no connected Studio (the maker reports the same)",
     smallest_fix: "(a) roblox-audio.md:52: 'Doppler: SoundService.DopplerScale applies to legacy Sound only; the docs say it does not affect AudioPlayer or AudioEmitter (SoundService.yaml:194-195), and the graph classes have no Doppler property. Assume no engine Doppler on graph emitters: a travel loop that needs a pitch pass-by gets it from a scripted PlaybackSpeed change or accepts none; probe only to confirm.' SC-10's bracket: '(graph emitters get no engine Doppler: roblox-audio.md §B)'. Proposals row 'library sound.md' (c): same wording. (b) roblox-audio.md:107: 'read DistanceAttenuationMode; if Custom, the GetDistanceAttenuation() keys (empty table = the default curve); otherwise DistanceAttenuationBounds and the mode; also the AudioListener's GetDistanceAttenuation(), which applies as well; compare with the card's studs'. Add 'a preset mode ignores the custom curve' to R-16"}
  - {id: F3, class: blocking, check: C1 + C3 (5 checkable findings landed as a rule without a self-review line),
     where: "SD-28 (craft-process.md:89 points to review.md §2, which has no reference; no R-line); SD-21 sibling distinctness (SKILL.md:94 SC-11 rule; review.md:53 R-13 checks 'named and present' only); SS-05 (SKILL.md:94 'sharp transients for threats, soft attacks for friendly'; no R-line); WT-02 (craft-process.md:60 S-82 pitch per size class; no R-line); GD-02 celebration length (reward-and-juice.md:29 S-194 'under about 2 s'; no R-line)",
     expected: "Owner: 'Turn every checkable finding into a line in the role's self-review'. Each of these checks can be run with the agent's own inputs: F-measures of the reference file beside the pick, F-10 and F-06 between sibling signatures, F-02 minus F-01 (onset to peak) on threat vs friendly cues, F-10 steps across size tiers, F-12 of an in-play celebration, plus one check-in question where only a listen can tell",
     observed: "The rules are in the books and are correct; the checks are not. The coverage table lists SD-28 as 'rv R-61' (stand-ins only) and SS-05 and WT-02 as 'standard / core principle'. It is honest that there is no check for these, but the owner's rule asks for one. craft-process.md:89 'Pick against the card and the category reference (review.md §2)' is a dead pointer: §2 has no reference row",
     evidence: "library checks: SD-28 'A/B listen against the category reference is logged'; SD-21 'each signature is distinct in pitch and timbre'; SS-05 (sound mapping) 'sharp transients vs soft attacks'; WT-02 'compare ... against the declared values; flag outliers'; GD-02 'the celebration ... ends before the player's next decision (measure its length)'; grep of review.md for 'reference' finds only R-62 (real-world references for a new setting)",
     smallest_fix: "Append clauses (about 5 short lines): R-62 '+ the pick's F-01..F-10 are listed beside the category reference's (identity sheet References row)'; review.md §2 row B 'plus the category reference, loudness-matched, after the options'; R-13 '+ sibling signatures differ: F-10 note at least 3 st (P) apart or a different main band (F-06); at check-in C: \"all weapons in sequence: is each one distinct?\"'; R-12 '+ threat cues have a shorter onset-to-peak (F-02 minus F-01) than friendly cues in the same scene'; R-15 '+ size tiers of one family step in pitch by the S-82 interval (F-10), the same step in every family; an in-play celebration lasts at most about 2 s (P) (F-12)'"}
  - {id: R1, class: recommendation, check: C8 V4,
     where: "SKILL.md:130 D-07; references/reward-and-juice.md:64 (S-164 last sentence)",
     expected: "platform-policy/references/rules.md §A row 9: a player with ArePaidRandomItemsRestricted MUST NOT use the generator; Roblox changes the region list centrally (never hard-code it). Roblox gives the game no under-13 flag for paid rolls; PolicyService decides",
     observed: "'No countdown tension or jackpot siren on paid rolls for under-13 or restricted-region players' reads as if restricted players still roll and as if the game sorts players by age or region. This is stricter, not looser, so it is not a policy break, but it points the agent toward an age or region branch that platform-policy forbids",
     evidence: "rules.md §A (ArePaidRandomItemsRestricted row), §D row 59 (PolicyService for younger players)",
     smallest_fix: "D-07: 'No countdown tension or jackpot siren on any paid roll; restricted players never reach one (ArePaidRandomItemsRestricted, platform-policy).' S-164 last sentence: point to D-07"}
  - {id: R2, class: recommendation, check: C8 V3 (more wrong-number cases with no error),
     where: "references/review.md:109-126 (§4 preamble, F-01, F-04, F-06, F-10)",
     expected: "The table lists each measure's wrong-number trap",
     observed: "Two traps are missing. (1) A DC offset (common in generated audio) makes F-01 report 0 ms, so a leading silence is hidden on non-hit cues, where only the onset is checked. It also inflates the below-cut share in F-06 and keeps F-04's ends_above flag on. (2) F-10 searches 60 Hz-4 kHz only, so a chime or sparkle with its fundamental above 4 kHz reports a noise peak as a note",
     evidence: "V3 run: 4 kHz tick + 0.02 DC: F-01 0.00 ms, below-300 Hz share 16.2 %, F-04 flag true; 5,274 Hz chime with -48 dB noise: F-10 = 606 Hz (D#5 -45 cents), no error",
     smallest_fix: "§4 preamble: 'subtract the mean of each channel first'. F-10 'wrong number' cell: '+ a fundamental above 4 kHz is outside the band: the reported note is noise; check that the peak stands at least 20 dB above the band median'"}
  - {id: R3, class: recommendation, check: C8 V6 + C7 (drift),
     where: "sync window numbers: SKILL.md:111 (S-133, the home), cue-card.md:33 and :88, review.md:84 (R-43), :94 (R-54), craft-process.md:33; attempt/outcome rule: SKILL.md:116, :206 (§7 #19), review.md:47 (R-07), craft-process.md:32-35, role file :58",
     expected: "One rule, one place; the other places point to it (V6)",
     observed: "The '0 to +40 ms, never more than one frame early' numbers are written out in 5 places, and the attempt/outcome rule in 5. They agree today; a later change to S-133 will leave copies behind (the animator's own books already show this: see R6)",
     evidence: "grep of '+40' and 'confirmed' across the books",
     smallest_fix: "R-54, R-43, cue-card field 22 and its example say 'inside the S-133 window' and keep only the signed bounds the check compares; craft-process.md:33 'S-133'"}
  - {id: R4, class: recommendation, check: C5,
     where: "SKILL.md:143-157 (§5) and review.md:81 (R-40) vs old SKILL.md §5 line 'Roblox wiring uses the audio graph, the Asset property, client playback for cosmetic SFX, pooled players'",
     expected: "Every old self-check line is kept or replaced by something at least as good (the coverage table, section c, says 'every old line kept ... wiring')",
     observed: "The new §5 and R-40 keep the graph. Client playback for cosmetic SFX, pooled AudioPlayers and the `Asset` property are no longer checked. The rules still exist (S-150 and the §1 deliverable item 6), but nothing checks them",
     evidence: "git show df13ff4:.agents/skills/sound-design/SKILL.md (§5, 9th item); SKILL.md:153",
     smallest_fix: "R-40: '+ cosmetic SFX play on the client from replicated events; one-shots come from pooled AudioPlayers that set `Asset` from the cue table'"}
  - {id: R5, class: recommendation, check: C8 V11 (same-wave rows, for round 2),
     where: "proposals/progression-designer.md:24, proposals/ui-ux-designer.md:30, proposals/environment-designer.md:36 (written in wave 2, in parallel with this maker)",
     expected: "V11 covers earlier waves only, so this is not a defect. These rows now exist, though, and are cheap to settle in round 2",
     observed: "Not handled: map the reward tiers to the progression tier table T1-T4 and read rates from it; a UI cue list template keyed to the UI designer's event names; read the ambience map's emotion per zone; a footstep refusal names the material to use instead. The S-133 rows from the film director and the VFX designer are already met",
     evidence: "the three proposal rows; craft-process.md:18-21 (ambience map row has no emotion); review.md:52 R-12, :54 R-14",
     smallest_fix: "Round 2: adopt or decline each row in coverage section d. Likely adopt: one line in craft-process.md §1 (emotion per zone; tier table T1-T4 as an input) and §8 (a refusal names the substitute material)"}
  - {id: R6, class: recommendation, check: C8 V10 (for the lead; not the sound maker's files),
     where: ".agents/skills/animation-design/references/game-timing.md:44; animation-design/references/review.md:139 (G-04)",
     expected: "Partner books agree once the sound window is aligned",
     observed: "The animator's books still say that sound-design's current window is wider and that until it is aligned the offset is reported as MEASURED. The sound book is now aligned (SKILL.md:111), so that sentence is out of date",
     evidence: "the two lines; SKILL.md:111",
     smallest_fix: "The lead deletes the 'until it is aligned' clause in both animator lines (the animator books are closed from wave 1)"}
  - {id: R7, class: recommendation, check: C8 V7,
     where: "SKILL.md §1-§5 (lines 1-157)",
     expected: "Steps, rules and self-check in about the first 5,000 tokens (about 18 KB)",
     observed: "§5 ends at 19,541 bytes, and the text has many multi-byte symbols (arrows, minus signs, multiplication signs), so the last self-check lines may fall past the 5,000-token cut. SKILL.md:19 tells the agent to re-read §1-§5 and §7 after a compaction, which covers the risk. The always-loaded text (role file + SKILL.md) grew from about 24 KB to 38 KB",
     evidence: "byte offsets measured; old SKILL.md 16,875 bytes, new 27,142; role file 7,011 → 10,767",
     smallest_fix: "Optional: move the 'Craft numbers' rows S-75 and S-78 (SKILL.md:106-107) to craft-satisfying.md, where the impact recipes already point. That gains about 0.4 KB of margin and moves no step"}
  - {id: R8, class: recommendation, check: C7 (evals, proposal only),
     where: ".agents/skills/sound-design/evals/briefs.md check 3.5 vs SKILL.md:91 SC-08 and craft-satisfying.md S-84 (rewritten)",
     expected: "The evals grade what the books now teach",
     observed: "Check 3.5 expects 'Dry assets + one engine reverb per space (S-84)'. The new books bake each sound's designed tail and glue, and keep only the room live. A grader could fail a correct answer",
     evidence: "evals/briefs.md 3.5; craft-satisfying.md S-84 row",
     smallest_fix: "Add to the evals proposal row (proposals/sound-designer.md:25): 'check 3.5: the room is not baked; the designed tail and glue are baked (SC-08)'"}
keep: [
  "the 'You cannot hear' frame: every check names its input (D, T, F, S, L, G, V, O-A/B/C), labels, could-not-check list (review.md §1)",
  "owner check-ins A/B/C with goal questions and budgets (review.md §2): solo then full mix, phone and headphones, busiest moment plus 10 s burst",
  "the file-measure table F-01..F-12 with a 'wrong number with no error' column, found by real runs (noise head, harmonic trap, cut tail, seam ratio, centroid window)",
  "R-43: log-diff read from the signed column, with --tol-ms forbidden for sync because it is symmetric (verified: shotlist.py:1174 compares abs)",
  "stage sheet keyed to the timing list's event ids; attempt cue at once, outcome layer only on confirmation; one sync rule shared with animation and VFX",
  "five layer jobs, the processing order with purpose per step, baked vs live split (SC-08) replacing the old 'dry assets' rule",
  "game sound identity sheet (signatures, forbidden list, sound-code table, footstep table) and the partner table with when to ask",
  "D-03 strengthened: one windup asset, rarity after the result, tap to skip, batch opens; S-166/S-172 deferred to platform-policy",
  "worked examples that show the step order and the checks that prove each step",
  "proposals for a cue_check.py tool and an asymmetric log-diff tolerance, with the V3 evidence"
  ]
verdict: fix-first
</spec>
```

## C1-C8 results

| Check | Result | Note |
| --- | --- | --- |
| C1 coverage | fail (5 of 96 rows) | All 96 tagged IDs have a row, and the 5 rejections have sound reasons. 91 landings were opened. The rule is there in all of them; the check is missing in SD-21, SD-28, SS-05, WT-02, GD-02 (F3). The 22 untagged rows used were spot-checked; all OK |
| C2 core principles | pass | §7 has all 20 UP rows, each stated for sound with an example and a check (input codes). No contradiction with the master. It sits after §6, and §1 says to re-read it after a compaction |
| C3 self-review | fail | F3 (5 missing lines); F1 (R-31 cannot prove D-03) |
| C4 kit rules and engine | fail | F2: the Doppler claim misreads SoundService.yaml:194-195; the distance-curve check misses DistanceAttenuationMode. No invented tool modes (shotlist cues/log-diff, clip_check verified). D-07 wording: R1 |
| C5 nothing valuable lost | pass (one rec.) | Every moved S-rule was found in its new home with the same text. S-73/S-74 lengths are in game-design §7. The old S-133 window was replaced by the agreed one. The wiring self-check item was dropped (R4) |
| C6 fixed rules | pass | Role frontmatter byte-identical to df13ff4. SKILL.md has 207 lines; the description has 328 characters. No section renumbered (§3 retitled; §7 and roblox-audio §G appended). The J018 phrase is in every changed file. 'Riot' appears in headers only. No library IDs, champions or transcript lines. No tips section. evals/ and evidence/ unchanged. LF line endings |
| C7 better work | yes, clearly | see below |
| C8 brief v2 | fail on V3 | V1 pass (inputs and budgets per line, 'images: none'). V2 pass. V3: the maker's runs reproduce (clip_check exit 1 with FAIL on the missing marker; the log-diff fixture). My runs found R-31 (F1) and the Studio curve trap (F2b). V4 rec. (R1). V6 rec. (R3). V7 borderline (R7). V10 pass (event names, sync rule, attempt/outcome, ambience map keys match the animator, VFX, game-design and environment books). V11 pass (animator and game-designer rows adopted); same-wave rows: R5 |

## Will an agent make better work with these books?

Yes. I read eval brief 1 (coin pickup at 20 per second) and brief 3 (building collapse on phones) as the agent would. The old books gave a good rule table and a cue card, but no process. With the old books the agent would design straight from rules, write an untestable "listening-test plan" and pick sounds by label. With the new books it does these things:
- It frames the job, the verb and the rate first.
- It writes a stage sheet on the animator's event ids and splits the attempt tick from the confirmed outcome.
- It reuses library parts and puts temp sound on the markers before any prompt.
- It prompts by texture, with an odd variant.
- It measures every file, with known traps listed.
- It asks the owner goal questions at three check-ins, instead of claiming it listened.

Worked example 2 almost answers brief 1 with the right merge window and caps. The sync rule now matches the animator and VFX books.

Weak spots:
- The one line that guards honest paid reveals measures RMS, not loudness (F1).
- One engine claim and one Studio check misread the docs (F2).
- Five findings have rules but no checks (F3).
- The workflow has 11 steps and three check-ins for every job. A single minor cue is lighter only through the short card and "minor cues picked by numbers".
- The always-loaded text grew by about 14 KB.
- The sync and attempt/outcome numbers are written in several places (R3).

All three blocking fixes are a few lines each.
