from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "decision_trials.csv"

trials = pd.read_csv(data_path)
completed_trials = trials.loc[trials["response_time_ms"].notna()].copy()

analysis = completed_trials.loc[
    :, ["participant_code", "trial_number", "condition", "response_time_ms", "points"]
].copy()
analysis["bonus_payment_ils"] = (analysis["points"] * 0.05).round(2)

summary = (
    analysis.groupby("condition", as_index=False)
    .agg(
        completed_trials=("trial_number", "count"),
        mean_response_time_ms=("response_time_ms", "mean"),
        mean_points=("points", "mean"),
        mean_bonus_payment_ils=("bonus_payment_ils", "mean"),
    )
    .round(2)
)

print("Derived trial data:")
print(analysis.to_string(index=False))
print("\nCondition summary:")
print(summary.to_string(index=False))

assert analysis.shape == (10, 6)
assert summary.shape == (2, 5)
assert set(summary["condition"]) == {"bonus", "control"}
assert summary["completed_trials"].sum() == 10
