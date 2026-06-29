# 💼 Interview Questions: Conditionals

## What is an IndentationError?
Python uses whitespace (indentation) to define blocks of code (like what belongs inside an `if` statement). If you forget to indent, or mix spaces and tabs improperly, Python throws an `IndentationError`. In other languages like Java or C++, curly braces `{}` define blocks, so indentation is just for readability. In Python, indentation is mandatory syntax.

---

## What is the difference between multiple `if` statements and using `if-elif`?
If you use multiple `if` statements, Python will evaluate **every single condition**, even if the first one is true. 
If you use `if-elif-else`, Python stops checking conditions as soon as it finds the first `True` condition. This makes `elif` much more efficient when checking mutually exclusive conditions.

---

## What are "Falsy" values in Python?
In Python, you don't always have to compare a variable to `True` or `False`. You can just say `if variable:`. 
Certain values automatically evaluate to `False` (these are called Falsy values).
The Falsy values are:
- `False`
- `0` (integer zero)
- `0.0` (float zero)
- `""` (empty string)
- `None`
- `[]`, `{}`, `()` (empty lists, dicts, tuples)

Everything else evaluates to `True`.

---

## What is a Ternary Operator in Python?
It is a one-line shorthand for an `if-else` statement. 
Example:
```python
# Normal
if score > 50:
    result = "Pass"
else:
    result = "Fail"

# Ternary (One line)
result = "Pass" if score > 50 else "Fail"
```
