"""The ffmpeg operations (editor-design.md section 4, build step 4): denoise, declick, pitch, stretch, chorus.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 4)

Each runs through the timing adapter (`ffmpeg.py`) and then a before/after guard on what it must not damage. The
rules, with the probes behind them (2026-10-23, ffmpeg 9.0.2, scratch probes 3 and 4):

| op | ffmpeg | kinds | timing | guard |
| --- | --- | --- | --- | --- |
| denoise | afftdn | any; nf at most 3 dB over the take's tail floor | waveform lag per channel = 1,102 / 1,200 samples (independent of nr, nf), compensated | level, length above the floor, balance, attack share both ways, main transient within 1 ms, roughness rise <= 0.05 |
| declick | adeclick | sustained and loop kinds only (on a clean hit it cut the attack share 0.137 -> 0.022) | lag 0 per channel | as denoise |
| pitch | rubberband pitch, transients=smooth | sustained kinds only (on a hit it smears the attack; percussive takes use varispeed) | +-3 semitones; event positions within 1 ms + 3 ms per semitone (smooth moves them 2.6-2.9 ms per semitone) | as denoise; roughness rise <= 0.05; pitch within 5 cents on a trusted note |
| stretch | rubberband tempo, transients=smooth | sustained kinds only; ratio 0.8-1.25 | length x ratio, event positions x ratio within 2 ms + 40 ms x abs(ratio - 1) (smooth moves them about 40 ms x abs(ratio - 1)) | as pitch, pitch unchanged |
| chorus | chorus | any | the audio timed on the dry path (decay 0), lag 0 per channel; the full graph timed on the probe and a stand-in; the length grows by delay + depth (declared) | channel balance only (its copies change level and envelope by design) |

Context: denoise, declick, pitch and stretch read the audio with 100 ms of context at both ends (wrap for loop
kinds, reflect otherwise) so the filter's start-up ramp falls outside the sound. When the audio cannot be timed on
itself (a tone, a loop), the timing is proven on a probe and on a stand-in of the cue's kind (the log says so).

Guard (PROPOSAL values; repair round 2 after 10 real takes), checked in both directions where both are damage:
the denoise nf at most 3 dB above the take's measured tail floor (before running; by default nf is that
floor); rubberband's broadband level loss (0.4-4.3 dB measured) restored by gain, more than 6 dB refused; F-09 within +-1.5 dB; the part of
the sound 10 dB over its floor keeps 85 % of its length (x ratio for stretch); the channel balance within 1 dB (chorus 2 dB); a sound
with an attack (attack share 0.02 or more) keeps its share within 80-125 %, its attack rise within +-2 ms and its
main transient within 1 ms, whatever the filter; an attack-free sound keeps its main transient within the filter's
own tolerance (1 ms; pitch 1 ms + 3 ms per semitone; stretch 2 ms + 40 ms x |ratio - 1|). chorus changes level and
envelope by design: only its timing and channel balance are guarded. A pitch shift on a hit labelled sustained moved
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
RISE_CHANGE_MS = 2.0  # ... its attack rise changes at most +-2 ms (design section 4: transient and rise before/after)
LEVEL_CHANGE_DB = 1.5  # PROPOSAL: F-09 moves at most +-1.5 dB through a clean-up or pitch step (not chorus)
LENGTH_KEEP = 0.85  # PROPOSAL: the sound clearly above its noise keeps 85 % of its length ...
LENGTH_FLOOR_MARGIN_DB = 10.0  # ... "clearly above" = 10 dB over the take's tail floor
BALANCE_MOVE_DB = 1.0  # PROPOSAL: the left-right level difference moves at most 1 dB ...
BALANCE_MOVE_CHORUS_DB = 2.0  # ... 2 dB for chorus (its copies follow each channel: up to 0.96 dB on 62 real takes)
NF_MARGIN_DB = 3.0  # PROPOSAL: denoise's nf may sit at most 3 dB above the take's measured tail floor
CHORUS_WET_MAX_RATIO = 0.9  # chorus decay must stay under 0.9 x in_gain: at 0.90 the probe first saw two equal copies
                            # (sweep 2026-10-23, weakest modulation, every delay, in_gain and rate; 0.85-0.89 passed)
AFFTDN_NF_MIN = -80.0  # afftdn's lowest nf: a floor under it has nothing for denoise to remove
RUBBERBAND_MAX_LOSS_DB = 6.0  # PROPOSAL: smooth rubberband loses 0.4-4.3 dB by content and rate (probe 2026-10-23);
                              # the loss is restored by gain, and more than 6 dB is refused as damage
PITCH_EVENT_BASE_MS = 1.0  # PROPOSAL: rubberband pitch (smooth) moves events about 2.6-2.9 ms per semitone, so the
PITCH_EVENT_PER_ST_MS = 3.0  # tolerance is 1 ms + 3 ms per semitone (probe: 0.5 st 1.3 ms, 2 st 5.4, 3 st 8.6)
PITCH_MAX_ST = 3.0  # PROPOSAL: larger shifts move events past 10 ms (5 st: 15 ms): use varispeed
STRETCH_MIN, STRETCH_MAX = 0.8, 1.25  # PROPOSAL: smooth rubberband moves events about 40 ms x |ratio - 1| (probe
STRETCH_EVENT_BASE_MS = 2.0             # sweep 0.6-1.5: 0.9 4.2 ms, 0.8 8.4, 1.25 10.0, 1.4 15.5, 1.5 19.6), so the
STRETCH_EVENT_PER_UNIT_MS = 40.0        # range stops at 10 ms of shift and the tolerance is 2 ms + 40 ms x |ratio - 1|
ROUGH_RISE = 0.05  # PROPOSAL: roughness may rise at most 0.05 (crisp-mode rubberband flutter read 0.08-0.17)
PITCH_CENTS_TOL = 5.0  # PROPOSAL: on a trusted note, pitch lands within 5 cents of the asked one (smooth: 0.0)
RUBBERBAND_MODE = "transients=smooth"  # probe 6: the default (crisp) put 12-27 % AM and up to 9.5 cents error on a
                                       # steady tone; smooth: AM under 1 %, 0.0 cents


def _num(lo, hi, default=REQ):
    return {"type": float, "lo": lo, "hi": hi, "default": default}


SPEC = {
    "denoise": {"nr_db": _num(1, 60, 12.0), "nf_db": _num(-80, -20, None)},  # nf default: the take's measured floor
    "declick": {"window_ms": _num(10, 100, 55.0), "overlap_pct": _num(50, 95, 75.0), "threshold": _num(1, 100, 2.0)},
    "pitch": {"semitones": _num(-PITCH_MAX_ST, PITCH_MAX_ST)},
    "stretch": {"ratio": _num(STRETCH_MIN, STRETCH_MAX)},
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
    mono = a.mean(axis=1)
    on = measures.onset_index(mono)
    end, _ = measures.sound_end(mono, rate)
    rms_ch = np.sqrt(np.mean(a ** 2, axis=0))
    return {"attack_share": measures.attack_share(a, rate), "main_transient_ms": measures.main_transient_ms(a, rate),
            "attack_rise_ms": measures.attack_rise_ms(a, rate),
            "f09_db": measures.db(measures.f09_rms(mono[on:end], rate)),
            "channel_db": [measures.db(float(v)) for v in rms_ch], "floor_dbfs": measures.tail_noise(a, rate)["floor_dbfs"]}


def sound_ms_above(x: np.ndarray, rate: int, threshold: float) -> float:
    """Length (ms) from the first to the last 10 ms window whose RMS (mono, DC removed) is at or above `threshold`."""
    a = np.asarray(x, dtype=np.float64)
    a = a - a.mean(axis=0)
    rms, n = measures.windows_rms(a.mean(axis=1), rate)
    hit = np.nonzero(rms >= threshold)[0]
    return 0.0 if not len(hit) else 1000 * (int(hit[-1]) - int(hit[0]) + 1) * n / rate


def _length_threshold(x: np.ndarray, rate: int, floor_dbfs: float | None) -> float:
    """The part of a sound that stands clearly above its noise: windows within 40 dB of the loudest one and at least
    10 dB over the take's tail floor (so removing hiss never counts as shortening the sound)."""
    a = np.asarray(x, dtype=np.float64)
    a = a - a.mean(axis=0)
    rms, _ = measures.windows_rms(a.mean(axis=1), rate)
    thr = float(rms.max()) * 10 ** (-40 / 20)
    if floor_dbfs is not None:
        thr = max(thr, 10 ** ((floor_dbfs + LENGTH_FLOOR_MARGIN_DB) / 20))
    return thr


def _guard(op: str, before: dict, after: dict, move_ms: float, scale: float = 1.0,
           x: np.ndarray | None = None, y: np.ndarray | None = None, rate: int | None = None) -> dict:
    """What the filter must not damage, checked in both directions where both are damage (F1, repair round 2):
      - level: F-09 within +-1.5 dB (not chorus: its gains change the level by design);
      - length: the part of the sound clearly above the noise keeps 85 % of its length (x ratio for stretch; not
        chorus, whose copies lengthen it by design);
      - channel balance: the left-right level difference moves at most 1 dB;
      - a sound with an attack (share >= SHARE_MIN): attack share within 80 %..125 % of its value, attack rise
        within +-2 ms, main transient within 1 ms (none of these for chorus: its copies change the envelope after
        the attack by design; its timing is proven on its dry path and the probe);
      - an attack-free sound keeps its main transient within the filter's own tolerance (`move_ms`)."""
    rec: dict = {}
    sb, sa = before["attack_share"], after["attack_share"]
    has_attack = sb is not None and sb >= SHARE_MIN
    if op != "chorus":
        fb, fa = before["f09_db"], after["f09_db"]
        if fb is not None and (fa is None or abs(fa - fb) > LEVEL_CHANGE_DB):
            raise SoundbenchError(f"{op}: F-09 level {fb:.1f} -> {fa if fa is None else round(fa, 1)} dBFS (more than "
                                  f"+-{LEVEL_CHANGE_DB} dB): it changes the sound itself, refused")
        rec["f09_db"] = [fb, fa]
        if x is not None and y is not None:
            thr = _length_threshold(x, rate, before["floor_dbfs"])
            lb, la = sound_ms_above(x, rate, thr), sound_ms_above(y, rate, thr)
            if lb > 0 and la < LENGTH_KEEP * lb * scale:
                raise SoundbenchError(f"{op}: the sound above its noise floor shrank {lb * scale:.0f} -> {la:.0f} ms "
                                      f"(keeps under {LENGTH_KEEP:.0%}): it eats the sound, refused")
            rec["sound_ms_above_floor"] = [round(lb, 1), round(la, 1)]
    cb, ca = before["channel_db"], after["channel_db"]
    if len(cb) > 1 and None not in cb and None not in ca:
        moved_bal = (ca[0] - ca[1]) - (cb[0] - cb[1])
        bal_limit = BALANCE_MOVE_CHORUS_DB if op == "chorus" else BALANCE_MOVE_DB
        if abs(moved_bal) > bal_limit:
            raise SoundbenchError(f"{op}: the channel balance moved {moved_bal:+.2f} dB (limit {bal_limit} dB): refused")
        rec["balance_moved_db"] = round(moved_bal, 3)
    if op == "chorus":
        rec.update({"attack_share": [sb, sa], "has_attack": has_attack, "attack_checks": "not for chorus"})
        return rec
    if has_attack and (sa is None or not SHARE_KEEP * sb <= sa <= sb / SHARE_KEEP):
        raise SoundbenchError(f"{op}: attack share {sb:.3f} -> {sa if sa is None else round(sa, 3)} (outside "
                              f"{SHARE_KEEP:.0%}..{1 / SHARE_KEEP:.0%}): it damages the attack or eats the body, refused")
    limit = TRANSIENT_MOVE_MS if has_attack else move_ms
    tb, ta = before["main_transient_ms"], after["main_transient_ms"]
    moved = None if tb is None or ta is None else ta - tb * scale
    if moved is not None and abs(moved) > limit:
        raise SoundbenchError(f"{op}: main transient moved {moved:+.2f} ms (limit {limit} ms"
                              f"{' for a sound with an attack' if has_attack else ''}): refused")
    rb, ra = before["attack_rise_ms"], after["attack_rise_ms"]
    grew = None if rb is None or ra is None else ra - rb * scale
    if has_attack and grew is not None and abs(grew) > RISE_CHANGE_MS:
        raise SoundbenchError(f"{op}: attack rise changed {grew:+.2f} ms (limit +-{RISE_CHANGE_MS} ms): refused")
    rec.update({"attack_share": [sb, sa], "main_transient_ms": [tb, ta],
                "transient_moved_ms": None if moved is None else round(moved, 3), "attack_rise_ms": [rb, ra],
                "has_attack": has_attack})
    return rec


def denoise_floor_check(x: np.ndarray, rate: int, nf_db: float | None) -> tuple[float, float]:
    """afftdn's nf is an absolute noise floor (dBFS): above the take's own floor it treats the sound as noise. The
    reviewer's case: a take peaking at -36 dBFS with nf -20 lost 14.5 dB and two thirds of its length."""
    a = np.asarray(x, dtype=np.float64)
    floor = measures.tail_noise(a - a.mean(axis=0), rate)["floor_dbfs"]
    if floor is None:
        raise SoundbenchError("denoise: the take's tail is digital silence: there is no noise floor to remove, refused")
    if nf_db is None:  # the default: afftdn's floor at the take's own measured floor
        if floor < AFFTDN_NF_MIN:
            raise SoundbenchError(f"denoise: the take's floor {floor:.1f} dBFS is under afftdn's lowest nf "
                                  f"({AFFTDN_NF_MIN:g} dBFS): nothing to remove, refused")
        nf_db = round(floor, 1)
    if nf_db > floor + NF_MARGIN_DB:
        raise SoundbenchError(f"denoise: nf {nf_db:.2f} dBFS is above the limit {floor + NF_MARGIN_DB:.2f} dBFS (the take's "
                              f"measured tail floor {floor:.2f} dBFS + {NF_MARGIN_DB:g} dB): afftdn would treat the sound "
                              "as noise; set nf_db at or below the floor, refused")
    return floor, nf_db


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
        floor, nf = denoise_floor_check(x32, rate, p["nf_db"])
        before["nf_used"] = {"floor_dbfs": floor, "nf_db": nf, "auto": p["nf_db"] is None}
        graph = f"afftdn=nr={_fmt(p['nr_db'])}:nf={_fmt(nf)}"
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
        scale = p["ratio"]
        move = STRETCH_EVENT_BASE_MS + STRETCH_EVENT_PER_UNIT_MS * abs(p["ratio"] - 1)
        graph = f"rubberband=tempo={_fmt(1 / p['ratio'])}:{RUBBERBAND_MODE}"
        res = ffmpeg.run_filter_events(x32, rate, graph, time_scale=p["ratio"], tolerance_ms=move,
                                       standin_kind=ctx["kind"], context=context)
    else:  # chorus: a modulated delay under the dry sound; no start-up ramp, the tail grows
        def chorus_graph(decay: float) -> str:
            return (f"chorus={_fmt(p['in_gain'])}:{_fmt(p['out_gain'])}:{_fmt(p['delay_ms'])}:{_fmt(decay)}:"
                    f"{_fmt(p['speed_hz'])}:{_fmt(p['depth_ms'])}")

        graph = chorus_graph(p["decay"])
        lat = ffmpeg.known_latency("chorus", rate)
        # its wet copy moves the audio's correlation peak (real whoosh: 11 samples): the audio is timed on the dry
        # path (the same graph, decay 0), and the full graph on the probe and a stand-in of the kind (F5)
        dry = ffmpeg.run_filter(x32, rate, chorus_graph(0.0), latency_samples=lat, length_change=True,
                                standin_kind=ctx["kind"])
        res = ffmpeg.run_filter(x32, rate, graph, latency_samples=lat, length_change=True,
                                standin_kind=ctx["kind"], timing="probe")
        res.log["dry_path_timing"] = {k: dry.log.get(k) for k in ("timing_source", "channel_lags_samples")}
    y = np.asarray(res.audio, dtype=np.float64)
    y = y[:, None] if y.ndim == 1 else y
    info = {"graph": graph, "timing": {k: v for k, v in res.log.items() if k not in ("ffmpeg",)}}
    if "nf_used" in before:
        info["nf_used"] = before.pop("nf_used")
    if op in ("pitch", "stretch"):  # restore rubberband's broadband gain loss by gain; refuse a loss that big
        rin = float(np.sqrt(np.mean(np.asarray(x32, dtype=np.float64) ** 2)))
        rout = float(np.sqrt(np.mean(y ** 2)))
        if rin > 0 and rout > 0:
            loss = 20 * np.log10(rin / rout)
            if loss > RUBBERBAND_MAX_LOSS_DB:
                raise SoundbenchError(f"{op}: rubberband lost {loss:.1f} dB (limit {RUBBERBAND_MAX_LOSS_DB} dB): refused")
            y = y * (rin / rout)
            info["level_restored_db"] = round(float(loss), 3)
    info["guard"] = _guard(op, before, _snap(y, rate), move, scale, x32, y, rate)
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
