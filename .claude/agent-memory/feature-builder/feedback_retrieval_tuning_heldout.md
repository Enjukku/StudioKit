---
name: retrieval-tuning-heldout
description: For ranking/retrieval work scored on hidden cases - write extra practice cases before tuning, sweep for a plateau, and prefer signals the kit already owns (citations) over synonym lists
metadata:
  type: feedback
---

When a ranking change is scored on held-out cases (J010-T26 Roblox docs routing), write your own practice cases from the role map BEFORE tuning, then sweep every constant on a grid and pick the middle of a flat plateau, not the peak.

**Why:** the 10 given practice cases were 9/10 after tuning but my 14 pre-written cases were 8/14 - the gap is the honest estimate of held-out quality. Plain BM25 alone could not bridge player words ("streak behind the sword") to doc titles; fusing in "pages cited by the top-ranked kit notes" was the biggest general gain (+3 of 24) without a hand-made synonym list.

**How to apply:** for any retrieval/routing brief - (1) add builder cases marked "builder-added before tuning", (2) report given-set and own-set scores separately, (3) prefer data the repo already maintains (cross-references, link graphs, folder structure) as ranking signals, (4) keep the gate's other users unchanged with a byte-equality test (see [[planted-faults-unequal]]).
