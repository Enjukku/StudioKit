"""Tests for tools/audio/soundbench/ffmpeg.py: finding ffmpeg and the G-7 time checks (J020 step 1).

Every call is checked for the right answer AND what it must not change (rate, channels, length, lag, channel order).
review-1's afftdn bug (25 ms late, tail cut, no error) is the case these tests exist for. Tests that run ffmpeg skip
with a reason when it is missing.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import numpy as np
    import scipy  # noqa: F401
    import soundfile  # noqa: F401
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy and soundfile")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
needs_ffmpeg = unittest.skipUnless(FOUND, "ffmpeg not found (SOUNDBENCH_FFMPEG, PATH, WinGet folder): skipped")
CONFIGS = [(r, c) for r in fx.RATES for c in fx.CHANNELS]
AFFTDN_LAG_MS = 25.0  # review-1 and probe 2026-10-23 on ffmpeg 9.0.2: 1,102 samples at 44.1 kHz, 1,200 at 48 kHz


def noisy_hit(rate, ch, seed=3):
    """The clean hit under a -50 dBFS hiss on every channel (what afftdn is for)."""
    x = fx.make("clean_hit", rate, ch)
    x = x + 0.003 * np.random.RandomState(seed).standard_normal(x.shape)
    return x.astype(np.float32)


def fake_exe(folder: Path) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    p = folder / ("ffmpeg.exe" if os.name == "nt" else "ffmpeg")
    p.write_bytes(b"")
    p.chmod(0o755)
    return p


class FindTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_env_override_wins_over_path_and_winget(self):
        forced = fake_exe(self.d / "forced")
        on_path = fake_exe(self.d / "onpath")
        env = {sbf.ENV_VAR: str(forced), "PATH": str(on_path.parent), "PATHEXT": ".EXE", "LOCALAPPDATA": str(self.d)}
        got = sbf.find_ffmpeg(env)
        self.assertEqual((got.path, got.how), (forced, sbf.ENV_VAR))

    def test_env_override_to_a_missing_file_is_an_error_not_a_fallback(self):
        fake_exe(self.d / "onpath")
        env = {sbf.ENV_VAR: str(self.d / "nope.exe"), "PATH": str(self.d / "onpath"), "PATHEXT": ".EXE"}
        with self.assertRaises(SoundbenchError):
            sbf.find_ffmpeg(env)

    def test_path_then_winget_folder(self):
        on_path = fake_exe(self.d / "onpath")
        winget = fake_exe(self.d / "Microsoft" / "WinGet" / "Packages" / "Gyan.FFmpeg_x" / "ffmpeg-9.0.2" / "bin")
        if os.name != "nt":
            winget = winget.rename(winget.with_name("ffmpeg.exe"))
        base = {"PATHEXT": ".EXE", "LOCALAPPDATA": str(self.d)}
        self.assertEqual(sbf.find_ffmpeg({**base, "PATH": str(on_path.parent)}).how, "PATH")
        got = sbf.find_ffmpeg({**base, "PATH": str(self.d / "empty")})
        self.assertEqual((got.path, got.how), (winget, "WinGet"))
        self.assertIsNone(sbf.find_ffmpeg({"PATH": str(self.d / "empty"), "LOCALAPPDATA": str(self.d / "none")}))


@needs_ffmpeg
class RunFilterTest(unittest.TestCase):
    def assert_kept(self, x, out, rate, res):
        """What every call must keep: rate, channels, length, lag 0, channel order."""
        self.assertEqual(res.rate, rate)
        self.assertEqual(out.shape, x.shape)
        self.assertEqual(out.dtype, np.float32)
        lag = m.lag(x, out, rate, int(0.1 * rate))  # measured here, independently of the adapter
        self.assertTrue(lag["clear"], lag)
        self.assertEqual(lag["lag_samples"], 0)
        if x.ndim == 2 and x.shape[1] == 2:
            for c in range(2):  # each output channel lines up with its own input channel
                self.assertEqual(m.lag(x[:, c], out[:, c], rate, int(0.1 * rate))["lag_samples"], 0)
            self.assertGreater(np.sum(out[:, 0] ** 2), np.sum(out[:, 1] ** 2))  # left stays the louder channel

    def test_volume_gives_the_exact_answer_and_keeps_everything(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch).astype(np.float32)
                res = sbf.run_filter(x, rate, "volume=0.5")
                np.testing.assert_allclose(res.audio, 0.5 * x, atol=1e-6)
                self.assert_kept(x, res.audio, rate, res)
                self.assertEqual(res.lag_samples, 0)

    def test_one_dimensional_input_comes_back_one_dimensional(self):
        x = fx.make("clean_hit", 44100, 1)[:, 0].astype(np.float32)
        res = sbf.run_filter(x, 44100, "volume=1")
        self.assertEqual(res.audio.shape, x.shape)
        np.testing.assert_array_equal(res.audio, x)

    def test_afftdn_lag_is_compensated_to_zero(self):
        """review-1 #1: afftdn delays by 25 ms and cuts the tail. After the adapter: zero lag, full tail."""
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = noisy_hit(rate, ch)
                res = sbf.run_filter(x, rate, "afftdn", max_lag_ms=50)
                self.assert_kept(x, res.audio, rate, res)
                self.assertEqual(res.lag_samples, round(AFFTDN_LAG_MS / 1000 * rate),
                                 "afftdn's latency changed on this ffmpeg: re-probe (doctor warns on a new version)")
                self.assertTrue(res.log["compensated"])
                mono_in, mono_out = x.mean(axis=1), res.audio.mean(axis=1)
                self.assertEqual(m.onset_index(mono_out), m.onset_index(mono_in))
                self.assertAlmostEqual(m.main_transient_ms(res.audio.astype(np.float64), rate),
                                       m.main_transient_ms(x.astype(np.float64), rate), delta=0.5)
                tail = slice(len(x) - int(0.07 * rate), None)  # the last 70 ms: the hiss after the hit
                self.assertLess(float(np.sqrt(np.mean(mono_out[tail] ** 2))),
                                float(np.sqrt(np.mean(mono_in[tail] ** 2))) * 0.7)  # it did denoise
                body = slice(int(0.02 * rate), int(0.2 * rate))
                ratio = np.sqrt(np.sum(mono_out[body] ** 2) / np.sum(mono_in[body] ** 2))
                self.assertAlmostEqual(float(ratio), 1.0, delta=0.05)  # the hit itself is kept

    def test_afftdn_without_compensation_is_refused(self):
        x = noisy_hit(44100, 2)
        with self.assertRaisesRegex(SoundbenchError, "compensation is off"):
            sbf.run_filter(x, 44100, "afftdn", max_lag_ms=50, compensate=False)

    def test_a_wrong_first_lag_reading_is_caught_by_the_recheck(self):
        """The safety net: if the first lag reading were one sample off, the re-check after compensation refuses."""
        real = m.lag
        calls = []

        def off_by_one(*a, **k):
            r = dict(real(*a, **k))
            calls.append(r["lag_samples"])
            if len(calls) == 1 and r["lag_samples"]:
                r["lag_samples"] -= 1
            return r

        x = noisy_hit(44100, 2)
        with mock.patch.object(sbf.measures, "lag", off_by_one):
            with self.assertRaisesRegex(SoundbenchError, "after compensation"):
                sbf.run_filter(x, 44100, "afftdn", max_lag_ms=50)

    def test_an_undeclared_latency_is_refused(self):
        x = noisy_hit(48000, 1)
        with self.assertRaisesRegex(SoundbenchError, "unknown latency"):
            sbf.run_filter(x, 48000, "afftdn")  # max_lag_ms 0: any lag is unknown
        with self.assertRaisesRegex(SoundbenchError, "unknown latency"):
            sbf.run_filter(x, 48000, "afftdn", max_lag_ms=10)

    def test_a_declared_delay_is_compensated_sample_exactly(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch).astype(np.float32)
                pad = int(np.ceil(0.04 * rate))
                delays = "|".join(["30"] * ch)
                res = sbf.run_filter(x, rate, f"adelay={delays},atrim=end_sample={len(x) + pad}", max_lag_ms=40)
                self.assertEqual(res.lag_samples, int(0.03 * rate))
                np.testing.assert_array_equal(res.audio, x)

    def test_rate_channel_count_and_length_changes_are_refused(self):
        x = fx.make("clean_hit", 48000, 2).astype(np.float32)
        for graph, why in (("aresample=44100", "sample rate"), ("pan=mono|c0=c0", "channels"),
                           ("apad=pad_len=480", "length")):
            with self.subTest(graph=graph):
                with self.assertRaisesRegex(SoundbenchError, why):
                    sbf.run_filter(x, 48000, graph)

    def test_a_channel_swap_is_refused(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make("clean_hit", rate, 2).astype(np.float32)
                with self.assertRaisesRegex(SoundbenchError, "channel"):
                    sbf.run_filter(x, rate, "channelmap=1|0")

    def test_a_declared_length_change_passes_with_zero_lag(self):
        x = fx.make("clean_hit", 44100, 2).astype(np.float32)
        res = sbf.run_filter(x, 44100, "apad=pad_len=441", length_change=True)
        self.assertEqual(len(res.audio), len(x) + 441)
        np.testing.assert_array_equal(res.audio[: len(x)], x)

    def test_unprovable_timing_is_refused(self):
        x = fx.make("clean_hit", 44100, 1).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "cannot be proven"):
            sbf.run_filter(x, 44100, "areverse")
        t = np.arange(22050) / 44100
        sine = (0.5 * np.sin(2 * np.pi * 441 * t)).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "cannot be proven"):
            sbf.run_filter(sine, 44100, "volume=1")  # periodic: the lag cannot be told from one period

    def test_silent_input(self):
        x = np.zeros((4410, 2), np.float32)
        self.assertEqual(sbf.run_filter(x, 44100, "volume=0.5").audio.shape, x.shape)
        with self.assertRaisesRegex(SoundbenchError, "silent input"):
            sbf.run_filter(x, 44100, "aeval=0.1*sin(2*PI*440*t)|0.1*sin(2*PI*440*t)")

    def test_bad_inputs_are_refused_before_ffmpeg_runs(self):
        x = fx.make("clean_hit", 44100, 1).astype(np.float32)
        bad = x.copy()
        bad[10] = np.nan
        for args, why in (((bad, 44100, "volume=1"), "NaN"), ((x.astype(np.int16), 44100, "volume=1"), "float"),
                          ((x, 44100.5, "volume=1"), "sample rate"), ((x, 44100, "volume=1\nvolume=2"), "one"),
                          ((x[:1], 44100, "volume=1"), "fewer than 2")):
            with self.subTest(why=why):
                with self.assertRaisesRegex(SoundbenchError, why):
                    sbf.run_filter(*args)
        with self.assertRaisesRegex(SoundbenchError, "max_lag_ms"):
            sbf.run_filter(x, 44100, "volume=1", max_lag_ms=float("nan"))

    def test_ffmpeg_failure_is_an_error(self):
        x = fx.make("clean_hit", 44100, 1).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "ffmpeg failed"):
            sbf.run_filter(x, 44100, "nosuchfilter")

    def test_same_call_twice_gives_the_same_samples(self):
        x = noisy_hit(44100, 2)
        a = sbf.run_filter(x, 44100, "afftdn", max_lag_ms=50).audio
        b = sbf.run_filter(x, 44100, "afftdn", max_lag_ms=50).audio
        np.testing.assert_array_equal(a, b)

    def test_the_input_buffer_is_not_changed(self):
        x = noisy_hit(48000, 2)
        before = x.copy()
        sbf.run_filter(x, 48000, "afftdn", max_lag_ms=50)
        np.testing.assert_array_equal(x, before)


if __name__ == "__main__":
    unittest.main()
