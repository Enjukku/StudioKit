---
name: direction-test-craft
description: How to run a cheap 2-direction image test with art_refs.py and measure "X reads first" in generated scenes (J009-T13 lessons)
metadata:
  type: feedback
---

Lessons from the first direction test (Guard the Dragon Egg, 2026-10-21, 4 images + 3 retries):

- Generate the character first, review it, then attach it as `inputs` to the scene row; `art_refs.py print` fails on a row whose input does not exist yet, so print/run in two passes.
- gpt-image ignores soft proportion words ("head about one third"); state it as heads-tall plus a body-part length ("about three heads tall, legs one head long").
- Thieves/threats drawn generically become dragons/wyverns even with "No dragon"; describe what they ARE and list "no long neck, no tail". Also keep threat outlines apart from the heroes' (hooded raiders echoed hooded keepers).
- "Exactly 6 torches" came back as 5 three times out of four; give positions ("2 in front, 1 each side, 2 behind") — that fixed it once.
- A faceted world pulls the "only smooth" hero object into facets too; repeat "no facets, plates or plane lines at all" in the lock.
- Measuring "reads first" without hand boxes: seed = largest connected region of luminance >= p98, grow into connected >= p90, fill holes; check the overlay. p98 alone catches only cracks/highlights. Add "non-subject pixels >= subject median, as share of subject area" to find competitors (snow).
- Phone check for a 3D camera: fit by height (Roblox FieldOfView is vertical), not a centre crop.

**Why:** owner grades by look at a pro bar and worries about image usage; prior blind grades were two steps too kind.
**How to apply:** grade generated concept art C+ when it is cohesive but a familiar AI look; reserve B for images with their own grammar and correct counts. Put STATUS + coverage inside deliverable files, not only in the hand-back.
