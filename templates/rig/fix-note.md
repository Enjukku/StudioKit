---
type: template
scope: universal
status: active
updated: 2026-10-21
source: J005 step 1; rules/messages.md §2 (brief format), §5 (evidence)
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20

```text
<intent>
<What fails for the next role or the player, and why it matters. Example: the left arm cannot rise to the
attack pose without the shoulder cap showing from the gameplay camera, so the heavy swing reads as broken.>
</intent>
<spec>
id: <job-id>-T<nn>
from: character-rigger            # or animator
to: modeler                       # or character-rigger
asset: <asset-id> rev <n>
round: 1 of 2                     # round 3 does not exist: after round 2 the status is failed → lead
items:
  - item: N1
    part: P03 left upper arm
    check: S4-seam-cover
    measured: cap visible at raise 80 deg, front and 3/4 views   # number + unit, or what is seen
    where: vertex group cut_L_shoulder; frame 24 of test clip T-envelope-upper; evidence content/rigs/<id>/tests/s4_r1_front.png
    why: rig sheet P03 animator.rom raise 0..80 deg (attack_heavy); rigger.cut hide_by socket
    pass_when: no cap, gap or backface visible in the 6 review views at 0, 40 and 80 deg
open: [how to fix each item: re-cut, deeper overlap, re-model, other]
not_in_scope: [parts not listed above; the joint plan (changes to it go back to the rigger as a counter-proposal)]
rules: [Edit a working copy, never the source snapshot. Keep every §B row the part already passes. Hand back with STATUS and coverage per item (rules/messages.md §3).]
deliver: updated part files + rig sheet §D rows for the listed parts
checks:
  - C1: each item's pass_when, re-run by the sender on the returned files
return: hand-back to <sender>
</spec>
```
