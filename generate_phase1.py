import os

def create_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# ==============================================================================
# DAY 4: LOOPS
# ==============================================================================
d4_readme = """
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
"""

d4_examples = """
# ==============================
# LOOPS EXAMPLES
# ==============================

# Example 1: The 'for' Loop with range
print("--- FOR LOOP ---")
for i in range(5):
    print(f"Count: {i}")

# Example 2: The 'while' Loop
print("\\n--- WHILE LOOP ---")
battery = 100
while battery > 90:
    print(f"Battery at {battery}%. Phone is running.")
    battery -= 5
print("Battery low!")

# Example 3: The 'break' Statement
print("\\n--- BREAK ---")
for i in range(10):
    if i == 4:
        print("Hit number 4! Breaking out!")
        break
    print(i)

# Example 4: The 'continue' Statement
print("\\n--- CONTINUE ---")
for i in range(5):
    if i == 2:
        print("Skipping 2!")
        continue
    print(i)
"""

d4_exercises = """
# 🎯 Loops Playground

## Level 1: Easy

### Challenge 1
Write a `for` loop that prints your name 5 times.

---

### Challenge 2
Write a `while` loop that starts at `count = 10` and counts down to 1. 
Print "Happy New Year!" at the end.

---

## Level 2: Medium

### Challenge 3 (Multiplication Table)
Use a `for` loop to print the multiplication table of 5 (e.g., 5 x 1 = 5, 5 x 2 = 10 ... up to 10).

---

### Challenge 4 (Skip the Odds)
Write a `for` loop from 1 to 10. Use the `continue` statement to skip all odd numbers, printing only the even ones.

---

## Boss Challenge 👑 (FizzBuzz)
This is a famous FAANG interview question!
Write a loop from 1 to 20.
- If the number is divisible by 3, print "Fizz".
- If the number is divisible by 5, print "Buzz".
- If the number is divisible by both 3 AND 5, print "FizzBuzz".
- Otherwise, just print the number.
"""

d4_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
for i in range(5):
    print("Rahul")

# Challenge 2
count = 10
while count > 0:
    print(count)
    count -= 1
print("Happy New Year!")

# Challenge 3
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Challenge 4
for i in range(1, 11):
    if i % 2 != 0: # If it is odd
        continue
    print(i)

# Boss Challenge (FizzBuzz)
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""

d4_interview = """
# 💼 Interview Questions: Loops

## What is an infinite loop and how do you stop it?
An infinite loop occurs when a `while` loop's condition never becomes False. It runs forever and crashes the program. 
You can stop it programmatically using a `break` statement, or manually by pressing `Ctrl + C` in the terminal (KeyboardInterrupt).

---

## What is the difference between a `for` loop and a `while` loop?
A `for` loop is used for **definite iteration**, meaning you know exactly how many times the loop should run (e.g., looping over a list of items or a specific `range`). 
A `while` loop is used for **indefinite iteration**, meaning it runs until a specific condition changes.

---

## Does Python have a `do-while` loop?
No. Unlike C++ or Java, Python does not have a built-in `do-while` loop (which guarantees the code runs at least once before checking the condition). To mimic it in Python, you must use a `while True:` loop and put an `if condition: break` at the end of the block.

---

## What does the `else` block do in a Python loop?
This is a Python-specific feature! You can put an `else` block after a `for` or `while` loop. 
The `else` block will execute **ONLY IF** the loop finishes naturally (meaning it did not hit a `break` statement). It is often used in search algorithms (e.g., loop through items, if found -> break; else -> print "not found").
"""

# ==============================================================================
# DAY 5: FUNCTIONS
# ==============================================================================
d5_readme = """
# 🐍 Day 05: Functions (Reusable Machines)

# 🤔 Imagine This...

You want to make a cup of coffee. ☕
You don't build a coffee machine from scratch every single time you want a cup.
You build the machine **ONCE**, and then you just press a button whenever you need coffee.

In coding, if you write a chunk of code that does something useful, you don't want to copy-paste it 100 times.
You want to package it into a "machine" and just press a button.

In Python, this machine is called a **Function**.

---

# 👶🐣 Baby Version

Imagine a **Juicer Machine**. 🍎⚙️🥤

**The Machine:** The Juicer (Function)
**Input:** You put an Apple in (Arguments)
**Process:** The blades spin (Code execution)
**Output:** Apple Juice comes out (Return value)

```python
def juicer(fruit):
    juice = fruit + " Juice"
    return juice
```
When we want juice, we just "call" the machine:
```python
my_drink = juicer("Apple")
print(my_drink) # Apple Juice
```

---

# 🏗️ How to Build a Function (Syntax)

To build a function in Python, we use the `def` keyword (which stands for **Define**).

```python
# 1. Define the machine
def greet(name):
    print("Hello", name)

# 2. Use (call) the machine
greet("Rahul")
greet("Vamshi")
```

---

# 📥 Arguments vs 📤 Return

## Arguments (Input)
Arguments are the raw materials you feed into the machine. 
In `def add(a, b):`, `a` and `b` are the arguments.

## Return (Output)
`print()` just shows text on the screen. It doesn't give data back to the program.
If you want the machine to actually hand you back a result that you can save in a variable, you MUST use `return`.

```python
def multiply(a, b):
    result = a * b
    return result  # Hands the result back!

# We can save the returned value in a variable!
answer = multiply(5, 10)
print(answer) # 50
```

---

# 🚨 Variable Scope (The Magic Las Vegas Rule)

**"What happens in the function, stays in the function."**

Variables created *inside* a function cannot be seen from the outside. They are called **Local Variables**.

```python
def secret_room():
    hidden_treasure = 1000

print(hidden_treasure) # ❌ ERROR! Python doesn't know what this is outside the function!
```

---

# 🧠 The 5 Second Rule

`def` ➡ Used to create the machine.
`()` ➡ The mouth where you feed the inputs (arguments).
`return` ➡ The dispenser where the final product comes out.

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
def say_hi():
    print("Hi!")

say_hi()
say_hi()
```

**Snippet 2:**
```python
def add_ten(num):
    return num + 10

x = add_ten(5)
print(x)
```

**Snippet 3:**
```python
def do_nothing(a):
    a = a + 5

my_num = 10
do_nothing(my_num)
print(my_num)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:**
```text
Hi!
Hi!
```
(We built the machine, and then pressed the button twice).

**Snippet 2 Answer:** `15`
(5 goes in, 15 comes out, gets saved in x, and printed).

**Snippet 3 Answer:** `10`
(Trick question! The function `do_nothing` modifies `a` inside, but doesn't `return` anything. The original `my_num` outside stays exactly the same!)
"""

d5_examples = """
# ==============================
# FUNCTIONS EXAMPLES
# ==============================

# Example 1: A simple function (No arguments)
def say_hello():
    print("Hello from the function!")

say_hello()

# Example 2: Function with Arguments
def greet_person(name):
    print(f"Welcome, {name}!")

greet_person("Rahul")
greet_person("Vamshi")

# Example 3: Function with Return
def calculate_area(length, width):
    area = length * width
    return area

my_room_area = calculate_area(10, 5)
print(f"Area is {my_room_area} sq meters.")

# Example 4: Default Arguments
# If we don't provide a country, it defaults to 'India'
def user_info(name, country="India"):
    print(f"{name} is from {country}")

user_info("Rahul")          # Uses default
user_info("Alex", "USA")    # Overrides default

# Example 5: Multiple Return Values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = get_min_max([10, 20, 5, 100])
print("Min:", lowest)
print("Max:", highest)
"""

d5_exercises = """
# 🎯 Functions Playground

## Level 1: Easy

### Challenge 1
Write a function called `print_my_name()` that simply prints your name. Then call the function.

---

### Challenge 2
Write a function called `subtract(a, b)` that takes two numbers, subtracts `b` from `a`, and **returns** the result.
Print the result of `subtract(10, 3)`.

---

## Level 2: Medium

### Challenge 3 (Even or Odd Machine)
Write a function called `is_even(number)`.
If the number is even, **return** `True`. If it is odd, **return** `False`.
*(Hint: Use the modulo operator `%`)*

---

### Challenge 4 (Greeting with Default)
Write a function called `welcome(name, message="Welcome back!")`.
It should print `"{name}, {message}"`.
Call it once using only a name, and once providing a custom message.

---

## Boss Challenge 👑 (The Calculator)
Write a single function called `calculator(num1, num2, operation)`.
- If operation is "+", return num1 + num2
- If operation is "-", return num1 - num2
- If operation is "*", return num1 * num2
- If operation is "/", return num1 / num2
- If it's anything else, return "Invalid Operation"
"""

d5_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
def print_my_name():
    print("Rahul")

print_my_name()

# Challenge 2
def subtract(a, b):
    return a - b

print(subtract(10, 3))

# Challenge 3
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
# Shorthand pro-way for Challenge 3:
# def is_even(number):
#     return number % 2 == 0

# Challenge 4
def welcome(name, message="Welcome back!"):
    print(f"{name}, {message}")

welcome("Rahul")
welcome("Vamshi", "Good Morning!")

# Boss Challenge
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))
"""

d5_interview = """
# 💼 Interview Questions: Functions

## What is the difference between a parameter and an argument?
- A **Parameter** is the variable listed inside the parentheses in the function definition (e.g., `def greet(name):`).
- An **Argument** is the actual value that is sent to the function when it is called (e.g., `greet("Rahul")`).

---

## What is the difference between `print()` and `return`?
`print()` simply displays a value on the console for the human to read. It evaluates to `None` in the code.
`return` passes a value back to the caller in the code so it can be saved in a variable, used in math, or passed to another function. If a function doesn't have a `return` statement, it automatically returns `None`.

---

## Explain Local Scope vs Global Scope.
- **Global Scope:** Variables defined outside of any function. They can be accessed from anywhere in the file.
- **Local Scope:** Variables defined inside a function. They are destroyed as soon as the function finishes executing, and cannot be accessed from outside the function.

---

## What are `*args` and `**kwargs`?
They are used to pass a variable number of arguments to a function.
- `*args` (Non-Keyword Arguments): Allows you to pass any number of positional arguments. Inside the function, they are wrapped in a Tuple.
- `**kwargs` (Keyword Arguments): Allows you to pass any number of named arguments (e.g., `name="Rahul", age=21`). Inside the function, they are wrapped in a Dictionary.
"""

# ==============================================================================
# DAY 6: STRINGS
# ==============================================================================
d6_readme = """
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
"""

d6_examples = """
# ==============================
# STRINGS EXAMPLES
# ==============================

# Example 1: Indexing
text = "HELLO"
print("First letter:", text[0])  # H
print("Last letter:", text[-1])  # O (Negative index counts from the end!)

# Example 2: Slicing
word = "PYTHON"
print("First 3 letters:", word[0:3]) # PYT
print("Reverse:", word[::-1])        # NOHTYP

# Example 3: String Methods
sentence = "i love python programming"
print("Upper:", sentence.upper())
print("Title:", sentence.title()) # Capitalizes every word
print("Replace:", sentence.replace("python", "java"))

# Example 4: Splitting a string into a list of words
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print("Split result:", fruits)

# Example 5: F-Strings
name = "Vamshi"
score = 99
print(f"Player {name} achieved a score of {score}!")
"""

d6_exercises = """
# 🎯 Strings Playground

## Level 1: Easy

### Challenge 1
Create a variable `word = "SUPERMAN"`.
Use indexing to print the letter "P".

---

### Challenge 2
Use slicing on `word = "SUPERMAN"` to extract and print just "SUPER".

---

## Level 2: Medium

### Challenge 3 (The Shouter)
Write a function `shout(text)` that takes a string, converts it to fully UPPERCASE, and adds "!!!" at the end using an f-string.
Example: `shout("hello")` -> `"HELLO!!!"`

---

### Challenge 4 (Palindrome Checker)
A palindrome is a word that reads the same forwards and backwards (e.g., "racecar").
Write a function `is_palindrome(word)` that returns `True` if a word is a palindrome, and `False` if it isn't.
*(Hint: Use the `[::-1]` trick!)*

---

## Boss Challenge 👑 (Word Counter)
Create a string: `text = "apple banana apple cherry banana apple"`
Use string methods to count how many times the word "apple" appears in the text, and print the result in a nice f-string.
"""

d6_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
word = "SUPERMAN"
print(word[2]) # P

# Challenge 2
print(word[0:5]) # SUPER

# Challenge 3
def shout(text):
    return f"{text.upper()}!!!"

print(shout("hello"))

# Challenge 4
def is_palindrome(word):
    # Check if the word is equal to its reversed version
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("racecar")) # True
print(is_palindrome("python"))  # False

# Boss Challenge
text = "apple banana apple cherry banana apple"
apple_count = text.count("apple")
print(f"The word 'apple' appears {apple_count} times.")
"""

d6_interview = """
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
"""

def generate():
    # Day 4
    d4_path = os.path.join("Day-04-Loops")
    os.makedirs(d4_path, exist_ok=True)
    create_file(os.path.join(d4_path, "README.md"), d4_readme)
    create_file(os.path.join(d4_path, "examples.py"), d4_examples)
    create_file(os.path.join(d4_path, "exercises.md"), d4_exercises)
    create_file(os.path.join(d4_path, "solutions.py"), d4_solutions)
    create_file(os.path.join(d4_path, "interview_questions.md"), d4_interview)

    # Day 5
    d5_path = os.path.join("Day-05-Functions")
    os.makedirs(d5_path, exist_ok=True)
    create_file(os.path.join(d5_path, "README.md"), d5_readme)
    create_file(os.path.join(d5_path, "examples.py"), d5_examples)
    create_file(os.path.join(d5_path, "exercises.md"), d5_exercises)
    create_file(os.path.join(d5_path, "solutions.py"), d5_solutions)
    create_file(os.path.join(d5_path, "interview_questions.md"), d5_interview)

    # Day 6
    d6_path = os.path.join("Day-06-Strings")
    os.makedirs(d6_path, exist_ok=True)
    create_file(os.path.join(d6_path, "README.md"), d6_readme)
    create_file(os.path.join(d6_path, "examples.py"), d6_examples)
    create_file(os.path.join(d6_path, "exercises.md"), d6_exercises)
    create_file(os.path.join(d6_path, "solutions.py"), d6_solutions)
    create_file(os.path.join(d6_path, "interview_questions.md"), d6_interview)

if __name__ == "__main__":
    generate()
    print("Phase 1 generated successfully.")
