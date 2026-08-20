"""Check that the packages required for Class 10 are ready."""

from importlib.metadata import PackageNotFoundError, version
import sys


REQUIRED_PACKAGES = {
    "pandas": "3.0.5",
    "matplotlib": "3.11.1",
}

problems = []

for package_name, required_version in REQUIRED_PACKAGES.items():
    try:
        installed_version = version(package_name)
    except PackageNotFoundError:
        print(f"{package_name} is not ready: it is not installed")
        problems.append(package_name)
        continue

    if installed_version != required_version:
        print(
            f"{package_name} is not ready: version {installed_version} is installed "
            f"(course version: {required_version})"
        )
        problems.append(package_name)
        continue

    print(f"{package_name} is ready: {installed_version}")

if problems:
    print("\nPython used for this check:", sys.executable)
    print("Next step: run install_packages.py, then run this check again.")
    raise SystemExit(1)
