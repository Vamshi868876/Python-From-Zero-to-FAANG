# ==============================
# SETS EXAMPLES
# ==============================

# Example 1: Removing Duplicates from a List
messy_list = [1, 2, 2, 3, 4, 4, 4, 5]
clean_set = set(messy_list)
print("Unique items:", clean_set)

# Example 2: Adding and Removing
fruits = {"Apple", "Banana"}
fruits.add("Cherry") # Adds an item
fruits.discard("Apple") # Removes an item safely
print(fruits)

# Example 3: Set Math
tech_stack = {"Python", "SQL", "AWS"}
data_stack = {"Python", "SQL", "Tableau"}

print("Union (All skills):", tech_stack | data_stack)
print("Intersection (Common skills):", tech_stack & data_stack)
print("Difference (Tech only):", tech_stack - data_stack)
