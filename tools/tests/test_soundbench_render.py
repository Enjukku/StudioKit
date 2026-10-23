"""Tests for soundbench card.json / recipe.json checks and the two-pass `render` (J020 step 3).

Cue folders are built in temp folders. Most use a take whose intake record is written by the test (so render logic is
tested without ffmpeg); one goes through a real MP3 encode and intake. G-1: two separate processes render the same
recipe to the same pre-encode audio hash.
"""

import copy
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
    import soundfile as sf
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile, pyloudnorm and matplotlib")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import card as cardmod  # noqa: E402
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import intake, render  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, audio_sha256, file_sha256, read_float32  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
HAS_LAME = bool(FOUND) and "libmp3lame" in sbf.encoders(FOUND.path)

CARD = {"cue": "SFX-T-HIT", "kind": "hit", "category": "sfx", "tier": "minor",
        "level": {"measure": "F-09", "target": -27.0, "tolerance": 0.5, "must": True},  # fits a hit's ~24 dB crest
        "targets": {"onset_ms": {"max": 3, "must": True}, "true_peak_dbtp": {"max": -1.0, "must": True},
                    "sound_ms": {"min": 100, "max": 600, "must": False}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}
RECIPE = {"cue": "SFX-T-HIT", "take": "takes/SFX-T-HIT.r1.t1.mp3",
          "design": [{"op": "dc"}, {"op": "highpass", "hz": 60}],
          "edit": [{"op": "peak"}, {"op": "loudness"}, {"op": "fade", "out_ms": 20}, {"op": "trim"},
                   {"op": "cut", "after_sound_ms": 30}]}


def make_cue(root: Path, x: np.ndarray, rate: int, card: dict, recipe: dict) -> Path:
    """A cue folder: card, recipe, a take file, its master WAV and a sidecar with the intake record."""
    cue = root / card["cue"]
    takes = cue / "takes"
    takes.mkdir(parents=True, exist_ok=True)
    take = cue / recipe["take"]
    take.write_bytes(b"stand-in take bytes for " + card["cue"].encode())
    master = intake.master_path(take)
    fx.write_wav(master, x, rate)
    y, _ = read_float32(master)
    side = {"prompt": "test", "intake": {"take_sha256": file_sha256(take), "master_audio_sha256": audio_sha256(y),
                                         "rate": rate, "decoder": "test (no decode)"}}
    take.with_suffix(".json").write_text(json.dumps(side), encoding="utf-8")
    (cue / "card.json").write_text(json.dumps(card), encoding="utf-8")
    (cue / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
    return cue


def named(card: dict, recipe: dict, cue: str) -> tuple[dict, dict]:
    c, r = copy.deepcopy(card), copy.deepcopy(recipe)
    c["cue"] = r["cue"] = cue
    r["take"] = f"takes/{cue}.r1.t1.mp3"
    return c, r


class CardTest(unittest.TestCase):
    def test_a_good_card_and_recipe_pass(self):
        cardmod.check_card(copy.deepcopy(CARD))
        cardmod.check_recipe(copy.deepcopy(RECIPE))

    def test_every_wrong_field_is_named(self):
        cases = [
            (("kind",), "drum", "card.kind"), (("category",), "fx", "card.category"),
            (("level", "measure"), "LUFS", "card.level.measure"), (("level", "target"), float("nan"), "finite"),
            (("level", "tolerance"), -1, "0 or more"), (("targets", "onset_ms", "must"), "yes", "true or false"),
            (("targets", "sound_ms", "min"), 700, "above max"), (("targets", "onsets_ms"), {"max": 1, "must": True},
                                                                 "unknown target"),
            (("targets", "onset_ms", "binds_to"), "peak", "binds_to"), (("tiers",), "minor", "unknown field"),
            (("playback", "space"), "3D", "falloff"), (("form",), {"variants": 2}, None),
            (("cue",), "a/b", "cue id"), (("targets", "true_peak_dbtp"), {"must": True}, "min, max"),
        ]
        for path, value, why in cases:
            with self.subTest(path=path):
                c = copy.deepcopy(CARD)
                d = c
                for k in path[:-1]:
                    d = d[k]
                d[path[-1]] = value
                if why is None:
                    cardmod.check_card(c)  # variants on a hit are allowed
                    continue
                with self.assertRaisesRegex(SoundbenchError, why):
                    cardmod.check_card(c)

    def test_no_variants_for_tells_warnings_and_countdowns(self):
        for kind in ("tell", "warning", "countdown"):
            c = {**copy.deepcopy(CARD), "kind": kind, "form": {"variants": 3}}
            with self.assertRaisesRegex(SoundbenchError, "SC-12"):
                cardmod.check_card(c)

    def test_onset_binding_by_kind_and_override(self):
        self.assertEqual(cardmod.onset_binding(CARD), "main_transient")
        for kind in ("tell", "whoosh", "riser", "loop_bed"):
            self.assertEqual(cardmod.onset_binding({**CARD, "kind": kind, "targets": {}}), "F-01")
        c = copy.deepcopy(CARD)
        c["targets"]["onset_ms"]["binds_to"] = "F-01"
        self.assertEqual(cardmod.target_key(c, "onset_ms"), "F-01_onset_ms")

    def test_recipe_checks(self):
        for change, why in ((lambda r: r["edit"].append({"op": "trim"}), "more than once"),
                            (lambda r: r["edit"].append({"op": "eq"}), "not an edit step"),
                            (lambda r: r["design"].append({"op": "trim"}), "belongs in recipe.edit"),
                            (lambda r: r.update(take="../other/x.mp3"), "inside the cue folder"),
                            (lambda r: r.update(take="takes/x.wav"), ".mp3"),
                            (lambda r: r["design"].append({"op": "eq", "why": ""}), "non-empty reason"),
                            (lambda r: r.update(extra=1), "unknown field")):
            with self.subTest(why=why):
                r = copy.deepcopy(RECIPE)
                change(r)
                with self.assertRaisesRegex(SoundbenchError, why):
                    cardmod.check_recipe(r)


class RenderTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def test_render_reaches_the_card_and_logs_every_step(self):
        for rate, ch in ((44100, 2), (48000, 1)):
            with self.subTest(rate=rate, ch=ch):
                c, r = named(CARD, RECIPE, f"SFX-T-HIT{rate}{ch}")
                x = fx.make("late_hit", rate, ch) * 0.4
                cue = make_cue(self.d, x, rate, c, r)
                doc, code = render.render(cue)
                self.assertEqual(code, 0, doc["must_failed"])
                out = cue / "out" / f"{c['cue']}.flac"
                info = sf.info(str(out))
                self.assertEqual((info.format, info.samplerate, info.channels), ("FLAC", rate, ch))
                y, _ = read_float32(out)
                self.assertAlmostEqual(m.level_db(y, rate, "F-09"), -27.0, delta=0.05)
                self.assertLessEqual(m.true_peak_db(y), -1.0)
                self.assertEqual(doc["edit_order"], ["trim", "cut", "fade", "loudness", "peak", "export"])
                self.assertTrue(doc["edit_reordered"])
                self.assertEqual([s["op"] for s in doc["steps"]], ["dc", "highpass", "trim", "cut", "fade", "loudness",
                                                                   "peak"])
                for s in doc["steps"]:
                    self.assertIn("before", s)
                    self.assertIn("after", s)
                    self.assertIn("params", s)
                trim = next(s for s in doc["steps"] if s["op"] == "trim")
                self.assertIn("lead_in_ms", trim["info"])
                log = json.loads((cue / "out" / f"{c['cue']}.log.json").read_text(encoding="utf-8"))
                self.assertEqual(log["export"]["audio_sha256_float32"], doc["export"]["audio_sha256_float32"])
                self.assertTrue((cue / "report" / f"{c['cue']}.render.md").is_file())
                self.assertFalse((cue / "report" / f"{c['cue']}.after.png").exists())  # all passed, minor: no picture

    def test_a_must_miss_exits_1_writes_the_file_and_a_picture(self):
        c, r = named(CARD, RECIPE, "SFX-T-SPIKY")
        c["level"]["target"] = -8.0  # the spiky hit cannot reach it under the true-peak ceiling (review-1 #9)
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 2), 44100, c, r)
        doc, code = render.render(cue)
        self.assertEqual(code, 1)
        self.assertIn("level", doc["must_failed"])
        self.assertTrue((cue / "out" / "SFX-T-SPIKY.flac").is_file())
        self.assertTrue((cue / "report" / "SFX-T-SPIKY.after.png").is_file())
        level = next(t for t in doc["targets"] if t["target"] == "level")
        self.assertEqual(level["result"], "miss")

    def test_a_changed_take_or_master_is_refused(self):
        c, r = named(CARD, RECIPE, "SFX-T-CHANGED")
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 1), 44100, c, r)
        take = cue / r["take"]
        take.write_bytes(take.read_bytes() + b"!")
        with self.assertRaisesRegex(SoundbenchError, "original take changed"):
            render.render(cue)
        c, r = named(CARD, RECIPE, "SFX-T-MASTER")
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 1), 44100, c, r)
        fx.write_wav(intake.master_path(cue / r["take"]), fx.make("clean_hit", 44100, 1) * 0.5, 44100)
        with self.assertRaisesRegex(SoundbenchError, "differs from the one decoded"):
            render.render(cue)

    def test_order_and_params_are_checked_before_any_audio(self):
        c, r = named(CARD, RECIPE, "SFX-T-ORDER")
        r["design"] = [{"op": "eq", "bands": [{"type": "bell", "hz": 300, "gain_db": -2}]}, {"op": "dc"}]
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 1), 44100, c, r)
        with self.assertRaisesRegex(SoundbenchError, "SC-09"):
            render.render(cue)
        self.assertFalse((cue / "out").exists())
        r["design"] = [{"op": "highpass", "hz": 5}]
        (cue / "recipe.json").write_text(json.dumps(r), encoding="utf-8")
        with self.assertRaisesRegex(SoundbenchError, "outside"):
            render.render(cue)

    def test_cue_ids_must_agree(self):
        c, r = named(CARD, RECIPE, "SFX-T-IDS")
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 1), 44100, c, r)
        r["cue"] = "SFX-OTHER"
        (cue / "recipe.json").write_text(json.dumps(r), encoding="utf-8")
        with self.assertRaisesRegex(SoundbenchError, "cue ids differ"):
            render.render(cue)

    def test_form_key_and_loop_targets(self):
        c, r = named(CARD, RECIPE, "SFX-T-FORM")
        c["form"] = {"mono": True}
        c["key"] = {"root": "A", "scale": "major", "must": False}
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 2) * 0.4, 44100, c, r)
        doc, code = render.render(cue)
        rows = {t["target"]: t for t in doc["targets"]}
        self.assertEqual(rows["form.mono"]["result"], "miss")  # stereo out, card says mono: a must
        self.assertEqual(code, 1)
        self.assertIn(rows["key"]["result"], ("pass", "miss"))  # E4 body: not in A major
        r["edit"].append({"op": "mono"})
        (cue / "recipe.json").write_text(json.dumps(r), encoding="utf-8")
        doc, code = render.render(cue)
        self.assertEqual({t["target"]: t for t in doc["targets"]}["form.mono"]["result"], "pass")

    def _members(self, root: Path, specs: dict) -> dict:
        """Declare every member first (cards and takes), render nothing. specs: cue -> (family or None, audio, target)."""
        base = copy.deepcopy(CARD)
        base["level"] = {"measure": "F-09", "target": -20.0, "tolerance": 0.5, "must": True}
        out = {}
        for name, (family, audio, target) in specs.items():
            c, r = named(base, RECIPE, name)
            c["level"]["target"] = target
            if family is not None:
                c["family"] = family
            out[name] = make_cue(root, audio, 44100, c, r)
        return out

    def test_paid_reveal_family_check(self):
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        fam = lambda me: {"id": "egg", "paid_reveal": True,  # noqa: E731
                          "siblings": [n for n in ("SFX-EGG-COMMON", "SFX-EGG-RARE") if n != me]}
        cues = self._members(self.d, {n: (fam(n), chime, -20.0) for n in ("SFX-EGG-COMMON", "SFX-EGG-RARE")})
        doc, code = render.render(cues["SFX-EGG-COMMON"])
        self.assertEqual((doc["family"]["result"], code), ("incomplete", 3))  # LD-a: never a pass
        self.assertIn("re-render after the siblings", doc["family"]["reason"])
        doc, code = render.render(cues["SFX-EGG-RARE"])
        self.assertEqual((doc["family"]["result"], code), ("pass", 0), doc["family"])
        state = json.loads((self.d / "egg.family.json").read_text(encoding="utf-8"))
        self.assertEqual(sorted(state["file_sha256"]), ["SFX-EGG-COMMON", "SFX-EGG-RARE"])
        # the re-render-louder sequence (F2): any member's render re-checks the whole family on the current files
        card = json.loads((cues["SFX-EGG-RARE"] / "card.json").read_text(encoding="utf-8"))
        card["level"]["target"] = -15.0
        (cues["SFX-EGG-RARE"] / "card.json").write_text(json.dumps(card), encoding="utf-8")
        doc, code = render.render(cues["SFX-EGG-RARE"])
        self.assertEqual((doc["family"]["result"], code), ("fail", 1))
        self.assertGreater(doc["family"]["spread_lu"], 1.0)
        self.assertEqual(json.loads((self.d / "egg.family.json").read_text(encoding="utf-8"))["result"], "fail")
        doc, code = render.render(cues["SFX-EGG-COMMON"])  # the other member sees the same failure
        self.assertEqual((doc["family"]["result"], code), ("fail", 1))

    def test_a_one_sided_family_is_refused_from_both_sides(self):
        """F2: A lists B, B declares no family. Before: B rendered (0), A passed, then B re-rendered 8 dB louder went
        unseen. Now both renders refuse (exit 2) until both cards declare the family."""
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        cues = self._members(self.d, {"SFX-A": ({"id": "pair", "paid_reveal": True, "siblings": ["SFX-B"]}, chime, -20.0),
                                      "SFX-B": (None, chime, -12.0)})
        with self.assertRaisesRegex(SoundbenchError, "declares no family"):
            render.render(cues["SFX-B"])
        with self.assertRaisesRegex(SoundbenchError, "declares no family"):
            render.render(cues["SFX-A"])
        self.assertFalse((cues["SFX-A"] / "out").exists())  # refused before any audio

    def test_a_family_declared_differently_is_refused(self):
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        cases = (("paid", {"id": "f", "paid_reveal": False, "siblings": ["SFX-P1"]}, "paid_reveal False"),
                 ("id", {"id": "g", "paid_reveal": True, "siblings": ["SFX-P1"]}, "id 'g'"),
                 ("members", {"id": "f", "paid_reveal": True, "siblings": ["SFX-P1", "SFX-P3"]}, "declares members"))
        for label, second, why in cases:
            with self.subTest(label=label):
                root = self.d / label
                root.mkdir()
                specs = {"SFX-P1": ({"id": "f", "paid_reveal": True, "siblings": ["SFX-P2"]}, chime, -20.0),
                         "SFX-P2": (second, chime, -20.0)}
                cues = self._members(root, specs)
                with self.assertRaisesRegex(SoundbenchError, why):
                    render.render(cues["SFX-P1"])

    def test_a_card_listing_a_stranger_is_refused(self):
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        fam = lambda me: {"id": "f", "paid_reveal": True, "siblings": [n for n in ("SFX-Q1", "SFX-Q2") if n != me]}  # noqa: E731
        cues = self._members(self.d, {"SFX-Q1": (fam("SFX-Q1"), chime, -20.0), "SFX-Q2": (fam("SFX-Q2"), chime, -20.0),
                                      "SFX-Q3": ({"id": "h", "paid_reveal": True, "siblings": ["SFX-Q1"]}, chime, -20.0)})
        with self.assertRaisesRegex(SoundbenchError, "not members"):
            render.render(cues["SFX-Q1"])

    def test_two_pairs_sharing_one_family_id_are_refused(self):
        """R2-1 (re-review): four cards declare family 'egg'; COMMON/RARE list only each other, EPIC/LEGEND only each
        other and run 5 dB hotter. Each pair was consistent, so both passed and the true 5 LU spread went unseen.
        Every render must refuse (exit 2) until the four cards declare one member set; then D-03 sees all four."""
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        pairs = {"SFX-EGG-COMMON": (["SFX-EGG-RARE"], -20.0), "SFX-EGG-RARE": (["SFX-EGG-COMMON"], -20.0),
                 "SFX-EGG-EPIC": (["SFX-EGG-LEGEND"], -15.0), "SFX-EGG-LEGEND": (["SFX-EGG-EPIC"], -15.0)}
        cues = self._members(self.d, {n: ({"id": "egg", "paid_reveal": True, "siblings": sibs}, chime, target)
                                      for n, (sibs, target) in pairs.items()})
        for name, cue in cues.items():
            with self.subTest(cue=name):
                with self.assertRaisesRegex(SoundbenchError, "same family id"):
                    render.render(cue)
                self.assertFalse((cue / "out").exists())
        self.assertFalse((self.d / "egg.family.json").exists())
        everyone = sorted(pairs)
        for name, cue in cues.items():  # one member set: now the whole family is checked
            card = json.loads((cue / "card.json").read_text(encoding="utf-8"))
            card["family"]["siblings"] = [n for n in everyone if n != name]
            (cue / "card.json").write_text(json.dumps(card), encoding="utf-8")
        codes = [render.render(cues[n])[1] for n in everyone]
        doc, code = render.render(cues["SFX-EGG-COMMON"])
        self.assertEqual((doc["family"]["result"], code), ("fail", 1))
        self.assertEqual(doc["family"]["members"], everyone)
        self.assertGreater(doc["family"]["spread_lu"], 1.0)
        self.assertNotIn(0, codes)  # no member passed while the hotter pair was in the family

    def test_a_malformed_card_is_exit_2_with_the_reason(self):
        """F6: "targets" as a list crashed with AttributeError and exit 1 (= a must-target failed)."""
        c, r = named(CARD, RECIPE, "SFX-T-BAD")
        cue = make_cue(self.d, fx.make("late_hit", 44100, 2) * 0.4, 44100, c, r)
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        for bad, why in (({"targets": [{"max": 3}]}, "card.targets"), ({"family": {"id": 7, "paid_reveal": True,
                                                                                     "siblings": []}}, "card.family.id")):
            with self.subTest(why=why):
                (cue / "card.json").write_text(json.dumps({**c, **bad}), encoding="utf-8")
                p_ = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "render", str(cue)], cwd=str(ROOT),
                                    capture_output=True, text=True, env=env)
                self.assertEqual(p_.returncode, 2, p_.stderr)
                self.assertIn(why, p_.stderr)
        self.assertFalse((cue / "out").exists())

    def test_an_unexpected_error_is_exit_2(self):
        from tools.audio.soundbench import __main__ as cli

        with mock.patch.object(render, "render", side_effect=KeyError("boom")):
            with mock.patch("sys.stderr"):
                self.assertEqual(cli.main(["render", str(self.d)]), 2)

    def _family(self, rare_target: float, rare_audio=None) -> dict:
        root = self.d / f"t{rare_target}{rare_audio is None}"
        root.mkdir(parents=True, exist_ok=True)
        chime = fx.make("wrong_chime", 44100, 2) * 0.3
        fam = lambda me: {"id": "fam", "paid_reveal": True,  # noqa: E731
                          "siblings": [n for n in ("SFX-FAM-A", "SFX-FAM-B") if n != me]}
        cues = self._members(root, {"SFX-FAM-A": (fam("SFX-FAM-A"), chime, -20.0),
                                    "SFX-FAM-B": (fam("SFX-FAM-B"), chime if rare_audio is None else rare_audio,
                                                  rare_target)})
        render.render(cues["SFX-FAM-A"])
        return render.render(cues["SFX-FAM-B"])[0]["family"]

    def test_family_limits_just_inside_and_just_outside(self):
        inside = self._family(-19.6)  # the same sound 0.4 dB louder
        self.assertEqual(inside["result"], "pass", inside)
        base = fx.make("wrong_chime", 44100, 2) * 0.3
        dense = np.tanh(4 * base) / np.tanh(4) * np.max(np.abs(base))  # lower crest: louder at about the same peak
        outside = self._family(-18.4, dense)
        self.assertGreater(outside["spread_lu"], 1.0)
        self.assertLess(outside["spread_lu"], 2.0)
        self.assertLessEqual(outside["peak_spread_db"], 1.0)  # only the LU limit can fail it
        self.assertEqual(outside["result"], "fail")

    def test_family_fails_on_peak_spread_alone(self):
        spiky = fx.make("wrong_chime", 44100, 2) * 0.3
        spiky[700:702] = 0.32  # a 2-sample spike under the ceiling: the peak rises, the momentary loudness hardly moves
        fam = self._family(-20.0, spiky)
        self.assertLessEqual(fam["spread_lu"], 1.0)
        self.assertGreater(fam["peak_spread_db"], 1.0)
        self.assertEqual(fam["result"], "fail")

    def test_g1_two_processes_render_the_same_audio(self):
        c, r = named(CARD, RECIPE, "SFX-T-G1")
        r["design"] += [{"op": "compress", "threshold_db": -24, "ratio": 3},
                        {"op": "space", "decay_s": 0.4, "wet": 0.2}, {"op": "transient", "attack_db": 2}]
        cue = make_cue(self.d, fx.make("clean_hit", 44100, 2) * 0.5, 44100, c, r)
        code = ("import sys, json; sys.path.insert(0, sys.argv[1]); from pathlib import Path; "
                "from tools.audio.soundbench import render; d, c = render.render(Path(sys.argv[2])); "
                "print(d['export']['audio_sha256_float32'])")
        hashes = [subprocess.run([sys.executable, "-c", code, str(ROOT), str(cue)], capture_output=True, text=True,
                                 check=True).stdout.strip() for _ in range(2)]
        self.assertEqual(hashes[0], hashes[1])
        self.assertEqual(len(hashes[0]), 64)

    def test_command_line(self):
        c, r = named(CARD, RECIPE, "SFX-T-CLI")
        cue = make_cue(self.d, fx.make("late_hit", 44100, 2) * 0.4, 44100, c, r)
        env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
        p = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "render", str(cue), "--json"], cwd=str(ROOT),
                           capture_output=True, text=True, env=env)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertEqual(json.loads(p.stdout)["exit_code"], 0)
        c["level"]["target"] = -6.0
        (cue / "card.json").write_text(json.dumps(c), encoding="utf-8")
        p = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "render", str(cue)], cwd=str(ROOT),
                           capture_output=True, text=True, env=env)
        self.assertEqual(p.returncode, 1)
        (cue / "recipe.json").write_text("{", encoding="utf-8")
        p = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "render", str(cue)], cwd=str(ROOT),
                           capture_output=True, text=True, env=env)
        self.assertEqual(p.returncode, 2)
        self.assertIn("not valid JSON", p.stderr)

    @unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: the MP3 render test skipped")
    def test_render_from_a_real_mp3_take_with_ffmpeg_steps(self):
        rate = 44100
        c, r = named(CARD, RECIPE, "SFX-T-MP3")
        r["design"] = [{"op": "dc"}, {"op": "denoise", "nr_db": 12}, {"op": "highpass", "hz": 60},
                       {"op": "chorus", "delay_ms": 30, "in_gain": 0.8}]
        cue = self.d / c["cue"]
        (cue / "takes").mkdir(parents=True)
        x = (fx.make("late_hit", rate, 2) * 0.4 + 0.002 * np.random.RandomState(3).standard_normal(
            fx.make("late_hit", rate, 2).shape)).astype(np.float32)
        wav = fx.write_wav(self.d / "src.wav", x, rate)
        mp3 = cue / r["take"]
        subprocess.run([str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", str(wav), "-c:a",
                        "libmp3lame", "-b:a", "192k", str(mp3)], check=True)
        intake.decode_take(mp3, requested_ms=1000 * len(x) / rate)
        (cue / "card.json").write_text(json.dumps(c), encoding="utf-8")
        (cue / "recipe.json").write_text(json.dumps(r), encoding="utf-8")
        doc, code = render.render(cue)
        self.assertEqual(code, 0, doc["must_failed"])
        den = next(s for s in doc["steps"] if s["op"] == "denoise")
        self.assertEqual(den["info"]["timing"]["channel_lags_samples"], [1102, 1102])
        self.assertLessEqual(abs(den["after"]["main_transient_ms"] - den["before"]["main_transient_ms"]), 1.0)


if __name__ == "__main__":
    unittest.main()
