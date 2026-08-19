from pathlib import Path

import pandas as pd


class_folder = Path(__file__).parent
source_path = class_folder / "data" / "trial_results.csv"
output_folder = class_folder / "output"
output_path = output_folder / "checked_trial_results.csv"

trials = pd.read_csv(source_path)

output_folder.mkdir(exist_ok=True)
trials.to_csv(output_path, index=False)

saved_trials = pd.read_csv(output_path)

assert list(saved_trials.columns) == list(trials.columns)
assert saved_trials.shape == trials.shape

print("Saved rows:", saved_trials.shape[0])
print("Saved columns:", saved_trials.shape[1])
print("Output file:", output_path.name)
