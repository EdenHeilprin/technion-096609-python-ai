import csv
from pathlib import Path
import matplotlib.pyplot as plt

# Read the CSV file
with open(Path(__file__).with_name("evac_data.csv"), newline="", encoding="utf-8") as file:
	rows = list(csv.DictReader(file))

# read the evacuated and Anx_Dep_mean columns
evacuated = [row["evacuated"] for row in rows]
anx_dep_mean = [float(row["Anx_Dep_mean"]) for row in rows]


# create bar plot
plt.figure()

bars = plt.bar(evacuated, anx_dep_mean)

plt.xlabel("Evacuated")
plt.ylabel("Anxiety/Depression Mean")
plt.title("Anxiety/Depression Mean by Evacuated")
plt.tight_layout()
plt.show()



