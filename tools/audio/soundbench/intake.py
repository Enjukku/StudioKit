"""Intake (design section 8): decode an MP3 take once into its float32 master WAV and record how.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Every later step reads the master, never the MP3 (design section 2). The decode:
  - runs ffmpeg with no resampling and no channel change, to a float32 WAV (`pcm_f32le`);
  - checks that the master's rate and channels equal the MP3 stream's (as ffmpeg reports the stream);
  - checks the decoded length against the duration that was asked for: an MP3 without its encoder-delay tag
    decodes about 25 ms late and about 27 ms long (probe 2026-10-23, ffmpeg 9.0.2, libmp3lame 192k at 44.1 kHz),
    so a difference over `tolerance_ms` (default 10 ms, PROPOSAL) is refused and the master is removed;
  - never overwrites an existing master (originals never change, design G-1);
  - writes, into the take's sidecar JSON under "intake": the take's file sha256, the master's audio sha256 (float32),
    the decoder name and ffmpeg version, rate, channels, samples, decoded and expected length.

Usage:
  from tools.audio.soundbench import intake
  info = intake.decode_take(Path("takes/hit.r1.t1.mp3"), expected_ms=500)
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

from . import ffmpeg
from .core import SoundbenchError, audio_sha256, file_sha256, read_float32

TOLERANCE_MS = 10.0  # PROPOSAL until real ElevenLabs takes are measured (open question in the hand-back)
STREAM_RE = re.compile(r"Stream #0:\d+.*?: Audio: (\w+)(?: \((\w+)\))?.*?, (\d+) Hz, ([\w.()]+)")
LAYOUT_CHANNELS = {"mono": 1, "stereo": 2}


def master_path(take: Path) -> Path:
    """takes/<cue>.r<k>.t<n>.mp3 -> takes/<cue>.r<k>.t<n>.master.wav"""
    return take.with_name(take.stem + ".master.wav")


def decode_take(take: Path, expected_ms: float, *, master: Path | None = None, sidecar: Path | None = None,
                tolerance_ms: float = TOLERANCE_MS, exe: Path | None = None) -> dict:
    take = Path(take)
    if not take.is_file():
        raise SoundbenchError(f"not a file: {take}")
    if not math.isfinite(expected_ms) or expected_ms <= 0:
        raise SoundbenchError(f"expected_ms must be a positive number, got {expected_ms}")
    master = master_path(take) if master is None else Path(master)
    sidecar = take.with_suffix(".json") if sidecar is None else Path(sidecar)
    if master.exists():
        raise SoundbenchError(f"master already exists, never overwritten: {master}")
    located = ffmpeg.require_ffmpeg() if exe is None else ffmpeg.Located(Path(exe), "argument")
    proc = ffmpeg._run([str(located.path), "-hide_banner", "-nostdin", "-threads", "1", "-i", str(take),
                        "-map", "0:a:0", "-map_metadata", "-1", "-c:a", "pcm_f32le", "-f", "wav", str(master)])
    try:
        if proc.returncode != 0 or not master.is_file():
            raise SoundbenchError(f"decode failed (exit {proc.returncode}): {proc.stderr.strip()[-400:]}")
        m = STREAM_RE.search(proc.stderr)
        if not m:
            raise SoundbenchError("cannot read the take's audio stream from ffmpeg's report")
        codec, decoder, stream_rate, layout = m.group(1), m.group(2) or m.group(1), int(m.group(3)), m.group(4)
        x, rate = read_float32(master)
        if rate != stream_rate:
            raise SoundbenchError(f"decoded rate {rate} differs from the stream's {stream_rate}: refused")
        want_ch = LAYOUT_CHANNELS.get(layout.split("(")[0])
        if want_ch is not None and x.shape[1] != want_ch:
            raise SoundbenchError(f"decoded {x.shape[1]} channels from a {layout} stream: refused")
        decoded_ms = 1000 * len(x) / rate
        delta = decoded_ms - expected_ms
        if abs(delta) > tolerance_ms:
            raise SoundbenchError(f"decoded length {decoded_ms:.1f} ms differs from the expected {expected_ms:.1f} ms "
                                  f"by {delta:+.1f} ms (limit {tolerance_ms} ms): a missing encoder-delay tag or a "
                                  "wrong duration; refused")
    except SoundbenchError:
        master.unlink(missing_ok=True)
        raise
    info = {"take": take.name, "take_sha256": file_sha256(take), "master": master.name,
            "master_audio_sha256": audio_sha256(x), "codec": codec, "decoder": f"ffmpeg {decoder}",
            "ffmpeg_version": ffmpeg.version(located.path), "rate": rate, "channels": int(x.shape[1]),
            "samples": int(len(x)), "decoded_ms": round(decoded_ms, 3), "expected_ms": expected_ms,
            "delta_ms": round(delta, 3), "tolerance_ms": tolerance_ms}
    doc = json.loads(sidecar.read_text(encoding="utf-8")) if sidecar.is_file() else {}
    doc["intake"] = info
    sidecar.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    return info
