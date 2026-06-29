import os

def create_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# ==============================================================================
# DAY 7: LISTS
# ==============================================================================
d7_readme = """
# 🐍 Day 07: Lists (The Magic Backpack)

# 🤔 Imagine This...

You are going to school. You have:
- A pen
- A book
- A laptop
- An apple

Do you carry them one by one in your hands?
❌ **No!** You put them all in a **Backpack**.

In Python, a **List** is exactly like a backpack. It is a single container where you can store many different items.

---

# 👶🐣 Baby Version

A list is just a box with dividers.
You can put anything in it: Numbers, Text, or even other boxes!
```python
backpack = ["Pen", "Book", "Laptop", "Apple"]
```
Python numbers the slots in the box starting from **0**.

Slot 0: `"Pen"`
Slot 1: `"Book"`
Slot 2: `"Laptop"`

If you want the book, you just ask for Slot 1:
```python
print(backpack[1]) # "Book"
```

---

# 🪄 Lists are MUTABLE (You can change them!)

This is the most important thing about lists.
Unlike strings (which you cannot change once made), lists are **Mutable**. You can take things out, put new things in, or replace things!

```python
backpack = ["Pen", "Book", "Apple"]

# 1. Replace an item (Swap Apple for Orange)
backpack[2] = "Orange"

# 2. Add a new item at the end
backpack.append("Water Bottle")

# 3. Take the last item out
backpack.pop()
```

---

# 🛠️ Important List Tools (Methods)

- `append(item)`: Adds an item to the end of the list.
- `insert(index, item)`: Sneaks an item into a specific spot.
- `remove(item)`: Finds and deletes the first match.
- `pop()`: Removes and returns the last item (like taking the top book off a stack).
- `sort()`: Sorts the list (A-Z or smallest to largest).

---

# 🧠 The 5 Second Rule

Square brackets `[]`? ➡ **List**
Can I change it? ➡ **Yes (Mutable)**
Add something? ➡ **`.append()`**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
nums = [10, 20, 30]
nums[1] = 99
print(nums)
```

**Snippet 2:**
```python
fruits = ["Apple", "Banana"]
fruits.append("Cherry")
print(fruits)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `[10, 99, 30]`
(We replaced index 1).

**Snippet 2 Answer:** `["Apple", "Banana", "Cherry"]`
(Append always adds to the end!)
"""

d7_examples = """
# ==============================
# LISTS EXAMPLES
# ==============================

# Example 1: Creating and Accessing
movies = ["Inception", "Interstellar", "Dune"]
print("First movie:", movies[0])
print("Last movie:", movies[-1])

# Example 2: Modifying a List
movies[0] = "Batman"
print("Modified movies:", movies)

# Example 3: Adding items
movies.append("Spider-Man") # Adds to end
movies.insert(1, "Iron Man") # Inserts at index 1
print("After adding:", movies)

# Example 4: Removing items
movies.remove("Dune") # Removes by name
last_item = movies.pop() # Removes and grabs last item
print("Popped item:", last_item)
print("After removing:", movies)

# Example 5: Sorting
numbers = [42, 10, 5, 99, 1]
numbers.sort()
print("Sorted numbers:", numbers)
"""

d7_exercises = """
# 🎯 Lists Playground

## Level 1: Easy

### Challenge 1
Create a list called `colors` containing "Red", "Green", and "Blue".
Print the second color.

---

### Challenge 2
Add "Yellow" to the end of the `colors` list. Print the list.

---

## Level 2: Medium

### Challenge 3 (The Swapper)
Given `scores = [10, 20, 30, 40]`, change the `30` to `99` using its index.

---

### Challenge 4 (List Slicing)
Just like strings, lists can be sliced!
Given `alphabet = ["A", "B", "C", "D", "E"]`, print only `["B", "C", "D"]`.

---

## Boss Challenge 👑 (The Shopping Cart)
1. Create an empty list called `cart = []`.
2. Append "Milk", "Bread", and "Eggs" to the cart.
3. You forgot you are vegan. Remove "Eggs".
4. Add "Tofu" at the very beginning of the cart (index 0).
5. Print the final cart.
"""

d7_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
colors = ["Red", "Green", "Blue"]
print(colors[1])

# Challenge 2
colors.append("Yellow")
print(colors)

# Challenge 3
scores = [10, 20, 30, 40]
scores[2] = 99
print(scores)

# Challenge 4
alphabet = ["A", "B", "C", "D", "E"]
print(alphabet[1:4])

# Boss Challenge
cart = []
cart.append("Milk")
cart.append("Bread")
cart.append("Eggs")

cart.remove("Eggs")
cart.insert(0, "Tofu")

print(cart)
"""

d7_interview = """
# 💼 Interview Questions: Lists

## What is the difference between `append()` and `extend()`?
- `append()` adds its argument as a **single element** to the end of a list. (If you append a list to a list, you get a list inside a list).
- `extend()` iterates over its argument and adds each element to the list, effectively merging them.

## Are lists Mutable?
Yes. Lists are mutable, meaning their contents can be altered after creation (items can be modified, added, or removed in-place).

## What is List Comprehension?
It is a concise way to create lists. Instead of doing:
```python
squares = []
for i in range(5):
    squares.append(i**2)
```
You can do it in one line:
`squares = [i**2 for i in range(5)]`

## What is the time complexity of `pop(0)` versus `pop()`?
- `pop()` removes the last element and is **O(1)** (very fast).
- `pop(0)` removes the first element and is **O(N)** (slow). This is because Python has to shift every single other element in the list one space to the left to fill the gap. (In FAANG interviews, if you need to pop from the left frequently, use `collections.deque`).
"""

# ==============================================================================
# DAY 8: TUPLES
# ==============================================================================
d8_readme = """
# 🐍 Day 08: Tuples (The Locked Box)

# 🤔 Imagine This...

Yesterday we learned about Lists (The Backpack). You can add and remove things.
But what if you have data that should **NEVER** be changed? 

For example, the GPS coordinates of your house: `(17.3850, 78.4867)`
If someone accidentally changes these coordinates in the code, your delivery will go to another city!

To lock data so it cannot be modified, Python uses **Tuples**.

---

# 👶🐣 Baby Version

A Tuple is a glass box locked with a key. 🔒
You can look inside and see the items.
But you **cannot** add new items. You **cannot** remove items. You **cannot** change items.

```python
# Tuples use parentheses ()
coordinates = (17.38, 78.48)

print(coordinates[0]) # 17.38 (You can look at it!)
coordinates[0] = 99.9 # ❌ ERROR! The box is locked!
```

---

# 📦 Packing and Unpacking (The Coolest Feature)

Python lets you "pack" multiple items into a tuple, and instantly "unpack" them into separate variables!

```python
# Packing
user_data = ("Rahul", 21, "Hyderabad")

# Unpacking (Assigning to 3 variables at once!)
name, age, city = user_data

print(name) # Rahul
print(city) # Hyderabad
```

---

# 🧠 The 5 Second Rule

Parentheses `()`? ➡ **Tuple**
Can I change it? ➡ **NO! (Immutable)**
Why use it? ➡ **Faster than lists, and safer for fixed data.**

---

# 🧠 Can You Predict?

Look at the following code snippets. Predict the output before scrolling down!

**Snippet 1:**
```python
my_tuple = (10, 20, 30)
my_tuple.append(40)
```

**Snippet 2:**
```python
a, b = (5, 10)
print(a + b)
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `AttributeError: 'tuple' object has no attribute 'append'`
(Tuples are locked! You cannot append).

**Snippet 2 Answer:** `15`
(Unpacking assigns 5 to `a` and 10 to `b`. 5 + 10 = 15).
"""

d8_examples = """
# ==============================
# TUPLES EXAMPLES
# ==============================

# Example 1: Creating a Tuple
colors = ("Red", "Green", "Blue")
print("First color:", colors[0])

# Example 2: Trying to change a Tuple (Will crash if uncommented)
# colors[0] = "Yellow"  # TypeError: 'tuple' object does not support item assignment

# Example 3: Tuple Unpacking
person = ("Vamshi", 25, "Software Engineer")
name, age, job = person

print(f"{name} is a {age} year old {job}.")

# Example 4: Returning Multiple Values from a Function
# (Functions actually return a tuple when you separate by commas!)
def get_dimensions():
    return 1920, 1080 # This creates a tuple!

width, height = get_dimensions()
print("Width:", width)
"""

d8_exercises = """
# 🎯 Tuples Playground

## Level 1: Easy

### Challenge 1
Create a tuple called `dimensions` containing `800` and `600`.
Print the first item.

---

### Challenge 2
Try to change `dimensions[0]` to `1920`. Watch it crash. Understand *why* it crashes.

---

## Level 2: Medium

### Challenge 3 (The Unpacker)
Given `student = ("Alex", "A+", 95)`, unpack this tuple into three variables: `name`, `grade`, and `score`. Print them.

---

## Boss Challenge 👑 (The Swapper Trick)
In many programming languages, to swap `a = 5` and `b = 10`, you need a temporary variable.
In Python, you can use Tuple Unpacking to swap them in ONE line!
Try to write the one-line code to swap `a` and `b`.
"""

d8_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
dimensions = (800, 600)
print(dimensions[0])

# Challenge 2
# dimensions[0] = 1920 # Crashes! Tuples are immutable.

# Challenge 3
student = ("Alex", "A+", 95)
name, grade, score = student
print(name, grade, score)

# Boss Challenge
a = 5
b = 10

# The Pythonic Tuple Swap!
a, b = b, a

print("a:", a)
print("b:", b)
"""

d8_interview = """
# 💼 Interview Questions: Tuples

## What is the difference between a List and a Tuple?
1. **Syntax:** Lists use `[]`, Tuples use `()`.
2. **Mutability:** Lists are mutable (changeable). Tuples are immutable (read-only).
3. **Memory/Performance:** Because tuples are immutable, Python optimizes them. They take up less memory and are faster to iterate over than lists.

## How do you create a tuple with only ONE item?
This is a famous trick question!
`my_tuple = (5)` -> This is an Integer! Python ignores the parentheses.
To make it a tuple, you MUST include a trailing comma:
`my_tuple = (5,)` -> This is a Tuple!

## Since Tuples are immutable, can a Tuple contain a Mutable object?
Yes! A tuple can contain a list: `my_tuple = (1, 2, [3, 4])`. 
While you cannot reassign the elements of the tuple (you can't change index 2 to a different list), you *can* mutate the list inside it (e.g., `my_tuple[2].append(5)` is perfectly valid).
"""

# ==============================================================================
# DAY 9: SETS
# ==============================================================================
d9_readme = """
# 🐍 Day 09: Sets (The VIP Club)

# 🤔 Imagine This...

You are hosting a VIP party. 
You invite "Rahul", "Vamshi", and "Alex".
Rahul accidentally fills out the RSVP form 3 times.

If you used a List, your guest list would look like this:
`["Rahul", "Vamshi", "Alex", "Rahul", "Rahul"]`
When giving out gift bags, Rahul gets 3 bags. That's a bug!

You need a data structure that automatically deletes duplicates.
Welcome to **Sets**.

---

# 👶🐣 Baby Version

A Set is a magic bag. 🎩
If you drop two identical apples into the bag... one vanishes!
A Set **only keeps UNIQUE items.**

```python
# Sets use curly braces {}
vip_list = {"Rahul", "Vamshi", "Alex", "Rahul"}

print(vip_list)
# Output: {'Alex', 'Rahul', 'Vamshi'}
```
*Notice two things:*
1. The extra "Rahul" disappeared!
2. The order changed! Sets have **NO ORDER**. There is no index 0 or index 1.

---

# 🛠️ Set Math (Venn Diagrams!)

Sets are incredibly powerful because they can do math operations incredibly fast.

Imagine two groups of friends:
```python
group_a = {"Rahul", "Vamshi"}
group_b = {"Vamshi", "Alex"}
```

**1. Union (Who is at the party?)** `|`
Combines everyone, removes duplicates.
`group_a | group_b` ➡ `{"Rahul", "Vamshi", "Alex"}`

**2. Intersection (Who is in BOTH groups?)** `&`
`group_a & group_b` ➡ `{"Vamshi"}`

**3. Difference (Who is in A but NOT B?)** `-`
`group_a - group_b` ➡ `{"Rahul"}`

---

# 🧠 The 5 Second Rule

Curly Braces `{}` with single items? ➡ **Set**
Can it have duplicates? ➡ **NO**
Does it have an order/index? ➡ **NO**

---

# 🧠 Can You Predict?

**Snippet 1:**
```python
nums = {1, 2, 2, 3, 3, 3}
print(len(nums))
```

**Snippet 2:**
```python
names = {"Alex", "Bob"}
print(names[0])
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `3`
(The set deletes the duplicates, so it just becomes `{1, 2, 3}`).

**Snippet 2 Answer:** `TypeError: 'set' object is not subscriptable`
(Sets have NO order. You cannot use `[0]` on a set!)
"""

d9_examples = """
# ==============================
# SETS EXAMPLES
# ==============================

# Example 1: Removing Duplicates from a List
messy_list = [1, 2, 2, 3, 4, 4, 4, 5]
clean_set = set(messy_list)
print("Unique items:", clean_set)

# Example 2: Adding and Removing
fruits = {"Apple", "Banana"}
fruits.add("Cherry") # Adds an item
fruits.discard("Apple") # Removes an item safely
print(fruits)

# Example 3: Set Math
tech_stack = {"Python", "SQL", "AWS"}
data_stack = {"Python", "SQL", "Tableau"}

print("Union (All skills):", tech_stack | data_stack)
print("Intersection (Common skills):", tech_stack & data_stack)
print("Difference (Tech only):", tech_stack - data_stack)
"""

d9_exercises = """
# 🎯 Sets Playground

## Level 1: Easy

### Challenge 1
Create a list with duplicate numbers: `[1, 1, 2, 2, 3]`.
Convert it to a set to remove the duplicates, and print it.

---

## Level 2: Medium

### Challenge 2
Create a set `A = {1, 2, 3, 4}` and `B = {3, 4, 5, 6}`.
Print the numbers that are present in BOTH sets.

---

### Challenge 3
Using the same sets above, print the numbers that are in set A, but NOT in set B.

---

## Boss Challenge 👑 (The Fast Searcher)
Why do FAANG companies use sets? Speed!
Create a set `usernames = {"admin", "guest", "root"}`.
Write an `if` statement to check if `"admin"` is `in` the set. Print "Found" if true.
*(Note: Checking if something is `in` a set takes O(1) instant time!)*
"""

d9_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
duplicates = [1, 1, 2, 2, 3]
unique = set(duplicates)
print(unique)

# Challenge 2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B) # {3, 4}

# Challenge 3
print(A - B) # {1, 2}

# Boss Challenge
usernames = {"admin", "guest", "root"}
if "admin" in usernames:
    print("Found")
"""

d9_interview = """
# 💼 Interview Questions: Sets

## Why are sets faster than lists for searching?
Sets are implemented using Hash Tables under the hood. When you check if an item exists in a set (`if item in my_set`), Python uses a hashing algorithm to go directly to the memory address. This makes lookups take **O(1)** (constant time). In a list, Python has to check every single element one by one, which takes **O(N)** time.

## Can a set contain a list?
No! Sets can only contain **hashable** (immutable) types. Since lists are mutable, they are unhashable, and putting a list inside a set will throw a `TypeError`. You can, however, put a Tuple inside a set.

## What is the difference between `.remove()` and `.discard()` in sets?
Both delete an item from the set. However:
- If the item does not exist, `.remove()` will throw a `KeyError` and crash your program.
- If the item does not exist, `.discard()` will do nothing and silently let the program continue.
"""

# ==============================================================================
# DAY 10: DICTIONARIES
# ==============================================================================
d10_readme = """
# 🐍 Day 10: Dictionaries (The Phonebook)

# 🤔 Imagine This...

If I tell you to find "Rahul's Phone Number" in a List of 10,000 numbers... you have to look at every single number one by one. Slow!

But what if you have a **Phonebook**?
You jump straight to "R", look for "Rahul", and instantly get his number.

In Python, this is called a **Dictionary**. It stores data in **Key-Value pairs**.

---

# 👶🐣 Baby Version

Imagine a cabinet with labeled drawers. 🗄️

Label: `Name` ➡ Inside: `"Rahul"`
Label: `Age` ➡ Inside: `21`
Label: `Role` ➡ Inside: `"Developer"`

The Label is the **Key**.
The Inside is the **Value**.

```python
# Dictionaries use curly braces {} with a colon :
user = {
    "Name": "Rahul",
    "Age": 21,
    "Role": "Developer"
}

# Pulling open a drawer!
print(user["Name"]) # Output: Rahul
```

---

# 🔑 Dictionary Rules

1. **Keys MUST be unique!** You can't have two "Age" drawers.
2. **Keys are usually Strings.** (They can be ints or tuples, but strings are standard).
3. **Values can be ANYTHING.** A value can be a string, a number, a list, or even another dictionary!

```python
# Adding or Changing a drawer
user["Salary"] = 100000  # Creates a new drawer!
user["Age"] = 22         # Updates the old drawer!
```

---

# 🛠️ Safe Searching (`.get()`)

If you try to open a drawer that doesn't exist:
```python
print(user["Car"]) # ❌ CRASH! KeyError!
```

**FAANG Best Practice:** Use `.get()`!
```python
print(user.get("Car")) # Returns None instead of crashing!
print(user.get("Car", "No Car Found")) # Returns a custom message!
```

---

# 🧠 The 5 Second Rule

`{}` with `Key: Value`? ➡ **Dictionary**
How to search? ➡ **Use the Key! `dict["key"]`**
Safe search? ➡ **`dict.get("key")`**

---

# 🧠 Can You Predict?

**Snippet 1:**
```python
data = {"A": 1, "B": 2, "A": 99}
print(data)
```

**Snippet 2:**
```python
person = {"name": "Alex"}
print(person.get("age", 18))
```

**Scroll down for answers...**
<br><br><br><br>

**Snippet 1 Answer:** `{'A': 99, 'B': 2}`
(Keys must be unique! The second "A" overwrites the first one).

**Snippet 2 Answer:** `18`
("age" does not exist, so `.get()` returns our backup default value `18`).
"""

d10_examples = """
# ==============================
# DICTIONARIES EXAMPLES
# ==============================

# Example 1: Creating a dictionary
car = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2024
}

# Example 2: Accessing data
print("Car Brand:", car["brand"])
print("Color:", car.get("color", "White")) # Safe access with default

# Example 3: Adding & Updating
car["color"] = "Red"   # Adds new key
car["year"] = 2025     # Updates existing key
print(car)

# Example 4: Getting Keys and Values
print("All Keys:", car.keys())
print("All Values:", car.values())

# Example 5: Looping through a dictionary
for key, value in car.items():
    print(f"{key.capitalize()} -> {value}")
"""

d10_exercises = """
# 🎯 Dictionaries Playground

## Level 1: Easy

### Challenge 1
Create a dictionary called `student` with keys: `"name"` and `"score"`. Assign them values.
Print the student's name using the key.

---

### Challenge 2
Add a new key `"grade"` to the `student` dictionary and assign it `"A"`. Print the dictionary.

---

## Level 2: Medium

### Challenge 3 (Safe Access)
Try to print the `"address"` of the student using the `.get()` method so it doesn't crash. Make it return `"Not Provided"` if the key doesn't exist.

---

## Boss Challenge 👑 (Nested Dictionary)
Create a dictionary containing a list!
```python
school = {
    "teacher": "Mr. Smith",
    "students": ["Rahul", "Alex", "Vamshi"]
}
```
Write the code to extract and print `"Vamshi"` from this dictionary.
"""

d10_solutions = """
# =================================
# SOLUTIONS
# =================================

# Challenge 1
student = {
    "name": "Rahul",
    "score": 95
}
print(student["name"])

# Challenge 2
student["grade"] = "A"
print(student)

# Challenge 3
print(student.get("address", "Not Provided"))

# Boss Challenge
school = {
    "teacher": "Mr. Smith",
    "students": ["Rahul", "Alex", "Vamshi"]
}

# Get the list first, then index it!
print(school["students"][2])
"""

d10_interview = """
# 💼 Interview Questions: Dictionaries

## What is the time complexity of looking up a key in a dictionary?
Dictionary lookups take **O(1)** (constant time) on average. Under the hood, Python dictionaries are Hash Maps. Python hashes the key, which gives the exact memory location of the value, bypassing the need to search through other items.

## Can a List be used as a Dictionary Key?
No. Dictionary keys must be **immutable** (hashable). Since lists are mutable (can be changed), their hash value would change, destroying the integrity of the hash map. You will get a `TypeError: unhashable type: 'list'`. You can, however, use a Tuple as a key!

## What is the difference between `dict.keys()`, `dict.values()`, and `dict.items()`?
- `.keys()` returns a view object of all the keys.
- `.values()` returns a view object of all the values.
- `.items()` returns a view object of tuples, where each tuple is `(key, value)`. This is highly useful for iterating in a `for` loop: `for k, v in my_dict.items():`
"""

def generate():
    # Day 7
    d7_path = os.path.join("Day-07-Lists")
    os.makedirs(d7_path, exist_ok=True)
    create_file(os.path.join(d7_path, "README.md"), d7_readme)
    create_file(os.path.join(d7_path, "examples.py"), d7_examples)
    create_file(os.path.join(d7_path, "exercises.md"), d7_exercises)
    create_file(os.path.join(d7_path, "solutions.py"), d7_solutions)
    create_file(os.path.join(d7_path, "interview_questions.md"), d7_interview)

    # Day 8
    d8_path = os.path.join("Day-08-Tuples")
    os.makedirs(d8_path, exist_ok=True)
    create_file(os.path.join(d8_path, "README.md"), d8_readme)
    create_file(os.path.join(d8_path, "examples.py"), d8_examples)
    create_file(os.path.join(d8_path, "exercises.md"), d8_exercises)
    create_file(os.path.join(d8_path, "solutions.py"), d8_solutions)
    create_file(os.path.join(d8_path, "interview_questions.md"), d8_interview)

    # Day 9
    d9_path = os.path.join("Day-09-Sets")
    os.makedirs(d9_path, exist_ok=True)
    create_file(os.path.join(d9_path, "README.md"), d9_readme)
    create_file(os.path.join(d9_path, "examples.py"), d9_examples)
    create_file(os.path.join(d9_path, "exercises.md"), d9_exercises)
    create_file(os.path.join(d9_path, "solutions.py"), d9_solutions)
    create_file(os.path.join(d9_path, "interview_questions.md"), d9_interview)

    # Day 10
    d10_path = os.path.join("Day-10-Dictionaries")
    os.makedirs(d10_path, exist_ok=True)
    create_file(os.path.join(d10_path, "README.md"), d10_readme)
    create_file(os.path.join(d10_path, "examples.py"), d10_examples)
    create_file(os.path.join(d10_path, "exercises.md"), d10_exercises)
    create_file(os.path.join(d10_path, "solutions.py"), d10_solutions)
    create_file(os.path.join(d10_path, "interview_questions.md"), d10_interview)

if __name__ == "__main__":
    generate()
    print("Phase 2 generated successfully.")
