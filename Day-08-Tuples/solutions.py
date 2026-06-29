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
