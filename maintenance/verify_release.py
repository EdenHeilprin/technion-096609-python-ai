"""Check current downloads and course links without touching student work.

The small HTTP helpers are shared with the disposable Class 9 runtime check.
"""
import ast
import hashlib
import json
import os
import re
import signal
import subprocess
import tempfile
import urllib.parse
import urllib.request
import zipfile
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CHECKS = 0


def check(condition, message):
    global CHECKS
    if not condition:
        raise RuntimeError(message)
    CHECKS += 1


def digest(content):
    return hashlib.sha256(content).hexdigest()


def verify_archive(number, folder):
    name = f"class-{number:02d}"
    source = REPO / name
    with zipfile.ZipFile(source / f"{name}-files.zip") as archive:
        paths = archive.namelist()
        check(len(paths) == len(set(paths)), f"{name}: duplicate archive entries")
        check(archive.testzip() is None, f"{name}: damaged ZIP")
        for entry in paths:
            path = Path(entry)
            check(path.parts[0] == name and ".." not in path.parts and not path.is_absolute(), f"Unsafe archive entry {entry}")
            check(not {".venv", "__pycache__", ".git", "outputs", "exports"}.intersection(path.parts), f"Private/runtime content: {entry}")
            check(path.name not in {".env", ".DS_Store", "db.sqlite3"} and path.suffix not in {".pyc", ".db", ".sqlite3"}, f"Unexpected artifact: {entry}")
        archive.extractall(folder)
    lesson = folder / name
    manifest_root = source if number == 8 else lesson
    manifest = json.loads((manifest_root / "DOWNLOAD_MANIFEST.json").read_text(encoding="utf-8"))
    actual = {p.relative_to(lesson).as_posix() for p in lesson.rglob("*") if p.is_file()}
    expected = set(manifest) if number == 8 else set(manifest) | {"DOWNLOAD_MANIFEST.json"}
    check(actual == expected, f"{name}: manifest file set differs")
    for relative, expected_hash in manifest.items():
        path = lesson / relative
        check(digest(path.read_bytes()) == expected_hash, f"{name}: hash {relative}")
        check((source / relative).read_bytes() == path.read_bytes(), f"{name}: source and ZIP differ: {relative}")
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        if path.suffix in {".md", ".py", ".html", ".js", ".css", ".json", ".csv", ".txt"}:
            text = path.read_text(encoding="utf-8")
            check(not re.search(r"/Users/|/private/tmp/|C:\\Users\\|sk-proj-", text), f"{relative}: machine path or secret")
    if number == 8:
        check(actual == {"experiment-brief.docx", "preregistration.docx"}, "Class 8 must contain exactly two context documents")
        for filename in sorted(actual):
            with zipfile.ZipFile(lesson / filename) as document:
                check(document.testzip() is None and "word/document.xml" in document.namelist(), f"Invalid Word file {filename}")
    if number == 9:
        check((lesson / "choice_task/__init__.py").is_file(), "Class 9 working experiment missing")
        check((lesson / "requirements.txt").read_text().strip() == "otree==6.0.15", "Class 9 oTree pin differs")
    print(f"PASS: {name} archive and source agreement", flush=True)


def verify_links():
    # Check local targets, including public URLs pointing back into this course.
    prefixes = (
        "https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/",
        "https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/",
        "https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/",
        "https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/",
    )
    roots = sorted(REPO.glob("*.md")) + [REPO / "00-syllabus", REPO / "maintenance", REPO / "student-lessons"]
    roots += sorted(REPO.glob("class-*"))
    pages = []
    for root in roots:
        pages.extend([root] if root.is_file() else root.rglob("*.md"))
    for page in pages:
        if {".venv", ".git", "__pycache__"}.intersection(page.relative_to(REPO).parts):
            continue
        for link in re.findall(r"\]\(([^\s)]+)\)", page.read_text(encoding="utf-8")):
            raw = urllib.parse.unquote(link.split("#")[0])
            prefix = next((item for item in prefixes if raw.startswith(item)), None)
            if prefix:
                target = REPO / raw.removeprefix(prefix)
            elif re.match(r"(?:https?:|mailto:|#)", link):
                continue
            else:
                target = page.parent / raw
            check(target.exists(), f"Broken course link: {page.relative_to(REPO)} -> {link}")
    print("PASS: course navigation and local download links", flush=True)


def verify_index():
    entries = json.loads((REPO / "maintenance/DOWNLOADS.json").read_text(encoding="utf-8"))
    expected = {f"class-{number:02d}/class-{number:02d}-files.zip" for number in (8, 9)}
    check(len(entries) == 2 and {item["file"] for item in entries} == expected, "Download index contains missing or retired packages")
    for item in entries:
        path = REPO / item["file"]
        check(path.stat().st_size == item["bytes"] and digest(path.read_bytes()) == item["sha256"], f"Index differs from {path.name}")
        with zipfile.ZipFile(path) as archive:
            check(len(archive.namelist()) == item["files"], f"Index count differs for {path.name}")
    for number in (11, 12):
        check(not (REPO / f"class-{number:02d}").exists(), "Retired class package remains in the student view")
    print("PASS: current download index", flush=True)


class HiddenInputs(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.values = {}
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if tag == "input" and fields.get("type") == "hidden" and fields.get("name"):
            self.values[fields["name"]] = fields.get("value", "")


def get(client, url, values=None, json_body=False):
    data = None
    headers = {}
    if values is not None:
        data = json.dumps(values).encode() if json_body else urllib.parse.urlencode(values).encode()
        headers["Content-Type"] = "application/json" if json_body else "application/x-www-form-urlencoded"
    with client.open(urllib.request.Request(url, data=data, headers=headers), timeout=10) as response:
        return response.geturl(), response.read().decode("utf-8-sig")


def submit(client, page, values):
    inputs = HiddenInputs(page[1]).values
    inputs.update(values)
    return get(client, page[0], inputs)


def stop_server(process):
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], capture_output=True)
    else:
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=5)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory(prefix="course-release-check-") as temp:
        for number in (8, 9):
            verify_archive(number, Path(temp))
    verify_index()
    verify_links()
    print(f"RELEASE CHECKS PASSED: {CHECKS}")
