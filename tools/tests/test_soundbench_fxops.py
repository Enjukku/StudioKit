"""Tests for tools/audio/soundbench/fxops.py and the step-4 adapter modes (context, stand-ins, event timing).

Each ffmpeg operation: it does its job AND keeps what it must (rate, channels, length or its declared change, per
channel timing, attack share, main transient). The review-1 probe cases are here: rubberband's smear on a 400 ms hit
and adeclick on a clean hit are refused. Tests that run ffmpeg skip with a reason when it is missing.
"""

import math
import sys
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
from tools.audio.soundbench import fxops, ops, standins  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
needs_ffmpeg = unittest.skipUnless(FOUND, "ffmpeg not found (SOUNDBENCH_FFMPEG, PATH, WinGet folder): skipped")


def run(op, x, rate, kind, **given):
    return fxops.run(op, x, rate, ops.check_params(op, {"op": op, **given}), {"kind": kind})


def noisy(x, level=0.003, seed=1):
    return x + level * np.random.RandomState(seed).standard_normal(x.shape)


def bed(rate, ch=2, s=1.0):
    return standins.make("bed", rate, ch, int(s * rate)).astype(np.float64)


def tonal_bed(rate, s=1.0):
    """A sustained tone mixture (periodic: timed on the probe and the stand-in)."""
    t = np.arange(int(s * rate)) / rate
    y = 0.2 * np.sin(2 * np.pi * 440 * t) + 0.1 * np.sin(2 * np.pi * 660 * t)
    return np.stack([y, 0.6 * y], axis=1)


def peak_hz(y, rate):
    v = y[:, 0] * np.hanning(len(y))
    spec = np.abs(np.fft.rfft(v, 8 * len(v)))
    i = int(np.argmax(spec))
    a, b, c = np.log(spec[i - 1:i + 2])
    return (i + 0.5 * (a - c) / (a - 2 * b + c)) * rate / (8 * len(v))


def snap(x, rate):
    a = x - x.mean(axis=0)
    return {"onset": m.onset_index(a.mean(axis=1)), "share": m.attack_share(a, rate),
            "mt": m.main_transient_ms(a, rate)}


class StandinTest(unittest.TestCase):
    def test_standins_are_non_periodic_unequal_and_timeable(self):
        for cls in standins.CLASSES:
            for rate in fx.RATES:
                with self.subTest(cls=cls, rate=rate):
                    s = standins.make(cls, rate, 2, int(0.6 * rate)).astype(np.float64)
                    self.assertEqual(s.shape, (int(0.6 * rate), 2))
                    self.assertGreater(np.sum(s[:, 0] ** 2), 1.5 * np.sum(s[:, 1] ** 2))  # a swap changes the order
                    for c in range(2):
                        r = m.lag(s[:, c], s[:, c], rate, int(0.05 * rate))
                        self.assertTrue(r["clear"], (cls, r))  # never periodic: its own lag is clear
        self.assertEqual(standins.make("loop_bed", 44100, 1, 1000).shape, (1000, 1))  # a kind name maps to its class
        with self.assertRaises(SoundbenchError):
            standins.make("nosuch", 44100, 1, 1000)


@needs_ffmpeg
class LatencyTableTest(unittest.TestCase):
    def test_measured_latencies(self):
        self.assertEqual(sbf.KNOWN_LATENCY["afftdn"], {44100: 1102, 48000: 1200})
        self.assertEqual(sbf.KNOWN_LATENCY["adeclick"], {44100: 0, 48000: 0})
        self.assertEqual(sbf.KNOWN_LATENCY["chorus"], {44100: 0, 48000: 0})

    def test_context_padding_keeps_a_beds_start(self):
        """Probe 4: without context adeclick dropped a bed's first 10 ms from 0.170 to 0.025 RMS."""
        for rate in fx.RATES:
            x = fx.make("bad_seam_bed", rate, 2).astype(np.float32)
            first = slice(0, int(0.01 * rate))
            res = sbf.run_filter(x, rate, "adeclick", context="wrap", standin_kind="loop_bed")
            ratio = np.sqrt(np.mean(res.audio[first] ** 2) / np.mean(x[first] ** 2))
            self.assertGreater(float(ratio), 0.9)
            res = sbf.run_filter(x, rate, "adeclick", standin_kind="loop_bed")  # no context: the ramp shows
            ratio = np.sqrt(np.mean(res.audio[first] ** 2) / np.mean(x[first] ** 2))
            self.assertLess(float(ratio), 0.5)


@needs_ffmpeg
class DenoiseTest(unittest.TestCase):
    def test_denoise_lowers_the_floor_and_keeps_the_hit(self):
        for rate in fx.RATES:
            for ch in fx.CHANNELS:
                with self.subTest(rate=rate, ch=ch):
                    x = noisy(fx.make("clean_hit", rate, ch))
                    y, info = run("denoise", x, rate, "hit", nr_db=20)
                    self.assertEqual(y.shape, x.shape)
                    tail = slice(len(x) - int(0.06 * rate), None)
                    self.assertLess(np.sqrt(np.mean(y[tail] ** 2)), 0.5 * np.sqrt(np.mean(x[tail] ** 2)))
                    for c in range(ch):
                        self.assertEqual(m.lag(x[:, c], y[:, c], rate, int(0.06 * rate))["lag_samples"], 0)
                    self.assertEqual(snap(y, rate)["onset"], snap(x, rate)["onset"])
                    self.assertAlmostEqual(snap(y, rate)["share"], snap(x, rate)["share"], delta=0.01)
                    self.assertEqual(info["timing"]["channel_lags_samples"], [sbf.known_latency("afftdn", rate)] * ch)

    def test_denoise_on_periodic_audio_is_timed_on_probe_and_standin(self):
        y, info = run("denoise", fx.make("wrong_chime", 48000, 2), 48000, "chime")
        self.assertTrue(info["timing"]["timing_source"].startswith("probe and chime stand-in"))
        self.assertEqual(info["timing"]["standin_lags_samples"], [1200, 1200])

    def test_an_unmeasured_rate_is_refused(self):
        x = noisy(fx.make("clean_hit", 44100, 1))
        from scipy.signal import resample_poly

        x32 = resample_poly(x, 320, 441, axis=0)  # 32 kHz
        with self.assertRaisesRegex(SoundbenchError, "never measured"):
            run("denoise", x32, 32000, "hit")


@needs_ffmpeg
class DeclickTest(unittest.TestCase):
    def test_declick_removes_a_click_from_a_bed(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = tonal_bed(rate)  # a click hides in a noise bed (the clicks measure's own false reading)
                at = int(0.5 * rate)
                x[at:at + 3] += 0.4
                self.assertEqual(m.clicks(x - x.mean(0), rate)["count"], 1)
                y, info = run("declick", x, rate, "loop_bed")
                self.assertEqual(m.clicks(y - y.mean(0), rate)["count"], 0)
                self.assertEqual(y.shape, x.shape)
                self.assertEqual(info["timing"]["context"], "wrap")
                for c in range(2):
                    self.assertEqual(m.lag(x[:, c], y[:, c], rate, int(0.05 * rate))["lag_samples"], 0)

    def test_declick_on_a_clean_hit_is_refused(self):
        """review-1 #6: on a clean hit adeclick cut the 5 ms attack share (here 0.137 -> 0.06)."""
        x = fx.make("clean_hit", 44100, 2)
        with self.assertRaisesRegex(SoundbenchError, "sustained sounds and loops only"):
            run("declick", x, 44100, "hit")
        with self.assertRaisesRegex(SoundbenchError, "attack share"):
            run("declick", x, 44100, "sustained")  # labelled sustained: the guard still refuses it


@needs_ffmpeg
class RubberbandTest(unittest.TestCase):
    def test_pitch_shifts_a_sustained_tone_and_keeps_its_length(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = tonal_bed(rate)
                y, info = run("pitch", x, rate, "sustained", semitones=2)
                self.assertEqual(y.shape, x.shape)
                self.assertAlmostEqual(peak_hz(y[rate // 4:3 * rate // 4], rate), 440 * 2 ** (2 / 12), delta=1.0)
                self.assertLessEqual(info["timing"]["worst_event_shift_ms"], fxops.PITCH_EVENT_BASE_MS + 2 * fxops.PITCH_EVENT_PER_ST_MS)
                self.assertEqual(info["timing"]["timing_source"], "events")

    def test_stretch_changes_the_length_by_the_ratio_and_keeps_the_pitch(self):
        for rate in fx.RATES:
            for ratio in (1.25, 0.8):
                with self.subTest(rate=rate, ratio=ratio):
                    x = tonal_bed(rate)
                    y, info = run("stretch", x, rate, "loop_bed", ratio=ratio)
                    self.assertEqual(len(y), int(round(len(x) * ratio)))
                    self.assertAlmostEqual(peak_hz(y[len(y) // 4:3 * len(y) // 4], rate), 440.0, delta=1.0)
                    self.assertLessEqual(info["timing"]["worst_event_shift_ms"],
                                         fxops.STRETCH_EVENT_BASE_MS + fxops.STRETCH_EVENT_PER_UNIT_MS * abs(ratio - 1))

    def test_percussive_kinds_are_refused(self):
        for op, given in (("pitch", {"semitones": 2}), ("stretch", {"ratio": 1.2})):
            with self.assertRaisesRegex(SoundbenchError, "varispeed"):
                run(op, fx.make("clean_hit", 44100, 2), 44100, "hit", **given)

    def test_rubberband_smear_on_a_400ms_hit_is_refused(self):
        """review-1 #2: on a 400 ms hit rubberband moved the onset early and cut the attack share. Labelled
        sustained (so the kind rule cannot help), the guard refuses it at both rates."""
        for rate in fx.RATES:
            for st in (2, -2):
                with self.subTest(rate=rate, st=st):
                    x = fx.make("clean_hit", rate, 2)
                    with self.assertRaisesRegex(SoundbenchError, "attack share|main transient|attack rise|events moved"):
                        run("pitch", x, rate, "sustained", semitones=st)

    def test_event_timing_refuses_a_wrong_scale(self):
        x = tonal_bed(44100).astype(np.float32)
        with self.assertRaisesRegex(SoundbenchError, "expected"):
            sbf.run_filter_events(x, 44100, "rubberband=tempo=0.8", time_scale=1.0, tolerance_ms=12,
                                  standin_kind="sustained")
        with self.assertRaisesRegex(SoundbenchError, "events moved"):
            sbf.run_filter_events(x, 44100, "adelay=20|20,atrim=end_sample=52920", time_scale=1.0, tolerance_ms=6,
                                  standin_kind="sustained")


@needs_ffmpeg
class ChorusTest(unittest.TestCase):
    def test_chorus_adds_movement_keeps_the_attack_and_declares_its_tail(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make("clean_hit", rate, 2)
                y, info = run("chorus", x, rate, "hit", delay_ms=40, depth_ms=2)
                self.assertGreater(len(y), len(x))
                self.assertLessEqual(len(y) - len(x), int(0.05 * rate))  # delay + depth, at most
                self.assertEqual(snap(y, rate)["onset"], snap(x, rate)["onset"])
                self.assertEqual(info["timing"]["dry_path_timing"]["channel_lags_samples"], [0, 0])  # F5: dry path
                self.assertTrue(info["timing"]["timing_source"].startswith("probe and"))  # the full graph: probe
                self.assertEqual(info["guard"]["attack_checks"], "not for chorus")
                late = slice(int(0.065 * rate), int(0.1 * rate))  # the delayed copy arrives after 40 ms
                self.assertGreater(np.sum((y[late] - 0.7 * x[late]) ** 2), 1e-4)


@needs_ffmpeg
class GuardTest(unittest.TestCase):
    @staticmethod
    def snapd(share=0.2, mt=20.0, rise=1.0, f09=-20.0, ch=(-20.0, -21.0), floor=-70.0):
        return {"attack_share": share, "main_transient_ms": mt, "attack_rise_ms": rise, "f09_db": f09,
                "channel_db": list(ch), "floor_dbfs": floor}

    def test_guard_limits_in_both_directions(self):
        s_ = self.snapd
        fxops._guard("x", s_(), s_(share=0.17, mt=20.9, rise=2.9, f09=-21.4, ch=(-21.0, -22.9)), 6.0)
        for after, why in ((s_(share=0.15), "attack share"), (s_(share=0.26), "attack share"),  # down and up
                           (s_(mt=21.2), "main transient"), (s_(mt=18.8), "main transient"),
                           (s_(rise=3.2), "attack rise"), (s_(rise=-1.2), "attack rise"),  # smeared and eaten
                           (s_(f09=-21.6), "F-09"), (s_(f09=-18.4), "F-09"),
                           (s_(ch=(-20.0, -22.2)), "balance"), (s_(ch=(-20.0, -19.8)), "balance")):
            with self.subTest(why=why, after=after):
                with self.assertRaisesRegex(SoundbenchError, why):
                    fxops._guard("x", s_(), after, 6.0)
        calm = s_(share=0.005, mt=0.5, rise=100.0)  # no attack to protect: only the filter's own tolerance
        fxops._guard("x", calm, s_(share=0.001, mt=5.5, rise=150.0), 6.0)
        with self.assertRaisesRegex(SoundbenchError, "main transient"):
            fxops._guard("x", calm, s_(share=0.001, mt=7.0, rise=100.0), 6.0)
        # chorus: level, attack shape and transient are its job; only the balance (2 dB) is guarded here
        fxops._guard("chorus", s_(), s_(share=0.4, mt=25.0, rise=9.0, f09=-15.0, ch=(-20.0, -22.5)), 1.0)
        with self.assertRaisesRegex(SoundbenchError, "balance"):
            fxops._guard("chorus", s_(), s_(ch=(-20.0, -23.2)), 1.0)
        self.assertTrue(math.isclose(fxops.SHARE_KEEP, 0.8))

    def test_length_guard_catches_an_eaten_tail(self):
        rate = 44100
        x = fx.make("wrong_chime", rate, 2)
        y = x.copy()
        y[int(0.2 * rate):] *= 0.001  # the tail is gone, the attack untouched
        with self.assertRaisesRegex(SoundbenchError, "shrank"):
            fxops._guard("x", fxops._snap(x, rate), fxops._snap(x, rate), 1.0, 1.0, x, y, rate)
        fxops._guard("x", fxops._snap(x, rate), fxops._snap(x, rate), 1.0, 1.0, x, x.copy(), rate)

    def test_roughness_guard(self):
        rate = 48000
        t = np.arange(rate) / rate
        x = (0.3 * np.sin(2 * np.pi * 440 * t))[:, None]
        fxops._rough_guard("x", x, x.copy(), rate)
        fluttered = x * (1 + 0.2 * np.sin(2 * np.pi * 70 * t))[:, None]  # 70 Hz movement: roughness about 0.2
        with self.assertRaisesRegex(SoundbenchError, "flutter"):
            fxops._rough_guard("x", x, fluttered, rate)

    def test_pitch_accuracy_guard(self):
        rate = 48000
        t = np.arange(rate) / rate
        x = (0.3 * np.sin(2 * np.pi * 440 * t))[:, None]
        up = (0.3 * np.sin(2 * np.pi * 440 * 2 ** (2 / 12) * t))[:, None]
        self.assertLess(abs(fxops._pitch_guard("x", x, up, rate, 200.0)), 0.5)
        off = (0.3 * np.sin(2 * np.pi * 440 * 2 ** (2.1 / 12) * t))[:, None]  # 10 cents sharp
        with self.assertRaisesRegex(SoundbenchError, "cents"):
            fxops._pitch_guard("x", x, off, rate, 200.0)
        hiss = fx.make("hiss_lock", rate, 1)
        self.assertIsNone(fxops._pitch_guard("x", hiss, hiss, rate, 0.0))  # no trusted note: not checked

    def test_crisp_rubberband_flutter_is_refused(self):
        """Probe 6: rubberband's default crisp mode put amplitude modulation on a steady tone (roughness 0.08 at
        44.1 kHz with only -0.5 cents of pitch error): the roughness guard must refuse it."""
        rate = 44100
        t = np.arange(rate) / rate
        x = np.stack([0.3 * np.sin(2 * np.pi * 440 * t), 0.2 * np.sin(2 * np.pi * 440 * t)], axis=1)
        old = fxops.RUBBERBAND_MODE
        try:
            fxops.RUBBERBAND_MODE = "transients=crisp"
            with self.assertRaisesRegex(SoundbenchError, "flutter|cents"):
                run("pitch", x, rate, "sustained", semitones=2)
        finally:
            fxops.RUBBERBAND_MODE = old

    def test_a_rubberband_loss_over_6_db_is_refused(self):
        """Smooth rubberband loses 0.4-4.3 dB (restored by gain); more than 6 dB is damage, not a gain to restore."""
        real = sbf.run_filter_events

        def quieter(*a, **k):
            res = real(*a, **k)
            res.audio = res.audio * 0.4  # -8 dB on top of rubberband's own loss
            return res

        with mock.patch.object(sbf, "run_filter_events", quieter):
            with self.assertRaisesRegex(SoundbenchError, "lost"):
                run("pitch", tonal_bed(44100), 44100, "sustained", semitones=1)
        y, info = run("pitch", tonal_bed(44100), 44100, "sustained", semitones=1)
        self.assertLess(info["level_restored_db"], fxops.RUBBERBAND_MAX_LOSS_DB)

    def test_pitch_events_moved_past_the_tolerance_are_refused(self):
        """A 2-semitone shift may move events 1 + 3 x 2 = 7 ms; 15 ms more delay on top must be refused."""
        rate = 44100
        x = tonal_bed(rate)
        body = len(x) + 2 * int(round(sbf.CONTEXT_MS * rate / 1000))
        old = fxops.RUBBERBAND_MODE
        try:
            fxops.RUBBERBAND_MODE = f"transients=smooth,adelay=15|15,atrim=end_sample={body}"
            with self.assertRaisesRegex(SoundbenchError, "events moved"):
                run("pitch", x, rate, "sustained", semitones=2)
        finally:
            fxops.RUBBERBAND_MODE = old


@needs_ffmpeg
class RealisticTakeTest(unittest.TestCase):
    """LD-c: quiet takes modelled on real ElevenLabs takes (peaks -24 to -36 dBFS, a mid-waveform start, 480 ms,
    uneven channels). F1: the reviewer's settings on a -36 dBFS take must be refused, by the nf check and, with
    that check off, by the damage guards."""

    def test_f1_denoise_with_nf_over_the_floor_is_refused(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make_real("quiet_hit", rate)
                with self.assertRaisesRegex(SoundbenchError, "above the take's measured tail floor"):
                    run("denoise", x, rate, "hit", nr_db=40, nf_db=-20)

    def test_f1_the_damage_guards_refuse_it_without_the_nf_check(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make_real("quiet_hit", rate)
                with mock.patch.object(fxops, "NF_MARGIN_DB", 200.0):
                    with self.assertRaisesRegex(SoundbenchError, "F-09|shrank|attack share|balance|transient|rise"):
                        run("denoise", x, rate, "hit", nr_db=40, nf_db=-20)

    def test_denoise_with_nf_at_the_floor_keeps_a_quiet_take(self):
        """A hit and a note keep their numbers. (A noise-only whoosh is left out: afftdn cannot tell its sound from
        noise, and on its swell the main transient moved 17.7 ms at 44.1 kHz: refused, as it should be.)"""
        for rate in fx.RATES:
            for name, kind in (("quiet_hit", "hit"), ("soft_note", "chime")):
                with self.subTest(rate=rate, name=name):
                    x = fx.make_real(name, rate)
                    y, info = run("denoise", x, rate, kind)
                    self.assertTrue(info["nf_used"]["auto"])
                    self.assertAlmostEqual(info["nf_used"]["nf_db"], info["nf_used"]["floor_dbfs"], delta=0.1)
                    g = info["guard"]
                    self.assertLessEqual(abs(g["f09_db"][1] - g["f09_db"][0]), fxops.LEVEL_CHANGE_DB)
                    self.assertLessEqual(abs(g["balance_moved_db"]), fxops.BALANCE_MOVE_DB)

    def test_hiss_removal_on_a_normal_take_still_works(self):
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = noisy(fx.make("clean_hit", rate, 2), 0.003)
                y, info = run("denoise", x, rate, "hit", nr_db=20, nf_db=-50)
                tail = slice(len(x) - int(0.06 * rate), None)
                self.assertLess(np.sqrt(np.mean(y[tail] ** 2)), 0.5 * np.sqrt(np.mean(x[tail] ** 2)))

    def test_denoise_refuses_a_silent_tail_and_a_floor_under_afftdn(self):
        x = np.repeat(fx.make("clean_hit", 44100, 1), 2, axis=1)  # digital silence after the hit (no fixture noise)
        with self.assertRaisesRegex(SoundbenchError, "digital silence|under afftdn"):
            run("denoise", x, 44100, "hit")
        quiet = noisy(x, 0.00002)  # floor about -94 dBFS
        with self.assertRaisesRegex(SoundbenchError, "under afftdn"):
            run("denoise", quiet, 44100, "hit")

    def test_chorus_on_a_low_thump_is_timed_on_its_dry_path(self):
        """F5: on a 60 Hz thump the wet copy moves the audio's correlation peak 18-30 samples (as on the real whoosh-2:
        11 samples); timing the audio on the dry path (decay 0) and the full graph on the probe gives the true 0."""
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make("bass_thump", rate, 2)
                y, info = run("chorus", x, rate, "impact")
                self.assertEqual(info["timing"]["dry_path_timing"]["channel_lags_samples"], [0, 0])
                self.assertGreater(len(y), len(x))

    def test_chorus_on_a_quiet_whoosh(self):
        """F5: real whooshes were refused (the wet copy moved the correlation peak 11 samples)."""
        for rate in fx.RATES:
            with self.subTest(rate=rate):
                x = fx.make_real("quiet_whoosh", rate)
                y, info = run("chorus", x, rate, "whoosh")
                self.assertGreater(len(y), len(x))
                self.assertEqual(info["timing"]["dry_path_timing"]["channel_lags_samples"], [0, 0])


@needs_ffmpeg
class StretchRangeTest(unittest.TestCase):
    """F4: the accepted range stops where the measured shift reaches 10 ms (0.8-1.25); the tolerance is
    2 ms + 40 ms x |ratio - 1|."""

    def test_the_range_ends_just_inside_and_just_outside(self):
        for ratio in (0.79, 1.26):
            with self.assertRaisesRegex(SoundbenchError, "outside"):
                ops.check_params("stretch", {"ratio": ratio})
        for rate in fx.RATES:
            for ratio in (0.8, 1.25):
                with self.subTest(rate=rate, ratio=ratio):
                    y, info = run("stretch", tonal_bed(rate), rate, "loop_bed", ratio=ratio)
                    self.assertLessEqual(info["timing"]["worst_event_shift_ms"], info["timing"]["event_tolerance_ms"])
                    self.assertAlmostEqual(info["timing"]["event_tolerance_ms"], 2 + 40 * abs(ratio - 1), places=6)

    def test_events_past_the_scaled_tolerance_are_refused(self):
        for rate in fx.RATES:
            for ratio, extra_ms in ((0.8, 5), (1.25, 25)):  # 0.8 moves events late, 1.25 early (probe sweep)
                with self.subTest(rate=rate, ratio=ratio):
                    x = tonal_bed(rate)
                    body = len(x) + 2 * int(round(sbf.CONTEXT_MS * rate / 1000))
                    old = fxops.RUBBERBAND_MODE
                    try:
                        fxops.RUBBERBAND_MODE = (f"transients=smooth,adelay={extra_ms}|{extra_ms},"
                                                 f"atrim=end_sample={int(round(body * ratio))}")
                        with self.assertRaisesRegex(SoundbenchError, "events moved"):
                            run("stretch", x, rate, "loop_bed", ratio=ratio)
                    finally:
                        fxops.RUBBERBAND_MODE = old


@needs_ffmpeg
class ChannelsAlikeTest(unittest.TestCase):
    def test_near_mono_channels_are_checked_by_level_only(self):
        """Real takes are often near-mono: chorus modulation flipped own-vs-cross shape matches on 3 of 62."""
        rate = 44100
        base = fx.make_real("quiet_whoosh", rate)
        x = np.stack([base[:, 0], 0.98 * base[:, 0]], axis=1)
        y = x.copy()
        y[:, 1] = 0.9 * x[:, 0] + 0.1 * np.roll(x[:, 0], 50)  # its own channel shifted a little
        self.assertIn("level only", sbf.check_channels(x, y, "test"))
        rs = np.random.RandomState(4)
        x2 = np.stack([base[:, 0], 0.98 * base[:, 0] + 0.33 * np.std(base[:, 0]) * rs.standard_normal(len(base))], axis=1)
        y2 = np.stack([x2[:, 0], x2[:, 0]], axis=1)  # channel 1 now matches input 0 (0.95) better than its own
        self.assertIn("level only", sbf.check_channels(x2, y2, "test"))  # shape would refuse it wrongly
        swapped = np.stack([x[:, 1] * 0.5, x[:, 0]], axis=1)  # unequal levels: the swap still shows
        with self.assertRaisesRegex(SoundbenchError, "level order"):
            sbf.check_channels(np.stack([x[:, 0], 0.5 * x[:, 1]], axis=1), swapped, "test")


if __name__ == "__main__":
    unittest.main()
