# Run using this project's .venv Python, as shown in the setup guide.
import sys
from importlib.metadata import PackageNotFoundError, version

# Show the actual executable so a different Python installation is easy to spot.
print("Python:", sys.version.split()[0])
print("Interpreter:", sys.executable)

if sys.version_info[:2] != (3, 13):
    sys.exit("Use Python 3.13 to create this project's .venv. See the setup guide.")

if sys.prefix == sys.base_prefix:
    sys.exit("Run this check using the .venv command in the setup guide.")

# A missing package is a setup issue, not an error in the experiment.
try:
    otree_version = version("otree")
except PackageNotFoundError:
    sys.exit("oTree is missing. Run the requirements.txt installation step.")

print("oTree:", otree_version)
if otree_version != "6.0.15":
    sys.exit("Install the oTree version in requirements.txt using this .venv.")

print("CLASS 9 SETUP PASSED")
