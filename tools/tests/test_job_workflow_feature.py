"""Feature workflow tests (.agents/workflows/jobs/job-feature.js) for the recipe rows of b2eeb73 and the risks arg, with fake agents.

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: the feature workflow runs the
recipe rows of orchestration/references/job-types.md §5 and the cross-type rules); revised by J024 test updater ·
claude-opus-5-5 · default · 2026-10-24 (J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md: no proof, needs tables before G1, each craft
once, fewer reviewers). Uses the helpers of test_job_workflows; skipped when Node.js is not installed.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run, span

NAME = "job-feature.js"
ALL_RISKS = ["saves", "remotes", "trades", "paid-random", "server-result", "rewards", "event", "performance"]   # J024 §7: + performance
CODE_RISKS = ("saves", "remotes", "trades", "paid-random")
NOT_VERIFIED = {"set": {"checks": [{"id": "C1", "result": "not verified", "evidence": "no second client"}]}}
# J024: the crafts are switched by the contract's presentation list (a D1, merge and B1-acceptance field), default [] in the fakes.
CRAFTS = ["animator", "ui-ux-designer", "vfx-designer", "sound-designer"]
ALL_CRAFTS = {"set": {"presentation": CRAFTS}}


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
        # J024: STAGES lost proof; `stage: "proof"` is refused first, before the risks check, with the no-proof reason.
        for stage in STAGES + ("proof",):
            for bad in (None, "saves", {"saves": True}):
                with self.subTest(stage=stage, risks=bad):
                    out = feat(stage, risks=bad)
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("no proof stage (J024)" if stage == "proof" else "risks", out["outcome"])

    def test_an_unknown_risk_token_is_blocked(self):
        for token in ("new-enemy", "money", "shop-screen"):
            with self.subTest(token=token):
                out = feat("build", risks=["saves", token])
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(token, out["outcome"])

    def test_every_stage_runs_clean_with_every_risk(self):
        # J024: no proof stage (M and L run the same stages); the token list adds performance, so every slot still runs.
        for stage in STAGES:
            for size in ("M", "L"):
                for scen in ({}, {"uniform": True}, {"conflicts": True, "refuseSign": True}, dict(ALL_CRAFTS)):
                    with self.subTest(stage=stage, size=size, scenario=scen):
                        out = feat(stage, scen, size=size, risks=ALL_RISKS)
                        self.assertDone(out)
                        self.assertLessEqual(out["maxConcurrent"], 5)
                        self.assertEqual(out["result"]["skipped_slots"], [])

    # ------------------------------------------------------------------ direction: plan, tables, merge, closed doors
    def test_direction_is_one_proposal_and_limits_sheets_then_one_sheet(self):
        # J024: D1 proposal + limits sheets + D3 synthesis → one D1 plan, the N1 limits tables against it, one D3 merge after every table.
        out = feat("direction", {"timeline": True, "dump": r"D1-plan|D3-merge"})
        self.assertDone(out)
        self.assertEqual(out["labels"][0], "game-designer: D1-plan")
        merge = span(out, r"^game-designer: D3-merge$")
        for table in (r"^architect: N1-limits-architect$", r"^progression-designer: N1-limits-progression-designer$"):
            with self.subTest(table=table):
                self.assertGreater(merge["start"], span(out, table)["end"], "the merge reads every limits table")
        self.assertRegex(out["labels"][-1], r"D3-merge$", "nothing runs after the merge")
        self.assertEqual(index(out["labels"], r"D2-|D3-sign-|D3-consult-|D3-resolution|D3-synthesis"), -1)
        self.assertEqual(index(out["labels"], r"^(animator|sound-designer|ui-ux-designer|vfx-designer):"), -1, "crafts join only when the presentation list names them")
        plan = brief(out, r"D1-plan")
        self.assertIn("feedback stack per action", plan)
        self.assertIn("failed a check", plan)
        self.assertIn("may return only if", brief(out, r"D3-merge"))

    def test_the_needs_meeting_follows_the_contract_crafts(self):
        # J024: the proof's needs meeting → N1 needs tables in direction, one per craft the D1 presentation list names.
        all_crafts = feat("direction", ALL_CRAFTS)
        self.assertDone(all_crafts)
        for role in CRAFTS:
            self.assertGreaterEqual(index(all_crafts["labels"], rf"^{role}: N1-needs-{role}$"), 0, role)
        quiet = feat("direction", {"set": {"presentation": ["animator", "ui-ux-designer", "vfx-designer"]}})
        self.assertDone(quiet)
        self.assertEqual(index(quiet["labels"], r"^sound-designer:"), -1)
        self.assertGreaterEqual(index(quiet["labels"], r"^animator: N1-needs-animator$"), 0)

    def test_a_limits_conflict_is_resolved_in_the_direction_sheet(self):
        # J024: D3-synthesis → the D3 merge settles every conflict it owns in direction.md (owner and resolution); no exchange round
        # without a reported conflict; each craft confirms the merged plan in its first build hand-back (PLAN-CONFIRM).
        out = feat("direction", {"set": {"conflicts": [{"about": "the hit window", "why": "too short to read", "needs": "6 frames"}]},
                                 "dump": r"D3-merge"})
        self.assertDone(out)
        self.assertEqual(index(out["labels"], r"D2-|D3-resolution|D3-sign-|: N2-"), -1)
        self.assertRegex(out["labels"][-1], r"^game-designer: D3-merge$")
        merge = brief(out, r"D3-merge")
        self.assertIn("each conflict with its owner and resolution", merge)
        self.assertIn("settle every conflict inside your authority", merge)
        build = feat("build", {"dump": r"^(qa-lead|feature-builder): B"})
        for d in build["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn("PLAN-CONFIRM", d["prompt"])

    # ------------------------------------------------------------------ contract time: tier table, trace table, needs round
    def test_rewards_put_the_tier_table_in_the_contract_before_production(self):
        # J024: P1-tiers → the progression-designer's N1 limits table writes the tier table in direction (before G1); the merge and
        # every build craft read it; M and L the same.
        for size in ("M", "L"):
            with self.subTest(size=size):
                dirn = feat("direction", {"dump": r"N1-limits-progression|D3-merge"}, size=size, numbers=False, risks=["rewards"])
                self.assertDone(dirn)
                self.assertLess(index(dirn["labels"], r"^progression-designer: N1-limits-progression-designer$"), index(dirn["labels"], r"D3-merge"))
                self.assertIn("tier-table.md", brief(dirn, r"N1-limits-progression"))
                self.assertIn("tier-table.md", brief(dirn, r"D3-merge"))
                out = feat("build", dict(ALL_CRAFTS, dump=r"B1-acceptance|B3-ui|B5-vfx|B6-sound"), size=size, risks=["rewards"])
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"P1-tiers"), -1)
                for pat in (r"^qa-lead: B1-acceptance$", r"^ui-ux-designer: B3-ui$", r"^vfx-designer: B5-vfx$", r"^sound-designer: B6-sound$"):
                    with self.subTest(size=size, step=pat):
                        self.assertIn("tier-table.md", brief(out, pat))
        none = feat("build", size="M")
        self.assertEqual(index(none["labels"], r"tiers"), -1)
        self.assertTrue(any("tier table" in s for s in none["result"]["skipped_slots"]))

    def test_trace_table_is_written_at_contract_time(self):
        # J024: P1-trace → the qa-lead writes the trace table with the protected tests in B1-acceptance, the first build run, from the
        # merged contract; the builder reads it.
        out = feat("build", {"dump": r"B7-build$|B1-acceptance"}, size="M")
        self.assertDone(out)
        self.assertEqual(out["labels"][0], "qa-lead: B1-acceptance")
        self.assertIn("trace table", brief(out, r"B1-acceptance"))
        self.assertIn("the merged contract approved at G1", brief(out, r"B1-acceptance"))
        self.assertIn("trace-table.md", brief(out, r"B7-build$"))

    def test_crafts_state_needs_before_the_plan_is_frozen(self):
        # J024: the proof meeting → every listed craft writes its N1 needs table before the merge freezes contract rev 2; the
        # architect's limits table holds the one marker list; in build VFX keys to the animator's markers and sound to the VFX frames.
        out = feat("direction", dict(ALL_CRAFTS, timeline=True, dump=r"N1-limits-architect"), size="M")
        self.assertDone(out)
        merge = span(out, r"^game-designer: D3-merge$")
        for role in CRAFTS:
            with self.subTest(role=role):
                self.assertGreater(merge["start"], span(out, rf"^{role}: N1-needs-{role}$")["end"], "the merge comes after every table")
        self.assertIn("one marker list where animation, VFX and sound meet", brief(out, r"N1-limits-architect"))
        built = feat("build", dict(ALL_CRAFTS, dump=r"B5-vfx|B6-sound|B7-build"), size="M")
        self.assertDone(built)
        self.assertIn("the animator's marker frames", brief(built, r"B5-vfx"))
        self.assertIn("keyed to the vfx-designer's frame scripts", brief(built, r"B6-sound"))
        self.assertIn("presentation contract", brief(built, r"B7-build"))
        for d in built["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn("knowledge/jobs/J099-test/architect/plan.md", d["prompt"], "every build brief reads the merged plan")

    def test_needs_rounds_are_at_most_two(self):
        # J024: one needs round (N1), a second (N2) only on a conflict the merge reports, one more merge, then needs-decision.
        out = feat("direction", {"set": {"open_conflicts": [{"about": "N1-row-2", "roles": ["architect"], "why": "w"}]}})
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        n2 = index(out["labels"], r": N2-")
        self.assertTrue(0 <= index(out["labels"], r"D3-merge$") < n2 < index(out["labels"], r"D3-merge-n2$"), out["labels"])
        self.assertEqual(len([x for x in out["labels"] if "D3-merge" in x]), 2, "the job lead merges at most twice")
        self.assertEqual(index(out["labels"], r"N3-|-r3|merge-n3"), -1)
        clean = feat("direction", {"conflicts": True})
        self.assertDone(clean)
        self.assertEqual(index(clean["labels"], r": N2-|D3-merge-n2"), -1, "no open conflict: one round, one merge")

    def test_no_motion_means_no_animator(self):
        # J024: crafts_not_needed → the animator runs only when the presentation list names it (direction N1 and build B4).
        others = {"set": {"presentation": ["ui-ux-designer", "vfx-designer", "sound-designer"]}}
        for stage in ("direction", "build"):
            with self.subTest(stage=stage):
                out = feat(stage, others)
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"^animator:"), -1)

    # ------------------------------------------------------------------ no prototype: each craft builds once
    def test_prototype_is_the_skeleton_with_temp_cues(self):
        # J024 (removed on purpose, design §2): no prototype, stand-ins or temp cues in any stage; the build makes the real thing once.
        for stage in STAGES:
            with self.subTest(stage=stage):
                out = feat(stage, ALL_CRAFTS)
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"P3-|prototype|temp-cues|stand-in"), -1)
        built = feat("build", dict(ALL_CRAFTS, dump=r"B6-sound|B7-build"))
        self.assertNotIn("temp cues", brief(built, r"B7-build"))
        self.assertNotIn("named stand-ins", brief(built, r"B7-build"))
        self.assertIn("the final sounds, once", brief(built, r"B6-sound"))

    # ------------------------------------------------------------------ build: acceptance tests, crafts, one build-and-integrate run
    def test_plan_check_runs_only_with_money_or_a_code_risk(self):
        # J024 (removed on purpose, design §2 / builder C): no plan check runs for any money or code risk; the architect's N1 limits
        # table is the plan and the reviewer reviews the code in every round 0, at high effort with money or a code risk.
        for money, risks in [(True, [])] + [(False, [r]) for r in CODE_RISKS] + [(False, []), (False, ["rewards", "server-result", "event"])]:
            with self.subTest(money=money, risks=risks):
                out = feat("build", {"dump": r"^reviewer: RV-candidate-r0"}, money=money, risks=risks)
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"plan-check|B1-plan"), -1)
                self.assertFalse(any("plan check" in s for s in out["result"]["skipped_slots"]), "no plan-check slot exists to skip")
                high = money or any(r in CODE_RISKS for r in risks)
                self.assertIn("effort: high" if high else "effort: medium", brief(out, r"^reviewer: RV-"))

    def test_plan_check_findings_get_one_architect_answer(self):
        # J024: the plan check and its architect answer are gone; a finding on the plan routes to the architect once (a capped FIX),
        # and the builder re-wires before the next capture.
        out = feat("build", {"blockLabelOnce": r"^reviewer: RV-candidate-r0", "maker": "architect"})
        self.assertDone(out)
        self.assertEqual(sum(1 for x in out["labels"] if x == "architect: FIX-candidate-r0-architect"), 1, "one answer")
        fix = index(out["labels"], r"^architect: FIX-candidate-r0-architect$")
        self.assertTrue(fix < index(out["labels"], r"^feature-builder: FIX-candidate-r0-feature-builder$") < index(out["labels"], r"RV-candidate-r1-capture"), out["labels"])
        self.assertEqual(index(feat("build")["labels"], r"^architect:"), -1)

    def test_skeleton_comes_before_the_presentation_pass(self):
        # J024: skeleton then crafts → the qa-lead's protected tests first; then the crafts (animator → VFX → sound, UI, tables); then one
        # build-and-integrate run after every craft.
        out = feat("build", dict(ALL_CRAFTS, timeline=True))
        self.assertDone(out)
        tests = span(out, r"^qa-lead: B1-acceptance$")
        ends = []
        for pat in (r"B2-tables", r"B3-ui", r"B4-animation", r"B5-vfx", r"B6-sound"):
            with self.subTest(step=pat):
                self.assertGreater(span(out, pat)["start"], tests["end"], "protected tests before anything is built")
                ends.append(span(out, pat)["end"])
        self.assertGreater(span(out, r"B5-vfx")["start"], span(out, r"B4-animation")["end"])
        self.assertGreater(span(out, r"B6-sound")["start"], span(out, r"B5-vfx")["end"])
        self.assertGreater(span(out, r"^feature-builder: B7-build$")["start"], max(ends))

    def test_integration_delivers_hooks_first_and_runs_the_worst_case_pass(self):
        # J024: B7-integrate → B7-build builds and integrates in one run: the hooks before the wiring, the run before the first capture.
        out = feat("build", {"dump": r"B7-build"})
        text = brief(out, r"B7-build")
        for phrase in ("test hooks", "debug log", "presentation.md §9", "worst-case pass"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, text)
        self.assertLess(text.index("test hooks"), text.index("wire everything"))
        self.assertLess(text.index("wire everything"), text.index("worst-case pass"))
        self.assertLess(index(out["labels"], r"B7-build"), index(out["labels"], r"^studio-operator: RV-candidate-r0-capture$"), "hooks exist before any capture")

    # ------------------------------------------------------------------ review chain
    def test_review_chain_runs_the_architect_beside_the_technical_checks(self):
        # J024 (removed on purpose, design §4.4): the architect no longer reviews; its placement and engine-gate checks are in the
        # reviewer's code review, which starts beside the other round-0 reviews right after the capture.
        for money, risks in ((True, ["saves"]), (False, [])):
            with self.subTest(money=money, risks=risks):
                out = feat("build", {"timeline": True, "dump": r"reviewer: RV-"}, money=money, risks=risks)
                self.assertDone(out)
                self.assertEqual(index(out["labels"], r"^architect:"), -1)
                code = span(out, r"^reviewer: RV-candidate-r0-reviewer$")
                self.assertGreater(code["start"], span(out, r"^studio-operator: RV-candidate-r0-capture$")["end"])
                self.assertLess(code["start"], span(out, r"^game-designer: RV-candidate-r0-game-designer$")["end"], "beside the integrated review, not after it")
                text = brief(out, r"reviewer: RV-")
                self.assertIn("placement and replication", text)
                self.assertIn("engine-gate answers", text)

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
        # J024: the art-director reviews only on visual_flags, so the creative order is the game-designer's integrated review (and the
        # art-director when flags exist); the live-ops review still runs after it (README per-type tests; design §4 "unchanged").
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = feat(stage, {"timeline": True, "dump": r"live-ops-designer: RV-|studio-operator: RV-", "affected": ["vfx-designer"]}, risks=["event"])
                self.assertDone(out)
                live = span(out, r"^live-ops-designer: RV-\w+-r0-live-ops-designer$")
                text = brief(out, r"live-ops-designer: RV-")
                self.assertIn("E-01 to E-19", text)
                self.assertIn("event-review.md §2-§3", text)
                self.assertIn("model: opus", text)
                self.assertIn("effort: medium", text)
                self.assertIn("event-review.md §2", brief(out, r"studio-operator: RV-"))
                plain = feat(stage, {"affected": ["vfx-designer"]})
                self.assertEqual(index(plain["labels"], r"live-ops-designer"), -1)
                self.assertGreater(live["start"], span(out, r"^game-designer: RV-\w+-r0-")["end"])
        flagged = feat("build", {"timeline": True, "set": {"visual_flags": ["x"]}}, risks=["event"])
        self.assertDone(flagged)
        self.assertGreater(span(flagged, r"^live-ops-designer: RV-candidate-r0")["start"], span(flagged, r"^art-director: RV-candidate-r0-")["end"])

    def test_live_ops_findings_route_to_makers_inside_the_round_limits(self):
        out = feat("build", {"blockLabelOnce": r"^live-ops-designer: RV-candidate-r0", "maker": "ui-ux-designer"}, risks=["event"])
        self.assertDone(out)
        self.assertGreaterEqual(index(out["labels"], r"^ui-ux-designer: FIX-candidate-r0-ui-ux-designer$"), 0)
        self.assertGreaterEqual(index(out["labels"], r"^live-ops-designer: RV-candidate-r1-"), 0)
        stuck = feat("build", {"blockLabel": r"^live-ops-designer: RV-", "maker": "ui-ux-designer"}, risks=["event"])
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])

    # ------------------------------------------------------------------ gate packets (cross-type rules)
    def test_gate_results_carry_could_not_check_and_owner_lines(self):
        # J024: no proof result and no G2 (proof is blocked); nothing plays before G3, so G1 has no owner-confirmed line; G3 keeps them.
        g1 = feat("direction", NOT_VERIFIED)
        self.assertDone(g1)
        self.assertTrue(g1["result"]["g1"]["could_not_check"])
        self.assertEqual(g1["result"]["g1"]["owner_confirmed"], [], "nothing plays before G3")
        g2 = feat("proof", NOT_VERIFIED)
        self.assertEqual((g2["status"], g2["agents"]), ("blocked", 0))
        sound = {"set": dict(NOT_VERIFIED["set"], presentation=["sound-designer"]), "affected": ["sound-designer"]}
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                g3 = feat(stage, sound)
                self.assertDone(g3)
                self.assertTrue(g3["result"]["could_not_check"])
                lines = g3["result"]["owner_confirmed"]
                self.assertTrue(any("feel at normal speed" in x for x in lines))
                self.assertTrue(any("two listens" in x and "phone speaker" in x and "headphones" in x for x in lines))
        silent = feat("build")
        self.assertDone(silent)
        self.assertTrue(any("feel at normal speed" in x for x in silent["result"]["owner_confirmed"]))
        self.assertFalse(any("two listens" in x for x in silent["result"]["owner_confirmed"]), "no sound in the presentation list: no listening line")


    # ------------------------------------------------------------------ J019 lead review: reviewer effort follows the code risks
    def test_reviewer_and_builder_run_high_for_code_risks_without_money(self):
        for risk in CODE_RISKS:
            with self.subTest(risk=risk):
                out = feat("build", {"dump": r"(reviewer|feature-builder): "}, risks=[risk], money=False)
                self.assertTrue(out["dumps"])
                self.assertTrue(all("effort: high" in d["prompt"] for d in out["dumps"]), [d["label"] for d in out["dumps"]])
        low = feat("build", {"dump": r"reviewer: RV-"}, risks=[], money=False)
        self.assertTrue(all("effort: medium" in d["prompt"] for d in low["dumps"]))

    # ------------------------------------------------------------------ J019 follow-up: a wide repair never starts more than 5 agents at once
    def test_a_repair_touching_many_crafts_stays_at_five_agents(self):
        roles = ["progression-designer", "architect", "qa-lead", "animator", "ui-ux-designer", "vfx-designer", "sound-designer", "game-designer", "feature-builder"]
        out = feat("repair", {"affected": roles}, risks=[])
        self.assertDone(out)
        self.assertLessEqual(out["maxConcurrent"], 5)
        self.assertFalse(out.get("violation"))


if __name__ == "__main__":
    unittest.main()
