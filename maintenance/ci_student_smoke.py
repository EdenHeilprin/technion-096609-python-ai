"""Fresh-download installation followed by portable release checks."""
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory(prefix="student download ") as temp:
    for number in (9,):
        with zipfile.ZipFile(REPO / f"class-{number:02d}/class-{number:02d}-files.zip") as archive:
            archive.extractall(temp)
    setup_project = Path(temp) / "class-09"
    subprocess.run([sys.executable, "-m", "venv", str(setup_project / ".venv")], check=True)
    setup_python = setup_project / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    subprocess.run([str(setup_python), "-m", "pip", "install", "-r", "requirements.txt"], cwd=setup_project, check=True)
    subprocess.run([str(setup_python), "check_setup.py"], cwd=setup_project, check=True)
    # Exercise the activation commands students actually use, not only absolute
    # executable paths. oTree's devserver child also needs this environment.
    if os.name == "nt":
        activation = ["cmd.exe", "/d", "/c",
                      r'call .venv\Scripts\activate.bat && python check_setup.py && otree --version']
    else:
        activation = ["/bin/bash", "-c",
                      "source .venv/bin/activate && python check_setup.py && otree --version"]
    subprocess.run(activation, cwd=setup_project, check=True)
    subprocess.run([str(setup_python), str(REPO / "maintenance/verify_hands_on.py"),
                    "--class9", str(setup_project)], check=True)
    subprocess.run([sys.executable, str(REPO / "maintenance/verify_contribution.py")], check=True)
    subprocess.run([sys.executable, str(REPO / "maintenance/verify_release.py")], check=True)
