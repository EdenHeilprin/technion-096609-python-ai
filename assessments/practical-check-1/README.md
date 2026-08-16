# Practical Check 1 prototype: repair a trial summary

Status: working prototype, not yet an announced graded assessment

## Purpose

This check asks whether you can use Python as a working tool: run a program, use runtime evidence, reason about data and denominators, repair defects, test edge cases, and explain a small change.

It is designed for the end of the fundamentals and debugging sequence, before pandas.

## Conditions

- Suggested working time: **75 minutes** on your computer.
- Follow-up: **5–7 minute individual demonstration** with the instructor.
- AI chats, coding agents, documentation, course materials, and the internet are permitted.
- You may ask for explanations, plans, code, debugging help, tests, and review.
- You remain responsible for the behavior of the submitted program.
- Use only the synthetic records supplied here. Do not add real participant data or identifiers.

## Starting point

The file [`starter.py`](starter.py) is intentionally defective. It includes both a runtime failure and plausible logic defects. A program that merely runs is not necessarily correct.

The data contract for each trial is:

| Field | Valid value |
|---|---|
| `trial_id` | Positive integer |
| `condition` | `"gain"` or `"loss"` |
| `response` | `"left"`, `"right"`, or `None` for an omission |
| `correct` | Boolean; an omitted response cannot be correct |
| `reaction_time_ms` | Positive integer for an answered trial; `None` for an omission |

## Required result

Create `submission.py`. It must retain these functions:

### `validate_trial(trial)`

Return `True` only when `trial` follows the complete data contract above. Return `False` for a missing field, an invalid value, or an inconsistent omission.

### `analyze_trials(trials)`

First reject an invalid record with `ValueError`. Otherwise return exactly these keys:

```python
{
    "total_trials": ...,
    "answered_trials": ...,
    "omission_trials": ...,
    "correct_trials": ...,
    "accuracy": ...,
    "mean_correct_rt_ms": ...,
}
```

Rules:

- accuracy is `correct_trials / answered_trials`, rounded to three decimals;
- mean correct RT includes only correct, answered trials and is rounded to one decimal;
- accuracy is `None` when there are no answered trials;
- mean correct RT is `None` when there are no correct trials;
- an empty list is valid and returns zero counts plus the two `None` values.

For the supplied sample, the result is:

```python
{
    "total_trials": 5,
    "answered_trials": 4,
    "omission_trials": 1,
    "correct_trials": 3,
    "accuracy": 0.75,
    "mean_correct_rt_ms": 533.3,
}
```

## Workflow and submission

1. Copy `starter.py` to `submission.py`.
2. Predict the first failure, then run the program.
3. Repair the implementation without changing the required function names or return keys.
4. Run `python public_check.py submission.py` from this folder.
5. Add at least two small assertions of your own to `submission.py`. At least one must cover an edge case not present in the sample data.
6. Complete [`response.md`](response.md).
7. Submit `submission.py` and `response.md` through Moodle. Do not open a public pull request with your answer.

Passing the public checker is necessary but not sufficient. The instructor will use additional synthetic cases and the short demonstration.

## Individual demonstration

The instructor will select one small adjacent change or tracing prompt. Examples include:

- add `incorrect_answered_trials` without changing existing results;
- add `accuracy_percent` while preserving the required proportion;
- trace one supplied trial and explain how each accumulator changes;
- predict, run, and explain an all-omission or no-correct case;
- diagnose a deliberately reintroduced denominator defect.

The objective is not speed typing. You may use the same tools. The evidence is that you can orient yourself, explain the relevant state, make or direct a bounded change, and verify what happened.
