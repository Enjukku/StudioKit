"""Control-flow tests for the marketing art job workflow (.agents/workflows/jobs/job-marketing-art.js), recipe rows of b2eeb73.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg);
revised by J024 test updater · claude-opus-5-5 · default · 2026-10-24 (J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md: no proof,
no roughs or warm-up, the final piece once, the art-director only on launch or visual_flags).
Uses the helpers of test_job_workflows (fake agents under tools/workflows/wf_harness.mjs, no tokens); skipped when Node is not installed.
Checks: the `risks` arg is required and accepts only `event` and `performance`; `event` adds the live-ops-designer review after the
job lead's integrated review in build and repair; the animator's hero pose (an N1 needs table) runs only when the hero is a character;
render, colour, polish, layers and crops run in that order inside the one final-piece run; G1 and G3 carry the could-not-check list;
the options not picked become closed doors.
"""

from __future__ import annotations

import re
import unittest

try:
    from tools.tests.test_job_workflows import NODE, full, index, run
except ImportError:   # unittest discovery with -t tools/tests (tools/verify.py) imports the sibling module by its bare name
    from test_job_workflows import NODE, full, index, run

NAME = "job-marketing-art.js"
HERO = {"set": {"hero_is_character": True}}


def args(**changes) -> dict:
    return full(NAME, **changes)


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class MarketingArtWorkflowTests(unittest.TestCase):
    # ------------------------------------------------------------------ risks arg (README args table)
    def test_risks_missing_or_not_a_list_is_blocked_before_any_agent(self):
        # J024: `stage: "proof"` is refused first, with the no-proof reason, before the risks check.
        for stage in ("direction", "proof", "build", "repair"):
            for bad in (None, "event"):
                with self.subTest(stage=stage, risks=bad):
                    out = run(NAME, args(stage=stage, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("no proof stage (J024)" if stage == "proof" else "risks", out["outcome"])

    def test_unknown_risk_token_is_blocked_and_named(self):
        out = run(NAME, args(stage="build", risks=["event", "money"]))
        self.assertEqual(out["status"], "blocked")
        self.assertEqual(out["agents"], 0)
        self.assertIn('"money"', out["outcome"])
        self.assertTrue(run(NAME, args(stage="build", risks=[]))["status"] == "done")

    # ------------------------------------------------------------------ risk event: live-ops review before G3
    def test_event_adds_live_ops_review_after_the_creative_reviews(self):
        # J024: the game-designer is not a reviewer and the art-director runs only on launch or visual_flags, so the creative order is
        # marketing's integrated review (which writes the owner package; the B6 package step is gone) and, when present, the art-director.
        for stage in ("build", "repair"):
            for extra in ({}, {"launch": True}):
                with self.subTest(stage=stage, extra=extra):
                    scenario = {"affected": ["marketing"], "dump": r"live-ops-designer: RV-"}
                    withe = run(NAME, args(stage=stage, risks=["event"], **extra), scenario)
                    self.assertEqual(withe["status"], "done", withe["outcome"])
                    labels = withe["labels"]
                    live = index(labels, r"live-ops-designer: RV-(candidate|repair)-r0-")
                    self.assertGreater(live, index(labels, r"marketing: RV-(candidate|repair)-r0-marketing"))
                    self.assertGreaterEqual(index(labels, r"marketing: RV-(candidate|repair)-r0-marketing"), 0)
                    if extra:
                        self.assertGreater(live, index(labels, r"art-director: RV-(candidate|repair)-r0-"))
                        self.assertGreaterEqual(index(labels, r"art-director: RV-(candidate|repair)-r0-"), 0)
                    self.assertTrue(withe["result"]["package"], "the live-ops review runs before the stage returns the package for G3")
                    text = withe["dumps"][0]["prompt"]
                    self.assertIn("effort: medium", text)
                    self.assertIn("event-review.md §3", text)
                    without = run(NAME, args(stage=stage, risks=[], **extra), {"affected": ["marketing"]})
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

    # ------------------------------------------------------------------ direction: animator needs table and G1 contents
    def test_animator_pose_runs_only_when_the_hero_is_a_character(self):
        # J024: D2-hero-pose → the animator's N1 needs table (the key pose) when D1 sets hero_is_character; the merge reads it and the
        # final piece poses the hero from it.
        hero = run(NAME, args(stage="direction"), dict(HERO, dump=r"N1-needs-animator|D3-merge"))
        self.assertEqual(hero["status"], "done", hero["outcome"])
        pose = index(hero["labels"], r"^animator: N1-needs-animator$")
        self.assertGreaterEqual(pose, 0)
        self.assertGreater(pose, index(hero["labels"], r"marketing: D1-plan"), "the pose follows the plan that names the hero")
        self.assertLess(pose, index(hero["labels"], r"D3-merge"))
        self.assertIn("J099-test/pose/", brief(hero, r"N1-needs-animator"))
        self.assertIn("needs/animator.md", brief(hero, r"D3-merge"), "the merge reads the pose table")
        final = run(NAME, args(stage="build"), {"dump": r"B1-final"})
        self.assertIn("J099-test/pose/", brief(final, r"B1-final"), "the final piece reads the pose")
        plain = run(NAME, args(stage="direction"))
        self.assertEqual(plain["status"], "done", plain["outcome"])
        self.assertEqual(index(plain["labels"], r"animator"), -1)

    def test_dead_animator_pose_fails_the_direction_stage(self):
        # J024: D2-hero-pose → N1-needs-animator; a dead table never reaches the merge.
        out = run(NAME, args(stage="direction"), dict(HERO, nullLabel=r"N1-needs-animator"))
        self.assertEqual(out["status"], "failed")
        self.assertEqual(index(out["labels"], r"D3-merge"), -1)

    def test_g1_shows_warm_up_failed_roughs_and_could_not_check(self):
        # J024: warm-up and roughs removed on purpose (§2); the D1 plan brings the options (L 2-3 from different hooks at equal finish),
        # failed_options, the crop plan and could_not_check; no warm-up or rough key or label.
        out = run(NAME, args(stage="direction"), {"dump": r"D1-plan"})
        self.assertEqual(out["status"], "done", out["outcome"])
        g1 = out["result"]["g1"]
        for key in ("options", "failed_options", "crop_plan", "could_not_check"):
            self.assertIn(key, g1)
        for key in ("warm_up", "roughs", "failed_roughs"):
            self.assertNotIn(key, g1)
        self.assertEqual(index(out["labels"], r"warm|rough"), -1)
        text = brief(out, r"D1-plan")
        for phrase in ("2-3 options", "different hook", "equal finish", "sell list", "may return only if", "failed_options", "highest image quality"):
            self.assertIn(phrase, text)
        medium = run(NAME, args(stage="direction", size="M"), {"dump": r"D1-plan"})
        self.assertIn("one direction inside the art bible", brief(medium, r"D1-plan"))

    # ------------------------------------------------------------------ the final piece once
    def test_value_study_and_light_setups_run_before_the_render(self):
        # J024 (value study, light set-ups and green light removed on purpose, §2): no such step in any stage or size; the old step order
        # render → colour → polish → layered file → crops holds inside the one B1-final run, then the scripts, then the review and package.
        self.assertEqual(run(NAME, args(stage="proof"))["status"], "blocked")
        order = [r"B1-final", r"RV-candidate-r0-scripts", r"marketing: RV-candidate-r0-marketing"]
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = run(NAME, args(stage="build", size=size), {"dump": r"B1-final"})
                self.assertEqual(out["status"], "done", out["outcome"])
                at = [index(out["labels"], p) for p in order]
                self.assertNotIn(-1, at, list(zip(order, at)))
                self.assertEqual(at, sorted(at), list(zip(order, at)))
                self.assertEqual(index(out["labels"], r"value|light|greenlight|B1-render|B1-colour|B2-polish|B3-layered|B4-crops"), -1)
                text = brief(out, r"B1-final")
                steps = ("render the option the owner chose at G1", "colour on the approved values", "detail and polish last", "one layered source file", "then every crop")
                at = [text.find(s) for s in steps]
                self.assertNotIn(-1, at, list(zip(steps, at)))
                self.assertEqual(at, sorted(at), list(zip(steps, at)))
        for stage in ("direction", "repair"):
            with self.subTest(stage=stage):
                self.assertEqual(index(run(NAME, args(stage=stage), {"affected": ["marketing"]})["labels"], r"value|light|greenlight"), -1)

    def test_pending_light_setups_stop_the_proof(self):
        # J024: P2-light is gone; a pending image batch in the final-piece run stops the build: nobody scripts or reviews unapproved art.
        out = run(NAME, args(stage="build"), {"images": "pending"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertGreaterEqual(index(out["labels"], r"B1-final"), 0)
        self.assertEqual(index(out["labels"], r": RV-"), -1, "nobody reviews unapproved art")
        self.assertTrue(out["result"]["images_pending"])

    def test_roughs_not_picked_are_closed_doors(self):
        # J024: P1-value / B1-render → the B1-final run records the options not picked as closed doors first, in L and M.
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = run(NAME, args(stage="build", size=size), {"dump": r"B1-final"})
                text = brief(out, r"B1-final")
                self.assertIn("may return only if", text)
                self.assertIn("closed doors", text)
                self.assertIn("campaign.md", text)
                self.assertLess(text.index("closed doors"), text.index("render the option"), "recorded first")

    def test_layered_file_has_effects_and_light_layers(self):
        # J024: B3-layered → the layered file is made inside B1-final.
        out = run(NAME, args(stage="build"), {"dump": r"B1-final"})
        self.assertIn("effects and light layers", brief(out, r"B1-final"))

    def test_g3_result_carries_could_not_check(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = run(NAME, args(stage=stage), {"affected": ["marketing"]})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertIn("could_not_check", out["result"])

    # ------------------------------------------------------------------ J019 lead review: a review that does not finish is never a pass
    def test_a_review_or_scripts_step_that_does_not_finish_is_not_clean(self):
        # J024: the art-director reviews only on launch (or visual_flags); marketing's integrated review always.
        for label, extra in ((r"live-ops-designer: RV-", {}), (r"RV-candidate-r0-scripts", {}), (r"marketing: RV-", {}), (r"art-director: RV-", {"launch": True})):
            with self.subTest(label=label):
                out = run(NAME, args(stage="build", risks=["event"], **extra), {"statusLabel": label, "status": "blocked"})
                self.assertEqual(out["status"], "blocked", out["outcome"])

    def test_a_skipped_event_slot_is_a_line_in_the_result(self):
        self.assertEqual(run(NAME, args(stage="build", risks=[]))["result"]["skipped_slots"], ["live-ops event review: risks has no event"])
        self.assertEqual(run(NAME, args(stage="build", risks=["event"]))["result"]["skipped_slots"], [])


if __name__ == "__main__":
    unittest.main()
