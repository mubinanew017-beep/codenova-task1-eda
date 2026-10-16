
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Use the folder containing this script
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "penguins.csv"
OUTPUT_DIR = BASE_DIR / "eda_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

sns.set_theme(style="whitegrid")

# 1. Load the dataset
df = pd.read_csv(DATASET_PATH)

print("===== DATASET OVERVIEW =====")
print("Original shape:", df.shape)
print("\nFirst five rows:")
print(df.head())

print("\nColumn data types:")
print(df.dtypes)

print("\nDataset information:")
df.info()

print("\nSummary statistics:")
print(df.describe(include="all").T)

# 2. Check missing values
print("\n===== MISSING VALUES BEFORE CLEANING =====")
print(df.isnull().sum())

# 3. Check and remove duplicate rows
duplicate_count = df.duplicated().sum()
print("\nDuplicate rows found:", duplicate_count)

df = df.drop_duplicates().copy()
print("Shape after removing duplicates:", df.shape)

# 4. Detect potential outliers using the IQR method
# Detection only: potential outliers are not automatically deleted.
numeric_cols = df.select_dtypes(include="number").columns

print("\n===== POTENTIAL OUTLIERS (IQR METHOD) =====")
for col in numeric_cols:
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outlier_count = (
        (df[col] < lower_bound) | (df[col] > upper_bound)
    ).sum()

    print(
        f"{col}: {outlier_count} potential outliers "
        f"(bounds: {lower_bound:.2f} to {upper_bound:.2f})"
    )

# 5. Handle missing values
# Median is less affected by extreme values than the mean.
# Mode fills missing categorical values using the most frequent category.
for col in numeric_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns

for col in categorical_cols:
    if df[col].isnull().any():
        mode_values = df[col].mode()
        if not mode_values.empty:
            df[col] = df[col].fillna(mode_values.iloc[0])

print("\n===== MISSING VALUES AFTER CLEANING =====")
print(df.isnull().sum())

# Save cleaned data
cleaned_path = BASE_DIR / "penguins_cleaned.csv"
df.to_csv(cleaned_path, index=False)
print("\nCleaned dataset saved to:", cleaned_path)

# 6. Plot 1: Species distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="species", hue="species", legend=False)
plt.title("Distribution of Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Number of Penguins")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "species_count.png", dpi=300)
plt.close()

# 7. Plot 2: Body mass by species
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="species", y="body_mass_g", hue="species",
            legend=False)
plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "body_mass_by_species.png", dpi=300)
plt.close()

# 8. Plot 3: Correlation heatmap
plt.figure(figsize=(9, 6))
correlation = df.select_dtypes(include="number").corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm",
            fmt=".2f", vmin=-1, vmax=1)
plt.title("Correlation Between Numeric Features")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=300)
plt.close()

# 9. Plot 4: Numeric feature distributions
numeric_features = list(numeric_cols)

df[numeric_features].hist(
    figsize=(12, 8),
    bins=20,
    edgecolor="black"
)
plt.suptitle("Distributions of Numeric Penguin Features")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "feature_distributions.png", dpi=300)
plt.close()

# 10. Plot 5: Pairwise scatter plots
pairplot = sns.pairplot(
    df,
    vars=numeric_features,
    hue="species",
    diag_kind="hist"
)
pairplot.figure.suptitle(
    "Pairwise Relationships Between Numeric Features",
    y=1.02
)
pairplot.savefig(
    OUTPUT_DIR / "pairwise_scatter_plots.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close("all")

# 11. Plot 6: Missing values in the original dataset
original_df = pd.read_csv(DATASET_PATH)
missing_counts = original_df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]

if not missing_counts.empty:
    plt.figure(figsize=(9, 5))
    missing_counts.sort_values().plot(kind="bar")
    plt.title("Missing Values by Feature Before Cleaning")
    plt.xlabel("Feature")
    plt.ylabel("Number of Missing Values")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "missing_values.png", dpi=300)
    plt.close()

print("\n===== KEY DATASET FINDINGS =====")
print("Final dataset shape:", df.shape)

if "species" in df.columns:
    print("\nNumber of records by species:")
    print(df["species"].value_counts())

if {"species", "body_mass_g"}.issubset(df.columns):
    print("\nAverage body mass by species:")
    print(df.groupby("species")["body_mass_g"].mean().round(2))

print("\nEDA completed. Charts saved in:", OUTPUT_DIR)
