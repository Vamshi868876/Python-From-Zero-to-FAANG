# Day 2 - Variables, Data Types & Built-in Functions

## 1. Learning Objectives
By the end of this lesson, you will be able to:
- Understand what variables are and how they store data in memory.
- Identify and use basic Python data types: Integers, Floats, Strings, and Booleans.
- Write clean and readable variable names using Python conventions.
- Use built-in functions like `print()`, `type()`, and `len()`.

## 2. Baby Version 👶🐣
Imagine Python is a giant **toy room**. 🎈

**📦 Variable = Toy Box**
You have a toy box.
On the outside of the box, you stick a label with a **NAME**.
Inside the box, you keep a **TOY** (your data).

If you write `name = "Rahul"`, it means:
- 📦 Box name = `name`
- 🎁 Inside = `Rahul`

**Data Types:**
- 🍎 **Integer (int):** Whole numbers. Like counting apples: 1, 2, 3. (No dot)
- 🥛 **Float:** Numbers with a dot. Like measuring milk: 1.5 liters. (Dot = Float)
- 🐱 **String (str):** Words or text. Like your pet's name: "Tom". (Always in quotes `" "`)
- 🚦 **Boolean (bool):** Only 2 answers. Is the light on? `True` (Yes) or `False` (No).

## 3. Beginner Version 🧑‍🎓
In programming, a **variable** is a container for storing data values. A **Data Type** specifies what kind of value a variable holds. Python is dynamically typed, meaning you don't have to declare the type; Python figures it out automatically!

```python
# Creating variables with different data types
age = 25              # This is an integer (int)
price = 19.99         # This is a float (float)
city = "New York"     # This is a string (str)
is_raining = False    # This is a boolean (bool)
```

## 4. Interview Version 💼
**Variables** in Python are symbolic names that act as references or pointers to objects in memory. When you assign a value to a variable, Python creates an object in memory and binds the variable name to that object.
The four primitive data types in Python are `int`, `float`, `str`, and `bool`. Python uses dynamic typing and reference counting for memory management.

## 5. Syntax
```python
variable_name = value
```
- `variable_name`: The name you choose (must start with a letter or underscore).
- `=`: The assignment operator (binds the value to the name).
- `value`: The data you are storing.

## 6. Code Examples

### Basic Examples
```python
first_name = "Alice"
age = 30
print(first_name) # Output: Alice
print(age)        # Output: 30
```

### Built-in Functions Examples
```python
# Using type() to check what kind of data we have
number = 42
text = "Python"

print(type(number))    # Output: <class 'int'>
print(type(text))      # Output: <class 'str'>

# Using len() to find the length of a string
print(len(text))       # Output: 6
```

## 7. Common Mistakes

❌ **Wrong Code:**
```python
# 1. Variable name starting with a number
1st_place = "John"

# 2. Using spaces in variable names
my age = 25

# 3. Forgetting quotes for strings
name = Rahul
```

✅ **Correct Code:**
```python
# 1. Start with a letter or underscore
first_place = "John"

# 2. Use underscores (snake_case) instead of spaces
my_age = 25

# 3. Always use quotes for strings
name = "Rahul"
```

## 8. Visual Memory Tricks 🧠
| See This | Think This | Type |
| --- | --- | --- |
| `10` | No Dot | `int` |
| `3.14` | Has Dot | `float` |
| `"Hello"` | Inside Quotes | `str` |
| `True` | Yes/No | `bool` |

**Rule of Thumb for Naming:** `snake_case_is_best_case`.

## 9. Interview Questions

### Beginner Question
**Q: How do you find the data type of a variable in Python?**
**A:** You use the built-in `type()` function. Example: `print(type(my_var))`.

### FAANG-Level Question
**Q: How does Python handle memory allocation for small integers?**
**A:** Python pre-allocates an array of small integers from `-5` to `256` during initialization. If two variables are assigned the same integer within this range, they will point to the exact same object in memory (reference the same ID). This is known as "integer caching" or "interning", which optimizes memory usage.

## 10. Practice Problems

**Easy:**
Create four variables representing your own: Name, Age, Height (in meters), and if you like coffee (True/False). Print them all.

**Medium:**
Write a script that uses `len()` to find the length of your first name, and print the result.

**Hard:**
Write a program that defines two variables, `a = 10` and `b = 20`. Swap their values without creating a third variable. (Hint: Python has a special syntax for this).

## 11. Mini Project
**Coffee Shop Receipt Generator**
Create a small script that defines variables for a coffee order:
- Customer name
- Coffee type
- Price
- Quantity
- Is it a takeaway? (Boolean)

Calculate the total price (Price * Quantity) and print a nice receipt using the variables.

## 12. Cheat Sheet
```python
# Assignment
x = 5

# Check type & length
type(10)      # <class 'int'>
len("Hello")  # 5

# Naming Rules:
# 1. Must start with letter or _
# 2. Case-sensitive (age vs Age)
# 3. Standard is snake_case (my_variable_name)
```

## 13. Key Takeaways
1. Variables are named boxes that hold data.
2. `int`, `float`, `str`, and `bool` are the building blocks of data.
3. Always name variables descriptively using `snake_case`.
4. Built-in functions like `print()`, `type()`, and `len()` are ready to use anytime.
