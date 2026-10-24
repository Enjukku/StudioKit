"""Synthetic test sounds with known answers (design section 9): no audio files live in the repo.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Every fixture is made from fixed formulas and a seeded `numpy.random.RandomState` (its stream is stable across numpy
versions), so the same call gives the same samples on every run. Each returns float64 samples shaped (n, channels).
Stereo fixtures are deliberately unequal (the right channel is quieter and carries its own noise), so a channel swap
changes a number. Times are in ms, levels in dBFS.

Usage (tests and probes):
  from tools.audio.soundbench import fixtures
  x = fixtures.make("clean_hit", 44100, 2)
  fixtures.write_wav(path, x, 44100)
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

RATES = (44100, 48000)
CHANNELS = (1, 2)
RIGHT_GAIN = 0.6  # stereo fixtures: right channel level vs the left

# Known answers the tests use (the fixture is built from these numbers).
CLEAN_HIT_ONSET_MS = 20.0
LATE_HIT_ONSET_MS = 120.0
HIT_LENGTH_MS = 400.0
CHIME_HZ = 554.37  # C#5: the "wrong note" in an A-major game
ROUGH_CARRIER_HZ = 440.0
ROUGH_MOD_HZ = 70.0
ROUGH_DEPTH = 0.6
THUMP_HZ = 60.0
HUM_HZ = 50.0
DC_OFFSET = 0.08


def _t(rate: int, ms: float) -> np.ndarray:
    return np.arange(int(round(rate * ms / 1000))) / rate


def _silence(rate: int, ms: float) -> np.ndarray:
    return np.zeros(int(round(rate * ms / 1000)))


def _fade_out(y: np.ndarray, rate: int, ms: float = 5.0) -> np.ndarray:
    """A short linear fade at the end, so a fixture never ends on a cut (a real click)."""
    k = min(len(y), int(round(rate * ms / 1000)))
    y = y.copy()
    y[len(y) - k:] *= np.linspace(1, 0, k)
    return y


def _hit_body(rate: int, ms: float, rs: np.random.RandomState) -> np.ndarray:
    """A broadband hit: a noise crack plus a 330 Hz body, fast decay; peak about -3 dBFS."""
    t = _t(rate, ms)
    crack = rs.standard_normal(len(t)) * np.exp(-t * 60)
    body = np.sin(2 * np.pi * 330 * t) * np.exp(-t * 10)
    y = 0.35 * crack + 0.45 * body
    return _fade_out(y / np.max(np.abs(y)) * 10 ** (-3 / 20), rate)


def _mono(name: str, rate: int, rs: np.random.RandomState) -> np.ndarray:
    if name == "clean_hit":
        return np.concatenate([_silence(rate, CLEAN_HIT_ONSET_MS), _hit_body(rate, HIT_LENGTH_MS, rs), _silence(rate, 80)])
    if name == "late_hit":
        return np.concatenate([_silence(rate, LATE_HIT_ONSET_MS), _hit_body(rate, HIT_LENGTH_MS, rs), _silence(rate, 80)])
    if name == "bass_thump":
        t = _t(rate, 350)
        y = _fade_out(0.7 * np.sin(2 * np.pi * THUMP_HZ * t) * np.exp(-t * 9), rate)
        return np.concatenate([_silence(rate, 10), y, _silence(rate, 40)])
    if name == "hiss_lock":  # noise only: no note, no transient
        return 0.1 * rs.standard_normal(len(_t(rate, 300)))
    if name == "wrong_chime":
        t = _t(rate, 600)
        y = sum(a * np.sin(2 * np.pi * CHIME_HZ * k * t) for k, a in ((1, 1.0), (2, 0.3), (3, 0.12)))
        return np.concatenate([_silence(rate, 15), _fade_out(0.5 * y * np.exp(-t * 5), rate), _silence(rate, 30)])
    if name == "rough_tone":
        t = _t(rate, 500)
        am = 1 + ROUGH_DEPTH * np.sin(2 * np.pi * ROUGH_MOD_HZ * t)
        return 0.3 * np.sin(2 * np.pi * ROUGH_CARRIER_HZ * t) * am
    if name == "clipped":
        t = _t(rate, 300)
        return np.clip(3.0 * np.sin(2 * np.pi * 220 * t) * np.exp(-t * 4), -1.0, 1.0)
    if name == "dc_offset":
        return _mono("clean_hit", rate, rs) + DC_OFFSET
    if name == "hummed":
        y = _mono("clean_hit", rate, rs)
        t = np.arange(len(y)) / rate
        hum = sum(a * np.sin(2 * np.pi * HUM_HZ * k * t) for k, a in ((1, 1.0), (2, 0.5), (3, 0.25)))
        return y + 0.03 * hum
    if name == "bad_seam_bed":  # a bed that starts at 0 and ends near its crest: a jump at the loop wrap
        t = _t(rate, 1000)
        return 0.25 * np.sin(2 * np.pi * 220.25 * t) + 0.15 * np.sin(2 * np.pi * 110.25 * t)
    raise KeyError(f"unknown fixture {name!r}")


NAMES = ("clean_hit", "late_hit", "bass_thump", "hiss_lock", "wrong_chime", "rough_tone", "clipped", "dc_offset",
         "hummed", "bad_seam_bed")


def make(name: str, rate: int, channels: int = 1, seed: int = 7) -> np.ndarray:
    """One fixture as float64 (n, channels). Stereo: right = RIGHT_GAIN x left plus its own -60 dBFS noise."""
    rs = np.random.RandomState(seed + NAMES.index(name))
    left = _mono(name, rate, rs)
    if channels == 1:
        return left[:, None]
    if channels != 2:
        raise ValueError("fixtures are mono or stereo")
    right = RIGHT_GAIN * left + 0.001 * rs.standard_normal(len(left)) * (np.abs(left) > 0)
    if name == "clipped":
        right = np.clip(right, -1.0, 1.0)
    return np.stack([left, right], axis=1)


# Realistic takes (LD-c), modelled on 10 real ElevenLabs takes measured 2026-10-23: 480 ms for a 0.5 s request, 6
# of 10 peaking at -24 dBFS or lower, 7 of 10 starting mid-waveform (the first sample -4 to -12 dB re the peak), a
# tail floor 40-50 dB under the peak, stereo with channels about 1 dB apart. Kept apart from NAMES (the golden JSON
# covers NAMES only).
REAL_NAMES = ("quiet_hit", "soft_note", "quiet_whoosh")
REAL_LENGTH_MS = 480.0
REAL_PEAKS_DBFS = {"quiet_hit": -36.0, "soft_note": -24.0, "quiet_whoosh": -30.0}
REAL_FIRST_DB_RE_PEAK = {"quiet_hit": -5.0, "soft_note": -12.0, "quiet_whoosh": -8.0}
REAL_FLOOR_DB_RE_PEAK = -45.0
REAL_RIGHT_DB = -1.1


def _real_mono(name: str, rate: int, rs: np.random.RandomState) -> np.ndarray:
    n = int(round(rate * REAL_LENGTH_MS / 1000))
    t = np.arange(n) / rate
    if name == "quiet_hit":  # a crack and a 210 Hz body, already sounding at sample 0
        y = 0.5 * rs.standard_normal(n) * np.exp(-t * 45) + 0.6 * np.sin(2 * np.pi * 210 * t + 1.2) * np.exp(-t * 9)
    elif name == "soft_note":  # a 523 Hz note with two partials, decaying
        y = sum(a * np.sin(2 * np.pi * 523.25 * k * t + 0.9) for k, a in ((1, 1.0), (2, 0.35), (3, 0.12)))
        y = y * np.exp(-t * 6)
    elif name == "quiet_whoosh":  # band-limited noise swelling then falling
        from scipy.signal import butter, sosfilt

        y = sosfilt(butter(2, (300, 4000), "bandpass", fs=rate, output="sos"), rs.standard_normal(n))
        y = y * np.sin(np.pi * np.clip(t / (REAL_LENGTH_MS / 1000), 0, 1)) ** 2 + 0.3 * y * np.exp(-t * 30)
    else:
        raise KeyError(f"unknown realistic fixture {name!r}")
    y = y / np.max(np.abs(y))
    want0 = 10 ** (REAL_FIRST_DB_RE_PEAK[name] / 20)  # the first sample sits at its stated level re the peak
    y[0] = want0 * (1 if y[0] >= 0 else -1)
    floor = 10 ** (REAL_FLOOR_DB_RE_PEAK / 20) * rs.standard_normal(n)
    return (y + floor) / np.max(np.abs(y + floor)) * 10 ** (REAL_PEAKS_DBFS[name] / 20)


def make_real(name: str, rate: int, channels: int = 2, seed: int = 11) -> np.ndarray:
    """A realistic quiet take as float64 (n, channels): the right channel 1.1 dB lower with its own floor noise."""
    rs = np.random.RandomState(seed + REAL_NAMES.index(name))
    left = _real_mono(name, rate, rs)
    if channels == 1:
        return left[:, None]
    floor = 10 ** ((REAL_PEAKS_DBFS[name] + REAL_FLOOR_DB_RE_PEAK) / 20) * rs.standard_normal(len(left))
    right = 10 ** (REAL_RIGHT_DB / 20) * left + 0.5 * floor
    return np.stack([left, right], axis=1)


# Long material for loops (J020 step 6): beds of 2-30 s, noise-like and tonal, at real-take levels (quiet, the right
# channel 1.1 dB lower with its own floor). `real_bed` and `chain` build long sounds from short takes the way the rank
# repair did: takes slowed x4 (two octaves down, four times longer) and spliced with equal-power crossfades.
BED_KINDS = ("steady_noise", "noise_bed", "steady_tone", "tonal_pad", "real_bed")
BED_PEAK_DBFS = {"steady_noise": -30.0, "noise_bed": -30.0, "steady_tone": -24.0, "tonal_pad": -24.0, "real_bed": -30.0}


def slow(x: np.ndarray, factor: int = 4) -> np.ndarray:
    """A take played `factor` times slower (length x factor, pitch down by log2(factor) octaves)."""
    from scipy.signal import resample_poly

    return resample_poly(np.asarray(x, dtype=np.float64), factor, 1, axis=0)


def chain(parts: list, rate: int, seconds: float, cross_ms: float = 60.0, seed: int = 0) -> np.ndarray:
    """Parts (each (n, ch)) spliced end to start with equal-power crossfades, in a seeded order that never repeats a
    part twice in a row, until `seconds` long; every part normalised to the same RMS first."""
    rs = np.random.RandomState(seed)
    ch = max(p.shape[1] for p in parts)
    norm = [np.repeat(p, ch, axis=1) if p.shape[1] < ch else p for p in parts]
    norm = [p / max(float(np.sqrt(np.mean(p ** 2))), 1e-12) for p in norm]
    n_total = int(round(seconds * rate))
    k = int(round(cross_ms * rate / 1000))
    out = norm[rs.randint(len(norm))].copy()
    last = None
    while len(out) < n_total + k:
        i = rs.randint(len(norm))
        if len(norm) > 1 and i == last:
            continue
        last = i
        nxt = norm[i]
        t = np.arange(1, k + 1) / (k + 1)
        mixed = out[-k:] * np.cos(np.pi / 2 * t)[:, None] + nxt[:k] * np.sin(np.pi / 2 * t)[:, None]
        out = np.vstack([out[:-k], mixed, nxt[k:]])
    return out[:n_total]


def make_bed(kind: str, rate: int, seconds: float, channels: int = 2, seed: int = 5) -> np.ndarray:
    """A bed of `seconds` as float64 (n, channels), peaking at BED_PEAK_DBFS[kind].

    steady_noise: noise low-passed at 3 kHz, steady level. noise_bed: the same with a slow +-3 dB swell (0.37 Hz) and
    a little high hiss. steady_tone: 220 Hz with two harmonics, exactly periodic. tonal_pad: an A-minor-ish chord
    (220, 261.6, 329.6 Hz) with a slow 6-cent vibrato, so no two periods are equal. real_bed: `chain` of the realistic
    takes (`make_real`) slowed x4."""
    from scipy.signal import butter, sosfilt

    rs = np.random.RandomState(seed + BED_KINDS.index(kind))
    n = int(round(seconds * rate))
    t = np.arange(n) / rate
    if kind in ("steady_noise", "noise_bed"):
        y = sosfilt(butter(2, 3000, "lowpass", fs=rate, output="sos"), rs.standard_normal(n))
        if kind == "noise_bed":
            y = y * 10 ** (3 * np.sin(2 * np.pi * 0.37 * t) / 20)
            y = y + 0.05 * sosfilt(butter(2, 6000, "highpass", fs=rate, output="sos"), rs.standard_normal(n))
    elif kind == "steady_tone":
        y = sum(a * np.sin(2 * np.pi * 220 * h * t) for h, a in ((1, 1.0), (2, 0.4), (3, 0.2)))
    elif kind == "tonal_pad":
        vib = 2 ** (6 / 1200 * np.sin(2 * np.pi * 0.3 * t))
        phase = 2 * np.pi * np.cumsum(vib) / rate
        y = sum(a * np.sin(f * phase + p) for f, a, p in ((220.0, 1.0, 0.0), (261.63, 0.7, 1.1), (329.63, 0.6, 2.3)))
    elif kind == "real_bed":
        parts = [slow(make_real(name, rate, 1, seed=seed)) for name in REAL_NAMES]
        y = chain(parts, rate, seconds, seed=seed)[:, 0]
    else:
        raise KeyError(f"unknown bed {kind!r}")
    floor = 10 ** (REAL_FLOOR_DB_RE_PEAK / 20) * float(np.max(np.abs(y)))
    left = y + floor * rs.standard_normal(n)
    left = left / np.max(np.abs(left)) * 10 ** (BED_PEAK_DBFS[kind] / 20)
    if channels == 1:
        return left[:, None]
    right = 10 ** (REAL_RIGHT_DB / 20) * left + 10 ** ((BED_PEAK_DBFS[kind] + REAL_FLOOR_DB_RE_PEAK) / 20) * \
        rs.standard_normal(n)
    return np.stack([left, right], axis=1)


def write_wav(path: Path, x: np.ndarray, rate: int) -> Path:
    """Float32 WAV (no quantisation beyond float32), the format every measure test reads."""
    import soundfile as sf

    sf.write(str(path), np.asarray(x, dtype=np.float32), rate, subtype="FLOAT")
    return path
