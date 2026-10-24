---
name: batched-transport-flood
description: Batched transports (Blink, Zap) pack many events per remote request; per-packet guards and per-event rate limits do not bound server work. Probe one max-size packet of the smallest valid event.
metadata:
  type: feedback
---

When reviewing a guard over a batched transport, do not stop at "bad packets are blocked" and "each event is rate-limited". Send one maximum-size packet whose every byte is the smallest valid event (a no-data event) and one packet of unknown event indexes, and time it.

**Why:** J025 Net r1 (2026-10-24): the guard blocked only on decode errors; a 65,535-byte packet of one-byte StateHydrate events cost 104-112 ms in Lune (one task.spawn per event + Net's rate denial), was never a reject and never blocked. Unknown indexes were silently skipped (7 ms per packet). The engine's ~500 requests/s limit counts packets, not events. Builder, QA and the contract budget all covered only bad-packet floods.

**How to apply:** for any transport that decodes several events per request, ask "what bounds events per client per second before the spawn?" and run the probe on the spec harness in a scratch copy. See [[same-server-rejoin]] for the same "trace the case nobody listed" habit.
