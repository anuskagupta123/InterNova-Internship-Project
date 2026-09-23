print("=" * 60)
print("          PYTHON FUNDAMENTALS - TASK 4")
print("                GRADE CALCULATOR")
print("=" * 60)

# Taking marks as input
marks = float(input("\nEnter your marks (0-100): "))

print("\n" + "-" * 60)
print("                    RESULT")
print("-" * 60)

# Checking whether the marks are within the valid range
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter a value between 0 and 100.")

# Determining the grade
elif marks >= 90:
    print(f"Marks : {marks:g}")
    print("Grade : A")
    print("Performance : Excellent")

elif marks >= 75:
    print(f"Marks : {marks:g}")
    print("Grade : B")
    print("Performance : Very Good")

elif marks >= 60:
    print(f"Marks : {marks:g}")
    print("Grade : C")
    print("Performance : Good")

else:
    print(f"Marks : {marks:g}")
    print("Grade : Fail")
    print("Performance : Needs Improvement")

print("-" * 60)
print("Grade evaluation completed.")
print("=" * 60)