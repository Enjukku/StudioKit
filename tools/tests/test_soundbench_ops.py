"""Tests for tools/audio/soundbench/ops.py: the numpy operations (J020 step 3, editor-design.md section 4, 9).

Each operation: the right answer on a fixture with a known answer (often exact by construction, or against
`scipy.signal.sosfreqz` / `scipy.signal.butter` as an independent oracle) AND what it must keep (rate, channels,
onset, attack share, length where it must not change). Parameters and the SC-09 order are checked before audio.
"""

import math
import sys
import unittest
from pathlib import Path

try:
    import numpy as np
    import pyloudnorm  # noqa: F401
    import scipy  # noqa: F401
    import soundfile  # noqa: F401
    from scipy.signal import butter, sosfreqz
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile and pyloudnorm")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench import ops  # noqa: E402
from tools.audio.soundbench import standins  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError  # noqa: E402

CONFIGS = [(r, c) for r in fx.RATES for c in fx.CHANNELS]
CTX = {"kind": "hit", "category": "sfx", "binding": "main_transient",
       "level": {"measure": "F-09", "target": -18.0, "tolerance": 0.5, "must": True}, "key": None, "fade_out_ms": 0.0}


def tone(rate, ms, hz, amp=0.25, ch=1):
    t = np.arange(int(rate * ms / 1000)) / rate
    y = amp * np.sin(2 * np.pi * hz * t)
    return np.repeat(y[:, None], ch, axis=1)


def steady_db(y, rate):
    """RMS level (dB) of the second half (the filter's start-up is over)."""
    h = y[len(y) // 2:]
    return 10 * math.log10(float(np.mean(h ** 2)))


def run(op, x, rate, ctx=None, **given):
    return ops.run(op, x, rate, ops.check_params(op, {"op": op, **given}), ctx or CTX)


def snap(x, rate):
    a = x - x.mean(axis=0)
    return {"onset": m.onset_index(a.mean(axis=1)), "share": m.attack_share(a, rate),
            "mt": m.main_transient_ms(a, rate)}


def peak_hz(y, rate):
    """Frequency of the strongest component, zero-padded FFT with parabolic interpolation (an independent oracle)."""
    v = y[:, 0] * np.hanning(len(y))
    spec = np.abs(np.fft.rfft(v, 8 * len(v)))
    i = int(np.argmax(spec))
    a, b, c = np.log(spec[i - 1:i + 2])
    return (i + 0.5 * (a - c) / (a - 2 * b + c)) * rate / (8 * len(v))


class ParamsAndOrderTest(unittest.TestCase):
    def test_params_are_checked_before_any_audio(self):
        for op, given, why in (("highpass", {}, "required"), ("highpass", {"hz": 5}, "outside"),
                               ("highpass", {"hz": 100, "order": 3}, "not one of"),
                               ("highpass", {"hz": 100, "slope": 12}, "unknown parameter"),
                               ("highpass", {"hz": True}, "finite number"),
                               ("highpass", {"hz": float("nan")}, "finite number"),
                               ("dehum", {"hz": 55}, "not one of"), ("space", {"decay_s": 2.0}, "outside"),
                               ("cut", {}, "exactly one"), ("cut", {"end_ms": 100, "after_sound_ms": 10}, "exactly one"),
                               ("varispeed", {"semitones": 30}, "outside"), ("nosuch", {}, "unknown operation"),
                               ("gate", {"threshold_db": -40, "hold_ms": 2.5e9}, "outside"),
                               ("dehum", {"hz": 50, "harmonics": 2.5}, "whole number")):
            with self.subTest(op=op, given=given):
                with self.assertRaisesRegex(SoundbenchError, why):
                    ops.check_params(op, {"op": op, **given})
        self.assertEqual(ops.check_params("highpass", {"op": "highpass", "hz": 80})["order"], 2)

    def test_eq_boost_over_6_db_needs_a_why(self):
        band = [{"type": "bell", "hz": 3000, "gain_db": 8, "q": 1}]
        with self.assertRaisesRegex(SoundbenchError, "cut before boost"):
            ops.check_params("eq", {"op": "eq", "bands": band})
        ops.check_params("eq", {"op": "eq", "bands": band, "why": "presence for phone speakers"})
        ops.check_params("eq", {"op": "eq", "bands": [{"type": "bell", "hz": 3000, "gain_db": 6, "q": 1}]})
        with self.assertRaisesRegex(SoundbenchError, "unknown field"):
            ops.check_params("eq", {"op": "eq", "bands": [{"type": "notch", "hz": 50, "gain_db": -3}]})

    def test_sc09_order(self):
        ok = [{"op": "dc"}, {"op": "denoise"}, {"op": "varispeed"}, {"op": "highpass"}, {"op": "eq"},
              {"op": "compress"}, {"op": "space"}, {"op": "compress"}, {"op": "transient"}, {"op": "saturate"}]
        self.assertEqual(ops.check_order(ok), ["clean", "clean", "pitch", "eq", "eq", "compress", "add",
                                               "compress_again", "transient", "air"])
        with self.assertRaisesRegex(SoundbenchError, "SC-09"):
            ops.check_order([{"op": "eq"}, {"op": "denoise"}])
        with self.assertRaisesRegex(SoundbenchError, "SC-09"):
            ops.check_order([{"op": "saturate"}, {"op": "compress"}])
        out = ops.check_order([{"op": "eq"}, {"op": "denoise", "why": "the EQ boost raised the hiss"}])
        self.assertIn("out of order", out[1])
        with self.assertRaisesRegex(SoundbenchError, "not a design operation"):
            ops.check_order([{"op": "trim"}])


class FilterTest(unittest.TestCase):
    def test_highpass_and_lowpass_are_3db_down_at_f0_like_butterworth(self):
        for rate in fx.RATES:
            for kind, hz in (("highpass", 200.0), ("lowpass", 3000.0)):
                for order in (2, 4):
                    with self.subTest(rate=rate, kind=kind, order=order):
                        x = tone(rate, 1000, hz)
                        y, _ = run(kind, x, rate, hz=hz, order=order)
                        self.assertAlmostEqual(steady_db(y, rate) - steady_db(x, rate), -3.01, delta=0.05)
                        oracle = butter(order, hz, kind, fs=rate, output="sos")  # independent design
                        for f in (hz / 4, hz * 4):
                            if f < rate / 2:
                                _, h_ours = sosfreqz(ops.pass_sos(kind, hz, rate, order), worN=[f], fs=rate)
                                _, h_ref = sosfreqz(oracle, worN=[f], fs=rate)
                                self.assertAlmostEqual(20 * math.log10(abs(h_ours[0])),
                                                       20 * math.log10(abs(h_ref[0])), delta=0.2)

    def test_eq_bands_give_their_gain_at_f0(self):
        for rate in fx.RATES:
            for band, at, want in (({"type": "bell", "hz": 1000, "gain_db": -6, "q": 2}, 1000, -6.0),
                                   ({"type": "bell", "hz": 2500, "gain_db": 4, "q": 0.7}, 2500, 4.0),
                                   ({"type": "low_shelf", "hz": 200, "gain_db": 5, "q": 0.7071}, 30, 5.0),
                                   ({"type": "high_shelf", "hz": 4000, "gain_db": -5, "q": 0.7071}, 18000, -5.0),
                                   ({"type": "low_shelf", "hz": 300, "gain_db": -6, "q": 0.7071}, 300, -3.0)):
                with self.subTest(rate=rate, band=band):
                    x = tone(rate, 1000, at)
                    y, _ = run("eq", x, rate, bands=[band])
                    self.assertAlmostEqual(steady_db(y, rate) - steady_db(x, rate), want, delta=0.5)
                    _, h = sosfreqz(ops.eq_sos(ops.check_params("eq", {"bands": [band]})["bands"], rate), worN=[at], fs=rate)
                    self.assertAlmostEqual(steady_db(y, rate) - steady_db(x, rate), 20 * math.log10(abs(h[0])), delta=0.05)
                    self.assertEqual(y.shape, x.shape)
        x = tone(48000, 1000, 1000)
        y, _ = run("eq", x, 48000, bands=[{"type": "notch", "hz": 1000, "q": 5}])
        self.assertLess(steady_db(y, 48000) - steady_db(x, 48000), -40)

    def test_filters_keep_onset_and_shape(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch)
                for op, given in (("highpass", {"hz": 80}), ("lowpass", {"hz": 12000}),
                                  ("eq", {"bands": [{"type": "bell", "hz": 330, "gain_db": -3, "q": 1.4}]})):
                    y, _ = run(op, x, rate, **given)
                    self.assertEqual(y.shape, x.shape)
                    self.assertAlmostEqual(snap(y, rate)["onset"], snap(x, rate)["onset"], delta=int(0.0002 * rate) + 1)

    def test_dc_removes_the_offset_exactly(self):
        x = fx.make("dc_offset", 44100, 2)
        y, info = run("dc", x, 44100)
        np.testing.assert_allclose(y.mean(axis=0), 0.0, atol=1e-12)
        np.testing.assert_allclose(y, x - x.mean(axis=0))
        self.assertEqual(len(info["removed_offset"]), 2)

    def test_dehum_removes_the_hum_and_keeps_the_hit(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                t = np.arange(rate) / rate
                hum = (0.05 * sum(np.sin(2 * np.pi * 50 * k * t) / k for k in (1, 2, 3)))[:, None]
                y, info = run("dehum", hum, rate, hz=50, harmonics=4)
                self.assertLess(steady_db(y, rate) - steady_db(hum, rate), -30)
                self.assertEqual(info["notches_hz"], [50, 100, 150, 200])
                x = fx.make("clean_hit", rate, 2)
                y, _ = run("dehum", x, rate, hz=50)
                self.assertAlmostEqual(snap(y, rate)["share"], snap(x, rate)["share"], delta=0.01)


class DynamicsTest(unittest.TestCase):
    def test_compressor_static_curve(self):
        """Steady sine peaks against the static curve; 0.2 dB tolerance: the peak detector ripples between peaks."""
        rate = 48000
        # threshold -20, ratio 4, knee 6, make-up +2, worked by hand: under the knee y = x; in it
        # y = x + (1/4 - 1)(x + 20 + 3)^2 / 12; over it y = -20 + (x + 20) / 4
        # the threshold is relative to the input's peak: a one-sample 0 dBFS click at the very end sets the peak,
        # so threshold -20 dB re peak = -20 dBFS and the hand-worked values hold (the click is not measured)
        for a_db, want in ((-30.0, -28.0), (-23.0, -21.0), (-20.0, -18.5625), (-18.0, -17.5625), (-14.0, -16.5),
                           (-6.0, -14.5)):
            with self.subTest(level=a_db):
                x = tone(rate, 1000, 1000, 10 ** (a_db / 20))
                x[-1] = 1.0
                y, info = run("compress", x, rate, threshold_db=-20, ratio=4, knee_db=6, attack_ms=1, release_ms=200,
                              makeup_db=2)
                self.assertAlmostEqual(info["threshold_dbfs"], -20.0, places=6)
                got = 20 * math.log10(float(np.max(np.abs(y[rate // 2:-1000]))))
                self.assertAlmostEqual(got, want, delta=0.2)
        x = tone(rate, 500, 1000, 10 ** (-40 / 20))  # far under the knee: untouched, makeup only
        x[-1] = 1.0
        y, info = run("compress", x, rate, threshold_db=-20, ratio=4, knee_db=6, makeup_db=0)
        y, x = y[:-1000], x[:-1000]
        np.testing.assert_allclose(y, x)
        self.assertEqual(info["deepest_gain_reduction_db"], 0.0)

    def test_limiter_holds_the_true_peak_ceiling(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch) * 1.8
                ctx = {**CTX, "category": "music"}
                y, info = run("limit", x, rate, ctx, ceiling_dbtp=-1.0)
                self.assertLessEqual(m.true_peak_db(y), -1.0 + 0.01)
                self.assertGreater(info["deepest_gain_reduction_db"], 3)
                quiet = slice(len(x) - int(0.05 * rate), None)  # the decayed tail, far from the peak: untouched
                np.testing.assert_allclose(y[quiet], x[quiet], rtol=1e-9, atol=1e-12)

    def test_sfx_limiting_a_transient_needs_a_why(self):
        x = fx.make("clean_hit", 44100, 2) * 1.8
        with self.assertRaisesRegex(SoundbenchError, "transient"):
            run("limit", x, 44100, CTX)
        y, info = run("limit", x, 44100, {**CTX, "why": "the hit is meant to crunch"})
        self.assertLessEqual(m.true_peak_db(y), -1.0 + 0.01)
        quiet = fx.make("clean_hit", 44100, 2) * 0.3  # nothing to limit: allowed without a why
        y, info = run("limit", quiet, 44100, CTX)
        np.testing.assert_allclose(y, quiet)

    def test_gate_closes_the_tail_and_never_touches_the_attack(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                body = standins.make("hit", rate, ch, int(0.3 * rate)).astype(np.float64)
                tail = np.zeros((int(0.4 * rate), ch))
                x = np.vstack([body, tail]) + 0.0005 * np.random.RandomState(3).standard_normal((len(body) + len(tail), ch))
                y, info = run("gate", x, rate, threshold_db=-40, range_db=60)
                self.assertEqual(snap(y, rate)["onset"], snap(x, rate)["onset"])
                self.assertAlmostEqual(snap(y, rate)["share"], snap(x, rate)["share"], delta=0.002)
                head = slice(int(0.02 * rate), int(0.05 * rate))  # from the stand-in's onset: passed exactly
                np.testing.assert_allclose(y[head], x[head])
                last = slice(len(x) - int(0.1 * rate), None)  # raw RMS: tail_noise would read the DC-removal residue
                self.assertLess(steady_db(y[last], rate), steady_db(x[last], rate) - 55)  # range 60 dB

    def test_transient_shaper(self):
        rate = 48000
        x = fx.make("clean_hit", rate, 2)
        up, _ = run("transient", x, rate, attack_db=6)
        self.assertGreater(snap(up, rate)["share"], 1.2 * snap(x, rate)["share"])
        down, _ = run("transient", x, rate, sustain_db=-6)
        tail = slice(int(0.2 * rate), int(0.4 * rate))
        self.assertLess(steady_db(down[tail], rate), steady_db(x[tail], rate) - 3)
        for y in (up, down):
            self.assertEqual(snap(y, rate)["onset"], snap(x, rate)["onset"])
        steady = tone(rate, 1000, 500)
        y, _ = run("transient", steady, rate, attack_db=6, sustain_db=-6)
        mid = slice(rate // 4, 3 * rate // 4)
        self.assertAlmostEqual(steady_db(y[mid], rate), steady_db(steady[mid], rate), delta=0.1)

    def test_saturate_is_its_formula(self):
        x = tone(44100, 300, 1000, 0.5, 2)
        y, info = run("saturate", x, 44100, drive_db=12, mix=0.5)
        g, pk = 10 ** (12 / 20), float(np.max(np.abs(x)))  # the sampled peak, as the op reads it
        np.testing.assert_allclose(y, 0.5 * x + 0.5 * pk * np.tanh(g * x / pk) / math.tanh(g), rtol=1e-9)
        self.assertLess(info["residual_db"], -10)  # it added harmonics, and says how much
        same, _ = run("saturate", x, 44100, drive_db=0)
        np.testing.assert_array_equal(same, x)


class QuietTakeTest(unittest.TestCase):
    """F3 and F7 on takes modelled on real ElevenLabs takes (LD-c): quiet, starting mid-waveform."""

    def test_saturate_and_compress_act_the_same_on_a_quiet_take(self):
        for rate in fx.RATES:
            for name in fx.REAL_NAMES:
                with self.subTest(rate=rate, name=name):
                    x = fx.make_real(name, rate)
                    k = 0.9 / float(np.max(np.abs(x)))  # the same take normalised
                    for op, given in (("saturate", {"drive_db": 12}), ("compress", {"threshold_db": -20, "ratio": 4})):
                        yq, iq = run(op, x, rate, **given)
                        yn, i_n = run(op, x * k, rate, **given)
                        np.testing.assert_allclose(yq * k, yn, rtol=1e-9, atol=1e-12)
                        if op == "saturate":
                            self.assertEqual(iq["residual_db"], i_n["residual_db"])
                            self.assertLess(iq["residual_db"], -20 + 15)  # it really saturated (not -69 dB)
                        else:
                            self.assertEqual(iq["deepest_gain_reduction_db"], i_n["deepest_gain_reduction_db"])
                            self.assertGreater(iq["deepest_gain_reduction_db"], 3)  # it really compressed

    def test_trim_fades_a_mid_waveform_start(self):
        for rate in fx.RATES:
            for name in fx.REAL_NAMES:
                with self.subTest(rate=rate, name=name):
                    x = fx.make_real(name, rate)
                    a = x - x.mean(axis=0)
                    self.assertIn("start", m.clicks(a, rate)["edges"])
                    y, info = run("trim", x, rate, {**CTX, "binding": "F-01"})
                    self.assertTrue(info["edge_faded"])
                    self.assertAlmostEqual(info["first_sample_db_re_peak"][0], fx.REAL_FIRST_DB_RE_PEAK[name], delta=0.6)
                    self.assertEqual(float(np.max(np.abs(y[0]))), 0.0)
                    self.assertNotIn("start", m.clicks(y - y.mean(axis=0), rate)["edges"])
                    k = int(round(ops.EDGE_FADE_MS * rate / 1000))
                    np.testing.assert_allclose(y[k:], x[len(x) - len(y) + k:])  # only the first 0.5 ms changed

    def test_trim_leaves_a_silent_start_alone(self):
        x = fx.make("late_hit", 44100, 2)
        y, info = run("trim", x, 44100)
        self.assertFalse(info["edge_faded"])


class PitchTest(unittest.TestCase):
    def test_varispeed_changes_pitch_and_length_together(self):
        for rate, ch in CONFIGS:
            for st in (2.0, -3.0, 0.5):
                with self.subTest(rate=rate, ch=ch, st=st):
                    x = tone(rate, 1000, 440, ch=ch)
                    y, info = run("varispeed", x, rate, semitones=st)
                    self.assertAlmostEqual(peak_hz(y, rate), 440 * 2 ** (st / 12), delta=0.2)
                    self.assertAlmostEqual(len(y), len(x) / 2 ** (st / 12), delta=2)
                    self.assertAlmostEqual(info["cents"], 100 * st, delta=0.5)
                    self.assertEqual(y.shape[1], ch)
        x = fx.make("late_hit", 44100, 2)
        y, _ = run("varispeed", x, 44100, semitones=12)  # one octave up: twice as fast, onsets at half the time
        self.assertAlmostEqual(snap(y, 44100)["onset"], snap(x, 44100)["onset"] / 2, delta=3)

    def test_to_key_moves_to_the_nearest_note_of_the_key(self):
        rate = 48000
        x = tone(rate, 800, 450.0, 0.4)  # A4 + 39 cents
        ctx = {**CTX, "key": {"root": "C", "scale": "major"}}
        y, info = run("to_key", x, rate, ctx)
        self.assertEqual(info["to_note"], "A4")
        self.assertAlmostEqual(peak_hz(y, rate), 440.0, delta=0.5)
        self.assertEqual(ops.nearest_in_key(466.16, "C", "major")[0] in ("A4", "B4"), True)
        self.assertEqual(ops.nearest_in_key(466.16, "F", "major")[0], "A#4")  # B flat is in F major

    def test_to_key_is_refused_when_f10_is_untrusted_or_no_key(self):
        hiss = fx.make("hiss_lock", 44100, 1)
        with self.assertRaisesRegex(SoundbenchError, "untrusted"):
            run("to_key", hiss, 44100, {**CTX, "key": {"root": "A", "scale": "major"}})
        with self.assertRaisesRegex(SoundbenchError, "no key"):
            run("to_key", tone(44100, 500, 450), 44100, CTX)


class AddTest(unittest.TestCase):
    def test_echo_repeats_exactly(self):
        imp = np.zeros((4800, 1))
        imp[100] = 1.0
        y, info = run("echo", imp, 48000, delay_ms=10, feedback=0.5, mix=0.4)
        nz = np.nonzero(np.abs(y[:, 0]) > 1e-9)[0]
        self.assertEqual(list(nz[:4]), [100, 580, 1060, 1540])
        np.testing.assert_allclose(y[[100, 580, 1060, 1540], 0], [1.0, 0.4, 0.2, 0.1])
        self.assertEqual(len(y), len(imp) + 480 * info["repeats"])

    def test_space_adds_a_tail_and_keeps_the_dry_sound(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("clean_hit", rate, ch)
                y, info = run("space", x, rate, decay_s=0.6, predelay_ms=15, wet=0.3)
                pre = int((fx.CLEAN_HIT_ONSET_MS + 15) / 1000 * rate)
                np.testing.assert_allclose(y[:pre], x[:pre], atol=1e-12)  # no tail before onset + predelay (FFT round-off only)
                self.assertEqual(snap(y, rate)["onset"], snap(x, rate)["onset"])
                self.assertEqual(len(y) - len(x), info["tail_samples"])
                imp = np.zeros((int(0.05 * rate), ch))
                imp[0] = 1.0
                r, _ = run("space", imp, rate, decay_s=0.6, predelay_ms=0, wet=1.0, damping=0.0)
                env = r[1:, 0] ** 2
                e1 = np.mean(env[int(0.1 * rate):int(0.2 * rate)])
                e2 = np.mean(env[int(0.3 * rate):int(0.4 * rate)])
                rt60 = 60 / (10 * math.log10(e1 / e2) / 0.2)  # dB fall over 0.2 s -> time to fall 60 dB
                self.assertAlmostEqual(rt60, 0.6, delta=0.12)
        with self.assertRaisesRegex(SoundbenchError, "outside"):
            ops.check_params("space", {"decay_s": 3.0})  # a room, not the sound's own tail (J020-D10)


class EditTest(unittest.TestCase):
    def test_trim_binds_hits_to_the_main_transient(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("late_hit", rate, ch)
                y, info = run("trim", x, rate)
                self.assertEqual(info["binding"], "main_transient")
                self.assertAlmostEqual(m.main_transient_ms(y - y.mean(0), rate), ops.TRIM_PREROLL_MS, delta=0.6)
                self.assertAlmostEqual(info["trimmed_ms"], fx.LATE_HIT_ONSET_MS - ops.TRIM_PREROLL_MS, delta=1.0)
                np.testing.assert_allclose(y, x[len(x) - len(y):])  # silent preroll: no fade, samples unchanged

    def test_trim_binds_rising_kinds_to_f01_and_logs_the_lead_in(self):
        rate = 44100
        riser = np.vstack([np.zeros((int(0.08 * rate), 2)), standins.make("riser", rate, 2, int(0.6 * rate))])
        ctx = {**CTX, "kind": "riser", "binding": "F-01"}
        y, info = run("trim", riser.astype(np.float64), rate, ctx)
        self.assertEqual(info["binding"], "F-01")
        f01 = 1000 * m.onset_index((y - y.mean(0)).mean(1)) / rate
        self.assertAlmostEqual(f01, ops.TRIM_PREROLL_MS, delta=0.1)
        mt = m.main_transient_ms(y - y.mean(0), rate)
        self.assertAlmostEqual(info["lead_in_ms"], mt - f01, delta=0.05)
        self.assertGreater(info["lead_in_ms"], 100)  # a riser's main transient is late by design: never trimmed to

    def test_trim_fades_a_non_silent_preroll(self):
        rate = 48000
        x = fx.make("late_hit", rate, 1) + 0.001 * np.random.RandomState(1).standard_normal((len(fx.make("late_hit", rate, 1)), 1))
        y, info = run("trim", x, rate)
        self.assertTrue(info["preroll_faded"])
        self.assertLess(abs(y[0, 0]), 1e-12)

    def test_cut_through_sound_needs_a_fade(self):
        rate = 44100
        x = fx.make("wrong_chime", rate, 2)
        with self.assertRaisesRegex(SoundbenchError, "fade-out"):
            run("cut", x, rate, end_ms=200)
        y, info = run("cut", x, rate, {**CTX, "fade_out_ms": 10}, end_ms=200)
        self.assertEqual(len(y), int(0.2 * rate))
        self.assertTrue(info["through_sound"])
        y, info = run("cut", x, rate, after_sound_ms=20)
        end, _ = m.sound_end((x - x.mean(0)).mean(1), rate)
        self.assertEqual(len(y), min(len(x), end + int(0.02 * rate)))

    def test_fade_ramps_and_guards_the_attack(self):
        rate = 48000
        x = np.ones((4800, 2)) * 0.5
        y, _ = run("fade", x, rate, out_ms=10, curve="linear")
        np.testing.assert_allclose(y[-480:, 0], 0.5 * np.linspace(0, 1, 480, endpoint=False)[::-1])
        np.testing.assert_array_equal(y[:-480], x[:-480])
        hit = fx.make("clean_hit", rate, 2)
        with self.assertRaisesRegex(SoundbenchError, "softens the attack"):
            run("fade", hit, rate, in_ms=30)
        run("fade", hit, rate, {**CTX, "why": "a soft entry for this hit"}, in_ms=30)
        run("fade", hit, rate, in_ms=5)  # ends before the onset at 20 ms: allowed

    def test_mono(self):
        x = fx.make("clean_hit", 44100, 2)
        y, info = run("mono", x, 44100)
        np.testing.assert_allclose(y[:, 0], x.mean(axis=1))
        self.assertIsNotNone(info["mono_drop_db"])

    def test_loudness_lands_on_its_measure(self):
        for rate, ch in CONFIGS:
            for measure_name, target, name in (("F-09", -18.0, "clean_hit"), ("F-13a", -20.0, "wrong_chime"),
                                               ("LUFS-I", -16.0, "wrong_chime")):
                with self.subTest(rate=rate, ch=ch, measure=measure_name):
                    x = fx.make(name, rate, ch) * 0.3
                    ctx = {**CTX, "level": {"measure": measure_name, "target": target, "tolerance": 0.5, "must": True}}
                    y, info = run("loudness", x, rate, ctx)
                    self.assertAlmostEqual(m.level_db(y, rate, measure_name), target, delta=ops.LOUDNESS_MAX_ERROR_DB)
                    g = y[np.argmax(np.abs(x[:, 0])), 0] / x[np.argmax(np.abs(x[:, 0])), 0]
                    np.testing.assert_allclose(y, g * x)  # a gain, nothing else
        with self.assertRaisesRegex(SoundbenchError, "0.4 s"):
            m.level_db(fx.make("clean_hit", 44100, 1)[:8000], 44100, "LUFS-I")

    def test_f13a_level_equals_the_family_parity_value(self):
        import tempfile

        rate = 48000
        x = fx.make("wrong_chime", rate, 2)
        with tempfile.TemporaryDirectory() as d:
            a = fx.write_wav(Path(d) / "a.wav", x, rate)
            b = fx.write_wav(Path(d) / "b.wav", fx.make("clean_hit", rate, 2), rate)
            fam = m.parity([a, b], "integrated")["lufs"][0]  # padded to the longer file + 0.4 s
        self.assertAlmostEqual(m.level_db(x.astype(np.float32).astype(np.float64), rate, "F-13a"), fam, delta=0.01)

    def test_peak_is_gain_only(self):
        for rate in fx.RATES:
            x = fx.make("clean_hit", rate, 2) * 1.5
            y, info = run("peak", x, rate, ceiling_dbtp=-1.0, margin_db=0.5)
            self.assertAlmostEqual(m.true_peak_db(y), -1.5, delta=0.01)
            i = int(np.argmax(np.abs(x[:, 0])))
            np.testing.assert_allclose(y, x * (y[i, 0] / x[i, 0]), rtol=1e-12)  # one gain for every sample
            self.assertAlmostEqual(20 * math.log10(y[i, 0] / x[i, 0]), info["gain_db"], delta=0.001)
            low = fx.make("clean_hit", rate, 2) * 0.1
            y, info = run("peak", low, rate)
            np.testing.assert_array_equal(y, low)
            self.assertEqual(info["gain_db"], 0.0)


if __name__ == "__main__":
    unittest.main()
