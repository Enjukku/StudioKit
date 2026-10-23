"""Optional tests on real takes (LD-c): set SOUNDBENCH_REAL_TAKES to a folder of ElevenLabs MP3s (with their sidecar
JSON, if any) to run them; otherwise they skip with the reason. No audio is committed; the takes are copied into a
temp folder and never changed.

What every real take must survive (the repair-round findings, 2026-10-23):
  - intake: decoded length = the file's stated length; the requested length only logged (0.5 s came back 480 ms);
  - a normal render (dc, high-pass, trim, fade, loudness, peak) ends 0 or 1, never a crash, and starts silent;
  - denoise with the reviewer's settings (nr 40, nf -20 dBFS) is refused on every take whose floor is under -23 dBFS;
  - saturate and compress act on a quiet take exactly as on the same take normalised;
  - chorus is not refused on the takes' own timing;
  - rank (J020 step 5, review-rank round 1): each sound's takes t1..tN ranked as one round with every level measure
    (F-09, F-13a, LUFS-I): exit 0 or 1 (never a refusal), the order equals the documented key recomputed from the
    table, no clean take reads clipped, a miss called fixed passes after the fix, the derived level matches the
    simulated one, the top take's proof render agrees (and runs only when it passes), every kept plan of every take
    renders and agrees or was refused by rank with render's own reason (review-rank R2-1, the reviewer's e5), and
    nothing is written to out/.
"""

import json
import os
import re
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    import pyloudnorm  # noqa: F401
    import scipy  # noqa: F401
    import soundfile  # noqa: F401
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile and pyloudnorm")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fxops, intake, ops, rank, render  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, read_float32  # noqa: E402

FOLDER = os.environ.get("SOUNDBENCH_REAL_TAKES", "").strip()
TAKES = sorted(Path(FOLDER).glob("*.mp3")) if FOLDER and Path(FOLDER).is_dir() else []
try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
SKIP = ("set SOUNDBENCH_REAL_TAKES to a folder of real MP3 takes to run these" if not TAKES
        else "ffmpeg not found" if not FOUND else None)

CARD = {"kind": "hit", "category": "sfx", "tier": "minor",
        "level": {"measure": "F-09", "target": -24.0, "tolerance": 0.5, "must": False},
        "targets": {"edge_clicks": {"max": 0, "must": True}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}
RANK_CARD = {"category": "sfx", "level": {"measure": "F-09", "target": -18.0, "tolerance": 1.0, "must": True},
             "targets": {"onset_ms": {"max": 5, "must": True}, "true_peak_dbtp": {"max": -1.0, "must": True},
                         "edge_clicks": {"max": 0, "must": True}, "sound_ms": {"min": 40, "max": 400, "must": False},
                         "phone_loss_db": {"max": 12, "must": False}},
             "playback": {"space": "2D", "takes_room": False, "ducks": None}}
RECIPE = {"design": [{"op": "dc"}, {"op": "highpass", "hz": 60}],
          "edit": [{"op": "trim"}, {"op": "fade", "out_ms": 10}, {"op": "loudness"}, {"op": "peak"}]}


def requested_ms(mp3: Path):
    side = mp3.with_suffix(".json")
    try:
        sec = json.loads(side.read_text(encoding="utf-8")).get("request", {}).get("duration_seconds")
        return None if sec is None else 1000 * float(sec)
    except (OSError, ValueError, AttributeError):
        return None


@unittest.skipIf(SKIP, SKIP or "")
class RealTakeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._t = tempfile.TemporaryDirectory()
        cls.d = Path(cls._t.name)
        cls.cues = {}
        for mp3 in TAKES:
            cue = "REAL-" + mp3.stem.replace(".", "-")
            take = cls.d / cue / "takes" / f"{cue}.r1.t1.mp3"
            take.parent.mkdir(parents=True)
            shutil.copyfile(mp3, take)
            cls.cues[cue] = (mp3, take)

    @classmethod
    def tearDownClass(cls):
        cls._t.cleanup()

    def test_intake_render_and_guards_on_every_take(self):
        for cue, (src, take) in self.cues.items():
            with self.subTest(take=src.name):
                asked = requested_ms(src)
                info = intake.decode_take(take, requested_ms=asked)
                self.assertLessEqual(abs(info["decoded_ms"] - info["stated_ms"]), intake.TOLERANCE_MS)
                if asked is not None and abs(info["decoded_ms"] - asked) > intake.TOLERANCE_MS:
                    self.assertTrue(info["warnings"])  # logged, never refused
                card = {**CARD, "cue": cue}
                recipe = {**RECIPE, "cue": cue, "take": f"takes/{cue}.r1.t1.mp3"}
                (take.parents[1] / "card.json").write_text(json.dumps(card), encoding="utf-8")
                (take.parents[1] / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
                doc, code = render.render(take.parents[1])
                self.assertIn(code, (0, 1))
                self.assertNotIn("edge_clicks", doc["must_failed"])  # trim faded a mid-waveform start
                y, rate = read_float32(take.parents[1] / "out" / f"{cue}.flac")
                self.assertEqual(float(np.max(np.abs(y[0]))), 0.0)
                x, rate = read_float32(intake.master_path(take))
                x = x.astype(np.float64)
                floor = m.tail_noise(x - x.mean(axis=0), rate)["floor_dbfs"]
                if floor is not None and floor < -23:
                    with self.assertRaises(SoundbenchError):
                        fxops.run("denoise", x, rate, ops.check_params("denoise", {"nr_db": 40, "nf_db": -20}),
                                  {"kind": "hit"})
                k = 0.9 / float(np.max(np.abs(x)))
                for op, given in (("saturate", {"drive_db": 12}), ("compress", {"threshold_db": -20, "ratio": 4})):
                    yq, _ = ops.run(op, x, rate, ops.check_params(op, given), {"kind": "hit", "category": "sfx"})
                    yn, _ = ops.run(op, x * k, rate, ops.check_params(op, given), {"kind": "hit", "category": "sfx"})
                    np.testing.assert_allclose(yq * k, yn, rtol=1e-9, atol=1e-12)
                fxops.run("chorus", x, rate, ops.check_params("chorus", {}), {"kind": "whoosh"})

    def test_rank_every_real_round(self):
        rounds: dict = {}
        for mp3 in TAKES:
            found = re.match(r"^(.+)\.t(\d+)$", mp3.stem)
            if found:
                rounds.setdefault(found[1], []).append((int(found[2]), mp3))
        self.assertTrue(rounds, "no takes named <sound>.t<n>.mp3")
        with tempfile.TemporaryDirectory() as tmp:
            for sound, takes in sorted(rounds.items()):
                with self.subTest(sound=sound):
                    cue = "REAL-" + re.sub(r"[^A-Za-z0-9-]", "-", sound)
                    folder = Path(tmp) / cue
                    (folder / "takes").mkdir(parents=True)
                    for n, src in takes:
                        take = folder / "takes" / f"{cue}.r1.t{n}.mp3"
                        shutil.copyfile(src, take)
                        intake.decode_take(take, requested_ms=requested_ms(src))
                    kind = "whoosh" if re.search(r"whoosh|swish", sound) else "hit"
                    tier = {3: "minor", 4: "frequent"}.get(len(takes), "important")
                    for measure in ("F-09", "F-13a", "LUFS-I"):  # every level measure a card can name (review-rank F2)
                        with self.subTest(sound=sound, measure=measure):
                            self._rank_one(folder, {**RANK_CARD, "cue": cue, "kind": kind, "tier": tier,
                                                    "level": {**RANK_CARD["level"], "measure": measure}})

    def _rank_one(self, folder: Path, card: dict):
        (folder / "card.json").write_text(json.dumps(card), encoding="utf-8")
        doc, code = rank.rank(folder)  # a derived/simulated level disagreement would raise here (exit 2)
        self.assertIn(code, (0, 1))
        keys = [e["rank_key"] for e in doc["takes"]]
        self.assertEqual(keys, sorted(keys))
        for e in doc["takes"]:
            self.assertEqual(e["rank_key"], [int(bool(e["rejected"])), int(not e["passes_after_fix"]),
                                             len(e["must_after"]), len(e["aim_after"]), len(e["fixed"]),
                                             len(e["near_after"]), e["n"]])
            self.assertFalse(e["clip"]["clipped"], e["clip"])  # the 62 clean real takes: no clip rejection
            after = {r["target"]: r for r in e["after"]}
            for x in e["misses"]:
                if x["fix"] == "fixed":
                    self.assertEqual(after[x["target"]]["result"], "pass")
            lv = (e["fix"] or {}).get("level")
            if lv:
                cut = max(0.0, lv["true_peak_in_dbtp"] + lv["gain_needed_db"] - lv["peak_limit_dbtp"])
                self.assertAlmostEqual(lv["peak_cut_db"], cut, delta=0.002)
                self.assertLessEqual(abs(lv["predicted_level"] - lv["simulated_level"]), rank.LEVEL_AGREE_DB)
                if abs(abs(lv["predicted_level"] - lv["target"]) - lv["tolerance"]) > rank.LEVEL_AGREE_DB:
                    self.assertEqual(after["level"]["result"] == "pass", lv["fits"])
        if doc["proof"] is not None:
            self.assertTrue(doc["proof"]["agrees"])
        self.assertEqual(doc["proof"] is not None, doc["takes"][0]["passes_after_fix"])  # only a "use" is proven
        for e in doc["takes"]:  # e5 (review-rank R2-1): every kept plan renders, or rank refused it as render would
            if e["rejected"]:
                continue
            if e["fix"]["plan"] is not None:
                self.assertTrue(rank.prove(card, folder, e)["agrees"])
                continue
            reasons = [p["error"] for p in e["fix"]["refused_plans"]]
            with self.assertRaises(SoundbenchError) as raised:
                rank.prove(card, folder, {**e, "fix": {**e["fix"], "steps": []}})
            self.assertTrue(any(str(raised.exception) in r for r in reasons), (str(raised.exception), reasons))
        self.assertFalse((folder / "out").exists())

if __name__ == "__main__":
    unittest.main()
