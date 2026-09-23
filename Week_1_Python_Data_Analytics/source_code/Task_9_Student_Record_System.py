# ==========================================================
# STUDENT DATA STORAGE
# ==========================================================

student_records = []


# ==========================================================
# FUNCTION: ADD STUDENT
# ==========================================================

def add_student():
    """Add a new student record to the system."""

    print("\n" + "-" * 65)
    print("                    ADD STUDENT")
    print("-" * 65)

    student_id = input("Enter student ID     : ").strip()

    # Check whether the ID already exists
    for student in student_records:
        if student["id"] == student_id:
            print("\nA student with this ID already exists.")
            return

    name = input("Enter student name   : ").strip()
    branch = input("Enter branch         : ").strip()

    # Validate marks
    while True:
        try:
            marks = float(input("Enter marks (0-100)  : "))

            if 0 <= marks <= 100:
                break

            print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    # Creating a dictionary for the student
    student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    # Adding dictionary to the list
    student_records.append(student)

    print("\nStudent record added successfully!")


# ==========================================================
# FUNCTION: DISPLAY STUDENTS
# ==========================================================

def display_students():
    """Display all student records."""

    print("\n" + "-" * 65)
    print("                 ALL STUDENT RECORDS")
    print("-" * 65)

    if not student_records:
        print("No student records available.")
        return

    for number, student in enumerate(student_records, start=1):
        print(f"\nStudent {number}")
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Branch : {student['branch']}")
        print(f"Marks  : {student['marks']:g}")
        print("-" * 65)


# ==========================================================
# FUNCTION: SEARCH STUDENT
# ==========================================================

def search_student():
    """Search for a student using their name."""

    print("\n" + "-" * 65)
    print("                  SEARCH STUDENT")
    print("-" * 65)

    search_name = input("Enter student name to search: ").strip().lower()

    found = False

    for student in student_records:
        if search_name in student["name"].lower():
            print("\nStudent found!")
            print(f"ID     : {student['id']}")
            print(f"Name   : {student['name']}")
            print(f"Branch : {student['branch']}")
            print(f"Marks  : {student['marks']:g}")
            found = True

    if not found:
        print("\nNo student found with that name.")


# ==========================================================
# FUNCTION: DELETE STUDENT
# ==========================================================

def delete_student():
    """Delete a student record using the student ID."""

    print("\n" + "-" * 65)
    print("                  DELETE STUDENT")
    print("-" * 65)

    student_id = input("Enter student ID to delete: ").strip()

    for student in student_records:
        if student["id"] == student_id:
            student_records.remove(student)
            print("\nStudent record deleted successfully!")
            return

    print("\nNo student found with that ID.")


# ==========================================================
# FUNCTION: DISPLAY MENU
# ==========================================================

def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 65)
    print("        STUDENT RECORD MANAGEMENT SYSTEM")
    print("=" * 65)

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. Delete Student")
    print("5. Exit")

    print("=" * 65)


# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("\n" + "=" * 65)
print("        WELCOME TO STUDENT RECORD MANAGEMENT SYSTEM")
print("=" * 65)

while True:

    display_menu()

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("\nThank you for using the Student Record Management System!")
        print("Program terminated successfully.")
        print("=" * 65)
        break

    else:
        print("\nInvalid choice. Please select a number from 1 to 5.")