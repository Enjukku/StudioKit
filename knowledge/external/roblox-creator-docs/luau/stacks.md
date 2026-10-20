---
title: Stacks
description: Stacks are data structures that follow the Last in First Out (LIFO) principle.
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/stacks.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/stacks.md). Published page: [https://create.roblox.com/docs/luau/stacks](https://create.roblox.com/docs/luau/stacks).

A stack is a linear data structure with a collection of items that follows the Last-In-First-Out (LIFO) principle. The top of the stack is the item most recently added to the stack, and the bottom of the stack is the item that was least recently added.

You can think of the stack data structure as a stack of dinner plates: you start with one, and then you put another above it. When you take plates from the stack, the **first** one you remove from the stack is the **last** one you put on the top.

Stacks have two main operations: **push** for adding an element to the top of the stack and **pop** for removing the element from the top of the stack. A Stack can either have a fixed size or be dynamically resized. Stacks are helpful for design usage such as backtracking algorithms.

## Implement stacks

Though Luau doesn't have stacks as a built-in data structure, you can use [[external/roblox-creator-docs/luau/tables|tables]] to implement stacks. The following code sample shows how to create a stack, `push` an object to a stack, and `pop` an object from the stack. To use this implementation for your game, you should save it as a `Class.ModuleScript` and store it in `Class.ReplicatedStorage`, so your stack is accessible for both client and server.

```lua Implement a Stack Using Table
local Stack = {}
Stack.__index = Stack

function Stack.new()
	local self = setmetatable({}, Stack)

	self._stack = {}

	return self
end

-- Check if the stack is empty
function Stack:isEmpty()
	return #self._stack == 0
end

-- Put a new value onto the stack
function Stack:push(value)
	table.insert(self._stack, value)
end

-- Take a value off the stack
function Stack:pop()
	if self:isEmpty() then
		return nil
	end

	return table.remove(self._stack, #self._stack)
end

return Stack
```

The following code sample is a usage example as a `Class.Script` under `Class.Workspace`. You can modify the code, type, and storage location to fit your own usage, as long as you have the previous implementation code sample properly stored.

```lua title="Stack Usage Example"
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Stack = require(ReplicatedStorage:WaitForChild("Stack"))

local s = Stack.new()

-- Change the stack 	Resulting stack		 Output

s:push(1)      			-- {1}

s:push(5)      			-- {1, 5}

s:push(10)     			-- {1, 5, 10}

print(s:pop()) 			-- {1, 5}            10

print(s:pop()) 			-- {1}               5

s:push(20)     			-- {1, 20}

print(s:pop()) 			-- {1}               20

print(s:pop()) 			-- {}                1
```

<Alert severity="warning">
When running `pop()` on a stack, make sure the stack is not empty.
</Alert>

If you run the previous code sample without changing anything, the expected output is:

```lua title="Example Output"
10
5
20
1
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
- [[external/roblox-creator-docs/luau/nil]] - Nil.
- [[external/roblox-creator-docs/luau/numbers]] - Numbers.
- [[external/roblox-creator-docs/luau/operators]] - Operators.
- [[external/roblox-creator-docs/luau/queues]] - Queues.
- [[external/roblox-creator-docs/luau/scope]] - Scope.
- [[external/roblox-creator-docs/luau/strings]] - Strings.
- [[external/roblox-creator-docs/luau/tables]] - Tables.
- ...and 5 more local docs.
