# Analyze script 
# Code by Tristen Garcia
# Uploaded by Benjamin Hays
# Direct copy from sent script from Discord 
# November 20, 2026

import pandas as pd
from pathlib import Path

############### 
# Battting
############### 

script_folder = Path(__file__).resolve().parent
csv_file = script_folder / "batting.csv"

# Load the dataset
df = pd.read_csv(csv_file)

# 1. Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# 2. Display basic information about the dataset
print("\nDataset Information:")
df.info()

# 3. Calculate descriptive statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Display all column names
print("\nColumn Names:")
print(df.columns.tolist())


#######################
# PEOPLE
#######################

script_folder = Path(__file__).resolve().parent
csv_file = script_folder / "people.csv"

# Load the dataset
df = pd.read_csv(csv_file)

# 1. Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# 2. Display basic information about the dataset
print("\nDataset Information:")
df.info()

# 3. Calculate descriptive statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Display all column names
print("\nColumn Names:")
print(df.columns.tolist())

###############################
# SALARY
###############################

script_folder = Path(__file__).resolve().parent
csv_file = script_folder / "salary.csv"

# Load the dataset
df = pd.read_csv(csv_file)

# 1. Display the first 5 rows
print("First 5 Rows:")
print(df.head())

# 2. Display basic information about the dataset
print("\nDataset Information:")
df.info()

# 3. Calculate descriptive statistics
print("\nSummary Statistics:")
print(df.describe())

# 4. Display all column names
print("\nColumn Names:")
print(df.columns.tolist())
