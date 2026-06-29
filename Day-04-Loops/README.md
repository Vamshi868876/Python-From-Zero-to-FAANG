# 🐍 Day 04: Loops (Doing Things Repeatedly)

# 🤔 Imagine This...

Your boss tells you:
*"Print 'Hello' 10,000 times."*

Are you going to write `print("Hello")` 10,000 times?
❌ **No.** Your fingers will break.

Instead, you tell the computer:
*"Print 'Hello'. Do this 10,000 times."*

To do things repeatedly without writing the same code over and over, Python uses **Loops**.

---

# 👶🐣 Baby Version

Imagine eating a bowl of 10 grapes. 🍇

You don't say:
*"Eat a grape. Eat a grape. Eat a grape. Eat a grape..."*

You simply say:
*"Keep eating a grape **UNTIL** the bowl is empty."*
or
*"For **EVERY** grape in the bowl, eat it."*

Python has exactly two types of loops to do this:
1. **The `for` loop:** (When you know EXACTLY how many grapes you have).
2. **The `while` loop:** (When you just want to keep eating UNTIL they are gone).

---

# 🎡 1. The `for` Loop

Use this when you know **how many times** you want to repeat something.

### Real Life Example:
Clapping 5 times.
👏 👏 👏 👏 👏

### Python Code:
```python
for i in range(5):
    print("Clap 👏")
```
*(Note: `range(5)` means count from 0 to 4. Total = 5 times).*

---

# 🔄 2. The `while` Loop

Use this when you want to repeat something **until a condition becomes False**.

### Real Life Example:
Filling a glass of water.
Keep pouring water **WHILE** the glass is not full.

### Python Code:
```python
glass_full = False
water_level = 0

while glass_full == False:
    print("Pouring water...")
    water_level += 1
    
    if water_level == 3:
        glass_full = True
        print("Glass is full! Stop pouring.")
```

---

# 🛑 Control The Loop: `break` and `continue`

Sometimes you want to manipulate the loop while it's running.

## 1. `break` (The Emergency Stop Button)
Imagine eating a bag of chips. You find a spider in the bag. 🕷️
Do you keep eating? NO! You **break** out of the loop immediately.

```python
for chip in range(10):
    if chip == 3:
        print("Spider found! BREAK!")
        break
    print("Eating chip", chip)
```

## 2. `continue` (The Skip Button)
Imagine eating Skittles. You hate the yellow ones. 🟡
When you see a yellow one, you don't throw the whole bag away (`break`). You just **skip** it and eat the next one.

```python
for skittle in ["red", "yellow", "green"]:
    if skittle == "yellow":
        print("Ew, skip the yellow one!")
        continue
    print("Ate a", skittle, "skittle.")
```

---

# 🧠 The 5 Second Rule

Know how many times? ➡ **`for` loop**
Waiting for a condition to stop? ➡ **`while` loop**
Emergency Stop? ➡ **`break`**
Skip this one? ➡ **`continue`**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
for x in range(3):
    print("Python")
```

**Snippet 2:**
```python
count = 0
while count < 2:
    print(count)
    count += 1
```

**Snippet 3:**
```python
for num in range(5):
    if num == 2:
        continue
    print(num)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:**
```text
Python
Python
Python
```
(It prints 3 times because `range(3)` is 0, 1, 2).

**Snippet 2 Answer:**
```text
0
1
```
(It prints 0, then 1, and stops before 2 because `2 < 2` is False).

**Snippet 3 Answer:**
```text
0
1
3
4
```
(Notice `2` is missing! The `continue` statement skipped it.)
