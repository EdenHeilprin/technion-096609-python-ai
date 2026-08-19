from pathlib import Path
from time import perf_counter

import pandas as pd

from experiment_core import OUTPUT_COLUMNS, build_trial_row, prepare_session


PARTICIPANT_CODE = "P900"
RANDOM_SEED = 12
MAX_RESPONSE_TIME_MS = 12000


def option_text(option_name, trial):
    if option_name == "sure":
        return f"Sure option: {trial['sure_points']} points"
    return (
        "Risky option: 50% chance of "
        f"{trial['risky_low_points']} points and 50% chance of "
        f"{trial['risky_high_points']} points"
    )


def collect_response(trial, condition):
    if condition == "sure_first":
        option_1 = "sure"
        option_2 = "risky"
    else:
        option_1 = "risky"
        option_2 = "sure"

    print(f"1 — {option_text(option_1, trial)}")
    print(f"2 — {option_text(option_2, trial)}")

    start_time = perf_counter()
    selected_key = input("Choose 1 or 2, or press Enter to simulate no response: ").strip()

    while selected_key not in ["1", "2", ""]:
        selected_key = input("Please choose 1 or 2, or press Enter: ").strip()

    response_time_ms = max(1, round((perf_counter() - start_time) * 1000))
    timed_out = selected_key == "" or response_time_ms > MAX_RESPONSE_TIME_MS
    return selected_key, response_time_ms, timed_out


base_folder = Path(__file__).parent
stimuli_path = base_folder / "data" / "stimuli.csv"
output_folder = base_folder / "output"
output_folder.mkdir(exist_ok=True)

stimuli = pd.read_csv(stimuli_path).to_dict("records")
condition, ordered_trials = prepare_session(stimuli, RANDOM_SEED)

print(f"Participant: {PARTICIPANT_CODE}")
print(f"Condition: {condition}")
print()

trial_rows = []

for display_position, trial in enumerate(ordered_trials, start=1):
    print(f"Trial {display_position} of {len(ordered_trials)}")
    selected_key, response_time_ms, timed_out = collect_response(trial, condition)

    row = build_trial_row(
        participant_code=PARTICIPANT_CODE,
        condition=condition,
        trial_id=trial["trial_id"],
        display_position=display_position,
        selected_key=selected_key,
        response_time_ms=response_time_ms,
        timed_out=timed_out,
    )
    trial_rows.append(row)
    print()

output_path = output_folder / f"{PARTICIPANT_CODE}.csv"
pd.DataFrame(trial_rows, columns=OUTPUT_COLUMNS).to_csv(output_path, index=False)

print(f"Saved {len(trial_rows)} rows to {output_path}")
