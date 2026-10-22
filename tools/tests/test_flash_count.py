"""Tests for tools/vfx/flash_count.py: the J018 review cases as synthetic frame folders (G3-P1)."""

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
import flash_count as fc  # noqa: E402

W, H = 96, 54


def write(folder: Path, levels, fps=30, name="png"):
    """levels: per frame either a grey level (whole frame) or an array (H, W) of grey levels."""
    for i, v in enumerate(levels, 1):
        arr = np.full((H, W), v, np.uint8) if np.isscalar(v) else v.astype(np.uint8)
        img = Image.fromarray(np.stack([arr] * 3, -1))
        if name == "png":
            img.save(folder / f"{i:04d}.png")
        else:
            img.save(folder / f"f{i:03d}_{round((i - 1) * 1000 / fps)}ms.jpg", quality=95)


class FlashCountTest(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()

    def large(self, fps=30):
        return fc.run(self.d, fps)["counts"]["10%"]["most_in_any_1s"]

    def test_three_hard_flashes_in_one_second(self):
        lv = [30] * 30
        for k in (3, 13, 23):
            lv[k] = 230
        write(self.d, lv)
        self.assertEqual(self.large(), 3)

    def test_eased_pulse_counts_once_at_30_and_60_fps(self):
        for fps in (30, 60):
            with self.subTest(fps=fps):
                for p in self.d.iterdir():
                    p.unlink()
                n = fps  # one second: rise over 0.2 s, hold, fall
                ramp = [int(30 + 200 * min(1, i / (0.2 * fps))) for i in range(int(0.5 * fps))]
                write(self.d, [30] * (n // 4) + ramp + ramp[::-1] + [30] * (n // 4), fps)
                self.assertEqual(self.large(fps), 1)

    def test_lasting_dim_then_small_flashes(self):
        # a bright stage dims and stays dim, then three 8 % flashes in 1 s: none at 10 %, all three at 3 %
        frames = [np.full((H, W), 200)] * 5 + [np.full((H, W), 60)] * 5
        for k in range(30):
            f = np.full((H, W), 60)
            if k in (2, 12, 22):
                f[:, : int(W * 0.08) + 1] = 255
            frames.append(f)
        write(self.d, frames)
        c = fc.run(self.d, 30)["counts"]
        self.assertEqual(c["10%"]["most_in_any_1s"], 0)
        self.assertEqual(c["3%"]["most_in_any_1s"], 3)

    def test_figure_walking_is_no_flash(self):
        frames = []
        for k in range(30):
            f = np.full((H, W), 40)
            x = 5 + k * 2
            f[20:40, x:x + 3] = 240  # a bright 3 % figure walking across
            frames.append(f)
        write(self.d, frames)
        c = fc.run(self.d, 30)["counts"]
        self.assertEqual((c["10%"]["most_in_any_1s"], c["3%"]["most_in_any_1s"]), (0, 0))

    def test_times_from_capture_names_and_box_rate(self):
        lv = [40 if (i // 4) % 2 == 0 else 200 for i in range(60)]  # a 3.75 Hz square pulse at 30 fps
        write(self.d, lv, name="jpg")
        rec = fc.run(self.d, 30, [0.2, 0.2, 0.8, 0.8])
        self.assertEqual(rec["times_from"], "the names (ms)")
        self.assertAlmostEqual(rec["box"]["hz"], 3.75, delta=0.1)

    def test_input_stops(self):
        write(self.d, [30, 40])
        (self.d / "0001.luminance.png").write_bytes((self.d / "0001.png").read_bytes())
        with self.assertRaises(fc.FlashError):
            fc.run(self.d, 30)
        (self.d / "0001.luminance.png").unlink()
        with self.assertRaises(fc.FlashError):
            fc.run(self.d, 30, [0.5, 0.2, 0.1, 0.8])

    def test_cli(self):
        import contextlib
        import io
        write(self.d, [30] * 10)
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(fc.main([str(self.d), "30", "--json"]), 0)
            self.assertEqual(fc.main([str(self.d / "missing"), "30"]), 2)


if __name__ == "__main__":
    unittest.main()
