"""Offline tests for tools/env/scene_audit.py (no Roblox Studio needed)."""

import contextlib
import copy
import io
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "env"))
import scene_audit as sa  # noqa: E402

FIX = ROOT / "tools" / "tests" / "fixtures" / "env"
PROBE = json.loads((FIX / "probe_stage.json").read_text(encoding="utf-8"))
MAP = sa.parse_ambience_map((FIX / "ambience-map.md").read_text(encoding="utf-8"))
S = "Workspace.Stage."


def probe(drop=()):
    d = copy.deepcopy(PROBE)
    d["parts"] = [p for p in d["parts"] if p["path"].rsplit(".", 1)[1] not in drop]
    return d


def paths(r):
    return [i["path"].rsplit(".", 1)[1] for i in r["listed"]]


class FloatingTest(unittest.TestCase):
    def test_lists_gaps_without_tolerance(self):
        r = sa.check_floating(PROBE["parts"])
        self.assertEqual(r["verdict"], "MEASURED")
        self.assertEqual(paths(r), ["Lantern", "Crate", "StrayRock"])
        self.assertEqual([i["gap"] for i in r["listed"]], [4.5, 0.1, "NO_HIT"])
        self.assertEqual([u["path"] for u in r["unknown"]], [S + "Mystery"])
        self.assertEqual(r["skipped_unanchored_or_invisible"], 2)  # Ball, Blocker

    def test_tolerance_gives_pass_fail_or_unverified(self):
        r = sa.check_floating(PROBE["parts"], 0.5)
        self.assertEqual(r["verdict"], "FAIL")
        self.assertEqual([i["over_tolerance"] for i in r["listed"]], [True, False, True])
        clean = probe(drop=("Lantern", "StrayRock", "Mystery"))["parts"]
        self.assertEqual(sa.check_floating(clean, 0.5)["verdict"], "PASS")
        self.assertEqual(sa.check_floating(clean + [PROBE["parts"][9]], 0.5)["verdict"], "UNVERIFIED")

    def test_rotated_part_uses_world_height(self):
        # 10 x 1 x 1 part turned 90 degrees about Z: world half-height 5; ground hit 6 below the centre
        p = {"path": "W.Beam", "anchored": True, "transparency": 0, "contacts": 0, "down_hit": "W.G", "down_dist": 6.0,
             "cf": [0, 6, 0, 0, -1, 0, 1, 0, 0, 0, 0, 1], "size": [10, 1, 1]}
        self.assertAlmostEqual(sa.check_floating([p])["listed"][0]["gap"], 1.0)


class BuriedTest(unittest.TestCase):
    def test_terrain_depth_and_enclosure(self):
        r = sa.check_buried(PROBE["parts"])
        self.assertEqual(r["verdict"], "MEASURED")
        self.assertEqual(paths(r), ["SunkLog", "HiddenBox"])
        self.assertEqual(r["listed"][0]["depth"], 1.5)
        self.assertEqual(r["listed"][1]["enclosed_by"], S + "Ground")
        self.assertIn("bounding-box estimate", r["method"])

    def test_tolerance(self):
        self.assertEqual(sa.check_buried(PROBE["parts"], 2.0)["verdict"], "FAIL")  # enclosure fails any tolerance
        self.assertEqual(sa.check_buried(probe(drop=("HiddenBox",))["parts"], 2.0)["verdict"], "PASS")
        self.assertEqual(sa.check_buried(probe(drop=("HiddenBox",))["parts"], 1.0)["verdict"], "FAIL")


class OutOfBoundsTest(unittest.TestCase):
    def test_overshoot(self):
        r = sa.check_out_of_bounds(PROBE["parts"], PROBE["play_areas"])
        self.assertEqual((paths(r), r["listed"][0]["overshoot"], r["verdict"]), (["StrayRock"], 91.0, "MEASURED"))
        self.assertEqual(sa.check_out_of_bounds(PROBE["parts"], PROBE["play_areas"], 100)["verdict"], "PASS")
        self.assertEqual(sa.check_out_of_bounds(PROBE["parts"], PROBE["play_areas"], 0)["verdict"], "FAIL")

    def test_no_play_area_is_not_checked(self):
        self.assertEqual(sa.check_out_of_bounds(PROBE["parts"], [])["verdict"], "NOT_CHECKED")


class ZoneCountTest(unittest.TestCase):
    def test_counts(self):
        z = sa.zone_counts(PROBE)["zones"]
        f = z["Z-FALLS"]
        self.assertEqual((f["parts"], f["mesh_parts"], f["lights"], f["lights_with_shadows"], f["cast_shadow_parts"],
                          f["audio_sources"], f["particle_emitters"]), (10, 1, 2, 1, 7, 4, 1))
        self.assertEqual(f["lights_by_class"], {"PointLight": 1, "SurfaceLight": 1})
        self.assertEqual(f["unknown"], {"cast_shadow": 1, "shadows": 1})
        self.assertEqual(f["triangles"], "UNKNOWN")
        c = z["Z-CAVE"]
        self.assertEqual((c["parts"], c["lights_by_class"], c["audio_by_class"]), (1, {"SpotLight": 1}, {"Sound": 2}))
        self.assertEqual(z["Z-ROOF"]["parts"], 0)
        self.assertEqual((z["unzoned"]["parts"], z["unpositioned"]["audio_sources"]), (1, 1))
        self.assertEqual(f["verdict"], "MEASURED")

    def test_budgets(self):
        b = {"zones": {"*": {"lights_with_shadows": 1}, "Z-FALLS": {"parts": 5}, "Z-CAVE": {"triangles": 1000}}}
        z = sa.zone_counts(PROBE, b)["zones"]
        self.assertEqual(z["Z-FALLS"]["verdicts"], {"lights_with_shadows": "UNVERIFIED", "parts": "FAIL"})
        self.assertEqual(z["Z-CAVE"]["verdicts"], {"lights_with_shadows": "PASS", "triangles": "UNVERIFIED"})
        self.assertEqual(z["unzoned"]["verdict"], "MEASURED")
        with self.assertRaises(ValueError):
            sa.audit(PROBE, budgets={"zones": {"*": {"lamps": 3}}})


class MapTest(unittest.TestCase):
    def test_parse_reads_only_yaml_blocks_in_b_and_c(self):
        self.assertEqual(MAP["zones"], ["Z-FALLS", "Z-CAVE", "Z-SWAMP"])
        self.assertEqual([s["id"] for s in MAP["sources"]], ["FALL-MAIN", "RIVER-OUT", "CAVE-DRIP", "BIRDS", "CAVE-DRIP"])
        self.assertEqual(MAP["sources"][1]["kind"], "sound+effect")

    def test_every_mismatch_kind(self):
        r = sa.map_vs_place(PROBE, MAP)
        self.assertEqual(r["map_zones_missing_in_place"], ["Z-SWAMP"])
        self.assertEqual(r["place_zones_missing_in_map"], ["Z-ROOF"])
        self.assertEqual(r["map_sources_missing_in_place"], ["BIRDS"])
        self.assertEqual(r["place_sources_missing_in_map"], ["GHOST-ID"])
        self.assertEqual(r["unlisted_audio"], [S + "Lantern.Creak"])  # under the stage root: FAIL
        self.assertEqual(r["global_audio"], {"listed": ["SoundService.Music"], "verdict": "MEASURED"})
        self.assertEqual([(k["id"], k["missing"][:6]) for k in r["kind_mismatch"]], [("RIVER-OUT", "effect")])
        self.assertEqual(r["duplicates"], {"map_zone_ids": [], "map_source_ids": ["CAVE-DRIP"],
                                           "place_source_ids": ["CAVE-DRIP"]})
        self.assertEqual(r["verdict"], "FAIL")

    def test_matching_map_passes_and_each_defect_fails_alone(self):
        d = copy.deepcopy(PROBE)
        d["objects"] = [o for o in d["objects"] if o.get("anchor_id")]
        d["anchors"] = [a for a in d["anchors"] if a["path"] != S + "CaveDrip2"]
        m = {"zones": ["Z-FALLS", "Z-CAVE", "Z-ROOF"],
             "sources": [{"id": i, "kind": "sound"} for i in ("FALL-MAIN", "RIVER-OUT", "CAVE-DRIP", "GHOST-ID")]}
        self.assertEqual(sa.map_vs_place(d, m)["verdict"], "PASS")
        dup = copy.deepcopy(m)
        dup["zones"].append("Z-ROOF")
        self.assertEqual(sa.map_vs_place(d, dup)["verdict"], "FAIL")
        d["zones"][2].pop("zone_id")
        r = sa.map_vs_place(d, m)
        self.assertEqual(r["zone_volumes_without_zone_id"], [S + "Zones.Roof"])
        self.assertEqual(r["verdict"], "FAIL")

    def test_two_volumes_one_zone_id(self):
        d = copy.deepcopy(PROBE)
        d["zones"].append({"path": S + "Zones.FallsWing", "zone_id": "Z-FALLS",
                           "cf": [300, 5, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], "size": [10, 10, 10]})
        z = sa.zone_counts(d)["zones"]
        self.assertEqual((z["Z-FALLS"]["parts"], z["unzoned"]["parts"]), (11, 0))  # StrayRock now in the wing
        r = sa.map_vs_place(d, MAP)
        self.assertNotIn("place_zone_ids", r["duplicates"])
        self.assertEqual(r["place_zones_missing_in_map"], ["Z-ROOF"])
        d["objects"] = [o for o in d["objects"] if o.get("anchor_id") or o.get("scope") != "stage"]
        d["anchors"] = [a for a in d["anchors"] if a["path"] != S + "CaveDrip2"]
        m = {"zones": ["Z-FALLS", "Z-CAVE", "Z-ROOF"],
             "sources": [{"id": i, "kind": "sound"} for i in ("FALL-MAIN", "RIVER-OUT", "CAVE-DRIP", "GHOST-ID")]}
        r = sa.map_vs_place(d, m)
        self.assertEqual((r["verdict"], r["global_audio"]["listed"]), ("PASS", ["SoundService.Music"]))

    def test_no_map_is_not_checked(self):
        self.assertEqual(sa.map_vs_place(PROBE, None)["verdict"], "NOT_CHECKED")


class ProbeIoTest(unittest.TestCase):
    def test_slices_join_in_any_order_with_log_noise(self):
        doc = json.dumps(PROBE)
        n = 3
        size = math.ceil(len(doc) / n)
        lines = [f"SCENE_PROBE {k}/{n} {doc[(k - 1) * size:k * size]}" for k in range(1, n + 1)]
        text = ["12:00:01  " + lines[2], lines[0] + "\n" + lines[0], "Output: " + lines[1]]
        self.assertEqual(sa.load_probe(text), PROBE)
        with self.assertRaises(ValueError):
            sa.load_probe([lines[0], lines[2]])

    def test_plain_json_and_probe_error(self):
        self.assertEqual(sa.load_probe([json.dumps(PROBE)])["root"], "Workspace.Stage")
        with self.assertRaises(ValueError):
            sa.load_probe(['SCENE_PROBE 1/1 {"error": "root not found: Workspace/Nope"}'])

    def test_probe_source_config_and_static_shape(self):
        src = sa.probe_source("Workspace/Stages/Falls", 800, 60000, 2)
        self.assertIn('local ROOT_PATH = "Workspace/Stages/Falls"', src)
        self.assertIn("local CHUNK_SIZE = 60000", src)
        self.assertIn("local CHUNK_INDEX = 2", src)
        self.assertTrue(src.startswith("--!strict"))
        for bad in ("Instance.new", ":Destroy(", ":Clone(", "def ", "import "):
            self.assertNotIn(bad, src)
        with self.assertRaises(ValueError):
            sa.probe_source('Workspace/"; os.exit()')


class UnknownFieldTest(unittest.TestCase):
    def test_missing_fields_are_unknown_not_defaults(self):
        d = {"parts": [{"path": "W.A", "anchored": True, "transparency": 0}],  # no cf, size, rays, contacts
             "zones": [], "play_areas": [{"path": "W.PA", "cf": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], "size": [9, 9, 9]}],
             "objects": [{"kind": "light", "class": "PointLight", "path": "W.L", "positioned": True, "pos": [0, 0, 0]}]}
        r = sa.audit(d, floating_tol=1, buried_tol=1, oob_tol=1,
                     budgets={"unzoned": {"lights_with_shadows": 5}, "unpositioned": {"parts": 1}})
        for k in ("floating", "buried", "out_of_bounds"):
            self.assertEqual(r[k]["verdict"], "UNVERIFIED", k)
            self.assertEqual(r[k]["listed"], [], k)
        self.assertEqual(r["per_zone_counts"]["zones"]["unzoned"]["unknown"], {"shadows": 1})
        self.assertEqual(r["per_zone_counts"]["zones"]["unzoned"]["verdicts"], {"lights_with_shadows": "UNVERIFIED"})
        self.assertEqual(r["per_zone_counts"]["zones"]["unpositioned"]["parts"], 1)  # no cf: position unknown
        self.assertEqual(r["triangles"], "UNKNOWN")
        self.assertEqual(r["verdict"], "UNVERIFIED")


class CliTest(unittest.TestCase):
    def test_audit_writes_json_and_markdown(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review" / "audit.json"
            with contextlib.redirect_stdout(io.StringIO()):
                code = sa.main(["audit", "--probe", str(FIX / "probe_stage.json"), "--map", str(FIX / "ambience-map.md"),
                                "--floating-tol", "0.5", "--out", str(out)])
            self.assertEqual(code, 1)
            report = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual((report["verdict"], report["floating"]["tolerance"], report["buried"]["verdict"]),
                             ("FAIL", 0.5, "MEASURED"))
            md = out.with_suffix(".md").read_text(encoding="utf-8")
            self.assertIn("| Z-FALLS | 10 | 1 | 2 | 1 | 7 | 4 | 1 | UNKNOWN | MEASURED |", md)


if __name__ == "__main__":
    unittest.main()


class DiffProbesTest(unittest.TestCase):
    """J018 G3-P8: the current place against the approved blockout's probe."""

    def p(self, path, x, collide=True, size=(4, 1, 4)):
        return {"path": path, "cf": [x, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], "size": list(size), "can_collide": collide}

    def test_added_removed_moved_and_collision(self):
        base = {"parts": [self.p("W.Wall", 0), self.p("W.Cover", 10), self.p("W.Old", 20)]}
        cur = {"parts": [self.p("W.Wall", 0.2), self.p("W.Cover", 12, collide=False), self.p("W.New", 30)]}
        d = sa.diff_probes(base, cur, 0.5)
        self.assertEqual(d["added"], ["W.New"])
        self.assertEqual(d["removed"], ["W.Old"])
        self.assertEqual([m["path"] for m in d["moved"]], ["W.Cover"])      # 0.2 studs stays under the step
        self.assertEqual(d["collision_changed"][0]["path"], "W.Cover")
        self.assertEqual(d["colliding_added"], ["W.New"])

    def test_old_probe_without_collision_is_unknown(self):
        old = {"parts": [{"path": "W.Wall", "cf": [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], "size": [4, 1, 4]}]}
        d = sa.diff_probes(old, {"parts": [self.p("W.Wall", 0)]})
        self.assertEqual(d["collision_unknown"], ["W.Wall"])
