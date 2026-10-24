---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J025 build plan (after G1)

Inputs: `proposal.md` (layers L1-L19 as amended), `decisions.md` (J025-G1, J025-D2, CD-1..CD-6), `research/*.md`. Run this stage in a fresh session (`rules/assistants/claude.md`, Session size).

## The quality bar (what "robust, fast, clean" means, measured)

Every block passes all of these before it is done. The `BAR` row of each hand-back cites the evidence.

| # | Bar | Check |
| --- | --- | --- |
| Q1 | Small public API: a block does one job; no option a game does not use today | API list in the block's contract ≤ 10 functions (Session, Admin may need more: say why) |
| Q2 | `--!strict` everywhere, no `:: any` in the public API | luau-lsp analyze = 0 errors; grep `:: any` in public types = 0 |
| Q3 | Every behaviour and every failure case has a test that can fail | one spec per row of the contract; planted-fault check: break the code, the test goes red |
| Q4 | Failure paths are defined: DataStore errors, throttling, a client that sends bad data, a player who leaves mid-call | each named in the contract with its behaviour and a test |
| Q5 | No leaks | 1,000 join/leave (or open/close) cycles leave 0 live connections and 0 Janitor entries |
| Q6 | Fast | no table allocation per frame in hot paths; measured cost per call (server heartbeat ms, client frame ms, bytes per message) recorded against a budget the architect sets |
| Q7 | Server authority | every client call is checked on the server (type, NaN/inf, range, rate, ownership, state); a rejected call changes nothing |
| Q8 | Engine first | each block names the engine feature it builds on (docs path:line) and why a package or own code is still needed |
| Q9 | Readable by agents | a contract card + a 10-line usage example per block in `engineering-craft/references/framework.md` |

## Steps

| # | Step | Who (role · model · effort) | Done when |
| --- | --- | --- | --- |
| 1 | **Probes**: Blink vs Zap (3 real payloads, NaN/inf/oversize/spam, unreliable, strict output); DataStore + ConfigService inside Open Cloud Luau Execution; Roblox Jest start-up and strict types; `Anim` markers and replication in Studio | researcher / studio-operator · sonnet · medium | each probe has a verdict with evidence; a failed probe switches to the proposal's alternative (Zap, plain-remote wrapper, Lune-only lane) |
| 2 | **Repo and gate**: `Enjukku/roblox-game-framework` with one folder per block; Rokit pins; Selene, StyLua, luau-lsp; Lune spec runner; Jest lane; CI; tags + changelog; kit copy tool + lock-hash check in `tools/verify.py` | feature-builder · opus · medium | an empty block passes the gate locally and in CI |
| 3 | **Contracts**: one short contract per block: API, invariants, owner of each fact, failure behaviour, budget (Q6), test list | architect · opus · high | the reviewer reads each contract before code; no open question |
| 4 | **Build the blocks**, failing tests first, in dependency order: Loader → Session (+ purchases) → Net → State → Screens → Motion → Anim → Config → Analytics → helpers (RateLimit, Amount, ledger) → Admin panel | feature-builder · opus · medium (Session, Net, Admin: high) | gate PASS; Q1-Q9 evidence per block |
| 5 | **Hard tests** for the risky blocks: Session against a mock store that throttles, fails, crashes mid-save, is stolen by a second server, shuts down with a full server; Net against spam, NaN, oversize, wrong owner; Admin: a non-admin call is refused | qa-lead · opus · medium (protected tests the builder cannot edit) | all pass; planted faults caught |
| 6 | **Reviews**: every block; deep for Session, Net, Admin | reviewer · opus · high | ready-to-merge verdict; ≤ 3 rounds (`rules/anti-overengineering.md` §20) |
| 7 | **Game template**: Rojo, Rokit, Wally files, gate, entry scripts, folders, one sample system with tests, the content-test pattern, a filled packages row | feature-builder · opus · medium | a new game is created from it in one command |
| 8 | **Proof**: a blank game from the template, in Studio with 2 clients: join → data loads with a lock → a checked remote changes saved data → UI shows it → admin panel works for an admin and is refused for a non-admin → leave → data saved. Measure Q6 numbers | studio-operator · sonnet · medium | every step MCP-verified with Output and numbers |
| 9 | **Kit books**: `engineering-craft` (`references/framework.md`), `architecture`, `data-saving` §5, `networking-security`, `code-review` greps, `testing` lanes, `ui-basics`, `animation-craft`, `game-profile.md` packages row, `rules/packages.md` ProfileStore exception, `knowledge/reference/<package>.md` per package | orchestrator writes briefs; kit-writer stand-in · opus · medium | `python tools/verify.py` PASS; `sync_harness.py --check` PASS |
| 10 | **G3**: the owner sees the proof run, the numbers, and what is not verified | orchestrator | owner's words recorded with the approved tag |
| 11 | **Adopt in old games**, one block per small job (loader, then Session on the same ProfileStore keys, then Net); never two transports at once | per game | each game's gate PASS after each block |
| 12 | **Keep it strong**: tagged versions; every game's lessons flow back as framework tickets; the framework steward agent (D-135) later | lead, per game | changelog per tag |

## Risks to watch

- Session is the one block where a bug loses player data: it gets the most tests (step 5) and the deepest review.
- Admin is the biggest exploit surface: server check on every action, client code only for admins.
- Over-building: any option, hook or abstraction with one user is cut in review (`rules/anti-overengineering.md` §5).
