"""Package Class 8's minimal demonstration and Classes 9–12's guided projects.

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


def project_snapshot(destination, stage, brief=None):
    copy_source(CANONICAL, destination)
    if stage in {"scaffold", "minimal", "extension-start", "full-experiment"}:
        remove_generated(destination / "analysis")
        remove_generated(destination / "data")
        (destination / "data").mkdir()
        (destination / "data/README.md").write_text(
            "# Your exports\n\nSave the lesson's custom CSV export here. Keep the original unchanged. "
            "Actual participant responses stay local, not in the public course repository.\n", encoding="utf-8")
    if stage in {"scaffold", "minimal", "extension-start"}:
        remove_generated(destination / "experiment")
        copy_source(PHASE / "minimal-experiment", destination / "experiment")
    if stage == "scaffold":
        remove_generated(destination / "experiment/choice_task")
        remove_generated(destination / "experiment/_static")
    if stage == "analysis-start":
        for name in ("analyze_choices.py", "explore_confidence.py"):
            remove_generated(destination / "analysis" / name)
    if brief:
        shutil.copyfile(brief, destination / "docs" / brief.name)
    if stage in {"scaffold", "minimal"}:
        shutil.copyfile(REPO / "class-09/BUILD_BRIEF.md", destination / "docs/STUDY_SPEC.md")
        (destination / "docs/DECISIONS.md").write_text(
            "# Decisions\n\nCurrent milestone: minimal-v1, one choice and no confidence field on the page.\n"
            "Follow BUILD_BRIEF.md. Record the changes you actually make below.\n", encoding="utf-8")
    if stage in {"scaffold", "minimal", "extension-start", "full-experiment"}:
        state = {
            "scaffold": "Class 9 scaffold: settings exist; choice_task has not been built yet. Follow docs/BUILD_BRIEF.md to build minimal-v1.",
            "minimal": "Class 9 working checkpoint: minimal-v1 is implemented. Follow docs/BUILD_BRIEF.md to inspect and test it.",
            "extension-start": "Class 10 starting point: minimal-v1 is implemented. Follow docs/EXTENSION_BRIEF.md to build full-v1 before starting the server. STUDY_SPEC.md describes that target, not the current one-round implementation.",
            "full-experiment": "Class 10 working checkpoint: full-v1 is implemented. Follow docs/EXTENSION_BRIEF.md to inspect and test it.",
        }[stage]
        (destination / "PROJECT.md").write_text(
            "# Sure or gamble\n\n" + state + "\n\n"
            "Open this research-project folder in VS Code and Codex. Follow the class SETUP.md for this project's environment. "
            "Run run_experiment.py once the named milestone exists. The experiment is inside experiment/. "
            "Keep exports under data/ (create that folder when needed). This stage does not include the later analysis scripts.\n\n"
            "Do not overwrite your earlier work, change saved data, or publish actual participant exports. "
            "Use readable English comments in generated code.\n", encoding="utf-8")
    if stage == "scaffold":
        (destination / "experiment/README.md").write_text(
            "# Experiment scaffold\n\nsettings.py already names the sure_or_gamble session and choice_task app. "
            "Build the missing app using ../docs/BUILD_BRIEF.md before running the server. "
            "Do not run otree startproject in this existing folder.\n", encoding="utf-8")


def build_class8():
    # An explicit list keeps classroom exports and generated results out of the ZIP.
    target = REPO / "class-08"
    names = [
        "README.md", "Teaching Notes.md", "Analysis reference.py",
        "minimal-project/.gitignore", "minimal-project/_static/.gitkeep",
        "minimal-project/preregistration.txt", "minimal-project/example_responses.csv",
        "minimal-project/settings.py", "minimal-project/requirements.txt",
        "minimal-project/choice_task/__init__.py", "minimal-project/choice_task/Choice.html",
        "minimal-project/choice_task/ThankYou.html",
    ]
    manifest = {name: hashlib.sha256((target / name).read_bytes()).hexdigest() for name in sorted(names)}
    (target / "DOWNLOAD_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    archive_path = target / "class-08-files.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(names + ["DOWNLOAD_MANIFEST.json"]):
            info = zipfile.ZipInfo("class-08/" + name, (2026, 10, 10, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, (target / name).read_bytes())
    return {"file": str(archive_path.relative_to(REPO)), "bytes": archive_path.stat().st_size,
            "sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": len(manifest) + 1}


def build_one(number):
    if number == 8:
        return build_class8()
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
        brief = target / ("BUILD_BRIEF.md" if number == 9 else "EXTENSION_BRIEF.md") if number in {9, 10} else None
        stage = {9: "scaffold", 10: "extension-start", 11: "analysis-start", 12: "complete"}[number]
        project_snapshot(lesson / "research-project", stage, brief)
        if number in {9, 10, 11}:
            checkpoint, checkpoint_stage = {9: ("minimal", "minimal"), 10: ("full", "full-experiment"), 11: ("analysis", "complete")}[number]
            project_snapshot(lesson / "checkpoints" / checkpoint / "research-project", checkpoint_stage, brief)
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
