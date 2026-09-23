print("=" * 65)
print("          PYTHON FUNDAMENTALS - TASK 7")
print("              STRINGS & COLLECTIONS")
print("=" * 65)


# ==========================================================
# PART 1: STRING OPERATIONS
# ==========================================================

print("\n1. STRING OPERATIONS")
print("-" * 65)

student_name = "Anuska Gupta"
course = "Artificial Intelligence and Data Science"

print(f"Original String : {student_name}")
print(f"Uppercase       : {student_name.upper()}")
print(f"Lowercase       : {student_name.lower()}")

updated_name = student_name.replace("Gupta", "Student")
print(f"After Replace   : {updated_name}")

position = student_name.find("Gupta")
print(f"Position of 'Gupta' : {position}")


# ==========================================================
# PART 2: LIST OPERATIONS
# ==========================================================

print("\n2. LIST OPERATIONS")
print("-" * 65)

subjects = ["Python", "Statistics", "Database", "Machine Learning"]

print(f"Original List : {subjects}")

# append()
subjects.append("Data Visualization")
print(f"After append  : {subjects}")

# remove()
subjects.remove("Database")
print(f"After remove  : {subjects}")

# sort()
subjects.sort()
print(f"After sort    : {subjects}")


# ==========================================================
# PART 3: TUPLE CREATION AND INDEXING
# ==========================================================

print("\n3. TUPLE CREATION & INDEXING")
print("-" * 65)

student_details = ("Anuska Gupta", "AI & DS", 2026)

print(f"Tuple : {student_details}")
print(f"First element  : {student_details[0]}")
print(f"Second element : {student_details[1]}")
print(f"Third element  : {student_details[2]}")


# ==========================================================
# PART 4: DICTIONARY - STUDENT INFORMATION
# ==========================================================

print("\n4. STUDENT INFORMATION DICTIONARY")
print("-" * 65)

student = {
    "Name": "Anuska Gupta",
    "Branch": "Artificial Intelligence and Data Science",
    "Year": "Third Year",
    "College": "KPR Institute of Engineering and Technology"
}

print("Student Details:")

for key, value in student.items():
    print(f"{key:<10}: {value}")


# ==========================================================
# PART 5: SET OPERATIONS
# ==========================================================

print("\n5. SET OPERATIONS")
print("-" * 65)

skills = {"Python", "SQL", "Machine Learning"}

print(f"Original Set : {skills}")

# add()
skills.add("Data Analytics")
print(f"After add    : {skills}")

# remove()
skills.remove("SQL")
print(f"After remove : {skills}")


# ==========================================================
# COMPLETION MESSAGE
# ==========================================================

print("\n" + "-" * 65)
print("String and collection operations completed successfully.")
print("=" * 65)