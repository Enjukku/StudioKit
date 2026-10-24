"""Layers, loops and variants (editor-design.md section 4, build step 6): one delivered sound from several takes, or
several deliveries from one sound. `render` runs them; this module holds their parameters and their numpy work.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 6)

Where they sit in a render (each step logged with before/after numbers, G-2):
  source(s) -> [each layer: resample to the mix rate if needed (logged), its own design pass, gain, fades, placed]
  -> mix (each layer's share measured; peak and true peak checked with export's own check) -> design pass (on the
  mix when there are layers) -> loop -> [each variant: varispeed, level offset] -> edit pass -> export (FLAC).

Layers (recipe "layers", instead of "take"): each layer is {"take", "design", "offset_ms" or "align", "gain_db",
  "fade_in_ms", "fade_out_ms", "targets", "name"}. A layer lands at round(offset_ms x rate / 1000) samples, exactly,
  on every channel in its own channel order (a mono layer goes to both channels of a stereo mix); `align` puts the
  layer's main transient (or F-01 onset), as `measures` reads it, on the marker sample round(to_ms x rate / 1000).
  The mix rate is the first layer's rate; a layer at another rate is resampled on load with `resample_poly` at the
  exact rational ratio (zero phase: its events keep their time within one sample), with a log line.
Loops (recipe "loop"): `loop_bed` and `loop_music` both deliver x[s : s+n] whose last `crossfade` samples fade from
  the loop's own end into the material just before its start, x[s-L : s]: the file's last sample is exactly x[s-1]
  and its first exactly x[s], so the wrap is a pair of neighbouring source samples (sample-exact by construction, and
  kept through FLAC export by export's own read-back). `loop_bed` takes start and end in ms (and can search the end
  for the best match); `loop_music` takes the downbeat, the BPM, the bars and the beats per bar: n is the bar length
  rounded to a whole sample, and the rounding drift is logged. The curve is equal power for uncorrelated material and
  equal gain for correlated material (`auto` picks by the measured correlation of the two crossfaded parts).
Variants (recipe "variants" or "takes"): n files with stratified seeded pitch (`varispeed`) and level changes from
  one sound, or one file per take. Refused for tell, warning and countdown cards (SC-12).

Usage:
  from tools.audio.soundbench import assemble
  y, info = assemble.loop_bed(x, 44100, ops.check_params("loop_bed", step, assemble.LOOP_SPEC["loop_bed"]))
"""

from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

from . import measures, ops
from .core import SoundbenchError

REQ = ops.REQ
_num = ops._num

# PROPOSAL values
MAX_LAYERS = 8  # the five layer jobs (craft-process section 3) plus room for splices
CROSSFADE_MAX_SHARE = 0.5  # a loop's crossfade is at most half the loop
LINEAR_FROM_CORRELATION = math.sqrt(2) - 1  # derived: above it an equal-gain crossfade's middle sits closer to 0 dB
VARIANT_MAX_COUNT = 16  # S-88: 4-10 for the most frequent cues
VARIANT_MAX_DB = 1.0  # R-31: variants of one sound within +-1 dB
VARIANT_KEYED_MAX_CENTS = 30.0  # S-91: pitched and reward cues +-0-30 cents (a card with a key)

LAYER_SPEC = {"offset_ms": _num(0, 60000, None), "gain_db": _num(-48, 12, 0.0), "fade_in_ms": _num(0, 10000, 0.0),
              "fade_out_ms": _num(0, 10000, 0.0)}
ALIGN_SPEC = {"to_ms": _num(0, 60000), "on": {"type": "choice", "options": ("main_transient", "F-01"),
                                               "default": "main_transient"}}
CURVES = {"type": "choice", "options": ("auto", "power", "linear"), "default": "auto"}
LOOP_SPEC = {
    "loop_bed": {"crossfade_ms": _num(5, 10000, 500.0), "start_ms": _num(0, 7 * 60 * 1000, None),
                 "end_ms": _num(1, 7 * 60 * 1000, None), "search_ms": _num(0, 100, 0.0), "curve": CURVES},
    "loop_music": {"bpm": _num(40, 300), "bars": _num(1, 256, REQ, int), "beats_per_bar": _num(1, 16, 4, int),
                   "start_ms": _num(0, 7 * 60 * 1000), "crossfade_ms": _num(1, 2000, 20.0), "curve": CURVES},
}
VARIANT_SPEC = {"count": _num(2, VARIANT_MAX_COUNT, None, int), "seed": _num(0, 2 ** 31 - 1, REQ, int),
                "max_cents": _num(0, 200, 50.0), "max_db": _num(0, VARIANT_MAX_DB, 0.5)}


def samples(ms: float, rate: int) -> int:
    return int(round(ms * rate / 1000))


# --------------------------------------------------------------------------------------------- layers

def resample(x: np.ndarray, rate: int, to_rate: int) -> tuple[np.ndarray, dict]:
    """A layer at another rate, resampled at the exact rational ratio (zero phase: no delay)."""
    from scipy.signal import resample_poly

    f = Fraction(to_rate, rate)
    y = resample_poly(x, f.numerator, f.denominator, axis=0)
    return y, {"from_rate": rate, "to_rate": to_rate, "up": f.numerator, "down": f.denominator,
               "samples": [len(x), len(y)]}


def transient_index(x: np.ndarray, rate: int, on: str) -> int:
    """The sample a layer is aligned by: F-01's onset, or the main transient as `measures.main_transient_ms` reads it
    (envelope index + the window-centre offset, so the placed layer measures to the marker)."""
    pad = 2 * max(1, int(round(measures.ENV_S * rate)))  # read the layer as it will sit in the file, after silence:
    a = np.vstack([np.zeros((pad, x.shape[1])), x])     # a take loud at its first sample read 0.84 ms later alone
    a = a - a.mean(axis=0)
    if on == "F-01":
        return measures.onset_index(a.mean(axis=1)) - pad
    found = measures.main_transient_index(a, rate)
    if found is None:
        raise SoundbenchError("align: the layer is silent, it has no transient")
    return found[0] + int(found[1]) - pad


def shape_layer(x: np.ndarray, rate: int, gain_db: float, fade_in_ms: float, fade_out_ms: float) -> np.ndarray:
    y = x * 10 ** (gain_db / 20)
    ni, no = min(len(y), samples(fade_in_ms, rate)), min(len(y), samples(fade_out_ms, rate))
    if ni:
        y[:ni] *= ops._ramp(ni, "cosine")[:, None]
    if no:
        y[len(y) - no:] *= ops._ramp(no, "cosine")[::-1][:, None]
    return y


def place(parts: list[tuple[np.ndarray, int]]) -> tuple[np.ndarray, list[np.ndarray]]:
    """Mix (audio, offset in samples) pairs: each lands at its offset on its own channels (mono goes to every channel);
    the mix is as long as the latest layer end. Returns the mix and each layer as placed (the mix's length)."""
    channels = max(a.shape[1] for a, _ in parts)
    length = max(off + len(a) for a, off in parts)
    placed = []
    for a, off in parts:
        if a.shape[1] != channels:
            if a.shape[1] != 1:
                raise SoundbenchError(f"layers: a {a.shape[1]}-channel layer cannot go into a {channels}-channel mix")
            a = np.repeat(a, channels, axis=1)
        p = np.zeros((length, channels))
        p[off:off + len(a)] = a
        placed.append(p)
    return np.sum(placed, axis=0), placed


def shares(placed: list[np.ndarray], mix: np.ndarray) -> dict:
    """Each layer's share of the mix, measured on the placed layers (before the mix's design pass):
    `energy`: its energy over the sum of every layer's energy (what it would weigh with no interference);
    `of_mix`: its projection on the mix, sum(layer x mix) / sum(mix x mix) (these add to 1; negative = it cancels);
    `interference_db`: the mix's energy against the sum of the layers' energies (0 dB: independent layers; + they add
    in phase; - they cancel)."""
    e = [float(np.sum(p ** 2)) for p in placed]
    em = float(np.sum(mix ** 2))
    tot = sum(e)
    return {"energy": [round(v / tot, 4) if tot > 0 else None for v in e],
            "of_mix": [round(float(np.sum(p * mix)) / em, 4) if em > 0 else None for p in placed],
            "interference_db": None if tot <= 0 or em <= 0 else round(10 * math.log10(em / tot), 2)}


# --------------------------------------------------------------------------------------------- loops

def crossfade_gains(n: int, curve: str) -> tuple[np.ndarray, np.ndarray]:
    """(fade in, fade out) over n samples, ending exactly at (1, 0)."""
    t = np.arange(1, n + 1) / n
    if curve == "linear":
        return t, 1.0 - t
    fi, fo = np.sin(np.pi / 2 * t), np.cos(np.pi / 2 * t)
    fi[-1], fo[-1] = 1.0, 0.0
    return fi, fo


def correlation(a: np.ndarray, b: np.ndarray) -> float | None:
    a, b = a.mean(axis=1), b.mean(axis=1)
    a, b = a - a.mean(), b - b.mean()
    d = math.sqrt(float(np.sum(a * a)) * float(np.sum(b * b)))
    return None if d <= 0 else float(np.sum(a * b)) / d


def wrap(x: np.ndarray, s: int, n: int, cross: int, curve: str) -> np.ndarray:
    """x[s : s+n] with its last `cross` samples faded into x[s-cross : s]: last sample x[s-1], first x[s]."""
    y = x[s:s + n].copy()
    fi, fo = crossfade_gains(cross, curve)
    y[n - cross:] = fo[:, None] * x[s + n - cross:s + n] + fi[:, None] * x[s - cross:s]
    return y


def crossfade_level(out: np.ndarray, a: np.ndarray, b: np.ndarray, rate: int) -> dict:
    """The crossfade measured against its own two source parts (a fades out, b fades in), in 50 ms windows (one window
    when shorter): how far the level made lies outside the band between the two parts' own levels in that window (dB;
    0 = between them, as a crossfade that adds no interference makes it; negative = under both: out-of-phase parts,
    an equal-gain curve on uncorrelated parts; positive = over both: in-phase parts on an equal-power curve).
    Relative to the material itself, so the bed's own swells and a loud part fading into a quiet one do not count."""
    n = len(out)
    w = min(n, max(1, int(round(measures.LOOP_WINDOW_S * rate))))
    devs = []
    for st in range(0, n - w + 1, w):
        ea, eb = float(np.sum(a[st:st + w] ** 2)), float(np.sum(b[st:st + w] ** 2))
        eo = float(np.sum(out[st:st + w] ** 2))
        lo, hi = min(ea, eb), max(ea, eb)
        if lo <= 0 or eo <= 0:
            continue
        devs.append(10 * math.log10(eo / lo) if eo < lo else 10 * math.log10(eo / hi) if eo > hi else 0.0)
    return {"window_ms": round(1000 * w / rate, 2), "windows": len(devs),
            "min_db": round(min(devs), 2) if devs else None, "max_db": round(max(devs), 2) if devs else None}


def _curve(asked: str, corr: float | None) -> str:
    if asked != "auto":
        return asked
    return "linear" if corr is not None and corr >= LINEAR_FROM_CORRELATION else "power"


def _mid_db(curve: str, corr: float | None) -> float | None:
    """The expected level at the crossfade's middle for two equally loud parts with this correlation (0 dB = even)."""
    if corr is None:
        return None
    g = (1 + corr) if curve == "power" else 0.5 * (1 + corr)
    return None if g <= 0 else round(10 * math.log10(g), 2)


def _check_region(x: np.ndarray, s: int, n: int, cross: int, what: str) -> None:
    if cross < 1:
        raise SoundbenchError(f"{what}: the crossfade is under one sample")
    if s < cross:
        raise SoundbenchError(f"{what}: the loop starts {s} samples in, under its crossfade of {cross}: the crossfade "
                              "fades into the material before the start (start later or shorten the crossfade)")
    if s + n > len(x):
        raise SoundbenchError(f"{what}: the loop ends at sample {s + n}, past the sound's end {len(x)}")
    if cross > CROSSFADE_MAX_SHARE * n:
        raise SoundbenchError(f"{what}: the crossfade ({cross} samples) is over {CROSSFADE_MAX_SHARE:.0%} of the loop "
                              f"({n} samples)")


def loop_bed(x: np.ndarray, rate: int, p: dict) -> tuple[np.ndarray, dict]:
    cross = samples(p["crossfade_ms"], rate)
    s = cross if p["start_ms"] is None else samples(p["start_ms"], rate)
    e = len(x) if p["end_ms"] is None else samples(p["end_ms"], rate)
    _check_region(x, s, e - s, cross, "loop_bed")
    info: dict = {}
    if p["search_ms"] > 0:
        e, info["search"] = _search_end(x, s, e, cross, samples(p["search_ms"], rate))
        _check_region(x, s, e - s, cross, "loop_bed")
    n = e - s
    corr = correlation(x[e - cross:e], x[s - cross:s])
    curve = _curve(p["curve"], corr)
    info.update({"start_sample": s, "end_sample": e, "loop_samples": n, "crossfade_samples": cross,
                 "correlation": None if corr is None else round(corr, 4), "curve": curve,
                 "expected_mid_db": _mid_db(curve, corr), "wrap_from_source": [s - 1, s]})
    y = wrap(x, s, n, cross, curve)
    info["crossfade_level_db"] = crossfade_level(y[n - cross:], x[e - cross:e], x[s - cross:s], rate)
    return y, info


def _search_end(x: np.ndarray, s: int, e: int, cross: int, span: int) -> tuple[int, dict]:
    """The end within +-span samples whose last `cross` samples best match the material before the start."""
    from scipy.signal import correlate

    mono = x.mean(axis=1) - x.mean()
    lo, hi = max(s + 2 * cross, e - span), min(len(x), e + span)
    if hi < lo:
        return e, {"from": e, "to": e, "correlation": None}
    b = mono[s - cross:s]
    seg = mono[lo - cross:hi]
    dots = correlate(seg, b, mode="valid")  # dots[j] = segment ending at lo + j
    c = np.concatenate([[0.0], np.cumsum(seg ** 2)])
    en = c[cross:] - c[:-cross]
    nb = math.sqrt(float(np.sum(b * b)))
    score = dots / np.maximum(np.sqrt(np.maximum(en, 0.0)) * nb, 1e-30)
    j = int(np.argmax(score))
    return lo + j, {"from": e, "to": lo + j, "moved_samples": lo + j - e, "correlation": round(float(score[j]), 4)}


def bar_samples(bars: int, beats_per_bar: int, bpm: float, rate: int) -> tuple[int, float]:
    """The loop length in whole samples (rounded, never floored: the drift stays within half a sample per loop) and
    the exact length it stands for."""
    exact = bars * beats_per_bar * 60.0 / bpm * rate
    return int(round(exact)), exact


def loop_music(x: np.ndarray, rate: int, p: dict) -> tuple[np.ndarray, dict]:
    n, exact = bar_samples(p["bars"], p["beats_per_bar"], p["bpm"], rate)
    s = samples(p["start_ms"], rate)
    cross = samples(p["crossfade_ms"], rate)
    _check_region(x, s, n, cross, "loop_music")
    corr = correlation(x[s + n - cross:s + n], x[s - cross:s])
    curve = _curve(p["curve"], corr)
    drift = n - exact
    y = wrap(x, s, n, cross, curve)
    return y, {
        "crossfade_level_db": crossfade_level(y[n - cross:], x[s + n - cross:s + n], x[s - cross:s], rate),
        "downbeat_sample": s, "loop_samples": n, "exact_samples": round(exact, 4), "drift_samples_per_loop": round(drift, 4),
        "drift_ms_per_10_min": round(1000 * drift / rate * (600.0 / (n / rate)), 3), "crossfade_samples": cross,
        "correlation": None if corr is None else round(corr, 4), "curve": curve, "expected_mid_db": _mid_db(curve, corr),
        "wrap_from_source": [s - 1, s]}


LOOPS = {"loop_bed": loop_bed, "loop_music": loop_music}


# --------------------------------------------------------------------------------------------- variants

def variant_plan(count: int, seed: int, max_cents: float, max_db: float) -> list[dict]:
    """Stratified seeded draws: the range is cut into `count` equal slots, one value drawn in each, and the slots are
    shuffled, so the set spreads over the whole range (two plain random draws can land on the same value). The same
    seed gives the same plan (numpy RandomState: its stream is stable across numpy versions)."""
    rs = np.random.RandomState(seed)

    def strata(m: float) -> list[float]:
        if m == 0:
            return [0.0] * count
        edges = np.linspace(-m, m, count + 1)
        vals = edges[:-1] + rs.uniform(0, 1, count) * (edges[1:] - edges[:-1])
        return [float(v) for v in vals[rs.permutation(count)]]

    cents, gains = strata(max_cents), strata(max_db)
    return [{"k": i + 1, "cents": round(c, 1), "gain_db": round(g, 2)} for i, (c, g) in enumerate(zip(cents, gains))]
