---
name: web-access-quirks
description: Which policy and docs sites WebFetch can and cannot read (403s, redirects) and which workaround URLs worked, checked 2026-10-21
metadata:
  type: reference
---

Checked 2026-10-21 with WebFetch (returns a model extract, not raw text):

- Roblox help center (`en.help.roblox.com`: Terms of Use, Privacy Policy, Community Standards article, Creator Third Party App Policy) returns 403. `about.roblox.com/community-standards` is readable.
- DevForum topics are readable by appending `.json` to the topic URL (gives dates and staff flags per post). Plain topic URLs often return only the first posts.
- Discord: `discord.com/terms`, `/privacy`, `/guidelines` readable. `docs.discord.com/developers/events/gateway` and the privileged-intent review page are readable. Developer Terms and Developer Policy (`support-dev.discord.com`, and the `docs.discord.com/...policies-and-agreements` redirects) and `support.discord.com` articles return 403.
- `create.roblox.com/docs/cloud/llms.txt` lists Open Cloud feature groups and a "Not Available via API" list. It can disagree with the guides (it lists DAU as not available while the Analytics guide documents it).
- The local mirror lacks the Open Cloud scope table (generated from `openapi.json`).

Film and craft sources (checked 2026-10-21, J013-T07):
- Readable: dga.org DGA Quarterly pages, awn.com, skwigly.co.uk, awardsdaily.com, cartoonbrew.com, blog.syncsketch.com, blog.playstation.com, marclaidlaw.com, combineoverwiki.net (read with `offset` for pages over 100000 chars), gameanim.com, news.blizzard.com, disneyanimation.com, provideocoalition.com, theasc.com articles, nofilmschool.com, cined.com, adobe.com/creativecloud pages, edmundoptics.eu, rosetta.to, en.wikipedia.org.
- 403 or blocked: britishcinematographer.co.uk, filmmakermagazine.com, helpx.adobe.com, www.cambridgeincolour.com (use `cdn.cambridgeincolour.com` same path: works), edmundoptics.com (use `.eu`), techspot.com, amara.org SRT, filot.com, YouTube transcripts; `wired.com` is refused by the tool; web.archive.org is refused; hollywoodreporter.com is paywalled (402). A downloaded PDF cannot be read (no pdftoppm).
- Spoken YouTube lines (video essays) are usually unverifiable here; say so rather than guess.

Game-studio sites (checked 2026-10-21, J014-T05):
- Readable: playadopt.me, supercell.com (Brawl Stars, Clash Royale), support.riotgames.com, leagueoflegends.com, teamfighttactics.leagueoflegends.com, overwatch.blizzard.com, hearthstone.blizzard.com, gdcvault.com, nintendo.com/us/whatsnew, engadget.com, gematsu.com, gamingonlinux.com.
- Not readable: fortnite.com and epicgames.com (403), x.com (402), r.jina.ai (401), neowin.com and elevenforum.com (403). Script shells with no body: genshin.hoyoverse.com, bungie.net, dota2.com/news. minecraft.net timed out on every try.
- Workarounds that worked: Dota patch feed `https://www.dota2.com/datafeed/patchnoteslist?language=english` (versions with UTC timestamps) and `.../datafeed/patchnotes?version=7.41e&language=english`; Valve's Steam Community posts through `https://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=570&count=N&maxlength=0&enddate=<unix>`. Roblox game metadata: `apis.roblox.com/universes/v1/places/<placeId>/universe`, then `games.roblox.com/v1/games?universeIds=<id>` (has "updated").
- `playhearthstone.com` redirects (301) to `hearthstone.blizzard.com`.
- For studio posts, try the official feed or API before press, and say which text was actually read.

**How to apply:** for Terms-type clauses, say which text was actually read; do not fill 403 pages from search snippets.
