> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. J010. Format: `rules/messages.md` (§2 brief, §3 hand-back). Values in angle brackets are filled per ticket; example values are examples, not defaults. Every brief is sent whole in one message and lists every rule the receiver must keep.

# Engineering hand-offs

## 0. Who hands what to whom
| From → to | When | Carries |
| --- | --- | --- |
| lead → architect | new system, refactor, repeated failure | intent, owner decisions, scope, budget |
| architect → feature-builder / quick-builder | plan done | owned files, interface, invariants, checks, docs, effort |
| architect → qa-lead | plan done | invariants and failure cases for the trace table |
| architect → performance-engineer | hard-by-nature design | the budget and the measurement to design first |
| builder → reviewer | candidate ready | change manifest, intent, test results |
| reviewer → builder | blocking findings | proven findings, disposition |
| builder → qa-lead | candidate ready | revision, manifest |
| qa-lead → builder | acceptance failed | test name, observed vs expected, revision |
| any engineer → performance-engineer | lag, memory, join size | symptom, scene, budget |
| performance-engineer → builder | fix inside the builder's files | capture, bottleneck, budget, behaviour to keep |
| builder → architect | third patch, or the API cannot meet the contract | the attempts and measurements, or the 4-part decision |
| engineer → game-designer | missing design intent | the question, options, default |
| engineer ↔ ui-ux-designer, vfx-designer, sound-designer, animator, environment-designer | a feature needs their craft, or their output needs wiring | the gameplay contract (fixed), the craft (open) |

Rules for every hand-off: the receiver checks what it gets against the brief before building on it; the reply goes to the asker; a ledger ticket exists (`rules/company.md` §3); `inside: no` → `needs-decision`.

## 1. architect → feature-builder (build ticket)
```text
<intent>
Players can buy <item> with <currency> from the shop screen. The purchase must never charge twice or grant without charging, even if the player spams the button or leaves mid-purchase; it is the first money path in the game, so it sets the pattern for the rest.
</intent>
<spec>
id: <J0nn-T0n>
from: architect
to: feature-builder
model: opus
effort: high                       # money (owner 2026-10-21)
skills: [engineering-craft, testing, data-saving, networking-security, platform-policy]
refs:
  - knowledge/jobs/<job>/architect/plan.md     # invariants I-1..I-4, owners, placement
  - knowledge/external/roblox-creator-docs/<page for each engine system>
fixed:
  files_owned: [src/server/Shop/PurchaseService.luau, src/shared/Shop/Prices.luau, tests/shop/*.spec.luau]
  interface: "PurchaseService.requestPurchase(player: Player, itemId: string): (\"done\" | \"denied\" | \"unavailable\", string?)"   # plan §3
  invariants: [I-1 balance never negative, I-2 one grant per request id, I-3 price read on the server from Prices, I-4 rejected request changes nothing]
  remote: Shop.Purchase (RemoteFunction)        # plan §4
open: [code structure inside the owned files, helper names, test layout]
avoid: [a purchase framework, a second balance owner, trusting a client price]
not_in_scope: [shop UI, new items, analytics events]
rules: [Validate every client argument: type, NaN/inf, range, rate, ownership, state. Server authority for money. Content as data: prices live in Prices.luau. --!strict in shared and server code. Engine features first; any custom infrastructure needs the engine-gate answer. Failing tests first, on the real price table. Never edit protected acceptance tests or shared registries; return the lines you need.]
deliver: the owned files, tests, change manifest
checks:
  - C1: double request inside one frame → one charge, one grant (spec)
  - C2: leave between charge and save → no grant without a committed save, no lost purchase (spec with the store fake)
  - C3: NaN, negative, unknown itemId → "denied", balance unchanged
  - C4: luau-analyze clean; full test run PASS; Studio purchase run MCP-verified
return: hand-back to architect, rules/messages.md §3, change manifest (engineering-craft EC-13)
</spec>
```

## 2. architect → quick-builder
```text
<intent>Add the <name> item to the shop. Nothing else changes; the shop already supports items of this kind.</intent>
<spec>
id: <id>  from: architect  to: quick-builder  model: opus  effort: medium
skills: [engineering-craft]
fixed:
  files_owned: [src/shared/Shop/Items.luau, tests/shop/items.spec.luau]
  values: {id: "<id>", price: <n>, icon: "<asset id>"}   # owner decision D-<n>
not_in_scope: [prices of other items, shop code, UI]
rules: [Same checks as any change. Stop and return if the change needs code outside the owned files, touches money logic, saves or remotes, or needs a design choice. Real class and property names from _api-reference only.]
checks: [C1 item appears in Items with the fixed values (spec), C2 existing item specs still PASS, C3 luau-analyze clean]
return: hand-back to architect, short change manifest
</spec>
```

## 3. builder → reviewer
```text
<intent>Review the purchase path before merge: it is the first money path, so a duplicate grant or a client-set price would hurt players and the game's trust.</intent>
<spec>
id: <id>  from: feature-builder  to: reviewer  model: opus  effort: high   # money
skills: [code-review, engineering-craft, data-saving, networking-security, platform-policy]
refs: [knowledge/jobs/<job>/architect/plan.md, <change manifest path>, <test log path>]
fixed: {base: <commit>, candidate: <commit>, files: [<owned files>]}
rules: [Find first, filter second. Report only real problems with proof: file:line, input or sequence, wrong outcome. No style findings. A clean change gets "no blocking findings". Check engine-gate answers, docs read, placement, and that the tests can fail.]
checks: [C1 every harm area walked or skipped with a reason, C2 every finding re-read in the code]
return: disposition (merge / fix first) and findings to feature-builder; copy to the ledger
</spec>
```

## 4. reviewer → builder (fix first)
```text
<intent>Two findings block the merge: one lets a player be charged twice on a retry. Fix those; the notes are optional.</intent>
<spec>
id: <id>  from: reviewer  to: feature-builder
fixed:
  blocking:
    - "Critical · PurchaseService.luau:88 · two requests with the same id while the save yields → both pass the pending check → two charges · data-saving D-11 · record the request id before the yield"
    - "High · PurchaseService.luau:120 · player leaves during the save → connection never disconnected → leak per purchase · architecture R-11 · give it a lifetime owner"
  notes: ["Low · Prices.luau:4 · unused constant"]
rules: [Fix only the blocking items unless the brief says otherwise. Add a failing test for each fix first. Round 2 reviews only the new diff.]
return: candidate commit + test results to reviewer
</spec>
```

## 5. any engineer → performance-engineer
```text
<intent>Players report a hitch when a large structure collapses. Find what costs the time and bring the worst frame under budget without changing how the collapse looks or plays.</intent>
<spec>
id: <id>  from: <role>  to: performance-engineer  model: opus  effort: high
skills: [performance, engineering-craft, studio-mcp]
refs: [<scene or place version>, <owner report D-n>]
fixed:
  budget: {frame_p95_ms: 16.7, worst_frame_ms: 50}   # game performance note or J010-D2 test default
  must_not_change: [collapse result, debris lifetime rule, what players stand on]
open: [the bottleneck, the fix, the capture tools]
rules: [Measure before any change: fixed recipe, 3+ runs, spread. One change at a time behind a default-off switch. Same recipe after. Behaviour checks must PASS. No physical phone → phone result BLOCKED.]
checks: [C1 before/after table from the same recipe, C2 behaviour checks PASS, C3 change manifest]
return: hand-back to <role>
</spec>
```

## 6. performance-engineer → builder (fix in the builder's files)
```text
<intent>The collapse hitch is the reset rebuilding every part in one frame (capture attached). Spread or avoid the rebuild so the worst frame stays under budget; the rebuilt structure must be identical.</intent>
<spec>
id: <id>  from: performance-engineer  to: feature-builder  effort: medium
refs: [<capture path>, <recipe path>]
fixed: {bottleneck: "<scope> <ms> in frame <n>", budget: {worst_frame_ms: 50}, files_owned: [<files>]}
rules: [Engine features first. Behaviour identical (golden check). Hand the candidate back to me for the after-capture; do not claim the speed-up yourself.]
return: candidate commit to performance-engineer
</spec>
```

## 7. architect → qa-lead
```text
<intent>Plan the tests that prove the purchase path is safe on the real price table, including what a hand-written case would miss.</intent>
<spec>
id: <id>  from: architect  to: qa-lead  model: opus  effort: medium
skills: [testing, engineering-craft, data-saving, networking-security]
refs: [knowledge/jobs/<job>/architect/plan.md]   # invariants I-1..I-4, failure cases F-1..F-5
fixed: {acceptance_path: tests/acceptance/shop/ (builder has no write access), candidate: <commit when ready>}
rules: [Trace table first. Real content and scale. Expected results from the plan, not from the code. Planted-fault check: report caught x of n and false alarms. Verdict words with revision and logs.]
return: trace table, tests, results and the owner's result card to architect
</spec>
```

## 8. qa-lead → builder (acceptance failed)
```text
<intent>One acceptance check fails on your candidate: a refund path leaves the balance one unit high.</intent>
<spec>
id: <id>  from: qa-lead  to: feature-builder
fixed: {candidate: <commit>, failed: "shop.refund_after_rejoin: expected balance 100, observed 101", log: <path>}
rules: [Do not edit the acceptance tests. If you believe the test is wrong, say why to me and the architect.]
return: new candidate commit to qa-lead
</spec>
```

## 9. builder → architect (stop: third patch, or the API cannot do it)
```text
<intent>The contract cannot be met as planned: the engine does not report contact forces in this mode, so "damage from impact force" has no source.</intent>
<spec>
id: <id>  from: feature-builder  to: architect  status: needs-decision
fixed:
  assumption: "contact force is available per collision"
  proof: "probe output <path>: BindToCollisionSummaries errors 'not enabled' (Studio <build>)"
  alternatives: ["damage from velocity change (cheap, tunable)", "wait for the feature flag (unknown date)"]
  player_tradeoff: "velocity damage feels right for falls, weaker for slow pushes"
return: decision to feature-builder
</spec>
```

## 10. engineer → game-designer (missing design intent)
```text
<intent>The cooldown system is built to the plan, but the brief has no cooldown values and no rule for what happens when a player swaps tools mid-cooldown. Those are design choices, so I need yours before the numbers ship.</intent>
<spec>
id: <id>  from: <architect | feature-builder>  to: game-designer
fixed: {data_file: src/shared/Combat/Cooldowns.luau (content as data), current: PROPOSAL values listed in open-questions Q-<n>}
open: [the values, the swap rule]
questions:
  - {q: "cooldown per tool in seconds", default: "the PROPOSAL values in Cooldowns.luau"}
  - {q: "swap mid-cooldown: keep or reset?", default: "keep"}
rules: [Design is the owner's: return proposals for the owner digest, not locked values.]
return: proposals to the asker; the lead puts them in the owner digest
</spec>
```

## 11. engineer ↔ ui-ux-designer
To UI (a feature needs a screen):
```text
<intent>The shop needs a purchase confirmation the player cannot misread: price, what they get, and a clear failure message when the purchase is denied or the service is down.</intent>
<spec>
id: <id>  from: feature-builder  to: ui-ux-designer
fixed:
  states: [idle, confirming, pending, done, denied(reason), unavailable]   # PurchaseService results, plan §3
  data_from_server: {price: number, itemId: string, balanceAfter: number}
  events: [Shop.Purchase result arrives 0.1-2 s after the press]
open: [layout, look, motion, wording]
rules: [Every state from the list has a screen state. Phones first. Paid-random rules in ui-design if the item is random.]
return: spec + Figma node ids + export notes to feature-builder
</spec>
```
From UI (a spec to build): the builder builds the states and bindings exactly as specified, keeps every state, and returns screenshots per state at phone size (MCP-verified) to the ui-ux-designer for a look check.

## 12. engineer ↔ vfx-designer
To VFX: `fixed` holds the gameplay truth the effect must show and must not change (radius, timing, hit frame, who sees it), the event name the code fires, the per-frame budget (`max_particles`, emitter count) and where the effect is anchored; `open` holds every craft choice. From VFX: the builder wires the effect from `spec.json` as data on the event it names, plays it on the client, never adds gameplay to it (visual effects never deal damage), and returns a capture request to the vfx-designer.
```text
<spec>
id: <id>  from: feature-builder  to: vfx-designer
fixed: {event: Combat.HitResolved (client), radius_studs: 6, impact_t: 0.18 s, budget: {max_particles: 400}}   # combat contract, perf budget
open: [layers, textures, curves, camera feel]
return: spec.json + frame script + capture request to feature-builder
</spec>
```

## 13. engineer ↔ sound-designer
To sound: cue ids the code will play, the moment each fires (event name and timing), how often it can repeat at worst, and the voice budget. From sound: the builder plays each cue by its id from data, on the client unless the brief says otherwise, respects priority and the voice cap, and reports any cue it cannot place.
```text
<spec>
id: <id>  from: feature-builder  to: sound-designer
fixed: {cues: [sfx.shop.confirm, sfx.shop.denied], fires_on: Shop.Purchase result, max_rate: 2 per second per player}
open: [the sounds, layers, mix inside the budget]
return: cue cards + asset ids to feature-builder
</spec>
```

## 14. engineer ↔ animator
To animation: the action states the code drives, the gameplay timing contract (wind-up, hit frame, recovery in seconds), the marker names the code listens for, and whether the server or the client plays the clip. From animation: the builder loads clips through `Animator`, listens for the named markers instead of guessing times, and never lets an animation finishing decide gameplay (`architecture` R-04).
```text
<spec>
id: <id>  from: feature-builder  to: animator
fixed: {states: [idle, windup, strike, recover], timing: {windup: 0.25, hit_marker: "Hit", recover: 0.4}, plays_on: client (server decides the hit)}
open: [poses, arcs, secondary motion]
return: clip ids + marker list + rig notes to feature-builder
</spec>
```

## 15. engineer ↔ environment-designer
To environment: what the code needs from a place: tags or attribute names on parts the code reads, collision groups, which parts must be anchored or simulated, streaming mode per model group, spawn and route points, and the place's Part, triangle and replicated-size budget. From environment: the builder never edits the stage; it reports placement or budget problems back with the measurement (`performance` captures, join-size breakdown).
```text
<spec>
id: <id>  from: <architect | performance-engineer>  to: environment-designer
fixed: {tags: [Breakable, SpawnPoint], collision_groups: [World, Debris], streaming: {Landmarks: Persistent, Props: Default}, budget: {client_parts: <n>, join_size_mb: <n>}}   # plan §5, performance note
open: [the place, its look, its dressing]
return: place version + scene audit to the asker
</spec>
```
