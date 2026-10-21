---
type: job
scope: universal
status: active
updated: 2026-10-21
source: "J014 synthetic test data (test-pack/game.md)"
supersedes: []
---
SYNTHETIC TEST DATA (J014-T07). Not a real game, not real players.

# Mothlight Meadow: game page (invented game, state on 2026-10-20 23:59 UTC)

| Field | Value |
| --- | --- |
| Genre | Cozy collection and upgrade game |
| Launched | 2026-09-29 (Tuesday) |
| Experience guidelines label | Mild. Kids (5-8) and Select (9-15) accounts can play |
| Platforms | Phone (most players), PC, tablet, console |
| Build live now | 1.1.1 (2026-10-13 16:00 UTC) |
| Team | Owner (creative director) and the studio's AI roles. One builder lane, see `capacity.md` |

## 1. Core loop
1. Walk the meadow at dusk. Moths fly around lanterns.
2. Swing the net at a moth (tap or click) to catch it.
3. Drop the caught moth in the Jar. The Jar pays Glow Dust.
4. Spend Glow Dust on lantern upgrades, net upgrades and zone gates. Better lanterns bring rarer moths.
5. Fill the Moth Book. Moths shown in your Terrarium pay a small amount of Glow Dust every minute, also while you are away (up to 8 hours).

A normal session is 6 to 12 minutes. Players visit a friend's Grove to look, but there is no trading and no shared catching.

## 2. Tutorial (first session)
| Step | What the player does |
| --- | --- |
| 1 | Swing the net and catch the first moth |
| 2 | Drop the moth in the Jar and receive the first Glow Dust |
| 3 | Take a lantern from the Satchel and place it on a Lantern Post in the Grove (build mode) |
| 4 | Buy the first lantern upgrade, then free play |

## 3. Systems
| System | What it is |
| --- | --- |
| Moth Book | 54 moths in 5 rarities (Common, Uncommon, Rare, Epic, Mythic). Plus 6 Parade moths that could only be earned during the Lantern Parade |
| Lanterns | Placed on Lantern Posts. Each upgrade level raises the rare-moth chance. 8 levels |
| Terrarium | Display shelves. Shown moths pay Glow Dust per minute. The Terrarium Shop (Dust prices) sells shelves, decorations and moth dyes |
| Zones | 4 zones, see section 4 |
| Dusk Board | A wooden board in the Grove hub. 3 daily quests, plus the quest chains that open Zone 3 and Zone 4. It is a world object; there is no menu shortcut for it |
| Dewdrop Crate | A paid random item, see section 6 |
| Spark Swap | A stall in the Parade Plaza that turns Parade Sparks into Glow Dust, see section 7 |
| Friends | Visit a friend's Grove. No trading, no gifting, no shared catching |

## 4. Zones
| Zone | Gate | Notes |
| --- | --- | --- |
| 1. Meadow Edge | Start zone | Common and Uncommon moths |
| 2. Reed Pond | 1,500 Glow Dust at the gate post | Rare moths. The Parade Plaza is on the east shore. The pond frogs are scenery |
| 3. Old Orchard | 6,000 Glow Dust and the Dusk Board chain "Light the three Beacons" | Epic moths |
| 4. Hollow Cave | Dusk Board chain "Find the Cave Key" (needs the Orchard) | Mythic moths, including the Moonmoth |

## 5. Currencies
| Currency | How you get it | What it buys | Notes |
| --- | --- | --- | --- |
| Glow Dust | Catching, Jar, Terrarium, Dusk Board, Spark Swap | Lantern and net upgrades, zone gates, Terrarium Shop items | Soft currency. No cap |
| Starlight Beads | Bought with Robux (packs below). A few from the Dusk Board | Dewdrop Crate, cosmetics, skip timers | Hard currency |
| Parade Sparks | Lantern Parade only (2026-10-09 to 2026-10-13) | Parade shop, Spark Swap | Event currency. No expiry rule was written |

Starlight Beads packs (developer products):
| Pack | Beads | Robux |
| --- | --- | --- |
| Small | 100 | 49 |
| Medium | 280 | 129 |
| Large | 650 | 299 |

## 6. Dewdrop Crate (paid random item)
| Field | Value |
| --- | --- |
| Price | 50 Starlight Beads per open (Beads come from Robux) |
| Drop table (design sheet, sums to 100.0 %) | Common 62.0 %, Uncommon 28.0 %, Rare 8.5 %, Epic 1.3 %, Mythic (Moonmoth) 0.2 % |
| Odds display | The odds are listed on the crate's info panel, opened with the "i" button |
| Policy gate | Shown only where PolicyService allows paid random items. Other players see the Moth Cabinet (fixed price) |

## 7. What shipped, and when
| Build | Date (UTC) | Content |
| --- | --- | --- |
| 1.0.0 | 2026-09-29 | Launch: 4 zones, 54 moths, Terrarium, Dusk Board, Dewdrop Crate, Beads packs |
| 1.0.2 | 2026-10-02 | Net hitbox fix. Tutorial step events added to analytics |
| 1.1.0 | 2026-10-08 | Lantern Parade event content, 6 Parade moths, the "Tell us" in-game feedback form |
| 1.1.1 | 2026-10-13 16:00 | Parade closed. Terrarium saves now batched every 60 seconds. The Spark Swap stall stays in the Plaza (no end date in its config) |

### The Lantern Parade (week-2 event, finished)
| Field | Value |
| --- | --- |
| Dates | Start 2026-10-09 15:00 UTC, gameplay end 2026-10-13 15:00 UTC (4 days) |
| Entrance | Parade Plaza on the east shore of Reed Pond |
| Activity | Catch Parade fireflies and float-lanterns to earn Parade Sparks. A 12-stage reward track |
| Rewards | Cosmetics and 6 Parade moths from the Parade shop (Sparks). All deterministic, none paid |
| Spark Swap | 10 Sparks give 150 Glow Dust. Open the whole time since 2026-10-09 |
| Marketing | One announcement in the game and one post on the community server |

## 8. What is live now (2026-10-20)
- Build 1.1.1, all four zones, the Dusk Board, the Dewdrop Crate, the Beads packs, the Spark Swap stall.
- The Parade shop and the Parade moths are gone.
- Feedback routes: the Roblox rating prompt (Creator Hub export), the Discord forum channel "feedback", the in-game "Tell us" form (since 1.1.0).
- Committed work: a Reed Pond performance pass for phones (see `capacity.md`).
