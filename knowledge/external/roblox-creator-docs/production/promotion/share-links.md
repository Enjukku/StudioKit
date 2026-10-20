---
title: Share links
description: How to create and use share links to promote your games and track acquisition metrics.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/promotion/share-links.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/promotion/share-links.md). Published page: [https://create.roblox.com/docs/production/promotion/share-links](https://create.roblox.com/docs/production/promotion/share-links).

Share links are unique and trackable links that generate metrics that allow you to track and grow your off-platform user acquisition. You can also use custom `Class.Player:GetJoinData()|LaunchData` to provide in-game perks to users that join through your share link.

The analytics available for share links include metrics like how many new users have arrived at the game details page through a share link, and which off-platform channel has brought in the most engaged users. There is no limit to how many share links you can create per game; creating different links for different channels can help you keep better track of acquisition metrics.

For more information on the analytics for share links, see the [[external/roblox-creator-docs/production/analytics/acquisition|Acquisition]] page.

## Create a share link

<Alert severity="warning">
You can only create share links for games you own. For group-owned games, you must be a member of the group with the **<Translation keyName='Group.ShareLinksManager.Label' />** permission, and the share link must be created from the group account.
</Alert>

To create a share link:

1. In the [Creator Dashboard](https://create.roblox.com/dashboard/creations), go to **Creations** and select the **Share Links** tab.
2. Click **Create link**.
3. Enter a unique campaign name and select the game you want to create a share link for.
4. <Chip label="OPTIONAL" size="small" variant="outlined" /> To enable custom `Class.Player:GetJoinData()|LaunchData`, toggle on **Use custom LaunchData** and enter a `LaunchData` parameter.
5. Click **Generate link**.

The new share link generates instantly and is ready to be shared.


## Related Files

- [[external/roblox-creator-docs/production/promotion/ad-integrations]] - Ad integrations.
- [[external/roblox-creator-docs/production/promotion/ads-manager]] - Ads Manager.
- [[external/roblox-creator-docs/production/promotion/reporting-and-billing]] - Ads Manager reporting and billing.
- [[external/roblox-creator-docs/production/promotion/advertise-on-roblox]] - Advertise on Roblox.
- [[external/roblox-creator-docs/production/promotion/advertise]] - Advertising for creators.
- [[external/roblox-creator-docs/production/promotion/comply-with-advertising-standards]] - Advertising standards.
- [[external/roblox-creator-docs/production/promotion/content-maturity]] - Content maturity and compliance.
- [[external/roblox-creator-docs/production/promotion/deeplinks]] - Deep links.
- [[external/roblox-creator-docs/production/promotion/experience-events]] - Experience events and updates.
- [[external/roblox-creator-docs/production/promotion/experience-guidelines]] - Experience guidelines.
- [[external/roblox-creator-docs/production/promotion/experience-notifications]] - Experience notifications.
- [[external/roblox-creator-docs/production/promotion/referral-system]] - Friend referral system.
- [[external/roblox-creator-docs/production/promotion/invite-prompts]] - Player invite prompts.
- [[external/roblox-creator-docs/production/promotion/index]] - Promotion.
- [[external/roblox-creator-docs/production/promotion/regional-content-availability]] - Regional Content Availability.
- [[external/roblox-creator-docs/production/promotion/rewarded-video-ads]] - Rewarded video ads.
- ...and 2 more local docs.
