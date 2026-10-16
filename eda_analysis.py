import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
#Load the real dataset
penguins = pd.read_csv("Task1-EDA/penguins.csv")

print("\n--- First 5 Rows ---")
print(penguins.head())

print("\n--- Dataset Shape ---")
print(penguins.shape)

print("\n--- Missing Values ---")
print(penguins.isnull().sum())
print("\n--- Penguin Species ---")
print(penguins["species"].value_counts())

print("\n--- Basic Statistics ---")
print(penguins.describe())

# Count of each penguin species
plt.figure(figsize=(8, 5))

sns.countplot(data=penguins, x="species")

plt.title("Count of Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Number of Penguins")

plt.savefig("Task1-EDA/species_count.png")
plt.show()

print("Species count graph created successfully!")

# Body mass comparison by species
plt.figure(figsize=(8, 5))

sns.boxplot(data=penguins, x="species", y="body_mass_g")

plt.title("Body Mass Distribution by Penguin Species")
plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")

plt.savefig("Task1-EDA/body_mass_by_species.png")
plt.show()

print("Body mass graph created successfully!")

# Correlation heatmap
numeric_data = penguins.select_dtypes(include="number")

correlation = numeric_data.corr()

plt.figure(figsize=(8, 6))

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap of Penguin Measurements")

plt.savefig("Task1-EDA/correlation_heatmap.png")
plt.show()

print("Correlation heatmap created successfully!")

# Handle missing values
print("\n--- Missing Values Before Cleaning ---")
print(penguins.isnull().sum())

# Create a copy of the dataset
cleaned_penguins = penguins.copy()

# Fill missing numeric values with their column median
numeric_columns = cleaned_penguins.select_dtypes(include="number").columns

for column in numeric_columns:
    cleaned_penguins[column] = cleaned_penguins[column].fillna(
        cleaned_penguins[column].median()
    )

# Fill missing categorical values with the most common value
categorical_columns = cleaned_penguins.select_dtypes(
    include=["object", "category"]
).columns

for column in categorical_columns:
    cleaned_penguins[column] = cleaned_penguins[column].fillna(
        cleaned_penguins[column].mode()[0]
    )

print("\n--- Missing Values After Cleaning ---")
print(cleaned_penguins.isnull().sum())

# Save the cleaned dataset
cleaned_penguins.to_csv("Task1-EDA/penguins_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully!")

# Final EDA Summary
print("\n========== EDA SUMMARY ==========")

print("\n1. Dataset Overview")
print(f"Total penguin records: {len(penguins)}")
print(f"Total columns: {len(penguins.columns)}")

print("\n2. Species Distribution")
print(penguins["species"].value_counts())

print("\n3. Average Body Mass by Species")
print(
    penguins.groupby("species")["body_mass_g"]
    .mean()
    .round(2)
)

print("\n4. Average Flipper Length by Species")
print(
    penguins.groupby("species")["flipper_length_mm"]
    .mean()
    .round(2)
)

print("\n5. EDA completed successfully!")
