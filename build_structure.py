import os
import shutil

base_dir = r"C:\Users\vamsi\Desktop\python\Python-From-Zero-to-FAANG"

# 1. Delete old 0X_Day folders
for item in os.listdir(base_dir):
    if item.endswith("_Day_Conclusions") or ("_Day_" in item and os.path.isdir(os.path.join(base_dir, item))):
        shutil.rmtree(os.path.join(base_dir, item))

# 2. New 30 days structure
days = [
    "Day-01-Variables-and-Data-Types",
    "Day-02-Operators",
    "Day-03-Conditionals",
    "Day-04-Loops",
    "Day-05-Functions",
    "Day-06-Strings",
    "Day-07-Lists",
    "Day-08-Tuples",
    "Day-09-Sets",
    "Day-10-Dictionaries",
    "Day-11-Modules",
    "Day-12-List-Comprehension",
    "Day-13-Higher-Order-Functions",
    "Day-14-Type-Errors",
    "Day-15-Date-Time",
    "Day-16-Exception-Handling",
    "Day-17-Regular-Expressions",
    "Day-18-File-Handling",
    "Day-19-Package-Manager",
    "Day-20-Classes-and-Objects",
    "Day-21-Web-Scraping",
    "Day-22-Virtual-Environment",
    "Day-23-Statistics",
    "Day-24-Pandas",
    "Day-25-Python-Web",
    "Day-26-Python-with-MongoDB",
    "Day-27-API",
    "Day-28-Building-API",
    "Day-29-Data-Science-Basics",
    "Day-30-Conclusions"
]

files_to_create = [
    "README.md",
    "examples.py",
    "exercises.md",
    "solutions.py",
    "interview_questions.md"
]

for day_folder in days:
    folder_path = os.path.join(base_dir, day_folder)
    os.makedirs(folder_path, exist_ok=True)
    
    for file_name in files_to_create:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            if file_name == "README.md":
                f.write(f"# {day_folder.replace('-', ' ')}\n\nPremium explanation goes here.")
            elif file_name == "examples.py":
                f.write(f"# Code playground for {day_folder}\n")
            elif file_name == "exercises.md":
                f.write(f"# Exercises for {day_folder}\n")
            elif file_name == "solutions.py":
                f.write(f"# Solutions for {day_folder}\n")
            elif file_name == "interview_questions.md":
                f.write(f"# Interview Questions for {day_folder}\n")

print("New scaffolding created successfully!")
