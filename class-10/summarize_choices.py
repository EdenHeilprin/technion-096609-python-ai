# Run this whole file with VS Code's Run Python File in Terminal button.
# Input: sample_choices.csv beside this script; output: summary.csv beside it.

# These modules come with Python; no package installation is needed.
import csv
from pathlib import Path


def percentage(count, total):
    """Return a count as a percentage, rounded to one decimal place."""
    # An empty dataset has no meaningful percentage.
    if total == 0:
        raise ValueError("Cannot calculate a percentage with no decisions.")
    return round(100 * count / total, 1)


# Build paths relative to this script, not the terminal's current folder.
folder = Path(__file__).resolve().parent
input_file = folder / "sample_choices.csv"
output_file = folder / "summary.csv"

# Read each CSV row as a dictionary, then collect the rows into a list.
# newline and encoding make file reading consistent on Windows and Mac.
with open(input_file, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    choices = list(reader)

# Count decisions, not participants: each participant contributes seven rows.
total_decisions = len(choices)
gamble_count = 0

for decision in choices:
    # Stop on an unexpected label rather than silently counting it as 'sure'.
    if decision["choice"] not in ["sure", "gamble"]:
        raise ValueError("Each choice must be 'sure' or 'gamble'. Check the CSV.")
    if decision["choice"] == "gamble":
        gamble_count = gamble_count + 1

gamble_percentage = percentage(gamble_count, total_decisions)
print("Decisions:", total_decisions)
print("Gamble choices:", gamble_count)
print("Gamble choices (%):", gamble_percentage)

# Exercise: calculate and print the sure count and percentage here.

# Write a new summary without changing the original choices.
# 'w' replaces only this output file if it already exists.
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["choice", "count", "percentage"])
    writer.writerow(["gamble", gamble_count, gamble_percentage])
    # Exercise: add a second row for sure choices here.

print("Saved:", output_file)
