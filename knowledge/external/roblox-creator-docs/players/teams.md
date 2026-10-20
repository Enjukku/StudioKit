---
title: Implement teams
description: The Teams service allows you assign players to different teams within your game.
tags: [roblox, documentation, external-reference, priority-reference, players]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [players/teams.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/players/teams.md). Published page: [https://create.roblox.com/docs/players/teams](https://create.roblox.com/docs/players/teams).

You can divide players in your game into multiple teams using the `Class.Teams` service. By [configuring](#add-teams) the `Class.Teams` service and [assigning teams](#assign-players-to-teams), players are automatically differentiated by their [[external/roblox-creator-docs/characters/name-health-display|display name]] color, as well as their name in the default player list.

## Add teams

By default, no teams are configured. To add teams:

1. In the [[external/roblox-creator-docs/studio/explorer|Explorer]] hierarchy, hover over the `Class.Teams` object and click the **&CirclePlus;** icon to show a list of objects.
2. Insert a new `Class.Team` object under the `Class.Teams` service.

   <img src="../assets/studio/explorer/Teams-Team.png" width="320" />

3. Select the new `Class.Team` object and, in the [[external/roblox-creator-docs/studio/properties|Properties]] window, change the team `Class.Team.Name|Name` and assign a unique matching `Class.Team.TeamColor|TeamColor`. A team's name and color both appear in the game's player list.

   <img src="../assets/studio/properties/Team-Name-TeamColor.png" width="320" />

4. Repeat these steps to add more teams.

## Assign players to teams

By default, Roblox **auto-assigns** new players joining the game to the team with the fewest members, and you can still use the following steps to assign players to a specific team.

1. Select each `Class.Team` object in the `Class.Teams` service to display its properties.

2. Uncheck the `Class.Team.AutoAssignable|AutoAssignable` checkbox.

   <img src="../assets/studio/properties/Team-AutoAssignable-Disabled.png" width="320" />

3. Assign a player to a specific team by changing their `Class.Player.Team` property to the team name in the format of `Teams[TEAM_NAME]`, such as <Typography noWrap>`Teams["Blue Team"]`</Typography>.

## Team spawn locations

You can use `Class.SpawnLocation` objects to spawn players of different teams at specific locations when they join or respawn. By default, `Class.SpawnLocation|SpawnLocations` are **neutral** and any player can spawn upon them, so you need to lock each one to the team that can occupy it using the following steps:

1. Using the [[external/roblox-creator-docs/studio/explorer|Explorer]], insert a new `Class.SpawnLocation` into the workspace.
2. With the new `Class.SpawnLocation` selected, uncheck its `Class.SpawnLocation.Neutral|Neutral` checkbox in the [[external/roblox-creator-docs/studio/properties|Properties]] window.
3. Set the spawn's `Class.SpawnLocation.TeamColor|TeamColor` property to the `Class.Team.TeamColor|TeamColor` of an existing [team](#add-teams). For example, if the intended team's `Class.Team.TeamColor` is `Lapis`, set the spawn's `Class.SpawnLocation.TeamColor` to `Lapis` as well.

   <Grid container spacing={3} alignItems="end">
	 <Grid item>
	 <figure>
	 <img src="../assets/studio/properties/Team-Name-TeamColor.png" width="320" />
	 <figcaption>`Class.Team.TeamColor`</figcaption>
   </figure>
	 </Grid>
	 <Grid item>
   <figure>
	 <img src="../assets/studio/properties/SpawnLocation-TeamColor.png" width="320" />
   <figcaption>`Class.SpawnLocation.TeamColor`</figcaption>
   </figure>
	 </Grid>
	 </Grid>

<Alert severity="warning">
Note that the `Class.SpawnLocation.TeamColor` property is different from `Class.SpawnLocation.BrickColor` and `Class.SpawnLocation.Color` which represent the **visual** color of the spawn object and are not related to team functionality.
</Alert>


## Related Files

- [[external/roblox-creator-docs/players/avatar-context-menu]] - Avatar Context Menu.
- [[external/roblox-creator-docs/players/avatar-editor]] - Avatar Editor Service.
- [[external/roblox-creator-docs/players/avatar-inspect-menu]] - Avatar Inspect Menu.
- [[external/roblox-creator-docs/players/disable-ui]] - Disable default UI.
- [[external/roblox-creator-docs/players/tools]] - In-game tools.
- [[external/roblox-creator-docs/players/leaderboards]] - Leaderboards.
- [[external/roblox-creator-docs/players/loading-screens]] - Loading screens.
- [[external/roblox-creator-docs/players/users]] - Users and domain-scoped user IDs.
- [[external/roblox-creator-docs/players/index]] - Users and players.
