import random


CONDITIONS = ["sure_first", "risky_first"]

OUTPUT_COLUMNS = [
    "participant_code",
    "condition",
    "trial_id",
    "display_position",
    "option_1",
    "selected_key",
    "choice",
    "response_time_ms",
    "timed_out",
]


def prepare_session(stimuli, seed):
    rng = random.Random(seed)
    condition = rng.choice(CONDITIONS)
    ordered_trials = stimuli.copy()
    rng.shuffle(ordered_trials)
    return condition, ordered_trials


def first_option(condition):
    if condition == "sure_first":
        return "sure"
    return "risky"


def choice_from_key(selected_key, option_1):
    if selected_key == "1":
        return option_1
    if option_1 == "sure":
        return "risky"
    return "sure"


def build_trial_row(
    participant_code,
    condition,
    trial_id,
    display_position,
    selected_key,
    response_time_ms,
    timed_out,
):
    option_1 = first_option(condition)

    if timed_out:
        selected_key = None
        choice = None
        response_time_ms = None
    else:
        choice = choice_from_key(selected_key, option_1)

    return {
        "participant_code": participant_code,
        "condition": condition,
        "trial_id": trial_id,
        "display_position": display_position,
        "option_1": option_1,
        "selected_key": selected_key,
        "choice": choice,
        "response_time_ms": response_time_ms,
        "timed_out": timed_out,
    }
