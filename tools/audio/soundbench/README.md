# tools/audio/soundbench: the kit's audio editor for an agent

> Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2). Kit tool (universal). Design: `knowledge/jobs/J020-sound-workbench/editor-design.md`.

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

`tools/audio/cue_check.py` still works with the same command line and output: it is a thin wrapper over `measures.py` (G-3).

## Guarantees (and the test that holds each)

| # | Guarantee | Held by |
| --- | --- | --- |
| 1 | After every ffmpeg call: same rate, same channels, same length (unless declared), no NaN, **lag 0 by cross-correlation**. A measured lag is compensated only when the correlation is clear and the lag is within the call's declared `max_lag_ms`; otherwise `SoundbenchError`. The input is padded with `max_lag_ms` of silence, so the tail is not cut | `test_soundbench_ffmpeg.py` (afftdn at 44.1/48 kHz, mono/stereo; refused rate, channel, length changes; undeclared latency; unprovable timing) |
| 2 | The channel order is kept (a swap is refused: the mono-sum lag check cannot see it) | `test_a_channel_swap_is_refused` |
| 3 | ffmpeg runs with `-threads 1 -filter_threads 1`, float32 WAV in and out: the same call gives the same samples | `test_same_call_twice_gives_the_same_samples` |
| 4 | F-01 to F-13 equal the old `cue_check.py` output number for number (golden JSON from git 78c730f, 55 cases) | `test_soundbench_measures.py` `GoldenTest` |
| 5 | Intake decodes an MP3 once to a float32 master with no resampling; rate and channels match the stream; the length matches the asked duration within 10 ms (an untagged MP3 decodes 25 ms late and is refused); a master is never overwritten; the take's sidecar gets the hashes, decoder and version | `test_soundbench_io.py` `IntakeTest` |
| 6 | Export is FLAC 24-bit at the given rate; a different source rate, a rate over 48 kHz, samples at full scale, over 7 minutes or over 20 MB are refused (no file left); the read-back is within one 24-bit step; the log holds the float32 audio sha256, the encode settings and tool versions; two processes give the same hashes | `ExportTest` |
| 7 | Measuring and filtering never change the input buffer | `test_measuring_never_changes_the_audio`, `test_the_input_buffer_is_not_changed` |

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
| lag (`compare`, the adapter) | cross-correlation of the mono sums | periodic, silent, noise-only or inverted input reads "not clear" |

PROPOSAL values (start points a check may change): the click factor 8, the flatness limits 0.05 / 0.30, the lag limits (correlation 0.5, second peak under 90 %), the intake tolerance 10 ms.

## Known limits

- **Speed on long files:** F-09 and F-10 (moved unchanged from cue_check) find their loudest 400 ms and 200 ms windows with `np.convolve`, which grows with file length times window length: a 2-minute music bed takes minutes. The new measures use cumulative sums (120 s stereo: about 2 s). A faster F-09/F-10 needs its own golden check before it replaces the old arithmetic.
- **Lag on periodic sounds:** a steady tone or a loop correlates equally at every period, so the adapter refuses it ("timing cannot be proven"). Filters for loops are checked on a non-periodic stand-in or get their own guard in step 4.
- **Intake takes MP3 only.** A WAV or PCM take from ElevenLabs (design section 8) needs its own intake path in step 7.

## Not built yet (design section 10, steps 3-9)

The numpy operations, recipes and `render` with its log and family checks; the ffmpeg operations (`denoise`, `declick`, `pitch`, `stretch`, `chorus`) and their guards, including how a time-stretch is checked for timing; `rank`; layers, loops, variants; `generate`; the Ogg path for files over 20 MB.

## Python use

```python
from tools.audio.soundbench import ffmpeg, measures, intake, export, pictures
res = ffmpeg.run_filter(x, 44100, "afftdn", max_lag_ms=50)   # res.audio, res.lag_samples, res.log
rec = measures.measure(path)
info = intake.decode_take(take_mp3, expected_ms=1500)
log = export.export_flac(x, 44100, out_flac, source_rate=44100)
```

Fixtures for tests and probes: `fixtures.make(name, rate, channels)` (no audio files in the repo).
