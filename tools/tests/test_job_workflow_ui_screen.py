"""Control-flow tests for job-ui-screen.js: the recipe rows of job-types.md §4 (J019, commit b2eeb73) and the `risks` arg.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4); revised by J024 test updater ·
claude-opus-5-5 · default · 2026-10-24 (J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md: no proof and no G2, needs tables before G1,
no plan check, capture and scripts on the studio-operator, fewer reviewers).
Runs tools/workflows/wf_harness.mjs under Node with fake agents (no tokens); skipped when Node is not installed.
Shared helpers and the base args come from tools/tests/test_job_workflows.py.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

UI = "job-ui-screen.js"
EFFECTS = {"set": {"ui_effects": True}}   # J024: the vfx-designer runs only when the plan lists UI effects (D1, merge and B1-figma field)


def ui(**changes) -> dict:
    return full(UI, **changes)


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class UiScreenRecipeTests(unittest.TestCase):
    # ------------------------------------------------------------------ the risks arg (README args table)
    def test_missing_risks_is_blocked_before_any_agent(self):
        # J024: STAGES lost proof; `stage: "proof"` is refused first, with the no-proof reason.
        for stage in STAGES + ("proof",):
            for bad in (None, "paid-random", {"a": 1}):
                with self.subTest(stage=stage, risks=bad):
                    out = run(UI, ui(stage=stage, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("no proof stage (J024)" if stage == "proof" else "risks", out["outcome"])
        self.assertIn("risks", run(UI, ui(stage="direction"))["meta"]["whenToUse"])

    def test_unknown_risk_token_is_blocked_by_name(self):
        for token in ("saves", "new-enemy", "Paid-Random"):
            with self.subTest(token=token):
                out = run(UI, ui(stage="build", risks=["event", token]))
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    def test_every_accepted_token_runs_every_stage(self):
        # J024: no proof stage; the token list adds performance (§7).
        all_risks = ["paid-random", "server-result", "shop-screen", "event", "performance"]
        for stage in STAGES:
            with self.subTest(stage=stage):
                out = run(UI, ui(stage=stage, risks=all_risks), {"affected": ["ui-ux-designer"]})
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(out["result"]["risks"], all_risks)

    # ------------------------------------------------------------------ direction (G1)
    def test_information_list_comes_before_the_ui_flow(self):
        # J024: the game-designer's D1 is gone; the ui-ux-designer's D1 plan writes the decision record and the information list (read
        # times, one read rank) before the states and transitions, and the 2-3 wireframe options at equal finish with the grey value pass.
        out = run(UI, ui(stage="direction"), {"dump": r": D1-plan"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"^game-designer:"), -1)
        plan = brief(out, r"ui-ux-designer: D1-plan")
        for text in ("the decision record", "information list per moment with read times and one read rank", "every action including Back and Close",
                     "2-3 options at equal finish, each a wireframe with real content", "look_check.py value --compare-subjects"):
            with self.subTest(text=text):
                self.assertIn(text, plan)
        self.assertLess(plan.index("the decision record"), plan.index("information list per moment"))
        self.assertLess(plan.index("information list per moment"), plan.index("the transitions with stable event ids"), "information before flow")

    def test_g1_carries_failed_options_closed_doors_and_could_not_check(self):
        # J024: D3-synthesis → g1 from the D1 plan (failed options, grey value pass) and the D3 merge (closed doors).
        out = run(UI, ui(stage="direction"), {"dump": r"D1-plan|D3-merge"})
        g1 = out["result"]["g1"]
        for key in ("failed_options", "closed_doors", "could_not_check", "owner_confirmed"):
            with self.subTest(key=key):
                self.assertIn(key, g1)
        self.assertIn("grey value pass", brief(out, r"D1-plan"))
        self.assertIn("failed a check are listed with the reason", brief(out, r"D1-plan"))
        self.assertIn('"Closed doors" section', brief(out, r"D3-merge"))
        self.assertIn("may return only if", out["outcome"])

    def test_progression_designer_joins_direction_for_a_shop_screen(self):
        # J024: D1-progression-designer → its N1 limits table, with shop, shop-screen or paid-random.
        for changes in (dict(shop=False, risks=["shop-screen"]), dict(shop=True), dict(shop=False, risks=["paid-random"])):
            with self.subTest(changes=changes):
                odds = run(UI, ui(stage="direction", **changes))
                self.assertGreaterEqual(index(odds["labels"], r"^progression-designer: N1-limits-progression-designer$"), 0)
                self.assertLess(index(odds["labels"], r"N1-limits-progression"), index(odds["labels"], r"D3-merge"))
        plain = run(UI, ui(stage="direction", shop=False))
        self.assertEqual(index(plain["labels"], r"progression-designer"), -1)

    # ------------------------------------------------------------------ no proof (G2)
    def test_g2_has_the_owner_confirmed_motion_line(self):
        # J024 (G2 removed on purpose, design §1): proof is refused; G1 says motion feel is judged at G3, the G3 packet carries the
        # owner-confirmed motion line, and the Figma build keeps the closed doors.
        proof = run(UI, ui(stage="proof"))
        self.assertEqual((proof["status"], proof["agents"]), ("blocked", 0))
        g1 = run(UI, ui(stage="direction"))["result"]["g1"]
        self.assertTrue(any("motion feel is judged at normal speed" in x and "G3" in x for x in g1["owner_confirmed"]))
        out = run(UI, ui(stage="build"), {"dump": r"B1-figma"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertIn("motion feel at normal speed on the Studio build", out["result"]["g3"]["owner_confirmed"])
        self.assertIn("closed doors", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ production order (build)
    def test_plan_check_runs_before_the_builder_only_with_the_risk(self):
        # J024 (plan check removed on purpose): no plan check in any size or risk; the architect's code contract is its N1 limits table,
        # written before G1, and the builder reads it.
        cases = [dict(shop=True, risks=[]), dict(shop=False, risks=["paid-random"]), dict(shop=False, risks=[]), dict(shop=False, risks=["server-result", "shop-screen", "event"])]
        for changes in cases:
            for size in ("M", "L"):
                with self.subTest(changes=changes, size=size):
                    out = run(UI, ui(stage="build", size=size, **changes), {"dump": r"feature-builder: B4-build"})
                    self.assertEqual(out["status"], "done", out["outcome"])
                    self.assertEqual(index(out["labels"], r"plan-check|plan-fix|B0-"), -1, out["labels"])
                    self.assertFalse(any("plan check" in s for s in out["result"]["skipped_slots"]))
                    self.assertIn("contract-code.md", brief(out, r"B4-build"))
                    dirn = run(UI, ui(stage="direction", size=size, **changes))
                    self.assertLess(index(dirn["labels"], r"^architect: N1-limits-architect$"), index(dirn["labels"], r"D3-merge"))
                    self.assertGreaterEqual(index(dirn["labels"], r"^architect: N1-limits-architect$"), 0)

    def test_plan_check_findings_correct_the_plan_before_the_build(self):
        # J024: no plan check; a code-review finding on the plan goes to the ui-ux-designer first (state map and layout before what is
        # built on them), the builder rebuilds after it, then the recapture; a code-contract finding (architect) is the lead's call.
        out = run(UI, ui(stage="build", size="M"), {"blockLabelOnce": r"^reviewer: RV-candidate-r0", "maker": "ui-ux-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        fix = index(labels, r"^ui-ux-designer: FIX-candidate-r0-ui-ux-designer$")
        self.assertTrue(0 <= fix < index(labels, r"^feature-builder: FIX-candidate-r0") < index(labels, r"RV-candidate-r1-capture"), labels)
        self.assertEqual(sum(1 for x in labels if "FIX-candidate-r0-ui-ux-designer" in x), 1, "one fix, no second exchange")
        arch = run(UI, ui(stage="build", size="M"), {"blockLabelOnce": r"^reviewer: RV-candidate-r0", "maker": "architect"})
        self.assertEqual(arch["status"], "needs-decision", arch["outcome"])
        self.assertEqual(index(arch["labels"], r": FIX-"), -1, "nothing is rebuilt on an unrouted plan finding")

    def test_beat_list_and_meeting_notes_come_before_the_figma_build(self):
        # J024: C1 contract + C2 meeting → the D1 plan writes the spec and the beat list, the N1 sound and VFX tables answer on it, the
        # merge makes it the one marker list, all before G1; the Figma build reads the merged plan and the beat list.
        out = run(UI, ui(stage="direction", size="M"), dict(EFFECTS, timeline=True, dump=r"D1-plan|D3-merge"))
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"storyboard|C1-|C2-"), -1)
        plan = span(out, r"ui-ux-designer: D1-plan")
        vfx = span(out, r"vfx-designer: N1-needs-vfx-designer")
        sound = span(out, r"sound-designer: N1-needs-sound-designer")
        merge = span(out, r"ui-ux-designer: D3-merge")
        self.assertGreater(vfx["start"], plan["end"])
        self.assertGreater(sound["start"], plan["end"])
        self.assertGreater(merge["start"], max(sound["end"], vfx["end"]), "the beats are merged before G1")
        self.assertIn("motion/storyboard.md", brief(out, r"D1-plan"))
        self.assertIn("one marker list", brief(out, r"D3-merge"))
        build = run(UI, ui(stage="build", size="M"), dict(EFFECTS, dump=r"B1-figma"))
        prompt = brief(build, r"B1-figma")
        for text in ("motion/storyboard.md", "the merged plan approved at G1", "/needs/", "one marker list"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_storyboard_without_world_rewards_skips_vfx_beats(self):
        # J024: world_to_hud → the vfx-designer runs only with ui_effects (D1 / merge for N1, B1-figma for build); its briefs carry
        # the world-to-HUD beats.
        ask = "world-to-HUD"
        for stage in ("direction", "build"):
            with self.subTest(stage=stage):
                plain = run(UI, ui(stage=stage, size="M"))
                self.assertEqual(plain["status"], "done", plain["outcome"])
                self.assertEqual(index(plain["labels"], r"^vfx-designer:"), -1)
                world = run(UI, ui(stage=stage, size="M"), dict(EFFECTS, dump=r"^vfx-designer: "))
                self.assertEqual(world["status"], "done", world["outcome"])
                self.assertIn(ask, brief(world, r"^vfx-designer: (N1-needs|B2-ui-effects)"))

    def test_hooks_and_debug_log_come_before_the_first_capture(self):
        # J024: B2-implement → B4-build (implement and integrate in one run) delivers the hooks before the first capture.
        out = run(UI, ui(stage="build", risks=["paid-random"]), {"dump": r"B4-build"})
        labels = out["labels"]
        self.assertLess(index(labels, r"feature-builder: B4-build"), index(labels, r"studio-operator: RV-candidate-r0-capture"))
        prompt = out["dumps"][0]["prompt"]
        for text in ("test hooks and the debug log before any capture", "presentation.md §9", "Reject", "DelayMs", "Outcome or Seed"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    # ------------------------------------------------------------------ review captures and review order
    def test_studio_operator_takes_the_named_captures(self):
        # J024: B6-capture → the capture-and-scripts run RV-<tag>-capture (same named captures, plus the gate and look_check).
        cases = [(dict(shop=False, risks=["paid-random"]), True, False), (dict(shop=False, risks=["server-result"]), False, True),
                 (dict(shop=True, risks=[]), False, True), (dict(shop=False, risks=[]), False, False)]
        for changes, tiers, rejected in cases:
            with self.subTest(changes=changes):
                out = run(UI, ui(stage="build", **changes), {"dump": r"RV-.*-capture"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertTrue(out["dumps"])
                for d in out["dumps"]:
                    self.assertTrue(d["label"].startswith("studio-operator: "), d["label"])
                    p = d["prompt"]
                    for text in ("Device Simulator", "smallest phone", "busiest gameplay moment", "f###_<ms>ms.jpg", "S-33", "reduced motion", "largest text size",
                                 "python tools/verify.py", "look_check.py value --compare-subjects"):
                        self.assertIn(text, p)
                    self.assertEqual("paid-reveal tier" in p, tiers)
                    self.assertEqual("a rejected request (hook Reject)" in p, rejected)

    def test_a_repair_round_is_recaptured_before_the_next_review(self):
        # J024: B6-capture-<tag>-fix → every round starts with RV-<tag>-capture, so round 1 recaptures after the builder's fix.
        out = run(UI, ui(stage="build"), {"blockLabelOnce": r"ui-ux-designer: RV-candidate-r0", "maker": "ui-ux-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        recap = index(labels, r"studio-operator: RV-candidate-r1-capture")
        first_review = min(i for i, x in enumerate(labels) if ": RV-candidate-r1-" in x and not x.startswith("studio-operator"))
        self.assertTrue(index(labels, r"feature-builder: FIX-candidate-r0") < recap < first_review, labels)

    def test_qa_slot_runs_the_truth_rows(self):
        out = run(UI, ui(stage="build"), {"dump": r"qa-lead: RV-candidate-r0"})
        prompt = out["dumps"][0]["prompt"]
        for text in ("rejected request and the pending path", "after a burst", "buy during the count-up", "refusals shown at the control", "reduced motion on", "smallest phone"):
            with self.subTest(text=text):
                self.assertIn(text, prompt)

    def test_progression_review_sits_between_ui_and_art_only_with_the_risk(self):
        # J024 (progression review removed on purpose, design §4.4): no progression-designer review in any case; with shop,
        # shop-screen or paid-random the qa-lead checks every shown number against the progression tables; not on server-result alone.
        cases = [(dict(shop=True, risks=[]), True), (dict(shop=False, risks=["shop-screen"]), True), (dict(shop=False, risks=["paid-random"]), True),
                 (dict(shop=False, risks=["server-result"]), False)]
        for changes, expect in cases:
            with self.subTest(changes=changes):
                out = run(UI, ui(stage="build", **changes), {"dump": r"qa-lead: RV-"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(index(out["labels"], r"progression-designer: RV-"), -1, out["labels"])
                p = brief(out, r"qa-lead: RV-candidate-r0")
                self.assertEqual("every shown price, quantity and odd against the progression tables" in p, expect)
                self.assertEqual("totalling 100 %" in p, expect)

    def test_progression_findings_route_to_the_progression_designer(self):
        # J024: the progression-designer no longer reviews, but a number finding (from the qa-lead) still routes to it as the fixer.
        out = run(UI, ui(stage="build", shop=False, risks=["shop-screen"]),
                  {"blockLabelOnce": r"qa-lead: RV-candidate-r0", "maker": "progression-designer"})
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
        # J024: the art-director reviews only with newLook or visual_flags; every reviewer (the job lead's integrated review always) keeps
        # the layer rule, and the ui-ux-designer's fix brief sends a read-order finding back to the grey value pass.
        out = run(UI, ui(stage="build"), {"dump": r"ui-ux-designer: (RV-candidate-r0|FIX-)", "blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "ui-ux-designer"})
        lead = brief(out, r"ui-ux-designer: RV-candidate-r0")
        self.assertIn("returns to the grey value pass", lead)
        self.assertIn("read order", lead)
        self.assertIn("a read-order finding goes back to the grey value pass", brief(out, r"ui-ux-designer: FIX-"))
        art = run(UI, ui(stage="build", newLook=True), {"dump": r"art-director: RV-candidate-r0"})
        self.assertIn("returns to the grey value pass", brief(art, r"art-director: RV-candidate-r0"))

    # ------------------------------------------------------------------ J019 lead review: a review that does not finish is never a pass
    def test_a_plan_check_that_does_not_finish_stops_the_build(self):
        # J024: the plan check is gone; the first build step that does not finish (the Figma build) stops the build before any code.
        out = run(UI, ui(stage="build", size="M", risks=["paid-random"]), {"statusLabel": r"B1-figma", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(index(out["labels"], r"B4-build|: RV-"), -1, "no build after an unfinished step")

    def test_a_code_review_that_does_not_finish_is_not_clean(self):
        # J024: CR-candidate-code-r0 → the reviewer slot RV-candidate-r0-reviewer inside the chain.
        out = run(UI, ui(stage="build"), {"statusLabel": r"reviewer: RV-candidate-r0-reviewer", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        dead = run(UI, ui(stage="build"), {"nullLabel": r"reviewer: RV-candidate-r0-reviewer"})
        self.assertEqual(dead["status"], "failed", dead["outcome"])

    def test_a_paid_reveal_gets_the_progression_review_and_a_high_reviewer(self):
        # J024: the progression review is gone; on a paid reveal the qa-lead checks the odds rows and the reviewer runs at high effort.
        out = run(UI, ui(stage="build", size="M", risks=["paid-random"], shop=False), {"dump": r"(reviewer|qa-lead): RV-candidate-r0"})
        self.assertIn("effort: high", brief(out, r"reviewer: RV-candidate-r0"))
        self.assertIn("odds rows equal to the server's data", brief(out, r"qa-lead: RV-candidate-r0"))

    # ------------------------------------------------------------------ J019-LD2: the beat list comes before the first build
    def test_l_proof_runs_the_beat_list_and_plan_check_before_the_prototype(self):
        # J024 (proof and prototype removed on purpose): proof is refused; in L direction the beat list (D1) and the sound and VFX
        # tables come before the merge, all before G1; no prototype runs in any stage.
        proof = run(UI, ui(stage="proof", size="L", shop=True))
        self.assertEqual((proof["status"], proof["agents"]), ("blocked", 0))
        out = run(UI, ui(stage="direction", size="L", shop=True), dict(EFFECTS, timeline=True))
        self.assertEqual(out["status"], "done", out["outcome"])
        sound = span(out, r"sound-designer: N1-needs-sound-designer")
        self.assertTrue(span(out, r"ui-ux-designer: D1-plan")["end"] < sound["start"] and sound["end"] < span(out, r"ui-ux-designer: D3-merge")["start"], out["labels"])
        for stage in STAGES:
            with self.subTest(stage=stage):
                self.assertEqual(index(run(UI, ui(stage=stage, size="L", shop=True), {"affected": ["ui-ux-designer"]})["labels"], r"prototype|storyboard|plan-check"), -1)

    def test_l_build_keeps_the_g2_beat_list_and_runs_no_second_storyboard(self):
        # J024: the beat list is in the merged plan approved at G1 (no G2); build runs no second storyboard and no plan check.
        out = run(UI, ui(stage="build", size="L", shop=True), {"dump": r"B1-figma"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"storyboard"), -1)
        self.assertEqual(index(out["labels"], r"plan-check"), -1)
        self.assertIn("the merged plan approved at G1", out["dumps"][0]["prompt"])
        self.assertIn("motion/storyboard.md", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ J019 follow-up: after a repair the gate runs first
    def test_after_a_repair_the_gate_recheck_runs_before_the_other_reviews(self):
        # J024: the separate gate recheck → the capture-and-scripts run runs the gate first every round; the reviewer reruns only when
        # the repair changed code; a gate or scripts FAIL holds back every review that round.
        code = {"blockLabelOnce": r"ui-ux-designer: RV-candidate-r0", "maker": "ui-ux-designer", "set": {"files": ["src/client/Shop.luau"]}}
        out = run(UI, ui(stage="build"), code)
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        cap = index(labels, r"studio-operator: RV-candidate-r1-capture")
        recheck = index(labels, r"reviewer: RV-candidate-r1-reviewer")
        self.assertGreaterEqual(recheck, 0)
        self.assertLess(cap, recheck)
        self.assertLess(cap, index(labels, r"qa-lead: RV-candidate-r1-"))
        self.assertLess(cap, index(labels, r"ui-ux-designer: RV-candidate-r1-"))
        no_code = run(UI, ui(stage="build"), {"blockLabelOnce": r"ui-ux-designer: RV-candidate-r0", "maker": "ui-ux-designer"})
        self.assertEqual(no_code["status"], "done", no_code["outcome"])
        self.assertEqual(index(no_code["labels"], r"reviewer: RV-candidate-r1-reviewer"), -1, "no code changed: no code recheck")
        self.assertGreaterEqual(index(no_code["labels"], r"qa-lead: RV-candidate-r1-qa-lead"), 0, "the protected suite always reruns")
        held = run(UI, ui(stage="build"), {"blockLabel": r"ui-ux-designer: RV-candidate-r0|studio-operator: RV-candidate-r1-capture", "maker": "feature-builder", "set": code["set"]})
        self.assertEqual(index(held["labels"], r"ui-ux-designer: RV-candidate-r1-"), -1, "a failing gate or script holds back the other reviews that round")
        self.assertEqual(index(held["labels"], r"reviewer: RV-candidate-r1-"), -1)


if __name__ == "__main__":
    unittest.main()
