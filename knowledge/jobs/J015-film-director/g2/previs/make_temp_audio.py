# TEMP sounds for the animatic, one file per cue id, timed from the shot list (never final audio).
# Author: film-director · claude-opus-5-5 · high · 2026-10-21
# python make_temp_audio.py <shots.json> <out_dir>   -> TEMP_<cue>.wav + cues_temp.json (start frame per file)
import json
import sys
import wave
from pathlib import Path

import numpy as np

shots_path, out = sys.argv[1], Path(sys.argv[2])
out.mkdir(parents=True, exist_ok=True)
d = json.load(open(shots_path, encoding="utf-8"))
num, den = d["fps"]
fps = num / den
start = {}
f = d.get("start_frame", 1)
for s in d["shots"]:
    start[s["id"]] = f
    f += s["frames"]
END = f  # first frame after the sequence
SR = 48000
rng = np.random.default_rng(15)


def env(n, a, r):
    e = np.ones(n)
    a, r = int(a * SR), int(r * SR)
    if a:
        e[:a] = np.linspace(0, 1, a)
    if r:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def lowpass(x, k):
    return np.convolve(x, np.ones(k) / k, mode="same")


def tone(freqs, dur, amp):
    t = np.arange(int(dur * SR)) / SR
    return amp * sum(np.sin(2 * np.pi * fr * t) for fr in freqs) / len(freqs)


def save(name, x):
    x = np.clip(x, -1, 1)
    with wave.open(str(out / f"TEMP_{name}.wav"), "wb") as w:
        w.setnchannels(1), w.setsampwidth(2), w.setframerate(SR)
        w.writeframes((x * 32767).astype(np.int16).tobytes())


cue_frame = {}
for c in d["cues"]:
    cue_frame[c["id"]] = start[c["shot"]] + c["at"]


def dur_to_end(cid, end_off=None):
    c = next(c for c in d["cues"] if c["id"] == cid)
    if end_off is None and "end" in c:
        end_off = c["end"]
    if end_off is not None:
        return (start[c["shot"]] + end_off - cue_frame[cid]) / fps
    return None


total_s = (END - 1 + 30) / fps  # sequence + 1 s hold
n = int(total_s * SR)
amb = lowpass(rng.normal(0, 1, n), 60) * 0.10
for k in range(8):  # drips
    p = int(rng.uniform(0.2, total_s - 0.2) * SR)
    amb[p:p + 2400] += tone([1400 + 300 * k], 0.05, 0.08) * env(2400, 0.001, 0.045)
save("amb.water.observatory", amb)

pd = dur_to_end("sfx.beacon.pulse")
t = np.arange(int(pd * SR)) / SR
peak, rise = 5 / fps, 18 / fps
envp = np.exp(-((t - peak) ** 2) / 0.006) + np.where(t > rise, (t - rise) / (pd - rise), 0) * 0.8
save("sfx.beacon.pulse", tone([220, 330, 440], pd, 0.5) * envp)  # stops dead on the collapse

dd = dur_to_end("sfx.water.disturbance")
x = lowpass(rng.normal(0, 1, int(dd * SR)), 25) * 0.5
save("sfx.water.disturbance", x * env(len(x), 0.3, 0.4))
x = np.zeros(int(0.6 * SR))
for k in range(9):
    p = int(rng.uniform(0, 0.5) * SR)
    x[p:p + 600] += rng.normal(0, 0.6, 600) * np.linspace(1, 0, 600)
save("sfx.guardian.stone", x)
rd = dur_to_end("sfx.guardian.rise")
x = (lowpass(rng.normal(0, 1, int(rd * SR)), 200) * 2.5 + tone([48, 61], rd, 0.4)) * env(int(rd * SR), 0.15, 0.3)
save("sfx.guardian.rise", x)
t = np.arange(int(0.9 * SR)) / SR
x = 0.6 * np.sin(2 * np.pi * (85 + 6 * np.sin(2 * np.pi * 7 * t)) * t) * env(len(t), 0.08, 0.4)
save("vo.guardian.vocal", x + lowpass(rng.normal(0, 0.2, len(t)), 8) * env(len(t), 0.08, 0.4))
t = np.arange(int(0.8 * SR)) / SR
x = np.sin(2 * np.pi * 55 * t) * np.exp(-t * 9) * 0.9 + lowpass(rng.normal(0, 1, len(t)), 6) * np.exp(-t * 6) * 0.4
save("sfx.guardian.slam", x)
md = (END - cue_frame["music.encounter.entry"] + 30) / fps
save("music.encounter.entry", tone([73.4, 110, 146.8], md, 0.35) * env(int(md * SR), 0.05, 0.5))
save("ui.interact.available", np.concatenate([tone([880], 0.08, 0.3), tone([1320], 0.12, 0.3)]))
files = {k: {"file": f"TEMP_{k}.wav", "frame": v} for k, v in cue_frame.items()
         if (out / f"TEMP_{k}.wav").exists()}
json.dump({"revision": d["revision"], "fps": [num, den], "end_frame": END - 1, "files": files},
          open(out / "cues_temp.json", "w"), indent=1)
print("TEMP AUDIO", len(files), "files for rev", d["revision"], "->", out)
