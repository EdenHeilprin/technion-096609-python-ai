# Class 11 — From Research Method to Implementation Specification

A research method describes what a study is intended to do. A reliable implementation also needs precise behavior, interpretable output fields, and evidence that the result follows the method. Today you will connect those pieces before building a larger research project.

## By the end of class

You should be able to:

- distinguish a source-method fact from a local implementation decision and an unresolved question;
- translate method prose into ordered program behavior;
- define the unit of observation and fields in a data contract;
- connect requirements to exact acceptance checks and evidence;
- recognize which claims can be checked from a CSV and which need code tests or direct observation;
- describe a thin vertical slice that connects one input to one checked output;
- use Codex to audit traceability across several project files without asking it to invent missing details.

## Get the files for this class

1. [Download the Class 11 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-11-method-to-specification/class-11/class-11-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-11`. On Windows, it may appear inside an additional folder named `class-11-files`.
3. Move `class-11` into your local course folder, next to `class-00-setup` through `class-10`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-11`.

If your course folder already contains `class-11`, you do not need to download it again.

## Rehearsal — recover the pandas sequence

Create a new Python file inside `class-11` named `class_11_rehearsal.py`. Begin with this supplied setup:

```python
from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "pilot_trials.csv"
```

The three lines below are out of order. Put them in an order that loads the data, keeps completed trials, and then counts completed trials in each condition.

```python
completed = trials.loc[trials["timed_out"] == False].copy()
trials = pd.read_csv(data_path)
print(completed.groupby("condition").size())
```

Write the ordered lines beneath the supplied setup, predict the output, and run the file before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
from pathlib import Path

import pandas as pd


data_path = Path(__file__).parent / "data" / "pilot_trials.csv"

trials = pd.read_csv(data_path)
completed = trials.loc[trials["timed_out"] == False].copy()
print(completed.groupby("condition").size())
```

```text
condition
risky_first    7
sure_first     4
dtype: int64
```

</details>

## Four ideas to recognize

### 1. A method is not yet an implementation specification

A method may state that trials are randomized or that response time is recorded. Code still needs exact labels, steps, missing-value rules, units, and stopping behavior.

When moving from a method to code, separate three categories:

| Category | Meaning | Example |
| --- | --- | --- |
| Method fact | The source explicitly requires it | Each participant remains in one display condition |
| Implementation decision | A precise local choice that preserves the method | Store the conditions as `sure_first` and `risky_first` |
| Unresolved question | The source does not provide enough information | What should happen after an invalid key press? |

An implementation decision should be visible and documented. An unresolved question should remain marked as unresolved rather than being silently guessed.

### 2. A data contract defines what every row and field means

A **data contract** begins with the unit of observation:

> One row represents one participant completing, or timing out on, one decision trial.

It then defines each field's meaning, allowed values, and missing-value rule. This prevents a technically valid CSV from becoming scientifically ambiguous.

### 3. An acceptance check needs observable evidence

“Randomization works” is not an exact check. An acceptance check states what will be inspected:

- every participant has each trial identity exactly once;
- a timed-out row has no selected key, choice, or response time;
- a known random seed produces an expected trial order in a test;
- direct observation confirms that no option begins selected.

Different requirements need different evidence. One small CSV can establish internal relationships in its recorded rows, but it cannot prove how the program generated those rows.

### 4. A thin vertical slice crosses the complete path

A **thin vertical slice** is the smallest working path from input to checked output. For an experiment, it might use one fixed participant and one fixed trial, accept one response, save one row, and validate that row.

It does not contain every feature. Its value is that the participant-facing behavior, stored data, and verification already connect end to end.

## Activity 1 — separate facts, decisions, and questions

Read [`methods/choice_order_method.md`](methods/choice_order_method.md). Classify each statement before opening the answer:

1. Every participant completes four trials.
2. The CSV stores response time in milliseconds.
3. A timed-out response is represented by three empty cells.
4. The same option-order condition applies to all trials for one participant.
5. An invalid key is ignored while the original 12-second timer continues.
6. The stored condition labels are `sure_first` and `risky_first`.

Use only these labels: **method fact**, **implementation decision**, or **unsupported until clarified**.

<details>
<summary>Check the classifications</summary>

| Statement | Classification | Reason |
| --- | --- | --- |
| 1 | Method fact | The method explicitly states four trials |
| 2 | Implementation decision | The method requires response time but does not state its stored unit |
| 3 | Implementation decision | The method requires timeout records but not their CSV representation |
| 4 | Method fact | The method explicitly keeps condition fixed within participant |
| 5 | Unsupported until clarified | The method identifies invalid-key behavior as unresolved |
| 6 | Implementation decision | These exact machine-readable labels are locally chosen |

</details>

Now open [`specification/implementation_spec.md`](specification/implementation_spec.md). Locate the separate sections that preserve these distinctions. Find one decision that improves the interpretability of a later analysis even though the participant never sees it.

<details>
<summary>Check one strong answer</summary>

The specification stores both `selected_key` and `choice`. The raw key preserves what the participant pressed; the semantic choice preserves whether that key meant `sure` or `risky` under the current display order.

</details>

## Activity 2 — inspect a data contract and challenge it with an error

Read [`specification/data_contract.md`](specification/data_contract.md) before opening the CSV files. Predict:

1. how many rows one participant should have;
2. which fields should be missing on a timed-out trial;
3. what `option_1` should contain for a participant in `risky_first`;
4. whether key `1` always means `sure`.

Open and run [`inspect_pilot.py`](inspect_pilot.py). Connect each printed result to the contract rather than judging the file from appearance alone.

<details>
<summary>Check the central inspection results</summary>

- The table has 12 rows and 9 columns.
- Each of the three participant codes has four rows.
- Each participant has exactly one condition value.
- One timed-out row creates one missing value in each of `selected_key`, `choice`, and `response_time_ms`.
- Key `1` means whichever semantic option appears first; it does not always mean `sure`.

</details>

Next, inspect [`validate_pilot.py`](validate_pilot.py). You do not need to memorize every pandas expression. For each assertion, state the contract rule it checks.

The `DATA_FILENAME` line initially selects [`data/pilot_trials.csv`](data/pilot_trials.csv). Run the script before making any change. It should finish with:

```text
File: pilot_trials.csv
Rows: 12
Participants: 3
All contract checks passed
```

Now change only the filename at the top of the script:

```python
DATA_FILENAME = "pilot_trials_with_error.csv"
```

Predict which contract relationship will fail, then run the script again. Read the final line of the traceback and use it to locate the row. Restore `pilot_trials.csv` and confirm that all checks pass before continuing.

<details>
<summary>Check the failed assertion</summary>

```text
AssertionError: P003 T04: option_1 should be risky for condition risky_first
```

Participant `P003` is assigned to `risky_first`, but the flawed file records `sure` as option 1 on trial `T04`. Every individual value looks permissible; the relationship between fields is wrong.

</details>

## Activity 3 — audit traceability with Codex

Open the `class-11` folder as a Codex project and select **Read only**. Send:

> Inspect `methods/choice_order_method.md`, `specification/implementation_spec.md`, `specification/data_contract.md`, and `validate_pilot.py` without editing. Build a traceability table with four columns: method requirement, specification decision or output field, exact executable check, and evidence to inspect. Then identify (1) one requirement that cannot be established from a small pilot CSV alone and (2) the unresolved method question. Do not fill missing details or propose new requirements.

Review the response against the four files. In particular, reject any answer that treats an observed trial order as proof that the program randomized it.

<details>
<summary>What a sound audit should distinguish</summary>

- The CSV checks can establish row counts, allowed labels, within-participant consistency, trial coverage, display positions, key-to-choice mapping, timeout missingness, and response-time bounds.
- A small pilot CSV cannot establish that equal-probability assignment or randomized ordering was actually generated by the intended mechanism. Those claims need implementation inspection and controlled tests.
- The CSV also cannot show when the timer began or whether the interface initially displayed no selection; those claims need direct observation or interface-level tests.
- Invalid-key behavior remains unresolved and should not be invented.

</details>

Choose one row from Codex's traceability table and verify every cell yourself. Name the exact source sentence, specification statement, assertion, and observed report that support it.

## Activity 4 — draft a bounded specification

Open [`specification/specification_template.md`](specification/specification_template.md) and save a copy inside `class-11` as `my_specification.md`.

Choose one case:

- **Decision-making experiment:** use the option-order method and worked specification, then restate the smallest end-to-end slice in your own precise terms.
- **Survey plus Python:** read [`methods/survey_transfer_case.md`](methods/survey_transfer_case.md) and specify its first end-to-end data-processing slice.

Complete every section of the template:

- three source-method facts;
- three local implementation decisions;
- one unresolved question;
- one thin vertical slice connecting input, behavior, saved output, and a check;
- a unit of observation and at least five fields;
- three requirements with exact checks and evidence.

Exchange the file with a partner. The reviewer should mark any sentence that silently changes a source fact, presents a local choice as if it came from the method, or uses a vague check such as “make sure it works.” Revise those sentences before saving the file.

## Class 11 reference

| Term | Simple meaning |
| --- | --- |
| Source-method fact | A requirement explicitly supported by the method description |
| Implementation decision | A precise local choice needed to build or store the procedure |
| Unresolved question | A detail that available evidence does not answer |
| Implementation specification | A precise description of intended program behavior and outputs |
| Unit of observation | What one row represents |
| Data contract | The expected fields, meanings, values, types, and missing-value rules |
| Invariant | A relationship that should remain true, such as one condition per participant |
| Acceptance check | A specific test or inspection used to judge one requirement |
| Evidence | The file, output, test result, or observation that supports a claim |
| Traceability | A visible connection from source requirement to implementation and verification |
| Thin vertical slice | The smallest working path from an input through behavior to a checked output |

### Reusable planning sequence

```text
Read the method
    ↓
Separate facts, decisions, and unresolved questions
    ↓
Describe ordered behavior
    ↓
Define the unit of observation and data contract
    ↓
Connect every requirement to a check and evidence
    ↓
Build one thin end-to-end slice
```

## Companion tutorial

Watch Khan Academy's 3:27 **[Planning with pseudo-code](https://www.youtube.com/watch?v=4S5ckWkMnMU)**.

It demonstrates how to begin with the behavior a program should perform, write those steps in ordinary language, and then translate one step at a time into code. The example uses JavaScript drawing commands, but the planning method applies directly here. JavaScript comments begin with `//`; Python comments begin with `#`.
