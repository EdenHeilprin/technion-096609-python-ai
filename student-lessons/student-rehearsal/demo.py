# Path helps find the CSV beside this script, regardless of the terminal folder.
from pathlib import Path

# Import pandas and give it the conventional short name pd.
import pandas as pd

# __file__ is this script; parent is its folder; / adds the CSV file name.
data_file = Path(__file__).parent / "responses.csv"

# Read the fictional responses into a table, with one row per participant.
responses = pd.read_csv(data_file)

# Display the rows so we can see exactly which values enter the calculation.
print("Responses included:")
print(responses)

# Split by instruction type, select response times, and average each group.
group_means = responses.groupby("instructions")["response_ms"].mean()

# Print a clear label and the calculated means, measured in milliseconds.
print("\nMean response time (ms):")
print(group_means)
