# 💼 Interview Questions: Strings

## Are strings mutable or immutable in Python?
Strings are **immutable**. This means once a string is created in memory, it cannot be changed. When you do operations like `text.upper()` or `text.replace()`, Python is not modifying the original string; it is creating a brand new string in memory and returning it.

---

## How do you reverse a string in Python?
The most "Pythonic" and fastest way to reverse a string is using slicing with a negative step:
`reversed_string = my_string[::-1]`
*(Note: You could also use the `reversed()` built-in function and join it, but slicing is preferred in interviews).*

---

## What is the time complexity of string concatenation (`+`) in a loop?
Concatenating strings using `+` inside a loop has a terrible time complexity of **O(N^2)** because strings are immutable. Every time you concatenate, Python has to create a new string and copy the contents of the old strings over. 
**FAANG Best Practice:** Append the strings to a List instead, and then use `"".join(my_list)` at the end. This is **O(N)**.

---

## How does string indexing work with negative numbers?
Python supports negative indexing, which means counting from the end of the iterable.
`-1` refers to the last character, `-2` refers to the second to last character, and so on.
