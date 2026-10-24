---
type: job
scope: universal
status: active
updated: 2026-10-24
source: J025-B4
supersedes: []
---
> Author: feature-builder · claude-opus-5-5 · medium · 2026-10-24

# Screens: Q1-Q9 evidence (J025-B4)

Artifact: `roblox-game-framework/src/Screens/` {init.luau, Screens.spec.luau, Screens.engine.spec.luau, test/Gui.luau}, files as of 2026-10-24 (repo uncommitted, rule 7). Contract: `contracts/Screens.md` (frozen; review r1 "ready"). Extraction source read: GWS `src/client/Controllers/PanelController.luau:1-203` (stack, Back action, select on open, clear on close); taken: one stack, selection on gamepad only; left: `wireGrid`, `toggle`, SelectionGroup setup, InputController coupling.

## Red run (before code; stub erroring "not built")
`lune run tools/spec/run.luau src/Screens` → `specs: 1 files, 0 passed, 15 failed` (each "Screens.register not built"). First green run: 10/15; the 5 reds were the fake (no child-by-name index) and one wrong expectation of mine in Sc-T3 (Hud was open); code unchanged.

## Q1-Q9
| Q | Result | Evidence |
| --- | --- | --- |
| Q1 API | PASS | 5 functions (`register`, `open`, `close`, `back`, `view`) + `Layer`, `Handle`, `Def`, `View` types, as the contract. Spec hook `_debugCounts()` |
| Q2 strict | PASS (gate-verified) | `--!strict` in all 4 files; luau-lsp new solver 0 errors; `grep ":: any" src/Screens/init.luau` = 0. One typed alias `table.freeze :: <T>(T) -> T` (the solver marks frozen fields read-only, which breaks Charm's `Update<View>`) |
| Q3 tests can fail | PASS | row table below; 10 planted faults, 10 red (F4 and F8 first survived: F4 was a wrong-target plant, re-planted in `back` → red; F8 nav always on survived → added the ScreensNav `Enabled` assertions to Sc7 → red) |
| Q4 failure paths | PASS (Lune) | build error (Sc-T10: nothing in PlayerGui, its janitor cleaned once, error with the build message rethrown); unknown id errors (Sc-T10); late answer (Sc-T5); `firstSelect` missing (Sc-T11, one sampled warn); respawn: `ResetOnSpawn = false` (Sc8; real respawn Sc-T9 engine) |
| Q5 leaks | PASS (Lune) / not verified (engine) | spec "Sc-T4 (Lune half), Q5": 1,000 cycles of open Shop → open Confirm → reopen Shop → close both (alternating `close` and `back`): 0 ScreenGuis, live fake connections back to baseline, `_debugCounts` {open 0, ids 0}. Engine half in `Screens.engine.spec.luau` Sc-T4 (NOT RUN) |
| Q6 cost | PASS (Lune screening, fake instances) / not verified (engine) | 2,000 iterations × 3 runs: reopen (close + open) 0.023 / 0.015 / 0.016 ms; open + close 0.024 / 0.012 / 0.017 ms (budget open ≤ 0.5 ms, close ≤ 1 ms). Fake instances are cheaper than real ones; the engine Sc-T4 prints ms per cycle. Idle: no per-frame work (no RenderStepped/Heartbeat connection); per open: one ScreenGui, one Janitor, one View table + ids list |
| Q7 server authority | n/a | client-only presentation (contract); screens grant nothing |
| Q8 engine first | PASS | below |
| Q9 usage | PASS (Lune) | spec "Q9": the contract usage example (Shop with BuyButton, `alive()` check) with a fake layout and remote; a non-string prop errors "Shop needs an item id" |

## Contract test rows → specs (`src/Screens/Screens.spec.luau` unless named)
| Row | Spec | Planted fault → red |
| --- | --- | --- |
| Sc-T1 | Lune "Sc-T1 (stack logic) ..."; engine "Sc-T1 Bag over Shop ..." | F3 below not hidden → red |
| Sc-T2 | "Sc-T2: back closes the Modal first ..." | F4 back prefers Screen → red |
| Sc-T3 | "Sc-T3: view().blocking follows opens and closes ..." (Charm computed + effect spy; frozen View) | F8 (via Sc7) |
| Sc-T4 | Lune "Sc-T4 (Lune half), Q5 ..."; engine "Sc-T4 open/close x1,000 ..." | F1 no janitor destroy → red; F6 reopen without close → red |
| Sc-T5 | "Sc-T5: a late answer after close finds alive() false ..." | F2 alive always true → red |
| Sc-T6 | "Sc-T6: opening an open id gives one copy ..." (+ an old handle never closes the new open) | F6 → red |
| Sc-T7 | Lune "Sc6 (Lune half of Sc-T7) ..." + "Sc6: switching to a gamepad ..."; engine "Sc-T7 ..." (scenario `gamepad`) | F7 no focus restore → red |
| Sc-T8 | Lune "Sc7 (Lune half of Sc-T8) ..."; engine "Sc-T8 ..." (driver presses ButtonB) | F8 nav always on → red |
| Sc-T9 | engine "Sc-T9 a respawn ..."; Lune "Sc8: ... ResetOnSpawn false ..." | F9 ResetOnSpawn true → red |
| Sc-T10 | "Sc-T10: build throws ..." | F5 no undo on build fail → red |
| Sc-T11 | "Sc-T11: firstSelect names nothing ..." | (warn count) |
| Def.input rule | "Def.input is enabled only while its screen is the top of its layer" | F10 input stays on → red |
| Lifecycle | "register: an unknown layer or an id registered before errors ..." | |

## Q8 engine features
| Need | Engine | Source |
| --- | --- | --- |
| Layer order | `ScreenGui.DisplayOrder` | `_api-reference/classes/ScreenGui.yaml:81` |
| Safe area (U-01) | `ScreenGui.ScreenInsets` = DeviceSafeInsets | `ScreenGui.yaml:176` |
| Survive respawn | `LayerCollector.ResetOnSpawn` = false | `LayerCollector.yaml:55` |
| Hide the Screen below | `LayerCollector.Enabled` | `LayerCollector.yaml:34` |
| Gamepad focus; first selectable fallback | `GuiService.SelectedObject`, `GuiService:Select(root)` | `GuiService.yaml:289`, `:801` |
| Last input device | `UserInputService:GetLastInputType`, `.LastInputTypeChanged` | `UserInputService.yaml:928`, `:1929` |
| Back action; screen-owned actions | `InputContext` (`Enabled`, `Priority`, `Sink`), `InputAction.Pressed`, `InputBinding.KeyCode` | `InputContext.yaml:23-80`, `InputAction.yaml:300`, `InputBinding.yaml:203`; `input/input-action-system.md:24-36` |
Own code still needed: no engine screen stack, back, focus restore or per-open cleanup (`research/state-ui-animation.md` §6).

## Decisions and notes (PROPOSAL)
- ScreensNav: Priority 1000, `Sink = true`, Enabled only while blocking (so it never sinks gameplay's ButtonB outside menus), parented to PlayerGui. **Backspace left out**: it would call `back()` while a player edits a TextBox. Not verified in the engine: that a script-made InputContext under PlayerGui receives input (Sc-T8 engine).
- `build` failure: rethrown with the id and the build's message, not also warned (one line, quiet logs); the caller's thread logs it.
- Hud and Toast inputs are enabled while open (each is the top of its own layer: they do not stack). A Screen's `input` stays enabled under a Modal (contract: "top of its layer").
- Sampled warn helper is duplicated from State (12 lines): follow-up, one shared helper in Helpers.

## Repair round 1 (review code-g1-r1 F1; feature-builder · claude-opus-5-5 · medium · 2026-10-24)
- Fix (`src/Screens/init.luau`, sha256 a3da6bedb37e234c): `closeEntry` removes from openList only when `table.find` returns an index; `open` sets `byId[id]` before `build`, so a `close(id)` or a second `open(id)` while build yields closes this open (Sc5: the newer open wins); after the pcall a closed entry cleans what build added later, destroys `root` and returns its handle; a failing build goes through `closeEntry`. `closeEntry` uses `janitor:Cleanup()` instead of `Destroy()`: a destroyed Janitor has no metatable, so a yielding build's later `janitor:Add` would throw. No API change.
- Red (before fix, `lune run tools/spec/run.luau src/Screens src/Analytics`): `Sc3 (review F1 sequence A)` FAIL "The Parent property of Empty is locked" (closed entry re-parented); `Sc5 (review F1 sequence B)` FAIL at :303 "expected false, got true" (two copies). Green after: 29 passed, 0 failed.
- Planted faults (each red, then restored): drop the `if index` guard → sequence A red; `Destroy` back in closeEntry → A and B red; `byId[id]` set after build → 10 specs red. Sc-T4 (1,000 cycles, 0 guis, 0 entries, connections at baseline), Sc-T6, Sc-T10 still green.
