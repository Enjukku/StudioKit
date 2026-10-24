---
name: contract-reviews
description: Reviewing architect contracts before code (J025 framework): where real defects hid; check library source and API security tags, not just the contract text
metadata:
  type: feedback
---

Contract (pre-code) reviews find most real defects by reading the wrapped library's source against each failure row, not by reading the contract alone (J025-S3-R1, 2026-10-24: 10 blocking, all proven from source or API reference).

**Why:** the contract named library behaviour that the library only gives under other options (ProfileStore's 120 s load timeout is skipped when `Cancel` is passed, init.luau:1610-1614); own calls fired the same signal as external events (EndSession fires OnSessionEnd, so "OnSessionEnd -> kick" also hit Session's own degraded path); a cited property existed but its read was RobloxScriptSecurity (Workspace.AuthorityMode).

**How to apply:**
- For each failure row, open the library function it relies on and check the option the contract passes.
- For each "X happens on signal S", list who else fires S (including our own calls).
- For each engine property, read the `security: read:` field in `_api-reference`, not only that the name exists.
- Look for two rows that define one case twice (failure table vs test table); broken markdown table rows can swallow a test row.
- Tests asserting "record byte-identical" fail on library metadata writes; assert the data subtree.
- Generated transport code: check what happens to events with no listener (Blink queues without cap).
- Related: [[workflow-script-reviews]].
