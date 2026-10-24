"""Control-flow tests for the J024 flow in job-character.js and job-stage.js (knowledge/jobs/J024-flow-cuts-r2/design.md §1-7, §6 Character and Stage rows).

Kit test (universal). Author: J024 builder B · claude-opus-5-5 · default · 2026-10-24.
Uses the fake-agent harness through the helpers of tools/tests/test_job_workflows.py; skipped when Node is not installed.
§1: no proof stage and no G2 (a proof call is blocked before any agent). §2: no roughs (one run per craft, no rough labels).
§3: direction = D1 plan, N1 needs and limits tables on the plan file only (12 rows, omitted line), one merge, N2 and a second merge
only on a conflict the merge reports; each craft confirms the merged plan in its first build hand-back. §4: one capture-and-scripts
run (visual_flags, cue_log), the job lead's integrated review always, conditional reviewers by args, risks and flags; selective
recheck. §5a: capped repair and recheck briefs. §6: run-count ceilings. §7: newLook (stage) and the performance token (both).
Every test here fails on the J023 scripts (checked once by copying the J023 versions over these two scripts).
"""

from __future__ import annotations

import re
import unittest

try:
    from tools.tests.test_job_workflows import JOBS, NODE, index, run
except ImportError:   # unittest discovery with -t tools/tests (tools/verify.py)
    from test_job_workflows import JOBS, NODE, index, run

CHAR = "job-character.js"
STAGE = "job-stage.js"
COMMON = {"job": "J099-test", "studioId": "studio-1", "change": "make it slower", "images": ["content/art/refs/approved.png"], "size": "L", "risks": []}
ARGS = {CHAR: dict(COMMON, variant=False, playable=False, base="archer"), STAGE: dict(COMMON, newLook=False)}
NO_PROOF = "no proof stage (J024): direction → G1 → build → G3"
ROUGH = re.compile(r"blockout|greybox|proxy|rough|check-?in|paint-?over|light-variant|lineup|proof|blocking|polish|board|animatic|prototype|temp", re.I)
COLUMNS = "id | need or limit | from (role) | value or range, with unit | why (one line) | blocks build (yes/no)"


def go(name: str, scenario: dict | None = None, **changes) -> dict:
    args = dict(ARGS[name])
    args.update(changes)
    return run(JOBS / name, {k: v for k, v in args.items() if v is not None}, scenario)


def ids(out: dict) -> list[str]:
    return [label.split(": ", 1)[1] for label in out["labels"]]


def block(prompt: str, key: str) -> list[str]:
    """The list items of one brief key (inputs, refs, findings, previous_findings)."""
    lines = prompt.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"{key}:"):
            out = []
            for item in lines[i + 1:]:
                if not item.startswith("  - "):
                    break
                out.append(item[4:])
            return out
    return []


def dumped(out: dict, pattern: str) -> dict:
    hits = [d for d in out["dumps"] if re.search(pattern, d["label"])]
    if not hits:
        raise AssertionError(f"no dump matches {pattern}: {out['labels']}")
    return hits[0]


def reviewers(out: dict) -> set[str]:
    return {x.split(": ", 1)[0] for x in out["labels"] if ": RV-" in x}


def findings(n: int, maker: str) -> list[dict]:
    return [{"id": f"F{i}", "class": "blocking", "maker_role": maker, "where": "w", "expected": "e", "observed": "o",
             "evidence": f"knowledge/jobs/J099-test/captures/f{i}.png", "smallest_fix": "f"} for i in range(1, n + 1)]


@unittest.skipIf(NODE is None, "Node.js not installed")
class J024CharacterStageTests(unittest.TestCase):
    def done(self, out: dict) -> None:
        self.assertEqual(out["violation"], "")
        self.assertEqual(out["status"], "done", out["outcome"])

    # ------------------------------------------------------------------ §1 no proof stage, no G2
    def test_proof_stage_is_refused_before_any_agent(self):
        for name in (CHAR, STAGE):
            for size in ("L", "M"):
                with self.subTest(script=name, size=size):
                    out = go(name, stage="proof", size=size)
                    self.assertEqual(out["status"], "blocked")
                    self.assertEqual(out["agents"], 0)
                    self.assertEqual(out["outcome"], NO_PROOF)

    def test_no_g2_and_no_proof_phase_anywhere(self):
        for name in (CHAR, STAGE):
            for stage in ("direction", "build", "repair"):
                with self.subTest(script=name, stage=stage):
                    out = go(name, {"dump": ".*"}, stage=stage, **({"playable": True} if name == CHAR else {"newLook": True}))
                    self.done(out)
                    self.assertNotIn("G2", out["outcome"])
                    for d in out["dumps"]:
                        self.assertNotIn("G2", d["prompt"], d["label"])
                        self.assertNotRegex(d["prompt"], r"stage proof|the proof stage of|approved proof", d["label"])
                    titles = [p["title"] for p in out["meta"]["phases"]]
                    self.assertEqual([t for t in titles if re.search(r"proof|greybox|blockout|check-in|light", t, re.I)], [], titles)

    # ------------------------------------------------------------------ §3 direction: plan, needs, merge
    def test_direction_is_plan_then_needs_then_one_merge(self):
        crafts = ["N1-game-designer", "N1-character-rigger", "N1-animator", "N1-modeler", "N1-vfx-designer", "N1-sound-designer"]
        cases = [
            (CHAR, {}, crafts),
            (CHAR, {"playable": True}, crafts + ["N1-limits-architect"]),
            (CHAR, {"size": "M"}, crafts),
            (CHAR, {"variant": True}, crafts[:4]),
            (STAGE, {}, ["N1-game-designer", "N1-modeler", "N1-vfx-designer", "N1-sound-designer"]),
            (STAGE, {"size": "M"}, ["N1-game-designer", "N1-modeler", "N1-vfx-designer", "N1-sound-designer"]),
            (STAGE, {"risks": ["performance"], "newLook": True}, ["N1-game-designer", "N1-modeler", "N1-vfx-designer", "N1-sound-designer", "N1-limits-performance-engineer", "N1-limits-art-director"]),
        ]
        for name, args, needs in cases:
            with self.subTest(script=name, args=args):
                out = go(name, stage="direction", **args)
                self.done(out)
                got = ids(out)
                self.assertEqual(got[0], "D1-plan")
                self.assertEqual(got[-1], "M-r1-merge")
                self.assertEqual(sorted(got[1:-1]), sorted(needs))
                lead = "art-director" if name == CHAR else "environment-designer"
                self.assertEqual(out["labels"][0], f"{lead}: D1-plan")
                self.assertEqual(out["labels"][-1], f"{lead}: M-r1-merge")
                self.assertLessEqual(out["maxConcurrent"], 5)

    def test_needs_briefs_cite_only_the_plan_and_keep_the_data_limit(self):
        for name, plan in ((CHAR, "plan/character-sheet.md@rev"), (STAGE, "blueprint.md@rev")):
            with self.subTest(script=name):
                out = go(name, {"dump": r"N1-|M-r1-merge"}, stage="direction", **({"playable": True} if name == CHAR else {"risks": ["performance"], "newLook": True}))
                self.done(out)
                needs = [d for d in out["dumps"] if ": N1-" in d["label"]]
                self.assertGreaterEqual(len(needs), 4)
                for d in needs:
                    with self.subTest(label=d["label"]):
                        inputs = block(d["prompt"], "inputs")
                        self.assertEqual(len(inputs), 1, inputs)
                        self.assertIn(plan, inputs[0])
                        for text in ("at most 12 rows", "omitted:", "templates/jobs/needs-table.md", COLUMNS, "never another craft's needs or limits table"):
                            self.assertIn(text, d["prompt"])
                merge = block(dumped(out, r"M-r1-merge")["prompt"], "inputs")
                for d in needs:
                    role = d["label"].split(": ", 1)[0]
                    self.assertTrue(any(f"needs/{role}.md" in x for x in merge), (role, merge))

    def test_second_needs_round_only_on_a_conflict_the_merge_reports(self):
        cases = {CHAR: ["character-rigger", "animator"], STAGE: ["game-designer", "sound-designer"]}
        for name, inside in cases.items():
            with self.subTest(script=name):
                clean = go(name, stage="direction")
                self.done(clean)
                self.assertEqual(index(clean["labels"], r"N2-|M-r2-merge"), -1)
                conflict = [{"about": "a shared row", "roles": inside, "rows": ["X1", "Y2"], "why": "w"}]
                out = go(name, {"set": {"unsettled_conflicts": conflict}, "dump": r"N2-"}, stage="direction")
                self.done(out)
                got = ids(out)
                self.assertEqual(sorted(x for x in got if x.startswith("N2-")), sorted(f"N2-{r}" for r in inside))
                self.assertEqual(got[-1], "M-r2-merge")
                self.assertGreater(got.index("M-r2-merge"), max(got.index(f"N2-{r}") for r in inside))
                self.assertEqual(sum(1 for x in got if "merge" in x), 2, "never more than 2 needs rounds")
                for d in out["dumps"]:
                    self.assertEqual(len(block(d["prompt"], "inputs")), 1, d["label"])
                    self.assertIn("conflicting_rows:", d["prompt"])
                self.assertEqual(out["result"]["g1"]["needs_rounds"], 2)

    def test_crafts_confirm_the_merged_plan_in_their_first_build_hand_back(self):
        firsts = {CHAR: ["modeler: B1-model", "character-rigger: B2-rig", "animator: B3-animation", "vfx-designer: B4-vfx", "sound-designer: B5-sound"],
                  STAGE: ["vfx-designer: B2-ambience-vfx", "sound-designer: B3-ambience-sound", "modeler: B4-kit"]}
        for name, labels in firsts.items():
            with self.subTest(script=name):
                out = go(name, {"dump": ".*", "set": {"kit_piece_ids": ["k1"]}, "blockLabelOnce": r"RV-candidate-r0", "maker": "vfx-designer"}, stage="build")
                self.done(out)
                briefs = {d["label"]: d["prompt"] for d in out["dumps"]}
                for label in labels:
                    self.assertIn("Merged plan (no sign-off run, J024)", briefs[label], label)
                self.assertNotIn("Merged plan (no sign-off run, J024)", briefs["vfx-designer: FIX-candidate-r0-vfx-designer"])
                first = labels[1] if name == CHAR else labels[0]
                stop = go(name, {"statusLabel": re.escape(first.split(": ")[1]) + "$", "status": "needs-decision"}, stage="build")
                self.assertEqual(stop["status"], "needs-decision")
                self.assertIn("incompatibility", stop["outcome"])

    # ------------------------------------------------------------------ §2 and §4.1-4.2: one run per craft, no roughs
    def test_build_runs_each_craft_once_in_dependency_order(self):
        out = go(CHAR, stage="build", playable=True)
        self.done(out)
        got = ids(out)
        order = ["B0-reference-set", "B1-model", "B2-rig", "B3-animation", "B4-vfx", "B5-sound", "B6-wiring", "CAP-candidate-r0"]
        self.assertEqual([x for x in got if x in order], order)
        roles = [x.split(": ", 1)[0] for x in out["labels"]]
        for role in ("modeler", "character-rigger", "animator", "vfx-designer", "sound-designer", "feature-builder", "studio-operator"):
            self.assertEqual(roles.count(role), 1, role)
        self.assertEqual(roles.count("art-director"), 2, "the reference set and the integrated review")
        st = go(STAGE, stage="build")
        self.done(st)
        sg = ids(st)
        sroles = [x.split(": ", 1)[0] for x in st["labels"]]
        for role in ("vfx-designer", "sound-designer", "studio-operator"):
            self.assertEqual(sroles.count(role), 1, role)
        self.assertEqual(sroles.count("environment-designer"), 3, "build, integrate and freeze, the integrated review")
        self.assertLess(sg.index("B2-ambience-vfx"), sg.index("B3-ambience-sound"))
        self.assertLess(sg.index("B3-ambience-sound"), sg.index("B5-integrate"))
        self.assertLess(sg.index("B5-integrate"), sg.index("CAP-candidate-r0"))

    def test_no_rough_or_check_in_runs(self):
        runs = [(CHAR, {}, s) for s in ("direction", "build", "repair")] + [
            (CHAR, {"size": "M"}, "build"), (CHAR, {"playable": True, "risks": ["new-enemy"]}, "direction"), (CHAR, {"playable": True}, "build"),
            (CHAR, {"variant": True}, "build"), (STAGE, {}, "direction"), (STAGE, {}, "build"), (STAGE, {"size": "M"}, "build"),
            (STAGE, {"newLook": True}, "build"), (STAGE, {}, "repair")]
        for name, args, stage in runs:
            with self.subTest(script=name, args=args, stage=stage):
                out = go(name, {"set": {"kit_piece_ids": ["k1"], "geometry_changed": True}}, stage=stage, **args)
                self.done(out)
                self.assertEqual([x for x in ids(out) if ROUGH.search(x)], [])

    # ------------------------------------------------------------------ §4.3-4.4: capture and scripts, the reviewer table
    def test_one_capture_and_scripts_run_hands_back_flags_and_cue_log(self):
        for name, scripts in ((CHAR, ("model_audit.py", "rig_audit.py", "clip_check.py", "look_check.py", "tools/verify.py")),
                              (STAGE, ("scene_audit.py", "look_check.py"))):
            with self.subTest(script=name):
                out = go(name, {"dump": r"CAP-candidate-r0$|RV-candidate-r0-(art-director|environment-designer)$"}, stage="build")
                self.done(out)
                cap = dumped(out, r"CAP-candidate-r0$")
                self.assertTrue(cap["label"].startswith("studio-operator: "))
                self.assertIn("model: sonnet", cap["prompt"])
                for key in ("visual_flags", "cue_log", "findings"):
                    self.assertIn(key, cap["returned"])
                for s in scripts:
                    self.assertIn(s, cap["prompt"])
                lead = dumped(out, r"RV-candidate-r0-")
                for text in ("look_check.py", "phone size", "cue_log: [", "visual_flags: ["):
                    self.assertIn(text, lead["prompt"])
                self.assertEqual(sum(1 for x in out["labels"] if x.startswith("studio-operator: ")), 1)

    def test_character_reviewer_table(self):
        cases = [
            ({}, {"art-director"}),
            ({"playable": True}, {"art-director", "reviewer", "qa-lead"}),
            ({"risks": ["performance"]}, {"art-director", "performance-engineer"}),
            ({"variant": True, "risks": ["sold-variant"]}, {"art-director", "qa-lead"}),
            ({"risks": ["event"]}, {"art-director", "live-ops-designer"}),
        ]
        for args, expected in cases:
            with self.subTest(args=args):
                out = go(CHAR, stage="build", **args)
                self.done(out)
                self.assertEqual(reviewers(out), expected)
        off = go(CHAR, stage="build")
        self.assertIn("performance-engineer review (review chain): risks does not name performance", off["result"]["skipped_slots"])
        sold = go(CHAR, stage="build", variant=True, risks=["sold-variant"])
        self.assertGreaterEqual(index(sold["labels"], r"^qa-lead: RV-candidate-r0-pf13$"), 0)
        event = go(CHAR, stage="build", risks=["event"])
        self.assertLess(index(event["labels"], r"CAP-candidate-r0-event$"), index(event["labels"], r"live-ops-designer: RV-candidate-r0"))

    def test_stage_reviewer_table(self):
        cases = [
            ({}, None, {"environment-designer"}),
            ({"newLook": True}, None, {"environment-designer", "art-director"}),
            ({}, {"set": {"visual_flags": ["first view value 0.04 under the 0.08 floor"]}}, {"environment-designer", "art-director"}),
            ({"risks": ["performance"]}, None, {"environment-designer", "performance-engineer"}),
            ({"risks": ["event"]}, None, {"environment-designer", "live-ops-designer"}),
        ]
        for args, scenario, expected in cases:
            with self.subTest(args=args, scenario=scenario):
                out = go(STAGE, scenario, stage="build", **args)
                self.done(out)
                self.assertEqual(reviewers(out), expected)
        off = go(STAGE, stage="build")
        self.assertIn("performance-engineer review (risks has no performance)", off["result"]["skipped_slots"])

    def test_a_scripts_fail_stops_the_other_reviews(self):
        for name, maker in ((CHAR, "animator"), (STAGE, "environment-designer")):
            with self.subTest(script=name):
                out = go(name, {"blockLabelOnce": r"CAP-candidate-r0$", "maker": maker}, stage="build")
                self.done(out)
                got = ids(out)
                self.assertEqual(index(out["labels"], r"RV-candidate-r0-"), -1)
                self.assertLess(got.index(f"FIX-candidate-r0-{maker}"), got.index("CAP-candidate-r1"))
                self.assertGreaterEqual(index(out["labels"], r"RV-candidate-r1-"), 0, "reviewers with no verdict yet run in round 1")

    # ------------------------------------------------------------------ §4.5 selective recheck with the new chain
    def test_character_recheck_reruns_what_failed_and_what_depends_on_it(self):
        out = go(CHAR, {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "vfx-designer"}, stage="build", playable=True, risks=["performance"])
        self.done(out)
        got = ids(out)
        fix = got.index("FIX-candidate-r0-vfx-designer")
        for again in ("CAP-candidate-r1", "RV-candidate-r1-qa-lead", "RV-candidate-r1-art-director", "RV-candidate-r1-performance-engineer"):
            self.assertGreater(got.index(again), fix, again)
        self.assertNotIn("RV-candidate-r1-reviewer", got)
        self.assertTrue(any("carried: reviewer (round 0, revision" in x for x in out["result"]["carried"]))
        code = go(CHAR, {"blockLabelOnce": r"reviewer: RV-candidate-r0", "maker": "feature-builder"}, stage="build", playable=True, risks=["performance"])
        self.done(code)
        self.assertIn("RV-candidate-r1-reviewer", ids(code))
        self.assertNotIn("RV-candidate-r1-performance-engineer", ids(code))
        self.assertTrue(any("carried: performance-engineer (round 0" in x for x in code["result"]["carried"]))
        geo = go(CHAR, {"blockLabelOnce": r"art-director: RV-candidate-r0", "maker": "modeler"}, stage="build")
        self.done(geo)
        g = ids(geo)
        self.assertTrue(g.index("FIX-candidate-r0-modeler") < g.index("RECHECK-candidate-r0-rig") < g.index("REFREEZE-candidate-r0") < g.index("CAP-candidate-r1"))

    def test_stage_recheck_reruns_what_failed_and_what_depends_on_it(self):
        out = go(STAGE, {"blockLabelOnce": r"environment-designer: RV-candidate-r0", "maker": "game-designer"}, stage="build", newLook=True, risks=["performance"])
        self.done(out)
        got = ids(out)
        fix = got.index("FIX-candidate-r0-game-designer")
        self.assertGreater(got.index("CAP-candidate-r1"), fix)
        self.assertGreater(got.index("RV-candidate-r1-environment-designer"), fix)
        for kept in ("art-director", "performance-engineer"):
            self.assertNotIn(f"RV-candidate-r1-{kept}", got)
            self.assertTrue(any(f"carried: {kept} (round 0, revision" in x for x in out["result"]["carried"]), kept)
        fx = go(STAGE, {"blockLabelOnce": r"environment-designer: RV-candidate-r0", "maker": "vfx-designer"}, stage="build", newLook=True, risks=["performance"])
        self.done(fx)
        f = ids(fx)
        self.assertTrue(f.index("FIX-candidate-r0-vfx-designer") < f.index("FIX-candidate-r0-integrate") < f.index("CAP-candidate-r1"))
        for again in ("RV-candidate-r1-environment-designer", "RV-candidate-r1-art-director", "RV-candidate-r1-performance-engineer"):
            self.assertIn(again, f)

    # ------------------------------------------------------------------ §5a capped repair and recheck briefs
    def test_repair_briefs_are_capped(self):
        for name, maker in ((CHAR, "modeler"), (STAGE, "vfx-designer")):
            with self.subTest(script=name):
                out = go(name, {"set": {"findings": findings(12, maker)}, "dump": rf"FIX-candidate-r0-{maker}$"}, stage="build")
                d = dumped(out, rf"FIX-candidate-r0-{maker}$")
                prompt = d["prompt"]
                self.assertEqual(len(block(prompt, "findings")), 10)
                omitted = [x for x in prompt.splitlines() if x.startswith("omitted:")]
                self.assertEqual(len(omitted), 1)
                self.assertIn("F11", omitted[0])
                self.assertIn("F12", omitted[0])
                self.assertIn("lower rank, sent next round if still open", omitted[0])
                self.assertRegex(prompt, r"(?m)^changed_parts: \[")
                self.assertRegex(prompt, r"(?m)^protected: \[")
                self.assertLessEqual(len(prompt.split()), 1500)
                self.assertEqual([x for x in block(prompt, "inputs") if "/reviews/" in x], [], "never the other reviewers' review files")
                for f in block(prompt, "findings"):
                    for key in ('"id"', '"expected"', '"observed"', '"evidence"'):
                        self.assertIn(key, f)
                one = go(name, {"blockLabelOnce": r"RV-candidate-r0", "maker": maker, "dump": r"FIX-candidate-r0-|RV-candidate-r1-"}, stage="build")
                self.done(one)
                fixp = dumped(one, rf"FIX-candidate-r0-{maker}$")["prompt"]
                self.assertEqual([x for x in fixp.splitlines() if x.startswith("omitted:")], ["omitted: none (lower rank, sent next round if still open)"])
                recheck = dumped(one, r"RV-candidate-r1-(art-director|environment-designer)$")["prompt"]
                self.assertEqual(len(block(recheck, "previous_findings")), 1)
                self.assertRegex(recheck, r"(?m)^changed_parts: \[")
                self.assertEqual(sum(1 for x in recheck.splitlines() if x.startswith("omitted:")), 1)

    # ------------------------------------------------------------------ §6 conditional crafts, each switch on and off
    def test_conditional_crafts_switch_on_and_off(self):
        off = go(CHAR, stage="build")
        on = go(CHAR, stage="build", playable=True)
        for out in (off, on):
            self.done(out)
        self.assertNotIn("B6-wiring", ids(off))
        self.assertIn("B6-wiring", ids(on))
        palette = go(CHAR, stage="build", variant=True)
        shaped = go(CHAR, {"set": {"geometry_changed": True}}, stage="build", variant=True)
        self.done(palette)
        self.done(shaped)
        self.assertNotIn("B2-rig", ids(palette), "a palette-only variant skips the rig run")
        self.assertIn("B2-rig", ids(shaped))
        for out in (palette, shaped):
            self.assertEqual(index(out["labels"], r"B4-vfx|B5-sound"), -1, "variant mode keeps its skips")
        clips = go(CHAR, {"set": {"geometry_changed": True, "new_moving_parts": True}, "dump": r"B3-animation$"}, stage="build", variant=True)
        self.assertIn("only the motion of the new moving parts", dumped(clips, r"B3-animation$")["prompt"])
        noclip = go(CHAR, {"set": {"geometry_changed": True}, "dump": r"B3-animation$"}, stage="build", variant=True)
        self.assertNotIn("only the motion of the new moving parts", dumped(noclip, r"B3-animation$")["prompt"])
        nokit = go(STAGE, stage="build")
        kit = go(STAGE, {"set": {"kit_piece_ids": ["arch-01"]}}, stage="build")
        self.done(nokit)
        self.done(kit)
        self.assertEqual(index(nokit["labels"], r"^modeler: "), -1)
        k = ids(kit)
        self.assertTrue(k.index("B1-place") < k.index("B4-kit") < k.index("B5-integrate"))
        merged = go(STAGE, {"set": {"conditional_crafts": ["modeler"]}}, stage="direction")
        self.assertEqual(merged["result"]["g1"]["conditional_crafts"], ["modeler"])

    # ------------------------------------------------------------------ §7 args: newLook, performance, images and studioId
    def test_new_args(self):
        for stage in ("direction", "build", "repair"):
            with self.subTest(stage=stage):
                for bad in ({"newLook": None}, {"newLook": "no"}, {"newLook": True, "size": "M"}):
                    out = go(STAGE, stage=stage, **bad)
                    self.assertEqual((out["status"], out["agents"]), ("blocked", 0), bad)
                    self.assertTrue(any("newLook" in x or "size L" in x for x in out["result"]["required"]))
        for name in (CHAR, STAGE):
            with self.subTest(script=name):
                self.done(go(name, stage="build", risks=["performance"]))
                self.assertEqual(go(name, stage="build", risks=["speed"])["agents"], 0)
                for stage in ("build", "repair"):
                    for arg in ("images", "studioId"):
                        out = go(name, stage=stage, **{arg: None})
                        self.assertEqual((out["status"], out["agents"]), ("blocked", 0), (stage, arg))
                self.done(go(name, stage="direction", studioId=None, images=None))
        self.assertEqual(go(CHAR, stage="direction", studioId=None, risks=["new-enemy"])["status"], "blocked")

    def test_run_count_ceilings(self):
        def total(name, **args):
            n = 0
            for stage in ("direction", "build"):
                out = go(name, stage=stage, **args)
                self.done(out)
                n += out["agents"]
            return n
        self.assertLessEqual(total(CHAR), 16)
        self.assertLessEqual(total(CHAR, playable=True), 20)
        self.assertLessEqual(total(CHAR, size="M"), total(CHAR))
        self.assertLessEqual(total(CHAR, size="M", playable=True), total(CHAR, playable=True))
        self.assertLessEqual(total(STAGE), 12)
        self.assertLessEqual(total(STAGE, size="M"), total(STAGE))

    def test_dead_agent_is_never_a_pass(self):
        for name, label in ((CHAR, r"CAP-candidate-r0$"), (CHAR, r"N1-modeler$"), (STAGE, r"CAP-candidate-r0$"), (STAGE, r"N1-sound-designer$"), (STAGE, r"B2-ambience-vfx$")):
            with self.subTest(script=name, label=label):
                stage = "direction" if "N1-" in label else "build"
                out = go(name, {"nullLabel": label}, stage=stage)
                self.assertEqual(out["status"], "failed", out["outcome"])
                self.assertGreaterEqual(index(out["labels"], label), 0)


if __name__ == "__main__":
    unittest.main()
