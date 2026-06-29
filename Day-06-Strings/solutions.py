# =================================
# SOLUTIONS
# =================================

# Challenge 1
word = "SUPERMAN"
print(word[2]) # P

# Challenge 2
print(word[0:5]) # SUPER

# Challenge 3
def shout(text):
    return f"{text.upper()}!!!"

print(shout("hello"))

# Challenge 4
def is_palindrome(word):
    # Check if the word is equal to its reversed version
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("racecar")) # True
print(is_palindrome("python"))  # False

# Boss Challenge
text = "apple banana apple cherry banana apple"
apple_count = text.count("apple")
print(f"The word 'apple' appears {apple_count} times.")
