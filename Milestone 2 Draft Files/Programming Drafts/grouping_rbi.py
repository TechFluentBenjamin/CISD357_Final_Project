import pandas as pd

# input Raw URL for the CSV file containing salary data
url = "batting.csv"
df = pd.read_csv(url)


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