"""Control-flow tests for the stage job workflow's J019 rows (.agents/workflows/jobs/job-stage.js) with fake agents (no tokens).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg);
revised by J024 test updater · claude-opus-5-5 · default · 2026-10-24 (J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md: no proof
stage and no G2; direction = D1 plan, N1 needs tables, merge; the environment-designer builds the final place once in B1-place; one
capture-and-scripts run; reviewers: the environment-designer always, the art-director with newLook or visual_flags, performance on its risk).
Covers what the shared file (test_job_workflows.py) does not: the `risks` arg, the live-ops event review (risk: event), the key light chosen
in grey inside the one place run (the paint-over, art check-ins and greybox are gone), the floor-material list reaching the sound-designer
before materials are built, and the G1 and G3 results' could-not-check list and owner-confirmed lines.
Recipe: .agents/skills/orchestration/references/job-types.md §3 and "Cross-type rules". Skipped when Node.js is not installed.
"""

from __future__ import annotations

import re
import unittest

try:
    from tools.tests.test_job_workflows import NODE, full, index, run, span
except ImportError:   # unittest discovery with -t tools/tests (tools/verify.py)
    from test_job_workflows import NODE, full, index, run, span

NAME = "job-stage.js"
# J024: no proof stage (design §1); a proof call is refused before any arg check (test_j024_character_stage).
STAGES = ("direction", "build", "repair")
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"


def stage(**changes) -> dict:
    return full(NAME, **changes)


def brief(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dumped brief matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class StageWorkflowTests(unittest.TestCase):
    # ------------------------------------------------------------------ risks arg (README args table)
    def test_risks_missing_or_not_a_list_is_blocked_before_any_agent(self):
        # J024: the proof stage is gone; in the three stages a missing or non-list risks is still named before any agent.
        for st in STAGES:
            for bad in (None, "event", {"event": True}):
                with self.subTest(stage=st, risks=bad):
                    out = run(NAME, stage(stage=st, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])
                    self.assertIn("risks", out["meta"]["whenToUse"], "whenToUse names every required arg")

    def test_an_unknown_risk_token_is_blocked_and_named(self):
        # J024: proof (token named in the refusal) → proof is refused first with the no-proof reason; the other stages still name the token.
        for st in STAGES:
            for token in ("money", "new-enemy", "shop-screen"):
                with self.subTest(stage=st, token=token):
                    out = run(NAME, stage(stage=st, risks=["event", token]))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn(token, out["outcome"])
        proof = run(NAME, stage(stage="proof", risks=["event", "money"]))
        self.assertEqual((proof["status"], proof["agents"], proof["outcome"]), ("blocked", 0, NO_PROOF))

    def test_every_stage_runs_clean_with_the_event_risk(self):
        # J024: proof done → proof is blocked; direction, build and repair stay done with the event risk.
        for st in STAGES:
            with self.subTest(stage=st):
                out = run(NAME, stage(stage=st, risks=["event"]))
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(out["result"]["risks"], ["event"])
        self.assertEqual(run(NAME, stage(stage="proof", risks=["event"]))["status"], "blocked")

    # ------------------------------------------------------------------ (risk: event) live-ops review before G3
    def test_event_adds_one_live_ops_review_after_the_creative_reviews(self):
        # J024: after the game, art, sound and VFX reviews → after the environment-designer's integrated review and the art-director
        # (newLook); the other creative reviewers are removed. skipped_slots keeps the performance line when risks has no performance.
        for st in ("build", "repair"):
            with self.subTest(stage=st):
                extra = {"affected": ["environment-designer"]} if st == "repair" else {}
                plain = run(NAME, stage(stage=st, risks=[], newLook=True), dict(extra, timeline=True))
                event = run(NAME, stage(stage=st, risks=["event"], newLook=True), dict(extra, timeline=True, dump=r"live-ops-designer: RV-"))
                self.assertEqual(plain["status"], "done", plain["outcome"])
                self.assertEqual(event["status"], "done", event["outcome"])
                self.assertEqual(index(plain["labels"], r"^live-ops-designer:"), -1)
                self.assertEqual(event["agents"], plain["agents"] + 1, "one live-ops review in a clean round")
                self.assertTrue(plain["result"]["skipped_slots"], "a skipped risk slot is a line, not a silent gap")
                self.assertEqual(event["result"]["skipped_slots"], ["performance-engineer review (risks has no performance)"])
                lo = span(event, r"^live-ops-designer: RV-\w+-r0-")
                for creative in ("environment-designer", "art-director"):
                    self.assertGreater(lo["start"], span(event, rf"^{creative}: RV-\w+-r0-{creative}")["end"], f"after the {creative} review")
                for removed in ("game-designer", "sound-designer", "vfx-designer", "qa-lead"):
                    self.assertEqual(index(event["labels"], rf"^{removed}: RV-"), -1, f"{removed} no longer reviews")
                text = brief(event, r"live-ops-designer: RV-")
                self.assertIn("model: opus", text)
                self.assertIn("effort: medium", text)
                self.assertIn("E-01 to E-19", text)
                self.assertIn("event-review.md", text)

    def test_event_findings_go_to_makers_inside_the_round_limits(self):
        out = run(NAME, stage(stage="build", risks=["event"]), {"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "environment-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        fix = index(out["labels"], r"FIX-candidate-r0-environment-designer")
        self.assertGreater(fix, index(out["labels"], r"live-ops-designer: RV-candidate-r0"))
        self.assertGreater(index(out["labels"], r"live-ops-designer: RV-candidate-r1"), fix, "the new candidate gets the event review again")
        stuck = run(NAME, stage(stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "environment-designer"})
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])
        self.assertEqual(index(stuck["labels"], r"RV-candidate-r3"), -1, "at most 2 repair rounds")

    def test_event_capture_set_is_asked_for_only_with_the_event_risk(self):
        # J024: PT-candidate-record → the one capture-and-scripts run (CAP-candidate-r0) asks for the event capture set, only with event.
        event = run(NAME, stage(stage="build", risks=["event"]), {"dump": r"CAP-candidate-r0$"})
        plain = run(NAME, stage(stage="build", risks=[]), {"dump": r"CAP-candidate-r0$"})
        self.assertIn("event-review.md §2", brief(event, r"CAP-candidate-r0$"))
        self.assertNotIn("event-review.md", brief(plain, r"CAP-candidate-r0$"))

    # ------------------------------------------------------------------ the one place run (J024 §2: no paint-over, check-ins or greybox)
    def test_paint_over_comes_after_the_rough_art_and_before_set_dressing(self):
        # J024: B1-art-blockout → CI-blockout → AC-paintover → B2-art-production is removed (no roughs, J023-D6/D7): the
        # environment-designer builds the final place once (B1-place: terrain, dressing, light, atmosphere, sky) before anything builds on it.
        out = run(NAME, stage(stage="build", newLook=True), {"timeline": True, "dump": r"B1-place$"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"paintover|blockout|CI-|AC-|art-production"), -1, out["labels"])
        self.assertEqual(sum(1 for x in out["labels"] if x.endswith(": B1-place")), 1, "one place run")
        place = span(out, r"^environment-designer: B1-place$")
        self.assertLess(place["end"], span(out, r"B5-integrate")["start"])
        for item in ("terrain", "atmosphere", "sky", "approved"):
            self.assertIn(item, brief(out, r"B1-place$"))

    def test_a_pending_paint_over_stops_before_set_dressing(self):
        # J024: AC-paintover is removed; a pending image batch stops the build only where later steps build on it (the kit model
        # sheets, B4-kit): nothing is integrated, captured or reviewed on unapproved images.
        out = run(NAME, stage(stage="build"), {"images": "pending", "imagesLabel": r"B4-kit", "set": {"kit_piece_ids": ["rock-a"]}})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertGreaterEqual(index(out["labels"], r"^modeler: B4-kit"), 0)
        self.assertEqual(index(out["labels"], r"B5-integrate|CAP-|RV-"), -1, "nothing is placed or reviewed on an unapproved model sheet")
        self.assertTrue(out["result"]["images_pending"])
        self.assertEqual(index(out["labels"], r"paintover"), -1)

    def test_grey_lighting_variants_are_reviewed_before_the_light_pass(self):
        # J024: B3-light-variants → AC-light-variants → B3-light-atmosphere → one run: B1-place chooses the key light from 2-3
        # directions compared in grey by the numbers (LA-15) and measures the first view before it lights the place.
        out = run(NAME, stage(stage="build"), {"dump": r"B1-place$"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"light-variants|light-atmosphere|AC-"), -1)
        place = brief(out, r"B1-place$")
        for item in ("key light direction from 2-3 compared directions in grey by the numbers", "LA-15", "measure the first view",
                     "look_check.py numbers per direction"):
            self.assertIn(item, place)

    def test_art_check_ins_are_bounded_and_stop_the_light_pass(self):
        # J024: the art check-in loop is removed (absence asserted); the bound moves to the review chain: a finding that never clears
        # stops with needs-decision after 2 repair rounds and nothing is reviewed a third time.
        out = run(NAME, stage(stage="build"), {"blockLabel": r"environment-designer: RV-", "maker": "environment-designer"})
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(index(out["labels"], r"RV-candidate-r3|FIX-candidate-r2"), -1)
        self.assertEqual(index(out["labels"], r"AC-"), -1)

    # ------------------------------------------------------------------ contract: read plan, floor-material list
    def test_floor_material_list_reaches_sound_before_materials_are_built(self):
        # J024: P2-blueprint and P3-needs-r1-sound-designer (M build) → the sound-designer answers the floor-material list in its N1 table
        # in direction, the merge writes it into kit-pieces.md before G1, and the one place run builds its surfaces from it.
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = run(NAME, stage(stage="direction", size=size), {"timeline": True, "dump": r"N1-sound-designer|M-r1-merge"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertIn("floor-material list", brief(out, r"N1-sound-designer"))
                self.assertIn("floor-material list", brief(out, r"M-r1-merge"))
                self.assertLess(span(out, r"N1-sound-designer")["end"], span(out, r"M-r1-merge")["start"])
                b = run(NAME, stage(stage="build", size=size), {"dump": r"B1-place$"})
                self.assertEqual(b["status"], "done", b["outcome"])
                self.assertIn("Surface materials come from the floor-material list", brief(b, r"B1-place$"))
                self.assertEqual(index(b["labels"], r"needs-r|N1-"), -1, "build never re-asks")

    def test_a_material_off_the_list_goes_to_sound_who_may_refuse_it(self):
        out = run(NAME, stage(stage="build"), {"set": {"new_surface_materials": ["wet moss"]}, "refuseSign": True, "dump": r"B1-materials"})
        self.assertIn("not on the floor-material list", brief(out, r"B1-materials"))
        self.assertGreater(index(out["labels"], r"B1-swap-materials"), index(out["labels"], r"B1-materials"), "a refused material is swapped")

    def test_read_plan_is_built_on_the_route_table_and_the_art_bible(self):
        # J024: P1-route-graph and P2-blueprint (proof) → the game-designer's N1 table brings the route table, hazard sheets and read rank;
        # the merge writes read-plan.md on them and the art bible (value bands; the bible's locks and colour roles in its refs).
        out = run(NAME, stage(stage="direction"), {"dump": r"N1-game-designer|M-r1-merge"})
        self.assertEqual(out["status"], "done", out["outcome"])
        route = brief(out, r"N1-game-designer")
        for item in ("route table", "hazard sheet", "read rank"):
            self.assertIn(item, route)
        plan = brief(out, r"M-r1-merge")
        for item in ("read-plan.md", "route table", "hazard sheets", "read rank", "value bands", "knowledge/design/art-bible.md"):
            self.assertIn(item, plan)

    # ------------------------------------------------------------------ the grey value pass moved into the place run (J024 §2)
    def test_greybox_runs_the_grey_value_pass(self):
        # J024: P4-greybox and its proof review → no greybox (absence); the grey comparison of key light directions and the first-view
        # measure run inside B1-place, and the job lead's integrated review measures the first view again on the final captures (J015).
        out = run(NAME, stage(stage="build"), {"dump": r"B1-place$|environment-designer: RV-candidate-r0"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"greybox|PR-r|PT-"), -1)
        place = brief(out, r"B1-place$")
        self.assertIn("in grey", place)
        self.assertIn("key light direction", place)
        self.assertIn("first view", place)
        review = brief(out, r"environment-designer: RV-candidate-r0")
        self.assertIn("look_check.py", review)
        self.assertIn("first view", review)

    # ------------------------------------------------------------------ G1 shows; gate packets (cross-type rules)
    def test_direction_brings_layouts_route_table_and_hazard_sheets(self):
        # J024: game-designer D1 proposal + D3-synthesis → the environment-designer's D1 plan brings the 2-3 options with route sketches;
        # the game-designer's N1 table the route table and hazard sheets.
        out = run(NAME, stage(stage="direction"), {"dump": r"D1-plan|N1-game-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(out["labels"][0], "environment-designer: D1-plan")
        lead = brief(out, r"D1-plan")
        for item in ("2-3 options at equal finish", "top-down route sketch", "may return only if", "failed_options"):
            self.assertIn(item, lead)
        needs = brief(out, r"N1-game-designer")
        for item in ("route table", "hazard sheet"):
            self.assertIn(item, needs)
        self.assertIn("could_not_check", out["result"]["g1"])

    def test_gate_results_carry_could_not_check_and_owner_lines(self):
        # J024: the proof result is gone (proof is blocked); G1 and the build and repair results keep their lines.
        g1 = run(NAME, stage(stage="direction"))["result"]["g1"]
        for key in ("layouts", "failed_options", "closed_doors", "could_not_check", "owner_confirms"):
            self.assertIn(key, g1)
        for st in ("build", "repair"):
            with self.subTest(stage=st):
                res = run(NAME, stage(stage=st), {"affected": ["environment-designer"]})["result"]
                self.assertIn("could_not_check", res)
                lines = " ".join(res["owner_confirms"])
                self.assertIn("normal speed", lines)
                self.assertIn("phone speaker", lines)
                self.assertIn("headphones", lines)
        self.assertEqual(run(NAME, stage(stage="proof"))["status"], "blocked")

    # ------------------------------------------------------------------ review order slots
    def test_art_and_qa_slots_name_their_captures_and_checks(self):
        # J024: the qa-lead is removed from the stage chain; its checks (jump height, scene audit, graphics quality, spawns) are in the
        # capture-and-scripts run; the art-director runs only with newLook (or visual_flags) and keeps its look checks and named captures.
        out = run(NAME, stage(stage="build", newLook=True), {"dump": r"art-director: RV-candidate-r0|CAP-candidate-r0$"})
        art = brief(out, r"art-director: RV-candidate-r0")
        for item in ("layer cuts", "environment-only", "lowest-graphics", "mask capture", "environment band", "reserved colours", "focus numbers"):
            self.assertIn(item, art)
        rec = brief(out, r"CAP-candidate-r0$")
        for item in ("environment-only", "mask capture", "head-height"):
            self.assertIn(item, rec)
        for item in ("jump height", "scene_audit.py", "lowest and highest graphics", "spawn positions and facing"):
            self.assertIn(item, rec)
        self.assertEqual(index(out["labels"], r"^qa-lead:"), -1)
        plain = run(NAME, stage(stage="build"), {"dump": r"CAP-candidate-r0$"})
        self.assertEqual(index(plain["labels"], r"^art-director:"), -1, "no art review without newLook or visual_flags")
        self.assertNotIn("mask capture", brief(plain, r"CAP-candidate-r0$"), "the art captures are asked for only when the art-director reviews")


    # ------------------------------------------------------------------ J019 lead review
    def test_a_script_fail_holds_back_the_other_reviews_that_round(self):
        # J024: RV-candidate-r0-scripts + game-designer review → the scripts run inside CAP-candidate-r0; a FAIL there holds back every
        # RV-candidate-r0 review; the job lead's integrated review runs on the repaired candidate in round 1.
        out = run(NAME, stage(stage="build", risks=[]), {"blockLabelOnce": r"CAP-candidate-r0$", "maker": "environment-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r": RV-candidate-r0-"), -1, "no review while a script FAIL is open")
        self.assertGreater(index(out["labels"], r"environment-designer: RV-candidate-r1-"), index(out["labels"], r"FIX-candidate-r0-environment-designer"))

    def test_a_live_ops_finding_with_itself_as_maker_goes_to_the_lead(self):
        out = run(NAME, stage(stage="build", risks=["event"]), {"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "live-ops-designer"})
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(index(out["labels"], r"FIX-candidate-r0-live-ops-designer"), -1)

    def test_steps_that_do_not_finish_stop_the_stage(self):
        # J024: RV-candidate-r0-scripts, PT-candidate-record and PR-r0-game-designer are removed → the steps that hold those places now:
        # the capture-and-scripts run, the place run, the integrator's freeze, the integrated review and the merge in direction.
        for st, label in (("build", r"CAP-candidate-r0$"), ("build", r"B1-place$"), ("build", r"B5-integrate$"),
                          ("build", r"environment-designer: RV-candidate-r0-environment-designer"), ("direction", r"M-r1-merge$")):
            with self.subTest(label=label):
                out = run(NAME, stage(stage=st, risks=[]), {"statusLabel": label, "status": "blocked"})
                self.assertNotEqual(out["status"], "done", out["outcome"])
                self.assertGreaterEqual(index(out["labels"], label), 0, "the pattern names a real step")


if __name__ == "__main__":
    unittest.main()
