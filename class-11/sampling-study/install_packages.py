"""Install the Classes 11–12 packages into VS Code's selected interpreter."""

from pathlib import Path
import subprocess
import sys


requirements_path = Path(__file__).parent / "requirements.txt"

print("Installing the Classes 11–12 packages...")
print("Python used for installation:", sys.executable)

try:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "-r",
            str(requirements_path),
        ],
        check=True,
    )
except subprocess.CalledProcessError:
    print("\nInstallation did not finish successfully.")
    print("Open package-troubleshooting.md for the next steps.")
    raise SystemExit(1)

print("\nInstallation finished.")
print("Run check_packages.py again.")
