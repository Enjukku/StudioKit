"""Tests for soundbench `rank` (J020 step 5; editor-design.md section 6).

Rounds are built in temp folders from the realistic fixtures (`fixtures.make_real`: quiet, mid-waveform starts, 480 ms)
with intake records written by the test, as in test_soundbench_render.py; one round goes through a real MP3 encode.
Oracles: the construction of each take (a late start is late, a bass thump has no phone band, a spike eats the
headroom) and the design's level formula computed here from the measures, never copied from rank's output. The
planted-fault test at the end shows each named fault makes these tests fail.
"""

import copy
import io
import json
import os
import subprocess
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest import mock

try:
    import matplotlib  # noqa: F401
    import numpy as np
    import pyloudnorm  # noqa: F401
    import scipy  # noqa: F401
    import soundfile  # noqa: F401
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile, pyloudnorm and matplotlib")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import card as cardmod  # noqa: E402
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import intake, ops, rank, render  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, audio_sha256, file_sha256, read_float32  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
HAS_LAME = bool(FOUND) and "libmp3lame" in sbf.encoders(FOUND.path)

R = 44100
CARD = {"cue": "SFX-R-HIT", "kind": "hit", "category": "sfx", "tier": "minor",
        "level": {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True},
        "targets": {"onset_ms": {"max": 5, "must": True}, "true_peak_dbtp": {"max": -1.0, "must": True},
                    "edge_clicks": {"max": 0, "must": True}, "phone_loss_db": {"max": 12, "must": True}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}


def card_for(cue: str, **changes) -> dict:
    c = copy.deepcopy(CARD)
    c["cue"] = cue
    for k, v in changes.items():
        c[k] = v
    return c


def make_round(root: Path, card: dict, takes: list, rate: int = R, round_no: int = 1, start: int = 1) -> Path:
    """A cue folder with card.json and takes/<cue>.r<k>.t<n>.mp3 (stand-in bytes), masters and intake sidecars."""
    cue = root / card["cue"]
    (cue / "takes").mkdir(parents=True, exist_ok=True)
    (cue / "card.json").write_text(json.dumps(card), encoding="utf-8")
    for n, x in enumerate(takes, start):
        take = cue / "takes" / f"{card['cue']}.r{round_no}.t{n}.mp3"
        take.write_bytes(f"stand-in take {card['cue']} r{round_no} t{n}".encode())
        master = intake.master_path(take)
        fx.write_wav(master, x, rate)
        y, _ = read_float32(master)
        side = {"prompt": "test", "intake": {"take_sha256": file_sha256(take), "master_audio_sha256": audio_sha256(y),
                                             "rate": rate, "decoder": "test (no decode)"}}
        take.with_suffix(".json").write_text(json.dumps(side), encoding="utf-8")
    return cue


def late_hit() -> np.ndarray:
    """The realistic quiet hit after 80 ms of floor-level noise: a late start that `trim` fixes."""
    q = fx.make_real("quiet_hit", R)
    floor = 10 ** ((fx.REAL_PEAKS_DBFS["quiet_hit"] + fx.REAL_FLOOR_DB_RE_PEAK) / 20)
    return np.vstack([floor * np.random.RandomState(5).standard_normal((int(0.08 * R), 2)), q])


def quiet_bass() -> np.ndarray:
    """A bass thump at a real take's level (-30 dBFS): all its energy under 120 Hz, so a phone cue cannot use it."""
    b = fx.make("bass_thump", R, 2)
    return b / np.max(np.abs(b)) * 10 ** (-30 / 20)


def spiky_note() -> np.ndarray:
    """The realistic soft note (-24 dBFS) with a 3-sample spike at -3 dBFS: the spike eats the true-peak headroom."""
    s = fx.make_real("soft_note", R)
    i = int(0.1 * R)
    s[i:i + 3] = 10 ** (-3 / 20)
    return s


def row(entry: dict, target: str, part: str = "after") -> dict:
    return next(r for r in entry[part] if r["target"] == target)


def miss(entry: dict, target: str) -> dict:
    return next(x for x in entry["misses"] if x["target"] == target)


def entry(doc: dict, n: int) -> dict:
    return next(e for e in doc["takes"] if e["n"] == n)


class RankTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_a_realistic_round_is_ranked_with_its_fixes(self):
        cue = make_round(self.d, card_for("SFX-R-HIT"), [quiet_bass(), late_hit(), fx.make_real("quiet_hit", R)])
        doc, code = rank.rank(cue)
        self.assertEqual(code, 0)
        self.assertEqual(doc["round"], 1)
        self.assertEqual(doc["order"][-1], "SFX-R-HIT.r1.t1.mp3")  # the bass thump: a must-miss no step can fix
        bass, late, hit = entry(doc, 1), entry(doc, 2), entry(doc, 3)
        self.assertEqual(miss(bass, "phone_loss_db")["fix"], "prompt")
        self.assertIn("no edit-pass step moves phone_loss_db", miss(bass, "phone_loss_db")["why"])
        self.assertFalse(bass["passes_after_fix"])
        self.assertEqual(miss(late, "onset_ms")["fix"], "fixed")
        self.assertEqual(miss(late, "onset_ms")["by"], "trim")
        self.assertEqual(miss(hit, "edge_clicks")["fix"], "fixed")  # the mid-waveform start: trim's edge fade
        for e in (late, hit):
            self.assertTrue(e["passes_after_fix"], e["must_after"])
            self.assertEqual(miss(e, "level")["fix"], "fixed")  # -55 dBFS F-09 to -24: the gain fits the headroom
            self.assertEqual([s["op"] for s in e["fix"]["steps"]], ["trim", "loudness", "peak"])
        self.assertTrue(doc["proof"]["agrees"])
        self.assertEqual(doc["proof"]["must_failed"], [])
        self.assertEqual(doc["verdict"]["action"], "use")
        top = next(e for e in doc["takes"] if e["take"] == doc["top"])
        self.assertEqual(doc["verdict"]["recipe_edit"], top["fix"]["steps"])
        self.assertEqual(doc["proof"]["recipe_edit"], top["fix"]["steps"])
        self.assertFalse((cue / "out").exists())  # rank never writes delivered files
        self.assertTrue((cue / "report" / "SFX-R-HIT.r1.rank.md").is_file())
        saved = json.loads((cue / "report" / "SFX-R-HIT.r1.rank.json").read_text(encoding="utf-8"))
        self.assertEqual(saved["order"], doc["order"])

    def test_the_order_is_the_documented_key_recomputed_from_the_table(self):
        cue = make_round(self.d, card_for("SFX-R-ORD"), [quiet_bass(), late_hit(), fx.make_real("quiet_hit", R),
                                                         fx.make("clipped", R, 2)])
        doc, _ = rank.rank(cue)
        keys = [[int(bool(e["rejected"])), int(not e["passes_after_fix"]),
                 sum(r["must"] and r["result"] != "pass" for r in e["after"]),
                 sum(not r["must"] and r["result"] != "pass" for r in e["after"]),
                 sum(x["fix"] == "fixed" for x in e["misses"]), sum(r["score"] == "near" for r in e["after"]), e["n"]]
                for e in doc["takes"]]
        self.assertEqual(keys, sorted(keys))
        self.assertEqual([e["rank_key"] for e in doc["takes"]], keys)
        passes = [i for i, e in enumerate(doc["takes"]) if e["passes_after_fix"]]
        fails = [i for i, e in enumerate(doc["takes"]) if not e["passes_after_fix"]]
        self.assertTrue(passes and fails)
        self.assertLess(max(passes), min(fails))  # no must-miss ranks above a pass
        self.assertTrue(doc["takes"][-1]["rejected"])  # the clipped take is last

    def test_a_must_miss_never_ranks_above_a_pass_with_more_aims_and_fixes(self):
        c = card_for("SFX-R-MUST")
        c["targets"]["sound_ms"] = {"max": 300, "must": False}  # every quiet hit misses this aim and needs a cut
        c["targets"]["above_5k"] = {"max": 0.1, "must": False}  # the quiet hit (0.17) misses this aim
        # t1: the bass: no aim misses after its fix, one must miss; t2: the late hit: passes every must, two aims
        cue = make_round(self.d, c, [quiet_bass(), late_hit()])
        doc, code = rank.rank(cue)
        self.assertEqual(code, 0)
        self.assertEqual(doc["order"], ["SFX-R-MUST.r1.t2.mp3", "SFX-R-MUST.r1.t1.mp3"])
        bass = entry(doc, 1)
        self.assertEqual(bass["must_after"], ["phone_loss_db"])

    def test_too_quiet_is_fixable_only_inside_the_true_peak_headroom(self):
        c = card_for("SFX-R-SPIKE", targets={"true_peak_dbtp": {"max": -1.0, "must": True}})
        c["level"]["target"] = -20.0
        clean, spiky = fx.make_real("soft_note", R), spiky_note()
        cue = make_round(self.d, c, [clean, spiky])
        doc, code = rank.rank(cue)
        self.assertEqual(code, 0)
        self.assertEqual(doc["order"][0], "SFX-R-SPIKE.r1.t1.mp3")
        limit = min(ops.PEAK_CEILING_DBTP, -1.0) - ops.PEAK_MARGIN_DB
        for n, x, fits in ((1, clean, True), (2, spiky, False)):
            with self.subTest(take=n):
                y = read_float32(cue / "takes" / f"SFX-R-SPIKE.r1.t{n}.master.wav")[0].astype(np.float64)
                level_in, tp_in = m.level_db(y, R, "F-09"), m.true_peak_db(y)
                gain = -20.0 - level_in
                cut = max(0.0, tp_in + gain - limit)  # the design's formula, from the measures
                e = entry(doc, n)
                lv = e["fix"]["level"]
                self.assertAlmostEqual(lv["gain_needed_db"], gain, delta=0.002)
                self.assertAlmostEqual(lv["headroom_db"], limit - tp_in, delta=0.002)
                self.assertAlmostEqual(lv["simulated_level"], -20.0 - cut, delta=0.06)
                self.assertEqual(lv["fits"], fits)
                self.assertEqual(miss(e, "level")["fix"], "fixed" if fits else "prompt")
        why = miss(entry(doc, 2), "level")["why"]
        self.assertIn("true-peak headroom", why)
        self.assertIn("do not limit transients", why)

    def test_the_headroom_boundary_just_inside_and_just_outside(self):
        x = fx.make_real("soft_note", R)
        level_in, tp_in = m.level_db(x, R, "F-09"), m.true_peak_db(x)
        limit = ops.PEAK_CEILING_DBTP - ops.PEAK_MARGIN_DB
        edge = level_in + (limit - tp_in) + 1.0  # the highest target the gain can reach within a 1 dB tolerance
        for name, target, fits in (("IN", edge - 0.03, True), ("OUT", edge + 0.03, False)):
            with self.subTest(side=name):
                c = card_for(f"SFX-R-EDGE{name}", targets={})
                c["level"]["target"] = round(target, 4)
                doc, code = rank.rank(make_round(self.d, c, [x]))
                self.assertEqual(entry(doc, 1)["fix"]["level"]["fits"], fits)
                self.assertEqual(code, 0 if fits else 1)

    def test_too_loud_is_always_fixable_and_music_gets_the_limit_note(self):
        loud = fx.make_real("soft_note", R) * 10 ** (23 / 20)  # peak -1 dBFS
        c = card_for("SFX-R-LOUD", targets={})
        c["level"]["target"] = -30.0
        doc, code = rank.rank(make_round(self.d, c, [loud]))
        self.assertEqual(code, 0)
        self.assertLess(entry(doc, 1)["fix"]["level"]["gain_needed_db"], 0)
        c = card_for("MUS-R-SPIKE", targets={}, category="music", kind="stinger")
        c["level"]["target"] = -20.0
        doc, code = rank.rank(make_round(self.d, c, [spiky_note()]))
        self.assertEqual(code, 1)
        self.assertIn("`limit` design step", miss(entry(doc, 1), "level")["why"])

    def test_a_long_take_is_cut_and_a_short_one_needs_a_prompt(self):
        c = card_for("SFX-R-LONG")
        c["targets"]["sound_ms"] = {"min": 50, "max": 200, "must": True}
        doc, code = rank.rank(make_round(self.d, c, [fx.make_real("quiet_hit", R)]))
        self.assertEqual(code, 0, entry(doc, 1)["must_after"])
        e = entry(doc, 1)
        self.assertEqual([s["op"] for s in e["fix"]["steps"]], ["trim", "cut", "fade", "loudness", "peak"])
        self.assertEqual(miss(e, "sound_ms")["fix"], "fixed")
        self.assertLessEqual(row(e, "sound_ms")["value"], 200)
        c = card_for("SFX-R-SHORT")
        c["targets"]["sound_ms"] = {"min": 600, "must": True}
        doc, code = rank.rank(make_round(self.d, c, [fx.make_real("quiet_hit", R)]))
        self.assertEqual(code, 1)
        self.assertIn("no edit-pass step adds time", miss(entry(doc, 1), "sound_ms")["why"])

    def test_a_late_long_take_is_cut_on_its_trimmed_length(self):
        c = card_for("SFX-R-LATELONG")
        c["targets"]["sound_ms"] = {"min": 50, "max": 200, "must": True}
        doc, code = rank.rank(make_round(self.d, c, [late_hit()]))  # 80 ms late, 480 ms of sound
        e = entry(doc, 1)
        self.assertEqual(code, 0, e["must_after"])
        cut = next(s for s in e["fix"]["steps"] if s["op"] == "cut")
        # on the trimmed timeline: its F-01 (about 1 ms) + 200 - 1; planned on the untrimmed take it would be 279 or more
        self.assertLess(cut["end_ms"], 210)
        self.assertLessEqual(row(e, "sound_ms")["value"], 200)

    def test_a_miss_the_fix_causes_is_reported(self):
        c = card_for("SFX-R-CAUSE")
        c["targets"]["file_ms"] = {"min": 520, "must": True}  # the late take is 560 ms; trim makes it shorter
        doc, _ = rank.rank(make_round(self.d, c, [late_hit()]))
        e = entry(doc, 1)
        self.assertEqual([i["target"] for i in e["introduced"]], ["file_ms"])
        self.assertFalse(e["passes_after_fix"])

    def test_rejected_outright_clipped_near_silent_and_no_band(self):
        c = card_for("SFX-R-REJ")
        c["targets"]["band_500_5k"] = {"min": 0.3, "must": True}
        silent = fx.make_real("quiet_hit", R) * 10 ** (-34 / 20)  # peak -70 dBFS
        takes = [fx.make("clipped", R, 2), silent, quiet_bass(), fx.make_real("soft_note", R)]
        doc, code = rank.rank(make_round(self.d, c, takes))
        self.assertIn("clipped at the source", entry(doc, 1)["rejected"][0])
        self.assertIn("near-silent", entry(doc, 2)["rejected"][0])
        self.assertTrue(any("no sound in the band" in r for r in entry(doc, 3)["rejected"]))
        self.assertEqual(entry(doc, 4)["rejected"], [])
        self.assertEqual(doc["order"][0], "SFX-R-REJ.r1.t4.mp3")
        for n in (1, 2, 3):
            self.assertIsNone(entry(doc, n)["fix"])  # no fix is claimed for a rejected take
        self.assertEqual(code, 0)

    def test_full_scale_clean_takes_are_not_clipped(self):
        for name, x in (("clean_hit", fx.make("clean_hit", R, 2)), ("soft_note", fx.make_real("soft_note", R)),
                        ("bass_thump", fx.make("bass_thump", R, 2))):
            with self.subTest(fixture=name):
                y = x / np.max(np.abs(x)) * 10 ** (-0.1 / 20)
                self.assertFalse(rank.clip_reading(y, R)["clipped"], rank.clip_reading(y, R))
        self.assertTrue(rank.clip_reading(fx.make("clipped", R, 2), R)["clipped"])

    @unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: the MP3 clip test skipped")
    def test_clipped_broadband_takes_after_mp3_are_rejected_at_128k_and_192k(self):
        """F1 (review-rank): clipping happens at full scale; the MP3 decoder's overshoot must not hide it. Broadband
        real-like takes hard-clipped at full scale, encoded at ElevenLabs' two MP3 rates and decoded at intake."""
        cases = (("quiet_whoosh", 12, True), ("quiet_whoosh", 8, True), ("soft_note", 6, True), ("soft_note", 12, True), ("quiet_hit", 12, True),
                 ("quiet_whoosh", 0, False), ("soft_note", 0, False), ("quiet_hit", 0, False),
                 ("quiet_hit", 6, False))  # known false reading: a short crack clipped by 6 dB reads ~2 ms, not caught
        for name, gain, want in cases:
            for kbps in (128, 192):
                with self.subTest(fixture=name, gain=gain, kbps=kbps):
                    x = fx.make_real(name, R)
                    x = x / np.max(np.abs(x)) * 10 ** ((gain if gain else -0.1) / 20)
                    y = np.clip(x, -1.0, 1.0)
                    wav = fx.write_wav(self.d / f"{name}{gain}{kbps}.wav", y, R)
                    mp3 = self.d / f"{name}{gain}{kbps}.mp3"
                    subprocess.run([str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i",
                                    str(wav), "-c:a", "libmp3lame", "-b:a", f"{kbps}k", str(mp3)], check=True)
                    intake.decode_take(mp3, sidecar=self.d / f"{name}{gain}{kbps}.side.json")
                    z = read_float32(intake.master_path(mp3))[0].astype(np.float64)
                    self.assertEqual(rank.clip_reading(z, R)["clipped"], want, rank.clip_reading(z, R))

    @unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: the long-take clip test skipped")
    def test_the_clip_reading_does_not_grow_with_the_take_length(self):
        """R2-2 (review-rank round 2): clean long takes near full scale are not rejected, and long clipped takes still
        are, after MP3 at 128k and 192k. The pad is the reviewer's e7 case (it read 12.83 ms in total and was
        rejected); the note loop is 20 repeats of the realistic soft note (9.6 s)."""
        t = np.arange(int(2.0 * R)) / R
        env = np.minimum(1, t / 0.2) * np.minimum(1, (2.0 - t) / 0.3)
        chord = env * (np.sin(2 * np.pi * 220 * t) + 0.5 * np.sin(2 * np.pi * 277.2 * t) + 0.3 * np.sin(2 * np.pi * 329.6 * t))
        pad = np.stack([chord, chord], axis=1)
        loop = np.vstack([fx.make_real("soft_note", R)] * 20)
        whoosh = np.vstack([fx.make_real("quiet_whoosh", R)] * 4)
        full = lambda y: y / np.max(np.abs(y)) * 10 ** (-0.1 / 20)  # noqa: E731
        clip = lambda y, g: np.clip(y / np.max(np.abs(y)) * 10 ** (g / 20), -1.0, 1.0)  # noqa: E731
        for name, y, want in (("pad 2 s", full(pad), False), ("note loop 9.6 s", full(loop), False),
                              ("whoosh x4 clean", full(whoosh), False), ("whoosh x4 +12 dB", clip(whoosh, 12), True)):
            for kbps in (128, 192):
                with self.subTest(case=name, kbps=kbps):
                    tag = f"{name.replace(' ', '_').replace('+', 'p')}{kbps}"
                    wav = fx.write_wav(self.d / f"{tag}.wav", y, R)
                    mp3 = self.d / f"{tag}.mp3"
                    subprocess.run([str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i",
                                    str(wav), "-c:a", "libmp3lame", "-b:a", f"{kbps}k", str(mp3)], check=True)
                    intake.decode_take(mp3, sidecar=self.d / f"{tag}.side.json")
                    z = read_float32(intake.master_path(mp3))[0].astype(np.float64)
                    self.assertEqual(rank.clip_reading(z, R)["clipped"], want, rank.clip_reading(z, R))

    def test_level_derivation_uses_the_gain_loudness_applied_for_gated_measures(self):
        """F2 (review-rank): F-13a and LUFS-I gate blocks at -70 LUFS, so on a quiet take the gain loudness applies is
        not target - level_in. Rank must rank the round (no refusal) and its derivation must match the simulation."""
        quiet = fx.make_real("quiet_hit", R) * 10 ** (-12 / 20)  # peak -48 dBFS: 2.6 dB non-linear at the -70 gate
        for measure in ("F-09", "F-13a", "LUFS-I"):
            with self.subTest(measure=measure):
                c = card_for(f"SFX-R-GATE{measure.replace('-', '')}", targets={"true_peak_dbtp": {"max": -1.0, "must": True}})
                c["level"] = {"measure": measure, "target": -20.0, "tolerance": 1.0, "must": True}
                doc, code = rank.rank(make_round(self.d, c, [quiet]))
                lv = entry(doc, 1)["fix"]["level"]
                self.assertLessEqual(abs(lv["predicted_level"] - lv["simulated_level"]), rank.LEVEL_AGREE_DB)
                y = read_float32(self.d / c["cue"] / "takes" / f"{c['cue']}.r1.t1.master.wav")[0].astype(np.float64)
                self.assertAlmostEqual(lv["level_in"], m.level_db(y, R, measure), delta=0.002)
                self.assertIn(code, (0, 1))

    def test_a_take_that_passes_untouched_is_never_told_to_regenerate(self):
        """F3 (review-rank, the thump-4 t2 case): raw level passes, raw true peak between the peak limit (-1.5) and
        the card's max (-1.0), an aim edge miss. The all-steps plan (trim, fade, loudness, peak) cuts the level under
        its tolerance; the take with no step passes every must, so rank says use."""
        x = fx.make_real("soft_note", R)  # starts and ends mid-waveform: an edge-click aim miss
        x = x / m.true_peak_db(x) ** 0 * 10 ** ((-1.2 - m.true_peak_db(x)) / 20)  # true peak -1.2 dBTP
        level = m.level_db(x, R, "F-09")
        c = card_for("SFX-R-THUMP4", targets={"true_peak_dbtp": {"max": -1.0, "must": True},
                                              "edge_clicks": {"max": 0, "must": False}})
        c["level"]["target"] = round(level + 0.9, 3)  # raw level passes, 0.1 dB inside a 1 dB tolerance
        doc, code = rank.rank(make_round(self.d, c, [x]))
        e = entry(doc, 1)
        self.assertEqual(code, 0, e["must_after"])
        self.assertEqual(e["must_after"], [])
        self.assertTrue(e["fix"]["dropped_aim_fixes"])  # the edge fix it left out is reported
        self.assertTrue(doc["proof"]["agrees"])

    def test_a_sample_peak_max_sets_the_peak_ceiling(self):
        """F4 (review-rank): a card's sample_peak_dbfs max is a ceiling the fix must respect."""
        x = fx.make_real("soft_note", R)  # crest about 12.8 dB: F-09 -15.5 puts the peak near -2.7 dBFS
        c = card_for("SFX-R-SPMAX", targets={"sample_peak_dbfs": {"max": -3.0, "must": True}})
        c["level"]["target"] = -15.5
        doc, code = rank.rank(make_round(self.d, c, [x]))
        e = entry(doc, 1)
        self.assertEqual(code, 0, e["must_after"])
        peak = next(s for s in e["fix"]["steps"] if s["op"] == "peak")
        self.assertEqual(peak["ceiling_dbtp"], -3.0)
        self.assertLessEqual(row(e, "sample_peak_dbfs")["value"], -3.0)
        self.assertEqual(e["fix"]["level"]["peak_limit_dbtp"], -3.0 - ops.PEAK_MARGIN_DB)

    def test_a_take_whose_fix_was_refused_never_sorts_above_a_pass(self):
        """F5 (review-rank): a refused fix with no raw must miss and no aim miss against a passing take with two aim
        misses: the passing take is first."""
        refused = {"rejected": [], "passes_after_fix": False, "must_after": [], "aim_after": [], "fixed": [],
                   "near_after": [], "n": 1}
        passing = {"rejected": [], "passes_after_fix": True, "must_after": [], "aim_after": ["sound_ms", "flatness"],
                   "fixed": ["level"], "near_after": [], "n": 2}
        self.assertEqual([e["n"] for e in rank.order([refused, passing])], [2, 1])

    def test_a_refused_fix_names_its_reason(self):
        """F5 (review-rank): LUFS-I refuses a fix that leaves the file under 0.4 s; the take does not pass (its raw
        level misses) and the level miss says why the fix was refused."""
        c = card_for("SFX-R-LUFSCUT")
        c["level"] = {"measure": "LUFS-I", "target": -20.0, "tolerance": 1.0, "must": True}
        c["targets"]["file_ms"] = {"max": 350, "must": True}  # the cut makes the file 350 ms: under 0.4 s
        doc, code = rank.rank(make_round(self.d, c, [fx.make_real("quiet_hit", R)]))
        e = entry(doc, 1)
        self.assertFalse(e["passes_after_fix"])
        self.assertEqual(code, 1)
        self.assertIn("0.4 s", miss(e, "level")["why"])
        self.assertIn("refused", miss(e, "level")["why"])

    def test_a_take_over_full_scale_keeps_a_plan_render_can_export(self):
        """R2-1 (review-rank round 2, e6 case c): a master whose sample peak reaches full scale passes every must
        untouched, but render cannot export it with no step. The no-step plan is refused with export's own reason
        and the take keeps loudness + peak; its proof render agrees."""
        x = fx.make_real("soft_note", R)
        x = x / np.max(np.abs(x)) * 1.02  # an MP3 decode over full scale (11 of 62 real masters reach 0 dBTP)
        c = card_for("SFX-R-OVERFS", targets={})
        # the level passes untouched (1.2 dB off, tolerance 1.5); after loudness the peak cut to -1.5 dBTP is about
        # 0.5 dB, so loudness + peak also lands inside
        c["level"] = {**c["level"], "target": round(m.level_db(x, R, "F-09") - 1.2, 3), "tolerance": 1.5}
        doc, code = rank.rank(make_round(self.d, c, [x]))
        e = entry(doc, 1)
        self.assertEqual(code, 0, e["fix_error"])
        self.assertEqual([s_["op"] for s_ in e["fix"]["steps"]], ["loudness", "peak"])
        self.assertTrue(any(p_["plan"] == "none" and "reaches full scale" in p_["error"]
                            for p_ in e["fix"]["refused_plans"]))
        self.assertTrue(doc["proof"]["agrees"])

    def test_a_round_where_no_take_passes_exits_1_without_a_proof(self):
        """R2-1: the proof render runs only for a top take that passes; a failing round is regenerate (exit 1)."""
        c = card_for("SFX-R-NOPASS")
        doc, code = rank.rank(make_round(self.d, c, [quiet_bass()]))  # a phone cue: no step fixes the phone loss
        self.assertEqual((code, doc["verdict"]["action"]), (1, "regenerate"))
        self.assertIsNone(doc["proof"])

    def test_a_take_render_cannot_export_is_refused_with_renders_reason(self):
        """R2-1: every kept plan either renders or is refused by rank with the reason render would give. A 96 kHz
        take: render refuses it whatever the steps (Roblox takes up to 48 kHz), so every plan is refused, the take
        does not pass and its misses carry the reason; the round exits 1, never 2."""
        x = fx.make_real("soft_note", 96000)
        doc, code = rank.rank(make_round(self.d, card_for("SFX-R-96K"), [x], rate=96000))
        e = entry(doc, 1)
        self.assertEqual(code, 1)
        self.assertFalse(e["passes_after_fix"])
        self.assertIn("over Roblox's 48000 Hz", miss(e, "level")["why"])
        self.assertIsNone(doc["proof"])

    def test_regenerate_lists_what_the_prompt_must_change_and_round_3_goes_to_the_owner(self):
        c = card_for("SFX-R-REGEN")
        cue = make_round(self.d, c, [quiet_bass(), quiet_bass() * 0.5, quiet_bass() * 0.25])
        doc, code = rank.rank(cue)
        self.assertEqual(code, 1)
        v = doc["verdict"]
        self.assertEqual(v["action"], "regenerate")
        top = v["prompt_must_change"][0]
        self.assertEqual((top["target"], top["must"], top["takes_missing"], top["of"]), ("phone_loss_db", True, 3, 3))
        self.assertEqual(top["closest"]["direction"], "too high")
        make_round(self.d, c, [quiet_bass(), quiet_bass() * 0.5, quiet_bass() * 0.25], round_no=3)
        doc, code = rank.rank(cue)
        self.assertEqual((doc["round"], code, doc["verdict"]["action"]), (3, 1, "owner"))
        self.assertIn("J020-D7", doc["verdict"]["say"])
        doc, _ = rank.rank(cue, round_no=1)
        self.assertEqual(doc["round"], 1)
        make_round(self.d, c, [quiet_bass()], round_no=4)
        with self.assertRaisesRegex(SoundbenchError, "at most 3 rounds"):
            rank.rank(cue)
        with self.assertRaisesRegex(SoundbenchError, "no takes"):
            rank.rank(cue, round_no=2)

    def test_takes_per_round_by_tier_is_a_warning(self):
        doc, _ = rank.rank(make_round(self.d, card_for("SFX-R-FEW", tier="important"), [fx.make_real("quiet_hit", R)]))
        self.assertIn("gets 6 per round (J020-D9)", doc["warnings"][0])
        self.assertTrue(any(p.endswith("rank-after.png") for p in doc["pictures"]))  # important: the top take drawn

    def test_a_changed_take_is_refused(self):
        cue = make_round(self.d, card_for("SFX-R-G1"), [fx.make_real("quiet_hit", R)])
        (cue / "takes" / "SFX-R-G1.r1.t1.mp3").write_bytes(b"changed")
        with self.assertRaisesRegex(SoundbenchError, "G-1"):
            rank.rank(cue)

    def test_a_family_member_is_checked_as_render_does_and_its_state_untouched(self):
        a = card_for("SFX-R-EGGA", family={"id": "egg", "paid_reveal": True, "siblings": ["SFX-R-EGGB"]})
        b = card_for("SFX-R-EGGB", family={"id": "egg", "paid_reveal": True, "siblings": ["SFX-R-EGGA"]})
        cue_a = make_round(self.d, a, [fx.make_real("quiet_hit", R)])
        make_round(self.d, b, [fx.make_real("quiet_hit", R)])
        state = self.d / "egg.family.json"
        state.write_text('{"result": "pass"}', encoding="utf-8")
        doc, code = rank.rank(cue_a)
        self.assertEqual(code, 0)
        self.assertTrue(doc["proof"]["agrees"])
        self.assertIn("render checks it", doc["family"]["note"])
        self.assertEqual(state.read_text(encoding="utf-8"), '{"result": "pass"}')
        self.assertFalse((cue_a / "out").exists())
        b["family"]["siblings"] = []  # one-sided now: refused before any audio, as render refuses it
        (self.d / "SFX-R-EGGB" / "card.json").write_text(json.dumps(b), encoding="utf-8")
        with self.assertRaisesRegex(SoundbenchError, "refused"):
            rank.rank(cue_a)

    def test_every_target_has_a_near_margin(self):
        self.assertEqual(set(cardmod.TARGETS) | {"level", "form.loop"}, set(rank.NEAR))

    def test_command_line_exit_codes(self):
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        run = lambda cue: subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "rank", str(cue)],  # noqa: E731
                                         cwd=str(ROOT), capture_output=True, text=True, env=env)
        good = make_round(self.d, card_for("SFX-R-CLI0"), [fx.make_real("quiet_hit", R)])
        p = run(good)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertIn("verdict:", p.stdout)
        self.assertEqual(run(make_round(self.d, card_for("SFX-R-CLI1"), [quiet_bass()])).returncode, 1)
        (good / "card.json").write_text("{", encoding="utf-8")
        p = run(good)
        self.assertEqual(p.returncode, 2)
        self.assertIn("not valid JSON", p.stderr)

    @unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: the MP3 rank test skipped")
    def test_a_round_through_a_real_mp3_encode(self):
        c = card_for("SFX-R-MP3")
        cue = self.d / c["cue"]
        (cue / "takes").mkdir(parents=True)
        (cue / "card.json").write_text(json.dumps(c), encoding="utf-8")
        for n, x in enumerate((fx.make_real("quiet_hit", R), fx.make("clipped", R, 2), late_hit()), 1):
            wav = fx.write_wav(self.d / f"src{n}.wav", x, R)
            mp3 = cue / "takes" / f"{c['cue']}.r1.t{n}.mp3"
            subprocess.run([str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", str(wav),
                            "-c:a", "libmp3lame", "-b:a", "128k", str(mp3)], check=True)
            intake.decode_take(mp3, requested_ms=500)
        doc, code = rank.rank(cue)
        self.assertEqual(code, 0)
        self.assertIn("clipped at the source", entry(doc, 2)["rejected"][0])  # clipping survives the MP3 round trip
        self.assertTrue(entry(doc, 1)["passes_after_fix"] and entry(doc, 3)["passes_after_fix"])
        self.assertTrue(doc["proof"]["agrees"])


# ------------------------------------------------------------------------------------------------- planted faults

def _no_peak_plan(orig):
    def plan(*a, **k):
        return [s for s in orig(*a, **k) if s["op"] != "peak"]
    return plan


def _flag_fixed_when_a_step_ran(orig):
    def classify(card, raw_rows, fix):
        misses, intro = orig(card, raw_rows, fix)
        for x in misses:
            if fix and x["fix"] == "prompt":
                x.update({"fix": "fixed", "by": "planted"})
        return misses, intro
    return classify


def _score_raw_as_after(orig):
    def simulate(card, x, rate, steps, raw_rows):
        out = orig(card, x, rate, steps, raw_rows)
        out["rows"] = raw_rows
        return out
    return simulate


def _clip_against_own_peak(orig):
    def clip_reading(x, rate):
        return orig(np.asarray(x) / np.max(np.abs(x)), rate)  # the decoded overshoot becomes the reference again
    return clip_reading


def _gain_from_the_target(card, y_pre, y_loud, rate):
    return card["level"]["target"] - m.level_db(y_pre, rate, card["level"]["measure"])


def _old_gain(orig_simulate):
    def simulate(card, x, rate, steps, raw_rows):
        with mock.patch.object(rank, "applied_gain_db",
                               lambda before, after: _gain_from_the_target(card, before, after, rate)):
            return orig_simulate(card, x, rate, steps, raw_rows)
    return simulate


def _cut_planned_before_trim(orig):
    def apply(passes, card, ctx, x, rate):
        if [s["op"] for _, seq in passes for s in seq] == ["trim", "export"]:
            return x, []  # rank's look at the trimmed length now sees the untrimmed take
        return orig(passes, card, ctx, x, rate)
    return apply


FAULTS = {
    "fixability without the headroom check (peak dropped from the fix)":
        (lambda: mock.patch.object(rank, "fix_plan", _no_peak_plan(rank.fix_plan)),
         ["test_too_quiet_is_fixable_only_inside_the_true_peak_headroom",
          "test_the_headroom_boundary_just_inside_and_just_outside"]),
    "the order reversed":
        (lambda: mock.patch.object(rank, "order", lambda es: sorted(_keyed(es), key=lambda e: e["rank_key"],
                                                                    reverse=True)),
         ["test_the_order_is_the_documented_key_recomputed_from_the_table",
          "test_a_realistic_round_is_ranked_with_its_fixes"]),
    "a must-miss ranked above a pass (must count left out of the key)":
        (lambda: mock.patch.object(rank, "rank_key", lambda e: [int(bool(e["rejected"])), 0, len(e["aim_after"]),
                                                                len(e["fixed"]), len(e["near_after"]), e["n"]]),
         ["test_a_must_miss_never_ranks_above_a_pass_with_more_aims_and_fixes"]),
    "a miss counted fixed without measuring again":
        (lambda: mock.patch.object(rank, "classify", _flag_fixed_when_a_step_ran(rank.classify)),
         ["test_too_quiet_is_fixable_only_inside_the_true_peak_headroom",
          "test_a_long_take_is_cut_and_a_short_one_needs_a_prompt"]),
    "the after-fix rows taken from the raw take":
        (lambda: mock.patch.object(rank, "simulate", _score_raw_as_after(rank.simulate)),
         ["test_a_realistic_round_is_ranked_with_its_fixes"]),
    "the clip check off":
        (lambda: mock.patch.object(rank, "CLIP_MS", 1e9),
         ["test_rejected_outright_clipped_near_silent_and_no_band", "test_full_scale_clean_takes_are_not_clipped"]),
    "the clip check at any time near full scale (no 10 ms run)":
        (lambda: mock.patch.object(rank, "CLIP_MS", 0.0),
         ["test_full_scale_clean_takes_are_not_clipped"]),
    "F1: the clip check measured against the decoded peak":
        (lambda: mock.patch.object(rank, "clip_reading", _clip_against_own_peak(rank.clip_reading)),
         ["test_clipped_broadband_takes_after_mp3_are_rejected_at_128k_and_192k"]),
    "F2: the level gain taken as target - level_in":
        (lambda: mock.patch.object(rank, "simulate", _old_gain(rank.simulate)),
         ["test_level_derivation_uses_the_gain_loudness_applied_for_gated_measures"]),
    "F3: only the all-steps plan scored":
        (lambda: mock.patch.object(rank, "PLAN_MODES", ("all",)),
         ["test_a_take_that_passes_untouched_is_never_told_to_regenerate"]),
    "F4: the peak ceiling from the true-peak max only":
        (lambda: mock.patch.object(rank, "peak_ceiling", lambda card: min(
            [-1.0] + [card["targets"][k]["max"] for k in ("true_peak_dbtp",) if k in card.get("targets", {})])),
         ["test_a_sample_peak_max_sets_the_peak_ceiling"]),
    "F5: passes left out of the order key":
        (lambda: mock.patch.object(rank, "rank_key", lambda e: [int(bool(e["rejected"])), len(e["must_after"]),
                                                                len(e["aim_after"]), len(e["fixed"]),
                                                                len(e["near_after"]), e["n"]]),
         ["test_a_take_whose_fix_was_refused_never_sorts_above_a_pass"]),
    "F5: a refused fix without its reason":
        (lambda: mock.patch.object(rank, "_why", lambda card, r, fix, a: rank._why_kept(card, r, fix, a)
                                   if fix else "rejected"),
         ["test_a_refused_fix_names_its_reason"]),
    "R2-1: plans kept without the export check":
        (lambda: mock.patch.object(rank, "exportmod", types.SimpleNamespace(check_exportable=lambda *a: None)),
         ["test_a_take_over_full_scale_keeps_a_plan_render_can_export",
          "test_a_take_render_cannot_export_is_refused_with_renders_reason"]),
    "R2-1: the proof run for a top take that does not pass":
        (lambda: mock.patch.object(rank, "needs_proof", lambda top: not top["rejected"]),
         ["test_a_round_where_no_take_passes_exits_1_without_a_proof"]),
    "R2-2: the clip reading in total (a window longer than any take)":
        (lambda: mock.patch.object(rank, "CLIP_WINDOW_MS", 1e9),
         ["test_the_clip_reading_does_not_grow_with_the_take_length"]),
    "R2-2: a window too short for a clipped swell (50 ms)":
        (lambda: mock.patch.object(rank, "CLIP_WINDOW_MS", 50.0),
         ["test_the_clip_reading_does_not_grow_with_the_take_length",
          "test_clipped_broadband_takes_after_mp3_are_rejected_at_128k_and_192k"]),
    "near-silent set at -20 dBFS (rejects real quiet takes)":
        (lambda: mock.patch.object(rank, "NEAR_SILENT_DBFS", -20.0),
         ["test_a_realistic_round_is_ranked_with_its_fixes"]),
    "the cut placed 50 ms past the maximum":
        (lambda: mock.patch.object(rank, "CUT_INSIDE_MS", -50.0),
         ["test_a_long_take_is_cut_and_a_short_one_needs_a_prompt"]),
    "the cut planned on the length before trim":
        (lambda: mock.patch.object(render, "apply_steps", _cut_planned_before_trim(render.apply_steps)),
         ["test_a_late_long_take_is_cut_on_its_trimmed_length"]),
    "round 4 allowed":
        (lambda: mock.patch.object(rank, "MAX_ROUNDS", 4),
         ["test_regenerate_lists_what_the_prompt_must_change_and_round_3_goes_to_the_owner"]),
}


def _keyed(es):
    for e in es:
        e["rank_key"] = rank.rank_key(e)
    return es


class PlantedFaultTest(unittest.TestCase):
    """Each planted fault must make at least one of its named tests fail; the correct build passes them all."""

    def test_every_planted_fault_is_caught(self):
        caught = {}
        for name, (patcher, tests) in FAULTS.items():
            suite = unittest.TestSuite(RankTest(t) for t in tests)
            with patcher():
                res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
            caught[name] = not res.wasSuccessful()
        self.assertEqual([n for n, c in caught.items() if not c], [], "planted faults that survived")


if __name__ == "__main__":
    unittest.main()
