"""CI-only production smoke test against a disposable local PostgreSQL service.

This never connects to Heroku or oTree Hub. CI must supply the exact disposable
course_ci database account below. Only this run's newly created schema is removed.
No credentials, participant identifiers, response data, or server logs are printed.
"""

import csv
import io
import json
import os
import secrets
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from html.parser import HTMLParser
from http.cookiejar import CookieJar
from importlib.metadata import version
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import (
    HTTPRedirectHandler, HTTPCookieProcessor, ProxyHandler, Request, build_opener,
)


EXPERIMENT = Path(__file__).resolve().parents[1] / "project/experiment"
COLUMNS = [
    "session_code", "participant_code", "study_version", "round_number",
    "sure_points", "gamble_high", "gamble_probability", "choice", "confidence",
]
OFFERS = [2, 3, 4, 6, 7, 8]
CHOICES = ["gamble", "sure", "gamble", "gamble", "sure", "sure"]
CONFIDENCE = [1, 7, 3, 5, 2, 6]


class CheckFailure(Exception):
    """A safe, fixed diagnostic that contains no server state or credentials."""


def require(condition, message):
    if not condition:
        raise CheckFailure(message)


def validate_database_url(value):
    """Reject all databases except the deliberately public, local CI fixture."""
    try:
        parsed = urlsplit(value)
        valid = (
            parsed.scheme in {"postgres", "postgresql"}
            and parsed.hostname in {"localhost", "127.0.0.1"}
            and parsed.port == 5432
            and parsed.username == "course_ci"
            and parsed.password == "course_ci_only"
            and parsed.path == "/course_ci"
            and not parsed.query
            and not parsed.fragment
            and not any(character.isspace() for character in value)
        )
    except (ValueError, TypeError):
        valid = False
    require(valid, "Refusing a database outside the exact disposable localhost CI fixture.")
    # Use a numeric loopback address rather than trusting hostname resolution.
    return "postgresql://course_ci:course_ci_only@127.0.0.1:5432/course_ci"


class HiddenInputs(HTMLParser):
    """Retain form tokens without requiring another third-party test package."""

    def __init__(self):
        super().__init__()
        self.values = {}
        self.has_form = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "form":
            self.has_form = True
        if tag == "input" and attrs.get("type") == "hidden" and attrs.get("name"):
            self.values[attrs["name"]] = attrs.get("value", "")


class LocalRedirects(HTTPRedirectHandler):
    def __init__(self, origin, follow):
        self.origin = origin
        self.follow = follow

    def redirect_request(self, request, fp, code, message, headers, new_url):
        parsed = urlsplit(new_url)
        require(f"{parsed.scheme}://{parsed.netloc}" == self.origin,
                "Server attempted a redirect outside the disposable local test.")
        if not self.follow:
            return None
        return super().redirect_request(request, fp, code, message, headers, new_url)


@dataclass
class Reply:
    status: int
    url: str
    text: str
    headers: object


class Client:
    def __init__(self, origin, rest_key=None):
        self.origin = origin
        self.rest_key = rest_key
        self.cookies = CookieJar()

    def request(self, path, *, payload=None, form=None, follow=True, key=None):
        url = path if path.startswith("http://") else self.origin + path
        parsed = urlsplit(url)
        require(f"{parsed.scheme}://{parsed.netloc}" == self.origin,
                "Refusing a request outside the disposable local server.")
        headers = {}
        rest_key = self.rest_key if key is None else key
        if rest_key:
            headers["otree-rest-key"] = rest_key
        data = None
        if payload is not None:
            data = json.dumps(payload).encode()
            headers["Content-Type"] = "application/json"
        if form is not None:
            data = urlencode(form).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        # Disable proxies, including inherited CI environment proxy settings.
        opener = build_opener(ProxyHandler({}), HTTPCookieProcessor(self.cookies),
                              LocalRedirects(self.origin, follow))
        try:
            response = opener.open(Request(url, data=data, headers=headers), timeout=10)
        except HTTPError as error:
            response = error
        with response:
            return Reply(response.status, response.url,
                         response.read().decode("utf-8"), response.headers)

    def submit(self, page, answers):
        tokens = HiddenInputs()
        tokens.feed(page.text)
        require(tokens.has_form, "Expected a participant form in the production response.")
        return self.request(page.url, form={**tokens.values, **answers})


def exercise_server(origin, rest_key, admin_password):
    """Check access controls, then compare a known journey with its protected CSV."""
    anonymous = Client(origin)
    api = Client(origin, rest_key)
    for path in ["/static/choice_task/study.css", "/static/choice_task/confidence.js"]:
        require(anonymous.request(path).status == 200, "Production participant asset could not be served.")
    for path in ["/sessions", "/ExportIndex"]:
        response = anonymous.request(path, follow=False)
        require(response.status in {302, 303, 307}, "Anonymous administration was not redirected.")
        require(urlsplit(response.headers.get("Location", "")).path == "/login",
                "Anonymous administration did not require login.")
    for path in ["/api/sessions", "/api/otree_version",
                 "/api/export_app_custom?app=choice_task"]:
        require(anonymous.request(path).status == 403, "REST endpoint allowed a missing REST key.")
        require(anonymous.request(path, key="intentionally-invalid-ci-key").status == 403,
                "REST endpoint allowed an incorrect REST key.")
    require(anonymous.request("/api/sessions", payload={
        "session_config_name": "sure_or_gamble", "num_participants": 2,
    }).status == 403, "Unauthenticated session creation was not blocked.")

    # Verify browser administration works only after the generated password is supplied.
    admin = Client(origin)
    login = admin.request("/login")
    invalid = admin.submit(login, {"username": "admin", "password": "incorrect-ci-password"})
    require(urlsplit(invalid.url).path == "/login", "Incorrect admin password was accepted.")
    valid = admin.submit(login, {"username": "admin", "password": admin_password})
    require(valid.status == 200 and urlsplit(valid.url).path != "/login",
            "Generated admin password did not permit login.")
    require(admin.request("/ExportIndex").status == 200, "Authenticated export page failed.")

    running_version = api.request("/api/otree_version")
    require(running_version.status == 200 and json.loads(running_version.text)["version"] == "6.0.15",
            "The running production server is not oTree 6.0.15.")
    created = api.request("/api/sessions", payload={
        "session_config_name": "sure_or_gamble", "num_participants": 2,
    })
    require(created.status == 200, "Protected synthetic-session creation failed.")
    session_code = json.loads(created.text)["code"]
    detail = api.request("/api/get_session/" + session_code, payload={})
    require(detail.status == 200, "Protected session lookup failed.")
    participants = json.loads(detail.text)["participants"]
    require(len(participants) == 2, "Synthetic session did not have two participants.")
    first, second = [participant["code"] for participant in participants]

    participant = Client(origin)
    page = participant.request("/InitializeParticipant/" + first)
    require(page.status == 200 and "Six decisions. Your preferences." in page.text,
            "Public participant link failed in STUDY mode.")
    page = participant.submit(page, {})
    for index, offer in enumerate(OFFERS):
        require(page.status == 200 and f"{offer} points</span>" in page.text,
                "Production participant flow showed the wrong offer.")
        # This detects an accidental development/debug launch under production settings.
        require("debug-info" not in page.text, "Production page exposed development debug information.")
        page = participant.submit(page, {
            "choice": CHOICES[index], "confidence": str(CONFIDENCE[index]),
        })
    require(page.status == 200 and "Your six responses are recorded." in page.text,
            "Production participant did not reach the saved-response receipt.")

    export_path = "/api/export_app_custom?" + urlencode({
        "app": "choice_task", "session_code": session_code,
    })
    require(anonymous.request(export_path).status == 403,
            "Unauthenticated access exposed the populated export.")
    exported = api.request(export_path)
    require(exported.status == 200, "Protected custom export failed.")
    reader = csv.DictReader(io.StringIO(exported.text))
    require(reader.fieldnames == COLUMNS, "Production custom export schema changed.")
    rows = list(reader)
    require(len(rows) == 12, "Production export omitted complete or unvisited rounds.")
    expected = []
    for code in [first, second]:
        for index, offer in enumerate(OFFERS):
            expected.append(dict(zip(COLUMNS, [
                session_code, code, "full-v1", str(index + 1), str(offer), "10", "0.5",
                CHOICES[index] if code == first else "",
                str(CONFIDENCE[index]) if code == first else "",
            ])))
    sort_key = lambda row: (row["participant_code"], int(row["round_number"]))
    require(sorted(rows, key=sort_key) == sorted(expected, key=sort_key),
            "Production export differed from the exact known and unvisited response rows.")
    participant.request(page.url)
    require(api.request(export_path).text == exported.text, "Receipt refresh changed saved response data.")


def stop_server(process):
    """Stop only the new process group, including oTree's timeout subprocess."""
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        return
    try:
        process.wait(timeout=10)
    except subprocess.TimeoutExpired:
        pass
    # A child can outlive its parent; do not leave it running after schema cleanup.
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    process.wait(timeout=5)


def main():
    require(sys.platform == "linux" and os.environ.get("CI") == "true",
            "This disposable hosting check runs only in Linux CI with CI=true.")
    database_url = validate_database_url(os.environ.get("DATABASE_URL", ""))
    require(version("otree") == "6.0.15" and version("psycopg2") == "2.9.13",
            "Install the experiment's pinned server requirements before this check.")
    # Import the driver only after all safety checks; no database is touched on refusal.
    import psycopg2
    from psycopg2 import sql

    executable = Path(sys.executable).parent / "otree"
    require(executable.is_file(), "The current Python environment lacks its oTree command.")
    schema = "ci_verify_" + secrets.token_hex(12)
    connection = psycopg2.connect(database_url, connect_timeout=5, options="")
    connection.autocommit = True
    schema_created = False
    process = None
    try:
        with connection.cursor() as cursor:
            # A CI container reports its internal address, not the host's forwarded loopback.
            cursor.execute("SELECT current_database(), current_user")
            require(cursor.fetchone() == ("course_ci", "course_ci"),
                    "Connected database identity is not the disposable CI fixture.")
            # Never reuse an existing schema, reset a database, or touch public tables.
            cursor.execute(sql.SQL("CREATE SCHEMA {} AUTHORIZATION course_ci").format(sql.Identifier(schema)))
            schema_created = True
        with tempfile.TemporaryDirectory(prefix="course-hosting-ci-") as temporary:
            app = Path(temporary) / "experiment"
            shutil.copytree(EXPERIMENT, app, ignore=shutil.ignore_patterns(
                "__pycache__", "*.pyc", "*.sqlite3", ".env", ".venv", ".git",
            ))
            with socket.socket() as listener:
                listener.bind(("127.0.0.1", 0))
                port = listener.getsockname()[1]
            origin = f"http://127.0.0.1:{port}"
            admin_password = secrets.token_urlsafe(32)
            rest_key = secrets.token_urlsafe(32)
            # Do not inherit cloud credentials, app configuration, or in-memory SQLite flags.
            environment = {key: os.environ[key] for key in ["HOME", "LANG", "TMPDIR"] if key in os.environ}
            environment.update({
                "PATH": str(executable.parent) + os.pathsep + os.defpath,
                "PYTHONUNBUFFERED": "1",
                "DATABASE_URL": database_url,
                "PGOPTIONS": f"-c search_path={schema}",
                "DYNO": "course-ci-disposable",
                "OTREE_PRODUCTION": "1",
                "OTREE_AUTH_LEVEL": "STUDY",
                "OTREE_ADMIN_PASSWORD": admin_password,
                "OTREE_SECRET_KEY": secrets.token_urlsafe(48),
                "OTREE_REST_KEY": rest_key,
            })
            try:
                process = subprocess.Popen(
                    [str(executable), "prodserver", f"127.0.0.1:{port}"],
                    cwd=app, env=environment, start_new_session=True,
                    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                )
                deadline = time.monotonic() + 60
                while time.monotonic() < deadline:
                    require(process.poll() is None, "Production server exited before readiness.")
                    try:
                        if Client(origin).request("/login").status == 200:
                            break
                    except (URLError, TimeoutError, ConnectionError):
                        pass
                    time.sleep(0.25)
                else:
                    raise CheckFailure("Production server did not become ready within 60 seconds.")
                exercise_server(origin, rest_key, admin_password)
                # Inspect only our schema to prove this was PostgreSQL, not a SQLite fallback.
                with connection.cursor() as cursor:
                    cursor.execute(sql.SQL("SELECT COUNT(*) FROM {}.choice_task_player").format(sql.Identifier(schema)))
                    require(cursor.fetchone()[0] == 12, "PostgreSQL did not contain the expected 12 round records.")
            finally:
                if process is not None:
                    stop_server(process)
                    process = None
    finally:
        try:
            if schema_created:
                with connection.cursor() as cursor:
                    cursor.execute(sql.SQL("DROP SCHEMA {} CASCADE").format(sql.Identifier(schema)))
        finally:
            connection.close()
    print("PASS: production PostgreSQL flow, admin/REST protection, exact export, and isolated cleanup.")


if __name__ == "__main__":
    try:
        main()
    except CheckFailure as error:
        print("FAIL:", error, file=sys.stderr)
        raise SystemExit(1)
    except Exception as error:
        # Library exceptions can embed DB credentials or participant URLs. Print only type.
        print(f"FAIL: hosting verification raised {type(error).__name__}; sensitive details suppressed.", file=sys.stderr)
        raise SystemExit(1)
