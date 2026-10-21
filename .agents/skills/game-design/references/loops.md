> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: DS (four parts, name the fun, goals vs tactics; Riot transcripts 2026-10-15), N3 §2 (loops, scales, coupling, prototype gate, core-loop check), FI (prototype counts). Tags as in SKILL.md.

# Loops: what repeats, what changes, what persists

## 1. Four parts of a game (DS §1)
| Part | Question | Missing means |
| --- | --- | --- |
| Goal | what is the player trying to do now, this session, long term? | aimless play |
| Opposition | what stands in the way? | no challenge, no satisfaction |
| Decisions | which meaningful choices get past it? | a toy or a cutscene |
| Rules | what framework governs it, consistently? | confusion, unfairness |

Not every moment must be a hard choice: social, expressive, contemplative or comfortable play can keep a different promise (Koster D25 O vs Sylvester D26 O; N3 §3.3).

## 2. Name the fun (DS §2)
Pick one or two target experiences per feature, written down: living a fantasy (power, role) · thrill and sensation · fellowship and team play · mastery · exploration and discovery · creativity and expression · collection and completion · competition and status · comfort and routine. Art, design and engineering aim at the same target. Separate the **goal** ("feel huge power when the tower falls") from the **tactics** ("rocket damage ×2"); agree the goal first, then compare tactics against it.

## 3. Loops and arcs
A loop is a repeated exchange between the player's mental model and a system that responds; an arc is an experience consumed once. Both are ingredients and can be mixed on purpose (Cook D01 O). A click → animation → currency chain is an interaction loop, not automatically a learning loop (N3 §2.1 O).

| Scale | Sequence | Ask | Warning |
| --- | --- | --- | --- |
| Moment | perceive state → choose → act → perceive consequence | what information changes the next decision? | cosmetic feedback is not a decision |
| Session | pick a purpose → prepare → bounded activity → outcome → reflect → stop or continue | what makes a natural stop, and what makes the player want the next session? Record the real session-length distribution | never assign a prescribed number of minutes |
| Long term | choose an aspiration → grow skill, resources, relationships or expression → face changed possibilities → reassess | which aspirations exist, and can they change? | days and weeks are an analysis horizon, not a licence to demand daily attendance |

(The session and long-term questions are this kit's wording; the paper gives instructions only, N3 W06.)

## 4. Coupling (N3 §2.3 O)
Draw it: **session entry state → moment decisions → session outcome → retained state → changed options next session.** Label what resets, what persists and why. Two failure signs:
- The only lasting change is a bigger multiplier meeting bigger costs → ask what the player anticipates, expresses or enjoys differently next time (an investigation, not an automatic rejection of incremental games).
- Meta rewards make the most effective route skip the intended moment play → the systems conflict.

## 5. Prototype gate (N3 §2.5 O)
Experiment card, one page, 8 fields: player promise · riskiest assumption · smallest playable situation that exposes it · target players · help the facilitator may give · observations · a contrasting explanation · the decision after the test.

- Test feel separately from long-term aspiration when needed, then together: a paper economy cannot show motor feel; a polished combat room cannot show a month-long economy.
- **PASS:** the build can answer the risky question and the team named a result that would change or drop the idea.
- **FAIL:** success defined as "testers liked it"; the only test is the designer playing well; every disappointing result blamed on missing polish without evidence.
- Signs of promise (triangulated, never one metric): players understand an immediate intention; actions have readable consequences; alternatives respond to context; players find or state a better strategy; repeats differ meaningfully; the intended audience continues when free to stop. Confounds: novelty, politeness, rewards for testing, no alternative available.
- Scoped history, not quotas: Splatoon picked a prototype from 70 ideas and already played 4 vs 4; Wonder gathered 2,000+ sticky-note ideas; Supercell cancelled nine games during Clash Royale's development (2016 lecture; the paper's "1 release in 2 years" framing was not found, FI IC56) and counted 5 hits vs 30+ killed (2023). None sets a prototype quota or kill rate (N3 §2.4; verdicts FI). Keep the tested interaction when presentation changes: Splatoon's character and arena changes temporarily broke what ink and hiding meant (D03 E).

## 6. Core loop check (12 items, N3 §2.8 O)
Mark each **Pass / Fail / Unproven**. A readiness failure (no test yet) is not an observed design failure; store the verdict and its reason. Reasons are this kit's (the paper gives none, N3 W07).
| # | Item | Pass when | Why it matters |
| --- | --- | --- | --- |
| 1 | Goal | the player can state or show an immediate objective without help | no goal, no reason to act |
| 2 | Action | an input changes relevant state and the player links it to the goal | otherwise the loop is a toy |
| 3 | Choice | choices serve the intended strategy, expression, social play or comfort; cosmetic variety is not depth | choices are where the player's skill and taste show |
| 4 | Feedback | under target conditions the player sees what happened, why, and what to do next | unreadable cause and effect feels unfair |
| 5 | Consequence | success, failure or partial progress changes the situation as intended | without it, actions do not matter |
| 6 | Repeat | the next round brings a changed problem, more skill, a social consequence or an expressive chance that fits the fantasy | repetition without change becomes a chore |
| 7 | Mastery | an advertised mastery goal says what can be learned and how improvement shows (or the record says why mastery is not central) | players need to see themselves get better |
| 8 | Variety | variation changes decisions or experience, not just labels and assets | reskinned variety does not hold attention |
| 9 | Promise | ordinary play delivers the title's action; record the real path and time | the title is a promise the first session must keep |
| 10 | Exit and return | the player can stop safely, knows what persists, has an honest reason to return without punishment | coercion destroys trust |
| 11 | Target conditions | evaluated on the intended device, input and solo or group setup | phones and groups change everything |
| 12 | Evidence | claims name build, cohort, sample, observation, uncertainty; FAIL FOR READINESS when no test exists | taste is not evidence |
