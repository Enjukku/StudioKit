"""Tests for soundbench intake (MP3 -> master), export (FLAC), pictures, doctor and the command line (J020 step 1-2).

Real takes are 44.1 kHz stereo MP3 (design section 9): the intake tests encode fixtures with ffmpeg's libmp3lame and
skip with a reason when it is missing. The key-entry check must never open the key file (AGENTS.md section 3.4).
"""

import builtins
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

try:
    import matplotlib  # noqa: F401
    import numpy as np
    import scipy  # noqa: F401
    import soundfile as sf
except ImportError:  # optional deps: the kit gate is standard library only
    raise unittest.SkipTest("needs numpy, scipy, soundfile and matplotlib")

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.audio.soundbench import doctor, export, intake, pictures  # noqa: E402
from tools.audio.soundbench import ffmpeg as sbf  # noqa: E402
from tools.audio.soundbench import fixtures as fx  # noqa: E402
from tools.audio.soundbench import measures as m  # noqa: E402
from tools.audio.soundbench.core import SoundbenchError, audio_sha256, file_sha256  # noqa: E402

try:
    FOUND = sbf.find_ffmpeg()
except SoundbenchError:
    FOUND = None
HAS_LAME = bool(FOUND) and "libmp3lame" in sbf.encoders(FOUND.path)
needs_lame = unittest.skipUnless(HAS_LAME, "ffmpeg with libmp3lame not found: MP3 intake tests skipped")
CONFIGS = [(r, c) for r in fx.RATES for c in fx.CHANNELS]


def encode_mp3(wav: Path, mp3: Path, tagged: bool = True) -> Path:
    args = [str(FOUND.path), "-hide_banner", "-nostdin", "-y", "-loglevel", "error", "-i", str(wav),
            "-c:a", "libmp3lame", "-b:a", "192k"] + ([] if tagged else ["-write_xing", "0"]) + [str(mp3)]
    subprocess.run(args, check=True, capture_output=True)
    return mp3


class TempDir(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.d = Path(self._t.name)

    def tearDown(self):
        self._t.cleanup()


@needs_lame
class IntakeTest(TempDir):
    def take(self, name, rate, ch, tagged=True):
        x = fx.make(name, rate, ch).astype(np.float32)
        wav = fx.write_wav(self.d / f"{name}{rate}{ch}.wav", x, rate)
        return x, encode_mp3(wav, self.d / f"{name}.r1.t{rate}{ch}.mp3", tagged)

    def test_decode_keeps_rate_channels_length_and_timing(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x, mp3 = self.take("clean_hit", rate, ch)
                info = intake.decode_take(mp3, expected_ms=1000 * len(x) / rate)
                master = intake.master_path(mp3)
                y, r = sf.read(str(master), always_2d=True, dtype="float32")
                self.assertEqual(sf.info(str(master)).subtype, "FLOAT")
                self.assertEqual((r, y.shape), (rate, x.shape))
                self.assertEqual((info["rate"], info["channels"], info["samples"]), (rate, ch, len(x)))
                self.assertEqual(m.lag(x, y, rate, int(0.1 * rate))["lag_samples"], 0)
                self.assertAlmostEqual(m.main_transient_ms(y.astype(np.float64), rate), fx.CLEAN_HIT_ONSET_MS, delta=1)
                self.assertEqual(info["decoder"], "ffmpeg mp3float")
                self.assertEqual(info["master_audio_sha256"], audio_sha256(y))
                self.assertEqual(info["take_sha256"], file_sha256(mp3))

    def test_untagged_mp3_decodes_late_and_is_refused(self):
        """review-1 #13: without the encoder-delay tag the take decodes about 25 ms late and 27 ms long."""
        x, mp3 = self.take("clean_hit", 44100, 2, tagged=False)
        with self.assertRaisesRegex(SoundbenchError, "encoder-delay"):
            intake.decode_take(mp3, expected_ms=1000 * len(x) / 44100)
        self.assertFalse(intake.master_path(mp3).exists())  # no half-made master left behind

    def test_master_is_never_overwritten_and_sidecar_keeps_its_fields(self):
        x, mp3 = self.take("wrong_chime", 44100, 2)
        side = mp3.with_suffix(".json")
        side.write_text(json.dumps({"prompt": "a chime", "credits": 12}), encoding="utf-8")
        intake.decode_take(mp3, expected_ms=1000 * len(x) / 44100)
        doc = json.loads(side.read_text(encoding="utf-8"))
        self.assertEqual((doc["prompt"], doc["credits"]), ("a chime", 12))
        self.assertIn("intake", doc)
        before = file_sha256(intake.master_path(mp3))
        with self.assertRaisesRegex(SoundbenchError, "never overwritten"):
            intake.decode_take(mp3, expected_ms=1000 * len(x) / 44100)
        self.assertEqual(file_sha256(intake.master_path(mp3)), before)

    def test_the_mp3_round_trip_master_goes_through_afftdn_in_time(self):
        x, mp3 = self.take("clean_hit", 44100, 2)
        intake.decode_take(mp3, expected_ms=1000 * len(x) / 44100)
        y, rate = sf.read(str(intake.master_path(mp3)), always_2d=True, dtype="float32")
        y = y + (0.003 * np.random.RandomState(1).standard_normal(y.shape)).astype(np.float32)
        res = sbf.run_filter(y, rate, "afftdn", max_lag_ms=50)
        self.assertEqual(m.lag(y, res.audio, rate, 4410)["lag_samples"], 0)
        self.assertEqual(res.audio.shape, y.shape)


class ExportTest(TempDir):
    def test_flac_at_the_input_rate_with_a_matching_log(self):
        for rate, ch in CONFIGS:
            with self.subTest(rate=rate, ch=ch):
                x = (0.9 * fx.make("wrong_chime", rate, ch)).astype(np.float32)
                out = self.d / f"c{rate}{ch}.flac"
                rec = export.export_flac(x, rate, out, source_rate=rate)
                info = sf.info(str(out))
                self.assertEqual((info.format, info.subtype, info.samplerate, info.channels, info.frames),
                                 ("FLAC", "PCM_24", rate, ch, len(x)))
                back, _ = sf.read(str(out), always_2d=True, dtype="float64")
                self.assertLessEqual(float(np.max(np.abs(back - x))), 2.0 ** -23)
                self.assertEqual(rec["audio_sha256_float32"], audio_sha256(x))
                self.assertEqual(rec["file_sha256"], file_sha256(out))
                log = json.loads(out.with_name(f"c{rate}{ch}.log.json").read_text(encoding="utf-8"))
                self.assertEqual(log["encode"]["rate"], rate)
                self.assertIn("libsndfile", log["tools"])
                self.assertEqual(m.lag(x, back, rate, 4000)["lag_samples"], 0)

    def test_refusals_leave_no_file(self):
        x = fx.make("clean_hit", 44100, 2).astype(np.float32)
        loud = x.copy()
        loud[100, 0] = 1.0
        nan = x.copy()
        nan[5, 1] = np.nan
        cases = (((x, 44100), {"source_rate": 48000}, "never resampled"), ((x, 96000), {}, "48000"),
                 ((loud, 44100), {}, "full scale"), ((nan, 44100), {}, "NaN"),
                 ((np.zeros((100, 3), np.float32), 44100), {}, "channels"))
        for i, (args, kw, why) in enumerate(cases):
            with self.subTest(why=why):
                out = self.d / f"bad{i}.flac"
                with self.assertRaisesRegex(SoundbenchError, why):
                    export.export_flac(*args, out, **kw)
                self.assertFalse(out.exists())

    def test_two_processes_give_the_same_audio_hash_and_file(self):
        code = ("import sys; sys.path.insert(0, sys.argv[1]); from pathlib import Path; "
                "from tools.audio.soundbench import export, fixtures as fx; "
                "x = (0.5 * fx.make('hummed', 44100, 2)); "
                "r = export.export_flac(x, 44100, Path(sys.argv[2])); print(r['audio_sha256_float32'], r['file_sha256'])")
        outs = [subprocess.run([sys.executable, "-c", code, str(ROOT), str(self.d / f"p{i}.flac")], capture_output=True,
                               text=True, check=True).stdout.split() for i in range(2)]
        self.assertEqual(outs[0], outs[1])
        self.assertEqual(len(outs[0]), 2)


class PictureTest(TempDir):
    def test_png_written_and_audio_untouched(self):
        for rate, ch in ((44100, 2), (48000, 1)):
            with self.subTest(rate=rate, ch=ch):
                x = fx.make("wrong_chime", rate, ch).astype(np.float32)
                before = x.copy()
                out = pictures.picture(x, rate, self.d / f"p{rate}.png", title="chime")
                self.assertEqual(out.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
                self.assertGreater(out.stat().st_size, 10_000)
                np.testing.assert_array_equal(x, before)


class DoctorKeyTest(TempDir):
    def write_keys(self, entries):
        p = self.d / "knowledge" / "design"
        p.mkdir(parents=True, exist_ok=True)
        (p / "keys.json").write_text(json.dumps({"keys": entries}), encoding="utf-8")

    def test_key_entry_states(self):
        key = self.d / "key.txt"
        key.write_text("not-a-real-key", encoding="utf-8")
        self.assertEqual(doctor._key_entry(self.d)[0], "FAIL")  # no keys.json
        self.write_keys([{"env": "OTHER", "path": str(key)}])
        self.assertIn("no ELEVENLABS_API_KEY entry", doctor._key_entry(self.d)[1])
        self.write_keys([{"env": "ELEVENLABS_API_KEY", "path": ""}])
        self.assertIn("no path", doctor._key_entry(self.d)[1])
        self.write_keys([{"env": "ELEVENLABS_API_KEY", "path": str(self.d / "missing.txt")}])
        self.assertIn("no file", doctor._key_entry(self.d)[1])
        self.write_keys([{"env": "ELEVENLABS_API_KEY", "path": str(key)}])
        real_open, real_io_open = builtins.open, io.open

        def guarded(target, *a, **k):
            if Path(str(target)).resolve() == key.resolve():
                raise AssertionError("doctor opened the key file")
            return real_open(target, *a, **k)

        with mock.patch("builtins.open", guarded), mock.patch("io.open", guarded):
            status, detail = doctor._key_entry(self.d)
        self.assertEqual(status, "PASS")
        self.assertNotIn("not-a-real-key", detail)
        self.assertIs(io.open, real_io_open)

    def test_doctor_rows_name_every_check(self):
        rows = doctor.checks(self.d)
        names = {r["check"] for r in rows}
        for want in ("python", "lib numpy", "lib pyloudnorm", "ffmpeg found", "keys.json ELEVENLABS_API_KEY"):
            self.assertIn(want, names)
        if FOUND:
            self.assertIn("G-7 self-test", names)
        self.assertEqual(next(r for r in rows if r["check"].startswith("keys.json"))["status"], "FAIL")


class CommandLineTest(TempDir):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, "-m", "tools.audio.soundbench", *map(str, args)], cwd=str(ROOT),
                              capture_output=True, text=True, env={**os.environ, "PYTHONIOENCODING": "utf-8"})

    def test_measure_json_and_picture(self):
        p = fx.write_wav(self.d / "hit.wav", fx.make("clean_hit", 44100, 2), 44100)
        png = self.d / "hit.png"
        r = self.run_cli("measure", p, "--json", "--picture", png)
        self.assertEqual(r.returncode, 0, r.stderr)
        rec = json.loads(r.stdout)
        self.assertAlmostEqual(rec["F-01_onset_ms"], fx.CLEAN_HIT_ONSET_MS, delta=0.5)
        self.assertIn("main_transient_ms", rec)
        self.assertTrue(png.is_file())

    def test_compare_reads_the_lag_between_two_files(self):
        x = fx.make("clean_hit", 48000, 1)
        a = fx.write_wav(self.d / "a.wav", x, 48000)
        b = fx.write_wav(self.d / "b.wav", np.vstack([np.zeros((1200, 1)), x[:-1200]]), 48000)
        r = self.run_cli("compare", a, b, "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        rec = json.loads(r.stdout)
        self.assertEqual(rec["lag_b_vs_a"]["lag_samples"], 1200)
        row = next(x for x in rec["rows"] if x["measure"] == "F-01_onset_ms")
        self.assertAlmostEqual(row["b_minus_a"], 25.0, delta=0.1)
        self.assertEqual(self.run_cli("compare", a, b).returncode, 0)

    def test_parity_matches_the_module(self):
        a = fx.write_wav(self.d / "a.wav", fx.make("clean_hit", 44100, 2), 44100)
        b = fx.write_wav(self.d / "b.wav", fx.make("wrong_chime", 44100, 2), 44100)
        r = self.run_cli("parity", a, b, "--mode", "momentary", "--json")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout)["spread_lu"], m.parity([a, b], "momentary")["spread_lu"])

    def test_errors_exit_2(self):
        r = self.run_cli("measure", self.d / "missing.wav")
        self.assertEqual(r.returncode, 2)
        self.assertIn("ERROR", r.stderr)


if __name__ == "__main__":
    unittest.main()
