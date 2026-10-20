---
title: Core scripts
comments:
description: Explains the two scripts responsible for the Battle Royale gameplay loop.
tags: [roblox, documentation, external-reference, priority-reference, resources, scripting]
prev: /resources/battle-royale/run-the-game
next: /resources/battle-royale/pickup-system
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [resources/battle-royale/core-scripts.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/resources/battle-royale/core-scripts.md). Published page: [https://create.roblox.com/docs/resources/battle-royale/core-scripts](https://create.roblox.com/docs/resources/battle-royale/core-scripts).

The core game loop in Roblox Battle Royale is generally handled by two scripts, specifically `ServerScriptService/Server` on the server and `StarterPlayer/StarterPlayerScripts/Client` on the client.

## Initial setup

The `ReplicatedFirst/InitialSetup` script configures a few engine-level systems — built-in UI, chat, etc. — and ensures that the client loads the assets referenced in `ReplicatedFirst/Configurations/AssetPreloads` before proceeding.

## Game stages

The initialization and updating of specific systems is done differently depending on the current stage of the game. Most of these cases are handled by `ServerScriptService/Core/GameStageHandler` on the server and `ReplicatedStorage/Core/StageManager` on the client. When a stage is requested, a module of the same name is required and various setup functions called on it. If there is already a module handling the current stage, shutdown functions are called on it prior to the new stage handler being initialized.

## Places/server roles

Within `ReplicatedFirst/Configurations/MainConfiguration`, different gameplay modes are organized into lists of stages to be executed.

```lua
local _roleStages = {
	Lobby = {"Lobby"},
	Queue = {"Queue"},
	Gameplay = {"Waiting", "Gameplay", "EndGame"},
}
```

There are 3 different roles that a place can have:

- **Lobby** — Initial place where options like game mode are selected.
- **Queue** — Where a cohort of players gather for a particular game mode, building and fighting while waiting for the configured number of minimum players. Once the minimum numbers of players have arrived, a countdown will start, currently configured for 3:00 minutes, at the end of which gameplay will be initiated.
- **Gameplay** — The place where skydiving takes place and the game is played until completion.


## Related Files

- [[external/roblox-creator-docs/resources/battle-royale/index]] - Battle Royale.
- [[external/roblox-creator-docs/resources/battle-royale/building-system]] - Building system.
- [[external/roblox-creator-docs/resources/battle-royale/installation-and-setup]] - Installation and setup.
- [[external/roblox-creator-docs/resources/battle-royale/minimap-system]] - Minimap system.
- [[external/roblox-creator-docs/resources/battle-royale/pickup-system]] - Pickup system.
- [[external/roblox-creator-docs/resources/battle-royale/run-the-game]] - Run the game.
- [[external/roblox-creator-docs/resources/battle-royale/the-storm]] - The storm.
