# Script created by Benjamin Hays
# W0018940
# November 19, 2026

# Script imports csv information from the local directory for analysis.

import pandas as pd

# input the CSV file containing salary data
url = "batting.csv"
df = pd.read_csv(url)
df["year"] = pd.to_numeric(df["yearID"], errors="coerce")

rbi = pd.to_numeric(df["RBI"], errors="coerce").dropna()

# Finding the mean
mean_rbi = rbi.mean()
print(f"Mean rbi: ${mean_rbi:,.2f}\n")

# Use pandas qauntitle function to calculate the 25th and 75th percentiles of the salary data. The 25th percentile is the value below which 25% of the salaries fall, and the 75th percentile is the value below which 75% of the salaries fall.
q25 = rbi.quantile(0.25)
q75 = rbi.quantile(0.75)

# Group info into bins
bins = [float("-inf"), q25, q75, float("inf")]
labels = ["Bottom 25%", "Between 25% and 75%", "Above 75%"]

range_counts = (
    pd.cut(rbi, bins=bins, labels=labels, include_lowest=True)
    .value_counts()
    .reindex(labels)
)

# print output
print("RBI Range Counts:")
print(range_counts.to_string())

# any missing data????
rbi_numeric = pd.to_numeric(df["RBI"], errors="coerce")
missing_rbi_count = rbi_numeric.isna().sum()

print(f"Missing RBI rows: {missing_rbi_count:,}\n")

# Drop missing values for the calculations
rbi = rbi_numeric.dropna()

# finding how many years there are in the data
earliest_year = df["year"].min()
most_recent_year = df["year"].max()
print(f"\nData Range: {earliest_year} to {most_recent_year}")

# Yikes! That's a lot of years! Let's put them into bins
# Define bins for the years. We use 1985 because that's the oldest information in our salary sheet.

year_bins = [1985, 1990, 2000, 2020, 2025]
year_labels = ["1985 - 1989", "1990 - 1999", "2000 - 2019", "2020 - 2024"]

# Cutting time with pd.cut to group the years.
year_groups = pd.cut(df["year"], bins=year_bins, labels=year_labels, right=False)
year_counts = year_groups.value_counts().sort_index()

# And let's print!
print("\nYearly Entry Counts:")
print(year_counts.to_string())
