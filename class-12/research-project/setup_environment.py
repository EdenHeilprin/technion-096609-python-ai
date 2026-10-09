"""Create this course project's isolated Python environment and install packages."""

from pathlib import Path
import subprocess
import sys
import venv


# Locate the project using this file, not the terminal's current folder.
PROJECT = Path(__file__).resolve().parent
ENVIRONMENT = PROJECT / ".venv"
# Windows and macOS store the environment's Python in different subfolders.
PYTHON = ENVIRONMENT / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def main():
    """Use Python 3.13 and install only inside this project's .venv folder."""
    if sys.version_info[:2] != (3, 13):
        print("Select Python 3.13 in VS Code, then run this file again.")
        print("This run used:", sys.executable)
        return 1

    if not PYTHON.exists():
        # venv creates a separate package environment without changing global Python.
        print("Creating project environment...", flush=True)
        venv.create(ENVIRONMENT, with_pip=True)

    # Refuse to silently reuse an environment created with another Python series.
    version = subprocess.check_output(
        [str(PYTHON), "-c", "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"],
        text=True,
    ).strip()
    if version != "3.13":
        print("This .venv uses Python", version)
        print("Set up a fresh copy of the project with Python 3.13; keep this folder's work.")
        return 1

    print("Installing the pinned course packages...", flush=True)
    # -m pip ties installation to the exact environment that will run the project.
    subprocess.run(
        [str(PYTHON), "-m", "pip", "install", "--disable-pip-version-check", "-r", str(PROJECT / "requirements.txt")],
        check=True,
    )
    print("\nENVIRONMENT READY")
    print("Select this interpreter in VS Code:", PYTHON)
    print("Then run check_environment.py.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, subprocess.CalledProcessError) as error:
        print("\nSetup stopped:", error)
        print("Check the error above and TROUBLESHOOTING.md; your source files were not changed.")
        raise SystemExit(1)
