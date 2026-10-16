# Penguin Dataset — Exploratory Data Analysis

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Palmer Penguins dataset to understand penguin species, physical measurements, data quality, and relationships between numeric features.

## Objectives

- Inspect dataset structure, dimensions, data types, and summary statistics.
- Identify missing values and duplicate records.
- Detect potential outliers using the Interquartile Range (IQR) method.
- Clean missing data using median and mode imputation.
- Visualize feature distributions, correlations, and pairwise relationships.
- Summarize meaningful findings from the analysis.

## Dataset Information

- **Records:** 344
- **Features:** 8
- **Species:** Adelie, Chinstrap, Gentoo
- **Categorical features:** species, island, sex
- **Numeric features:** bill length, bill depth, flipper length, body mass, year

## Data Cleaning

The initial dataset contained:

- 2 missing values in `bill_length_mm`
- 2 missing values in `bill_depth_mm`
- 2 missing values in `flipper_length_mm`
- 2 missing values in `body_mass_g`
- 11 missing values in `sex`
- 0 duplicate rows

Missing numeric values were filled using the median of each column. Missing categorical values were filled using the most frequent category (mode). No duplicate rows were removed because none were detected.

The cleaned dataset retained 344 records and 8 columns, with no missing values remaining.

Potential outliers were investigated using the IQR method. Unusual measurements should not automatically be removed because they may represent valid biological variation.

## Visualizations

The project generates the following charts:

1. **Correlation Heatmap:** Examines relationships between numeric measurements.
2. **Feature Distributions:** Shows the distributions of bill length, bill depth, flipper length, and body mass.
3. **Boxplots:** Displays medians, spread, and potential outliers.
4. **Pairwise Scatter Plots:** Compares numeric features and distinguishes species by colour.
5. **Body Mass by Species:** Compares body mass distributions across species.

## Key Findings

- Adelie is the most frequent species in the dataset, with 152 records.
- Numeric features have different measurement ranges and distributions.
- The heatmap helps identify numeric features that vary together.
- Pairwise scatter plots help explore relationships and possible separation between species.
- Boxplots highlight measurements that may require further investigation.

Specific correlation strengths and species-level differences should be interpreted from the generated charts.

## Project Files

- `eda_analysis.py` — Python script for EDA and chart generation.
- `penguins.csv` — Original dataset.
- `penguins_cleaned.csv` — Cleaned dataset.
- `penguins_eda_analysis.ipynb` — Jupyter Notebook containing the analysis and explanations.
- `correlation_heatmap.png` — Correlation visualization.
- `feature_distributions.png` — Numeric feature histograms.
- `boxplots.png` — Boxplots for potential outlier analysis.
- `pairwise_scatter_plots.png` — Pairwise feature relationships.
- `body_mass_by_species.png` — Body mass comparison by species.

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook / Google Colab

## How to Run

Install the required libraries:

```bash
python -m pip install pandas matplotlib seaborn
```

Place `penguins.csv` in the same folder as `eda_analysis.py`, then run:

```bash
python eda_analysis.py
```

The generated charts are saved in the `eda_outputs` directory.

## Limitations

- Median and mode imputation can affect the original distributions.
- Correlation does not establish causation.
- IQR-based outlier detection identifies potential outliers, not necessarily incorrect data.
- Findings describe the available dataset and should not automatically be generalized to every penguin population.

## Conclusion

This project demonstrates data inspection, cleaning, outlier detection, statistical summaries, and visualization using Python. It provides a reproducible starting point for understanding the Palmer Penguins dataset.
