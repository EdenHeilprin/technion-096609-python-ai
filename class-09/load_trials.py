from pathlib import Path

import pandas as pd


class_folder = Path(__file__).parent
data_path = class_folder / "data" / "trial_results.csv"

trials = pd.read_csv(data_path)

print("First five rows:")
print(trials.head())
print("Shape:", trials.shape)
