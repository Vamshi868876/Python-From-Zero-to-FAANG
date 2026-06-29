# 🐍 Day 10: Dictionaries (The Phonebook)

# 🤔 Imagine This...

If I tell you to find "Rahul's Phone Number" in a List of 10,000 numbers... you have to look at every single number one by one. Slow!

But what if you have a **Phonebook**?
You jump straight to "R", look for "Rahul", and instantly get his number.

In Python, this is called a **Dictionary**. It stores data in **Key-Value pairs**.

---

# 👶🐣 Baby Version

Imagine a cabinet with labeled drawers. 🗄️

Label: `Name` ➡ Inside: `"Rahul"`
Label: `Age` ➡ Inside: `21`
Label: `Role` ➡ Inside: `"Developer"`

The Label is the **Key**.
The Inside is the **Value**.

```python
# Dictionaries use curly braces {} with a colon :
user = {
    "Name": "Rahul",
    "Age": 21,
    "Role": "Developer"
}

# Pulling open a drawer!
print(user["Name"]) # Output: Rahul
```

---

# 🔑 Dictionary Rules

1. **Keys MUST be unique!** You can't have two "Age" drawers.
2. **Keys are usually Strings.** (They can be ints or tuples, but strings are standard).
3. **Values can be ANYTHING.** A value can be a string, a number, a list, or even another dictionary!

```python
# Adding or Changing a drawer
user["Salary"] = 100000  # Creates a new drawer!
user["Age"] = 22         # Updates the old drawer!
```

---

# 🛠️ Safe Searching (`.get()`)

If you try to open a drawer that doesn't exist:
```python
print(user["Car"]) # ❌ CRASH! KeyError!
```

**FAANG Best Practice:** Use `.get()`!
```python
print(user.get("Car")) # Returns None instead of crashing!
print(user.get("Car", "No Car Found")) # Returns a custom message!
```

---

# 🧠 The 5 Second Rule

`{}` with `Key: Value`? ➡ **Dictionary**
How to search? ➡ **Use the Key! `dict["key"]`**
Safe search? ➡ **`dict.get("key")`**

---

# 🧠 Can You Predict?

**Snippet 1:**
```python
data = {"A": 1, "B": 2, "A": 99}
print(data)
```

**Snippet 2:**
```python
person = {"name": "Alex"}
print(person.get("age", 18))
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `{'A': 99, 'B': 2}`
(Keys must be unique! The second "A" overwrites the first one).

**Snippet 2 Answer:** `18`
("age" does not exist, so `.get()` returns our backup default value `18`).
