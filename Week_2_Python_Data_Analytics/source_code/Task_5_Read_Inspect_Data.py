"""
Week 2 Internship: NumPy & Pandas for Data Analytics
Task 5: Reading & Inspecting Data

This program demonstrates how to read a CSV file
and inspect its structure using Pandas.
"""

import pandas as pd

print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 5")
print("              READING & INSPECTING DATA")
print("=" * 70)

# ------------------------------------------------------------
# 1. READ CSV FILE
# ------------------------------------------------------------

file_path = "datasets/students.csv"

df = pd.read_csv(file_path)

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 70)
print(df)

# ------------------------------------------------------------
# 2. DISPLAY FIRST FIVE ROWS
# ------------------------------------------------------------

print("\n2. FIRST FIVE ROWS")
print("-" * 70)
print(df.head())

# ------------------------------------------------------------
# 3. DISPLAY LAST FIVE ROWS
# ------------------------------------------------------------

print("\n3. LAST FIVE ROWS")
print("-" * 70)
print(df.tail())

# ------------------------------------------------------------
# 4. DATASET SHAPE
# ------------------------------------------------------------

print("\n4. DATASET SHAPE")
print("-" * 70)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")
print(f"Shape   : {df.shape}")

# ------------------------------------------------------------
# 5. COLUMN NAMES
# ------------------------------------------------------------

print("\n5. COLUMN NAMES")
print("-" * 70)
print(list(df.columns))

# ------------------------------------------------------------
# 6. DATA TYPES
# ------------------------------------------------------------

print("\n6. DATA TYPES")
print("-" * 70)
print(df.dtypes)

# ------------------------------------------------------------
# 7. DATASET INFORMATION
# ------------------------------------------------------------

print("\n7. DATASET INFORMATION")
print("-" * 70)
df.info()

# ------------------------------------------------------------
# 8. STATISTICAL SUMMARY
# ------------------------------------------------------------

print("\n8. STATISTICAL SUMMARY")
print("-" * 70)
print(df.describe())

print("\n" + "-" * 70)
print("Reading and inspecting the dataset completed successfully.")
print("=" * 70)