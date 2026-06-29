# 🐍 Day 06: Strings (Text Manipulation)

# 🤔 Imagine This...

You have a necklace made of alphabet beads.
`[P] - [Y] - [T] - [H] - [O] - [N]`

What if you want to pull out just the first bead?
What if you want to swap the `[P]` for a `[J]`?
What if you want to make all the beads UPPERCASE?

In Python, text is exactly like this bead necklace. It is a sequence of characters.
We call it a **String**.

---

# 👶🐣 Baby Version

A string is just a line of characters inside quotes `" "`.

Think of a string as a **Train** with numbered seats. 🚂
Seat numbers (Indexes) in Python ALWAYS start at **0**.

String: `"APPLE"`
Seat 0: `A`
Seat 1: `P`
Seat 2: `P`
Seat 3: `L`
Seat 4: `E`

If you want the letter in Seat 0, you ask Python: `fruit[0]`

---

# ✂️ String Slicing (Slicing the Train)

You can grab a whole chunk of the train using slicing.
Syntax: `string[start : stop : step]`

```python
word = "PYTHON"

print(word[0:3])  # PYT (Starts at 0, stops BEFORE 3)
print(word[3:])   # HON (Starts at 3, goes to the end)
print(word[::-1]) # NOHTYP (The magic trick to REVERSE a string!)
```

---

# 🛠️ String Methods (Built-in Magic Tools)

Python provides tools to modify strings instantly.
*(Note: Strings are immutable, meaning these tools return a NEW string, they don't change the original).*

```python
name = "rahul"

# 1. Make it uppercase
print(name.upper()) # RAHUL

# 2. Make the first letter capital
print(name.capitalize()) # Rahul

# 3. Replace characters
print(name.replace("r", "j")) # jahul

# 4. Count how many times a letter appears
print(name.count("a")) # 1
```

---

# ✨ f-strings (The Best Feature in Python!)

In the old days, combining text and variables was annoying.
`print("My name is " + name + " and I am " + str(age) + " years old.")` 🤮

**f-strings** (formatted strings) make it beautiful. Just put an `f` before the quotes, and wrap variables in curly `{}` braces!

```python
name = "Rahul"
age = 21

print(f"My name is {name} and I am {age} years old.") 
# Beautiful! 😍
```

---

# 🧠 The 5 Second Rule

Index starts at? ➡ **0**
Reverse a string? ➡ **`[::-1]`**
Combine variables & text? ➡ **f-strings `f"{var}"`**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
text = "BATMAN"
print(text[1])
```

**Snippet 2:**
```python
word = "hello"
word.upper()
print(word)
```

**Snippet 3:**
```python
food = "Burger"
print(f"I want a {food.upper()}")
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `A`
(Indexes start at 0. So B is 0, A is 1!)

**Snippet 2 Answer:** `hello`
(Trick question! `word.upper()` creates a new uppercase string, but we didn't save it to a variable! The original `word` remains lowercase).

**Snippet 3 Answer:** `I want a BURGER`
(You can run string methods directly inside f-strings!)
