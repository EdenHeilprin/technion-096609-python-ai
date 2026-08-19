from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class_folder = Path(__file__).parent
data_path = class_folder / "data" / "decision_trials.csv"
output_folder = class_folder / "output"
cleaned_path = output_folder / "cleaned_trials.csv"
summary_path = output_folder / "condition_summary.csv"
plot_path = output_folder / "mean_points_by_condition.png"

trials = pd.read_csv(data_path)
assert trials.shape == (12, 6)

completed_trials = trials.loc[trials["response_time_ms"].notna()].copy()
assert completed_trials.shape == (10, 6)

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

assert summary.shape == (2, 5)
assert set(summary["condition"]) == {"bonus", "control"}
assert summary["completed_trials"].sum() == 10

output_folder.mkdir(exist_ok=True)
analysis.to_csv(cleaned_path, index=False)
summary.to_csv(summary_path, index=False)

axis = summary.plot.bar(
    x="condition",
    y="mean_points",
    legend=False,
    color=["#4C78A8", "#F58518"],
)
axis.set_title("Mean points by condition")
axis.set_xlabel("Condition")
axis.set_ylabel("Mean points per completed trial")
axis.tick_params(axis="x", rotation=0)

figure = axis.get_figure()
figure.tight_layout()
figure.savefig(plot_path, dpi=150)

saved_analysis = pd.read_csv(cleaned_path)
saved_summary = pd.read_csv(summary_path)

assert saved_analysis.shape == analysis.shape
assert list(saved_analysis.columns) == list(analysis.columns)
assert saved_summary.shape == summary.shape
assert list(saved_summary.columns) == list(summary.columns)
assert plot_path.exists()
assert plot_path.stat().st_size > 0

print("Analysis rows:", saved_analysis.shape[0])
print("Summary rows:", saved_summary.shape[0])
print("Saved:", cleaned_path.name)
print("Saved:", summary_path.name)
print("Saved:", plot_path.name)
print("All pipeline checks passed")

plt.show()
