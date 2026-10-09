"""Class 11 working file. Add the short analysis steps from the lesson below."""

from settings import DATA_FILE, DATA_LABEL
from study_data import read_export, select_complete_participants


# The provided checks protect the raw file and return only six-round completers.
raw = read_export(DATA_FILE)
clean, participation = select_complete_participants(raw)
print(DATA_LABEL)
print(participation.to_string(index=False))
print("\nIncluded trial rows:", len(clean))

# Step 1: inspect the six rows from SYN01 using .loc (synthetic example).

# Step 2: add a chose_gamble column: 1 for gamble, 0 for sure.

# Step 3: group by sure_points to calculate counts and the gamble rate.

# Step 4: save the table and create a labeled plot.
