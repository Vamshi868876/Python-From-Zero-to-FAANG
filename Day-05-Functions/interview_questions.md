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
