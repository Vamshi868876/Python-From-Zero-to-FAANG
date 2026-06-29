# ==============================
# FUNCTIONS EXAMPLES
# ==============================

# Example 1: A simple function (No arguments)
def say_hello():
    print("Hello from the function!")

say_hello()

# Example 2: Function with Arguments
def greet_person(name):
    print(f"Welcome, {name}!")

greet_person("Rahul")
greet_person("Vamshi")

# Example 3: Function with Return
def calculate_area(length, width):
    area = length * width
    return area

my_room_area = calculate_area(10, 5)
print(f"Area is {my_room_area} sq meters.")

# Example 4: Default Arguments
# If we don't provide a country, it defaults to 'India'
def user_info(name, country="India"):
    print(f"{name} is from {country}")

user_info("Rahul")          # Uses default
user_info("Alex", "USA")    # Overrides default

# Example 5: Multiple Return Values
def get_min_max(numbers):
    return min(numbers), max(numbers)

lowest, highest = get_min_max([10, 20, 5, 100])
print("Min:", lowest)
print("Max:", highest)
