# tools/audio/soundbench: the kit's audio editor for an agent

> Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 steps 1-5; repair rounds 2 and 3). Kit tool (universal). Design: `knowledge/jobs/J020-sound-workbench/editor-design.md`.

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
| `render <cue-folder> [--picture] [--json]` | applies `recipe.json` to the take, exports FLAC, re-measures the delivered file against `card.json`, runs the paid-reveal family check. Exit 0 every must-target passed; 1 a must-target, the level or the family check failed (the file is still written, the report says why); 2 refused (also any malformed input or unexpected error); 3 a paid-reveal family is incomplete: re-render after the siblings |
| `rank <cue-folder> [--round K] [--picture] [--json]` | scores every take of one round (`takes/<cue>.r<k>.t<n>.mp3`, the highest round unless `--round`; round 4 refused, J020-D7) against `card.json`, computes which misses the edit pass can fix, orders the takes and proves the top take's fix with a real render on a temp copy (section below). Writes `report/<cue>.r<k>.rank.json` and `.md` only. Exit 0 the top take passes every must-target after its fixable steps; 1 no take does: regenerate with a changed prompt, or after round 3 the cue goes to the owner with its numbers; 2 refused (bad input, a changed take, an inconsistent family, or rank and render disagree) |

## A cue folder (design section 2)

`content/audio/<cue-id>/`: `card.json` (kind, category, tier, level with its measure, targets with `must` or aim, key, form, family, playback), `recipe.json` (the take and the two passes), `takes/<cue>.r<k>.t<n>.mp3` with its sidecar `.json` (the intake record) and `.master.wav`, and after `render`: `out/<cue>.flac`, `out/<cue>.log.json` (every step with its parameters, its numbers and a before/after snapshot), `report/<cue>.render.json` and `.md`, and pictures when a target misses, for important cues, or with `--picture`. The schemas with an example are in the `card.py` docstring; kinds and scales are data in `tables.json`.

## Operations (design section 4)

Design pass, in the SC-09 order clean > pitch > eq > compress > add > compress again > transient > air (a step out of order needs a `why`, otherwise refused):

| Stage | Operation | What it guarantees (tested) |
| --- | --- | --- |
| clean | `dc`, `highpass`, `lowpass` (RBJ biquads, order 2 or 4) | -3.01 dB at f0, the same curve as `scipy.signal.butter`; onset kept |
| clean | `denoise` (ffmpeg afftdn) | nf at most 3 dB above the take's measured tail floor (default: that floor; afftdn is absolute dBFS, so a fixed nf ate quiet takes); latency 1,102 / 1,200 samples compensated per channel; level, length above the floor, balance, attack share, main transient (1 ms), roughness kept |
| clean | `declick` (ffmpeg adeclick) | sustained and loop kinds only; latency 0; read with wrap/reflect context so its start-up ramp stays outside the sound |
| clean | `dehum` (50/60 Hz notches and harmonics), `gate` (tail floor; lookahead, so the attack is passed exactly) | hum down 30 dB or more; attack untouched |
| pitch | `varispeed` (scipy resample_poly) | pitch within 0.5 cent, length changes with it; the default for percussive takes |
| pitch | `pitch` and `stretch` (ffmpeg rubberband, `transients=smooth`) | sustained kinds only; pitch within 5 cents of the asked shift on a trusted note; its broadband level loss (0.4-4.3 dB measured) restored by gain, more than 6 dB refused; event positions (click probe, the audio, a stand-in of the kind) within 1 ms + 3 ms per semitone (pitch, at most 3 semitones) or 2 ms + 40 ms x abs(ratio - 1) (stretch, ratio 0.8-1.25: the measured shift is about 40 ms x abs(ratio - 1)); length x ratio; roughness rise at most 0.05 |
| pitch | `to_key` | refused when F-10 is untrusted; moves to the nearest note of the card's key |
| eq | `eq` (bell, low shelf, high shelf, notch) | the asked gain at f0 within 0.5 dB (the `sosfreqz` value within 0.05 dB); a boost over 6 dB needs a `why` |
| compress | `compress` (soft knee; threshold in dB below the input's own peak), `limit` (lookahead true-peak, absolute dBTP ceiling) | the static curve within 0.2 dB on a steady tone; a quiet take is compressed exactly as the same take normalised; the limiter holds the true-peak ceiling (x4) and reports its deepest reduction; on sfx and ui a transient cut over 0.5 dB needs a `why` |
| add | `space` (generated tail, RT60 at most 1.5 s: never a room, J020-D10), `echo`, `chorus` (ffmpeg, latency 0, its tail declared; the audio timed on its dry path, the full graph on the probe and a stand-in; decay at 0.9 x in_gain or more is refused at the parameter check: a wet copy as strong as the dry one cannot be timed) | the dry sound untouched before onset + predelay; RT60 within 20 %; echo exact |
| transient | `transient` (fast vs slow peak follower) | attack up raises the attack share; sustain down lowers the tail; a steady tone untouched |
| air | `saturate` (tanh soft clip relative to the input's own peak) | exactly its formula pk tanh(g x / pk) / tanh(g); a quiet take is saturated exactly as the same take normalised; logs the nonlinear residual over the whole file (`residual_db`) and over the body outside the peak +-10 ms (`residual_body_db`: the peak-relative drive hits a transient hard and the body hardly), and the phone loss before and after |

Edit pass, always in this order whatever the recipe lists (the log says when it reordered): `trim` (to the kind's onset binding: rising kinds to F-01, hits to the main transient, 1 ms preroll faded when not silent; a first sample above peak - 60 dB gets a 0.5 ms fade from sample 0, since 7 of 10 real takes started mid-waveform; it logs the first-sample level, the attack share before and after the fade and `lead_in_ms`; when the fade leaves under 90 % of the attack share it still fades (a click is worse) and logs `edge_fade_attack_loss`, and the card's attack targets decide) > `cut` (a cut through sound needs a fade-out of 5 ms or more) > `fade` (a fade-in that softens the attack needs a `why`) > `mono` > `loudness` (the card's own level measure: F-09, F-13a or LUFS-I for 0.4 s or more, within 0.05 dB) > `peak` (true-peak ceiling minus a 0.5 dB margin, by gain only, never a limiter) > `export` (FLAC).

Design-pass dynamics (`compress`, `saturate`, `gate`) are relative to the take's own peak, so a quiet take and a loud one are shaped the same; the edit pass sets the absolute level. The limiter's ceiling stays absolute: it is a delivery limit.

Every ffmpeg operation is guarded after it runs, in both directions where both are damage: F-09 within +-1.5 dB; the part of the sound 10 dB over its floor keeps 85 % of its length (x ratio for stretch); the channel balance within 1 dB; a sound with an attack (attack share 0.02 or more) keeps its share within 80-125 %, its rise within +-2 ms and its main transient within 1 ms. chorus changes level and envelope by design: it is guarded on timing and balance (2 dB) only. Channels that correlate 0.9 or more (real takes are often near-mono) are checked for a swap by level order only. The review-1 cases are refused: rubberband on a 400 ms hit, adeclick on a clean hit (even when mislabelled sustained); and the repair-round case: denoise nr 40 nf -20 on a take peaking at -36 dBFS (refused by the nf check and, without it, by the level guard).

`tools/audio/cue_check.py` still works with the same command line and output: it is a thin wrapper over `measures.py` (G-3).

## Guarantees (and the test that holds each)

| # | Guarantee | Held by |
| --- | --- | --- |
| 1 | After every ffmpeg call: same rate, same channels, same length (unless declared), no NaN, and **every channel's lag, measured against its own input channel, equals the call's declared latency** (`latency_samples`, from `ffmpeg.known_latency`; tolerance 0 samples). Channels that disagree, or a lag other than the declared one, are refused (G-7: a known latency is compensated, an unknown one refused). Compensation shifts by the declared value; the input is padded by it, so the tail is not cut. When the audio gives no clear reading (a tone, a chime, a loop) the latency is proven on a probe signal (a noise burst per channel) through the same graph, and the log says `timing_source: probe` | `test_soundbench_ffmpeg.py` (afftdn on every fixture at 44.1/48 kHz; one channel moved; `afftdn,lowpass` and `afftdn,aphaser` refused; declared value off by one refused; refused rate, channel, length changes; unprovable timing) |
| 2 | The channel order is kept (a swap is refused: the mono-sum lag check cannot see it) | `test_a_channel_swap_is_refused` |
| 3 | ffmpeg runs with `-threads 1 -filter_threads 1`, float32 WAV in and out: the same call gives the same samples | `test_same_call_twice_gives_the_same_samples` |
| 4 | F-01 to F-13 equal the old `cue_check.py` output number for number (golden JSON from git 78c730f, 55 cases) | `test_soundbench_measures.py` `GoldenTest` |
| 5 | Intake decodes an MP3 once to a float32 master with no resampling; rate and channels match the stream; the decoded length matches the file's own stated length within 10 ms; a stream that states no encoder delay (an untagged MP3: it decodes 25 ms late and states its wrong length) is refused; the requested length is logged beside the received one, with a warning over 10 ms, never a refusal (LD-b: real 0.5 s requests come back 480 ms); a master is never overwritten; the take's sidecar gets the hashes, decoder and version | `test_soundbench_io.py` `IntakeTest` |
| 6 | Export is FLAC 24-bit at the given rate; a different source rate, a rate over 48 kHz, samples at full scale, over 7 minutes or over 20 MB are refused (no file left); the read-back is within one 24-bit step; the log holds the float32 audio sha256, the encode settings and tool versions; two processes give the same hashes | `ExportTest` |
| 7 | Measuring and filtering never change the input buffer | `test_measuring_never_changes_the_audio`, `test_the_input_buffer_is_not_changed` |
| 8 | `render` checks the take's file sha256 and the master's audio sha256 against the sidecar before reading anything (G-1: originals never change), checks every parameter and the SC-09 order before touching audio, and logs every step with before/after numbers (G-2) | `test_soundbench_render.py` |
| 9 | Same recipe, same audio: two separate processes render the same pre-encode audio sha256 (G-1) | `test_g1_two_processes_render_the_same_audio` |
| 10 | A paid-reveal family is checked from every member: each member's card must declare the same family id, paid_reveal and member set; no other card may list a member one-sided, and every card that declares the same family id must be in the member set (two pairs sharing one id are refused, R2-1) (exit 2, before any audio). Every member's render re-checks the whole family on the current delivered files: F-13 b within 1 LU and F-03 sample peaks within 1 dB; a member not rendered yet is exit 3, never a pass (LD-a); the family state is written beside the cue folders as `<family-id>.family.json` with each member's file sha256 | `test_paid_reveal_family_check`, `test_a_one_sided_family_is_refused_from_both_sides` |

## New measures (design section 5)

In `measure` output next to F-01..F-12. Known false readings are in each function's docstring in `measures.py`; the main ones:

| Key | Measure | Watch for |
| --- | --- | --- |
| `main_transient_ms` | first point of the 1 ms envelope within 10 dB of its maximum | a rising sound is late by design |
| `attack_rise_ms` | 10 % to 90 % of the 1 ms envelope | cannot read a rise under about 2 ms |
| `attack_share_5ms` | energy in the first 5 ms after F-01 / the F-12 sound's energy | a noise head moves the onset |
| `phone_loss_db` | dB lost through a 400 Hz high-pass and 10 kHz low-pass (4th order) | a rough phone model |
| `tail_noise` | floor after the F-12 sound (or the last 100 ms) and signal-to-noise | `sound_reaches_end` true: the floor is the sound itself |
| `clicks` | steps over 8x the local step RMS (±2 ms) and 1 % of the peak, every channel; `edges`: a first or last sample, as stored (before the mean is removed: playback starts from it), at 1 % of the peak or more (card target `edge_clicks`) | a hard edge from silence reads as a click; a click in loud noise hides; a loop's end edge is its seam |
| `tonality` | spectral flatness (tonal / mixed / noisy) and the notes present | harmonics are listed as notes |
| `roughness` | depth of 30-150 Hz envelope movement | two close notes beating read rough |
| lag (`compare`; the adapter per channel) | cross-correlation, mean removed | periodic, silent or inverted input reads "not clear" |

PROPOSAL values (start points a check may change; each is a named constant in its module): the click factor 8, the flatness limits 0.05 / 0.30, the lag limits (correlation 0.5, second peak under 90 %), the intake tolerance 10 ms, the latency tolerance 0 samples, the denoise nf margin 3 dB, the level guard 1.5 dB, the length keep 85 %, the balance 1 dB (chorus 2 dB), the channels-alike correlation 0.9, the rubberband loss limit 6 dB, the edge fade 0.5 ms, the chorus wet limit 0.9 x in_gain (measured: the probe first fails at 0.90), the saturate body window +-10 ms; rank: near-silent -60 dBFS, clipped 10 ms or more at or above -1 dBFS, a missing band under a tenth of its minimum, the fix fade-out 10 ms, the cut 1 ms inside, the `near` margins in `tables.json`.

## Known limits

- **Speed on long files:** F-10 (moved unchanged from cue_check) finds its loudest 200 ms window with `np.convolve`, which grows with file length times window length: a 2-minute music bed takes minutes. F-09 now uses a cumulative sum over the same 400 ms windows (J020 step 5: the convolve was 97 % of a rank's time; the 55-case golden test passes and the old and new arithmetic differ by under 1e-13 dB on every fixture); the new measures use cumulative sums too. A faster F-10 needs the same golden check before it replaces the old arithmetic.
- **Lag on periodic sounds:** a steady tone or a loop correlates equally at every period, so its timing is proven on the probe signal, not on the audio itself (the log says so). That proves the graph's latency, not that this audio came out aligned.
- **Known latencies are measured per rate:** afftdn 1,102 samples at 44.1 kHz, 1,200 at 48 kHz on ffmpeg 9.0.2. Not a formula (22,050 Hz reads 550, not round(0.025 x rate) = 551): other rates and other filters are refused until measured and added to `KNOWN_LATENCY`.
- **Intake takes MP3 only.** A WAV or PCM take from ElevenLabs (design section 8) needs its own intake path in step 7.

- **rubberband is not sample-exact.** Even in smooth mode it moves events about 2.6-2.9 ms per semitone and about 40 ms x abs(ratio - 1) when stretching; the guards bound that (and refuse more), they cannot remove it. Hence sustained kinds only, pitch within 3 semitones and stretch within 0.8-1.25. Its default (crisp) mode put 12-27 % amplitude modulation and up to 9.5 cents of pitch error on a steady tone, so soundbench always uses `transients=smooth`.
- **Denoise on a noise-only sound** (a whoosh made of noise) can move its swell: afftdn cannot tell such a sound from noise; the main-transient guard refuses it when it does (17.7 ms on the quiet whoosh fixture at 44.1 kHz).
- **The compressor's detector ripples** on low tones: its static curve holds within 0.2 dB on a steady sine, not exactly.

## Real takes

`tools/tests/test_soundbench_realtakes.py` runs every check above on real ElevenLabs takes when `SOUNDBENCH_REAL_TAKES` names a folder of MP3s (with their sidecars), and skips with the reason otherwise; no audio is committed. Fixtures modelled on real takes (peaks -24 to -36 dBFS, a mid-waveform start, 480 ms, channels 1.1 dB apart) are `fixtures.make_real(name, rate)`.

## Ranking takes (`rank`, design section 6)

Every number in the rank table is a measure of `measures.py` scored by `render.evaluate` (the function `render` uses on the delivered file), so a reader can recompute it.

1. **Rejected outright** (no fix is claimed): clipped at the source (10 ms or more in total at or above -1 dBFS, read against full scale, never the decoded take's own peak: the MP3 decoder overshoots above a clipped plateau. The 62 clean real takes read at most 7.23 ms at 128k and 5.78 ms re-encoded at 192k: a 2.8 ms margin. Hard-clipped and MP3 round-tripped copies of the same takes: caught at 128k / 192k +12 dB 37 / 39 of 62, +6 dB 24 / 24, +3 dB 15 / 15, +1 dB 2 / 2. Sustained takes (whooshes, notes, swishes) are caught at every gain; **short hits are not caught even at +12 dB** (3-9.5 ms): their clipped tips last under a millisecond each and the MP3 smears them, and no feature tried separated them from clean full-scale hits with a margin); near-silent (sample peak under -60 dBFS; the quietest real take peaks at -43.9); no sound in a band the card needs (a `must` band share under a tenth of its minimum).
2. **Each target scored**: `inside`, `near` (inside but within the `near` margin in `tables.json`; still a pass, as render counts it) or `miss`, with `miss_by` (how far outside) or `margin` (how far inside).
3. **Fixable is computed, never guessed.** The edit-pass steps for the take's misses (a late onset or main transient, or a click at the start edge: `trim`; sound or file too long: `cut` 1 ms inside the maximum with a 10 ms fade-out, planned on the audio after `trim`, since trimming moves the length; a click at the end edge: `fade`; `mono`; then `loudness` and `peak` whenever any step runs, `peak`'s ceiling the lowest of -1.0, the card's true-peak max and its sample-peak max) are run through render's own step loop (`render.apply_steps`), measured again and scored again. **Three plans are scored**: every miss, the must misses only, and no step; the fewest must misses after it wins, then the fewest aim misses, then the order all > must > none. So an aim fix that breaks a must (the level reset after a trim, on a take whose true peak sits between the peak limit and the card's max) never turns a usable take into a regenerate; the aim fixes left out are reported. A plan an operation refuses (a cut that leaves LUFS-I under 0.4 s) is recorded and its reason is written into every miss it leaves. A miss counts as fixed only when its re-measured row passes; a row the fix itself breaks is listed under `introduced`. Anything no edit-pass step moves (bands, phone loss, flatness, attack, key, too short or too early) is a prompt miss: rank does not compute design steps.
4. **The level is derived as well as simulated** (review-1 #9: `peak` is gain only, sfx and ui do not limit transients): `gain_needed` = the gain `loudness` applied (the ratio of the peaks; for F-09 it is `target - level_in`, for F-13a and LUFS-I on a quiet take it is not, because the -70 LUFS absolute gate moves blocks as the gain changes), `peak_limit = min(-1.0, card true_peak max, card sample_peak max) - 0.5`, `headroom = peak_limit - true_peak_in`, `peak_cut = max(0, true_peak_in + gain_needed - peak_limit)`, `predicted = level after loudness - peak_cut`; it fits when `|predicted - target| <= tolerance`. The derived and the simulated level must agree within 0.1 dB, or rank refuses (exit 2). A take too loud always fits. For music, ambience and voice the reason adds that a `limit` design step could make room (not computed).
5. **Order** (`rank_key`): rejected last; then a take that passes after its fix before one that does not; then fewest must-misses after the fix, fewest aim-misses after it, fewest misses that needed a fix, fewest near readings, the take number. A must-miss never ranks above a pass.
6. **Proof**: the top take's fix recipe (empty design pass) is rendered for real on a temp copy of the cue (hash checks, parameter checks, edit pass, FLAC export, the delivered file measured again); every target row must match the simulation (values within 0.02 or 0.2 %), or rank refuses. The copy is removed; rank never writes `out/` or `<family-id>.family.json`.
7. **Verdict**: `use` (the top take and its edit steps, a start for `recipe.json`), `regenerate` (round 1 or 2: the targets still missed after the fix, how many takes miss each, the closest value and its direction) or `owner` (round 3, J020-D7). Takes per round other than minor 3, frequent 4, important 6 (J020-D9) is a warning.
8. **Pictures** (light-check rule): the top take before and after its fix when an after-fix row misses or reads near, or for an important cue; `--picture` draws every take.

Paid-reveal families: rank refuses an inconsistent family declaration exactly as `render` does (exit 2) and never checks or writes D-03 state; `render` still runs F-13 b and the F-03 1 dB check on every member's delivered file.

Known limits: rank computes edit-pass fixes only, so a miss an `eq` or `limit` design step could close reads as a prompt miss (the sound designer may still try it; `render` measures the result). The clip check cannot see clipping that was scaled down after it happened, clipping under full scale (a ceiling at -0.9 dBFS was caught on 1 of 9 copies), or a clipped short hit after MP3 (not caught even at +12 dB), and a sustained low tone normalised to full scale can read clipped. A clipped hit that passes rank reads as a level miss at most (`peak` cannot repair distortion): the owner's play-test is the check.

## Not built yet (design section 10, steps 6-9)

Layers (several takes, `align`), loops (`loop_bed`, `loop_music`), variants (step 6); `generate` (step 7); the books (step 8); the Ogg path for files over 20 MB. Flanger, a second exciter and `anlmdn` are not built (design section 4).

## Python use

```python
from tools.audio.soundbench import ffmpeg, measures, intake, export, pictures, ops, render
res = ffmpeg.run_filter(x, 44100, "afftdn", latency_samples=ffmpeg.known_latency("afftdn", 44100))  # 1102
rec = measures.measure(path)
info = intake.decode_take(take_mp3, requested_ms=500)   # the length asked of the service (logged, never refused)
log = export.export_flac(x, 44100, out_flac, source_rate=44100)
y, info = ops.run("eq", x, 44100, ops.check_params("eq", {"bands": [...]}), ctx)   # ctx: kind, category, binding, level
doc, code = render.render(Path("content/audio/SFX-COMBAT-HIT"))
```

Fixtures for tests and probes: `fixtures.make(name, rate, channels)` (no audio files in the repo).
