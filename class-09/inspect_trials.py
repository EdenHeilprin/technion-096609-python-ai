from pathlib import Path

import pandas as pd


class_folder = Path(__file__).parent
data_path = class_folder / "data" / "trial_results.csv"

trials = pd.read_csv(data_path)

print("Shape:", trials.shape)
print("Columns:", list(trials.columns))
print("\nData types:")
print(trials.dtypes)
print("\nMissing values:")
print(trials.isna().sum())
