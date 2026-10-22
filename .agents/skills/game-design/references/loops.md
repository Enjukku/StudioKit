> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: DS (four parts, name the fun, goals vs tactics; Riot transcripts 2026-10-15), N3 §2 (loops, scales, coupling, prototype gate, core-loop check), FI (prototype counts). Tags as in SKILL.md. Revised by J018 maker game-designer · claude-opus-5-5 · high · 2026-10-22: built also from the owner's Riot transcripts (J018) (four parts one line each, plain-block test, crudest prototype, verdict before art, feedback and promise items in the check).

# Loops: what repeats, what changes, what persists

## 1. Four parts of a game (DS §1)
| Part | Question | Missing means |
| --- | --- | --- |
| Goal | what is the player trying to do now, this session, long term? | aimless play |
| Opposition | what stands in the way? | no challenge, no satisfaction |
| Decisions | which meaningful choices get past it? | a toy or a cutscene |
| Rules | what framework governs it, consistently? | confusion, unfairness |

Every loop, mode, boss and mini-game spec states all four, one line each. An empty or vague "decisions" line is a finding: without a choice that gets past the opposition, it is an activity, not a game (eating cereal vs tennis). Each obstacle in the opposition line names the counter tool or skill that beats it.

Not every moment must be a hard choice: social, expressive, contemplative or comfortable play can keep a different promise (Koster D25 O vs Sylvester D26 O; N3 §3.3).

## 2. Name the fun (DS §2)
Pick one or two target experiences per feature, written down: living a fantasy (power, role) · thrill and sensation · fellowship and team play · mastery · exploration and discovery · creativity and expression · collection and completion · competition and status · comfort and routine. Art, design and engineering aim at the same target. Separate the **goal** ("feel huge power when the tower falls") from the **tactics** ("rocket damage ×2"); agree the goal first, then compare tactics against it.

"Fun" is not a target: a brief that says "make it fun" is sent back. Every proposed addition (a story layer, a cutscene, a second currency, a social feature) answers "which named target experience does this serve?"; one that serves another kind of fun is filed as a proposal, not built, because mixed kinds of fun pull the crafts apart. Roblox games are often social, so fellowship is a common second target; write it down when it is one.

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

- **Crudest form first.** Build only the exciting part, in the simplest way that answers the question: paper and cards for a system, plain Studio Parts and a short script for feel ("this red block deals damage"). Stand-ins use a colour and shape nobody can mistake for final art. Paper can feel more fun than a phone build (a false positive): confirm feel in Studio on the target device before the verdict.
- **Verdict before art.** Write the play-test verdict (PASS / FAIL / Unproven, with the observations) in the job folder before any production art brief for that mechanic; every art, VFX and model brief cites it. Reference images may come earlier: they are cheap targets, not production.
- Test feel separately from long-term aspiration when needed, then together: a paper economy cannot show motor feel; a polished combat room cannot show a month-long economy.
- **PASS:** the build can answer the risky question and the team named a result that would change or drop the idea.
- **FAIL:** success defined as "testers liked it"; the only test is the designer playing well; every disappointing result blamed on missing polish without evidence.
- Signs of promise (triangulated, never one metric): players understand an immediate intention; actions have readable consequences; alternatives respond to context; players find or state a better strategy; repeats differ meaningfully; the intended audience continues when free to stop. Confounds: novelty, politeness, rewards for testing, no alternative available.
- Scoped history, not quotas: Splatoon picked a prototype from 70 ideas and already played 4 vs 4; Wonder gathered 2,000+ sticky-note ideas; Supercell cancelled nine games during Clash Royale's development (2016 lecture; the paper's "1 release in 2 years" framing was not found, FI IC56) and counted 5 hits vs 30+ killed (2023). None sets a prototype quota or kill rate (N3 §2.4; verdicts FI). Keep the tested interaction when presentation changes: Splatoon's character and arena changes temporarily broke what ink and hiding meant (D03 E).

**5b. Plain-block test (behaviour read).** Before art, run each new enemy, object or ability as plain blocks in Studio (studio-operator capture): a tester who has not read the spec says what the thing is, what it does and how dangerous it is from its behaviour alone (a block that hops is a frog; one that dashes and stops is a ninja; one that slowly expands and vanishes is a bomb). Enemies of different types are told apart by movement alone. A miss means the behaviour (pattern, radius, speed, timing) is changed first; art may only reinforce a behaviour, never invent one. Tester: a play-test participant, or a fresh-context subagent given only the capture frames.

## 6. Core loop check (12 items, N3 §2.8 O)
Mark each **Pass / Fail / Unproven**. A readiness failure (no test yet) is not an observed design failure; store the verdict and its reason. Reasons are this kit's (the paper gives none, N3 W07).
| # | Item | Pass when | Why it matters |
| --- | --- | --- | --- |
| 1 | Goal | the player can state or show an immediate objective without help | no goal, no reason to act |
| 2 | Action | an input changes relevant state and the player links it to the goal | otherwise the loop is a toy |
| 3 | Choice | choices serve the intended strategy, expression, social play or comfort; cosmetic variety is not depth | choices are where the player's skill and taste show |
| 4 | Feedback | under target conditions the player sees what happened, why, and what to do next; every input answers at once, the big layer waits for the confirmed outcome, failure and refusal have their own cue | unreadable cause and effect feels unfair; a celebration before the result lies |
| 5 | Consequence | success, failure or partial progress changes the situation as intended | without it, actions do not matter |
| 6 | Repeat | the next round brings a changed problem, more skill, a social consequence or an expressive chance that fits the fantasy | repetition without change becomes a chore |
| 7 | Mastery | an advertised mastery goal says what can be learned and how improvement shows (or the record says why mastery is not central) | players need to see themselves get better |
| 8 | Variety | variation changes decisions or experience, not just labels and assets | reskinned variety does not hold attention |
| 9 | Promise | ordinary play delivers the title's action; record the real path and time; what things look like matches what they do | the title is a promise the first session must keep; a look that lies breaks prediction |
| 10 | Exit and return | the player can stop safely, knows what persists, has an honest reason to return without punishment | coercion destroys trust |
| 11 | Target conditions | evaluated on the intended device, input and solo or group setup | phones and groups change everything |
| 12 | Evidence | claims name build, cohort, sample, observation, uncertainty; FAIL FOR READINESS when no test exists | taste is not evidence |
