import numpy as np


print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 2")
print("          INDEXING, SLICING & RESHAPING")
print("=" * 70)


# ---------------------------------------------------------
# 1. ONE-DIMENSIONAL ARRAY
# ---------------------------------------------------------

scores = np.array([72, 85, 91, 68, 77, 88, 95, 81, 74, 89])

print("\n1. ORIGINAL ONE-DIMENSIONAL ARRAY")
print("-" * 70)
print(scores)


# ---------------------------------------------------------
# 2. INDEXING
# ---------------------------------------------------------

print("\n2. INDEXING")
print("-" * 70)

print(f"First element       : {scores[0]}")
print(f"Third element       : {scores[2]}")
print(f"Last element        : {scores[-1]}")


# ---------------------------------------------------------
# 3. SLICING
# ---------------------------------------------------------

print("\n3. SLICING")
print("-" * 70)

print(f"Elements 2 to 5     : {scores[1:5]}")
print(f"First five elements : {scores[:5]}")
print(f"Last three elements : {scores[-3:]}")


# ---------------------------------------------------------
# 4. TWO-DIMENSIONAL ARRAY
# ---------------------------------------------------------

score_matrix = scores.reshape(2, 5)

print("\n4. TWO-DIMENSIONAL ARRAY")
print("-" * 70)
print(score_matrix)


# ---------------------------------------------------------
# 5. ROW AND COLUMN ACCESS
# ---------------------------------------------------------

print("\n5. ROW AND COLUMN ACCESS")
print("-" * 70)

print(f"First row           : {score_matrix[0]}")
print(f"Second row          : {score_matrix[1]}")
print(f"First column        : {score_matrix[:, 0]}")
print(f"Third column        : {score_matrix[:, 2]}")
print(f"Element [1, 3]      : {score_matrix[1, 3]}")


# ---------------------------------------------------------
# 6. RESHAPING
# ---------------------------------------------------------

reshaped_array = scores.reshape(5, 2)

print("\n6. RESHAPING")
print("-" * 70)

print("Original Shape      :", scores.shape)
print("\nReshaped Array (5 × 2):")
print(reshaped_array)

print("\nReshaped Shape      :", reshaped_array.shape)


print("\n" + "-" * 70)
print("Indexing, slicing and reshaping completed successfully.")
print("=" * 70)