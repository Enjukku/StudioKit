"""Tests for tools/audio/cue_check.py: the J018 sound review cases as synthetic files (G3-P1)."""

import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    import pyloudnorm  # noqa: F401
    import soundfile as sf
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, soundfile and pyloudnorm")

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "audio"))
import cue_check as cc  # noqa: E402

RATE = 48000


def tone(ms, hz=880.0, peak_db=-1.0, decay=False):
    t = np.arange(int(RATE * ms / 1000)) / RATE
    y = np.sin(2 * np.pi * hz * t) * 10 ** (peak_db / 20)
    return y * np.exp(-t * 8) if decay else y


def silence(ms):
    return np.zeros(int(RATE * ms / 1000))


class CueCheckTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def save(self, name, y, dc=0.0):
        p = self.d / name
        sf.write(str(p), (y + dc).astype(np.float32), RATE, subtype="FLOAT")
        return p

    def test_onset_tail_length_and_dc_offset(self):
        p = self.save("a.wav", np.concatenate([silence(50), tone(200), silence(300)]), dc=0.05)
        r = cc.measure(p)
        self.assertAlmostEqual(r["F-01_onset_ms"], 50, delta=1)  # the DC offset does not hide the silent head
        self.assertAlmostEqual(r["F-12_length"]["sound_ms"], 200, delta=12)
        self.assertAlmostEqual(r["F-12_length"]["file_ms"], 550, delta=1)
        self.assertFalse(r["F-04_tail"]["ends_above_-40"])

    def test_cut_before_decay_is_flagged(self):
        r = cc.measure(self.save("cut.wav", tone(200)))
        self.assertTrue(r["F-04_tail"]["ends_above_-40"])

    def test_pitch_names_the_note(self):
        r = cc.measure(self.save("a5.wav", tone(400, 880.0)))
        self.assertEqual(r["F-10_pitch"]["note"], "A5")
        self.assertTrue(r["F-10_pitch"]["trusted"])

    def test_momentary_parity_ignores_trailing_silence(self):
        # an honest pair: the rare result is longer at the same level; trailing silence must not change the verdict
        common = np.concatenate([tone(120, 880.0)])
        rare = np.concatenate([tone(120, 880.0), tone(120, 880.0)])
        a, b = self.save("c.wav", common), self.save("r.wav", rare)
        pa, pb = self.save("cp.wav", np.concatenate([common, silence(300)])), self.save("rp.wav", np.concatenate([rare, silence(300)]))
        plain = cc.parity([a, b], "momentary")["spread_lu"]
        padded = cc.parity([pa, pb], "momentary")["spread_lu"]
        self.assertLess(plain, 1.0)
        self.assertAlmostEqual(plain, padded, delta=0.2)

    def test_momentary_parity_catches_a_louder_rare_result(self):
        a = self.save("c.wav", tone(200, 880.0, -6))
        b = self.save("r.wav", tone(200, 880.0, -2))
        self.assertGreater(cc.parity([a, b], "momentary")["spread_lu"], 3.0)

    def test_integrated_parity_uses_one_common_length(self):
        a = self.save("o1.wav", tone(300))
        b = self.save("o2.wav", tone(600))
        r = cc.parity([a, b], "integrated")
        self.assertGreater(r["common_length_ms"], 600)

    def test_errors(self):
        with self.assertRaises(cc.CueError):
            cc.measure(self.d / "missing.wav")
        with self.assertRaises(cc.CueError):
            cc.parity([self.save("one.wav", tone(100))], "momentary")


if __name__ == "__main__":
    unittest.main()
