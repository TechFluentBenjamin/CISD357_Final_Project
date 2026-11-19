# Code by Benjamin Hays
# W0018940
# Script updated November 19, 2026

# Used as input for Table 4-2, Salary grouping

import pandas as pd

# input Raw URL for the CSV file containing salary data
url = "salary.csv"
df = pd.read_csv(url)
df["year"] = pd.to_numeric(df["yearID"], errors="coerce")

# Ensure salary is numeric and drop any missing values
salaries = pd.to_numeric(df["salary"], errors="coerce").dropna()

# The mean salary clculations using pandas mean() function. The mean salary is calculated by summing all the salaries and dividing by the number of salaries.
mean_salary = salaries.mean()
print(f"Mean Salary: ${mean_salary:,.2f}\n")

# Use pandas qauntitle function to calculate the 25th and 75th percentiles of the salary data. The 25th percentile is the value below which 25% of the salaries fall, and the 75th percentile is the value below which 75% of the salaries fall.
q25 = salaries.quantile(0.25)
q75 = salaries.quantile(0.75)

print(f"25th Percentile Cutoff: ${q25:,.2f}")
print(f"75th Percentile Cutoff: ${q75:,.2f}\n")

# Group info into bins
bins = [float("-inf"), q25, q75, float("inf")]
labels = ["Bottom 25%", "Between 25% and 75%", "Above 75%"]

range_counts = (
    pd.cut(salaries, bins=bins, labels=labels, include_lowest=True)
    .value_counts()
    .reindex(labels)
)

print("Salary Range Counts:")
print(range_counts.to_string())

# What's the year range in our spreadshet? 
earliest_year = df["year"].min()
most_recent_year = df["year"].max()
print(f"\nData Range: {earliest_year} to {most_recent_year}")

# Grouping salry information. To be used to "normalize" salary calculations

# Define bins for the years.
year_bins = [1980, 1990, 2000, 2020, 2025]
year_labels = ["1980 - 1989", "1990 - 1999", "2000 - 2019", "2020 - 2024"]

# pd.cut to cut
year_groups = pd.cut(df["year"], bins=year_bins, labels=year_labels, right=False)
year_counts = year_groups.value_counts().sort_index()

# Display the text
print("\nYearly Entry Counts:")
print(year_counts.to_string())