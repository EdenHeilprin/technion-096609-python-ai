"""Class 12 worked extension: descriptive confidence by guaranteed offer."""

import hashlib
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from settings import DATA_FILE, DATA_LABEL, IS_SYNTHETIC, OUTPUT_DIR
from study_data import read_export, select_complete_participants


def run_confidence(data_file=DATA_FILE, output_dir=OUTPUT_DIR,
                   data_label=DATA_LABEL, is_synthetic=IS_SYNTHETIC):
    """Revalidate the raw export and summarize confidence without using another analysis."""
    data_file = Path(data_file)
    output_dir = Path(output_dir)
    # Use the provided checks directly, independent of how your Class 11 script was written.
    raw = read_export(data_file)
    clean, participation = select_complete_participants(raw)
    included_people = int(participation["included"].sum())
    if included_people == 0:
        print(participation.to_string(index=False))
        raise ValueError("No participant completed all six rounds. No confidence outputs were regenerated.")

    # At each offer, every included participant supplies exactly one confidence rating.
    confidence = clean.groupby("sure_points", as_index=False).agg(
        mean_confidence=("confidence", "mean"),
        participant_count=("confidence", "size"),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    confidence.to_csv(output_dir / "confidence_by_offer.csv", index=False)

    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(confidence["sure_points"], confidence["mean_confidence"],
              marker="o", color="#7B4B94", linewidth=2.2, markersize=7)
    axis.set(xlabel="Guaranteed alternative (points)", ylabel="Mean confidence (1–7)",
             xticks=confidence["sure_points"], ylim=(1, 7), yticks=list(range(1, 8)))
    axis.set_title("Reported confidence by guaranteed offer", loc="left", fontsize=16, pad=32)
    axis.text(0, 1.035, f"{data_label} · {included_people} complete participants",
              transform=axis.transAxes, fontsize=10, color="#4B5563")
    axis.grid(axis="y", color="#DEE3E7", linewidth=0.7)
    axis.spines[["top", "right"]].set_visible(False)
    figure.text(0.13, 0.025, "Descriptive extension. Offers also differ in presentation order.",
                fontsize=9, color="#4B5563")
    figure.tight_layout(rect=(0, 0.055, 1, 1))
    figure.savefig(output_dir / "confidence_by_offer.png", dpi=180)
    plt.close(figure)

    # Retain unrounded values and the exact source identity for the writing step.
    record = {
        "question": "How does mean reported confidence vary across guaranteed offers?",
        "study_version": "full-v1",
        "data_label": data_label,
        "is_synthetic": bool(is_synthetic),
        "source_file": data_file.name,
        "source_sha256": hashlib.sha256(data_file.read_bytes()).hexdigest(),
        "input_rows": len(raw),
        "input_participants": len(participation),
        "included_participants": included_people,
        "excluded_participants": int((~participation["included"]).sum()),
        "included_trials": len(clean),
        "exclusions": participation.loc[~participation["included"]].to_dict(orient="records"),
        "inclusion_rule": "Six unique, valid, answered full-v1 rounds per participant within a session.",
        "by_offer": confidence.to_dict(orient="records"),
        "interpretation_limit": "Descriptive only; repeated ratings, fixed offer order, and no random assignment to offers.",
    }
    (output_dir / "confidence_summary.json").write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"{data_label}\nConfidence extension: {included_people} complete participants.")
    print(confidence.to_string(index=False))
    print(f"Saved results to: {output_dir}")
    return record


if __name__ == "__main__":
    try:
        run_confidence()
    except (ValueError, OSError) as error:
        raise SystemExit(f"Extension stopped: {error}")
