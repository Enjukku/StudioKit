"""Tests for soundbench layers, loops and variants (J020 step 6, editor-design.md section 4).

Cue folders are built in temp folders with stand-in take files whose intake record the test writes (no ffmpeg); the
audio is the realistic fixtures (`fixtures.make_real`, quiet, mid-waveform starts, unequal stereo) and long beds of 2-30 s
(`fixtures.make_bed`: steady and swelling noise, a steady tone, a tonal pad, and a bed spliced from realistic takes
slowed x4). Oracles: sample positions computed from the recipe (offset x rate), the source samples the wrap must hold,
the length ratio a pitch change in cents must give, the card's own limits, and the click detector of `measures` run on
the file rotated so the seam sits inside it. The planted-fault test at the end shows each named fault is caught.
"""

import copy
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import matplotlib  # noqa: F401
    import numpy as np
    import pyloudnorm  # noqa: F401
    import scipy  # noqa: F401
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile, pyloudnorm and matplotlib")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import assemble, intake, ops, render  # noqa: E402
from tools.audio.soundbench import rank as rank_mod  # noqa: E402
from tools.audio.soundbench import export as exportmod  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, audio_sha256, file_sha256, read_float32  # noqa: E402

R = 44100
STEP = 2.0 ** -23  # one 24-bit step: the FLAC read-back tolerance
PLAYBACK = {"space": "2D", "takes_room": False, "ducks": None}


def card(cue: str, kind: str = "hit", **extra) -> dict:
    c = {"cue": cue, "kind": kind, "category": "sfx", "tier": "minor",
         "level": {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": False}, "targets": {},
         "playback": PLAYBACK}
    c.update(extra)
    return c


def add_take(cue_dir: Path, rel: str, x: np.ndarray, rate: int) -> None:
    """A stand-in take file, its master WAV and a sidecar with the intake record (as test_soundbench_render does)."""
    take = cue_dir / rel
    take.parent.mkdir(parents=True, exist_ok=True)
    take.write_bytes(b"stand-in take bytes for " + rel.encode())
    master = intake.master_path(take)
    fx.write_wav(master, x, rate)
    y, _ = read_float32(master)
    side = {"prompt": "test", "intake": {"take_sha256": file_sha256(take), "master_audio_sha256": audio_sha256(y),
                                         "rate": rate, "decoder": "test (no decode)"}}
    take.with_suffix(".json").write_text(json.dumps(side), encoding="utf-8")


def make_cue(root: Path, c: dict, recipe: dict, takes: dict) -> Path:
    """takes: relative path -> (audio, rate)."""
    cue = root / c["cue"]
    cue.mkdir(parents=True, exist_ok=True)
    for rel, (x, rate) in takes.items():
        add_take(cue, rel, x, rate)
    (cue / "card.json").write_text(json.dumps(c), encoding="utf-8")
    (cue / "recipe.json").write_text(json.dumps({"cue": c["cue"], **recipe}), encoding="utf-8")
    return cue


def take(cue: str, n: int = 1) -> str:
    return f"takes/{cue}.r1.t{n}.mp3"


def delivered(cue_dir: Path, name: str | None = None) -> np.ndarray:
    return read_float32(cue_dir / "out" / f"{name or cue_dir.name}.flac")[0].astype(np.float64)


def master(cue_dir: Path, rel: str) -> np.ndarray:
    return read_float32(intake.master_path(cue_dir / rel))[0].astype(np.float64)


def rows_by(doc: dict) -> dict:
    return {r["target"]: r for r in doc["targets"] + doc["form_checks"]}


def f08(y: np.ndarray) -> float:
    """F-08 as review.md section 4 defines it: |last - first| / the 95th percentile of the sample steps (mono)."""
    a = y - y.mean(axis=0)
    mono = a.mean(axis=1)
    return abs(float(mono[-1] - mono[0])) / float(np.percentile(np.abs(np.diff(mono)), 95))


def click(n: int, at: int, amp: float, rate: int = R, width_ms: float = 0.3) -> np.ndarray:
    """A smooth click (Gaussian, about 0.3 ms) peaking exactly at sample `at`."""
    t = (np.arange(n) - at) / rate
    return amp * np.exp(-0.5 * (t / (width_ms / 1000)) ** 2)


# --------------------------------------------------------------------------------------------- layers

class LayerTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_offsets_land_to_the_sample_on_each_channel_in_order(self):
        for rate in (44100, 48000):
            with self.subTest(rate=rate):
                cue = f"SFX-L-OFF{rate}"
                a = np.zeros((2000, 2))
                a[100, 0], a[160, 1] = 0.3, -0.2  # unequal channels: a swap or a shift changes a number
                b = np.zeros((900, 1))
                b[50, 0] = 0.25
                rec = {"layers": [{"name": "body", "take": take(cue, 1), "design": [], "offset_ms": 0},
                                  {"name": "tick", "take": take(cue, 2), "design": [], "offset_ms": 12.5,
                                   "gain_db": -6.0}],
                       "design": [], "edit": []}
                d = make_cue(self.d, card(cue), rec, {take(cue, 1): (a, rate), take(cue, 2): (b, rate)})
                doc, code = render.render(d)
                off = int(round(12.5 * rate / 1000))  # the recipe's offset in samples: 551 at 44.1 kHz, 600 at 48
                y = delivered(d)
                self.assertEqual(y.shape, (max(2000, off + 900), 2))
                want = np.zeros_like(y)
                want[100, 0], want[160, 1] = 0.3, -0.2
                want[off + 50, :] = 0.25 * 10 ** (-6 / 20)  # the mono layer on both channels
                np.testing.assert_allclose(y, want, atol=2 * STEP)
                self.assertEqual([e["offset_samples"] for e in doc["layers"]["layers"]], [0, off])

    def test_align_puts_each_layers_transient_on_the_marker(self):
        """The oracle is the measure itself on the delivered file: a layer rendered alone, aligned, reads the marker."""
        hit = fx.make("late_hit", R, 2) * 0.3  # main transient near 120 ms
        quiet = fx.make_real("quiet_hit", R)  # starts mid-waveform, transient near 0
        whoosh = fx.make_real("quiet_whoosh", R)
        for name, x, on, to in (("late", hit, "main_transient", 150.0), ("quiet", quiet, "main_transient", 40.0),
                                ("whoosh", whoosh, "F-01", 10.0)):
            with self.subTest(layer=name):
                cue = f"SFX-L-ALIGN-{name.upper()}"
                rec = {"layers": [{"take": take(cue), "design": [], "align": {"to_ms": to, "on": on}}],
                       "design": [], "edit": []}
                d = make_cue(self.d, card(cue, "whoosh" if name == "whoosh" else "hit"), rec, {take(cue): (x, R)})
                doc, _ = render.render(d)
                y = delivered(d)
                y = y - y.mean(axis=0)
                got = (m.main_transient_ms(y, R) if on == "main_transient" else
                       1000 * m.onset_index(y.mean(axis=1)) / R)
                self.assertAlmostEqual(got, to, delta=1000 / R + 0.005)  # one sample (and the 0.01 ms rounding)
                key = "main_transient_ms" if on == "main_transient" else "F-01_onset_ms"
                self.assertAlmostEqual(doc["layers"]["layers"][0]["measured"][key], to, delta=1000 / R + 0.005)
        cue = "SFX-L-ALIGN-TWO"  # two layers on one marker: their clicks coincide in the mix
        a, b = click(3000, 400, 0.2)[:, None], click(5000, 2500, 0.1)[:, None]
        rec = {"layers": [{"take": take(cue, 1), "design": [], "align": {"to_ms": 70.0}},
                          {"take": take(cue, 2), "design": [], "align": {"to_ms": 70.0}}], "design": [], "edit": []}
        d = make_cue(self.d, card(cue), rec, {take(cue, 1): (a, R), take(cue, 2): (b, R)})
        doc, _ = render.render(d)
        offs = [e["offset_samples"] for e in doc["layers"]["layers"]]
        self.assertEqual(offs[0] + 400, offs[1] + 2500)  # both click peaks land on the same sample

    def test_the_logged_transient_is_read_after_placing_and_matches_the_marker(self):
        """Review step 6 R3: a rising layer with DC, placed in a long mix, logged its main transient at 372.22 ms for a
        400 ms marker (the layer's own mean was removed for align, the placed file's mean for the log). The log is now
        read on the placed layer, and align corrects once by that same reading: the two agree within one sample, or
        the log flags the reading as unstable."""
        for dc in (0.0, 0.1, 0.3):
            with self.subTest(dc=dc):
                cue = f"SFX-L-DC{int(dc * 10)}"
                sw = fx.make_real("quiet_whoosh", R)
                sw = sw + dc * float(np.max(np.abs(sw)))
                rec = {"layers": [{"name": "swish", "take": take(cue, 1), "design": [], "align": {"to_ms": 400.0}},
                                  {"name": "bed", "take": take(cue, 2), "design": [], "offset_ms": 0}],
                       "design": [], "edit": [{"op": "peak"}]}
                d = make_cue(self.d, card(cue, "whoosh"), rec,
                             {take(cue, 1): (sw, R), take(cue, 2): (fx.make_bed("steady_noise", R, 5.0) * 0.1, R)})
                doc, _ = render.render(d)
                lay = doc["layers"]["layers"][0]
                self.assertFalse(lay["align_unstable"], lay)
                self.assertAlmostEqual(lay["measured"]["main_transient_ms"], 400.0, delta=1000 / R + 0.005)
                # lead decision (round 2, F2): DC is removed for the reading only, never from the audio
                self.assertEqual([st for st in doc["steps"] if st["op"] == "dc"], [])
                self.assertAlmostEqual(lay["reading_dc"][0], float(np.mean(sw[:, 0])), delta=1e-4)  # of the layer
                # as placed: its 0.5 ms edge fades move the mean by about 1e-5
                self.assertLessEqual(abs(lay["align_correction_samples"]), 1)
                self.assertLessEqual(abs(lay["standalone_index"] + lay["offset_samples"] - lay["placed_index"]), 1)

    def test_a_dc_layer_that_ends_at_zero_is_placed_untouched_and_gains_no_edge_click(self):
        """Review step 6 round 2 F2: the automatic `dc` step shifted a layer that fades to 0 by its mean, so it started
        and ended at -mean: two new clicks at the layer's edges, at exit 0. The delivered audio is the take itself."""
        cue = "SFX-L-EDGE"
        n = int(0.48 * R)
        t = np.arange(n) / R
        env = np.sin(np.pi * t / t[-1]) ** 3  # rises and falls to exactly 0 at both ends
        tone = (0.6 + np.sin(2 * np.pi * 180 * t)) * env * 0.05  # carries DC: its mean is about 0.6 x 0.05 x 0.42
        x = np.stack([tone, 0.9 * tone], axis=1)
        self.assertGreater(abs(float(np.mean(x[:, 0]))), 0.005)
        rec = {"layers": [{"name": "swell", "take": take(cue), "design": [], "align": {"to_ms": 300.0}}],
               "design": [], "edit": []}
        d = make_cue(self.d, card(cue, "whoosh"), rec, {take(cue): (x, R)})
        doc, _ = render.render(d)
        y = delivered(d)
        off = doc["layers"]["layers"][0]["offset_samples"]
        np.testing.assert_allclose(y[off:off + n], x, atol=STEP)  # the take itself, sample for sample
        self.assertEqual(float(np.max(np.abs(y[:off]))), 0.0)
        self.assertEqual(m.clicks(y - y.mean(axis=0), R)["count"], 0)

    def test_a_layer_that_starts_and_ends_mid_waveform_is_faded_and_does_not_click(self):
        """Edge round (F7 class): a take that starts and ends mid-waveform clicked at both edges inside the mix and the
        render exited 0. Each layer's edges get trim's own hot-edge fade (0.5 ms when the edge sample is over peak -
        60 dB), logged as trim logs it, and the layer's edge clicks are a row, read with the clicks measure."""
        cue = "SFX-L-HOT"
        x = fx.make_real("quiet_hit", R)  # its first sample sits 5 dB under its peak
        x = x[: int(0.3 * R)]  # cut mid-body: its last sample is hot too
        pk = float(np.max(np.abs(x)))
        self.assertGreater(float(np.max(np.abs(x[-1]))), pk * 10 ** (-60 / 20))
        rec = {"layers": [{"name": "hit", "take": take(cue), "design": [], "offset_ms": 100.0}],
               "design": [], "edit": []}
        d = make_cue(self.d, card(cue), rec, {take(cue): (x, R)})
        doc, code = render.render(d)
        edge = doc["layers"]["layers"][0]["edge_fade"]
        self.assertEqual((edge["start"]["faded"], edge["end"]["faded"]), (True, True))
        self.assertEqual(len(edge["attack_share"]), 2)
        y = delivered(d)
        self.assertEqual(m.clicks(y - y.mean(axis=0), R)["count"], 0)
        row = rows_by(doc)["layer[hit].edge_clicks"]
        self.assertEqual((row["value"], row["must"], row["result"]), (0, False, "pass"))
        self.assertEqual(code, 0)
        off, k = int(round(0.1 * R)), int(round(0.5 * R / 1000))
        np.testing.assert_allclose(y[off + k:off + len(x) - k], x[k:len(x) - k], atol=STEP)  # only the edges change

    def test_layer_edge_clicks_are_read_and_must_for_important_cues(self):
        """A spike 0.7 ms into the layer, past the 0.5 ms fade: an edge click the fade cannot remove. It is an aim miss
        on a minor cue (exit 0, listed) and a must miss on an important one (exit 1)."""
        for tier, want_must, want_code in (("minor", False, 0), ("important", True, 1)):
            with self.subTest(tier=tier):
                cue = f"SFX-L-SPK-{tier.upper()}"
                x = fx.make_real("quiet_whoosh", R)
                x[30] += 0.5 * float(np.max(np.abs(x)))
                lay = {"name": "air", "take": take(cue), "design": [], "offset_ms": 50.0}
                if tier == "important":
                    lay["targets"] = {"sound_ms": {"min": 1, "must": False}}
                d = make_cue(self.d, card(cue, "whoosh", tier=tier),
                             {"layers": [lay], "design": [], "edit": []}, {take(cue): (x, R)})
                doc, code = render.render(d)
                row = rows_by(doc)["layer[air].edge_clicks"]
                self.assertEqual((row["value"], row["must"], row["result"]), (1, want_must, "miss"))
                self.assertEqual(code, want_code)

    def test_trim_still_fades_its_start_through_the_shared_function(self):
        """trim and the layers call one hot-edge fade (no copy): trim's log keys and numbers are unchanged."""
        x = fx.make_real("soft_note", R)
        y, info = ops.run("trim", x, R, ops.check_params("trim", {}), {"binding": "main_transient"})
        self.assertTrue(info["edge_faded"])
        self.assertEqual(float(np.max(np.abs(y[0]))), 0.0)
        for k in ("first_sample_db_re_peak", "attack_share"):
            self.assertEqual(len(info[k]), 2)
        with mock.patch.object(ops, "fade_hot_edges", side_effect=AssertionError("called")):
            with self.assertRaises(AssertionError):
                ops.run("trim", x, R, ops.check_params("trim", {}), {"binding": "main_transient"})

    def test_the_correction_after_placing_still_lands_a_skewed_reading(self):
        """The safety net kept by the lead: when the first reading is off (here forced 600 samples off), the one
        correction after placing lands the layer on the marker by the as-placed reading of the layer alone."""
        cue = "SFX-L-NET"
        sw = fx.make_real("quiet_whoosh", R)
        sw = sw + 0.1 * float(np.max(np.abs(sw)))
        rec = {"layers": [{"name": "swish", "take": take(cue, 1), "design": [], "align": {"to_ms": 400.0}},
                          {"name": "bed", "take": take(cue, 2), "design": [], "offset_ms": 0}],
               "design": [], "edit": [{"op": "peak"}]}
        d = make_cue(self.d, card(cue, "whoosh"), rec,
                     {take(cue, 1): (sw, R), take(cue, 2): (fx.make_bed("steady_noise", R, 5.0) * 0.1, R)})
        orig = assemble.transient_index
        with mock.patch.object(assemble, "transient_index", lambda x, rate, on: orig(x, rate, on) - 600):
            doc, _ = render.render(d)  # a first reading 600 samples off
        lay = doc["layers"]["layers"][0]
        self.assertEqual(lay["align_correction_samples"], -600)
        self.assertFalse(lay["align_unstable"])
        self.assertAlmostEqual(lay["measured"]["main_transient_ms"], 400.0, delta=1000 / R + 0.005)

    def test_a_layer_at_another_rate_is_resampled_with_a_log_line_and_keeps_its_time(self):
        cue = "SFX-L-RATE"
        a = np.zeros((4410, 2))
        a[10, 0] = 0.1
        b48 = np.stack([click(9600, 4800, 0.3), click(9600, 7200, 0.2)], axis=1)  # 100 and 150 ms at 48 kHz
        rec = {"layers": [{"take": take(cue, 1), "design": [], "offset_ms": 0},
                          {"take": take(cue, 2), "design": [], "offset_ms": 20}], "design": [], "edit": []}
        d = make_cue(self.d, card(cue), rec, {take(cue, 1): (a, 44100), take(cue, 2): (b48, 48000)})
        doc, _ = render.render(d)
        y = delivered(d)
        self.assertEqual(doc["take"]["rate"], 44100)
        res = [s for s in doc["steps"] if s["op"] == "resample"]
        self.assertEqual(len(res), 1)
        self.assertEqual((res[0]["info"]["from_rate"], res[0]["info"]["to_rate"]), (48000, 44100))
        self.assertEqual(res[0]["layer"], "L2")
        off = int(round(20 * 44100 / 1000))
        for ch, at48 in ((0, 4800), (1, 7200)):  # each channel's click keeps its own time
            want = off + at48 * 44100 / 48000
            got = int(np.argmax(np.abs(y[off + 1000:, ch]))) + off + 1000
            self.assertLessEqual(abs(got - want), 1.0, (ch, got, want))

    def test_layer_shares_are_measured_not_assumed(self):
        rs = np.random.RandomState(4)
        n1, n2 = 0.05 * rs.standard_normal((R, 2)), 0.05 * rs.standard_normal((R, 2))
        for label, second, want_mix in (("independent", n2, (0.8, 0.2)), ("inverted", -n1, (2.0, -1.0))):
            with self.subTest(label=label):
                cue = f"SFX-L-SHARE-{label.upper()}"
                rec = {"layers": [{"take": take(cue, 1), "design": [], "offset_ms": 0},
                                  {"take": take(cue, 2), "design": [], "offset_ms": 0, "gain_db": -6.0206}],
                       "design": [], "edit": []}
                d = make_cue(self.d, card(cue), rec, {take(cue, 1): (n1, R), take(cue, 2): (second, R)})
                doc, _ = render.render(d)
                ls = doc["layers"]["layers"]
                self.assertAlmostEqual(ls[0]["share_energy"], 0.8, delta=0.01)  # 1 : 0.25 by energy either way
                self.assertAlmostEqual(ls[0]["share_of_mix"], want_mix[0], delta=0.02)
                self.assertAlmostEqual(ls[1]["share_of_mix"], want_mix[1], delta=0.02)
                self.assertAlmostEqual(ls[0]["share_of_mix"] + ls[1]["share_of_mix"], 1.0, delta=1e-3)
                want_int = 0.0 if label == "independent" else 10 * np.log10(0.25 / 1.25)  # -6.99 dB: they cancel
                self.assertAlmostEqual(doc["layers"]["interference_db"], want_int, delta=0.2)

    def test_the_summed_peak_is_checked_with_exports_own_check(self):
        cue = "SFX-L-SUM"
        x = fx.make("clean_hit", R, 2)
        x = x / np.max(np.abs(x)) * 0.7  # each layer under full scale; together 1.4
        rec = {"layers": [{"take": take(cue, 1), "design": [], "offset_ms": 0},
                          {"take": take(cue, 2), "design": [], "offset_ms": 0}], "design": [], "edit": []}
        d = make_cue(self.d, card(cue), rec, {take(cue, 1): (x, R), take(cue, 2): (x, R)})
        with mock.patch.object(exportmod, "check_exportable", wraps=exportmod.check_exportable) as spy:
            with self.assertRaisesRegex(SoundbenchError, "summed mix is not exportable .*full scale"):
                render.render(d)
        self.assertEqual(spy.call_args_list[0].args[0].shape, x.shape)  # export's check ran on the mix itself
        self.assertFalse((d / "out").exists())
        rec["edit"] = [{"op": "peak"}]
        (d / "recipe.json").write_text(json.dumps({"cue": cue, **rec}), encoding="utf-8")
        doc, _ = render.render(d)
        head = doc["layers"]["headroom"]
        self.assertFalse(head["exportable"])
        self.assertAlmostEqual(head["sample_peak_dbfs"], 20 * np.log10(1.4), delta=0.02)
        self.assertAlmostEqual(head["loudest_layer_peak_dbfs"], 20 * np.log10(0.7), delta=0.02)
        self.assertLessEqual(m.true_peak_db(delivered(d)), -1.5 + 0.01)

    def test_per_layer_targets_fail_the_render_and_name_the_layer(self):
        cue = "SFX-L-TARGETS"
        rec = {"layers": [{"name": "weight", "take": take(cue, 1), "design": [], "offset_ms": 0,
                           "targets": {"band_500_5k": {"min": 0.3, "must": True}}},
                          {"name": "contact", "take": take(cue, 2), "design": [], "offset_ms": 0,
                           "targets": {"above_5k": {"min": 0.01, "must": True}}}],
               "design": [], "edit": [{"op": "peak"}]}
        d = make_cue(self.d, card(cue), rec, {take(cue, 1): (fx.make("bass_thump", R, 2) * 0.3, R),
                                              take(cue, 2): (fx.make("clean_hit", R, 2) * 0.3, R)})
        doc, code = render.render(d)
        self.assertEqual(code, 1)
        self.assertEqual(doc["must_failed"], ["layer[weight].band_500_5k"])  # the thump has no 500 Hz-5 kHz body
        self.assertEqual(rows_by(doc)["layer[contact].above_5k"]["result"], "pass")

    def test_layer_refusals_come_before_any_audio(self):
        base = {"take": "takes/X.r1.t1.mp3", "design": [], "offset_ms": 0}
        cases = (
            ("important without layer targets", {"tier": "important"}, [base], "needs its own targets"),
            ("too many layers", {}, [dict(base, name=f"n{i}") for i in range(9)], "over 8"),
            ("one name twice", {}, [dict(base, name="a"), dict(base, name="a")], "used twice"),
            ("gain out of range", {}, [dict(base, gain_db=30)], "outside"),
            ("align marker field", {}, [{"take": base["take"], "design": [], "align": {"to_ms": 5, "at": 1}}],
             "unknown parameter"),
        )
        for label, extra, layers, why in cases:
            with self.subTest(case=label):
                cue = "SFX-L-REF"
                c = card(cue, **extra)
                with self.assertRaisesRegex(SoundbenchError, why):
                    render.plan_form(c, {"layers": layers}, [])
        cue = "SFX-L-NEG"
        rec = {"layers": [{"take": take(cue), "design": [], "align": {"to_ms": 5.0}}], "design": [], "edit": []}
        d = make_cue(self.d, card(cue), rec, {take(cue): (fx.make("late_hit", R, 2) * 0.3, R)})
        with self.assertRaisesRegex(SoundbenchError, "start before the file"):
            render.render(d)
        self.assertFalse((d / "out").exists())

    def test_spliced_layers_with_fades_have_no_click(self):
        """craft-process section 6: beds spliced from several takes with crossfades, a short fade on every splice."""
        cue = "SFX-L-SPLICE"
        a, b = fx.make_bed("steady_noise", R, 1.0, seed=1), fx.make_bed("steady_noise", R, 1.0, seed=2)
        rec = {"layers": [{"take": take(cue, 1), "design": [], "offset_ms": 0, "fade_out_ms": 20},
                          {"take": take(cue, 2), "design": [], "offset_ms": 980, "fade_in_ms": 20}],
               "design": [], "edit": []}
        d = make_cue(self.d, card(cue, "ambience"), rec, {take(cue, 1): (a, R), take(cue, 2): (b, R)})
        doc, _ = render.render(d)
        y = delivered(d)
        self.assertEqual(len(y), int(round(0.98 * R)) + len(b))
        self.assertEqual(m.clicks(y - y.mean(axis=0), R)["count"], 0)


# --------------------------------------------------------------------------------------------- loops

def loop_params(op: str, **p) -> dict:
    return ops.check_params(op, p, assemble.LOOP_SPEC[op])


def judge(y: np.ndarray, info: dict | None, c: dict | None = None) -> dict:
    """render's loop rows on a buffer (F-08 by review.md's definition): target -> row."""
    rows, _ = render.loop_rows(c or card("X", "loop_bed"), {"F-08_loop_seam": round(f08(y), 3)}, y, R, info)
    return {r["target"]: r for r in rows}


def failing(rows: dict) -> set:
    return {k for k, r in rows.items() if r["must"] and r["result"] != "pass"}


def search_for(kind: str) -> float:
    return 20.0 if kind in ("steady_tone", "tonal_pad") else 0.0


def wind_rain_bed(seconds: float, quiet_db: float = -30.0, loud_share: float = 0.5, seed: int = 3) -> np.ndarray:
    """The reviewer's R1 bed (review step 6, lib.bed2): circular wind low-passed at 400 Hz at `quiet_db`, rain
    (low-passed at 6 kHz) swelling in over the middle `loud_share` of the loop; it loops exactly; peak 0.5."""
    rs = np.random.RandomState(seed)
    n = int(seconds * R)
    t = np.arange(n) / n
    f = np.fft.rfftfreq(n, 1 / R)
    lp = lambda fc: 1 / np.sqrt(1 + (f / fc) ** 4)  # noqa: E731
    wind = np.stack([np.fft.irfft(np.fft.rfft(rs.standard_normal(n)) * lp(400), n) for _ in range(2)], 1)
    rain = np.stack([np.fft.irfft(np.fft.rfft(rs.standard_normal(n)) * lp(6000), n) for _ in range(2)], 1)
    wind /= np.sqrt(np.mean(wind ** 2))
    rain /= np.sqrt(np.mean(rain ** 2))
    c = np.cos(np.pi * loud_share)
    env = np.clip((np.cos(2 * np.pi * (t - 0.5)) - c) / (1 - c), 0, None)
    y = wind * 10 ** (quiet_db / 20) + rain * env[:, None]
    return y / np.max(np.abs(y)) * 0.5


def seam_jump(y: np.ndarray, j: float) -> np.ndarray:
    """A level step of j over the last 200 ms (eased in over 50 ms): at the wrap the file jumps back by j."""
    z = y.copy()
    k, ramp = int(0.2 * R), int(0.05 * R)
    off = np.zeros(len(z))
    off[-k:] = j
    off[-k:-k + ramp] = j * (0.5 - 0.5 * np.cos(np.pi * np.arange(ramp) / ramp))
    return z + off[:, None]


class LoopTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_loop_bed_wrap_is_sample_exact_through_flac(self):
        for kind, sec in (("steady_noise", 2), ("tonal_pad", 5), ("real_bed", 10)):
            with self.subTest(bed=kind, seconds=sec):
                cue = f"AMB-LOOP-{kind.upper().replace('_', '-')}"
                rec = {"take": take(cue), "design": [], "edit": [],
                       "loop": {"op": "loop_bed", "crossfade_ms": 250, "search_ms": search_for(kind)}}
                c = card(cue, "loop_bed", category="ambience", form={"loop": True})
                d = make_cue(self.d, c, rec, {take(cue): (fx.make_bed(kind, R, sec + 0.5), R)})
                doc, code = render.render(d)
                self.assertEqual(code, 0, doc["must_failed"])
                x, y = master(d, take(cue)), delivered(d)
                info = doc["loop"]
                s, e = info["start_sample"], info["end_sample"]
                self.assertEqual(len(y), e - s)
                np.testing.assert_allclose(y[0], x[s], atol=STEP)  # the first sample is the source's x[s] ...
                np.testing.assert_allclose(y[-1], x[s - 1], atol=STEP)  # ... the last its neighbour x[s-1]
                np.testing.assert_allclose(y[: e - s - info["crossfade_samples"]],
                                           x[s:e - info["crossfade_samples"]], atol=STEP)  # untouched before the fade
                for r in doc["targets"] + doc["form_checks"]:
                    if r["must"]:
                        self.assertEqual(r["result"], "pass", r)

    def test_loops_of_2_to_30_s_pass_and_every_planted_seam_fails_for_its_reason(self):
        """Noise-like, tonal and spliced-real beds at 2, 5, 10 and 30 s. Each planted fault is caught by the row named
        for it (the reason), and the good loop by no row."""
        for kind in fx.BED_KINDS:
            for sec in (2, 5, 10, 30):
                with self.subTest(bed=kind, seconds=sec):
                    x = fx.make_bed(kind, R, sec + 0.5)
                    y, info = assemble.loop_bed(x, R, loop_params("loop_bed", crossfade_ms=250,
                                                                  search_ms=search_for(kind)))
                    self.assertEqual(failing(judge(y, info)), set())
                    pk = float(np.max(np.abs(y)))
                    noisy = kind in ("steady_noise", "noise_bed")
                    spike = y.copy()
                    spike[-3] += (0.5 if noisy else 0.25) * pk  # a click 3 samples before the end: F-08 cannot see it
                    got = failing(judge(spike, info))
                    self.assertTrue(got & {"form.loop_wrap_clicks", "form.loop_wrap_hf"}, got)
                    self.assertNotIn("form.loop_f08", got)
                    if kind != "real_bed":  # a fade gap: F-08 reads 0 (review.md F-08's own false reading)
                        gap = y.copy()
                        k = int(0.1 * R)
                        gap[:k] *= np.linspace(0, 1, k)[:, None]
                        gap[-k:] *= np.linspace(1, 0, k)[:, None]
                        self.assertLess(f08(gap), 0.1)
                        self.assertIn("form.loop_seam_gap", failing(judge(gap, info)))
                    if kind in ("steady_tone", "tonal_pad", "real_bed"):  # a drift jump of 0.3 x peak at the wrap
                        jump = y + np.linspace(0, 0.3 * pk, len(y))[:, None]
                        self.assertIn("form.loop_f08", failing(judge(jump, info)))

    def test_the_wrap_has_no_blind_spot(self):
        """What the click detector sees when the seam sits inside the file, loop_wrap sees at the wrap."""
        for kind in fx.BED_KINDS:
            x = fx.make_bed(kind, R, 3.0)
            y, _ = assemble.loop_bed(x, R, loop_params("loop_bed", crossfade_ms=250, search_ms=search_for(kind)))
            pk = float(np.max(np.abs(y)))
            for size in (0.05, 0.1, 0.25, 0.5, 1.0):
                with self.subTest(bed=kind, spike=size):
                    z = y.copy()
                    z[-2] += size * pk
                    a = z - z.mean(axis=0)
                    r = len(a) // 2
                    seen = m.clicks(np.roll(a, r, axis=0), R)["first_ms"]  # (i + 1) / rate in ms for step i
                    inside = [t for t in seen if abs(t - 1000 * r / R) <= 1.0]
                    self.assertEqual(m.loop_wrap(z, R)["wrap_clicks"] > 0, len(inside) > 0, (seen, 1000 * r / R))

    def test_the_curve_follows_the_correlation_and_a_wrong_curve_fails_both_ways(self):
        noise, tone = fx.make_bed("steady_noise", R, 4.0), fx.make_bed("steady_tone", R, 4.0)
        _, info = assemble.loop_bed(noise, R, loop_params("loop_bed", crossfade_ms=250))
        self.assertEqual(info["curve"], "power")
        _, info = assemble.loop_bed(tone, R, loop_params("loop_bed", crossfade_ms=250, search_ms=20))
        self.assertEqual(info["curve"], "linear")
        y, info = assemble.loop_bed(noise, R, loop_params("loop_bed", crossfade_ms=250, curve="linear"))
        row = judge(y, info)["form.loop_crossfade_level"]
        self.assertEqual(row["result"], "miss")
        self.assertLess(row["value"], -render.LOOP_CROSSFADE_DB)  # a dip: equal gain on uncorrelated noise
        y, info = assemble.loop_bed(tone, R, loop_params("loop_bed", crossfade_ms=250, search_ms=20, curve="power"))
        row = judge(y, info)["form.loop_crossfade_level"]
        self.assertEqual(row["result"], "miss")
        self.assertGreater(row["value"], render.LOOP_CROSSFADE_DB)  # a bump: equal power on in-phase parts

    def test_the_loop_rows_read_a_quiet_bed_as_the_same_bed_normalised(self):
        """Every loop threshold is relative to the loop's own material: -40 dB changes no reading."""
        for kind in ("noise_bed", "tonal_pad", "real_bed"):
            with self.subTest(bed=kind):
                y, info = assemble.loop_bed(fx.make_bed(kind, R, 3.0), R,
                                            loop_params("loop_bed", crossfade_ms=250, search_ms=search_for(kind)))
                y[-3] += 0.25 * float(np.max(np.abs(y)))
                loud, quiet = judge(y, info), judge(y * 0.01, info)
                for k in loud:
                    if k == "form.loop_crossfade_level":
                        continue  # measured by the loop step on its own audio, not on this buffer
                    self.assertAlmostEqual(loud[k]["value"], quiet[k]["value"], delta=0.02, msg=k)
                    self.assertEqual(loud[k]["result"], quiet[k]["result"], k)

    def test_loop_music_is_bar_aligned_and_keeps_its_downbeat(self):
        x = fx.make_bed("tonal_pad", R, 14.0)
        for bpm, bars, exact in ((120, 2, 176400), (93, 2, 2 * 4 * 60 / 93 * R)):
            with self.subTest(bpm=bpm):
                cue = f"MUS-LOOP-{bpm}"
                rec = {"take": take(cue), "design": [], "edit": [],
                       "loop": {"op": "loop_music", "bpm": bpm, "bars": bars, "start_ms": 2000, "crossfade_ms": 40}}
                c = card(cue, "loop_music", category="music", form={"loop": True})
                d = make_cue(self.d, c, rec, {take(cue): (x, R)})
                doc, code = render.render(d)
                y = delivered(d)
                n = int(round(exact))  # 120 BPM: 176,400 exactly; 93 BPM: 227,612.9 -> 227,613
                self.assertEqual(len(y), n)
                self.assertAlmostEqual(doc["loop"]["drift_samples_per_loop"], n - exact, places=3)
                np.testing.assert_allclose(y[0], master(d, take(cue))[int(round(2.0 * R))], atol=STEP)  # the downbeat
                self.assertEqual(rows_by(doc)["form.loop_length_samples"]["result"], "pass")
                self.assertEqual(code, 0, doc["must_failed"])

    def test_loop_refusals_come_before_any_audio(self):
        lc = card("AMB-R", "loop_bed", form={"loop": True})
        edit = lambda *names: [{"op": n, "params": {}} for n in names]  # noqa: E731
        cases = ((card("AMB-R", "loop_bed"), {"loop": {"op": "loop_bed"}}, [], "form.loop is not true"),
                 (lc, {"loop": {"op": "loop_bed"}}, edit("trim"), "across the seam"),
                 (lc, {"loop": {"op": "loop_bed"}}, edit("fade"), "across the seam"),
                 (lc, {"loop": {"op": "loop_bed", "crossfade_ms": 1}}, [], "outside"),
                 (lc, {"loop": {"op": "loop_music", "bpm": 120}}, [], "required"),
                 (dict(lc, form={"loop": True, "variants": 2}), {"loop": {"op": "loop_bed"},
                                                                "variants": {"seed": 1}}, [], "variants of a loop"))
        for c, rec, ed, why in cases:
            with self.subTest(why=why):
                with self.assertRaisesRegex(SoundbenchError, why):
                    render.plan_form(c, rec, ed)
        x = fx.make_bed("steady_noise", R, 2.0)
        for p, why in (({"crossfade_ms": 250, "start_ms": 100}, "under its crossfade"),
                       ({"crossfade_ms": 1500}, "over 50%"), ({"crossfade_ms": 250, "end_ms": 2500}, "past the sound")):
            with self.subTest(why=why):
                with self.assertRaisesRegex(SoundbenchError, why):
                    assemble.loop_bed(x, R, loop_params("loop_bed", **p))

    def test_a_card_seam_target_tightens_r26_and_loosens_it_only_as_a_must_with_a_why(self):
        """Review step 6 F1: an aim loop_seam {max: 50} lifted the must F-08 row to 50, so a 0.1 x peak drift jump at
        the wrap of a tonal pad (F-08 2.7-3.2, caught by no other row) passed at exit 0. A card limit only tightens
        R-26's 2; it loosens it only as a must target with a `why`."""
        for sec in (2, 10, 30):
            x = fx.make_bed("tonal_pad", R, sec + 0.5)
            y, info = assemble.loop_bed(x, R, loop_params("loop_bed", crossfade_ms=250, search_ms=20))
            z = y + np.linspace(0, 0.1 * float(np.max(np.abs(y))), len(y))[:, None]
            for label, seam, want_max in (("aim 50", {"max": 50, "must": False}, 2.0),
                                          ("aim 3", {"max": 3, "must": False}, 2.0),
                                          ("must 50 without why", {"max": 50, "must": True}, 2.0),
                                          ("stricter aim 1.0", {"max": 1.0, "must": False}, 1.0),
                                          ("must 50 with why", {"max": 50, "must": True,
                                                                "why": "a granular bed: its seam steps are its texture"},
                                           50.0)):
                with self.subTest(seconds=sec, card=label):
                    c = card("X", "loop_bed", targets={"loop_seam": seam})
                    row = judge(z, info, c)["form.loop_f08"]
                    self.assertEqual(row["max"], want_max)
                    self.assertGreater(row["value"], 2.0)
                    self.assertEqual(row["result"], "pass" if want_max == 50.0 else "miss")
        cue = "AMB-AIM50"  # the reviewer's full render (fa_render.py): exit 1, not 0
        x = fx.make_bed("tonal_pad", R, 10.5)
        y, _ = assemble.loop_bed(x, R, loop_params("loop_bed", crossfade_ms=250, search_ms=20))
        z = y + np.linspace(0, 0.1 * float(np.max(np.abs(y))), len(y))[:, None]
        c = card(cue, "ambience", category="ambience", form={"loop": True},
                 targets={"loop_seam": {"max": 50, "must": False}})
        d = make_cue(self.d, c, {"take": take(cue), "design": [], "edit": []}, {take(cue): (z, R)})
        doc, code = render.render(d)
        self.assertEqual(code, 1)
        self.assertIn("form.loop_f08", doc["must_failed"])
        own = rows_by(doc)["loop_seam"]  # the card's own aim row is unchanged (rank's proof compares it)
        self.assertEqual((own["max"], own["must"], own["result"]), (50, False, "pass"))
        self.assertEqual(rows_by(doc)["form.loop_f08"]["limit_from"],
                         "R-26 (the card's looser limit needs must: true and a why)")

    def test_known_miss_a_seam_in_the_quiet_part_of_a_bed_with_a_loud_section(self):
        """Pinned known limit (review step 6 R1, lead's decision: named, not recalibrated): wind with rain swelling in
        over the middle half, looping exactly; a seam jump the size of the wind's own RMS sits under the click floor
        (1 % of the file peak), and F-08 and wrap_hf read it against the loud rain, so every row passes. The same
        jump 12 dB larger is caught by the click count. When this test fails, the limit has moved: update the
        README and docstrings."""
        y = wind_rain_bed(10.0)
        local = float(np.sqrt(np.mean(y[-int(0.05 * R):] ** 2)))
        miss = judge(seam_jump(y, local), None)
        self.assertEqual(failing(miss), set())  # the known miss
        self.assertLess(miss["form.loop_wrap_hf"]["value"], -20.0)  # blind by far: the rain sets the baseline
        caught = judge(seam_jump(y, local * 10 ** (12 / 20)), None)
        self.assertIn("form.loop_wrap_clicks", failing(caught))


    def test_rank_still_ranks_and_proves_a_loop_card(self):
        """rank's proof compares render's `targets` with its own simulation row by row: the loop rows live in
        `form_checks`, so a loop card's round is ranked as before (no refusal), and its proof agrees."""
        from tools.audio.soundbench import rank

        cue = "AMB-RANK"
        c = card(cue, "loop_bed", category="ambience", form={"loop": True})
        c["level"]["must"] = True
        c["targets"] = {"true_peak_dbtp": {"max": -1.0, "must": True}}
        d = make_cue(self.d, c, {"take": take(cue), "design": [], "edit": []},
                     {take(cue, n): (fx.make_bed("noise_bed", R, 2.0, seed=n), R) for n in (1, 2, 3)})
        (d / "recipe.json").unlink()
        doc, code = rank.rank(d)
        self.assertIn(code, (0, 1))
        self.assertTrue(doc["proof"] is None or doc["proof"]["agrees"])
        self.assertIsNotNone(doc["proof"])  # the noise beds reach the level: the top take is proven
        rd, _ = render.render(self._recipe(d, cue, doc))
        self.assertEqual({r["target"] for r in rd["targets"]}, {r["target"] for r in doc["takes"][0]["after"]})
        self.assertTrue(any(r["target"] == "form.loop_wrap_hf" for r in rd["form_checks"]))

    def _recipe(self, d: Path, cue: str, doc: dict) -> Path:
        top = doc["takes"][0]
        (d / "recipe.json").write_text(json.dumps({"cue": cue, "take": f"takes/{top['take']}", "design": [],
                                                   "edit": top["fix"]["steps"]}), encoding="utf-8")
        return d

    def test_a_loop_card_judges_the_wrap_even_without_a_loop_step(self):
        cue = "AMB-NATIVE"
        x = fx.make_bed("tonal_pad", R, 3.0)
        mono = x.mean(axis=1)
        cut = int(2.6 * R) + int(np.argmax(np.abs(mono[int(2.6 * R) - 1:int(2.8 * R) - 1] - mono[0])))
        x = x[:cut]  # cut where the wrap jumps furthest from the first sample
        c = card(cue, "ambience", category="ambience", form={"loop": True})
        d = make_cue(self.d, c, {"take": take(cue), "design": [], "edit": []}, {take(cue): (x, R)})
        doc, code = render.render(d)
        self.assertEqual(code, 1)
        self.assertIn("form.loop_f08", doc["must_failed"])
        self.assertGreater(rows_by(doc)["form.loop_f08"]["value"], render.LOOP_F08_MUST_MAX)


# --------------------------------------------------------------------------------------------- variants

def variant_cue(root: Path, cue: str, n: int, variants: dict | None = None, takes: int = 0, **card_extra) -> Path:
    c = card(cue, form={"variants": n}, **card_extra)
    c["level"] = {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True}
    edit = [{"op": "trim"}, {"op": "fade", "out_ms": 10}, {"op": "loudness"}, {"op": "peak"}]
    srcs = [fx.make_real("quiet_hit", R, seed=11 + k) for k in range(max(1, takes))]
    if takes:
        rec = {"takes": [take(cue, k + 1) for k in range(takes)], "design": [], "edit": edit}
    else:
        rec = {"take": take(cue), "design": [], "edit": edit, "variants": variants}
    return make_cue(root, c, rec, {take(cue, k + 1): (srcs[k], R) for k in range(len(srcs))})


class VariantTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_the_plan_is_seeded_and_spreads_over_the_range(self):
        a, b = assemble.variant_plan(4, 7, 50.0, 0.5), assemble.variant_plan(4, 7, 50.0, 0.5)
        self.assertEqual(a, b)
        self.assertNotEqual(a, assemble.variant_plan(4, 8, 50.0, 0.5))
        cents = sorted(v["cents"] for v in a)
        for i, c in enumerate(cents):  # one draw in each quarter of -50..50 (stratified)
            self.assertTrue(-50 + 25 * i - 0.05 <= c <= -25 + 25 * i + 0.05, cents)
        self.assertTrue(all(abs(v["gain_db"]) <= 0.5 for v in a))
        self.assertEqual(assemble.variant_plan(3, 1, 0.0, 0.0), [{"k": k, "cents": 0.0, "gain_db": 0.0}
                                                                 for k in (1, 2, 3)])

    def test_a_planned_set_passes_r31_as_render_reads_it_over_many_seeds(self):
        """review-rank-layers round 2 (lead decision): R-31 reads each file's level against the set's mean
        (render.variant_rows), so the plan must keep every gain within max_db of the set's mean, not of 0. Seed 19 with
        4 variants at max_db 1.0 used to plan 1.0975 dB. Checked with render's own row over 2..16 variants x 300 seeds x
        max_db 0.5 and 1.0, levels on a -24 target; the plan stays seeded and keeps its spread (the outer slots)."""
        for max_db in (0.5, 1.0):
            for count in range(2, 17):
                for seed in range(300):
                    draws = assemble.variant_plan(count, seed, 30.0, max_db)
                    gains = [d["gain_db"] for d in draws]
                    mean = sum(gains) / count
                    self.assertLessEqual(max(abs(g - mean) for g in gains), max_db + 1e-9, (count, seed, gains))
                    rows = render.variant_rows(count, {f"v{d['k']}": -24.0 + d["gain_db"] for d in draws})
                    spread = next(r for r in rows if r["target"] == "variants.level_spread")
                    self.assertEqual(spread["result"], "pass", (count, seed, max_db, spread["value"]))
                    if count >= 4:  # stratified, centred and scaled: the set still uses most of its range
                        self.assertGreaterEqual(max(gains) - min(gains), max_db, (count, seed, gains))
        self.assertEqual(assemble.variant_plan(4, 19, 30.0, 1.0), assemble.variant_plan(4, 19, 30.0, 1.0))

    def test_variant_files_carry_their_pitch_and_level(self):
        d = variant_cue(self.d, "SFX-V-HIT", 4, {"seed": 3, "max_cents": 80, "max_db": 0.5})
        (d / "out").mkdir()
        for stale in ("SFX-V-HIT.flac", "SFX-V-HIT-v5.flac", "SFX-V-HIT-v6.log.json"):  # an earlier render's files
            (d / "out" / stale).write_bytes(b"stale")
        doc, code = render.render(d)
        self.assertEqual(sorted(f.name for f in (d / "out").glob("*.flac")),
                         [f"SFX-V-HIT-v{k}.flac" for k in (1, 2, 3, 4)])
        self.assertFalse((d / "out" / "SFX-V-HIT-v6.log.json").exists())
        self.assertEqual(code, 0, doc["must_failed"])
        draws = assemble.variant_plan(4, 3, 80.0, 0.5)
        self.assertEqual(doc["variants"]["draws"], draws)
        levels = []
        for dr in draws:
            name = f"SFX-V-HIT-v{dr['k']}"
            out = next(o for o in doc["outputs"] if o["name"] == name)
            vs = next(s for s in out["steps"] if s["op"] == "varispeed")
            n_in, n_out = vs["info"]["samples"] if dr["cents"] else (1, 1)
            if dr["cents"]:  # the length ratio a pitch change of c cents gives: 2 ** (-c / 1200), within one sample
                self.assertLessEqual(abs(n_out - n_in * 2 ** (-dr["cents"] / 1200)), 1.0)
            y = delivered(d, name)
            levels.append(m.level_db(y, R, "F-09"))
            self.assertAlmostEqual(levels[-1], -24.0 + dr["gain_db"], delta=0.06)  # the level offset, measured
        self.assertGreaterEqual(max(levels) - min(levels), 0.5)  # stratified: the outer slots are drawn
        r = rows_by(doc)
        self.assertEqual((r["form.variants"]["value"], r["form.variants"]["result"]), (4, "pass"))
        self.assertEqual(r["variants.level_spread"]["result"], "pass")
        self.assertIn("S-92", doc["variants"]["note"])

    def test_g1_two_processes_render_the_same_variant_audio(self):
        d = variant_cue(self.d, "SFX-V-G1", 3, {"seed": 11, "max_cents": 60, "max_db": 0.5})
        code = ("import sys, json; sys.path.insert(0, sys.argv[1]); from pathlib import Path; "
                "from tools.audio.soundbench import render; d, c = render.render(Path(sys.argv[2])); "
                "print(json.dumps({o['name']: o['export']['audio_sha256_float32'] for o in d['outputs']}))")
        runs = [json.loads(subprocess.run([sys.executable, "-c", code, str(ROOT), str(d)], capture_output=True,
                                          text=True, check=True).stdout) for _ in range(2)]
        self.assertEqual(runs[0], runs[1])
        self.assertEqual(len(set(runs[0].values())), 3)  # three different files

    def test_a_variant_that_misses_a_must_is_named(self):
        d = variant_cue(self.d, "SFX-V-MISS", 4, {"seed": 22, "max_cents": 30, "max_db": 1.0})
        c = json.loads((d / "card.json").read_text(encoding="utf-8"))
        c["level"]["tolerance"] = 0.2
        (d / "card.json").write_text(json.dumps(c), encoding="utf-8")
        doc, code = render.render(d)
        draws = assemble.variant_plan(4, 22, 30.0, 1.0)  # gains -0.5, 0.78, 0.06, -0.33: none within 0.1 of 0.2
        self.assertTrue(all(abs(abs(v["gain_db"]) - 0.2) > 0.1 for v in draws))
        want = sorted(f"SFX-V-MISS-v{v['k']}:level" for v in draws if abs(v["gain_db"]) > 0.2)  # the card's tolerance
        self.assertTrue(want)
        self.assertEqual(code, 1)
        self.assertEqual(sorted(x for x in doc["must_failed"] if x.endswith(":level")), want)

    def test_tells_warnings_and_countdowns_get_no_variants(self):
        for kind in ("tell", "warning", "countdown"):
            for label, extra in (("seeded", {"variants": {"seed": 1}}), ("per take", {"takes": ["takes/a.mp3",
                                                                                                  "takes/b.mp3"]})):
                with self.subTest(kind=kind, how=label):
                    with self.assertRaisesRegex(SoundbenchError, "SC-12"):
                        render.plan_form(card("X", kind), extra, [])
        cue = "SFX-V-TELL"
        d = make_cue(self.d, card(cue, "tell"), {"take": take(cue), "design": [], "edit": [],
                                                 "variants": {"seed": 1, "count": 2}},
                     {take(cue): (fx.make_real("quiet_whoosh", R), R)})
        p = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "render", str(d)], cwd=str(ROOT),
                           capture_output=True, text=True, env={**__import__("os").environ, "PYTHONIOENCODING": "utf-8"})
        self.assertEqual(p.returncode, 2, p.stderr)  # a hard refusal
        self.assertIn("SC-12", p.stderr)
        self.assertFalse((d / "out").exists())

    def test_rank_use_names_the_form_rows_its_proof_leaves_to_render(self):
        """Review step 6 R2: rank said "passes every must-target" while its own proof render failed form.variants (the
        proof recipe makes no variants). The verdict and exit code stay; the "use" text names the form rows."""
        from tools.audio.soundbench import rank

        cue = "SFX-V-RANK"
        c = card(cue, form={"variants": 4})
        c["level"] = {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True}
        d = make_cue(self.d, c, {"take": take(cue), "design": [], "edit": []},
                     {take(cue, n): (fx.make_real("quiet_hit", R, seed=10 + n), R) for n in (1, 2, 3)})
        (d / "recipe.json").unlink()
        doc, code = rank.rank(d)
        self.assertEqual((code, doc["verdict"]["action"]), (0, "use"))
        self.assertEqual(doc["proof"]["must_failed"], ["form.variants"])
        self.assertIn("form rows (loop, variants) are judged at render: form.variants", doc["verdict"]["say"])

    def test_one_variant_file_per_take(self):
        d = variant_cue(self.d, "SFX-V-TAKES", 3, takes=3)
        doc, code = render.render(d)
        self.assertEqual(code, 0, doc["must_failed"])
        hashes = {o["name"]: o["export"]["audio_sha256_float32"] for o in doc["outputs"]}
        for k in (1, 2, 3):  # each variant is exactly its own take through the same recipe
            single = self.d / f"SFX-V-ONE{k}"
            rec = json.loads((d / "recipe.json").read_text(encoding="utf-8"))
            c = card(single.name)
            c["level"] = {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True}
            s = make_cue(self.d, c, {"take": take(single.name), "design": [], "edit": rec["edit"]},
                         {take(single.name): (master(d, take("SFX-V-TAKES", k)), R)})
            sdoc, _ = render.render(s)
            self.assertEqual(sdoc["export"]["audio_sha256_float32"], hashes[f"SFX-V-TAKES-v{k}"])

    def test_variant_counts_and_limits_are_checked(self):
        cases = ((card("X", form={"variants": 4}), {"variants": {"seed": 1, "count": 3}}, "the card says"),
                 (card("X"), {"variants": {"seed": 1}}, "0 or absent"),
                 (card("X", form={"variants": 2}), {"takes": ["takes/a.mp3"]}, "the card says how many"),
                 (card("X", form={"variants": 2}), {"variants": {"count": 2}}, "seed.*required"),
                 (card("X", form={"variants": 2}), {"variants": {"seed": 1, "max_db": 1.5}}, "outside"),
                 (card("X", form={"variants": 2}, key={"root": "A", "scale": "major"}),
                  {"variants": {"seed": 1, "max_cents": 40}}, "over 30"),
                 (card("X", "chime", form={"variants": 2}), {"variants": {"seed": 1, "max_cents": 50}}, "over 30"),
                 (card("X", form={"variants": 2}), {"variants": {"seed": 1, "max_cents": 150}}, "over 100"))
        for c, rec, why in cases:
            with self.subTest(why=why):
                with self.assertRaisesRegex(SoundbenchError, why):
                    render.plan_form(c, rec, [])

    def test_a_paid_reveal_family_checks_every_variant_file(self):
        """D-03 is not weakened: every variant file of a member counts, and a stale file of the other form is never
        read (render removes it; the card says which files are current)."""
        fam = lambda me: {"id": "egg", "paid_reveal": True,  # noqa: E731
                          "siblings": [n for n in ("SFX-EGG-A", "SFX-EGG-B") if n != me]}
        chime = fx.make("wrong_chime", R, 2) * 0.3
        b = card("SFX-EGG-B", "chime", family=fam("SFX-EGG-B"))
        b["level"] = {"measure": "F-09", "target": -20.0, "tolerance": 0.5, "must": True}
        edit = [{"op": "loudness"}, {"op": "peak"}]
        make_cue(self.d, b, {"take": take("SFX-EGG-B"), "design": [], "edit": edit}, {take("SFX-EGG-B"): (chime, R)})
        for label, max_db, want in (("level jitter 1 dB", 1.0, "fail"), ("no jitter", 0.0, "pass")):
            with self.subTest(case=label):
                a = card("SFX-EGG-A", "chime", family=fam("SFX-EGG-A"), form={"variants": 3})
                a["level"] = dict(b["level"])
                ad = make_cue(self.d, a, {"take": take("SFX-EGG-A"), "design": [], "edit": edit,
                                          "variants": {"seed": 2, "max_cents": 0, "max_db": max_db}},
                              {take("SFX-EGG-A"): (chime, R)})
                render.render(self.d / "SFX-EGG-B")
                (ad / "out").mkdir(exist_ok=True)
                loud = chime * 3  # a stale single-file render of A, far louder, left in out/
                exportmod.export_flac(loud / np.max(np.abs(loud)) * 0.9, R, ad / "out" / "SFX-EGG-A.flac")
                doc, code = render.render(ad)
                self.assertFalse((ad / "out" / "SFX-EGG-A.flac").exists())
                self.assertEqual(sorted(Path(f).name for f in doc["family"]["files"]),
                                 ["SFX-EGG-A-v1.flac", "SFX-EGG-A-v2.flac", "SFX-EGG-A-v3.flac", "SFX-EGG-B.flac"])
                self.assertEqual(doc["family"]["result"], want, doc["family"])
                self.assertEqual(code, 1 if want == "fail" else 0)
                bdoc, bcode = render.render(self.d / "SFX-EGG-B")  # the other member sees the same files
                self.assertEqual(bdoc["family"]["result"], want)


# --------------------------------------------------------------------------------------------- planted faults

def _shift_place(orig):
    def place(parts):
        return orig([(a, off + 1) for a, off in parts])
    return place


def _swap_place(orig):
    def place(parts):
        return orig([(a[:, ::-1], off) for a, off in parts])
    return place


def _abs_gap(orig):
    def loop_wrap(x, rate, seam_ms=None):
        out = orig(x, rate, seam_ms)
        w = int(0.05 * rate)
        edge = np.concatenate([x[-w:], x[:w]])
        if 20 * np.log10(max(float(np.sqrt(np.mean(edge ** 2))), 1e-12)) < -60:  # an absolute floor in dBFS
            out["seam_gap_db"] = -20.0
        return out
    return loop_wrap


def _dips_only(orig):
    def crossfade_level(*a, **k):
        out = orig(*a, **k)
        out["max_db"] = min(0.0, out["max_db"])
        return out
    return crossfade_level


def _no_gain(orig):
    def variant_plan(*a, **k):
        return [{**v, "gain_db": 0.0} for v in orig(*a, **k)]
    return variant_plan


def _first_file_only(orig_check, orig_files):
    def family_check(card_, cue_dir, out_files):
        with mock.patch.object(render, "delivered_files", lambda cd, c: orig_files(cd, c)[:1]):
            return orig_check(card_, cue_dir, out_files[:1])
    return family_check


def _shares_from_gains(placed, mix):
    e = [float(np.sum(p ** 2)) for p in placed]
    return {"energy": [v / sum(e) for v in e], "of_mix": [v / sum(e) for v in e], "interference_db": 0.0}


def _wrap_into_the_start(x, s, n, cross, curve):
    y = x[s:s + n].copy()
    fi, fo = assemble.crossfade_gains(cross, curve)
    y[n - cross:] = fo[:, None] * x[s + n - cross:s + n] + fi[:, None] * x[s:s + cross]
    return y


def _dc_shaped(orig):
    def shape_layer(x, rate, *a):
        return orig(x - x.mean(axis=0), rate, *a)
    return shape_layer


class _read_the_mix:
    """Planted fault: after placing, every reading is taken on the de-meaned mix, not on the layer alone."""

    def __enter__(self):
        held, place, index = {}, assemble.place, assemble.layer_index

        def placed(parts):
            mix, ps = place(parts)
            held["mix"] = mix
            return mix, ps

        def reading(x, rate, on, at):
            return index(held["mix"], rate, on, 0) if "mix" in held else index(x, rate, on, at)

        self._p = [mock.patch.object(assemble, "place", placed), mock.patch.object(assemble, "layer_index", reading)]
        for p in self._p:
            p.start()
        return self

    def __exit__(self, *exc):
        for p in self._p:
            p.stop()


def _floored_bars(bars, beats_per_bar, bpm, rate):
    exact = bars * beats_per_bar * 60.0 / bpm * rate
    return int(exact), exact


RS = np.random.RandomState

FAULTS = {
    "a layer placed one sample late":
        (lambda: mock.patch.object(assemble, "place", _shift_place(assemble.place)),
         [(LayerTest, "test_offsets_land_to_the_sample_on_each_channel_in_order")]),
    "a stereo layer's channels swapped":
        (lambda: mock.patch.object(assemble, "place", _swap_place(assemble.place)),
         [(LayerTest, "test_offsets_land_to_the_sample_on_each_channel_in_order")]),
    "a layer at another rate not resampled":
        (lambda: mock.patch.object(assemble, "resample", lambda x, r, to: (x, {"from_rate": r, "to_rate": to})),
         [(LayerTest, "test_a_layer_at_another_rate_is_resampled_with_a_log_line_and_keeps_its_time")]),
    "shares from the gains, not measured":
        (lambda: mock.patch.object(assemble, "shares", _shares_from_gains),
         [(LayerTest, "test_layer_shares_are_measured_not_assumed")]),
    "the summed mix not checked before the edit pass":
        (lambda: mock.patch.object(exportmod, "check_exportable", lambda x, rate, src=None: (x, rate, 0.0)),
         [(LayerTest, "test_the_summed_peak_is_checked_with_exports_own_check")]),
    "per-layer targets ignored":
        (lambda: mock.patch.object(render, "layer_rows", lambda *a: []),
         [(LayerTest, "test_per_layer_targets_fail_the_render_and_name_the_layer")]),
    "the loop fades into the start instead of the material before it":
        (lambda: mock.patch.object(assemble, "wrap", _wrap_into_the_start),
         [(LoopTest, "test_loop_bed_wrap_is_sample_exact_through_flac")]),
    "the wrap read by F-08 and the click count only (no high-frequency reading)":
        (lambda: mock.patch.object(render, "LOOP_WRAP_HF_DB", 1e9),
         [(LoopTest, "test_loops_of_2_to_30_s_pass_and_every_planted_seam_fails_for_its_reason")]),
    "no F-08 row for loops (only the aim row of evaluate)":
        (lambda: mock.patch.object(render, "LOOP_F08_MUST_MAX", 1e9),
         [(LoopTest, "test_loops_of_2_to_30_s_pass_and_every_planted_seam_fails_for_its_reason"),
          (LoopTest, "test_a_loop_card_judges_the_wrap_even_without_a_loop_step")]),
    "no gap reading (F-08's fade-to-silence false reading passes)":
        (lambda: mock.patch.object(render, "LOOP_GAP_DB", 1e9),
         [(LoopTest, "test_loops_of_2_to_30_s_pass_and_every_planted_seam_fails_for_its_reason")]),
    "the crossfade guarded for dips only":
        (lambda: mock.patch.object(assemble, "crossfade_level", _dips_only(assemble.crossfade_level)),
         [(LoopTest, "test_the_curve_follows_the_correlation_and_a_wrong_curve_fails_both_ways")]),
    "a gap read against an absolute floor (-60 dBFS)":
        (lambda: mock.patch.object(m, "loop_wrap", _abs_gap(m.loop_wrap)),
         [(LoopTest, "test_the_loop_rows_read_a_quiet_bed_as_the_same_bed_normalised")]),
    "the bar length floored instead of rounded":
        (lambda: mock.patch.object(assemble, "bar_samples", _floored_bars),
         [(LoopTest, "test_loop_music_is_bar_aligned_and_keeps_its_downbeat")]),
    "F1: an aim loop_seam target sets the must F-08 limit (review step 6)":
        (lambda: mock.patch.object(render, "f08_limit", lambda c: (c.get("targets", {}).get("loop_seam", {}).get(
            "max", render.LOOP_F08_MUST_MAX), "card")),
         [(LoopTest, "test_a_card_seam_target_tightens_r26_and_loosens_it_only_as_a_must_with_a_why")]),
    "F1: the card limit never applied (a stricter card limit ignored)":
        (lambda: mock.patch.object(render, "f08_limit", lambda c: (render.LOOP_F08_MUST_MAX, "R-26")),
         [(LoopTest, "test_a_card_seam_target_tightens_r26_and_loosens_it_only_as_a_must_with_a_why")]),
    "R2: rank's use text without the form rows":
        (lambda: mock.patch.object(rank_mod, "form_note", lambda proof: ""),
         [(VariantTest, "test_rank_use_names_the_form_rows_its_proof_leaves_to_render")]),
    "F2: DC removed from the layer's audio (the old automatic dc step)":
        (lambda: mock.patch.object(assemble, "shape_layer", _dc_shaped(assemble.shape_layer)),
         [(LayerTest, "test_a_dc_layer_that_ends_at_zero_is_placed_untouched_and_gains_no_edge_click")]),
    "F2: the as-placed reading uses the mix instead of the layer alone":
        (lambda: _read_the_mix(),
         [(LayerTest, "test_the_logged_transient_is_read_after_placing_and_matches_the_marker")]),
    "R3: no correction after placing (align read on the layer alone)":
        (lambda: mock.patch.object(render, "ALIGN_CORRECTIONS", 0),
         [(LayerTest, "test_the_correction_after_placing_still_lands_a_skewed_reading")]),
    "edge round: layer edges not faded":
        (lambda: mock.patch.object(render, "fade_layer_edges", lambda y, rate: (y, {
            "start": {"faded": False}, "end": {"faded": False}, "attack_share": [None, None]})),
         [(LayerTest, "test_a_layer_that_starts_and_ends_mid_waveform_is_faded_and_does_not_click")]),
    "edge round: the edge-click row always reads 0":
        (lambda: mock.patch.object(render, "layer_edge_clicks", lambda p, off, n, rate: 0),
         [(LayerTest, "test_layer_edge_clicks_are_read_and_must_for_important_cues")]),
    "edge round: the edge-click row always an aim":
        (lambda: mock.patch.object(render, "EDGE_CLICKS_MUST_TIERS", ()),
         [(LayerTest, "test_layer_edge_clicks_are_read_and_must_for_important_cues")]),
    "variants drawn without the seed":
        (lambda: mock.patch.object(assemble.np.random, "RandomState", lambda seed=None: RS(None)),
         [(VariantTest, "test_the_plan_is_seeded_and_spreads_over_the_range")]),
    "variant gains drawn around 0, not kept within max_db of the set's mean":
        (lambda: mock.patch.object(assemble, "centre_gains", lambda gains, max_db: gains),
         [(VariantTest, "test_a_planned_set_passes_r31_as_render_reads_it_over_many_seeds")]),
    "the variant level change not applied":
        (lambda: mock.patch.object(assemble, "variant_plan", _no_gain(assemble.variant_plan)),
         [(VariantTest, "test_variant_files_carry_their_pitch_and_level")]),
    "the family check reads one variant file":
        (lambda: mock.patch.object(render, "family_check", _first_file_only(render.family_check,
                                                                             render.delivered_files)),
         [(VariantTest, "test_a_paid_reveal_family_checks_every_variant_file")]),
    "variants allowed on a tell (SC-12 refusal dropped)":
        (lambda: mock.patch.dict(render.cardmod.KINDS["tell"], {"no_variants": False}),
         [(VariantTest, "test_tells_warnings_and_countdowns_get_no_variants")]),
}


class PlantedFaultTest(unittest.TestCase):
    """Each planted fault must make at least one of its named tests fail; the correct build passes them all."""

    def test_every_planted_fault_is_caught(self):
        survived = []
        for name, (patcher, tests) in FAULTS.items():
            suite = unittest.TestSuite(cls(t) for cls, t in tests)
            with patcher():
                res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
            if res.wasSuccessful():
                survived.append(name)
        self.assertEqual(survived, [], "planted faults that survived")


if __name__ == "__main__":
    unittest.main()
