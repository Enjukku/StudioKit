---
type: job
scope: universal
status: draft
updated: 2026-10-23
source: J020 stage 2 (after G1, J020-D13); revised after the architect review (review-1, 2026-10-23)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-23; revised the same day from the architect's review-1 (13 findings, four of them measured probes; the lead reproduced the afftdn lag: 1,102 samples, 25.0 ms)

# J020 editor design: `soundbench`, the kit's AI audio editor

Built for the agent, never for a person (J020-D2): text in, numbers and pictures out. New code (J020-D5); GreatWallSim's `audio_edit.py` is a reference only. Workflow it serves: `workflow-map.md` §3 (G1 approved).

## 1. What it must guarantee
| # | Guarantee | Why |
| --- | --- | --- |
| G-1 | **Original takes are never changed.** Each take's sha256 is in its sidecar and `render` checks it. Every output is rebuilt from a take plus a written recipe. **Same recipe, same audio:** the sha256 of the float32 audio before encoding, plus the encode settings, on the tool versions written in the log. On another machine or version: the same measures within a tolerance (0.1 dB, 1 ms), not the same bytes | review-1 #3: an Ogg file's stream serial number is random, so two encodes of the same audio never have the same file hash |
| G-2 | **Every step is logged** with its parameters and the numbers before and after | the agent cannot hear, so the log is how anyone checks what happened |
| G-3 | **One way to measure.** The measures of `cue_check.py` (F-01 to F-13) move into the editor; `cue_check.py` stays as a thin wrapper, its outputs captured as golden JSON before the move | GreatWallSim's tool and the kit tool disagreed by 1.5-4.6 LU on short sounds (review F17) |
| G-4 | **A number is a screening aid, never a taste verdict.** Each measure lists its known false readings; the tool never says "sounds good" | the J018 lesson; the owner judges in play-tests (J020-D3) |
| G-5 | **Tested on the real faults.** Every operation and measure has an offline test, including what it must *not* change (§9); planted faults prove the tests can fail | a wrong number with no error is the worst failure (J018) |
| G-6 | **No Roblox editing.** The editor bakes everything except the room; the room is Roblox's zone reverb (J020-D10) | J020-D1 |
| G-7 | **Every external step keeps time.** After each ffmpeg step: same sample rate, same channels, same length (unless the step is declared to change length) and **zero lag** by cross-correlation with its input. A known latency is compensated; an unknown one is refused | review-1 #1: `afftdn` delays the sound 25 ms and cuts the tail by the same amount, with no error |
| G-8 | **The delivered file is lossless.** Export is FLAC; Ogg only for a file that would pass 20 MB | review-1 #4: Roblox transcodes every import (`audio/assets.md`: "Studio transcodes imported audio before saving it"), so an Ogg export puts a third lossy codec after ElevenLabs' MP3 and our Vorbis; FLAC is accepted (`.mp3`, `.ogg`, `.wav` or `.flac`, under 20 MB and 7 minutes, up to 48 kHz) and keeps loops sample-exact |

## 2. Where things live
Tool: `tools/audio/soundbench/` (a package; run as `python -m tools.audio.soundbench <command>`).

Per game, one folder per cue, `content/audio/<cue-id>/`:
| File | Holds | Written by |
| --- | --- | --- |
| `card.json` | the cue card's machine part: kind, tier, 2D or 3D (map §6), takes the room or not, ducking, the **targets** (§7) | sound designer |
| `takes/<cue-id>.r<round>.t<n>.mp3` + `.json` | each ElevenLabs take as received, untouched; sidecar: prompt, settings, model, date, credits, sha256 | `generate` |
| `takes/<cue-id>.r<round>.t<n>.master.wav` | the take decoded **once** at intake to float32 WAV, with the decoder and its version in the sidecar; every later step reads this | `generate` |
| `recipe.json` | the chosen take(s) and the two passes (§4) | sound designer |
| `out/<cue-id>[-v<k>].flac` + `.log.json` | the finished file(s) and their log | `render` |
| `report/` | numbers (JSON), a short table (Markdown), pictures (PNG) | `measure`, `rank`, `render` |

## 3. Commands
| Command | Does | Output |
| --- | --- | --- |
| `doctor` | finds ffmpeg (PATH, the WinGet folder, or `SOUNDBENCH_FFMPEG`), checks its version and the filters used, the Python libraries, the ElevenLabs key entry | pass, or the missing items |
| `generate <cue>` | asks ElevenLabs for this round's takes: minor 3, frequent 4, important 6 (J020-D9); layers of important sounds one prompt each; stops before a call that would pass the credit budget; round 4 refused (J020-D7); decodes each take to its master | takes, masters, sidecars; credits spent |
| `measure <file or cue>` | every measure in §5 | JSON; `--picture` adds a waveform and spectrogram PNG |
| `rank <cue>` | scores every take of the round against the card's targets (§6) | ranked table: each target passed or missed, which misses a recipe can fix |
| `render <cue>` | checks take hashes, applies `recipe.json`, re-measures, compares to the targets, runs the family checks (§7) | file(s), log, report; exit code 1 when a must-target or a guardrail fails |
| `compare <a> <b>` | the numbers of two files side by side | table |
| `parity <files>` | loudness parity (F-13) for siblings and paid reveals | table |

## 4. The edit operations: two passes
A recipe has two parts, run in this order (review-1 #7):
1. **Design pass** in the book's processing order (SC-09): clean → pitch → EQ → compress → add → compress again → transient → air and saturation. A step out of this order needs a `why`, or `render` refuses it.
2. **Edit pass**, fixed order (SKILL step 8, SC-13): `trim` → `cut` → `fade` → `mono` → `loudness` → `peak` → `export`. The tool runs these in this order whatever the recipe lists, so a tail is never cut before it is added and `mono` never runs after the level is set.

| Pass, stage | Operation | Engine | Rules |
| --- | --- | --- | --- |
| Design: clean | `dc`, `highpass`, `lowpass` | numpy/scipy (biquad, RBJ formulas; second-order sections) | exact and testable |
| Design: clean | `denoise` (hiss) | ffmpeg `afftdn`, under G-7 (its latency compensated) | refused when the attack share (energy in the first 5 ms after the onset) or the main-transient time moves past a limit (PROPOSAL until tested) |
| Design: clean | `declick` | ffmpeg `adeclick`, under G-7 | **sustained sounds and loops only**: on a clean hit it cut the 5 ms attack share from 0.216 to 0.056 (review-1 #6) |
| Design: clean | `dehum` (50/60 Hz and harmonics), `gate` (the tail's noise floor) | numpy/scipy | |
| Design: pitch | `varispeed` (pitch and length change together) | scipy `resample_poly` | **the default for percussive takes and layers** |
| Design: pitch | `pitch` (length kept), `stretch` (pitch kept) | ffmpeg `rubberband`, under G-7 | **sustained layers only**: on a 400 ms hit it moved the onset 18 ms early and cut the 5 ms attack share from 0.216 to 0.001, also with `transients=crisp` (review-1 #2); main transient and attack rise measured before and after, refused past a limit |
| Design: pitch | `to_key` (nearest note of the game's key, ±50 cents, S-127) | F-10, then `varispeed` or `pitch` | refused when F-10 is untrusted (its peak under 20 dB above the band median) |
| Design: EQ | `eq` bands: bell, low shelf, high shelf, notch (frequency, gain, Q) | numpy/scipy biquads | "cut before boost" (SC-06): a boost over a set dB needs a `why` |
| Design: compress | `compress` (threshold, ratio, knee, attack, release, make-up), `limit` (lookahead, true-peak ceiling) | numpy | the limiter reports its deepest gain reduction; sfx and ui refuse limiting a transient unless the recipe says why (GreatWallSim review F12) |
| Design: add | `space` (the sound's own tail and glue, never the room: decay, pre-delay, damping, wet), `echo`, `chorus` (movement, SC-10) | numpy convolution with a generated tail; ffmpeg `chorus` under G-7 | the room stays in Roblox (J020-D10) |
| Design: transient | `transient` (attack and sustain up or down) | numpy (fast vs slow envelope) | |
| Design: air | `saturate` (soft clip, drive, mix; for phone speakers, S-156) | numpy | the phone-loss measure shows whether it helped |
| Edit | `trim` | numpy | trims to the onset the card names for this kind (§7); a rising sound (a tell, a whoosh, a riser) is trimmed to F-01, never to the main transient; the log writes `lead_in_ms` (onset to main transient) so the integrator can start the sound early |
| Edit | `cut`, `fade` (in, out, curve), `mono` | numpy | |
| Edit | `loudness` | the same function as the card's level measure (§7) | |
| Edit | `peak` (true-peak ceiling, a margin for Roblox's transcode: PROPOSAL until the first upload is measured) | numpy | |
| Edit | `export` | libsndfile | FLAC (G-8); written at the take's sample rate; never resampled silently |
| Layers | `layers`: several takes, each with its own design pass, mixed at offsets in ms with gains; `align` puts each layer's transient on a marker; per-layer targets for important sounds | numpy | mixed-rate layers are resampled on load, with a log line |
| Loops | `loop_bed` (crossfade wrap), `loop_music` (bar-aligned from the BPM) | numpy | the seam is measured (F-08) |
| Variants | `variants`: n files with small seeded pitch (`varispeed`) and level changes, or one per take | numpy | **refused** for cards of kind tell, warning or countdown (SC-12: the same attack always has the same tell) |

Not built until a real cue needs it (rule: build what is asked; review-1 #11): flanger, a second exciter, `anlmdn` (it crashed on every call in the probe), a stereo-width measure (F-07 covers mono safety).

## 5. Measures
From `cue_check.py`, unchanged in meaning: F-01 onset, F-02 peak position, F-03 sample and true peak, F-04 tail, F-05 envelope, F-06 bands, F-07 mono drop, F-08 loop seam, F-09 loudness, F-10 pitch, F-11 movement, F-12 length, F-13 parity. New, each with its known false readings written next to it:
| Measure | Why | Known false readings (start list) |
| --- | --- | --- |
| Phone-speaker loss (high-pass 400 Hz, low-pass 10 kHz; the dB lost) | review F1, F4, F5, F8, F9: sounds near-silent on phones | a rough model of a phone speaker, applied the same way to every file |
| Main-transient time (to within 10 dB of the maximum, 1 ms envelope) | review F3, F10: hits 30-60 ms late | a rising sound's main transient is late by design |
| Attack rise time (10 % to 90 % of the envelope) | threat hits sharp, friendly soft (SC-11) | the 1 ms envelope cannot read a rise under about 2 ms |
| Attack share (energy in the first 5 ms after the onset ÷ the sound's energy) | the guard for `denoise`, `declick`, `pitch` (review-1 #2, #6) | noise heads move the onset (F-01) |
| Noise floor and signal-to-noise in the tail | generated takes often end in hiss | |
| Clicks (sample jumps far above the file's normal steps) | edits and loop wraps | a real hard transient reads as a click |
| Tonal or noisy (spectral flatness) and the notes present | review F4, F6, F7: a "whistle" with no whistle, a jingle that is hiss, wrong notes | as F-10 |
| Roughness (30-150 Hz movement in the envelope) | review F11 | a screening number only (the review's own words) |
| Lag (cross-correlation with the input) | G-7, after every external step | silence or noise-only input |

**Pictures:** a PNG with the waveform and spectrogram (matplotlib), before and after when rendered. The light-check rule applies (owner J005-D8): numbers for every take; a picture only when a number fails or is near its limit, and for important cues.

## 6. Ranking takes
1. **Rejected outright:** clipped at the source, near-silent, no sound in the band the card needs.
2. **Each target scored:** inside, near (within its tolerance), or missed, with the distance.
3. **Fixable or not:** a miss a recipe step can fix counts less than one it cannot. A late start → `trim`; too long → `cut`. **Too quiet is fixable only when the gain needed fits inside the true-peak headroom**: sfx and ui do not limit transients, so a spiky take cannot reach its level (review-1 #9). Unfixable: all energy below 120 Hz on a phone cue; the wrong sound entirely.
4. **Output:** the order, the reasons, and for the top take the steps that would fix its misses. When no take passes after the fixable steps: "regenerate with a changed prompt", with the misses the prompt must change (J020-D7: at most 3 rounds, then the cue goes to the owner with its numbers).

## 7. Targets on the card (`card.json`)
Start values from the book (S-76, S-133, S-156, the genre preset, the mix slots), tagged PROPOSAL until a play-test confirms them. Each target says `must` or `aim`.
- **Timing:** onset (max ms) **and which onset it binds to** (F-01 for rising sounds; the main transient for hits, review-1 #8); main transient (max ms); attack rise (range); sound length (range).
- **Spectrum:** band shares (min and max); phone loss (max dB); notes or key.
- **Level, with its measure named** (review-1 #5; the book's S-103, S-209, S-210): F-09 for one-shots; F-13a (integrated, padded) for a family of siblings; integrated LUFS only for files of 0.4 s or more (pyloudnorm refuses shorter clips). `loudness` (§4) uses the same function. True peak (max dBTP).
- **Form:** loop (yes or no), mono, variants (count).
- **Playback:** 2D or 3D, and for 3D the falloff mode and range (map §6); takes the room (yes or no, J020-D10); ducks (what, how much, why, J020-D11). For a 3D cue the card can ask for a mono export (a Studio probe first: how a stereo file plays on an AudioEmitter is not checked).
- **Family checks run by `render`:** a card in a **paid-reveal family** runs F-13b and the F-03 1 dB check across its siblings and exits 1 on a miss (guardrail D-03, hard).

## 8. ElevenLabs
Endpoints and models as GreatWallSim used them (audio plan §11: sound generation `eleven_text_to_sound_v2`, music, text to speech), re-checked against the owner's guide before `generate` is built. ElevenLabs' sound-effects API page (`/v1/sound-generation`, read 2026-10-23, https://elevenlabs.io/docs/api-reference/text-to-sound-effects/convert): `output_format` defaults to `mp3_44100_128`; "MP3 with 192kbps bitrate requires you to be subscribed to Creator tier or above. PCM and WAV formats with 44.1kHz sample rate requires you to be subscribed to Pro tier or above"; models `eleven_text_to_sound_v2` (default) and `eleven_text_to_sound_v3`; `duration_seconds` 0.5-30; `prompt_influence` 0-1 (default 0.3); `loop`; the `character-cost` response header carries the billing. So `generate` asks for WAV at 44.1 kHz first and skips the MP3 decode; when the plan refuses it, it falls back to `mp3_44100_192`, then `mp3_44100_128`, and logs which format it got. Which model gives better game sounds (v2 or v3) is tested on the first real cue set. Otherwise each MP3 is decoded once at intake; a take without the encoder-delay tag decoded 23 ms late in the probe (review-1 #13), so the intake checks the decoded length against the requested duration and logs the decoder. The key: one `ELEVENLABS_API_KEY` entry in each game's `knowledge/design/keys.json`, loaded by `tools/keys.py run` (AGENTS.md §3.4); the tool never reads a key file. The credit budget per run is an argument with a default; each take's credits go into its sidecar.

## 9. Tests (`tools/tests/test_soundbench_*.py`)
- **Fixtures made in the test** (no audio files in the repo): a clean hit, a late-start hit, a bass-only thump, a hiss-only "lock", a wrong-note chime, a rough tone, a clipped take, a DC-offset take, a hummed take, a music bed with a bad seam. Each at 44.1 and 48 kHz, mono and stereo, and once through an MP3 encode and decode (real takes are 44.1 kHz stereo MP3).
- **Each operation:** does what it says (for example, `eq` gives the set gain at its frequency within 0.5 dB) **and does not change what it must keep**: onset, attack share, sample rate, channels, lag (review-1 #12: a pitch test that checks only F-10 and the length passes on rubberband's smeared output).
- **Each measure:** the right number on a fixture with a known answer; its listed false readings tested as such; the moved `cue_check` measures equal their golden JSON.
- **Planted faults, a named list:** an off-by-one window, a channel swap, a wrong sample rate, an uncompensated latency, each review §4 false reading; each must make a test fail.
- **Reproducibility:** `render` in two separate processes gives the same pre-encode audio hash.
- **ffmpeg tests** skip with a reason where ffmpeg is missing; the gate prints how many were skipped.

## 10. Build order (each a commit with the gate passing)
1. **ffmpeg adapter spike** (G-7: rate, channels, length, lag; `-threads 1`; float32 WAV in and out; latency per filter measured and compensated) and `doctor`. Golden JSON of the current `cue_check` captured.
2. Measures and pictures (with `cue_check.py` as the wrapper); the intake decode; export as FLAC (G-1, G-8 settled here, because F-03 and the hash depend on them).
3. The numpy operations, the two-pass recipe and `render` with its log and the family checks.
4. The ffmpeg operations (`denoise`, `declick`, `pitch`, `stretch`, `chorus`) with their guards.
5. `rank`.
6. Layers, loops, variants.
7. `generate` (after the owner's guide).
8. The books: craft-process §5-§6, review §4, the prompt book (from the guide), `roblox-audio.md` (map §6), the cue card fields (§7), the role file without the listening check-ins (J020-LD3); workflow map §3 step 8 says FLAC.
9. One real cue set end to end, then G3.

## 11. Risks and open checks
| Risk or open check | Plan |
| --- | --- |
| A measure or a filter gives a wrong number or a shifted sound with no error | G-7 after every external step; false readings per measure; fixtures with known answers; planted faults |
| Roblox's transcode codec and how far it overshoots the true peak | not documented; the first upload in a real game is measured (upload, play, capture), then the `peak` margin is set |
| How a stereo file plays on an AudioEmitter | a Studio probe in the first real game |
| Whether the owner's plan allows WAV output (Pro tier or above) | `generate` tries WAV first and logs the format it got |
| A sound passes every number and still feels wrong | said plainly in every report; the owner's play-test is the judge (J020-D3) |
| The recipe language grows into a second program | only the operations above; a new one is added with its test, when a real cue needs it |
