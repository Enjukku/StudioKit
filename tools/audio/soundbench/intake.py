"""Intake (design section 8): decode an MP3 take once into its float32 master WAV and record how.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2; LD-b revision
2026-10-23: the decode is checked against the file's own stated duration, not the requested one)

Every later step reads the master, never the MP3 (design section 2). The decode:
  - reads what the file states about itself with ffprobe (next to ffmpeg): codec, rate, channels, duration and the
    stream's start time, which carries the encoder delay;
  - refuses a stream that states no encoder delay (start time 0): such an MP3 decodes about 25 ms late and states a
    duration as long as its wrong decode (probe 7, 2026-10-23: 480 ms of audio stated and decoded as 522 ms), so no
    length check can catch it. Every real ElevenLabs take states 0.025057 s at 44.1 kHz;
  - runs ffmpeg with no resampling and no channel change, to a float32 WAV (`pcm_f32le`);
  - checks the master's rate and channels against the stream, and its length against the stated duration within
    `tolerance_ms` (10 ms, PROPOSAL); a miss removes the master and refuses;
  - logs the requested duration beside the one received, with a warning when they differ by more than 10 ms: the
    service decides the length (every real 0.5 s request came back 480 ms), so that is never a refusal (LD-b);
  - never overwrites an existing master (originals never change, design G-1);
  - writes, into the take's sidecar JSON under "intake": the take's file sha256, the master's audio sha256 (float32),
    the decoder name and ffmpeg version, rate, channels, samples, decoded, stated and requested length.

Usage:
  from tools.audio.soundbench import intake
  info = intake.decode_take(Path("takes/hit.r1.t1.mp3"), requested_ms=500)
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

from . import ffmpeg
from .core import SoundbenchError, audio_sha256, file_sha256, read_float32

TOLERANCE_MS = 10.0  # PROPOSAL: decoded vs stated length; also the requested-length warning threshold
DECODER_RE = re.compile(r"Stream #0:\d+.*?: Audio: (\w+)(?: \((\w+)\))?")


def master_path(take: Path) -> Path:
    """takes/<cue>.r<k>.t<n>.mp3 -> takes/<cue>.r<k>.t<n>.master.wav"""
    return take.with_name(take.stem + ".master.wav")


def ffprobe_path(exe: Path) -> Path:
    p = exe.with_name("ffprobe.exe" if exe.suffix.lower() == ".exe" else "ffprobe")
    if not p.is_file():
        raise SoundbenchError(f"ffprobe not found next to ffmpeg ({p}): intake reads the file's stated duration with it")
    return p


def stream_info(take: Path, exe: Path) -> dict:
    """The first audio stream as the file states it (ffprobe JSON)."""
    proc = ffmpeg._run([str(ffprobe_path(exe)), "-v", "error", "-select_streams", "a:0", "-show_entries",
                        "stream=codec_name,sample_rate,channels,start_time,duration", "-of", "json", str(take)])
    try:
        st = json.loads(proc.stdout)["streams"][0]
        # ffprobe 9.0.2 states no start_time for a PCM WAV (ElevenLabs wav_44100, 2026-10-24): PCM has no encoder
        # delay, so its start is 0. An MP3 must still state one (the encoder-delay rule below).
        start = 0.0 if "start_time" not in st and str(st.get("codec_name", "")).startswith("pcm_") else st["start_time"]
        return {"codec": st["codec_name"], "rate": int(st["sample_rate"]), "channels": int(st["channels"]),
                "start_s": float(start), "duration_ms": 1000 * float(st["duration"])}
    except (json.JSONDecodeError, KeyError, IndexError, TypeError, ValueError) as err:
        raise SoundbenchError(f"cannot read the take's audio stream with ffprobe: {proc.stderr.strip()[-200:]}") from err


def decode_take(take: Path, requested_ms: float | None = None, *, master: Path | None = None,
                sidecar: Path | None = None, tolerance_ms: float = TOLERANCE_MS, exe: Path | None = None) -> dict:
    take = Path(take)
    if not take.is_file():
        raise SoundbenchError(f"not a file: {take}")
    if requested_ms is not None and (not math.isfinite(requested_ms) or requested_ms <= 0):
        raise SoundbenchError(f"requested_ms must be a positive number, got {requested_ms}")
    master = master_path(take) if master is None else Path(master)
    sidecar = take.with_suffix(".json") if sidecar is None else Path(sidecar)
    if master.exists():
        raise SoundbenchError(f"master already exists, never overwritten: {master}")
    located = ffmpeg.require_ffmpeg() if exe is None else ffmpeg.Located(Path(exe), "argument")
    st = stream_info(take, located.path)
    if st["codec"] == "mp3" and st["start_s"] <= 0:
        raise SoundbenchError(f"{take.name} states no encoder delay (stream start 0): an MP3 without its encoder-delay "
                              "tag decodes about 25 ms late and states its wrong length; refused")
    proc = ffmpeg._run([str(located.path), "-hide_banner", "-nostdin", "-threads", "1", "-i", str(take),
                        "-map", "0:a:0", "-map_metadata", "-1", "-c:a", "pcm_f32le", "-f", "wav", str(master)])
    try:
        if proc.returncode != 0 or not master.is_file():
            raise SoundbenchError(f"decode failed (exit {proc.returncode}): {proc.stderr.strip()[-400:]}")
        x, rate = read_float32(master)
        if rate != st["rate"]:
            raise SoundbenchError(f"decoded rate {rate} differs from the stream's {st['rate']}: refused")
        if x.shape[1] != st["channels"]:
            raise SoundbenchError(f"decoded {x.shape[1]} channels from a {st['channels']}-channel stream: refused")
        decoded_ms = 1000 * len(x) / rate
        delta = decoded_ms - st["duration_ms"]
        if abs(delta) > tolerance_ms:
            raise SoundbenchError(f"decoded length {decoded_ms:.1f} ms differs from the stated {st['duration_ms']:.1f} ms "
                                  f"by {delta:+.1f} ms (limit {tolerance_ms} ms): refused")
    except SoundbenchError:
        master.unlink(missing_ok=True)
        raise
    found = DECODER_RE.search(proc.stderr)
    decoder = (found.group(2) or found.group(1)) if found else st["codec"]
    info = {"take": take.name, "take_sha256": file_sha256(take), "master": master.name,
            "master_audio_sha256": audio_sha256(x), "codec": st["codec"], "decoder": f"ffmpeg {decoder}",
            "ffmpeg_version": ffmpeg.version(located.path), "rate": rate, "channels": int(x.shape[1]),
            "samples": int(len(x)), "decoded_ms": round(decoded_ms, 3), "stated_ms": round(st["duration_ms"], 3),
            "encoder_delay_s": st["start_s"], "requested_ms": requested_ms, "tolerance_ms": tolerance_ms,
            "warnings": []}
    if requested_ms is not None and abs(decoded_ms - requested_ms) > tolerance_ms:
        info["warnings"].append(f"the service returned {decoded_ms:.1f} ms for a {requested_ms:.1f} ms request "
                                f"({decoded_ms - requested_ms:+.1f} ms): targets and trims use the received length")
    doc = json.loads(sidecar.read_text(encoding="utf-8")) if sidecar.is_file() else {}
    doc["intake"] = info
    sidecar.write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    return info
