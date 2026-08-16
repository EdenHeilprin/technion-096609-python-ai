"""Dependency-free public checker for Practical Check 1.

Run:
    python public_check.py submission.py
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys


VALID_TRIAL = {
    "trial_id": 10,
    "condition": "gain",
    "response": "left",
    "correct": True,
    "reaction_time_ms": 450,
}


def load_submission(path_text):
    path = Path(path_text)
    if not path.is_file():
        raise FileNotFoundError(f"Submission file not found: {path}")

    spec = spec_from_file_location("practical_check_1_submission", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load: {path}")

    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect(label, condition):
    if not condition:
        raise AssertionError(label)
    print(f"PASS: {label}")


def expect_raises_value_error(label, function, argument):
    try:
        function(argument)
    except ValueError:
        print(f"PASS: {label}")
        return
    raise AssertionError(label)


def run_checks(module):
    expect("required functions exist", callable(module.validate_trial) and callable(module.analyze_trials))
    expect("valid trial is accepted", module.validate_trial(VALID_TRIAL.copy()) is True)

    missing_field = VALID_TRIAL.copy()
    del missing_field["condition"]
    expect("missing field is rejected", module.validate_trial(missing_field) is False)

    invalid_condition = VALID_TRIAL.copy()
    invalid_condition["condition"] = "neutral"
    expect(
        "unknown condition is rejected",
        module.validate_trial(invalid_condition) is False,
    )

    invalid_response = VALID_TRIAL.copy()
    invalid_response["response"] = "up"
    expect(
        "unknown response is rejected",
        module.validate_trial(invalid_response) is False,
    )

    invalid_correct_type = VALID_TRIAL.copy()
    invalid_correct_type["correct"] = 1
    expect(
        "non-Boolean correct value is rejected",
        module.validate_trial(invalid_correct_type) is False,
    )

    invalid_trial_id = VALID_TRIAL.copy()
    invalid_trial_id["trial_id"] = True
    expect(
        "Boolean trial ID is not treated as an integer ID",
        module.validate_trial(invalid_trial_id) is False,
    )

    impossible_omission = VALID_TRIAL.copy()
    impossible_omission.update(
        {"response": None, "correct": True, "reaction_time_ms": None}
    )
    expect(
        "inconsistent omission is rejected",
        module.validate_trial(impossible_omission) is False,
    )

    invalid_rt = VALID_TRIAL.copy()
    invalid_rt["reaction_time_ms"] = 0
    expect("non-positive RT is rejected", module.validate_trial(invalid_rt) is False)

    boolean_rt = VALID_TRIAL.copy()
    boolean_rt["reaction_time_ms"] = True
    expect(
        "Boolean RT is not treated as an integer RT",
        module.validate_trial(boolean_rt) is False,
    )

    expected_sample = {
        "total_trials": 5,
        "answered_trials": 4,
        "omission_trials": 1,
        "correct_trials": 3,
        "accuracy": 0.75,
        "mean_correct_rt_ms": 533.3,
    }
    expect(
        "sample summary matches the contract",
        module.analyze_trials(module.SAMPLE_TRIALS) == expected_sample,
    )

    expected_empty = {
        "total_trials": 0,
        "answered_trials": 0,
        "omission_trials": 0,
        "correct_trials": 0,
        "accuracy": None,
        "mean_correct_rt_ms": None,
    }
    expect("empty input is handled", module.analyze_trials([]) == expected_empty)

    omissions = [
        {
            "trial_id": 1,
            "condition": "loss",
            "response": None,
            "correct": False,
            "reaction_time_ms": None,
        },
        {
            "trial_id": 2,
            "condition": "gain",
            "response": None,
            "correct": False,
            "reaction_time_ms": None,
        },
    ]
    expected_omissions = {
        "total_trials": 2,
        "answered_trials": 0,
        "omission_trials": 2,
        "correct_trials": 0,
        "accuracy": None,
        "mean_correct_rt_ms": None,
    }
    expect(
        "all-omission input is handled",
        module.analyze_trials(omissions) == expected_omissions,
    )

    expect_raises_value_error(
        "invalid records are rejected by analyze_trials",
        module.analyze_trials,
        [impossible_omission],
    )


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python public_check.py submission.py")

    try:
        submission = load_submission(sys.argv[1])
        run_checks(submission)
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}")
        raise SystemExit(1) from error

    print("PASS: all public checks completed")


if __name__ == "__main__":
    main()
