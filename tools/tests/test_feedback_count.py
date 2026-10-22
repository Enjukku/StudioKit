#!/usr/bin/env python3
"""Offline tests for tools/liveops/feedback_count.py (temp dirs only, fake author keys). J014-T06."""
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "liveops"))
import feedback_count as fc  # noqa: E402

START, END = "2026-10-01T00:00:00Z", "2026-10-08T00:00:00Z"
EXAMPLE = Path(__file__).resolve().parent.parent / "liveops" / "items.example.jsonl"


def item(n, author, source="discord", themes=("t.shop",), when="2026-10-02T12:00:00Z", **kw):
    return {"item_id": f"i-{n:04d}", "source": source, "author_key": author, "occurred_at_utc": when,
            "themes": list(themes), **kw}


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rows, name="items.jsonl"):
        path = self.dir / name
        path.write_text("\n".join(r if isinstance(r, str) else json.dumps(r) for r in rows) + "\n", encoding="utf-8")
        return str(path)

    def run_cli(self, *argv):
        out, err = StringIO(), StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = fc.main(list(argv))
        return code, out.getvalue(), err.getvalue()

    def count_json(self, rows, *extra):
        code, out, err = self.run_cli("count", self.write(rows), "--start", START, "--end", END, "--json", *extra)
        return code, json.loads(out), err

    @staticmethod
    def theme(result, theme, source):
        rows = [t for t in result["themes"] if t["theme"] == theme and t["source"] == source]
        return rows[0] if rows else None


class Counting(Base):
    def test_one_author_25_items_one_theme_counts_once(self):  # C1
        rows = [item(n, "a-001") for n in range(25)] + [item(100, "a-002", themes=())]
        code, r, _ = self.count_json(rows)
        self.assertEqual(code, 0)
        t = self.theme(r, "t.shop", "discord")
        self.assertEqual((t["distinct_authors"], t["sampled_authors"], t["messages"]), (1, 2, 25))
        self.assertEqual(t["share"], 0.5)
        self.assertTrue(any("one loud author: 25 of 25" in f for f in t["flags"]))

    def test_one_author_two_tags_counts_once_in_each_theme(self):  # C1
        rows = [item(1, "a-001", themes=("t.shop", "t.lag")), item(2, "a-001", themes=("t.shop", "t.lag", "t.shop")),
                item(3, "a-002", themes=("t.lag",))]
        _, r, _ = self.count_json(rows)
        shop, lag = self.theme(r, "t.shop", "discord"), self.theme(r, "t.lag", "discord")
        self.assertEqual((shop["distinct_authors"], shop["messages"]), (1, 2))
        self.assertEqual((lag["distinct_authors"], lag["messages"]), (2, 3))
        self.assertEqual(lag["sampled_authors"], 2)

    def test_same_author_two_sources_without_scheme_overlap_unknown_no_combined(self):  # C1
        rows = [item(1, "a-001", source="discord"), item(2, "a-001", source="in-game")]
        code, out_md, _ = self.run_cli("count", self.write(rows), "--start", START, "--end", END)
        _, r, _ = self.count_json(rows)
        self.assertEqual(r["overlap"]["status"], "unknown")
        self.assertEqual(r["overlap"]["themes"], [])
        self.assertEqual(self.theme(r, "t.shop", "discord")["distinct_authors"], 1)
        self.assertEqual(self.theme(r, "t.shop", "in-game")["distinct_authors"], 1)
        self.assertIn("**unknown**", out_md)
        self.assertNotIn("distinct across", out_md)

    def test_same_author_two_sources_with_scheme_combined_is_one(self):  # C1
        rows = [item(1, "a-001", source="discord"), item(2, "a-001", source="in-game"),
                item(3, "a-002", source="in-game")]
        code, r, _ = self.count_json(rows, "--same-key-scheme", "discord,in-game")
        self.assertEqual(code, 0)
        row = r["overlap"]["themes"][0]
        self.assertEqual((row["theme"], row["distinct_authors"], row["possible_cross_source_overlap"]),
                         ("t.shop", 2, 1))
        rows1 = rows[:2]
        _, r1, _ = self.count_json(rows1, "--same-key-scheme", "discord,in-game")
        self.assertEqual(r1["overlap"]["themes"][0]["distinct_authors"], 1)
        _, md, _ = self.run_cli("count", self.write(rows1), "--start", START, "--end", END,
                                "--same-key-scheme", "discord,in-game")
        self.assertIn("1 (distinct across discord, in-game)", md)

    def test_scheme_does_not_merge_a_source_outside_it(self):
        rows = [item(1, "a-001", source="discord"), item(2, "a-001", source="reviews")]
        _, r, _ = self.count_json(rows, "--same-key-scheme", "discord,in-game")
        self.assertEqual(r["overlap"]["themes"][0]["distinct_authors"], 1)
        self.assertEqual(r["overlap"]["outside_scheme"], ["reviews"])

    def test_window_start_inclusive_end_exclusive(self):  # C1
        rows = [item(1, "a-001", when=START), item(2, "a-002", when=END),
                item(3, "a-003", when="2026-09-30T23:59:59Z"), item(4, "a-004", when="2026-10-07T23:59:59Z")]
        _, r, _ = self.count_json(rows)
        t = self.theme(r, "t.shop", "discord")
        self.assertEqual((t["distinct_authors"], t["sampled_authors"], t["messages"]), (2, 2, 2))

    def test_untagged_items_count_in_sampled_authors_not_in_themes(self):  # C1
        rows = [item(1, "a-001"), item(2, "a-002", themes=()), item(3, "a-003", themes=())]
        _, r, _ = self.count_json(rows)
        self.assertEqual(r["sampling"][0], {"source": "discord", "status": "data", "items": 3,
                                            "sampled_authors": 3, "untagged_items": 2})
        self.assertEqual([(t["theme"], t["distinct_authors"]) for t in r["themes"]], [("t.shop", 1)])
        self.assertEqual(self.theme(r, "t.shop", "discord")["sampled_authors"], 3)

    def test_share_is_within_one_source_only(self):
        rows = [item(1, "a-001", source="discord"), item(2, "a-002", source="discord", themes=()),
                item(3, "a-003", source="in-game"), item(4, "a-004", source="in-game", themes=()),
                item(5, "a-005", source="in-game", themes=()), item(6, "a-006", source="in-game", themes=())]
        _, r, _ = self.count_json(rows)
        self.assertEqual(self.theme(r, "t.shop", "discord")["share"], 1 / 2)
        self.assertEqual(self.theme(r, "t.shop", "in-game")["share"], 1 / 4)

    def test_source_with_no_items_in_window_is_no_data_not_zero(self):
        rows = [item(1, "a-001", source="discord"), item(2, "a-002", source="support", when="2026-09-01T00:00:00Z")]
        code, md, _ = self.run_cli("count", self.write(rows), "--start", START, "--end", END)
        _, r, _ = self.count_json(rows)
        self.assertIn({"source": "support", "status": "no data in window"}, r["sampling"])
        self.assertIsNone(self.theme(r, "t.shop", "support"))
        self.assertIn("| support | no data in window |", md)
        self.assertNotIn("| support | 0", md)

    def test_urgent_listed_and_also_counted(self):
        rows = [item(1, "a-001", urgent=True, severity="critical"), item(2, "a-002")]
        _, r, _ = self.count_json(rows)
        self.assertEqual(r["urgent"], [{"source": "discord", "item_ids": ["i-0001"]}])
        self.assertEqual(self.theme(r, "t.shop", "discord")["distinct_authors"], 2)


class Validation(Base):
    def test_duplicate_item_id_rejected_with_line_number_and_exit_1(self):  # C1
        rows = [item(1, "a-001"), item(2, "a-002"), item(1, "a-003")]
        code, r, err = self.count_json(rows)
        self.assertEqual(code, 1)
        self.assertEqual(len(r["rejected_lines"]), 1)
        self.assertIn("items.jsonl:3: duplicate item_id", r["rejected_lines"][0])
        self.assertEqual(self.theme(r, "t.shop", "discord")["distinct_authors"], 2)  # good lines still counted
        self.assertIn("REJECTED items.jsonl:3", err)

    def test_duplicate_item_id_across_files(self):
        a = self.write([item(1, "a-001")], "a.jsonl")
        b = self.write([item(1, "a-002")], "b.jsonl")
        code, out, err = self.run_cli("validate", a, b)
        self.assertEqual(code, 1)
        self.assertIn("b.jsonl:1: duplicate item_id", err)

    def test_bad_lines_rejected_good_lines_counted(self):
        bad = [
            "{not json",
            json.dumps({k: v for k, v in item(10, "a-010").items() if k != "author_key"}),
            json.dumps(item(11, "a-011", when="2026-10-02 12:00:00")),
            json.dumps(item(12, "a-012", when="2026-10-02T12:00:00+02:00")),
            json.dumps(item(13, "a-013", source="twitter")),
            json.dumps({**item(14, "a-014"), "themes": "t.shop"}),
            json.dumps(item(15, "a-015", severity="huge")),
            json.dumps(item(16, "a-016", urgent="yes")),
            json.dumps(item(17, "a-017", excerpt="x" * 281)),
            json.dumps(item(18, "")),
            json.dumps(item(19, "a-019", when="2026-10-02")),
            "[1, 2]",
        ]
        good = [item(1, "a-001", excerpt="x" * 280, cohort="new", build="1.2", extra_field={"kept": True})]
        code, r, _ = self.count_json(good + bad)
        self.assertEqual(code, 1)
        self.assertEqual(len(r["rejected_lines"]), len(bad))
        self.assertEqual([int(x.split(":")[1]) for x in r["rejected_lines"]], list(range(2, 2 + len(bad))))
        self.assertEqual(self.theme(r, "t.shop", "discord")["distinct_authors"], 1)

    def test_validate_clean_file_exit_0(self):
        code, out, err = self.run_cli("validate", self.write([item(1, "a-001")]))
        self.assertEqual((code, err), (0, ""))
        self.assertIn("1 good item(s), 0 rejected", out)

    def test_bad_arguments_exit_2(self):
        path = self.write([item(1, "a-001")])
        for argv in (["--start", END, "--end", START], ["--start", "x", "--end", END],
                     ["--start", START, "--end", END, "--same-key-scheme", "discord"],
                     ["--start", START, "--end", END, "--same-key-scheme", "discord,twitter"]):
            self.assertEqual(self.run_cli("count", path, *argv)[0], 2, argv)
        self.assertEqual(self.run_cli("validate", str(self.dir / "missing.jsonl"))[0], 2)

    def test_relative_path_resolves_in_data_dir(self):
        self.write([item(1, "a-001")], "week.jsonl")
        os.environ["FEEDBACK_DATA_DIR"] = str(self.dir)
        try:
            code, out, _ = self.run_cli("validate", "week.jsonl")
        finally:
            del os.environ["FEEDBACK_DATA_DIR"]
        self.assertEqual(code, 0)


class Privacy(Base):
    def test_output_never_contains_author_keys(self):  # C2
        keys = [f"a-{n:03d}" for n in range(1, 8)] + ["zz-secret-key-9"]
        rows = [item(n, k, source=s, themes=th, urgent=(n == 3))
                for n, (k, s, th) in enumerate(zip(keys, ["discord", "in-game", "support", "reviews"] * 2,
                                                   [("t.shop",), ("t.lag", "t.shop"), (), ("t.lag",)] * 2))]
        rows.append(json.dumps(item(1, "zz-dup-author")))           # rejected duplicate
        rows.append(json.dumps(item(50, "zz-bad-time", when="bad")))  # rejected bad time
        keys += ["zz-dup-author", "zz-bad-time"]
        path = self.write(rows)
        outputs = []
        for extra in ([], ["--json"], ["--same-key-scheme", "discord,in-game"],
                      ["--same-key-scheme", "discord,in-game", "--json"]):
            code, out, err = self.run_cli("count", path, "--start", START, "--end", END, *extra)
            self.assertEqual(code, 1)
            outputs += [out, err]
        file_out = self.dir / "out" / "counts.md"
        self.run_cli("count", path, "--start", START, "--end", END, "--out", str(file_out))
        outputs.append(file_out.read_text(encoding="utf-8"))
        outputs += list(self.run_cli("validate", path)[1:])
        for text in outputs:
            for k in keys:
                self.assertNotIn(k, text)


class ExampleFile(Base):
    def test_example_file_is_valid_and_uses_fake_keys(self):
        code, out, err = self.run_cli("validate", str(EXAMPLE))
        self.assertEqual((code, err), (0, ""))
        for line in EXAMPLE.read_text(encoding="utf-8").splitlines():
            self.assertRegex(json.loads(line)["author_key"], r"^a-\d{3}$")

    def test_example_counts(self):
        code, out, _ = self.run_cli("count", str(EXAMPLE), "--start", START, "--end", END, "--json")
        r = json.loads(out)
        self.assertEqual(code, 0)
        loud = self.theme(r, "economy.upgrade-cost", "discord")
        self.assertEqual((loud["distinct_authors"], loud["messages"]), (1, 6))
        self.assertTrue(loud["flags"])


if __name__ == "__main__":
    unittest.main()


class J018FixesTest(Base):
    """J018 live-ops review: a date-only --end dropped the last day; several loud authors raised no flag."""

    def test_date_only_end_includes_that_day(self):
        rows = [item(1, "a", when="2026-10-07T18:00:00Z")]
        code, out, _ = self.run_cli("count", self.write(rows), "--start", "2026-10-01", "--end", "2026-10-07", "--json")
        self.assertEqual(code, 0)
        res = json.loads(out)
        self.assertTrue(res["window"]["end_utc"].startswith("2026-10-08"))
        self.assertEqual(sum(t["distinct_authors"] for t in res["themes"]), 1)

    def test_a_few_loud_authors_flag(self):
        rows, n = [], 0
        for a in ("l1", "l2", "l3", "l4"):
            for _ in range(6):
                n += 1
                rows.append(item(n, a))
        for a in ("q1", "q2", "q3", "q4"):
            n += 1
            rows.append(item(n, a))
        code, out, _ = self.run_cli("count", self.write(rows), "--start", START, "--end", END, "--json")
        flags = json.loads(out)["themes"][0]["flags"]
        self.assertTrue(any("a few loud authors" in f for f in flags), flags)
        self.assertFalse(any("one loud author" in f for f in flags))
