from pathlib import Path


class_folder = Path(__file__).parent
data_path = class_folder / "data" / "trial_results.csv"

print("Class folder:", class_folder.name)
print("Data file:", data_path.name)
print("File exists:", data_path.exists())
