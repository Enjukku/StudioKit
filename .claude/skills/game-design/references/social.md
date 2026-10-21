> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Part of `game-design`. Sources: N4 §2 (multiplayer and social), FR (RC29-RC34), FI. Tags as in SKILL.md.

# Multiplayer and social design

## 1. Cooperation as structure
- Left 4 Dead built cooperation into enemies (rescue needs, separation punished through the fiction) and lowered coordination cost (resource sharing, automatic callouts); it rejected invisible leashes and teleporting stragglers (D12 E, FI).
- Design interdependence with understandable chances to help, never dependence that lets one player hold everyone hostage (O).
- Cooperation must stay understandable without open chat or voice: shared-state cues, readable help requests, a safe exit. Check friend joining, group separation, mixed progression and language differences in real setups. A social KPI is reviewed together with spam, exclusion, coercion and recovery, never optimized alone (N4 5.05 O).

## 2. Group lifecycle (8 stages, O)
Discover or join a friend → understand the shared goal → coordinate → contribute visibly → resolve differences → survive a mismatch or disconnect → finish → continue together or leave safely. Friendship value is not a party button. Test 6 conditions: mixed experience, late join, unequal unlocks, language differences, no voice, a player who wants to leave.

## 3. Competition and status (O)
- Demand both fair outcomes and understandable agency. Inspect: skill-estimate uncertainty, party advantage, role assignment, low-traffic population, rematches, match length, surrender, smurfing assumptions.
- Never guarantee close matches; never force losses in secret to raise retention; never claim matchmaking the system does not do. Riot frames matchmaking as a tradeoff of fair matches, preferred roles and queue time, with no single best queue length (D22 E).
- Status: say what is visible, to whom, and what it means (skill, generosity, creativity, tenure, identity, spending). Desirable status must be reachable without humiliating others or locking newcomers out. Visible purchase is not earned mastery.

## 4. Abuse (O)
- Tell agreed theft, deception or sabotage that the rules allow apart from targeted harassment and exploitation.
- Inspect: blocking, kicking, hostage-taking, unwanted contact, unfair resource loss, abusive trade.
- Pair every potentially harmful affordance with **prevention, visibility, recovery and a safe exit**. Muting must not make essential cooperation impossible. Reports and sanctions cannot repair incentives that reward antisocial play; prevention belongs in the game structure (Riot D23 E). New event incentives: check for kill stealing and competition between teammates.
- Concepts built on stealing or sabotage (e.g. *Steal a Brainrot*-style theft): prototype newcomer protection and comeback paths with the theft rule, not after it (game-concept case library).

## 5. Roblox audiences and chat (FR, checked 2026-10-20; recheck before launch)
| Fact | RC |
| --- | --- |
| Tiers: Kids 5-8, Select 9-15 (age-checked), Roblox 16+ | RC29 |
| Reaching under-16 players needs a verified creator, 2FA, a maturity rating, a fee or Plus/Premium, and 250 unique plays by highly engaged age-checked users within 60 days ("highly engaged" includes platform spend in the last 60 days); expedited review costs 50,000 Robux, refundable | RC30, FR |
| Chat is off by default for Kids and for self-declared Select users; access varies with tier, consent and region | RC31 |
| Intentional co-play days is a discovery signal; discovery is increasingly age-aware (2026-09-11) | RC32, RC33 |
| Offline solo play is planned for mid-2027 and is not available now; roadmap items are not capabilities | RC34 |

Design rule (O): a social game for young players must work with chat off. Communicate through the game (pings, emotes, shared goals, visible help), and check every social feature against `platform-policy`.
