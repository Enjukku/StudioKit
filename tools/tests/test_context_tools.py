"""Offline tests for context_packet.py, kb_index.py and eval_context.py.

Run: python tools/tests/test_context_tools.py
"""

from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import context_packet as cp  # noqa: E402
import eval_context as ev  # noqa: E402
import kb_index as kb  # noqa: E402
import verify  # noqa: E402


def quiet(fn, *args):
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        return fn(*args)


def fm(type_="reference", status="active", updated="2026-10-01", extra=""):
    return f"---\ntype: {type_}\nscope: universal\nstatus: {status}\nupdated: {updated}\nsource: test\n{extra}---\n> Author: tester · model · low · 2026-10-01\n\n"


class Repo(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp(prefix="kit-ctx-"))
        self.addCleanup(shutil.rmtree, self.root, ignore_errors=True)

    def write(self, rel: str, text: str) -> None:
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text) if not text.startswith("---") else text, encoding="utf-8")

    def ranked(self, query: str) -> list[cp.Hit]:
        return cp.rank(cp.Corpus(self.root), query)[0]


class RankingTests(Repo):
    def test_bm25_prefers_focused_heading_match(self):
        self.write("knowledge/design/a.md", fm() + "# Alpha\n\n## Debris cleanup\n\nDebris is removed after 30 s.\n\n## Other\n\nUnrelated text about doors.\n")
        self.write("knowledge/design/b.md", fm() + "# Beta\n\n## Misc\n\n" + "Doors windows roofs walls floors. " * 30 + "debris once.\n")
        hits = self.ranked("debris cleanup")
        self.assertEqual(hits[0].path, "knowledge/design/a.md")
        self.assertEqual(hits[0].heading, "Debris cleanup")
        self.assertEqual(hits[0].kind, "match")
        self.assertTrue(hits[0].excerpt and "Debris" in hits[0].excerpt[0])

    def test_rare_terms_weigh_more_and_output_is_deterministic(self):
        for i in range(5):
            self.write(f"knowledge/logs/l{i}.md", fm("log") + f"# Log {i}\n\nThe game was tested today.\n")
        self.write("knowledge/systems/eggs.md", fm("system") + "# Eggs\n\nEgg hatch odds per tier.\n")
        hits = self.ranked("game egg odds")
        self.assertEqual(hits[0].path, "knowledge/systems/eggs.md")
        first = cp.build(self.root, "game egg odds")
        second = cp.build(self.root, "game egg odds")
        self.assertEqual(first, second)
        self.assertEqual(cp.render(first), cp.render(second))

    def test_type_boost_orders_equal_text(self):
        body = "# Note\n\nRetry budget for failed hand-backs is two.\n"
        self.write("knowledge/logs/x.md", fm("log") + body)
        self.write("knowledge/systems/x.md", fm("system") + body)
        hits = self.ranked("retry budget")
        self.assertEqual([h.path for h in hits[:2]], ["knowledge/systems/x.md", "knowledge/logs/x.md"])

    def test_superseded_notes_are_skipped_and_reported(self):
        self.write("knowledge/systems/new-sell.md", fm("system") + "# Sell v2\n\nSelling bricks pays gold.\n")
        self.write(
            "knowledge/systems/old-sell.md",
            fm("system", status="superseded") + "# Sell flow\n\nSell flow for bricks and gold. Replaced by [[systems/new-sell]].\n",
        )
        hits, superseded = cp.rank(cp.Corpus(self.root), "sell flow bricks gold")
        self.assertNotIn("knowledge/systems/old-sell.md", [h.path for h in hits])
        self.assertEqual(superseded[0]["path"], "knowledge/systems/old-sell.md")
        self.assertEqual(superseded[0]["see"], "knowledge/systems/new-sell.md")
        self.assertIn("superseded, see `knowledge/systems/new-sell.md`", cp.render(cp.build(self.root, "sell flow bricks gold")))

    def test_link_neighbours_join_with_lower_score(self):
        self.write("knowledge/systems/blast.md", fm("system") + "# Blast radius\n\nBlast radius math. See [[reference/physics-card]].\n")
        self.write("knowledge/reference/physics-card.md", fm() + "# Physics card\n\nAssembly limits and sleeping parts.\n")
        hits = self.ranked("blast radius")
        by_path = {h.path: h for h in hits}
        neighbour = by_path["knowledge/reference/physics-card.md"]
        self.assertEqual(neighbour.kind, "link")
        self.assertIn("linked from knowledge/systems/blast.md", neighbour.why)
        self.assertLess(neighbour.score, by_path["knowledge/systems/blast.md"].score)

    def test_overlay_included_for_matched_skill(self):
        self.write(".agents/skills/sound-design/SKILL.md", "---\nname: sound-design\ndescription: Use when designing sound, SFX and music.\n---\n\n# Sound design\n\nLayer transient, body, tail.\n")
        self.write("knowledge/overlays/sound-design.md", fm("overlay") + "# Sound design for this game\n\nCartoon palette only.\n")
        self.write("knowledge/overlays/animation.md", fm("overlay") + "# Animation for this game\n\nSnappy.\n")
        hits = self.ranked("design a sound for the reward")
        paths = [h.path for h in hits]
        self.assertIn("knowledge/overlays/sound-design.md", paths)
        self.assertNotIn("knowledge/overlays/animation.md", paths)
        self.assertLess(paths.index(".agents/skills/sound-design/SKILL.md"), paths.index("knowledge/overlays/sound-design.md"))

    def test_config_roots_and_side_lists(self):
        self.write("docs/guide.md", "# Guide\n\nCamera shake rules.\n")
        self.write("knowledge/design/x.md", fm() + "# X\n\nCamera shake.\n")
        self.write("kit.json", json.dumps({"context": {"search_roots": ["docs"]}}))
        self.write("AGENTS.md", "# Rules\n\n## 0. Authority\n\ntext\n\n## 1. Studio\n\ntext\n")
        self.write("knowledge/design/decisions.md", fm("decision") + "# Ledger\n\n| ID | date | decision | words |\n| --- | --- | --- | --- |\n| D-1 | 2026-10-01 | Camera shake capped at 0.4 | \"less shake\" |\n| D-2 | 2026-10-02 | Gold icon is round | \"round\" |\n")
        self.write("src/client/CameraShakeController.luau", "return {}")
        packet = cp.build(self.root, "camera shake")
        paths = {r["path"] for r in packet["results"]}
        self.assertIn("docs/guide.md", paths)
        self.assertNotIn("knowledge/design/x.md", paths)
        self.assertEqual([d["line"] for d in packet["decisions"]], [14])
        self.assertEqual(packet["code_hints"][0]["path"], "src/client/CameraShakeController.luau")
        self.assertEqual(packet["agents_sections"], ["0. Authority", "1. Studio"])

    def test_budget_limits_entries(self):
        for i in range(30):
            self.write(f"knowledge/design/n{i:02}.md", fm() + f"# Note {i}\n\nCollect bricks into the backpack {i}.\n")
        small = cp.build(self.root, "collect bricks backpack", budget=200, max_items=50)
        large = cp.build(self.root, "collect bricks backpack", budget=8000, max_items=50)
        self.assertLess(len(small["results"]), len(large["results"]))

    def test_empty_query_rejected(self):
        with self.assertRaises(ValueError):
            cp.rank(cp.Corpus(self.root), "the and of")

    def test_stem_merges_plurals_and_forms(self):
        self.assertEqual(cp.stem("drafts"), cp.stem("draft"))
        self.assertEqual(cp.stem("approve"), cp.stem("approval"))
        self.assertEqual(cp.stem("statuses"), cp.stem("status"))


MIRROR = "knowledge/external/roblox-creator-docs"


def page(title: str, description: str, body: str) -> str:
    return f"---\ntitle: {title}\ndescription: {description}\ntags: [roblox]\n---\n\n> [!info] Local Roblox Creator Docs mirror\n> Mirrored from [x](https://example.com/x).\n\n{body}\n"


class RobloxDocsTests(Repo):
    def mirror(self):
        self.write(f"{MIRROR}/README.md", "---\ntitle: Mirror readme\n---\n\n# Mirror\n\nTrails beams sword.\n")
        self.write(f"{MIRROR}/effects/trails.md", page("Trails", "Trails create visual motion effects as an object moves.", "A `Class.Trail` draws a streak behind two attachments, such as a sword slashing through the air.\n\n## Lifetime\n\nHow long the streak lasts."))
        self.write(f"{MIRROR}/effects/beams.md", page("Beams", "Beams connect two attachments.", "A `Class.Beam` draws a texture between two points, like a laser.\n\n## Width\n\nBeam width."))
        self.write(f"{MIRROR}/tutorials/long.md", page("Build a whole game", "A long tutorial.", "Step text about doors and coins. " * 80 + "A sword appears once."))
        self.write(f"{MIRROR}/audio/effects.md", page("Audio effects", "Change how sound is heard.", "Reverb makes a cave echo.\n\n## Echo\n\nEcho repeats the sound."))
        for name in ("Trail", "Beam", "Part", "UICorner"):
            self.write(f"{MIRROR}/_api-reference/classes/{name}.yaml", f"name: {name}\nsummary: The {name} class.\n")
        self.write(f"{MIRROR}/_includes/fragment.md", "Trails trails trails sword sword.\n")

    def test_section_lists_pages_after_kit_notes(self):
        self.mirror()
        self.write("knowledge/design/vfx.md", fm() + "# Sword effects\n\nThe sword swing gets a streak.\n")
        packet = cp.build(self.root, "a glowing streak that follows the sword swing")
        pages = packet["roblox_docs"]["pages"]
        self.assertEqual(pages[0]["path"], f"{MIRROR}/effects/trails.md")
        self.assertEqual(pages[0]["title"], "Trails")
        self.assertTrue(pages[0]["why"])
        paths = [p["path"] for p in pages]
        self.assertNotIn(f"{MIRROR}/README.md", paths)
        self.assertFalse(any("/_includes/" in p or "/_api-reference/" in p for p in paths))
        text = cp.render(packet)
        self.assertIn("## Roblox docs", text)
        self.assertLess(text.index("## Ranked"), text.index("knowledge/design/vfx.md"))
        self.assertLess(text.index("knowledge/design/vfx.md"), text.index("## Roblox docs"))
        self.assertLess(text.index("## Roblox docs"), text.index("## Read next"))
        self.assertIn(f"`{MIRROR}/effects/trails.md` · Trails", text)

    def test_at_most_five_pages_and_focused_page_beats_long_tutorial(self):
        self.mirror()
        for i in range(8):
            self.write(f"{MIRROR}/misc/p{i}.md", page(f"Page {i}", "Sword notes.", f"Sword fact {i}."))
        pages = cp.build(self.root, "sword trail")["roblox_docs"]["pages"]
        self.assertEqual(len(pages), 5)
        self.assertEqual(pages[0]["path"], f"{MIRROR}/effects/trails.md")
        self.assertNotEqual(pages[0]["path"], f"{MIRROR}/tutorials/long.md")

    def test_api_lines_only_for_exact_class_names(self):
        self.mirror()
        packet = cp.build(self.root, "add a Trail and a UICorner, not a trail or a Partition or a Beams")
        api = packet["roblox_docs"]["api"]
        self.assertEqual([a["class"] for a in api], ["Trail", "UICorner"])
        self.assertEqual(api[0]["path"], f"{MIRROR}/_api-reference/classes/Trail.yaml")
        self.assertIn(f"API: Trail → {MIRROR}/_api-reference/classes/Trail.yaml", cp.render(packet))

    def test_kit_ranking_unchanged_by_mirror(self):
        self.write("knowledge/design/vfx.md", fm() + "# Sword effects\n\nThe sword swing gets a streak.\n")
        before = cp.build(self.root, "sword streak")
        self.mirror()
        after = cp.build(self.root, "sword streak")
        self.assertEqual(before["results"], after["results"])
        self.assertEqual(before["searched"], after["searched"])
        self.assertEqual(before["roblox_docs"], {"pages": [], "api": []})
        self.assertNotIn("## Roblox docs", cp.render(before))

    def test_cache_written_and_rebuilt_when_mirror_changes(self):
        self.mirror()
        first = cp.build(self.root, "cave echo")["roblox_docs"]["pages"]
        self.assertEqual(first[0]["path"], f"{MIRROR}/audio/effects.md")
        cache = self.root / cp.DOCS_CACHE
        self.assertTrue(cache.is_file())
        self.assertTrue(cp.DOCS_CACHE.startswith("knowledge/generated/"))
        self.assertEqual(cp.build(self.root, "cave echo")["roblox_docs"], cp.build(self.root, "cave echo")["roblox_docs"])
        self.write(f"{MIRROR}/environment/caves.md", page("Caves", "Cave echo and cave sound.", "Cave echo cave echo."))
        again = cp.build(self.root, "cave echo")["roblox_docs"]["pages"]
        self.assertIn(f"{MIRROR}/environment/caves.md", [p["path"] for p in again])

    def test_corrupt_cache_is_rebuilt(self):
        self.mirror()
        cache = self.root / cp.DOCS_CACHE
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text("{not json", encoding="utf-8")
        pages = cp.build(self.root, "laser beam")["roblox_docs"]["pages"]
        self.assertEqual(pages[0]["path"], f"{MIRROR}/effects/beams.md")
        json.loads(cache.read_text(encoding="utf-8"))

    def test_pages_cited_by_top_kit_notes_rank_up(self):
        self.mirror()
        self.write(f"{MIRROR}/physics/sleep.md", page("Sleep system", "Assemblies at rest stop simulating.", "Sleeping parts wake on contact."))
        self.write(f"{MIRROR}/scripting/index.md", page("Scripting", "Scripts.", "Scripts run code."))
        # No page shares the task's words; kit notes about the task cite the right pages in three forms.
        task = "idle bricks ignore nudges"
        self.assertEqual(cp.build(self.root, task)["roblox_docs"]["pages"], [])
        self.write("knowledge/reference/a.md", fm() + "# Idle bricks\n\nIdle bricks ignore nudges: see `knowledge/external/roblox-creator-docs/physics/sleep.md`.\n")
        self.write("knowledge/reference/b.md", fm() + "# Nudges\n\nNudges and idle bricks: [[external/roblox-creator-docs/scripting]] and effects/beams.md.\n")
        pages = cp.build(self.root, task)["roblox_docs"]["pages"]
        paths = [p["path"] for p in pages]
        self.assertEqual(paths[0], f"{MIRROR}/physics/sleep.md")
        self.assertIn(f"{MIRROR}/scripting/index.md", paths)
        self.assertIn(f"{MIRROR}/effects/beams.md", paths)
        self.assertIn("cited by top kit notes", pages[0]["why"])

    def test_generated_related_files_tail_is_not_indexed(self):
        self.mirror()
        self.write(f"{MIRROR}/effects/glow.md", page("Glow", "Light bloom.", "Bloom.\n\n## Related Files\n\n- [[external/roblox-creator-docs/effects/trails]] - Gizmo widgets."))
        self.assertEqual(cp.build(self.root, "gizmo widgets")["roblox_docs"]["pages"], [])

    def test_cli_docs_flag_and_json(self):
        self.mirror()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            self.assertEqual(cp.main(["--root", str(self.root), "packet", "sword trail", "--docs", "1", "--json"]), 0)
        self.assertEqual(len(json.loads(out.getvalue())["roblox_docs"]["pages"]), 1)


FIXTURE = TOOLS / "tests" / "fixtures" / "context"
GOLDEN_ARGS = {  # same queries as the recorder that wrote fixtures/context/golden/ from the pre-J016 tool
    "storyboard.txt": ["storyboard the boss intro"],
    "storyboard-json.json": ["storyboard the boss intro", "--json"],
    "saves.txt": ["save player data retries", "--budget", "400", "--max", "3"],
    "camera-json.json": ["camera cutscene Camera timing", "--json", "--docs", "1"],
}


def run_cli(fn, argv: list[str]) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = fn(argv)
    return code, out.getvalue(), err.getvalue()


class FixtureRepo(unittest.TestCase):
    """A copy of tools/tests/fixtures/context/repo: roles, overlays, docs map, two job folders, tagged notes."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="kit-ctx-fx-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.root = self.tmp / "repo"
        shutil.copytree(FIXTURE / "repo", self.root)

    def packet(self, *args: str) -> tuple[int, str, str]:
        return run_cli(cp.main, ["--root", str(self.root), "packet", *args])


class NoFlagRegressionTests(FixtureRepo):
    def test_output_without_role_and_job_is_byte_identical_to_pre_change_golden(self):
        for name, args in GOLDEN_ARGS.items():
            with self.subTest(golden=name):
                code, out, _ = self.packet(*args)
                self.assertEqual(code, 0)
                self.assertEqual(out, (FIXTURE / "golden" / name).read_bytes().decode("utf-8"))


class RoleFlagTests(FixtureRepo):
    def test_role_tagged_note_ranks_higher(self):
        plain = [h.path for h in cp.rank(cp.Corpus(self.root), "storyboard the boss intro")[0]]
        tagged = [h.path for h in cp.rank(cp.Corpus(self.root), "storyboard the boss intro", role="film-director")[0]]
        self.assertLess(plain.index("knowledge/lessons/storyboard-generic.md"), plain.index("knowledge/lessons/storyboard-tagged.md"))
        self.assertEqual(tagged[0], "knowledge/lessons/storyboard-tagged.md")

    def test_role_block_lists_file_skills_overlays_and_docs_row_verbatim(self):
        code, out, _ = self.packet("storyboard the boss intro", "--role", "film-director")
        self.assertEqual(code, 0)
        block = out.split("## For role film-director", 1)[1].split("\n## ", 1)[0]
        self.assertIn("`.agents/roles/film-director.md`", block)
        self.assertIn("film-direction, film-craft", block)
        self.assertIn("`knowledge/overlays/film-director.md`", block)
        self.assertIn("`knowledge/overlays/film-craft.md`", block)
        self.assertNotIn("knowledge/overlays/film-direction.md", block)  # no such overlay
        self.assertIn("\n| film-director | `workspace/camera/`, `animation/` | workspace/camera/index.md | Camera, TweenService |\n", block)
        self.assertNotIn("feature-builder", block)

    def test_role_in_shared_docs_map_row_and_block_list_skills(self):
        info = cp.role_info(self.root, "feature-builder")
        self.assertEqual(info["skills"], ["engineering-craft", "testing"])
        self.assertEqual(info["overlays"], [])
        self.assertEqual([r["row"].split("|")[1].strip() for r in info["docs_map"]], ["architect, feature-builder, reviewer"])

    def test_unknown_role_exits_2(self):
        code, out, err = self.packet("storyboard", "--role", "film-directr")
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("unknown role `film-directr`", err)
        self.assertIn("film-director", err)  # lists the kit roles
        self.assertEqual(self.packet("storyboard", "--role", "README")[0], 2)

    def test_role_block_outside_note_budget(self):
        args = ("save player data retries", "--budget", "200")
        base = json.loads(self.packet(*args, "--json")[1])
        with_role = json.loads(self.packet(*args, "--json", "--role", "film-director")[1])
        self.assertEqual(base["results"], with_role["results"])  # no film-director-tagged note matches this task
        self.assertTrue(with_role["role"]["lines"])


class JobFlagTests(FixtureRepo):
    def test_job_folder_notes_rank_higher(self):
        plain = [h.path for h in cp.rank(cp.Corpus(self.root), "storyboard the boss intro")[0]]
        job = [h.path for h in cp.rank(cp.Corpus(self.root), "storyboard the boss intro", job="J016-demo")[0]]
        self.assertNotEqual(plain[0], "knowledge/jobs/J016-demo/notes.md")
        self.assertEqual(job[0], "knowledge/jobs/J016-demo/notes.md")

    def test_boost_reason_named_once_per_hit(self):
        hits = cp.rank(cp.Corpus(self.root), "boss intro gates storyboard", role="film-director", job="J016-demo")[0]
        card = [h for h in hits if h.path == "knowledge/jobs/J016-demo/job-card.md"]
        self.assertEqual(len(card), 2)  # two sections of one note: the suffix must not pile up
        for hit in card:
            self.assertEqual(hit.why.count("; in job J016-demo"), 1)
        tagged = next(h for h in hits if h.path == "knowledge/lessons/storyboard-tagged.md")
        self.assertTrue(tagged.why.endswith("; tagged for role film-director"))

    def test_job_block_lists_canonical_files_in_order_with_revisions(self):
        code, out, _ = self.packet("storyboard the boss intro", "--job", "J016-demo")
        self.assertEqual(code, 0)
        block = out.split("## Job J016-demo", 1)[1].split("\n## ", 1)[0]
        base = "knowledge/jobs/J016-demo/"
        expected = [
            f"`{base}job-card.md` · revision 4",
            f"`{base}decisions.md` · revision 3",
            f"`{base}ledger.md`",
            f"`{base}g2/beat-sheet.md`",
            f"`{base}contract-camera.md` · revision 2 (camera handover)",
            f"`{base}g2/boss.shots.json` · revision 5",
        ]
        positions = [block.index(item) for item in expected]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn("notes.md", block)
        self.assertNotIn("ledger.md` · revision", block)

    def test_unique_prefix_selects_job(self):
        self.assertEqual(cp.resolve_job(self.root, "J016"), "J016-demo")
        self.assertEqual(cp.resolve_job(self.root, "J016-demo"), "J016-demo")

    def test_unknown_or_ambiguous_job_exits_2(self):
        for job, fragment in (("J099", "unknown job `J099`"), ("J01", "ambiguous job `J01`")):
            with self.subTest(job=job):
                code, out, err = self.packet("storyboard", "--job", job)
                self.assertEqual(code, 2)
                self.assertEqual(out, "")
                self.assertIn(fragment, err)

    def test_job_block_capped_at_25_lines(self):
        for i in range(40):
            (self.root / f"knowledge/jobs/J016-demo/contract-{i:02}.md").write_text(f"Revision: {i}\n", encoding="utf-8")
        info = cp.job_info(self.root, "J016-demo")
        self.assertLessEqual(len(info["lines"]), cp.BLOCK_MAX_LINES)
        self.assertIn("more", info["lines"][-1])
        code, out, _ = self.packet("storyboard", "--job", "J016")
        block = out.split("## Job J016-demo", 1)[1].split("\n## ", 1)[0]
        self.assertLessEqual(len(("## Job J016-demo" + block).strip("\n").splitlines()), cp.BLOCK_MAX_LINES)

    def test_cap_keeps_25_lines_and_cuts_26(self):
        lines = [f"- line {i}" for i in range(26)]
        self.assertEqual(cp.cap_lines(lines[:25]), lines[:25])
        capped = cp.cap_lines(lines)
        self.assertEqual(len(capped), 25)
        self.assertEqual(capped[:24], lines[:24])
        self.assertIn("2 more lines", capped[-1])

    def test_json_carries_role_and_job_blocks(self):
        code, out, _ = self.packet("storyboard the boss intro", "--json", "--role", "film-director", "--job", "J016")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["role"]["role"], "film-director")
        self.assertEqual(data["job"]["job"], "J016-demo")
        self.assertEqual(data["job"]["files"][0], {"path": "knowledge/jobs/J016-demo/job-card.md", "revision": "4"})
        text = self.packet("storyboard the boss intro", "--role", "film-director", "--job", "J016")[1]
        for line in data["role"]["lines"] + data["job"]["lines"]:
            self.assertIn(line, text)
        self.assertNotIn("role", json.loads(self.packet("storyboard the boss intro", "--json")[1]))


REPO = TOOLS.parent


def role_file(name: str, skills: str, body: str) -> str:
    return f"---\nname: {name}\ndescription: {name} role.\nskills: {skills}\n---\n\n{body}\n"


class WithheldTests(Repo):
    """J016 G3 audit D B1-B3, R12, R13, E TT-01, TT-17, TT-18; lead decision LD8 (rules/knowledge.md §3 withheld table)."""

    def held_out_notes(self) -> None:
        text = fm("job") + "# Boss anchor answers\n\nThe boss anchor answers: art bible anchors review.\n"
        for rel in (
            "knowledge/jobs/J1-x/hidden-answers.md",
            "knowledge/jobs/J1-x/grades-hidden.md",
            "knowledge/jobs/J1-x/evals-hidden.md",
            "knowledge/jobs/J1-x/analyst/hidden-rerun/q1.md",
            "knowledge/jobs/J1-x/Hidden-Cases.md",
        ):
            self.write(rel, text)
        self.write("knowledge/jobs/J1-x/hidden-rerun/decisions.md", fm("job") + "# Decisions\n\nRevision: 9\n")
        self.write("knowledge/jobs/J1-x/contract-hidden.md", fm("job", extra="revision: 2\n") + "# Contract\n\ntext\n")
        self.write("knowledge/jobs/J1-x/job-card.md", fm("job", extra="revision: 1\n") + "# Job card\n\nReview the art bible anchors.\n")
        self.write("knowledge/design/anchors.md", fm() + "# Anchor register\n\nArt bible anchors for the boss review. See [[jobs/J1-x/hidden-answers]].\n")

    def test_hidden_files_are_never_ranked_linked_or_named(self):
        self.held_out_notes()
        self.write("kit.json", json.dumps({"context": {"exclude": ["knowledge/generated"]}}))  # a config exclude list cannot re-admit them
        corpus = cp.Corpus(self.root)
        self.assertFalse([p for p in corpus.notes if "hidden" in p.lower()])
        for role, job in ((None, None), (None, "J1-x")):
            hits = cp.rank(corpus, "boss anchor answers art bible review", job=job)[0]
            self.assertIn("knowledge/design/anchors.md", [h.path for h in hits])
            self.assertFalse([h.path for h in hits if "hidden" in h.path.lower()])
        packet = cp.build(self.root, "boss anchor answers art bible review", job="J1-x")
        self.assertNotIn("hidden", json.dumps(packet).lower())
        self.assertNotIn("hidden", cp.render(packet).lower())
        self.assertEqual([f["path"] for f in packet["job"]["files"]], ["knowledge/jobs/J1-x/job-card.md"])
        self.assertIsNone(corpus.resolve_link("hidden-answers"))  # a bare stem never resolves to a held-out file

    def test_hidden_files_never_reach_generated_indexes_or_lint_output(self):
        self.held_out_notes()
        self.write("knowledge/jobs/J1-x/hidden-broken.md", "# no frontmatter\n")
        outputs = kb.build_indexes(self.root)
        self.assertIn("anchors.md", outputs["knowledge/generated/index-design.md"])
        self.assertNotIn("hidden", "".join(outputs.values()).lower())
        self.assertFalse([p for p in kb.knowledge_notes(self.root) if "hidden" in p.lower()])
        errors, warnings = kb.lint(self.root)
        self.assertNotIn("hidden", "\n".join(errors + warnings).lower())

    def test_direction_proposals_never_reach_the_packet(self):
        proposal = fm("job") + "# Direction proposal: art-director\n\nBoss intro cutscene direction proposal: storyboard, palette, cold light.\n"
        self.write("knowledge/jobs/J2-demo/direction/proposal-art-director.md", proposal)
        self.write("knowledge/jobs/J2-demo/direction/proposal-film-director.md", proposal.replace("art-director", "film-director"))
        self.write("knowledge/jobs/J2-demo/direction.md", fm("job", extra="revision: 1\n") + "# Direction sheet\n\nBoss intro cutscene direction after synthesis.\n")
        self.write("knowledge/jobs/J2-demo/job-card.md", fm("job") + "# Job card\n\nBoss intro cutscene.\n")
        packet = cp.build(self.root, "write the boss intro cutscene direction proposal and storyboard", job="J2-demo")
        self.assertNotIn("/proposal-", json.dumps(packet))
        self.assertIn("knowledge/jobs/J2-demo/direction.md", [r["path"] for r in packet["results"]])
        self.assertNotIn("proposal-", "".join(kb.build_indexes(self.root).values()))

    def test_underscore_material_from_another_game_is_withheld(self):
        self.write("knowledge/overlays/_moved-from-other-game.md", fm("overlay").replace("scope: universal", "scope: game") + "# Moved from OtherGame\n\nFireball effect lines for the VFX lab place.\n")
        self.write("knowledge/overlays/vfx-design.md", fm("overlay") + "# VFX design for this game\n\nFireball effect rules.\n")
        paths = [h.path for h in self.ranked("build a fireball effect for the VFX lab place")]
        self.assertIn("knowledge/overlays/vfx-design.md", paths)
        self.assertNotIn("knowledge/overlays/_moved-from-other-game.md", paths)
        self.assertNotIn("_moved", "".join(kb.build_indexes(self.root).values()))

    def test_skill_evals_not_ranked_and_read_next_names_skill_md(self):
        self.write(".agents/skills/data-saving/SKILL.md", "---\nname: data-saving\ndescription: Use when saving player data.\n---\n\n# Data saving\n\nSessions and locks.\n")
        self.write(".agents/skills/data-saving/references/receipts.md", "# Receipts\n\nShop purchase receipt saving: grant once per receipt.\n")
        self.write(".agents/skills/data-saving/evals/briefs.md", "# Eval briefs\n\n## E-01 shop purchase receipt saving\n\nPass when the shop purchase receipt saving grants once.\n")
        packet = cp.build(self.root, "shop purchase receipt saving")
        self.assertNotIn("/evals/", json.dumps(packet))
        self.assertEqual(packet["results"][0]["path"], ".agents/skills/data-saving/references/receipts.md")
        self.assertTrue(packet["read_next"][0].startswith("load skill `data-saving` (.agents/skills/data-saving/SKILL.md)"), packet["read_next"][0])
        self.assertIn(".agents/skills/data-saving/references/receipts.md", packet["read_next"][0])

    def test_sibling_copies_of_one_section_take_one_slot(self):
        for name in ("anime", "cartoon", "claytoy", "pixel"):
            self.write(f"knowledge/jobs/J3-x/art/bible-{name}.md", fm("job") + f"# Bible {name}\n\n## Families\n\nShape families for the character model review.\n")
        self.write("knowledge/design/review.md", fm() + "# Review\n\n## Character model review\n\nReview the character model.\n")
        for name, extra in (("doc-keeper", ""), ("explore", " Lesson drafts go to the inbox."), ("modeler", " More words here for length.")):
            self.write(f".agents/roles/{name}.md", f"---\nname: {name}\n---\n\n## Hand-back\n\nLesson drafts after the job ends.{extra}\n")
        hits = self.ranked("character model review families")
        families = [h for h in hits if h.heading == "Families"]
        self.assertEqual(len(families), 1)
        handbacks = [h for h in self.ranked("where do lesson drafts go after a job ends") if h.heading == "Hand-back"]
        self.assertEqual(len(handbacks), 1)  # different scores, same section in sibling files (audit D: role hand-backs filled 4 slots)

    def test_real_repo_corpus_and_indexes_name_no_held_out_path(self):
        # Real content and scale (testing T-03). Paths only: never print a held-out file's content.
        corpus = cp.Corpus(REPO)
        self.assertGreater(len(corpus.notes), 300)
        leaked = sorted(p for p in corpus.notes if "hidden" in p.lower())
        self.assertEqual(leaked, [], "held-out paths in the packet corpus")
        rows = [line for text in kb.build_indexes(REPO).values() for line in text.splitlines() if line.startswith("| [")]
        self.assertGreater(len(rows), 300)
        linked = [line.split("](", 1)[1].split(")", 1)[0] for line in rows]
        self.assertEqual([p for p in linked if "hidden" in p.lower()], [], "held-out paths in the generated indexes")
        self.assertEqual(sum(1 for line in rows if cp.names_held_out(line)), 0, "index rows that name a held-out file")


class RepairRoundTests(Repo):
    """J016 G3 repair round 1: audit E N-01 (held_out frontmatter key), audit D N1 (job history for craft roles), N2 (distinct siblings)."""

    def test_held_out_key_withholds_a_visible_name_like_a_hidden_one(self):
        grade = "# Grades\n\nDaily reward rubric line: spacing of usable rewards, pass.\n"
        self.write("knowledge/jobs/J1-x/grades-g2.md", fm("job", extra="held_out: true\n") + grade)
        self.write("knowledge/jobs/J1-x/contract-rubric.md", fm("job", extra="held_out: true\nrevision: 2\n") + "# Contract\n\nDaily reward rubric.\n")
        self.write("knowledge/jobs/J1-x/kept.md", fm("job", extra="held_out: false\n") + "# Kept\n\nDaily reward rubric spacing notes.\n")
        self.write("knowledge/jobs/J1-x/job-card.md", fm("job") + "# Job card\n\nDaily reward chest.\n")
        self.write("knowledge/design/reward.md", fm() + "# Daily reward\n\nDaily reward rubric spacing. See [[jobs/J1-x/grades-g2]] and [[grades-g2]].\n")
        corpus = cp.Corpus(self.root)
        self.assertNotIn("knowledge/jobs/J1-x/grades-g2.md", corpus.notes)
        self.assertIsNone(corpus.resolve_link("grades-g2"))
        packet = cp.build(self.root, "daily reward rubric spacing usable rewards", job="J1-x")
        paths = [r["path"] for r in packet["results"]] + [f["path"] for f in packet["job"]["files"]]
        self.assertNotIn("knowledge/jobs/J1-x/grades-g2.md", paths)
        self.assertNotIn("knowledge/jobs/J1-x/contract-rubric.md", paths)
        self.assertIn("knowledge/jobs/J1-x/kept.md", paths)  # held_out: false is an ordinary note
        self.assertNotIn("grades-g2.md", " ".join(packet["read_next"]))
        index = "".join(kb.build_indexes(self.root).values())
        self.assertNotIn("grades-g2.md", index)
        self.assertNotIn("contract-rubric.md", index)
        self.assertIn("kept.md", index)
        errors, warnings = kb.lint(self.root)
        self.assertEqual(errors, [])
        self.assertFalse(any("`held_out`" in w for w in warnings), warnings)

    def test_real_repo_marked_notes_are_withheld(self):
        marked = sorted(rel for rel in kb.knowledge_notes(REPO) if cp.marked_held_out((cp.load_note(REPO, REPO / rel).meta or {})))
        self.assertGreaterEqual(len(marked), 20)
        corpus = cp.Corpus(REPO)
        self.assertEqual([p for p in marked if p in corpus.notes], [])
        index = "".join(kb.build_indexes(REPO).values())
        self.assertEqual([p for p in marked if "(../" + p.split("/", 1)[1] + ")" in index], [])

    def job_history(self) -> None:
        self.write(".agents/roles/sound-designer.md", role_file("sound-designer", "sound-design", "Sound."))
        self.write(".agents/roles/doc-keeper.md", role_file("doc-keeper", "orchestration", "Records."))
        self.write(".agents/skills/sound-design/SKILL.md", "---\nname: sound-design\ndescription: Use for SFX.\n---\n\n# Sound design\n\nA boss stinger cue for the reveal.\n")
        audit = fm("job") + "# Audit\n\n## Design the boss stinger and reveal cue sounds\n\nDesign the boss stinger and reveal cue sounds: boss stinger, reveal cue, sounds ranked for the boss stinger.\n"
        self.write("knowledge/jobs/J7-x/reviews/audit.md", audit)
        self.write("knowledge/jobs/J7-x/exchange/r1-vfx.md", audit.replace("# Audit", "# Exchange"))
        self.write("knowledge/jobs/J7-x/job-card.md", fm("job") + "# Job card\n\nBoss intro.\n")

    def test_job_history_ranks_below_a_craft_roles_book(self):
        self.job_history()
        corpus = cp.Corpus(self.root)
        task = "design the boss stinger and reveal cue sounds"
        plain = [h.path for h in cp.rank(corpus, task, None, "J7-x")[0]]
        self.assertLess(plain.index("knowledge/jobs/J7-x/reviews/audit.md"), plain.index(".agents/skills/sound-design/SKILL.md"))
        craft = [h.path for h in cp.rank(corpus, task, "sound-designer", "J7-x")[0]]
        self.assertEqual(craft[0], ".agents/skills/sound-design/SKILL.md")
        self.assertLess(craft.index(".agents/skills/sound-design/SKILL.md"), craft.index("knowledge/jobs/J7-x/exchange/r1-vfx.md"))
        for role in ("orchestrator", "doc-keeper"):  # the lead and the filer keep the job history at full weight
            with self.subTest(role=role):
                hits = {h.path: h.score for h in cp.rank(corpus, task, role, "J7-x")[0]}
                base = {h.path: h.score for h in cp.rank(corpus, task, None, "J7-x")[0]}
                self.assertAlmostEqual(hits["knowledge/jobs/J7-x/reviews/audit.md"], base["knowledge/jobs/J7-x/reviews/audit.md"])

    def test_closed_job_history_ranks_lower_for_everyone(self):
        # J016 follow-up: a closed job's reviews and exchange notes are history (its lessons were filed at close),
        # so they rank lower for every role; an open job's keep full weight for the lead and the filer.
        self.write("knowledge/jobs/active.md", "# Active jobs\n\n- J8-open · an open job\n")
        text = fm("job") + "# Review\n\nThe quest reward chest timing review found the chest opens late.\n"
        self.write("knowledge/jobs/J8-open/reviews/chest.md", text)
        self.write("knowledge/jobs/J9-done/reviews/chest.md", text)
        corpus = cp.Corpus(self.root)
        task = "quest reward chest timing"
        for role in (None, "orchestrator", "doc-keeper"):
            with self.subTest(role=role):
                hits = {h.path: h.score for h in cp.rank(corpus, task, role)[0]}
                self.assertLess(hits["knowledge/jobs/J9-done/reviews/chest.md"], hits["knowledge/jobs/J8-open/reviews/chest.md"])
        asked = {h.path: h.score for h in cp.rank(corpus, task, "orchestrator", "J9-done")[0]}
        self.assertGreater(asked["knowledge/jobs/J9-done/reviews/chest.md"], asked["knowledge/jobs/J8-open/reviews/chest.md"], "a job named with --job is never lowered")

    def test_distinct_sibling_sections_both_rank(self):
        self.write("knowledge/inbox/2026-10-21-J11-lead.md", fm("lesson") + "# Lead draft\n\n## Owner corrections\n\nThe owner said the curve felt too slow after level ten; cut the wall.\n")
        self.write("knowledge/inbox/2026-10-21-J11-designer.md", fm("lesson") + "# Designer draft\n\n## Owner corrections\n\nThe owner asked for owner-visible milestones and fewer corrections to pity odds.\n")
        heads = [h.path for h in self.ranked("owner corrections in the lesson drafts") if h.heading == "Owner corrections"]
        self.assertEqual(sorted(heads), ["knowledge/inbox/2026-10-21-J11-designer.md", "knowledge/inbox/2026-10-21-J11-lead.md"])


class RoleRankingTests(Repo):
    """J016 G3 audit D R1, B6, E TT-15, TT-16: --role ranks the role's own book and lists its precedents."""

    def roles(self) -> None:
        self.write(".agents/roles/sound-designer.md", role_file("sound-designer", "sound-design", "You design sound."))
        self.write(".agents/roles/film-director.md", role_file("film-director", "film-direction", "You direct the boss entrance: stinger, reveal and cue timing for the boss entrance."))
        self.write(".agents/skills/sound-design/SKILL.md", "---\nname: sound-design\ndescription: Use when designing SFX, music and cues.\n---\n\n# Sound design\n\n## Reveal cues\n\nA stinger cue for a reveal: layer the hit.\n")
        self.write(".agents/skills/film-direction/SKILL.md", "---\nname: film-direction\ndescription: Use for cutscenes.\n---\n\n# Film direction\n\nShots.\n")

    def test_role_ranks_its_own_skill_above_another_roles_file(self):
        self.roles()
        task = "design the boss entrance stinger and reveal cue sounds"
        corpus = cp.Corpus(self.root)
        plain = [h.path for h in cp.rank(corpus, task)[0]]
        self.assertLess(plain.index(".agents/roles/film-director.md"), plain.index(".agents/skills/sound-design/SKILL.md"))  # the audit's case
        hits = cp.rank(corpus, task, role="sound-designer")[0]
        ranked = [h.path for h in hits]
        self.assertLess(ranked.index(".agents/skills/sound-design/SKILL.md"), ranked.index(".agents/roles/film-director.md"))
        own = next(h for h in hits if h.path == ".agents/skills/sound-design/SKILL.md")
        self.assertIn("; own book of role sound-designer", own.why)

    def test_role_block_lists_precedents_of_the_role_and_names_vocabulary(self):
        self.roles()
        self.write(
            "knowledge/design/precedents.md",
            fm() + "# Precedents\n\n| ID | Craft (kit roles) | What it is | Why | Path @ revision | Decision | Date |\n| --- | --- | --- | --- | --- | --- | --- |\n"
            "| P-1 | sound-designer | Boss stinger | \"that hit\" | content/sound/stinger.md@3 | D-4 | 2026-10-20 |\n"
            "| P-2 | vfx-designer, film-director | Slam shot | \"yes\" | content/vfx/slam.md@2 | D-5 | 2026-10-20 |\n",
        )
        self.write("knowledge/design/vocabulary.md", fm() + "# Vocabulary\n\n| Name | Kind |\n| --- | --- |\n")
        info = cp.role_info(self.root, "sound-designer")
        self.assertEqual([r["row"].split("|")[1].strip() for r in info["precedents"]], ["P-1"])
        text = "\n".join(info["lines"])
        self.assertIn("| P-1 | sound-designer | Boss stinger |", text)
        self.assertNotIn("P-2", text)
        self.assertIn("`knowledge/design/vocabulary.md`", text)
        self.assertEqual([r["row"].split("|")[1].strip() for r in cp.role_info(self.root, "film-director")["precedents"]], ["P-2"])

    def test_orchestrator_role_loads_the_orchestration_skill(self):
        self.write(".agents/skills/orchestration/SKILL.md", "---\nname: orchestration\ndescription: The lead's playbook.\n---\n\n# Orchestration\n\nSize the job.\n")
        info = cp.role_info(self.root, "orchestrator")
        self.assertEqual(info["skills"], ["orchestration"])
        self.assertIn("orchestration", "\n".join(info["lines"]))
        code, _, err = run_cli(cp.main, ["--root", str(self.root), "packet", "size the job", "--role", "orchestrator"])
        self.assertEqual(code, 0, err)

    def test_unknown_job_message_says_what_to_do(self):
        (self.root / "knowledge/jobs").mkdir(parents=True)
        code, out, err = run_cli(cp.main, ["--root", str(self.root), "packet", "storyboard", "--job", "J099-tabletop"])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("unknown job `J099-tabletop`", err)
        self.assertIn("omit --job", err)


class EvalCaseTests(Repo):
    """J016 G3 audit D B4, E TT-01: cases carry role and job; a case can forbid paths."""

    def test_case_role_and_job_reach_the_ranking(self):
        self.write(".agents/roles/sound-designer.md", role_file("sound-designer", "sound-design", "Sound."))
        self.write(".agents/roles/film-director.md", role_file("film-director", "film-direction", "Boss entrance stinger and reveal cue timing."))
        self.write(".agents/skills/sound-design/SKILL.md", "---\nname: sound-design\ndescription: Use for SFX.\n---\n\n# Sound design\n\nA stinger cue for a reveal at the boss entrance.\n")
        self.write("knowledge/jobs/J5-demo/job-card.md", fm("job") + "# Job card\n\nBoss entrance stinger reveal cue.\n")
        self.write("knowledge/jobs/J6-other/job-card.md", fm("job") + "# Job card\n\nBoss entrance stinger reveal cue.\n")
        task = "boss entrance stinger reveal cue"
        expect = [".agents/skills/sound-design/SKILL.md", "knowledge/jobs/J5-demo/job-card.md"]
        plain = ev.evaluate(self.root, [{"task": task, "expect": expect}])["cases"][0]
        tagged = ev.evaluate(self.root, [{"task": task, "expect": expect, "role": "sound-designer", "job": "J5"}])["cases"][0]
        self.assertEqual(plain["ranks"][1], 2)  # without --job the two equal job cards tie; J5 wins on path order only
        self.assertGreater(plain["ranks"][0], 1)  # without --role another role's file outranks the skill
        self.assertEqual(sorted(tagged["ranks"]), [1, 2])  # with both: the role's skill and the job's card lead

    def test_forbidden_path_fails_a_case(self):
        self.write("knowledge/systems/eggs.md", fm("system") + "# Eggs\n\nEgg hatch odds.\n")
        self.write("knowledge/systems/egg-draft.md", fm("system") + "# Egg draft\n\nEgg hatch odds draft.\n")
        cases = [
            {"task": "egg hatch odds", "expect": ["knowledge/systems/eggs.md"], "forbid": ["*-draft.md"]},
            {"task": "egg hatch odds", "expect": ["knowledge/systems/eggs.md"], "forbid": ["*hidden*"]},
        ]
        rows = ev.evaluate(self.root, cases)["cases"]
        self.assertFalse(rows[0]["pass"])
        self.assertEqual(rows[0]["forbidden"], ["knowledge/systems/egg-draft.md"])
        self.assertTrue(rows[1]["pass"])
        self.assertIn("forbidden", ev.report(ev.evaluate(self.root, cases), 5))

    def test_bad_role_or_forbid_field_is_a_bad_line(self):
        self.write("knowledge/evals/retrieval.jsonl", '{"task": "egg odds", "expect": ["a.md"], "forbid": "*hidden*"}\n')
        self.assertEqual(quiet(ev.main, ["--root", str(self.root)]), 2)


class DescriptionBudgetTests(Repo):
    """verify.py check f (J016-D4): every .agents/skills/*/SKILL.md description <= 400 characters."""

    def test_long_descriptions_listed_with_length(self):
        self.write(".agents/skills/short/SKILL.md", "---\nname: short\ndescription: Use when x.\n---\n# S\n")
        self.write(".agents/skills/edge/SKILL.md", "---\nname: edge\ndescription: " + "e" * 400 + "\n---\n# E\n")
        self.write(".agents/skills/long/SKILL.md", "---\nname: long\ndescription: \"" + "l" * 401 + "\"\n---\n# L\n")
        self.write(".agents/skills/none/SKILL.md", "# No frontmatter\n")
        self.assertEqual(verify.long_descriptions(self.root), [("long", 401)])

    def test_gate_line_f(self):
        self.write(".agents/skills/long/SKILL.md", "---\nname: long\ndescription: " + "l" * 450 + "\n---\n# L\n")
        buf = io.StringIO()
        self.assertEqual(verify.run(self.root, fast=True, out=buf), 1)
        self.assertIn("FAIL skill descriptions: 1 over 400 characters: long 450", buf.getvalue())
        (self.root / ".agents/skills/long/SKILL.md").write_text("---\nname: long\ndescription: ok\n---\n", encoding="utf-8")
        buf = io.StringIO()
        verify.run(self.root, fast=True, out=buf)
        self.assertIn("PASS skill descriptions: all <= 400 characters", buf.getvalue())


class LintTests(Repo):
    def test_roles_key_accepted_and_unknown_role_names_warned(self):
        self.write(".agents/roles/film-director.md", "---\nname: film-director\n---\nx\n")
        self.write(".agents/roles/README.md", "# not a role\n")
        self.write("knowledge/lessons/a.md", fm("lesson", extra="roles: [film-director, animatr]\n") + "# A\n\ntext\n")
        self.write("knowledge/lessons/b.md", fm("lesson", extra="roles: film-director\n") + "# B\n\ntext\n")
        errors, warnings = kb.lint(self.root)
        self.assertEqual(errors, [])
        self.assertFalse(any("unknown frontmatter key `roles`" in w for w in warnings))
        self.assertIn("knowledge/lessons/a.md: roles lists `animatr`, not a kit role (.agents/roles/)", warnings)
        self.assertFalse(any("b.md: roles" in w for w in warnings))

    def test_revision_key_accepted(self):
        self.write("knowledge/jobs/J1-x/direction-sheet.md", fm("job", extra="revision: 3\n") + "# Direction\n\ntext\n")
        self.write("knowledge/jobs/J1-x/contract-camera.md", fm("job", extra="revision: r2 camera handover\n") + "# Contract\n\ntext\n")
        errors, warnings = kb.lint(self.root)
        self.assertEqual(errors, [])
        self.assertFalse(any("`revision`" in w for w in warnings), warnings)

    def test_frontmatter_errors(self):
        self.write("knowledge/design/none.md", "# No frontmatter\n\ntext\n")
        self.write("knowledge/design/bad.md", "---\ntype: thing\nscope: everywhere\nstatus: active\nupdated: last week\n---\n# Bad\n")
        self.write("knowledge/design/README.md", "# Readme is exempt\n")
        self.write("knowledge/templates/t.md", "# Template is exempt\n")
        self.write("knowledge/design/good.md", fm() + "# Good\n\ntext\n")
        errors, warnings = kb.lint(self.root)
        text = "\n".join(errors)
        self.assertIn("knowledge/design/none.md:1: missing frontmatter", text)
        self.assertIn("invalid type `thing`", text)
        self.assertIn("invalid scope `everywhere`", text)
        self.assertIn("`updated: last week` is a relative date", text)
        self.assertNotIn("README.md", text)
        self.assertNotIn("templates", text)
        self.assertNotIn("good.md", text)
        self.assertTrue(any("bad.md: frontmatter missing `source`" in w for w in warnings))
        self.assertEqual(quiet(kb.main, ["--root", str(self.root), "--lint"]), 1)

    def test_dead_links_and_superseded_without_replacement(self):
        self.write("knowledge/design/a.md", fm() + "# A\n\nSee [[design/b]] and [[design/missing]] and `[[in/code]]`.\n")
        self.write("knowledge/design/b.md", fm() + "# B\n\ntext\n")
        self.write("knowledge/design/old.md", fm(status="superseded") + "# Old\n\nNo pointer.\n")
        self.write("rules/x.md", "# Rule\n\n[[nowhere/at-all]]\n")
        errors, _ = kb.lint(self.root)
        text = "\n".join(errors)
        self.assertIn("knowledge/design/a.md:12: dead link [[design/missing]]", text)
        self.assertNotIn("[[design/b]]", text)
        self.assertNotIn("in/code", text)
        self.assertIn("rules/x.md:3: dead link [[nowhere/at-all]]", text)
        self.assertIn("old.md: superseded but links no replacement", text)

    def test_warnings_long_notes_and_duplicate_titles(self):
        self.write("knowledge/design/long.md", fm() + "# Same\n\n" + "line\n" * 310)
        self.write("knowledge/logs/other.md", fm("log") + "# Same\n\ntext\n")
        errors, warnings = kb.lint(self.root)
        self.assertEqual(errors, [])
        self.assertTrue(any("over 300" in w for w in warnings))
        self.assertTrue(any(w.startswith("duplicate title `same`") for w in warnings))
        self.assertEqual(quiet(kb.main, ["--root", str(self.root), "--lint"]), 0)


class IndexTests(Repo):
    def test_index_generation_is_deterministic_and_checked(self):
        self.write("knowledge/index.md", fm("index") + "# Hand index\n")
        self.write("knowledge/systems/b.md", fm("system") + "# Bravo\n\nBravo does things. More text.\n")
        self.write("knowledge/systems/a.md", fm("system") + "# Alpha | pipe\n\n- Alpha first sentence. Second.\n")
        self.write("knowledge/logs/2026-10-01-x.md", fm("log") + "# Log\n\nDid it.\n")
        self.write("knowledge/external/docs/x.md", "# External\n")
        first = kb.build_indexes(self.root)
        self.assertEqual(first, kb.build_indexes(self.root))
        self.assertEqual(sorted(first), ["knowledge/generated/index-logs.md", "knowledge/generated/index-systems.md"])
        systems = first["knowledge/generated/index-systems.md"]
        self.assertLess(systems.index("Alpha"), systems.index("Bravo"))
        self.assertIn("Alpha first sentence.", systems)
        self.assertNotIn("Second.", systems)
        self.assertIn("Alpha \\| pipe", systems)
        self.assertEqual(quiet(kb.main, ["--root", str(self.root), "--check"]), 1)
        hand = (self.root / "knowledge/index.md").read_text(encoding="utf-8")
        self.assertEqual(quiet(kb.main, ["--root", str(self.root)]), 0)
        self.assertEqual(quiet(kb.main, ["--root", str(self.root), "--check"]), 0)
        self.assertEqual((self.root / "knowledge/index.md").read_text(encoding="utf-8"), hand)
        (self.root / "knowledge/logs/2026-10-01-x.md").unlink()
        self.assertEqual(kb.stale(self.root), ["orphan knowledge/generated/index-logs.md (area has no notes)"])


class EvalTests(Repo):
    def test_metrics_math(self):
        self.assertEqual(ev.recall_at([1, 7, None], 5), 1 / 3)
        self.assertEqual(ev.recall_at([1, 7, None], 10), 2 / 3)
        self.assertEqual(ev.reciprocal_rank([7, 3, None]), 1 / 3)
        self.assertEqual(ev.reciprocal_rank([None]), 0.0)

    def test_expectation_matching(self):
        self.assertTrue(ev.matches("rules/company.md#2", "rules/company.md", "2. Job sizes and owner gates"))
        self.assertFalse(ev.matches("rules/company.md#2", "rules/company.md", "20. Other"))
        self.assertTrue(ev.matches("rules/company.md", "rules/company.md", "anything"))
        self.assertTrue(ev.matches("a.md#job-sizes", "a.md", "Job sizes"))
        self.assertFalse(ev.matches("b.md", "a.md", "x"))

    def test_evaluate_and_compare(self):
        self.write("knowledge/systems/eggs.md", fm("system") + "# Eggs\n\nEgg hatch odds.\n")
        self.write("knowledge/systems/shop.md", fm("system") + "# Shop\n\nBuy gear with gold.\n")
        cases = [
            {"task": "egg hatch odds", "expect": ["knowledge/systems/eggs.md"]},
            {"task": "buy gear", "expect": ["knowledge/systems/shop.md#shop", "knowledge/systems/missing.md"]},
        ]
        result = ev.evaluate(self.root, cases)
        self.assertEqual(result["overall"]["passed"], 1)
        self.assertEqual(result["cases"][1]["recall@10"], 0.5)
        self.assertEqual(result["overall"]["recall@10"], 0.75)
        self.assertEqual(result["overall"]["mrr"], 1.0)
        better = json.loads(json.dumps(result))
        better["overall"]["recall@10"] = 0.9
        _, dropped = ev.compare(result, better)
        self.assertTrue(dropped)
        _, dropped = ev.compare(result, result)
        self.assertFalse(dropped)

    def test_compare_keeps_same_task_cases_apart(self):
        # Two cases may share a task and differ by role or job (J016 follow-up): each is compared with its own saved row.
        row = {"task": "t", "expect": [], "ranks": [], "recall@5": 1.0, "recall@10": 1.0, "mrr": 1.0, "pass": True, "top": [], "forbidden": []}
        a = dict(row, role=None, job=None)
        b = dict(row, role="architect", job=None, mrr=0.5)
        result = {"overall": {"recall@5": 1.0, "recall@10": 1.0, "mrr": 0.75}, "cases": [a, b]}
        text, dropped = ev.compare(result, json.loads(json.dumps(result)))
        self.assertFalse(dropped)
        self.assertNotIn("->", text.split("overall")[0], "no change line for unchanged cases")

    def test_mirror_expectations_scored_against_docs_list(self):
        self.write("knowledge/systems/sword.md", fm("system") + "# Sword\n\nSword swing streak.\n")
        base = "knowledge/external/roblox-creator-docs"
        self.write(f"{base}/effects/trails.md", page("Trails", "Streak behind a moving sword.", "Trail streak sword."))
        self.write(f"{base}/effects/beams.md", page("Beams", "Laser between points.", "Beam laser."))
        self.write(f"{base}/_api-reference/classes/Trail.yaml", "name: Trail\n")
        cases = [
            {"task": "sword streak", "expect": [f"{base}/effects/trails.md"]},
            {"task": "sword streak with a Trail", "expect": ["knowledge/systems/sword.md", f"{base}/_api-reference/classes/Trail.yaml", f"{base}/effects/beams.md"]},
        ]
        result = ev.evaluate(self.root, cases)
        self.assertEqual(result["cases"][0]["ranks"], [1])
        ranks = result["cases"][1]["ranks"]
        self.assertEqual(ranks[0], 1)
        self.assertEqual(ranks[1], 1)
        self.assertIsNone(ranks[2])
        self.assertTrue(any(t.startswith(f"{base}/effects/trails.md") for t in result["cases"][0]["top"]))

    def test_cli_save_compare_and_bad_lines(self):
        self.write("knowledge/systems/eggs.md", fm("system") + "# Eggs\n\nEgg hatch odds.\n")
        self.write("knowledge/evals/retrieval.jsonl", '# comment\n{"task": "egg odds", "expect": ["knowledge/systems/eggs.md"]}\n')
        saved = self.root / "run.json"
        self.assertEqual(quiet(ev.main, ["--root", str(self.root), "--save", str(saved)]), 0)
        self.assertEqual(json.loads(saved.read_text(encoding="utf-8"))["overall"]["recall@10"], 1.0)
        self.assertEqual(quiet(ev.main, ["--root", str(self.root), "--compare", str(saved)]), 0)
        self.write("knowledge/evals/retrieval.jsonl", '{"task": "x"}\n')
        self.assertEqual(quiet(ev.main, ["--root", str(self.root)]), 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
