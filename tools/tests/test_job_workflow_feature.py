"""Feature workflow tests (.agents/workflows/jobs/job-feature.js) for the recipe rows of b2eeb73 and the risks arg, with fake agents.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: the feature workflow runs the
recipe rows of orchestration/references/job-types.md §5 and the cross-type rules). Uses the helpers of test_job_workflows;
skipped when Node.js is not installed.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

NAME = "job-feature.js"
ALL_RISKS = ["saves", "remotes", "trades", "paid-random", "server-result", "rewards", "event"]
CODE_RISKS = ("saves", "remotes", "trades", "paid-random")
NOT_VERIFIED = {"set": {"checks": [{"id": "C1", "result": "not verified", "evidence": "no second client"}]}}


def feat(stage: str, scenario: dict | None = None, **changes) -> dict:
    return run(NAME, full(NAME, stage=stage, **changes), scenario)


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class FeatureWorkflowTests(unittest.TestCase):
    def assertDone(self, out: dict) -> None:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])

    # ------------------------------------------------------------------ the risks arg (README args table)
    def test_risks_must_be_a_list_in_every_stage(self):
        for stage in STAGES:
            for bad in (None, "saves", {"saves": True}):
                with self.subTest(stage=stage, risks=bad):
                    out = feat(stage, risks=bad)
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])

    def test_an_unknown_risk_token_is_blocked(self):
        for token in ("new-enemy", "money", "shop-screen"):
            with self.subTest(token=token):
                out = feat("build", risks=["saves", token])
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    def test_every_stage_runs_clean_with_every_risk(self):
        for stage in STAGES:
            for size in ("M", "L"):
                if stage == "proof" and size == "M":
                    continue
                for scen in ({}, {"uniform": True}, {"conflicts": True, "refuseSign": True}):
                    with self.subTest(stage=stage, size=size, scenario=scen):
                        out = feat(stage, scen, size=size, risks=ALL_RISKS)
                        self.assertDone(out)
                        self.assertLessEqual(out["maxConcurrent"], 5)
                        self.assertEqual(out["result"]["skipped_slots"], [])

    # ------------------------------------------------------------------ direction: feedback stack, consults, closed doors
    def test_direction_consults_come_after_the_draft_and_before_signatures(self):
        out = feat("direction", {"timeline": True, "dump": r": D1-game-designer|D3-synthesis"})
        self.assertDone(out)
        draft = span(out, r"^game-designer: D3-synthesis$")
        sign = span(out, r"^architect: D3-sign-architect$")
        for role in ("animator", "sound-designer"):
            with self.subTest(role=role):
                consult = span(out, rf"^{role}: D3-consult-{role}$")
                self.assertGreater(consult["start"], draft["end"], "a consult reads the game-designer's spec, so it follows the draft")
                self.assertGreater(sign["start"], consult["end"], "signers read the consult notes")
        self.assertIn("feedback stack per action", brief(out, r": D1-game-designer"))
        synth = brief(out, r"D3-synthesis")
        self.assertIn("may return only if", synth)
        self.assertIn("failed a check", synth)

    def test_direction_consults_follow_the_draft_flags(self):
        quiet = feat("direction", {"set": {"no_timed_actions": True}})
        self.assertDone(quiet)
        self.assertEqual(index(quiet["labels"], r"^animator:"), -1)
        self.assertGreaterEqual(index(quiet["labels"], r"^sound-designer: D3-consult"), 0)
        mute = feat("direction", {"set": {"no_player_feedback": True}})
        self.assertDone(mute)
        self.assertEqual(index(mute["labels"], r"^sound-designer:"), -1)

    def test_a_consult_conflict_goes_to_the_resolution_round(self):
        clean = feat("direction")
        self.assertEqual(index(clean["labels"], r"D3-resolution"), -1)
        out = feat("direction", {"set": {"conflicts": [{"about": "the hit window", "why": "too short to read", "needs": "6 frames"}]}})
        self.assertDone(out)
        self.assertGreater(index(out["labels"], r"^game-designer: D3-resolution$"), index(out["labels"], r"D3-sign-architect"))

    # ------------------------------------------------------------------ contract time: tier table, trace table, needs round
    def test_rewards_put_the_tier_table_in_the_contract_before_production(self):
        out = feat("build", {"dump": r"B4-ui|B5-vfx|B6-sound"}, size="M", risks=["rewards"])
        self.assertDone(out)
        tiers = index(out["labels"], r"^progression-designer: P1-tiers$")
        self.assertGreater(tiers, index(out["labels"], r"^game-designer: P1-contract$"))
        self.assertLess(tiers, index(out["labels"], r": P2-needs-r1-"), "the crafts state needs against the tiers")
        for pat in (r"^ui-ux-designer: B4-ui$", r"^vfx-designer: B5-vfx$", r"^sound-designer: B6-sound$"):
            with self.subTest(step=pat):
                self.assertLess(tiers, index(out["labels"], pat))
                self.assertIn("tier-table.md", brief(out, pat))
        large = feat("build", {"dump": r"B4-ui"}, risks=["rewards"])
        self.assertEqual(index(large["labels"], r"P1-tiers"), -1, "an L build takes the tier table approved at G2")
        self.assertIn("tier-table.md", brief(large, r"B4-ui"))
        none = feat("build", size="M")
        self.assertEqual(index(none["labels"], r"P1-tiers"), -1)
        self.assertTrue(any("tier table" in s for s in none["result"]["skipped_slots"]))

    def test_trace_table_is_written_at_contract_time(self):
        out = feat("build", {"dump": r"B1-plan$|B1-acceptance"}, size="M")
        self.assertDone(out)
        trace = index(out["labels"], r"^qa-lead: P1-trace$")
        self.assertGreater(trace, index(out["labels"], r"^game-designer: P1-contract$"))
        self.assertLess(trace, index(out["labels"], r": P2-needs-r1-"))
        self.assertIn("trace-table.md", brief(out, r"B1-plan$"))
        self.assertIn("trace-table.md", brief(out, r"B1-acceptance"))

    def test_crafts_state_needs_before_the_plan_is_frozen(self):
        out = feat("build", {"timeline": True, "dump": r"B1-plan$"}, size="M")
        self.assertDone(out)
        plan = index(out["labels"], r"^architect: B1-plan$")
        for role in ("animator", "ui-ux-designer", "vfx-designer", "sound-designer"):
            with self.subTest(role=role):
                self.assertGreaterEqual(index(out["labels"], rf"^{role}: P2-needs-r1-{role}$"), 0)
                self.assertLess(index(out["labels"], rf"^{role}: P2-needs-r1-{role}$"), plan)
        merge = span(out, r"^architect: P2-presentation-r1$")
        for role in ("animator", "ui-ux-designer", "vfx-designer", "sound-designer"):
            self.assertGreater(merge["start"], span(out, rf"^{role}: P2-needs-r1-")["end"], "the architect merges after every note")
        # One marker list: the animator writes first, VFX keys to it, sound answers VFX.
        self.assertGreater(span(out, r"^vfx-designer: P2-needs-r1-")["start"], span(out, r"^animator: P2-needs-r1-")["end"])
        self.assertGreater(span(out, r"^sound-designer: P2-needs-r1-")["start"], span(out, r"^vfx-designer: P2-needs-r1-")["end"])
        self.assertIn("presentation-contract.md@rev", brief(out, r"B1-plan$"))
        large = feat("build", {"dump": r"B1-plan$"})
        self.assertIn("presentation-contract.md@<the revision approved at G2", brief(large, r"B1-plan$"))

    def test_needs_rounds_are_at_most_two(self):
        out = feat("proof", {"conflicts": True})
        self.assertDone(out)
        self.assertGreaterEqual(index(out["labels"], r"^game-designer: P2-merge-r1$"), 0)
        self.assertGreaterEqual(index(out["labels"], r"^architect: P2-presentation-r2$"), 0)
        self.assertEqual(index(out["labels"], r"-r3"), -1)
        clean = feat("proof")
        self.assertEqual(index(clean["labels"], r"P2-.*-r2"), -1, "no open item: one round")

    def test_no_motion_means_no_animator(self):
        out = feat("proof", {"set": {"crafts_not_needed": [{"role": "animator", "why": "no timed action"}]}})
        self.assertDone(out)
        self.assertEqual(index(out["labels"], r"^animator:"), -1)

    # ------------------------------------------------------------------ proof: the skeleton with temp cues
    def test_prototype_is_the_skeleton_with_temp_cues(self):
        out = feat("proof", {"timeline": True, "dump": r"P3-prototype"})
        self.assertDone(out)
        self.assertGreater(span(out, r"feature-builder: P3-prototype")["start"], span(out, r"^sound-designer: P3-temp-cues$")["end"])
        proto = brief(out, r"P3-prototype")
        self.assertIn("named stand-ins", proto)
        self.assertIn("temp cues", proto)
        silent = feat("proof", {"set": {"crafts_not_needed": [{"role": "sound-designer", "why": "no sound"}]}})
        self.assertDone(silent)
        self.assertEqual(index(silent["labels"], r"P3-temp-cues"), -1)

    # ------------------------------------------------------------------ build: plan check, skeleton, presentation pass, integration
    def test_plan_check_runs_only_with_money_or_a_code_risk(self):
        for money, risks in [(True, [])] + [(False, [r]) for r in CODE_RISKS]:
            with self.subTest(money=money, risks=risks):
                out = feat("build", money=money, risks=risks)
                self.assertDone(out)
                plan = index(out["labels"], r"^architect: B1-plan$")
                check = index(out["labels"], r"^reviewer: B1-plan-check$")
                build = index(out["labels"], r"^feature-builder: B2-build$")
                self.assertTrue(0 <= plan < check < build, out["labels"])
        for risks in ([], ["rewards", "server-result", "event"]):
            with self.subTest(money=False, risks=risks):
                out = feat("build", money=False, risks=risks)
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"B1-plan-check"), -1)
                self.assertTrue(any("plan check" in s for s in out["result"]["skipped_slots"]))

    def test_plan_check_findings_get_one_architect_answer(self):
        out = feat("build", {"blockLabel": r"^reviewer: B1-plan-check$", "maker": "architect"})
        self.assertDone(out)
        self.assertEqual(sum(1 for x in out["labels"] if x == "architect: B1-plan-answer"), 1, "one exchange")
        self.assertLess(index(out["labels"], r"B1-plan-answer"), index(out["labels"], r"^feature-builder: B2-build$"))
        self.assertEqual(index(feat("build")["labels"], r"B1-plan-answer"), -1)

    def test_skeleton_comes_before_the_presentation_pass(self):
        out = feat("build", {"timeline": True})
        self.assertDone(out)
        skel = span(out, r"^feature-builder: B2-build$")
        self.assertGreater(skel["start"], span(out, r"^qa-lead: B1-acceptance$")["end"], "protected tests before code")
        ends = []
        for pat in (r"B3-tables", r"B4-ui", r"B5-vfx", r"B6-sound"):
            with self.subTest(step=pat):
                self.assertGreater(span(out, pat)["start"], skel["end"])
                ends.append(span(out, pat)["end"])
        self.assertGreater(span(out, r"B7-integrate")["start"], max(ends))

    def test_integration_delivers_hooks_first_and_runs_the_worst_case_pass(self):
        out = feat("build", {"dump": r"B7-integrate"})
        text = brief(out, r"B7-integrate")
        for phrase in ("test hooks", "debug log", "before any partner's first capture", "presentation.md §9", "worst-case pass"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        self.assertLess(text.index("test hooks"), text.index("wire everything"))

    # ------------------------------------------------------------------ review chain
    def test_review_chain_runs_the_architect_beside_the_technical_checks(self):
        out = feat("build", {"timeline": True, "dump": r"architect: RV-"})
        self.assertDone(out)
        arch = span(out, r"^architect: RV-candidate-r0-architect$")
        self.assertLess(arch["start"], span(out, r"^studio-operator: RV-candidate-r0-capture$")["end"], "starts beside the capture, not after the creative order")
        self.assertIn("review-checklist.md", brief(out, r"architect: RV-"))

    def test_game_designer_judges_the_named_captures(self):
        out = feat("build", {"dump": r"game-designer: RV-|studio-operator: RV-"}, money=True)
        for pat in (r"game-designer: RV-", r"studio-operator: RV-"):
            text = brief(out, pat)
            for name in ("rejected request", "slow confirmation", "two-client", "grayscale, sound off, reduced motion", "the real rate and a burst", "lowest graphics"):
                with self.subTest(step=pat, capture=name):
                    self.assertIn(name, text)
        server = feat("build", {"dump": r"game-designer: RV-"}, money=False, risks=["server-result"])
        self.assertIn("rejected request", brief(server, r"game-designer: RV-"))
        plain = feat("build", {"dump": r"game-designer: RV-"}, money=False)
        self.assertNotIn("rejected request", brief(plain, r"game-designer: RV-"))
        self.assertTrue(any("rejected-request" in s for s in plain["result"]["skipped_slots"]))

    def test_event_adds_the_live_ops_review_after_the_creative_reviews(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = feat(stage, {"timeline": True, "dump": r"live-ops-designer: RV-|studio-operator: RV-"}, risks=["event"])
                self.assertDone(out)
                live = span(out, r"^live-ops-designer: RV-\w+-r0-live-ops-designer$")
                self.assertGreater(live["start"], span(out, r"^art-director: RV-\w+-r0-")["end"])
                self.assertGreater(live["start"], span(out, r"^game-designer: RV-\w+-r0-")["end"])
                text = brief(out, r"live-ops-designer: RV-")
                self.assertIn("E-01 to E-19", text)
                self.assertIn("event-review.md §2-§3", text)
                self.assertIn("model: opus", text)
                self.assertIn("effort: medium", text)
                self.assertIn("event-review.md §2", brief(out, r"studio-operator: RV-"))
                plain = feat(stage)
                self.assertEqual(index(plain["labels"], r"live-ops-designer"), -1)

    def test_live_ops_findings_route_to_makers_inside_the_round_limits(self):
        out = feat("build", {"blockLabelOnce": r"^live-ops-designer: RV-candidate-r0", "maker": "ui-ux-designer"}, risks=["event"])
        self.assertDone(out)
        self.assertGreaterEqual(index(out["labels"], r"^ui-ux-designer: FIX-candidate-r0-ui-ux-designer$"), 0)
        self.assertGreaterEqual(index(out["labels"], r"^live-ops-designer: RV-candidate-r1-"), 0)
        stuck = feat("build", {"blockLabel": r"^live-ops-designer: RV-", "maker": "ui-ux-designer"}, risks=["event"])
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])

    # ------------------------------------------------------------------ gate packets (cross-type rules)
    def test_gate_results_carry_could_not_check_and_owner_lines(self):
        g1 = feat("direction", NOT_VERIFIED)
        self.assertDone(g1)
        self.assertTrue(g1["result"]["g1"]["could_not_check"])
        self.assertEqual(g1["result"]["g1"]["owner_confirmed"], [], "nothing plays before G2")
        g2 = feat("proof", NOT_VERIFIED)
        self.assertDone(g2)
        self.assertTrue(g2["result"]["could_not_check"])
        self.assertTrue(any("feel at normal speed" in x for x in g2["result"]["owner_confirmed"]))
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                g3 = feat(stage, NOT_VERIFIED)
                self.assertDone(g3)
                self.assertTrue(g3["result"]["could_not_check"])
                lines = g3["result"]["owner_confirmed"]
                self.assertTrue(any("feel at normal speed" in x for x in lines))
                self.assertTrue(any("two listens" in x and "phone speaker" in x and "headphones" in x for x in lines))
        silent = feat("build", {"set": {"crafts_not_needed": [{"role": "sound-designer", "why": "no sound"}]}})
        self.assertDone(silent)
        self.assertFalse(any("two listens" in x for x in silent["result"]["owner_confirmed"]))


    # ------------------------------------------------------------------ J019 lead review: reviewer effort follows the code risks
    def test_reviewer_and_builder_run_high_for_code_risks_without_money(self):
        for risk in CODE_RISKS:
            with self.subTest(risk=risk):
                out = feat("build", {"dump": r"(reviewer|feature-builder): "}, risks=[risk], money=False)
                self.assertTrue(out["dumps"])
                self.assertTrue(all("effort: high" in d["prompt"] for d in out["dumps"]), [d["label"] for d in out["dumps"]])
        low = feat("build", {"dump": r"reviewer: RV-"}, risks=[], money=False)
        self.assertTrue(all("effort: medium" in d["prompt"] for d in low["dumps"]))


if __name__ == "__main__":
    unittest.main()
