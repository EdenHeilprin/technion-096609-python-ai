# Build milestones

Complete one milestone, inspect its diff, and verify it before beginning the next.

## Class 11

### Milestone 1 — one working trial

- Create a current oTree project in this folder with one app named `sampling_task`.
- Use the first row of `stimuli.csv` as one fixed trial.
- Add instructions, decision, and completion pages.
- Require five samples from each option before choice.
- Save sample counts, selected side, semantic choice, `decision_rt_ms`, and `trial_rt_ms`.
- Run locally and complete one manual browser pilot.

Do not add multiple rounds, conditions, timeout, bots, custom export, payment, or deployment.

### Milestone 2 — four trials and stored randomization

- Load and validate all four stimulus rows.
- Give every participant all four trial IDs exactly once in a randomized order that remains stable across rounds.
- Randomize and store the left-right mapping on every trial.
- Pre-generate and store five sample outcomes per option so a refresh does not create a different sequence.
- Store the lottery values and fields already required by `DATA_CONTRACT.md`.
- Complete and inspect one four-trial manual pilot.

Do not add feedback conditions, timeout, bots, or custom export.

### Milestone 3 — feedback manipulation

- Add the participant-level `persistent` and `transient` conditions.
- Add one ordinary random-condition session config and one forced config for each condition.
- Implement the two feedback behaviors exactly as specified.
- Store condition in every trial row.
- Manually pilot both forced configs and inspect their saved rows.

Do not add timeout, bots, custom export, payment, recruitment, or deployment.

## Class 12

### Milestone 4 — timeout and server-side integrity

- Add the 90-second timeout.
- Enforce completed-choice relationships on the server.
- Store explicit timeout state and clear side, choice, and timing fields after timeout.
- Show completed-trial count on the final page.

### Milestone 5 — automated pilots and curated export

- Add oTree bots for ordinary choices and one timeout case.
- Run bots under both forced-condition configs.
- Add the exact 21-column custom export in `DATA_CONTRACT.md`.
- Generate a synthetic export and validate its row-level relationships.

### Milestone 6 — documentation and release audit

- Add concise module and function docstrings.
- Add comments only for non-obvious research, data, timing, and verification decisions.
- Add a project README with setup, run, test, and export instructions.
- Run the complete automated and manual verification sequence.
- Report remaining limitations without adding new features.
