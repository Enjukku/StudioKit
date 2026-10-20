> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Source: owner-supplied operations paper, digest `knowledge/reference/architecture/roblox-operations-2026-10.md` §3. **These are proposed starting gates, not Roblox limits and not measurements of any game.** A game adopts them as PROPOSAL in its performance note, then replaces them with its own measured envelope.

# Starting performance budgets (when a game has none)

## Devices (record exact model, OS, Roblox build, quality level)
| Tier | Example devices | Frame goal |
| --- | --- | --- |
| Floor phone | Galaxy A13 4 GB, iPhone SE (2nd gen); graphics quality 3 and automatic | steady 30 FPS |
| Target phone | Galaxy A54, iPhone 13; quality 5 and automatic | 60 FPS |
| Desktop | integrated-GPU laptop (e.g. Intel Iris Xe, 16 GB), 1920×1080, quality 5 (also test 10) | 60 FPS |
Roblox itself names no minimum device: pick from the game's real audience when known.

## Gates
| Metric | Floor phone | Target phone / desktop |
| --- | --- | --- |
| Frame interval | p95 ≤ 35 ms, p99 ≤ 50 ms, ≤ 1 hitch > 100 ms per 10 min | p95 ≤ 18 ms, p99 ≤ 25 ms, ≤ 3 hitches > 50 ms per 10 min |
| Client CPU, GPU (separately) | p95 ≤ 25 ms, p99 ≤ 30 ms | p95 ≤ 12 ms, p99 ≤ 16 ms |
| Our client scripts | - | p95 ≤ 3 ms |
| Client memory | ≤ 1,000 MB steady, ≤ 1,200 MB peak, no out-of-memory | ≤ 1,500 MB steady, ≤ 1,800 MB peak |
| Memory retention | same checkpoint rises ≤ 5 % (or 50 MB) over 20 identical cycles; a steady climb blocks release | same |

| Server metric | Gate |
| --- | --- |
| Work per frame | p95 ≤ 12 ms, p99 ≤ 16 ms; ≥ 59 FPS in every 60 s window |
| Physics | p95 ≤ 3 ms (part of the work budget) |
| Our server scripts | p95 ≤ 4 ms |
| Memory | ≤ 3,000 MB and < 50 % of 6.25 GiB + 100 MiB × peak players |

| Network and loading | Gate |
| --- | --- |
| Our remotes, client → server | ≤ 30 events/s and ≤ 5 KB/s per player |
| Our remotes, server → client | ≤ 10 KB/s per player (10 s average); cosmetic streams 10-20 Hz, interpolated |
| Total per client | receive p95 ≤ 30 KB/s, send p95 ≤ 10 KB/s; investigate > 50 KB/s for 5 s |
| Join to play | cold p50 ≤ 5 s, p95 ≤ 10 s (constrained network p95 ≤ 15 s); warm p95 ≤ 5 s |
| Streaming | no falling through missing floors; unplanned pause p95 ≤ 250 ms |
| Review trigger | > 50 moving replicated assemblies near one client: profile (not a hard cap) |

## Method
- 15 min warm-up, then three 10-minute scripted routes through spawn, the busiest area, combat or interaction, a map edge, respawn, shop UI and chat. Record heat, charging state, battery, graphics mode; cold and warm joins.
- Server tests with 1, 6 and a full server of real clients; a 2-hour soak with join, leave, respawn and round resets.
- Network fixtures: nominal 50 ms RTT; constrained 150 ms RTT, 20 ms jitter, 1 % loss (Studio Network Simulator for latency and loss).
- Use per-frame distributions; never average percentiles. ≥ 100 joins for a join p95. On the dashboard, **P10 FPS is the slow end**.
- A failing floor device means profile or change content or the device tier, never "average it with fast devices".
