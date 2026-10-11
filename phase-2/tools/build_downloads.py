"""Package current Classes 8–10 and the unrevised Class 11/12 projects.

Run from any directory with Python 3.13. This only replaces named generated
folders inside this repository; personal student folders are never targets.
"""
import argparse
import hashlib
import json
import shutil
import tempfile
import zipfile
from pathlib import Path

PHASE = Path(__file__).resolve().parents[1]
REPO = PHASE.parent
CANONICAL = PHASE / "project"
EXCLUDE = {".venv", "__pycache__", ".git", ".pytest_cache", ".vscode", "outputs"}
SKIP_NAMES = {".DS_Store", ".env", "db.sqlite3"}


def copy_source(source, destination):
    for path in sorted(source.rglob("*")):
        parts = path.relative_to(source).parts
        if (not path.is_file() or EXCLUDE.intersection(parts)
                or path.name in SKIP_NAMES or path.suffix in {".pyc", ".sqlite3", ".db"}):
            continue
        # Never infer which new local CSVs are safe to publish.
        if path.suffix == ".csv" and path.name != "synthetic_choices.csv":
            raise ValueError(f"Unexpected source CSV requires review: {path}")
        target = destination / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)


def remove_generated(path):
    # Called only on builder-owned temporary or generated children, never a root.
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def project_snapshot(destination, stage):
    copy_source(CANONICAL, destination)
    if stage == "analysis-start":
        for name in ("analyze_choices.py", "explore_confidence.py"):
            remove_generated(destination / "analysis" / name)


def build_class8():
    # An explicit list keeps classroom exports and generated results out of the ZIP.
    target = REPO / "class-08"
    names = ["experiment-brief.docx", "preregistration.docx"]
    manifest = {name: hashlib.sha256((target / name).read_bytes()).hexdigest() for name in sorted(names)}
    (target / "DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    archive_path = target / "class-08-files.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        # Keep the maintainer manifest online, outside the two-file starter.
        for name in sorted(names):
            info = zipfile.ZipInfo("class-08/" + name, (2026, 10, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (target / name).read_bytes())
    return {"file": str(archive_path.relative_to(REPO)), "bytes": archive_path.stat().st_size,
            "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": len(manifest)}


def build_one(number):
    if number == 8:
        return build_class8()
    if number in {9, 10}:
        return build_hands_on(number)
    class_name = f"class-{number:02d}"
    target = REPO / class_name
    with tempfile.TemporaryDirectory(prefix=f"{class_name}-build-") as temp:
        lesson = Path(temp) / class_name
        lesson.mkdir()
        # These top-level lesson files are authored, not regenerated project copies.
        for path in sorted(target.glob("*.md")):
            if path.name not in {"SETUP.md", "TROUBLESHOOTING.md"}:
                shutil.copyfile(path, lesson / path.name)
        for name in ("SETUP.md", "TROUBLESHOOTING.md"):
            shutil.copyfile(PHASE / name, lesson / name)
        stage = {11: "analysis-start", 12: "complete"}[number]
        project_snapshot(lesson / "research-project", stage)
        if number == 11:
            project_snapshot(lesson / "checkpoints/analysis/research-project", "complete")
        files = sorted(p for p in lesson.rglob("*") if p.is_file())
        manifest = {str(p.relative_to(lesson)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
        (lesson / "DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        # Explicit owned children only. No personal folder is inferred from a glob.
        for name in ("research-project", "checkpoints", "reference-results", "worked-examples"):
            remove_generated(target / name)
            if (lesson / name).exists():
                shutil.copytree(lesson / name, target / name)
        for name in ("SETUP.md", "TROUBLESHOOTING.md", "DOWNLOAD_MANIFEST.json"):
            shutil.copyfile(lesson / name, target / name)
        archive_path = target / f"{class_name}-files.zip"
        # Fixed metadata makes a rebuild of the same source byte-for-byte identical.
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            for path in sorted(p for p in lesson.rglob("*") if p.is_file()):
                info = zipfile.ZipInfo(str(path.relative_to(Path(temp))).replace("\\", "/"), (2026, 10, 10, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                archive.writestr(info, path.read_bytes())
        return {"file": str(archive_path.relative_to(REPO)), "bytes": archive_path.stat().st_size,
                "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": len(manifest) + 1}


def build_hands_on(number):
    # These lessons are authored directly. Only explicitly reviewed files ship.
    names = {
        9: ["README.md", "macos.md", "windows.md", "TROUBLESHOOTING.md",
            ".gitignore", "requirements.txt", "check_setup.py", "settings.py",
            "choice_task/__init__.py", "choice_task/Consent.html",
            "choice_task/Details.html", "choice_task/Decision.html",
            "choice_task/ThankYou.html", "_static/choice_task/design.css"],
        10: ["README.md", ".gitignore", "summarize_choices.py", "sample_choices.csv"],
    }[number]
    target = REPO / f"class-{number:02d}"
    manifest = {name: hashlib.sha256((target / name).read_bytes()).hexdigest()
                for name in sorted(names)}
    (target / "DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    archive_path = target / f"{target.name}-files.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(names + ["DOWNLOAD_MANIFEST.json"]):
            info = zipfile.ZipInfo(target.name + "/" + name, (2026, 10, 11, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (target / name).read_bytes())
    return {"file": str(archive_path.relative_to(REPO)), "bytes": archive_path.stat().st_size,
            "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": len(names) + 1}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("classes", nargs="*", type=int, choices=range(8, 13))
    args = parser.parse_args()
    results = [build_one(number) for number in (args.classes or range(8, 13))]
    index_path = PHASE / "DOWNLOADS.json"
    previous = json.loads(index_path.read_text(encoding="utf-8")) if index_path.exists() else []
    entries = {item["file"]: item for item in previous + results}
    index_path.write_text(json.dumps([entries[name] for name in sorted(entries)], indent=2) + "\n", encoding="utf-8")
    for item in results:
        print(f"{item['file']}: {item['files']} files, {item['bytes']:,} bytes")
