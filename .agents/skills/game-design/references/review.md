> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N4 §4 (critique, severity, fix ranking, feature check, finding template), N4 §6 (AI review procedure, do-not list), DS game-designer role (evidence per finding, marked-up maps). Tags O unless marked. The DS 0-2 point totals are dropped: the paper's rule against pseudo-scientific totals wins (J003 decision in the reference README).

# Review: evidence, mechanism, minimal fix, one recommendation

## 1. Procedure (12 steps)
1. **Identify** the artifact, version, owner decision and the question. Keep approved intent apart from suggestions, references and discarded variants.
2. **Causal model.** Loop: goal, action, state change, feedback, next decision. System: stocks, flows, dependencies, incentives. Level: routes, information, challenge. Feature: inputs, states, outputs.
3. **Claim ledger.** V / E / O with source date and scope; unsourced values isolated as hypotheses, never stated in an authoritative tone.
4. **Consistency before taste.** Walk a success path, a failure path, a boundary and the relevant multiplayer disagreement. Find contradictions between documents, tuning data, marketing and the build.
5. **Against the approved fantasy and target players.** What does the player do, perceive, choose, learn, repeat? Do not swap in your preferred genre.
6. **Checklists** (loop, principles, systems, social, level, feature). Each failure cites an observed example or a missing artifact. Kind of issue: observed player problem · implementation contradiction · plausible risk · unresolved preference.
7. **Adversarial and cross-system cases:** optimal-but-unfun strategies, griefing, collusion, dominant builds, resource runaway, reward farming, interrupted saves, low-information decisions.
8. **Rank fixes** (§3). Policy violations and data-loss risks block release on their own, independent of taste. Separate launch blockers from experiments and polish.
9. **Minimal fix + one alternative** with a different tradeoff: what changes, why it should help, what could get worse, the craft work needed, the test that tells the options apart.
10. **One recommendation** to the owner with the strongest contrary evidence. Ask for a decision only where direction, scope, cost or risk is open. Do not reopen settled decisions without material new evidence.
11. **After an approved change:** update the canonical spec and tuning revision, check integration, rerun affected tests. A repaired symptom does not show the whole design improved.
12. **Close:** each finding gets one disposition: fixed and checked · accepted risk · deferred (reason) · rejected (reason) · awaiting evidence. Failed hypotheses go to `knowledge/design/tried-and-failed.md`.

Critique order (9): audience and promise → causal loop → choice and information → skill and learning → systemic consistency → social consequences → content feasibility → time and monetization limits → evidence adequacy. A critique that names a symptom without a plausible mechanism or an observable test is incomplete.

## 2. Ratings and severity
- Per check: **Pass / Fail / Unproven**. Unproven is not Pass and not a claim the feature is bad. No weighted totals; never average a blocker away with good art or content volume.
- Severity (internal labels, not industry scores): **Blocker** (contradicts the core promise, safety, fairness or feasibility) · **Major** (frequent or substantial harm) · **Minor** (local polish).

## 3. Ranking fixes (one list; the paper gives three slightly different ones, N4 W10)
Show these 7 components per fix, in words, no invented arithmetic: harm (severity) · population affected · recurrence (how often) · coupling (what else depends on it) · confidence in the evidence · reversibility · cost. Prefer the fix of the enabling cause over compensating for symptoms. When uncertainty is high and the decision is expensive, the best next task may be a test, not a feature.

## 4. Feature check (9 items)
| # | Item | Pass when | Why (this kit's reason; the paper gives none) |
| --- | --- | --- | --- |
| F1 | Purpose | supports a named player outcome and pillar; leaving it out was considered | features without purpose dilute the game |
| F2 | Behaviour | inputs, states, transitions, consequences, interruptions specified so two builders would not build different rules | ambiguity becomes bugs and arguments |
| F3 | Authority | who decides shared outcomes; how disagreements, reconnects and duplicate actions resolve | multiplayer breaks at the edges |
| F4 | Craft fit | UI, VFX, sound, animation and world show the same event and priority | mixed signals make polished parts incoherent |
| F5 | Acceptance | observable criteria cover failure and boundary paths | happy-path tests miss real failures |
| F6 | Measurement | intended effect and the harms have defined observations; the metric cannot improve by making the experience worse | a metric that rewards harm will be optimized |
| F7 | Dependency | prerequisites, order, tuning refs, content workload, migrations recorded | hidden work stalls production |
| F8 | Safety and policy | restrictions, abuse cases, accessibility, audience reviewed | policy problems block release |
| F9 | Decision | the owner approved scope and tradeoff; alternatives are not shown as final | only the owner sets direction |

A feature is ready when its open questions are understood and accepted by the owner, not when a checklist has decorative ticks.

## 5. Finding template (13 fields)
Write in `output/design/<task-slug>/review-<artifact>.md` (or the path the brief names) as a table: finding id · artifact and build · player consequence (what, to whom) · evidence mark (V / E / O) · evidence (observation, source, sample, context; `path:line`, a coordinate or an image region) · reproduction or reasoning · severity rationale · minimal fix · alternative · risks introduced · acceptance check · owner decision (pending or exact) · resolution. When a layout image exists, add a marked-up copy (route arrows, numbered problem circles) with the numbers matching the table (DS role). Add a "keep: what works" list and a "could not check" list.

## 6. Do not
- Report ideas as prototypes or historical attrition as a quota (D02-D05; FI).
- Invent target session lengths, retention benchmarks, drop rates or difficulty tolerances; put unsupported numbers in the assumptions list.
- Let the fastest reward path displace the activity that defines the game (Diablo III, D17 E; not a ban on markets).
- Assume instruction-heavy goals keep self-directed discovery (Don't Starve, D19; unverified at fact-check, OPINION).
- Treat short beta retention as validation of long-term systems (Squad Busters, D29).
- Read metrics without context, or accept every requested solution as the right cause (D13, D16 E).
- Copy another game's parameters without its mechanics, audience and evidence.
- Equate more rewards with progress, more health with fair difficulty, more content with depth, more time played with player value.
- Present an imagined playthrough, an invented persona or a numerical model as playtest evidence.
- Cite the popular "Zelda terrain triangle" account as fact: it was not found in a primary source (N4 Q7).
