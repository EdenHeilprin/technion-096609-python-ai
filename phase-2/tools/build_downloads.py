"""Build the Class 8/9 downloads from explicit, reviewed source lists.

Class 10 uses a Git clone; Classes 11–13 use the student-lessons folders.
Only the named ZIPs, manifests, and download index are generated here.
"""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

PHASE = Path(__file__).resolve().parents[1]
REPO = PHASE.parent
FILES = {
    8: ["experiment-brief.docx", "preregistration.docx"],
    9: ["README.md", "macos.md", "windows.md", "git-setup.md", "TROUBLESHOOTING.md",
        ".gitignore", "requirements.txt", "check_setup.py", "settings.py",
        "choice_task/__init__.py", "choice_task/Consent.html",
        "choice_task/Details.html", "choice_task/Decision.html",
        "choice_task/ThankYou.html", "_static/choice_task/design.css"],
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_one(number):
    target = REPO / f"class-{number:02d}"
    names = FILES[number]
    manifest = {name: digest(target / name) for name in sorted(names)}
    (target / "DOWNLOAD_MANIFEST.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    # Class 8 deliberately opens with only two context documents.
    packaged = names if number == 8 else names + ["DOWNLOAD_MANIFEST.json"]
    archive_path = target / f"{target.name}-files.zip"
    timestamp = (2026, 10, 10 if number == 8 else 11, 0, 0, 0)
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(packaged):
            info = zipfile.ZipInfo(target.name + "/" + name, timestamp)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (target / name).read_bytes())
    return describe(number)


def describe(number):
    path = REPO / f"class-{number:02d}/class-{number:02d}-files.zip"
    with zipfile.ZipFile(path) as archive:
        count = len(archive.namelist())
    return {"file": path.relative_to(REPO).as_posix(), "bytes": path.stat().st_size,
            "sha256": digest(path), "files": count}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("classes", nargs="*", type=int, choices=(8, 9))
    args = parser.parse_args()
    for number in args.classes or (8, 9):
        item = build_one(number)
        print(f"{item['file']}: {item['files']} files, {item['bytes']:,} bytes")
    # Rebuild the complete current index; never carry forward retired packages.
    entries = [describe(number) for number in (8, 9)]
    (PHASE / "DOWNLOADS.json").write_text(json.dumps(entries, indent=2) + "\n", encoding="utf-8")
