import os

days = [
    "01_Day_Introduction",
    "02_Day_Variables_builtin_functions",
    "03_Day_Operators",
    "04_Day_Strings",
    "05_Day_Lists",
    "06_Day_Tuples",
    "07_Day_Sets",
    "08_Day_Dictionaries",
    "09_Day_Conditionals",
    "10_Day_Loops",
    "11_Day_Functions",
    "12_Day_Modules",
    "13_Day_List_comprehension",
    "14_Day_Higher_order_functions",
    "15_Day_Python_type_errors",
    "16_Day_Python_date_time",
    "17_Day_Exception_handling",
    "18_Day_Regular_expressions",
    "19_Day_File_handling",
    "20_Day_Python_package_manager",
    "21_Day_Classes_and_objects",
    "22_Day_Web_scraping",
    "23_Day_Virtual_environment",
    "24_Day_Statistics",
    "25_Day_Pandas",
    "26_Day_Python_web",
    "27_Day_Python_with_mongodb",
    "28_Day_API",
    "29_Day_Building_API",
    "30_Day_Conclusions"
]

base_dir = r"C:\Users\vamsi\Desktop\python\Python-From-Zero-to-FAANG"

for day_folder in days:
    folder_path = os.path.join(base_dir, day_folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # Create the single markdown file inside (e.g. 01_introduction.md)
    parts = day_folder.split("_")
    number = parts[0]
    name_parts = parts[2:]
    md_name = f"{number}_{'_'.join(name_parts).lower()}.md"
    
    md_path = os.path.join(folder_path, md_name)
    
    # Default template for all days
    template = f"""# Day {int(number)} - {' '.join(name_parts).replace('_', ' ')}

## 1. Learning Objectives
What students will learn today.

## 2. Baby Version 👶🐣
Explain the concept so a 5-year-old can understand.

## 3. Beginner Version 🧑‍🎓
Simple explanation with examples.

## 4. Interview Version 💼
Professional FAANG-style definition.

## 5. Syntax
Explain syntax line by line.

## 6. Code Examples
Code snippets and real-world examples.

## 7. Common Mistakes
Show wrong code and correct code.

## 8. Visual Memory Tricks 🧠
Create easy-to-remember tricks.

## 9. Interview Questions
Provide questions and answers.

## 10. Practice Problems
Easy, Medium, Hard problems.

## 11. Mini Project
Create a small project using this topic.

## 12. Cheat Sheet
One-page quick revision.

## 13. Key Takeaways
Important points to remember.
"""
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(template)

print("30 days structure created successfully.")
