---
title: Battle Royale
comments:
description: Battle Royale is an example game-kit with instructions on specific gameplay implementations.
tags: [roblox, documentation, external-reference, priority-reference, resources, index]
next: /resources/battle-royale/installation-and-setup
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [resources/battle-royale/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/resources/battle-royale/index.md). Published page: [https://create.roblox.com/docs/resources/battle-royale](https://create.roblox.com/docs/resources/battle-royale).

<Alert severity="warning">
Processes and features may have changed since the writing of this documentation. Refer to the appropriate feature documentation for up-to-date information on any features and workflows.

The content of this project and documentation can be used under Roblox's [[external/roblox-creator-docs/resources/limited-use-license|Limited Use License]].
</Alert>

**Roblox Battle Royale** is a game kit built by internal Roblox developers consisting of multiplayer battles on a large island with destructible buildings, a variety of vehicles and weapons, and interesting areas to explore. The default game loop is simple: join a match, skydive onto the island, stay out of the storm, and survive until you are the last person standing. Players can also build their own structures by laying down building tiles. This project is [available to join](https://www.roblox.com/games/5158731546/Roblox-Battle-Royale) as a public game.

<img
  alt="Drop onto a region in a classic battle royale game."
  src="../../assets/resources/battle-royale/introduction/Battle-Royale-Slide-B.jpeg"
  width="80%" />

## Features

At a high level, Roblox Battle Royale contains the following:

- Code for 3rd-person cameras.
- A robust and customizable ranged [[external/roblox-creator-docs/resources/weapons-kit|weapon system]], including 9 different weapons preconfigured.
- A building system.
- A destruction system.

All of these systems are supported on a wide range of hardware, screen sizes, and game controllers, from mobile phones to Xbox to high-end desktop PCs. The code is designed to be performant and easy to read so anyone can learn how to build a game like this.

## Play modes

There are 4 play modes included in this project:

- **Last One Standing** — Traditional battle royale; players who are eliminated are removed from the match and the last person to survive wins.
- **Solo Deathmatch** — Players will respawn after dying; the player with the highest kill count wins.
- **Team Deathmatch** — Two teams of players attempt to eliminate the other team; the team with players still alive at the end wins.
- **Free Play** — Players can enter the game and play around with the building system, weapons, and vehicles.


## Related Files

- [[external/roblox-creator-docs/resources/battle-royale/building-system]] - Building system.
- [[external/roblox-creator-docs/resources/battle-royale/core-scripts]] - Core scripts.
- [[external/roblox-creator-docs/resources/battle-royale/installation-and-setup]] - Installation and setup.
- [[external/roblox-creator-docs/resources/battle-royale/minimap-system]] - Minimap system.
- [[external/roblox-creator-docs/resources/battle-royale/pickup-system]] - Pickup system.
- [[external/roblox-creator-docs/resources/battle-royale/run-the-game]] - Run the game.
- [[external/roblox-creator-docs/resources/battle-royale/the-storm]] - The storm.
