print("=" * 65)
print("          PYTHON FUNDAMENTALS - TASK 8")
print("                 FILE HANDLING")
print("=" * 65)


# ----------------------------------------------------------
# File location
# ----------------------------------------------------------

file_path = "output_files/student_introduction.txt"


# ----------------------------------------------------------
# Taking introduction details from the user
# ----------------------------------------------------------

print("\nEnter your introduction details")
print("-" * 65)

name = input("Enter your name    : ")
college = input("Enter your college : ")
branch = input("Enter your branch  : ")


# ----------------------------------------------------------
# Creating and writing to the text file
# ----------------------------------------------------------

introduction = f"""Student Introduction
=====================

Name    : {name}
College : {college}
Branch  : {branch}

I am a student interested in Python, Data Analytics,
Artificial Intelligence, and Machine Learning.
"""

with open(file_path, "w") as file:
    file.write(introduction)


print("\n" + "-" * 65)
print("Introduction successfully written to the text file.")
print(f"File location: {file_path}")


# ----------------------------------------------------------
# Reading the file contents
# ----------------------------------------------------------

print("\nSTORED FILE CONTENT")
print("-" * 65)

with open(file_path, "r") as file:
    file_contents = file.read()

print(file_contents)

print("-" * 65)
print("File handling operation completed successfully.")
print("=" * 65)