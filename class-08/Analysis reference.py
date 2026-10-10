"""Instructor fallback: run the simple analysis without a live AI response."""

import csv  # Read a CSV row as a dictionary, using the column names as keys.
from pathlib import Path  # Locate the minimal project beside this reference script.
import matplotlib.pyplot as plt  # Draw and save the graph.

# For classroom data, change the filename, session code, and figure label.
DATA_FILE = "example_responses.csv"
SESSION = "FICTIONAL"
DATA_LABEL = "Fictional example data"

# Open the CSV and collect its rows in a list of dictionaries.
folder = Path(__file__).resolve().parent / "minimal-project"
with open(folder / DATA_FILE, encoding="utf-8-sig", newline="") as file:
    all_rows = list(csv.DictReader(file))

# Keep the chosen session, leaving other sessions and the original CSV untouched.
rows = []
for row in all_rows:
    if row["session"] == SESSION:
        rows.append(row)

offers = [2, 3, 4, 6, 7, 8]
participants = []

# Count each participant once, even though they answer several times.
for row in rows:
    if row["choice"] not in ["", "Sure", "Gamble"] or int(row["offer"]) not in offers:
        raise ValueError("Unexpected choice or offer: check the original export.")
    if row["choice"] != "" and row["participant"] not in participants:
        participants.append(row["participant"])

if len(participants) == 0:
    raise ValueError("No recorded choices for this session. Check SESSION and the export.")


def count_choices(offer):
    """Return the number of Gamble choices and total recorded choices for one offer."""
    gambles = 0
    total = 0
    for row in rows:
        # A missing response is not a Sure choice: leave it out of both counts.
        if int(row["offer"]) == offer and row["choice"] != "":
            total += 1
            if row["choice"] == "Gamble":
                gambles += 1
    return {"gambles": gambles, "total": total}


# Repeat the same calculation for each offer, using our function.
percentages = []
summary = f"{DATA_LABEL}\nSource: {DATA_FILE}\nSession: {SESSION}\n"
summary += f"Participants with at least one recorded choice: {len(participants)}\n\n"
for offer in offers:
    counts = count_choices(offer)
    gambles = counts["gambles"]
    total = counts["total"]
    if total == 0:
        percentages.append(None)  # A gap in the graph means no responses, not zero gambles.
        summary += f"{offer} sure points: no recorded choices\n"
    else:
        percentage = 100 * gambles / total
        percentages.append(percentage)
        summary += f"{offer} sure points: {gambles}/{total} chose Gamble ({percentage:.1f}%)\n"

# Save the same numbers we inspect in the terminal, without changing the CSV.
print(summary)
with open(folder / "results.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Draw the six percentages and label the full 0–100% scale.
plt.figure(figsize=(8, 5))
plt.plot(offers, percentages, marker="o")
plt.xticks(offers)
plt.ylim(-3, 103)
plt.yticks([0, 25, 50, 75, 100])
plt.xlabel("Guaranteed points")
plt.ylabel("Gamble choices (%)")
plt.title(f"Sure or gamble\n{DATA_LABEL}")
plt.tight_layout()
plt.savefig(folder / "results.png", dpi=160)
plt.close()
