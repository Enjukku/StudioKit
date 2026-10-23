"""Tests for tools/audio/soundbench/measures.py and the cue_check.py wrapper (J020 step 2, design G-3, G-4, section 9).

The moved measures (F-01 to F-13) must equal the golden JSON captured from the old cue_check (git 78c730f) on every
fixture; each new measure gets a known answer at 44.1 and 48 kHz, mono and stereo, its listed false readings as
tests, and a check that measuring never changes the audio.
"""

import json
import subprocess
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
from tools.audio import cue_check as cc  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402

GOLDEN = ROOT / "tools" / "audio" / "soundbench" / "golden" / "cue_check_golden.json"
CONFIGS = [(r, c) for r in fx.RATES for c in fx.CHANNELS]


def loaded(name, rate, ch):
    x = fx.make(name, rate, ch).astype(np.float32).astype(np.float64)  # as written and read back (float32 WAV)
    return x - x.mean(axis=0)


def tone(rate, ms, hz=440.0, amp=0.5):
    t = np.arange(int(rate * ms / 1000)) / rate
    return amp * np.sin(2 * np.pi * hz * t)


def col(y, ch=1):
    y = np.asarray(y, dtype=np.float64)[:, None]
    return np.repeat(y, ch, axis=1) if ch > 1 else y


class GoldenTest(unittest.TestCase):
    """F-01..F-13 after the move equal the old tool's output, number for number."""

    @classmethod
    def setUpClass(cls):
        cls.doc = json.loads(GOLDEN.read_text(encoding="utf-8"))
        cls._t = tempfile.TemporaryDirectory()
        cls.d = Path(cls._t.name)

    @classmethod
    def tearDownClass(cls):
        cls._t.cleanup()

    def paths(self, i, case):
        return [fx.write_wav(self.d / f"{i}_{n}_{case['rate']}_{case['channels']}.wav",
                             fx.make(n, case["rate"], case["channels"]), case["rate"]) for n in case["fixtures"]]

    def test_golden_covers_every_fixture_rate_and_layout(self):
        seen = {(c["fixtures"][0], c["rate"], c["channels"]) for c in self.doc["cases"] if c["kind"] == "measure"}
        self.assertEqual(len(seen), len(fx.NAMES) * 4)
        self.assertEqual({c["mode"] for c in self.doc["cases"] if c["kind"] == "parity"}, {"integrated", "momentary"})

    def test_every_moved_measure_equals_the_golden(self):
        for i, case in enumerate(self.doc["cases"]):
            with self.subTest(case=i, fixtures=case["fixtures"], rate=case["rate"], ch=case["channels"]):
                paths = self.paths(i, case)
                if case["kind"] == "measure":
                    for got in (cc.measure(paths[0], case["low_cut"], case["high_pitch"]),
                                m.cue_record(paths[0], case["low_cut"], case["high_pitch"], tool="cue_check measure")):
                        got.pop("file")
                        self.assertEqual(got, case["expected"])
                else:
                    got = cc.parity(paths, case["mode"])
                    got.pop("files")
                    self.assertEqual(got, case["expected"])

    def test_soundbench_measure_keeps_every_cue_check_number(self):
        case = next(c for c in self.doc["cases"] if c["kind"] == "measure" and c["channels"] == 2)
        rec = m.measure(self.paths(900, case)[0])
        for key, val in case["expected"].items():
            if key != "tool":
                self.assertEqual(rec[key], val, key)

    def test_cue_check_command_line_output_unchanged(self):
        case = next(c for c in self.doc["cases"] if c["kind"] == "measure" and c["fixtures"] == ["hummed"])
        p = self.paths(901, case)[0]
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "audio" / "cue_check.py"), "measure", str(p),
                              "--json"], capture_output=True, text=True, check=True).stdout
        got = json.loads(out)
        got.pop("file")
        self.assertEqual(got, case["expected"])


class NewMeasuresTest(unittest.TestCase):
    def test_main_transient_and_attack_on_hits(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                self.assertAlmostEqual(m.main_transient_ms(loaded("clean_hit", rate, ch), rate), fx.CLEAN_HIT_ONSET_MS, delta=1)
                self.assertAlmostEqual(m.main_transient_ms(loaded("late_hit", rate, ch), rate), fx.LATE_HIT_ONSET_MS, delta=1)
                self.assertLess(m.attack_rise_ms(loaded("clean_hit", rate, ch), rate), 2.0)

    def test_exact_answers_on_a_steady_square_wave(self):
        """Exact by construction: every sample has the same energy and the onset is one sample (48 kHz)."""
        rate = 48000
        sq = np.where((np.arange(9600) // 24) % 2 == 0, 0.5, -0.5)  # 200 ms, 1 kHz, DC-free
        x = col(np.concatenate([np.zeros(2400), sq, np.zeros(2400)]))  # onset at 50.0 ms
        self.assertEqual(m.attack_share(x, rate), 0.025)  # 240 / 9600 samples
        v = m.main_transient_ms(x, rate)  # centre of the first 1 ms window within 10 dB: 0.4 ms before a step
        self.assertTrue(49.5 <= v <= 50.0, v)

    def test_attack_rise_reads_a_50ms_linear_ramp_as_40ms(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                y = tone(rate, 300, 1000)
                k = int(0.05 * rate)
                y[:k] *= np.linspace(0, 1, k)
                self.assertAlmostEqual(m.attack_rise_ms(col(y, ch), rate), 40.0, delta=2.0)

    def test_attack_share_falls_when_the_attack_is_smeared(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = loaded("clean_hit", rate, ch)
                clean = m.attack_share(x, rate)
                self.assertTrue(0.1 <= clean <= 0.3, clean)
                s = x.copy()
                on = int(fx.CLEAN_HIT_ONSET_MS / 1000 * rate)
                k = int(0.03 * rate)
                s[on:on + k] *= np.linspace(0, 1, k)[:, None]
                self.assertLess(m.attack_share(s, rate), clean / 2)

    def test_phone_loss(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                self.assertGreater(m.phone_loss_db(loaded("bass_thump", rate, ch), rate), 30)
                self.assertLess(m.phone_loss_db(col(tone(rate, 300, 1000), ch), rate), 0.5)
                self.assertLess(m.phone_loss_db(loaded("wrong_chime", rate, ch), rate), 1.0)
                self.assertGreater(m.phone_loss_db(col(tone(rate, 300, 16000), ch), rate), 12)  # the 10 kHz low-pass

    def test_tail_noise_reads_the_floor_and_digital_silence(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = np.repeat(loaded("clean_hit", rate, 1), ch, axis=1)  # no fixture noise on any channel
                quiet = m.tail_noise(x, rate)  # digital silence after the hit (only the DC removal's residue)
                self.assertTrue(quiet["floor_dbfs"] is None or quiet["floor_dbfs"] < -90, quiet)
                noisy = x + 0.001 * np.random.RandomState(5).standard_normal((len(x), 1))
                r = m.tail_noise(noisy, rate)
                self.assertAlmostEqual(r["floor_dbfs"], -60.0, delta=1.5)
                self.assertGreater(r["snr_db"], 40)
                self.assertFalse(r["sound_reaches_end"])

    def test_phone_loss_equals_the_filters_computed_attenuation(self):
        """Exact answer: a steady tone loses what the two 4th-order Butterworth filters pass at its frequency."""
        from scipy.signal import butter, sosfreqz

        for rate in fx.RATES:
            hp = butter(4, 400, "highpass", fs=rate, output="sos")
            lp = butter(4, 10000, "lowpass", fs=rate, output="sos")
            for hz in (300.0, 14000.0):
                with self.subTest(rate=rate, hz=hz):
                    _, h1 = sosfreqz(hp, worN=[hz], fs=rate)
                    _, h2 = sosfreqz(lp, worN=[hz], fs=rate)
                    want = -20 * np.log10(abs(h1[0] * h2[0]))
                    self.assertAlmostEqual(m.phone_loss_db(col(tone(rate, 2000, hz)), rate), want, delta=0.05)

    def test_tail_noise_reads_exactly_the_last_100ms(self):
        """The floor window is the last 100 ms after the sound: 50 ms at -55 dBFS then 50 ms at -65 dBFS."""
        rate = 48000
        rs = np.random.RandomState(11)

        def noise(ms, dbfs):
            z = rs.standard_normal(int(rate * ms / 1000))
            return z / np.sqrt(np.mean(z ** 2)) * 10 ** (dbfs / 20)

        y = np.concatenate([np.zeros(480), tone(rate, 200, 1000, 0.7), noise(200, -75), noise(50, -55), noise(50, -65)])
        r = m.tail_noise(col(y), rate)
        want = 10 * np.log10((10 ** (-55 / 10) + 10 ** (-65 / 10)) / 2)  # -57.6 dBFS: the mean power of both halves
        self.assertEqual(r["window_ms"], 100.0)
        self.assertAlmostEqual(r["floor_dbfs"], want, delta=0.1)

    def test_lag_second_peak_limit_just_inside_and_just_outside(self):
        """Exact answer: k copies of one noise block correlate (k-1)/k at one block's shift (limit 0.9)."""
        block = np.random.RandomState(4).standard_normal(1000)
        inside, outside = np.tile(block, 9), np.tile(block, 11)  # 8/9 = 0.889 and 10/11 = 0.909
        r_in, r_out = m.lag(inside, inside, 44100, 2500), m.lag(outside, outside, 44100, 2500)
        self.assertAlmostEqual(r_in["second_peak_ratio"], 8 / 9, delta=0.003)
        self.assertAlmostEqual(r_out["second_peak_ratio"], 10 / 11, delta=0.003)
        self.assertTrue(r_in["clear"])
        self.assertFalse(r_out["clear"])

    def test_lag_ignores_a_dc_offset(self):
        """F4: an offset correlates at every lag; the mean is removed first."""
        for rate in fx.RATES:
            x = loaded("clean_hit", rate, 1) + 0.2
            y = np.vstack([np.full((37, 1), 0.2), x[:-37]])
            r = m.lag(x, y, rate, 2400)
            self.assertTrue(r["clear"], r)
            self.assertEqual(r["lag_samples"], 37)

    def test_tail_noise_false_reading_sound_still_playing_is_flagged(self):
        r = m.tail_noise(loaded("hiss_lock", 44100, 1), 44100)
        self.assertTrue(r["sound_reaches_end"])  # the "floor" is the sound itself: the flag says so
        self.assertLess(r["snr_db"], 3)

    def test_clicks_finds_a_planted_click_once_and_not_on_clean_sounds(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                for name in ("clean_hit", "wrong_chime", "bad_seam_bed", "hummed", "dc_offset"):
                    self.assertEqual(m.clicks(loaded(name, rate, ch), rate)["count"], 0, name)
                x = loaded("wrong_chime", rate, ch)
                at = int(0.15 * rate)
                x[at, -1] += 0.3  # on the last channel only: every channel is checked
                r = m.clicks(x, rate)
                self.assertEqual(r["count"], 1)
                self.assertAlmostEqual(r["first_ms"][0], 150.0, delta=0.1)

    def test_clicks_reports_edges_that_start_or_stop_mid_waveform(self):
        rate = 44100
        x = loaded("clean_hit", rate, 2)
        self.assertEqual(m.clicks(x, rate)["edges"], [])  # starts and ends in silence
        t = np.arange(int(0.2 * rate)) / rate
        y = col(0.5 * np.sin(2 * np.pi * 440 * t + 1.0), 2)  # starts at 0.42 and ends mid-cycle
        r = m.clicks(y, rate)
        self.assertEqual((r["edges"], r["edge_count"]), (["start", "end"], 2))
        self.assertEqual(r["count"], 0)  # edges are reported apart from interior clicks

    def test_edges_read_the_samples_playback_starts_from(self):
        """Playback starts and stops from the file's own first and last samples, not from the mean-removed audio (J020
        step 5: a real low thump that starts and ends at exactly 0 read two edge clicks after its -0.0135 mean was
        removed). Both directions: a net offset with zero edges reads none; a DC take with hot edges reads both."""
        rate = 44100
        t = np.arange(int(0.3 * rate)) / rate
        half = col(0.4 * np.sin(np.pi * t / 0.3) * np.sin(2 * np.pi * 60 * t) + 0.3 * np.sin(np.pi * t / 0.3) ** 8, 2)
        half[0] = half[-1] = 0.0  # starts and ends at exactly 0, as a trimmed and faded render does
        self.assertGreater(abs(float(half.mean())), 0.01 * float(np.max(np.abs(half))))  # a real net offset
        dc = fx.make("dc_offset", rate, 2)  # silence + 0.08 at both ends: playback jumps to 0.08
        with tempfile.TemporaryDirectory() as d:
            for name, x, want in (("half", half, []), ("dc", dc, ["start", "end"])):
                with self.subTest(case=name):
                    p = fx.write_wav(Path(d) / f"{name}.wav", x, rate)
                    self.assertEqual(m.measure(p)["clicks"]["edges"], want)
                    self.assertEqual(m.measure_audio(x, rate)["clicks"]["edges"], want)

    def test_clicks_false_reading_hidden_in_noise(self):
        x = loaded("hiss_lock", 48000, 1)
        x[4800, 0] += 0.3
        self.assertEqual(m.clicks(x, 48000)["count"], 0)

    def test_tonality_names_notes_and_hears_hiss(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                hiss = m.tonality(loaded("hiss_lock", rate, ch), rate)
                self.assertEqual(hiss["reading"], "noisy")
                self.assertGreater(hiss["flatness"], 0.3)
                chime = m.tonality(loaded("wrong_chime", rate, ch), rate)
                self.assertEqual(chime["reading"], "tonal")
                self.assertEqual(chime["notes"][0], "C#5")
                self.assertIn("C#6", chime["notes"])  # false reading: harmonics are listed as notes
                self.assertEqual(len(chime["notes"]), len(set(chime["notes"])))  # each note once
                two = tone(rate, 400, 1730, 0.3) + tone(rate, 400, 1790, 0.25)  # two peaks, both A6
                self.assertEqual(m.tonality(col(two, ch), rate)["notes"], ["A6"])

    def test_roughness(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                self.assertAlmostEqual(m.roughness(loaded("rough_tone", rate, ch), rate), fx.ROUGH_DEPTH, delta=0.05)
                self.assertLess(m.roughness(col(tone(rate, 500), ch), rate), 0.05)
                self.assertIsNone(m.roughness(col(tone(rate, 60), ch), rate))
                t = np.arange(int(0.6 * rate)) / rate
                slow = 0.3 * np.sin(2 * np.pi * 440 * t) * (1 + 0.6 * np.sin(2 * np.pi * 10 * t))
                self.assertLess(m.roughness(col(slow, ch), rate), 0.1)  # a 10 Hz tremolo is movement, not roughness

    def test_roughness_false_reading_two_close_notes_beating(self):
        rate = 44100
        y = tone(rate, 500, 440, 0.3) + tone(rate, 500, 500, 0.3)  # 60 Hz beat
        self.assertGreater(m.roughness(col(y), rate), 0.3)

    def test_main_transient_false_reading_riser_reads_late(self):
        rate = 48000
        y = tone(rate, 400, 600) * np.linspace(0.01, 1, int(0.4 * rate))
        self.assertGreater(m.main_transient_ms(col(y), rate), 100)  # late by design, not a late start

    def test_lag_reads_a_known_shift_exactly(self):
        for rate, ch in CONFIGS:
            for shift in (37, 1102, 1200):
                with self.subTest(rate=rate, ch=ch, shift=shift):
                    x = loaded("clean_hit", rate, ch)
                    y = np.vstack([np.zeros((shift, ch)), x[:-shift]])
                    r = m.lag(x, y, rate, 2400)
                    self.assertTrue(r["clear"])
                    self.assertEqual(r["lag_samples"], shift)
                    self.assertEqual(m.lag(y, x, rate, 2400)["lag_samples"], -shift)

    def test_lag_false_readings_are_not_clear(self):
        rate = 44100
        sine = col(tone(rate, 500))
        self.assertFalse(m.lag(sine, sine, rate, 4410)["clear"])  # periodic: every period correlates
        silent = np.zeros((rate // 2, 1))
        self.assertFalse(m.lag(silent, silent, rate, 4410)["clear"])
        x = loaded("clean_hit", rate, 1)
        self.assertFalse(m.lag(x, -x, rate, 4410)["clear"])  # inverted

    def test_measuring_never_changes_the_audio(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = loaded("hummed", rate, ch)
                before = x.copy()
                m.new_numbers(x, rate)
                m.cue_numbers(x, rate, 200.0, True)
                m.lag(x, x, rate, 100)
                np.testing.assert_array_equal(x, before)

    def test_new_measures_present_in_measure_record(self):
        with tempfile.TemporaryDirectory() as d:
            p = fx.write_wav(Path(d) / "a.wav", fx.make("clean_hit", 44100, 2), 44100)
            rec = m.measure(p)
        for key in ("main_transient_ms", "attack_rise_ms", "attack_share_5ms", "phone_loss_db", "tail_noise",
                    "clicks", "tonality", "roughness", "F-01_onset_ms", "F-12_length"):
            self.assertIn(key, rec)
        self.assertEqual(rec["tool"], "soundbench measure")


class MovedFalseReadingsTest(unittest.TestCase):
    """review.md section 4 false readings the moved measures must keep handling."""

    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_dc_offset_does_not_hide_the_silent_head(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                p = fx.write_wav(self.d / f"dc{rate}{ch}.wav", fx.make("dc_offset", rate, ch), rate)
                self.assertAlmostEqual(m.cue_record(p)["F-01_onset_ms"], fx.CLEAN_HIT_ONSET_MS, delta=0.5)

    def test_f09_trims_trailing_silence(self):
        rate = 48000
        y = tone(rate, 200, 880, 0.5)
        a = fx.write_wav(self.d / "a.wav", col(y), rate)
        b = fx.write_wav(self.d / "b.wav", col(np.concatenate([y, np.zeros(int(0.3 * rate))])), rate)
        self.assertAlmostEqual(m.cue_record(a)["F-09_loudness_rms_dbfs"], m.cue_record(b)["F-09_loudness_rms_dbfs"], delta=0.1)

    def test_f10_does_not_trust_a_note_on_noise(self):
        p = fx.write_wav(self.d / "hiss.wav", fx.make("hiss_lock", 44100, 1), 44100)
        self.assertFalse(m.cue_record(p)["F-10_pitch"]["trusted"])

    def test_f13b_measures_all_channels_not_the_mono_sum(self):
        rate = 48000
        y = tone(rate, 200, 880, 0.4)
        wide = np.stack([y, -y], axis=1)  # the mono sum is silent
        a = fx.write_wav(self.d / "n.wav", np.stack([y, y], axis=1), rate)
        b = fx.write_wav(self.d / "w.wav", wide, rate)
        self.assertLess(m.parity([a, b], "momentary")["spread_lu"], 0.5)

    def test_f08_false_reading_fade_to_silence_reads_zero(self):
        rate = 44100
        y = tone(rate, 500)
        y *= np.concatenate([np.linspace(0, 1, 2000), np.ones(len(y) - 4000), np.linspace(1, 0, 2000)])
        p = fx.write_wav(self.d / "fade.wav", col(y), rate)
        self.assertEqual(m.cue_record(p)["F-08_loop_seam"], 0.0)  # hides any gap: the docs say look at the waveform

    def test_f08_reads_the_bad_seam(self):
        p = fx.write_wav(self.d / "seam.wav", fx.make("bad_seam_bed", 44100, 1), 44100)
        self.assertGreater(m.cue_record(p)["F-08_loop_seam"], 1.0)


if __name__ == "__main__":
    unittest.main()
