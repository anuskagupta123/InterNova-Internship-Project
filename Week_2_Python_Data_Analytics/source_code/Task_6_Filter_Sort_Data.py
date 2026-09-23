import pandas as pd

print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 6")
print("           SELECTING, FILTERING & SORTING DATA")
print("=" * 70)

# ------------------------------------------------------------
# 1. READ DATASET
# ------------------------------------------------------------

file_path = "datasets/students.csv"

df = pd.read_csv(file_path)

print("\n1. ORIGINAL DATASET")
print("-" * 70)
print(df)

# ------------------------------------------------------------
# 2. SELECT A SINGLE COLUMN
# ------------------------------------------------------------

print("\n2. SELECTING A SINGLE COLUMN")
print("-" * 70)

print("Student Names:")
print(df["Name"])

# ------------------------------------------------------------
# 3. SELECT MULTIPLE COLUMNS
# ------------------------------------------------------------

print("\n3. SELECTING MULTIPLE COLUMNS")
print("-" * 70)

selected_columns = df[["Name", "Branch", "Maths"]]

print(selected_columns)

# ------------------------------------------------------------
# 4. FILTER STUDENTS BASED ON MATHS SCORE
# ------------------------------------------------------------

print("\n4. FILTERING STUDENTS WITH MATHS SCORE >= 80")
print("-" * 70)

high_math_students = df[df["Maths"] >= 80]

print(high_math_students)

# ------------------------------------------------------------
# 5. FILTER STUDENTS BY BRANCH
# ------------------------------------------------------------

print("\n5. FILTERING AI & DS STUDENTS")
print("-" * 70)

ai_ds_students = df[df["Branch"] == "AI & DS"]

print(ai_ds_students)

# ------------------------------------------------------------
# 6. MULTIPLE CONDITIONS
# ------------------------------------------------------------

print("\n6. FILTERING AI & DS STUDENTS WITH MATHS >= 80")
print("-" * 70)

filtered_students = df[
    (df["Branch"] == "AI & DS") &
    (df["Maths"] >= 80)
]

print(filtered_students)

# ------------------------------------------------------------
# 7. SORT BY MATHS SCORE - ASCENDING
# ------------------------------------------------------------

print("\n7. SORTING BY MATHS SCORE - ASCENDING")
print("-" * 70)

ascending_data = df.sort_values(
    by="Maths",
    ascending=True
)

print(ascending_data)

# ------------------------------------------------------------
# 8. SORT BY MATHS SCORE - DESCENDING
# ------------------------------------------------------------

print("\n8. SORTING BY MATHS SCORE - DESCENDING")
print("-" * 70)

descending_data = df.sort_values(
    by="Maths",
    ascending=False
)

print(descending_data)

# ------------------------------------------------------------
# 9. TOP THREE STUDENTS
# ------------------------------------------------------------

print("\n9. TOP THREE STUDENTS BY MATHS SCORE")
print("-" * 70)

top_three = df.sort_values(
    by="Maths",
    ascending=False
).head(3)

print(top_three[["Student_ID", "Name", "Branch", "Maths"]])

print("\n" + "-" * 70)
print("Selecting, filtering and sorting completed successfully.")
print("=" * 70)