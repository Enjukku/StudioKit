---
type: reference
scope: universal
status: active
updated: 2026-10-20
source: "moved from DestructionSimulator 2026-10-20"
supersedes: []
held_out: true   # repeats held-out cases, keys, rubrics or answers (rules/knowledge.md §3)
---
> Author: kit-mover · claude-sonnet-5-5 · medium · 2026-10-20 (moved from DestructionSimulator; original author line kept below)

> Author: orchestrator · claude-opus-5-5 · default · 2026-10-20

# VFX benchmark: study set, hidden test set, frame scripts, similarity score

**Why :** the vfx-designer must get a good effect on the first try, from a plan, with no Studio tuning loop. We train it on the 38 pro effects we hold as data + clip pairs, and prove it on effects it never studied.

## Sets
| Set | Effects (`output/vfx/training-dumps/json/<name>.json`, clips in `output/vfx/training-captures/`) |
| --- | --- |
| **Hidden test (8)** | `sTier__Missile_Sequence`, `sTier__Purple_arcane_showcase`, `aTier__Slashes`, `aTier__Constellations`, `bTier__explosion`, `bTier__Healing_VFX`, `cTier__fiya_beam`, `Unknown__Portal_VFX` |
| **Study (30)** | every other file in `training-dumps/json/`. The fireball references (Elemental Guns, Flame Beziers, StylizedFireballsTrails) stay here |

Hidden-set rules: no agent opens a hidden effect's JSON, outline, attributes or scripts while building skills, recipes or building blocks. Its frame script (written from the clip only) is allowed, because the test gives the model that text. **Leak risk:** the 2026-10-16 teardowns (`sTier-/aTier-/bTier-/cTier-unknown-teardown.md`) were written from all files. Recipe IDs taken from hidden effects must not move into the skill; check the source file of every ST/AT/BT/CT ID before using it.

## Frame scripts (`frame-scripts/<clip>.md`)
A frame script is the written picture of an effect: what the screen shows at key moments, with numbers. It replaces 2D mock-ups . Pro clips get one from frames only (never from data), so the plan format and the test input are the same thing. Format:

```
# <clip> · <tier> · camera <side|front|follow>, about <n> studs
Event: <one sentence: what happens, in game words>
Phases: windup a-b ms · launch · travel · impact/peak · follow-through · tail (only the ones present)
| ms | Coverage % (metrics) | Where (box) | Shapes on screen | Colours (approx hex) | Brightness | Motion |
<6-10 rows: onset, build, peak, just after peak, follow-through, tail, end>
Layers seen: <job: count, e.g. hot core 1, cross flare 1, flame blobs many, sparks ~20, rings 2, dark smoke 3>
Size vs character: <head/burst size in character heights>
What makes it look good: <3 bullets, concrete>
Weak points: <0-3 bullets>
```

## Measures (`tools/vfx/clip_metrics.py` → `<clip>/metrics.json`)
Per frame vs a median background: `coverage_pct`, `bright_pct` (luma ≥230), `box`, `centre`, `mean_rgb`, `peak_luma`. Summary: onset, peak time and coverage, visible duration. Limits: looping clips (auras) put part of the effect into the background; `_follow` clips move the camera (flagged); our own captures count moving bricks as "effect", so benchmark captures run in the dark test place with no bricks.

## Similarity score (to build, step 4)
Hidden effect → model gets its frame script + event + camera → plans and builds → captured with the same camera → score vs the pro clip: coverage curve over time, bright curve, mean colour per phase, onset/peak/visible ms, box size at peak, plus the owner's look rating. Score only goes up if the skill really improved; the final test is the hidden 8.
