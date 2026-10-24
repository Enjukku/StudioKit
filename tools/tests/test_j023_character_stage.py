"""Control-flow tests for the J023 flow changes in job-character.js and job-stage.js (knowledge/jobs/J023-flow-speed/design.md B-F).

Kit test (universal). Author: J023 builder B · claude-opus-5-5 · default · 2026-10-24; revised by J024 test updater ·
claude-opus-5-5 · default · 2026-10-24 (the J023 rules retargeted to the J024 flow, knowledge/jobs/J024-flow-cuts-r2/design.md).
Uses the fake-agent harness through the helpers of tools/tests/test_job_workflows.py; skipped when Node is not installed.
B: a later review round reruns only the capture-and-scripts run, the qa-lead suite, the reviewers with a blocking finding and the
reviewers whose area depends on a repaired layer; the others are carried. C (J024 §3): the needs step is N1 in direction (VFX and sound in
it from the start in the character job), a second round only on a conflict the merge reports, at most two merges. D: no proposals from
other leads and no sign-off run; the confirmation is in each craft's first build hand-back. E (J024 §1): no proof stage in any size; M
direction + build is no bigger than L. F: captures run on the studio-operator (Sonnet), one capture-and-scripts run per round.
J023_JOBS_DIR (optional) points the tests at another copy of the scripts, for the one-time check that they fail on the old ones.
"""

from __future__ import annotations

import os
import re
import unittest
from pathlib import Path

try:
    from tools.tests.test_job_workflows import JOBS, NODE, full, index, run, span
except ImportError:   # unittest discovery with -t tools/tests (tools/verify.py)
    from test_job_workflows import JOBS, NODE, full, index, run, span

DIR = Path(os.environ.get("J023_JOBS_DIR") or JOBS)
CHAR = "job-character.js"
STAGE = "job-stage.js"
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"


def go(name: str, scenario: dict | None = None, **changes) -> dict:
    return run(DIR / name, full(name, **changes), scenario)


def ids(out: dict) -> list[str]:
    return [label.split(": ", 1)[1] for label in out["labels"]]


@unittest.skipIf(NODE is None, "Node.js not installed")
class J023CharacterStageTests(unittest.TestCase):
    def done(self, out: dict) -> None:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])

    # ------------------------------------------------------------------ B: re-check only what failed
    def test_character_recheck_reruns_what_failed_and_what_depends_on_it(self):
        # J024: the scripts (qa-lead) and the game-designer reviewer → the scripts are CAP-candidate-r1 (every round) and the qa-lead
        # suite always reruns; a game-designer repair (gameplay sheet) is not a visual, code or cost layer, so the art-director, the
        # reviewer and the performance-engineer (risk performance) are carried. The game-designer is no longer a reviewer.
        out = go(CHAR, {"blockLabelOnce": r"qa-lead: RV-candidate-r0", "maker": "game-designer"}, stage="build", risks=["performance"])
        self.done(out)
        got = out["labels"]
        fix = index(got, r"FIX-candidate-r0-game-designer")
        self.assertGreater(index(got, r"^studio-operator: CAP-candidate-r1$"), fix, "the capture and scripts run every round")
        self.assertGreater(index(got, r"^qa-lead: RV-candidate-r1-qa-lead"), fix, "the protected suite (and the reviewer that blocked) reruns")
        for kept in ("art-director", "reviewer", "performance-engineer"):
            self.assertEqual(index(got, rf"RV-candidate-r1-{kept}"), -1, kept)
            self.assertTrue(any(f"carried: {kept} (round 0, revision" in x for x in out["result"]["carried"]), kept)
        self.assertEqual(index(got, r"game-designer: RV-"), -1, "the game-designer is not a reviewer (J024 §4.4)")

    def test_character_code_repair_reruns_the_code_reviewer_only_where_code_matters(self):
        # J024: the game-designer review reruns after a wiring fix → the game-designer is not a reviewer; the job lead's integrated
        # review reruns instead (the wiring fires the cues), beside the reviewer; the performance-engineer is carried.
        out = go(CHAR, {"blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "feature-builder"}, stage="build", playable=True, risks=["performance"])
        self.done(out)
        got = out["labels"]
        fix = index(got, r"FIX-candidate-r0-feature-builder")
        self.assertGreater(index(got, r"^reviewer: RV-candidate-r1-reviewer"), fix)
        self.assertGreater(index(got, r"^art-director: RV-candidate-r1-"), fix, "the wiring is part of the integrated read")
        self.assertEqual(index(got, r"performance-engineer: RV-candidate-r1-"), -1)
        self.assertEqual(index(got, r"game-designer: RV-"), -1)

    def test_character_proof_recheck_is_selective(self):
        # J024: the proof recheck (RV-proof-r1) is removed with the proof; the same rule holds in the build chain: a rig repair is a
        # visual and cost layer, so the job lead and the performance-engineer rerun, the reviewer is carried; the animator refreezes.
        self.assertEqual(go(CHAR, stage="proof")["outcome"], NO_PROOF)
        out = go(CHAR, {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "character-rigger"}, stage="build", risks=["performance"])
        self.done(out)
        got = out["labels"]
        fix = index(got, r"FIX-candidate-r0-character-rigger")
        self.assertTrue(fix < index(got, r"^animator: REFREEZE-candidate-r0") < index(got, r"^studio-operator: CAP-candidate-r1$"), got)
        self.assertGreater(index(got, r"^art-director: RV-candidate-r1-"), fix, "a rig repair is a visual layer for the job lead")
        self.assertGreater(index(got, r"^performance-engineer: RV-candidate-r1-"), fix)
        self.assertEqual(index(got, r"reviewer: RV-candidate-r1-"), -1)
        self.assertEqual(len(out["result"]["carried"]), 1)
        self.assertIn("carried: reviewer (round 0, revision", out["result"]["carried"][0])

    def test_stage_recheck_reruns_what_failed_and_what_depends_on_it(self):
        # J024: FZ-candidate-r1, the qa-lead and the sound, game and VFX reviewers → after a sound repair the integrator refreezes
        # (FIX-candidate-r0-integrate) and CAP-candidate-r1 follows; the environment-designer and the performance-engineer (sources cost)
        # rerun, the art-director (newLook) is carried because sound is not a visual layer. The removed reviewers never run.
        out = go(STAGE, {"blockLabelOnce": r"environment-designer: RV-candidate-r0", "maker": "sound-designer"}, stage="build", newLook=True, risks=["performance"])
        self.done(out)
        got = out["labels"]
        fix = index(got, r"FIX-candidate-r0-sound-designer")
        self.assertTrue(fix < index(got, r"^environment-designer: FIX-candidate-r0-integrate") < index(got, r"^studio-operator: CAP-candidate-r1$"), got)
        for always in (r"^environment-designer: RV-candidate-r1-environment-designer", r"^performance-engineer: RV-candidate-r1-"):
            self.assertGreater(index(got, always), fix, always)
        self.assertEqual(index(got, r"art-director: RV-candidate-r1-"), -1)
        self.assertTrue(any("carried: art-director (round 0, revision" in x for x in out["result"]["carried"]))
        for removed in ("qa-lead", "game-designer", "sound-designer", "vfx-designer"):
            self.assertEqual(index(got, rf"^{removed}: RV-"), -1, removed)

    def test_stage_proof_recheck_is_selective(self):
        # J024: the proof recheck (PT-greybox-r1, PR-r1) is removed with the proof; in build a fresh capture runs every later round, the
        # reviewer that blocked reruns with the job lead (its area depends on sound), and exactly the art-director is carried.
        self.assertEqual(go(STAGE, stage="proof")["outcome"], NO_PROOF)
        out = go(STAGE, {"blockLabelOnce": r"live-ops-designer: RV-candidate-r0", "maker": "sound-designer"}, stage="build", newLook=True, risks=["event"])
        self.done(out)
        got = out["labels"]
        self.assertGreaterEqual(index(got, r"^studio-operator: CAP-candidate-r1$"), 0, "a fresh capture every later round")
        self.assertGreaterEqual(index(got, r"^live-ops-designer: RV-candidate-r1-live-ops-designer"), 0)
        self.assertGreaterEqual(index(got, r"^environment-designer: RV-candidate-r1-environment-designer"), 0)
        self.assertEqual(index(got, r"RV-candidate-r1-art-director"), -1)
        self.assertEqual(len(out["result"]["carried"]), 1)

    # ------------------------------------------------------------------ C: one needs step
    def test_character_needs_meeting_has_vfx_and_sound_from_the_start(self):
        # J024: NM-r1 and P1-sound-plan (proof) → N1-vfx-designer and N1-sound-designer run in direction in parallel with the other
        # crafts, each on the plan file only, and one merge by the job lead closes it before G1. Sound answers the VFX envelope in build
        # (B5-sound after B4-vfx, on its frame scripts); build reads the merged plan and never re-asks.
        out = go(CHAR, {"timeline": True}, stage="direction")
        self.done(out)
        got = out["labels"]
        merge = index(got, r"M-r1-merge")
        for craft in (r"^modeler: N1-modeler", r"^animator: N1-animator", r"^character-rigger: N1-character-rigger",
                      r"^vfx-designer: N1-vfx-designer", r"^sound-designer: N1-sound-designer"):
            self.assertTrue(0 < index(got, craft) < merge, craft)
            self.assertLess(span(out, craft)["end"], span(out, r"M-r1-merge")["start"], craft)
        self.assertEqual(index(got, r"N2-|M-r2-"), -1, "round 2 is skipped when round 1 is clean")
        self.assertEqual(sum(1 for x in got if "merge" in x), 1, "the job lead merges once")
        self.assertRegex(got[merge], r"^art-director:")
        b = go(CHAR, {"timeline": True, "dump": r"B4-vfx$|B5-sound$|B2-rig$"}, stage="build", size="M")
        self.done(b)
        self.assertGreater(span(b, r"B5-sound$")["start"], span(b, r"B4-vfx$")["end"], "sound answers the VFX envelope")
        self.assertEqual(index(b["labels"], r"N1-|N2-|merge"), -1)
        for d in b["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn("plan/character-sheet.md", d["prompt"])
                self.assertIn("never a new needs round", d["prompt"])

    def test_character_needs_round_2_runs_only_on_a_conflict(self):
        # J024: NM-r2 for all 5 crafts on any conflict → tables that conflict but that the merge settles run no N2; a conflict the merge
        # reports runs N2 only for the crafts named in it, then the second and last merge, still before G1 (the end of direction).
        settled = go(CHAR, {"conflicts": True}, stage="direction")
        self.done(settled)
        self.assertEqual(index(settled["labels"], r"N2-|M-r2-merge"), -1)
        conflict = [{"about": "the shoulder cut", "roles": ["character-rigger"], "rows": ["R3"], "why": "w"}]
        out = go(CHAR, {"set": {"unsettled_conflicts": conflict}}, stage="direction")
        self.done(out)
        got = ids(out)
        self.assertEqual([x for x in got if x.startswith("N2-")], ["N2-character-rigger"])
        self.assertEqual(sum(1 for x in got if "merge" in x), 2)
        self.assertEqual(got[-1], "M-r2-merge")
        self.assertGreater(got.index("M-r2-merge"), got.index("N2-character-rigger"))

    def test_stage_needs_meeting_merges_once(self):
        # J024: P3-needs and P3-merge (proof) → N1 tables and one merge in direction; N2 and M-r2-merge only on a reported conflict;
        # an M build starts with the place run and asks no craft again.
        clean = go(STAGE, {"conflicts": True}, stage="direction")
        self.done(clean)
        self.assertEqual(index(clean["labels"], r"N2-|M-r2-merge|route-merge"), -1, "a settled round 1 needs no round 2")
        self.assertEqual(sum(1 for x in clean["labels"] if re.search(r"merge", x)), 1)
        conflict = [{"about": "the cave floor", "roles": ["sound-designer"], "rows": ["S2"], "why": "w"}]
        out = go(STAGE, {"set": {"unsettled_conflicts": conflict}}, stage="direction")
        self.done(out)
        got = out["labels"]
        self.assertEqual([x for x in got if "N2-" in x], ["sound-designer: N2-sound-designer"])
        self.assertEqual(index(got, r"route-merge"), -1)
        self.assertTrue(index(got, r"N2-sound-designer") < index(got, r"^environment-designer: M-r2-merge") == len(got) - 1)
        m = go(STAGE, stage="build", size="M")
        self.done(m)
        self.assertEqual(m["labels"][0], "environment-designer: B1-place")
        self.assertEqual(index(m["labels"], r"N1-|N2-|needs"), -1)

    # ------------------------------------------------------------------ D: lighter direction
    def test_direction_proposals_from_choice_owners_limits_from_constraint_owners(self):
        # J024: D1 proposals, D1-limits and D3-synthesis → the job lead's D1 plan, the N1 needs and limits tables, one merge.
        cases = {CHAR: ["D1-plan", "N1-game-designer", "N1-character-rigger", "N1-animator", "N1-modeler", "N1-vfx-designer",
                        "N1-sound-designer", "N1-limits-architect", "M-r1-merge"],
                 STAGE: ["D1-plan", "N1-game-designer", "N1-modeler", "N1-vfx-designer", "N1-sound-designer", "M-r1-merge"]}
        for name, expected in cases.items():
            with self.subTest(script=name):
                out = go(name, stage="direction")
                self.done(out)
                self.assertEqual(sorted(ids(out)), sorted(expected), "no exchange without a conflict, no sign-off run")
                self.assertEqual(index(out["labels"], r"D1-(game|art|environment|limits)|D3-"), -1, "no proposals from other leads")

    def test_exchange_runs_only_for_the_leads_in_a_conflict(self):
        # J024: D2 exchange on direction_conflicts and D3-resolution → N2 for the crafts in the merge's unsettled_conflicts only, then
        # M-r2-merge; no sign-off run.
        cases = {CHAR: (["game-designer", "animator"], ["character-rigger", "modeler", "vfx-designer", "sound-designer"]),
                 STAGE: (["game-designer", "vfx-designer"], ["modeler", "sound-designer"])}
        for name, (inside, outside) in cases.items():
            with self.subTest(script=name):
                conflict = [{"about": "the signature action", "roles": inside, "rows": ["A1", "B1"], "why": "w"}]
                out = go(name, {"set": {"unsettled_conflicts": conflict}}, stage="direction")
                self.done(out)
                got = ids(out)
                for lead in inside:
                    self.assertIn(f"N2-{lead}", got)
                for lead in outside:
                    self.assertNotIn(f"N2-{lead}", got)
                self.assertEqual(got[-1], "M-r2-merge")
                self.assertEqual([x for x in got if re.search(r"sign-|D2-|D3-", x)], [])

    def test_each_lead_confirms_direction_in_its_first_hand_back_of_the_next_stage(self):
        # J024: the confirmation in the proof stage (S0-sheet, P1-route-graph) → each craft with a needs table confirms the merged plan
        # in its first build hand-back; later briefs of the same craft do not ask again; an incompatibility there is needs-decision.
        out = go(CHAR, {"dump": r"B1-model$|B3-animation$|FIX-candidate-r0-modeler|RECHECK-candidate-r0-rig|REFREEZE-",
                        "blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler"}, stage="build")
        self.done(out)
        briefs = {d["label"]: d["prompt"] for d in out["dumps"]}
        for first in ("modeler: B1-model", "animator: B3-animation"):
            self.assertIn("no sign-off run", briefs[first], first)
        for later in ("modeler: FIX-candidate-r0-modeler", "character-rigger: RECHECK-candidate-r0-rig", "animator: REFREEZE-candidate-r0"):
            self.assertNotIn("no sign-off run", briefs[later], later)
        for name, label in ((CHAR, r"B1-model$"), (STAGE, r"B3-ambience-sound$")):
            with self.subTest(script=name):
                stop = go(name, {"statusLabel": label, "status": "needs-decision"}, stage="build")
                self.assertEqual(stop["status"], "needs-decision", stop["outcome"])
                self.assertIn("incompatibility", stop["outcome"])

    # ------------------------------------------------------------------ E: no proof, M no bigger than L
    def test_m_build_runs_no_proof_calls_and_fewer_agents_than_l_proof_and_build(self):
        # J024: M build has no proof calls and fewer agents than L proof + build → no size has a proof stage (refused, 0 agents), no
        # build runs a proof-type call, and M direction + build is never bigger than L direction + build.
        proof_calls = {CHAR: r"blockout|P3-|RV-proof|RECAP-|lineup|proxy", STAGE: r"greybox|P5-|PR-r|PT-|blockout|paintover"}
        for name, pattern in proof_calls.items():
            with self.subTest(script=name):
                totals = {}
                for size in ("L", "M"):
                    proof = go(name, stage="proof", size=size)
                    self.assertEqual((proof["status"], proof["agents"]), ("blocked", 0))
                    d, b = go(name, stage="direction", size=size), go(name, stage="build", size=size)
                    self.done(d)
                    self.done(b)
                    self.assertEqual(index(b["labels"], pattern), -1, b["labels"])
                    totals[size] = d["agents"] + b["agents"]
                self.assertLessEqual(totals["M"], totals["L"])

    def test_m_direction_is_the_job_lead_alone_with_the_limits_sheets(self):
        # J024: M direction = the limits sheets and D3-synthesis → M direction has the shape of L (D1 plan with one direction and no look
        # options, the same N1 tables, one merge); only the D1 brief differs.
        for name in (CHAR, STAGE):
            with self.subTest(script=name):
                m = go(name, {"dump": r"D1-plan"}, stage="direction", size="M")
                large = go(name, stage="direction", size="L")
                self.done(m)
                self.done(large)
                self.assertEqual(sorted(ids(m)), sorted(ids(large)))
                self.assertEqual(ids(m)[0], "D1-plan")
                self.assertIn("no look options", m["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ F: captures on the studio-operator (Sonnet)
    def test_character_captures_run_on_the_studio_operator(self):
        # J024: S3-capture, S3-art-checkin, CAP-candidate, REFREEZE then CAP-...-fix and the proof captures → one studio-operator
        # CAP-candidate-r<n> (Sonnet) per review round; the animator refreezes after a model fix before the round-1 capture; the
        # behaviour test capture stays on the studio-operator; the Opus makers take no review captures.
        build = go(CHAR, {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler", "dump": ".*"}, stage="build")
        direction = go(CHAR, {"dump": r"D4-behaviour-capture"}, stage="direction", risks=["new-enemy"])
        self.done(build)
        self.done(direction)
        got = build["labels"]
        self.assertEqual(index(got, r"S3-|S7-|checkin"), -1)
        self.assertGreater(index(got, r"^studio-operator: CAP-candidate-r0$"), index(got, r"^animator: B3-animation$"))
        self.assertTrue(index(got, r"^animator: REFREEZE-candidate-r0") < index(got, r"^studio-operator: CAP-candidate-r1$") < index(got, r"^qa-lead: RV-candidate-r1-qa-lead"))
        self.assertEqual([x.split(": ")[0] for x in got if re.search(r": CAP-", x)], ["studio-operator", "studio-operator"], "one capture run per round")
        captures = [d for d in build["dumps"] + direction["dumps"] if re.search(r": (CAP-|D4-behaviour-capture)", d["label"])]
        self.assertEqual(len(captures), 3)
        for d in captures:
            with self.subTest(label=d["label"]):
                self.assertIn("to: studio-operator", d["prompt"])
                self.assertIn("model: sonnet", d["prompt"])
        for d in build["dumps"]:
            if re.search(r"(B1-model|B2-rig|B3-animation|REFREEZE-candidate-r0|FIX-candidate-r0-modeler)$", d["label"]):
                with self.subTest(label=d["label"]):
                    self.assertIn("model: opus", d["prompt"])
                    self.assertIn("do not take review captures", d["prompt"])


if __name__ == "__main__":
    unittest.main()
