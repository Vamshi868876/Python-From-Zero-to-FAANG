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
