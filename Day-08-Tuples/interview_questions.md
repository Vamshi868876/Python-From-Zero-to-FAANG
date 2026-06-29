# 💼 Interview Questions: Tuples

## What is the difference between a List and a Tuple?
1. **Syntax:** Lists use `[]`, Tuples use `()`.
2. **Mutability:** Lists are mutable (changeable). Tuples are immutable (read-only).
3. **Memory/Performance:** Because tuples are immutable, Python optimizes them. They take up less memory and are faster to iterate over than lists.

## How do you create a tuple with only ONE item?
This is a famous trick question!
`my_tuple = (5)` -> This is an Integer! Python ignores the parentheses.
To make it a tuple, you MUST include a trailing comma:
`my_tuple = (5,)` -> This is a Tuple!

## Since Tuples are immutable, can a Tuple contain a Mutable object?
Yes! A tuple can contain a list: `my_tuple = (1, 2, [3, 4])`. 
While you cannot reassign the elements of the tuple (you can't change index 2 to a different list), you *can* mutate the list inside it (e.g., `my_tuple[2].append(5)` is perfectly valid).
