"""Start the local oTree experiment with this project's installed environment."""

from pathlib import Path
import os
import subprocess
import sys


PROJECT = Path(__file__).resolve().parent
BIN = PROJECT / ".venv" / ("Scripts" if sys.platform == "win32" else "bin")
OTREE = BIN / ("otree.exe" if sys.platform == "win32" else "otree")


def main():
    """Keep server startup independent of the terminal's current directory."""
    # Never let a local teaching run inherit a remote database or hosted mode.
    if any(os.environ.get(name) for name in ("DATABASE_URL", "DYNO", "OTREE_PRODUCTION")):
        print("Local startup stopped: this environment contains database/hosting settings.")
        print("Use a local terminal without those settings; do not point this helper at a live study.")
        return 1
    if not OTREE.is_file():
        print("Run setup_environment.py first; see SETUP.md in the class folder.")
        return 1
    if not (PROJECT / "experiment" / "choice_task" / "__init__.py").is_file():
        print("The experiment app has not been built yet. Follow the Class 9 build task.")
        return 1

    # The server's child commands must find this project's tools first.
    environment = os.environ.copy()
    environment["PATH"] = str(BIN) + os.pathsep + environment.get("PATH", "")
    print("Open http://localhost:8000 in your browser.", flush=True)
    print("Keep this terminal running. Stop the server with Ctrl+C.", flush=True)
    try:
        return subprocess.call([str(OTREE), "devserver"], cwd=PROJECT / "experiment", env=environment)
    except KeyboardInterrupt:
        print("\nServer stopped.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
