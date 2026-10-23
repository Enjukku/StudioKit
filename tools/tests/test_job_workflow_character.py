"""Control-flow tests for job-character.js: the recipe rows of b2eeb73 and the risks arg (J019, G3-P4).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg).
Uses the fake-agent harness through the helpers of tools/tests/test_job_workflows.py; skipped when Node is not installed.
Recipe: .agents/skills/orchestration/references/job-types.md §2, "Cross-type rules", "Named review captures".
"""

from __future__ import annotations

import unittest

from tools.tests.test_job_workflows import NODE, STAGES, full, index, run

NAME = "job-character.js"


def labels(**changes) -> tuple[dict, list[str]]:
    scenario = changes.pop("scenario", None)
    out = run(NAME, full(NAME, **changes), scenario)
    return out, out["labels"]


@unittest.skipIf(NODE is None, "Node.js not installed")
class CharacterWorkflowTests(unittest.TestCase):
    def done(self, out: dict) -> None:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])

    # ------------------------------------------------------------------ the risks arg (README args row)
    def test_risks_is_required_in_every_stage(self):
        for stage in STAGES:
            for bad in (None, "new-enemy", {"new-enemy": True}):
                with self.subTest(stage=stage, risks=bad):
                    out = run(NAME, full(NAME, stage=stage, risks=bad))
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("risks", out["outcome"])

    def test_an_unknown_risk_token_is_blocked_by_name(self):
        for token in ("money", "saves", "paid-random", ""):
            with self.subTest(token=token):
                out = run(NAME, full(NAME, stage="build", risks=["event", token]))
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(f'"{token}"', out["outcome"])

    def test_sold_variant_needs_variant_mode(self):
        out = run(NAME, full(NAME, stage="build", risks=["sold-variant"]))
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(out["agents"], 0)
        self.assertIn("sold-variant needs variant", out["outcome"])
        self.done(run(NAME, full(NAME, stage="build", variant=True, risks=["sold-variant"])))

    def test_new_enemy_needs_studio_in_direction(self):
        out = run(NAME, full(NAME, stage="direction", studioId=None, risks=["new-enemy"]))
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(out["agents"], 0)
        self.assertIn("studioId", out["outcome"])
        self.assertIn("studioId in direction when risks names new-enemy", out["meta"]["whenToUse"])
        self.done(run(NAME, full(NAME, stage="direction", studioId=None)))

    def test_every_risk_slot_is_a_line_in_the_result(self):
        out = run(NAME, full(NAME, stage="direction"))
        self.done(out)
        slots = {s["risk"]: s["runs"] for s in out["result"]["risk_slots"]}
        self.assertEqual(slots, {"new-enemy": False, "sold-variant": False, "event": False})

    # ------------------------------------------------------------------ behaviour test (risk new-enemy)
    def test_new_enemy_adds_the_behaviour_test_before_g1(self):
        plain, plain_labels = labels(stage="direction")
        self.done(plain)
        self.assertEqual(index(plain_labels, r"D4-behaviour"), -1)
        self.assertNotIn("behaviour_test", plain["result"]["g1"])
        out, got = labels(stage="direction", risks=["new-enemy"])
        self.done(out)
        cap, verdict = index(got, r"^studio-operator: D4-behaviour-capture"), index(got, r"^game-designer: D4-behaviour-verdict")
        last_sign = max(i for i, x in enumerate(got) if "D3-sign-" in x)
        self.assertTrue(last_sign < cap < verdict == len(got) - 1, got)
        self.assertEqual(index(got, r"^modeler:"), -1, "no modeler brief before the verdict")
        self.assertIn("behaviour_test", out["result"]["g1"])
        self.assertTrue(any("behaviour test" in x for x in out["result"]["g1"]["owner_confirmed"]))

    def test_a_failed_behaviour_test_stops_for_the_owner(self):
        out, got = labels(stage="direction", risks=["new-enemy"], scenario={"set": {"behaviour_verdict": "does not play as intended"}})
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(out["result"]["g1"]["behaviour_test"]["verdict"], "does not play as intended")

    def test_the_behaviour_verdict_reaches_the_blockout(self):
        out = run(NAME, full(NAME, stage="proof", risks=["new-enemy"]), {"dump": r"P2-blockout"})
        self.done(out)
        self.assertIn("behaviour-test/verdict.md", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ direction leads and G1 (cross-type rules)
    def test_direction_leads_state_windows_rates_and_r15_limits(self):
        out = run(NAME, full(NAME, stage="direction"), {"dump": r": D1-"})
        briefs = {d["label"].split(":")[0]: d["prompt"] for d in out["dumps"]}
        self.assertIn("reaction window for each threat's tell", briefs["game-designer"])
        self.assertIn("play rate of each action", briefs["game-designer"])
        for role in ("character-rigger", "animator"):
            with self.subTest(role=role):
                self.assertIn("no clavicles, no fingers", briefs[role])
                self.assertIn("custom rig is an owner choice", briefs[role])
        self.assertIn("warm-up", briefs["art-director"])
        self.assertIn("radical", briefs["art-director"])
        self.assertIn("grey pass", briefs["art-director"])

    def test_g1_carries_failed_options_closed_doors_and_could_not_check(self):
        out = run(NAME, full(NAME, stage="direction"), {"dump": r"D3-synthesis"})
        self.done(out)
        g1 = out["result"]["g1"]
        for key in ("failed_options", "closed_doors", "why_others_lost", "could_not_check", "owner_confirmed"):
            with self.subTest(key=key):
                self.assertIn(key, g1)
        synth = out["dumps"][0]["prompt"]
        self.assertIn('"may return only if"', synth)
        self.assertIn("numbers list", synth)
        self.assertIn("black-fill at phone size", synth)

    # ------------------------------------------------------------------ contract and interfaces before the proof
    def test_the_reference_check_runs_before_the_rig_plan(self):
        for changes in (dict(stage="proof"), dict(stage="build", size="M")):
            with self.subTest(changes=changes):
                out, got = labels(**changes)
                self.done(out)
                check = index(got, r"^modeler: P1-reference-check")
                self.assertGreater(check, index(got, r"art-director: P1-reference-set"))
                self.assertLess(check, index(got, r"animator: S1-needs"))
                self.assertLess(check, index(got, r"character-rigger: S2-plan"))
                self.assertEqual(index(got, r"P1-reference-answer"), -1, "no answer step without asks")

    def test_reference_asks_are_answered_before_s1(self):
        ask = {"about": "back view", "why": "missing", "needs": "a view"}
        out, got = labels(stage="proof", scenario={"set": {"asks": [ask]}})
        self.done(out)
        answer = index(got, r"^art-director: P1-reference-answer")
        self.assertTrue(index(got, r"P1-reference-check") < answer < index(got, r"S1-needs"), got)

    def test_the_sound_plan_comes_before_any_clip(self):
        out, got = labels(stage="build", size="M", scenario={"dump": r"S7-sound"})
        self.done(out)
        plan = index(got, r"^sound-designer: P1-sound-plan")
        self.assertGreaterEqual(plan, 0)
        self.assertLess(plan, index(got, r"animator: S7-blocking"))
        self.assertIn("sound-plan.md", out["dumps"][0]["prompt"])
        variant, vgot = labels(stage="build", size="M", variant=True)
        self.done(variant)
        self.assertEqual(index(vgot, r"P1-sound-plan"), -1, "a variant keeps the base sound (no sound step in variant mode)")

    # ------------------------------------------------------------------ proof (G2)
    def test_proof_shows_pose_options_stress_numbers_and_roster_lineup(self):
        out = run(NAME, full(NAME, stage="proof"), {"dump": r"P3-proxy-pose|RV-proof-r0-"})
        self.done(out)
        got = out["labels"]
        lineup = index(got, r"^studio-operator: P3-roster-lineup")
        self.assertTrue(index(got, r"P3-proxy-pose") < lineup < index(got, r"RV-proof-r0-"), got)
        prompts = {d["label"].split(":")[0] + ":" + d["label"].split(": ")[1]: d["prompt"] for d in out["dumps"]}
        pose = prompts["character-rigger:P3-proxy-pose"]
        for text in ("2-3 signature pose options", "black-fill at the game camera at phone size", "overlap_pairs", "cap_count"):
            with self.subTest(text=text):
                self.assertIn(text, pose)
        self.assertIn("stress-pose overlap and cap-exposure numbers", prompts["animator:RV-proof-r0-animator"])
        self.assertIn("roster lineup", prompts["game-designer:RV-proof-r0-game-designer"])
        self.assertIn("pick the signature pose", prompts["art-director:RV-proof-r0-art-director"])

    def test_a_proof_repair_retakes_the_lineup(self):
        out, got = labels(stage="proof", scenario={"blockLabelOnce": r"art-director: RV-proof-r0", "maker": "modeler"})
        self.done(out)
        retake = index(got, r"^studio-operator: RECAP-proof-r0-lineup")
        self.assertTrue(index(got, r"FIX-proof-r0-modeler") < retake < index(got, r"RV-proof-r1-"), got)

    # ------------------------------------------------------------------ sold variant (PF-13)
    def test_sold_variant_adds_the_pf13_check(self):
        plain, pgot = labels(stage="build", variant=True)
        self.done(plain)
        self.assertEqual(index(pgot, r"RV-candidate-r0-pf13"), -1)
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out = run(NAME, full(NAME, stage=stage, variant=True, risks=["sold-variant"]), {"affected": ["modeler"], "dump": r"RV-candidate-r0-pf13|RV-repair-r0-pf13"})
                self.done(out)
                self.assertGreaterEqual(index(out["labels"], r"^qa-lead: RV-(candidate|repair)-r0-pf13"), 0)
                self.assertIn("PF-13", out["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ event (live-ops review before G3)
    def test_event_adds_the_live_ops_review_after_the_creative_chain(self):
        plain, pgot = labels(stage="build")
        self.done(plain)
        self.assertEqual(index(pgot, r"live-ops-designer"), -1)
        for stage in ("build", "repair"):
            with self.subTest(stage=stage):
                out, got = labels(stage=stage, risks=["event"], scenario={"affected": ["animator"]})
                self.done(out)
                tag = "candidate" if stage == "build" else "repair"
                live = index(got, rf"^live-ops-designer: RV-{tag}-r0-live-ops-designer")
                cap = index(got, rf"^studio-operator: CAP-{tag}-r0-event")
                self.assertGreater(cap, index(got, rf"art-director: RV-{tag}-r0-"))
                self.assertGreater(cap, index(got, rf"game-designer: RV-{tag}-r0-"))
                self.assertEqual(live, cap + 1, got)

    def test_event_findings_route_to_makers_inside_the_round_limits(self):
        out, got = labels(stage="build", risks=["event"], scenario={"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "modeler"})
        self.done(out)
        self.assertGreater(index(got, r"FIX-candidate-r0-modeler"), index(got, r"live-ops-designer: RV-candidate-r0"))
        self.assertGreaterEqual(index(got, r"live-ops-designer: RV-candidate-r1"), 0)
        stuck = run(NAME, full(NAME, stage="build", risks=["event"]), {"blockLabel": r"live-ops-designer: RV-", "maker": "modeler"})
        self.assertEqual(stuck["status"], "needs-decision", stuck["outcome"])

    # ------------------------------------------------------------------ G3 packet lines (cross-type rules)
    def test_g3_carries_could_not_check_and_owner_lines(self):
        out = run(NAME, full(NAME, stage="build"))
        self.done(out)
        g3 = out["result"]["g3"]
        self.assertIn("could_not_check", g3)
        self.assertTrue(any("feel at normal speed" in x for x in g3["owner_confirmed"]))
        self.assertTrue(any("phone speaker and on headphones" in x for x in g3["owner_confirmed"]))
        variant = run(NAME, full(NAME, stage="build", variant=True))
        self.done(variant)
        self.assertFalse(any("two listens" in x for x in variant["result"]["g3"]["owner_confirmed"]), "a variant makes no sound")
        repair = run(NAME, full(NAME, stage="repair"), {"affected": ["modeler"]})
        self.done(repair)
        self.assertIn("g3", repair["result"])


    # ------------------------------------------------------------------ J019 lead review: a step that does not finish is never a pass
    def test_a_dead_lineup_recapture_fails_the_proof(self):
        out, got = labels(stage="proof", scenario={"blockLabelOnce": r"art-director: RV-proof-r0", "maker": "modeler", "nullLabel": r"RECAP-proof-r0-lineup"})
        self.assertEqual(out["status"], "failed", out["outcome"])
        self.assertEqual(index(got, r"RV-proof-r1-"), -1, "the old lineup is never reviewed again")

    def test_a_dead_fix_step_fails_the_proof(self):
        out, _ = labels(stage="proof", scenario={"blockLabelOnce": r"art-director: RV-proof-r0", "maker": "modeler", "nullLabel": r"FIX-proof-r0-modeler"})
        self.assertEqual(out["status"], "failed", out["outcome"])


if __name__ == "__main__":
    unittest.main()
