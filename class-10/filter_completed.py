"""Keep completed decision trials without changing the raw trial table."""

from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "decision_trials.csv"

trials = pd.read_csv(data_path)

# A recorded response time is the study's definition of a completed trial.
completed_mask = trials["response_time_ms"].notna()
completed_trials = trials.loc[completed_mask].copy()

print("Raw rows:", trials.shape[0])
print("Completed rows:", completed_trials.shape[0])
print("Timed-out rows:", (~completed_mask).sum())
print(
    "Missing response times after filtering:",
    completed_trials["response_time_ms"].isna().sum(),
)

assert trials.shape == (12, 6)
assert completed_trials.shape == (10, 6)
assert completed_trials["response_time_ms"].notna().all()
