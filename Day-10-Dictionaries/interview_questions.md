# 💼 Interview Questions: Dictionaries

## What is the time complexity of looking up a key in a dictionary?
Dictionary lookups take **O(1)** (constant time) on average. Under the hood, Python dictionaries are Hash Maps. Python hashes the key, which gives the exact memory location of the value, bypassing the need to search through other items.

## Can a List be used as a Dictionary Key?
No. Dictionary keys must be **immutable** (hashable). Since lists are mutable (can be changed), their hash value would change, destroying the integrity of the hash map. You will get a `TypeError: unhashable type: 'list'`. You can, however, use a Tuple as a key!

## What is the difference between `dict.keys()`, `dict.values()`, and `dict.items()`?
- `.keys()` returns a view object of all the keys.
- `.values()` returns a view object of all the values.
- `.items()` returns a view object of tuples, where each tuple is `(key, value)`. This is highly useful for iterating in a `for` loop: `for k, v in my_dict.items():`
