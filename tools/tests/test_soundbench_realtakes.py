"""Optional tests on real takes (LD-c): set SOUNDBENCH_REAL_TAKES to a folder of ElevenLabs MP3s (with their sidecar
JSON, if any) to run them; otherwise they skip with the reason. No audio is committed; the takes are copied into a
temp folder and never changed.

What every real take must survive (the repair-round findings, 2026-10-23):
  - intake: decoded length = the file's stated length; the requested length only logged (0.5 s came back 480 ms);
  - a normal render (dc, high-pass, trim, fade, loudness, peak) ends 0 or 1, never a crash, and starts silent;
  - denoise with the reviewer's settings (nr 40, nf -20 dBFS) is refused on every take whose floor is under -23 dBFS;
  - saturate and compress act on a quiet take exactly as on the same take normalised;
  - chorus is not refused on the takes' own timing.
"""

import json
import os
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
from tools.audio.soundbench import fxops, intake, ops, render  # noqa: E402
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


if __name__ == "__main__":
    unittest.main()
