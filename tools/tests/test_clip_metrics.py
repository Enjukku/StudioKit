"""Offline tests for tools/vfx/clip_metrics.py (synthetic frames, no captures needed)."""

import sys
import tempfile
import unittest
from pathlib import Path

try:
    import numpy as np
    from PIL import Image
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy and Pillow")

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "vfx"))
import clip_metrics as cm  # noqa: E402


def write_clip(folder: Path, squares: list[int]) -> None:
    """One frame per entry; each draws a white square of that side (px at 256 wide) in the centre."""
    for i, side in enumerate(squares):
        img = np.full((144, 256, 3), 20, dtype=np.uint8)
        if side:
            c = 128
            img[72 - side // 2 : 72 + side // 2, c - side // 2 : c + side // 2] = 255
        Image.fromarray(img).save(folder / f"f{i:03d}_{i * 33:04d}ms.jpg", quality=95)


class ClipMetricsTest(unittest.TestCase):
    def test_coverage_peak_and_onset(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d) / "clip"
            folder.mkdir()
            write_clip(folder, [0, 0, 0, 20, 40, 20, 0, 0, 0, 0])
            r = cm.measure(folder)
            s = r["summary"]
            self.assertEqual(s["peak_ms"], 4 * 33)
            self.assertAlmostEqual(s["peak_coverage_pct"], 100 * 40 * 40 / (256 * 144), delta=0.3)
            self.assertEqual(s["onset_ms"], 3 * 33)
            self.assertEqual(s["visible_ms"], 2 * 33)
            self.assertGreater(s["peak_bright_pct"], 3.5)
            self.assertIsNone(r["frames"][0]["box"])
            self.assertTrue((folder / "metrics.json").exists())

    def test_ui_corner_ignored(self):
        bg = np.zeros((144, 256, 3), dtype=np.int16)
        frame = bg.copy()
        frame[0:5, 0:10] = 255
        self.assertEqual(cm.frame_metrics(frame, bg)["coverage_pct"], 0.0)

    def test_moving_camera_flag(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d) / "shot_follow"
            folder.mkdir()
            write_clip(folder, [0, 10, 0])
            self.assertTrue(cm.measure(folder)["summary"]["moving_camera"])


if __name__ == "__main__":
    unittest.main()


class FrameOrderTest(unittest.TestCase):
    """J018: frames are read in numeric order (a name sort put f1000 before f101)."""

    def test_numeric_order(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            for i in (99, 100, 101, 1000):
                Image.fromarray(np.zeros((8, 8, 3), np.uint8)).save(folder / f"f{i}_{i * 33}ms.jpg")
            times, _ = cm.load_frames(folder)
            self.assertEqual(times, [99 * 33, 100 * 33, 101 * 33, 1000 * 33])
