print("=" * 60)
print("          PYTHON FUNDAMENTALS - TASK 5")
print("                     LOOPS")
print("=" * 60)


# ----------------------------------------------------------
# Part 1: Print numbers from 1 to 20 using a for loop
# ----------------------------------------------------------

print("\n1. NUMBERS FROM 1 TO 20")
print("-" * 60)

for number in range(1, 21):
    print(number, end=" ")

print()


# ----------------------------------------------------------
# Part 2: Multiplication table using a for loop
# ----------------------------------------------------------

print("\n2. MULTIPLICATION TABLE")
print("-" * 60)

table_number = int(input("Enter a number for the multiplication table: "))

print(f"\nMultiplication Table of {table_number}")
print()

for multiplier in range(1, 11):
    result = table_number * multiplier
    print(f"{table_number:>3} × {multiplier:>2} = {result}")


# ----------------------------------------------------------
# Part 3: Even numbers from 1 to 50 using a while loop
# ----------------------------------------------------------

print("\n3. EVEN NUMBERS FROM 1 TO 50")
print("-" * 60)

number = 2

while number <= 50:
    print(number, end=" ")
    number += 2

print()

print("-" * 60)
print("All loop demonstrations completed successfully.")
print("=" * 60)