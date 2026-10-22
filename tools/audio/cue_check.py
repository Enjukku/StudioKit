"""Measure a delivered sound file (F-01 to F-12) and loudness parity across files (F-13) - without AI taste.

Kit tool (universal). It replaces the hand-written recipes of `sound-design/references/review.md` section 4 (owner
decision J018-D7, G3-P1). The measures and their known false readings are defined there; this tool computes them
the same way. Every number is a screening aid: a FAIL, or a reading near its limit, is looked at on a waveform and
spectrogram before any fix note (review.md section 4).

Reading: `soundfile` (always 2-D), the mean of each channel subtracted first (generated audio often carries a DC
offset); mono = the mean of the channels. F-03 true peak needs `scipy`; F-13 needs `pyloudnorm`.

Usage:
  python tools/audio/cue_check.py measure <file> [--low-cut HZ] [--high-pitch] [--json]
  python tools/audio/cue_check.py parity <file> <file> [...] --mode integrated|momentary [--json]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np

WIN_S = 0.010  # RMS window (F-04, F-05, F-12)
TAIL_DB = 40.0  # F-04 / F-12: a window within this many dB of the loudest still belongs to the sound
ONSET_DB = 30.0  # F-01: first sample within this many dB of the peak
MOMENTARY_S = 0.100  # F-13 (b): window, or the shortest trimmed result if shorter
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


class CueError(Exception):
    pass


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


def measure(path: Path, low_cut: float | None = None, high_pitch: bool = False) -> dict:
    x, rate = load(path)
    mono = x.mean(axis=1)
    n = len(mono)
    ms = lambda i: round(1000 * i / rate, 2)
    peak = float(np.max(np.abs(x)))
    rec = {"tool": "cue_check measure", "file": str(path), "rate": rate, "channels": x.shape[1], "verdict":
           "measured (screening aid: look at the waveform before any fix note; review.md section 4)"}
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
    w = int(0.4 * rate)
    if len(snd) > w:
        e = np.convolve(snd ** 2, np.ones(w), "valid") / w
        lvl = float(np.sqrt(e.max()))
    else:
        lvl = float(np.sqrt(np.mean(snd ** 2))) if len(snd) else 0.0
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


def parity(paths: list[Path], mode: str) -> dict:
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
    out = {"tool": "cue_check parity", "mode": mode, "files": [str(p) for p in paths], "rate": rate,
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("measure", help="F-01 to F-12 for one file")
    m.add_argument("file", type=Path)
    m.add_argument("--low-cut", type=float, help="the layer's low cut in Hz (F-06 share below it)")
    m.add_argument("--high-pitch", action="store_true", help="F-10 band up to 12 kHz (chimes, sparkles, ticks)")
    m.add_argument("--json", action="store_true")
    p = sub.add_parser("parity", help="F-13 loudness parity across files")
    p.add_argument("files", type=Path, nargs="+")
    p.add_argument("--mode", choices=("integrated", "momentary"), required=True,
                   help="integrated: options and siblings; momentary: paid random results (trimmed, 100 ms)")
    p.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        rec = measure(a.file, a.low_cut, a.high_pitch) if a.cmd == "measure" else parity(a.files, a.mode)
    except CueError as err:
        print(f"ERROR: {err}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(rec, indent=2))
    else:
        for k, v in rec.items():
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
