"""Pictures: one PNG with the waveform (every channel) over the spectrogram (mono sum), for an agent to look at.

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 step 1-2)

matplotlib with the Agg canvas (no window, no pyplot state). Light-check rule (owner J005-D8): numbers for every take;
a picture when a number fails or is near its limit, and for important cues. The picture reads the audio only.

Usage:
  from tools.audio.soundbench import pictures
  pictures.picture(x, 44100, Path("report/hit.png"), title="hit.r1.t1")
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .core import as_2d, check_rate

WIDTH_IN, HEIGHT_IN, DPI = 10.0, 6.0, 100


def picture(x: np.ndarray, rate: int, out: Path, title: str = "") -> Path:
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    from scipy.signal import spectrogram

    audio = as_2d(np.asarray(x), "picture input")
    rate = check_rate(rate)
    t = np.arange(len(audio)) / rate * 1000
    fig = Figure(figsize=(WIDTH_IN, HEIGHT_IN), dpi=DPI)
    FigureCanvasAgg(fig)
    wave, spec = fig.subplots(2, 1, sharex=True, gridspec_kw={"height_ratios": [1, 1.4]})
    for c in range(audio.shape[1]):
        wave.plot(t, audio[:, c], linewidth=0.6, label=f"ch {c}")
    wave.set_ylim(-1.05, 1.05)
    wave.set_ylabel("amplitude")
    wave.grid(True, alpha=0.3)
    if audio.shape[1] > 1:
        wave.legend(loc="upper right", fontsize=8)
    wave.set_title(title or "waveform and spectrogram")
    nper = min(1024, len(audio))
    f, tt, s = spectrogram(audio.mean(axis=1).astype(np.float64), fs=rate, nperseg=nper, noverlap=nper * 3 // 4)
    level = 10 * np.log10(np.maximum(s, 1e-12))
    top = float(level.max())
    spec.pcolormesh(tt * 1000, f, level, vmin=top - 90, vmax=top, shading="auto", cmap="magma")
    spec.set_yscale("symlog", linthresh=200)
    spec.set_ylim(20, rate / 2)
    spec.set_ylabel("Hz")
    spec.set_xlabel("ms")
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(str(out))
    return out
