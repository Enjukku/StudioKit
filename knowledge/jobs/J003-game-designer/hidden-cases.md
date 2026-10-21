---
type: job
scope: universal
status: active
updated: 2026-10-20
source: J003
supersedes: []
---
> Author: extractor · claude-sonnet-5-5 · high · 2026-10-20

Source: `Game_Designer_Part_1_Research.txt`, lines 252-264 (cases 16-18) plus registry entries R19, R22, R23, R26, R27, R28. Paraphrased; the paper stays outside git.

# Held-out cases 16-18 (test set for the game-concept skills)

Use rule: these three cases are a held-out test set. A skill must not be built from them and a builder must not read the answer key. Give an agent under test only the "Given to the agent" block. A grader compares the agent's pitch against the answer key. Nothing here is in `knowledge/reference/game-design/01-ideation-hook.md`.

Reading rule for the grader: the evidence lines keep the paper's tags (VERIFIED, EXPERIENCE, OPINION) and source IDs. The seven field rows are OPINION (analytical proposals by the paper, GP1:80), not facts about the real pitch. Cite as `GP1:<line>`.

## Case 16 Dead Rails (GP1:252-254)

### Given to the agent

Dead Rails is a multiplayer Roblox game made by a studio called RCM Games. Players, usually with friends, board a train and ride it through a desert that is full of zombies. The train stops at places along its route. At each stop players gather resources and defend against threats, then get back on and depart. The journey's stated end is a cure.

### Answer key (grader only)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox reports one million concurrent users in March 2025. RCM Games describes a train expedition through a zombie-infested desert toward a cure. The evidence does not isolate the train's effect on growth | VERIFIED | R19, R26 |
| fantasy and promise | Keep a vulnerable expedition moving through danger | OPINION | - |
| curiosity and stakes | What lies at the next stop, and what must be risked to continue? | OPINION | - |
| first image | A shared train cutting through a hostile landscape | OPINION | - |
| loop and twist | Travel, stop, gather, defend and depart. A moving base joins survival, route choice and cooperation | OPINION | - |
| shareable moment | A last-second boarding or rescue | OPINION | - |
| smallest version | A train, a meaningful stop, a resource tradeoff and a threat that makes departure consequential | OPINION | - |
| transfer | Let one tangible object organise several compatible design jobs | OPINION | - |

## Case 17 Dress to Impress (GP1:256-258)

### Given to the agent

Dress to Impress is a multiplayer Roblox game. In each round players are given a theme. They build an outfit from a wardrobe, pose, and walk a runway where the other players see them. Players then vote on the outfits. Rounds repeat with new themes.

### Answer key (grader only)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox's 2023-12-22 year review reports more than 40 million visits in two months. Visits are not unique players and not current traffic. The creator description combines outfit creation, posing, runway presentation and voting | VERIFIED | R22, R27 |
| fantasy and promise | Make a look that other people notice and interpret | OPINION | - |
| curiosity and stakes | How will this theme become my style, and how will an audience react? | OPINION | - |
| first image | A personally assembled outfit on a runway | OPINION | - |
| loop and twist | Create, present, receive social feedback, and reinterpret the next prompt | OPINION | - |
| shareable moment | A reveal that communicates an unexpected idea | OPINION | - |
| smallest version | A usable wardrobe, an expressive theme, a presentation space and understandable feedback | OPINION | - |
| transfer | Connect creation to an audience, while testing fairness and room for non-conforming expression | OPINION | - |

## Case 18 Blue Lock Rivals (GP1:260-262)

### Given to the agent

Blue Lock Rivals is a Roblox soccer game. Two teams of five play each match. Players have classes and powers that they use during the match while they play for their team.

### Answer key (grader only)

| row | content | tag | source IDs |
| --- | --- | --- | --- |
| evidence | Roblox reported over four billion visits in its 2025-11-11 licensing announcement. The live listing describes 5v5 soccer with classes and powers and states License Manager permission, without claiming that the author supervised the work | VERIFIED | R23, R28 |
| fantasy and promise | Become an exceptional football rival through a conspicuous personal ability | OPINION | - |
| curiosity and stakes | Can my role create the decisive play? | OPINION | - |
| first image | A recognisable goal attempt changed by a readable special power | OPINION | - |
| loop and twist | A familiar team sport gains character-specific tactical options | OPINION | - |
| shareable moment | A coordinated or individual reversal at the goal | OPINION | - |
| smallest version | Understandable sport rules plus a differentiated ability layer and fair feedback | OPINION | - |
| transfer | Use the familiar grammar to explain the new decision. The example gives no right to reuse its franchise, branding or expression | OPINION | - |

## Grader notes: weak spots in the key

Observations only. They do not change the key.

| id | place | observation |
| --- | --- | --- |
| HW1 | Case 16 | The registry excerpt for R19 is about 21.6 million simultaneous users, dated 2025-06-24. The paper cites R19 for one million concurrent users in March 2025. The excerpt does not show that figure or name the game |
| HW2 | Case 17 | The 40 million visits come from a CEO year-in-review letter (R22). The registry excerpt does not name the game and does not give the start date of the two months |
| HW3 | Case 18 | "Over four billion visits" does not say whose visits (the game, the platform, or the licence programme). The R23 registry excerpt is only the game title. The license-manager statement is in the paper's text, not in the R28 excerpt |
| HW4 | Cases 16-18 | The evidence in each case is concurrency or visits, which are reach numbers. The paper does not tie any of them to retention or to the concept |
| HW5 | Given blocks | The "Given" paragraphs were built only from the paper's evidence sentences and the loop wording in the key. They add no facts. Words such as "usually with friends" and "a theme" come from the R26 listing excerpt and from the key's "next prompt" and "this theme" |

## Numbers in this file (for the fact-check ticket)

| # | claim | GP1 | source IDs |
| --- | --- | --- | --- |
| HF1 | One million concurrent users, March 2025 | 253 | R19, R26 |
| HF2 | More than 40 million visits in two months; review dated 2023-12-22 | 257 | R22, R27 |
| HF3 | Over four billion visits; announcement dated 2025-11-11; 5v5 soccer | 261 | R23, R28 |

## Sources for the key

Titles are the registry's, with its stripped punctuation shown as " - ". None of these entries has a scope line in the registry.

| id | title; issuer | date (registry) | registry tag | URL |
| --- | --- | --- | --- | --- |
| R19 | The Infrastructure Supporting Record Breaking Experiences; Roblox | 2025-06-24 | VERIFIED | https://about.roblox.com/newsroom/2025/06/roblox-infrastructure-supporting-record-breaking-games |
| R22 | 2023 Year in Review - A Letter From Our CEO; Roblox | 2023-12-22 | VERIFIED | https://about.roblox.com/newsroom/2023/12/2023-year-review-letter-ceo |
| R23 | Roblox Launches Self Serve IP Licensing; Roblox | 2025-11-11 | VERIFIED | https://about.roblox.com/newsroom/2025/11/roblox-self-serve-ip-licensing |
| R26 | Dead Rails - official RCM Games listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/116495829188952/Dead-Rails |
| R27 | Dress to Impress - official creator game listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/15101393044/Dress-To-Impress |
| R28 | Blue Lock - Rivals - official game listing; Roblox | Live listing accessed 2026-10-21 | VERIFIED | https://www.roblox.com/games/18668065416/Blue-Lock-Rivals |
