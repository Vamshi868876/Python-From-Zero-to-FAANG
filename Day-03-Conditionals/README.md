# 🐍 Day 03: Conditionals (Decision Making)

# 🤔 Imagine This...

You are driving a car. You see a traffic signal.

🚦 **Red Light**
Do you keep driving?
❌ No. You **STOP**.

🚦 **Green Light**
Do you stop?
❌ No. You **GO**.

You are making **decisions** based on a **condition** (the color of the light).

Computers are dumb. They execute code line by line. 
But what if we want the computer to make a decision?
What if we want it to do one thing if a condition is True, and another thing if it is False?

To solve this problem, Python uses **Conditionals** (`if`, `elif`, `else`).

---

# 👶🐣 Baby Version

Imagine your Mom makes a rule for dinner:

"**IF** you eat your vegetables, you get Ice Cream."
"**ELSE**, you get nothing."

You have a choice:
Vegetables eaten? = `True` ➔ 🍦 Ice Cream!
Vegetables eaten? = `False` ➔ 🛑 Nothing!

Python does exactly the same.

```python
ate_vegetables = True

if ate_vegetables:
    print("Here is your Ice Cream!")
else:
    print("No Ice Cream for you!")
```

---

# 🏗️ The 3 Pillars of Decisions

## 1. `if` (The Boss)
The `if` statement checks a condition. If it is True, it runs the code inside it.

```python
score = 100

if score == 100:
    print("You got a perfect score!")
```

## 2. `else` (The Backup Plan)
What if the condition is False? We use `else`. It catches everything that fails the `if` condition.

```python
score = 50

if score > 35:
    print("You passed!")
else:
    print("You failed. Study harder!")
```

## 3. `elif` (Multiple Choices)
What if we have more than 2 choices? (Like grading: A, B, C, Fail).
`elif` stands for "Else If".

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
else:
    print("Grade: Fail")
```

---

# 🚨 The Golden Rule: Indentation

Look closely at this code:
```python
if True:
    print("Hello")
```
Notice the space before `print`? That is called **Indentation** (usually 4 spaces or 1 Tab).

In other languages (like C++ or Java), they use curly braces `{ }` to group code. 
Python uses **Indentation**.

If you forget it, Python will crash and cry: `IndentationError`.

### Super Memory Trick
`Indentation = Belonging`
If a line is indented under an `if` statement, it *belongs* to that `if` statement.

---

# 🎮 Decision Detective Game

Will this print anything?
```python
is_raining = False

if is_raining:
    print("Take an umbrella")
```
Answer: **No.** (The condition is False, and there is no `else`).

---

Will this print "Yes" or "No"?
```python
x = 10
if x > 5:
    print("Yes")
else:
    print("No")
```
Answer: **Yes.**

---

# 🧠 The 5 Second Rule

Only `if`? ➡ Just one condition.
`if` and `else`? ➡ Condition + Backup Plan.
`elif`? ➡ Checking multiple conditions one by one.

---

# 🚀 Cheat Sheet

```python
# Comparison Operators you will use often:
a == b  # Equals
a != b  # Not Equals
a > b   # Greater than
a < b   # Less than
a >= b  # Greater than or equal to
a <= b  # Less than or equal to
```

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
x = 10
if x > 20:
    print("Apple")
elif x == 10:
    print("Banana")
else:
    print("Cherry")
```

**Snippet 2:**
```python
is_vip = True
if is_vip:
    print("Enter VIP Lounge")
print("Enjoy the party")
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `Banana`
(Python checks `x > 20` -> False. Then checks `elif x == 10` -> True! It stops there.)

**Snippet 2 Answer:**
```text
Enter VIP Lounge
Enjoy the party
```
(Why both? Because `print("Enjoy the party")` is NOT indented! It runs no matter what.)