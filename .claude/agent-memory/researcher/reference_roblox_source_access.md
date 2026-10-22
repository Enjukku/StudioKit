---
name: reference-roblox-source-access
description: How to read Roblox sources that block WebFetch (Help Center 403) and which mirror gaps need live reads
metadata:
  type: reference
---

- en.help.roblox.com article HTML answers HTTP 403. The JSON endpoint works: `https://en.help.roblox.com/api/v2/help_center/en-us/articles/<id>.json` (gives `updated_at`). Results are still a small-model extract.
- The docs mirror (`knowledge/external/roblox-creator-docs/`) prunes education pages (for example `education/developer/beta-testing-experiences`); read those live.
- Avoid reading whole `ad-integrations.md` or `README.md` of the mirror: country tables and page lists burn tokens. Use Grep or offset/limit.
- Existing fact-check files (`knowledge/reference/marketing/fact-check-roblox-*.md`) hold reusable FD/FA row ids; re-read the mirror lines before relying on them.
- Live `create.roblox.com/docs/reference/engine/classes/<Class>` returns only metadata tags through WebFetch (no prose). Use the upstream raw file `raw.githubusercontent.com/Roblox/creator-docs/main/content/en-us/reference/engine/classes/<Class>.yaml` to compare with the mirror (J006: Animator identical to mirror).
- Mirror has no page on animation asset permissions; the DevForum sharing posts (2025-05, 2025-08) are the only source. Animation docs live in `animation/` plus `ref/Animator.yaml`, `ref/AnimationTrack.yaml`; server-authority and Maya/emote import pages hold extra animation rules (J006 fact-check-roblox-runtime.md).
- Roblox Monetization page (`production/monetization/index.md:140-190`) holds the offer-presentation rules (genuine discounts, no false timers); easy to miss because the same page is cited only for the "weekly cadence" line.
