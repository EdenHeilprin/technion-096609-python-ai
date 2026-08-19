from pathlib import Path

import pandas as pd


DATA_FILENAME = "pilot_trials.csv"
data_path = Path(__file__).parent / "data" / DATA_FILENAME

EXPECTED_COLUMNS = [
    "participant_code",
    "condition",
    "trial_id",
    "display_position",
    "option_1",
    "selected_key",
    "choice",
    "response_time_ms",
    "timed_out",
]

EXPECTED_TRIALS = {"T01", "T02", "T03", "T04"}
EXPECTED_POSITIONS = {1, 2, 3, 4}
ALLOWED_CONDITIONS = {"sure_first", "risky_first"}


def validate_pilot(file_path):
    trials = pd.read_csv(file_path)

    assert list(trials.columns) == EXPECTED_COLUMNS, "The column schema is incorrect"
    assert trials["participant_code"].notna().all(), "A participant code is missing"
    assert trials["condition"].isin(ALLOWED_CONDITIONS).all(), "A condition label is invalid"

    for participant_code, participant_trials in trials.groupby("participant_code"):
        assert participant_trials.shape[0] == 4, (
            f"{participant_code}: expected 4 trial rows"
        )
        assert participant_trials["condition"].nunique() == 1, (
            f"{participant_code}: condition changes within participant"
        )
        assert set(participant_trials["trial_id"]) == EXPECTED_TRIALS, (
            f"{participant_code}: trial identities are incomplete or duplicated"
        )
        assert set(participant_trials["display_position"]) == EXPECTED_POSITIONS, (
            f"{participant_code}: display positions are incomplete or duplicated"
        )

    for _, row in trials.iterrows():
        expected_first = "sure" if row["condition"] == "sure_first" else "risky"
        row_label = f"{row['participant_code']} {row['trial_id']}"

        assert row["option_1"] == expected_first, (
            f"{row_label}: option_1 should be {expected_first} "
            f"for condition {row['condition']}"
        )

        if row["timed_out"]:
            assert pd.isna(row["selected_key"]), (
                f"{row_label}: a timed-out trial has a selected key"
            )
            assert pd.isna(row["choice"]), (
                f"{row_label}: a timed-out trial has a choice"
            )
            assert pd.isna(row["response_time_ms"]), (
                f"{row_label}: a timed-out trial has a response time"
            )
        else:
            assert row["selected_key"] in [1, 2], (
                f"{row_label}: selected_key must be 1 or 2"
            )

            expected_choice = row["option_1"]
            if row["selected_key"] == 2:
                expected_choice = "risky" if row["option_1"] == "sure" else "sure"

            assert row["choice"] == expected_choice, (
                f"{row_label}: selected key and semantic choice do not agree"
            )
            assert 0 < row["response_time_ms"] <= 12000, (
                f"{row_label}: response time is outside the allowed range"
            )

    return trials


checked_trials = validate_pilot(data_path)

print("File:", DATA_FILENAME)
print("Rows:", checked_trials.shape[0])
print("Participants:", checked_trials["participant_code"].nunique())
print("All contract checks passed")
