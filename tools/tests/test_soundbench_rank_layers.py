"""Tests for soundbench `rank` on layered rounds (J020: important cues' layers, `<cue>.<layer>.r<k>.t<n>`).

The takes are written at the names `generate` plans for a prompts.json with layers (its own `plan`, so rank reads what
generate writes), with realistic fixtures as their masters. Oracles: the construction of each take (a bass thump holds
99.8 % of its energy under 120 Hz, a whoosh 0.01 %), and `render` itself: every verdict's recipe is rendered by the test
and render's exit code and rows are the expected values, never rank's own numbers. The planted-fault test at the end
shows each named fault makes its tests FAIL (an assertion, never an error).
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
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import generate, intake, rank, render  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, audio_sha256, file_sha256, read_float32  # noqa: E402

R = 44100
CARD = {"cue": "SFX-LR-SLAM", "kind": "hit", "category": "sfx", "tier": "important",
        "level": {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": True},
        "targets": {"true_peak_dbtp": {"max": -1.0, "must": True}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}
# Each layer's own targets, unlike each other on purpose: swapping them flips every result.
SUB = {"below_120": {"min": 0.5, "must": True}}
AIR = {"below_120": {"max": 0.2, "must": True}, "tail_snr_db": {"min": 0, "must": False}}


def bass() -> np.ndarray:
    """A bass thump at a real take's level (-30 dBFS), 400 ms: 99.8 % of its energy under 120 Hz."""
    b = fx.make("bass_thump", R, 2)
    return b / np.max(np.abs(b)) * 10 ** (-30 / 20)


def whoosh() -> np.ndarray:
    """The realistic quiet whoosh (-30 dBFS, 480 ms, mid-waveform start): 0.01 % of its energy under 120 Hz."""
    return fx.make_real("quiet_whoosh", R)


def hit() -> np.ndarray:
    """The realistic quiet hit (-36 dBFS): 0.2 % under 120 Hz, so a sub layer has no sound in its band."""
    return fx.make_real("quiet_hit", R)


def write_take(take: Path, x: np.ndarray, rate: int = R) -> None:
    """A stand-in take file, its master WAV and its intake sidecar (as test_soundbench_rank.make_round)."""
    take.parent.mkdir(parents=True, exist_ok=True)
    take.write_bytes(f"stand-in take {take.name}".encode())
    fx.write_wav(intake.master_path(take), x, rate)
    y, _ = read_float32(intake.master_path(take))
    side = {"prompt": "test", "intake": {"take_sha256": file_sha256(take), "master_audio_sha256": audio_sha256(y),
                                         "rate": rate, "decoder": "test (no decode)"}}
    take.with_suffix(".json").write_text(json.dumps(side), encoding="utf-8")


def layer_round(cue_dir: Path, layers: dict) -> int:
    """One generate round of the given layers ({layer: [audio per take]}): the stems come from generate's own plan of
    a prompts.json with those layers (so the names and the cue round are generate's). Returns the round."""
    doc = {"cue": cue_dir.name, "duration_s": 0.5,
           "layers": [{"name": name, "prompts": [f"{name} texture"], "takes": len(xs)} for name, xs in layers.items()]}
    (cue_dir / "prompts.json").write_text(json.dumps(doc), encoding="utf-8")
    _, sounds, calls, _ = generate.plan(cue_dir)
    for call in calls:
        write_take(cue_dir / "takes" / f"{call['stem']}.mp3", layers[call["layer"]][call["take"] - 1])
    return sounds[0]["round"]


def plain_take(cue_dir: Path, round_no: int, n: int, x: np.ndarray) -> None:
    write_take(cue_dir / "takes" / f"{cue_dir.name}.r{round_no}.t{n}.mp3", x)


def cue_folder(root: Path, card: dict, layers: list | None = None) -> Path:
    """card.json and recipe.json with the layer plan: sub aligned on its main transient at 300 ms (so the mix is
    longer than the air layer alone), air from the start at -3 dB."""
    cue = root / card["cue"]
    (cue / "takes").mkdir(parents=True, exist_ok=True)
    (cue / "card.json").write_text(json.dumps(card), encoding="utf-8")
    if layers is None:
        layers = [{"name": "sub", "take": f"takes/{card['cue']}.sub.r1.t1.mp3", "design": [],
                   "align": {"to_ms": 300.0, "on": "main_transient"}, "targets": SUB},
                  {"name": "air", "take": f"takes/{card['cue']}.air.r1.t1.mp3", "design": [], "offset_ms": 0,
                   "gain_db": -3.0, "targets": AIR}]
    recipe = {"cue": card["cue"], "layers": layers, "design": [], "edit": []}
    (cue / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
    return cue


def card_for(cue: str, **changes) -> dict:
    c = copy.deepcopy(CARD)
    c["cue"] = cue
    c.update(changes)
    return c


def layer(doc: dict, name: str) -> dict:
    return next(lay for lay in doc["layers"] if lay["name"] == name)


def render_choice(cue: Path, layers: list, edit: list) -> tuple[dict, int]:
    """Render a layers recipe in the cue folder itself (the test's own oracle; rank renders only temp copies)."""
    rec = json.loads((cue / "recipe.json").read_text(encoding="utf-8"))
    (cue / "recipe.json").write_text(json.dumps({**rec, "layers": layers, "design": [], "edit": edit}),
                                     encoding="utf-8")
    try:
        return render.render(cue)
    finally:
        (cue / "recipe.json").write_text(json.dumps(rec), encoding="utf-8")


class LayerRankTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def rank(self, cue: Path, round_no=None) -> tuple[dict, int]:
        """rank, with a refusal turned into a test failure (a planted fault must fail, not crash)."""
        try:
            return rank.rank(cue, round_no)
        except SoundbenchError as err:
            self.fail(f"rank refused: {err}")

    def test_layer_takes_are_found_and_ranked_against_their_own_layers_targets(self):
        cue = cue_folder(self.d, card_for("SFX-LR-FIND"))
        layer_round(cue, {"sub": [hit(), bass()], "air": [bass(), whoosh()]})
        doc, code = self.rank(cue)
        self.assertEqual((doc["form"], doc["round"]), ("layers", 1))
        sub, air = layer(doc, "sub"), layer(doc, "air")
        self.assertEqual(sub["order"], ["SFX-LR-FIND.sub.r1.t2.mp3", "SFX-LR-FIND.sub.r1.t1.mp3"])
        self.assertEqual(air["order"], ["SFX-LR-FIND.air.r1.t2.mp3", "SFX-LR-FIND.air.r1.t1.mp3"])
        hit_entry = sub["takes"][1]  # the hit has no sound in the sub band: rejected outright, as a one-shot would be
        self.assertIn("no sound in the band", hit_entry["rejected"][0])
        bass_in_air = air["takes"][1]
        self.assertEqual(bass_in_air["must_after"], ["layer[air].below_120"])  # air's own max 0.2, not sub's min 0.5
        row = next(r for r in bass_in_air["after"] if r["target"] == "layer[air].below_120")
        self.assertGreater(row["value"], 0.9)  # the bass: 99.8 % under 120 Hz by construction
        self.assertIn("a layer has no edit pass", bass_in_air["misses"][0]["why"])
        for lay in doc["layers"]:  # the order is rank's documented key, recomputed from the table
            keys = [[int(bool(e["rejected"])), int(not e["passes_after_fix"]), len(e["must_after"]),
                     len(e["aim_after"]), len(e["fixed"]), len(e["near_after"]), e["n"]] for e in lay["takes"]]
            self.assertEqual(keys, sorted(keys))
        self.assertTrue(any("gets 6 per round" in w for w in doc["warnings"]))
        self.assertIn(code, (0, 1))
        self.assertTrue((cue / "report" / "SFX-LR-FIND.r1.rank.md").is_file())
        self.assertFalse((cue / "out").exists())

    def test_use_is_proven_by_a_real_render_of_the_layers_recipe(self):
        cue = cue_folder(self.d, card_for("SFX-LR-USE"))
        layer_round(cue, {"sub": [hit(), bass()], "air": [bass(), whoosh()]})
        doc, code = self.rank(cue)
        v = doc["verdict"]
        self.assertEqual((code, v["action"]), (0, "use"), v["say"])
        self.assertEqual(v["takes"], {"sub": "SFX-LR-USE.sub.r1.t2.mp3", "air": "SFX-LR-USE.air.r1.t2.mp3"})
        self.assertTrue(doc["proof"]["agrees"])
        self.assertEqual(doc["proof"]["layer_rows_compared"], 5)  # sub: edge_clicks, below_120; air: + tail_snr_db
        # the test's own render of the verdict's recipe: exit 0, the same audio, every row as rank simulated it
        out, rcode = render_choice(cue, v["recipe_layers"], v["recipe_edit"])
        self.assertEqual((rcode, out["must_failed"]), (0, []))
        self.assertEqual(out["export"]["audio_sha256_float32"], doc["proof"]["audio_sha256_float32"])
        sim = {r["target"]: r for r in doc["mix"]["after"] + doc["mix"]["layer_rows"]}
        for r in out["targets"] + [r for r in out["form_checks"] if r["target"].startswith("layer[")]:
            self.assertEqual(r["result"], sim[r["target"]]["result"], r["target"])
            self.assertAlmostEqual(r["value"], sim[r["target"]]["value"], delta=max(0.02, 0.002 * abs(r["value"])))

    def test_the_layer_rows_are_read_in_the_mix_length_as_render_reads_them(self):
        """The air layer (480 ms) sits in a mix of about 700 ms (sub placed at 300 ms): its tail reading differs alone
        and in the mix, and rank must give render's value."""
        cue = cue_folder(self.d, card_for("SFX-LR-FRAME"))
        layer_round(cue, {"sub": [bass()], "air": [whoosh()]})
        doc, _ = self.rank(cue)
        top = layer(doc, "air")["takes"][0]
        ranked = next(r for r in top["after"] if r["target"] == "layer[air].tail_snr_db")["value"]
        out, _ = render_choice(cue, doc["proof"]["recipe_layers"], doc["proof"]["recipe_edit"])
        rendered = next(r for r in out["form_checks"] if r["target"] == "layer[air].tail_snr_db")["value"]
        self.assertEqual(ranked, rendered)
        card = card_for("SFX-LR-FRAME")  # the same placed audio read alone, at its own length: another value
        air = next(lay for lay in rank.layer_plan(cue, card)[0] if lay["name"] == "air")
        c = rank.place_candidate(cue, card, air, 1, "takes/SFX-LR-FRAME.air.r1.t1.mp3", 1)
        alone = render.layer_rows(card, [air], [c["_p"]], R, [c["_info"]])
        self.assertNotEqual(next(r for r in alone if r["target"] == "layer[air].tail_snr_db")["value"], rendered)
        self.assertGreater(doc["frame"]["length_samples"], len(c["_p"]))

    def test_the_mix_missing_a_must_is_never_use(self):
        """Both layers pass alone; the card wants the whole cue under 30 % sub energy and the bass dominates the mix.
        No edit step moves a band share, so render exits 1 on this choice and rank must say so plainly."""
        card = card_for("SFX-LR-MIX", targets={**CARD["targets"], "below_120": {"max": 0.3, "must": True}})
        cue = cue_folder(self.d, card)
        layer_round(cue, {"sub": [bass()], "air": [whoosh()]})
        doc, code = self.rank(cue)
        v = doc["verdict"]
        self.assertTrue(layer(doc, "sub")["has_passing_take"] and layer(doc, "air")["has_passing_take"])
        self.assertEqual((code, v["action"]), (1, "mix_misses"))
        self.assertIn("the layers pass alone", v["say"])
        self.assertIn("the mix misses below_120", v["say"])
        self.assertIsNone(doc["proof"])
        layers = [{**lay, "take": f"takes/{v['takes'][lay['name']]}", "design": []}
                  for lay in json.loads((cue / "recipe.json").read_text(encoding="utf-8"))["layers"]]
        out, rcode = render_choice(cue, layers, doc["mix"]["fix"]["steps"])
        self.assertEqual(rcode, code)  # the exit code render gives this choice
        self.assertIn("below_120", out["must_failed"])
        self.assertEqual(v["mix_must_misses"], [t for t in out["must_failed"] if not t.startswith("layer[")])

    def test_a_layer_without_a_passing_take_is_named_with_its_prompt_misses(self):
        cue = cue_folder(self.d, card_for("SFX-LR-REGEN"))
        layer_round(cue, {"sub": [bass()], "air": [bass(), bass() * 0.5]})
        doc, code = self.rank(cue)
        v = doc["verdict"]
        self.assertEqual((code, v["action"]), (1, "regenerate"))
        self.assertEqual(v["layers_without_a_passing_take"], ["air"])
        self.assertEqual(v["passing_layers"], {"sub": "SFX-LR-REGEN.sub.r1.t1.mp3"})
        pm = v["prompt_must_change"]["air"]
        self.assertEqual([d["target"] for d in pm], ["layer[air].below_120"])
        d = pm[0]
        self.assertEqual((d["target"], d["must"], d["takes_missing"], d["of"], d["closest"]["direction"]),
                         ("layer[air].below_120", True, 2, 2, "too high"))
        self.assertNotIn("sub", v["prompt_must_change"])
        self.assertIsNone(doc["mix"])

    def test_the_cue_round_counts_every_layer_and_round_3_goes_to_the_owner(self):
        cue = cue_folder(self.d, card_for("SFX-LR-ROUND"))
        self.assertEqual(layer_round(cue, {"sub": [bass()], "air": [bass()]}), 1)
        plain_take(cue, 2, 1, whoosh())  # a one-shot round in between: the cue round counts it too
        os.remove(cue / "prompts.json")
        self.assertEqual(layer_round(cue, {"air": [bass(), bass()]}), 3)  # only the failing layer regenerated
        doc, code = self.rank(cue)
        self.assertEqual((doc["round"], code, doc["verdict"]["action"]), (3, 1, "owner"))
        self.assertEqual(layer(doc, "sub")["round"], 1)  # the sub layer's latest takes, round 1
        self.assertTrue(any("layer sub: no takes in round 3" in w for w in doc["warnings"]))
        self.assertIn("J020-D7", doc["verdict"]["say"])
        doc, code = self.rank(cue, round_no=2)  # the plain round is ranked as a one-shot round
        self.assertNotIn("form", doc)
        self.assertEqual(doc["round"], 2)
        with self.assertRaisesRegex(SoundbenchError, "at most 3 rounds"):
            rank.rank(cue, round_no=4)

    def test_a_round_with_layer_and_plain_takes_is_refused(self):
        cue = cue_folder(self.d, card_for("SFX-LR-BOTH"))
        layer_round(cue, {"sub": [bass()], "air": [whoosh()]})
        plain_take(cue, 1, 1, whoosh())
        with self.assertRaisesRegex(SoundbenchError, "one sound or its layers, never both"):
            rank.rank(cue)
        p = subprocess.run([sys.executable, "-m", "tools.audio.soundbench", "rank", str(cue)], cwd=str(ROOT),
                           capture_output=True, text=True, env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        self.assertEqual(p.returncode, 2, p.stdout)

    def test_an_important_layer_without_targets_is_refused_as_render_refuses_it(self):
        card = card_for("SFX-LR-NOTGT")
        lays = [{"name": "sub", "take": "takes/SFX-LR-NOTGT.sub.r1.t1.mp3", "design": [], "offset_ms": 0,
                 "targets": SUB},
                {"name": "air", "take": "takes/SFX-LR-NOTGT.air.r1.t1.mp3", "design": [], "offset_ms": 0}]
        cue = cue_folder(self.d, card, lays)
        layer_round(cue, {"sub": [bass()], "air": [whoosh()]})
        with self.assertRaises(SoundbenchError) as by_render:
            render.render(cue)
        with self.assertRaises(SoundbenchError) as by_rank:
            rank.rank(cue)
        self.assertEqual(str(by_rank.exception), str(by_render.exception))
        self.assertIn("needs its own targets", str(by_rank.exception))

    def test_a_layer_the_recipe_does_not_name_or_a_missing_recipe_is_refused(self):
        cue = cue_folder(self.d, card_for("SFX-LR-STRAY"))
        layer_round(cue, {"sub": [bass()], "air": [whoosh()], "crack": [hit()]})
        with self.assertRaisesRegex(SoundbenchError, r"layers \['crack'\], which recipe.json's layers do not name"):
            rank.rank(cue)
        (cue / "recipe.json").unlink()
        with self.assertRaisesRegex(SoundbenchError, "no recipe.json"):
            rank.rank(cue)

    def test_one_shot_rounds_never_read_layer_takes(self):
        """A plain round next to layer takes of an earlier round is ranked as before: the same doc as without them."""
        card = card_for("SFX-LR-PLAIN", tier="minor")
        cue = cue_folder(self.d, card)
        plain_take(cue, 1, 1, hit())
        before, code_before = self.rank(cue)
        write_take(cue / "takes" / "SFX-LR-PLAIN.sub.r1.t1.mp3", bass())  # a stray layer take in round 1: refused
        with self.assertRaisesRegex(SoundbenchError, "never both"):
            rank.rank(cue)
        os.remove(cue / "takes" / "SFX-LR-PLAIN.sub.r1.t1.mp3")
        doc, code = self.rank(cue)
        strip = lambda d: {k: v for k, v in d.items() if k not in ("tools", "pictures")}  # noqa: E731
        self.assertEqual((json.dumps(strip(doc), default=str), code), (json.dumps(strip(before), default=str),
                                                                       code_before))


# ------------------------------------------------------------------------------------------------- planted faults

def _swap_targets(orig):
    def plan(cue_dir, card):
        lays, raw, warnings = orig(cue_dir, card)
        t = [lay["targets"] for lay in lays]
        return [{**lay, "targets": t[(i + 1) % len(t)]} for i, lay in enumerate(lays)], raw, warnings
    return plan


def _mix_judged_as_passing(orig):
    def mix(cue_dir, card, plan_layers, tops):
        return {**orig(cue_dir, card, plan_layers, tops), "passes_after_fix": True}
    return mix


def _round_per_layer(cue_dir, cue, layered, round_no):
    return min(max(rounds) for rounds in layered.values()) if round_no is None else round_no


def _fake_proof(orig):
    def prove(card, cue_dir, raw_layers, mix):
        return {"takes": mix["takes"], "recipe_layers": [{**r, "take": f"takes/{mix['takes'][r['name']]}",
                                                          "design": []} for r in raw_layers],
                "recipe_edit": mix["fix"]["steps"], "must_failed": [], "rows_compared": len(mix["after"]),
                "layer_rows_compared": len(mix["layer_rows"]), "agrees": True, "audio_sha256_float32": None}
    return prove


FAULTS = {
    "layer takes ignored (only <cue>.r<k>.t<n> read)":
        (lambda: mock.patch.object(rank, "layer_rounds", lambda cue_dir, cue: {}),
         ["test_layer_takes_are_found_and_ranked_against_their_own_layers_targets"]),
    "one layer's targets used for another":
        (lambda: mock.patch.object(rank, "layer_plan", _swap_targets(rank.layer_plan)),
         ["test_layer_takes_are_found_and_ranked_against_their_own_layers_targets"]),
    "use while the mix misses (the mix never judged)":
        (lambda: mock.patch.object(rank, "mix_entry", _mix_judged_as_passing(rank.mix_entry)),
         ["test_the_mix_missing_a_must_is_never_use"]),
    "a layered and a plain round mixed together":
        (lambda: mock.patch.object(rank, "plain_rounds", lambda cue_dir, cue: {}),
         ["test_a_round_with_layer_and_plain_takes_is_refused"]),
    "the cue round ignored (the round counted per layer)":
        (lambda: mock.patch.object(rank, "cue_round", _round_per_layer),
         ["test_the_cue_round_counts_every_layer_and_round_3_goes_to_the_owner"]),
    "layer rows read on the layer alone (not at the mix's length)":
        (lambda: mock.patch.object(rank, "in_frame", lambda p, frame: p),
         ["test_the_layer_rows_are_read_in_the_mix_length_as_render_reads_them"]),
    "use without a real render (proof faked)":
        (lambda: mock.patch.object(rank, "prove_layers", _fake_proof(rank.prove_layers)),
         ["test_use_is_proven_by_a_real_render_of_the_layers_recipe"]),
    "a layer that fails is not named (every layer listed)":
        (lambda: mock.patch.object(rank, "prompt_misses", lambda entries: []),
         ["test_a_layer_without_a_passing_take_is_named_with_its_prompt_misses"]),
}


class PlantedFaultTest(unittest.TestCase):
    """Each planted fault must make at least one of its named tests FAIL (an assertion, not an error); the correct
    build passes them all."""

    def test_every_planted_fault_is_caught_by_an_assertion(self):
        report = {}
        for name, (patcher, tests) in FAULTS.items():
            suite = unittest.TestSuite(LayerRankTest(t) for t in tests)
            with patcher():
                res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
            report[name] = (len(res.failures), [str(e[1]).strip().splitlines()[-1] for e in res.errors])
        survived = [n for n, (fails, errors) in report.items() if not fails]
        errored = {n: errors for n, (fails, errors) in report.items() if errors}
        self.assertEqual(survived, [], f"planted faults not caught by an assertion: {report}")
        self.assertEqual(errored, {}, "planted faults that crashed a test instead of failing it")


if __name__ == "__main__":
    unittest.main()
