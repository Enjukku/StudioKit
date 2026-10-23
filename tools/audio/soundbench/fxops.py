"""The ffmpeg operations (editor-design.md section 4, build step 4): denoise, declick, pitch, stretch, chorus.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 4)

Each runs through the timing adapter (`ffmpeg.py`) and then a before/after guard on what it must not damage. The
rules, with the probes behind them (2026-10-23, ffmpeg 9.0.2, scratch probes 3 and 4):

| op | ffmpeg | kinds | timing | guard |
| --- | --- | --- | --- | --- |
| denoise | afftdn | any | waveform lag per channel = 1,102 / 1,200 samples (independent of nr, nf), compensated | attack share kept, main transient within 1 ms, roughness rise <= 0.05 |
| declick | adeclick | sustained and loop kinds only (on a clean hit it cut the attack share 0.137 -> 0.022) | lag 0 per channel | as denoise |
| pitch | rubberband pitch, transients=smooth | sustained kinds only (on a hit it smears the attack; percussive takes use varispeed) | +-3 semitones; event positions within 1 ms + 3 ms per semitone (smooth moves them 2.6-2.9 ms per semitone) | as denoise; roughness rise <= 0.05; pitch within 5 cents on a trusted note |
| stretch | rubberband tempo, transients=smooth | sustained kinds only | length x ratio, event positions x ratio within 15 ms (smooth moves them 7-12 ms) | as pitch, pitch unchanged |
| chorus | chorus | any | lag 0 per channel; the length grows by delay + depth (declared) | as denoise |

Context: denoise, declick, pitch and stretch read the audio with 100 ms of context at both ends (wrap for loop
kinds, reflect otherwise) so the filter's start-up ramp falls outside the sound. When the audio cannot be timed on
itself (a tone, a loop), the timing is proven on a probe and on a stand-in of the cue's kind (the log says so).

Guard (PROPOSAL values): a sound with an attack (attack share 0.02 or more) keeps 80 % of its attack share (not
for chorus, whose copies add energy after the attack by design), its main transient within 1 ms and its attack rise
within +2 ms, whatever the filter; an attack-free sound keeps its main transient within the filter's own tolerance
(1 ms; pitch 1 ms + 3 ms per semitone; stretch 15 ms, scaled by the ratio). A pitch shift on a hit labelled sustained moved
its transient 2.8 ms at 48 kHz in the probe: refused by the 1 ms rule.

Usage:
  from tools.audio.soundbench import fxops
  y, info = fxops.run("denoise", x, 44100, {"nr_db": 12, "nf_db": -50}, {"kind": "hit"})
"""

from __future__ import annotations

import numpy as np

from . import ffmpeg, measures
from .card import KINDS
from .core import SoundbenchError

REQ = object()
SHARE_KEEP = 0.8  # PROPOSAL: the attack share keeps at least 80 % of its value ...
SHARE_MIN = 0.02  # ... when it is at least 0.02
TRANSIENT_MOVE_MS = 1.0  # PROPOSAL: a sound with an attack: the main transient moves at most 1 ms, any filter ...
RISE_GROW_MS = 2.0  # ... and its attack rise grows at most 2 ms (design section 4: transient and rise before/after)
PITCH_EVENT_BASE_MS = 1.0  # PROPOSAL: rubberband pitch (smooth) moves events about 2.6-2.9 ms per semitone, so the
PITCH_EVENT_PER_ST_MS = 3.0  # tolerance is 1 ms + 3 ms per semitone (probe: 0.5 st 1.3 ms, 2 st 5.4, 3 st 8.6)
PITCH_MAX_ST = 3.0  # PROPOSAL: larger shifts move events past 10 ms (5 st: 15 ms): use varispeed
STRETCH_EVENT_TOL_MS = 15.0  # PROPOSAL: rubberband tempo (smooth) moved events 7-12 ms (ratios 0.8-2)
ROUGH_RISE = 0.05  # PROPOSAL: roughness may rise at most 0.05 (crisp-mode rubberband flutter read 0.08-0.17)
PITCH_CENTS_TOL = 5.0  # PROPOSAL: on a trusted note, pitch lands within 5 cents of the asked one (smooth: 0.0)
RUBBERBAND_MODE = "transients=smooth"  # probe 6: the default (crisp) put 12-27 % AM and up to 9.5 cents error on a
                                       # steady tone; smooth: AM under 1 %, 0.0 cents


def _num(lo, hi, default=REQ):
    return {"type": float, "lo": lo, "hi": hi, "default": default}


SPEC = {
    "denoise": {"nr_db": _num(1, 60, 12.0), "nf_db": _num(-80, -20, -50.0)},
    "declick": {"window_ms": _num(10, 100, 55.0), "overlap_pct": _num(50, 95, 75.0), "threshold": _num(1, 100, 2.0)},
    "pitch": {"semitones": _num(-PITCH_MAX_ST, PITCH_MAX_ST)},
    "stretch": {"ratio": _num(0.5, 2.0)},
    "chorus": {"delay_ms": _num(5, 100, 40.0), "decay": _num(0, 1, 0.4), "speed_hz": _num(0.05, 5, 0.25),
               "depth_ms": _num(0.1, 10, 2.0), "in_gain": _num(0, 1, 0.7), "out_gain": _num(0, 1, 0.9)},
}


def _fmt(v: float) -> str:
    return f"{v:.6g}"


def _kind(ctx: dict) -> dict:
    k = ctx.get("kind")
    if k not in KINDS:
        raise SoundbenchError(f"ffmpeg operations need the card's kind, got {k!r}")
    return KINDS[k]


def _sustained_only(op: str, ctx: dict) -> None:
    if not _kind(ctx)["sustained"]:
        raise SoundbenchError(f"{op}: sustained sounds and loops only; a {ctx['kind']} is not sustained "
                              f"({'percussive takes use varispeed' if op in ('pitch', 'stretch') else 'on a clean hit it cut the attack share from 0.137 to 0.022'})")


def _snap(x: np.ndarray, rate: int) -> dict:
    a = np.asarray(x, dtype=np.float64)
    a = a - a.mean(axis=0)
    return {"attack_share": measures.attack_share(a, rate), "main_transient_ms": measures.main_transient_ms(a, rate),
            "attack_rise_ms": measures.attack_rise_ms(a, rate)}


def _guard(op: str, before: dict, after: dict, move_ms: float, scale: float = 1.0) -> dict:
    """What the filter must not damage. A sound with an attack (share >= SHARE_MIN) keeps 80 % of its attack share
    (not checked for chorus: its copies add energy after the attack by design), its main transient within 1 ms and
    its rise within +2 ms, whatever the filter's own event tolerance; an attack-free sound keeps its main transient
    within the filter's tolerance (`move_ms`). Times scale by the stretch ratio."""
    sb, sa = before["attack_share"], after["attack_share"]
    has_attack = sb is not None and sb >= SHARE_MIN
    if has_attack and op != "chorus" and (sa is None or sa < SHARE_KEEP * sb):
        raise SoundbenchError(f"{op}: attack share {sb:.3f} -> {sa if sa is None else round(sa, 3)} (keeps under "
                              f"{SHARE_KEEP:.0%}): it damages the attack, refused")
    limit = TRANSIENT_MOVE_MS if has_attack else move_ms
    tb, ta = before["main_transient_ms"], after["main_transient_ms"]
    moved = None if tb is None or ta is None else ta - tb * scale
    if moved is not None and abs(moved) > limit:
        raise SoundbenchError(f"{op}: main transient moved {moved:+.2f} ms (limit {limit} ms"
                              f"{' for a sound with an attack' if has_attack else ''}): refused")
    rb, ra = before["attack_rise_ms"], after["attack_rise_ms"]
    grew = None if rb is None or ra is None else ra - rb * scale
    if has_attack and grew is not None and grew > RISE_GROW_MS:
        raise SoundbenchError(f"{op}: attack rise grew {grew:+.2f} ms (limit {RISE_GROW_MS} ms): it smears the attack, "
                              "refused")
    return {"attack_share": [sb, sa], "main_transient_ms": [tb, ta], "transient_moved_ms": None if moved is None
            else round(moved, 3), "attack_rise_ms": [rb, ra], "has_attack": has_attack}


def run(op: str, x: np.ndarray, rate: int, p: dict, ctx: dict) -> tuple[np.ndarray, dict]:
    if op not in SPEC:
        raise SoundbenchError(f"unknown ffmpeg operation {op!r}")
    kind = _kind(ctx)
    context = "wrap" if kind["loop"] else "reflect"
    x32 = np.asarray(x, dtype=np.float32)
    x32 = x32[:, None] if x32.ndim == 1 else x32
    before = _snap(x32, rate)
    scale, move = 1.0, TRANSIENT_MOVE_MS
    if op == "denoise":
        graph = f"afftdn=nr={_fmt(p['nr_db'])}:nf={_fmt(p['nf_db'])}"
        res = ffmpeg.run_filter(x32, rate, graph, latency_samples=ffmpeg.known_latency("afftdn", rate),
                                context=context, standin_kind=ctx["kind"])
    elif op == "declick":
        _sustained_only(op, ctx)
        graph = f"adeclick=w={_fmt(p['window_ms'])}:o={_fmt(p['overlap_pct'])}:t={_fmt(p['threshold'])}"
        res = ffmpeg.run_filter(x32, rate, graph, latency_samples=ffmpeg.known_latency("adeclick", rate),
                                context=context, standin_kind=ctx["kind"])
    elif op == "pitch":
        _sustained_only(op, ctx)
        graph = f"rubberband=pitch={_fmt(2 ** (p['semitones'] / 12))}:{RUBBERBAND_MODE}"
        move = PITCH_EVENT_BASE_MS + PITCH_EVENT_PER_ST_MS * abs(p["semitones"])
        res = ffmpeg.run_filter_events(x32, rate, graph, time_scale=1.0, tolerance_ms=move,
                                       standin_kind=ctx["kind"], context=context)
    elif op == "stretch":
        _sustained_only(op, ctx)
        scale, move = p["ratio"], STRETCH_EVENT_TOL_MS
        graph = f"rubberband=tempo={_fmt(1 / p['ratio'])}:{RUBBERBAND_MODE}"
        res = ffmpeg.run_filter_events(x32, rate, graph, time_scale=p["ratio"], tolerance_ms=STRETCH_EVENT_TOL_MS,
                                       standin_kind=ctx["kind"], context=context)
    else:  # chorus: a modulated delay under the dry sound; no start-up ramp, the tail grows
        graph = (f"chorus={_fmt(p['in_gain'])}:{_fmt(p['out_gain'])}:{_fmt(p['delay_ms'])}:{_fmt(p['decay'])}:"
                 f"{_fmt(p['speed_hz'])}:{_fmt(p['depth_ms'])}")
        res = ffmpeg.run_filter(x32, rate, graph, latency_samples=ffmpeg.known_latency("chorus", rate),
                                length_change=True, standin_kind=ctx["kind"])
    y = np.asarray(res.audio, dtype=np.float64)
    y = y[:, None] if y.ndim == 1 else y
    info = {"graph": graph, "timing": {k: v for k, v in res.log.items() if k not in ("ffmpeg",)}}
    info["guard"] = _guard(op, before, _snap(y, rate), move, scale)
    if op != "chorus":  # chorus adds movement on purpose
        info["guard"]["roughness"] = _rough_guard(op, x32, y, rate)
    if op in ("pitch", "stretch"):
        want = p["semitones"] * 100 if op == "pitch" else 0.0
        info["guard"]["pitch_cents"] = _pitch_guard(op, x32, y, rate, want)
    return y, info


def _rough_guard(op: str, x: np.ndarray, y: np.ndarray, rate: int) -> list:
    rb = measures.roughness(np.asarray(x, dtype=np.float64) - x.mean(axis=0), rate)
    ra = measures.roughness(y - y.mean(axis=0), rate)
    if rb is not None and ra is not None and ra - rb > ROUGH_RISE:
        raise SoundbenchError(f"{op}: roughness {rb:.3f} -> {ra:.3f} (rise over {ROUGH_RISE}): it adds flutter, refused")
    return [rb, ra]


def fine_pitch_hz(x: np.ndarray, rate: int) -> float | None:
    """The strongest component (60 Hz-4 kHz) of the middle half of the sound: Hann window, zero padding x8,
    parabolic interpolation (F-10's 200 ms window reads only to 5 Hz)."""
    a = np.asarray(x, dtype=np.float64).mean(axis=1)
    a = a[len(a) // 4:3 * len(a) // 4]
    if len(a) < 256:
        return None
    spec = np.abs(np.fft.rfft(a * np.hanning(len(a)), 8 * len(a)))
    f = np.fft.rfftfreq(8 * len(a), 1 / rate)
    band = np.nonzero((f >= 60) & (f <= 4000))[0]
    i = int(band[np.argmax(spec[band])])
    if spec[i] <= 0 or i < 1 or i + 1 >= len(spec):
        return None
    lo, mid, hi = np.log(np.maximum(spec[i - 1:i + 2], 1e-30))
    den = lo - 2 * mid + hi
    return float((i + (0.5 * (lo - hi) / den if den else 0.0)) * rate / (8 * len(a)))


def _pitch_guard(op: str, x: np.ndarray, y: np.ndarray, rate: int, want_cents: float) -> float | None:
    """On a trusted note (F-10), the pitch must land within PITCH_CENTS_TOL of the asked shift."""
    a = np.asarray(x, dtype=np.float64)
    f10 = measures.pitch((a - a.mean(axis=0)).mean(axis=1), rate, False)
    if not f10.get("trusted"):
        return None
    hb, ha = fine_pitch_hz(a, rate), fine_pitch_hz(y, rate)
    if not hb or not ha:
        return None
    err = 1200 * np.log2(ha / hb) - want_cents
    if abs(err) > PITCH_CENTS_TOL:
        raise SoundbenchError(f"{op}: the pitch landed {err:+.1f} cents from the asked shift (limit {PITCH_CENTS_TOL}): "
                              "refused")
    return round(float(err), 2)
