# Summary Stats code by Benjamin Hays
# W0018940
# To be used to complete Table 4-1
# Analayzes salary_adjusted.csv and batting_clean.csv, and places information in a .CSV file, "analysis_summary.csv"
# Automatically opens the file
# November 23, 2026

import os
import platform
import subprocess
import pandas as pd


# Performs analysis on the two files
def analyze_csv_files(file_list, auto_open=True):
    all_summaries = []

    # Loop to read the files in the file_list
    for file_name in file_list:
        if not os.path.exists(file_name):
            print(f"Warning: {file_name} not found. Skipping.")
            continue

        df = pd.read_csv(file_name)
        df.columns = df.columns.str.strip()

        # Exclude yearID. Not case sensitive. YearID does not need to be analyzed.
        cols_to_drop = [c for c in df.columns if c.lower() == "yearid"]
        if cols_to_drop:
            df = df.drop(columns=cols_to_drop)

        summary = df.describe().T
        summary.index.name = "Attribute Name"
        summary["Source File"] = file_name
        all_summaries.append(summary)

    final_report = pd.concat(all_summaries, axis=0)

    # Change names of columns based on assignment requirements.
    final_report = final_report.rename(
        columns={
            "count": "Valid Count",
            "mean": "Mean",
            "std": "Std Deviation",
            "min": "Min",
            "50%": "Median",
            "25%": "25th Percentile",
            "75%": "75th Percentile",
            "max": "Max",
        }
    )

    # The filter. I want $ signs for salary, none for rbi.
    final_report["Valid Count"] = final_report["Valid Count"].astype(int)
    float_cols = [
        "Mean",
        "Min",
        "Median",
        "25th Percentile",
        "75th Percentile",
        "Max",
        "Std Deviation",
    ]

    final_report[float_cols] = final_report[float_cols].astype(object)

    # And now we get into the loop that applies the dollar signs (and the commas)
    def format_row(row):
        is_salary = "salary" in str(row["Source File"]).lower()
        for col in float_cols:
            if col in row and pd.notnull(row[col]):
                val = float(row[col])
                row[col] = f"${val:,.2f}" if is_salary else f"{val:.2f}"
        return row

    final_report = final_report.apply(format_row, axis=1)
    final_report = final_report.sort_values(by=["Source File", "Attribute Name"])

    output_filename = "analysis_summary.csv"
    final_report.to_csv(output_filename, index=True)

    if auto_open:
        open_file(output_filename)

    return final_report, output_filename


# Let's automatically open the file as well.
# I started coding for Linux. Gave up. I Don't know what default app opens it.


def open_file(filepath):
    system = platform.system()
    try:
        print(f"Attempting to open {filepath}...")
        if system == "Windows":
            subprocess.run(["notepad.exe", filepath])
        elif system == "Darwin":
            subprocess.run(["open", filepath])
    # elif system == "Linux":
    # I'm not fmailiar enough with Linux, and honestly I don't have time to figure out what app opens .CSV in Linux.
    except Exception as e:
        print(f"Could not open file automatically: {e}")


# main
if __name__ == "__main__":
    target_files = ["batting_clean.csv", "salary_adjusted.csv"]
    print("Starting analysis... (Strictly excluding yearID)...\n")

    report, output_file = analyze_csv_files(target_files, auto_open=True)

    if not report.empty:
        print("--- Statistical Analysis Report ---")
        print(report)
        print(f"\nSummary saved to '{output_file}'")
    else:
        print("No data was processed.")
