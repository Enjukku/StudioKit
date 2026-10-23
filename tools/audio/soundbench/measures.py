"""Every soundbench measure: F-01 to F-13 (moved from cue_check.py, unchanged in meaning) and the design section 5 measures.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

One way to measure (design G-3): `tools/audio/cue_check.py` is now a thin wrapper over this module, and golden JSON
captured from the old tool (`golden/cue_check_golden.json`) is checked in the tests. Definitions and known false
readings of F-01 to F-13: `.agents/skills/sound-design/references/review.md` section 4. The new measures carry their
false readings in their docstrings. **Every number is a screening aid, never a taste verdict** (design G-4): a FAIL,
or a reading near its limit, is looked at on a waveform and spectrogram before any fix note.

Reading: `soundfile` (always 2-D), the mean of each channel subtracted first (generated audio often carries a DC
offset); mono = the mean of the channels. F-03 true peak needs `scipy`; F-13 needs `pyloudnorm`.

Usage:
  from tools.audio.soundbench import measures
  rec = measures.measure(path)                 # F-01..F-12 plus the new measures
  rec = measures.parity([a, b], "momentary")   # F-13
  lag = measures.lag(reference, candidate, rate, search_samples)
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np

from .core import SoundbenchError

CueError = SoundbenchError  # the name cue_check used

WIN_S = 0.010  # RMS window (F-04, F-05, F-12)
TAIL_DB = 40.0  # F-04 / F-12: a window within this many dB of the loudest still belongs to the sound
ONSET_DB = 30.0  # F-01: first sample within this many dB of the peak
MOMENTARY_S = 0.100  # F-13 (b): window, or the shortest trimmed result if shorter
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# New measures (design section 5). PROPOSAL values: starting points a check may change.
ENV_S = 0.001  # main transient and attack rise: 1 ms RMS envelope
MAIN_TRANSIENT_DB = 10.0  # main transient: first point within this many dB of the envelope maximum
ATTACK_SHARE_S = 0.005  # attack share: the first 5 ms after the F-01 onset
PHONE_HP_HZ, PHONE_LP_HZ = 400.0, 10000.0  # phone-speaker model (design section 5)
TAIL_NOISE_S = 0.100  # noise floor: RMS of the last 100 ms of the file
CLICK_FACTOR = 8.0  # PROPOSAL: a click is a sample step over 8 x the RMS of the steps around it ...
CLICK_LOCAL_S = 0.002  # ... in a centred window of +-2 ms ...
CLICK_MIN_OF_PEAK = 0.01  # ... and at least 1 % of the file's sample peak
TONAL_BELOW, NOISY_ABOVE = 0.05, 0.30  # PROPOSAL: spectral flatness readings
NOTE_PEAK_DB = 20.0  # a note is present when its peak stands 20 dB over the band median (as F-10's trust rule)
NOTE_RANGE_DB = 30.0  # ... and within 30 dB of the strongest peak
ROUGH_BAND_HZ = (30.0, 150.0)  # roughness: envelope movement band
LAG_MIN_CORRELATION = 0.5  # PROPOSAL: lag is "clear" at a normalised correlation of 0.5 or more ...
LAG_MAX_SECOND_PEAK = 0.9  # PROPOSAL: ... and when no other correlation peak reaches 90 % of the best one


# ---------------------------------------------------------------------------------------------------------------
# F-01 to F-13, moved from tools/audio/cue_check.py (git 78c730f). The arithmetic is unchanged; the golden test
# (tools/tests/test_soundbench_measures.py) compares every number with the old tool's output.
# ---------------------------------------------------------------------------------------------------------------

def load(path: Path) -> tuple[np.ndarray, int]:
    try:
        import soundfile as sf
    except ImportError as err:
        raise CueError("needs the soundfile package") from err
    if not path.is_file():
        raise CueError(f"not a file: {path}")
    x, rate = sf.read(str(path), always_2d=True, dtype="float64")
    if len(x) < 2:
        raise CueError(f"{path.name}: fewer than 2 samples")
    return x - x.mean(axis=0), rate


def db(v: float) -> float | None:
    return None if v <= 0 else 20 * math.log10(v)


def windows_rms(mono: np.ndarray, rate: int) -> tuple[np.ndarray, int]:
    n = max(1, int(round(WIN_S * rate)))
    k = len(mono) // n
    if k == 0:
        return np.array([float(np.sqrt(np.mean(mono ** 2)))]), len(mono)
    return np.sqrt(np.mean(mono[: k * n].reshape(k, n) ** 2, axis=1)), n


def onset_index(mono: np.ndarray) -> int:
    peak = float(np.max(np.abs(mono)))
    return int(np.argmax(np.abs(mono) >= peak * 10 ** (-ONSET_DB / 20))) if peak > 0 else 0


def sound_end(mono: np.ndarray, rate: int) -> tuple[int, bool]:
    """F-12 end (sample index, exclusive) and F-04's ends_above_-40 flag."""
    rms, n = windows_rms(mono, rate)
    loud = float(rms.max())
    if loud <= 0:
        return len(mono), False
    above = np.nonzero(rms >= loud * 10 ** (-TAIL_DB / 20))[0]
    last_w = int(above[-1])
    seg_start, seg_end = last_w * n, min(len(mono), (last_w + 1) * n)
    peak = float(np.max(np.abs(mono)))
    inside = np.nonzero(np.abs(mono[seg_start:seg_end]) >= peak * 10 ** (-TAIL_DB / 20))[0]
    end = seg_start + int(inside[-1]) + 1 if len(inside) else seg_end
    return end, last_w == len(rms) - 1


def pitch(mono: np.ndarray, rate: int, high: bool) -> dict:
    n = int(0.2 * rate)
    if len(mono) > n:
        e = np.convolve(mono ** 2, np.ones(n), "valid")
        s = int(np.argmax(e))
        seg = mono[s:s + n]
    else:
        seg = mono
    spec = np.abs(np.fft.rfft(seg * np.hanning(len(seg))))
    f = np.fft.rfftfreq(len(seg), 1 / rate)
    band = (f >= 60) & (f <= (12000 if high else 4000))
    if not band.any() or spec[band].max() <= 0:
        return {"hz": None}
    i = np.nonzero(band)[0][int(np.argmax(spec[band]))]
    hz = float(f[i])
    midi = 69 + 12 * math.log2(hz / 440)
    near = int(round(midi))
    height = db(float(spec[i]) / max(float(np.median(spec[band])), 1e-12))
    return {"hz": round(hz, 2), "note": f"{NOTE_NAMES[near % 12]}{near // 12 - 1}", "cents": round(100 * (midi - near), 1),
            "peak_over_band_median_db": None if height is None else round(height, 1),
            "trusted": height is not None and height >= 20}


def cue_record(path: Path, low_cut: float | None = None, high_pitch: bool = False,
               tool: str = "soundbench measure") -> dict:
    """F-01 to F-12 of one file, in cue_check's record shape (cue_check.measure with a tool label)."""
    x, rate = load(path)
    rec = {"tool": tool, "file": str(path), "rate": rate, "channels": x.shape[1], "verdict":
           "measured (screening aid: look at the waveform before any fix note; review.md section 4)"}
    rec.update(cue_numbers(x, rate, low_cut, high_pitch))
    return rec


def cue_numbers(x: np.ndarray, rate: int, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    """F-01 to F-12 of a loaded buffer (DC already removed, as `load` returns it)."""
    mono = x.mean(axis=1)
    n = len(mono)
    ms = lambda i: round(1000 * i / rate, 2)
    peak = float(np.max(np.abs(x)))
    rec: dict = {}
    on = onset_index(mono)
    end, flag = sound_end(mono, rate)
    rec["F-01_onset_ms"] = ms(on)
    rec["F-02_peak_position_ms"] = ms(int(np.argmax(np.abs(mono))))
    tp = None
    try:
        from scipy.signal import resample_poly
        tp = db(float(np.max(np.abs(resample_poly(x, 4, 1, axis=0)))))
    except ImportError:
        pass
    rec["F-03_peaks"] = {"sample_peak_dbfs": None if db(peak) is None else round(db(peak), 2),
                         "true_peak_dbtp": None if tp is None else round(tp, 2)}
    rec["F-04_tail"] = {"tail_end_ms": ms(end), "ends_above_-40": flag}
    rms, wn = windows_rms(mono, rate)
    li = int(np.argmax(rms))
    loud = float(rms[li])
    after = np.nonzero(rms[li:] <= loud * 10 ** (-20 / 20))[0]
    k100 = li + int(round(0.1 / WIN_S))
    rec["F-05_envelope"] = {"loudest_window_ms": ms(li * wn),
                            "to_minus_20db_ms": None if not len(after) else round(1000 * after[0] * WIN_S, 1),
                            "level_100ms_after_db": None if k100 >= len(rms) or loud <= 0 or rms[k100] <= 0
                            else round(db(float(rms[k100]) / loud), 1)}
    p = np.abs(np.fft.rfft(mono)) ** 2
    f = np.fft.rfftfreq(n, 1 / rate)
    tot = float(p.sum()) or 1.0
    share = lambda lo, hi: round(float(p[(f >= lo) & (f < hi)].sum()) / tot, 4)
    rec["F-06_bands"] = {"below_120": share(0, 120), "120_500": share(120, 500), "500_5k": share(500, 5000),
                         "above_5k": share(5000, rate), **({"below_low_cut": share(0, low_cut)} if low_cut else {})}
    if x.shape[1] > 1:
        mean_ch = float(np.mean(np.sqrt(np.mean(x ** 2, axis=0))))
        mono_r = float(np.sqrt(np.mean(mono ** 2)))
        rec["F-07_mono_drop_db"] = None if mean_ch <= 0 or mono_r <= 0 else round(db(mono_r / mean_ch), 2)
    else:
        rec["F-07_mono_drop_db"] = 0.0
    steps = np.abs(np.diff(mono))
    p95 = float(np.percentile(steps, 95)) if len(steps) else 0.0
    rec["F-08_loop_seam"] = None if p95 <= 0 else round(abs(float(mono[-1] - mono[0])) / p95, 3)
    snd = mono[on:end]
    lvl = f09_rms(snd, rate)
    rec["F-09_loudness_rms_dbfs"] = None if db(lvl) is None else round(db(lvl), 2)
    rec["F-10_pitch"] = pitch(snd if len(snd) > 16 else mono, rate, high_pitch)
    hop = int(0.05 * rate)
    cents = []
    if len(mono) >= 2 * hop:
        frames = [mono[i:i + hop] for i in range(0, len(mono) - hop + 1, hop)]
        en = np.array([float(np.sum(fr ** 2)) for fr in frames])
        ff = np.fft.rfftfreq(hop, 1 / rate)
        for fr, e_ in zip(frames, en):
            if e_ > 0 and e_ >= en.max() * 0.1:
                sp = np.abs(np.fft.rfft(fr * np.hanning(hop)))
                if sp.sum() > 0:
                    cents.append(float((sp * ff).sum() / sp.sum()))
    rec["F-11_movement"] = None if len(cents) < 2 else round(float(np.std(cents) / np.mean(cents)), 4)
    rec["F-12_length"] = {"file_ms": ms(n), "sound_ms": ms(end - on)}
    return rec


def f09_rms(snd: np.ndarray, rate: int) -> float:
    """F-09's linear RMS: the loudest 400 ms window of the F-12 sound (mono), or the whole sound if shorter."""
    w = int(0.4 * rate)
    if len(snd) > w:
        e = np.convolve(snd ** 2, np.ones(w), "valid") / w
        return float(np.sqrt(e.max()))
    return float(np.sqrt(np.mean(snd ** 2))) if len(snd) else 0.0


def parity(paths: list[Path], mode: str, tool: str = "soundbench parity") -> dict:
    try:
        import pyloudnorm as pyln
    except ImportError as err:
        raise CueError("F-13 needs the pyloudnorm package") from err
    if len(paths) < 2:
        raise CueError("parity needs 2 or more files")
    loaded = [load(p) for p in paths]
    rates = {r for _, r in loaded}
    if len(rates) > 1:
        raise CueError(f"files have different sample rates {sorted(rates)}: resample to one rate first")
    rate = rates.pop()
    out = {"tool": tool, "mode": mode, "files": [str(p) for p in paths], "rate": rate,
           "verdict": "measured (screening aid: look at the waveforms before any fix note; review.md F-13)"}
    if mode == "integrated":  # (a) one common length: the longest file plus 0.4 s of silence
        length = max(len(x) for x, _ in loaded) + int(0.4 * rate)
        meter = pyln.Meter(rate)
        vals = [meter.integrated_loudness(np.vstack([x, np.zeros((length - len(x), x.shape[1]))])) for x, _ in loaded]
        out["common_length_ms"] = round(1000 * length / rate, 1)
    else:  # (b) momentary maximum of each result trimmed to its F-12 sound, all channels
        trimmed = []
        for x, _ in loaded:
            mono = x.mean(axis=1)
            on = onset_index(mono)
            end, _ = sound_end(mono, rate)
            trimmed.append(x[on:end])
        win = min(int(round(MOMENTARY_S * rate)), min(len(t) for t in trimmed))
        if win < 2:
            raise CueError("a trimmed result is shorter than 2 samples")
        meter = pyln.Meter(rate, block_size=(win - 1) / rate)
        step = max(1, int(round(0.01 * rate)))
        vals = []
        for t in trimmed:
            best = -math.inf
            for s in range(0, len(t) - win + 1, step):
                v = meter.integrated_loudness(t[s:s + win])
                best = max(best, v)
            vals.append(best)
        out["window_ms"] = round(1000 * win / rate, 2)
        out["trimmed_sound_ms"] = [round(1000 * len(t) / rate, 2) for t in trimmed]
    out["lufs"] = [None if not math.isfinite(v) else round(float(v), 2) for v in vals]
    fin = [v for v in vals if math.isfinite(v)]
    out["spread_lu"] = round(max(fin) - min(fin), 2) if len(fin) > 1 else None
    return out


# ---------------------------------------------------------------------------------------------------------------
# New measures (design section 5). Each takes a loaded buffer (DC removed, as `load` returns it).
# ---------------------------------------------------------------------------------------------------------------

def envelope_1ms(mono: np.ndarray, rate: int) -> tuple[np.ndarray, float]:
    """Sliding 1 ms RMS envelope (hop 1 sample); value i covers samples i .. i+w-1. Returns (envelope, w/2 offset)."""
    w = max(1, int(round(ENV_S * rate)))
    if len(mono) < w:
        return np.array([float(np.sqrt(np.mean(mono ** 2)))]), len(mono) / 2
    c = np.concatenate([[0.0], np.cumsum(mono.astype(np.float64) ** 2)])
    return np.sqrt(np.maximum(c[w:] - c[:-w], 0.0) / w), w / 2


def main_transient_ms(x: np.ndarray, rate: int) -> float | None:
    """Time of the main transient: the first point where the 1 ms envelope comes within 10 dB of its maximum (ms,
    at the window centre).

    Known false readings: a rising sound (a tell, a whoosh, a riser) has its main transient late by design, so a
    late value there is not a late start; two hits of nearly equal level read the first one."""
    env, off = envelope_1ms(x.mean(axis=1), rate)
    top = float(env.max())
    if top <= 0:
        return None
    i = int(np.argmax(env >= top * 10 ** (-MAIN_TRANSIENT_DB / 20)))
    return round(1000 * (i + off) / rate, 2)


def attack_rise_ms(x: np.ndarray, rate: int) -> float | None:
    """Attack rise time: from the first point at 10 % to the first point at 90 % of the 1 ms envelope's maximum
    (linear amplitude), searched up to the maximum (ms).

    Known false readings: the 1 ms envelope cannot read a rise under about 2 ms (an instant step reads about 0.8 ms);
    a noise head at 10 % of the peak starts the rise at the file start; a swell that peaks late reads its whole swell."""
    env, _ = envelope_1ms(x.mean(axis=1), rate)
    top_i = int(np.argmax(env))
    top = float(env[top_i])
    if top <= 0:
        return None
    head = env[: top_i + 1]
    i10 = int(np.argmax(head >= 0.1 * top))
    i90 = int(np.argmax(head >= 0.9 * top))
    return round(1000 * (i90 - i10) / rate, 2)


def attack_share(x: np.ndarray, rate: int) -> float | None:
    """Energy in the first 5 ms after the F-01 onset divided by the energy of the F-12 sound (onset to end).

    It guards denoise, declick and pitch (design section 4): a clean hit reads about 0.2; a smeared attack far less.
    Known false readings: a noise head moves the onset (F-01) to the file start, so the 5 ms hold noise, not attack;
    a sound shorter than 5 ms reads 1.0."""
    mono = x.mean(axis=1)
    on = onset_index(mono)
    end, _ = sound_end(mono, rate)
    total = float(np.sum(mono[on:end] ** 2))
    if total <= 0:
        return None
    k = max(1, int(round(ATTACK_SHARE_S * rate)))
    return round(float(np.sum(mono[on:min(end, on + k)] ** 2)) / total, 4)


def phone_loss_db(x: np.ndarray, rate: int) -> float | None:
    """Phone-speaker loss: the level lost (dB, positive = lost) through a 4th-order Butterworth high-pass at 400 Hz and
    low-pass at 10 kHz (the low-pass is left out when 10 kHz is at or above 95 % of the Nyquist frequency).

    Known false readings: a rough model of a phone speaker, the same for every file (real phones differ, and many
    boost around 1-3 kHz); it reads energy, not how loud a sound feels."""
    from scipy.signal import butter, sosfilt

    mono = x.mean(axis=1)
    e0 = float(np.sum(mono ** 2))
    if e0 <= 0:
        return None
    y = sosfilt(butter(4, PHONE_HP_HZ, "highpass", fs=rate, output="sos"), mono)
    if PHONE_LP_HZ < 0.95 * rate / 2:
        y = sosfilt(butter(4, PHONE_LP_HZ, "lowpass", fs=rate, output="sos"), y)
    e1 = float(np.sum(y ** 2))
    return None if e1 <= 0 else round(-10 * math.log10(e1 / e0), 2)


def tail_noise(x: np.ndarray, rate: int) -> dict:
    """Noise floor (dBFS) and signal-to-noise (loudest 10 ms window over the floor, dB). The floor is the RMS of the
    last 100 ms after the F-12 sound's end when at least 10 ms follow it; otherwise of the last 100 ms of the file
    (or its last quarter, if shorter), with `sound_reaches_end` true.

    Known false readings: when the sound reaches the file end (`sound_reaches_end`, F-04's flag) the floor is read
    on the sound's own tail; digital silence reads a floor far below -90 dBFS or None, not "no noise"; noise that
    exists only under the sound, not after it, is not seen."""
    mono = x.mean(axis=1)
    rms, _ = windows_rms(mono, rate)
    end, flag = sound_end(mono, rate)
    after = len(mono) - end
    if not flag and after >= int(round(WIN_S * rate)):
        k = min(int(round(TAIL_NOISE_S * rate)), after)
    else:
        k = min(int(round(TAIL_NOISE_S * rate)), max(1, len(mono) // 4))
    floor = float(np.sqrt(np.mean(mono[-k:] ** 2)))
    fl = db(floor)
    loud = db(float(rms.max()))
    return {"floor_dbfs": None if fl is None else round(fl, 2),
            "snr_db": None if fl is None or loud is None else round(loud - fl, 2),
            "window_ms": round(1000 * k / rate, 2), "sound_reaches_end": flag}


def clicks(x: np.ndarray, rate: int) -> dict:
    """Clicks: sample-to-sample steps over 8 x the RMS of the steps around them (a centred 4 ms window, the step
    itself included) and at least 1 % of the file's sample peak, on every channel; nearby hits within 1 ms count once.

    Known false readings: a real hard transient that starts from silence on a square edge reads as a click; a click
    inside a loud noisy passage hides under its large normal steps; a click under 1 % of the peak is not counted."""
    steps = np.abs(np.diff(x, axis=0))
    peak = float(np.max(np.abs(x)))
    w = 2 * max(1, int(round(CLICK_LOCAL_S * rate))) + 1
    if peak <= 0 or len(steps) < w:
        return {"count": 0, "first_ms": []}
    kernel = np.ones(w) / w
    local = np.sqrt(np.stack([np.convolve(steps[:, c] ** 2, kernel, "same") for c in range(x.shape[1])], axis=1))
    big = (steps > CLICK_FACTOR * local) & (steps >= CLICK_MIN_OF_PEAK * peak)
    idx = np.nonzero(np.any(big, axis=1))[0]
    merged: list[int] = []
    for i in idx:
        if not merged or i - merged[-1] > int(0.001 * rate):
            merged.append(int(i))
    return {"count": len(merged), "first_ms": [round(1000 * (i + 1) / rate, 2) for i in merged[:10]]}


def tonality(x: np.ndarray, rate: int) -> dict:
    """Tonal or noisy: spectral flatness (geometric / arithmetic mean of the power, 60 Hz to 12 kHz) of the loudest
    200 ms of the F-12 sound, and the notes present (peaks 20 dB over the band median and within 30 dB of the
    strongest, strongest first, at most 8). Reading: tonal under 0.05, noisy over 0.30 (PROPOSAL), else mixed.

    Known false readings (as F-10): harmonics are named as notes (a C#5 chime also lists C#6 and G#6); a fundamental
    under 60 Hz is missed; on noise the notes list is empty or random; a sound shorter than 200 ms is measured whole."""
    mono = x.mean(axis=1)
    on = onset_index(mono)
    end, _ = sound_end(mono, rate)
    snd = mono[on:end] if end - on > 16 else mono
    n = int(0.2 * rate)
    if len(snd) > n:
        c = np.concatenate([[0.0], np.cumsum(snd ** 2)])  # sliding 200 ms energy in O(n) (long beds stay fast)
        s = int(np.argmax(c[n:] - c[:-n]))
        snd = snd[s:s + n]
    p = np.abs(np.fft.rfft(snd * np.hanning(len(snd)))) ** 2
    f = np.fft.rfftfreq(len(snd), 1 / rate)
    band = (f >= 60) & (f <= min(12000.0, rate / 2))
    pb = p[band]
    if not band.any() or pb.max() <= 0:
        return {"flatness": None, "reading": None, "notes": []}
    flat = float(np.exp(np.mean(np.log(pb + 1e-30))) / np.mean(pb))
    reading = "tonal" if flat < TONAL_BELOW else "noisy" if flat > NOISY_ABOVE else "mixed"
    fb = f[band]
    med = float(np.median(pb))
    peaks = [i for i in range(1, len(pb) - 1) if pb[i] > pb[i - 1] and pb[i] >= pb[i + 1]
             and pb[i] >= med * 10 ** (NOTE_PEAK_DB / 10) and pb[i] >= pb.max() * 10 ** (-NOTE_RANGE_DB / 10)]
    notes: list[str] = []
    for i in sorted(peaks, key=lambda j: -pb[j]):
        midi = int(round(69 + 12 * math.log2(fb[i] / 440)))
        name = f"{NOTE_NAMES[midi % 12]}{midi // 12 - 1}"
        if name not in notes:
            notes.append(name)
        if len(notes) == 8:
            break
    return {"flatness": round(flat, 4), "reading": reading, "notes": notes}


def roughness(x: np.ndarray, rate: int) -> float | None:
    """Roughness: depth of the 30-150 Hz movement of the amplitude envelope (Hilbert) of the F-12 sound, as
    sqrt(2) x RMS of the band-passed envelope / mean envelope (a tone with 60 % amplitude modulation at 70 Hz
    reads about 0.6). The first and last 20 ms are left out (edge effects). None for sounds under 100 ms.

    Known false readings: a screening number only (review F11's own words): two close notes beating at 30-150 Hz read
    as rough, which they are, and so does a fast tremolo meant as an effect; a very short decay can read slightly
    rough from its own envelope."""
    from scipy.signal import butter, hilbert, sosfiltfilt

    mono = x.mean(axis=1)
    on = onset_index(mono)
    end, _ = sound_end(mono, rate)
    snd = mono[on:end]
    if len(snd) < int(0.1 * rate):
        return None
    env = np.abs(hilbert(snd))
    band = sosfiltfilt(butter(2, ROUGH_BAND_HZ, "bandpass", fs=rate, output="sos"), env)
    k = int(0.02 * rate)
    env, band = env[k:-k], band[k:-k]
    mean = float(np.mean(env))
    return None if mean <= 0 else round(float(math.sqrt(2) * np.sqrt(np.mean(band ** 2)) / mean), 4)


def lag(reference: np.ndarray, candidate: np.ndarray, rate: int, search_samples: int) -> dict:
    """Lag of `candidate` behind `reference` by cross-correlation of their mono sums, each with its mean removed
    (samples; positive = late). Pass one channel of each to time that channel alone (the adapter does, per channel:
    a mono sum hides one channel moved against the other).

    `clear` is True when the normalised correlation at the best lag is 0.5 or more and no other correlation peak in
    the search range reaches 90 % of it (PROPOSAL limits). Searched over -search_samples .. +search_samples.
    Known false readings: silence has no clear lag (reported as not clear); a periodic sound (a
    steady tone, a loop) correlates equally at every period, so it is not clear by design; an inverted output reads
    as not clear."""
    a = np.asarray(reference, dtype=np.float64)
    b = np.asarray(candidate, dtype=np.float64)
    a = a.mean(axis=1) if a.ndim == 2 else a
    b = b.mean(axis=1) if b.ndim == 2 else b
    a, b = a - a.mean(), b - b.mean()  # a DC offset correlates at every lag and would hide the true peak
    ea, eb = float(np.sum(a ** 2)), float(np.sum(b ** 2))
    if ea <= 0 or eb <= 0:
        return {"lag_samples": None, "lag_ms": None, "correlation": None, "second_peak_ratio": None, "clear": False}
    from scipy.signal import correlate

    c = correlate(b, a, mode="full", method="fft")
    zero = len(a) - 1  # index of lag 0
    lo, hi = max(0, zero - search_samples), min(len(c), zero + search_samples + 1)
    w = c[lo:hi]
    best = int(np.argmax(w))
    top = float(w[best])
    corr = top / math.sqrt(ea * eb)
    inner = np.arange(1, len(w) - 1)
    is_peak = (w[inner] > w[inner - 1]) & (w[inner] >= w[inner + 1])
    others = [float(w[i]) for i in inner[is_peak] if i != best]
    second = max(others) / top if others and top > 0 else 0.0
    found = lo + best - zero
    return {"lag_samples": int(found), "lag_ms": round(1000 * found / rate, 3), "correlation": round(corr, 4),
            "second_peak_ratio": round(second, 4),
            "clear": corr >= LAG_MIN_CORRELATION and second < LAG_MAX_SECOND_PEAK}


def new_numbers(x: np.ndarray, rate: int) -> dict:
    """The design section 5 measures of a loaded buffer (DC removed)."""
    return {"main_transient_ms": main_transient_ms(x, rate), "attack_rise_ms": attack_rise_ms(x, rate),
            "attack_share_5ms": attack_share(x, rate), "phone_loss_db": phone_loss_db(x, rate),
            "tail_noise": tail_noise(x, rate), "clicks": clicks(x, rate), "tonality": tonality(x, rate),
            "roughness": roughness(x, rate)}


def measure(path: Path, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    """Every measure of one file: F-01 to F-12 (cue_check's record) plus the design section 5 measures."""
    path = Path(path)
    rec = cue_record(path, low_cut, high_pitch)
    x, rate = load(path)
    rec.update(new_numbers(x, rate))
    return rec


def measure_audio(x: np.ndarray, rate: int, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    """Every measure of a buffer, the same way `measure` reads a file (DC removed per channel, float64)."""
    a = np.asarray(x, dtype=np.float64)
    a = a[:, None] if a.ndim == 1 else a
    a = a - a.mean(axis=0)
    rec = {"rate": rate, "channels": int(a.shape[1])}
    rec.update(cue_numbers(a, rate, low_cut, high_pitch))
    rec.update(new_numbers(a, rate))
    return rec


LUFS_MIN_S = 0.4  # pyloudnorm needs one 400 ms block (S-103: integrated LUFS only for 0.4 s or more)


def level_db(x: np.ndarray, rate: int, measure_name: str) -> float:
    """The card's level measure (editor-design.md section 7), unrounded; `loudness` uses this same function.

    F-09: RMS dBFS of the loudest 400 ms of the F-12 sound (one-shots).
    F-13a: integrated LUFS of the file padded with 0.4 s of silence (a family's parity value: padding a file further
    with digital silence cannot change it, because silent blocks fall under the -70 LUFS absolute gate).
    LUFS-I: integrated LUFS of the file itself, only for files of 0.4 s or more.
    Known false readings: as F-09 and F-13 in review.md section 4 (F-09 is RMS, never LUFS)."""
    a = np.asarray(x, dtype=np.float64)
    a = a[:, None] if a.ndim == 1 else a
    a = a - a.mean(axis=0)
    if measure_name == "F-09":
        mono = a.mean(axis=1)
        on = onset_index(mono)
        end, _ = sound_end(mono, rate)
        v = db(f09_rms(mono[on:end], rate))
    elif measure_name in ("F-13a", "LUFS-I"):
        import pyloudnorm as pyln

        if measure_name == "LUFS-I" and len(a) < LUFS_MIN_S * rate:
            raise CueError(f"LUFS-I needs 0.4 s or more; this sound is {1000 * len(a) / rate:.0f} ms: use F-09")
        if measure_name == "F-13a":
            a = np.vstack([a, np.zeros((int(0.4 * rate), a.shape[1]))])
        v = float(pyln.Meter(rate).integrated_loudness(a))
        v = v if math.isfinite(v) else None
    else:
        raise CueError(f"unknown level measure {measure_name!r}")
    if v is None:
        raise CueError(f"{measure_name}: the sound is silent, no level")
    return float(v)


def true_peak_db(x: np.ndarray) -> float | None:
    """F-03's true peak (x4 oversampling, `resample_poly`), unrounded, dBTP."""
    from scipy.signal import resample_poly

    a = np.asarray(x, dtype=np.float64)
    a = a[:, None] if a.ndim == 1 else a
    return db(float(np.max(np.abs(resample_poly(a, 4, 1, axis=0)))))
