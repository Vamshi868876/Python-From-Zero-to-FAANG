# ==============================
# CONDITIONALS EXAMPLES
# ==============================

# Example 1: Simple IF
age = 20

if age >= 18:
    print("You can vote!")

# Example 2: IF - ELSE
temperature = 30

if temperature > 25:
    print("It's a hot day. Drink water.")
else:
    print("It's a cool day.")

# Example 3: IF - ELIF - ELSE
marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# Example 4: Nested IF (If inside an If)
is_weekend = True
has_money = False

if is_weekend:
    if has_money:
        print("Let's go to the movies!")
    else:
        print("Let's watch Netflix at home.")
else:
    print("You have to work!")

# Example 5: Multiple Conditions (and / or)
has_passport = True
has_ticket = True

if has_passport and has_ticket:
    print("You can board the flight.")
else:
    print("You cannot board.")
