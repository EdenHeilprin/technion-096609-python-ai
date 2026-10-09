"""Recreate the fictional teaching data; never reads or changes classroom data."""

import csv
from pathlib import Path


def main():
    # These invented choice patterns make a small, easy-to-check worked example.
    # Each number is the number of initial rounds in which a fictional person gambles.
    gamble_round_counts = [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 0]
    offers = [2, 3, 4, 6, 7, 8]
    columns = [
        "session_code", "participant_code", "study_version", "round_number",
        "sure_points", "gamble_high", "gamble_probability", "choice", "confidence",
    ]
    rows = []
    for person, gamble_count in enumerate(gamble_round_counts, start=1):
        for round_number, sure_points in enumerate(offers, start=1):
            rows.append([
                "SYNTHETIC", f"SYN{person:02d}", "full-v1", round_number,
                sure_points, 10, 0.5,
                "gamble" if round_number <= gamble_count else "sure",
                1 + (person + round_number) % 7,
            ])

    # A fictional unfinished participant demonstrates why rows are not people.
    for round_number, sure_points in enumerate(offers, start=1):
        answered = round_number <= 2
        rows.append([
            "SYNTHETIC", "SYN16", "full-v1", round_number,
            sure_points, 10, 0.5,
            "gamble" if answered else "", 4 if answered else "",
        ])

    destination = Path(__file__).resolve().parents[1] / "data" / "synthetic_choices.csv"
    with destination.open("w", encoding="utf-8", newline="") as file:
        # Fixed line endings keep the synthetic file's hash identical on Mac and Windows.
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(rows)
    print(f"Created {len(rows)} fictional rows in {destination.name}.")


if __name__ == "__main__":
    main()
