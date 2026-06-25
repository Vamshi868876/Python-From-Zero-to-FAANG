# 💼 Interview Questions: Data Types

## How does Python know the data type of a variable?
Python is dynamically typed. This means you do not have to explicitly declare the data type (like `int x = 10` in C++ or Java). Python automatically infers the data type based on the value you assign to it during runtime.

---

## What is the difference between `100` and `"100"`?
`100` is an **Integer**, which means Python can perform mathematical operations on it (like addition, multiplication).
`"100"` is a **String**, which means Python treats it as raw text. If you try to add `"100" + "100"`, Python will concatenate them to give `"100100"`, not `200`.

---

## How can you check the data type of a variable in Python?
You can use the built-in `type()` function.
```python
x = 10.5
print(type(x)) # Output: <class 'float'>
```

---

## Are Data Types objects in Python?
Yes! In Python, everything is an object. When you assign `x = 10`, `x` is a reference pointing to an integer object in memory containing the value `10`. Data types are actually classes, and variables are instances of those classes.
