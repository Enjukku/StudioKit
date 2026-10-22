> Author: orchestrator · claude-opus-5-5 · high · 2026-10-21. Part of `progression-craft`. Sources: notes 01 (curve library, CV/CD rows), 02 (FM, L, G, RP rows), 03 (EA, RC10, NP, SM, FM rows); fact-check FC-M (formulas and sources checked, 2026-10-21). Every formula here is implemented and tested in `tools/progression/curves.py`; use the tool, not mental arithmetic. Coefficients are design inputs, never suggested constants (01:CD). Revised by J018 maker progression-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§6 display rounding points to the hand-off rule).

# The math: curves, incremental, RPG, probability, ledger, precision

Notation: n, k, l = non-negative integer index (state which origin); all times in seconds of active play unless marked calendar. "V derivation" = exact algebra under the stated model, not a measured fact about players.

## 1. Curve library (01:CV1-CV9; O for the intended feel)
| Curve | f(n), domain | Feel (O) | Use (O) | f(0); f(1); f(2) |
| --- | --- | --- | --- | --- |
| Affine | a + b·n; a, b ≥ 0 | equal readable steps | early fixed unlock prices | a; a+b; a+2b |
| Polynomial | a + b·n^p; p > 1 | absolute steps grow | growth without a fixed % inflation | a; a+b; a+b·2^p |
| Triangular cumulative | F(n) = b·n(n+1)/2 (step cost b·n) | rising marginal effort | linear step cost, quadratic total | 0; b; 3b |
| Exponential | a·r^n; a > 0, r > 1 | constant % growth | escalating prices, always compared with income | a; ar; ar² |
| Logarithmic | a + b·log_r(1+n); r > 1 | shrinking marginal progress | compressed displays or transforms | a; a+b·log_r 2; a+b·log_r 3 |
| Fractional power | a + b·n^α; 0 < α < 1 | soft compression, no hard cap | a prestige transform | a; a+b; a+b·2^α |
| Saturating | a + b·n/(h+n); h > 0 | approaches a limit | capped progression | a; a+b/(h+1); a+2b/(h+2) |
| Piecewise linear | slope b₁ up to K, then b₂ (continuous at K) | deliberate pacing bands | change slope at approved band edges; keep K | depends on K |
| Milestone step | base(n)·Π mᵢ^[n ≥ Kᵢ] | deliberate spikes | count- or unlock-based boosts | evaluate at the real Kᵢ |

**Per-level vs cumulative (01:CD, V derivation).** If level 1 starts at 0, cumulative X_l = Σ_{j<l} e_j. Constant e → linear X; linear e → quadratic X. A curve in XP is not the same curve in time: time = X/q only for constant q XP/s; otherwise solve ∫q dt = X. Always say whether a table is per-step or cumulative.

## 2. Incremental and simulator math (02:FM1-FM11; V derivation unless marked)
| Quantity | Formula | Notes |
| --- | --- | --- |
| Next price with k owned (k from 0) | C(k) = b·r^k | the paper's idle example re-indexes from k = 1 (first unit free): C(k) = 4·1.07^(k−1); say which |
| Bulk price for n more | B(k,n) = b·r^k·(r^n − 1)/(r − 1); r = 1 → b·n | only for unchanged exponential prices; with rounding, discounts or milestones that change prices, sum the real prices |
| Max affordable | n = ⌊log_r(1 + w(r−1)/(b·r^k))⌋, then **confirm** B(k,n) ≤ w < B(k,n+1) | the inequality decides, never the float log alone |
| Wait to next purchase | T = max(0, C − w)/P | P = 0 and C > w → **unreachable**, never 0 |
| Simple payback | C/ΔP | a ranking aid, not proof a purchase is best: ignores future unlocks and other buys (O) |
| Prestige, total entitlement | award = max(0, ⌊F(L)⌋ − already_awarded) | spent prestige ≠ already awarded (O accounting) |
| Prestige, per run | award = ⌊G(R)⌋ | |
| Prestige scaling | F = A·x^α: z× the entitlement needs z^(1/α)× the input | cube root: 2× prestige needs 8× input |
| Published prestige formulas (C01, 2017, historical) | AdCap 150·√(L/10^15); Cookie Clicker (L/10^12)^(1/3); Realm Grinder (√(1 + 8M/10^12) − 1)/2 | L = lifetime, M = maximum earnings; four bases exist (max, lifetime, since reset, upgrades since reset; FC-M #1) |
| Offline earnings | η·P_saved·min(Δt, T_cap) | η, cap, auto-buy, generator chains and buff expiry are design inputs; no default (02:FM10-11, O). Decide whether offline income counts toward the prestige basis (lifetime, run) — it changes when resets happen (J011-T08) |

**Worked check (the paper's idle model, M01 inputs, FC-M confirmed).** First unit free, next price 4·1.07^(k−1), income 1.67·k per s, ×2 at 25 and again at 50 owned, buy as soon as affordable: waits 400/167, 214/167, 11449/12525, … s; T_K = (400/167)·Σ_{j=1}^{K−1} 1.07^(j−1)/j; income 40.08 at 24, 83.5 at 25, 163.66 at 49, 334 at 50. Waits fall until about 15 owned, then rise until the next multiplier (02:L13). The source's printed 7.87 is 4·1.07^10 on its simplified base; the cost at 10 owned in this re-indexed model is 4·1.07^9 ≈ 7.3538 (FC-M #3). These are test fixtures, never tuning (03:DN7).

**Continuous vs discrete (02:G1-G4).** A second-tier generator making first-tier generators at 1/s, each making 1 currency/s, gives C(t) = t²/2 continuously. A tick simulator with integer generators is a different model: state whether a new generator produces in its creation tick; a difference from t²/2 is not automatically a bug.

## 3. RPG and action math (02:RP1-RP11)
| Quantity | Formula | Notes |
| --- | --- | --- |
| XP table (M04's reported rule, E; formula = the paper's reading, FC-M #4) | step 1000·l; cumulative X_l = 500·l(l−1); points A_l = l(l−1)/2; X_l = 1000·A_l | time = Σ 1000·l/q_l with q_l XP/s per segment; q is never invented (03:DN1) |
| Hits to kill | N = ⌈H/d⌉ | variable damage: smallest n with Σd_i ≥ H |
| Time to kill | TTK = t₀ + (N − 1)·τ | t₀ = 0 (hit on contact) or τ (full windup); H/(d/τ) is only an approximation |
| Time to die | same rule with the enemy's numbers | an enemy killed before its next strike never lands it: simulate the duel as events, with simultaneous-hit priority stated |
| Effective health | H/(1 − ρ), 0 ≤ ρ < 1 | per damage type; label conditional uptime |
| Stacking | additive bonuses sum inside one factor; multiplicative factors multiply: (1 + 0.18)·(1 + 0.20) − 1 = 0.416 | Diablo IV Season of Blood worked example, 2023, M06 (V; 18 % = example gear value) |
| Random damage | ⌈H/E[D]⌉ is not the expected hit count; expected DPS is not expected TTK | sample or solve the distribution |

**Breakpoints rule (02:RP6, D-06).** On a 5-HP enemy, 4 → 5 damage is +25 % but cuts hits from 2 to 1 (M04's example is about a cost peak; the hit counts are the paper's arithmetic, FC-M). Tune and review by hit counts on named reference enemies, never by smooth DPS.

**Difficulty bands (02:RP11, O).** A band is a named encounter/build pair, not a universal level multiplier. Per approved build and enemy archetype, export HP, effective hit damage, attack timing, hit-count breakpoints, TTK, TTD and recovery cost. Boss mechanics (invulnerable phases, positioning) are written apart from stats.

## 4. Probability (03:RC10, V derivation)
| Quantity | Formula | Use |
| --- | --- | --- |
| Expected cost to first success, independent constant p, no pity | c/p (c = cost per attempt) | a mean, not a guarantee; not "the fair price" (O) |
| Chance of success within n attempts | 1 − (1 − p)^n | |
| Attempts for q confidence | n_q = ⌈log(1 − q)/log(1 − p)⌉ | report the unlucky tail (e.g. q = 0.9, 0.99) next to the mean |
| Pity / guarantee / changing odds | multiply the actual conditional failure probabilities per attempt | the formulas above do not apply unchanged |
Roblox's own policy example: a 10-Robux draw at 5 % next to a 200-Robux guaranteed purchase (= c/p) (03:RC9; FC-R). Paid random rules: `platform-policy`.

## 5. Ledger and affordability (03:EA1-EA6, PC1)
- Per currency and interval: end = start + sources + transfers in − sinks − transfers out ± named adjustments (cap loss, conversion, rounding, reset). An unexplained residual is a model or logging bug (O check on an accounting identity).
- Population: B(t+1) = B(t) + S(t) − K(t); player-to-player transfers cancel, a transfer tax does not; add players entering or leaving the observed set.
- Keep earned, purchased and promotional currency apart in analysis even when the wallet merges them.
- Affordability, not wealth: T = max(0, C − B)/r for constant net rate r; integrate when r changes. A positive net source can be intended (growing population, incremental games); Roblox's "net near zero" is a heuristic, not a law (03:EA5-EA6; FC-R).
- Fixed-basket price index for traded economies: same items, quality and base quantities in both periods; use executed trades, not listings.

## 6. Precision and rounding in Luau (03:NP1-NP4; FC-R)
- Luau numbers are IEEE 754 doubles: integers exact up to 2^53 = 9,007,199,254,740,992; decimals below that are not all exact. An API "int64" label does not add an exact integer type.
- Choose together: smallest meaningful unit, maximum planned balance, representation. Test that adding one unit still changes the balance at the maximum. Display suffixes ("Qa") change text, not precision; past the safe range, a big-number type with defined arithmetic, comparison, saving and rounding (an engineering decision: `architecture`, `data-saving`).
- ⌊x·y⌋ ≠ ⌊x⌋·⌊y⌋ in general: fix the order of modifiers, taxes, discounts, caps and rounding, and whether bulk cost = sum of rounded unit prices or the rounded closed form. Display rounding never changes balances; its direction (balances down, prices up) and fixtures: `data-handoff.md` §5.
