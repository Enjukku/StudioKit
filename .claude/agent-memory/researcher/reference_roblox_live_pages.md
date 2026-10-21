---
name: reference-roblox-live-pages
description: Where Roblox Open Cloud analytics/experiments rate limits and stability labels live (not in the local mirror) and WebFetch quirks seen in J013-T01
metadata:
  type: reference
---

The docs mirror (rev 7400643, 2026-10-20) has no `cloud/reference/features/*` pages. Rate limits, Beta/Experimental labels and calculateMde exist only live: `https://create.roblox.com/docs/cloud/reference/features/{analytics,experiments,virtual-events}.md` (fetchable, carry a last-updated stamp). `https://create.roblox.com/docs/cloud/llms.txt` lists the feature pages.

WebFetch of live docs and DevForum returns a model extract, so exact post wording cannot be proven; say "extract". Extracts can omit lines the mirror has (e.g. matchmaking 3-variant limit): prefer mirror raw text when both exist.

Used in: knowledge/reference/analyst/01-roblox-platform-facts.md (J013-T01, 2026-10-21).
