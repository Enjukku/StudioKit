---
name: vendor-facts-measure-first
description: Before building on a paid API, spend a few cheap real calls to read its real limits, formats, error shapes and billing; docs were wrong on 2 of 3 facts
metadata:
  type: feedback
---

Before writing an API client, run a tiny probe script (scratchpad, stdlib, key from env, redacted output) that reads
the real answers: status and body shape for each error, the billing header, the formats the plan really gets. Cross-
check the billing header total against the account counter after a few minutes (J020 step 7: header sum 330 =
counter delta 330; the counter lagged at first).

**Why:** J020 step 7 (2026-10-24): ElevenLabs' own docs said WAV needs Pro (the Creator key got WAV 44.1 and 48 kHz),
another page said 0.1 s minimum (0.5 is enforced, 400) and 40 credits/s (it is ceil(11 x d), 55 flat without a
duration). An invalid key came back as 400, not 401, so an auth check on status alone would have misfired. A user-level
Windows variable held a key ID that silently won over keys.json.

**How to apply:** probe first, then design the detection (refusals, auth, billing) on the real bodies; keep fakes in
tests shaped like the recorded answers. When a key fails, check where the environment got it (length and prefix only,
never the value) before blaming the key file. Related: [[fixtures-like-real-inputs]].
