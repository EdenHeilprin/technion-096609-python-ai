# Experiment specification

## Purpose

Build a local oTree experiment in which participants sample outcomes from two lotteries and then choose one. The experiment compares two ways of displaying sampled outcomes.

This is a teaching and pilot build. It does not recruit participants, calculate real payment, or deploy to a public server.

## Participant flow

1. Show one instructions page.
2. Present four decision trials, one for each row of `stimuli.csv`.
3. On every trial, show one lottery on the left and one on the right.
4. Require exactly five samples from each option.
5. Enable the two choice buttons only after both sample counts reach five.
6. Record the choice and timing, then continue to the next trial.
7. Show a completion page after the fourth trial.

## Lottery data

`stimuli.csv` is the only source for the four lottery pairs. Each option has:

- a low outcome;
- a high outcome;
- the probability of the high outcome.

The loader must require the exact columns in the supplied file, exactly four unique non-empty trial IDs, numeric outcomes, a low outcome below its high outcome, and a high-outcome probability strictly between 0 and 1. Invalid data must raise a clear error.

## Randomization

- Assign each participant once to `persistent` or `transient` in the ordinary session config. Keep that assignment for all four rounds.
- Provide one forced session config for each condition so the behavior can be piloted directly.
- Shuffle the four trial IDs once for each participant and preserve the resulting order across rounds.
- Randomize the left-right mapping of Options A and B separately on every trial and store the mapping.
- Generate the five available outcomes for each option on the server before the page is shown. Store the sequences so refreshing the page does not silently generate different outcomes.

Equal numbers across conditions are not required for this small local build. The assignment mechanism and stored label must nevertheless be explicit and testable.

## Feedback conditions

### Persistent

After each sample, keep the complete revealed history for that option visible.

### Transient

After each sample, show only the newest outcome for 800 milliseconds. Disable both sample buttons during that interval. Then hide the outcome and re-enable any sample button that has not reached five samples.

The conditions change feedback display only. They do not change lottery values, sample limits, trial order rules, available outcomes, or choice rules.

## Timing

- `trial_rt_ms` measures milliseconds from the decision page becoming available until choice.
- `decision_rt_ms` measures milliseconds from the moment both options have five samples until choice.
- Class 12 adds a 90-second page timeout. A timed-out trial must be marked explicitly and must not be stored as either Option A or Option B.

## Completion and timeout

- A completed trial has five samples from each option and a valid left or right choice.
- After the Class 12 timeout milestone, a timed-out trial may contain partial sample counts but must have blank selected side, semantic choice, and response-time fields.
- The completion page reports how many of the four trials were completed without timeout.

## Output

The final Class 12 build must provide a curated trial-level export that follows `DATA_CONTRACT.md`. One row represents one participant in one trial.

## Out of scope

Do not add demographics, participant-entered identifiers, consent, real payments, bonuses, recruitment links, deployment, databases beyond oTree's local development database, additional conditions, serial sampling, representative sampling, rare-event classifications, or extra stimulus formats.
