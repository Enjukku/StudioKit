#!/usr/bin/env python3
"""tools/keys.py: keys load from files into the child environment only, an owner-set variable wins, bad files
stop before the command starts, and no key value reaches stdout or stderr."""
import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import keys  # noqa: E402

PLANTED = "TEST-PLANTED-k3y-do-not-leak"


class KeysTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = Path(self.tmp.name)
        self.addCleanup(self.tmp.cleanup)

    def keyfile(self, text, name="k.txt"):
        p = self.dir / name
        p.write_text(text, encoding="utf-8")
        return str(p)

    def entries(self, path):
        return [{"env": "A_KEY", "service": "a", "path": path}, {"env": "B_KEY", "service": "b", "path": ""}]

    def test_loads_key_trimmed(self):
        env = keys.key_env(self.entries(self.keyfile(f"\n  {PLANTED}  \n")), None, {})
        self.assertEqual(env["A_KEY"], PLANTED)
        self.assertNotIn("B_KEY", env)  # no path yet: skipped when not asked for

    def test_owner_env_wins(self):
        env = keys.key_env(self.entries(self.keyfile(PLANTED)), None, {"A_KEY": "from-setx"})
        self.assertEqual(env["A_KEY"], "from-setx")

    def test_refusals_name_path_not_value(self):
        cases = [
            (self.entries(self.keyfile(f"{PLANTED}\nsecond", "two-lines.txt")), None),
            (self.entries(str(self.dir / "missing.txt")), None),
            (self.entries(self.keyfile(PLANTED)), ["B_KEY"]),
            (self.entries(self.keyfile(PLANTED)), ["NOPE"]),
        ]
        for entries, only in cases:
            with self.assertRaises(keys.KeyError_) as cm:
                keys.key_env(entries, only, {})
            self.assertNotIn(PLANTED, str(cm.exception))

    def test_run_passes_key_to_child_and_prints_nothing(self):
        entries = [{"env": "A_KEY", "service": "a", "path": self.keyfile(PLANTED)}]
        child = [sys.executable, "-c", f"import os,sys; sys.exit(0 if os.environ['A_KEY'] == {PLANTED!r} else 7)"]
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(keys, "load_registry", lambda: entries), mock.patch.dict(os.environ), \
                redirect_stdout(out), redirect_stderr(err):
            os.environ.pop("A_KEY", None)
            code = keys.main(["run", "--", *child])
            keys.main(["list"])
        self.assertEqual(code, 0)
        self.assertNotIn("A_KEY", os.environ)
        self.assertNotIn(PLANTED, out.getvalue() + err.getvalue())

    def test_repo_registry_has_no_values(self):
        for e in keys.load_registry():
            self.assertEqual(set(e) - {"env", "service", "path", "used_by", "note"}, set(), e["env"])
            self.assertTrue(e["env"].isupper())


if __name__ == "__main__":
    unittest.main()
