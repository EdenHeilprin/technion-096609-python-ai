from experiment_core import build_trial_row, choice_from_key, prepare_session


def test_repeatable_session():
    stimuli = [
        {"trial_id": "T01"},
        {"trial_id": "T02"},
        {"trial_id": "T03"},
        {"trial_id": "T04"},
    ]

    first_condition, first_order = prepare_session(stimuli, 12)
    second_condition, second_order = prepare_session(stimuli, 12)

    assert first_condition == second_condition
    assert first_order == second_order
    assert sorted(trial["trial_id"] for trial in first_order) == [
        "T01",
        "T02",
        "T03",
        "T04",
    ]


def test_key_mapping():
    assert choice_from_key("1", "sure") == "sure"
    assert choice_from_key("2", "sure") == "risky"
    assert choice_from_key("1", "risky") == "risky"
    assert choice_from_key("2", "risky") == "sure"


def test_completed_row():
    row = build_trial_row(
        participant_code="P900",
        condition="risky_first",
        trial_id="T02",
        display_position=1,
        selected_key="2",
        response_time_ms=840,
        timed_out=False,
    )

    assert row["option_1"] == "risky"
    assert row["selected_key"] == "2"
    assert row["choice"] == "sure"
    assert row["response_time_ms"] == 840
    assert row["timed_out"] is False


def test_timeout_row():
    row = build_trial_row(
        participant_code="P900",
        condition="sure_first",
        trial_id="T03",
        display_position=4,
        selected_key="1",
        response_time_ms=12500,
        timed_out=True,
    )

    assert row["option_1"] == "sure"
    assert row["selected_key"] is None
    assert row["choice"] is None
    assert row["response_time_ms"] is None
    assert row["timed_out"] is True


test_repeatable_session()
test_key_mapping()
test_completed_row()
test_timeout_row()

print("All experiment-core tests passed")
