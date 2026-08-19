from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "pilot_trials.csv"

trials = pd.read_csv(data_path)

print("Shape:", trials.shape)
print("Columns:", list(trials.columns))
print()
print("Rows per participant:")
print(trials.groupby("participant_code").size())
print()
print("Conditions per participant:")
print(trials.groupby("participant_code")["condition"].nunique())
print()
print("Missing values:")
print(trials.isna().sum())
