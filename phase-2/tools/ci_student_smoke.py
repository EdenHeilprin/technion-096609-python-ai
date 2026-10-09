"""Fresh-download installation followed by portable release checks."""
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix="student-download-") as temp:
    with zipfile.ZipFile(REPO / "class-08/class-08-files.zip") as archive:
        archive.extractall(temp)
    project = Path(temp) / "class-08/research-project"
    subprocess.run([sys.executable, str(project / "setup_environment.py")], cwd=project, check=True)
    executable = project / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    subprocess.run([str(executable), str(project / "check_environment.py")], cwd=project, check=True)
    subprocess.run([str(executable), str(REPO / "phase-2/tools/verify_release.py"), "--runtime"], check=True)
