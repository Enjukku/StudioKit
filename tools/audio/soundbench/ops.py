"""The numpy edit operations (editor-design.md section 4): the design pass and the edit pass.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 3)

Every operation takes float64 audio shaped (samples, channels), the rate and its checked parameters, and returns
(audio, info): `info` holds the numbers the log needs (gains, reductions, lengths). Operations never resample: the
rate is the take's rate from intake to export. Parameters are checked against `SPEC` before a render starts
(`check_params`): an unknown name, a wrong type or a value out of range is refused with the reason. PROPOSAL values
(limits a check may change) are named constants below.

Filters are RBJ cookbook biquads (Robert Bristow-Johnson, "Cookbook formulae for audio EQ biquad filter
coefficients") as second-order sections, run causally with `scipy.signal.sosfilt` (no pre-ringing before an
attack). `highpass`/`lowpass` order 4 is two biquads with the Butterworth Q values (0.5412, 1.3066).

Usage:
  from tools.audio.soundbench import ops
  params = ops.check_params("eq", {"bands": [{"type": "bell", "hz": 1000, "gain_db": -3, "q": 1.4}]})
  y, info = ops.run("eq", x, 44100, params, ctx)
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

from . import measures
from .card import KINDS, NOTE_NAMES, SCALES
from .core import SoundbenchError

REQ = object()  # a required parameter

# PROPOSAL values
EQ_BOOST_WHY_DB = 6.0  # an EQ boost above this needs a `why` (SC-06: cut before boost)
VARISPEED_MAX_CENTS_ERROR = 0.5  # the rational resampling ratio must hit the asked pitch within 0.5 cent
TO_KEY_MAX_CENTS = 600.0  # to_key never shifts more than half an octave
LIMIT_TRANSIENT_DB = 0.5  # sfx/ui: limiting a transient by more than 0.5 dB needs a `why`
TRANSIENT_REGION_MS = 10.0  # ... the transient region runs from the F-01 onset to 10 ms after the main transient
SPACE_MAX_DECAY_S = 1.5  # `space` is the sound's own tail, never a room (J020-D10): longer decays are refused
TRIM_PREROLL_MS = 1.0  # trim keeps 1 ms before the binding onset (a fade over it when it is not silent)
CUT_FADE_MIN_MS = 5.0  # a cut through sound needs a fade-out of at least 5 ms
CUT_SILENT_DB = -60.0  # ... "through sound" = the last 1 ms before the cut above peak - 60 dB
FADE_IN_KEEP_SHARE = 0.9  # a fade-in that leaves under 90 % of the attack share needs a `why`
PEAK_CEILING_DBTP = -1.0  # peak: default true-peak ceiling ...
PEAK_MARGIN_DB = 0.5  # ... minus a margin for Roblox's transcode overshoot (PROPOSAL until an upload is measured)
LOUDNESS_MAX_ERROR_DB = 0.05  # loudness must land within 0.05 dB of the target on its own measure


def _num(lo, hi, default=REQ, kind=float):
    return {"type": kind, "lo": lo, "hi": hi, "default": default}


SPEC: dict[str, dict] = {
    "dc": {},
    "highpass": {"hz": _num(10, 20000), "order": {"type": "choice", "options": (2, 4), "default": 2}},
    "lowpass": {"hz": _num(100, 22000), "order": {"type": "choice", "options": (2, 4), "default": 2}},
    "eq": {"bands": {"type": "bands", "default": REQ}},
    "dehum": {"hz": {"type": "choice", "options": (50, 60), "default": REQ}, "harmonics": _num(1, 8, 4, int),
              "q": _num(5, 100, 30.0)},
    "gate": {"threshold_db": _num(-90, -10), "range_db": _num(6, 120, 60.0), "attack_ms": _num(0.1, 20, 1.0),
             "hold_ms": _num(0, 500, 20.0), "release_ms": _num(1, 2000, 80.0)},
    "varispeed": {"semitones": _num(-24, 24)},
    "to_key": {"method": {"type": "choice", "options": ("varispeed", "pitch"), "default": "varispeed"}},
    "compress": {"threshold_db": _num(-80, 0), "ratio": _num(1, 50), "knee_db": _num(0, 24, 6.0),
                 "attack_ms": _num(0.05, 500, 5.0), "release_ms": _num(1, 5000, 100.0), "makeup_db": _num(-24, 24, 0.0)},
    "limit": {"ceiling_dbtp": _num(-24, 0, -1.0), "lookahead_ms": _num(0.5, 20, 5.0), "release_ms": _num(1, 2000, 80.0)},
    "space": {"decay_s": _num(0.05, SPACE_MAX_DECAY_S), "predelay_ms": _num(0, 100, 10.0), "damping": _num(0, 1, 0.5),
              "wet": _num(0, 1, 0.2), "seed": _num(0, 2 ** 31 - 1, 1, int)},
    "echo": {"delay_ms": _num(1, 1000), "feedback": _num(0, 0.9, 0.3), "mix": _num(0, 1, 0.3)},
    "transient": {"attack_db": _num(-12, 12, 0.0), "sustain_db": _num(-12, 12, 0.0)},
    "saturate": {"drive_db": _num(0, 24), "mix": _num(0, 1, 1.0)},
    "trim": {"to": {"type": "choice", "options": ("card", "F-01", "main_transient"), "default": "card"},
             "preroll_ms": _num(0, 20, TRIM_PREROLL_MS)},
    "cut": {"end_ms": _num(1, 7 * 60 * 1000, None), "after_sound_ms": _num(0, 10000, None)},
    "fade": {"in_ms": _num(0, 5000, 0.0), "out_ms": _num(0, 10000, 0.0),
             "curve": {"type": "choice", "options": ("linear", "cosine"), "default": "cosine"}},
    "mono": {},
    "loudness": {},
    "peak": {"ceiling_dbtp": _num(-24, 0, PEAK_CEILING_DBTP), "margin_db": _num(0, 6, PEAK_MARGIN_DB)},
    "export": {},
}
FFMPEG_OPS = ("denoise", "declick", "pitch", "stretch", "chorus")  # specs and code in fxops.py

STAGES = ("clean", "pitch", "eq", "compress", "add", "compress_again", "transient", "air")  # SC-09
OP_STAGES = {"dc": ("clean",), "highpass": ("clean", "eq"), "lowpass": ("clean", "eq"), "denoise": ("clean",),
             "declick": ("clean",), "dehum": ("clean",), "gate": ("clean",), "varispeed": ("pitch",),
             "pitch": ("pitch",), "stretch": ("pitch",), "to_key": ("pitch",), "eq": ("eq",),
             "compress": ("compress", "compress_again"), "limit": ("compress", "compress_again"),
             "space": ("add",), "echo": ("add",), "chorus": ("add",), "transient": ("transient",),
             "saturate": ("air",)}
BAND_TYPES = ("bell", "low_shelf", "high_shelf", "notch")


def check_params(op: str, step: dict) -> dict:
    """Resolve a recipe step's parameters against SPEC (defaults filled); SoundbenchError on anything wrong."""
    if op in FFMPEG_OPS:
        from . import fxops

        spec = fxops.SPEC[op]
    elif op in SPEC:
        spec = SPEC[op]
    else:
        raise SoundbenchError(f"unknown operation {op!r}")
    given = {k: v for k, v in step.items() if k not in ("op", "why")}
    extra = set(given) - set(spec)
    if extra:
        raise SoundbenchError(f"{op}: unknown parameter(s) {sorted(extra)} (known: {sorted(spec)})")
    out = {}
    for name, rule in spec.items():
        where = f"{op}.{name}"
        if name not in given:
            if rule["default"] is REQ:
                raise SoundbenchError(f"{where}: required")
            out[name] = rule["default"]
            continue
        v = given[name]
        if rule["type"] == "choice":
            if v not in rule["options"] or isinstance(v, bool):
                raise SoundbenchError(f"{where}: {v!r} is not one of {list(rule['options'])}")
        elif rule["type"] == "bands":
            v = _check_bands(v, step.get("why"))
        else:
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
                raise SoundbenchError(f"{where}: needs a finite number, got {v!r}")
            if rule["type"] is int and int(v) != v:
                raise SoundbenchError(f"{where}: needs a whole number, got {v!r}")
            if not rule["lo"] <= v <= rule["hi"]:
                raise SoundbenchError(f"{where}: {v} is outside {rule['lo']}..{rule['hi']}")
            v = rule["type"](v)
        out[name] = v
    if op == "cut" and (out["end_ms"] is None) == (out["after_sound_ms"] is None):
        raise SoundbenchError("cut: give exactly one of end_ms or after_sound_ms")
    return out


def _check_bands(bands, why) -> list[dict]:
    if not isinstance(bands, list) or not bands:
        raise SoundbenchError("eq.bands: needs a list of bands")
    out = []
    for i, b in enumerate(bands):
        where = f"eq.bands[{i}]"
        if not isinstance(b, dict) or b.get("type") not in BAND_TYPES:
            raise SoundbenchError(f"{where}: needs a type from {list(BAND_TYPES)}")
        allowed = {"type", "hz", "q"} | ({"gain_db"} if b["type"] != "notch" else set())
        extra = set(b) - allowed
        if extra:
            raise SoundbenchError(f"{where}: unknown field(s) {sorted(extra)}")
        r = {"type": b["type"]}
        for name, lo, hi, default in (("hz", 10, 22000, REQ), ("q", 0.1, 100, 0.7071),
                                      ("gain_db", -24, 24, REQ if b["type"] != "notch" else 0.0)):
            if name == "gain_db" and b["type"] == "notch":
                continue
            v = b.get(name, default)
            if v is REQ:
                raise SoundbenchError(f"{where}.{name}: required")
            if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or not lo <= v <= hi:
                raise SoundbenchError(f"{where}.{name}: needs a number from {lo} to {hi}, got {v!r}")
            r[name] = float(v)
        if r.get("gain_db", 0.0) > EQ_BOOST_WHY_DB and not why:
            raise SoundbenchError(f"{where}: a boost of {r['gain_db']} dB (over {EQ_BOOST_WHY_DB} dB) needs a `why` "
                                  "(SC-06: cut before boost)")
        out.append(r)
    return out


def check_order(design: list[dict]) -> list[str]:
    """The SC-09 stage of each design step. A step before the current stage needs a `why`, otherwise refused."""
    cur, stages = -1, []
    for i, step in enumerate(design):
        allowed = [STAGES.index(s) for s in OP_STAGES.get(step["op"], ())]
        if not allowed:
            raise SoundbenchError(f"design[{i}]: {step['op']!r} is not a design operation")
        later = [s for s in allowed if s >= cur]
        if later:
            cur = min(later)
            stages.append(STAGES[cur])
        elif step.get("why"):
            stages.append(STAGES[max(allowed)] + " (out of order: " + step["why"] + ")")
        else:
            raise SoundbenchError(f"design[{i}]: {step['op']!r} ({'/'.join(OP_STAGES[step['op']])}) comes after "
                                  f"{STAGES[cur]}; the SC-09 order is {' > '.join(STAGES)}: give a `why` or move it")
    return stages


# --------------------------------------------------------------------------------------------- filters (RBJ)

def rbj(kind: str, hz: float, rate: int, q: float = 0.7071, gain_db: float = 0.0) -> np.ndarray:
    """One RBJ cookbook biquad as a second-order section [b0 b1 b2 1 a1 a2]."""
    if not 0 < hz < rate / 2:
        raise SoundbenchError(f"{kind} at {hz} Hz is not below the Nyquist frequency {rate / 2} Hz")
    w0 = 2 * math.pi * hz / rate
    cw, sw = math.cos(w0), math.sin(w0)
    alpha = sw / (2 * q)
    a = 10 ** (gain_db / 40)
    if kind == "lowpass":
        b, den = [(1 - cw) / 2, 1 - cw, (1 - cw) / 2], [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "highpass":
        b, den = [(1 + cw) / 2, -(1 + cw), (1 + cw) / 2], [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "notch":
        b, den = [1, -2 * cw, 1], [1 + alpha, -2 * cw, 1 - alpha]
    elif kind == "bell":
        b, den = [1 + alpha * a, -2 * cw, 1 - alpha * a], [1 + alpha / a, -2 * cw, 1 - alpha / a]
    elif kind in ("low_shelf", "high_shelf"):
        sa = 2 * math.sqrt(a) * alpha
        if kind == "low_shelf":
            b = [a * ((a + 1) - (a - 1) * cw + sa), 2 * a * ((a - 1) - (a + 1) * cw), a * ((a + 1) - (a - 1) * cw - sa)]
            den = [(a + 1) + (a - 1) * cw + sa, -2 * ((a - 1) + (a + 1) * cw), (a + 1) + (a - 1) * cw - sa]
        else:
            b = [a * ((a + 1) + (a - 1) * cw + sa), -2 * a * ((a - 1) + (a + 1) * cw), a * ((a + 1) + (a - 1) * cw - sa)]
            den = [(a + 1) - (a - 1) * cw + sa, 2 * ((a - 1) - (a + 1) * cw), (a + 1) - (a - 1) * cw - sa]
    else:
        raise SoundbenchError(f"unknown filter {kind!r}")
    return np.array([b[0] / den[0], b[1] / den[0], b[2] / den[0], 1.0, den[1] / den[0], den[2] / den[0]])


BUTTERWORTH_Q4 = (0.5411961, 1.3065630)


def pass_sos(kind: str, hz: float, rate: int, order: int) -> np.ndarray:
    qs = (0.7071068,) if order == 2 else BUTTERWORTH_Q4
    return np.vstack([rbj(kind, hz, rate, q) for q in qs])


def _sosfilt(sos: np.ndarray, x: np.ndarray) -> np.ndarray:
    from scipy.signal import sosfilt

    return sosfilt(sos, x, axis=0)


# --------------------------------------------------------------------------------------------- design pass

def op_dc(x, rate, p, ctx):
    off = x.mean(axis=0)
    return x - off, {"removed_offset": [round(float(v), 6) for v in off]}


def op_highpass(x, rate, p, ctx):
    return _sosfilt(pass_sos("highpass", p["hz"], rate, p["order"]), x), {}


def op_lowpass(x, rate, p, ctx):
    return _sosfilt(pass_sos("lowpass", p["hz"], rate, p["order"]), x), {}


def eq_sos(bands: list[dict], rate: int) -> np.ndarray:
    return np.vstack([rbj(b["type"], b["hz"], rate, b["q"], b.get("gain_db", 0.0)) for b in bands])


def op_eq(x, rate, p, ctx):
    return _sosfilt(eq_sos(p["bands"], rate), x), {}


def op_dehum(x, rate, p, ctx):
    freqs = [p["hz"] * k for k in range(1, p["harmonics"] + 1) if p["hz"] * k < 0.45 * rate]
    sos = np.vstack([rbj("notch", f, rate, p["q"]) for f in freqs])
    return _sosfilt(sos, x), {"notches_hz": freqs}


def _box_back(v: np.ndarray, width: int) -> np.ndarray:
    """Backward moving average: out[n] = mean(v[n-width+1 .. n]) (values before the start count as v[0])."""
    if width <= 1:
        return v.copy()
    c = np.concatenate([np.full(width, v[0]), v]).cumsum()
    return (c[width:] - c[:-width]) / width


def op_gate(x, rate, p, ctx):
    """Downward gate on the tail's noise floor, linked across channels. It opens `attack_ms` before the first sample
    over the threshold (lookahead, so the attack is never touched), holds, then closes over `release_ms`."""
    peak = float(np.max(np.abs(x)))
    if peak <= 0:
        return x.copy(), {"closed_ms": 0.0}
    thr = peak * 10 ** (p["threshold_db"] / 20)
    loud = (np.max(np.abs(x), axis=1) >= thr).astype(np.float64)
    la, hold = max(1, int(round(p["attack_ms"] * rate / 1000))), int(round(p["hold_ms"] * rate / 1000))
    mask = _open_window(loud, la, hold)
    rel = max(1, int(round(p["release_ms"] * rate / 1000)))
    g = np.maximum(_box_back(mask, la), _box_back(mask, rel))
    g = np.minimum(g, 1.0)
    floor = 10 ** (-p["range_db"] / 20)
    gain = floor + (1 - floor) * g
    return x * gain[:, None], {"threshold_dbfs": round(20 * math.log10(thr), 2),
                               "closed_ms": round(1000 * float(np.sum(gain < 0.5)) / rate, 2)}


def _open_window(loud: np.ndarray, la: int, hold: int) -> np.ndarray:
    """mask[n] = 1 when any loud sample lies in [n - hold, n + la] (lookahead la, hold after the last loud one)."""
    c = np.concatenate([[0.0], np.cumsum(loud)])
    n = np.arange(len(loud))
    lo = np.clip(n - hold, 0, len(loud))
    hi = np.clip(n + la + 1, 0, len(loud))
    return ((c[hi] - c[lo]) > 0).astype(np.float64)


def varispeed_ratio(semitones: float) -> tuple[Fraction, float]:
    """resample_poly up/down for a pitch change of `semitones` (length changes with it) and the cents it achieves."""
    want = 2 ** (semitones / 12)  # playback speed: higher pitch = shorter
    frac = Fraction(1 / want).limit_denominator(4000)  # output samples per input sample
    got_cents = -1200 * math.log2(float(frac))
    return frac, got_cents


def op_varispeed(x, rate, p, ctx):
    from scipy.signal import resample_poly

    if p["semitones"] == 0:
        return x.copy(), {"ratio": 1.0, "cents": 0.0}
    frac, cents = varispeed_ratio(p["semitones"])
    err = cents - 100 * p["semitones"]
    if abs(err) > VARISPEED_MAX_CENTS_ERROR:
        raise SoundbenchError(f"varispeed: the resampling ratio misses the pitch by {err:.2f} cents")
    y = resample_poly(x, frac.numerator, frac.denominator, axis=0)
    return y, {"up": frac.numerator, "down": frac.denominator, "cents": round(cents, 3),
               "time_scale": round(float(frac), 6), "samples": [len(x), len(y)]}


def nearest_in_key(hz: float, root: str, scale: str) -> tuple[str, float]:
    """The nearest note of the key to `hz` and the shift to it in cents."""
    midi = 69 + 12 * math.log2(hz / 440)
    root_pc = NOTE_NAMES.index(root)
    pcs = {(root_pc + s) % 12 for s in SCALES[scale]}
    best = min((m for m in range(int(midi) - 12, int(midi) + 13) if m % 12 in pcs), key=lambda m: abs(m - midi))
    return f"{NOTE_NAMES[best % 12]}{best // 12 - 1}", 100 * (best - midi)


def op_to_key(x, rate, p, ctx):
    key = ctx.get("key")
    if not key:
        raise SoundbenchError("to_key: the card names no key")
    a = x - x.mean(axis=0)
    f10 = measures.pitch(a.mean(axis=1), rate, False)
    if not f10.get("trusted"):
        raise SoundbenchError(f"to_key: F-10 is untrusted (peak {f10.get('peak_over_band_median_db')} dB over the band "
                              "median, needs 20): the note cannot be named, refused")
    note, cents = nearest_in_key(f10["hz"], key["root"], key["scale"])
    if abs(cents) > TO_KEY_MAX_CENTS:
        raise SoundbenchError(f"to_key: {cents:.0f} cents is over the {TO_KEY_MAX_CENTS:.0f} cent limit")
    info = {"from_hz": f10["hz"], "from_note": f10["note"], "to_note": note, "shift_cents": round(cents, 1),
            "method": p["method"]}
    if abs(cents) < 1:
        return x.copy(), info
    if p["method"] == "varispeed":
        y, vi = op_varispeed(x, rate, {"semitones": cents / 100}, ctx)
    else:
        from . import fxops

        y, vi = fxops.run("pitch", x, rate, check_params("pitch", {"semitones": round(cents / 100, 6)}), ctx)
    info.update(vi)
    return y, info


def _onepole_env(level: np.ndarray, rate: int, attack_ms: float, release_ms: float) -> np.ndarray:
    """Peak follower: rises with the attack time constant, falls with the release one (per sample loop)."""
    aa = math.exp(-1 / (attack_ms * rate / 1000))
    ar = math.exp(-1 / (release_ms * rate / 1000))
    out = np.empty_like(level)
    e = 0.0
    lv = level.tolist()
    for i, v in enumerate(lv):
        e = aa * e + (1 - aa) * v if v > e else ar * e + (1 - ar) * v
        out[i] = e
    return out


def static_curve_db(level_db: np.ndarray, threshold: float, ratio: float, knee: float) -> np.ndarray:
    """The compressor's static output level for an input level (Giannoulis, Massberg and Reiss 2012, soft knee)."""
    x = np.asarray(level_db, dtype=np.float64)
    y = x.copy()
    over = 2 * (x - threshold)
    if knee > 0:
        k = np.abs(over) <= knee
        y[k] = x[k] + (1 / ratio - 1) * (x[k] - threshold + knee / 2) ** 2 / (2 * knee)
    hi = over > knee
    y[hi] = threshold + (x[hi] - threshold) / ratio
    return y


def op_compress(x, rate, p, ctx):
    level = np.max(np.abs(x), axis=1)
    env = _onepole_env(level, rate, p["attack_ms"], p["release_ms"])
    env_db = 20 * np.log10(np.maximum(env, 1e-12))
    gain_db = static_curve_db(env_db, p["threshold_db"], p["ratio"], p["knee_db"]) - env_db
    deepest = float(-gain_db.min())
    g = 10 ** ((gain_db + p["makeup_db"]) / 20)
    return x * g[:, None], {"deepest_gain_reduction_db": round(deepest, 2),
                            "deepest_at_ms": round(1000 * int(np.argmin(gain_db)) / rate, 2)}


def _true_peak_per_sample(x: np.ndarray) -> np.ndarray:
    """Per input sample: the largest |value| among the sample and its 3 interpolated neighbours (x4), all channels."""
    from scipy.signal import resample_poly

    up = np.abs(resample_poly(x, 4, 1, axis=0))[: 4 * len(x)]
    up = up.reshape(len(x), 4, x.shape[1]).max(axis=1)
    return np.maximum(up, np.abs(x)).max(axis=1)


def op_limit(x, rate, p, ctx):
    """Lookahead true-peak limiter. The gain is the future minimum of the needed gain over the lookahead, averaged
    back over the lookahead (so it is fully down at every peak) and released by a longer average; offline, so the
    lookahead adds no delay. Iterates until the true peak (x4) is at or under the ceiling."""
    ceiling = 10 ** (p["ceiling_dbtp"] / 20)
    la = max(1, int(round(p["lookahead_ms"] * rate / 1000)))
    rel = max(la, int(round(p["release_ms"] * rate / 1000)))
    target = ceiling
    total = np.ones(len(x))
    y = x
    for _ in range(6):
        tp = _true_peak_per_sample(y)
        if float(tp.max()) <= ceiling * (1 + 1e-6):
            break
        need = np.minimum(1.0, target / np.maximum(tp, 1e-12))
        fut = _future_min(need, la)
        g = _box_back(fut, la)
        g = np.minimum(g, _box_back(g, rel))
        total = total * g
        y = x * total[:, None]
        target *= 0.999
    else:
        raise SoundbenchError("limit: the true peak did not reach the ceiling in 6 passes")
    gr = -20 * np.log10(np.maximum(total, 1e-12))
    info = {"deepest_gain_reduction_db": round(float(gr.max()), 2),
            "deepest_at_ms": round(1000 * int(np.argmax(gr)) / rate, 2)}
    if ctx.get("category") in ("sfx", "ui") and not ctx.get("why"):
        a = x - x.mean(axis=0)
        on = measures.onset_index(a.mean(axis=1))
        mt = measures.main_transient_ms(a, rate) or 0.0
        end = int((mt + TRANSIENT_REGION_MS) / 1000 * rate)
        region = gr[on:max(on + 1, end)]
        if len(region) and float(region.max()) > LIMIT_TRANSIENT_DB:
            raise SoundbenchError(f"limit: it cuts the transient by {region.max():.2f} dB (over {LIMIT_TRANSIENT_DB} dB) "
                                  f"on a {ctx['category']} cue: give a `why` (GreatWallSim review F12)")
        info["transient_reduction_db"] = round(float(region.max()) if len(region) else 0.0, 2)
    return y, info


def _future_min(v: np.ndarray, la: int) -> np.ndarray:
    """out[n] = min(v[n .. n+la]) (the last value repeats past the end)."""
    from numpy.lib.stride_tricks import sliding_window_view

    pad = np.concatenate([v, np.full(la, v[-1])])
    return sliding_window_view(pad, la + 1).min(axis=1)[: len(v)]


def op_space(x, rate, p, ctx):
    """The sound's own tail and glue (never a room, J020-D10): a generated decaying-noise impulse response per channel
    (RT60 = decay_s, damping = a low-pass on the tail, predelay), mixed under the dry sound. The length grows by
    the tail."""
    from scipy.signal import butter, fftconvolve, sosfilt

    n_ir = int(p["decay_s"] * 1.2 * rate)
    t = np.arange(n_ir) / rate
    pre = int(p["predelay_ms"] * rate / 1000)
    cutoff = min(0.45 * rate, 1000 + 15000 * (1 - p["damping"]))
    lp = butter(2, cutoff, "lowpass", fs=rate, output="sos")
    ir = np.zeros((pre + n_ir, x.shape[1]))
    for c in range(x.shape[1]):
        noise = np.random.RandomState(p["seed"] + c).standard_normal(n_ir) * np.exp(-6.9078 * t / p["decay_s"])
        noise = sosfilt(lp, noise)
        ir[pre:, c] = noise / np.sqrt(np.sum(noise ** 2))
    wet = np.stack([fftconvolve(x[:, c], ir[:, c]) for c in range(x.shape[1])], axis=1)
    y = np.vstack([x, np.zeros((len(wet) - len(x), x.shape[1]))]) + p["wet"] * wet
    return y, {"tail_samples": int(len(wet) - len(x)), "ir_ms": round(1000 * len(ir) / rate, 1)}


def op_echo(x, rate, p, ctx):
    d = int(round(p["delay_ms"] * rate / 1000))
    repeats = 1 if p["feedback"] == 0 else int(math.ceil(math.log(1e-3) / math.log(p["feedback"]))) + 1
    y = np.vstack([x, np.zeros((d * repeats, x.shape[1]))])
    for k in range(1, repeats + 1):
        y[k * d:k * d + len(x)] += p["mix"] * p["feedback"] ** (k - 1) * x
    return y, {"delay_samples": d, "repeats": repeats}


def _lp1(v: np.ndarray, rate: int, ms: float) -> np.ndarray:
    from scipy.signal import lfilter

    a = math.exp(-1 / (ms * rate / 1000))
    return lfilter([1 - a], [1, -a], v)


TRANSIENT_DEADBAND_DB = 1.0  # PROPOSAL: envelope differences under 1 dB (detector ripple) change nothing ...
TRANSIENT_FULL_DB = 6.0  # ... and the full attack/sustain gain applies 6 dB past the dead band


def op_transient(x, rate, p, ctx):
    """Transient shaper: a fast peak follower (0.5 ms attack, 20 ms release) and a slow one (15 ms attack, 250 ms
    release). Where the fast one is above the slow one the sound is attacking (attack_db applies), where it is below
    it is decaying (sustain_db applies), each scaled from 0 at a 1 dB difference to full at 7 dB; steady sound and
    detector ripple under 1 dB are untouched."""
    level = np.max(np.abs(x), axis=1)
    fast = _onepole_env(level, rate, 0.5, 20.0)
    slow = _onepole_env(level, rate, 15.0, 250.0)
    d = 20 * np.log10(np.maximum(fast, 1e-9)) - 20 * np.log10(np.maximum(slow, 1e-9))
    att = np.clip((d - TRANSIENT_DEADBAND_DB) / TRANSIENT_FULL_DB, 0, 1)
    sus = np.clip((-d - TRANSIENT_DEADBAND_DB) / TRANSIENT_FULL_DB, 0, 1)
    gain_db = _lp1(p["attack_db"] * att + p["sustain_db"] * sus, rate, 0.5)
    return x * (10 ** (gain_db / 20))[:, None], {"max_gain_db": round(float(gain_db.max()), 2),
                                                 "min_gain_db": round(float(gain_db.min()), 2)}


def op_saturate(x, rate, p, ctx):
    """Soft clip: tanh(g x) / tanh(g) (full scale stays full scale), mixed with the dry sound."""
    g = 10 ** (p["drive_db"] / 20)
    if g == 1:
        return x.copy(), {}
    wet = np.tanh(g * x) / math.tanh(g)
    return (1 - p["mix"]) * x + p["mix"] * wet, {}


# --------------------------------------------------------------------------------------------- edit pass

def binding_ms(x: np.ndarray, rate: int, binding: str) -> float:
    a = x - x.mean(axis=0)
    if binding == "F-01":
        return 1000 * measures.onset_index(a.mean(axis=1)) / rate
    v = measures.main_transient_ms(a, rate)
    return 0.0 if v is None else float(v)


def op_trim(x, rate, p, ctx):
    """Trim the head to the card's onset binding (rising kinds: F-01, hits: the main transient) minus a preroll; the
    preroll gets a fade-in when it is not silent, so the cut never clicks and the attack itself is untouched."""
    binding = ctx["binding"] if p["to"] == "card" else p["to"]
    t = binding_ms(x, rate, binding)
    start = max(0, int(round((t - p["preroll_ms"]) * rate / 1000)))
    y = x[start:].copy()
    pre = int(round(t * rate / 1000)) - start
    faded = False
    if start > 0 and pre > 0 and np.any(np.abs(y[:pre]) > 0):
        y[:pre] *= np.linspace(0, 1, pre, endpoint=False)[:, None]
        faded = True
    a = y - y.mean(axis=0)
    f01 = 1000 * measures.onset_index(a.mean(axis=1)) / rate
    mt = measures.main_transient_ms(a, rate)
    return y, {"binding": binding, "trimmed_ms": round(1000 * start / rate, 3), "preroll_faded": faded,
               "lead_in_ms": None if mt is None else round(max(0.0, mt - f01), 2)}


def op_cut(x, rate, p, ctx):
    if p["end_ms"] is not None:
        end = int(round(p["end_ms"] * rate / 1000))
    else:
        a = x - x.mean(axis=0)
        e, _ = measures.sound_end(a.mean(axis=1), rate)
        end = e + int(round(p["after_sound_ms"] * rate / 1000))
    end = min(len(x), max(2, end))
    peak = float(np.max(np.abs(x)))
    k = max(1, int(0.001 * rate))
    last = float(np.sqrt(np.mean(x[max(0, end - k):end] ** 2)))
    through = peak > 0 and last > peak * 10 ** (CUT_SILENT_DB / 20)
    if through and ctx.get("fade_out_ms", 0.0) < CUT_FADE_MIN_MS:
        raise SoundbenchError(f"cut: it cuts through sound ({20 * math.log10(last / peak):.1f} dB re peak) without a "
                              f"fade-out of {CUT_FADE_MIN_MS} ms or more in the edit pass: refused (a click)")
    return x[:end].copy(), {"cut_at_ms": round(1000 * end / rate, 3), "through_sound": through}


def _ramp(n: int, curve: str) -> np.ndarray:
    r = np.linspace(0, 1, n, endpoint=False) if n else np.zeros(0)
    return np.sin(r * math.pi / 2) if curve == "cosine" else r


def op_fade(x, rate, p, ctx):
    y = x.copy()
    ni = min(len(y), int(round(p["in_ms"] * rate / 1000)))
    no = min(len(y), int(round(p["out_ms"] * rate / 1000)))
    before = measures.attack_share(x - x.mean(axis=0), rate)
    if ni:
        y[:ni] *= _ramp(ni, p["curve"])[:, None]
    if no:
        y[len(y) - no:] *= _ramp(no, p["curve"])[::-1][:, None]
    after = measures.attack_share(y - y.mean(axis=0), rate)
    if ni and before and after is not None and after < FADE_IN_KEEP_SHARE * before and not ctx.get("why"):
        raise SoundbenchError(f"fade: the fade-in leaves attack share {after:.3f} of {before:.3f} (under "
                              f"{FADE_IN_KEEP_SHARE:.0%}): it softens the attack; give a `why`")
    return y, {"attack_share": [before, after]}


def op_mono(x, rate, p, ctx):
    a = x - x.mean(axis=0)
    drop = measures.cue_numbers(a, rate)["F-07_mono_drop_db"] if x.shape[1] > 1 else 0.0
    return x.mean(axis=1, keepdims=True), {"mono_drop_db": drop}


def op_loudness(x, rate, p, ctx):
    lv = ctx["level"]
    before = measures.level_db(x, rate, lv["measure"])
    g = lv["target"] - before
    y = x * 10 ** (g / 20)
    for _ in range(3):  # F-09 is exactly linear; LUFS gating can move a little: correct and re-measure
        now = measures.level_db(y, rate, lv["measure"])
        if abs(now - lv["target"]) <= LOUDNESS_MAX_ERROR_DB:
            break
        y = y * 10 ** ((lv["target"] - now) / 20)
    else:
        raise SoundbenchError(f"loudness: {lv['measure']} did not land within {LOUDNESS_MAX_ERROR_DB} dB of the target")
    return y, {"measure": lv["measure"], "before": round(before, 3), "after": round(now, 3), "gain_db": round(g, 3)}


def op_peak(x, rate, p, ctx):
    """True-peak ceiling minus a margin, by gain only (never a limiter): a spiky take loses level instead of shape."""
    limit = p["ceiling_dbtp"] - p["margin_db"]
    tp = measures.true_peak_db(x)
    if tp is None or tp <= limit:
        return x.copy(), {"true_peak_dbtp": None if tp is None else round(tp, 3), "gain_db": 0.0, "limit_dbtp": limit}
    g = limit - tp
    y = x * 10 ** (g / 20)
    return y, {"true_peak_dbtp": [round(tp, 3), round(measures.true_peak_db(y), 3)], "gain_db": round(g, 3),
               "limit_dbtp": limit}


OPS = {"dc": op_dc, "highpass": op_highpass, "lowpass": op_lowpass, "eq": op_eq, "dehum": op_dehum, "gate": op_gate,
       "varispeed": op_varispeed, "to_key": op_to_key, "compress": op_compress, "limit": op_limit, "space": op_space,
       "echo": op_echo, "transient": op_transient, "saturate": op_saturate, "trim": op_trim, "cut": op_cut,
       "fade": op_fade, "mono": op_mono, "loudness": op_loudness, "peak": op_peak}


def run(op: str, x: np.ndarray, rate: int, params: dict, ctx: dict) -> tuple[np.ndarray, dict]:
    """Run one operation. `ctx`: the card's context (kind, category, binding, level, key, why, fade_out_ms)."""
    if op in FFMPEG_OPS:
        from . import fxops

        return fxops.run(op, x, rate, params, ctx)
    y, info = OPS[op](np.asarray(x, dtype=np.float64), rate, params, ctx)
    if not np.all(np.isfinite(y)):
        raise SoundbenchError(f"{op}: produced NaN or infinite samples")
    return y, info


def kind_of(ctx: dict) -> dict:
    return KINDS[ctx["kind"]]
