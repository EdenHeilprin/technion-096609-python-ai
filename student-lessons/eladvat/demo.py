import csv
import matplotlib.pyplot as plt

# Read the CSV file
with open("student-lessons\\eladvat\\evac_data.csv", newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))

# read the needs_mean column
needs_mean = [float(row["needs_mean"]) for row in data]
# Histogram of participants' needs_mean scores
plt.figure()
plt.hist(needs_mean, bins=10, edgecolor="black")
plt.title("Distribution of Needs Scores")
plt.xlabel("needs_mean")
plt.ylabel("Number of participants")

plt.show()
