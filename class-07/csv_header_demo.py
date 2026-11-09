# csv provides tools for reading CSV files.
import csv
# Path lets us locate a file beside this script, wherever the folder is saved.
from pathlib import Path


def calculate_bonus(trial_points):
    """Return the bonus in pence for a list of trial points, at 10 pence per point."""
    # Start a fresh total for this participant.
    total_points = 0

    # Add each trial's points to the total.
    for points in trial_points:
        total_points = total_points + points

    # Convert the total to pence at 10 pence per point.
    bonus_pence = total_points * 10
    # Send the calculated bonus back to the code that called the function.
    return bonus_pence


# __file__ identifies this script; with_name selects the CSV in the same folder.
input_path = Path(__file__).with_name("trial_results.csv")

# Open the CSV for reading; with closes it automatically when this block ends.
# newline="" lets csv handle line endings; encoding="utf-8" reads the text format.
with input_path.open("r", newline="", encoding="utf-8") as input_file:
    # Use the header names as dictionary keys; each row's values are text.
    reader = csv.DictReader(input_file)
    # Read one participant's row at a time.
    for row in reader:
        # Look up the three scores by column name and convert them to numbers.
        trial_points = [int(row["trial_1"]), int(row["trial_2"]), int(row["trial_3"])]
        # Reuse the bonus function, then add the participation fee in pence.
        bonus = calculate_bonus(trial_points)
        total_payment = 100 + bonus
        # Display this participant's ID and payment amounts.
        print(row["participant_id"], "Bonus (pence):", bonus,
              "Total payment (pence):", total_payment)
