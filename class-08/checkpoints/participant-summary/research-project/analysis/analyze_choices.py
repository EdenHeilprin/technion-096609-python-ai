"""Completed Class 11 analysis: rebuild tables and a figure from the original CSV."""

import hashlib
import json
from pathlib import Path

import matplotlib

# Save a figure without depending on an interactive window or browser.
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from settings import DATA_FILE, DATA_LABEL, IS_SYNTHETIC, OUTPUT_DIR
from study_data import read_export, select_complete_participants


def run_analysis(data_file=DATA_FILE, output_dir=OUTPUT_DIR,
                 data_label=DATA_LABEL, is_synthetic=IS_SYNTHETIC):
    """Validate one source, summarize completers, and save traceable results."""
    data_file = Path(data_file)
    output_dir = Path(output_dir)
    raw = read_export(data_file)
    clean, participation = select_complete_participants(raw)

    # Every included person contributes exactly six choices.
    clean["chose_gamble"] = clean["choice"].eq("gamble").astype(int)
    included_people = int(participation["included"].sum())
    if included_people == 0:
        print(participation.to_string(index=False))
        raise ValueError("No participant completed all six rounds. No analysis outputs were regenerated.")

    # Group rows that share an offer; sum counts gambles and size counts choices.
    by_offer = clean.groupby("sure_points", as_index=False).agg(
        gamble_count=("chose_gamble", "sum"),
        choice_count=("chose_gamble", "size"),
    )
    by_offer["gamble_rate"] = by_offer["gamble_count"] / by_offer["choice_count"]

    # A second table has one row per person, rather than one row per choice.
    by_person = clean.groupby(["session_code", "participant_code"], as_index=False).agg(
        completed_rounds=("round_number", "size"),
        gamble_count=("chose_gamble", "sum"),
        gamble_rate=("chose_gamble", "mean"),
        mean_confidence=("confidence", "mean"),
    )

    # All derived files go to outputs. The input CSV is never overwritten.
    output_dir.mkdir(parents=True, exist_ok=True)
    clean.to_csv(output_dir / "clean_trials.csv", index=False)
    participation.to_csv(output_dir / "exclusions.csv", index=False)
    by_offer.to_csv(output_dir / "choice_by_offer.csv", index=False)
    by_person.to_csv(output_dir / "participant_summary.csv", index=False)

    # Plot percentages, keep the full 0–100% range, and identify the actual source.
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.plot(by_offer["sure_points"], by_offer["gamble_rate"] * 100,
              marker="o", color="#176B87", linewidth=2.2, markersize=7)
    axis.set(xlabel="Guaranteed alternative (points)", ylabel="Gamble choices (%)",
             xticks=by_offer["sure_points"], ylim=(-3, 103), yticks=[0, 25, 50, 75, 100])
    axis.set_title("Gamble choice by guaranteed offer", loc="left", fontsize=16, pad=32)
    axis.text(0, 1.035, f"{data_label} · {included_people} complete participants",
              transform=axis.transAxes, fontsize=10, color="#4B5563")
    axis.grid(axis="y", color="#DEE3E7", linewidth=0.7)
    axis.spines[["top", "right"]].set_visible(False)
    figure.text(0.13, 0.025, "Offers appeared in this ascending order; offer and order cannot be separated.",
                fontsize=9, color="#4B5563")
    figure.tight_layout(rect=(0, 0.055, 1, 1))
    figure.savefig(output_dir / "choice_by_offer.png", dpi=180)
    plt.close(figure)

    # Hashing identifies the exact input even if two files share the same filename.
    summary = {
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
        "gamble_count": int(clean["chose_gamble"].sum()),
        "gamble_rate": float(clean["chose_gamble"].mean()),
        "mean_participant_gamble_rate": float(by_person["gamble_rate"].mean()),
        "by_offer": by_offer.to_dict(orient="records"),
        "exclusions": participation.loc[~participation["included"]].to_dict(orient="records"),
        "inclusion_rule": "Six unique, valid, answered full-v1 rounds per participant within a session.",
        "design_note": "Fixed ascending offers: 2, 3, 4, 6, 7, 8. Offer and order are confounded.",
    }
    (output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(data_label)
    print(f"Included {included_people} of {len(participation)} participants: {len(clean)} choices.")
    print(f"Gamble choices: {summary['gamble_count']}/{len(clean)} = {summary['gamble_rate']:.1%}")
    print(by_offer.to_string(index=False))
    print(f"Saved results to: {output_dir}")
    return summary


if __name__ == "__main__":
    try:
        run_analysis()
    except (ValueError, OSError) as error:
        raise SystemExit(f"Analysis stopped: {error}")
