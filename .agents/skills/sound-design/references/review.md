> Author: J018 maker sound-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018). Revised by orchestrator · claude-opus-5-5 · high · 2026-10-23 (J021-D4, on 982592c): R-01. Revised by J020 step 8 follow-up sound-designer · claude-opus-5-5 · high · 2026-10-24: soundbench known limits (§4).

# Review: inputs, the owner's play-test, self-review list, file measures

SKILL.md §5 runs this file before every hand-back, and §5 of this file is the procedure for reviewing someone
else's sound. I cannot hear. Every line below names the input that proves it; a line whose input is missing goes
to the could-not-check list, never to "passed".

## 1. What each input can prove

| Code | Input | Proves | Cannot prove |
| --- | --- | --- | --- |
| D | my documents: cue card, stage sheet, identity sheet, the timing list and feature spec revisions I built on | that a decision was made and is consistent | how it sounds |
| T | the animator's `tools/anim/clip_check.py <samples> --timing <timing.json>` events records | each event I key to exists as a marker (missing = FAIL) and its offset in frames | output timing |
| F | the measures in §4 on the delivered file (the FLAC that ships, after export): `python -m tools.audio.soundbench measure`, or the `render` report (targets vs measured, every step's log) | onset, main transient, attack, peaks, envelope, bands, phone loss, mono, seam, clicks, pitch, loudness of that file; must-targets passed or missed | feel, masking in the mix, engine latency |
| S | Studio MCP (skill `studio-mcp`, named `studio_id`): read-only `execute_luau` inspection of the audio graph and the place; `get_console_output` with the integrator's debug cue log during a play-test. Run by the studio operator or the lead on your request when your tools line has no Studio MCP: name the inspection (`roblox-audio.md` §G) and read the returned output | what is wired, distance curves, bus names, which cue fired on which event and how often (script time) | what the player hears; captures are stills without sound |
| L | `python tools/film/shotlist.py log-diff <shots.json> <log.json>` (cutscenes) | planned vs logged cue times, missing and extra cues | output latency |
| G | Grep of the game's source | hard-coded asset ids | anything else |
| V | a device capture with sound (owner or studio operator, on the target phone and headphones) | sync and loudness on the device | taste |
| P | the owner's play-test (§2): the owner's flags word for word, dated, with the build revision played | feel, emotion, verb, heaviness, the full mix on the owner's devices | numbers; it is never asked for as a listening session |

Every T, F, S, L and G reading is a **screening aid**, not a verdict: its known false readings sit next to its command (§3 R-40, R-43, R-44; §4 last column; `roblox-audio.md` §G last column). A failing or borderline reading is checked by eye (a waveform and spectrogram plot of the file, `soundbench measure --picture`, the listed instances or log lines) before any fix note goes out; feel stays the owner's play-test; a pass on a case that matches a listed false reading is checked the same way. Never send a fix note on a number alone.

Labels in the hand-back: MEASURED (numbers without a tolerance from the brief), gate-verified, MCP-verified, owner-confirmed, not verified. A start value marked (P) can fail a line only as "outside start value, owner to judge", never as a hard FAIL.

## 2. The owner's play-test (replaces the check-ins A, B and C)

The listening check-ins A (temp), B (options) and C (preview) are retired (J020-D3, J020-LD3, GreatWallSim D-064): the
owner does not judge sounds in listening sessions, and you never ask for one. What replaces them:

| Question | Who answers | With what |
| --- | --- | --- |
| Is the file right? | you | the measures inside the card's must-targets: `soundbench render` exit 0; aim misses listed (R-36) |
| Does it play on its event? | you, from the studio operator's run | the debug cue log in a play-test: each cue once on its event, in order, one per merge window (R-41, R-50) |
| Is it in sync on a device? | studio operator or owner | a device capture with sound (R-54), else "not verified" |
| Does it feel right? | **the owner, in their own play-tests** | the owner's flags |

- "Done" = measured and proven to play on its event. Never write "sounds good", "approved" or "auditioned" without the owner's play-test behind it.
- When the owner flags a sound: record the owner's words, the date and the build revision on the card (field 50); fix it (a changed prompt and a new round when the take is wrong, J020-D7; a recipe change when the edit is wrong); return a `lesson` (type owner-correction, the owner's words, the layer: prompt, pick, recipe, mix or playback) so the books learn.
- A cue that still misses its must-targets after 3 regenerate rounds goes to the owner with its numbers (the rank and render tables), not with a request to listen (J020-D7).
- No reference sounds (CD-2): a pick is made against the card's targets, never against a "category reference".
- A craft rule a cue breaks (SC-16) needs its reason on the card and in the hand-back, so the owner's play-test can overrule it.

## 3. Self-review list (run before every hand-back)

Run every line that fits the cue type; mark each passed, failed, MEASURED or not run, with its input.

**a. Frame and stages (input D, unless named)**
| ID | Look for |
| --- | --- |
| R-01 | The card names the job (cue, feedback, emotion), the story point in one line, and quotes the target-experience line with its sentence; the emotion row chosen traces to that sentence. |
| R-02 | Every state change in the feature spec has a cue or a written reason for none; miss, block, refusal and success each have their own cue; refusal sounds are soft and rate-limited (at most about one per 0.5 s (P)). |
| R-03 | The card names the emotion, not only the object; mood variants exist where the object appears in areas of different mood. |
| R-04 | An ability card starts with the mechanic verb, the same word as the animator's clip card and the VFX frame script; the chosen texture moves like it (a slow has the longest tail of its family, F-05). |
| R-05 | The stage sheet has a row for every stage in the timing list revision, with the same names; a stage with no sound has a reason. |
| R-06 | (T) Every event my cues key to exists: no missing marker in the events records, offset 0 frames for my events (or my cue follows the marker time and says so). |
| R-07 | Attempt cues are keyed to the input event; outcome layers (impact weight, reward, celebration) only to a confirmed event, never to `contact_candidate` or a client prediction. |
| R-08 | An enemy tell starts on the VFX tell's event, is one asset with no pitch or timing jitter, lasts the reaction window from the threat sheet (F-12 sound length) and stops on the damage event. |
| R-09 | A state with a timer or breaking point has a warning cue keyed to its end-of-state event, and its level rises toward the end (F: F-05 envelope peak in the last third). |
| R-10 | Combo and multi-hit cues follow the timing list's unequal gaps; nothing is placed on an even grid. |
| R-11 | Every effect cue has build, peak and resolve with start times; each result starts after its cause; the build is loudest at the release. |
| R-12 | Each character cue traces to a feel word of the character card; the nearest similar character is named and the plan differs from it; a variant re-themes every ability's sound and keeps the signature. |
| R-13 | Each weapon, ability and character has its signature element named and present in every stage's layer list; nothing on the identity sheet's forbidden list is used; the tone words fit; siblings differ (R-35). |
| R-14 | (D + S) The sound-code table has no family with two opposite meanings; every floor material found in the place (read-only `execute_luau` listing walkable part materials and terrain materials) has a footstep set. |
| R-15 | The cue's loudness tier and cap come from the read rank; a reward cue's tier and rate come from the progression designer's reward tier table (T1-T4); a cue played every second is shorter and quieter than a rare cue of the same family. |
| R-16 | (D + S) The card states the hearing distance in studs; must-act sounds carry farther than small ones; the emitter's real roll-off matches the card (read the mode first: a preset `DistanceAttenuationMode` ignores the custom curve, and the listener's curve multiplies with it; `roblox-audio.md` §G); a far-carrying cue has its high layer on a shorter curve than its low body. |
| R-17 | Each ambience zone carries the map's emotion (`feeling`) and has its signature element, every point source names its visible cause on the ambience map, and natural phenomena use natural-sounding sources or a named stand-in. |
| R-18 | A round, boss fight or event has an intensity plan (music state, cue tiers over time) that rises toward its climax, not flat. |
| R-19 | Count-ups play no sound per digit; a flying-coin sequence ticks on the first few arrivals and closes with one sound on the last. |

**b. The file (input F, the measures in §4)**
| ID | Look for |
| --- | --- |
| R-20 | Starts on its transient: onset (F-01) ≤ 5 ms (P), and on hits the peak (F-02) within 10 ms (P) of the onset. A larger gap means a noise head or a slow attack: inspect. |
| R-21 | Sample peak ≤ −1 dBFS and true peak ≤ −1 dBTP (F-03) on the delivered format. |
| R-22 | One-shots end below −40 dB re their peak inside the file (F-04 `ends_above_-40` false); cues played every second reach −40 dB within about 500 ms (P); the heavy version decays more slowly than the light one (F-05); an in-play celebration ends (F-04) within about 2 s (P) (S-194). |
| R-23 | Essential cues keep at least about 10 % (P) of their energy in 500 Hz-5 kHz (F-06) and lose at most the card's phone-loss target (`phone_loss_db`, §4); below that, fix the file (saturation for harmonics, a mid layer) or regenerate; how it sounds on the owner's phone is the owner's play-test. |
| R-24 | Bright layers keep at most 0.5 % (P) of their energy below their low cut (F-06); in each cue only one layer (the low-end owner) has more than about 10 % (P) of its energy below 120 Hz. |
| R-25 | A stereo file loses at most 3 dB summed to mono (F-07). |
| R-26 | Loops: seam ratio (F-08) ≤ 2 (P); a long-stay bed lasts 15-20 s or more per segment (F-12, S-100). `render` judges every `form.loop` card with the must rows `form.loop_f08`, `form.loop_wrap_clicks`, `form.loop_wrap_hf`, `form.loop_seam_gap` (with a loop step also `form.loop_crossfade_level`, and `form.loop_length_samples` for music); a card's `loop_seam` only tightens the 2, loosening needs `must: true` and a `why` (`craft-process.md` §6); the blind spots are in §4. |
| R-27 | Pitched and tonal parts sit within ±50 cents of a game-key note (F-10); check a surprising note for the harmonic trap. |
| R-28 | Charges and build-ups rise in pitch first to last (F-10) and peak in the last 10 % of the file (F-05). |
| R-29 | Sustained magic, travel and loop layers vary over time: centroid variation (F-11) ≥ 0.05 (P). Never applied to one-shot hits. |
| R-30 | A pass-by's envelope peak sits in the middle third, not at the start (F-05). |
| R-31 | Variants of one sound: F-09 within ±1 dB. Options and siblings with different spectra: F-13 a, never F-09. Paid random reveal results: F-13 b momentary maximum within 1 LU of each other and sample peaks (F-03) within 1 dB (D-03); never F-13 a, which a longer, quieter tail pulls down. A variant set rendered as files is checked by `render`'s `variants.level_spread` row; every variant file of a paid-reveal member enters its D-03 check. |
| R-32 | (D + F) Every tier of a paid random reveal uses the same windup asset (same asset id, or the same file hash), so length and sound are identical up to the result. |
| R-33 | Size tiers of one family step down in pitch by the card's declared interval (S-82: 3-5 st per size class (P)), the same step in every family: F-10 on each tier's body or tonal part, and F-05 decay longer per tier. A step off the declared one by more than 1 st (P) is flagged; a step near 7 or 12 st off is the harmonic trap: compare the same partial. |
| R-34 | In one scene, threat hits and attacks (impact and contact one-shots) rise faster than friendly one-shots: onset-to-peak (F-02 minus F-01) of each is shorter than that of every friendly one-shot (SC-11). Tells, warnings, charges and build-ups are not compared: they rise by design (S-76, R-09, R-28). |
| R-35 | Sibling signatures (weapons, abilities, characters of one game) differ: main note (F-10) at least 3 st (P) apart, or a different main band (F-06); whether they are told apart by ear is the owner's play-test. |
| R-36 | (F) `soundbench render` exit 0 on the delivered FLAC: every must-target and the level (by the measure the card names) pass; every aim miss is listed with its distance; the log shows the design pass in the SC-09 order (a step out of order has its `why`) and the fixed edit pass; a paid-reveal family passes its family check (R-31). Exit 1 or 3 is not done. |

**c. In Studio and in the game (inputs S, L, G)**
| ID | Look for |
| --- | --- |
| R-40 | (S) The graph matches the card: AudioPlayer → bus AudioFader named by category → output (2D) or emitter and listener (3D); no audio effect except one AudioReverb per space type on the SFX bus (music and UI bypass it; J020-D1, D10); ducks are AudioFader volume changes from a script, no AudioCompressor. (S, G) Cosmetic SFX play from client scripts on replicated events; one-shots come from pooled AudioPlayers that set `Asset` from the cue table (R-44): (S) no AudioPlayer or Sound is created during a 10 s burst after warm-up (`roblox-audio.md` §G creation counter; a count before and after reads flat for create-and-destroy code too); (G) no `Instance.new("AudioPlayer")` or `Instance.new("Sound")` outside the pool module. Screening aid: the grep misses a template `:Clone()` and the counter misses a player never parented into the data model, so run both; read each counted instance's full name and each grep hit's line before a fix note. |
| R-41 | (S) Debug cue log in a play-test: each event fires its cue once; at the burst rate one cue per merge window; a request the server rejects logs no outcome cue. |
| R-42 | (S) A countdown or pulse cue ticks on the timer's events (the log's tick times match the timer); a tick paired with a visual blink has the blink's rate (at most 3 per second); audio-only warning pulses use the S-135 spacing. |
| R-43 | (L) Cutscene: run `log-diff --tol-ms 40 --early-ms 16.7 --tol-source "S-133"` (the one-sided S-133 window, −16.7 ms to +40 ms) and read the signed diff of each cue; "planned, not logged" is a missing cue. `--tol-ms` without `--early-ms` is symmetric and passes early cues: never use it for sync. Screening aid: the log is script time, not output time; a cue at the window edge (within 5 ms (P)) is checked on a device capture (input V) before a fix note. |
| R-44 | (G) Grep the game's source, case-insensitive, for the patterns `rbxassetid://`, `asset/?\?id=`, `\.Asset\s*=` and `SoundId\s*=` (the second and fourth catch legacy `http://www.roblox.com/asset/?id=` ids on `Sound.SoundId`): no hit outside the cue data table, except a line that reads its asset from that table. Screening aid: the grep misses a bare number later joined into an id in another file, and ids inside binary place or model files (`.rbxl`, `.rbxm`) or set in Studio only (the R-40 graph listing shows those): read every `.Asset =` and `SoundId =` line it finds. |
| R-45 | (D + S) Playback matches the card (`roblox-audio.md` §H): 2D or 3D by the rule, with the reason; a player's action has its actor version 2D and its others version 3D; each 3D emitter's `DistanceAttenuationMode` and `DistanceAttenuationBounds` (or Custom curve) match the card's studs (read the mode first, R-16); `SoundService.DefaultListenerLocation` is `Character`; cues that take the room route through the zone reverb, cues that do not bypass it; each duck has the card's four answers and only the buses it names go down. |

**d. Proof and device (inputs S, F, V; feel is the owner's play-test P)**
| ID | Look for |
| --- | --- |
| R-50 | (S) Temp pass: the debug cue log shows every temp cue firing on its event id, in the stage order of the timing list, before the design pass starts; temp sources marked TEMP. (Was the check-in A listen, retired J020-LD3.) |
| R-51 | (F) Raw vs processed: `soundbench compare <take master> <delivered>`: the core's note (F-10, when trusted) and main band (F-06) kept unless the card's recipe means to move them; the reason is on the card. (Was the check-in B listen, retired.) |
| R-52 | Retired (J020-LD3; was the check-in C listen). Screen-covered naming, emotion, masking in the full mix and phone or headphone feel are the owner's play-test; the numbers that screen them are R-23, R-34, R-35, R-41 and R-45. |
| R-53 | Retired (J020-LD3; was the check-in C sequence listen). Distinctness by ear is the owner's play-test; screened by R-33 and R-35. |
| R-54 | (V) On the target device the sound onset lands inside the S-133 window (−16.7 ms to +40 ms of the first lit contact frame). Without a device capture: "not verified". |

**e. Hand-back (input D)**
| ID | Look for |
| --- | --- |
| R-60 | Every note and fix names a term (frequency, envelope, attenuation, EQ, reverb, level, timing), a direction and an amount, and the problem it solves; after the fix the problem itself is re-checked. |
| R-61 | Stand-ins are named with their better source; reused and new parts are listed; every finished cue lists its parts and the source of each layer. |
| R-62 | Takes per round by tier were made (minor 3, frequent 4, important 6; an important sound's layers one prompt each, J020-D9), one of them odd; the unprocessed take was tried; (F) the rank table is recorded: each take's targets passed, near or missed, which misses a recipe can fix, the pick and why each other take lost; good unpicked takes filed in the library; for a new setting or material, the real-world properties used in the prompt are named. No reference sound is used (CD-2). |
| R-63 | Every broken craft rule has a reason on the card and in the hand-back (SC-16); no guardrail (SKILL.md §4) is broken; nothing is edited in Roblox but the zone reverb and fader volumes (J020-D1). |
| R-64 | The could-not-check list names, per line, the missing input and the check or capture that closes it. |
| R-65 | Every gameplay fact a cue carries also shows on screen (sound off), and every intense cue has a reduced version that keeps the information. |
| R-66 | The stop criteria hold and the pass budget used is stated; a part that stayed stuck is logged. |
| R-67 | Regenerate rounds: a take that missed after its fixable steps was regenerated with a changed prompt (the misses the prompt had to change are written), not piled with edits; at most 3 rounds; a cue still missing after round 3 went to the owner with its rank and render numbers (J020-D7). Every owner play-test flag is on the card word for word and returned as a `lesson`. |

## 4. Measuring a file (input F)

Run the kit editor's measures (`soundbench`, J020; one way to measure, G-3): `python -m tools.audio.soundbench measure <file> [--low-cut HZ] [--high-pitch] [--json] [--picture PNG]` for F-01 to F-12 and the new measures below; `python -m tools.audio.soundbench parity <files> --mode integrated|momentary [--json]` for F-13 (integrated for options and siblings, momentary for paid random results); `python -m tools.audio.soundbench compare <a> <b> [--json]` for two files side by side (raw vs processed, R-51). `render <cue-folder>` re-measures every delivered file against its `card.json` (R-36). `tools/audio/cue_check.py` stays as a thin wrapper with the same command line and output (its numbers equal the editor's: golden JSON). The tool reads the file with `soundfile`, subtracts each channel's mean first (generated audio often carries a DC offset: it hides a leading silence in F-01, fills the low band in F-06 and keeps F-04's flag on), and takes mono as the mean of the channels; the tables below define every measure. `doctor` reports a missing package or ffmpeg; a measure it cannot compute is NOT RUN.

**These recipes are screening aids.** The last column lists every false reading found so far. A FAIL, or a reading
within about 20 % of its limit (0.5 dB or LU on level lines) (P), is looked at on a waveform and spectrogram plot of
the files before any fix note; feel is never asked: it is the owner's play-test (§2). A PASS on a
case that matches a listed false reading is not trusted: check it the same way. Write the result "MEASURED, screened:
<what the plot or the owner showed>".

| # | Measure | Compute | Known false readings (wrong number with no error) |
| --- | --- | --- | --- |
| F-01 | Onset (ms) | first sample whose absolute value reaches the peak minus 30 dB | a noise head within 30 dB of the peak gives 0 ms: compare with F-02 |
| F-02 | Peak position (ms) | position of the largest absolute sample | a loud tail hit after the transient moves it late: for attack comparisons (R-34) measure the attack layer's part |
| F-03 | Peaks | sample peak in dBFS; true peak = the peak of the file resampled ×4 (`scipy.signal.resample_poly`) in dBTP | an MP3 or OGG measured before export hides decoder overshoot: measure the delivered format |
| F-04 | Tail | last 10 ms window whose RMS is within 40 dB of the loudest window; flag when the last window is still above it (`ends_above_-40`) | a file cut before the decay reports the file length as the tail: read the flag; a noise floor within 40 dB of the loudest window also keeps the flag on and reads the file end as the tail: look at the waveform |
| F-05 | Envelope | 10 ms RMS windows: position of the loudest window, time from it to −20 dB, level 100 ms after it | a short file has no −20 dB point (reported as none, not as long) |
| F-06 | Bands | share of power (FFT of the whole file) below 120 Hz, 120-500 Hz, 500 Hz-5 kHz, above 5 kHz, and below the layer's low cut | a long silent head or tail does not change shares; a hard clip adds false highs |
| F-07 | Mono drop | RMS of the mono sum vs the mean channel RMS, in dB | uncorrelated stereo noise drops about 3 dB by nature: listen before rejecting |
| F-08 | Loop seam | the jump between the last and first sample divided by the 95th percentile of sample-to-sample steps | a fade to silence at both ends reads 0 and hides a gap in the loop |
| F-09 | Loudness | RMS of the loudest 400 ms window of the F-12 sound (or the whole sound if shorter), in dBFS; integrated LUFS only for files of 0.4 s or more and for whole-mix captures (S-103) | on the untrimmed file, trailing silence pulls a sound under 400 ms down (a 200 ms variant with 300 ms of silence read 3 dB quieter): trim first; a noise floor within about 40 dB of the loudest 10 ms window carries the F-12 sound to the file end and gives the same 3 dB (−42 dBFS floor under a −1 dBFS note: −7.06 vs −4.05 dBFS): look at the waveform; never call F-09 RMS "LUFS" (S-209); RMS has no K-weighting: two files with equal F-09 can differ by 4 LU when their spectra differ, so any parity check across spectra uses F-13 |
| F-10 | Pitch | strongest spectral peak from 60 Hz to 4 kHz (to 12 kHz for chimes, sparkles and ticks) in the loudest 200 ms → note and cents, and its height above the band median in dB; also per 50 ms frame, first and last | a strong harmonic above a weak fundamental names the wrong note (an octave or a fifth up); a fundamental above the band reports a noise peak as a note: trust a note only when its peak stands at least 20 dB above the band median; on noise the number is meaningless |
| F-11 | Movement | spectral centroid per 50 ms Hann frame (frames within 10 dB of the loudest), standard deviation ÷ mean | on one-shot hits the attack frame inflates it: sustained layers only |
| F-12 | Length | file: samples ÷ rate, in ms; sound (the F-12 sound): from the F-01 onset to the end of the last 10 ms window whose RMS is within 40 dB of the loudest window (as F-04), then back to the last sample at or above the peak minus 40 dB inside it (sample-exact, no 10 ms grid error) | silence padding counts in the file length: length checks on a cue (R-08, D-03 tail) use the sound length; a per-sample end alone moves to the file end under a noise floor about 50 dB under the peak (noise peaks about 12 dB over its RMS), hence the window step; a floor within about 40 dB of the loudest window still reaches the file end (−42 dBFS under a −1 dBFS note): when the sound length is near the file length, look at the waveform; a reverb tail above the limit is part of the sound (a 150 ms pluck with −20 dB wet reverb: 245 ms) |
| F-13 | Loudness parity (LUFS, `pyloudnorm`, BS.1770 K-weighted) | (a) integrated, for options and siblings: pad every compared file with silence to one common length (the longest file plus 0.4 s), then `integrated_loudness`. (b) momentary maximum, for paid results: trim each result to its F-12 sound before measuring and measure all channels; window = 100 ms, or the shortest trimmed result's length if shorter; `Meter(rate, block_size=(window samples − 1) / rate)` (a block of exactly the result's length raises an error on some lengths through float rounding), `integrated_loudness` of every window at 10 ms steps, the largest value | (a) files padded to different lengths shift by up to 3 LU (gating counts the tail blocks differently): one common length for the set; (a) averages the tail in: a longer, quieter tail hides a body about 3 LU louder, so paid results use (b). (b) a window longer than the shortest result reads a longer result about 3 LU louder at the same level; a window that follows a result's length grows with trailing silence, a noise floor or a reverb tail and fails an honest longer result the same way (a window grown to 400 ms by a −50 dBFS floor: 3.59 LU; to 244 ms by the same −20 dB wet reverb on both: 2.80 LU): keep it at 100 ms and trim first; a mono sum reads a wide result up to 3 dB quieter: all channels; a higher register reads louder at the same sample level (K-weighting: a 1,320 Hz note about 1 LU over 880 Hz): a true difference, balance the level; (b) reads the loudest 100 ms only, so more notes at the same level read equal (5 overlapping bells vs 1: 0.18 LU), as D-03 allows; when the shortest result is a short decaying pluck the window shrinks to it and a sustained result reads far louder (40 ms pluck vs a sustained note at the same peak: 8.45 LU): look at both waveforms before any fix note; a denser burst of about 20 ms at the same peak passes (0.26 LU) and a 30 ms square burst reads just over the limit (1.22 LU): compare the attack measures (`attack_share_5ms`, `attack_rise_ms`) of the results; the trim inherits F-12's noise-floor limit. Neither says anything about peaks: pair with F-03 |

**New measures (soundbench, J020; named by their output key).** Known false readings as above; full list in each function's docstring (`tools/audio/soundbench/measures.py`).

| Key | Measure | Known false readings (start list) |
| --- | --- | --- |
| `main_transient_ms` | first point of the 1 ms envelope within 10 dB of its maximum; hits and impacts bind their onset target and `trim` to it | a rising sound (tell, whoosh, riser) is late by design: those bind to F-01 |
| `attack_rise_ms` | 10 % to 90 % of the 1 ms envelope (threat sharp, friendly soft, SC-11) | cannot read a rise under about 2 ms |
| `attack_share_5ms` | energy in the first 5 ms after F-01 ÷ the F-12 sound's energy; the guard of `denoise`, `declick`, `pitch` | a noise head moves the onset |
| `phone_loss_db` | dB lost through a 400 Hz high-pass and a 10 kHz low-pass (a rough phone-speaker model) | the same rough model for every file: a screen, not a phone |
| `tail_noise` | floor after the F-12 sound and signal-to-noise (generated takes often end in hiss) | `sound_reaches_end` true: the floor is the sound itself |
| `clicks` | sample steps far above the local step size; `edges`: a first or last sample far from zero | a hard edge from silence reads as a click; a loop's end edge is its seam |
| `tonality` | spectral flatness (tonal, mixed, noisy) and the notes present | harmonics are listed as notes (as F-10) |
| `roughness` | depth of 30-150 Hz movement in the envelope | two close notes beating read rough; a screen only |
| lag (`compare`, and after every ffmpeg step) | cross-correlation with the input | periodic, silent or inverted input reads "not clear": proven on a probe signal instead |

Pictures (`--picture`, or `render` on a miss): a waveform and spectrogram PNG, before and after. Light checks: numbers for every take; a picture only when a number fails or is near its limit, and for important cues.

**soundbench known limits: do not trust a green result past these** (`tools/audio/soundbench/README.md` "Known limits", "Ranking takes", "Layers, loops and variants"; J020 `job-card.md` Progress rows 5-6, `review-rank.md`, `review-step6.md`). A pass on a case in this table is written "MEASURED, inside a known blind spot: <which>", checked on a picture where the row says so, and listed for the owner's play-test.

| Case | What the tool misses | What to do |
| --- | --- | --- |
| A short hit that clipped before the MP3 encode | `rank`'s clip check: the clipped tips last under 1 ms and the MP3 smears them; not caught even at +12 dB. Clipping scaled down after it happened, or under full scale, is not caught either | picture of every important hit take (`rank --picture`); a hit that looks flat-topped is regenerated; a clipped hit that passes reads at most as a level miss (`peak` cannot repair distortion) |
| Steady full-scale rumble or a steady low tone | reads as clipped (rejected) though clean | look at the take before trusting a "clipped" rejection of a sub or rumble layer; ask for it quieter in the next prompt rather than override |
| Takes of 2 s or more | no real ElevenLabs take of 2 s or more has been measured yet: the clip limit (10 ms in 300 ms, 2.8 ms margin) and the loop calibration rest on 480-800 ms real takes and fixtures built from them | the first long cue's takes are measured against the calibration and reported to the lead; a long take rejected as clipped gets a picture before it is dropped |
| A loop seam in the quiet part of a bed with a loud section | F-08 and `form.loop_wrap_hf` read the seam against the whole loop; only the click floor (1 % of peak) is left. Also not read: a spike inside low-passed noise, a gap in a bed with near-silent lulls, a slope break with no jump | `render --picture` and look at the wrap; list the bed for the owner's play-test |
| Roblox's transcode at the loop point | the seam is sample-exact in the FLAC; what Roblox's transcode does at the wrap is not measured | proven only in the play-test (the debug cue log proves it plays, not that it is seamless) |
| `rank` on a loop or variant card | judges each take as a one-shot; the form rows are judged only at `render` | never stop at rank's `use` for a loop or variant cue: `render` must pass the `form.*` and `variants.*` rows |
| `rank` and design steps | computes edit-pass fixes only: a miss an `eq` or `limit` could close reads as a prompt miss | try the design step in `recipe.json` when it is small; `render` measures it |
| Layer edge fades | the automatic 0.5 ms fade on a hot layer edge can cost attack (`edge_fade_attack_loss`) and moves the align reading up to 1.6 ms; clicks inside a take (over 1 ms from an edge) stay screening-only | read `edge_fade_attack_loss` per layer; a hit layer losing much attack is regenerated |
| Any result at all | **nobody has listened to any soundbench result**: every number is a screen | feel and audible defects are the owner's play-test (§2), never your claim |

## 5. Reviewing a sound set (someone else's or a game's current one)

1. Open the cards, the timing list and the files before the maker's hand-back.
2. Run §3 a-d on the documents, files and Studio state.
3. Check in two passes: each cue solo (its file measures and targets, `render`), then the mix (family parity F-13 a, one low-end owner across the scene's layers, tiers and level slots, 2D or 3D and falloff, ducks with their four answers, the debug cue log at the burst rate); log findings for each pass separately. Feel is not yours to grade: list what the owner's next play-test would show, never ask for a listening session.
4. Findings table: problem → layer (job, stage, envelope, band, space, level, timing, repetition, policy) → rule ID → concrete fix with a term, direction and amount → severity (blocking, recommendation, new request).
5. Restate the problem behind any note that came with a solution; fix the worst problem first and re-check it.
6. End with the could-not-check list. Never edit the work under review.

## 6. When a cue is done

Stop when: every §3 line that fits is passed or MEASURED inside its start values; `render` exits 0 (every must-target passed); the cue is proven on its event in the debug cue log; the stand-ins are named; and the last note round brought no new problem. A cue still missing its must-targets after 3 regenerate rounds goes to the owner with its numbers (J020-D7). The owner's play-test flags reopen a done cue. New ideas past that point go to the follow-up list. A part stuck after two passes is logged, parked, and revisited after the next pass; a third failure goes up as `needs-decision`.
