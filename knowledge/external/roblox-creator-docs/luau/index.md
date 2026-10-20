---
title: Luau
description: Luau is the scripting language creators use in Roblox Studio.
tags: [roblox, documentation, external-reference, priority-reference, luau, scripting, index]
---


> [!info] Local Roblox Creator Docs mirror
> Mirrored from [luau/index.md](https://github.com/Roblox/creator-docs/blob/main/content/en-us/luau/index.md). Published page: [https://create.roblox.com/docs/luau](https://create.roblox.com/docs/luau).

[Luau](https://luau.org) is the scripting language creators use in Roblox Studio. It is a fast, small, safe, gradually typed embeddable scripting language derived from [Lua 5.1](https://www.lua.org/manual/5.1/).

<Alert severity="success">
Contributing your Luau scripts for AI training can help enhance Luau-focused AI tools in Studio. For more information, see [Empower Luau creation](https://create.roblox.com/data-collection).
</Alert>

## Support in Studio

The **Script Editor** in Studio supports Luau with autocompletion, syntax highlighting, static linting, type checking, and script analysis. It also shows documentation and function signatures for members of the [Roblox Engine API](/reference/engine).

## Types

Luau includes the following data types:

- [[external/roblox-creator-docs/luau/nil|Nil]] represents non-existence or nothingness. It's different from any other value or data type.
- [[external/roblox-creator-docs/luau/booleans|Booleans]], or `bool`, have a value of either `false` or `true`.
- [[external/roblox-creator-docs/luau/numbers|Numbers]], or `double`, represent double-precision (64-bit) floating-point numbers.
- [[external/roblox-creator-docs/luau/strings|Strings]] are sequences of characters, such as letters, numbers, and symbols.
- [[external/roblox-creator-docs/luau/tables|Tables]] are [[external/roblox-creator-docs/luau/tables#arrays|arrays]] or [[external/roblox-creator-docs/luau/tables#dictionaries|dictionaries]] of any value except `nil`.
- [[external/roblox-creator-docs/luau/enums|Enums]] are fixed lists of items.

Luau is dynamically typed by default. Variables, function parameters, and return values can be any data type. This helps you write code faster because you don't need to provide types for each piece of data. You can still declare explicit types for variables in Luau and enable [[external/roblox-creator-docs/luau/type-checking|strict type checking]] to make type issues obvious and easy to locate.

## Data structures

You can also implement the following data structures using primitive data types:

- [[external/roblox-creator-docs/luau/stacks|Stacks]] are Last-In-First-Out collections of items that you can implement using tables.
- [[external/roblox-creator-docs/luau/queues|Queues]] are First-In-First-Out collections of items that you can implement using tables.
- [[external/roblox-creator-docs/luau/metatables|Metatables]] are tables with advanced configurations that can achieve functionalities such as storing pairs of keys and values and calculating arithmetic operations.

## Features

In Luau, [[external/roblox-creator-docs/luau/variables|variables]] and [[external/roblox-creator-docs/luau/functions|functions]] can have global and local [[external/roblox-creator-docs/luau/scope|scope]] within a script. Luau has logical, relational, and compound assignment [[external/roblox-creator-docs/luau/operators|operators]]. You can use [[external/roblox-creator-docs/luau/control-structures|control structures]] and [[external/roblox-creator-docs/luau/functions|functions]] to control when Luau executes code. Many operators and variable assignments perform [[external/roblox-creator-docs/luau/type-coercion|type coercion]] to change values to the types that Luau expects.


## Related Files

- [[external/roblox-creator-docs/luau/booleans]] - Booleans.
- [[external/roblox-creator-docs/luau/control-structures]] - Control structures.
- [[external/roblox-creator-docs/luau/enums]] - Enums.
- [[external/roblox-creator-docs/luau/functions]] - Functions.
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
- [[external/roblox-creator-docs/luau/tables]] - Tables.
- ...and 5 more local docs.
