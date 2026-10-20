---
title: About GDPR and CCPA
description: Explains the General Data Protection Regulation and California Consumer Privacy Act.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/publishing/about-GDPR-and-CCPA.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/publishing/about-GDPR-and-CCPA.md). Published page: [https://create.roblox.com/docs/production/publishing/about-GDPR-and-CCPA](https://create.roblox.com/docs/production/publishing/about-GDPR-and-CCPA).

> [!warning] Not in the current upstream docs
> Not published in [github.com/Roblox/creator-docs](https://github.com/Roblox/creator-docs) as of 2026-10-20 (revision `74006430`). The closest current page is [[external/roblox-creator-docs/production/publishing/RTBF-and-creators]]. Kept locally so existing links keep working; read that page for current information.

<Alert severity="warning">
   The information below is provided for general informational purposes only and is not legal advice. If you have any questions about this information or your specific situation or rights, please contact an attorney.
</Alert>

## What is GDPR?

GDPR stands for the **General Data Protection Regulation**. The GDPR is a law in the European Union that focuses on protecting the personal information of everyone in the European Union and European Economic Area by guaranteeing specific rights to the collection, use, and sharing of their personal information. These rights extend beyond the territorial boundaries of Europe, such that many companies or individuals that collect EU personal information are subject to GDPR.

## What is CCPA?

CCPA stands for the **California Consumer Privacy Act**. This law provides rights to consumers who reside in California, USA, including knowing what information is collected about them, requesting a business to delete any personal information about a consumer from that consumer, and not to discriminate against a consumer if they exercise their privacy rights.

<Alert severity="warning">
<AlertTitle>What is personal information?</AlertTitle>

Most people associate the terms "personal information" or "personally identifiable information" (PII) as data like a name, email address, or home address. However, GDPR and CCPA have broader definitions for personal information which can also cover information that does not directly link to a specific individual, such as user IDs or IP addresses.

As a general rule, developers should **not** collect more personal information than what is supplied by Roblox, for instance the user ID and username for their players. For more information, see our [community rules](https://en.help.roblox.com/hc/en-us/articles/203313410-Roblox-Community-Rules).
</Alert>

## Impact on developers

As a developer, here are some ways to honor a player's rights under GDPR and CCPA:

- You may receive a message from Roblox regarding a **personal information deletion request**. Roblox takes special care to verify these requests to ensure that they're legitimate, so you should **only comply to requests from Roblox**. If a player contacts you first, please ask them to make the request at [https://www.roblox.com/support](https://www.roblox.com/support).
- Aside from user ID and username, do **not** store other forms of personal information such as birth dates or personal photos.
- If you're **asked by Roblox** to delete personal information about an individual who has exercised their right under GDPR or CCPA, you may need to delete specific data from your experience's [[external/roblox-creator-docs/cloud-services/data-stores/index|data stores]].
- If you have already stored other personal information beyond what Roblox provides access to, remove it and update your experience so that it doesn't store that data in the future.


## Related Files

- [[external/roblox-creator-docs/production/publishing/accessibility]] - Accessibility guidelines.
- [[external/roblox-creator-docs/production/publishing/account-verification]] - Account verification.
- [[external/roblox-creator-docs/production/publishing/adaptive-design]] - Adaptive design guidelines.
- [[external/roblox-creator-docs/production/publishing/badges]] - Badges.
- [[external/roblox-creator-docs/production/publishing/console-guidelines]] - Console development guidelines.
- [[external/roblox-creator-docs/production/publishing/publish-experiences-and-places]] - Create and publish experiences and places.
- [[external/roblox-creator-docs/cloud-services/data-stores/index]] - Data stores.
- [[external/roblox-creator-docs/production/publishing/dmca-guidelines]] - DMCA guidelines.
- [[external/roblox-creator-docs/production/publishing/descriptions]] - Experience descriptions.
- [[external/roblox-creator-docs/production/index]] - Production.
