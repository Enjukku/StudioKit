---
name: planted-faults-session-fakes
description: How to make planted-fault proofs cheap and honest for save/session blocks on FakeWorld-style fakes (J025-Q1, 2026-10-24)
metadata:
  type: feedback
---

Make every acceptance spec function take an optional `patch` argument and raise labelled errors ("<label>: expected X, got Y"); the planted-fault spec then reruns the exact acceptance spec with the fault and asserts the error contains the label, and that every plant's text still matched (a stale plant fails loudly).

**Why:** J025-Q1 Session: one matrix run (every plant × every spec) found 3 survivors that were equivalent mutants (IsActive, IsClosing guards, OnSessionEnd close) because ProfileStore 1.0.3 fires OnSessionEnd synchronously; only direct-state specs could hold those guards. Labels proved each red was for the planted cause, not a crash elsewhere.

**How to apply:** run the full matrix once in a throwaway script before choosing targets; report survivors as equivalent (with the vendor lines) or add a direct-state spec for the contract rule; never pass a plant whose target fails with an unrelated error. Assert `#world.errors == 0` so faults that crash server threads still turn the spec red. Related: [[light-checks-by-default]].

Addendum J025-Q2 Net (2026-10-24): a plant that edits two modules (e.g. generated acceptance + framework module) must count a miss only for files the spec actually loaded, or every single-module target reports a false "stale". Keep spec volumes (spam counts) under limits a pending fix will add (per-player event allowance), or a correct fix turns old specs red (false alarm).
