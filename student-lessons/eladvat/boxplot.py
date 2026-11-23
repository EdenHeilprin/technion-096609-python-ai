import csv
import matplotlib.pyplot as plt

# Read the CSV file
with open("evac_data.csv", newline="", encoding="utf-8-sig") as file:
    data = list(csv.DictReader(file))

# read the needs_mean column
needs = [[float(row["autonomy"]) for row in data],
        [float(row["competence"]) for row in data]]

# Boxplot of participants' needs scores
plt.figure()
plt.boxplot(needs, tick_labels=["Autonomy", "Competence"])
plt.title("Distribution of Needs Scores")
plt.xlabel("needs")
plt.ylabel("Number of participants")

plt.show()
