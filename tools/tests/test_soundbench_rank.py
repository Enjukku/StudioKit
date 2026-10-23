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
        keys = [[int(bool(e["rejected"])), sum(r["must"] and r["result"] != "pass" for r in e["after"]),
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
    def simulate(card, x, rate, raw_rows, flat):
        out = orig(card, x, rate, raw_rows, flat)
        out["rows"] = raw_rows
        return out
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
        (lambda: mock.patch.object(rank, "CLIP_TOP_MS", 1e9),
         ["test_rejected_outright_clipped_near_silent_and_no_band", "test_full_scale_clean_takes_are_not_clipped"]),
    "the clip check reads absolute level only (no own-peak run)":
        (lambda: mock.patch.object(rank, "CLIP_TOP_MS", 0.0),
         ["test_full_scale_clean_takes_are_not_clipped"]),
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
