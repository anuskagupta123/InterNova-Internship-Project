import pandas as pd
import numpy as np

print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 7")
print("                 HANDLING MISSING VALUES")
print("=" * 70)

# ------------------------------------------------------------
# 1. CREATE DATASET WITH MISSING VALUES
# ------------------------------------------------------------

data = {
    "Student_ID": [
        "S101", "S102", "S103", "S104", "S105",
        "S106", "S107", "S108"
    ],
    "Name": [
        "Student A", "Student B", "Student C", "Student D",
        "Student E", "Student F", "Student G", "Student H"
    ],
    "Branch": [
        "AI & DS", "CSE", "AI & DS", "ECE",
        "CSE", "AI & DS", "ECE", "CSE"
    ],
    "Maths": [
        72, 85, np.nan, 68, 77, 88, 95, 81
    ],
    "Reading": [
        78, 82, 90, np.nan, 80, 85, 92, 79
    ],
    "Writing": [
        75, 88, 94, 65, np.nan, 90, 96, 84
    ]
}

df = pd.DataFrame(data)

print("\n1. DATASET WITH MISSING VALUES")
print("-" * 70)
print(df)

# ------------------------------------------------------------
# 2. IDENTIFY MISSING VALUES
# ------------------------------------------------------------

print("\n2. IDENTIFYING MISSING VALUES")
print("-" * 70)

print(df.isnull())

# ------------------------------------------------------------
# 3. COUNT MISSING VALUES
# ------------------------------------------------------------

print("\n3. COUNT OF MISSING VALUES")
print("-" * 70)

missing_count = df.isnull().sum()

print(missing_count)

# ------------------------------------------------------------
# 4. TOTAL MISSING VALUES
# ------------------------------------------------------------

print("\n4. TOTAL MISSING VALUES")
print("-" * 70)

total_missing = df.isnull().sum().sum()

print(f"Total Missing Values : {total_missing}")

# ------------------------------------------------------------
# 5. DROP ROWS WITH MISSING VALUES
# ------------------------------------------------------------

print("\n5. DATASET AFTER DROPPING MISSING ROWS")
print("-" * 70)

dropped_df = df.dropna()

print(dropped_df)

# ------------------------------------------------------------
# 6. FILL MISSING NUMERICAL VALUES WITH MEAN
# ------------------------------------------------------------

print("\n6. FILLING MISSING VALUES WITH COLUMN MEAN")
print("-" * 70)

filled_df = df.copy()

numeric_columns = ["Maths", "Reading", "Writing"]

for column in numeric_columns:
    filled_df[column] = filled_df[column].fillna(
        filled_df[column].mean()
    )

print(filled_df)

# ------------------------------------------------------------
# 7. VERIFY MISSING VALUES AFTER FILLING
# ------------------------------------------------------------

print("\n7. MISSING VALUES AFTER FILLING")
print("-" * 70)

print(filled_df.isnull().sum())

print("\n" + "-" * 70)
print("Missing value handling completed successfully.")
print("=" * 70)