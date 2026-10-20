---
title: Bans
description: The Creator Hub Bans dashboard lets you ban users and manage bans.
tags: [roblox, documentation, external-reference, priority-reference, production]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [production/bans.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/production/bans.md). Published page: [https://create.roblox.com/docs/production/bans](https://create.roblox.com/docs/production/bans).

The **Bans** dashboard lets you view current bans, ban users, and unban users. You can view both public and private reasons for each ban, expiration dates for non-permanent bans, and ban history for the user.

![Overview of the Bans dashboard.](../assets/analytics/bans/bans-overview.png)

## Access the dashboard

To access the Bans page, you must either be the game owner or have [[external/roblox-creator-docs/projects/groups#roles-and-permissions|Configure bans for all group games permissions]].

1. Navigate to your [Creations](https://create.roblox.com/dashboard/creations) page on **Creator Dashboard** and select your game.
1. In the **Moderation** menu on the left, select **Bans**.

## Ban users

To ban a user, select the **Add users** button, fill out the details, and click **Apply Ban**.

- You must have the numeric user ID for each user you want to ban. To ban multiple users, include a comma-separated list of IDs.
- **Apply ban to all known alt accounts** lets you also include alt (alternate) accounts.
- Include a public and private reason for the ban. These fields can be identical. Roblox displays the public reason for the ban to the user if they attempt to join your game.
- For guidelines on banning users, see [[external/roblox-creator-docs/players/index#ban-guidelines|Users and players]].

## View bans

The default dashboard view shows current bans. You can sort by date of the ban and search for a particular user ID.

Under the **More** column, choose **See ban history** to view history for the user. When choosing whether to unban a user, this information can help you decide if the user was a one-time problem or persistently breaks the rules.

## Unban users

To unban users, choose one or more and click **Unban users**. Unbanned users can immediately access your game again. Manually unbanning a user does **not** remove their ban history.


## Related Files

- [[external/roblox-creator-docs/production/creator-store]] - Creator Store.
- [[external/roblox-creator-docs/production/configs]] - Experience configs.
- [[external/roblox-creator-docs/production/experiments]] - Experiments.
- [[external/roblox-creator-docs/production/index]] - Production.
- [[external/roblox-creator-docs/production/recommendation]] - Recommendation systems.
- [[external/roblox-creator-docs/production/rewarded-video-guides]] - Rewarded video genre guides.
- [[external/roblox-creator-docs/production/roblox-user-base]] - The Roblox user base.
