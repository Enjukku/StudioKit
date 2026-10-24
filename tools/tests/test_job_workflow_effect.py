"""Effect workflow tests (.agents/workflows/jobs/job-effect.js) for the recipe rows of b2eeb73 and the risks arg, with fake agents.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: the effect workflow runs the
recipe rows of orchestration/references/job-types.md §6 and the cross-type rules); revised by J024 test updater ·
claude-opus-5-5 · default · 2026-10-24 (J024 flow: knowledge/jobs/J024-flow-cuts-r2/design.md: no proof or blocking pass, one
run per craft, capture and scripts in one studio-operator run, the vfx-designer's integrated review, the qa-lead only with
server-result or paid-random). Uses the helpers of test_job_workflows; skipped when Node.js is not installed.
"""

from __future__ import annotations

import unittest

from tools.tests.test_job_workflows import NODE, full, index, run, span

NAME = "job-effect.js"
TRUTH = ("server-result", "danger-area", "paid-random", "frequent-effect")
PF = {"server-result": "PF-02", "danger-area": "PF-04", "paid-random": "PF-06", "frequent-effect": "PF-10"}
QA = ("server-result", "paid-random")          # J024 §6: the qa-lead reviews only these
MEASURED = ("danger-area", "frequent-effect")  # J024 §6: measured rows in the capture-and-scripts run + game-designer limits in direction
SCRIPTS = r"studio-operator: RV-candidate-r0-scripts"
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"


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
        # J024: proof asked for risks too → proof is refused first, with the J024 reason, before any arg check.
        for bad in (None, "danger-area"):
            out = fx("proof", risks=bad)
            self.assertEqual((out["status"], out["agents"]), ("blocked", 0), out["outcome"])
            self.assertIn(NO_PROOF, out["outcome"])
        for stage in ("direction", "build", "repair"):
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
        # J024: proof stage dropped from the loop (refused, above); the token list adds the universal `performance`.
        for stage in ("direction", "build", "repair"):
            with self.subTest(stage=stage):
                out = fx(stage, risks=list(TRUTH) + ["event", "performance"])
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertLessEqual(out["maxConcurrent"], 5)

    # ------------------------------------------------------------------ qa-lead protected acceptance (risk-gated)
    def test_qa_acceptance_runs_with_each_truth_risk_and_not_without(self):
        # J024: qa-lead for every truth risk → design §6: qa-lead only with server-result or paid-random (its PF row in the brief);
        # danger-area and frequent-effect become measured PF rows in the capture-and-scripts run instead; skipped lines name each slot.
        for stage in ("build", "repair"):
            for risk in TRUTH:
                with self.subTest(stage=stage, risk=risk):
                    out = fx(stage, {"dump": r"qa-lead: RV-|studio-operator: RV-"}, risks=[risk])
                    self.assertEqual(out["status"], "done", out["outcome"])
                    skipped = out["result"]["skipped_slots"]
                    self.assertIn("live-ops event review: risks has no event", skipped)
                    self.assertIn("performance-engineer review: risks has no performance", skipped)
                    if risk in QA:
                        self.assertGreaterEqual(index(out["labels"], r"^qa-lead: RV-(candidate|repair)-r0-qa-lead"), 0)
                        self.assertIn(PF[risk], brief(out, r"qa-lead: RV-"))
                        self.assertEqual(len(skipped), 2, skipped)
                    else:
                        self.assertEqual(index(out["labels"], r"^qa-lead:"), -1)
                        self.assertIn(PF[risk], brief(out, r"studio-operator: RV-"), "the truth row is measured in the scripts run")
            for risks in ([], ["event"]):
                with self.subTest(stage=stage, risks=risks):
                    out = fx(stage, risks=risks)
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertEqual(index(out["labels"], r"^qa-lead:"), -1)
                    self.assertIn("qa-lead protected acceptance: risks names neither server-result nor paid-random", out["result"]["skipped_slots"])

    def test_qa_acceptance_is_not_run_on_the_blocking_pass(self):
        # J024: no qa-lead run on the blocking pass → no blocking pass or proof exists; in M and L the qa-lead runs on the candidate only.
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = fx("build", size=size, risks=["server-result"])
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(index(out["labels"], r"qa-lead: RV-(proof|blocking)|blocking|CAP-proof"), -1)
                self.assertGreaterEqual(index(out["labels"], r"qa-lead: RV-candidate-r0"), 0)

    def test_qa_failure_routes_to_its_maker_inside_the_round_limit(self):
        # J024: risk frequent-effect no longer switches the qa-lead on → server-result does; routing and the round limit are unchanged.
        out = fx("build", {"blockLabelOnce": r"qa-lead: RV-candidate-r0", "maker": "feature-builder"}, risks=["server-result"])
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertLess(index(labels, r"qa-lead: RV-candidate-r0"), index(labels, r"feature-builder: W-candidate-r0-sync"))
        self.assertGreaterEqual(index(labels, r"qa-lead: RV-candidate-r1"), 0)
        always = fx("build", {"blockLabel": r"qa-lead: RV-", "maker": "feature-builder"}, risks=["server-result"])
        self.assertEqual(always["status"], "needs-decision", always["outcome"])
        self.assertEqual(index(always["labels"], r"RV-candidate-r4-"), -1, "code findings: at most 3 repair rounds")

    # ------------------------------------------------------------------ live-ops event review (risk: event)
    def test_event_adds_the_live_ops_review_after_the_creative_reviews(self):
        for stage, label in (("build", "candidate"), ("repair", "repair")):
            with self.subTest(stage=stage):
                out = fx(stage, {"dump": r"live-ops-designer: RV-", "affected": ["vfx-designer"]}, risks=["event"])
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                live = index(labels, rf"^live-ops-designer: RV-{label}-r0-live-ops-designer")
                self.assertGreaterEqual(live, 0)
                # J024: after the game-designer, art-director and sound-designer → after the vfx-designer's integrated review and the
                # reviewer (the removed reviewers never run, design §4.4).
                for creative in ("vfx-designer", "reviewer"):
                    self.assertGreaterEqual(index(labels, rf"^{creative}: RV-{label}-r0-{creative}"), 0, creative)
                    self.assertLess(index(labels, rf"^{creative}: RV-{label}-r0-{creative}"), live)
                self.assertEqual(index(labels, r"^(game-designer|sound-designer): RV-"), -1)
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
        # J024: proof ran no event review → proof is refused before any agent; direction runs none either.
        proof = fx("proof", risks=["event"])
        self.assertEqual((proof["status"], proof["agents"]), ("blocked", 0))
        self.assertEqual(index(fx("direction", risks=["event"])["labels"], r"^live-ops-designer:"), -1)

    def test_event_findings_route_to_makers_inside_the_round_limit(self):
        once = fx("build", {"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "vfx-designer"}, risks=["event"])
        self.assertEqual(once["status"], "done", once["outcome"])
        self.assertGreaterEqual(index(once["labels"], r"vfx-designer: FIX-candidate-r0-vfx-designer"), 0)
        always = fx("build", {"blockLabel": r"live-ops-designer: RV-", "maker": "vfx-designer"}, risks=["event"])
        self.assertEqual(always["status"], "needs-decision", always["outcome"])
        self.assertEqual(index(always["labels"], r"RV-candidate-r3-"), -1, "no round beyond the limit")

    def test_event_capture_set_is_requested(self):
        # J024: CAP-candidate-r0 → the event capture rows are in the capture-and-scripts brief, only with the token.
        out = fx("build", {"dump": SCRIPTS}, risks=["event"])
        self.assertIn("event-review.md §2", brief(out, SCRIPTS))
        self.assertNotIn("event-review.md §2", brief(fx("build", {"dump": SCRIPTS}, risks=[]), SCRIPTS))

    # ------------------------------------------------------------------ direction: the art-director's place
    def test_art_director_consults_when_the_effect_extends_the_art_bible(self):
        # J024: D2 art consult (adds_colour_role / adds_shape_code) → removed on purpose (design §4.4, §6): the art-director writes a
        # limits table in N1 only with newLook and reviews when newLook or visual_flags; an art-bible extension surfaces as a flag.
        for key in ("adds_colour_role", "adds_shape_code"):
            with self.subTest(key=key):
                out = fx("direction", {"set": {key: True}}, newLook=False)
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(index(out["labels"], r"^art-director:"), -1, "no consult run without newLook")
                self.assertEqual(index(out["labels"], r"D2-|D3-sign-"), -1)
        new_look = fx("direction", {"set": {"adds_colour_role": True}}, newLook=True)
        art = index(new_look["labels"], r"^art-director: N1-art-director")
        self.assertGreaterEqual(art, 0)
        self.assertLess(art, index(new_look["labels"], r"vfx-designer: M1-merge"), "the limits table reaches the merge")
        self.assertEqual(index(new_look["labels"], r"D2-consult|art-director: D1-"), -1, "a limits table is not an independent proposal")
        flagged = fx("build", {"set": {"visual_flags": ["peak value 0.98 > 0.92"]}}, newLook=False)
        self.assertGreaterEqual(index(flagged["labels"], r"^art-director: RV-candidate-r0-art-director"), 0)
        self.assertEqual(index(fx("build", newLook=False)["labels"], r"^art-director:"), -1)

    # ------------------------------------------------------------------ cooperation and production order
    def test_blocking_markers_reach_vfx_and_sound_before_either_builds(self):
        # J024: P1 blocking timing list (proof) → the animator's N1 needs table answers the D1 marker list in direction, and in build
        # its final clip and timing list (B1-animator) come before the VFX and sound builds, which read the timing list.
        direction = fx("direction", animated=True)
        self.assertLess(index(direction["labels"], r"vfx-designer: D1-plan"), index(direction["labels"], r"^animator: N1-animator"))
        out = fx("build", {"timeline": True, "dump": r"B1-animator|B2-vfx|B3-sound"}, animated=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        markers = span(out, r"^animator: B1-animator")
        for later in (r"vfx-designer: B2-vfx", r"sound-designer: B3-sound"):
            self.assertLess(markers["end"], span(out, later)["start"], later)
            self.assertIn("timing-list.md", brief(out, later))
        self.assertIn("re-sent in this same hand-back", brief(out, r"B1-animator"))
        still = fx("build", {"dump": r"B3-sound"}, animated=False)
        self.assertEqual(index(still["labels"], r"^animator:"), -1)
        self.assertNotIn("timing-list.md", brief(still, r"B3-sound"))

    def test_retime_is_resent_in_the_same_handback(self):
        # J024: animator B1-polish → B1-animator (one run); the animator's FIX brief keeps the rule (the art-director no longer reviews,
        # so the integrated vfx-designer review routes the finding).
        out = fx("build", {"dump": r"animator: B1-animator|animator: FIX-", "blockLabelOnce": r"vfx-designer: RV-candidate-r0", "maker": "animator"}, animated=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        for pat in (r"animator: B1-animator", r"animator: FIX-"):
            self.assertIn("re-sent in this same hand-back", brief(out, pat))

    def test_final_sound_comes_after_the_timing_lock_and_the_vfx_build(self):
        # J024: B1-lock + B2-spec + B1-polish → no lock step; B1-animator (animated) → B2-vfx (build timeline and envelopes) → B3-sound.
        for animated in (True, False):
            with self.subTest(animated=animated):
                out = fx("build", {"timeline": True, "dump": r"B3-sound"}, animated=animated)
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(index(out["labels"], r"lock|polish|spec|cues"), -1)
                cues = span(out, r"sound-designer: B3-sound")
                self.assertGreater(cues["start"], span(out, r"vfx-designer: B2-vfx")["end"])
                if animated:
                    self.assertGreater(cues["start"], span(out, r"animator: B1-animator")["end"])
                    self.assertIn("timing-list.md@rev", brief(out, r"B3-sound"))

    def test_art_blocking_check_comes_before_any_texture_pick(self):
        # J024: art-director B0 blocking check-in before textures → removed on purpose (no rough passes, design §2): the vfx-designer
        # builds the final spec once (B2-vfx); the art-director reviews the final only with newLook or visual_flags.
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = fx("build", size=size)
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(index(out["labels"], r"B0-|checkin|first-spec|CAP-blocking|^art-director:"), -1, out["labels"])
                self.assertEqual([x for x in out["labels"] if x.startswith("vfx-designer: B")], ["vfx-designer: B2-vfx"])

    def test_blocking_pass_capture_has_at_most_four_key_stills(self):
        # J024: CAP-proof-r0 (blocking pass, 4 key stills, temporary cue times) → no proof capture; one capture-and-scripts run per review
        # round, with the check budget; the first playable is shown at G3.
        self.assertIn(NO_PROOF, fx("proof")["outcome"])
        out = fx("build", {"dump": SCRIPTS})
        caps = [x for x in out["labels"] if x.startswith("studio-operator:")]
        self.assertEqual(caps, ["studio-operator: RV-candidate-r0-scripts"])
        self.assertIn("Check budget (owner J005-D8)", brief(out, SCRIPTS))
        self.assertIn("G3", " ".join(fx("direction")["result"]["owner_confirmed"]))

    # ------------------------------------------------------------------ integrator: test hooks before any capture
    def test_wiring_delivers_the_test_hooks_before_the_first_capture(self):
        # J024: proof W-proof and the CAP- label → the build wiring (W-candidate) delivers the hooks before the capture-and-scripts run;
        # the proof case becomes the repair sync, which keeps the hooks working before the repair capture.
        out = fx("build", {"dump": r"W-candidate$"})
        wire, cap = r"W-candidate$", r"studio-operator: RV-candidate-r0-scripts"
        self.assertGreaterEqual(index(out["labels"], wire), 0)
        self.assertLess(index(out["labels"], wire), index(out["labels"], cap))
        text = brief(out, wire)
        for hook in ("`Rate`", "`Reject`", "`DebugShape`", "presentation.md §9", "player-facing.md §3"):
            self.assertIn(hook, text)
        repair = fx("repair", {"dump": r"W-repair-sync", "affected": ["vfx-designer"]})
        self.assertLess(index(repair["labels"], r"W-repair-sync"), index(repair["labels"], r"studio-operator: RV-repair-r0-scripts"))
        self.assertIn("Keep the test hooks working", brief(repair, r"W-repair-sync"))

    # ------------------------------------------------------------------ review order: scripts, named captures
    def test_scripts_run_the_flash_counter(self):
        out = fx("build", {"dump": r"RV-candidate-r0-scripts"})
        self.assertIn("tools/vfx/flash_count.py", brief(out, r"RV-candidate-r0-scripts"))
        self.assertEqual(index(out["labels"], r"RV-candidate-r0-scripts"), index(out["labels"], r": RV-candidate-r0-"), "scripts run first")

    def test_named_captures_follow_the_risks(self):
        # J024: CAP-candidate-r0 + the game-designer's review → the same named captures in the capture-and-scripts run; the judge is the
        # vfx-designer's integrated review (two-client) and, for a server result, the qa-lead (rejected request).
        cases = {(): (), ("danger-area",): ("hit-shape overlay",), ("server-result",): ("rejected request",),
                 ("danger-area", "server-result"): ("hit-shape overlay", "rejected request")}
        for risks, wanted in cases.items():
            with self.subTest(risks=risks):
                out = fx("build", {"dump": r"RV-candidate-r0-(scripts|vfx-designer|qa-lead)"}, risks=list(risks))
                cap = brief(out, SCRIPTS)
                judge = brief(out, r"vfx-designer: RV-candidate-r0")
                self.assertIn("two-client", cap)
                self.assertIn("two-client", judge)
                for name in ("hit-shape overlay", "rejected request"):
                    self.assertEqual(name in cap, name in wanted, name)
                if "server-result" in risks:
                    self.assertIn("rejected request", brief(out, r"qa-lead: RV-candidate-r0"))

    # ------------------------------------------------------------------ cross-type rules
    def test_options_not_picked_become_closed_doors(self):
        # J024: D3-synthesis → M1-merge writes direction.md with each option's "may return only if"; B2-spec/B0-first-spec → B2-vfx, B3-sound.
        out = fx("direction", {"dump": r"M1-merge"})
        self.assertIn('"may return only if"', brief(out, r"vfx-designer: M1-merge"))
        self.assertIn("closed doors", out["outcome"])
        self.assertIn("closed_doors", out["result"]["g1"])
        build = fx("build", {"dump": r"B2-vfx|B3-sound"}, size="M")
        for pat in (r"B2-vfx", r"B3-sound"):
            self.assertRegex(brief(build, pat), r"avoid: \[[^\]]*may return only if")

    def test_one_marker_list_where_animation_vfx_and_sound_meet(self):
        # J024: E-r1-sound-designer meeting note (proof) → the D1 timeline holds the one marker list, the merge keeps it, and the build
        # sound brief carries the one-marker-list rule.
        out = fx("direction", {"dump": r"D1-plan|M1-merge"})
        self.assertIn("one marker list", brief(out, r"vfx-designer: D1-plan"))
        self.assertIn("One marker list", brief(out, r"vfx-designer: M1-merge"))
        self.assertIn("One marker list", brief(fx("build", {"dump": r"B3-sound"}), r"sound-designer: B3-sound"))

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

    # ------------------------------------------------------------------ J019 follow-up: the wiring gets the code review
    def test_the_proof_wiring_gets_the_code_review(self):
        # J024: the L proof wiring's code review → no proof; the reviewer reviews the build and repair wiring in every round 0, M and L.
        for stage, tag in (("build", "candidate"), ("repair", "repair")):
            for size in ("L", "M"):
                with self.subTest(stage=stage, size=size):
                    out = run(NAME, full(NAME, stage=stage, size=size, risks=[]), {"dump": rf"reviewer: RV-{tag}-r0-reviewer", "affected": ["vfx-designer"]})
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertGreaterEqual(index(out["labels"], rf"reviewer: RV-{tag}-r0-reviewer"), 0)
                    self.assertIn("wiring", out["dumps"][0]["prompt"])
                    self.assertIn("networking-security", out["dumps"][0]["prompt"])


if __name__ == "__main__":
    unittest.main()
