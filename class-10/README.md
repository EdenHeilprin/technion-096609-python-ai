# Class 10 — Transforming, Summarizing, and Visualizing Data

Class 9 established what a trial-data file contains. Today you will turn a synthetic decision-making export into a small reproducible analysis: define the rows that answer the question, create a derived bonus column, summarize the completed trials by condition, and save both tables and a plot.

## By the end of class

You should be able to:

- create and inspect a Boolean mask;
- filter DataFrame rows with `.loc` without changing the raw data;
- select the columns needed for an analysis;
- create a new column from an existing numeric column;
- use `groupby()` to calculate summaries for each condition;
- create and label a simple bar chart;
- save cleaned data, a summary table, and a plot;
- verify that the pipeline kept the intended trials and produced the intended files;
- use docstrings and comments to explain a program's purpose and non-obvious decisions;
- use Codex to audit a plausible filtering rule, then verify its diagnosis against the data and executed output.

## Get the files for this class

1. [Download the Class 10 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-10-transformations/class-10/class-10-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-10`. On Windows, it may appear inside an additional folder named `class-10-files`.
3. Move `class-10` into your local course folder, next to `class-00-setup` through `class-09`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-10`.

If your course folder already contains `class-10`, you do not need to download it again.

## Prepare the two packages

Open and run [`check_packages.py`](check_packages.py). The final lines should be:

```text
pandas is ready: 3.0.5
matplotlib is ready: 3.11.1
```

If either package is not ready, open and run [`install_packages.py`](install_packages.py) with the same VS Code Run button. When it finishes, run `check_packages.py` again.

The installer uses the Python interpreter selected in VS Code, so no operating-system-specific path is required. If it reports an error, use the short [package setup troubleshooting guide](package-troubleshooting.md).

## Documentation helps readers follow longer code

The activity files are now long enough that names and syntax alone do not explain every research decision.

- A **module docstring** appears at the top of a Python file and states the file's purpose.
- A **function docstring** appears inside a function and states its contract.
- A **comment** begins with `#` and explains a decision that would otherwise be unclear.

Open [`filter_completed.py`](filter_completed.py). Its docstring states the script's overall purpose. The comment above `completed_mask` records why response time—not points—defines completion. Neither annotation narrates obvious syntax.

The short [`documentation guide`](DOCUMENTATION_GUIDE.md) gives examples and a standard to reuse when you or an AI tool documents a program.

## Rehearsal — reload and inspect the trial table

Create a new Python file inside `class-10` named `class_10_rehearsal.py`. Begin with this supplied path setup:

```python
from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "decision_trials.csv"
```

Then write three lines from memory that:

1. load the CSV file into a DataFrame named `trials`;
2. print its shape;
3. print the missing-value count for every column.

Run the file before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "decision_trials.csv"

trials = pd.read_csv(data_path)
print(trials.shape)
print(trials.isna().sum())
```

The shape is `(12, 6)`. The `choice` and `response_time_ms` columns each contain two missing values.

</details>

## Begin with the analytical question

The file [`data/decision_trials.csv`](data/decision_trials.csv) contains 12 synthetic trials from two experimental conditions. Two trials timed out. One completed trial earned zero points.

Our question is:

> Among completed trials, what are the mean response time, points, and trial-level bonus payment for each condition?

For this class, a **completed trial** means a trial with a recorded response time. That definition—not a convenient-looking value—determines which rows belong in the analysis.

The raw CSV is the record of what was collected. The scripts will read it but never overwrite it. Filtered and summarized results will be stored as new objects and new files.

## A Boolean mask selects rows

This expression checks every value in one column:

```python
completed_mask = trials["response_time_ms"].notna()
```

The result is a pandas **Series** containing one Boolean value for every row:

- `True` means that the response time is present;
- `False` means that it is missing.

The mask can select the rows where the condition is `True`:

```python
completed_trials = trials.loc[completed_mask].copy()
```

- `.loc[...]` selects rows by the supplied condition.
- `.copy()` creates an independent DataFrame for the analysis.
- `trials` still refers to all 12 raw rows.

## Activity 1 — keep the completed trials

Open [`filter_completed.py`](filter_completed.py). Before running it, predict:

1. how many values in `completed_mask` are `True`;
2. how many rows remain in `completed_trials`;
3. whether the raw `trials` DataFrame changes shape.

Run the file.

<details>
<summary>Check the output</summary>

```text
Raw rows: 12
Completed rows: 10
Timed-out rows: 2
Missing response times after filtering: 0
```

The raw DataFrame still has 12 rows. Filtering created a separate 10-row DataFrame; it did not delete anything from the source CSV or from `trials`.

</details>

Change `.notna()` to `.isna()` and predict the four displayed numbers. Run the file, then restore `.notna()` and rerun it successfully.

## A plausible filter can still encode the wrong rule

The two timed-out rows happen to have zero points, so this shortcut may look reasonable:

```python
positive_point_trials = trials.loc[trials["points"] > 0].copy()
```

But points and completion do not mean the same thing. A participant can complete a trial and earn zero points.

## Activity 2 — audit the filtering rule

Open [`audit_filter.py`](audit_filter.py). Inspect the two filters and predict whether they keep the same rows. Then run the file.

<details>
<summary>Check the central result</summary>

```text
Completed by response time: 10
Rows with positive points: 9

Completed zero-point trials:
participant_code  trial_number  points
            P003             1       0
```

The positive-points shortcut wrongly removes participant `P003`'s first trial even though that trial has a recorded response time.

</details>

Open the `class-10` folder as a Codex project and select **Read only**. Send:

> Inspect `data/decision_trials.csv` and `audit_filter.py` without editing. The analysis defines a completed trial as one with a recorded response time. Compare that rule with the `points > 0` shortcut. Identify the exact completed row that the shortcut loses, explain why it is lost, and name the printed output that verifies each claim.

Check the response against the CSV and the output you ran. The useful answer is the one supported by those two sources of evidence.

## Select columns and create a derived column

An analysis table often keeps only the variables needed for its question:

```python
analysis = completed_trials.loc[
    :, ["participant_code", "trial_number", "condition", "response_time_ms", "points"]
].copy()
```

Inside `.loc[rows, columns]`, the colon means **all rows** and the list names the columns to keep.

Suppose every point is worth ILS 0.05. This line creates a new value for every analysis row:

```python
analysis["bonus_payment_ils"] = (analysis["points"] * 0.05).round(2)
```

pandas applies the multiplication to the entire `points` column. A separate Python loop is not needed.

## Summarize “for each condition”

`groupby()` is useful when the question can be phrased as **for each group**. Here the group is `condition`.

```python
summary = analysis.groupby("condition", as_index=False).agg(
    completed_trials=("trial_number", "count"),
    mean_response_time_ms=("response_time_ms", "mean"),
    mean_points=("points", "mean"),
    mean_bonus_payment_ils=("bonus_payment_ils", "mean"),
)
```

The named summaries inside `.agg()` follow one pattern:

```text
new_column_name=(source_column, calculation)
```

`as_index=False` keeps `condition` as an ordinary column in the resulting DataFrame. `.round(2)` can then make the displayed numeric results easier to read.

## Activity 3 — derive and summarize

Open [`derive_and_summarize.py`](derive_and_summarize.py). Before running it, predict:

1. how many rows the analysis table contains;
2. how many rows the condition summary contains;
3. which condition has the larger mean points value.

Run the file and inspect both tables.

<details>
<summary>Check the condition summary</summary>

```text
condition  completed_trials  mean_response_time_ms  mean_points  mean_bonus_payment_ils
    bonus                 5                  830.6          6.4                    0.32
  control                 5                 1006.2          4.4                    0.22
```

The summary has one row for each of the two conditions. These numbers describe the supplied synthetic trials; they are not a statistical test.

</details>

Temporarily change `groupby("condition", ...)` to `groupby("participant_code", ...)`. Predict how many summary rows will appear, run the file, and then restore `condition`.

## A plot turns one summary into a visual comparison

pandas can pass a DataFrame summary to matplotlib:

```python
axis = summary.plot.bar(
    x="condition",
    y="mean_points",
    legend=False,
)
```

The chart should state what its axes represent:

```python
axis.set_xlabel("Condition")
axis.set_ylabel("Mean points per completed trial")
```

The figure can be saved as a PNG file before it is displayed:

```python
figure = axis.get_figure()
figure.savefig(plot_path, dpi=150)
```

## Activity 4 — run and verify the complete pipeline

Open [`build_analysis.py`](build_analysis.py). Trace the script from its source path to its three output paths. Identify the assertions that check:

- the raw row count;
- the completed row count;
- the expected conditions and summary size;
- the reloaded output tables;
- the saved plot file.

Run the script. A plot window should open. Close it after inspecting the title, axes, and two bars. If no plot window appears, open `output/mean_points_by_condition.png` in VS Code instead.

The terminal should include:

```text
Analysis rows: 10
Summary rows: 2
Saved: cleaned_trials.csv
Saved: condition_summary.csv
Saved: mean_points_by_condition.png
All pipeline checks passed
```

Open the `output` folder in VS Code and inspect all three files. Run the script a second time. The same checked outputs should be replaced, not duplicated.

<details>
<summary>What the complete pipeline preserves</summary>

- `data/decision_trials.csv` remains unchanged with 12 rows.
- `cleaned_trials.csv` contains the 10 completed trials and the derived bonus column.
- `condition_summary.csv` contains one row for `bonus` and one for `control`.
- `mean_points_by_condition.png` visualizes the summary's `mean_points` column.
- Reloading both CSV outputs reproduces their expected rows and columns.

</details>

### Ask Codex to document the complete pipeline

Open the `class-10` folder as a Codex project, select **Auto**, and send:

> Read `DOCUMENTATION_GUIDE.md` and `build_analysis.py`. First explain the script's data flow in order. Then add documentation only: (1) a short module docstring naming the input, the three outputs, and the script's purpose; and (2) concise comments for the completed-trial rule, bonus derivation, grouped summary, saved artifacts, and reload checks. Explain research decisions and verification—not obvious Python syntax. Do not refactor, rename, or change behavior. Show the diff, run the script, and confirm that the same three output files are created and all assertions pass.

Review the diff before accepting it. Every added line should improve understanding; no executable line should change. Then run `build_analysis.py` yourself and verify the same terminal output and three saved files.

<details>
<summary>Check the kind of documentation we want</summary>

Useful annotations include:

```python
"""Build checked analysis tables and a plot from data/decision_trials.csv.

Outputs: cleaned_trials.csv, condition_summary.csv, and
mean_points_by_condition.png.
"""

# Completion is defined by a recorded response time, so completed zero-point
# trials remain in the analysis.
```

Avoid comments such as `# import pandas`, `# make a DataFrame`, or `# print rows`; they repeat syntax without explaining a decision.

</details>

## Class 10 reference

### Central terms

| Term | Simple meaning |
| --- | --- |
| Raw data | The original recorded data, preserved without overwriting |
| Analysis rule | A substantive definition that determines which data answer the question |
| Boolean mask | One `True` or `False` value for every DataFrame row |
| Filter | A selection that keeps rows meeting a stated condition |
| Series | A one-dimensional pandas object; one DataFrame column is a Series |
| `.loc` | A pandas selector for rows and columns by labels or a Boolean condition |
| `.copy()` | Creates an independent DataFrame from a selection |
| Derived column | A new column calculated from existing values |
| Vectorized operation | One pandas expression applied across a column without an explicit Python loop |
| Group | Rows sharing a category value, such as one experimental condition |
| Aggregation | A calculation that reduces several values to a summary, such as count or mean |
| `groupby()` | Splits rows into groups so a calculation can be performed for each group |
| Plot | A visual representation of selected data or a summary |
| Pipeline | A repeatable sequence from input data through transformations to checked outputs |
| Documentation | Explanatory text that records purpose, contracts, decisions, or limitations |
| Module docstring | A description at the top of a Python file stating its purpose and important inputs or outputs |
| Function docstring | A concise contract immediately inside a function |
| Comment | Explanatory text after `#` that Python does not execute |

### Reusable transformation sequence

```python
trials = pd.read_csv(data_path)

completed_mask = trials["response_time_ms"].notna()
completed_trials = trials.loc[completed_mask].copy()

analysis = completed_trials.loc[:, required_columns].copy()
analysis["bonus_payment_ils"] = (analysis["points"] * 0.05).round(2)

summary = analysis.groupby("condition", as_index=False).agg(
    completed_trials=("trial_number", "count"),
    mean_points=("points", "mean"),
)
```

The syntax matters, but the decisions come first: define the relevant rows, preserve the raw data, name the required columns, state each derived quantity, and verify the resulting tables.

## Companion tutorial

Watch Microsoft Developer's 3:33 **[How to Analyze and Clean a Dataset](https://www.youtube.com/watch?v=5qGjczWTrDQ)**.

It begins with an analytical question, then filters relevant rows, checks missingness, removes unrelated columns, and creates derived columns. This class applies the same reasoning to synthetic decision-making trials and continues through grouped summaries, saved tables, and a checked plot.
