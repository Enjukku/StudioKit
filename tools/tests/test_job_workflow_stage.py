"""Control-flow tests for the stage job workflow's J019 rows (.agents/workflows/jobs/job-stage.js) with fake agents (no tokens).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg).
Covers what the shared file (test_job_workflows.py) does not: the `risks` arg, the live-ops event review (risk: event), the art-director's
paint-over before set dressing and grey lighting variants before the light pass, the floor-material list reaching the sound-designer before
materials are built, the grey value pass in the proof, and the G1 and G3 results' could-not-check list and owner-confirmed lines.
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
STAGES = ("direction", "proof", "build", "repair")


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
        for st in STAGES:
            for bad in (None, "event", {"event": True}):
                with self.subTest(stage=st, risks=bad):
                    out = run(NAME, stage(stage=st, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])
                    self.assertIn("risks", out["meta"]["whenToUse"], "whenToUse names every required arg")

    def test_an_unknown_risk_token_is_blocked_and_named(self):
        for st in STAGES:
            for token in ("money", "new-enemy", "shop-screen"):
                with self.subTest(stage=st, token=token):
                    out = run(NAME, stage(stage=st, risks=["event", token]))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn(token, out["outcome"])

    def test_every_stage_runs_clean_with_the_event_risk(self):
        for st in STAGES:
            with self.subTest(stage=st):
                out = run(NAME, stage(stage=st, risks=["event"]))
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(out["result"]["risks"], ["event"])

    # ------------------------------------------------------------------ (risk: event) live-ops review before G3
    def test_event_adds_one_live_ops_review_after_the_creative_reviews(self):
        for st in ("build", "repair"):
            with self.subTest(stage=st):
                extra = {"affected": ["environment-designer"]} if st == "repair" else {}
                plain = run(NAME, stage(stage=st, risks=[]), dict(extra, timeline=True))
                event = run(NAME, stage(stage=st, risks=["event"]), dict(extra, timeline=True, dump=r"live-ops-designer: RV-"))
                self.assertEqual(plain["status"], "done", plain["outcome"])
                self.assertEqual(event["status"], "done", event["outcome"])
                self.assertEqual(index(plain["labels"], r"^live-ops-designer:"), -1)
                self.assertEqual(event["agents"], plain["agents"] + 1, "one live-ops review in a clean round")
                self.assertTrue(plain["result"]["risk_slots_skipped"], "a skipped risk slot is a line, not a silent gap")
                self.assertEqual(event["result"]["risk_slots_skipped"], [])
                lo = span(event, r"^live-ops-designer: RV-\w+-r0-")
                for creative in ("game-designer", "art-director", "sound-designer", "vfx-designer"):
                    self.assertGreater(lo["start"], span(event, rf"^{creative}: RV-\w+-r0-{creative}")["end"], f"after the {creative} review")
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
        event = run(NAME, stage(stage="build", risks=["event"]), {"dump": r"PT-candidate-record"})
        plain = run(NAME, stage(stage="build", risks=[]), {"dump": r"PT-candidate-record"})
        self.assertIn("event-review.md §2", brief(event, r"PT-candidate-record"))
        self.assertNotIn("event-review.md", brief(plain, r"PT-candidate-record"))

    # ------------------------------------------------------------------ check-ins (recipe §3)
    def test_paint_over_comes_after_the_rough_art_and_before_set_dressing(self):
        out = run(NAME, stage(stage="build"), {"timeline": True, "dump": r"B2-art-production"})
        self.assertEqual(out["status"], "done", out["outcome"])
        paint = span(out, r"^art-director: AC-paintover-r0")
        self.assertGreater(paint["start"], span(out, r"B1-art-blockout")["end"])
        self.assertGreater(paint["start"], span(out, r"CI-blockout-r0-game-designer")["end"])
        self.assertLess(paint["end"], span(out, r"B2-art-production")["start"])
        self.assertIn("paint-over", brief(out, r"B2-art-production"))

    def test_a_pending_paint_over_stops_before_set_dressing(self):
        out = run(NAME, stage(stage="build"), {"images": "pending"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertGreaterEqual(index(out["labels"], r"AC-paintover-r0"), 0)
        self.assertEqual(index(out["labels"], r"B2-art-production"), -1, "nothing is dressed on an unapproved paint-over")
        self.assertTrue(out["result"]["images_pending"])

    def test_grey_lighting_variants_are_reviewed_before_the_light_pass(self):
        out = run(NAME, stage(stage="build"), {"timeline": True, "dump": r"B3-light-variants|AC-light-variants"})
        self.assertEqual(out["status"], "done", out["outcome"])
        variants = span(out, r"B3-light-variants")
        review = span(out, r"^art-director: AC-light-variants-r0")
        light = span(out, r"B3-light-atmosphere")
        self.assertGreater(variants["start"], span(out, r"CI-art-r0-game-designer")["end"], "variants on the dressed place")
        self.assertGreater(review["start"], variants["end"])
        self.assertLess(review["end"], light["start"])
        self.assertIn("2-3 lighting variants", brief(out, r"B3-light-variants"))
        self.assertIn("game camera", brief(out, r"AC-light-variants"))

    def test_art_check_ins_are_bounded_and_stop_the_light_pass(self):
        out = run(NAME, stage(stage="build"), {"blockLabel": r"art-director: AC-light-variants", "maker": "environment-designer"})
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(index(out["labels"], r"AC-light-variants-r3"), -1)
        self.assertEqual(index(out["labels"], r"B3-light-atmosphere"), -1)

    # ------------------------------------------------------------------ contract: read plan, floor-material list
    def test_floor_material_list_reaches_sound_before_materials_are_built(self):
        out = run(NAME, stage(stage="build", size="M"), {"timeline": True, "dump": r"P2-blueprint|P3-needs-r1-sound-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertIn("floor-material list", brief(out, r"P2-blueprint"))
        self.assertIn("floor-material list", brief(out, r"P3-needs-r1-sound-designer"))
        sound = span(out, r"P3-needs-r1-sound-designer")
        for maker in (r"P4-greybox", r"B1-art-blockout", r"B2-art-production"):
            self.assertLess(sound["end"], span(out, maker)["start"], f"sound reads the list before {maker}")

    def test_a_material_off_the_list_goes_to_sound_who_may_refuse_it(self):
        out = run(NAME, stage(stage="build"), {"set": {"new_surface_materials": ["wet moss"]}, "refuseSign": True, "dump": r"B1-materials"})
        self.assertIn("not on the floor-material list", brief(out, r"B1-materials"))
        self.assertGreater(index(out["labels"], r"B1-swap-materials"), index(out["labels"], r"B1-materials"), "a refused material is swapped")

    def test_read_plan_is_built_on_the_route_table_and_the_art_bible(self):
        out = run(NAME, stage(stage="proof"), {"dump": r"P1-route-graph|P2-blueprint"})
        self.assertEqual(out["status"], "done", out["outcome"])
        route = brief(out, r"P1-route-graph")
        for item in ("route table", "hazard sheet", "read rank"):
            self.assertIn(item, route)
        plan = brief(out, r"P2-blueprint")
        for item in ("read-plan.md", "route table", "hazard sheets", "read rank", "value bands", "reserved colours"):
            self.assertIn(item, plan)

    # ------------------------------------------------------------------ proof: grey value pass (G2)
    def test_greybox_runs_the_grey_value_pass(self):
        out = run(NAME, stage(stage="proof"), {"dump": r"P4-greybox|art-director: PR-r0"})
        self.assertEqual(out["status"], "done", out["outcome"])
        grey = brief(out, r"P4-greybox")
        self.assertIn("grey value pass", grey)
        self.assertIn("key light direction", grey)
        self.assertIn("first view", grey)
        self.assertIn("grey value pass", brief(out, r"art-director: PR-r0"))
        self.assertIn("grey value pass", out["outcome"])

    # ------------------------------------------------------------------ G1 shows; gate packets (cross-type rules)
    def test_direction_brings_layouts_route_table_and_hazard_sheets(self):
        out = run(NAME, stage(stage="direction"), {"dump": r"game-designer: D1-|D3-synthesis"})
        self.assertEqual(out["status"], "done", out["outcome"])
        lead = brief(out, r"game-designer: D1-")
        for item in ("route table", "hazard sheets", "2-3 layout options", "top-down route sketches"):
            self.assertIn(item, lead)
        synth = brief(out, r"D3-synthesis")
        for item in ("may return only if", "failed_options", "could_not_check", "equal finish"):
            self.assertIn(item, synth)

    def test_gate_results_carry_could_not_check_and_owner_lines(self):
        g1 = run(NAME, stage(stage="direction"))["result"]["g1"]
        for key in ("layouts", "failed_options", "closed_doors", "could_not_check", "owner_confirms"):
            self.assertIn(key, g1)
        for st in ("proof", "build", "repair"):
            with self.subTest(stage=st):
                res = run(NAME, stage(stage=st), {"affected": ["environment-designer"]})["result"]
                self.assertIn("could_not_check", res)
                lines = " ".join(res["owner_confirms"])
                self.assertIn("normal speed", lines)
                self.assertIn("phone speaker", lines)
                self.assertIn("headphones", lines)

    # ------------------------------------------------------------------ review order slots
    def test_art_and_qa_slots_name_their_captures_and_checks(self):
        out = run(NAME, stage(stage="build"), {"dump": r"(art-director|qa-lead): RV-candidate-r0|PT-candidate-record"})
        art = brief(out, r"art-director: RV-candidate-r0")
        for item in ("layer cuts", "environment-only", "lowest-graphics", "mask capture", "environment band", "reserved colours", "focus numbers"):
            self.assertIn(item, art)
        rec = brief(out, r"PT-candidate-record")
        for item in ("environment-only", "mask capture", "head-height"):
            self.assertIn(item, rec)
        qa = brief(out, r"qa-lead: RV-candidate-r0")
        for item in ("jump height", "scene_audit.py diff", "lowest and highest graphics", "spawn positions and facing"):
            self.assertIn(item, qa)


if __name__ == "__main__":
    unittest.main()
