"""Offline tests for the Claude Code hook scripts in tools/hooks/ (J016-T01).

Each hook runs as a real subprocess with JSON on stdin, against a copy of tools/tests/fixtures/context/repo.
Run: python -m unittest tools.tests.test_hooks
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
HOOKS = TOOLS / "hooks"
FIXTURE = TOOLS / "tests" / "fixtures" / "context" / "repo"
CAP = 4000
REASON = "Hand-back must start with 'STATUS: done | blocked | needs-decision | failed.' and include coverage (rules/messages.md §3)."
GOOD_HANDBACK = "STATUS: done. Built the tools.\n\n<spec>\ncoverage:\n  - C1: done\n</spec>\n"


class HookCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="kit-hooks-"))
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)
        self.root = self.tmp / "repo"
        shutil.copytree(FIXTURE, self.root)

    def hook(self, script: str, payload, root: Path | None = None) -> tuple[int, str, str]:
        data = payload if isinstance(payload, (str, bytes)) else json.dumps(payload)
        data = data.encode("utf-8") if isinstance(data, str) else data
        proc = subprocess.run(
            [sys.executable, str(HOOKS / script), "--root", str(root or self.root)],
            input=data, capture_output=True, timeout=60,
        )
        return proc.returncode, proc.stdout.decode("utf-8"), proc.stderr.decode("utf-8")

    def context(self, script: str, payload, event: str) -> str:
        code, out, err = self.hook(script, payload)
        self.assertEqual(code, 0, err)
        data = json.loads(out)
        self.assertEqual(list(data), ["hookSpecificOutput"])
        self.assertEqual(data["hookSpecificOutput"]["hookEventName"], event)
        text = data["hookSpecificOutput"]["additionalContext"]
        self.assertLessEqual(len(text), CAP)
        return text

    def assert_silent_success(self, script: str, payload, root: Path | None = None) -> str:
        code, out, err = self.hook(script, payload, root)
        self.assertEqual(code, 0)
        self.assertEqual(out, "")
        self.assertLessEqual(len(err.strip().splitlines()), 1)
        return err


def start(agent_type: str) -> dict:
    return {"session_id": "s1", "transcript_path": "t.jsonl", "cwd": "C:\\repo", "hook_event_name": "SubagentStart", "agent_id": "agent-1", "agent_type": agent_type}


class SubagentContextTests(HookCase):
    def test_kit_role_gets_job_pointer(self):
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("J016-demo · Boss intro cutscene", text)
        self.assertIn("`knowledge/jobs/J016-demo/job-card.md` · revision 4", text)
        self.assertIn("`knowledge/overlays/film-director.md`", text)
        self.assertIn("`knowledge/overlays/film-craft.md`", text)
        self.assertIn("`knowledge/reference/roblox/docs-map.md` L15", text)
        self.assertIn('Run: python tools/context_packet.py packet "<your task>" --role film-director --job J016-demo', text)

    def test_non_kit_agent_gets_nothing(self):
        for agent in ("general-purpose", "Explore", "README", ""):
            with self.subTest(agent=agent):
                self.assertEqual(self.assert_silent_success("subagent_context.py", start(agent)), "")  # a skip, not an error
        payload = start("x")
        del payload["agent_type"]
        self.assertEqual(self.assert_silent_success("subagent_context.py", payload), "")

    def test_no_active_jobs_still_gives_role_docs(self):
        # J026-D1: the docs row reaches the role in a game with no open job (GreatWallSim main had no active.md).
        active = self.root / "knowledge/jobs/active.md"
        active.write_text(active.read_text(encoding="utf-8").replace("- J016-demo · Boss intro cutscene\n", ""), encoding="utf-8")
        for _ in range(2):
            text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
            self.assertIn("Roblox docs for this role", text)
            self.assertIn('Run: python tools/context_packet.py packet "<your task>" --role film-director', text)
            self.assertNotIn("--job", text)
            if active.exists():
                active.unlink()

    def test_docs_row_cells_not_a_line_number(self):
        # J026-D1: the hook prints the role's sections and key pages, not only "docs-map.md L<n>".
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("sections `workspace/camera/`, `animation/`.", text)
        self.assertIn("Key pages: workspace/camera/index.md.", text)
        self.assertIn("list it in `docs_read`", text)

    def test_role_without_docs_row_says_so(self):
        shutil.copy(self.root / ".agents/roles/film-director.md", self.root / ".agents/roles/sound-designer.md")
        text = self.context("subagent_context.py", start("sound-designer"), "SubagentStart")
        self.assertIn("Roblox docs: no row names this role", text)

    def test_docs_pages_dropped_before_run_lines(self):
        # J026-D1: over the cap, job file lines go first, then the key pages; the Run line stays.
        docs_map = self.root / "knowledge/reference/roblox/docs-map.md"
        long_pages = "; ".join(f"workspace/camera/page-{i:03}.md" for i in range(300))
        docs_map.write_text(docs_map.read_text(encoding="utf-8").replace("| workspace/camera/index.md |", f"| {long_pages} |"), encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("Key pages: your role file.", text)
        self.assertIn('Run: python tools/context_packet.py packet "<your task>" --role film-director --job J016-demo', text)

    def test_context_capped_and_run_line_kept(self):
        for i in range(200):
            (self.root / f"knowledge/jobs/J016-demo/contract-{i:03}-a-long-file-name-for-the-cap.md").write_text(f"Revision: {i}\n", encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn('Run: python tools/context_packet.py packet "<your task>" --role film-director --job J016-demo', text)

    def test_active_job_without_folder_does_not_fail(self):
        active = self.root / "knowledge/jobs/active.md"
        active.write_text(active.read_text(encoding="utf-8") + "- J099-gone · Missing folder\n", encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("--job J016-demo", text)
        self.assertNotIn("--job J099-gone", text)

    def test_withheld_context_line(self):
        # Audit D B7: the withheld-context rule for the step (design-context §3b).
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("Withheld on purpose (rules/knowledge.md §3)", text)
        for item in ("other leads' direction proposals", "hidden", "the maker's hand-back", "other games' notes"):
            self.assertIn(item, text)

    def test_held_out_job_files_not_listed(self):
        (self.root / "knowledge/jobs/J016-demo/hidden-rerun").mkdir()
        (self.root / "knowledge/jobs/J016-demo/hidden-rerun/decisions.md").write_text("Revision: 9\n", encoding="utf-8")
        (self.root / "knowledge/jobs/J016-demo/contract-hidden.md").write_text("Revision: 2\n", encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("`knowledge/jobs/J016-demo/decisions.md`", text)
        self.assertNotIn("hidden-rerun", text)
        self.assertNotIn("contract-hidden", text)

    def test_role_precedents_and_vocabulary_named(self):
        # Audit D B6: the hook reuses the role block, so it names the role's precedent rows and the vocabulary.
        (self.root / "knowledge/design/precedents.md").write_text(
            "# Precedents\n\n| ID | Craft (kit roles) | What it is |\n| --- | --- | --- |\n| P-1 | film-director | Boss slam shot |\n| P-2 | vfx-designer | Spark |\n",
            encoding="utf-8")
        (self.root / "knowledge/design/vocabulary.md").write_text("# Vocabulary\n\n| Name | Kind |\n| --- | --- |\n", encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("Precedents for this role: `knowledge/design/precedents.md` L5", text)
        self.assertNotIn("L6", text)
        self.assertIn("knowledge/design/vocabulary.md", text)

    def test_two_active_jobs_get_a_lead_line(self):
        # Audit D R2: with parallel jobs the agent is told which one is its own.
        active = self.root / "knowledge/jobs/active.md"
        active.write_text(active.read_text(encoding="utf-8") + "- J017-other · Shop\n", encoding="utf-8")
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertIn("--job J016-demo", text)
        self.assertIn("--job J017-other", text)
        self.assertIn("Use the job your brief names; ignore the others.", text)

    def test_one_active_job_has_no_lead_line(self):
        text = self.context("subagent_context.py", start("film-director"), "SubagentStart")
        self.assertNotIn("Use the job your brief names", text)

    def test_bad_input_never_fails(self):
        for payload in (b"{not json", b"", b"[1, 2]", b"\xff\xfe"):
            with self.subTest(payload=payload):
                self.assert_silent_success("subagent_context.py", payload)
        self.assert_silent_success("subagent_context.py", start("film-director"), root=self.tmp / "no-such-repo")


def compact(source: str = "compact") -> dict:
    return {"session_id": "s1", "transcript_path": "t.jsonl", "cwd": "C:\\repo", "hook_event_name": "SessionStart", "source": source}


class CompactContextTests(HookCase):
    def test_status_and_undated_gates_then_reload_line(self):
        text = self.context("compact_context.py", compact(), "SessionStart")
        self.assertIn("J016-demo · Boss intro cutscene", text)
        self.assertIn("| Status | working: storyboard boards in review; G2 open |", text)
        self.assertIn("| G2 first samples | | |", text)
        self.assertIn("| G3 final look | — | |", text)
        self.assertNotIn("G1 brief", text)
        self.assertTrue(text.rstrip().endswith("Re-load the orchestration skill before the next step."))

    def test_open_tickets_counted_from_the_ledger(self):
        # Audit D R3: open tickets per job (design-context §3b: "open tickets").
        (self.root / "knowledge/jobs/J016-demo/ledger.md").write_text(
            "# Ledger\n\n| id | from | to | ask | inside | stage | status | result | updated |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
            "| T1 | a | b | x | yes | build | working | | 2026-10-20 |\n| T2 | a | b | x | yes | build | done | y | 2026-10-20 |\n"
            "| T3 | a | b | x | no | build | needs-decision | | 2026-10-21 |\n| T4 | a | b | x | yes | build | stale | | 2026-10-21 |\n",
            encoding="utf-8")
        text = self.context("compact_context.py", compact(), "SessionStart")
        self.assertIn("Open tickets: 2 (`knowledge/jobs/J016-demo/ledger.md`)", text)
        self.assertTrue(text.rstrip().endswith("Re-load the orchestration skill before the next step."))

    def test_other_session_sources_give_nothing(self):
        for source in ("startup", "resume", "clear"):
            with self.subTest(source=source):
                self.assert_silent_success("compact_context.py", compact(source))

    def test_capped_with_reload_line_last(self):
        card = self.root / "knowledge/jobs/J016-demo/job-card.md"
        card.write_text(card.read_text(encoding="utf-8") + "".join(f"| G{i} extra gate with a long name {'x' * 40} | | |\n" for i in range(4, 80)), encoding="utf-8")
        text = self.context("compact_context.py", compact(), "SessionStart")
        self.assertTrue(text.rstrip().endswith("Re-load the orchestration skill before the next step."))

    def test_bad_input_never_fails(self):
        for payload in (b"{not json", b"", b"null"):
            with self.subTest(payload=payload):
                self.assert_silent_success("compact_context.py", payload)
        (self.root / "knowledge/jobs/J016-demo/job-card.md").unlink()
        self.context("compact_context.py", compact(), "SessionStart")  # missing card: still the reload line


def stop(agent_type: str, message, active: bool = False) -> dict:
    payload = {"session_id": "s1", "transcript_path": "t.jsonl", "cwd": "C:\\repo", "hook_event_name": "SubagentStop", "stop_hook_active": active,
               "agent_id": "def456", "agent_type": agent_type, "agent_transcript_path": "a.jsonl", "last_assistant_message": message}
    if message is None:
        del payload["last_assistant_message"]
    return payload


class HandbackCheckTests(HookCase):
    def blocked(self, payload) -> None:
        code, out, err = self.hook("handback_check.py", payload)
        self.assertEqual(code, 0, err)
        self.assertEqual(json.loads(out), {"decision": "block", "reason": REASON})

    def test_good_handback_allowed(self):
        self.assert_silent_success("handback_check.py", stop("feature-builder", "\n\n" + GOOD_HANDBACK))

    def test_missing_status_first_line_blocked(self):
        self.blocked(stop("feature-builder", "Here is my work.\nSTATUS: done.\ncoverage:\n- x: done\n"))
        self.blocked(stop("feature-builder", "Status is done.\ncoverage: x\n"))

    def test_markdown_marks_before_status_allowed(self):
        # Audit D R4: a bold or heading STATUS line is still a STATUS first line.
        for first in ("**STATUS: done.** Built it.", "**STATUS:** done. Built it.", "## STATUS: done. Built it."):
            with self.subTest(first=first):
                self.assert_silent_success("handback_check.py", stop("feature-builder", first + "\n\ncoverage: all\n"))

    def test_coverage_only_in_prose_blocked(self):
        # Audit D R4: the word in a sentence is not the coverage list.
        self.blocked(stop("feature-builder", "STATUS: done. Test coverage is low, I skipped the list.\n"))
        for field in ("coverage:\n  - a: done", "- coverage: [a: done]", '{"coverage": ["a: done"]}', "**coverage:** a done"):
            with self.subTest(field=field):
                self.assert_silent_success("handback_check.py", stop("feature-builder", "STATUS: done. x\n<spec>\n" + field + "\n</spec>\n"))

    def test_coverage_only_in_an_example_block_blocked(self):
        # J018: a coverage line inside a code example is not the hand-back's coverage; a fenced <spec> block is.
        example = "STATUS: done. Built it.\n```text\ncoverage:\n  - a: done\n```\n"
        self.blocked(stop("feature-builder", example))
        spec_block = "STATUS: done. Built it.\n```text\n<spec>\ncoverage:\n  - a: done\n</spec>\n```\n"
        self.assert_silent_success("handback_check.py", stop("feature-builder", spec_block))

    def test_missing_coverage_blocked(self):
        self.blocked(stop("feature-builder", "STATUS: done. Built it.\nfiles: [a.py]\n"))

    def test_stop_hook_active_allows(self):
        self.assert_silent_success("handback_check.py", stop("feature-builder", "no status", active=True))

    def test_non_kit_agent_allowed(self):
        self.assert_silent_success("handback_check.py", stop("general-purpose", "no status"))

    def test_no_message_text_allowed(self):
        # A hand-back sent through a tool (SubagentHandback) can leave no final text; the hook cannot judge it.
        for message in (None, "", "  \n", 42):
            with self.subTest(message=message):
                self.assert_silent_success("handback_check.py", stop("feature-builder", message))

    def test_bad_input_never_fails(self):
        for payload in (b"{not json", b"", b"[]"):
            with self.subTest(payload=payload):
                self.assert_silent_success("handback_check.py", payload)


class HookSourceTests(unittest.TestCase):
    def test_no_network_modules(self):
        for script in ("subagent_context.py", "compact_context.py", "handback_check.py"):
            text = (HOOKS / script).read_text(encoding="utf-8")
            for module in ("socket", "urllib", "http.client", "requests", "subprocess"):
                self.assertNotIn(f"import {module}", text, script)


if __name__ == "__main__":
    unittest.main(verbosity=1)
