from pathlib import Path

import pandas as pd

from experiment_core import prepare_session


data_path = Path(__file__).parent / "data" / "stimuli.csv"
stimuli = pd.read_csv(data_path).to_dict("records")

for seed in [12, 12, 27]:
    condition, ordered_trials = prepare_session(stimuli, seed)
    trial_order = [trial["trial_id"] for trial in ordered_trials]
    print(f"Seed {seed}: condition={condition}, order={trial_order}")
