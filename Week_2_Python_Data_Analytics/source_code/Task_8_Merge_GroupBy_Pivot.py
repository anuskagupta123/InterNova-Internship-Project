import pandas as pd

print("=" * 75)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 8")
print("          MERGE, CONCATENATE, GROUPBY & PIVOT")
print("=" * 75)

# ------------------------------------------------------------
# 1. CREATE STUDENT DETAILS DATASET
# ------------------------------------------------------------

student_details = pd.DataFrame({
    "Student_ID": [
        "S101", "S102", "S103", "S104", "S105"
    ],
    "Name": [
        "Student A", "Student B", "Student C",
        "Student D", "Student E"
    ],
    "Branch": [
        "AI & DS", "CSE", "AI & DS", "ECE", "CSE"
    ]
})

# ------------------------------------------------------------
# 2. CREATE PERFORMANCE DATASET
# ------------------------------------------------------------

performance = pd.DataFrame({
    "Student_ID": [
        "S101", "S102", "S103", "S104", "S105"
    ],
    "Maths": [72, 85, 91, 68, 77],
    "Reading": [78, 82, 90, 70, 80],
    "Writing": [75, 88, 94, 65, 76]
})

print("\n1. STUDENT DETAILS")
print("-" * 75)
print(student_details)

print("\n2. STUDENT PERFORMANCE")
print("-" * 75)
print(performance)

# ------------------------------------------------------------
# 3. MERGE DATASETS
# ------------------------------------------------------------

print("\n3. MERGING DATASETS")
print("-" * 75)

merged_df = pd.merge(
    student_details,
    performance,
    on="Student_ID"
)

print(merged_df)

# ------------------------------------------------------------
# 4. CONCATENATING DATA
# ------------------------------------------------------------

print("\n4. CONCATENATING DATA")
print("-" * 75)

additional_students = pd.DataFrame({
    "Student_ID": ["S106", "S107"],
    "Name": ["Student F", "Student G"],
    "Branch": ["AI & DS", "ECE"]
})

concatenated_df = pd.concat(
    [student_details, additional_students],
    ignore_index=True
)

print(concatenated_df)

# ------------------------------------------------------------
# 5. GROUPBY - AVERAGE MATHS SCORE BY BRANCH
# ------------------------------------------------------------

print("\n5. GROUPBY - AVERAGE MATHS SCORE BY BRANCH")
print("-" * 75)

branch_average = merged_df.groupby(
    "Branch"
)["Maths"].mean()

print(branch_average)

# ------------------------------------------------------------
# 6. GROUPBY - AVERAGE OF ALL SUBJECTS BY BRANCH
# ------------------------------------------------------------

print("\n6. GROUPBY - SUBJECT AVERAGES BY BRANCH")
print("-" * 75)

subject_average = merged_df.groupby(
    "Branch"
)[["Maths", "Reading", "Writing"]].mean()

print(subject_average)

# ------------------------------------------------------------
# 7. PIVOT TABLE
# ------------------------------------------------------------

print("\n7. PIVOT TABLE - AVERAGE MARKS BY BRANCH")
print("-" * 75)

pivot_table = pd.pivot_table(
    merged_df,
    values=["Maths", "Reading", "Writing"],
    index="Branch",
    aggfunc="mean"
)

print(pivot_table)

# ------------------------------------------------------------
# 8. PIVOT TABLE BY BRANCH AND STUDENT
# ------------------------------------------------------------

print("\n8. PIVOT TABLE - STUDENT PERFORMANCE")
print("-" * 75)

student_pivot = pd.pivot_table(
    merged_df,
    values="Maths",
    index="Branch",
    columns="Name",
    aggfunc="mean"
)

print(student_pivot)

print("\n" + "-" * 75)
print("Merge, concatenate, GroupBy and Pivot Table operations")
print("completed successfully.")
print("=" * 75)