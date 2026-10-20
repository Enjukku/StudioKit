---
title: Cross-server chat
description: Cross-server chat allows players to interact with others across different servers.
tags: [roblox, documentation, external-reference, priority-reference, chat]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [chat/cross-server-chat.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/chat/cross-server-chat.md). Published page: [https://create.roblox.com/docs/chat/cross-server-chat](https://create.roblox.com/docs/chat/cross-server-chat).

**Cross-server chat** is a native extension of `Class.TextChatService` that allows players to safely communicate with others across different servers in the same universe. This increases social engagement, especially in games with low server occupancy or during live events with a global community.

Roblox automatically groups servers based on age, language, and occupancy to ensure meaningful and safe interactions. Like default Roblox chat, cross-server chat includes full support for abuse reporting, text filtering, chat rules, muting, and blocking.

<Alert severity="info">
Each global chat channel connects about 200 users to ensure chat remains readable and performant. If users send messages too quickly, a throttle applies to the senders and receivers, and messages drop to protect the chat system.
</Alert>

## Enable cross-server chat

When you enable cross-server chat, the [[external/roblox-creator-docs/chat/chat-window|chat window]] includes two tabs for either single or multi-server communication:

- **Here** - Players can chat with others in the same server.
- **Global** - Players can chat with others across different servers.

<img src="../assets/players/cross-server-chat/overview-example.png" width="60%" alt="Core components of the text chat window with cross-server chat enabled." />

Cross-server chat is **enabled by default** for all games, but you have full control to enable or disable it according to your game's design requirements. To access the cross-server chat setting:

1. Navigate to the [Creator Dashboard](https://create.roblox.com/dashboard/creations).
1. Select a game, then in the left-hand navigation, navigate to **Audience** > **Communication Settings**.
1. Under the **Cross-server chat** section, toggle **Allow cross-server chat** on or off to enable or disable cross-server chat.

<Alert severity="warning">
Even if cross-server chat is enabled, the **Global** tab is disabled in [[external/roblox-creator-docs/production/monetization/private-servers|private servers]] to respect the privacy of users who only want to access your game with specific friends.
</Alert>

## Global chat commands

The **Global** tab supports a subset of standard chat commands for global chat:

- `/mute <username>` - Mutes a specific user in global chat.
- `/unmute <username>` - Unmutes a user.
- `/help` - Lists commands available within global chat.
- `/clear` - Clears the local chat window history.


## Related Files

- [[external/roblox-creator-docs/chat/guidelines]] - Chat system guidelines.
- [[external/roblox-creator-docs/chat/bubble-chat]] - Customize bubble chat.
- [[external/roblox-creator-docs/chat/chat-window]] - Customize the chat window.
- [[external/roblox-creator-docs/chat/preset-system-guidelines]] - Preset system guidelines.
- [[external/roblox-creator-docs/chat/quick-words]] - Quick Words.
- [[external/roblox-creator-docs/chat/in-experience-text-chat]] - Text chat overview.
- [[external/roblox-creator-docs/chat/voice-chat]] - Voice Chat.
