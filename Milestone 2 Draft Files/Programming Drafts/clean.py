# Benjamin Hays
# W0018940
# CISP 357 - Introduction to Data Science
# Code to clean the csv files for missing information and specific column removal.
# Added values for infaltion adjusted
# November 19, 2026

import os
import pandas as pd


def normalize_col_name(col_name):
    # In data science, column names are lowercase
    return col_name.strip().lower().replace(" ", "_")


def remove_incomplete_rows(df):
    # Missing values be gone!
    initial_row_count = len(df)
    df_cleaned = df.dropna(axis=0, how="any")
    final_row_count = len(df_cleaned)

    dropped_count = initial_row_count - final_row_count
    if dropped_count > 0:
        print(f"  -> Removed {dropped_count} row(s) containing missing information.")
    else:
        print("  -> No incomplete rows found.")

    return df_cleaned


def clean_csv_headers(file_path, columns_to_drop=None, drop_if_column_blank=None):
    #    Converts headers to lowercase/underscores, removes specific columns, handles conditional row removal, and drops rows with missing values.
    try:
        #Load the original CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.\n")
        return
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.\n")
        return
    except Exception as e:
        print(f"An error occurred while reading '{file_path}': {e}\n")
        return

    # Cleaning columns
    df.columns = [normalize_col_name(col) for col in df.columns]

    # Whitespace to NaN (no text or information there. Required for stripping)
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # Let's remove rows with missing information!
    if drop_if_column_blank:
        target_col = normalize_col_name(drop_if_column_blank)
        if target_col in df.columns:
            initial_count = len(df)
            df = df[df[target_col].notna()]
            dropped_rows = initial_count - len(df)
            if dropped_rows > 0:
                print(
                    f"  -> Removed {dropped_rows} row(s) where '{target_col}' was blank."
                )
        else:
            print(
                f"  -> Warning: Blank-check column '{target_col}' not found in '{file_path}'."
            )

    # Column dropping
    if columns_to_drop:
        cols_to_remove = [normalize_col_name(c) for c in columns_to_drop]
        existing_cols_to_drop = [c for c in cols_to_remove if c in df.columns]
        missing_cols = [c for c in cols_to_remove if c not in df.columns]

        if missing_cols:
            print(f"  -> Warning: Columns not found and skipped: {missing_cols}")

        df = df.drop(columns=existing_cols_to_drop)

    # Rows with NaN, removed!
    df = remove_incomplete_rows(df)

    # New file name. NEVER work with an existing file
    base_name, ext = os.path.splitext(file_path)
    output_file_path = f"{base_name}_clean{ext}"

    # Saving
    df.to_csv(output_file_path, index=False)
    print(f"Success! Cleaned file saved as: '{output_file_path}'\n")


def calculate_inflationary_salary(file_path):
    # reads the clean salary file to perform calculations.
    try:
        # Load the cleaned file
        df = pd.read_csv(file_path)

        target_year_col = "yearid"
        target_salary_col = "salary"

        if target_year_col not in df.columns or target_salary_col not in df.columns:
            print(
                f"Error: Required columns ('{target_year_col}' or '{target_salary_col}') not found in {file_path}."
            )
            return

        # Create new column, initialized as empty
        df["salary_2026"] = pd.NA

        def get_multiplier(year):
            if 1980 <= year <= 1989:
                return 3.14
            elif 1990 <= year <= 1999:
                return 2.58
            elif 2000 <= year <= 2009:
                return 1.96
            elif 2010 <= year <= 2019:
                return 1.55
            elif 2020 <= year <= 2026:
                return 1.30
            else:
                return None

        print(f"Calculating inflation adjustments for {file_path}...")

        # Apply multiplier
        df["multiplier"] = df[target_year_col].apply(get_multiplier)

        # Perform the calculation. Round() to ensure no long trailing decimals from math operations
        df["salary_2026"] = (df[target_salary_col] * df["multiplier"]).round(0)

        # uses integers in 64. I don't want zeros!
        df[target_salary_col] = df[target_salary_col].astype("Int64")
        df["salary_2026"] = df["salary_2026"].astype("Int64")

        #adds a comma and dollar sign to currency for readabliltity. 
        df["salary_2026"] = df["salary_2026"].apply( lambda x: f"${int(x):,}" if pd.notna(x) else "" )


        # Drop the temporary multiplier column
        df = df.drop(columns=["multiplier"])

        # Save as a final version
        base_name, ext = os.path.splitext(file_path)
        final_output_path = f"salary_adjusted{ext}"
        df.to_csv(final_output_path, index=False)
        print(f"Success! Inflation-adjusted file saved as: '{final_output_path}'\n")

    except Exception as e:
        print(f"An error occurred during salary calculation: {e}\n")


if __name__ == "__main__":
    # Dictionary format! Allows easy editing on what to drop and not drop.
    file_configs = {
        "batting.csv": {
            "drop": [
                "stint",
                "teamid",
                "lgid",
                "g",
                "ab",
                "r",
                "h",
                "2b",
                "3b",
                "hr",
                "sb",
                "cs",
                "bb",
                "so",
                "ibb",
                "hbp",
                "sh",
                "sf",
                "gidp",
            ]
        },
        "people.csv": {
            "drop": [
                "id",
                "birthday",
                "birthcity",
                "birthcountry",
                "birthstate",
                "deathyear",
                "deathmonth",
                "deathday",
                "deathcountry",
                "deathstate",
                "deathcity",
                "weight",
                "height",
                "bats",
                "throws",
                "debut",
                "bbrefid",
                "retroid",
            ],
            "blank_check": "finalgame",
        },
        "salary.csv": {"drop": ["teamid", "lgid"]},
    }

    print("Starting CSV sanitization and column removal...\n")

    all_files = ["people.csv", "salary.csv", "batting.csv"]

    for file in all_files:
        print(f"Processing '{file}'...")
        config = file_configs.get(file, {})

        clean_csv_headers(
            file,
            columns_to_drop=config.get("drop"),
            drop_if_column_blank=config.get("blank_check"),
        )

    print("Starting inflation adjustments...\n")

    # What's in salary clean? Let's look at it!
    target_salary_file = "salary_clean.csv"
    if os.path.exists(target_salary_file):
        calculate_inflationary_salary(target_salary_file)
    else:
        print(
            f"Warning: Could not find '{target_salary_file}' to perform inflation math."
        )

    os.remove("salary_clean.csv")

    print("All processes completed!")
