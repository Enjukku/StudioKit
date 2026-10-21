import os
import sys
import tempfile
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "art"))
import art_refs  # noqa: E402

BIBLE = """# Art bible

| family | lock | world lock | anchors |
| --- | --- | --- | --- |
| character | CHARACTER LOCK | yes | |
| model | MODEL REF LOCK | yes | character |
| icon | ICON LOCK | no | |

```text
WORLD STYLE LOCK: stylized hand-painted world.
```

```text
CHARACTER LOCK: full body, front three-quarter view.
```

```text
MODEL REF LOCK: one character, T-pose, three-quarter view.
```

```text
ICON LOCK: one object, plain background, no text.
```
"""


class ArtBible(unittest.TestCase):
    def test_families_parsed(self):
        fams = art_refs.families(BIBLE)
        self.assertEqual(set(fams), {"character", "model", "icon"})
        self.assertTrue(fams["character"].world)
        self.assertFalse(fams["icon"].world)
        self.assertEqual(fams["model"].anchors, "character")
        self.assertEqual(fams["icon"].anchors, "icon")

    def test_bad_world_value_rejected(self):
        with self.assertRaises(ValueError):
            art_refs.families(BIBLE.replace("| no |", "| maybe |"))

    def test_locks_parsed(self):
        lks = art_refs.locks(BIBLE)
        self.assertIn("WORLD STYLE LOCK", lks)
        self.assertTrue(lks["ICON LOCK"].startswith("ICON LOCK:"))

    def test_missing_lock_block_stops(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "art-bible.md"
            p.write_text(BIBLE.replace("ICON LOCK: one object", "OTHER LOCK: one object"), encoding="utf-8")
            with self.assertRaises(SystemExit):
                art_refs.load_bible(p)


class Prompts(unittest.TestCase):
    def setUp(self):
        self.fams, self.lks = art_refs.families(BIBLE), art_refs.locks(BIBLE)
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def test_world_lock_only_where_set(self):
        p, _ = art_refs.build({"id": "hero", "family": "character", "identity": "a fox knight"}, self.fams, self.lks, self.root)
        self.assertIn("WORLD STYLE LOCK", p)
        self.assertIn("a fox knight", p)
        p, _ = art_refs.build({"id": "coin", "family": "icon", "identity": "a gold coin"}, self.fams, self.lks, self.root)
        self.assertNotIn("WORLD STYLE LOCK", p)
        self.assertIn("ICON LOCK", p)

    def test_anchors_owner_first_then_newest_generated(self):
        folder = self.root / "character"
        folder.mkdir()
        for name in ("a.png", "b.png", "c.png", "gen-old.png", "gen-new.png"):
            (folder / name).write_bytes(b"x")
        old = time.time() - 100
        os.utime(folder / "gen-old.png", (old, old))
        picks = art_refs.anchors_for(self.fams["model"], "hero", "", self.root)
        self.assertEqual(len(picks), 3)
        self.assertTrue(all(not p.name.startswith("gen-") for p in picks[:2]))
        self.assertEqual(picks[2].name, "gen-new.png")
        _, images = art_refs.build({"id": "hero", "family": "model", "identity": "x"}, self.fams, self.lks, self.root)
        self.assertEqual(len(images), 3)

    def test_manifest_validation(self):
        bad = self.root / "m.csv"
        bad.write_text("id,family,identity\nHero,character,x\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            art_refs.read_manifest(bad, self.fams)
        bad.write_text("id,family,identity\nhero,dragon,x\n", encoding="utf-8")
        with self.assertRaises(SystemExit):
            art_refs.read_manifest(bad, self.fams)
        good = self.root / "g.csv"
        good.write_text("id,family,identity\nhero,character,a fox knight\n", encoding="utf-8")
        self.assertEqual(len(art_refs.read_manifest(good, self.fams)), 1)


if __name__ == "__main__":
    unittest.main()
