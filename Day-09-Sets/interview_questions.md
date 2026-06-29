# 💼 Interview Questions: Sets

## Why are sets faster than lists for searching?
Sets are implemented using Hash Tables under the hood. When you check if an item exists in a set (`if item in my_set`), Python uses a hashing algorithm to go directly to the memory address. This makes lookups take **O(1)** (constant time). In a list, Python has to check every single element one by one, which takes **O(N)** time.

## Can a set contain a list?
No! Sets can only contain **hashable** (immutable) types. Since lists are mutable, they are unhashable, and putting a list inside a set will throw a `TypeError`. You can, however, put a Tuple inside a set.

## What is the difference between `.remove()` and `.discard()` in sets?
Both delete an item from the set. However:
- If the item does not exist, `.remove()` will throw a `KeyError` and crash your program.
- If the item does not exist, `.discard()` will do nothing and silently let the program continue.
