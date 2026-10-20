---
title: Tuples
description: Tuples are lists of values.
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/tuples.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/tuples.md). Published page: [https://create.roblox.com/docs/luau/tuples](https://create.roblox.com/docs/luau/tuples).

A **tuple** is a list of values. Many [[external/roblox-creator-docs/luau/functions#methods|methods]] and [[external/roblox-creator-docs/luau/functions#callbacks|callbacks]] in the [Roblox Engine API](/reference/engine) accept and return multiple values, but the API Reference says "Tuple" instead of those values.

## Parameters

If a [[external/roblox-creator-docs/luau/functions#methods|method]] or [[external/roblox-creator-docs/luau/functions#callbacks|callback]] accepts a tuple as a parameter, then it accepts multiple values. For example, the API Reference shows that the `Class.BindableFunction:Invoke()` method accepts a "Tuple" as a parameter, so it accepts multiple arguments.

```lua
BindableFunction:Invoke(1, true, "string", Vector3.new(0, 0, 0))
```

## Returns

If a [[external/roblox-creator-docs/luau/functions#methods|method]] or [[external/roblox-creator-docs/luau/functions#callbacks|callback]] returns a tuple, then it returns multiple values. For example, the API Reference shows that the `Class.Players:GetUserThumbnailAsync()` method returns a "Tuple", so it returns multiple values. The first return value is a Content URL, and the second is a [[external/roblox-creator-docs/luau/booleans|boolean]].

```lua
local Players = game:GetService("Players")

local userId = 156 -- builderman
local thumbType = Enum.ThumbnailType.HeadShot
local thumbSize = Enum.ThumbnailSize.Size420x420
local content, isReady = Players:GetUserThumbnailAsync(userId, thumbType, thumbSize)
print(content, isReady) -- rbxthumb://type=AvatarHeadShot&id=156&w=420&h=420 true
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
- [[external/roblox-creator-docs/luau/stacks]] - Stacks.
- [[external/roblox-creator-docs/luau/strings]] - Strings.
- ...and 5 more local docs.
