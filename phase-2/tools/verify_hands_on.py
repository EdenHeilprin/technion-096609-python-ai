"""Check Class 9 in a disposable extracted project, never personal work."""
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


def save_and_stop(process, port):
    # The non-interactive runner stops a process tree, not a terminal's Ctrl+C.
    # Flush via oTree's own devserver reload endpoint first; Windows taskkill
    # otherwise discards the in-memory database and creates a fake bug.
    try:
        if process.poll() is None:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/SaveDB", data=b"save", timeout=10) as response:
                check(response.status == 200, "oTree flushes the development database")
    finally:
        stop_server(process)
        # The launcher can exit before its child closes the listening socket.
        # Do not mistake that old child for the next server's readiness probe.
        for attempt in range(100):
            try:
                with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                    pass
            except OSError:
                break
            time.sleep(0.1)
        else:
            raise RuntimeError("The previous devserver is still listening after shutdown")


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
            configs = json.loads(get(client, base + "/api/session_configs")[1])
            check(len(configs) == 1 and configs[0]["display_name"] == "Sure or gamble",
                  "One experiment configuration with the lesson's displayed name")
            demo = get(client, base)[1]
            check("Sure or gamble" in demo and "TEST ONLY" not in demo, "No duplicate test demo")
            session = json.loads(get(client, base + "/api/sessions",
                                    {"session_config_name": "seven_choices", "num_participants": 2}, True)[1])
            info = json.loads(get(client, base + "/api/sessions/" + session["code"])[1])
            # Use the same per-app download as the lesson, including blank runs.
            export_url = base + "/api/export_app?app=choice_task"
            initial = list(csv.DictReader(io.StringIO(get(client, export_url)[1])))
            check(len(initial) == 14, "Fourteen participant-round rows in per-app export")
            conditions = {row["participant.code"]: row["player.condition"] for row in initial
                          if row["subsession.round_number"] == "1"}
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
            check(len(rows) == 14, "Two completed runs contribute fourteen decisions")
            for row in rows:
                prizes, answers, _ = expected[row["participant.code"]]
                number = int(row["subsession.round_number"])
                check(int(row["player.prize"]) == prizes[number - 1], "Saved prize")
                check(row["player.choice"] == answers[number - 1], "Saved response")
                check(row["session.code"] == session["code"], "Exported session identifier")
                if number == 1:
                    check(bool(row["player.completed_at"]), "Completion recorded")
            export_page = get(client, base + "/ExportIndex")[1]
            check("Per-app data" in export_page and 'id="app-choice_task"' in export_page,
                  "Per-app CSV button matches lesson")
        finally:
            save_and_stop(process, port)
        # Apply the manual wording edit only inside the disposable test copy.
        thanks = project / "choice_task/ThankYou.html"
        original = thanks.read_text(encoding="utf-8")
        revised = "Your seven decisions have been saved."
        thanks.write_text(original.replace("Your seven decisions have been recorded.", revised), encoding="utf-8")
        process = start_server(project, port, log)
        try:
            check(get(client, export_url)[1] == raw, "Restart preserves all saved responses")
            for _, _, url in expected.values():
                check(revised in get(client, url)[1], "Saved HTML edit appears after restart/refresh")
        finally:
            save_and_stop(process, port)
        # Check the subsequent formatting task separately from the manual edit.
        formatted = 'Your seven decisions have been <strong style="color: #166534;">saved</strong>.'
        thanks.write_text(original.replace("Your seven decisions have been recorded.", formatted), encoding="utf-8")
        process = start_server(project, port, log)
        try:
            check(get(client, export_url)[1] == raw, "Formatting leaves saved responses unchanged")
            for _, _, url in expected.values():
                check(formatted in get(client, url)[1], "Bold, dark-green saved word renders")
        finally:
            save_and_stop(process, port)
            thanks.write_text(original, encoding="utf-8")
    print("PASS: Class 9 single configuration, both orders, per-app CSV, restart, manual and formatting edits")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--class9", type=Path, required=True)
    args = parser.parse_args()
    # Test copies guarantee the caller's files and responses cannot be edited.
    with tempfile.TemporaryDirectory(prefix="hands on check ") as temporary:
        root = Path(temporary)
        shutil.copytree(args.class9, root / "class-09",
                        ignore=shutil.ignore_patterns(".venv", "__pycache__", "*.sqlite3", "*.db", "exports", "*.zip"))
        try:
            check_experiment(root / "class-09")
        except Exception:
            log = root / "class-09/server-test.log"
            if log.exists():
                print(log.read_text(encoding="utf-8", errors="replace"), file=sys.stderr)
            raise
