# =================================
# SOLUTIONS
# =================================

# Challenge 1
def print_my_name():
    print("Rahul")

print_my_name()

# Challenge 2
def subtract(a, b):
    return a - b

print(subtract(10, 3))

# Challenge 3
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
# Shorthand pro-way for Challenge 3:
# def is_even(number):
#     return number % 2 == 0

# Challenge 4
def welcome(name, message="Welcome back!"):
    print(f"{name}, {message}")

welcome("Rahul")
welcome("Vamshi", "Good Morning!")

# Boss Challenge
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid Operation"

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))
