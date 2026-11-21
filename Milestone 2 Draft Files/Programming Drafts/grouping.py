# Grouping script by Benjamin Hays
# Analyzes Basketball players, batting data, and salary data.
# W0018940
# Last updated November 19, 2026
# Runs BEFORE the cleaning script!

import pandas as pd

# ==========================================
# PART 1: PEOPLE DATA ANALYSIS
# ==========================================
print("--- PART 1: PEOPLE DATA ---")

# Load the downloaded People CSV file.
df_people = pd.read_csv("people.csv")

final_game_col = "finalGame"

# Filter to include only retired players (those with info in finalGame)
df_people_filtered = df_people[df_people[final_game_col].notna()].copy()

# Map the number to the month for readability.
month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

df_people_filtered["birthMonth_name"] = df_people_filtered["birthMonth"].map(
    month_names
)

# Group by month and count the number of players in each month.
month_counts = (
    df_people_filtered["birthMonth_name"]
    .value_counts(dropna=False)
    .reindex(list(month_names.values()) + [float("nan")])
    .rename_axis("birth_month")
    .reset_index(name="player_count")
)

# Label any remaining unknown birth months cleanly
month_counts["birth_month"] = month_counts["birth_month"].fillna("Unknown")

print(month_counts.to_string(index=False))

valid_months = month_counts[month_counts["birth_month"] != "Unknown"]

if not valid_months.empty:
    highest_month = valid_months.loc[valid_months["player_count"].idxmax()]
    lowest_month = valid_months.loc[valid_months["player_count"].idxmin()]

    # Calculate the difference and percentage difference
    difference = int(highest_month["player_count"] - lowest_month["player_count"])
    percentage_diff = (difference / int(lowest_month["player_count"])) * 100

    print(
        f"\nHighest: {highest_month['birth_month']} ({int(highest_month['player_count']):,})"
    )
    print(
        f"Lowest:  {lowest_month['birth_month']} ({int(lowest_month['player_count']):,})"
    )
    print(f"Difference between highest and lowest birth month: {difference:,}")
    print(f"Percentage difference: {percentage_diff:.2f}%")


# ==========================================
# PART 2: BATTING DATA ANALYSIS
# ==========================================
print("\n--- PART 2: BATTING DATA ---")

# input the CSV file containing batting data
df_batting = pd.read_csv("batting.csv")
df_batting["year"] = pd.to_numeric(df_batting["yearID"], errors="coerce")

# Convert RBI to numeric and handle missing values
rbi_series = pd.to_numeric(df_batting["RBI"], errors="coerce")
missing_rbi_count = rbi_series.isna().sum()

print(f"Missing RBI rows: {missing_rbi_count:,}")

# Drop missing values for calculations
rbi_clean = rbi_series.dropna()

# Calculate stats
mean_rbi = rbi_clean.mean()
print(f"Mean RBI: {mean_rbi:,.2f}\n")

# Use quantiles for binning
q25 = rbi_clean.quantile(0.25)
q75 = rbi_clean.quantile(0.75)

bins = [float("-inf"), q25, q75, float("inf")]
labels = ["Bottom 25%", "Between 25% and 75%", "Above 75%"]

range_counts = (
    pd.cut(rbi_clean, bins=bins, labels=labels, include_lowest=True)
    .value_counts()
    .reindex(labels)
)

print("RBI Range Counts:")
print(range_counts.to_string())

# Year range check
earliest_year = df_batting["year"].min()
most_recent_year = df_batting["year"].max()
print(f"\nData Range: {earliest_year} to {most_recent_year}")

# Grouping years into bins for display
year_bins = [1985, 1990, 2000, 2020, 2025]
year_labels = ["1985 - 1989", "1990 - 1999", "2000 - 2019", "2020 - 2024"]

year_groups = pd.cut(
    df_batting["year"], bins=year_bins, labels=year_labels, right=False
)
year_counts = year_groups.value_counts().sort_index()

print("\nYearly Entry Counts:")
print(year_counts.to_string())


# ==========================================
# PART 3: SALARY DATA ANALYSIS
# ==========================================
print("\n--- PART 3: SALARY DATA ---")

# input Raw URL for the CSV file containing salary data
df_salary = pd.read_csv("salary.csv")
df_salary["year"] = pd.to_numeric(df_salary["yearID"], errors="coerce")

# Ensure salary is numeric and drop any missing values
salaries = pd.to_numeric(df_salary["salary"], errors="coerce").dropna()

mean_salary = salaries.mean()
print(f"Mean Salary: ${mean_salary:,.2f}\n")

q25 = salaries.quantile(0.25)
q75 = salaries.quantile(0.75)

print(f"25th Percentile Cutoff: ${q25:,.2f}")
print(f"75th Percentile Cutoff: ${q75:,.2f}\n")

# Group info into bins for salary
salary_bins = [float("-inf"), q25, q75, float("inf")]
salary_labels = ["Bottom 25%", "Between 25% and 75%", "Above 75%"]

range_counts_sal = (
    pd.cut(salaries, bins=salary_bins, labels=salary_labels, include_lowest=True)
    .value_counts()
    .reindex(salary_labels)
)

print("Salary Range Counts:")
print(range_counts_sal.to_string())

# Year range check for salary
earliest_year_s = df_salary["year"].min()
most_recent_year_s = df_salary["year"].max()
print(f"\nData Range: {earliest_year_s} to {most_recent_year_s}")

# Grouping salary information by year
year_bins_s = [1980, 1990, 2000, 2020, 2025]
year_labels_s = ["1980 - 1989", "1990 - 1999", "2000 - 2019", "2020 - 2024"]

year_groups_s = pd.cut(
    df_salary["year"], bins=year_bins_s, labels=year_labels_s, right=False
)
year_counts_s = year_groups_s.value_counts().sort_index()

print("\nYearly Entry Counts:")
print(year_counts_s.to_string())
