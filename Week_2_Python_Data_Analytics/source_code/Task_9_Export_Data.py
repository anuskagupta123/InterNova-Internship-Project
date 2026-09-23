import pandas as pd
import os

print("=" * 70)
print("       NUMPY & PANDAS FOR DATA ANALYTICS - TASK 9")
print("                    EXPORTING DATA")
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
# 2. PROCESS THE DATA
# ------------------------------------------------------------

print("\n2. PROCESSING DATA")
print("-" * 70)

processed_df = df[
    ["Student_ID", "Name", "Branch", "Maths", "Reading", "Writing"]
].copy()

# Calculate average score
processed_df["Average"] = processed_df[
    ["Maths", "Reading", "Writing"]
].mean(axis=1)

# Sort by average score
processed_df = processed_df.sort_values(
    by="Average",
    ascending=False
)

print("Processed Dataset:")
print(processed_df)

# ------------------------------------------------------------
# 3. CREATE OUTPUT DIRECTORY
# ------------------------------------------------------------

output_directory = "output_files"

os.makedirs(
    output_directory,
    exist_ok=True
)

# ------------------------------------------------------------
# 4. EXPORT DATA TO CSV
# ------------------------------------------------------------

output_file = os.path.join(
    output_directory,
    "processed_students.csv"
)

processed_df.to_csv(
    output_file,
    index=False
)

print("\n3. DATA EXPORT")
print("-" * 70)
print(f"File exported successfully:")
print(output_file)

# ------------------------------------------------------------
# 5. VERIFY EXPORTED FILE
# ------------------------------------------------------------

print("\n4. VERIFYING EXPORTED FILE")
print("-" * 70)

if os.path.exists(output_file):

    print("Export Status : SUCCESS")
    print(f"File Name     : {output_file}")
    print(
        f"File Size     : {os.path.getsize(output_file)} bytes"
    )

else:

    print("Export Status : FAILED")

# ------------------------------------------------------------
# 6. READ EXPORTED FILE
# ------------------------------------------------------------

print("\n5. READING EXPORTED FILE")
print("-" * 70)

verified_df = pd.read_csv(output_file)

print(verified_df)

print("\n" + "-" * 70)
print("Data exporting and verification completed successfully.")
print("=" * 70)