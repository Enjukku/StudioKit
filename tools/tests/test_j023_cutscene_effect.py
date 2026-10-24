"""J023 flow-speed tests for the cutscene and effect workflows, retargeted to the J024 flow, with fake agents (no tokens).

Kit test (universal). Author: J023 builder A · claude-opus-5-5 · default · 2026-10-24. Binding design: knowledge/jobs/J023-flow-speed/design.md;
revised by J024 test updater · claude-opus-5-5 · default · 2026-10-24 (knowledge/jobs/J024-flow-cuts-r2/design.md: each J023 rule is
checked on the step that holds it now, or the removed step is checked absent).
Runs .agents/workflows/jobs/job-cutscene.js and job-effect.js under tools/workflows/wf_harness.mjs; skipped when Node is not installed.
Covers: B a later review round reruns only the scripts, the protected suite, the reviewer that blocked and the dependents of the repaired
layer, and lists every other verdict as carried (J024 chain); C the needs step runs once in direction (N1 in parallel on the plan, N2 only
for the crafts of a conflict, one merge per round), build never re-asks; D no sign-off and no proposal exchange, a constraint owner writes
one limits table, the table writers confirm the merged plan in their first build hand-back; E M and L share one direction shape and one
build, no proof calls anywhere; F capture, freeze and scripts on one studio-operator run (Sonnet), probes inside the builder's run, no
strips.
"""

from __future__ import annotations

import re
import unittest

from tools.tests.test_job_workflows import JOBS, NODE, full, index, run, span

CUT = JOBS / "job-cutscene.js"
FX = JOBS / "job-effect.js"
# J024: the 9-craft P2 meeting → the N1 needs and limits writers of design §6 (ui-ux-designer and art-director are switched on below).
CUT_MEET = ["animator", "environment-designer", "vfx-designer", "sound-designer", "architect"]
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"


def cut(scenario: dict | None = None, **changes) -> dict:
    out = run(CUT, full("job-cutscene.js", **changes), scenario)
    if out["violation"]:
        raise AssertionError(f"harness violation: {out['violation']}")
    return out


def fx(scenario: dict | None = None, **changes) -> dict:
    out = run(FX, full("job-effect.js", **changes), scenario)
    if out["violation"]:
        raise AssertionError(f"harness violation: {out['violation']}")
    return out


def matching(labels: list[str], pattern: str) -> list[str]:
    return [x for x in labels if re.search(pattern, x)]


def reviewers(labels: list[str], tag: str) -> set[str]:
    """The reviewer ids that ran in one review round, from labels like 'role: RV-candidate-r1-<id>'."""
    return {m.group(1) for x in labels for m in [re.search(rf": RV-{tag}-(.+)$", x)] if m}


def dump(out: dict, pattern: str) -> str:
    hits = [d["prompt"] for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dump matches {pattern}: {out['labels']}")
    return hits[0]


def carried(out: dict) -> list[str]:
    return sorted(c.split(" (")[0] for c in out["result"]["carried"])


@unittest.skipIf(NODE is None, "Node.js not installed")
class SelectiveRecheckTests(unittest.TestCase):
    """B: re-check only what failed."""

    def test_cutscene_round_1_reruns_the_blocker_the_regression_set_and_the_dependents(self):
        # J024: J023 chain (sound-designer reviewer, performance always) → an art finding (newLook) repaired by the sound-designer:
        # the art-director reran (it blocked), the film-director depends on a timing layer (sound sync is its review now), scripts and
        # qa-lead always; the performance-engineer (risk performance) and the code review keep their round-0 verdicts.
        out = cut({"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "sound-designer"}, stage="build", newLook=True,
                  risks=["performance"])
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "qa-lead", "art-director", "film-director"})
        for rid in ("performance-engineer", "reviewer"):
            self.assertTrue(any(c.startswith(f"carried: {rid} (round 0, revision ") for c in out["result"]["carried"]), out["result"]["carried"])
        self.assertEqual(len(out["result"]["carried"]), 2, out["result"]["carried"])

    def test_cutscene_code_repair_reruns_the_code_side_and_carries_the_look(self):
        # J024: J023 code side (performance-engineer, sound-designer rerun) → scripts, qa-lead, reviewer and the film-director (the player
        # code fires the cues it checks from cue_log); the art-director and the performance-engineer keep their verdicts.
        out = cut({"blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "feature-builder"}, stage="build", newLook=True, risks=["performance"])
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "qa-lead", "reviewer", "film-director"})
        self.assertEqual(carried(out), ["carried: art-director", "carried: performance-engineer"])

    def test_cutscene_proof_review_carries_the_architect_when_the_beat_sheet_is_unchanged(self):
        # J024: the proof review round → removed on purpose (no proof stage); the architect no longer reviews (it writes its limits table
        # once in N1), and a reviewer whose input did not change keeps its verdict with round and revision.
        self.assertIn(NO_PROOF, run(CUT, full("job-cutscene.js", stage="proof"))["outcome"])
        out = cut({"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "film-director"}, stage="build")
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(matching(out["labels"], r"^architect: "), [])
        self.assertTrue(all(re.match(r"carried: \S+ \(round 0, revision .+\)$", c) for c in out["result"]["carried"]), out["result"]["carried"])
        self.assertIn("reviewer", [c.split(" ")[1] for c in out["result"]["carried"]])

    def test_effect_round_1_reruns_the_blocker_the_regression_set_and_the_dependents(self):
        # J024: game-designer reviewer, sound-designer rerun → removed reviewers; the vfx-designer's integrated review (it blocked; sound
        # sync is in it) and the qa-lead suite (server-result) rerun with the scripts; the code review and the art-director are carried.
        out = fx({"blockLabelOnce": r"vfx-designer: RV-candidate-r0", "maker": "sound-designer"}, stage="build", risks=["server-result"], newLook=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "vfx-designer", "qa-lead"})
        self.assertEqual(carried(out), ["carried: art-director", "carried: reviewer"])

    def test_effect_wiring_repair_reruns_the_code_review(self):
        # J024: J023 chain members (sound-designer rerun; game-designer and vfx-designer carried) → the reviewer reruns on the wiring, the
        # vfx-designer's integrated review depends on the wiring (it fires the cues); the art-director is carried.
        out = fx({"blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "feature-builder"}, stage="build", newLook=True)
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(reviewers(out["labels"], "candidate-r1"), {"scripts", "reviewer", "vfx-designer"})
        self.assertEqual(carried(out), ["carried: art-director"])

    def test_a_dead_recheck_is_never_a_pass_and_a_carried_verdict_is_not_rerun(self):
        # J024: the art-director reviews only with newLook (design §4.4), so the dead recheck is set up with newLook.
        scen = {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "vfx-designer", "nullLabel": r"art-director: RV-candidate-r1"}
        for run_one, kept in ((cut, "reviewer"), (fx, "reviewer")):
            out = run_one(scen, stage="build", newLook=True)
            self.assertEqual(out["status"], "failed", out["outcome"])
            self.assertIn("art-director", reviewers(out["labels"], "candidate-r1"))
            self.assertNotIn(kept, reviewers(out["labels"], "candidate-r1"), "the code review keeps its verdict after a visual repair")


@unittest.skipIf(NODE is None, "Node.js not installed")
class JointNeedsMeetingTests(unittest.TestCase):
    """C: the needs step runs once, in direction before G1; round 2 only on a conflict; one merge per round; build never re-asks."""

    def test_cutscene_meeting_runs_once_with_every_consumer(self):
        # J024: P2 meeting of 9 crafts after G1 → N1 in direction: the needs crafts and constraint owners of design §6, once each,
        # after the D1 plan and before the one merge; ui-ux-designer when D1 lists UI, art-director with newLook.
        clean = cut(stage="direction")
        self.assertEqual(clean["status"], "done", clean["outcome"])
        labels = clean["labels"]
        self.assertEqual(sorted(x.split(": ")[0] for x in matching(labels, r": N1-")), sorted(CUT_MEET))
        self.assertEqual(matching(labels, r": N2-|M2-merge"), [], "round 2 is skipped when round 1 is clean")
        self.assertEqual(matching(labels, r"-merge"), ["film-director: M1-merge"])
        self.assertEqual(labels[-1], "film-director: M1-merge")
        full_set = cut({"set": {"ui_needed": True}}, stage="direction", newLook=True)
        self.assertEqual(sorted(x.split(": ")[0] for x in matching(full_set["labels"], r": N1-")), sorted(CUT_MEET + ["ui-ux-designer", "art-director"]))
        conflict = {"about": "E3 onset", "why": "w", "between": ["architect", "animator"], "rows": ["A1"]}
        with_conflict = cut({"set": {"open_conflicts": [conflict]}}, stage="direction")
        self.assertEqual(with_conflict["status"], "done", with_conflict["outcome"])
        self.assertEqual(sorted(matching(with_conflict["labels"], r": N2-")), ["animator: N2-animator", "architect: N2-architect"])
        self.assertEqual(matching(with_conflict["labels"], r"-merge"), ["film-director: M1-merge", "film-director: M2-merge"], "one merge per round")

    def test_cutscene_build_never_asks_again(self):
        # J024: the J023 joint meeting in build → the needs step is N1 in direction; build runs no N1/N2, merge or meeting, in L and M.
        for size in ("L", "M"):
            with self.subTest(size=size):
                out = cut(stage="build", size=size)
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(matching(out["labels"], r"needs|N1-|N2-|B1-plan|envelope|B1-lock|merge|meeting"), [])

    def test_effect_meeting_runs_once_on_the_timeline_draft(self):
        # J024: E-r1 meeting in build → N1 in direction against the D1 timeline (animator with animated), once, then one merge;
        # build never re-asks, and sound answers the VFX envelopes in build (B2-vfx before B3-sound).
        clean = fx(stage="direction", animated=True)
        self.assertEqual(clean["status"], "done", clean["outcome"])
        labels = clean["labels"]
        self.assertEqual(sorted(x.split(": ")[0] for x in matching(labels, r": N1-")), ["animator", "feature-builder", "sound-designer"])
        self.assertEqual(matching(labels, r": N2-"), [])
        self.assertEqual(matching(labels, r"-merge"), ["vfx-designer: M1-merge"])
        self.assertEqual(matching(labels, r"P1-window|E-r"), [], "the window from direction is not asked for again")
        timed = fx({"timeline": True}, stage="build")
        self.assertLess(span(timed, r"vfx-designer: B2-vfx")["end"], span(timed, r"sound-designer: B3-sound")["start"], "sound answers VFX's envelopes")
        conflict = {"about": "E1", "why": "w", "between": ["sound-designer", "animator"], "rows": ["S1"]}
        with_conflict = fx({"set": {"open_conflicts": [conflict]}}, stage="direction", animated=True)
        self.assertEqual(len(matching(with_conflict["labels"], r": N2-")), 2)
        self.assertEqual(matching(with_conflict["labels"], r"-merge"), ["vfx-designer: M1-merge", "vfx-designer: M2-merge"])
        build = fx(stage="build", animated=True)
        self.assertEqual(matching(build["labels"], r": E-|P1-window|needs|N1-|N2-|merge"), [])


@unittest.skipIf(NODE is None, "Node.js not installed")
class LighterDirectionTests(unittest.TestCase):
    """D: no sign-off and no proposal exchange; N2 only for the crafts in a conflict the merge reports."""

    def test_cutscene_direction_has_no_sign_off_and_no_exchange_without_conflict(self):
        # J024: D1 proposals, D2 exchange, D3 synthesis → D1 plan, N1 tables, M1 merge; N2 + M2 only on the merge's open_conflicts.
        out = cut(stage="direction")
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        self.assertEqual(matching(labels, r"D3-|D2-|-sign"), [])
        self.assertEqual(len(matching(labels, r"^architect: ")), 1, "a constraint owner writes one limits table and is not called again")
        self.assertEqual(matching(labels, r"^game-designer: "), [], "J024 §6: no game-designer limits in a cutscene")
        conflict = cut({"set": {"open_conflicts": [{"about": "B3", "why": "w", "between": ["architect", "vfx-designer"], "rows": ["L2"]}]}},
                       stage="direction")
        self.assertEqual(conflict["status"], "done", conflict["outcome"])
        self.assertEqual(sorted(matching(conflict["labels"], r": N2-")), ["architect: N2-architect", "vfx-designer: N2-vfx-designer"])
        self.assertGreater(index(conflict["labels"], r"M2-merge"), index(conflict["labels"], r": N2-"))
        self.assertEqual(matching(conflict["labels"], r"-sign|D2-"), [])

    def test_effect_direction_has_no_sign_off_and_no_exchange_without_conflict(self):
        # J024: D2 exchange labels on proposal_conflicts → no exchange at all; N2 only for the crafts of the merge's open_conflicts.
        out = fx({"set": {"proposal_conflicts": [{"about": "E1", "why": "w", "between": ["vfx-designer", "sound-designer"]}]}}, stage="direction")
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(matching(out["labels"], r"D3-sign|D2-|N2-"), [], "a proposal conflict alone starts no exchange")
        conflict = fx({"set": {"open_conflicts": [{"about": "E1", "why": "w", "between": ["sound-designer", "game-designer"], "rows": ["G1"]}]}},
                      stage="direction", risks=["danger-area"])
        self.assertEqual(sorted(matching(conflict["labels"], r": N2-")), ["game-designer: N2-game-designer", "sound-designer: N2-sound-designer"])
        self.assertEqual(matching(conflict["labels"], r"feature-builder: N2-"), [])

    def test_leads_confirm_the_direction_in_their_first_hand_back(self):
        # J024: the architect's P2-needs "Direction check" → each table writer's first build brief asks it to confirm the merged plan
        # (or name an incompatibility: needs-decision); later briefs do not; a needs-decision there stops the build.
        out = cut({"dump": r"."}, stage="build")
        for label in ("animator: B1-animator", "environment-designer: B2-set", "vfx-designer: B3-vfx", "sound-designer: B4-sound"):
            with self.subTest(label=label):
                p = dump(out, label)
                self.assertIn(f'"plan confirmed: {label.split(":")[0]} rev N"', p)
                self.assertIn("needs-decision", p)
        again = cut({"dump": r"FIX-|RV-candidate-r1", "blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "vfx-designer"}, stage="build")
        for d in again["dumps"]:
            with self.subTest(later=d["label"]):
                self.assertNotIn("plan confirmed", d["prompt"], "only the first hand-back confirms")
        stopped = cut({"statusLabel": r"animator: B1-animator", "status": "needs-decision"}, stage="build")
        self.assertEqual(stopped["status"], "needs-decision", "an incompatibility stops the stage")
        self.assertEqual(stopped["labels"], ["animator: B1-animator"])
        effect = fx({"dump": r"sound-designer: B3-sound"}, stage="build")
        self.assertIn('"plan confirmed: sound-designer rev N"', dump(effect, r"sound-designer: B3-sound"))


@unittest.skipIf(NODE is None, "Node.js not installed")
class MediumJobTests(unittest.TestCase):
    """E: M and L share the direction shape (M has one direction) and the build; no proof calls in any size."""

    def test_m_direction_is_the_job_lead_with_the_limits_sheets(self):
        # J024: M direction = the job lead alone with limits sheets → M direction is D1 plan (one direction), N1 tables, the merge.
        out = cut(stage="direction", size="M")
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(sorted(out["labels"]), sorted(["film-director: D1-plan", "film-director: M1-merge"] + [f"{r}: N1-{r}" for r in CUT_MEET]))
        out = fx(stage="direction", size="M")
        self.assertEqual(sorted(out["labels"]), ["animator: N1-animator", "feature-builder: N1-feature-builder", "sound-designer: N1-sound-designer",
                                                 "vfx-designer: D1-plan", "vfx-designer: M1-merge"])

    def test_m_build_runs_no_proof_calls(self):
        # J024: M build has no proof calls and fewer agents than L proof + build → no proof in any size (refused), and
        # M direction + build ≤ L direction + build.
        for name, run_one, proof_calls, extra in (
                ("job-cutscene.js", cut, r"P3a-|P4-|P3-|P5-|PR-|proof", {}),
                ("job-effect.js", fx, r"P3-|P4 |P5 |-proof|temp-sound|P1-window", {"animated": True})):
            with self.subTest(script=name):
                total = {}
                for size in ("L", "M"):
                    self.assertIn(NO_PROOF, run_one(stage="proof", size=size, **extra)["outcome"])
                    runs = [run_one(stage=s, size=size, **extra) for s in ("direction", "build")]
                    for out in runs:
                        self.assertEqual(out["status"], "done", out["outcome"])
                        self.assertEqual(matching(out["labels"], proof_calls), [])
                    total[size] = sum(o["agents"] for o in runs)
                self.assertLessEqual(total["M"], total["L"])

    def test_m_effect_keeps_the_art_blocking_check_before_any_texture_pick(self):
        # J024: B0 art blocking check-in → removed on purpose (no rough pass, design §2): the M build has no blocking pass or check-in
        # and no art-director run; the vfx-designer builds the final spec once.
        out = fx(stage="build", size="M")
        self.assertEqual(matching(out["labels"], r"B0-|checkin|first-spec|CAP-blocking|^art-director:"), [], out["labels"])
        self.assertEqual(matching(out["labels"], r"^vfx-designer: B"), ["vfx-designer: B2-vfx"])


@unittest.skipIf(NODE is None, "Node.js not installed")
class ModelAndAgentSizeTests(unittest.TestCase):
    """F: capture, freeze and scripts on one studio-operator run (Sonnet); probes inside the builder's run; no strips."""

    def test_cutscene_captures_and_probes_run_on_the_studio_operator(self):
        # J024: CAP-candidate, CAP-…-fix, P3-probes → one studio-operator capture-and-scripts run per review round (Sonnet, it freezes the
        # protected list); the architect's probes run inside the feature-builder's build run; repair captures once.
        out = cut({"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "vfx-designer", "dump": r"studio-operator: |PLY-candidate"}, stage="build")
        caps = matching(out["labels"], r"^studio-operator: ")
        self.assertEqual(caps, ["studio-operator: RV-candidate-r0-scripts", "studio-operator: RV-candidate-r1-scripts"])
        for d in out["dumps"]:
            if d["label"].startswith("studio-operator"):
                self.assertIn("model: sonnet", d["prompt"])
                self.assertIn("protected list", d["prompt"], "the capture freezes the candidate")
        self.assertIn("Run the Studio probes the architect's limits table names, inside this run", dump(out, r"PLY-candidate"))
        self.assertEqual(matching(out["labels"], r"probes"), [])
        repair = cut({"affected": ["animator"]}, stage="repair")
        self.assertEqual(matching(repair["labels"], r"^studio-operator: "), ["studio-operator: RV-repair-r0-scripts"])

    def test_effect_freeze_moves_from_the_maker_to_the_capture(self):
        # J024: CAP-candidate-r0 → the freeze is in the capture-and-scripts run (RV-candidate-r0-scripts).
        out = fx({"dump": r"RV-candidate-r0-(scripts|vfx-designer)"}, stage="build")
        cap = dump(out, r"RV-candidate-r0-scripts")
        self.assertIn("model: sonnet", cap)
        self.assertIn("Freeze the candidate", cap)
        self.assertRegex(cap, r"owns: \[[^\]]*evidence\.md")
        self.assertNotRegex(dump(out, r"vfx-designer: RV-candidate-r0"), r"owns: \[[^\]]*evidence\.md")

    def test_cutscene_strips_run_one_short_agent_per_shot_group(self):
        # J024: strips per shot group → removed on purpose (J023-D7): however many shots, direction plans every camera in one D1 run
        # and build makes no strip run.
        shots = [f"S{n:02d}" for n in range(1, 8)]
        for stage in ("direction", "build"):
            with self.subTest(stage=stage):
                out = cut({"set": {"shot_ids": shots}}, stage=stage)
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(matching(out["labels"], r"strip|board|animatic"), [])
        out = cut({"set": {"shot_ids": shots}}, stage="direction")
        self.assertEqual(matching(out["labels"], r"^film-director: "), ["film-director: D1-plan", "film-director: M1-merge"])


if __name__ == "__main__":
    unittest.main()
