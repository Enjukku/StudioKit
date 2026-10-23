"""Effect workflow tests (.agents/workflows/jobs/job-effect.js) for the recipe rows of b2eeb73 and the risks arg, with fake agents.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: the effect workflow runs the
recipe rows of orchestration/references/job-types.md §6 and the cross-type rules). Uses the helpers of test_job_workflows;
skipped when Node.js is not installed.
"""

from __future__ import annotations

import unittest

from tools.tests.test_job_workflows import NODE, full, index, run, span

NAME = "job-effect.js"
TRUTH = ("server-result", "danger-area", "paid-random", "frequent-effect")
PF = {"server-result": "PF-02", "danger-area": "PF-04", "paid-random": "PF-06", "frequent-effect": "PF-10"}


def fx(stage: str, scenario: dict | None = None, **changes) -> dict:
    return run(NAME, full(NAME, stage=stage, **changes), scenario)


def brief(out: dict, pattern: str) -> str:
    import re
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class EffectWorkflowTests(unittest.TestCase):
    # ------------------------------------------------------------------ the risks arg (README args table)
    def test_risks_missing_or_not_a_list_is_blocked(self):
        for stage in ("direction", "proof", "build", "repair"):
            for bad in (None, "danger-area", {"danger-area": True}):
                with self.subTest(stage=stage, risks=bad):
                    out = fx(stage, risks=bad)
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])

    def test_unknown_risk_token_is_blocked(self):
        for token in ("bogus", "new-enemy", "shop-screen"):
            with self.subTest(token=token):
                out = fx("build", risks=["danger-area", token])
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    def test_every_accepted_token_runs_clean(self):
        for stage in ("direction", "proof", "build", "repair"):
            with self.subTest(stage=stage):
                out = fx(stage, risks=list(TRUTH) + ["event"])
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertLessEqual(out["maxConcurrent"], 5)

    # ------------------------------------------------------------------ qa-lead protected acceptance (risk-gated)
    def test_qa_acceptance_runs_with_each_truth_risk_and_not_without(self):
        for stage in ("build", "repair"):
            for risk in TRUTH:
                with self.subTest(stage=stage, risk=risk):
                    out = fx(stage, {"dump": r"qa-lead: RV-"}, risks=[risk])
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertGreaterEqual(index(out["labels"], r"^qa-lead: RV-(candidate|repair)-r0-qa-lead"), 0)
                    self.assertIn(PF[risk], brief(out, r"qa-lead: RV-"))
                    self.assertEqual(out["result"]["skipped_slots"], ["live-ops event review: risks has no event"])
            for risks in ([], ["event"]):
                with self.subTest(stage=stage, risks=risks):
                    out = fx(stage, risks=risks)
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertEqual(index(out["labels"], r"^qa-lead:"), -1)
                    self.assertIn("qa-lead protected acceptance: risks names no gameplay-truth risk", out["result"]["skipped_slots"])

    def test_qa_acceptance_is_not_run_on_the_blocking_pass(self):
        out = fx("build", size="M", risks=["danger-area"])
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"qa-lead: RV-proof"), -1)
        self.assertGreaterEqual(index(out["labels"], r"qa-lead: RV-candidate-r0"), 0)

    def test_qa_failure_routes_to_its_maker_inside_the_round_limit(self):
        out = fx("build", {"blockLabelOnce": r"qa-lead: RV-candidate-r0", "maker": "feature-builder"}, risks=["frequent-effect"])
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertLess(index(labels, r"qa-lead: RV-candidate-r0"), index(labels, r"feature-builder: W-candidate-r0-sync"))
        self.assertGreaterEqual(index(labels, r"qa-lead: RV-candidate-r1"), 0)

    # ------------------------------------------------------------------ live-ops event review (risk: event)
    def test_event_adds_the_live_ops_review_after_the_creative_reviews(self):
        for stage, label in (("build", "candidate"), ("repair", "repair")):
            with self.subTest(stage=stage):
                out = fx(stage, {"dump": r"live-ops-designer: RV-", "affected": ["vfx-designer"]}, risks=["event"])
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                live = index(labels, rf"^live-ops-designer: RV-{label}-r0-live-ops-designer")
                self.assertGreaterEqual(live, 0)
                for creative in ("game-designer", "art-director", "sound-designer"):
                    self.assertLess(index(labels, rf"^{creative}: RV-{label}-r0-{creative}"), live)
                text = brief(out, r"live-ops-designer: RV-")
                self.assertIn("effort: medium", text)
                self.assertIn("E-01 to E-19", text)
                self.assertIn("event-review.md", text)
                self.assertNotIn("live-ops event review: risks has no event", out["result"]["skipped_slots"])

    def test_event_review_is_absent_without_event_and_on_the_proof(self):
        self.assertEqual(index(fx("build", risks=[])["labels"], r"^live-ops-designer:"), -1)
        medium = fx("build", size="M", risks=["event"])
        self.assertEqual(index(medium["labels"], r"live-ops-designer: RV-proof"), -1)
        self.assertGreaterEqual(index(medium["labels"], r"live-ops-designer: RV-candidate-r0"), 0)
        self.assertEqual(index(fx("proof", risks=["event"])["labels"], r"^live-ops-designer:"), -1)

    def test_event_findings_route_to_makers_inside_the_round_limit(self):
        once = fx("build", {"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "vfx-designer"}, risks=["event"])
        self.assertEqual(once["status"], "done", once["outcome"])
        self.assertGreaterEqual(index(once["labels"], r"vfx-designer: FIX-candidate-r0-vfx-designer"), 0)
        always = fx("build", {"blockLabel": r"live-ops-designer: RV-", "maker": "vfx-designer"}, risks=["event"])
        self.assertEqual(always["status"], "needs-decision", always["outcome"])
        self.assertEqual(index(always["labels"], r"RV-candidate-r3-"), -1, "no round beyond the limit")

    def test_event_capture_set_is_requested(self):
        out = fx("build", {"dump": r"CAP-candidate-r0"}, risks=["event"])
        self.assertIn("event-review.md §2", brief(out, r"CAP-candidate-r0"))

    # ------------------------------------------------------------------ direction: the art-director's place
    def test_art_director_consults_when_the_effect_extends_the_art_bible(self):
        for key in ("adds_colour_role", "adds_shape_code"):
            with self.subTest(key=key):
                out = fx("direction", {"set": {key: True}}, newLook=False)
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                consult = index(labels, r"^art-director: D2-consult-art-director")
                self.assertGreaterEqual(consult, 0)
                self.assertLess(consult, index(labels, r"vfx-designer: D3-synthesis"))
                self.assertGreater(index(labels, r"^art-director: D3-sign-art-director"), index(labels, r"vfx-designer: D3-synthesis"))
                self.assertEqual(index(labels, r"^art-director: D1-"), -1, "a consult is not an independent proposal")
        plain = fx("direction", newLook=False)
        self.assertEqual(index(plain["labels"], r"^art-director:"), -1)
        new_look = fx("direction", {"set": {"adds_colour_role": True}}, newLook=True)
        self.assertGreaterEqual(index(new_look["labels"], r"^art-director: D1-art-director"), 0)
        self.assertEqual(index(new_look["labels"], r"D2-consult"), -1)

    # ------------------------------------------------------------------ cooperation and production order
    def test_blocking_markers_reach_vfx_and_sound_before_either_builds(self):
        out = fx("proof", {"dump": r"P1-timing|E-r1-vfx-designer|E-r1-sound-designer|P3-first-spec|P3-temp-sound"}, animated=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        markers = index(labels, r"^animator: P1-timing")
        self.assertGreaterEqual(markers, 0)
        for later in (r"vfx-designer: E-r1-vfx-designer", r"sound-designer: E-r1-sound-designer", r"vfx-designer: P3-first-spec", r"sound-designer: P3-temp-sound"):
            self.assertLess(markers, index(labels, later), later)
            self.assertIn("timing-list.md", brief(out, later))
        self.assertIn("re-sent in this same hand-back", brief(out, r"P1-timing"))
        still = fx("proof", {"dump": r"P3-temp-sound"}, animated=False)
        self.assertEqual(index(still["labels"], r"^animator:"), -1)
        self.assertNotIn("timing-list.md", brief(still, r"P3-temp-sound"))

    def test_retime_is_resent_in_the_same_handback(self):
        out = fx("build", {"dump": r"animator: B1-polish|animator: FIX-", "blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "animator"}, animated=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        for pat in (r"animator: B1-polish", r"animator: FIX-"):
            self.assertIn("re-sent in this same hand-back", brief(out, pat))

    def test_final_sound_comes_after_the_timing_lock_and_the_vfx_build(self):
        for animated in (True, False):
            with self.subTest(animated=animated):
                out = fx("build", {"timeline": True, "dump": r"B2-cues"}, animated=animated)
                self.assertEqual(out["status"], "done", out["outcome"])
                cues = span(out, r"sound-designer: B2-cues")
                self.assertGreater(cues["start"], span(out, r"vfx-designer: B1-lock")["end"])
                self.assertGreater(cues["start"], span(out, r"vfx-designer: B2-spec")["end"])
                if animated:
                    self.assertGreater(cues["start"], span(out, r"animator: B1-polish")["end"])
                    self.assertIn("timing-list.md@rev", brief(out, r"B2-cues"))

    def test_art_blocking_check_comes_before_any_texture_pick(self):
        out = fx("build", {"dump": r"art-director: RV-(proof|candidate)-r0|B2-spec|P3-first-spec"}, size="M")
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        check = index(labels, r"^art-director: RV-proof-r0-art-director")
        self.assertGreaterEqual(check, 0)
        self.assertLess(check, index(labels, r"vfx-designer: B2-spec"))
        self.assertLess(check, index(labels, r"art-director: RV-candidate-r0-art-director"))
        blocking = brief(out, r"art-director: RV-proof-r0")
        self.assertIn("blocking check", blocking)
        self.assertIn("§I3", blocking)
        self.assertIn("No texture pick", brief(out, r"P3-first-spec"))
        self.assertIn("coloured build, after your blocking check", brief(out, r"art-director: RV-candidate-r0"))

    def test_blocking_pass_capture_has_at_most_four_key_stills(self):
        out = fx("proof", {"dump": r"CAP-proof-r0"})
        text = brief(out, r"CAP-proof-r0")
        self.assertIn("at most 4 key stills", text)
        self.assertIn("build, peak, result, tail", text)
        self.assertIn("temporary sound's cue times", text)
        self.assertIn("first playable", " ".join(out["result"]["owner_confirmed"]))

    # ------------------------------------------------------------------ integrator: test hooks before any capture
    def test_wiring_delivers_the_test_hooks_before_the_first_capture(self):
        for stage, wire, cap in (("proof", r"W-proof", r"CAP-proof-r0"), ("build", r"W-candidate$", r"CAP-candidate-r0")):
            with self.subTest(stage=stage):
                out = fx(stage, {"dump": wire})
                self.assertLess(index(out["labels"], wire), index(out["labels"], cap))
                text = brief(out, wire)
                for hook in ("`Rate`", "`Reject`", "`DebugShape`", "presentation.md §9", "player-facing.md §3"):
                    self.assertIn(hook, text)

    # ------------------------------------------------------------------ review order: scripts, named captures
    def test_scripts_run_the_flash_counter(self):
        out = fx("build", {"dump": r"RV-candidate-r0-scripts"})
        self.assertIn("tools/vfx/flash_count.py", brief(out, r"RV-candidate-r0-scripts"))
        self.assertEqual(index(out["labels"], r"RV-candidate-r0-scripts"), index(out["labels"], r": RV-candidate-r0-"), "scripts run first")

    def test_named_captures_follow_the_risks(self):
        cases = {(): (), ("danger-area",): ("hit-shape overlay",), ("server-result",): ("rejected request",),
                 ("danger-area", "server-result"): ("hit-shape overlay", "rejected request")}
        for risks, wanted in cases.items():
            with self.subTest(risks=risks):
                out = fx("build", {"dump": r"CAP-candidate-r0|game-designer: RV-candidate-r0"}, risks=list(risks))
                cap = brief(out, r"CAP-candidate-r0")
                judge = brief(out, r"game-designer: RV-candidate-r0")
                self.assertIn("two-client", cap)
                self.assertIn("two-client", judge)
                for name in ("hit-shape overlay", "rejected request"):
                    self.assertEqual(name in cap, name in wanted, name)
                    self.assertEqual(name in judge, name in wanted, name)

    # ------------------------------------------------------------------ cross-type rules
    def test_options_not_picked_become_closed_doors(self):
        out = fx("direction", {"dump": r"D3-synthesis"})
        self.assertIn('"may return only if"', brief(out, r"D3-synthesis"))
        self.assertIn("closed doors", out["outcome"])
        build = fx("build", {"dump": r"B2-spec|P3-first-spec"}, size="M")
        for pat in (r"B2-spec", r"P3-first-spec"):
            self.assertRegex(brief(build, pat), r"avoid: \[[^\]]*may return only if")

    def test_one_marker_list_where_animation_vfx_and_sound_meet(self):
        out = fx("proof", {"dump": r"E-r1-sound-designer"})
        self.assertIn("One marker list", brief(out, r"E-r1-sound-designer"))

    def test_gate_results_carry_could_not_check_and_owner_lines(self):
        unverified = {"set": {"checks": [{"id": "C1", "result": "not verified", "evidence": "no recording"}]}}
        direction = fx("direction", unverified)
        self.assertEqual(direction["status"], "done", direction["outcome"])
        self.assertTrue(direction["result"]["g1"]["could_not_check"])
        build = fx("build", unverified)
        self.assertEqual(build["status"], "done", build["outcome"])
        self.assertTrue(build["result"]["could_not_check"])
        for out in (direction, build):
            lines = " ".join(out["result"]["owner_confirmed"])
            for words in ("normal speed", "key event alone", "full mix", "phone speaker", "headphones"):
                self.assertIn(words, lines)
        self.assertEqual(fx("build")["result"]["could_not_check"], [], "clean checks leave the list empty")


if __name__ == "__main__":
    unittest.main()
