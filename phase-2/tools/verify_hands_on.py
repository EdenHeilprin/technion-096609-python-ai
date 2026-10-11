"""Check Classes 9/10 in disposable extracted projects, never personal work."""
import argparse
import csv
import http.cookiejar
import io
import json
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

from verify_release import check, get, stop_server, submit


def start_server(project, port, log):
    executable = Path(sys.executable).parent / ("otree.exe" if os.name == "nt" else "otree")
    environment = dict(os.environ)
    for key in ("DATABASE_URL", "OTREE_PRODUCTION", "OTREE_AUTH_LEVEL", "OTREE_ADMIN_PASSWORD",
                "OTREE_SECRET_KEY", "OTREE_REST_KEY", "DYNO"):
        environment.pop(key, None)
    environment["PATH"] = str(executable.parent) + os.pathsep + environment.get("PATH", "")
    process = subprocess.Popen([str(executable), "devserver", str(port)], cwd=project,
                               env=environment, stdout=log, stderr=subprocess.STDOUT,
                               start_new_session=os.name != "nt")
    try:
        for attempt in range(150):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/otree_version", timeout=2) as response:
                    check(json.load(response)["version"] == "6.0.15", "oTree version")
                return process
            except (urllib.error.URLError, TimeoutError, ConnectionError):
                if process.poll() is not None:
                    raise RuntimeError("oTree stopped; inspect server-test.log")
                time.sleep(0.2)
        raise RuntimeError("oTree did not become ready")
    except Exception:
        stop_server(process)
        raise


def check_experiment(project):
    with socket.socket() as available:
        available.bind(("127.0.0.1", 0))
        port = available.getsockname()[1]
    base = f"http://127.0.0.1:{port}"
    client = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
    expected = {}
    with (project / "server-test.log").open("w", encoding="utf-8") as log:
        process = start_server(project, port, log)
        try:
            session = json.loads(get(client, base + "/api/sessions",
                                    {"session_config_name": "seven_choices", "num_participants": 2}, True)[1])
            info = json.loads(get(client, base + "/api/sessions/" + session["code"])[1])
            # Read the same wide export named in the lesson, including blank runs.
            export_url = base + "/api/export_wide?session_code=" + session["code"]
            initial = list(csv.DictReader(io.StringIO(get(client, export_url)[1])))
            check(len(initial) == 2, "Two participant rows in wide export")
            conditions = {row["participant.code"]: row["choice_task.1.player.condition"] for row in initial}
            check(set(conditions.values()) == {"ascending", "descending"}, "Both orders assigned")
            for index, person in enumerate(info["participants"]):
                code = person["code"]
                page = get(client, base + "/InitializeParticipant/" + code)
                check("voluntary" in page[1], "Consent page renders")
                rejected = submit(client, page, {})
                check(rejected[0] == page[0], "Consent required")
                page = submit(client, page, {"consent": "y"})
                check("made-up classroom ID" in page[1], "Details page renders")
                rejected = submit(client, page, {"subject_id": "   "})
                check(rejected[0] == page[0], "Whitespace ID rejected")
                page = submit(client, page, {"subject_id": f"practice-{index}"})
                prizes = [2, 8, 14, 20, 26, 32, 38]
                if conditions[code] == "descending":
                    prizes.reverse()
                answers = []
                for round_number, prize in enumerate(prizes, 1):
                    check(f"Decision {round_number} of 7" in page[1], "Round heading")
                    check(f"50% chance of {prize} points" in page[1], "Displayed prize matches condition")
                    check("100% chance of 10 points" in page[1], "Sure amount stays fixed")
                    rejected = submit(client, page, {})
                    check(rejected[0] == page[0], "Choice required")
                    choice = "gamble" if round_number % 2 == 0 else "sure"
                    answers.append(choice)
                    page = submit(client, page, {"choice": choice})
                check("Your seven decisions have been recorded." in page[1], "Thank-you page")
                check("Return to Prolific" not in page[1], "No external completion destination")
                expected[code] = (prizes, answers, page[0])
            raw = get(client, export_url)[1]
            rows = list(csv.DictReader(io.StringIO(raw)))
            for row in rows:
                prizes, answers, _ = expected[row["participant.code"]]
                for number in range(1, 8):
                    check(int(row[f"choice_task.{number}.player.prize"]) == prizes[number - 1], "Saved prize")
                    check(row[f"choice_task.{number}.player.choice"] == answers[number - 1], "Saved response")
                check(bool(row["choice_task.1.player.completed_at"]), "Completion recorded")
            check("All apps (wide format)" in get(client, base + "/ExportIndex")[1], "Export label matches lesson")
        finally:
            stop_server(process)
        # Apply the exact tiny lesson edit only inside the disposable test copy.
        thanks = project / "choice_task/ThankYou.html"
        original = thanks.read_text(encoding="utf-8")
        revised = "Your seven decisions have been saved. Thank you for your time."
        thanks.write_text(original.replace("Your seven decisions have been recorded.", revised), encoding="utf-8")
        process = start_server(project, port, log)
        try:
            check(get(client, export_url)[1] == raw, "Restart preserves all saved responses")
            for _, _, url in expected.values():
                check(revised in get(client, url)[1], "Saved HTML edit appears after restart/refresh")
        finally:
            stop_server(process)
            thanks.write_text(original, encoding="utf-8")
    print("PASS: Class 9 consent, details, both seven-round orders, saved export, restart, HTML edit")


def check_python(lesson):
    script = lesson / "summarize_choices.py"
    source = lesson / "sample_choices.csv"
    original = source.read_bytes()

    def run():
        # Run from outside the project: paths must follow the script, not cwd.
        result = subprocess.run([sys.executable, str(script)], cwd=lesson.parent,
                                capture_output=True, text=True, timeout=30)
        check(result.returncode == 0, result.stdout + result.stderr)
        with (lesson / "summary.csv").open(newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    check(run() == [{"choice": "gamble", "count": "7", "percentage": "50.0"}], "Starter output")
    check(source.read_bytes() == original, "Input unchanged")
    text = script.read_text(encoding="utf-8")
    solution = text.replace("# Exercise: calculate and print the sure count and percentage here.",
                            'sure_count = total_decisions - gamble_count\nsure_percentage = percentage(sure_count, total_decisions)\nprint("Sure choices:", sure_count)\nprint("Sure choices (%):", sure_percentage)')
    solution = solution.replace("    # Exercise: add a second row for sure choices here.",
                                '    writer.writerow(["sure", sure_count, sure_percentage])')
    script.write_text(solution, encoding="utf-8")
    check(run() == [{"choice": "gamble", "count": "7", "percentage": "50.0"},
                    {"choice": "sure", "count": "7", "percentage": "50.0"}], "Exercise solution")
    source.write_bytes(original.replace(b"2,sure", b"2,gamble", 1))
    check(run() == [{"choice": "gamble", "count": "8", "percentage": "57.1"},
                    {"choice": "sure", "count": "6", "percentage": "42.9"}], "Student's additional check")
    source.write_bytes(original)
    script.write_text(text, encoding="utf-8")
    print("PASS: Class 10 starter, relative paths, unchanged input, exercise solution, changed-response check")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--class9", type=Path, required=True)
    parser.add_argument("--class10", type=Path, required=True)
    args = parser.parse_args()
    # Test copies guarantee the caller's files and responses cannot be edited.
    with tempfile.TemporaryDirectory(prefix="hands on check ") as temporary:
        root = Path(temporary)
        for number, source in [(9, args.class9), (10, args.class10)]:
            shutil.copytree(source, root / f"class-{number:02d}",
                            ignore=shutil.ignore_patterns(".venv", "__pycache__", "*.sqlite3", "*.db", "exports", "*.zip"))
        check_experiment(root / "class-09")
        check_python(root / "class-10")
