---
title: Release game updates
description: Explains how to release updates for games.
tags: [roblox, documentation, external-reference, priority-reference, projects]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [projects/update-games.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/projects/update-games.md). Published page: [https://create.roblox.com/docs/projects/update-games](https://create.roblox.com/docs/projects/update-games).

When you publish an updated version of a game to Roblox, players aren't immediately removed from old versions of the game. Instead, you can migrate players to the updated version by restarting all of your outdated servers.

If you don't restart servers, players transition to the new version of the game as the servers running old versions eventually empty and shut down. This option is non‑disruptive, but your player base might be playing different versions of the game for a prolonged period of time; if your underlying player data format changes, you should probably restart servers.

For time-sensitive updates, you might prefer to deploy early, hide content behind a [[external/roblox-creator-docs/production/configs|config]], and then change the config value to release your new content.

## Restart servers

To restart servers for release updates:

1. Go to [Creations](https://create.roblox.com/dashboard/creations) and select the game you want to restart servers for.
1. In the left-hand navigation, navigate to **Configurations** > **Server management**.
1. Select the places you want to restart.
1. Click **Restart Servers**.
1. In the **Confirm Server Restart** dialog:
   1. Select one or both of the following restart options:
      - **Restart only servers with outdated versions** to avoid restarting servers that are running the latest published place version.
      - **Delay server restart** to delay the shutdown of servers and allow players a set time between 1 and 60 minutes to leave the game on their own instead of being temporarily disconnected. This is also known as server bleed-off.
   1. Click **Restart**.

<Alert severity="warning">
Unless you have a game update workflow that is independent of place version, it's recommended that you always select **Restart only servers with outdated versions** to avoid unnecessarily disconnecting players.
</Alert>

After you restart servers, Roblox:

1. Stops all matchmaking to servers designated for shutdown. Players who join your game by clicking the **Play** button will not be matched to these servers, but they can still join them by accepting invites, teleporting, or joining another user from their profile.
1. Waits for the configured delay time, if you selected the **Delay server restart** option.
1. Automatically teleports players to the updated version of the game. All players on the same old server are sent to the same replacement server running the new version.

<Alert severity="info">
If you want to completely shut down your game and not allow players to reconnect after you restart your servers, you must revoke access to your game from the [[external/roblox-creator-docs/production/publishing/publish-games-and-places#target-audience|public]].
</Alert>

## Notifications on servers

When you launch a delayed server restart, the `Class.DataModel.ServerRestartScheduled` event will fire on affected servers with the following arguments:

- `restartTime` — A `Datatype.DateTime`. The earliest time the server is scheduled to shut down.
- `source` — This will always be `Enum.CloseReason.DeveloperUpdate` for your published updates.
- `attributes` — An optional JSON object you can use to provide custom information about the restart, such as the update reason, urgency, etc.

In your server scripts, you can subscribe to this event to provide players with information about the upcoming restart. You might choose to provide a countdown timer in your UI, prompt players to save their progress, or teleport them to updated servers at the most convenient time.

Servers will also be notified when Roblox needs to restart servers for infrastructure maintenance reasons. The same `Class.DataModel.ServerRestartScheduled` event fires, with `source` as `Enum.CloseReason.RobloxMaintenance` and `attributes` as an empty dictionary.


## Related Files

- [[external/roblox-creator-docs/projects/activity-history]] - Activity History.
- [[external/roblox-creator-docs/projects/client-server]] - Client-server runtime.
- [[external/roblox-creator-docs/projects/collaboration]] - Collaboration.
- [[external/roblox-creator-docs/projects/configure-games]] - Configure games and places.
- [[external/roblox-creator-docs/projects/cross-platform]] - Cross-platform development.
- [[external/roblox-creator-docs/projects/data-model]] - Data model.
- [[external/roblox-creator-docs/projects/game-ownership-transfer]] - Game ownership transfer.
- [[external/roblox-creator-docs/projects/group-guidelines]] - Group guidelines.
- [[external/roblox-creator-docs/projects/groups]] - Groups (teams).
- [[external/roblox-creator-docs/projects/place-files]] - Place files.
- [[external/roblox-creator-docs/projects/index]] - Projects.
- [[external/roblox-creator-docs/projects/teleport]] - Teleport between places.
- [[external/roblox-creator-docs/projects/external-tools]] - Third-party tools.
- [[external/roblox-creator-docs/projects/version-history]] - Version History.
