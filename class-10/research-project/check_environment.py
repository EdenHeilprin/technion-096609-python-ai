"""Check the interpreter and installed package versions without installing anything."""

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import sys


PROJECT = Path(__file__).resolve().parent


def main():
    """Print specific mismatches so the learner can select the correct interpreter."""
    print("Python:", sys.executable)
    problems = []
    if sys.version_info[:2] != (3, 13):
        problems.append("The course project uses Python 3.13.x.")
    # sys.prefix identifies the active environment even when its executable is a symlink.
    if Path(sys.prefix).resolve() != (PROJECT / ".venv").resolve():
        problems.append("Select this project's .venv interpreter in VS Code.")

    for requirement in (PROJECT / "requirements.txt").read_text(encoding="utf-8").splitlines():
        if not requirement.strip() or requirement.startswith("#"):
            continue
        name, expected = requirement.split("==")
        try:
            actual = version(name)
            print(f"{name}: {actual}")
            if actual != expected:
                problems.append(f"{name}: expected {expected}, found {actual}.")
        except PackageNotFoundError:
            problems.append(f"{name} is not installed in this interpreter.")

    if problems:
        print("\nENVIRONMENT CHECK NEEDS ATTENTION")
        for problem in problems:
            print("-", problem)
        print("See SETUP.md in the class folder.")
        return 1
    print("\nENVIRONMENT CHECK PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
