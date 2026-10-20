---
title: RTBF and creators
description: Explains the right to be forgotten and its impact on creators.
tags: [roblox, documentation, external-reference, priority-reference, production]
keywords:
  - GDPR
  - CCPA
  - LGPD
  - PIPA
  - right to erasure
  - right to be forgotten
  - data protection
  - privacy
  - PII
  - personal data
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/publishing/RTBF-and-creators.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/RTBF-and-creators.md). Published page: [https://create.roblox.com/docs/production/publishing/RTBF-and-creators](https://create.roblox.com/docs/production/publishing/RTBF-and-creators).

<Alert severity="info">
<AlertTitle>What is RTBF?</AlertTitle>
RTBF stands for the **right to be forgotten**, a principle in global privacy law that gives individuals the right to request the deletion of their personal data when it is no longer necessary. Honoring RTBF requests is a legal obligation for data controllers and is critical to maintaining user trust and regulatory compliance.
</Alert>

Global privacy regulations create rules for "controllers" of data, a term that means individuals or organizations that determine why and how data is processed. Privacy rules typically define "personal data" or Personally identifiable information (PII) broadly. It encompasses any information that relates to an identified or identifiable living individual. If a piece of data can be traced back to an individual user, it may be personal data subject to privacy regulations.

A fundamental principle across global frameworks is that controllers should not retain personal data indefinitely. Similarly, users can request the deletion of data that is no longer necessary. If a user requests that Roblox permanently delete their Roblox account, Roblox notifies creators so they can delete information that is no longer needed. The primary rule governing deletion is that personal data must be permanently erased after there is no longer a valid legal or business basis for processing it.

## RTBF notifications and automation

When an RTBF request affects one or more of your games, Roblox helps you identify and process the request in the following ways:

- **Roblox messages** — Roblox sends an automated message each day to your inbox that lists the RTBF requests requiring action and the affected games.
- **Automated data store deletion** — If you configure RTBF deletion templates for a game, Roblox uses them to automatically delete matching keys and data stores when it processes a request. For setup instructions, see [[external/roblox-creator-docs/cloud-services/data-stores/right-to-be-forgotten|Data store right to be forgotten (RTBF)]].
- **Creator webhooks** — If you configure a webhook with the **Right to Erasure Request** trigger, Roblox automatically invokes it for affected games. You can use the request payload in your own automation to delete personal data. For setup instructions and a sample workflow, see [[external/roblox-creator-docs/cloud/webhooks/automate-right-to-erasure|Automate right to erasure using webhooks]].

For automation, first use automated data store deletion for supported data. Use a creator webhook for more complex cases, such as custom deletion logic, data store schemas that RTBF deletion templates don't support, or personal data stored outside of data stores.

<Alert severity="warning">
Roblox always sends the daily RTBF message for affected games, regardless of whether you configure automated data store deletion or a creator webhook. You remain responsible for permanently deleting all personal data covered by an RTBF request. Review the daily message and verify that data outside configured templates or custom automation is also deleted.
</Alert>


## Related Files

- [[external/roblox-creator-docs/production/publishing/accessibility]] - Accessibility guidelines.
- [[external/roblox-creator-docs/production/publishing/account-verification]] - Account verification.
- [[external/roblox-creator-docs/production/publishing/adaptive-design]] - Adaptive design guidelines.
- [[external/roblox-creator-docs/production/publishing/badges]] - Badges.
- [[external/roblox-creator-docs/production/publishing/console-guidelines]] - Console development guidelines.
- [[external/roblox-creator-docs/production/publishing/publish-games-and-places]] - Create and publish games and places.
- [[external/roblox-creator-docs/production/publishing/dsa-ip-reporting]] - EU DSA IP infringement reporting.
- [[external/roblox-creator-docs/production/publishing/descriptions]] - Game descriptions.
- [[external/roblox-creator-docs/production/publishing/experience-genres]] - Genres.
- [[external/roblox-creator-docs/production/publishing/experience-icons]] - Icons.
- [[external/roblox-creator-docs/production/publishing/ip-guidelines]] - Intellectual Property Guidelines.
- [[external/roblox-creator-docs/production/publishing/rights-manager]] - Rights Manager.
- [[external/roblox-creator-docs/production/publishing/kids-and-select]] - Roblox Kids and Select.
- [[external/roblox-creator-docs/production/publishing/thumbnails]] - Thumbnails.
- [[external/roblox-creator-docs/production/publishing/vr-guidelines]] - VR guidelines.
