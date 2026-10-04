# ============================================================
# WEEK 4 ASSIGNMENT
# Statistics, Data Visualization & Exploratory Data Analysis
# ============================================================

import os
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

warnings.filterwarnings("ignore")

# ============================================================
# PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "Week_4_Sales_Dataset.csv"
)

VIS_DIR = os.path.join(BASE_DIR, "visualizations")
SCREENSHOT_DIR = os.path.join(BASE_DIR, "screenshots")

os.makedirs(VIS_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv(DATASET_PATH)
df["Date"] = pd.to_datetime(df["Date"])

print("=" * 70)
print("WEEK 4 - STATISTICS, VISUALIZATION & EDA")
print("=" * 70)

print("\nDataset loaded successfully!")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# TASK 1: MEAN, MEDIAN & MODE
# ============================================================

print("\n" + "=" * 70)
print("TASK 1: MEAN, MEDIAN & MODE")
print("=" * 70)

total_price = df["TotalPrice"].dropna()

mean_value = total_price.mean()
median_value = total_price.median()
mode_value = total_price.mode().iloc[0]

print(f"\nMean of TotalPrice   : {mean_value:.2f}")
print(f"Median of TotalPrice : {median_value:.2f}")
print(f"Mode of TotalPrice   : {mode_value:.2f}")

print("\nExplanation:")
print("Mean represents the average sales value.")
print("Median represents the middle sales value when the data is ordered.")
print("Mode represents the most frequently occurring sales value.")


# ============================================================
# TASK 2: VARIANCE & STANDARD DEVIATION
# ============================================================

print("\n" + "=" * 70)
print("TASK 2: VARIANCE & STANDARD DEVIATION")
print("=" * 70)

variance_value = total_price.var()
std_value = total_price.std()

print(f"\nVariance             : {variance_value:.2f}")
print(f"Standard Deviation   : {std_value:.2f}")

print("\nExplanation:")
print(
    "Variance measures how widely the sales values are spread "
    "around the mean."
)

print(
    "Standard deviation represents the typical amount by which "
    "sales values differ from the mean."
)


# ============================================================
# TASK 3: CORRELATION & PROBABILITY
# ============================================================

print("\n" + "=" * 70)
print("TASK 3: CORRELATION & PROBABILITY")
print("=" * 70)

correlation = df["Quantity"].corr(df["TotalPrice"])

print(f"\nCorrelation between Quantity and TotalPrice: {correlation:.4f}")

if correlation > 0.7:
    relationship = "strong positive"
elif correlation > 0.3:
    relationship = "moderate positive"
elif correlation > 0:
    relationship = "weak positive"
elif correlation < -0.7:
    relationship = "strong negative"
elif correlation < -0.3:
    relationship = "moderate negative"
elif correlation < 0:
    relationship = "weak negative"
else:
    relationship = "no"

print(f"Relationship: {relationship}")

# Probability of a randomly selected order being returned
returned_probability = df["Returned"].mean()

print(
    f"\nProbability that a randomly selected order is returned: "
    f"{returned_probability:.4f}"
)

print(
    f"Percentage probability: "
    f"{returned_probability * 100:.2f}%"
)


# ============================================================
# TASK 4: OUTLIER DETECTION
# IQR METHOD
# ============================================================

print("\n" + "=" * 70)
print("TASK 4: OUTLIER DETECTION")
print("=" * 70)

Q1 = total_price.quantile(0.25)
Q3 = total_price.quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[
    (df["TotalPrice"] < lower_bound)
    | (df["TotalPrice"] > upper_bound)
]

print(f"\nQ1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")

print(f"\nLower Bound: {lower_bound:.2f}")
print(f"Upper Bound: {upper_bound:.2f}")

print(f"\nNumber of outliers: {len(outliers)}")

print("\nIdentified outliers:")
print(
    outliers[
        ["OrderID", "Product", "Quantity", "TotalPrice"]
    ].head(20)
)

print(
    "\nOutliers can strongly affect the mean, variance, "
    "correlation and other statistical calculations."
)
# ------------------------------------------------------------
# 5.1 LINE CHART
# ------------------------------------------------------------

# Convert daily sales into monthly sales for a cleaner visualization
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["TotalPrice"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "matplotlib_line_chart.png"),
    dpi=300
)

plt.close()

print("Line chart created.")

# ------------------------------------------------------------
# 5.2 BAR CHART
# ------------------------------------------------------------

region_sales = (
    df.groupby("Region")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "matplotlib_bar_chart.png"),
    dpi=300
)

plt.close()

print("Bar chart created.")


# ------------------------------------------------------------
# 5.3 PIE CHART
# ------------------------------------------------------------

product_sales = (
    df.groupby("Product")["TotalPrice"]
    .sum()
)

plt.figure(figsize=(8, 8))

plt.pie(
    product_sales.values,
    labels=product_sales.index,
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Product")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "matplotlib_pie_chart.png"),
    dpi=300
)


plt.close()

print("Pie chart created.")


# ------------------------------------------------------------
# 5.4 HISTOGRAM
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.hist(
    total_price,
    bins=30
)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Price")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "matplotlib_histogram.png"),
    dpi=300
)

plt.close()

print("Histogram created.")


# ------------------------------------------------------------
# 5.5 SCATTER PLOT
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

plt.scatter(
    df["Quantity"],
    df["TotalPrice"],
    alpha=0.6
)

plt.title("Quantity vs Total Price")
plt.xlabel("Quantity")
plt.ylabel("Total Price")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "matplotlib_scatter_plot.png"),
    dpi=300
)

plt.close()

print("Scatter plot created.")


# ============================================================
# TASK 6: SEABORN VISUALIZATION
# ============================================================

print("\n" + "=" * 70)
print("TASK 6: SEABORN VISUALIZATION")
print("=" * 70)

sns.set_theme()


# ------------------------------------------------------------
# 6.1 COUNT PLOT
# ------------------------------------------------------------

plt.figure(figsize=(9, 6))

sns.countplot(
    data=df,
    x="Region"
)

plt.title("Number of Orders by Region")
plt.xlabel("Region")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "seaborn_count_plot.png"),
    dpi=300
)

plt.close()

print("Count plot created.")


# ------------------------------------------------------------
# 6.2 BOX PLOT
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Region",
    y="TotalPrice"
)

plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Total Price")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "seaborn_box_plot.png"),
    dpi=300
)

plt.close()

print("Box plot created.")


# ------------------------------------------------------------
# 6.3 HEATMAP
# ------------------------------------------------------------

numeric_columns = [
    "Quantity",
    "UnitPrice",
    "Discount",
    "Returned",
    "ShippingCost",
    "TotalPrice"
]

correlation_matrix = df[numeric_columns].corr()

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    os.path.join(VIS_DIR, "seaborn_heatmap.png"),
    dpi=300
)

plt.close()

print("Heatmap created.")


# ------------------------------------------------------------
# 6.4 PAIR PLOT
# ------------------------------------------------------------

pair_data = df[
    [
        "Quantity",
        "UnitPrice",
        "Discount",
        "TotalPrice"
    ]
].dropna()

pair_data_sample = pair_data.sample(
    min(500, len(pair_data)),
    random_state=42
)

pair_plot = sns.pairplot(
    pair_data_sample
)

pair_plot.fig.suptitle(
    "Pair Plot of Numerical Variables",
    y=1.02
)

pair_plot.savefig(
    os.path.join(VIS_DIR, "seaborn_pair_plot.png"),
    dpi=300
)

plt.close()

print("Pair plot created.")


# ============================================================
# TASK 7: EDA - DATA INSPECTION & CLEANING
# ============================================================

print("\n" + "=" * 70)
print("TASK 7: EDA - DATA INSPECTION & CLEANING")
print("=" * 70)

# Create a copy
eda_df = df.copy()

print("\n--- BEFORE CLEANING ---")

print("\nShape:")
print(eda_df.shape)

print("\nColumn names:")
print(eda_df.columns.tolist())

print("\nData types:")
print(eda_df.dtypes)

print("\nStatistical Summary:")
print(eda_df.describe(include="all"))

print("\nMissing values:")
print(eda_df.isnull().sum())

print("\nDuplicate records:")
print(eda_df.duplicated().sum())


# ------------------------------------------------------------
# HANDLE MISSING VALUES
# ------------------------------------------------------------

numeric_cols = eda_df.select_dtypes(
    include=np.number
).columns

categorical_cols = eda_df.select_dtypes(
    include="object"
).columns

# Numeric columns → median
for col in numeric_cols:
    eda_df[col] = eda_df[col].fillna(
        eda_df[col].median()
    )

# Categorical columns → mode
for col in categorical_cols:
    if eda_df[col].isnull().sum() > 0:
        eda_df[col] = eda_df[col].fillna(
            eda_df[col].mode()[0]
        )


# ------------------------------------------------------------
# REMOVE DUPLICATES
# ------------------------------------------------------------

before_duplicates = len(eda_df)

eda_df = eda_df.drop_duplicates()

after_duplicates = len(eda_df)

print(
    f"\nDuplicate rows removed: "
    f"{before_duplicates - after_duplicates}"
)


# ------------------------------------------------------------
# CHECK INVALID VALUES
# ------------------------------------------------------------

print("\nChecking invalid values:")

print(
    "Negative Quantity:",
    (eda_df["Quantity"] < 0).sum()
)

print(
    "Negative UnitPrice:",
    (eda_df["UnitPrice"] < 0).sum()
)

print(
    "Invalid Discount:",
    (
        (eda_df["Discount"] < 0)
        | (eda_df["Discount"] > 1)
    ).sum()
)


# ------------------------------------------------------------
# AFTER CLEANING
# ------------------------------------------------------------

print("\n--- AFTER CLEANING ---")

print("\nShape:")
print(eda_df.shape)

print("\nMissing values:")
print(eda_df.isnull().sum())

print("\nDuplicate records:")
print(eda_df.duplicated().sum())

print("\nFirst 5 cleaned rows:")
print(eda_df.head())


# Save cleaned dataset
cleaned_path = os.path.join(
    BASE_DIR,
    "dataset",
    "Week_4_Sales_Dataset_Cleaned.csv"
)

eda_df.to_csv(
    cleaned_path,
    index=False
)

print(
    f"\nCleaned dataset saved to: "
    f"{cleaned_path}"
)


# ============================================================
# TASK 8: EDA - CORRELATION & INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("TASK 8: EDA - CORRELATION & INSIGHTS")
print("=" * 70)

clean_corr = eda_df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(clean_corr.round(3))

# Find strongest relationship excluding diagonal
corr_pairs = (
    clean_corr
    .where(
        np.triu(
            np.ones(clean_corr.shape),
            k=1
        ).astype(bool)
    )
    .stack()
    .sort_values(
        key=lambda x: x.abs(),
        ascending=False
    )
)

print("\nStrongest correlations:")
print(corr_pairs.head(5))


# ------------------------------------------------------------
# BUSINESS INSIGHTS
# ------------------------------------------------------------

highest_region = (
    eda_df.groupby("Region")["TotalPrice"]
    .sum()
    .idxmax()
)

highest_region_sales = (
    eda_df.groupby("Region")["TotalPrice"]
    .sum()
    .max()
)

highest_product = (
    eda_df.groupby("Product")["TotalPrice"]
    .sum()
    .idxmax()
)

highest_product_sales = (
    eda_df.groupby("Product")["TotalPrice"]
    .sum()
    .max()
)

return_rate = eda_df["Returned"].mean() * 100

average_order_value = eda_df["TotalPrice"].mean()

print("\n--- THREE KEY INSIGHTS ---")

print(
    f"1. {highest_region} has the highest total sales "
    f"with approximately {highest_region_sales:,.2f}."
)

print(
    f"2. {highest_product} is the highest-selling product "
    f"by total sales with approximately "
    f"{highest_product_sales:,.2f}."
)

print(
    f"3. The overall order return rate is approximately "
    f"{return_rate:.2f}%."
)

print(
    f"\nAverage order value is approximately "
    f"{average_order_value:,.2f}."
)


# ============================================================
# TASK 9: BUSINESS RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 70)
print("TASK 9: BUSINESS RECOMMENDATIONS")
print("=" * 70)

print("\nRecommendation 1:")
print(
    f"Focus marketing and inventory planning on the "
    f"{highest_region} region because it generated the "
    f"highest total sales."
)

print("\nRecommendation 2:")
print(
    f"Prioritize the {highest_product} product through "
    f"inventory availability and targeted promotions because "
    f"it generated the highest product-level sales."
)

print("\nAdditional Recommendation:")
print(
    "Monitor returned orders and investigate the reasons "
    "for returns to reduce potential revenue loss and "
    "improve customer satisfaction."
)


# ============================================================
# SAVE CLEANED SUMMARY
# ============================================================

summary = pd.DataFrame({
    "Metric": [
        "Mean TotalPrice",
        "Median TotalPrice",
        "Mode TotalPrice",
        "Variance TotalPrice",
        "Standard Deviation TotalPrice",
        "Quantity-TotalPrice Correlation",
        "Return Probability",
        "Number of Outliers",
        "Highest Sales Region",
        "Highest Sales Product"
    ],
    "Value": [
        mean_value,
        median_value,
        mode_value,
        variance_value,
        std_value,
        correlation,
        returned_probability,
        len(outliers),
        highest_region,
        highest_product
    ]
})

summary_path = os.path.join(
    BASE_DIR,
    "statistics_summary.csv"
)

summary.to_csv(
    summary_path,
    index=False
)

print(
    f"\nStatistics summary saved to: "
    f"{summary_path}"
)


# ============================================================
# FINAL MESSAGE
# ============================================================

print("\n" + "=" * 70)
print("WEEK 4 ANALYSIS COMPLETED SUCCESSFULLY")
print("=" * 70)

print("\nGenerated files:")
print("1. Cleaned dataset")
print("2. Statistics summary")
print("3. Matplotlib visualizations")
print("4. Seaborn visualizations")
print("5. EDA results")
print("6. Correlation analysis")
print("7. Business insights")
print("8. Business recommendations")