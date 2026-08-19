# Class 9 — Files, CSV, and Your First pandas DataFrame

Experiment data must remain available after a Python program stops. Today you will locate a CSV file reliably, load synthetic trial records into pandas, inspect the resulting table, and save a checked copy without adding unwanted rows or columns.

## By the end of class

You should be able to:

- distinguish a file, a folder, and a path;
- recognize the header, rows, columns, and cells of a CSV file;
- build a path to a data file stored beside your Python program;
- load a CSV file into a pandas `DataFrame`;
- inspect its first rows, shape, column names, data types, and missing values;
- distinguish a CSV file on disk from a `DataFrame` in memory;
- write a `DataFrame` to a CSV file and verify the saved result;
- use Codex to audit file and data assumptions, then check its report against executed output.

## Get the files for this class

1. [Download the Class 9 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-09-csv-pandas/class-09/class-09-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-09`. On Windows, it may appear inside an additional folder named `class-09-files`.
3. Move `class-09` into your local course folder, next to `class-00-setup` through `class-08`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-09`.

If your course folder already contains `class-09`, you do not need to download it again.

## Check pandas once

Open and run [`check_pandas.py`](check_pandas.py). The final line should be:

```text
pandas is ready: 3.0.5
```

If pandas is missing or the displayed version is different, open **Terminal → New Terminal** in VS Code and run the command for your operating system:

**Windows**

```text
py -3.13 -m pip install --upgrade pandas==3.0.5
```

**macOS**

```text
/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13 -m pip install --upgrade pandas==3.0.5
```

When the command finishes, close the terminal and run `check_pandas.py` again.

If the command reports `externally-managed-environment`, use the short [local-environment fallback](pandas-environment.md).

## Rehearsal — reconstruct one trial record

Create a new Python file inside `class-09` named `class_09_rehearsal.py`. Write these three instructions from memory:

1. store a dictionary named `trial` whose choice is `"left"` and whose points are `8`;
2. print the stored choice;
3. assert that the stored points equal `8`.

Run the file. Try to reconstruct it before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
trial = {"choice": "left", "points": 8}

print(trial["choice"])
assert trial["points"] == 8
```

The displayed output is:

```text
left
```

The successful assertion is silent.

</details>

## From one dictionary to a table of trials

A dictionary can represent one trial while a Python program is running. An experiment normally produces many trial records that must still exist after the program ends.

The file [`data/trial_results.csv`](data/trial_results.csv) stores synthetic results from four participants. Open it in VS Code as ordinary text. Its first lines are:

```text
participant_code,trial_number,condition,choice,response_time_ms,points
P001,1,control,left,842,6
P001,2,control,right,1104,4
```

CSV means **comma-separated values**. In this file:

- the first line is the **header** and supplies the column names;
- every later line is one **row** representing one participant's trial;
- commas separate the **columns**;
- one value at the intersection of a row and column is a **cell**.

The file contains synthetic codes rather than names. Two timed-out trials have empty `choice` and `response_time_ms` cells; those blanks are meaningful data to detect, not lines to ignore.

## A path identifies a location

A **folder** can contain files and other folders. A **path** describes how to reach one of those locations.

These lines build a path from the current Python file to the CSV file inside its neighboring `data` folder:

```python
from pathlib import Path

class_folder = Path(__file__).parent
data_path = class_folder / "data" / "trial_results.csv"
```

- `Path` is supplied by Python's `pathlib` library.
- `__file__` means the path of the Python file currently running.
- `.parent` gives the folder containing that file.
- `/` joins the folder and names into a new path.

You do not need to memorize this pattern today. You should be able to recognize what location it constructs and reuse it when a script needs a nearby file.

## Activity 1 — locate the trial file

Open [`path_demo.py`](path_demo.py). Before running it, use the folder tree in VS Code to predict the three displayed values.

Run the file from VS Code.

<details>
<summary>Check the output</summary>

```text
Class folder: class-09
Data file: trial_results.csv
File exists: True
```

</details>

Temporarily change only the final filename in the path to `missing_results.csv` and run the file again. `File exists` should become `False`. Restore `trial_results.csv` before continuing.

The path starts from the location of `path_demo.py`, so it does not depend on which folder happened to be active in the terminal.

## pandas turns a CSV file into a DataFrame

**pandas** is a Python library for working with tabular data. The conventional import is:

```python
import pandas as pd
```

`pd` is an **alias**: a shorter name used to refer to pandas in the current file.

The following line loads the CSV file:

```python
trials = pd.read_csv(data_path)
```

`pd.read_csv()` reads the file and returns a **DataFrame**—pandas's table-like structure with labeled rows and columns. The variable `trials` refers to that DataFrame while the program is running. It is not the original file itself.

Two useful first inspections are:

```python
print(trials.head())
print(trials.shape)
```

- `.head()` returns the first five rows by default.
- `.shape` gives `(number_of_rows, number_of_columns)`.

## Activity 2 — load and inspect the first rows

Open [`load_trials.py`](load_trials.py). Before running it, answer:

1. Which file will `pd.read_csv()` open?
2. What does one row represent?
3. How many columns should the DataFrame contain?

Run the file. Use the output to check your answers.

<details>
<summary>Check the central results</summary>

- The file is `data/trial_results.csv` inside `class-09`.
- One row represents one trial completed or timed out by one synthetic participant.
- The DataFrame has 12 rows and 6 columns, so its shape is `(12, 6)`.
- `.head()` shows only the first five rows; it does not remove the other seven.

</details>

Change `trials.head()` to `trials.head(3)`, predict the visible difference, and run the file again. Restore the original call afterward.

## Inspect structure before analyzing values

The first rows show examples, but they do not establish the complete structure. These expressions answer different questions:

| Expression | What it reveals |
| --- | --- |
| `trials.shape` | Number of rows and columns |
| `list(trials.columns)` | Column names in order |
| `trials.dtypes` | The data type pandas assigned to each column |
| `trials.isna().sum()` | Number of missing cells in each column |

`trials.isna()` marks every missing cell as `True`. The following `.sum()` counts those `True` values separately for each column.

A numeric column containing blanks may be displayed as `float64` even when its recorded values look like whole milliseconds. pandas needs a representation that can hold both numbers and missing values.

## Activity 3 — audit the DataFrame and its assumptions

Open [`inspect_trials.py`](inspect_trials.py). Predict which columns contain missing values before running it. Then run the file and record:

1. the DataFrame shape;
2. the six column names;
3. the data type assigned to `response_time_ms`;
4. every column with one or more missing values;
5. the number of missing cells in each of those columns.

<details>
<summary>Check the inspection</summary>

- Shape: `(12, 6)`
- Columns: `participant_code`, `trial_number`, `condition`, `choice`, `response_time_ms`, `points`
- `response_time_ms` is `float64` because the column contains numeric values and blanks.
- `choice` has 2 missing cells.
- `response_time_ms` has 2 missing cells.
- The other four columns have 0 missing cells.

</details>

Open the `class-09` folder as a Codex project and select **Read only**. Send:

> Inspect `data/trial_results.csv` and `inspect_trials.py` without editing. Report (1) what one CSV row represents, (2) the file path assumed by the script, (3) the exact column names, (4) the columns containing blank values and their counts, and (5) which printed inspection result verifies each answer. Do not clean or rewrite anything.

Compare the report with the CSV text and the output you executed. Correct any claim that does not match that evidence.

## Save a checked copy safely

A DataFrame exists in memory only while the Python process is running. The `.to_csv()` method writes it to a file:

```python
trials.to_csv(output_path, index=False)
```

`index=False` prevents pandas's row labels (`0`, `1`, `2`, and so on) from becoming an extra CSV column.

The output folder can be prepared safely with:

```python
output_folder.mkdir(exist_ok=True)
```

If the folder already exists, `exist_ok=True` allows the program to continue. Writing repeatedly to the same output path replaces that file with the current table rather than appending another copy of all rows.

## Activity 4 — write, reload, and verify

Open [`export_trials.py`](export_trials.py). Before running it, identify:

- the source CSV path;
- the output CSV path;
- the two properties checked by the assertions.

Run the file twice. Both runs should display:

```text
Saved rows: 12
Saved columns: 6
Output file: checked_trial_results.csv
```

Open `output/checked_trial_results.csv` in VS Code. It should have the same six-column header and 12 data rows as the source file—not 24 rows and not an extra column of row numbers.

Now temporarily remove `index=False` from the `.to_csv()` call and run the file. The column assertion should fail because the saved file now contains an extra first column. Inspect the output CSV, restore `index=False`, and rerun the file to return to the checked result.

<details>
<summary>Why the assertions are useful</summary>

```python
assert list(saved_trials.columns) == list(trials.columns)
assert saved_trials.shape == trials.shape
```

The first assertion checks that reloading the output produces the same number of rows and columns. The second checks the exact column names and order. Together they expose an unwanted saved index column.

</details>

## Class 9 reference

### Central terms

| Term | Simple meaning |
| --- | --- |
| File | A named collection of stored information, such as a Python program or CSV table |
| Folder | A location that groups files and possibly other folders |
| Path | A description of how to reach a file or folder |
| CSV | A plain-text table whose values are separated by commas |
| Header | The first CSV row that supplies column names |
| Row | One horizontal record; here, one participant's trial |
| Column | One named kind of information repeated across rows |
| Cell | One value at a row-column intersection |
| Library | Reusable code that can be imported into a Python program |
| pandas | A Python library for tabular data work |
| Alias | A shorter local name for an imported library; `pd` refers to pandas |
| DataFrame | pandas's table-like structure in memory |
| Data type or dtype | pandas's representation of the values in one column |
| Missing value | A cell for which no value was recorded |
| Index | pandas's labels for DataFrame rows |
| Rerun safety | Repeating a program produces a valid current result rather than unintended accumulation |

### File on disk and DataFrame in memory

| CSV file | DataFrame |
| --- | --- |
| Stored on disk | Exists in Python memory while the program runs |
| Plain text | pandas object with rows, columns, labels, and methods |
| Loaded with `pd.read_csv(path)` | Saved with `dataframe.to_csv(path, index=False)` |

### Reusable inspection sequence

```python
print(trials.head())
print(trials.shape)
print(list(trials.columns))
print(trials.dtypes)
print(trials.isna().sum())
```

Inspect the structure before calculating summaries or changing values. A successful file load does not guarantee that the row count, column names, types, or missingness match your expectations.

## Companion tutorial

Watch Microsoft Developer's 3:44 **[Introducing DataFrame](https://www.youtube.com/watch?v=SdlaYzocgHg)**.

It reinforces why data inspection comes before analysis and demonstrates `.head()`, `.tail()`, `.shape`, and `.info()`. This class applies that inspection logic to a local synthetic experiment CSV and adds explicit column and missing-value checks.
