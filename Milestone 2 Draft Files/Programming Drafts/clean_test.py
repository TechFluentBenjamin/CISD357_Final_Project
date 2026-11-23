# Testing script
# Written by Benjamin Hays
# W0018940
# Always a good idea to test. This tests the program "clean.py"

import unittest
import pandas as pd
import numpy as np
from clean import normalize_col_name, remove_incomplete_rows


class TestCleaningLogic(unittest.TestCase):

    def test_normalize_col_name(self):
        # Are the column names stripped, lowercase, and spaces replace by underscores?
        self.assertEqual(normalize_col_name("  Salary 2026  "), "salary_2026")
        self.assertEqual(normalize_col_name("PlayerName"), "playername")
        self.assertEqual(normalize_col_name("team_id"), "team_id")

    def test_remove_incomplete_rows_with_nan(self):
        # Are NaN rows removed?
        data = {"name": ["Player A", "Player B", "Player C"], "score": [10, np.nan, 30]}
        df = pd.DataFrame(data)
        cleaned_df = remove_incomplete_rows(df)
        # Should only have 2 rows left. NaN gone?
        self.assertEqual(len(cleaned_df), 2)

    def test_remove_incomplete_rows_no_nan(self):
        # Are no rows removed if data is complete?
        data = {"name": ["Player A", "Player B"], "score": [10, 20]}
        df = pd.DataFrame(data)
        cleaned_df = remove_incomplete_rows(df)
        self.assertEqual(len(cleaned_df), 2)

    def test_regex_whitespace_to_na(self):
        # If there's whitespace, is it converted to NaN, simulating df = df.replace(r"^\s*$", pd.NA, regex=True
        data = {"name": ["Player A", "   ", "Player C"]}
        df = pd.DataFrame(data)
        # Logic!
        df = df.replace(r"^\s*$", pd.NA, regex=True)

        self.assertTrue(pd.isna(df.iloc[1, 0]))
        self.assertEqual(df.iloc[0, 0], "Player A")

    def test_column_normalization_loop(self):
        # Headers
        raw_headers = ["Name", "  Birth Date  ", "TEAM_ID"]
        cleaned_headers = [normalize_col_name(col) for col in raw_headers]

        expected_headers = ["name", "birth_date", "team_id"]
        self.assertEqual(cleaned_headers, expected_headers)


if __name__ == "__main__":
    unittest.main()
