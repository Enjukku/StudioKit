"""The ffmpeg adapter (design G-7): run one filter graph on a buffer and prove that time, rate and channels are kept.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Why it exists: review-1 measured that `afftdn` delays audio by exactly 1,102 samples (25.0 ms at 44.1 kHz; 1,200 at
48 kHz) and cuts the tail by the same amount, with no error and the same file length. So after every call this
adapter checks, and refuses with `SoundbenchError` instead of returning shifted or damaged audio:
  1. same sample rate and same channel count as the input;
  2. same length (padded input length), unless the call declares a length change;
  3. no NaN or infinite samples;
  4. lag 0 by cross-correlation with the input (`measures.lag`). A measured lag is compensated only when the
     correlation is clear and the lag is within the maximum the call declares (`max_lag_ms`; default 0 = any lag
     is refused). The input is padded at the end with `max_lag_ms` of silence first, so a compensated tail is not
     cut. After compensation the lag is measured again and must be 0.
A length-changing call is checked for rate and channels and must still read lag 0 on its shared start (no
compensation): the time-stretch guards come with the ffmpeg operations (design section 10 step 4).

Run: float32 WAV temp files in and out (no quantisation), `-threads 1 -filter_threads 1` (repeatable output),
`-nostdin`, metadata dropped. Finding ffmpeg: `SOUNDBENCH_FFMPEG` (overrides everything; a wrong path is an error,
never a silent fallback), then PATH, then the WinGet folder
`%LOCALAPPDATA%\\Microsoft\\WinGet\\Packages\\Gyan.FFmpeg*\\**\\bin\\ffmpeg.exe`.

Usage:
  from tools.audio.soundbench import ffmpeg
  res = ffmpeg.run_filter(x, 44100, "afftdn", max_lag_ms=50)   # res.audio, res.log
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
LAG_SEARCH_MIN_MS = 50.0  # the lag is searched over at least +-50 ms, so a lag past the declared maximum is seen
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


@dataclass
class FilterResult:
    audio: np.ndarray  # same shape convention as the input: (n,) or (n, channels), float32
    rate: int
    lag_samples: int  # measured lag before compensation (0 when none)
    log: dict = field(default_factory=dict)


def run_filter(x: np.ndarray, rate: int, graph: str, *, max_lag_ms: float = 0.0, length_change: bool = False,
               compensate: bool = True, exe: Path | None = None) -> FilterResult:
    """Run one ffmpeg audio filter graph on `x` and return audio that keeps rate, channels, length and timing.

    `max_lag_ms`: the largest latency this call may compensate (0: any lag is an unknown latency and is refused).
    `length_change`: the graph changes the length on purpose (no length check, no compensation).
    `compensate`: False refuses any measured lag instead of compensating it (used to prove the check fires)."""
    one_d = isinstance(x, np.ndarray) and x.ndim == 1
    src = as_2d(x, "filter input").astype(np.float32)
    rate = check_rate(rate)
    if not isinstance(graph, str) or not graph.strip() or "\n" in graph:
        raise SoundbenchError("filter graph must be one non-empty line")
    if not math.isfinite(max_lag_ms) or max_lag_ms < 0:
        raise SoundbenchError(f"max_lag_ms must be 0 or more, got {max_lag_ms}")
    n, ch = src.shape
    pad = 0 if length_change else int(math.ceil(max_lag_ms * rate / 1000))
    feed = np.vstack([src, np.zeros((pad, ch), np.float32)]) if pad else src
    exe = Path(exe) if exe is not None else require_ffmpeg().path
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
        info = sf.info(str(outp))
        raw, out_rate = sf.read(str(outp), always_2d=True, dtype="float32")

    log = {"graph": graph, "ffmpeg": str(exe), "rate": rate, "channels": ch, "samples_in": n, "pad_samples": pad,
           "samples_out_raw": int(len(raw)), "output_subtype": info.subtype, "max_lag_ms": max_lag_ms,
           "length_change": length_change}
    if out_rate != rate:
        raise SoundbenchError(f"{graph!r} changed the sample rate {rate} -> {out_rate}")
    if raw.shape[1] != ch:
        raise SoundbenchError(f"{graph!r} changed the channels {ch} -> {raw.shape[1]}")
    if not np.all(np.isfinite(raw)):
        raise SoundbenchError(f"{graph!r} produced NaN or infinite samples")
    if not length_change and len(raw) != len(feed):
        raise SoundbenchError(f"{graph!r} changed the length {len(feed)} -> {len(raw)} samples without declaring it")
    if len(raw) < 2:
        raise SoundbenchError(f"{graph!r} returned fewer than 2 samples")

    search = int(math.ceil(max(max_lag_ms, LAG_SEARCH_MIN_MS) * rate / 1000))
    src_silent = float(np.max(np.abs(src))) == 0.0
    if src_silent:  # no timing to measure: the output must stay silent
        if float(np.max(np.abs(raw))) > 0.0:
            raise SoundbenchError(f"{graph!r} made sound from a silent input")
        log.update({"lag_samples": 0, "lag_check": "silent input and output"})
        out = raw[:n] if not length_change else raw
        return FilterResult(out[:, 0] if one_d else out, rate, 0, log)

    m = measures.lag(feed, raw, rate, search)
    log.update({"lag_measured_samples": m["lag_samples"], "lag_measured_ms": m["lag_ms"],
                "correlation": m["correlation"], "second_peak_ratio": m["second_peak_ratio"]})
    if not m["clear"]:
        raise SoundbenchError(f"{graph!r}: timing cannot be proven (correlation {m['correlation']}, second peak "
                              f"{m['second_peak_ratio']} of the best): refused")
    found = int(m["lag_samples"])
    if length_change:
        if found != 0:
            raise SoundbenchError(f"{graph!r} (length change) moved the sound by {found} samples: refused")
        k = min(n, len(raw))
        log["channel_check"] = check_channels(src[:k], raw[:k], graph)
        log["lag_samples"] = 0
        return FilterResult(raw[:, 0] if one_d else raw, rate, 0, log)
    if found != 0:
        if not compensate:
            raise SoundbenchError(f"{graph!r} delayed the sound by {found} samples ({m['lag_ms']} ms): "
                                  "compensation is off, refused")
        if found < 0:
            raise SoundbenchError(f"{graph!r} moved the sound {-found} samples early: refused")
        if found > pad:
            raise SoundbenchError(f"{graph!r} delayed the sound by {found} samples ({m['lag_ms']} ms), more than the "
                                  f"declared maximum of {max_lag_ms} ms: unknown latency, refused")
    out = raw[found:found + n]
    if len(out) != n:
        raise SoundbenchError(f"{graph!r}: compensated output is {len(out)} samples, expected {n}")
    check = measures.lag(src, out, rate, search)
    if not check["clear"] or check["lag_samples"] != 0:
        raise SoundbenchError(f"{graph!r}: lag after compensation is {check['lag_samples']} samples: refused")
    log["channel_check"] = check_channels(src, out, graph)
    log.update({"lag_samples": found, "compensated": found != 0, "lag_after_samples": 0})
    return FilterResult(out[:, 0] if one_d else out, rate, found, log)


CHANNEL_LEVEL_DB = 1.0  # input channels this far apart in level must keep their order


def check_channels(src: np.ndarray, out: np.ndarray, graph: str) -> str:
    """Refuse a swapped or mixed-up channel order (the mono-sum lag check cannot see it).

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
