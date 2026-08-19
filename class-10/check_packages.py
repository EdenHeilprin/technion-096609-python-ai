required_pandas_version = "3.0.5"
required_matplotlib_version = "3.11.1"

try:
    import pandas as pd
except ModuleNotFoundError:
    print("pandas is not installed. Return to the Class 9 installation guidance.")
else:
    if pd.__version__ == required_pandas_version:
        print("pandas is ready:", pd.__version__)
    else:
        print("Installed pandas version:", pd.__version__)
        print("Course pandas version:", required_pandas_version)
        print("Return to the Class 9 installation guidance.")

try:
    import matplotlib
except ModuleNotFoundError:
    print("matplotlib is not installed. Use the Class 10 installation command.")
else:
    if matplotlib.__version__ == required_matplotlib_version:
        print("matplotlib is ready:", matplotlib.__version__)
    else:
        print("Installed matplotlib version:", matplotlib.__version__)
        print("Course matplotlib version:", required_matplotlib_version)
        print("Run the installation command in the Class 10 instructions.")
