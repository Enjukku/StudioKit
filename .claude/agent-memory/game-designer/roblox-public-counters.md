---
name: roblox-public-counters
description: How to get a dated "why now" check for Roblox reference games without blogs (public games API, place→universe, omni-search)
metadata:
  type: reference
---

Roblox public GET endpoints (no sign-in) give a dated snapshot for pitch "why now" lines:
- `https://games.roblox.com/v1/games?universeIds=<ids>`: playing (concurrent, one moment), visits (entries, not people), created, maxPlayers, genre, official description.
- `https://apis.roblox.com/universes/v1/places/<placeId>/universe`: place id (the number in a roblox.com/games URL) → universe id.
- `https://apis.roblox.com/search-api/omni-search?searchQuery=<name>&sessionId=x&pageType=all`: finds universe and root place ids by name.

**Why:** in J003-T07 (2026-10-21) blog lists disagreed with official dates; the API description of each game was a better loop source than guides.
**How to apply:** cite the UTC sample time; say "one moment, not daily users"; note the hour (04:00 UTC is a quiet US hour). The kit's `tools/trends/roblox_collector.py` wraps the same routes once the trend scout exists. See [[pitch-craft-lessons]].
