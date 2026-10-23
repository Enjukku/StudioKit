> Author: J019 P6 maker · claude-opus-5-5 · medium · 2026-10-22 (G3-P6). Eval briefs for `testing`. Run an agent with only the skill and the brief; score the must-pass checks. The rows named below are the book's (`references/player-facing.md` §2, §3; `SKILL.md` §3, §6).

# testing evals

## Common checks (every brief, must pass)
- C1 Sources of truth listed with their revision before the first row; a missing fact is a question to the briefer, never a guess (SKILL.md §3 step 1; QS-01).
- C2 Every row names its oracle, and no oracle for a truth is the tester's eye or a value copied from the implementation (T-04, T-15; QS-09).
- C3 Verdict words only (PASS, FAIL, BLOCKED, NOT RUN, RUNNER FAILED), each bound to a revision and an input; nothing is reported as run that the brief gives no input for (T-07, T-20).
- C4 A could-not-check list: the step, the missing input, the capture or test that closes it (QS-18).

## E-01 Sell button and boss slam (player-facing rows)
Brief: "Plan the tests for a feature with two parts. (1) A Sell button in the backpack: the client asks the server to sell the selected item; the server may refuse (item locked, backpack empty); on success coins fly to the counter with a '+N' label. Players sell fast, up to about 20 items per second with auto-sell. (2) A boss ground slam: the boss winds up, a ring shows the danger area, then everyone inside the radius takes damage. The radius comes from the data field `Slam.radius`. The game has a reduced-motion setting. Sources: feature contract rev 2, timing list rev 3, VFX read card rev 2."
Must pass:
- A rejected-request row for the sell request (PF-02): no outcome event, no coin layer, no balance change, the refusal shows its reason at the control; a pending state under added latency and no early success. Oracle: the server result in the log and the server balance. Hooks asked for: `Reject` and `DelayMs` (and `FxLog`). Conditions named (added latency) (T-14; QS-02, QS-14).
- A drawn-area row for the slam (PF-04): the drawn ring edge against `Slam.radius` at warning, contact and end, per quality level and viewer; nothing danger-coloured after the last tick. Oracle: the data field the effect reads, never a size judged by eye. Hooks: `DebugShape` built from the same data row, `Trigger`. Conditions named (lowest quality, threatened view, busiest moment) (T-15; QS-03).
- A burst row for the sell coins (PF-10, PF-05): 100 at one per second and a burst of about 20 per second; live copies within the cap, one label and one cue per merge window, the final count exact, counts back to baseline; buying right after a gain uses the true balance. Hooks: `Rate`, `FxLog`, `Set` for the balance (T-10; QS-15).
- A reduced row (PF-07): with reduced motion on, no camera shake or large flash remains and the slam warning keeps a second channel that fires in the log; pulse and blink rates within the PF-07 caps. Hook: `Reduced`. Conditions named (reduced motion, grayscale, sound off) (T-17; QS-16).
- The hook list goes to the builder at plan time with the row each hook serves, not at acceptance (SKILL.md §3 step 3; QS-06).
- A planted-fault list with at least one presentation fault per row group, for example a coin layer on a rejected sale, a ring sized from its own constant, a reduced variant that drops the warning (T-05; QS-11).
- Sound sync and feel are listed as not verified without a device capture or the owner (PF-15).
