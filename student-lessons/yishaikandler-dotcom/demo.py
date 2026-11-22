import csv
from pathlib import Path

# Read one fictional response from the file beside this script.
survey = Path(__file__).with_name("survey_responses.csv")
with survey.open(encoding="utf-8", newline="") as file:
    first_row = next(csv.DictReader(file))
    response = first_row["favorite_tool"]

# Quotes make the spaces at each end visible.
print("Original:", repr(response))
trimmed = response.strip()
print("After strip:", repr(trimmed))
lowercase = trimmed.lower()
print("After lower:", repr(lowercase))
clean = lowercase.replace("!", "")
print("After replace:", repr(clean))
print("Original again:", repr(response))
