---
name: owner-budget-renders
description: Owner wants rig checks cheap - numbers for every pose, look at images only for failures plus at most 8 key poses, no weight searches unless a check fails, report render and image counts
metadata:
  type: feedback
---

Run every pose as scripted numbers. Open and look at images only for failing poses, plus at most 8 key poses (gameplay camera and one close view). No new weight-variant searches unless a check fails. Report in the hand-back how many renders were made and how many images were looked at.

**Why:** the owner said (J005-T18, 2026-10-21): "this takes way too much usage, way too much time".

**How to apply:** default to headless flag renders with pixel counts and do not view them. Build one sheet image for the key poses. Skip textured 6-view renders for passing poses. One targeted variant is enough to test a weight hypothesis.

Related: [[craft-blender-bake-export]]
