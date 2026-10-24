---
name: permission-thresholds
description: In permission and exemption code, check what value a non-member or a reset gets: a threshold that 0 passes admits everyone; a flag set by a value-setting action must clear when the value returns to default
metadata:
  type: feedback
---

For any "rank >= min" or "flag while changed" rule in admin or anti-cheat code, ask two questions: what does the API return for someone outside the group (GetRolesInGroupAsync: IsMember false, no Roles, so rank 0), and what clears a flag that a slider or setter raised when the admin sets it back to the default.

**Why:** J025 Admin r1 (2026-10-24): start accepted minRank 0 (every player admin in a live server), and core.walkSpeed/jump left a target exempt from movement checks after the speed went back to 16, until respawn. Neither had a spec; 14 planted faults and QA's acceptance rows covered the guards but not these values.

**How to apply:** bracket each threshold at 0 and at the non-member value, and trace set-then-reset for every exemption flag. See [[same-server-rejoin]] for the same "trace the case nobody listed" habit.
