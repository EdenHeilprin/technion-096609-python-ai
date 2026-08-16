"""Practical Check 1 starter.

This file is intentionally defective. Copy it to submission.py before editing.
The records are synthetic and do not describe real participants.
"""


SAMPLE_TRIALS = [
    {
        "trial_id": 1,
        "condition": "gain",
        "response": "left",
        "correct": True,
        "reaction_time_ms": 520,
    },
    {
        "trial_id": 2,
        "condition": "gain",
        "response": "right",
        "correct": False,
        "reaction_time_ms": 710,
    },
    {
        "trial_id": 3,
        "condition": "loss",
        "response": None,
        "correct": False,
        "reaction_time_ms": None,
    },
    {
        "trial_id": 4,
        "condition": "loss",
        "response": "left",
        "correct": True,
        "reaction_time_ms": 480,
    },
    {
        "trial_id": 5,
        "condition": "gain",
        "response": "right",
        "correct": True,
        "reaction_time_ms": 600,
    },
]


def validate_trial(trial):
    """Return True only when one trial follows the published data contract."""
    required_fields = {
        "trial_id",
        "condition",
        "response",
        "correct",
        "reaction_time_ms",
    }

    for field in required_fields:
        if field not in trial:
            return False

    # This unfinished validation accepts inconsistent values.
    return True


def analyze_trials(trials):
    """Validate and summarize a list of behavioral trial dictionaries."""
    total_trials = len(trials)
    answered_trials = 0
    correct_trials = 0
    correct_reaction_times = []

    for position, trial in enumerate(trials):
        if not validate_trial(trial):
            raise ValueError(f"Invalid trial at position {position}")

        if trial["response"] is None:
            answered_trials += 1

        if trial["correct"]:
            correct_trials += 1
            correct_reaction_times.append(trial["reaction_time"])

    omission_trials = answered_trials - total_trials
    accuracy = round(correct_trials / total_trials, 3)
    mean_correct_rt_ms = round(
        sum(correct_reaction_times) / len(correct_reaction_times),
        1,
    )

    return {
        "total_trials": total_trials,
        "answered_trials": answered_trials,
        "omission_trials": omission_trials,
        "correct_trials": correct_trials,
        "accuracy": accuracy,
        "mean_correct_rt_ms": mean_correct_rt_ms,
    }


if __name__ == "__main__":
    print(analyze_trials(SAMPLE_TRIALS))

    # Add at least two meaningful assertions of your own before submission.
