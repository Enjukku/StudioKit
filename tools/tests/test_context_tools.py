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
