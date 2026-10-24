"""soundbench: the kit's audio editor, made for an agent that cannot hear (J020, `editor-design.md`).

Kit tool (universal). Author: feature-builder · claude-opus-5-5 · high · 2026-10-23 (J020 steps 1-4)

Built so far (design section 10 steps 1-4): the ffmpeg adapter with its time checks (`ffmpeg`), every measure
(`measures`, with F-01..F-13 moved from cue_check.py), pictures, the MP3 intake decode (`intake`), FLAC export
(`export`), `doctor`; the card and recipe (`card`), the numpy operations (`ops`), the ffmpeg operations (`fxops`,
with `standins`), the two-pass `render`, `rank`, layers, loops and variants (`assemble`), and `generate`
(ElevenLabs takes, step 7). Commands:
README.md.

Usage:
  python -m tools.audio.soundbench doctor | measure | compare | parity | render  (--help on each)
"""

from .core import VERSION, SoundbenchError  # noqa: F401
