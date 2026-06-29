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
