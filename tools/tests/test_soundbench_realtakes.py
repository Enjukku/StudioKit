"""Optional tests on real takes (LD-c): set SOUNDBENCH_REAL_TAKES to a folder of ElevenLabs MP3s (with their sidecar
JSON, if any) to run them; otherwise they skip with the reason. No audio is committed; the takes are copied into a
temp folder and never changed.

What every real take must survive (the repair-round findings, 2026-10-23):
  - intake: decoded length = the file's stated length; the requested length only logged (0.5 s came back 480 ms);
  - a normal render (dc, high-pass, trim, fade, loudness, peak) ends 0 or 1, never a crash, and starts silent;
  - denoise with the reviewer's settings (nr 40, nf -20 dBFS) is refused on every take whose floor is under -23 dBFS;
  - saturate and compress act on a quiet take exactly as on the same take normalised;
  - chorus is not refused on the takes' own timing;
  - rank (J020 step 5, review-rank round 1): each sound's takes t1..tN ranked as one round with every level measure
    (F-09, F-13a, LUFS-I): exit 0 or 1 (never a refusal), the order equals the documented key recomputed from the
    table, no clean take reads clipped, a miss called fixed passes after the fix, the derived level matches the
    simulated one, the top take's proof render agrees (and runs only when it passes), every kept plan of every take
    renders and agrees or was refused by rank with render's own reason (review-rank R2-1, the reviewer's e5), and
    nothing is written to out/.
"""

import json
import os
import re
import shutil
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
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fxops, intake, ops, rank, render  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, read_float32  # noqa: E402

FOLDER = os.environ.get("SOUNDBENCH_REAL_TAKES", "").strip()
TAKES = sorted(Path(FOLDER).glob("*.mp3")) if FOLDER and Path(FOLDER).is_dir() else []
try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
SKIP = ("set SOUNDBENCH_REAL_TAKES to a folder of real MP3 takes to run these" if not TAKES
        else "ffmpeg not found" if not FOUND else None)

CARD = {"kind": "hit", "category": "sfx", "tier": "minor",
        "level": {"measure": "F-09", "target": -24.0, "tolerance": 0.5, "must": False},
        "targets": {"edge_clicks": {"max": 0, "must": True}},
        "playback": {"space": "2D", "takes_room": False, "ducks": None}}
RANK_CARD = {"category": "sfx", "level": {"measure": "F-09", "target": -18.0, "tolerance": 1.0, "must": True},
             "targets": {"onset_ms": {"max": 5, "must": True}, "true_peak_dbtp": {"max": -1.0, "must": True},
                         "edge_clicks": {"max": 0, "must": True}, "sound_ms": {"min": 40, "max": 400, "must": False},
                         "phone_loss_db": {"max": 12, "must": False}},
             "playback": {"space": "2D", "takes_room": False, "ducks": None}}
RECIPE = {"design": [{"op": "dc"}, {"op": "highpass", "hz": 60}],
          "edit": [{"op": "trim"}, {"op": "fade", "out_ms": 10}, {"op": "loudness"}, {"op": "peak"}]}


def requested_ms(mp3: Path):
    side = mp3.with_suffix(".json")
    try:
        sec = json.loads(side.read_text(encoding="utf-8")).get("request", {}).get("duration_seconds")
        return None if sec is None else 1000 * float(sec)
    except (OSError, ValueError, AttributeError):
        return None


@unittest.skipIf(SKIP, SKIP or "")
class RealTakeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._t = tempfile.TemporaryDirectory()
        cls.d = Path(cls._t.name)
        cls.cues = {}
        for mp3 in TAKES:
            cue = "REAL-" + mp3.stem.replace(".", "-")
            take = cls.d / cue / "takes" / f"{cue}.r1.t1.mp3"
            take.parent.mkdir(parents=True)
            shutil.copyfile(mp3, take)
            cls.cues[cue] = (mp3, take)

    @classmethod
    def tearDownClass(cls):
        cls._t.cleanup()

    def test_intake_render_and_guards_on_every_take(self):
        for cue, (src, take) in self.cues.items():
            with self.subTest(take=src.name):
                asked = requested_ms(src)
                info = intake.decode_take(take, requested_ms=asked)
                self.assertLessEqual(abs(info["decoded_ms"] - info["stated_ms"]), intake.TOLERANCE_MS)
                if asked is not None and abs(info["decoded_ms"] - asked) > intake.TOLERANCE_MS:
                    self.assertTrue(info["warnings"])  # logged, never refused
                card = {**CARD, "cue": cue}
                recipe = {**RECIPE, "cue": cue, "take": f"takes/{cue}.r1.t1.mp3"}
                (take.parents[1] / "card.json").write_text(json.dumps(card), encoding="utf-8")
                (take.parents[1] / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
                doc, code = render.render(take.parents[1])
                self.assertIn(code, (0, 1))
                self.assertNotIn("edge_clicks", doc["must_failed"])  # trim faded a mid-waveform start
                y, rate = read_float32(take.parents[1] / "out" / f"{cue}.flac")
                self.assertEqual(float(np.max(np.abs(y[0]))), 0.0)
                x, rate = read_float32(intake.master_path(take))
                x = x.astype(np.float64)
                floor = m.tail_noise(x - x.mean(axis=0), rate)["floor_dbfs"]
                if floor is not None and floor < -23:
                    with self.assertRaises(SoundbenchError):
                        fxops.run("denoise", x, rate, ops.check_params("denoise", {"nr_db": 40, "nf_db": -20}),
                                  {"kind": "hit"})
                k = 0.9 / float(np.max(np.abs(x)))
                for op, given in (("saturate", {"drive_db": 12}), ("compress", {"threshold_db": -20, "ratio": 4})):
                    yq, _ = ops.run(op, x, rate, ops.check_params(op, given), {"kind": "hit", "category": "sfx"})
                    yn, _ = ops.run(op, x * k, rate, ops.check_params(op, given), {"kind": "hit", "category": "sfx"})
                    np.testing.assert_allclose(yq * k, yn, rtol=1e-9, atol=1e-12)
                fxops.run("chorus", x, rate, ops.check_params("chorus", {}), {"kind": "whoosh"})

    def test_rank_every_real_round(self):
        rounds: dict = {}
        for mp3 in TAKES:
            found = re.match(r"^(.+)\.t(\d+)$", mp3.stem)
            if found:
                rounds.setdefault(found[1], []).append((int(found[2]), mp3))
        self.assertTrue(rounds, "no takes named <sound>.t<n>.mp3")
        with tempfile.TemporaryDirectory() as tmp:
            for sound, takes in sorted(rounds.items()):
                with self.subTest(sound=sound):
                    cue = "REAL-" + re.sub(r"[^A-Za-z0-9-]", "-", sound)
                    folder = Path(tmp) / cue
                    (folder / "takes").mkdir(parents=True)
                    for n, src in takes:
                        take = folder / "takes" / f"{cue}.r1.t{n}.mp3"
                        shutil.copyfile(src, take)
                        intake.decode_take(take, requested_ms=requested_ms(src))
                    kind = "whoosh" if re.search(r"whoosh|swish", sound) else "hit"
                    tier = {3: "minor", 4: "frequent"}.get(len(takes), "important")
                    for measure in ("F-09", "F-13a", "LUFS-I"):  # every level measure a card can name (review-rank F2)
                        with self.subTest(sound=sound, measure=measure):
                            self._rank_one(folder, {**RANK_CARD, "cue": cue, "kind": kind, "tier": tier,
                                                    "level": {**RANK_CARD["level"], "measure": measure}})

    def _rank_one(self, folder: Path, card: dict):
        (folder / "card.json").write_text(json.dumps(card), encoding="utf-8")
        doc, code = rank.rank(folder)  # a derived/simulated level disagreement would raise here (exit 2)
        self.assertIn(code, (0, 1))
        keys = [e["rank_key"] for e in doc["takes"]]
        self.assertEqual(keys, sorted(keys))
        for e in doc["takes"]:
            self.assertEqual(e["rank_key"], [int(bool(e["rejected"])), int(not e["passes_after_fix"]),
                                             len(e["must_after"]), len(e["aim_after"]), len(e["fixed"]),
                                             len(e["near_after"]), e["n"]])
            self.assertFalse(e["clip"]["clipped"], e["clip"])  # the 62 clean real takes: no clip rejection
            after = {r["target"]: r for r in e["after"]}
            for x in e["misses"]:
                if x["fix"] == "fixed":
                    self.assertEqual(after[x["target"]]["result"], "pass")
            lv = (e["fix"] or {}).get("level")
            if lv:
                cut = max(0.0, lv["true_peak_in_dbtp"] + lv["gain_needed_db"] - lv["peak_limit_dbtp"])
                self.assertAlmostEqual(lv["peak_cut_db"], cut, delta=0.002)
                self.assertLessEqual(abs(lv["predicted_level"] - lv["simulated_level"]), rank.LEVEL_AGREE_DB)
                if abs(abs(lv["predicted_level"] - lv["target"]) - lv["tolerance"]) > rank.LEVEL_AGREE_DB:
                    self.assertEqual(after["level"]["result"] == "pass", lv["fits"])
        if doc["proof"] is not None:
            self.assertTrue(doc["proof"]["agrees"])
        self.assertEqual(doc["proof"] is not None, doc["takes"][0]["passes_after_fix"])  # only a "use" is proven
        for e in doc["takes"]:  # e5 (review-rank R2-1): every kept plan renders, or rank refused it as render would
            if e["rejected"]:
                continue
            if e["fix"]["plan"] is not None:
                self.assertTrue(rank.prove(card, folder, e)["agrees"])
                continue
            reasons = [p["error"] for p in e["fix"]["refused_plans"]]
            with self.assertRaises(SoundbenchError) as raised:
                rank.prove(card, folder, {**e, "fix": {**e["fix"], "steps": []}})
            self.assertTrue(any(str(raised.exception) in r for r in reasons), (str(raised.exception), reasons))
        self.assertFalse((folder / "out").exists())

    def test_rank_layered_real_rounds(self):
        """rank on layered rounds of real takes (J020: layer takes `<cue>.<layer>.r<k>.t<n>`): each hit or thump's
        takes as the `body` layer (aligned on its main transient at 300 ms; a phone-loss must of 15 dB that
        thumps miss) and the first whoosh's takes as the `air`
        layer (its F-01 at 60 ms, -6 dB), under F-09 and LUFS-I. Every round exits 0 or 1; each layer's order is the
        documented key; render of the chosen takes (the test's own render, in the cue folder) gives exactly the
        ranked layer rows, exits 0 on `use`, and exits 1 with the same whole-cue misses on `mix_misses`; rank writes
        no out/."""
        rounds: dict = {}
        for mp3 in TAKES:
            found = re.match(r"^(.+)\.t(\d+)$", mp3.stem)
            if found:
                rounds.setdefault(found[1], []).append((int(found[2]), mp3))
        air = next(sorted(t) for s, t in sorted(rounds.items()) if re.search(r"whoosh", s))
        verdicts: dict = {}
        with tempfile.TemporaryDirectory() as tmp:
            for sound, takes in sorted(rounds.items()):
                if not re.search(r"hit|thump", sound):
                    continue
                for measure in ("F-09", "LUFS-I"):
                    with self.subTest(sound=sound, measure=measure):
                        cue = "REAL-LR-" + re.sub(r"[^A-Za-z0-9-]", "-", sound) + "-" + measure.replace("-", "")
                        folder = Path(tmp) / cue
                        (folder / "takes").mkdir(parents=True)
                        for name, srcs in (("body", sorted(takes)), ("air", air)):
                            for n, src in srcs:
                                take = folder / "takes" / f"{cue}.{name}.r1.t{n}.mp3"
                                shutil.copyfile(src, take)
                                intake.decode_take(take, requested_ms=requested_ms(src))
                        card = {**RANK_CARD, "cue": cue, "kind": "hit", "tier": "important",
                                "level": {**RANK_CARD["level"], "measure": measure},
                                "targets": {"true_peak_dbtp": {"max": -1.0, "must": True},
                                            "sound_ms": {"min": 40, "max": 900, "must": False}}}
                        layers = [{"name": "body", "take": f"takes/{cue}.body.r1.t1.mp3", "design": [],
                                   "align": {"to_ms": 300.0, "on": "main_transient"},
                                   "targets": {"sound_ms": {"min": 40, "max": 600, "must": True},
                                               "phone_loss_db": {"max": 15, "must": True}}},
                                  {"name": "air", "take": f"takes/{cue}.air.r1.t1.mp3", "design": [],
                                   "align": {"to_ms": 60.0, "on": "F-01"}, "gain_db": -6.0,
                                   "targets": {"sound_ms": {"min": 100, "max": 900, "must": True}}}]
                        recipe = {"cue": cue, "layers": layers, "design": [], "edit": []}
                        (folder / "card.json").write_text(json.dumps(card), encoding="utf-8")
                        (folder / "recipe.json").write_text(json.dumps(recipe), encoding="utf-8")
                        doc, code = rank.rank(folder)
                        self.assertIn(code, (0, 1))
                        self.assertFalse((folder / "out").exists())
                        v = doc["verdict"]
                        verdicts[v["action"]] = verdicts.get(v["action"], 0) + 1
                        passes = f"frame passes {doc['frame']['passes']}"
                        verdicts[passes] = verdicts.get(passes, 0) + 1
                        for t in v.get("mix_must_misses", []) + v.get("layers_without_a_passing_take", []):
                            verdicts[t] = verdicts.get(t, 0) + 1
                        for lay in doc["layers"]:
                            keys = [e["rank_key"] for e in lay["takes"]]
                            self.assertEqual(keys, sorted(keys))
                            for e in lay["takes"]:
                                self.assertFalse(e["clip"]["clipped"], e["clip"])
                        tops = {lay["name"]: lay["takes"][0] for lay in doc["layers"]}
                        if any("cannot be placed" in " ".join(e["rejected"]) for e in tops.values()):
                            continue  # render refuses a take it cannot place: nothing to compare
                        edit = doc["mix"]["fix"]["steps"] if doc["mix"] else []
                        chosen = [{**lay, "take": f"takes/{tops[lay['name']]['take']}"} for lay in layers]
                        (folder / "recipe.json").write_text(json.dumps({**recipe, "layers": chosen, "edit": edit}),
                                                            encoding="utf-8")
                        out, rcode = render.render(folder)
                        ranked = {r["target"]: r for e in tops.values() for r in e["after"]}
                        rendered = [r for r in out["form_checks"] if r["target"].startswith("layer[")]
                        self.assertEqual(len(rendered), len(ranked))
                        for r in rendered:  # the ranked layer rows are render's, value for value
                            self.assertEqual((r["value"], r["result"]),
                                             (ranked[r["target"]]["value"], ranked[r["target"]]["result"]), r["target"])
                        if v["action"] == "use":
                            self.assertEqual((rcode, out["must_failed"]), (0, []))
                            self.assertTrue(doc["proof"]["agrees"])
                        elif v["action"] == "mix_misses":
                            self.assertEqual(rcode, 1)
                            self.assertEqual(v["mix_must_misses"],
                                             [t for t in out["must_failed"] if not t.startswith("layer[")])
                        else:
                            self.assertTrue(v["layers_without_a_passing_take"])
                            for name in v["layers_without_a_passing_take"]:
                                self.assertTrue(tops[name]["must_after"] or tops[name]["rejected"])
        print(f"\nlayered real rounds: {verdicts}", file=sys.stderr)

    def test_layers_loops_and_variants_from_real_takes(self):
        """J020 step 6 on real takes: every round as one variant file per take and as seeded variants of its first take
        (G-1 in-process, R-31 and the count rows present, never a refusal); each hit or thump layered over the first
        whoosh, each layer on its marker to the sample and the mix exported; beds of 2, 10 and 30 s spliced from the
        real takes slowed x4 looped with loop_bed: every must loop row passes on the good loop, and a spike 3 samples
        before the end of the delivered loop is caught by a wrap row."""
        rounds: dict = {}
        for mp3 in TAKES:
            found = re.match(r"^(.+)\.t(\d+)$", mp3.stem)
            if found:
                rounds.setdefault(found[1], []).append((int(found[2]), mp3))
        edit = [{"op": "trim"}, {"op": "fade", "out_ms": 10}, {"op": "loudness"}, {"op": "peak"}]
        level = {"measure": "F-09", "target": -24.0, "tolerance": 1.0, "must": False}
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            masters: dict = {}
            for sound, takes in sorted(rounds.items()):
                kind = "whoosh" if re.search(r"whoosh|swish", sound) else "hit"
                for how in ("takes", "seeded"):
                    with self.subTest(sound=sound, variants=how):
                        cue = "REAL-V-" + how.upper() + "-" + re.sub(r"[^A-Za-z0-9-]", "-", sound)
                        folder = root / cue
                        (folder / "takes").mkdir(parents=True)
                        rels = []
                        for n, src in sorted(takes):
                            rel = f"takes/{cue}.r1.t{n}.mp3"
                            shutil.copyfile(src, folder / rel)
                            intake.decode_take(folder / rel, requested_ms=requested_ms(src))
                            rels.append(rel)
                            masters.setdefault((sound, n), folder / rel)
                        count = len(rels) if how == "takes" else 4
                        c = {"cue": cue, "kind": kind, "category": "sfx", "tier": "frequent", "level": level,
                             "targets": {"edge_clicks": {"max": 0, "must": True}}, "form": {"variants": count},
                             "playback": PLAYBACK}
                        rec = ({"cue": cue, "takes": rels, "design": [], "edit": edit} if how == "takes" else
                               {"cue": cue, "take": rels[0], "design": [], "edit": edit,
                                "variants": {"seed": 1, "max_cents": 60, "max_db": 0.5}})
                        (folder / "card.json").write_text(json.dumps(c), encoding="utf-8")
                        (folder / "recipe.json").write_text(json.dumps(rec), encoding="utf-8")
                        doc, code = render.render(folder)
                        self.assertIn(code, (0, 1))
                        hashes = [o["export"]["audio_sha256_float32"] for o in doc["outputs"]]
                        self.assertEqual(len(hashes), count)
                        self.assertEqual(len(set(hashes)), count)
                        rows = {r["target"]: r for r in doc["form_checks"]}
                        self.assertEqual(rows["form.variants"]["result"], "pass")
                        self.assertIn("variants.level_spread", rows)
                        again, _ = render.render(folder)  # G-1: the same recipe gives the same audio
                        self.assertEqual([o["export"]["audio_sha256_float32"] for o in again["outputs"]], hashes)
            whoosh = next(p for (s, n), p in sorted(masters.items()) if re.search(r"whoosh", s) and n == 1)
            for (sound, n), src in sorted(masters.items()):
                if n != 1 or not re.search(r"hit|thump", sound):
                    continue
                with self.subTest(layers=sound):
                    cue = "REAL-L-" + re.sub(r"[^A-Za-z0-9-]", "-", sound)
                    folder = root / cue
                    (folder / "takes").mkdir(parents=True)
                    for stem, p in (("air", whoosh), ("hit", src)):  # a copy of each take, its sidecar and master
                        dst = folder / "takes" / f"{stem}.r1.t1.mp3"
                        shutil.copyfile(p, dst)
                        shutil.copyfile(p.with_suffix(".json"), dst.with_suffix(".json"))
                        shutil.copyfile(intake.master_path(p), intake.master_path(dst))
                    c = {"cue": cue, "kind": "hit", "category": "sfx", "tier": "minor", "level": level,
                         "targets": {"true_peak_dbtp": {"max": -1.0, "must": True}}, "playback": PLAYBACK}
                    rec = {"cue": cue, "layers": [
                        {"name": "air", "take": "takes/air.r1.t1.mp3", "design": [{"op": "highpass", "hz": 300}],
                         "align": {"to_ms": 5.0, "on": "F-01"}, "gain_db": -6.0},
                        {"name": "hit", "take": "takes/hit.r1.t1.mp3", "design": [],
                         "align": {"to_ms": 300.0, "on": "main_transient"}}],
                        "design": [], "edit": [{"op": "loudness"}, {"op": "peak"}]}
                    (folder / "card.json").write_text(json.dumps(c), encoding="utf-8")
                    (folder / "recipe.json").write_text(json.dumps(rec), encoding="utf-8")
                    doc, code = render.render(folder)
                    self.assertIn(code, (0, 1))
                    self.assertNotIn("true_peak_dbtp", doc["must_failed"])
                    ls = doc["layers"]["layers"]
                    self.assertAlmostEqual(ls[0]["measured"]["F-01_onset_ms"], 5.0, delta=1000 / 44100 + 0.001)
                    self.assertAlmostEqual(ls[1]["measured"]["main_transient_ms"], 300.0, delta=1000 / 44100 + 0.005)
                    self.assertAlmostEqual(sum(e["share_of_mix"] for e in ls), 1.0, delta=2e-3)
                    self.assertIn("exportable", doc["layers"]["headroom"])
            groups = {"whoosh": [p for (s, n), p in masters.items() if re.search(r"whoosh|swish", s)],
                      "note": [p for (s, n), p in masters.items() if re.search(r"note", s)],
                      "all": list(masters.values())}
            for name, paths in sorted(groups.items()):
                parts = [fx.slow(read_float32(intake.master_path(p))[0].astype(np.float64)) for p in paths]
                for sec in (2, 10, 30):
                    with self.subTest(bed=name, seconds=sec):
                        cue = f"REAL-LOOP-{name.upper()}-{sec}"
                        folder = root / cue
                        bed = fx.chain(parts, 44100, sec + 0.5, seed=sec)
                        bed = bed / float(np.max(np.abs(bed))) * 10 ** (-12 / 20)  # chain works at unit RMS
                        add_stand_in_take(folder, f"takes/{cue}.r1.t1.mp3", bed, 44100)
                        c = {"cue": cue, "kind": "loop_bed", "category": "ambience", "tier": "minor", "level": level,
                             "form": {"loop": True}, "playback": PLAYBACK}
                        rec = {"cue": cue, "take": f"takes/{cue}.r1.t1.mp3", "design": [], "edit": [],
                               "loop": {"op": "loop_bed", "crossfade_ms": 250}}
                        (folder / "card.json").write_text(json.dumps(c), encoding="utf-8")
                        (folder / "recipe.json").write_text(json.dumps(rec), encoding="utf-8")
                        doc, code = render.render(folder)
                        self.assertEqual(code, 0, doc["must_failed"])
                        y = read_float32(folder / "out" / f"{cue}.flac")[0].astype(np.float64)
                        y[-3] += 0.25 * float(np.max(np.abs(y)))
                        bad, _ = render.loop_rows(c, measures_f08(y), y, 44100, doc["loop"])
                        self.assertTrue({r["target"] for r in bad if r["result"] != "pass"} &
                                        {"form.loop_wrap_clicks", "form.loop_wrap_hf"})


PLAYBACK = {"space": "2D", "takes_room": False, "ducks": None}


def measures_f08(y) -> dict:
    return {"F-08_loop_seam": m.cue_numbers(y - y.mean(axis=0), 44100)["F-08_loop_seam"]}


def add_stand_in_take(cue_dir: Path, rel: str, x, rate: int) -> None:
    """A built bed as a take: a stand-in take file, its master WAV and a sidecar with the intake record."""
    from tools.audio.soundbench.core import audio_sha256, file_sha256

    take = cue_dir / rel
    take.parent.mkdir(parents=True, exist_ok=True)
    take.write_bytes(b"stand-in take bytes for " + rel.encode())
    fx.write_wav(intake.master_path(take), x, rate)
    y, _ = read_float32(intake.master_path(take))
    side = {"prompt": "bed built from real takes", "intake": {"take_sha256": file_sha256(take),
                                                              "master_audio_sha256": audio_sha256(y), "rate": rate,
                                                              "decoder": "test (no decode)"}}
    take.with_suffix(".json").write_text(json.dumps(side), encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
