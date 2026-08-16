"""Public self-check for Week 1. No third-party packages are required."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import sys


DEFAULT_SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "starter" / "first_research_script.py"
)
EXPECTED_OUTPUT = """Participant: SYN001
Condition: gain
Mean reaction time (ms): 500.0
Correct trials: 2 of 3
Accuracy rate: 0.67
"""


def check() -> None:
    """Run the submitted script and report the first useful mismatch."""
    script_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_SCRIPT_PATH
    captured_output = StringIO()

    try:
        with redirect_stdout(captured_output):
            variables = runpy.run_path(str(script_path))
    except Exception as error:
        print("NOT YET: The script raised an error when the check ran it.")
        print(f"{type(error).__name__}: {error}")
        print("Run the starter file directly, repair the error, and check again.")
        raise SystemExit(1)

    checks = {
        "mean_reaction_time_ms should equal 500.0": (
            variables.get("mean_reaction_time_ms") == 500.0
        ),
        "accuracy_rate should equal 0.67": variables.get("accuracy_rate") == 0.67,
        "the five output lines should match the specification": (
            captured_output.getvalue() == EXPECTED_OUTPUT
        ),
    }

    for message, passed in checks.items():
        if not passed:
            print(f"NOT YET: {message}.")
            print("Compare your calculation and output with the Week 1 specification.")
            raise SystemExit(1)

    print("PASS: Your calculations and output match the Week 1 core specification.")


if __name__ == "__main__":
    check()
