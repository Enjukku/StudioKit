"""Cutscene workflow tests for the J019 recipe rows (G3-P4: recipe rows of b2eeb73, the risks arg), with fake agents (no tokens).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22.
Runs .agents/workflows/jobs/job-cutscene.js under tools/workflows/wf_harness.mjs; skipped when Node is not installed.
Covers: the risks arg (missing, not a list, unknown token: blocked before any agent); the risk `event` live-ops review after the
creative chain; the blocking and value strips before the boards with the art-director's value-strip review between them; G1 options
with failed options and closed doors; closed doors carried in later briefs; the could-not-check list and owner-confirmed lines in every
gate result; the film-director's read lines in the review chain.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

NAME = "job-cutscene.js"
LIVE_OPS = r"live-ops-designer: RV-candidate-r0-live-ops-designer"
EVENT_CAPS = r"studio-operator: RV-candidate-r0-event-captures"


def cut(**changes) -> dict:
    return full(NAME, **changes)


def dump(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dump matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class CutsceneRecipeTests(unittest.TestCase):
    # ------------------------------------------------------------------ the risks arg
    def test_missing_risks_is_blocked_before_any_agent(self):
        for stage in STAGES:
            with self.subTest(stage=stage):
                out = run(NAME, cut(stage=stage, risks=None))
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn("risks", out["outcome"])
                self.assertIn("risks", out["meta"]["whenToUse"], "whenToUse must name every required arg")

    def test_risks_that_is_not_a_list_is_blocked(self):
        out = run(NAME, cut(stage="build", risks="event"))
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(out["agents"], 0)

    def test_unknown_risk_token_is_blocked_by_name(self):
        for token in ("paid-random", "new-enemy"):
            with self.subTest(token=token):
                out = run(NAME, cut(stage="build", risks=["event", token]))
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    # ------------------------------------------------------------------ risk event: the live-ops event review
    def test_event_adds_the_live_ops_review_only_with_the_token(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                on = run(NAME, cut(stage=stage, risks=["event"]), {"dump": r"live-ops-designer: RV-"})
                off = run(NAME, cut(stage=stage, risks=[]))
                for out in (on, off):
                    self.assertEqual(out["violation"], "")
                    self.assertEqual(out["status"], "done", out["outcome"])
                live_ops = r"live-ops-designer: RV-.*-live-ops-designer"
                self.assertGreaterEqual(index(on["labels"], live_ops), 0)
                self.assertGreaterEqual(index(on["labels"], r"studio-operator: RV-.*-event-captures"), 0)
                self.assertEqual(index(off["labels"], live_ops), -1)
                self.assertEqual(index(off["labels"], r"studio-operator: "), -1)
                brief = dump(on, r"live-ops-designer: RV-")
                for text in ("E-01 to E-19", "event-review.md §3", "model: opus", "effort: medium"):
                    self.assertIn(text, brief)
                self.assertEqual(on["result"]["skipped_slots"], [])
                self.assertTrue(off["result"]["skipped_slots"], "a slot skipped for no risk is a line, not a silent gap")

    def test_event_review_runs_after_the_creative_chain_on_its_captures(self):
        out = run(NAME, cut(stage="build", risks=["event"]), {"timeline": True})
        self.assertEqual(out["violation"], "")
        review = span(out, LIVE_OPS)
        caps = span(out, EVENT_CAPS)
        for creative in (r"film-director: RV-candidate-r0-film-director", r"art-director: RV-candidate-r0-art-director",
                         r"sound-designer: RV-candidate-r0-sound-designer", r"qa-lead: RV-candidate-r0-qa-lead",
                         r"performance-engineer: RV-candidate-r0-performance-engineer"):
            with self.subTest(after=creative):
                self.assertGreaterEqual(caps["start"], span(out, creative)["end"])
        self.assertGreaterEqual(review["start"], caps["end"], "the review judges the event captures")

    def test_event_findings_route_to_makers_inside_the_round_limits(self):
        once = run(NAME, cut(stage="build", risks=["event"]), {"blockLabelOnce": LIVE_OPS, "maker": "vfx-designer"})
        self.assertEqual(once["status"], "done", once["outcome"])
        labels = once["labels"]
        fix = index(labels, r"vfx-designer: FIX-candidate-r0-vfx-designer")
        self.assertGreater(fix, index(labels, LIVE_OPS))
        self.assertGreater(index(labels, r"film-director: CAP-candidate-r0-fix"), fix, "recaptured before the next round")
        self.assertGreater(index(labels, r"live-ops-designer: RV-candidate-r1-live-ops-designer"), fix)
        always = run(NAME, cut(stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "vfx-designer"})
        self.assertEqual(always["status"], "needs-decision", always["outcome"])
        self.assertEqual(len([x for x in always["labels"] if x.startswith("vfx-designer: FIX-")]), 2, "other findings: 2 repair rounds")

    # ------------------------------------------------------------------ proof: blocking and value strips before the boards
    def test_strips_and_their_review_come_before_the_boards(self):
        for changes in (dict(stage="proof"), dict(stage="build", size="M")):
            with self.subTest(**changes):
                out = run(NAME, cut(**changes), {"dump": r"P4-boards"})
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                strips = index(labels, r"film-director: P3a-strips$")
                review = index(labels, r"art-director: P3a-value-r1")
                boards = index(labels, r"film-director: P4-boards")
                self.assertTrue(0 <= strips < review < boards, labels)
                self.assertIn("strips/", dump(out, r"P4-boards"), "the strips are the boards' layout input")

    def test_strips_brief_names_the_measure_and_the_value_review_is_the_art_directors(self):
        out = run(NAME, cut(stage="proof"), {"dump": r"P3a-"})
        strips = dump(out, r"film-director: P3a-strips$")
        self.assertIn("look_check.py", strips)
        self.assertIn("value strip", strips)
        self.assertIn("value strip", dump(out, r"art-director: P3a-value-r1"))

    def test_a_blocking_value_note_is_fixed_before_the_boards(self):
        out = run(NAME, cut(stage="proof"), {"blockLabelOnce": r"art-director: P3a-value-r1", "maker": "film-director"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertTrue(index(labels, r"P3a-value-r1") < index(labels, r"P3a-strips-fix-r1") < index(labels, r"P3a-value-r2")
                        < index(labels, r"P4-boards"), labels)
        stuck = run(NAME, cut(stage="proof"), {"blockLabel": r"art-director: P3a-value-", "maker": "film-director"})
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])
        self.assertEqual(index(stuck["labels"], r"P4-boards"), -1, "no boards on an unreviewed value strip")

    # ------------------------------------------------------------------ G1: options, failed options, closed doors
    def test_g1_shows_equal_finish_options_and_records_closed_doors(self):
        out = run(NAME, cut(stage="direction"), {"dump": r"D1-film-director|D3-synthesis"})
        self.assertEqual(out["status"], "done", out["outcome"])
        film = dump(out, r"D1-film-director")
        for text in ("warm-up", "2-3 approaches", "contact sheets", "black-fill", "equal finish"):
            self.assertIn(text, film)
        synth = dump(out, r"D3-synthesis")
        for text in ("why each other option lost", "failed a check", "may return only if", "pictures on disk or rows in a pending prompts file"):
            self.assertIn(text, synth)
        g1 = out["result"]["g1"]
        self.assertIn("failed_options", g1)
        self.assertIn("closed_doors", g1)

    def test_later_briefs_carry_the_closed_doors(self):
        later = run(NAME, cut(stage="build"), {"dump": r"B1-lock|P1-contract"})
        self.assertIn("closed doors", dump(later, r"B1-lock"))
        early = run(NAME, cut(stage="direction"), {"dump": r"D1-"})
        self.assertNotIn("closed doors", dump(early, r"D1-film-director"), "direction opens the doors")

    # ------------------------------------------------------------------ every gate: could-not-check and owner-confirmed lines
    def test_every_gate_result_carries_could_not_check_and_owner_lines(self):
        for stage in STAGES:
            with self.subTest(stage=stage):
                out = run(NAME, cut(stage=stage), {"set": {"could_not_check": ["no phone"]}})
                self.assertEqual(out["status"], "done", out["outcome"])
                result = out["result"]
                self.assertTrue(any(x["line"] == "no phone" for x in result["could_not_check"]))
                lines = " ".join(result["owner_confirmed"])
                for text in ("normal speed", "key event alone", "full mix", "phone speaker", "headphones"):
                    self.assertIn(text, lines)

    # ------------------------------------------------------------------ review order and the marker list
    def test_film_review_checks_the_read_lines_on_the_captures(self):
        out = run(NAME, cut(stage="build"), {"dump": r"film-director: RV-candidate-r0-film-director|B3-polish"})
        brief = dump(out, r"film-director: RV-candidate-r0-film-director")
        for text in ("first-second read", "read order", "value lines"):
            self.assertIn(text, brief)
        self.assertIn("one marker list", dump(out, r"B3-polish"), "animation, VFX and sound meet on the timing list")


    # ------------------------------------------------------------------ J019 lead review: a step that does not finish is never a pass
    def test_an_unfinished_combined_check_in_stops_the_build(self):
        out = run(NAME, cut(stage="build"), {"statusLabel": r"B3-combined-checkin", "status": "failed"})
        self.assertEqual(out["status"], "failed", out["outcome"])
        self.assertEqual(index(out["labels"], r"B3-polish"), -1)


if __name__ == "__main__":
    unittest.main()
