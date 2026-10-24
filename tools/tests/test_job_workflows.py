"""Control-flow tests for the saved job workflows (.agents/workflows/jobs/*.js) with fake agents (no tokens).

Kit test (universal). Author: orchestrator · claude-opus-5-5 · high · 2026-10-21 (J016); revised by workflow-fixer W3 ·
claude-opus-5-5 · high · 2026-10-21, J016 G3 (audit fixes: auditor B F1-F16 and R1-R13, auditor E TT-02..TT-12, lead decisions LD1-LD15);
revised by J024 test updater · claude-opus-5-5 · default · 2026-10-24 (J024 flow: knowledge/jobs/J024-flow-cuts-r2/design.md; no proof stage).
Runs tools/workflows/wf_harness.mjs under Node; skipped when Node is not installed.
Every workflow must: refuse bad or missing args before any agent starts (no silent defaults); run each stage to `done` with clean
fakes; keep the harness contract on every agent() call (role, model on its tier, effort, the hand-back schema of
templates/jobs/handback.schema.json, a well-formed brief, at most 5 agents at once, one Studio driver, one Blender user and one browser
user at a time); stop with `needs-decision` when review findings never clear; never count a dead agent as a pass.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
JOBS = ROOT / ".agents" / "workflows" / "jobs"
HARNESS = ROOT / "tools" / "workflows" / "wf_harness.mjs"
TEMPLATE = ROOT / "templates" / "jobs" / "handback.schema.json"
NODE = shutil.which("node")
# J024: the proof stage is gone (design §1); `stage: "proof"` is refused in every type (test_the_proof_stage_is_refused_everywhere).
STAGES = ("direction", "build", "repair")
LATER = ("build", "repair")

# Complete args per workflow (the README args table); every test starts from these and changes one thing.
BASE = {"job": "J099-test", "studioId": "studio-1", "change": "make it slower", "images": ["content/art/refs/approved.png"], "size": "L",
        "risks": []}
EXTRA = {
    "job-cutscene.js": {"newLook": False, "ui": False},   # J024 §7: newLook required; ui = the direction result's build_args.ui
    "job-character.js": {"variant": False, "playable": True, "base": "archer"},
    "job-stage.js": {"newLook": False},                  # J024 §7: newLook required
    "job-ui-screen.js": {"shop": True, "newLook": False},
    "job-feature.js": {"money": True, "numbers": True},
    "job-effect.js": {"newLook": False, "animated": True},
    "job-marketing-art.js": {"piece": "thumbnails", "launch": False},
}
# Lead decision LD9: args that switch rules or gates, and the stages that need them (a missing one is `blocked`, 0 agents).
REQUIRED = {
    "job-cutscene.js": {"size": STAGES, "risks": STAGES, "newLook": STAGES, "ui": ("build",), "studioId": LATER, "images": LATER,
                        "change": ("repair",)},
    "job-character.js": {"size": STAGES, "risks": STAGES, "variant": STAGES, "playable": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-stage.js": {"size": STAGES, "risks": STAGES, "newLook": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-ui-screen.js": {"size": STAGES, "risks": STAGES, "shop": STAGES, "newLook": STAGES, "images": LATER, "studioId": ("build", "repair"), "change": ("repair",)},
    "job-feature.js": {"size": STAGES, "risks": STAGES, "money": STAGES, "numbers": STAGES, "studioId": LATER, "change": ("repair",)},
    "job-effect.js": {"size": STAGES, "risks": STAGES, "newLook": STAGES, "animated": STAGES, "studioId": LATER, "images": LATER, "change": ("repair",)},
    "job-marketing-art.js": {"size": STAGES, "risks": STAGES, "piece": STAGES, "launch": STAGES, "images": LATER, "change": ("repair",)},
}
# A maker each workflow routes repairs to (for the bounded-rounds test).
MAKER = {"job-cutscene.js": "vfx-designer", "job-character.js": "modeler", "job-stage.js": "environment-designer",
         "job-ui-screen.js": "ui-ux-designer", "job-feature.js": "game-designer", "job-effect.js": "vfx-designer",
         "job-marketing-art.js": "marketing"}
# A creative review label pattern per workflow, used to kill one review (R1).
# J024: the art-director reviews only with newLook / launch / visual_flags (design §4.4) → the review killed is the job lead's
# integrated review, which runs in every type and every round 0.
REVIEW = {"job-cutscene.js": r"film-director: RV-candidate-r0", "job-character.js": r"art-director: RV-candidate-r0",
          "job-stage.js": r"environment-designer: RV-candidate-r0", "job-ui-screen.js": r"ui-ux-designer: RV-candidate-r0",
          "job-feature.js": r"game-designer: RV-candidate-r0", "job-effect.js": r"vfx-designer: RV-candidate-r0",
          "job-marketing-art.js": r"marketing: RV-candidate-r0"}
# J024 design §3.3: the job lead's merge writes direction.md (it replaces the D3 synthesis). Marketing has a merge only when a
# limits table exists (launch: the art-director's), so its case runs with launch true.
MERGE = {"job-cutscene.js": r"film-director: M1-merge", "job-character.js": r"art-director: M-r1-merge",
         "job-stage.js": r"environment-designer: M-r1-merge", "job-ui-screen.js": r"ui-ux-designer: D3-merge",
         "job-feature.js": r"game-designer: D3-merge", "job-effect.js": r"vfx-designer: M1-merge",
         "job-marketing-art.js": r"marketing: D3-merge"}
MERGE_ARGS = {"job-marketing-art.js": {"launch": True}}
# J024 design §2: labels of the removed rough, proof and check-in passes; none may run in any stage of any type.
ROUGH = re.compile(r"rough|temp-|proto|blocking|greybox|proxy|strip|board|animatic|check-?in|polish|proof|greenlight|: P\d|: PR-|"
                   r"RECAP-|: PT-", re.I)


def run(script: Path | str, args: dict, scenario: dict | None = None) -> dict:
    script = JOBS / script if isinstance(script, str) else script
    proc = subprocess.run(
        [NODE, str(HARNESS), str(script), json.dumps(args), json.dumps(scenario or {})],
        capture_output=True, text=True, timeout=120, encoding="utf-8",
    )
    if proc.returncode not in (0, 1) or not proc.stdout.strip():
        raise AssertionError(f"{script.name}: harness error {proc.returncode}: {proc.stderr.strip()}")
    return json.loads(proc.stdout.strip().splitlines()[-1])


def full(name: str, **changes) -> dict:
    a = dict(BASE, **EXTRA[name])
    a.update(changes)
    return {k: v for k, v in a.items() if v is not None}


def index(labels: list[str], pattern: str) -> int:
    for i, label in enumerate(labels):
        if re.search(pattern, label):
            return i
    return -1


def span(out: dict, pattern: str) -> dict:
    hits = [t for t in out["timeline"] if re.search(pattern, t["label"])]
    if not hits:
        raise AssertionError(f"no call matches {pattern}: {out['labels']}")
    return hits[0]


@unittest.skipIf(NODE is None, "Node.js not installed")
class JobWorkflowTests(unittest.TestCase):
    def scripts(self) -> list[Path]:
        found = sorted(JOBS.glob("*.js"))
        self.assertTrue(found, "no job workflows found")
        self.assertEqual({p.name for p in found}, set(EXTRA), "a workflow was added or removed: update EXTRA and REQUIRED")
        return found

    def runs(self, jobs: list[tuple]) -> list[dict]:
        with ThreadPoolExecutor(max_workers=8) as pool:
            return list(pool.map(lambda j: run(*j), jobs))

    # ------------------------------------------------------------------ args (LD9, R2, R7, F14)
    def test_bad_args_are_refused_before_any_agent(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, {"job": "J099-test"})
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["agents"], 0)

    def test_required_args_are_never_silently_defaulted(self):
        jobs, keys = [], []
        for script in self.scripts():
            for arg, stages in REQUIRED[script.name].items():
                for stage in stages:
                    jobs.append((script, full(script.name, stage=stage, **{arg: None})))
                    keys.append((script.name, arg, stage))
        for (name, arg, stage), out in zip(keys, self.runs(jobs)):
            with self.subTest(script=name, arg=arg, stage=stage):
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertEqual(out["agents"], 0)
                self.assertIn(arg, out["outcome"])
                self.assertIn(arg, out["meta"]["whenToUse"], "whenToUse must name every required arg")

    def test_a_look_change_is_never_sized_m(self):
        for name in ("job-ui-screen.js", "job-effect.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build", size="M", newLook=True))
                self.assertEqual(out["status"], "blocked")
                self.assertEqual(out["agents"], 0)
                self.assertIn("sized L", out["outcome"])

    # ------------------------------------------------------------------ clean runs and the harness contract
    def test_every_stage_runs_clean_with_well_formed_briefs(self):
        jobs, keys = [], []
        for script in self.scripts():
            for stage in STAGES:
                for scen in ({}, {"uniform": True}, {"greybox": True, "conflicts": True, "refuseSign": True}):
                    jobs.append((script, full(script.name, stage=stage), scen))
                    keys.append((script.name, stage, json.dumps(scen)))
        for (name, stage, scen), out in zip(keys, self.runs(jobs)):
            with self.subTest(script=name, stage=stage, scenario=scen):
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertGreater(out["agents"], 0)
                self.assertLessEqual(out["maxConcurrent"], 5, "rules/company.md §9: at most 5 agents per stage")

    def test_medium_build_has_no_proof_stage(self):
        # J024: "M build runs no proof calls and fewer agents than L proof + build" → no proof in any size: stage proof is refused
        # before any agent in L and M, no stage runs a rough/proof/check-in label, the build is the same for both sizes and
        # M direction + build <= L direction + build (design §1, §2).
        for script in self.scripts():
            with self.subTest(script=script.name):
                for size in ("L", "M"):
                    proof = run(script, full(script.name, stage="proof", size=size))
                    self.assertEqual(proof["status"], "blocked", proof["outcome"])
                    self.assertEqual(proof["agents"], 0)
                    self.assertIn("no proof stage (J024)", proof["outcome"])
                total = {}
                for size in ("L", "M"):
                    outs = [run(script, full(script.name, stage=stage, size=size)) for stage in ("direction", "build")]
                    for out in outs:
                        self.assertEqual(out["violation"], "")
                        self.assertEqual(out["status"], "done", out["outcome"])
                        self.assertEqual([x for x in out["labels"] if ROUGH.search(x)], [], f"{size} runs no rough or proof calls")
                    total[size] = (outs[0]["agents"], outs[1]["agents"], outs[1]["labels"])
                self.assertEqual(total["M"][2], total["L"][2], "build is the same for L and M (design §1)")
                self.assertLessEqual(total["M"][0] + total["M"][1], total["L"][0] + total["L"][1])

    def test_the_proof_stage_is_refused_everywhere(self):
        # J024 design §1: `stage: "proof"` is refused before any agent and before any other arg check, with the J024 reason.
        for script in self.scripts():
            for args in (full(script.name, stage="proof"), {"job": "J099-test", "stage": "proof"}):
                with self.subTest(script=script.name, complete=len(args) > 2):
                    out = run(script, args)
                    self.assertEqual(out["status"], "blocked", out["outcome"])
                    self.assertEqual(out["agents"], 0)
                    self.assertIn("no proof stage (J024): direction → G1 → build → G3", out["outcome"])

    def test_handback_schema_matches_the_template(self):
        template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        props = list(template["properties"])
        self.assertIn("docs_read", template["required"])
        self.assertNotIn("lesson", template["required"], "the lesson draft is optional (LD11)")
        self.assertLess(props.index("docs_read"), props.index("status"))
        self.assertEqual(props[-2:], ["status", "outcome"], "evidence fields come before the answer fields")
        # The harness fails any agent() call whose schema differs from the template; the clean-run test covers every call.

    def test_a_blocked_step_stops_the_stage(self):
        # Smoke run 2026-10-21: every direction lead returned blocked and the stage still reported the direction sheet ready.
        for script in self.scripts():
            with self.subTest(script=script.name):
                # J024: "no synthesis on missing proposals" → no needs tables and no merge on a blocked D1 plan (design §3).
                out = run(script, full(script.name, stage="direction", **MERGE_ARGS.get(script.name, {})),
                          {"statusLabel": r": D1-", "status": "blocked"})
                self.assertNotEqual(out["status"], "done", "a blocked plan never yields a direction sheet")
                self.assertEqual(index(out["labels"], r": (N1-|N2-|M1-merge|M2-merge|M-r\d-merge|D3-)"), -1,
                                 "no needs tables and no merge on a missing plan")

    def test_harness_studio_check_matches_the_workflow_wording(self):
        # The harness's Studio exclusivity check keys on the driver sentence in each workflow's studioRule();
        # if either side drifts, the overlap check would go silent (J016 follow-up review F3).
        found = re.search(r"\['Studio', /(.+?)/\]", HARNESS.read_text(encoding="utf-8"))
        self.assertIsNotNone(found, "the harness has no Studio resource pattern")
        driver = re.compile(found.group(1))
        for name in ("job-cutscene.js", "job-character.js", "job-stage.js", "job-ui-screen.js", "job-feature.js", "job-effect.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build", size="L"), {"dump": ".*"})
                self.assertTrue(any(driver.search(d["prompt"]) for d in out["dumps"]), "no brief matches the harness's Studio driver pattern")

    def test_scripts_are_pure(self):
        banned = [r"Date\.now", r"Math\.random", r"new Date\(\s*\)", r"\brequire\(", r"^\s*import\s", r"\bfs\.", r"readFile", r"writeFile",
                  r"SendMessage", r"agentId", r"\bpeers\s*:"]
        for script in self.scripts():
            src = script.read_text(encoding="utf-8")
            for pat in banned:
                with self.subTest(script=script.name, pattern=pat):
                    self.assertIsNone(re.search(pat, src, re.M), f"{script.name} uses {pat}")

    def test_lesson_drafts_reach_the_lead(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"lesson": True})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertEqual(len(out["result"]["lessons"]), out["agents"], "every lesson draft is in the stage result (TT-10)")
                self.assertIn("cause", out["result"]["lessons"][0])
                empty = run(script, full(script.name, stage="direction"), {"lesson": "none"})
                self.assertEqual(empty["result"]["lessons"], [], "a lesson of type none is never filed")
                smoke = run(script, full(script.name, stage="direction", smoke=True), {"lesson": True})
                self.assertEqual(smoke["result"]["lessons"], [], "a smoke run files no lessons")

    # ------------------------------------------------------------------ bounded repairs and dead agents (LD5, R1)
    def test_repair_rounds_are_bounded(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="build"), {"blockAlways": True, "maker": MAKER[script.name]})
                self.assertEqual(out["violation"], "")
                self.assertEqual(out["status"], "needs-decision", out["outcome"])

    def test_a_dead_review_or_signature_is_never_a_pass(self):
        for script in self.scripts():
            with self.subTest(script=script.name, step="review"):
                out = run(script, full(script.name, stage="build"), {"nullLabel": REVIEW[script.name]})
                self.assertNotEqual(out["status"], "done", out["outcome"])
            # J024: "a dead D3 direction sheet fails the stage" → a dead D1 plan or a dead merge (the step that now writes
            # direction.md, design §3) fails direction, and no later step runs after it.
            for step, pattern in (("plan", r": D1-plan$"), ("direction sheet", MERGE[script.name] + "$")):
                with self.subTest(script=script.name, step=step):
                    out = run(script, full(script.name, stage="direction", **MERGE_ARGS.get(script.name, {})), {"nullLabel": pattern})
                    self.assertEqual(out["status"], "failed", out["outcome"])
                    self.assertRegex(out["labels"][-1], pattern, "no later step runs after a dead plan or direction sheet")

    # ------------------------------------------------------------------ images (LD2, F11, F13, TT-02)
    def test_pending_images_are_listed_not_failed(self):
        for script in self.scripts():
            if script.name == "job-feature.js":
                continue   # feature G1 shows player words; its images are made in the proof (next test)
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"images": "pending"})
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertTrue(out["result"]["images_pending"], "the stage result lists the pending batches")

    def test_feature_visible_parts_get_images_before_styling(self):
        # J024: "the proof makes the UI target and VFX key frames before styling" → those proof image steps are gone (design §2);
        # the owner-approved style references come from G1 in args.images, and a build whose presentation list names UI or VFX
        # stops before any visual craft without them; with no visible parts the build runs without images.
        name = "job-feature.js"
        visible = {"set": {"presentation": ["ui-ux-designer", "vfx-designer", "sound-designer", "animator"]}}
        direction = run(name, full(name, stage="direction"), dict(visible, images="pending"))
        self.assertEqual(direction["status"], "done", direction["outcome"])
        self.assertEqual(index(direction["labels"], r"P3-ui-target|P3-vfx-keyframes|ui-target|keyframes"), -1)
        blocked = run(name, full(name, stage="build", images=None), visible)
        self.assertEqual(blocked["status"], "blocked", blocked["outcome"])
        self.assertIn("images", blocked["result"]["required"])
        self.assertEqual(index(blocked["labels"], r"B3-ui|B4-anim|B5-vfx|B6-sound|B7-build"), -1, "no visual build without approved images")
        quiet = run(name, full(name, stage="build", images=None), {"set": {"presentation": ["sound-designer"]}})
        self.assertEqual(quiet["status"], "done", quiet["outcome"])

    def test_visual_briefs_carry_the_approved_images(self):
        img = BASE["images"][0]
        # J024: the rough set, blocking and VFX prototype briefs are gone (design §2) → every final visual craft brief in build
        # (animator, set, VFX, UI when the merge switched it on) carries the approved images and the no-image rule.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build", ui=True),
                  {"dump": r"B1-animator$|B2-set$|B3-vfx$|B5-ui$"})
        self.assertEqual(len(out["dumps"]), 4)
        for d in out["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn(img, d["prompt"])
                self.assertIn("No approved reference image path in refs means no visual build", d["prompt"])
        ui = next(d for d in out["dumps"] if "B5-ui" in d["label"])
        self.assertIn("ui-style-", ui["prompt"], "the cutscene UI loads the game's style book (F13)")
        # J024: the feature's UI and VFX run only when the presentation list names them (design §6), so the list names them here.
        feat = run("job-feature.js", full("job-feature.js", stage="build"),
                   {"set": {"presentation": ["ui-ux-designer", "vfx-designer"]}, "dump": r"B3-ui|B5-vfx"})
        self.assertEqual(len(feat["dumps"]), 2)
        for d in feat["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn(img, d["prompt"])
        self.assertIn("ui-style-", next(d for d in feat["dumps"] if "B3-ui" in d["label"])["prompt"])

    def test_one_image_maker_writes_prompts_first(self):
        for script in self.scripts():
            with self.subTest(script=script.name):
                out = run(script, full(script.name, stage="direction"), {"dump": r": D1-"})
                makers = [d for d in out["dumps"] if "write every image prompt first" in d["prompt"]]
                # Marketing makes its roughs in the direction sheet step, the feature makes no G1 pictures; the others have one D1 image maker.
                expected = 0 if script.name in ("job-feature.js", "job-marketing-art.js") else 1
                self.assertEqual(len(makers), expected, "one browser user per step, prompts first")
                for d in makers:
                    self.assertIn("images_approved: false", d["prompt"], "no download without the owner's yes (LD2)")
                    self.assertIn("image-prompts.md", d["prompt"], "one prompts-file name, as reference-images §4 says (N-07)")

    # ------------------------------------------------------------------ repair round 1 (auditor B recheck F11, N1-N3; auditor E recheck N-03)
    def test_direction_completes_with_pending_pictures(self):
        # J024: "a pending D1 batch must not fail the synthesis check" → the synthesis is gone; the D1 plan (the image maker,
        # design §3.1) checks its options against pictures on disk or rows in the pending prompts file, and no direction brief
        # (plan, tables, merge) asks for pictures that exist on disk.
        for name in ("job-character.js", "job-stage.js", "job-ui-screen.js", "job-cutscene.js", "job-effect.js"):
            with self.subTest(script=name):
                out = run(name, full(name, stage="direction"), {"images": "pending", "dump": r".*"})
                self.assertEqual(out["status"], "done", out["outcome"])
                plan = next(d for d in out["dumps"] if "D1-plan" in d["label"])["prompt"]
                self.assertRegex(plan, r"on disk or (a )?rows? in (a|the) (pending )?prompts file", "F11: a pending D1 batch must not fail the plan check")
                for d in out["dumps"]:
                    self.assertNotIn("pictures that exist on disk", d["prompt"], d["label"])
                # N2 (sign steps judge prompt rows) went with the sign steps (J023 design D3).

    def test_pending_art_that_later_steps_build_on_stops_the_stage(self):
        # J024: the proof cases (character proof reference set, cutscene boards) went with the proof stage (design §1-2) → the
        # pending batches that later steps build on are now in build: the UI icons and item art, the character reference set (L
        # and M), the marketing render, the stage kit sheets. The cutscene has no image step left in build (boards removed): a
        # build with no approved images is refused before any agent (REQUIRED) and no build brief writes image prompts.
        cases = [("job-ui-screen.js", dict(stage="build"), r"B1-figma", r"B2-ui-effects|B3-ui-sounds|B4-build|: RV-"),
                 ("job-character.js", dict(stage="build", size="M"), r"B0-reference-set", r"B1-model|B2-rig|B3-|B6-|CAP-|: RV-"),
                 ("job-character.js", dict(stage="build", size="L"), r"B0-reference-set", r"B1-model|B2-rig|B3-|B6-|CAP-|: RV-"),
                 ("job-marketing-art.js", dict(stage="build"), r"marketing: B1-final", r": RV-")]
        for name, changes, maker, later in cases:
            with self.subTest(script=name, changes=changes):
                out = run(name, full(name, **changes), {"images": "pending"})
                self.assertEqual(out["status"], "blocked", out["outcome"])
                self.assertGreaterEqual(index(out["labels"], maker), 0)
                self.assertEqual(index(out["labels"], later), -1, "nothing is built or reviewed on unapproved images")
                self.assertTrue(out["result"]["images_pending"])
        # only the kit model sheet is pending, so the run reaches the kit path (the paint-over check would stop it first)
        # J024: the kit sheets moved to `modeler: B4-kit` and the light pass into B1-place → nothing that places or reviews the kit
        # (integration, capture, reviews) runs on a pending kit sheet.
        kit = run("job-stage.js", full("job-stage.js", stage="build"), {"images": "pending", "imagesLabel": r"B4-kit", "set": {"kit_piece_ids": ["rock-a"]}})
        self.assertEqual(kit["status"], "blocked", kit["outcome"])
        self.assertIn("Kit pieces", kit["outcome"])
        self.assertGreaterEqual(index(kit["labels"], r"modeler: B4-kit"), 0)
        self.assertEqual(index(kit["labels"], r"B5-integrate|CAP-|: RV-"), -1)
        self.assertTrue(kit["result"]["images_pending"])
        cut = run("job-cutscene.js", full("job-cutscene.js", stage="build", ui=True), {"images": "pending", "dump": r".*"})
        self.assertEqual(cut["status"], "done", cut["outcome"])
        self.assertEqual([d["label"] for d in cut["dumps"] if "write every image prompt first" in d["prompt"]], [],
                         "no cutscene build step makes images (boards removed)")
        self.assertEqual(run("job-cutscene.js", full("job-cutscene.js", stage="build", images=None))["agents"], 0)

    # ------------------------------------------------------------------ cutscene: the pilot (auditor B F1-F13, auditor E TT-03, TT-04, TT-12)
    def test_cutscene_repair_recaptures_before_review(self):
        # J024: "IMP, SCN and CAP run between the last fix and the first review" → the animator's fix re-imports its clips in its
        # own run, the film-director re-assembles (SCN) after the last fix, and the first review of the round is the
        # capture-and-scripts run, which recaptures the repaired candidate (design §4.3, LD2).
        out = run("job-cutscene.js", full("job-cutscene.js", stage="repair"),
                  {"affected": ["animator", "vfx-designer"], "timing": True, "dump": r"animator: FIX-repair"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        last_fix = max(i for i, x in enumerate(labels) if ": FIX-repair-" in x)
        first_review = index(labels, r": RV-repair-r0-")
        scene = index(labels, r"film-director: SCN-repair")
        self.assertTrue(last_fix < scene < first_review, labels)
        self.assertRegex(labels[first_review], r"^studio-operator: RV-repair-r0-scripts$", "the recapture opens the round")
        self.assertRegex(out["dumps"][0]["prompt"], r"(?i)import", "the animator's fix re-imports its clips")
        self.assertEqual(index(labels, r"IMP-|CAP-"), -1, "no separate import or capture runs (folded, LD2)")
        self.assertGreaterEqual(index(labels, r"sound-designer: FIX-repair-sound-designer"), 0, "a moved beat makes sound recheck")

    def test_cutscene_scripts_run_first_every_round(self):
        # J024: "qa-lead scripts first, then a CAP-…-fix recapture" → the studio-operator capture-and-scripts run opens every round
        # (it recaptures after the fix and re-assembly); a scripts block still holds back the creative review.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "environment-designer"})
        self.assertEqual(out["status"], "done", out["outcome"])
        labels = out["labels"]
        for rnd in ("r0", "r1"):
            with self.subTest(round=rnd):
                first = index(labels, rf": RV-candidate-{rnd}-")
                self.assertRegex(labels[first], r"studio-operator: RV-candidate-%s-scripts" % rnd)
        fix = index(labels, r"environment-designer: FIX-candidate-r0")
        scene = index(labels, r"film-director: SCN-candidate-r0-fix")
        self.assertTrue(0 <= fix < scene < index(labels, r"RV-candidate-r1-scripts"), labels)
        blocked = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"blockLabelOnce": r"studio-operator: RV-candidate-r0-scripts", "maker": "feature-builder"})
        self.assertEqual(blocked["status"], "done", blocked["outcome"])
        self.assertEqual(index(blocked["labels"], r"film-director: RV-candidate-r0-film-director"), -1, "creative reviews wait when scripts block")
        self.assertGreaterEqual(index(blocked["labels"], r"film-director: RV-candidate-r1-film-director"), 0)

    def test_cutscene_vfx_and_sound_work_in_sequence(self):
        # J024: the proof pairs (needs meeting, temp VFX and sound) and the build prototypes are gone (design §2; N1 tables are
        # parallel by design §3.2) → in build the producers run before their consumers: animator markers → VFX → sound.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"timeline": True, "conflicts": True})
        for first, then in (("animator: B1-animator$", "vfx-designer: B3-vfx$"), ("vfx-designer: B3-vfx$", "sound-designer: B4-sound$")):
            with self.subTest(pair=first):
                self.assertGreater(span(out, then)["start"], span(out, first)["end"], "the consumer reads the producer's finished note")

    def test_cutscene_combined_pass_before_polish(self):
        # J024: "combined check-in after blocking, before polish" → the blocking pass, check-in and polish are removed on purpose
        # (design §2): none runs in L or M, each craft builds once, and the animator's final clip still comes before the VFX.
        for size in ("L", "M"):
            with self.subTest(size=size):
                labels = run("job-cutscene.js", full("job-cutscene.js", stage="build", size=size))["labels"]
                self.assertEqual([x for x in labels if re.search(r"(?i)combined|check-?in|blocking|polish|proto", x)], [])
                self.assertEqual([x for x in labels if x.startswith("animator: ")], ["animator: B1-animator"])
                self.assertLess(index(labels, r"animator: B1-animator"), index(labels, r"vfx-designer: B3-vfx$"))

    def test_cutscene_new_cast_stops_before_the_animatic(self):
        # J024: "a new cast stops the proof before the animatic" → it stops direction after the D1 plan, before any needs table
        # (design §6 cutscene row); the proof stage itself is refused.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="direction"), {"newCast": True})
        self.assertEqual(out["status"], "needs-decision")
        self.assertEqual(index(out["labels"], r"N1-|M1-merge|P5-animatic"), -1)
        self.assertEqual(out["agents"], 1)

    def test_cutscene_proof_fix_pins_the_new_beat_sheet(self):
        # J024: "a proof fix pins the new beat-sheet revision for the next review and the result" → the proof is gone; a build fix
        # of the film-director pins the returned revision in the re-assembly and in the next round's capture-and-scripts brief.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"),
                  {"blockLabelOnce": r"film-director: RV-candidate-r0", "maker": "film-director",
                   "dump": r"FIX-candidate-r0-film-director|SCN-candidate-r0-fix|RV-candidate-r1-scripts"})
        self.assertEqual(out["status"], "done", out["outcome"])
        fix = next(d for d in out["dumps"] if "FIX-candidate-r0-film-director" in d["label"])
        pin = f"beat-sheet.md@rev{fix['returned']['beat_sheet_revision']}"
        for label in ("SCN-candidate-r0-fix", "RV-candidate-r1-scripts"):
            with self.subTest(label=label):
                self.assertIn(pin, next(d for d in out["dumps"] if label in d["label"])["prompt"])

    def test_cutscene_player_brief_has_its_contract_spec_and_skills(self):
        # J024: the gameplay state sheet is in the beat sheet, the UI spec exists only when the merge switched UI on (ui), and the
        # architect writes the player contract with its code owners in its N1 limits table (no B1-player-contract run).
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build", ui=True), {"dump": r"PLY-candidate"})
        player = next(d for d in out["dumps"] if "PLY-candidate" in d["label"])["prompt"]
        for text in ("content/ui/test-cutscene/spec.md", "contract-player.md", "Code file owners", "networking-security", "ui-basics",
                     "return blocked with the files you need", "gameplay state sheet in the beat sheet"):
            with self.subTest(text=text):
                self.assertIn(text, player)
        self.assertEqual(index(out["labels"], r"B1-player-contract"), -1)
        direction = run("job-cutscene.js", full("job-cutscene.js", stage="direction"), {"dump": r"architect: N1-architect"})
        arch = direction["dumps"][0]["prompt"]
        self.assertIn("Code file owners", arch)
        self.assertIn("contract-player", arch)

    def test_cutscene_captures_name_what_studio_can_produce(self):
        # J024: CAP-candidate and the sound-designer review are gone → the capture-and-scripts brief and the film-director's
        # integrated review (which checks sound sync) carry the stills-only line.
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"dump": r"studio-operator: RV-|film-director: RV-"})
        self.assertEqual(len(out["dumps"]), 2)
        for d in out["dumps"]:
            with self.subTest(label=d["label"]):
                self.assertIn("screen_capture gives still images only", d["prompt"])
                self.assertNotIn("capture with sound exists", d["prompt"])

    # ------------------------------------------------------------------ code review (F9, LD15, TT-03), file owners (LD10, TT-04)
    def test_code_review_runs_when_the_candidate_has_code(self):
        cases = [("job-cutscene.js", {}, True), ("job-character.js", {"playable": True}, True), ("job-character.js", {"playable": False}, False),
                 ("job-feature.js", {}, True), ("job-ui-screen.js", {}, True), ("job-effect.js", {}, True)]
        for name, extra, expect in cases:
            for stage in ("build", "repair"):
                with self.subTest(script=name, extra=extra, stage=stage):
                    out = run(name, full(name, stage=stage, **extra), {"affected": [MAKER[name]]})
                    self.assertEqual(out["status"], "done", out["outcome"])
                    has = index(out["labels"], r"^reviewer: (RV|CR)-") >= 0
                    self.assertEqual(has, expect, out["labels"])

    def test_a_blocked_builder_stops_the_stage_before_review(self):
        out = run("job-cutscene.js", full("job-cutscene.js", stage="build"), {"statusLabel": r"PLY-candidate", "status": "blocked"})
        self.assertEqual(out["status"], "blocked", out["outcome"])
        self.assertEqual(index(out["labels"], r": RV-"), -1, "no review runs on a candidate that was never built")

    def test_code_briefs_take_file_owners_from_the_contract(self):
        # J024: the architect's contract runs (character P1-wiring-contract, UI C3-code-owners) moved into its N1 limits table in
        # direction (design §3.2, §6) → that table names the Code file owners before G1, and the build briefs take ownership from the
        # contract pinned at its G1 revision.
        out = run("job-character.js", full("job-character.js", stage="build", size="M"), {"dump": r"B6-wiring"})
        wire = next(d for d in out["dumps"] if "B6-wiring" in d["label"])["prompt"]
        self.assertRegex(wire, r"contract-wiring\.md@(rev\d+|<the revision approved at G1)")
        self.assertIn("Code file owners", wire)
        self.assertNotIn("the job card names", wire)
        cdir = run("job-character.js", full("job-character.js", stage="direction", size="M"), {"dump": r"architect: N1-limits-architect"})
        self.assertLess(index(cdir["labels"], r"architect: N1-limits-architect"), index(cdir["labels"], r"art-director: M-r1-merge"))
        self.assertIn("Code file owners", cdir["dumps"][0]["prompt"])
        ui = run("job-ui-screen.js", full("job-ui-screen.js", stage="build", size="M"), {"dump": r"feature-builder: B4-build"})
        self.assertEqual(ui["status"], "done", ui["outcome"])
        impl = ui["dumps"][0]["prompt"]
        self.assertIn("contract-code.md", impl)
        self.assertNotIn('listed under "File owners" in', impl)
        udir = run("job-ui-screen.js", full("job-ui-screen.js", stage="direction", size="M"), {"dump": r"architect: N1-limits-architect"})
        self.assertLess(index(udir["labels"], r"architect: N1-limits-architect"), index(udir["labels"], r"ui-ux-designer: D3-merge"))
        self.assertIn("contract-code.md", udir["dumps"][0]["prompt"])

    # ------------------------------------------------------------------ feature (F15, TT-06, TT-11)
    def test_feature_code_briefs_load_networking_security_without_money(self):
        # J024: the architect's B1-plan run is its N1 limits table in direction; the builder is B7-build (design §6 feature row).
        out = run("job-feature.js", full("job-feature.js", stage="build", money=False), {"dump": r"feature-builder: B7-build|reviewer: RV-"})
        plan = run("job-feature.js", full("job-feature.js", stage="direction", money=False), {"dump": r"architect: N1-limits-architect"})
        dumps = out["dumps"] + plan["dumps"]
        self.assertEqual(len(dumps), 3)
        for d in dumps:
            with self.subTest(label=d["label"]):
                self.assertRegex(d["prompt"], r"skills: \[[^\]]*networking-security")

    def test_feature_vfx_and_sound_work_in_sequence(self):
        # J024: the presentation crafts run only when the contract's presentation list names them (design §6) → named here; the
        # producers still finish before their consumers (animator markers → VFX → sound).
        out = run("job-feature.js", full("job-feature.js", stage="build"),
                  {"timeline": True, "set": {"presentation": ["ui-ux-designer", "animator", "vfx-designer", "sound-designer"]}})
        for first, then in (("B4-animation", "B5-vfx"), ("B5-vfx", "B6-sound")):
            with self.subTest(pair=first):
                self.assertGreater(span(out, then)["start"], span(out, first)["end"])

    def test_shared_cues_run_vfx_before_sound_in_every_workflow(self):
        # J024: the proof pairs (stage P3 needs meeting, effect P1 timeline → E-r1 meeting) are gone and N1 tables are parallel by
        # design (§3.2) → each build pair carries the order, and in effect direction the D1 timeline is written before the sound
        # designer's needs table answers it. The UI effects run only with the merge's ui_effects switch.
        cases = [("job-ui-screen.js", "build", {}, {"set": {"ui_effects": True}}, "B2-ui-effects", "B3-ui-sounds"),
                 ("job-stage.js", "build", {}, {}, "B2-ambience-vfx", "B3-ambience-sound"),
                 ("job-character.js", "build", {"playable": False}, {}, "B4-vfx", "B5-sound"),
                 ("job-effect.js", "build", {}, {}, "B2-vfx", "B3-sound"),
                 ("job-effect.js", "direction", {}, {}, "vfx-designer: D1-plan", "sound-designer: N1-sound-designer")]
        for name, stage, extra, scen, vfx, sound in cases:
            with self.subTest(script=name, stage=stage, pair=vfx):
                out = run(name, full(name, stage=stage, **extra), dict(scen, timeline=True))
                self.assertEqual(out["status"], "done", out["outcome"])
                self.assertGreater(span(out, sound)["start"], span(out, vfx)["end"])

    def test_capture_briefs_carry_the_check_budget(self):
        # J024: P4-play, CAP-candidate, B6-capture and PT- runs became the one capture-and-scripts run per round (design §4.3).
        for name, pat in (("job-feature.js", r"studio-operator: RV-.*-capture"), ("job-cutscene.js", r"studio-operator: RV-.*-scripts"),
                          ("job-ui-screen.js", r"studio-operator: RV-.*-capture"), ("job-effect.js", r"studio-operator: RV-.*-scripts"),
                          ("job-stage.js", r"studio-operator: CAP-"), ("job-character.js", r"studio-operator: CAP-")):
            with self.subTest(script=name):
                out = run(name, full(name, stage="build"), {"dump": pat})
                self.assertTrue(out["dumps"])
                for d in out["dumps"]:
                    self.assertIn("Check budget (owner J005-D8)", d["prompt"])

    # ------------------------------------------------------------------ others
    def test_stage_capture_findings_reach_the_next_playtest(self):
        # J024: the art-director no longer reviews without newLook and PT-…-record is the capture-and-scripts run CAP-…-r1 → a
        # capture gap named by the job lead's integrated review goes to the next capture, never to a FIX run of the operator.
        out = run("job-stage.js", full("job-stage.js", stage="build"),
                  {"blockLabelOnce": r"environment-designer: RV-candidate-r0", "maker": "studio-operator", "dump": r"studio-operator: CAP-candidate-r1"})
        self.assertEqual(out["status"], "done", out["outcome"])
        self.assertEqual(index(out["labels"], r"FIX-candidate-r0-studio-operator"), -1)
        self.assertIn("capture gaps", out["dumps"][0]["prompt"])

    def test_character_palette_only_variant_skips_the_rig_steps(self):
        # J024: S4-S6 are now B2-rig (S4 check, S5 rig) and the animator's S6 acceptance inside B3-animation → a palette-only
        # variant runs no rig step and the animator only import-checks the released base rig; a reshaped variant rigs.
        name = "job-character.js"
        palette = run(name, full(name, stage="build", variant=True), {"set": {"geometry_changed": False}, "dump": r"animator: B3-animation"})
        self.assertEqual(palette["status"], "done", palette["outcome"])
        self.assertEqual(index(palette["labels"], r"character-rigger: |S4-r0|S5-rig|S6-r0"), -1)
        self.assertIn("Palette-only variant", palette["dumps"][0]["prompt"])
        reshaped = run(name, full(name, stage="build", variant=True), {"set": {"geometry_changed": True}})
        self.assertGreaterEqual(index(reshaped["labels"], r"character-rigger: B2-rig"), 0)

    def test_marketing_slot_size_rerun_is_fresh(self):
        out = run("job-marketing-art.js", full("job-marketing-art.js", stage="direction"), {"set": {"slot_sizes_missing": ["Home tile"]}})
        self.assertEqual(out["status"], "needs-decision")
        self.assertIn("fresh", out["outcome"])
        self.assertNotIn("resume from cache", out["outcome"])


if __name__ == "__main__":
    unittest.main()
