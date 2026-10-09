"""Maintainer checks: archives, source agreement, then disposable student runs.

Run with the course environment and --runtime for local HTTP/analysis tests.
All test responses are synthetic and all servers bind to localhost.
"""
import argparse
import ast
import csv
import hashlib
import http.cookiejar
import io
import json
import os
import re
import signal
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
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
        check(len(paths) == len(set(paths)), f"{name}: no duplicate archive entries")
        for entry in paths:
            path = Path(entry)
            check(path.parts[0] == name and ".." not in path.parts and not path.is_absolute(), f"Unsafe archive entry {entry}")
            check(not {".venv", "__pycache__", ".git", "outputs"}.intersection(path.parts), f"Private/runtime content: {entry}")
            check(path.name not in {".env", ".DS_Store", "db.sqlite3"} and path.suffix not in {".pyc", ".db", ".sqlite3"}, f"Unexpected artifact: {entry}")
        archive.extractall(folder)
    lesson = folder / name
    manifest = json.loads((lesson / "DOWNLOAD_MANIFEST.json").read_text(encoding="utf-8"))
    actual = {str(p.relative_to(lesson)).replace("\\", "/") for p in lesson.rglob("*") if p.is_file()}
    check(actual == set(manifest) | {"DOWNLOAD_MANIFEST.json"}, f"{name}: exact manifest file set")
    for relative, expected in manifest.items():
        path = lesson / relative
        check(digest(path.read_bytes()) == expected, f"{name}: hash {relative}")
        check((source / relative).read_bytes() == path.read_bytes(), f"{name}: online source and ZIP differ: {relative}")
        if path.suffix == ".py":
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            check(True, f"{relative}: Python parses")
        if path.suffix in {".md", ".py", ".html", ".js", ".css", ".json", ".csv", ".txt"}:
            text = path.read_text(encoding="utf-8")
            check(not re.search(r"/Users/|/private/tmp/|C:\\Users\\|sk-proj-", text), f"{relative}: machine path or secret")
            if path.suffix == ".md":
                for link in re.findall(r"\]\(([^\s)]+)\)", text):
                    if not re.match(r"(?:https?:|mailto:|#)", link):
                        target = urllib.parse.unquote(link.split("#")[0])
                        check((path.parent / target).exists(), f"Broken relative Markdown link: {relative} -> {link}")
    check((lesson / "research-project/docs/STUDY_SPEC.md").exists(), f"{name}: supplied study context")
    if number in {9, 10}:
        check((lesson / "research-project/data").is_dir(), f"{name}: export destination exists")
    if number == 9:
        check(not (lesson / "research-project/experiment/choice_task").exists(), "Class9 is genuinely a scaffold")
        check((lesson / "checkpoints/minimal/research-project/experiment/choice_task/__init__.py").is_file(), "Class9 recovery")
    if number == 11:
        check(not (lesson / "research-project/analysis/analyze_choices.py").exists(), "Class11 preserves the build task")
        check((lesson / "checkpoints/analysis/research-project/analysis/analyze_choices.py").is_file(), "Class11 recovery")
    print(f"PASS: {name} archive, sources, syntax, privacy and links", flush=True)
    return lesson


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


def experiment_run(project, minimal=False, receipt=False):
    with socket.socket() as available:
        available.bind(("127.0.0.1", 0))
        port = available.getsockname()[1]
    base = f"http://127.0.0.1:{port}"
    bin_path = Path(sys.executable).parent
    executable = bin_path / ("otree.exe" if os.name == "nt" else "otree")
    environment = dict(os.environ, PATH=str(bin_path) + os.pathsep + os.environ.get("PATH", ""))
    for key in ("OTREE_PRODUCTION", "OTREE_AUTH_LEVEL", "OTREE_ADMIN_PASSWORD", "OTREE_SECRET_KEY", "DATABASE_URL", "DYNO"):
        environment.pop(key, None)
    environment["PYTHONUTF8"] = "1"
    client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    log_path = project / "server-test.log"
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen([str(executable), "devserver", str(port)], cwd=project / "experiment",
                                   env=environment, stdout=log, stderr=subprocess.STDOUT,
                                   start_new_session=os.name != "nt")
        try:
            for attempt in range(150):
                try:
                    version = json.loads(get(client, base + "/api/otree_version")[1])["version"]
                    break
                except (urllib.error.URLError, TimeoutError, ConnectionError):
                    if process.poll() is not None:
                        raise RuntimeError(log_path.read_text(encoding="utf-8"))
                    time.sleep(0.2)
            else:
                raise RuntimeError("Server did not become ready:\n" + log_path.read_text(encoding="utf-8"))
            check(version == "6.0.15", "Runtime is pinned oTree6.0.15")
            session = json.loads(get(client, base + "/api/sessions", {"session_config_name": "sure_or_gamble", "num_participants": 2}, True)[1])
            info = json.loads(get(client, base + "/api/sessions/" + session["code"])[1])
            page = get(client, base + "/InitializeParticipant/" + info["participants"][0]["code"])
            if not minimal:
                check("Six decisions. Your preferences." in page[1], "Welcome renders")
                page = submit(client, page, {})
            check("Which would you choose?" in page[1], "Choice renders")
            empty = submit(client, page, {})
            check(empty[0] == page[0], "Missing required answer does not advance")
            if not minimal:
                invalid = submit(client, page, {"choice": "sure", "confidence": "8"})
                check(invalid[0] == page[0], "Invalid confidence rejected server-side")
            offers = [4] if minimal else [2, 3, 4, 6, 7, 8]
            for index, offer in enumerate(offers):
                check(f"{offer} points</span>" in page[1], "Expected offer renders")
                old_page = page
                answers = {"choice": "gamble" if index < 3 else "sure"}
                if not minimal:
                    answers["confidence"] = str(index + 1)
                page = submit(client, page, answers)
                check(page[0] != old_page[0], "Valid response advances")
            check("recorded" in page[1], "Final acknowledgement renders")
            if receipt:
                check("<table" in page[1], "Showcase response summary renders")
            export_url = base + "/api/export_app_custom?" + urllib.parse.urlencode({"app": "choice_task", "session_code": session["code"]})
            exported = get(client, export_url)[1]
            rows = list(csv.DictReader(io.StringIO(exported)))
            check(len(rows) == 2 * len(offers), "Export includes complete and unvisited records")
            check(sum(bool(row["choice"]) for row in rows) == len(offers), "Only submitted responses are filled")
            check(all(row["study_version"] == ("minimal-v1" if minimal else "full-v1") for row in rows), "Version matches study")
            check(list(rows[0]) == ["session_code", "participant_code", "study_version", "round_number", "sure_points", "gamble_high", "gamble_probability", "choice", "confidence"], "Export exact contract")
            saved = [row for row in rows if row["choice"]]
            check([int(row["sure_points"]) for row in saved] == offers, "Stored offers match")
            print(f"PASS: {project.relative_to(project.parents[3])} oTree participant/export flow", flush=True)
            return exported
        finally:
            stop_server(process)


def runtime_checks(lessons):
    full_export = experiment_run(lessons[8] / "research-project")
    experiment_run(lessons[8] / "checkpoints/participant-summary/research-project", receipt=True)
    experiment_run(lessons[9] / "checkpoints/minimal/research-project", minimal=True)
    experiment_run(lessons[10] / "research-project", minimal=True)
    experiment_run(lessons[10] / "checkpoints/full/research-project")
    for number, relative in [(8, "research-project"), (11, "checkpoints/analysis/research-project"), (12, "research-project")]:
        project = lessons[number] / relative
        for script in ("inspect_data.py", "analyze_choices.py", "explore_confidence.py"):
            result = subprocess.run([sys.executable, str(project / "analysis" / script)], cwd=project.parent,
                                    capture_output=True, text=True, encoding="utf-8", timeout=90)
            check(result.returncode == 0, f"Class{number} {script}: {result.stdout}\n{result.stderr}")
        summary = json.loads((project / "outputs/synthetic_choices/summary.json").read_text(encoding="utf-8"))
        check((summary["input_rows"], summary["included_participants"], summary["included_trials"], summary["gamble_count"]) == (96, 15, 90, 46), "Reference arithmetic")
        check(summary["source_sha256"] == digest((project / "data/synthetic_choices.csv").read_bytes()), "Reference source provenance")
        print(f"PASS: Class {number} analysis and confidence extension", flush=True)
    project = lessons[11] / "research-project"
    result = subprocess.run([sys.executable, str(project / "analysis/my_analysis.py")], capture_output=True, text=True, timeout=60)
    check(result.returncode == 0, "Class11 starter executes")
    # Connect an actual locally collected oTree export to the canonical validator.
    sys.path.insert(0, str(lessons[12] / "research-project/analysis"))
    from study_data import read_export, select_complete_participants
    export = lessons[12] / "research-project/data/automated_test_export.csv"
    export.write_text(full_export, encoding="utf-8", newline="")
    clean, people = select_complete_participants(read_export(export))
    check(len(clean) == 6 and int(people["included"].sum()) == 1, "Fresh browser-shaped export passes analysis inclusion")
    check(clean["choice"].eq("gamble").sum() == 3, "Fresh export has expected saved decisions")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime", action="store_true")
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="course-phase2-check-") as temp:
        lessons = {number: verify_archive(number, Path(temp)) for number in range(8, 13)}
        if args.runtime:
            runtime_checks(lessons)
    print(f"RELEASE CHECKS PASSED: {CHECKS}")
