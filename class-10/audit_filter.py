"""Compare the study's completion rule with a plausible but incorrect shortcut."""

from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "decision_trials.csv"

trials = pd.read_csv(data_path)

# Zero-point trials can still be completed, so response time defines completion.
completed_trials = trials.loc[trials["response_time_ms"].notna()].copy()
positive_point_trials = trials.loc[trials["points"] > 0].copy()

completed_zero_point_trials = completed_trials.loc[
    completed_trials["points"] == 0,
    ["participant_code", "trial_number", "points"],
]

print("Completed by response time:", completed_trials.shape[0])
print("Rows with positive points:", positive_point_trials.shape[0])
print("\nCompleted zero-point trials:")
print(completed_zero_point_trials.to_string(index=False))

assert completed_trials.shape[0] == 10
assert positive_point_trials.shape[0] == 9
assert completed_zero_point_trials.shape[0] == 1
