import numpy as np


print("=" * 65)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 1")
print("                 NUMPY ARRAYS")
print("=" * 65)


# Creating a one-dimensional NumPy array
student_scores = np.array(
    [72, 85, 91, 68, 77, 88, 95, 81, 74, 89]
)

print("\n1. ONE-DIMENSIONAL ARRAY")
print("-" * 65)

print("Student Scores:")
print(student_scores)

print(f"\nShape     : {student_scores.shape}")
print(f"Size      : {student_scores.size}")
print(f"Data Type : {student_scores.dtype}")


# Creating a two-dimensional NumPy array
score_matrix = np.array([
    [72, 85, 91, 68, 77],
    [88, 95, 81, 74, 89]
])

print("\n2. TWO-DIMENSIONAL ARRAY")
print("-" * 65)

print("Score Matrix:")
print(score_matrix)

print(f"\nShape     : {score_matrix.shape}")
print(f"Size      : {score_matrix.size}")
print(f"Data Type : {score_matrix.dtype}")


print("\n" + "-" * 65)
print("NumPy array creation and inspection completed successfully.")
print("=" * 65)