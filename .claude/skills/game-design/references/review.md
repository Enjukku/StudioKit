> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N4 §4 (critique, severity, fix ranking, feature check, finding template), N4 §6 (AI review procedure, do-not list), DS game-designer role (evidence per finding, marked-up maps). Tags O unless marked. The DS 0-2 point totals are dropped: the paper's rule against pseudo-scientific totals wins (J003 decision in the reference README). Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (§1 steps 1, 2, 6, 9 sharpened; finding template fields; new §7 craft-output reviews per recipe, §8 notes, questions and recaps).

# Review: evidence, mechanism, minimal fix, one recommendation

## 1. Procedure (12 steps)
1. **Identify** the artifact, version, owner decision and the question. Keep approved intent apart from suggestions, references and discarded variants. Write the target experience and the game's parameters (camera, device, player count, input, session shape): genre conventions that let new players in stay unless the brief says otherwise.
2. **Causal model.** The four parts in one line each (goal, opposition, decisions, rules). Loop: goal, action, state change, feedback, next decision. System: stocks, flows, dependencies, incentives. Level: routes, information, challenge. Feature: inputs, states, outputs.
3. **Claim ledger.** V / E / O with source date and scope; unsourced values isolated as hypotheses, never stated in an authoritative tone.
4. **Consistency before taste.** Walk a success path, a failure path, a boundary and the relevant multiplayer disagreement. Find contradictions between documents, tuning data, marketing and the build.
5. **Against the approved fantasy and target players.** What does the player do, perceive, choose, learn, repeat? Do not swap in your preferred genre.
6. **Checklists** (loop, principles, feedback and threats, systems, cosmetics, social, spaces, level, feature). Each failure cites an observed example or a missing artifact, with the input it rests on labelled (`playtest-live.md` §1b). Kind of issue: observed player problem · implementation contradiction · plausible risk · unresolved preference.
7. **Adversarial and cross-system cases:** optimal-but-unfun strategies, griefing, collusion, dominant builds, resource runaway, reward farming, interrupted saves, low-information decisions.
8. **Rank fixes** (§3). Policy violations and data-loss risks block release on their own, independent of taste. Separate launch blockers from experiments and polish.
9. **Minimal fix + one alternative** with a different tradeoff: what changes, why it should help, what could get worse, the craft work needed, the test that tells the options apart.
10. **One recommendation** to the owner with the strongest contrary evidence. Ask for a decision only where direction, scope, cost or risk is open. Do not reopen settled decisions without material new evidence.
11. **After an approved change:** update the canonical spec and tuning revision, check integration, rerun affected tests. A repaired symptom does not show the whole design improved.
12. **Close:** each finding gets one disposition: fixed and checked · accepted risk · deferred (reason) · rejected (reason) · awaiting evidence. Failed hypotheses go to `knowledge/design/tried-and-failed.md`. End with an honest recap (§8) and the "could not check" list.

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
Write in `output/design/<task-slug>/review-<artifact>.md` (or the path the brief names) as a table: finding id · artifact and build · goal or tactic · player consequence (what, to whom) · evidence mark (V / E / O) and input status (gate-verified, MCP-verified, owner-confirmed, not verified) · evidence (observation, source, sample, context; `path:line`, a coordinate or an image region) · reproduction or reasoning · severity rationale · minimal fix · alternative · risks introduced · acceptance check · owner decision (pending or exact) · resolution. When a layout image exists, add a marked-up copy (route arrows, numbered problem circles) with the numbers matching the table (DS role). Add a "keep: what works" list and a "could not check" list.

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

## 7. Reviewing a craft's output in a job recipe (my review slots)
I judge play and truth to play, on the captures the recipe names (studio-operator play captures, frame sequences at a known frame rate, two-client captures where a per-viewer variant must be judged (the owner starts the local two-client server: batch them in one request; without one, those checks are Unproven), flat-key captures for every black-fill measure, Figma prototypes at phone size), never on the maker's hand-back alone. **Flat-key capture:** the same game-camera angle and distance as play, the subject in front of one flat colour that fills the frame's border (a large plain backdrop Part, magenta #FF00FF by default; under the subject for a top-down camera), one subject per capture or units spaced apart for `--component`, shadows off (`Lighting.GlobalShadows` false for the capture, restored after; probe first), the floor key under the subject within the key tolerance (`--key-tol`) of the backdrop key, and a key colour far from every colour on the subject: a cast shadow or a shaded floor on the key joins the outline, and a part close to the key colour is keyed out, both with no error. `look_check.py silhouette` finds no subject on a capture with the scene behind it (`invalid-mask`): then I ask for a recapture or a `--mask`, never fall back to judging the outline by eye and calling it measured. Each line is a check: Pass / Fail / Unproven with the capture frame or region as evidence. Findings go in the `rules/messages.md` §6 format; I never edit the work. For every asset, in this order: can the player read what it is and what it does (clarity), does it respond to the player (feel), does it look like the rest of the game (style, the art director's call).

**Character, creature, pet, unit (role reads in play)**
- [ ] A fresh reader names the role from the in-scene game-camera capture and from its black-fill alone (`python tools/art/look_check.py silhouette <flat-key capture>` writes the black-fill image), and it matches the role card (`preproduction/references/documents.md` §8).
- [ ] Lineup next to the roster at the same scale, on one flat-key capture: screen-size rank (`look_check.py silhouette --component N` area per unit) equals threat rank; its relative build (thinnest, average, bulkiest) is the one the role card set.
- [ ] Shape intent matches the role (threats sharp, friendly round); the source of power (weapon, casting hand, core) is the first thing seen.
- [ ] It does not look like its nearest roster neighbour at real size (shop icon at 150x150 with `tools/art/thumb_check.py icon`; in play at the game camera; `look_check.py silhouette <flat-key capture> --compare <neighbour's flat-key capture>`: a high aligned IoU is a flag).
- [ ] The player's own moves are identifiable from the silhouette at each key pose, seen from behind in the third-person camera.
- [ ] Enemy types are told apart by movement pattern alone; a giant moves slowly and heavily.
- [ ] Variants and cosmetics: anchors kept, role read kept, footprint inside the class band (flat-key captures of base and variant), no gameplay value changed (`systems-economy.md` §8).

**Stage (play captures, check-ins during the build)**
- [ ] The `spaces.md` §7 reads hold in the busiest-moment capture on a phone viewport; the first view frames the goal.
- [ ] The route table and spawn-to-contact times match the blockout; no walk past the limit without something to do or see.
- [ ] Collision, cover and sight lines equal the approved blockout (diff), or each change has my sign-off; materials follow the material-to-rule table; a walk capture with audio: each floor's look matches its footstep sound.
- [ ] Hazards show their source and edge, and the edge is the real kill or damage line; boundaries read as impassable and believable.
- [ ] Ambient effects and decoration stay off sight lines and out of the reserved gameplay colours; in the grayscale capture no environment element out-contrasts a character, threat or pickup (`tools/art/look_check.py value` with `--box` around the focal subject when in doubt: an in-scene capture has no key); dead space marked.

**Feature (grey-box verdict; final after code and QA)**
- [ ] The experiment card's risky question is answered by what the captures show; the verdict says PASS / FAIL / Unproven with the observations, not "testers liked it".
- [ ] The four parts hold in play; the plain-block test passes for new objects and enemies.
- [ ] Feedback stack: attempt cue on the press frame or the next (`tools/vfx/clip_metrics.py` `onset_ms`, `principles.md` §7 checks); outcome layer only on confirmation; a rejected request shows no success layer; miss, hit, blocked and big outcomes distinct with sound off; denials name the cause and the fix at the control; frequent events merge; counters end exact.
- [ ] Threats: tell inside the reaction window, two channels, identical across two captures, ended on the damage frame; drawn area on the server's hit shape (debug overlay).
- [ ] Every state change in the spec has its cue in play; the comfort settings in the spec exist and keep the warnings.

**UI screen (decision clear; decision works)**
- [ ] The screen serves one decision, and a tester makes it on the phone-size prototype without help; taps per task match the flow sheet, each extra tap has a reason.
- [ ] Each element says one thing and leads to one action; every HUD element in core play maps to a listed information need (none without one).
- [ ] Critical state (health, ability ready, objective) is read within the read time the information list sets (`preproduction/references/documents.md` §9) in a phone-size capture, in a fixed place clear of the thumbs.
- [ ] Each value sits next to the thing it describes; only the next action moves (one attention motion at a time).
- [ ] Every state exists (empty, error, loading, disabled with its reason, reward, purchase pending); refusals say what is wrong and how to fix it; counters show the true value; paid odds are visible before the buy button and change while a boost is active.

**Effect (does it hide information players need?)**
- [ ] With the worst-case count on screen, effects never cover other players, targets, the HUD, the shop or placement areas; nothing tall blocks the camera's view.
- [ ] Its importance tier and per-viewer variants match the spec (two-client capture, only for an effect with per-viewer variants): the bystander's screen is never shaken, flashed or tinted by it; threats stay full for the threatened player.
- [ ] Danger edge on the server's hit area from warning to last tick; nothing danger-coloured after the last tick.
- [ ] It tells a beginning, a middle and an end; the peak frame of picture (`clip_metrics.py` `peak_ms`) and sound match the contact marker; the big layer follows the confirmed outcome; hit-stop freezes only the attacker, the target and the hit's own particles, its length rises with hit strength and stays well under half a second, and none plays on explosions, projectile throwers or rapid fire.
- [ ] Colour and shape roles follow the code (heal, shield, damage; no hue with two meanings); the effect type reads in grayscale.
- [ ] Frequent effects stay short, merged and capped over 100 repeats; no pulse above 3 per second; camera punches only at the top tier; reduced mode keeps the information.
- [ ] Sound carries the gameplay read: key events identifiable with the screen covered; the sound moves like the mechanic (a slowing effect sounds like slowing); important and threatening sounds carry far, small ones only up close; each weapon or ability keeps its signature sound; a breaking state's warning rises before the break.

**Marketing art (truthful to play)**
- [ ] Every shown action, scale, reward and rarity maps to a promise-ledger row marked playable or planned; nothing shows rewards or rarities the game does not give.
- [ ] The image's moment is reachable in ordinary play from the game camera (no developer-only angle or effect).

**Cutscene (gameplay state sheet)**
- [ ] When control stops and returns, what the player knows and can do after, and that the essential information survives a skip.

## 8. Notes, questions and recaps
- A question to the owner or a reviewer names the goal from the brief ("which reads as most dangerous at phone size?"), never "do you like it?"; labelled options come with my recommendation, and the record names who chose and why.
- A note is a problem with the goal it serves, tagged goal or tactic, with evidence and a concrete target (a marked-up capture or a reference image when visual). When I receive a note that carries a solution ("delete the trees", "add more health"), I restate the problem behind it ("the scene is busy", "players die without knowing why") and solve that, then re-check the original problem, not only the requested change.
- Diagnose by layer (goal, loop, rules, feedback, read, numbers, content) and fix one named problem per pass, the worst first; a fix can create another problem, so re-check the other layers after it.
- Notes are direct; conflicting notes are not averaged: the conflict goes up to the decision owner with both positions stated.
- The best solution may come from any craft: when several crafts propose, I choose by fit to the target experience and record where each idea came from.
- When every option meets the brief, the rest is taste: choose, recommend, commit.
- Every hand-back ends with an honest recap: what works, what is too tame or too big, the weakest point and the next iteration.
