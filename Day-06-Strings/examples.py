# ==============================
# STRINGS EXAMPLES
# ==============================

# Example 1: Indexing
text = "HELLO"
print("First letter:", text[0])  # H
print("Last letter:", text[-1])  # O (Negative index counts from the end!)

# Example 2: Slicing
word = "PYTHON"
print("First 3 letters:", word[0:3]) # PYT
print("Reverse:", word[::-1])        # NOHTYP

# Example 3: String Methods
sentence = "i love python programming"
print("Upper:", sentence.upper())
print("Title:", sentence.title()) # Capitalizes every word
print("Replace:", sentence.replace("python", "java"))

# Example 4: Splitting a string into a list of words
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print("Split result:", fruits)

# Example 5: F-Strings
name = "Vamshi"
score = 99
print(f"Player {name} achieved a score of {score}!")
