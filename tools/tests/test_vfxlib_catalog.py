"""Offline tests for tools/vfx/vfxlib_catalog.py: codes, difference hash, duplicate finding, tag checks,
catalog merge and the shortlist filter. Standard library only (no network, no PIL).
Run: python -m unittest tools/tests/test_vfxlib_catalog.py
"""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools" / "vfx"))
import vfxlib_catalog as V  # noqa: E402

DATA = {
    "300": {"Name": "Images/a", "Keywords": ["Flare"]},
    "20": {"Name": "Images/b", "Keywords": ["Flare", "Star"]},
    "1000": {"Name": "Images/c", "Keywords": ["Slashes"], "Grid": 4, "Resolution": 1024, "Credits": "x"},
    "5": {"Name": "Images/d", "Keywords": ["Unlisted"]},
}


class Codes(unittest.TestCase):
    def test_codes_sorted_numeric_per_group(self):
        c = V.assign_codes(DATA)
        self.assertEqual(c["20"], "FL-0001")
        self.assertEqual(c["300"], "FL-0002")
        self.assertEqual(c["1000"], "SL-0001")

    def test_unknown_group_goes_to_other(self):
        self.assertEqual(V.assign_codes(DATA)["5"], "OT-0001")


class Hashing(unittest.TestCase):
    def test_dhash_gradient(self):
        falling = [[9 - x for x in range(9)] for _ in range(8)]
        self.assertEqual(V.dhash_bits(falling), (1 << 64) - 1)
        rising = [list(range(9)) for _ in range(8)]
        self.assertEqual(V.dhash_bits(rising), 0)

    def test_duplicates_need_same_grid_and_close_hash(self):
        items = [("A", 0b1111, 1), ("B", 0b1110, 1), ("C", 0b1110, 4), ("D", 0, 1), ("E", 0, 1)]
        self.assertEqual(V.find_duplicates(items, max_dist=1), {"B": "A"})

    def test_confirm_can_reject_a_hash_match(self):
        items = [("A", 0b1111, 1), ("B", 0b1110, 1)]
        self.assertEqual(V.find_duplicates(items, max_dist=1, confirm=lambda a, b: False), {})

    def test_visible_diff_ignores_shared_black(self):
        a = bytes([0] * 98 + [200, 0])
        b = bytes([0] * 98 + [0, 200])
        self.assertEqual(V.visible_diff(a, b), 200.0)
        self.assertEqual(V.visible_diff(a, a), 0.0)
        self.assertEqual(V.visible_diff(bytes(4), bytes(4)), 0.0)


class Flipbook(unittest.TestCase):
    def test_flip_frames_span_first_to_last(self):
        self.assertEqual(V.flip_frames(4), [0, 5, 10, 15])
        self.assertEqual(V.flip_frames(8), [0, 21, 42, 63])


class Tags(unittest.TestCase):
    def test_validate(self):
        self.assertEqual(V.validate_tag("FL-0001", {"style": "anime", "quality": "A", "shape": "4-point star"}), [])
        errs = V.validate_tag("FL-0001", {"style": "cool", "quality": "S", "shape": ""})
        self.assertEqual(len(errs), 3)


class MergeAndFilter(unittest.TestCase):
    def setUp(self):
        codes = V.assign_codes(DATA)
        feats = {
            "FL-0001": {"coverage": 0.1, "hardness": 0.9, "saturation": 0.0},
            "FL-0002": {"coverage": 0.2, "hardness": 0.2, "saturation": 0.1},
            "SL-0001": {"dead": True},
            "OT-0001": {"dup_of": "FL-0001"},
        }
        tags = {
            "FL-0001": {"style": "anime", "shape": "4-point star", "quality": "B", "note": "clean spikes"},
            "FL-0002": {"style": "soft", "shape": "round glow", "quality": "A", "note": ""},
        }
        self.rows = V.merge_rows(DATA, codes, feats, tags)

    def test_merge_drops_dead_and_duplicates(self):
        self.assertEqual([r["code"] for r in self.rows], ["FL-0001", "FL-0002"])
        self.assertEqual(self.rows[0]["id"], 20)

    def test_filter_by_style_shape_quality(self):
        self.assertEqual([r["code"] for r in V.filter_rows(self.rows, group="Flare")], ["FL-0002", "FL-0001"])
        self.assertEqual([r["code"] for r in V.filter_rows(self.rows, style="anime", shape="star")], ["FL-0001"])
        self.assertEqual(V.filter_rows(self.rows, min_quality="A", style="anime"), [])

    def test_filter_matches_secondary_keyword(self):
        self.assertEqual([r["code"] for r in V.filter_rows(self.rows, group="Star")], ["FL-0001"])


if __name__ == "__main__":
    unittest.main()
