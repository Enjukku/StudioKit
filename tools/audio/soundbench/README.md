# tools/audio/soundbench: the kit's audio editor for an agent

> Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 steps 1-4). Kit tool (universal). Design: `knowledge/jobs/J020-sound-workbench/editor-design.md`.

Built for an agent that cannot hear (J020-D2): text in, numbers and pictures out. Its first duty is to give right numbers and **never shift or damage a sound without an error**. Every number is a screening aid, never a taste verdict (G-4): the owner judges in play-tests (J020-D3).

Needs Python 3.11, numpy, scipy, soundfile, pyloudnorm, matplotlib, and ffmpeg (tested on 9.0.2). No network calls.

## Commands

`python -m tools.audio.soundbench <command>` from the repo root. Exit 0 done, 1 doctor found a missing item, 2 refused or failed (reason on stderr).

| Command | Does |
| --- | --- |
| `doctor [--root DIR] [--json]` | Python and libraries (FLAC in libsndfile, matplotlib Agg); ffmpeg found (`SOUNDBENCH_FFMPEG`, then PATH, then the WinGet folder) and how; its version (another version than 9.0.2 is a WARN: re-run the tests); the filters `afftdn`, `adeclick`, `rubberband`, `chorus`; the MP3 decoder; a live G-7 self-test (afftdn's lag measured and compensated to 0); the `ELEVENLABS_API_KEY` entry in `knowledge/design/keys.json` (the key file is only checked to exist, never opened) |
| `measure <file> [--low-cut HZ] [--high-pitch] [--json] [--picture PNG]` | F-01 to F-12 and the new measures (below); `--picture` writes a waveform + spectrogram PNG |
| `compare <a> <b> [--json]` | every measure of two files side by side with `b - a`, and the lag of b behind a (same rate only) |
| `parity <files> --mode integrated\|momentary [--json]` | F-13 loudness parity (integrated: options and siblings; momentary: paid random results) |
| `render <cue-folder> [--picture] [--json]` | applies `recipe.json` to the take, exports FLAC, re-measures the delivered file against `card.json`, runs the paid-reveal family check. Exit 0 every must-target passed; 1 a must-target, the level or the family check failed (the file is still written, the report says why); 2 refused |

## A cue folder (design section 2)

`content/audio/<cue-id>/`: `card.json` (kind, category, tier, level with its measure, targets with `must` or aim, key, form, family, playback), `recipe.json` (the take and the two passes), `takes/<cue>.r<k>.t<n>.mp3` with its sidecar `.json` (the intake record) and `.master.wav`, and after `render`: `out/<cue>.flac`, `out/<cue>.log.json` (every step with its parameters, its numbers and a before/after snapshot), `report/<cue>.render.json` and `.md`, and pictures when a target misses, for important cues, or with `--picture`. The schemas with an example are in the `card.py` docstring; kinds and scales are data in `tables.json`.

## Operations (design section 4)

Design pass, in the SC-09 order clean > pitch > eq > compress > add > compress again > transient > air (a step out of order needs a `why`, otherwise refused):

| Stage | Operation | What it guarantees (tested) |
| --- | --- | --- |
| clean | `dc`, `highpass`, `lowpass` (RBJ biquads, order 2 or 4) | -3.01 dB at f0, the same curve as `scipy.signal.butter`; onset kept |
| clean | `denoise` (ffmpeg afftdn) | latency 1,102 / 1,200 samples compensated per channel; attack share, main transient (1 ms), roughness kept |
| clean | `declick` (ffmpeg adeclick) | sustained and loop kinds only; latency 0; read with wrap/reflect context so its start-up ramp stays outside the sound |
| clean | `dehum` (50/60 Hz notches and harmonics), `gate` (tail floor; lookahead, so the attack is passed exactly) | hum down 30 dB or more; attack untouched |
| pitch | `varispeed` (scipy resample_poly) | pitch within 0.5 cent, length changes with it; the default for percussive takes |
| pitch | `pitch` and `stretch` (ffmpeg rubberband, `transients=smooth`) | sustained kinds only; pitch within 5 cents of the asked shift on a trusted note; event positions (click probe, the audio, a stand-in of the kind) within 1 ms + 3 ms per semitone (pitch, at most 3 semitones) or 15 ms (stretch, ratio 0.5-2), length x ratio; roughness rise at most 0.05 |
| pitch | `to_key` | refused when F-10 is untrusted; moves to the nearest note of the card's key |
| eq | `eq` (bell, low shelf, high shelf, notch) | the asked gain at f0 within 0.5 dB (the `sosfreqz` value within 0.05 dB); a boost over 6 dB needs a `why` |
| compress | `compress` (soft knee), `limit` (lookahead true-peak) | the static curve within 0.2 dB on a steady tone; the limiter holds the true-peak ceiling (x4) and reports its deepest reduction; on sfx and ui a transient cut over 0.5 dB needs a `why` |
| add | `space` (generated tail, RT60 at most 1.5 s: never a room, J020-D10), `echo`, `chorus` (ffmpeg, latency 0, its tail declared) | the dry sound untouched before onset + predelay; RT60 within 20 %; echo exact |
| transient | `transient` (fast vs slow peak follower) | attack up raises the attack share; sustain down lowers the tail; a steady tone untouched |
| air | `saturate` (tanh soft clip) | exactly its formula |

Edit pass, always in this order whatever the recipe lists (the log says when it reordered): `trim` (to the kind's onset binding: rising kinds to F-01, hits to the main transient, 1 ms preroll faded when not silent; logs `lead_in_ms`) > `cut` (a cut through sound needs a fade-out of 5 ms or more) > `fade` (a fade-in that softens the attack needs a `why`) > `mono` > `loudness` (the card's own level measure: F-09, F-13a or LUFS-I for 0.4 s or more, within 0.05 dB) > `peak` (true-peak ceiling minus a 0.5 dB margin, by gain only, never a limiter) > `export` (FLAC).

Every ffmpeg operation is guarded after it runs: a sound with an attack (attack share 0.02 or more) keeps 80 % of its share (not for chorus, whose copies add energy after the attack by design), its main transient within 1 ms and its rise within +2 ms. The review-1 cases are refused: rubberband on a 400 ms hit, adeclick on a clean hit (even when mislabelled sustained).

`tools/audio/cue_check.py` still works with the same command line and output: it is a thin wrapper over `measures.py` (G-3).

## Guarantees (and the test that holds each)

| # | Guarantee | Held by |
| --- | --- | --- |
| 1 | After every ffmpeg call: same rate, same channels, same length (unless declared), no NaN, and **every channel's lag, measured against its own input channel, equals the call's declared latency** (`latency_samples`, from `ffmpeg.known_latency`; tolerance 0 samples). Channels that disagree, or a lag other than the declared one, are refused (G-7: a known latency is compensated, an unknown one refused). Compensation shifts by the declared value; the input is padded by it, so the tail is not cut. When the audio gives no clear reading (a tone, a chime, a loop) the latency is proven on a probe signal (a noise burst per channel) through the same graph, and the log says `timing_source: probe` | `test_soundbench_ffmpeg.py` (afftdn on every fixture at 44.1/48 kHz; one channel moved; `afftdn,lowpass` and `afftdn,aphaser` refused; declared value off by one refused; refused rate, channel, length changes; unprovable timing) |
| 2 | The channel order is kept (a swap is refused: the mono-sum lag check cannot see it) | `test_a_channel_swap_is_refused` |
| 3 | ffmpeg runs with `-threads 1 -filter_threads 1`, float32 WAV in and out: the same call gives the same samples | `test_same_call_twice_gives_the_same_samples` |
| 4 | F-01 to F-13 equal the old `cue_check.py` output number for number (golden JSON from git 78c730f, 55 cases) | `test_soundbench_measures.py` `GoldenTest` |
| 5 | Intake decodes an MP3 once to a float32 master with no resampling; rate and channels match the stream; the length matches the asked duration within 10 ms (an untagged MP3 decodes 25 ms late and is refused); a master is never overwritten; the take's sidecar gets the hashes, decoder and version | `test_soundbench_io.py` `IntakeTest` |
| 6 | Export is FLAC 24-bit at the given rate; a different source rate, a rate over 48 kHz, samples at full scale, over 7 minutes or over 20 MB are refused (no file left); the read-back is within one 24-bit step; the log holds the float32 audio sha256, the encode settings and tool versions; two processes give the same hashes | `ExportTest` |
| 7 | Measuring and filtering never change the input buffer | `test_measuring_never_changes_the_audio`, `test_the_input_buffer_is_not_changed` |
| 8 | `render` checks the take's file sha256 and the master's audio sha256 against the sidecar before reading anything (G-1: originals never change), checks every parameter and the SC-09 order before touching audio, and logs every step with before/after numbers (G-2) | `test_soundbench_render.py` |
| 9 | Same recipe, same audio: two separate processes render the same pre-encode audio sha256 (G-1) | `test_g1_two_processes_render_the_same_audio` |
| 10 | A paid-reveal family passes only when F-13 b momentary maxima are within 1 LU and F-03 sample peaks within 1 dB across rendered siblings; a sibling not rendered yet is not a pass (D-03) | `test_paid_reveal_family_check` |

## New measures (design section 5)

In `measure` output next to F-01..F-12. Known false readings are in each function's docstring in `measures.py`; the main ones:

| Key | Measure | Watch for |
| --- | --- | --- |
| `main_transient_ms` | first point of the 1 ms envelope within 10 dB of its maximum | a rising sound is late by design |
| `attack_rise_ms` | 10 % to 90 % of the 1 ms envelope | cannot read a rise under about 2 ms |
| `attack_share_5ms` | energy in the first 5 ms after F-01 / the F-12 sound's energy | a noise head moves the onset |
| `phone_loss_db` | dB lost through a 400 Hz high-pass and 10 kHz low-pass (4th order) | a rough phone model |
| `tail_noise` | floor after the F-12 sound (or the last 100 ms) and signal-to-noise | `sound_reaches_end` true: the floor is the sound itself |
| `clicks` | steps over 8x the local step RMS (±2 ms) and 1 % of the peak, every channel | a hard edge from silence reads as a click; a click in loud noise hides |
| `tonality` | spectral flatness (tonal / mixed / noisy) and the notes present | harmonics are listed as notes |
| `roughness` | depth of 30-150 Hz envelope movement | two close notes beating read rough |
| lag (`compare`; the adapter per channel) | cross-correlation, mean removed | periodic, silent or inverted input reads "not clear" |

PROPOSAL values (start points a check may change; each is a named constant in its module): the click factor 8, the flatness limits 0.05 / 0.30, the lag limits (correlation 0.5, second peak under 90 %), the intake tolerance 10 ms, the latency tolerance 0 samples.

## Known limits

- **Speed on long files:** F-09 and F-10 (moved unchanged from cue_check) find their loudest 400 ms and 200 ms windows with `np.convolve`, which grows with file length times window length: a 2-minute music bed takes minutes. The new measures use cumulative sums (120 s stereo: about 2 s). A faster F-09/F-10 needs its own golden check before it replaces the old arithmetic.
- **Lag on periodic sounds:** a steady tone or a loop correlates equally at every period, so its timing is proven on the probe signal, not on the audio itself (the log says so). That proves the graph's latency, not that this audio came out aligned.
- **Known latencies are measured per rate:** afftdn 1,102 samples at 44.1 kHz, 1,200 at 48 kHz on ffmpeg 9.0.2. Not a formula (22,050 Hz reads 550, not round(0.025 x rate) = 551): other rates and other filters are refused until measured and added to `KNOWN_LATENCY`.
- **Intake takes MP3 only.** A WAV or PCM take from ElevenLabs (design section 8) needs its own intake path in step 7.

- **rubberband is not sample-exact.** Even in smooth mode it moves events about 2.6-2.9 ms per semitone and 7-12 ms when stretching; the guards bound that (and refuse more), they cannot remove it. Hence sustained kinds only, and pitch within 3 semitones. Its default (crisp) mode put 12-27 % amplitude modulation and up to 9.5 cents of pitch error on a steady tone, so soundbench always uses `transients=smooth`.
- **The compressor's detector ripples** on low tones: its static curve holds within 0.2 dB on a steady sine, not exactly.

## Not built yet (design section 10, steps 5-9)

`rank`; layers (several takes, `align`), loops (`loop_bed`, `loop_music`), variants (step 6); `generate` (step 7); the books (step 8); the Ogg path for files over 20 MB. Flanger, a second exciter and `anlmdn` are not built (design section 4).

## Python use

```python
from tools.audio.soundbench import ffmpeg, measures, intake, export, pictures, ops, render
res = ffmpeg.run_filter(x, 44100, "afftdn", latency_samples=ffmpeg.known_latency("afftdn", 44100))  # 1102
rec = measures.measure(path)
info = intake.decode_take(take_mp3, expected_ms=1500)
log = export.export_flac(x, 44100, out_flac, source_rate=44100)
y, info = ops.run("eq", x, 44100, ops.check_params("eq", {"bands": [...]}), ctx)   # ctx: kind, category, binding, level
doc, code = render.render(Path("content/audio/SFX-COMBAT-HIT"))
```

Fixtures for tests and probes: `fixtures.make(name, rate, channels)` (no audio files in the repo).
