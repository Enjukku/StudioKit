"""Shared basics of soundbench: the error type, audio shape checks, the audio hash and the tool versions.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

Audio inside soundbench is a numpy array shaped (samples, channels). The audio hash (design G-1) is the sha256 of the
samples as little-endian float32, interleaved, C order: two runs that give the same hash gave the same audio before
encoding, whatever the file container does with its own bytes.

Usage:
  from tools.audio.soundbench.core import SoundbenchError, as_2d, audio_sha256, versions
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import platform
from pathlib import Path

import numpy as np

VERSION = "0.1.0"  # step 1-2 of editor-design.md section 10


class SoundbenchError(Exception):
    """A refused or failed step. Raised instead of returning a plausible wrong result."""


def as_2d(x: np.ndarray, what: str = "audio") -> np.ndarray:
    """Check a buffer (finite, 1 or 2 dims, at least 2 samples) and return it as (samples, channels)."""
    if not isinstance(x, np.ndarray) or x.dtype.kind != "f":
        raise SoundbenchError(f"{what}: needs a float numpy array, got {type(x).__name__}"
                              f"{'' if not isinstance(x, np.ndarray) else ' of ' + str(x.dtype)}")
    if x.ndim == 1:
        x = x[:, None]
    if x.ndim != 2 or x.shape[1] < 1:
        raise SoundbenchError(f"{what}: needs shape (samples,) or (samples, channels), got {x.shape}")
    if x.shape[0] < 2:
        raise SoundbenchError(f"{what}: fewer than 2 samples")
    if not np.all(np.isfinite(x)):
        raise SoundbenchError(f"{what}: contains NaN or infinite samples")
    return x


def check_rate(rate: object) -> int:
    if isinstance(rate, bool) or not isinstance(rate, (int, np.integer)) or not 8000 <= int(rate) <= 192000:
        raise SoundbenchError(f"sample rate must be a whole number from 8000 to 192000 Hz, got {rate!r}")
    return int(rate)


def audio_sha256(x: np.ndarray) -> str:
    """sha256 of the audio as little-endian float32, interleaved (design G-1)."""
    return hashlib.sha256(np.ascontiguousarray(as_2d(np.asarray(x)), dtype="<f4").tobytes()).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def read_float32(path: Path) -> tuple[np.ndarray, int]:
    """A file as float32 (samples, channels), unchanged (no DC removal: that is a measuring step, not an edit)."""
    import soundfile as sf

    if not Path(path).is_file():
        raise SoundbenchError(f"not a file: {path}")
    x, rate = sf.read(str(path), always_2d=True, dtype="float32")
    return as_2d(x, str(path)), int(rate)


def versions() -> dict:
    """The tool versions an output depends on (written into every log)."""
    import soundfile as sf

    out = {"soundbench": VERSION, "python": platform.python_version(), "numpy": np.__version__,
           "soundfile": sf.__version__, "libsndfile": sf.__libsndfile_version__}
    for pkg in ("scipy", "pyloudnorm", "matplotlib"):
        try:
            out[pkg] = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            out[pkg] = None
    return out
