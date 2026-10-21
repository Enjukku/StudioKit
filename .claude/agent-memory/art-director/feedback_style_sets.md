---
name: style-set-craft
description: How to prompt one scene in N art styles with art_refs.py so it stays consistent but not stiff (J009-T14 lessons, 2026-10-21)
metadata:
  type: feedback
---

Lessons from style test 2 (T-rex vs meteor, 4 families, 4 images + 3 retries):

- Recipe that worked: one identical short identity (~80 words: subject, action, one key relationship, 1-3 must-haves) + one identical concept lock in every temporary bible; only the WORLD STYLE LOCK varies; `anchors=none`. 4 clearly different renderings, same scene.
- Leaving layout open does NOT give variety: 4 separate sessions picked the same default staging (hero left facing right, meteor top right, flyers top left, waterfall right, low camera). Consistency comes free; tell the owner it can read as "one template, four filters".
- A colour/light line in the shared identity ("washes the scene in warm orange") overrides every lock's palette. Put the light colour in each world lock; keep only the hierarchy ("X is the brightest light") in the identity.
- Mixed-media drift is the main lock failure: clay creature + photoreal fire/sky; low-poly hero + painted background. Fix: name the drifting parts inside the lock ("everything, including the distant jungle, clouds, spray..."), one retry each worked. "Droplets on wire" made the wires visible.
- Run the rows in parallel (separate `run` calls in the background); session folders keep them apart. About 1-2 min each.
- look_check thumb cannot mask a subject in a full scene (invalid_reason); measure "brightest light" with top-0.5% luminance centroid instead.

**Why:** owner wants sets that are consistent but not stiff or AI-looking; grades are at a pro bar.
**How to apply:** for any multi-style or multi-direction set; grade cohesive-but-default-staged sets C+ to B-, not B. See [[direction-test-craft]].
