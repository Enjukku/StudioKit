"""Stand-ins: non-periodic test sounds of a cue's own kind, run through the same ffmpeg graph as the cue to prove
its timing when the cue itself cannot be timed (a chime, a loop: every period correlates alike).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 4)

A probe signal proves the graph's latency on broadband noise; a stand-in proves it on material shaped like the cue
(a hit's crack, a riser's swell, a bed's slow movement), because a filter can treat a swell differently from a click.
All are seeded noise (never periodic), different on each channel, the right channel quieter (a swap changes the
level order). The kind's stand-in class is in `tables.json` (`standin`).

Usage:
  from tools.audio.soundbench import standins
  s = standins.make("hit", 44100, 2, 22050)
"""

from __future__ import annotations

import numpy as np

from .core import SoundbenchError

CLASSES = ("hit", "click", "riser", "bed")


def _shape(cls: str, rate: int, n: int) -> np.ndarray:
    t = np.arange(n) / rate
    start = min(int(0.02 * rate), n // 4)
    env = np.zeros(n)
    if cls == "hit":
        env[start:] = np.exp(-(t[: n - start]) * 25)
    elif cls == "click":
        k = min(n - start, int(0.004 * rate))
        env[start:start + k] = np.exp(-np.arange(k) / (0.001 * rate))
    elif cls == "riser":
        rise = max(1, int(0.6 * (n - start)))
        env[start:start + rise] = np.geomspace(0.01, 1.0, rise)
        tail = n - start - rise
        env[start + rise:] = np.exp(-np.arange(tail) / (0.02 * rate))
    elif cls == "bed":
        env[:] = 0.6 + 0.4 * np.sin(2 * np.pi * 1.3 * t) * np.sin(2 * np.pi * 0.37 * t + 1.0)
    else:
        raise SoundbenchError(f"unknown stand-in class {cls!r} (known: {CLASSES})")
    return env


def make(cls: str, rate: int, channels: int, n: int) -> np.ndarray:
    """A stand-in of class `cls`: float32 (n, channels)."""
    if cls in CLASSES:
        key = cls
    else:  # a kind name: its class from the kinds table
        from .card import KINDS

        if cls not in KINDS:
            raise SoundbenchError(f"unknown stand-in kind {cls!r}")
        key = KINDS[cls]["standin"]
    env = _shape(key, rate, n)
    out = np.zeros((n, channels), np.float32)
    for c in range(channels):
        noise = np.random.RandomState(300 + CLASSES.index(key) * 10 + c).standard_normal(n)
        out[:, c] = (noise * env * (0.25 if c == 0 else 0.17)).astype(np.float32)
    return out
