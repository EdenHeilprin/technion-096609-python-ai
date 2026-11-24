from pathlib import Path

import pandas as pd


# Find the CSV beside this script, even if VS Code runs it from another folder.
csv_path = Path(__file__).with_name("titanic.csv")
passengers = pd.read_csv(csv_path)

print("First five rows:")
print(passengers.head())
print("Passenger rows:", len(passengers))
