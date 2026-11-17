#Script by Benjamin Hays
#Groups players by birth month and counts the number of players in each month.
#Displasy information on console.

import pandas as pd

# Load the downloaded People CSV file. This uses a github copy from another individual.
df = pd.read_csv("https://raw.githubusercontent.com/SeanG347/LahmanBaseballDatabase/refs/heads/main/People.csv")

final_game_col = "finalGame" 

# The research question investigates only retired players, and those are players with information in the finalGame column. Filter the DataFrame to include only those players.
df_filtered = df[df[final_game_col].notna()].copy()

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

df_filtered["birthMonth_name"] = df_filtered["birthMonth"].map(month_names)

# Group by month and count the number of players in each month. Include a row for unknown birth months.
month_counts = (
    df_filtered["birthMonth_name"]
    .value_counts(dropna=False)
    .reindex(list(month_names.values()) + [float("nan")])
    .rename_axis("birth_month")
    .reset_index(name="player_count")
)

# Label any remaining unknown birth months cleanly
month_counts["birth_month"] = month_counts["birth_month"].fillna("Unknown")

print(month_counts.to_string(index=False))

valid_months = month_counts[month_counts["birth_month"] != "Unknown"]
highest_month = valid_months.loc[valid_months["player_count"].idxmax()]
lowest_month = valid_months.loc[valid_months["player_count"].idxmin()]

# Calculate the difference and percentage difference between the highest and lowest birth month counts

difference = int(highest_month["player_count"] - lowest_month["player_count"])

precentage_count = (difference / int(lowest_month["player_count"])) * 100

print(
    f"\nHighest: {highest_month['birth_month']} ({int(highest_month['player_count']):,})"
)
print(
    f"Lowest:  {lowest_month['birth_month']} ({int(lowest_month['player_count']):,})"
)
print(f"Difference between highest and lowest birth month: {difference:,}")
print(f"Percentage difference: {precentage_count:.2f}%")