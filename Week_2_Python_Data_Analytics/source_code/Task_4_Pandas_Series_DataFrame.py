import pandas as pd


print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 4")
print("              PANDAS SERIES & DATAFRAME")
print("=" * 70)


# ---------------------------------------------------------
# 1. PANDAS SERIES
# ---------------------------------------------------------

print("\n1. PANDAS SERIES")
print("-" * 70)

scores = pd.Series(
    [72, 85, 91, 68, 77],
    index=["S101", "S102", "S103", "S104", "S105"],
    name="Marks"
)

print(scores)


# ---------------------------------------------------------
# 2. CREATE A DATAFRAME
# ---------------------------------------------------------

print("\n2. STUDENT DATAFRAME")
print("-" * 70)

student_data = {
    "Student_ID": ["S101", "S102", "S103", "S104", "S105"],
    "Name": ["Student A", "Student B", "Student C",
             "Student D", "Student E"],
    "Branch": ["AI & DS", "CSE", "AI & DS", "ECE", "CSE"],
    "Marks": [72, 85, 91, 68, 77]
}

df = pd.DataFrame(student_data)

print(df)


# ---------------------------------------------------------
# 3. DISPLAY COLUMN NAMES
# ---------------------------------------------------------

print("\n3. COLUMN NAMES")
print("-" * 70)

print(list(df.columns))


# ---------------------------------------------------------
# 4. DISPLAY INDEX
# ---------------------------------------------------------

print("\n4. DATAFRAME INDEX")
print("-" * 70)

print(df.index)


# ---------------------------------------------------------
# 5. ADD A NEW COLUMN
# ---------------------------------------------------------

print("\n5. ADDING A NEW COLUMN")
print("-" * 70)

df["Status"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 50 else "Fail"
)

print(df)


print("\n" + "-" * 70)
print("Pandas Series and DataFrame operations completed successfully.")
print("=" * 70)