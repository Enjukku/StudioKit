---
type: lesson
scope: universal
status: draft
updated: 2026-10-20
source: J002 (/build-agent UI/UX designer)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

# Lessons: building the UI/UX designer agent (J002)

| What | Lesson | Evidence |
| --- | --- | --- |
| worked | Extraction per source on Sonnet high, then lead-written books, then one real test, then an independent checker. The test found 27 gaps and the checker found 8 must-fix errors that my own review missed | `content/ui/egg-shop/skill-gaps.md`, `knowledge/jobs/J002-ui-ux-designer/review-T08.md` |
| failed | My size math mapped the 1080 canvas to the full phone height; interactive UI sits below the top bar, so the real fit is ≈ 0.294, not 0.347. The tablet row also ignored width-bound fits | review M1, G2 G-06 |
| failed | Tutorial values copied at PC scale (3 px outline, 22-24 px text) vanish on phones; every style token needs a phone check | G2 G-08 |
| failed | Same look for focus and selected in three books: write state marks once (ui-figma F-15) and make books reference it | review M5 |
| failed | Numbers written next to a tutorial timestamp read as the tutor's values; mark PROPOSAL in the cell when the source states no number | review M3 |
| failed | Tags: a skill row citing a range (RA-44..48) hid an OPINION inside a VERIFIED tag; tag per id | review M4 |
| owner correction | "these Sonnet models be on high"; "the Figma can access use my Figma"; add ChatGPT reference images; load the figma-use skills; "the VFX agent has access to this large pool of assets ... it would be incredibly useful for your workflow" | decisions.md J002-D2..D7 |
| tool | `tools/vfx/vfxlib_catalog.py fetch` fails on a fresh checkout until `output/vfx/library/` exists | this job |
| harness | A role's `skills:` list preloads every listed skill; list only the always-needed ones and Read the per-game style book | review S12 |

## Owner review of both tests (2026-10-21)
- Owner words: "the quality is just like alright ... it's usable, but it's not it's like a B. It's like a B minus. With some buttons being pretty good, like an A." / "I think with the reference photos, this can be improved."
- Lesson: both tests built the look from words (style book tokens) with no whole-screen target image; the anime test generated character art only. A ChatGPT target reference of the screen is now step 4 of the role, required before styling, and self-review compares the build side by side with it (J002-D12).
- Owner correction: every new UI/UX agent must know it has ChatGPT image generation and the VFX texture library. Now stated at the top of the role file, in the ui-figma description and in each style book §1.
