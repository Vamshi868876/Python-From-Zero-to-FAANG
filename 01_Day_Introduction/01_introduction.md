# Day 1 - Introduction to Python

## 1. Learning Objectives
By the end of this lesson, you will be able to:
- Understand what Python is and why it's the most popular language in AI/ML.
- Set up your Python programming environment.
- Write and execute your first Python script.
- Understand the basic syntax and how Python reads your code.

## 2. Baby Version 👶🐣
Imagine you have a robot friend named **Python**. 🤖

Right now, your robot doesn't know how to do anything. But you have a magic notebook! 
Whenever you write a command in the notebook (like "Say Hello"), the robot reads it and does exactly what you wrote.

In programming, writing `print("Hello")` is exactly like writing in that magic notebook. You are just giving your robot instructions!

## 3. Beginner Version 🧑‍🎓
Python is a high-level programming language. "High-level" just means it is closer to human language (English) than computer language (1s and 0s). 
Because it is so easy to read, programmers love it for building websites, automating boring tasks, and creating Artificial Intelligence (AI).

To start writing Python, you just need to:
1. Install Python on your computer.
2. Open a text editor (like VS Code).
3. Type `print("Hello, World!")` and run it.

## 4. Interview Version 💼
**Python** is an interpreted, high-level, dynamically typed, and garbage-collected programming language. It emphasizes code readability with its use of significant indentation. Its comprehensive standard library and massive third-party ecosystem (PyPI) make it the industry standard for data science, machine learning, and backend infrastructure at companies like Google, Meta, and Netflix.

## 5. Syntax
The syntax is the "grammar" of a programming language.

```python
print("Hello, World!")
```
- `print`: A built-in function that tells Python to output something to the screen.
- `()` : Parentheses hold the data you are passing to the function.
- `" "` : Quotes tell Python that the data is text (a string).

## 6. Code Examples

### Basic Example: Your First Program
```python
# This is a comment. Python ignores it!
print("Hello, Python learners!")
```

### Intermediate Example: Math
```python
print(2 + 3)    # Addition: Outputs 5
print(10 - 2)   # Subtraction: Outputs 8
print(4 * 2)    # Multiplication: Outputs 8
```

## 7. Common Mistakes

❌ **Wrong Code:**
```python
print "Hello World"  # Missing parentheses (This worked in Python 2, but not Python 3!)
Print("Hello")       # Capital 'P' in print (Python is case-sensitive)
```

✅ **Correct Code:**
```python
print("Hello World")
```

## 8. Visual Memory Tricks 🧠
- **Python = A Snake** 🐍 (The logo is two snakes!).
- **Syntax = Grammar**. Just like English needs periods and commas, Python needs parentheses and quotes.
- `print()` = A megaphone 📣. It yells out whatever you put inside the parentheses.

## 9. Interview Questions

### Beginner Question
**Q: Is Python a compiled or interpreted language?**
**A:** Python is primarily an interpreted language. The source code is compiled into bytecode (`.pyc` files), which is then immediately executed by the Python Virtual Machine (PVM).

### FAANG-Level Question
**Q: What is the Global Interpreter Lock (GIL) in Python?**
**A:** The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once. This lock is necessary mainly because CPython's memory management is not thread-safe.

## 10. Practice Problems

**Easy:**
Write a Python script that prints your name and your favorite food on two separate lines.

**Medium:**
Write a Python script that prints the result of `50` multiplied by `50`.

**Hard:**
Print a multi-line string (a paragraph) using a single `print` statement. (Hint: Research how to use triple quotes `"""`).

## 11. Mini Project
**ASCII Art Maker**
Using multiple `print()` statements, draw a simple cat or dog using text characters (ASCII art).

Example:
```python
print(" /\\_/\\ ")
print("( o.o )")
print(" > ^ < ")
```

## 12. Cheat Sheet
```python
# Comments start with a hash symbol
print("Hello")      # Prints text
print(5 + 5)        # Prints numbers
```

## 13. Key Takeaways
1. Python is readable and beginner-friendly.
2. `print()` is your best friend for seeing outputs.
3. Python is case-sensitive (`print` is not the same as `Print`).
