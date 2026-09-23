"""
Week 2 Internship: NumPy & Pandas for Data Analytics
Task 10: Mini Data Analysis Project

Project:
Student Performance Data Analysis using Pandas

This project demonstrates a complete data analytics
workflow using a student performance dataset.
"""

import pandas as pd
import os

print("=" * 75)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 10")
print("          MINI STUDENT PERFORMANCE ANALYSIS")
print("=" * 75)

# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

file_path = "datasets/students.csv"

df = pd.read_csv(file_path)

print("\n1. DATASET LOADED")
print("-" * 75)
print(df)

# ------------------------------------------------------------
# 2. INSPECT DATASET
# ------------------------------------------------------------

print("\n2. DATASET INSPECTION")
print("-" * 75)

print(f"Number of Rows    : {df.shape[0]}")
print(f"Number of Columns : {df.shape[1]}")
print(f"Dataset Shape     : {df.shape}")

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

# ------------------------------------------------------------
# 3. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n3. MISSING VALUE ANALYSIS")
print("-" * 75)

missing_values = df.isnull().sum()

print(missing_values)

total_missing = missing_values.sum()

print(f"\nTotal Missing Values: {total_missing}")

# ------------------------------------------------------------
# 4. CREATE AVERAGE SCORE
# ------------------------------------------------------------

print("\n4. CALCULATING AVERAGE SCORES")
print("-" * 75)

subject_columns = ["Maths", "Reading", "Writing"]

df["Average"] = df[subject_columns].mean(axis=1)

print(df[
    ["Student_ID", "Name", "Branch", "Average"]
])

# ------------------------------------------------------------
# 5. ASSIGN PERFORMANCE LEVEL
# ------------------------------------------------------------

print("\n5. ASSIGNING PERFORMANCE LEVEL")
print("-" * 75)


def performance_level(average):
    if average >= 90:
        return "Excellent"
    elif average >= 80:
        return "Good"
    elif average >= 70:
        return "Average"
    else:
        return "Needs Improvement"


df["Performance"] = df["Average"].apply(
    performance_level
)

print(df[
    ["Student_ID", "Name", "Average", "Performance"]
])

# ------------------------------------------------------------
# 6. FILTER HIGH-PERFORMING STUDENTS
# ------------------------------------------------------------

print("\n6. HIGH-PERFORMING STUDENTS")
print("-" * 75)

high_performers = df[df["Average"] >= 80]

print(
    high_performers[
        ["Student_ID", "Name", "Branch", "Average", "Performance"]
    ]
)

# ------------------------------------------------------------
# 7. SORT STUDENTS BY AVERAGE SCORE
# ------------------------------------------------------------

print("\n7. STUDENTS SORTED BY AVERAGE SCORE")
print("-" * 75)

sorted_students = df.sort_values(
    by="Average",
    ascending=False
)

print(
    sorted_students[
        ["Student_ID", "Name", "Branch", "Average"]
    ]
)

# ------------------------------------------------------------
# 8. BRANCH-WISE ANALYSIS USING GROUPBY
# ------------------------------------------------------------

print("\n8. BRANCH-WISE PERFORMANCE ANALYSIS")
print("-" * 75)

branch_analysis = df.groupby("Branch")[
    ["Maths", "Reading", "Writing", "Average"]
].mean()

print(branch_analysis.round(2))

# ------------------------------------------------------------
# 9. PIVOT TABLE
# ------------------------------------------------------------

print("\n9. PIVOT TABLE")
print("-" * 75)

pivot = pd.pivot_table(
    df,
    values=["Maths", "Reading", "Writing"],
    index="Branch",
    aggfunc="mean"
)

print(pivot.round(2))

# ------------------------------------------------------------
# 10. OVERALL STATISTICS
# ------------------------------------------------------------

print("\n10. OVERALL PERFORMANCE")
print("-" * 75)

overall_average = df["Average"].mean()
highest_average = df["Average"].max()
lowest_average = df["Average"].min()

top_student = df.loc[
    df["Average"].idxmax()
]

print(f"Overall Average Score : {overall_average:.2f}")
print(f"Highest Average Score : {highest_average:.2f}")
print(f"Lowest Average Score  : {lowest_average:.2f}")

print(
    f"Top Student           : "
    f"{top_student['Name']}"
)

print(
    f"Top Student Average   : "
    f"{top_student['Average']:.2f}"
)

# ------------------------------------------------------------
# 11. SUBJECT-WISE AVERAGE
# ------------------------------------------------------------

print("\n11. SUBJECT-WISE AVERAGE")
print("-" * 75)

subject_averages = df[subject_columns].mean()

print(subject_averages.round(2))

# ------------------------------------------------------------
# 12. EXPORT ANALYSIS RESULT
# ------------------------------------------------------------

print("\n12. EXPORTING ANALYSIS RESULT")
print("-" * 75)

output_directory = "output_files"

os.makedirs(
    output_directory,
    exist_ok=True
)

output_file = os.path.join(
    output_directory,
    "student_performance_analysis.csv"
)

df.to_csv(
    output_file,
    index=False
)

print(f"Analysis exported to: {output_file}")

# ------------------------------------------------------------
# 13. FINAL INSIGHTS
# ------------------------------------------------------------

print("\n13. KEY INSIGHTS")
print("-" * 75)

best_subject = subject_averages.idxmax()
best_subject_score = subject_averages.max()

best_branch = branch_analysis["Average"].idxmax()
best_branch_score = branch_analysis["Average"].max()

high_performer_count = len(high_performers)

print(
    f"1. The overall average student score is "
    f"{overall_average:.2f}."
)

print(
    f"2. {high_performer_count} students have an "
    f"average score of 80 or above."
)

print(
    f"3. {best_subject} has the highest subject "
    f"average of {best_subject_score:.2f}."
)

print(
    f"4. {best_branch} has the highest branch-wise "
    f"average of {best_branch_score:.2f}."
)

print(
    f"5. {top_student['Name']} achieved the highest "
    f"overall average of {top_student['Average']:.2f}."
)

print("\n" + "-" * 75)
print("Mini data analysis project completed successfully.")
print("=" * 75)