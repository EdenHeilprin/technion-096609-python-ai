"""Fresh-download installation followed by portable release checks."""
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix="student-download-") as temp:
    for number in (9, 10):
        with zipfile.ZipFile(REPO / f"class-{number:02d}/class-{number:02d}-files.zip") as archive:
            archive.extractall(temp)
    setup_project = Path(temp) / "class-09"
    subprocess.run([sys.executable, "-m", "venv", str(setup_project / ".venv")], check=True)
    setup_python = setup_project / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    subprocess.run([str(setup_python), "-m", "pip", "install", "-r", "requirements.txt"], cwd=setup_project, check=True)
    subprocess.run([str(setup_python), "check_setup.py"], cwd=setup_project, check=True)
    subprocess.run([str(setup_python), str(REPO / "phase-2/tools/verify_hands_on.py"),
                    "--class9", str(setup_project), "--class10", str(Path(temp) / "class-10")], check=True)
    # Class 8 is watch-only; Class 12 retains the full student environment.
    with zipfile.ZipFile(REPO / "class-12/class-12-files.zip") as archive:
        archive.extractall(temp)
    project = Path(temp) / "class-12/research-project"
    subprocess.run([sys.executable, str(project / "setup_environment.py")], cwd=project, check=True)
    executable = project / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    subprocess.run([str(executable), str(project / "check_environment.py")], cwd=project, check=True)
    subprocess.run([str(executable), str(REPO / "phase-2/tools/verify_release.py"), "--runtime"], check=True)
