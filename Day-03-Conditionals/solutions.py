# =================================
# SOLUTIONS
# =================================

# Challenge 1
number = 15
if number > 10:
    print("Greater than 10")

# Challenge 2
weather = "Rainy"
if weather == "Rainy":
    print("Take an umbrella")
else:
    print("Wear sunglasses")

# Challenge 3
x = 7
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Challenge 4
# Output:
# B is bigger

# Challenge 5
# Output:
# Half Century
# Century
# (Because they are two separate 'if' statements, both get checked!)

# Boss Challenge
age = 22
is_drunk = False

if age >= 18:
    if not is_drunk: # or is_drunk == False
        print("Welcome to the club!")
    else:
        print("You are too drunk to enter.")
else:
    print("You are too young to enter.")

# Alternative way for Boss Challenge using 'and':
# if age >= 18 and is_drunk == False:
#     print("Welcome to the club!")
# else:
#     print("You cannot enter.")
