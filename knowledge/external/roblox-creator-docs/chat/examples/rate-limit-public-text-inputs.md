---
title: Rate-limited text inputs
description: Learn how to implement a rate limit for any text field that might be used by players to conduct a conversation.
tags: [roblox, documentation, external-reference, priority-reference, chat]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [chat/examples/rate-limit-public-text-inputs.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/chat/examples/rate-limit-public-text-inputs.md). Published page: [https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs](https://create.roblox.com/docs/chat/examples/rate-limit-public-text-inputs).

This example shows how to implement a rate limit of 1 minute on a text input field that allows players to post notes to a community bulletin board.

Add the following to a `Class.Script` in `Class.ServerScriptService`:

```lua title="Server"
local Players = game:GetService("Players")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

-- Create RemoteEvent for communication
local postNoteEvent = Instance.new("RemoteEvent")
postNoteEvent.Name = "PostNoteEvent"
postNoteEvent.Parent = ReplicatedStorage

-- Rate limit of one note per minute per player
local COOLDOWN_TIME = 60 -- Time in seconds
local lastPostTime = {}

local function canPlayerPost(player)
	local userId = player.UserId
	local currentTime = tick()

	if lastPostTime[userId] then
		local timeSinceLastPost = currentTime - lastPostTime[userId]
		if timeSinceLastPost < COOLDOWN_TIME then
			return false, COOLDOWN_TIME - timeSinceLastPost
		end
	end

	return true, 0
end

-- Handle post requests with rate limit and text filtering
postNoteEvent.OnServerEvent:Connect(function(player, noteData)
	local canPost, cooldown = canPlayerPost(player)

	if not canPost then
		postNoteEvent:FireClient(player, "cooldown", math.ceil(cooldown))
		return
	end

	-- All text shared publicly must go through a text filter
	local filterResult = getFilterResult(noteData.text, player.UserId)
	if filterResult then
		local success, filteredText = pcall(function()
		return filterResult:GetNonChatStringForBroadcastAsync()
	end)

	if success then
		-- Create the note
		local note = {
			text = filteredText
		}
		-- Update last post time
		lastPostTime[player.UserId] = tick()

		-- Send success response
		postNoteEvent:FireClient(player, "success", note)

		-- Broadcast new note to all players
		postNoteEvent:FireAllClients("newNote", note)
	else
		warn("Error filtering text!")
	end
end)

-- Clean up when player leaves
Players.PlayerRemoving:Connect(function(player)
	lastPostTime[player.UserId] = nil
end)
```


## Related Files

- [[external/roblox-creator-docs/chat/examples/group-chat-tags]] - Assign chat tags.
- [[external/roblox-creator-docs/chat/examples/custom-text-chat-commands]] - Custom text chat commands.
- [[external/roblox-creator-docs/chat/examples/simple-custom-frontend-ui]] - Custom text chat UI.
- [[external/roblox-creator-docs/chat/examples/proximity-chat]] - Proximity-based chat.
