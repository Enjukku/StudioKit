> Author: J018 maker vfx-designer · claude-opus-5-5 · high · 2026-10-22. Part of `vfx-design`; built also from the owner's Riot transcripts (J018). Numbers marked PROPOSAL are starting values a check may change; the game-designer's read rank, the game profile or the owner may replace them.

# The read card: what the effect must say, before any layer

Fill it at `vfx-design` §2 step 1. It is §1 of `content/vfx/<effect-id>/brief.md`; the frame script and `spec.json` follow from it. Every field holds a value, UNKNOWN with its owner, or "n/a" with a reason. Self-review lines PL-01 to PL-07 (`review.md` §I1) check it.

## 1. Fields
| Field | Holds | Source |
| --- | --- | --- |
| Job | what it is, what it does in play, how big (tiny, normal, big, rare) | brief, feature spec |
| Verb | the mechanic verb (slows, stuns, heals, knocks back, collects, warns), the same word as the timing list and the sound cue card; the effect moves like it (a slow decelerates and spreads, a stun snaps) | animator's timing list, game-designer |
| Three read lines | **shape:** help or harm (sharp, angular, spiky = harm; round, plus = help; circle = shield; outward, aimed or inward), in the game's shape vocabulary; when the art bible names a motif for the caster or the release, it appears at big, medium and small scale, built from a few basic shapes, never pasted as a literal symbol; **colour:** the role from the art bible's colour-role table, plus the caster's main hue; **timing:** each stage's start in seconds on the timeline's stage names (load, charge, release, travel, impact, tail) | art bible: Shape vocabulary (the effect shape code), Colour roles, Reserved colours, Theme libraries (motifs), Tier and format exceptions; event timeline |
| Three reads | **primary** = the gameplay core (where it is, what it hits) and its focus point (the casting hand, the projectile's head, the contact point, the danger edge); **secondary** = the theme ("this is frost"), clearly weaker; **tertiary** = a few small supporting bits | me |
| Importance | 1-10 for self, other (not threatened) and threatened; the loudness tier (§2); what it outranks and what it yields to | me, with the game-designer's read rank |
| Attempt and outcome | what plays on the input (small, on the client, on the press frame or the next) and what waits for the confirmed event (its source: server event or replicated state); the outcome tiers (miss, blocked, hit, big hit; sale sizes; rarity tiers) and the learnable cause that grades them; no reward effect before its trigger | feedback stack; reward tier table |
| Truth | each value (shape, radius, fuse, contact time, active end) with its data field; "visual only" when nothing is attached | config; threat or hazard sheet |
| Information areas | what must stay visible from this camera: other players, the HUD zones, targets, the shop and placement areas, the smallest gameplay object on the floor; the effect's maximum height in studs; for ambient effects the distance to the nearest sight line and route | read rank, game profile; ambience map (moving-things list) |
| Rate | expected rate and burst; for frequent effects the merge window, the live-copy cap, particles per copy | feedback stack; reward effects: the progression designer's tier table (tier, trigger, measured rate per event) |
| Per viewer | what the self, a bystander and the threatened player see; LocalTransparencyModifier level for others' non-threat layers | me |
| Reduced | the off path of every intense channel and what it keeps: a flash becomes a steady shape, a blink a steady glow with a fill countdown, shake none, FOV punch and push-ins none | me |
| Budget | unique textures, emitters, est. live particles at peak, lights; what the lowest tier drops (decoration only, never a truth layer) | `vfx-craft/references/pro-defaults.md` §C |
| Context and technique | gameplay moment, world event, object change, cutscene or UI; the tool per part | `vfx-design` §3 |
| Joining crafts | animator (markers, the freeze frame), sound (envelope), UI (world-to-HUD), builder (the test hooks by the names in `vfx-craft/references/measure.md` §1 Builder hooks), architect (the presentation contract rows, gameplay features) | me |
| Stop criteria and pass budget | the §I lines that must pass to stop; build passes and capture rounds allowed | brief, me |

## 2. Loudness tiers (PROPOSAL starting caps)
| Tier | Typical | Importance | Peak footprint at the game camera | Near-white | Visible length | Camera and screen |
| --- | --- | --- | --- | --- | --- | --- |
| T1 ambient | dust in light, embers, fireflies, torch flames | 1-2 | small, low, partly hidden; never the brightest or fastest thing near a sightline | none | long and slow; fades in and out | none |
| T2 frequent feedback | hit spark, pickup, footstep dust, coin, muzzle flash | 2-4, or any effect playing about once a second or more | about one character width (4-6 studs) | only the contact flash (0.03-0.05 s, about 0.5 % of the screen or less, at the contact point) and a target's brightness flash | tail ≤ 0.5 s; same-kind events merge inside about 100 ms | none |
| T3 ability or event | heavy hit, blast, slash, area attack, level-up | 4-7 | ≤ about 20 % of the screen | ≤ 2 frames, on the focus | ≤ about 1.5 s; sight-blocking dust see-through by about 2 s | none by default; a small shake only on a rare heavy hit when the owner allows |
| T4 rare top | ultimate, boss blast, finisher, legendary reveal | 8-10 | ≤ about 50 % for ≤ about 1 s | a pure-white core for 1-2 frames | up to about 3 s, plus the dust clear-by | rotation shake, FOV punch, grade pulse (`camera-and-screen.md`) |
Coverage comes from the frame-folder numbers (`vfx-craft/references/measure.md` §2) at the game camera; studs to screen %: `vfx-craft/references/plan-and-spec.md` §B. A threat uses the threatened player's tier for the threatened player even when the caster's own tier is lower. Only the top tier may fill the screen.

## 3. Worked card: ground slam (battlegrounds game, third-person camera about 14 studs behind and above)
| Field | Value |
| --- | --- |
| Job | a heavy enemy's ground slam; damages everyone inside a circle at contact; big |
| Verb | knocks back: the result drives outward and up, hard and short |
| Three read lines | shape: a jagged ring racing out from the fists, spikes pointing up and out = harm; colour: the enemy-ability role (art bible), next to the enemy's orange; timing: `tell_start` 0.00 s, charge 0.00-0.80 s, beat 0.80-0.90 s, `contact_candidate` 0.90 s, result 0.90-1.40 s, tail to 2.40 s |
| Three reads | primary: the danger ring on the ground at the true radius, from tell to the last tick (focus: the ring edge; at contact the fists); secondary: rock and dust theme (cracks, rubble ring); tertiary: a few pebbles and sparks |
| Importance | self n/a (an enemy); other 4; threatened 9 → T4 for the threatened player, T3 for bystanders |
| Attempt and outcome | the tell and the ground impact play on the enemy's timeline (the impact on `contact_candidate`); the hit layer on a player who was inside (a brightness flash on them, knock-back streaks) waits for `contact_confirmed`; a cancelled slam collapses the ring in 100 ms and plays no impact |
| Truth | radius `SlamConfig.radius` (12 studs), telegraph `SlamConfig.telegraphLead` (0.9 s), active end `SlamConfig.activeEnd` (0.95 s); the ring is removed at 0.95 s; the dust stop line equals the radius |
| Information areas | the threatened player's character; the health bar bottom-left; other enemies' tells; maximum height 6 studs (spikes inside the ring only). The ring edge is this effect's own primary: its dust and spikes stop at it (Truth), checked on the layer stills, not by the cover test |
| Rate | once per 6 s per boss, at most 3 bosses; no merge |
| Per viewer | threatened: everything full, rotation shake on contact within 1× radius falling to 0 at 3×; bystander: ring full (they can walk in), dust and spikes at LocalTransparencyModifier 0.5, no shake |
| Reduced | shake none; the contact flash becomes a steady bright ring edge for 0.2 s; the ring keeps its fill countdown |
| Budget | 8 unique textures, about 20 emitters, about 400 live particles at peak, 1 PointLight; the lowest tier drops pebbles, sparks and the second dust layer |
| Stop criteria | PL, BL, VS, CP, SP and IG lines pass or are owner-waived; 2 build passes, 2 capture rounds |
| Options (§2 step 4) | A "cracking ring" (cracks race out to the radius at contact); B "rising spikes" (spikes erupt along the edge); C atypical "inward suck" (dust pulled into the fists during the charge). Goal question: "which tells the threatened player at phone size where it hurts and when?" A wins (the edge is the read); C becomes the build (converging dust); B loses (spikes hide the edge from a low camera) |

## 4. Worked card: coin pickup (simulator, frequent)
| Field | Value |
| --- | --- |
| Job | a coin is collected; tiny |
| Verb | collects: motion goes from the coin to the counter |
| Three read lines | shape: round pop and a few sparkles = friendly; colour: the reward-gold role; timing: pop 0-80 ms, shrink to the chip 80-220 ms, tick on credit |
| Three reads | primary: the pop at the coin; secondary: the streak toward the backpack chip; tertiary: 3 sparkle specs |
| Importance | self 2, other 1, threatened n/a → T2 |
| Attempt and outcome | the pop on touch (client); the chip tick and "+N" on the server credit; a refused pickup (backpack full) shows the full icon at the chip, no pop |
| Truth | visual only (no area) |
| Information areas | other players, threats, the HUD counter's digits (the streak ends at the chip's edge; the landing and the tick are UI's, on one beat list); height under 2 studs |
| Rate | up to 20 per second with a magnet; merge window 100 ms; at most 8 live copies, at most 10 particles each |
| Per viewer | others' pickups at LocalTransparencyModifier 0.5 or hidden at "essential" clarity |
| Reduced | no intense channel; nothing changes |
| Budget | 1 shared texture, 2 emitters, ≤ 10 particles per copy |
| Stop criteria | the 100-trigger repeat and the burst run pass (IG-09); the count ends exact |
