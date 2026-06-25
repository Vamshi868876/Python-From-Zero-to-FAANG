# Day 1 - Variables & Data Types

## 1. Learning Objectives
By the end of this lesson, you will be able to:
- Understand what variables are and how they store data in memory.
- Identify and use basic Python data types: Integers, Floats, Strings, and Booleans.
- Write clean and readable variable names using Python conventions.
- Check the data type of any variable using the `type()` function.

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
- 🍎 **Integer (int):** Whole numbers. Like counting apples: 1, 2, 3, 4, 5. (No dot)
- 🥛 **Float:** Numbers with a dot. Like measuring milk: 1.5 liters. (Dot = Float)
- 🐱 **String (str):** Words or text. Like your pet's name: "Tom". (Always in quotes `" "`)
- 🚦 **Boolean (bool):** Only 2 answers. Is the light on? `True` (Yes) or `False` (No).

## 3. Beginner Version 🧑‍🎓
In programming, a **variable** is a container for storing data values. Unlike some other languages, Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.

A **Data Type** specifies what kind of value a variable holds. Python is dynamically typed, meaning you don't have to declare the type; Python figures it out automatically!

```python
# Creating variables with different data types
age = 25              # This is an integer (int)
price = 19.99         # This is a float (float)
city = "New York"     # This is a string (str)
is_raining = False    # This is a boolean (bool)
```

## 4. Interview Version 💼
**Variables** in Python are symbolic names that act as references or pointers to objects in memory. When you assign a value to a variable, Python creates an object in memory and binds the variable name to that object.
**Data Types** are classes, and variables are instances (objects) of these classes. The four primitive data types in Python are `int`, `float`, `str`, and `bool`. Python uses dynamic typing and reference counting for memory management.

## 5. Syntax
The syntax for assigning a variable is straightforward:
```python
variable_name = value
```
- `variable_name`: The name you choose (must start with a letter or underscore, no spaces).
- `=`: The assignment operator (binds the value to the name).
- `value`: The data you are storing.

Line by line breakdown:
```python
score = 100
# 1. 'score' is the identifier (variable name).
# 2. '=' is the assignment operator.
# 3. '100' is the integer object created in memory.
```

## 6. Code Examples

### Basic Examples
```python
# Just storing simple values
first_name = "Alice"
age = 30
print(first_name) # Output: Alice
print(age)        # Output: 30
```

### Intermediate Examples (Type Checking)
```python
# Using type() to check what kind of data we have
number = 42
pi = 3.14159
text = "Python is awesome"
is_active = True

print(type(number))    # Output: <class 'int'>
print(type(pi))        # Output: <class 'float'>
print(type(text))      # Output: <class 'str'>
print(type(is_active)) # Output: <class 'bool'>
```

### Real-world Example (User Profile)
```python
# Simulating a user profile in a database
user_id = 10459
username = "coder_vamsi"
account_balance = 450.75
is_premium_member = True

print("User Profile:")
print("ID:", user_id)
print("Username:", username)
print("Balance: $", account_balance)
print("Premium:", is_premium_member)
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

### Intermediate Question
**Q: Can a variable change its data type in Python?**
**A:** Yes, because Python is dynamically typed. A variable can hold an integer, and in the next line, it can be assigned a string.
```python
x = 10       # x is an int
x = "Hello"  # x is now a str
```

### FAANG-Level Question
**Q: How does Python handle memory allocation for small integers?**
**A:** Python pre-allocates an array of small integers from `-5` to `256` during initialization. If two variables are assigned the same integer within this range, they will point to the exact same object in memory (reference the same ID). This is known as "integer caching" or "interning", which optimizes memory usage.

## 10. Practice Problems

**Easy:**
Create four variables representing your own: Name, Age, Height (in meters), and if you like coffee (True/False). Print them all.

**Medium:**
Fix this code so it runs without errors:
```python
my-name = "Alex"
2nd_number = 50
print = True
```

**Hard:**
Write a program that defines two variables, `a = 10` and `b = 20`. Swap their values without creating a third variable. (Hint: Python has a special syntax for this: `a, b = b, a`).

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

# Data Types
int_val = 10        # Whole number
float_val = 10.5    # Decimal
str_val = "Hello"   # Text
bool_val = True     # True / False

# Check type
type(int_val) # <class 'int'>

# Variable naming rules:
# 1. Must start with letter or _
# 2. Can only contain alpha-numeric and _
# 3. Case-sensitive (age vs Age)
# 4. Standard is snake_case (my_variable_name)
```

## 13. Key Takeaways
1. Variables are named boxes that hold data.
2. Python has dynamic typing (no need to declare types).
3. `int`, `float`, `str`, and `bool` are the building blocks of data.
4. Always name variables descriptively using `snake_case`.
