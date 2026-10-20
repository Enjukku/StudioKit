> Author: orchestrator · claude-opus-5-5 · high · 2026-10-20. Read-only probes for `execute_luau`. Each returns one short string. Edit the constants at the top, not the logic.

# Studio probes

## P-01 State summary (Edit or Server)
```lua
local ws = workspace
local parts = {}
for _, name in { "Workspace", "ReplicatedStorage", "ServerScriptService", "ServerStorage", "StarterGui", "StarterPlayer" } do
	local s = game:GetService(name)
	table.insert(parts, string.format("%s=%d", name, #s:GetDescendants()))
end
return string.format(
	"%s | StreamingEnabled=%s SignalBehavior=%s | players=%d",
	table.concat(parts, " "),
	tostring(ws.StreamingEnabled),
	tostring(ws.SignalBehavior),
	#game:GetService("Players"):GetPlayers()
)
```

## P-02 Attributes and tags of one instance
```lua
local PATH = "Workspace.Map" -- dot path from game
local node: Instance? = game
for name in string.gmatch(PATH, "[^%.]+") do
	node = node and node:FindFirstChild(name)
end
if not node then return "missing: " .. PATH end
local out = {}
for k, v in node:GetAttributes() do
	table.insert(out, k .. "=" .. tostring(v))
end
table.sort(out)
return string.format("%s (%s) attrs: %s | tags: %s", node:GetFullName(), node.ClassName,
	table.concat(out, ", "), table.concat(game:GetService("CollectionService"):GetTags(node), ", "))
```

## P-03 Filtered log (errors and warnings, or a text filter)
```lua
local FILTER = "" -- substring to keep; "" keeps all errors and warnings
local MAX = 30
local out, n = {}, 0
for _, entry in game:GetService("LogService"):GetLogHistory() do
	local bad = entry.messageType == Enum.MessageType.MessageError or entry.messageType == Enum.MessageType.MessageWarning
	local keep = if FILTER == "" then bad else string.find(entry.message, FILTER, 1, true) ~= nil
	if keep then
		n += 1
		if n <= MAX then table.insert(out, entry.messageType.Name .. ": " .. string.sub(entry.message, 1, 200)) end
	end
end
return string.format("%d matching lines (showing %d)\n%s", n, math.min(n, MAX), table.concat(out, "\n"))
```
Not during a performance run (C-05).

## P-04 Scripts inside a model (check an inserted asset)
```lua
local PATH = "Workspace.InsertedModel"
local node: Instance? = game
for name in string.gmatch(PATH, "[^%.]+") do
	node = node and node:FindFirstChild(name)
end
if not node then return "missing: " .. PATH end
local found = {}
for _, d in node:GetDescendants() do
	if d:IsA("LuaSourceContainer") then table.insert(found, d:GetFullName() .. " (" .. d.ClassName .. ")") end
end
return #found .. " scripts\n" .. table.concat(found, "\n")
```
Any script in a store model: report it; do not keep the model until the brief owner decides.

## P-05 Restore the owner's camera
Edit mode, after screenshots:
```lua
workspace.CurrentCamera.CameraType = Enum.CameraType.Fixed
return "camera restored"
```
In Play, stop the test instead (or set `Custom` on the Client data model).

## P-06 Download footprint of ReplicatedStorage (what every client downloads)
```lua
local out = {}
for _, top in game:GetService("ReplicatedStorage"):GetChildren() do
	local n, bytes = 0, 0
	for _, d in top:GetDescendants() do
		n += 1
		if d:IsA("LuaSourceContainer") then bytes += #d.Source end
	end
	table.insert(out, string.format("%s: %d descendants, %d source bytes", top.Name, n, bytes))
end
return table.concat(out, "\n")
```
Source bytes are script text, not runtime memory. Say so in the report.
