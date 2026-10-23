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
AFFTDN_LAG = {44100: 1102, 48000: 1200}  # review-1 and probes 2026-10-23 on ffmpeg 9.0.2 (written here, not read)


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


def aligned(x, out):
    """Normalised correlation of each channel at lag 0 (an oracle that works on periodic audio too)."""
    return [float(np.dot(x[:, c], out[:, c]) / np.sqrt(np.dot(x[:, c], x[:, c]) * np.dot(out[:, c], out[:, c])))
            for c in range(x.shape[1])]


@needs_ffmpeg
class RunFilterTest(unittest.TestCase):
    def assert_kept(self, x, out, rate, res):
        """What every call must keep: rate, channels, length, lag 0 on every channel, channel order."""
        self.assertEqual(res.rate, rate)
        self.assertEqual(out.shape, x.shape)
        self.assertEqual(out.dtype, np.float32)
        x2, o2 = (x[:, None], out[:, None]) if x.ndim == 1 else (x, out)
        for c in range(x2.shape[1]):  # measured here per channel, independently of the adapter
            lag = m.lag(x2[:, c], o2[:, c], rate, int(0.1 * rate))
            self.assertTrue(lag["clear"], lag)
            self.assertEqual(lag["lag_samples"], 0, f"channel {c}")
        if x2.shape[1] == 2:
            self.assertGreater(np.sum(o2[:, 0] ** 2), np.sum(o2[:, 1] ** 2))  # left stays the louder channel

    def test_volume_gives_the_exact_answer_and_keeps_everything(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch).astype(np.float32)
                res = sbf.run_filter(x, rate, "volume=0.5")
                np.testing.assert_allclose(res.audio, 0.5 * x, atol=1e-6)
                self.assert_kept(x, res.audio, rate, res)
                self.assertEqual((res.lag_samples, res.log["timing_source"]), (0, "audio"))

    def test_one_dimensional_input_comes_back_one_dimensional(self):
        x = fx.make("clean_hit", 44100, 1)[:, 0].astype(np.float32)
        res = sbf.run_filter(x, 44100, "volume=1")
        self.assertEqual(res.audio.shape, x.shape)
        np.testing.assert_array_equal(res.audio, x)

    def test_known_latency_table(self):
        self.assertEqual({r: sbf.known_latency("afftdn", r) for r in fx.RATES}, AFFTDN_LAG)
        for args in (("afftdn", 22050), ("afftdn", 32000), ("rubberband", 44100)):
            with self.subTest(args=args):
                with self.assertRaisesRegex(SoundbenchError, "never measured"):
                    sbf.known_latency(*args)

    def test_afftdn_lag_is_compensated_to_zero(self):
        """review-1 #1: afftdn delays by 25 ms and cuts the tail. After the adapter: zero lag, full tail."""
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = noisy_hit(rate, ch)
                res = sbf.run_filter(x, rate, "afftdn", latency_samples=AFFTDN_LAG[rate])
                self.assert_kept(x, res.audio, rate, res)
                self.assertEqual(res.lag_samples, AFFTDN_LAG[rate])
                self.assertEqual(res.log["channel_lags_samples"], [AFFTDN_LAG[rate]] * ch)
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

    def test_afftdn_on_every_fixture_periodic_ones_proven_on_the_probe(self):
        """F4: DC-offset audio is timed on the audio; tonal and looped audio on the probe, and the log says so."""
        probe_names = ("wrong_chime", "rough_tone", "clipped", "bad_seam_bed")
        for name in fx.NAMES:
            for rate in fx.RATES:
                with self.subTest(name=name, rate=rate):
                    x = fx.make(name, rate, 2).astype(np.float32)
                    res = sbf.run_filter(x, rate, "afftdn", latency_samples=AFFTDN_LAG[rate])
                    self.assertEqual(res.audio.shape, x.shape)
                    self.assertEqual(res.log["channel_lags_samples"], [AFFTDN_LAG[rate]] * 2)
                    source = res.log["timing_source"]
                    self.assertTrue(source.startswith("probe") if name in probe_names else source == "audio", source)
                    if name in probe_names:
                        self.assertIn("not on the audio", source)
                    for v in aligned(x, res.audio):
                        self.assertGreater(v, 0.98)  # in time with the input (a 25 ms shift would read far lower)

    def test_afftdn_without_compensation_is_refused(self):
        x = noisy_hit(44100, 2)
        with self.assertRaisesRegex(SoundbenchError, "compensation is off"):
            sbf.run_filter(x, 44100, "afftdn", latency_samples=AFFTDN_LAG[44100], compensate=False)

    def test_an_undeclared_or_wrongly_declared_latency_is_refused(self):
        """F2: compensation uses the declared value; any other reading is unknown latency (tolerance 0 samples)."""
        for rate in fx.RATES:
            x = noisy_hit(rate, 2)
            for declared in (0, AFFTDN_LAG[rate] - 1, AFFTDN_LAG[rate] + 1, 2 * AFFTDN_LAG[rate]):
                with self.subTest(rate=rate, declared=declared):
                    with self.assertRaisesRegex(SoundbenchError, "unknown latency"):
                        sbf.run_filter(x, rate, "afftdn", latency_samples=declared)

    def test_a_graph_that_adds_delay_to_a_known_latency_is_refused(self):
        """F2 proofs: afftdn,lowpass read 1,105 and afftdn,aphaser 1,110; both were compensated before."""
        for graph, name in (("afftdn,lowpass=f=3000", "hummed"), ("afftdn,aphaser", "bass_thump")):
            for rate in fx.RATES:
                with self.subTest(graph=graph, rate=rate):
                    x = fx.make(name, rate, 2).astype(np.float32)
                    with self.assertRaisesRegex(SoundbenchError, "unknown latency"):
                        sbf.run_filter(x, rate, graph, latency_samples=AFFTDN_LAG[rate])

    def test_one_channel_moved_against_the_other_is_refused(self):
        """F1 proofs: the mono sum hid a 30 ms shift of one channel; each channel is now timed on its own."""
        for rate in fx.RATES:
            for name in ("clean_hit", "wrong_chime"):  # timed on the audio, and on the probe
                x = fx.make(name, rate, 2).astype(np.float32)
                n, d = len(x), int(0.03 * rate)
                for graph, declared in ((f"adelay=0|30,atrim=end_sample={n}", 0),
                                        (f"adelay=30|0,atrim=end_sample={n + d}", d),
                                        (f"adelay=0|30,atrim=end_sample={n + d}", d)):
                    with self.subTest(rate=rate, name=name, graph=graph):
                        with self.assertRaisesRegex(SoundbenchError, "channels disagree"):
                            sbf.run_filter(x, rate, graph, latency_samples=declared)

    def test_a_declared_delay_is_compensated_sample_exactly(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch).astype(np.float32)
                d = int(0.03 * rate)
                delays = "|".join(["30"] * ch)
                res = sbf.run_filter(x, rate, f"adelay={delays},atrim=end_sample={len(x) + d}", latency_samples=d)
                self.assertEqual(res.lag_samples, d)
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
        with self.assertRaisesRegex(SoundbenchError, "cannot declare a latency"):
            sbf.run_filter(x, 44100, "apad=pad_len=441", length_change=True, latency_samples=10)

    def test_periodic_audio_is_timed_on_the_probe(self):
        t = np.arange(22050) / 44100
        sine = (0.5 * np.sin(2 * np.pi * 441 * t)).astype(np.float32)
        res = sbf.run_filter(sine, 44100, "volume=1")  # the sine alone cannot be timed: every period correlates
        np.testing.assert_array_equal(res.audio, sine)
        self.assertTrue(res.log["timing_source"].startswith("probe"))

    def test_unprovable_timing_is_refused(self):
        x = fx.make("clean_hit", 44100, 1).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "cannot be proven"):
            sbf.run_filter(x, 44100, "areverse")  # neither the audio nor the probe reads a clear lag

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
        for bad_latency in (-1, 2.5, True, float("nan")):
            with self.subTest(latency=bad_latency):
                with self.assertRaisesRegex(SoundbenchError, "latency_samples"):
                    sbf.run_filter(x, 44100, "volume=1", latency_samples=bad_latency)

    def test_ffmpeg_failure_is_an_error(self):
        x = fx.make("clean_hit", 44100, 1).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "ffmpeg failed"):
            sbf.run_filter(x, 44100, "nosuchfilter")

    def test_same_call_twice_gives_the_same_samples(self):
        x = noisy_hit(44100, 2)
        a = sbf.run_filter(x, 44100, "afftdn", latency_samples=AFFTDN_LAG[44100]).audio
        b = sbf.run_filter(x, 44100, "afftdn", latency_samples=AFFTDN_LAG[44100]).audio
        np.testing.assert_array_equal(a, b)

    def test_the_input_buffer_is_not_changed(self):
        x = noisy_hit(48000, 2)
        before = x.copy()
        sbf.run_filter(x, 48000, "afftdn", latency_samples=AFFTDN_LAG[48000])
        np.testing.assert_array_equal(x, before)


if __name__ == "__main__":
    unittest.main()
