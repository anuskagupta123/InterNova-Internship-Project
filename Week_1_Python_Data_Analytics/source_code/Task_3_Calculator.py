print("=" * 60)
print("          PYTHON FUNDAMENTALS - TASK 3")
print("                 BASIC CALCULATOR")
print("=" * 60)

# Taking two numbers as input
first_number = float(input("\nEnter the first number  : "))
second_number = float(input("Enter the second number : "))

print("\n" + "-" * 60)
print("                 CALCULATION RESULTS")
print("-" * 60)

# Arithmetic operations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

print(f"Addition       : {addition:g}")
print(f"Subtraction    : {subtraction:g}")
print(f"Multiplication : {multiplication:g}")

# Checking before division and modulus
if second_number != 0:
    division = first_number / second_number
    modulus = first_number % second_number

    print(f"Division       : {division:g}")
    print(f"Modulus        : {modulus:g}")
else:
    print("Division       : Cannot divide by zero")
    print("Modulus        : Cannot divide by zero")

print("-" * 60)
print("Calculator execution completed successfully.")
print("=" * 60)