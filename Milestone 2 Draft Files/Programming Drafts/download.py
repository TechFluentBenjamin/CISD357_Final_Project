# Created by Benjamin Hays
# W0018940
# Thurdsday, November 19, 2026

# This file downloads the three .csv files and saves them locally
# This file does not use any type of robustness or additional modules

import urllib.request

print('Downlaoding batting information')

url = "https://raw.githubusercontent.com/cwhkami007/Lahmann-Baseball-Database-2025-2026-Salary-Updated-2024-/refs/heads/main/moneyballdatabase/Batting.csv"
filename1 = "batting.csv"

urllib.request.urlretrieve(url, filename1)

print("Download batting complet!")

print ('Downloading salary information')
url = "https://raw.githubusercontent.com/cwhkami007/Lahmann-Baseball-Database-2025-2026-Salary-Updated-2024-/main/moneyballdatabase/Salaries.csv"
filename2 = "salary.csv"

urllib.request.urlretrieve(url, filename2)

print ("Download salary complete!")

print ('Downloading RBI information')
url = "https://raw.githubusercontent.com/cwhkami007/Lahmann-Baseball-Database-2025-2026-Salary-Updated-2024-/refs/heads/main/moneyballdatabase/Batting.csv" 

filename3 = "rbi.csv"

urllib.request.urlretrieve(url, filename3)

print ("Download RBI complete!")

print ("Downlaoding People information")

url = "https://raw.githubusercontent.com/SeanG347/LahmanBaseballDatabase/refs/heads/main/People.csv"

filename4="people.csv"
urllib.request.urlretrieve(url, filename4)