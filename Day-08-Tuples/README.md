# 🐍 Day 08: Tuples (The Locked Box)

# 🤔 Imagine This...

Yesterday we learned about Lists (The Backpack). You can add and remove things.
But what if you have data that should **NEVER** be changed? 

For example, the GPS coordinates of your house: `(17.3850, 78.4867)`
If someone accidentally changes these coordinates in the code, your delivery will go to another city!

To lock data so it cannot be modified, Python uses **Tuples**.

---

# 👶🐣 Baby Version

A Tuple is a glass box locked with a key. 🔒
You can look inside and see the items.
But you **cannot** add new items. You **cannot** remove items. You **cannot** change items.

```python
# Tuples use parentheses ()
coordinates = (17.38, 78.48)

print(coordinates[0]) # 17.38 (You can look at it!)
coordinates[0] = 99.9 # ❌ ERROR! The box is locked!
```

---

# 📦 Packing and Unpacking (The Coolest Feature)

Python lets you "pack" multiple items into a tuple, and instantly "unpack" them into separate variables!

```python
# Packing
user_data = ("Rahul", 21, "Hyderabad")

# Unpacking (Assigning to 3 variables at once!)
name, age, city = user_data

print(name) # Rahul
print(city) # Hyderabad
```

---

# 🧠 The 5 Second Rule

Parentheses `()`? ➡ **Tuple**
Can I change it? ➡ **NO! (Immutable)**
Why use it? ➡ **Faster than lists, and safer for fixed data.**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
my_tuple = (10, 20, 30)
my_tuple.append(40)
```

**Snippet 2:**
```python
a, b = (5, 10)
print(a + b)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `AttributeError: 'tuple' object has no attribute 'append'`
(Tuples are locked! You cannot append).

**Snippet 2 Answer:** `15`
(Unpacking assigns 5 to `a` and 10 to `b`. 5 + 10 = 15).
