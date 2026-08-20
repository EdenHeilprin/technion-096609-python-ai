"""Check that the package required for Class 9 is ready."""

from importlib.metadata import PackageNotFoundError, version
import sys


REQUIRED_VERSION = "3.0.5"

try:
    installed_version = version("pandas")
except PackageNotFoundError:
    print("pandas is not ready: it is not installed")
    print("Python used for this check:", sys.executable)
    print("Next step: run install_packages.py, then run this check again.")
    raise SystemExit(1)

if installed_version != REQUIRED_VERSION:
    print("pandas is not ready: version", installed_version, "is installed")
    print("Course version:", REQUIRED_VERSION)
    print("Python used for this check:", sys.executable)
    print("Next step: run install_packages.py, then run this check again.")
    raise SystemExit(1)

print("pandas is ready:", installed_version)
