# 🐍 Day 07: Lists (The Magic Backpack)

# 🤔 Imagine This...

You are going to school. You have:
- A pen
- A book
- A laptop
- An apple

Do you carry them one by one in your hands?
❌ **No!** You put them all in a **Backpack**.

In Python, a **List** is exactly like a backpack. It is a single container where you can store many different items.

---

# 👶🐣 Baby Version

A list is just a box with dividers.
You can put anything in it: Numbers, Text, or even other boxes!
```python
backpack = ["Pen", "Book", "Laptop", "Apple"]
```
Python numbers the slots in the box starting from **0**.

Slot 0: `"Pen"`
Slot 1: `"Book"`
Slot 2: `"Laptop"`

If you want the book, you just ask for Slot 1:
```python
print(backpack[1]) # "Book"
```

---

# 🪄 Lists are MUTABLE (You can change them!)

This is the most important thing about lists.
Unlike strings (which you cannot change once made), lists are **Mutable**. You can take things out, put new things in, or replace things!

```python
backpack = ["Pen", "Book", "Apple"]

# 1. Replace an item (Swap Apple for Orange)
backpack[2] = "Orange"

# 2. Add a new item at the end
backpack.append("Water Bottle")

# 3. Take the last item out
backpack.pop()
```

---

# 🛠️ Important List Tools (Methods)

- `append(item)`: Adds an item to the end of the list.
- `insert(index, item)`: Sneaks an item into a specific spot.
- `remove(item)`: Finds and deletes the first match.
- `pop()`: Removes and returns the last item (like taking the top book off a stack).
- `sort()`: Sorts the list (A-Z or smallest to largest).

---

# 🧠 The 5 Second Rule

Square brackets `[]`? ➡ **List**
Can I change it? ➡ **Yes (Mutable)**
Add something? ➡ **`.append()`**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
nums = [10, 20, 30]
nums[1] = 99
print(nums)
```

**Snippet 2:**
```python
fruits = ["Apple", "Banana"]
fruits.append("Cherry")
print(fruits)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `[10, 99, 30]`
(We replaced index 1).

**Snippet 2 Answer:** `["Apple", "Banana", "Cherry"]`
(Append always adds to the end!)
