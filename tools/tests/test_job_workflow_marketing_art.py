"""Control-flow tests for the marketing art job workflow (.agents/workflows/jobs/job-marketing-art.js), recipe rows of b2eeb73.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg).
Uses the helpers of test_job_workflows (fake agents under tools/workflows/wf_harness.mjs, no tokens); skipped when Node is not installed.
Checks: the `risks` arg is required and accepts only `event`; `event` adds the live-ops-designer review after the creative reviews
in build and repair; the animator's hero pose runs only when the hero is a character; the silhouette and 3-value study, then the
light set-ups, run before the render; colour comes between render and polish; G1 and G3 carry the could-not-check list; the roughs
not picked become closed doors.
"""

from __future__ import annotations

import unittest

try:
    from tools.tests.test_job_workflows import NODE, full, index, run
except ImportError:   # unittest discovery with -t tools/tests (tools/verify.py) imports the sibling module by its bare name
    from test_job_workflows import NODE, full, index, run

NAME = "job-marketing-art.js"


def args(**changes) -> dict:
    return full(NAME, **changes)


@unittest.skipIf(NODE is None, "Node.js not installed")
class MarketingArtWorkflowTests(unittest.TestCase):
    # ------------------------------------------------------------------ risks arg (README args table)
    def test_risks_missing_or_not_a_list_is_blocked_before_any_agent(self):
        for stage in ("direction", "proof", "build", "repair"):
            for bad in (None, "event"):
                with self.subTest(stage=stage, risks=bad):
                    out = run(NAME, args(stage=stage, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])

    def test_unknown_risk_token_is_blocked_and_named(self):
        out = run(NAME, args(stage="build", risks=["event", "money"]))
        self.assertEqual(out["status"], "blocked")
        self.assertEqual(out["agents"], 0)
        self.assertIn('"money"', out["outcome"])
        self.assertTrue(run(NAME, args(stage="build", risks=[]))["status"] == "done")

    # ------------------------------------------------------------------ risk event: live-ops review before G3
    def test_event_adds_live_ops_review_after_the_creative_reviews(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                scenario = {"affected": ["marketing"], "dump": r"live-ops-designer: RV-"}
                withe = run(NAME, args(stage=stage, risks=["event"]), scenario)
                self.assertEqual(withe["status"], "done", withe["outcome"])
                labels = withe["labels"]
                live = index(labels, r"live-ops-designer: RV-(candidate|repair)-r0-")
                self.assertGreater(live, index(labels, r"game-designer: RV-(candidate|repair)-r0-"))
                self.assertGreater(index(labels, r"game-designer: RV-(candidate|repair)-r0-"), index(labels, r"art-director: RV-(candidate|repair)-r0-"))
                self.assertLess(live, index(labels, r"B6-package"), "the live-ops review runs before the stage returns for G3")
                brief = withe["dumps"][0]["prompt"]
                self.assertIn("effort: medium", brief)
                self.assertIn("event-review.md §3", brief)
                without = run(NAME, args(stage=stage, risks=[]), {"affected": ["marketing"]})
                self.assertEqual(without["status"], "done", without["outcome"])
                self.assertEqual(index(without["labels"], r"live-ops-designer"), -1)

    def test_event_review_is_not_in_the_green_light_review(self):
        out = run(NAME, args(stage="build", size="M", risks=["event"]))
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"live-ops-designer: RV-greenlight"), -1)
        self.assertGreaterEqual(index(out["labels"], r"live-ops-designer: RV-candidate-r0"), 0)

    def test_event_findings_go_to_the_makers_inside_the_round_limit(self):
        out = run(NAME, args(stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "marketing"})
        self.assertEqual(out["status"], "needs-decision")
        self.assertGreaterEqual(index(out["labels"], r"marketing: FIX-candidate-r0-marketing"), 0)
        self.assertEqual(index(out["labels"], r"RV-candidate-r3"), -1, "at most 2 repair rounds")

    # ------------------------------------------------------------------ direction: animator consult and G1 contents
    def test_animator_pose_runs_only_when_the_hero_is_a_character(self):
        hero = run(NAME, args(stage="direction"), {"set": {"hero_is_character": True}, "dump": r"D3-direction"})
        self.assertEqual(hero["status"], "done", hero["outcome"])
        pose = index(hero["labels"], r"animator: D2-hero-pose")
        self.assertGreaterEqual(pose, 0)
        self.assertGreater(pose, index(hero["labels"], r"marketing: D1-"), "the pose follows the proposal that names the hero")
        self.assertLess(pose, index(hero["labels"], r"D3-direction"))
        self.assertIn("J099-test/pose/", hero["dumps"][0]["prompt"], "the roughs read the pose")
        plain = run(NAME, args(stage="direction"))
        self.assertEqual(plain["status"], "done", plain["outcome"])
        self.assertEqual(index(plain["labels"], r"animator"), -1)

    def test_dead_animator_pose_fails_the_direction_stage(self):
        out = run(NAME, args(stage="direction"), {"set": {"hero_is_character": True}, "nullLabel": r"D2-hero-pose"})
        self.assertEqual(out["status"], "failed")
        self.assertEqual(index(out["labels"], r"D3-direction"), -1)

    def test_g1_shows_warm_up_failed_roughs_and_could_not_check(self):
        out = run(NAME, args(stage="direction"), {"dump": r"D3-direction"})
        self.assertEqual(out["status"], "done", out["outcome"])
        for key in ("warm_up", "roughs", "failed_roughs", "could_not_check"):
            self.assertIn(key, out["result"]["g1"])
        brief = out["dumps"][0]["prompt"]
        for text in ("labelled warm-up", "different hook", "equal finish", "colour, grey and black-fill", "sell list",
                     "may return only if", "failed_roughs", "highest image quality"):
            self.assertIn(text, brief)

    # ------------------------------------------------------------------ proof and production order
    def test_value_study_and_light_setups_run_before_the_render(self):
        out = run(NAME, args(stage="build", size="M"))
        self.assertEqual(out["status"], "done", out["outcome"])
        order = [r"P1-value", r"P2-light", r"RV-greenlight-r0", r"B1-render", r"B1-colour", r"B2-polish", r"B3-layered", r"B4-crops",
                 r"RV-candidate-r0-scripts", r"B6-package"]
        at = [index(out["labels"], p) for p in order]
        self.assertNotIn(-1, at, list(zip(order, at)))
        self.assertEqual(at, sorted(at), list(zip(order, at)))
        proof = run(NAME, args(stage="proof"))
        self.assertEqual(proof["status"], "done", proof["outcome"])
        self.assertLess(index(proof["labels"], r"P1-value"), index(proof["labels"], r"P2-light"))
        self.assertEqual(index(proof["labels"], r"B1-render"), -1)

    def test_pending_light_setups_stop_the_proof(self):
        out = run(NAME, args(stage="proof"), {"images": "pending"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertGreaterEqual(index(out["labels"], r"P2-light"), 0)
        self.assertEqual(index(out["labels"], r"RV-greenlight"), -1, "nobody reviews unapproved light set-ups")

    def test_roughs_not_picked_are_closed_doors(self):
        out = run(NAME, args(stage="build", size="M"), {"dump": r"P1-value|P2-light|B1-render"})
        briefs = {d["label"].split(": ")[1]: d["prompt"] for d in out["dumps"]}
        self.assertIn("may return only if", briefs["P1-value"])
        for step in ("P1-value", "P2-light", "B1-render"):
            with self.subTest(step=step):
                self.assertIn("closed doors in campaign.md", briefs[step])

    def test_layered_file_has_effects_and_light_layers(self):
        out = run(NAME, args(stage="build"), {"dump": r"B3-layered"})
        self.assertIn("effects and light layers", out["dumps"][0]["prompt"])

    def test_g3_result_carries_could_not_check(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = run(NAME, args(stage=stage), {"affected": ["marketing"]})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertIn("could_not_check", out["result"])


if __name__ == "__main__":
    unittest.main()
