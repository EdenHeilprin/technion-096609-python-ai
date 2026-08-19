from pathlib import Path

import pandas as pd

from experiment_core import OUTPUT_COLUMNS


PARTICIPANT_CODE = "P900"

output_path = Path(__file__).parent / "output" / f"{PARTICIPANT_CODE}.csv"
data = pd.read_csv(output_path)

assert data.columns.tolist() == OUTPUT_COLUMNS, "Unexpected output columns or order"
assert len(data) == 4, "Expected exactly four trial rows"
assert data["participant_code"].tolist() == [PARTICIPANT_CODE] * 4, (
    "Participant code should match the selected pilot"
)
assert data["condition"].nunique() == 1, "Condition must remain constant"
assert data["condition"].iloc[0] in ["sure_first", "risky_first"], (
    "Unexpected condition"
)
assert sorted(data["trial_id"].tolist()) == ["T01", "T02", "T03", "T04"], (
    "Each trial identity should appear once"
)
assert sorted(data["display_position"].tolist()) == [1, 2, 3, 4], (
    "Display positions should be 1 through 4"
)

expected_option_1 = "sure" if data["condition"].iloc[0] == "sure_first" else "risky"
assert data["option_1"].tolist() == [expected_option_1] * 4, (
    "option_1 does not match the assigned condition"
)

completed = data.loc[data["timed_out"] == False].copy()
timed_out = data.loc[data["timed_out"] == True].copy()

assert completed["selected_key"].isin([1, 2]).all(), "Completed keys must be 1 or 2"
assert completed["choice"].isin(["sure", "risky"]).all(), (
    "Completed choices must be sure or risky"
)
assert completed["response_time_ms"].between(1, 12000).all(), (
    "Completed response times must be from 1 through 12000 milliseconds"
)

for _, row in completed.iterrows():
    if int(row["selected_key"]) == 1:
        expected_choice = row["option_1"]
    elif row["option_1"] == "sure":
        expected_choice = "risky"
    else:
        expected_choice = "sure"
    assert row["choice"] == expected_choice, (
        f"{row['trial_id']}: selected key and semantic choice disagree"
    )

assert timed_out[["selected_key", "choice", "response_time_ms"]].isna().all().all(), (
    "Timeout rows should have no key, choice, or response time"
)

print(f"File: {output_path.name}")
print(f"Rows: {len(data)}")
print(f"Condition: {data['condition'].iloc[0]}")
print("All output checks passed")
