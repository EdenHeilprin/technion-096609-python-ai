# Worked handoff — supplied reference

## Question and current state

How does gamble choice vary across guaranteed offers? The complete reference contains the `full-v1` six-round oTree task and a working descriptive analysis. The input and results in this example are entirely synthetic. This file describes the supplied reference, not changes made in your own session.

## Start and run

1. Open the class's `research-project` folder in VS Code. Follow the accompanying `SETUP.md` to create and select its Python environment. Run `check_environment.py`.
2. Run `run_experiment.py` for a local participant preview. Stop its server with Ctrl+C in the terminal afterward.
3. Check `analysis/settings.py`: `synthetic_choices.csv`, `Synthetic teaching example`, and `IS_SYNTHETIC = True` are the default source settings.
4. Run `analysis/inspect_data.py`, then `analysis/analyze_choices.py` with Run Python File. For the confidence extension, run `analysis/explore_confidence.py`.
5. Open the files under `outputs/synthetic_choices/`. Inspect the figure, `summary.json`, and the exclusion table together.

## Inclusion and checks

The analysis requires `full-v1` and six unique valid answered rounds per session/participant. Malformed or duplicate records stop processing; incomplete participants are excluded and listed. The default fixture yields 15 included of 16 fictional participants, 90 analyzed choices, and 46 gambles. The input is not overwritten, and its hash is recorded in the summary.

## Limitations and next task

Synthetic patterns do not establish human behavior. The implemented study uses fixed ascending offers, so offer and order are confounded. The participant-summary demonstration checkpoint adds a display after the last response; it does not change saved variables or the CSV contract.

A useful next step is to run the same analysis on an instructor-approved `full-v1` classroom export using the settings in the codebook. Keep actual responses and their derived files local. For a later experiment, plan an explicitly versioned counterbalanced offer order rather than changing the meaning of already collected rows.
