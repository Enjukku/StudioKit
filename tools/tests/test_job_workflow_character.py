"""Control-flow tests for job-character.js: the recipe rows of b2eeb73 and the risks arg (J019, G3-P4).

Kit test (universal). Author: J019 workflow maker · claude-opus-5-5 · high · 2026-10-22 (G3-P4: recipe rows of b2eeb73, risks arg);
revised by J024 test updater · claude-opus-5-5 · default · 2026-10-24 (J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md: no proof
stage and no G2; direction = D1 plan, N1 needs tables, merge; one run per craft; one capture-and-scripts run; fewer reviewers).
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
        # J024: STAGES lost proof; a proof call is refused before any arg check (test_j024_character_stage), so risks is checked in the three stages.
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
        # J024: 3 risk slots → 4: the universal token performance adds the performance-engineer review slot (design §7).
        out = run(NAME, full(NAME, stage="direction"))
        self.done(out)
        slots = {s["risk"]: s["runs"] for s in out["result"]["risk_slots"]}
        self.assertEqual(slots, {"new-enemy": False, "sold-variant": False, "event": False, "performance": False})
        on = run(NAME, full(NAME, stage="direction", risks=["performance"]))
        self.done(on)
        self.assertTrue({s["risk"]: s["runs"] for s in on["result"]["risk_slots"]}["performance"])

    # ------------------------------------------------------------------ behaviour test (risk new-enemy)
    def test_new_enemy_adds_the_behaviour_test_before_g1(self):
        plain, plain_labels = labels(stage="direction")
        self.done(plain)
        self.assertEqual(index(plain_labels, r"D4-behaviour"), -1)
        self.assertNotIn("behaviour_test", plain["result"]["g1"])
        out, got = labels(stage="direction", risks=["new-enemy"])
        self.done(out)
        cap, verdict = index(got, r"^studio-operator: D4-behaviour-capture"), index(got, r"^game-designer: D4-behaviour-verdict")
        # J024: the behaviour test follows D3-synthesis → it follows the merge (M-r1-merge) and is still the last step before G1.
        merge = index(got, r"^art-director: M-r1-merge")
        self.assertTrue(0 <= merge < cap < verdict == len(got) - 1, got)
        # J024: the modeler writes only its needs table in direction; no modeler build runs before the verdict.
        self.assertEqual([x for x in got if x.startswith("modeler:")], ["modeler: N1-modeler"], "no modeler build before the verdict")
        self.assertIn("behaviour_test", out["result"]["g1"])
        self.assertTrue(any("behaviour test" in x for x in out["result"]["g1"]["owner_confirmed"]))

    def test_a_failed_behaviour_test_stops_for_the_owner(self):
        out, got = labels(stage="direction", risks=["new-enemy"], scenario={"set": {"behaviour_verdict": "does not play as intended"}})
        self.assertEqual(out["status"], "needs-decision", out["outcome"])
        self.assertEqual(out["result"]["g1"]["behaviour_test"]["verdict"], "does not play as intended")

    def test_the_behaviour_verdict_reaches_the_blockout(self):
        # J024: the verdict reaches the P2 blockout (proof) → it reaches the modeler's one final-model run (B1-model), only with new-enemy.
        out = run(NAME, full(NAME, stage="build", risks=["new-enemy"]), {"dump": r"B1-model$"})
        self.done(out)
        self.assertIn("behaviour-test/verdict.md", out["dumps"][0]["prompt"])
        plain = run(NAME, full(NAME, stage="build"), {"dump": r"B1-model$"})
        self.done(plain)
        self.assertNotIn("behaviour-test/verdict.md", plain["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ direction leads and G1 (cross-type rules)
    def test_direction_leads_state_windows_rates_and_r15_limits(self):
        # J024: D1 proposals and limits sheets → the D1 plan (art-director) and the N1 needs tables. The game-designer states the
        # gameplay windows per action in N1; the reaction window of each tell and the play rate are judged in the behaviour verdict.
        out = run(NAME, full(NAME, stage="direction", risks=["new-enemy"]), {"dump": r": (D1-plan|N1-|D4-behaviour-verdict)"})
        self.done(out)
        briefs = {d["label"]: d["prompt"] for d in out["dumps"]}
        self.assertIn("gameplay windows per action (startup, active, recovery, cancel, in seconds)", briefs["game-designer: N1-game-designer"])
        verdict = briefs["game-designer: D4-behaviour-verdict"]
        self.assertIn("reaction window of each threat's tell", verdict)
        self.assertIn("play rate of each action", verdict)
        for label in ("character-rigger: N1-character-rigger", "animator: N1-animator"):
            with self.subTest(label=label):
                self.assertIn("no clavicles, no fingers", briefs[label])
                self.assertIn("custom rig is an owner choice", briefs[label])
        plan = briefs["art-director: D1-plan"]
        self.assertIn("warm-up", plan)
        self.assertIn("radical", plan)
        self.assertIn("grey pass", plan)

    def test_g1_carries_failed_options_closed_doors_and_could_not_check(self):
        # J024: the D3-synthesis brief → the D1 plan brief carries the options, the grey pass and the closed doors; g1 keeps every key.
        out = run(NAME, full(NAME, stage="direction"), {"dump": r"D1-plan"})
        self.done(out)
        g1 = out["result"]["g1"]
        for key in ("failed_options", "closed_doors", "why_others_lost", "could_not_check", "owner_confirmed"):
            with self.subTest(key=key):
                self.assertIn(key, g1)
        plan = out["dumps"][0]["prompt"]
        self.assertIn('"may return only if"', plan)
        self.assertIn("a failing one is a numbers line", plan)
        self.assertIn("black-fill at phone size", plan)

    # ------------------------------------------------------------------ contract and interfaces before G1 (J024: the proof is gone)
    def test_the_reference_check_runs_before_the_rig_plan(self):
        # J024: P1-reference-check before S2-plan → the modeler's reference check (N1-modeler) and the rig plan (N1-character-rigger) run in
        # parallel on the plan file and are merged before G1; in build the rig (B2-rig) is built only on the final model (B1-model).
        for size in ("L", "M"):
            with self.subTest(size=size):
                d, dg = labels(stage="direction", size=size, scenario={"dump": r"N1-modeler$"})
                self.done(d)
                merge = index(dg, r"^art-director: M-r1-merge$")
                self.assertTrue(0 < index(dg, r"^modeler: N1-modeler$") < merge, dg)
                self.assertTrue(0 < index(dg, r"^character-rigger: N1-character-rigger$") < merge, dg)
                self.assertIn("the missing views the reference set must add", d["dumps"][0]["prompt"])
                self.assertEqual(index(dg, r"reference-answer"), -1, "no answer step: the merge answers the gaps")
                b, bg = labels(stage="build", size=size)
                self.done(b)
                self.assertTrue(0 == index(bg, r"^art-director: B0-reference-set") < index(bg, r"^modeler: B1-model") < index(bg, r"^character-rigger: B2-rig"), bg)

    def test_reference_asks_are_answered_before_s1(self):
        # J024: NM-merge answers the reference check before K1 (proof) → M-r1-merge answers the modeler's gaps before G1 and names the
        # missing views; the build's reference set (B0) makes them before any model, rig or clip (the S1 motion needs are in N1).
        out, got = labels(stage="direction", scenario={"dump": r"art-director: M-r1-merge"})
        self.done(out)
        merge = index(got, r"^art-director: M-r1-merge")
        self.assertTrue(0 < index(got, r"^modeler: N1-modeler") < merge, got)
        self.assertTrue(0 < index(got, r"^animator: N1-animator") < merge, got)
        prompt = out["dumps"][0]["prompt"]
        self.assertIn("Answer the modeler's gaps", prompt, "the merge answers every ask of the reference check")
        self.assertIn("a missing view becomes a row for the reference set after G1", prompt)
        self.assertIn("needs/modeler.md", prompt, "the merge reads the modeler's table")
        b = run(NAME, full(NAME, stage="build"), {"dump": r"B0-reference-set"})
        self.done(b)
        self.assertIn("the missing views the merge named", b["dumps"][0]["prompt"])
        self.assertEqual(b["labels"][0], "art-director: B0-reference-set", "the views come before any model, rig or clip")

    def test_the_sound_plan_comes_before_any_clip(self):
        # J024: P1-sound-plan before S7-blocking (M build) → the sound plan is the sound-designer's N1 table in direction, before G1;
        # the one clip run (B3-animation) and the sound run read it. S7-blocking is gone (no rough clips).
        d, dg = labels(stage="direction", size="M", scenario={"dump": r"N1-sound-designer"})
        self.done(d)
        self.assertGreaterEqual(index(dg, r"^sound-designer: N1-sound-designer$"), 0)
        self.assertIn("sound-plan.md", d["dumps"][0]["prompt"])
        out, got = labels(stage="build", size="M", scenario={"dump": r"B3-animation$|B5-sound$"})
        self.done(out)
        self.assertEqual(index(got, r"blocking"), -1)
        self.assertLess(index(got, r"^animator: B3-animation$"), index(got, r"^sound-designer: B5-sound$"))
        self.assertEqual(len(out["dumps"]), 2)
        for dmp in out["dumps"]:
            with self.subTest(label=dmp["label"]):
                self.assertIn("sound-plan.md", dmp["prompt"])
        variant, vgot = labels(stage="direction", size="M", variant=True)
        self.done(variant)
        self.assertEqual(index(vgot, r"sound-designer"), -1, "a variant keeps the base sound (no sound step in variant mode)")
        vb, vbg = labels(stage="build", size="M", variant=True)
        self.done(vb)
        self.assertEqual(index(vbg, r"sound-designer"), -1)

    # ------------------------------------------------------------------ the rigger's measured self-check (J024 §2: the proof and G2 are gone)
    def test_proof_shows_pose_options_stress_numbers_and_roster_lineup(self):
        # J024: P3-proxy-pose, P3-roster-lineup and the RV-proof reviews → the rigger measures the posed-proxy clearances inside its N1
        # run (J005); the shipped rig is measured again (rig_audit.py in the capture run), every stress pose is posed on the real rig in
        # the animator's run, and the job lead measures key frames. Pose options, the roster lineup and the proof reviews are removed.
        d = run(NAME, full(NAME, stage="direction"), {"dump": r"N1-character-rigger$"})
        self.done(d)
        rig = d["dumps"][0]["prompt"]
        for text in ("posed proxy", "signature action's peak", "black-fill render at the game camera at phone size", "overlap_pairs", "cap_count",
                     "the posed-proxy clearances (overlap pairs, cap exposure)", "it is not handed on"):
            with self.subTest(text=text):
                self.assertIn(text, rig)
        b = run(NAME, full(NAME, stage="build"), {"dump": r"CAP-candidate-r0$|B3-animation$|RV-candidate-r0-art-director$"})
        self.done(b)
        briefs = {x["label"]: x["prompt"] for x in b["dumps"]}
        self.assertIn("tools/rig/rig_audit.py on the shipped rig", briefs["studio-operator: CAP-candidate-r0"])
        self.assertIn("every §B extreme and stress pose", briefs["animator: B3-animation"])
        self.assertIn("look_check.py", briefs["art-director: RV-candidate-r0-art-director"])
        for out in (d, b):
            self.assertEqual(index(out["labels"], r"proxy-pose|lineup|RV-proof"), -1, out["labels"])

    def test_a_proof_repair_retakes_the_lineup(self):
        # J024: a proof repair retakes the roster lineup → the lineup is removed; a build repair round takes a fresh capture-and-scripts
        # run (CAP-candidate-r1) after the fix and the refreeze it needs, before any round-1 review.
        out, got = labels(stage="build", scenario={"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler"})
        self.done(out)
        retake = index(got, r"^studio-operator: CAP-candidate-r1$")
        self.assertTrue(index(got, r"FIX-candidate-r0-modeler") < index(got, r"REFREEZE-candidate-r0") < retake < index(got, r"RV-candidate-r1-"), got)
        self.assertEqual(index(got, r"lineup"), -1)

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
                # J024: after the art-director and game-designer reviews → after the whole chain (the game-designer no longer reviews):
                # the integrated review, the qa-lead and the reviewer (playable).
                for creative in ("art-director", "qa-lead", "reviewer"):
                    self.assertGreater(cap, index(got, rf"^{creative}: RV-{tag}-r0-"), creative)
                self.assertEqual(index(got, r"game-designer: RV-"), -1)
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
        # J024: a dead lineup recapture fails the proof → the lineup is gone; a dead recapture after a build repair (CAP-candidate-r1)
        # fails the stage and the old captures are never reviewed again.
        out, got = labels(stage="build", scenario={"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler", "nullLabel": r"CAP-candidate-r1$"})
        self.assertEqual(out["status"], "failed", out["outcome"])
        self.assertEqual(index(got, r"RV-candidate-r1-"), -1, "the old captures are never reviewed again")

    def test_a_dead_fix_step_fails_the_proof(self):
        # J024: a dead proof fix → a dead build fix (FIX-candidate-r0-modeler) fails the stage; nothing runs after it.
        out, got = labels(stage="build", scenario={"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler", "nullLabel": r"FIX-candidate-r0-modeler"})
        self.assertEqual(out["status"], "failed", out["outcome"])
        self.assertRegex(got[-1], r"FIX-candidate-r0-modeler")


if __name__ == "__main__":
    unittest.main()
