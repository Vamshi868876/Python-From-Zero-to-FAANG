# Functions

## Definition
A function is a reusable block of code that performs a specific task.

## Syntax

```python
def greet():
    print("Hello")
```

## Example

```python
def greet(name):
    return f"Hello {name}"

print(greet("Ram"))
```

## Common Mistakes
- Not returning a value when needed.
- Using mutable default arguments like lists or dictionaries.

## Interview Question
- What is the difference between `*args` and `**kwargs`?
- How do you write a lambda function?

## Practice Problems
- Write a function to check if a number is prime.
- Write a function to return the factorial of a number.
