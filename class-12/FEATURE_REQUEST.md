# Feature request — record the random seed

The session's random seed is needed to reproduce its condition assignment and trial order. Add it to the project as follows:

- Add a required integer field named `random_seed` immediately after `participant_code` in the data contract and output column order.
- Store the session's actual seed in every trial row.
- Keep the seed constant across all rows for one participant.
- Update the core tests to check the new field.
- Update the saved-output validator to require a non-missing integer seed that is constant within the participant.

Do not change condition assignment, trial ordering, option display, response mapping, timeout behavior, filenames, or any other field.
