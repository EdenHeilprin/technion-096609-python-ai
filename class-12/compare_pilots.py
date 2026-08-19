from pathlib import Path

import pandas as pd


output_folder = Path(__file__).parent / "output"

for participant_code in ["P900", "P901"]:
    pilot_path = output_folder / f"{participant_code}.csv"
    pilot = pd.read_csv(pilot_path)
    trial_order = pilot.sort_values("display_position")["trial_id"].tolist()
    timeout_count = int(pilot["timed_out"].sum())

    print(
        f"{participant_code}: condition={pilot['condition'].iloc[0]}, "
        f"order={trial_order}, timeouts={timeout_count}"
    )
