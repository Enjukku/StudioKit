"""The ffmpeg adapter (design G-7): run one filter graph on a buffer and prove that time, rate and channels are kept.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2; repair round 1:
per-channel lag, declared latency, probe for periodic audio)

Why it exists: review-1 measured that `afftdn` delays audio by exactly 1,102 samples (25.0 ms at 44.1 kHz; 1,200 at
48 kHz) and cuts the tail by the same amount, with no error and the same file length. So after every call this
adapter checks, and refuses with `SoundbenchError` instead of returning shifted or damaged audio:
  1. same sample rate and same channel count as the input; no NaN or infinite samples;
  2. same length (input plus its declared-latency padding), unless the call declares a length change;
  3. **every channel's lag, measured against its own input channel** (`measures.lag`, DC removed). All channels
     must read the same lag, and it must equal the call's **declared** latency (`latency_samples`, 0 by default)
     exactly (tolerance 0 samples: afftdn's delay is a whole number of samples, read identical on every channel of
     6 fixtures at 4 rates; a graph that adds any other delay, such as `afftdn,lowpass` at +3 samples, is refused).
     A known latency is compensated by the declared value, never by the reading; an unknown one is refused (G-7).
     The input is padded with the declared latency of silence first, so the compensated tail is not cut;
  4. the channel order (a swap is refused).
When the audio cannot give a clear reading on a channel (a steady tone, a loop, a chime: every period correlates
alike), the same graph is run on a probe (a decaying noise burst, different on each channel) and the latency is
proven there; the log then says `timing_source: probe` (timing proven on the probe, not on the audio).
A length-changing call must declare latency 0 and must read lag 0 on every channel (no compensation): the
time-stretch guards come with the ffmpeg operations (design section 10 step 4).

Known latencies (`KNOWN_LATENCY`, measured on ffmpeg 9.0.2, 2026-10-23): afftdn 1,102 samples at 44.1 kHz and
1,200 at 48 kHz. It is not round(0.025 x rate): 22,050 Hz reads 550 and 32,000 Hz reads 800, so other rates are
refused until measured.

Run: float32 WAV temp files in and out (no quantisation), `-threads 1 -filter_threads 1` (repeatable output),
`-nostdin`, metadata dropped. Finding ffmpeg: `SOUNDBENCH_FFMPEG` (overrides everything; a wrong path is an error,
never a silent fallback), then PATH, then the WinGet folder
`%LOCALAPPDATA%\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg*\\**\\bin\\ffmpeg.exe`.

Usage:
  from tools.audio.soundbench import ffmpeg
  lat = ffmpeg.known_latency("afftdn", 44100)                      # 1102
  res = ffmpeg.run_filter(x, 44100, "afftdn", latency_samples=lat)  # res.audio, res.log
"""

from __future__ import annotations

import math
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

import numpy as np

from . import measures
from .core import SoundbenchError, as_2d, check_rate

ENV_VAR = "SOUNDBENCH_FFMPEG"
WINGET_GLOB = "Gyan.FFmpeg*/**/bin/ffmpeg.exe"
TESTED_VERSION = "9.0.2"
KNOWN_LATENCY = {"afftdn": {44100: 1102, 48000: 1200}}  # samples, measured per rate (see the module docstring)
LATENCY_TOLERANCE_SAMPLES = 0
LAG_SEARCH_MIN_MS = 50.0  # the lag is searched over at least +-50 ms (and 2 x the declared latency)
PROBE_S = 0.4  # length of the probe's noise burst (the probe itself is as long as the padded input)
TIMEOUT_S = 120


@dataclass(frozen=True)
class Located:
    path: Path
    how: str  # "SOUNDBENCH_FFMPEG", "PATH" or "WinGet"


def find_ffmpeg(env: Mapping[str, str] | None = None) -> Located | None:
    """Locate ffmpeg: SOUNDBENCH_FFMPEG, then PATH, then the WinGet package folder. None when not found."""
    env = os.environ if env is None else env
    forced = env.get(ENV_VAR, "").strip()
    if forced:
        p = Path(forced)
        if not p.is_file():
            raise SoundbenchError(f"{ENV_VAR} points to a missing file: {forced}")
        return Located(p, ENV_VAR)
    on_path = shutil.which("ffmpeg", path=env.get("PATH"))
    if on_path:
        return Located(Path(on_path), "PATH")
    local = env.get("LOCALAPPDATA", "").strip()
    if local:
        found = sorted((Path(local) / "Microsoft" / "WinGet" / "Packages").glob(WINGET_GLOB))
        if found:
            return Located(found[-1], "WinGet")
    return None


_cached: Located | None = None


def require_ffmpeg() -> Located:
    """The ffmpeg this process uses (found once), or SoundbenchError."""
    global _cached
    if _cached is None:
        found = find_ffmpeg()
        if found is None:
            raise SoundbenchError(f"ffmpeg not found (set {ENV_VAR}, add it to PATH, or `winget install Gyan.FFmpeg`)")
        _cached = found
    return _cached


def _run(args: list[str]) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=TIMEOUT_S, encoding="utf-8",
                              errors="replace")
    except (OSError, subprocess.TimeoutExpired) as err:
        raise SoundbenchError(f"ffmpeg could not run: {err}") from err


def version(exe: Path) -> str:
    """The version token of `ffmpeg -version` ("9.0.2-full_build-www.gyan.dev" -> "9.0.2")."""
    out = _run([str(exe), "-hide_banner", "-version"]).stdout
    m = re.match(r"ffmpeg version (\S+)", out)
    if not m:
        raise SoundbenchError("cannot read the ffmpeg version")
    full = m.group(1)
    num = re.match(r"n?(\d+(?:\.\d+)*)", full)
    return num.group(1) if num else full


def _names(exe: Path, flag: str) -> set[str]:
    """Names from `ffmpeg -filters`, `-decoders` or `-encoders` (second column of each listing line)."""
    out = _run([str(exe), "-hide_banner", flag]).stdout
    names = set()
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 3 and parts[0] != "=" and not line.startswith(" ="):
            names.add(parts[1])
    return names


def filters(exe: Path) -> set[str]:
    return _names(exe, "-filters")


def decoders(exe: Path) -> set[str]:
    return _names(exe, "-decoders")


def encoders(exe: Path) -> set[str]:
    return _names(exe, "-encoders")


def known_latency(filter_name: str, rate: int) -> int:
    """The measured latency of a filter at a rate, in samples; SoundbenchError when it was never measured."""
    table = KNOWN_LATENCY.get(filter_name)
    if table is None or rate not in table:
        raise SoundbenchError(f"latency of {filter_name!r} at {rate} Hz was never measured: measure it before use")
    return table[rate]


@dataclass
class FilterResult:
    audio: np.ndarray  # same shape convention as the input: (n,) or (n, channels), float32
    rate: int
    lag_samples: int  # the latency measured on every channel (equal to the declared one) before compensation
    log: dict = field(default_factory=dict)


def _ffmpeg_once(feed: np.ndarray, rate: int, graph: str, exe: Path, length_change: bool) -> np.ndarray:
    """Run the graph once; check rate, channels, NaN and (unless declared) length."""
    import soundfile as sf

    with tempfile.TemporaryDirectory(prefix="soundbench_") as d:
        inp, outp = Path(d) / "in.wav", Path(d) / "out.wav"
        sf.write(str(inp), feed, rate, subtype="FLOAT")
        args = [str(exe), "-hide_banner", "-nostdin", "-loglevel", "error", "-filter_threads", "1",
                "-threads", "1", "-i", str(inp), "-af", graph, "-threads", "1", "-map_metadata", "-1",
                "-c:a", "pcm_f32le", "-f", "wav", str(outp)]
        proc = _run(args)
        if proc.returncode != 0 or not outp.is_file():
            raise SoundbenchError(f"ffmpeg failed on {graph!r} (exit {proc.returncode}): {proc.stderr.strip()[-400:]}")
        raw, out_rate = sf.read(str(outp), always_2d=True, dtype="float32")
    if out_rate != rate:
        raise SoundbenchError(f"{graph!r} changed the sample rate {rate} -> {out_rate}")
    if raw.shape[1] != feed.shape[1]:
        raise SoundbenchError(f"{graph!r} changed the channels {feed.shape[1]} -> {raw.shape[1]}")
    if not np.all(np.isfinite(raw)):
        raise SoundbenchError(f"{graph!r} produced NaN or infinite samples")
    if not length_change and len(raw) != len(feed):
        raise SoundbenchError(f"{graph!r} changed the length {len(feed)} -> {len(raw)} samples without declaring it")
    if len(raw) < 2:
        raise SoundbenchError(f"{graph!r} returned fewer than 2 samples")
    return raw


def channel_lags(ref: np.ndarray, out: np.ndarray, rate: int, search: int) -> list[dict | None]:
    """The lag of each output channel against its own input channel (None for a silent input channel)."""
    k = min(len(ref), len(out))
    return [None if not np.any(ref[:, c]) else measures.lag(ref[:k, c], out[:k, c], rate, search)
            for c in range(ref.shape[1])]


def probe_signal(rate: int, channels: int, length: int) -> np.ndarray:
    """The probe, as long as the padded input (graphs may name sample counts): a decaying noise burst per channel
    (a different seed on each), starting 20 ms in (or at once for short inputs), then silence. Broadband, never
    periodic."""
    out = np.zeros((length, channels), np.float32)
    start = min(int(0.02 * rate), length // 4)
    k = min(int(PROBE_S * rate), length - start)
    t = np.arange(k) / rate
    for c in range(channels):
        burst = np.random.RandomState(100 + c).standard_normal(k) * np.exp(-t * 20) * 0.3
        out[start:start + k, c] = burst.astype(np.float32)
    return out


def run_filter(x: np.ndarray, rate: int, graph: str, *, latency_samples: int = 0, length_change: bool = False,
               compensate: bool = True, exe: Path | None = None) -> FilterResult:
    """Run one ffmpeg audio filter graph on `x` and return audio that keeps rate, channels, length and timing.

    `latency_samples`: the graph's known latency (`known_latency`); every channel must read exactly this lag, and
    the output is shifted back by it. 0 (default): any lag is an unknown latency and is refused.
    `length_change`: the graph changes the length on purpose (no length check; latency must be 0).
    `compensate`: False refuses a graph with a latency instead of compensating it (proves the check fires)."""
    one_d = isinstance(x, np.ndarray) and x.ndim == 1
    src = as_2d(x, "filter input").astype(np.float32)
    rate = check_rate(rate)
    if not isinstance(graph, str) or not graph.strip() or "\n" in graph:
        raise SoundbenchError("filter graph must be one non-empty line")
    if isinstance(latency_samples, bool) or not isinstance(latency_samples, (int, np.integer)) or latency_samples < 0:
        raise SoundbenchError(f"latency_samples must be a whole number of samples, 0 or more, got {latency_samples!r}")
    latency = int(latency_samples)
    if length_change and latency:
        raise SoundbenchError("a length-changing call cannot declare a latency (no compensation for it)")
    n, ch = src.shape
    feed = np.vstack([src, np.zeros((latency, ch), np.float32)]) if latency else src
    exe = Path(exe) if exe is not None else require_ffmpeg().path
    raw = _ffmpeg_once(feed, rate, graph, exe, length_change)
    log = {"graph": graph, "ffmpeg": str(exe), "rate": rate, "channels": ch, "samples_in": n,
           "declared_latency_samples": latency, "latency_tolerance_samples": LATENCY_TOLERANCE_SAMPLES,
           "samples_out_raw": int(len(raw)), "length_change": length_change}

    if not np.any(src):  # no timing to measure: the output must stay silent
        if np.any(raw):
            raise SoundbenchError(f"{graph!r} made sound from a silent input")
        log.update({"timing_source": "silent input and output", "lag_samples": 0})
        out = raw if length_change else raw[latency:latency + n]
        return FilterResult(out[:, 0] if one_d else out, rate, 0, log)

    search = int(math.ceil(max(2 * latency, LAG_SEARCH_MIN_MS * rate / 1000)))
    readings = channel_lags(feed, raw, rate, search)
    source = "audio"
    if not all(r is None or r["clear"] for r in readings):
        probe = probe_signal(rate, ch, len(feed))
        praw = _ffmpeg_once(probe, rate, graph, exe, length_change)
        readings = channel_lags(probe, praw, rate, search)
        source = "probe"
        if not all(r is not None and r["clear"] for r in readings):
            raise SoundbenchError(f"{graph!r}: timing cannot be proven, neither on the audio nor on a probe signal "
                                  f"(per channel: {[None if r is None else r['second_peak_ratio'] for r in readings]})")
    lags = [r["lag_samples"] for r in readings if r is not None]
    log.update({"timing_source": source if source == "audio" else
                "probe (the audio gave no clear reading: timing proven on a probe signal through the same graph, "
                "not on the audio)",
                "channel_lags_samples": lags,
                "channel_correlation": [None if r is None else r["correlation"] for r in readings],
                "channel_second_peak_ratio": [None if r is None else r["second_peak_ratio"] for r in readings]})
    if len(set(lags)) != 1:
        raise SoundbenchError(f"{graph!r}: channels disagree on timing ({lags} samples, read on the {source}): refused")
    found = lags[0]
    if abs(found - latency) > LATENCY_TOLERANCE_SAMPLES:
        raise SoundbenchError(f"{graph!r} delayed the sound by {found} samples ({1000 * found / rate:.3f} ms), but "
                              f"{latency} were declared: unknown latency, refused")
    if found and not compensate:
        raise SoundbenchError(f"{graph!r} delays the sound by {found} samples ({1000 * found / rate:.3f} ms): "
                              "compensation is off, refused")
    out = raw if length_change else raw[latency:latency + n]
    if not length_change and len(out) != n:
        raise SoundbenchError(f"{graph!r}: compensated output is {len(out)} samples, expected {n}")
    k = min(n, len(out))
    log["channel_check"] = check_channels(src[:k], out[:k], graph)
    log.update({"lag_samples": found, "compensated": bool(latency)})
    return FilterResult(out[:, 0] if one_d else out, rate, found, log)


CHANNEL_LEVEL_DB = 1.0  # input channels this far apart in level must keep their order


def check_channels(src: np.ndarray, out: np.ndarray, graph: str) -> str:
    """Refuse a swapped or mixed-up channel order.

    Each output channel must correlate at least as well with its own input channel as with any other (within 0.02),
    and input channels more than 1 dB apart in level must keep their louder-quieter order."""
    ch = src.shape[1]
    if ch == 1:
        return "mono"
    s, o = src.astype(np.float64), out.astype(np.float64)
    es, eo = np.sum(s ** 2, axis=0), np.sum(o ** 2, axis=0)
    for c in range(ch):
        if eo[c] <= 0 or es[c] <= 0:
            continue
        own = float(np.dot(o[:, c], s[:, c]) / math.sqrt(eo[c] * es[c]))
        for k in range(ch):
            if k != c and es[k] > 0:
                cross = float(np.dot(o[:, c], s[:, k]) / math.sqrt(eo[c] * es[k]))
                if cross > own + 0.02:
                    raise SoundbenchError(f"{graph!r}: output channel {c} matches input channel {k} better than its "
                                          f"own ({cross:.3f} vs {own:.3f}): channel order changed, refused")
    for a in range(ch):
        for b in range(a + 1, ch):
            if es[a] > 0 and es[b] > 0 and abs(10 * math.log10(es[a] / es[b])) > CHANNEL_LEVEL_DB:
                if (es[a] > es[b]) != (eo[a] > eo[b]):
                    raise SoundbenchError(f"{graph!r}: channels {a} and {b} swapped their level order: refused")
    return "order kept"
