"""Cutscene workflow tests for the J019 recipe rows (G3-P4: recipe rows of b2eeb73, the risks arg), with fake agents (no tokens).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22; revised by J024 test updater ·
claude-opus-5-5 · default · 2026-10-24 (J024 flow: knowledge/jobs/J024-flow-cuts-r2/design.md).
Runs .agents/workflows/jobs/job-cutscene.js under tools/workflows/wf_harness.mjs; skipped when Node is not installed.
Covers: the risks arg (missing, not a list, unknown token: blocked before any agent; proof refused first); the risk `event` live-ops
review after the creative chain on the event captures of the capture-and-scripts run; no strips, boards or animatic (J023-D7): the
shot cameras and the marker list live in the D1 beat sheet, and the value measure runs on the final captures; G1 options with failed
options and closed doors; closed doors carried in later briefs; the could-not-check list and owner-confirmed lines in every gate
result; the film-director's read lines in the review chain; a maker that does not finish stops the build.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

NAME = "job-cutscene.js"
LIVE_OPS = r"live-ops-designer: RV-candidate-r0-live-ops-designer"
SCRIPTS = r"studio-operator: RV-candidate-r0-scripts"   # J024 §4.3: capture and scripts in one run (holds the event capture set)
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"
ROUGH = r"strip|board|animatic|value-r|blocking|polish|check-?in|proto|temp"


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
        # J024: proof asked for risks too → proof is refused first, before any arg check, with the J024 reason.
        out = run(NAME, cut(stage="proof", risks=None))
        self.assertEqual((out["status"], out["agents"]), ("blocked", 0), out["outcome"])
        self.assertIn(NO_PROOF, out["outcome"])
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
                # J024: the separate event-captures run → the event capture set is in the capture-and-scripts brief, only with the token.
                on = run(NAME, cut(stage=stage, risks=["event"]), {"dump": r"live-ops-designer: RV-|studio-operator: RV-.*-scripts"})
                off = run(NAME, cut(stage=stage, risks=[]), {"dump": r"studio-operator: RV-.*-scripts"})
                for out in (on, off):
                    self.assertEqual(out["violation"], "")
                    self.assertEqual(out["status"], "done", out["outcome"])
                live_ops = r"live-ops-designer: RV-.*-live-ops-designer"
                self.assertGreaterEqual(index(on["labels"], live_ops), 0)
                self.assertEqual(index(off["labels"], live_ops), -1)
                self.assertEqual(index(on["labels"], r"event-captures"), -1, "J024 LD2: no separate capture run")
                self.assertIn("event-review.md §2", dump(on, r"studio-operator: RV-.*-scripts"))
                self.assertIn("event/", dump(on, r"studio-operator: RV-.*-scripts"))
                self.assertNotIn("event-review.md", dump(off, r"studio-operator: RV-.*-scripts"), "only the event captures need the token")
                brief = dump(on, r"live-ops-designer: RV-")
                for text in ("E-01 to E-19", "event-review.md §3", "model: opus", "effort: medium", "event/"):
                    self.assertIn(text, brief)
                # J024: `performance` is a new universal token, so its skipped line stays unless risks names it.
                self.assertFalse([x for x in on["result"]["skipped_slots"] if "live-ops" in x], on["result"]["skipped_slots"])
                self.assertTrue([x for x in off["result"]["skipped_slots"] if "live-ops" in x], "a slot skipped for no risk is a line, not a silent gap")

    def test_event_review_runs_after_the_creative_chain_on_its_captures(self):
        # J024: event captures in their own run after the chain → taken in the capture-and-scripts run before every review; the
        # live-ops review still starts after every other round-0 review ends (the sound-designer no longer reviews, design §4.4;
        # newLook and risk performance switch on the art-director and performance-engineer to keep them in the order).
        out = run(NAME, cut(stage="build", risks=["event", "performance"], newLook=True), {"timeline": True})
        self.assertEqual(out["violation"], "")
        review = span(out, LIVE_OPS)
        caps = span(out, SCRIPTS)
        for creative in (r"film-director: RV-candidate-r0-film-director", r"art-director: RV-candidate-r0-art-director",
                         r"qa-lead: RV-candidate-r0-qa-lead", r"reviewer: RV-candidate-r0-reviewer",
                         r"performance-engineer: RV-candidate-r0-performance-engineer"):
            with self.subTest(after=creative):
                self.assertGreaterEqual(span(out, creative)["start"], caps["end"])
                self.assertGreaterEqual(review["start"], span(out, creative)["end"])
        self.assertGreaterEqual(review["start"], caps["end"], "the review judges the event captures")
        self.assertEqual(index(out["labels"], r"sound-designer: RV-"), -1)

    def test_event_findings_route_to_makers_inside_the_round_limits(self):
        once = run(NAME, cut(stage="build", risks=["event"]), {"blockLabelOnce": LIVE_OPS, "maker": "vfx-designer"})
        self.assertEqual(once["status"], "done", once["outcome"])
        labels = once["labels"]
        fix = index(labels, r"vfx-designer: FIX-candidate-r0-vfx-designer")
        self.assertGreater(fix, index(labels, LIVE_OPS))
        # J024: CAP-candidate-r0-fix → the round-1 capture-and-scripts run recaptures before the next review.
        self.assertGreater(index(labels, r"studio-operator: RV-candidate-r1-scripts"), fix, "recaptured before the next round (by the studio-operator)")
        self.assertGreater(index(labels, r"live-ops-designer: RV-candidate-r1-live-ops-designer"), fix)
        always = run(NAME, cut(stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "vfx-designer"})
        self.assertEqual(always["status"], "needs-decision", always["outcome"])
        self.assertEqual(len([x for x in always["labels"] if x.startswith("vfx-designer: FIX-")]), 2, "other findings: 2 repair rounds")

    # ------------------------------------------------------------------ no strips or boards: cameras and markers in the D1 beat sheet
    def test_strips_and_their_review_come_before_the_boards(self):
        # J024: strips → value review → boards (proof) → removed on purpose (J023-D7, design §2): no proof stage and no strip, board
        # or animatic step in any stage; the layout input the boards took is now every shot's camera in the D1 beat sheet.
        self.assertIn(NO_PROOF, run(NAME, cut(stage="proof"))["outcome"])
        for stage in STAGES:
            for size in ("L", "M"):
                with self.subTest(stage=stage, size=size):
                    out = run(NAME, cut(stage=stage, size=size))
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertEqual([x for x in out["labels"] if re.search(ROUGH, x, re.I)], [], out["labels"])
        d1 = dump(run(NAME, cut(stage="direction"), {"dump": r"film-director: D1-plan"}), r"film-director: D1-plan")
        self.assertIn("No strips, boards or animatic", d1)
        self.assertIn("every shot's camera (size, angle, FOV, move)", d1)

    def test_strips_brief_names_the_measure_and_the_value_review_is_the_art_directors(self):
        # J024: look_check.py value strips (film-director) + art-director value review → look_check.py value runs on the key stills in
        # the capture-and-scripts run, the film-director measures key frames itself, and the art-director reviews with newLook.
        out = run(NAME, cut(stage="build", newLook=True), {"dump": r"RV-candidate-r0-(scripts|film-director|art-director)"})
        self.assertIn("look_check.py value", dump(out, SCRIPTS))
        self.assertIn("visual_flags", dump(out, SCRIPTS))
        self.assertIn("look_check.py", dump(out, r"film-director: RV-candidate-r0-film-director"))
        self.assertGreaterEqual(index(out["labels"], r"art-director: RV-candidate-r0-art-director"), 0)

    def test_a_blocking_value_note_is_fixed_before_the_boards(self):
        # J024: a blocking value note is fixed before the boards → a blocking value number from the capture-and-scripts run goes to its
        # maker, the candidate is re-measured before review round 1, and the other reviews wait; a number that never clears is needs-decision.
        out = run(NAME, cut(stage="build"), {"blockLabelOnce": SCRIPTS, "maker": "film-director"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertTrue(index(labels, SCRIPTS) < index(labels, r"film-director: FIX-candidate-r0-film-director")
                        < index(labels, r"studio-operator: RV-candidate-r1-scripts") < index(labels, r"film-director: RV-candidate-r1-film-director"), labels)
        self.assertEqual(index(labels, r"film-director: RV-candidate-r0-film-director"), -1, "no review on an unmeasured candidate")
        stuck = run(NAME, cut(stage="build"), {"blockLabel": r"studio-operator: RV-candidate-r", "maker": "film-director"})
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])
        self.assertEqual(index(stuck["labels"], r"film-director: RV-"), -1, "no creative review on a failing value number")

    # ------------------------------------------------------------------ G1: options, failed options, closed doors
    def test_g1_shows_equal_finish_options_and_records_closed_doors(self):
        # J024: D1-film-director proposal + D3-synthesis → D1-plan (options with prompt rows) + M1-merge (direction.md, G1 rows).
        out = run(NAME, cut(stage="direction"), {"dump": r"D1-plan|M1-merge"})
        self.assertEqual(out["status"], "done", out["outcome"])
        film = dump(out, r"film-director: D1-plan")
        for text in ("2-3 options", "equal finish", "image prompt rows", "pictures on disk or rows in the prompts file"):
            self.assertIn(text, film)
        with self.subTest("option method in the D1 brief (suspected script defect: the J023 D1 brief named it, J024 dropped it)"):
            for text in ("warm-up", "contact sheets", "black-fill"):
                self.assertIn(text, film)
        merge = dump(out, r"film-director: M1-merge")
        for text in ("why it lost", "may return only if", "could_not_check"):
            self.assertIn(text, merge)
        g1 = out["result"]["g1"]
        for key in ("options", "recommended", "failed_options", "closed_doors", "open_conflicts"):
            self.assertIn(key, g1)
        self.assertIn("build_args", out["result"])

    def test_later_briefs_carry_the_closed_doors(self):
        # J024: architect B1-player-contract (build) → removed (the architect writes it in N1); every build and repair brief carries them.
        for stage in ("build", "repair"):
            later = run(NAME, cut(stage=stage), {"dump": r".", "affected": ["vfx-designer"]})
            for d in later["dumps"]:
                with self.subTest(stage=stage, label=d["label"]):
                    self.assertIn("closed doors", d["prompt"])
        early = run(NAME, cut(stage="direction"), {"dump": r"D1-"})
        self.assertNotIn("closed doors", dump(early, r"film-director: D1-plan"), "direction opens the doors")

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
                # J024: the feel line watched an animatic at G2 → the owner watches the Studio build at G3 (no animatic, no G2).
                self.assertIn("no animatic and no G2", lines)

    # ------------------------------------------------------------------ review order and the marker list
    def test_film_review_checks_the_read_lines_on_the_captures(self):
        # J024: "value lines" on the captures and B3-polish → the film-director measures key frames itself (look_check.py: first-second
        # read, read order, the J015 near-black shot) and checks sound sync from cue_log; the one marker list is in B1-animator.
        out = run(NAME, cut(stage="build"), {"dump": r"film-director: RV-candidate-r0-film-director|animator: B1-animator"})
        brief = dump(out, r"film-director: RV-candidate-r0-film-director")
        for text in ("first-second read", "read order", "look_check.py", "near-black", "cue_log", "marker list"):
            self.assertIn(text, brief)
        self.assertIn("one marker list", dump(out, r"animator: B1-animator"), "animation, VFX and sound meet on the timing list")


    # ------------------------------------------------------------------ J019 lead review: a step that does not finish is never a pass
    def test_an_unfinished_combined_check_in_stops_the_build(self):
        # J024: B3 combined check-in → removed (one run per craft); a maker that does not finish (or dies) still stops the build before
        # anything that builds on it, and nothing is reviewed.
        for label, later in ((r"animator: B1-animator", r"vfx-designer: B3-vfx|sound-designer: B4-sound"),
                             (r"vfx-designer: B3-vfx", r"sound-designer: B4-sound")):
            for scen in ({"statusLabel": label, "status": "failed"}, {"nullLabel": label}):
                with self.subTest(label=label, scenario=list(scen)[0]):
                    out = run(NAME, cut(stage="build"), scen)
                    self.assertEqual(out["status"], "failed", out["outcome"])
                    self.assertEqual(index(out["labels"], later), -1)
                    self.assertEqual(index(out["labels"], r": RV-"), -1)


if __name__ == "__main__":
    unittest.main()
