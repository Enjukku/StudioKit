---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025
supersedes: []
---
> Author: orchestrator · claude-opus-5-5 · default · 2026-10-24

# J025 step 4: what every block builder keeps (read after `common.md`, before your ticket)

## Inputs
- Your block's contract: `C:\Users\Firew\Downloads\uterd\roblox-game-framework\contracts\<Block>.md` and `contracts/README.md` (placement, rules every block keeps, test-lane rule, shared Types). **The contract is the spec.** Reviews: `knowledge/jobs/J025-base-framework/reviews/contracts-r1.md` (+ `contracts-r2.md` when present).
- Repo tooling: `README.md`, `REQUIRES.md` (require rule: `./` `../` inside a block, `@game/<Service>/Framework/<Block>` across blocks, `@game/ServerScriptService/vendor/<Pkg>`, `@game/ReplicatedStorage/Packages/<Name>`; no `script.Parent` requires), `tools/placement.json`, `tools/spec/` (Lune runner: a spec file returns `{ [name] = fn }`; `expect` toBe / toEqual / toThrow), `tools/engine/run_jest.luau`.
- Extraction sources named in the contract (GWS / DS file:line): read them, take what is right, leave the game ties.

## How
1. **Failing test first.** For each test row of your contract, write the spec and see it fail for the right reason before the code exists (paste one red run per block in your evidence file). A bug fix starts with a failing case.
2. Lanes: Lune specs `src/<Block>/*.spec.luau` (or `src/<Block>/test/`) run in the gate. Engine rows go in `src/<Block>/*.engine.spec.luau` (Jest 3.20.1, `--!strict`): **write them, do not run them** (no Studio window now: memory). The lead batches engine runs later; list them in the hand-back.
3. Build to the contract. If the contract is wrong or cannot be built as written, stop that part and return `needs-decision` with the smallest change; never change a contract yourself.
4. Q1-Q9 evidence per block, in `knowledge/jobs/J025-base-framework/evidence/<Block>.md` (≤ 80 lines): API count (Q1); `--!strict` + 0 errors + `:: any` grep in public types (Q2); test row → spec name table and one planted fault per risky row that turned the spec red (Q3); failure rows → spec (Q4); the 1,000-cycle leak spec result via `_debugCounts()` (Q5); cost per call measured in Lune with `os.clock` over N calls, and allocations in hot paths named (Q6; engine numbers come later: "not verified" is honest); every server entry point's checks (Q7); engine feature + docs path:line (Q8); the contract's usage example compiles as a spec (Q9).
5. `python tools/gate.py` → `RESULT: PASS` before you hand back. You may not edit `tools/`, other blocks, `contracts/`, `tests/acceptance/` (QA's protected specs), or kit files.
6. No git commit, no push.

## Hand-back (≤ 50 lines, `rules/messages.md` §3)
STATUS line; coverage per contract test row group; files; checks C1 gate last lines, C2 Q1-Q9 each pass / fail / not verified with evidence path; BAR row; engine specs written and not run; questions with defaults; docs_read; optional lesson.

## Bar (stop)
- floor: every contract test row has a spec, the gate passes.
- bar: a staff Roblox engineer would merge it unchanged: smallest code that keeps every invariant, no option with one user, every failure path tested, no allocation per frame in hot paths, quiet logs.
