# 💼 Interview Questions: Lists

## What is the difference between `append()` and `extend()`?
- `append()` adds its argument as a **single element** to the end of a list. (If you append a list to a list, you get a list inside a list).
- `extend()` iterates over its argument and adds each element to the list, effectively merging them.

## Are lists Mutable?
Yes. Lists are mutable, meaning their contents can be altered after creation (items can be modified, added, or removed in-place).

## What is List Comprehension?
It is a concise way to create lists. Instead of doing:
```python
squares = []
for i in range(5):
    squares.append(i**2)
```
You can do it in one line:
`squares = [i**2 for i in range(5)]`

## What is the time complexity of `pop(0)` versus `pop()`?
- `pop()` removes the last element and is **O(1)** (very fast).
- `pop(0)` removes the first element and is **O(N)** (slow). This is because Python has to shift every single other element in the list one space to the left to fill the gap. (In FAANG interviews, if you need to pop from the left frequently, use `collections.deque`).
