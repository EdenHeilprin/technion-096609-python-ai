"""Check that the packages required for Classes 11–12 are ready."""

from importlib.metadata import PackageNotFoundError, version
import sys


REQUIRED_PACKAGES = {
    "otree": "6.0.15",
    "requests": "2.34.2",
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
