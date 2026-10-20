---
title: Nil
description: Data type representing non-existence or nothingness.
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/nil.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/nil.md). Published page: [https://create.roblox.com/docs/luau/nil](https://create.roblox.com/docs/luau/nil).

In Luau, `nil` represents non-existence or nothingness. It's different from any other value or data type. You can use it to destroy a variable or remove a value in a table. It's the only value other than `false` which doesn't evaluate to [[external/roblox-creator-docs/luau/booleans|`true`]].

Luau has a **garbage collector** that removes data that is no longer accessible by any script. For best performance, redefine large variables as `nil` in long-running scripts when you don't need them anymore so the garbage collector removes them.

```lua
local variableToDelete = 5
print(variableToDelete) -- 5
variableToDelete = nil
print(variableToDelete) -- nil

local dictionaryTable = {
	Monday = 1,
	Tuesday = 2,
	Wednesday = 3
}
-- Output value of 'Tuesday' key
print(dictionaryTable.Tuesday) -- 2
-- Clear 'Tuesday' key
dictionaryTable.Tuesday = nil
-- Output value of key again
print(dictionaryTable.Tuesday) -- nil
```

You can use `nil` to clear some properties of objects. For example, you can set the `Parent` of an object to `nil` to effectively remove the object from the game. To return the object to the game after you remove it, reassign the `Parent`. The following example demonstrates how to use `nil` to remove a `Class.Part`:

```lua
local Workspace = game:GetService("Workspace")

-- Create a new brick
local part = Instance.new("Part")
-- Parent new part to the workspace, making it viewable
part.Parent = Workspace
task.wait(1)
-- Remove the part from view but not from memory
part.Parent = nil
task.wait(1)
-- Part still exists because it's referenced by the variable "part", so it can be returned to view
part.Parent = Workspace
task.wait(1)
-- Remove the part from view again
part.Parent = nil
-- Clear part reference so it gets picked up by the garbage collector
part = nil
```


## Related Files

- [[external/roblox-creator-docs/luau/booleans]] - Booleans.
- [[external/roblox-creator-docs/luau/control-structures]] - Control structures.
- [[external/roblox-creator-docs/luau/enums]] - Enums.
- [[external/roblox-creator-docs/luau/functions]] - Functions.
- [[external/roblox-creator-docs/luau/index]] - Luau.
- [[external/roblox-creator-docs/luau/luau-csharp-comparison]] - Luau and C# comparison.
- [[external/roblox-creator-docs/luau/comments]] - Luau comments.
- [[external/roblox-creator-docs/luau/metatables]] - Metatables.
- [[external/roblox-creator-docs/luau/native-code-gen]] - Native code generation.
- [[external/roblox-creator-docs/luau/numbers]] - Numbers.
- [[external/roblox-creator-docs/luau/operators]] - Operators.
- [[external/roblox-creator-docs/luau/queues]] - Queues.
- [[external/roblox-creator-docs/luau/scope]] - Scope.
- [[external/roblox-creator-docs/luau/stacks]] - Stacks.
- [[external/roblox-creator-docs/luau/strings]] - Strings.
- [[external/roblox-creator-docs/luau/tables]] - Tables.
- ...and 5 more local docs.
