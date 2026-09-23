# ----------------------------------------------------------
# Function 1: Calculate the square of a number
# ----------------------------------------------------------

def calculate_square(number):
    """Return the square of the given number."""
    return number ** 2


# ----------------------------------------------------------
# Function 2: Calculate the average of three numbers
# ----------------------------------------------------------

def calculate_average(first, second, third):
    """Return the average of three numbers."""
    return (first + second + third) / 3


# ----------------------------------------------------------
# Main Program
# ----------------------------------------------------------

print("=" * 60)
print("          PYTHON FUNDAMENTALS - TASK 6")
print("                    FUNCTIONS")
print("=" * 60)


# Taking input for square calculation
print("\n1. SQUARE OF A NUMBER")
print("-" * 60)

number = float(input("Enter a number: "))

square = calculate_square(number)

print(f"Square of {number:g} = {square:g}")


# Taking input for average calculation
print("\n2. AVERAGE OF THREE NUMBERS")
print("-" * 60)

first_number = float(input("Enter the first number : "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number : "))

average = calculate_average(
    first_number,
    second_number,
    third_number
)

print(f"\nAverage = {average:.2f}")

print("\n" + "-" * 60)
print("Both functions executed successfully.")
print("=" * 60)