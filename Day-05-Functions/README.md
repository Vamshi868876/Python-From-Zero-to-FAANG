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
