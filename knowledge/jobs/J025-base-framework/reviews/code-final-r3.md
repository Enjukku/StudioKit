---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: reviewer · claude-opus-5-5 · medium · 2026-10-24

# J025 final selective recheck (round 3): Admin R1, R2; Net R2-1, R2-2; template Admin wiring; install rules

Depth: standard on the changed lines only (all other verdicts carry). Code read at the candidate hashes before the evidence notes.
Candidate (sha256, re-read after the gate): `src/Admin/init.luau` bb129382, `src/Admin/Builtins.luau` cbf4e7ee, `src/Net/init.luau` 9067f189, `src/Net/tools/schema-lint.luau` fad552c2 (the brief's `tools/schema-lint.luau` lives at `src/Net/tools/`); template files and `tools/install.py`, `tools/check_lock.py` as on disk 2026-10-24.

Goal questions: (1) Ad9: does an exemption end when its reason (a non-default speed or jump) ends? (2) Ad1: can a def admit non-members? (3) CC-13/N6: does a departed sender's packet decode anything? (4) CC-15: can a client shape the lint passes still exceed Net's 512-value walk? (5) Ad2/Ad3/Ad10: does the template's game action write only for an admin, only in Studio, only through `save:update`, and does no test helper reach the place?

## Items

| Item | Verdict | Where | Re-traced sequence |
| --- | --- | --- | --- |
| Admin R1 | **closed** | `Builtins.luau:136`, `:148-156`; `init.luau:187-199` | Speed 32 → `exempt(who, "speed", true)`; speed 16 (= `StarterPlayer.CharacterWalkSpeed`) → `setExempt(on=false)` clears `speed`, and the entry goes nil when no flag is left → `isExempt` false. Jump uses the default its own `UseJumpPower` branch writes (`CharacterJumpPower` / `CharacterJumpHeight`). Separate `speed` and `jump` flags: resetting one keeps the other. Compared against the snapped control value, not the float32 Humanoid property. Spec Ad-T11 :463, :467 (red before, planted red). Known limit (JumpHeight 7.2 off the slider grid) ends on respawn or leave: stated in evidence, not a hole |
| Admin R2 | **closed** | `init.luau:473-476` | `isLimit` (finite number) first, then `minRank < 1` → `problem(...)` before any connection; 0, -1, 0.5 refused; NaN/inf refused by `isLimit`. Ad-T9 :375 |
| Net R2-1 | **closed** | `init.luau:207-210`, `:218-245` | Sender with `Parent ~= Players` → `allow` false before the first event → generated module raises `flood` → `reject`: `strikes` nil (cleared on leave), `flood` +1, the `Parent == Players` guard (:227) creates no strike, one sampled line per 10 s. 0 events decoded. Net-T23 (Transport.spec :490) |
| Net R2-2 | **closed** | `schema-lint.luau:459-540` | Count follows Net's walk (`init.luau:77-80`: each value and table once, keys not counted): array 1 + upper × inner, struct 1 + fields, tuple 0 + args, merge −1, set 1 + n, tagged union max + tag. `u8[..64][..64]` → 4161 fails; `(u8[..300], u8[..300])` → 602 fails; `struct {A: u8[..511]}` → 513 fails; flat `[..511]` → 512 passes and Net accepts 512 (`walked > 512`). Oversized inner arrays are reported once (`oversized == before`). Lint.spec :60-69 |
| Template Admin wiring | **closed** | `template/src/server/AdminActions.luau:20-33`; `Systems/AdminSetup.luau:16-34`; `src/admin/Pages.luau`; `default.project.json:4`, `:34`, `:40-42` | Admin runs its checks first (not_admin, value 1..1,000,000 integer, target present: `init.luau` handler order); then `give_coins` refuses `studio_only` unless `RunService:IsStudio()` (Admin has no Studio flag for game actions, `init.luau:437`, so the action's own check is the one way); grant only through `Save.handle:update` + `Coins.grant` (cap `coins_full`). Pages in ServerStorage. Spec `AdminActions.spec.luau`: admin done +500, non-admin not_admin with nothing written, outside Studio studio_only |
| Install rules (test/ helpers, dev tools) | **closed** | `tools/install.py:60-76`, `:166-195`; `tools/check_lock.py:23`, `:83-91`, `:94-115` | Block `test/` helpers copied to `Framework/<Block>/test/` without specs and listed in the lock; `DEV_TOOLS` copied and their roots derived from the lock, so an edit or extra file fails (`edited` / `extra file`). The game project ignores `**/test`, `**/test/**`, `**/*.spec.luau`. ProofGame (scratch) re-built by me: no `test`, `World`, `Lune` or `*.spec.luau` instance in the place; Admin, AdminSetup, AdminActions, AdminPages/Pages present; `check_lock.py` PASS 44 files |

No new blocking problem in the changed lines. No new findings.

## Gate
`python tools/gate.py` (framework, 2026-10-24): `RESULT: PASS`; specs 60 files, 488 passed, 0 failed (the Net Planted P03 failure named in the brief no longer shows); types 0 errors, 0 deprecated; copy-tool 11 tests; engine lane SKIP (Studio only). Gate-verified.

```text
<spec>
artifact: roblox-game-framework Admin init bb129382, Builtins cbf4e7ee; Net init 9067f189, schema-lint fad552c2; template Admin wiring; tools/install.py, tools/check_lock.py (2026-10-24)
reviewer: reviewer
looked_at_first: [src/Admin/Builtins.luau:100-157, src/Admin/init.luau:184-205 and :463-480, src/Net/init.luau:55-110 and :205-253, src/Net/tools/schema-lint.luau:455-540, template AdminActions/AdminSetup/Pages/default.project.json, tools/install.py, tools/check_lock.py, gate run]
findings: []
keep:
  - "R1: one flag per reason (speed, jump), each cleared when its value returns to the place's default; respawn and leave clears untouched"
  - "R2: minRank checked after the finite check and before any connection (no half state)"
  - "R2-1: departed sender spends nothing and creates no strike; reject's N6 guard kept"
  - "R2-2: lint counts the way Net's walk counts; boundary 512 consistent on both sides"
  - "Template: the sample grant is Studio-only, admin-gated by Admin, and writes only through save:update with the cap"
  - "Install: test helpers and dev tools locked; the game project keeps test/ and specs out of the place"
could_not_check:
  - {step: "R2-1 engine reach (a remote resuming after removal)", missing_input: "Studio probe", closes_it: "1-client probe in the throwaway place", who: "studio-operator"}
  - {step: "Template Admin wiring at runtime (panel copy, give_coins in Studio, studio_only live)", missing_input: "Studio multi-client run", closes_it: "the Studio proof (Ad-T8, Ad-T12)", who: "qa-lead / studio-operator"}
  - {step: "T-12 multi-root Jest runner", missing_input: "Studio engine lane", closes_it: "engine lane in the Studio proof", who: "qa-lead"}
weakest_part: "Install and lock rules were checked by code read and one ProofGame rebuild, not by re-running the game gate's planted lock edits."
verdict: ready for the Studio proof
</spec>
```

Note, outside scope (no finding): the built ProofGame place carries `Packages/_Index/evaera_promise@4.0.0/promise/lib/init.spec.lua` from a Wally dependency (the `*.spec.luau` ignore does not match `.lua`). Inert module, not a test hook; listed for the lead only.
