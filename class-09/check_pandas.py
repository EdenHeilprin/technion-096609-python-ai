import pandas as pd


required_version = "3.0.5"

if pd.__version__ == required_version:
    print("pandas is ready:", pd.__version__)
else:
    print("Installed pandas version:", pd.__version__)
    print("Course pandas version:", required_version)
    print("Run the installation command in the Class 9 instructions.")
