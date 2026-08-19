# Decision experiment build brief

## Purpose

Build a terminal prototype of the Class 11 option-order experiment. The prototype should connect condition assignment, trial order, participant input, trial-level CSV output, automated core tests, and independent output validation.

## Method facts to preserve

- Assign one participant to `sure_first` or `risky_first` with equal probability.
- Keep the assigned condition constant across all four trials.
- Present trials `T01` through `T04` once each in a newly randomized order.
- Display the sure option first in `sure_first` and the risky option first in `risky_first`.
- Accept key `1` or `2` as the response to the option in that position.
- End a trial after a valid response or after 12 seconds.
- Save one row for every completed or timed-out trial.

## Local implementation decisions

- Use fixed synthetic participant codes while developing.
- Use an integer seed so a session plan can be reproduced.
- Store response time in milliseconds.
- Store the raw key and the corresponding semantic choice.
- After an invalid key, show a neutral prompt and keep the original timer running.
- Write one CSV per synthetic participant inside an `output` folder.
- Re-running the same participant code replaces that participant's earlier pilot file.

## Known prototype limitation

Python's terminal `input()` waits until Enter is pressed, so this prototype cannot automatically advance at exactly 12 seconds.

- Pressing Enter without a key simulates no response.
- A key entered after 12 seconds is also stored as a timeout once input returns.
- A later experiment platform must implement and test the true automatic timeout and participant-facing interface.

This limitation concerns the terminal interface. The condition, ordering, key mapping, row construction, saving, and validation logic remain directly testable.

## Acceptance evidence

- `test_experiment_core.py` checks controlled condition, ordering, mapping, and row-building cases.
- `inspect_seeds.py` demonstrates repeatable session plans.
- Direct observation checks the terminal display and input sequence.
- `validate_output.py` reloads one saved pilot and checks the data contract.
