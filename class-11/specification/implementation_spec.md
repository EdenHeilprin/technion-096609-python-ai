# Worked implementation specification

## Purpose

Implement the synthetic option-order method in a way that preserves its experimental logic and produces interpretable trial-level data.

## Method facts that the implementation must preserve

- A participant is assigned once to either sure-first or risky-first, with equal probability.
- The same condition applies to all four trials for that participant.
- Each participant sees all four trials in a newly randomized order.
- Condition determines which semantic option appears as option 1.
- The participant responds with key `1` or `2`; no option begins selected.
- A trial ends after a valid response or after 12 seconds.
- Every trial produces a trial-level record, including timeouts.

## Local implementation decisions

- Store the condition as `sure_first` or `risky_first`.
- Store response time in milliseconds.
- Store both the raw selected key and its semantic meaning, `sure` or `risky`.
- Represent a timeout with `timed_out=True` and missing values for selected key, choice, and response time.
- Store one CSV row per participant-trial observation.
- Use the field names and rules in [`data_contract.md`](data_contract.md).

These choices are not claims about the original method. They make the method precise enough to implement and inspect.

## Program behavior

For each participant, the eventual program should:

1. create an anonymous participant code;
2. assign one option-order condition;
3. create a randomized order containing all four trial identities once;
4. display each trial according to the assigned condition;
5. translate key `1` or `2` into the semantic choice shown in that position;
6. record either a completed response or a timeout;
7. append one row that follows the data contract.

## Acceptance checks

A saved pilot file should satisfy all of these checks:

- the exact required columns are present;
- every participant has four rows and one condition;
- each participant has trials `T01` through `T04` exactly once;
- each participant has display positions 1 through 4 exactly once;
- `option_1` agrees with the participant's condition;
- key `1` and key `2` map to the correct semantic choice;
- completed trials have a valid key, choice, and response time;
- timed-out trials have none of those three response values;
- every completed response time is greater than 0 and at most 12000 milliseconds.

## Checks that need more than one pilot CSV

A small output file can show that the recorded rows are internally consistent. It cannot by itself establish that:

- condition assignment actually uses the intended random mechanism;
- trial order is generated randomly rather than copied from a fixed list;
- the timer starts when both options become visible;
- the interface begins with no option selected.

Those requirements need additional evidence: inspect the implementation, run controlled tests with known random seeds, and observe the interface directly.

## Unresolved question

The method does not specify what should happen after an invalid key press. That behavior must be clarified before the full implementation is treated as complete.

## First thin vertical slice

Before implementing random assignment, all four trials, and timeouts, build one end-to-end path:

1. use one fixed synthetic participant, condition, and trial;
2. display both options in the required order;
3. accept one valid key;
4. translate the key into `sure` or `risky`;
5. save one contract-compliant row;
6. run checks on that saved row.

This slice is deliberately incomplete, but it connects the participant-facing behavior to a checked data artifact. Later work can add one requirement at a time without losing that complete path.
