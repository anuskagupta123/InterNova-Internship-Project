import numpy as np


print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 3")
print("       MATHEMATICAL & STATISTICAL OPERATIONS")
print("=" * 70)


# Numerical dataset
scores = np.array([72, 85, 91, 68, 77, 88, 95, 81, 74, 89])

print("\nDATASET")
print("-" * 70)
print("Student Scores:")
print(scores)


# ---------------------------------------------------------
# 1. MATHEMATICAL OPERATIONS
# ---------------------------------------------------------

print("\n1. MATHEMATICAL OPERATIONS")
print("-" * 70)

addition = scores + 5
subtraction = scores - 5
multiplication = scores * 2
division = scores / 2

print("Original Values :", scores)
print("Addition (+5)   :", addition)
print("Subtraction (-5):", subtraction)
print("Multiplication  :", multiplication)
print("Division (/2)   :", division)


# ---------------------------------------------------------
# 2. STATISTICAL OPERATIONS
# ---------------------------------------------------------

print("\n2. STATISTICAL OPERATIONS")
print("-" * 70)

mean_value = np.mean(scores)
median_value = np.median(scores)
minimum_value = np.min(scores)
maximum_value = np.max(scores)
standard_deviation = np.std(scores)
total_value = np.sum(scores)

print(f"Mean               : {mean_value:.2f}")
print(f"Median             : {median_value:.2f}")
print(f"Minimum            : {minimum_value}")
print(f"Maximum            : {maximum_value}")
print(f"Standard Deviation : {standard_deviation:.2f}")
print(f"Sum                : {total_value}")


# ---------------------------------------------------------
# 3. SUMMARY
# ---------------------------------------------------------

print("\n3. DATASET SUMMARY")
print("-" * 70)

print(f"Number of Scores   : {scores.size}")
print(f"Average Score      : {mean_value:.2f}")
print(f"Highest Score      : {maximum_value}")
print(f"Lowest Score       : {minimum_value}")


print("\n" + "-" * 70)
print("Mathematical and statistical operations completed successfully.")
print("=" * 70)

