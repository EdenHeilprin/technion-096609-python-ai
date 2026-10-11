"""Rehearse Class 10 Git commands locally; never create a real fork or PR.

Two disposable bare repositories stand in for the course and a student's fork.
This checks local commands and branch isolation, not GitHub login or its GUI.
"""
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.parse import unquote

REPO = Path(__file__).resolve().parents[2]


def run(folder, *command):
    result = subprocess.run(command, cwd=folder, capture_output=True, text=True,
                            encoding="utf-8", timeout=60)
    if result.returncode:
        raise RuntimeError(f"{command}: {result.stdout}\n{result.stderr}")
    return result.stdout.strip()


def git(folder, *args):
    return run(folder, "git", "-c", "commit.gpgsign=false", *args)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def check_links():
    pages = list((REPO / "class-10").rglob("*.md")) + [REPO / "student-lessons/README.md"]
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for link in re.findall(r"\]\(([^\s)]+)\)", text):
            if not re.match(r"(?:https?:|mailto:|#)", link):
                target = unquote(link.split("#")[0])
                require((page.parent / target).exists(), f"Broken link in {page}: {link}")
    require(not (REPO / "class-10/class-10-files.zip").exists(), "Class 10 uses a clone, not an obsolete ZIP")
    print("PASS: Class 10 template and local links")


def rehearse():
    with tempfile.TemporaryDirectory(prefix="class 10 contribution ") as temporary:
        root = Path(temporary)
        course = root / "course"
        course.mkdir()
        git(course, "init", "--initial-branch=main")
        git(course, "config", "user.name", "Course test")
        git(course, "config", "user.email", "course@example.invalid")
        shutil.copytree(REPO / "class-10", course / "class-10")
        (course / "student-lessons").mkdir()
        shutil.copyfile(REPO / "student-lessons/README.md", course / "student-lessons/README.md")
        shutil.copyfile(REPO / ".gitignore", course / ".gitignore")
        git(course, "add", ".")
        git(course, "commit", "-m", "Course baseline")
        original = git(course, "rev-parse", "HEAD")
        upstream = root / "upstream.git"
        fork = root / "fork.git"
        git(root, "clone", "--bare", str(course), str(upstream))
        git(root, "clone", "--bare", str(upstream), str(fork))
        local = root / "class-10"
        local.mkdir()
        # This is the local Git arrangement made by gh repo fork --clone -- .
        git(local, "clone", str(fork), ".")
        git(local, "remote", "add", "upstream", str(upstream))
        git(local, "fetch", "upstream")
        git(local, "switch", "-c", "add-my-lesson", "upstream/main")
        git(local, "config", "user.name", "Student test")
        git(local, "config", "user.email", "student@example.invalid")
        require(git(local, "branch", "--show-current") == "add-my-lesson", "Wrong working branch")
        commands = [
            "mkdir student-lessons/student-demo",
            "cp class-10/lesson-template/README.md student-lessons/student-demo/README.md",
            "cp class-10/lesson-template/requirements.txt student-lessons/student-demo/requirements.txt",
        ]
        shell = ["powershell", "-NoProfile", "-NonInteractive", "-Command"] if os.name == "nt" else ["/bin/sh", "-c"]
        for command in commands:
            run(local, *shell, command)
        folder = local / "student-lessons/student-demo"
        # Git can use CRLF in a Windows checkout. Check the copy against its
        # actual source in this clone, then compare normalized text to the course.
        for name in ("README.md", "requirements.txt"):
            source = local / "class-10/lesson-template" / name
            require((folder / name).read_bytes() == source.read_bytes(), f"Template copy differs: {name}")
            require(source.read_text(encoding="utf-8") ==
                    (REPO / "class-10/lesson-template" / name).read_text(encoding="utf-8"),
                    f"Cloned template content differs: {name}")
        (folder / "README.md").write_text("# Test lesson\n\nA fictional contribution.\n", encoding="utf-8")
        (local / ".venv").mkdir()
        (local / ".venv/private-marker").write_text("not for submission", encoding="utf-8")
        require(git(local, "check-ignore", ".venv/private-marker") == ".venv/private-marker", "Environment not ignored")
        git(local, "add", "--", "student-lessons/student-demo")
        staged = git(local, "diff", "--cached", "--name-only").splitlines()
        require(len(staged) == 2 and all(name.startswith("student-lessons/student-demo/") for name in staged),
                "Submission includes unrelated files")
        git(local, "--no-pager", "diff", "--cached")
        git(local, "commit", "-m", "Add our student lesson")
        git(local, "push", "-u", "origin", "add-my-lesson")
        first = git(fork, "rev-parse", "add-my-lesson")
        (folder / "README.md").write_text("# Test lesson\n\nRevised after feedback.\n", encoding="utf-8")
        git(local, "add", "--", "student-lessons/student-demo")
        git(local, "commit", "-m", "Revise lesson after feedback")
        git(local, "push", "origin", "add-my-lesson")
        require(git(fork, "rev-parse", "add-my-lesson") != first, "Revision did not update the same remote branch")
        require(git(upstream, "rev-parse", "main") == original, "Original course changed before review")
        require(git(fork, "rev-parse", "main") == original, "Fork main changed")
        require(git(local, "status", "--porcelain") == "", "Unexpected leftover changes")
        print("PASS: clone, branch, shell copy commands, scoped commit, push, and revision; original main unchanged")


if __name__ == "__main__":
    check_links()
    rehearse()
