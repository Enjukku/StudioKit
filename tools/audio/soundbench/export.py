"""Export (design G-1, G-8): write the delivered file as FLAC at the input's sample rate, with a log that proves it.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Rules:
  - FLAC, 24-bit integer (`soundfile`, libsndfile); Roblox accepts .flac under 20 MB and 7 minutes, up to 48 kHz
    (`audio/assets.md`). The file is written at the rate it is given; a `source_rate` that differs is refused, and
    so is a rate over 48 kHz: soundbench never resamples silently.
  - Refused instead of damaged: samples past full scale (a 24-bit integer file would clip them), NaN, a file over
    7 minutes, a FLAC over 20 MB (the Ogg path of G-8 is not built: the file is removed and the call fails).
  - After writing, the file is read back: same rate, channels and length, every sample within one 24-bit step.
  - The log (`<name>.log.json` next to the file unless given): the sha256 of the float32 audio before encoding
    (G-1: same recipe, same audio), the encode settings, the file's own sha256, the read-back error and the tool
    versions.

Usage:
  from tools.audio.soundbench import export
  log = export.export_flac(x, 44100, Path("out/hit.flac"), source_rate=44100)
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from .core import SoundbenchError, as_2d, audio_sha256, check_rate, file_sha256, versions

MAX_RATE = 48000  # Roblox: up to 48 kHz
MAX_BYTES = 20 * 1000 * 1000  # Roblox: under 20 MB (decimal megabytes: the safer reading)
MAX_SECONDS = 7 * 60
SUBTYPE = "PCM_24"
STEP = 2.0 ** -23  # one 24-bit step


def check_exportable(x: np.ndarray, rate: int, source_rate: int | None = None) -> tuple[np.ndarray, int, float]:
    """Every refusal export makes before it writes (rate, channels, length, full scale), as (float32 audio, rate, sample
    peak). `rank` calls this same function on each plan's result, so a plan it keeps is one `render` can export (the
    20 MB size check needs the encoded file and is left to export)."""
    audio = as_2d(np.asarray(x), "export input").astype(np.float32)
    rate = check_rate(rate)
    if source_rate is not None and check_rate(source_rate) != rate:
        raise SoundbenchError(f"export rate {rate} differs from the source rate {source_rate}: never resampled silently")
    if rate > MAX_RATE:
        raise SoundbenchError(f"{rate} Hz is over Roblox's {MAX_RATE} Hz: resample in a declared step first")
    if audio.shape[1] > 2:
        raise SoundbenchError(f"{audio.shape[1]} channels: export takes mono or stereo")
    if len(audio) / rate > MAX_SECONDS:
        raise SoundbenchError(f"{len(audio) / rate:.1f} s is over Roblox's 7 minutes")
    peak = float(np.max(np.abs(audio)))
    if peak > 1.0 - STEP:
        raise SoundbenchError(f"sample peak {peak:.6f} reaches full scale: the 24-bit file would clip; set the level first")
    return audio, rate, peak


def export_flac(x: np.ndarray, rate: int, out: Path, *, source_rate: int | None = None, log: Path | None = None) -> dict:
    out = Path(out)
    audio, rate, peak = check_exportable(x, rate, source_rate)
    import soundfile as sf

    pre_hash = audio_sha256(audio)
    out.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(out), audio, rate, format="FLAC", subtype=SUBTYPE)
    size = out.stat().st_size
    if size > MAX_BYTES:
        out.unlink()
        raise SoundbenchError(f"FLAC is {size} bytes, over 20 MB: the Ogg path (design G-8) is not built yet")
    back, back_rate = sf.read(str(out), always_2d=True, dtype="float32")
    if back_rate != rate or back.shape != audio.shape:
        out.unlink()
        raise SoundbenchError(f"read-back differs: {back_rate} Hz {back.shape} vs {rate} Hz {audio.shape}")
    err = float(np.max(np.abs(back.astype(np.float64) - audio.astype(np.float64))))
    if err > STEP:
        out.unlink()
        raise SoundbenchError(f"read-back error {err:.3g} is over one 24-bit step")
    rec = {"file": out.name, "file_sha256": file_sha256(out), "bytes": size,
           "audio_sha256_float32": pre_hash,
           "encode": {"format": "FLAC", "subtype": SUBTYPE, "rate": rate, "channels": int(audio.shape[1]),
                      "samples": int(len(audio)), "compression": "libsndfile default", "dither": "none"},
           "sample_peak": round(peak, 6), "readback_max_error": err, "tools": versions()}
    log = out.with_name(out.name.rsplit(".", 1)[0] + ".log.json") if log is None else Path(log)
    log.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    return rec
