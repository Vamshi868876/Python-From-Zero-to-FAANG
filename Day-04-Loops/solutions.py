# =================================
# SOLUTIONS
# =================================

# Challenge 1
for i in range(5):
    print("Rahul")

# Challenge 2
count = 10
while count > 0:
    print(count)
    count -= 1
print("Happy New Year!")

# Challenge 3
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Challenge 4
for i in range(1, 11):
    if i % 2 != 0: # If it is odd
        continue
    print(i)

# Boss Challenge (FizzBuzz)
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
