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
