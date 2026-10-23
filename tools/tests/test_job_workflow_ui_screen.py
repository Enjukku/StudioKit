"""Control-flow tests for job-ui-screen.js: the recipe rows of job-types.md §4 (J019, commit b2eeb73) and the `risks` arg.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4).
Runs tools/workflows/wf_harness.mjs under Node with fake agents (no tokens); skipped when Node is not installed.
Shared helpers and the base args come from tools/tests/test_job_workflows.py.
"""

from __future__ import annotations

import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

UI = "job-ui-screen.js"


def ui(**changes) -> dict:
    return full(UI, **changes)


@unittest.skipIf(NODE is None, "Node.js not installed")
class UiScreenRecipeTests(unittest.TestCase):
    # ------------------------------------------------------------------ the risks arg (README args table)
    def test_missing_risks_is_blocked_before_any_agent(self):
        for stage in STAGES:
            for bad in (None, "paid-random", {"a": 1}):
                with self.subTest(stage=stage, risks=bad):
                    out = run(UI, ui(stage=stage, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])
        self.assertIn("risks", run(UI, ui(stage="direction"))["meta"]["whenToUse"])

    def test_unknown_risk_token_is_blocked_by_name(self):
        for token in ("saves", "new-enemy", "Paid-Random"):
            with self.subTest(token=token):
                out = run(UI, ui(stage="build", risks=["event", token]))
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    def test_every_accepted_token_runs_every_stage(self):
        all_risks = ["paid-random", "server-result", "shop-screen", "event"]
        for stage in STAGES:
            with self.subTest(stage=stage):
                out = run(UI, ui(stage=stage, risks=all_risks), {"affected": ["ui-ux-designer"]})
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(out["result"]["risks"], all_risks)

    # ------------------------------------------------------------------ direction (G1)
    def test_information_list_comes_before_the_ui_flow(self):
        out = run(UI, ui(stage="direction"), {"timeline": True, "dump": r": D1-(game|ui)"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertGreater(span(out, r"ui-ux-designer: D1-")["start"], span(out, r"game-designer: D1-")["end"])
        design = next(d for d in out["dumps"] if "game-designer" in d["label"])["prompt"]
        flow = next(d for d in out["dumps"] if "ui-ux-designer" in d["label"])["prompt"]
        for text in ("information-list.md", "read times", "read rank", "feedback stack", "documents.md §6, §9"):
            with self.subTest(text=text):
                self.assertIn(text, design)
        for text in ("information-list.md", "taps per task", "2-3 wireframe options", "look_check.py value --compare-subjects", "equal finish"):
            with self.subTest(text=text):
                self.assertIn(text, flow)

    def test_g1_carries_failed_options_closed_doors_and_could_not_check(self):
        out = run(UI, ui(stage="direction"), {"dump": r"D3-synthesis"})
        g1 = out["result"]["g1"]
        for key in ("failed_options", "closed_doors", "could_not_check", "owner_confirmed"):
            with self.subTest(key=key):
                self.assertIn(key, g1)
        synth = out["dumps"][0]["prompt"]
        self.assertIn("may return only if", synth)
        self.assertIn("grey value pass", synth)

    def test_progression_designer_joins_direction_for_a_shop_screen(self):
        odds = run(UI, ui(stage="direction", shop=False, risks=["shop-screen"]))
        self.assertGreaterEqual(index(odds["labels"], r"progression-designer: D1-"), 0)
        plain = run(UI, ui(stage="direction", shop=False))
        self.assertEqual(index(plain["labels"], r"progression-designer"), -1)

    # ------------------------------------------------------------------ proof (G2)
    def test_g2_has_the_owner_confirmed_motion_line(self):
        out = run(UI, ui(stage="proof"), {"dump": r"P1-prototype"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertIn("motion feel at normal speed on the Figma prototype", out["result"]["g2"]["owner_confirmed"])
        self.assertIn("normal speed", out["dumps"][0]["prompt"])
        self.assertIn("closed doors", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ production order (build)
    def test_plan_check_runs_before_the_builder_only_with_the_risk(self):
        cases = [(dict(shop=True, risks=[]), True), (dict(shop=False, risks=["paid-random"]), True),
                 (dict(shop=False, risks=[]), False), (dict(shop=False, risks=["server-result", "shop-screen", "event"]), False)]
        for changes, expect in cases:
            for size in ("M", "L"):
                with self.subTest(changes=changes, size=size):
                    # L: the plan check runs in the proof, before the storyboard (J019-LD2); M: at the start of build
                    out = run(UI, ui(stage="build" if size == "M" else "proof", size=size, **changes))
                    self.assertEqual(out["status"], "done", out["outcome"])
                    labels = out["labels"]
                    check = index(labels, r"^reviewer: B0-plan-check")
                    self.assertEqual(check >= 0, expect, labels)
                    if expect:
                        self.assertLess(check, index(labels, r"B0-storyboard"))
                        self.assertLess(check, index(labels, r"feature-builder: B2-implement" if size == "M" else r"P1-prototype"))
                        if size == "M":
                            self.assertGreater(check, index(labels, r"architect: C3-code-owners"))
                    else:
                        self.assertIn("reviewer plan check (no shop, no paid-random)", out["result"]["skipped_slots"])

    def test_plan_check_findings_correct_the_plan_before_the_build(self):
        for maker, fixer in (("architect", r"architect: B0-plan-fix-architect"), ("ui-ux-designer", r"ui-ux-designer: B0-plan-fix-ui-ux-designer")):
            with self.subTest(maker=maker):
                out = run(UI, ui(stage="build", size="M"), {"blockLabel": r"reviewer: B0-plan-check", "maker": maker})
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                fix = index(labels, fixer)
                self.assertTrue(index(labels, r"B0-plan-check") < fix < index(labels, r"B0-storyboard$"), labels)
                self.assertEqual(sum(1 for x in labels if "B0-plan-check" in x), 1, "one exchange, no second check")

    def test_storyboard_runs_vfx_then_sound_before_the_figma_build(self):
        out = run(UI, ui(stage="build", size="M"), {"timeline": True, "set": {"world_to_hud": True}, "dump": r"B1-figma"})
        self.assertEqual(out["status"], "done", out["outcome"])
        board = span(out, r"ui-ux-designer: B0-storyboard$")
        vfx = span(out, r"vfx-designer: B0-storyboard-vfx")
        sound = span(out, r"sound-designer: B0-storyboard-sound")
        figma = span(out, r"ui-ux-designer: B1-figma")
        self.assertGreater(vfx["start"], board["end"])
        self.assertGreater(sound["start"], vfx["end"], "sound answers the VFX beats")
        self.assertGreater(figma["start"], sound["end"], "the storyboard comes before the Figma motion work")
        prompt = out["dumps"][0]["prompt"]
        for text in ("motion/storyboard.md@rev", "storyboard-vfx-designer.md", "storyboard-sound-designer.md", "one marker list"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_storyboard_without_world_rewards_skips_vfx_beats(self):
        out = run(UI, ui(stage="build", size="M"), {"timeline": True, "dump": r"B0-storyboard-sound"})
        self.assertEqual(index(out["labels"], r"B0-storyboard-vfx"), -1)
        self.assertGreater(span(out, r"ui-ux-designer: B1-figma")["start"], span(out, r"sound-designer: B0-storyboard-sound")["end"])
        self.assertNotIn("storyboard-vfx-designer.md", out["dumps"][0]["prompt"])

    def test_hooks_and_debug_log_come_before_the_first_capture(self):
        out = run(UI, ui(stage="build", risks=["paid-random"]), {"dump": r"B2-implement"})
        labels = out["labels"]
        self.assertLess(index(labels, r"feature-builder: B2-implement"), index(labels, r"studio-operator: B6-capture"))
        prompt = out["dumps"][0]["prompt"]
        for text in ("test hooks and the debug log", "presentation.md §9", "Reject", "DelayMs", "Outcome or Seed"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    # ------------------------------------------------------------------ review captures and review order
    def test_studio_operator_takes_the_named_captures(self):
        cases = [(dict(shop=False, risks=["paid-random"]), True, False), (dict(shop=False, risks=["server-result"]), False, True),
                 (dict(shop=True, risks=[]), False, True), (dict(shop=False, risks=[]), False, False)]
        for changes, tiers, rejected in cases:
            with self.subTest(changes=changes):
                out = run(UI, ui(stage="build", **changes), {"dump": r"B6-capture"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertTrue(out["dumps"])
                for d in out["dumps"]:
                    self.assertTrue(d["label"].startswith("studio-operator: "), d["label"])
                    p = d["prompt"]
                    for text in ("Device Simulator", "smallest phone", "busiest gameplay moment", "f###_<ms>ms.jpg", "S-33", "reduced motion", "largest text size"):
                        self.assertIn(text, p)
                    self.assertEqual("paid-reveal tier" in p, tiers)
                    self.assertEqual("a rejected request (hook Reject)" in p, rejected)

    def test_a_repair_round_is_recaptured_before_the_next_review(self):
        out = run(UI, ui(stage="build"), {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "ui-ux-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        recap = index(labels, r"studio-operator: B6-capture-candidate-r0-fix")
        self.assertTrue(index(labels, r"feature-builder: FIX-candidate-r0") < recap < index(labels, r": RV-candidate-r1-"), labels)

    def test_qa_slot_runs_the_truth_rows(self):
        out = run(UI, ui(stage="build"), {"dump": r"qa-lead: RV-candidate-r0"})
        prompt = out["dumps"][0]["prompt"]
        for text in ("rejected request and the pending path", "after a burst", "buy during the count-up", "refusals shown at the control", "reduced motion on", "smallest phone"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_progression_review_sits_between_ui_and_art_only_with_the_risk(self):
        cases = [(dict(shop=True, risks=[]), True), (dict(shop=False, risks=["shop-screen"]), True), (dict(shop=False, risks=["paid-random"]), True),
                 (dict(shop=False, risks=["server-result"]), False)]   # a paid reveal shows odds rows (J019 lead review)
        for changes, expect in cases:
            with self.subTest(changes=changes):
                out = run(UI, ui(stage="build", **changes), {"dump": r"progression-designer: RV-"})
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                prog = index(labels, r"progression-designer: RV-candidate-r0")
                self.assertEqual(prog >= 0, expect, labels)
                if expect:
                    self.assertTrue(index(labels, r"ui-ux-designer: RV-candidate-r0") < prog < index(labels, r"art-director: RV-candidate-r0"), labels)
                    p = out["dumps"][0]["prompt"]
                    self.assertIn("data-handoff.md §4-§5", p)
                    self.assertIn("two timeline points", p)

    def test_progression_findings_route_to_the_progression_designer(self):
        out = run(UI, ui(stage="build", shop=False, risks=["shop-screen"]),
                  {"blockLabelOnce": r"progression-designer: RV-candidate-r0", "maker": "progression-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertGreaterEqual(index(out["labels"], r"progression-designer: FIX-candidate-r0"), 0)

    def test_event_adds_the_live_ops_review_after_the_creative_chain(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = run(UI, ui(stage=stage, risks=["event"]), {"affected": ["ui-ux-designer"], "dump": r"live-ops-designer: RV-"})
                self.assertEqual(out["status"], "done", out["outcome"])
                labels = out["labels"]
                label = f"RV-{'candidate' if stage == 'build' else 'repair'}-r0"
                ops = index(labels, rf"live-ops-designer: {label}")
                self.assertGreaterEqual(ops, 0, labels)
                for before in ("ui-ux-designer", "art-director", "game-designer"):
                    self.assertLess(index(labels, rf"{before}: {label}"), ops)
                p = out["dumps"][0]["prompt"]
                self.assertIn("model: opus", p)
                self.assertIn("effort: medium", p)
                self.assertIn("E-01 to E-19", p)
                self.assertIn("event-review.md §2-§3", p)
        plain = run(UI, ui(stage="build"))
        self.assertEqual(index(plain["labels"], r"live-ops-designer"), -1)
        self.assertIn("live-ops event review (no event)", plain["result"]["skipped_slots"])

    def test_event_findings_stay_inside_the_repair_limits(self):
        out = run(UI, ui(stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "ui-ux-designer"})
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(index(out["labels"], r"RV-candidate-r3-"), -1)

    def test_g3_carries_owner_confirmed_lines_and_could_not_check(self):
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = run(UI, ui(stage=stage), {"affected": ["ui-ux-designer"]})
                g3 = out["result"]["g3"]
                self.assertIn("could_not_check", g3)
                lines = " ".join(g3["owner_confirmed"])
                self.assertIn("motion feel at normal speed", lines)
                self.assertIn("the key event alone, then the full mix", lines)
                self.assertIn("phone speaker and on headphones", lines)

    def test_read_order_failures_return_to_the_grey_value_pass(self):
        out = run(UI, ui(stage="build"), {"dump": r"art-director: RV-candidate-r0"})
        self.assertIn("returns to the grey value pass", out["dumps"][0]["prompt"])
        self.assertIn("read order", out["dumps"][0]["prompt"])


    # ------------------------------------------------------------------ J019 lead review: a review that does not finish is never a pass
    def test_a_plan_check_that_does_not_finish_stops_the_build(self):
        out = run(UI, ui(stage="build", size="M", risks=["paid-random"]), {"statusLabel": r"B0-plan-check", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(index(out["labels"], r"B2-implement"), -1, "no build after an unfinished plan check")

    def test_a_code_review_that_does_not_finish_is_not_clean(self):
        out = run(UI, ui(stage="build"), {"statusLabel": r"CR-candidate-code-r0", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])

    def test_a_paid_reveal_gets_the_progression_review_and_a_high_reviewer(self):
        out = run(UI, ui(stage="build", size="M", risks=["paid-random"], shop=False), {"dump": r"reviewer: B0-plan-check"})
        self.assertGreater(index(out["labels"], r"progression-designer: RV-candidate-r0-"), -1)
        self.assertIn("effort: high", out["dumps"][0]["prompt"])


    # ------------------------------------------------------------------ J019-LD2: in L jobs the storyboard comes before the G2 prototype
    def test_l_proof_runs_plan_check_then_storyboard_then_the_prototype(self):
        out = run(UI, ui(stage="proof", size="L", shop=True), {"timeline": True, "set": {"world_to_hud": True}, "dump": r"P1-prototype"})
        self.assertEqual(out["status"], "done", out["outcome"])
        check = span(out, r"reviewer: B0-plan-check")
        board = span(out, r"ui-ux-designer: B0-storyboard$")
        sound = span(out, r"sound-designer: B0-storyboard-sound")
        proto = span(out, r"ui-ux-designer: P1-prototype")
        self.assertTrue(check["end"] < board["start"] and sound["end"] < proto["start"], out["labels"])
        prompt = out["dumps"][0]["prompt"]
        for text in ("motion/storyboard.md@rev", "storyboard-sound-designer.md", "G2 freezes those beats"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_l_build_keeps_the_g2_beat_list_and_runs_no_second_storyboard(self):
        out = run(UI, ui(stage="build", size="L", shop=True), {"dump": r"B1-figma"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"B0-storyboard"), -1)
        self.assertEqual(index(out["labels"], r"B0-plan-check"), -1, "the plan check ran in the proof")
        self.assertIn("the beat list the owner approved at G2", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ J019 follow-up: after a repair the gate recheck runs first, alone
    def test_after_a_repair_the_gate_recheck_runs_before_the_other_reviews(self):
        out = run(UI, ui(stage="build"), {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "ui-ux-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        recheck = index(labels, r"reviewer: RV-candidate-r1-reviewer")
        self.assertGreaterEqual(recheck, 0)
        self.assertLess(recheck, index(labels, r"qa-lead: RV-candidate-r1-"))
        self.assertLess(recheck, index(labels, r"ui-ux-designer: RV-candidate-r1-"))
        held = run(UI, ui(stage="build"), {"blockLabel": r"art-director: RV-candidate-r0|reviewer: RV-candidate-r1-reviewer", "maker": "ui-ux-designer"})
        self.assertEqual(index(held["labels"], r"ui-ux-designer: RV-candidate-r1-"), -1, "a failing recheck holds back the other reviews that round")


if __name__ == "__main__":
    unittest.main()
