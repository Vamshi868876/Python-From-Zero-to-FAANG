# ==============================
# LISTS EXAMPLES
# ==============================

# Example 1: Creating and Accessing
movies = ["Inception", "Interstellar", "Dune"]
print("First movie:", movies[0])
print("Last movie:", movies[-1])

# Example 2: Modifying a List
movies[0] = "Batman"
print("Modified movies:", movies)

# Example 3: Adding items
movies.append("Spider-Man") # Adds to end
movies.insert(1, "Iron Man") # Inserts at index 1
print("After adding:", movies)

# Example 4: Removing items
movies.remove("Dune") # Removes by name
last_item = movies.pop() # Removes and grabs last item
print("Popped item:", last_item)
print("After removing:", movies)

# Example 5: Sorting
numbers = [42, 10, 5, 99, 1]
numbers.sort()
print("Sorted numbers:", numbers)
