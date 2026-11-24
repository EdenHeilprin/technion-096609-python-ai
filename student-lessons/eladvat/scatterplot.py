import csv
import matplotlib.pyplot as plt

# Read the CSV file
with open("student-lessons\\eladvat\\evac_data.csv", newline="", encoding="utf-8") as file:
    data = list(csv.DictReader(file))


# read the depression and anxiety columns
depression = [float(row["depression"]) for row in data]
anxiety = [float(row["anxiety"]) for row in data]

# Scatter plot of anxiety by depression
plt.figure()
plt.scatter(depression, anxiety)
plt.title("Anxiety by Depression")
plt.xlabel("depression")
plt.ylabel("anxiety")

plt.show()
