# =================================
# SOLUTIONS
# =================================

# Challenge 1
student = {
    "name": "Rahul",
    "score": 95
}
print(student["name"])

# Challenge 2
student["grade"] = "A"
print(student)

# Challenge 3
print(student.get("address", "Not Provided"))

# Boss Challenge
school = {
    "teacher": "Mr. Smith",
    "students": ["Rahul", "Alex", "Vamshi"]
}

# Get the list first, then index it!
print(school["students"][2])
