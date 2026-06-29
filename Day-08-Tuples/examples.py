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
