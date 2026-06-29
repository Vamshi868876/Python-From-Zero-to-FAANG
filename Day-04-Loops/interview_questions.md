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
