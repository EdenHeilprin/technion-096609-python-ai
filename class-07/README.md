# Class 7 — Debugging with AI

A payment calculator crashes. A trial summary runs without complaint—and reports the wrong total. A CSV column looks correctly named, but Python cannot find it.

Today you will diagnose familiar errors yourself, use AI to investigate harder-to-see problems, and check that the repairs produce the right results.

## By the end of class

You should be able to:

- distinguish syntax, runtime, and logic errors;
- find the useful clues in an error message;
- give AI the code, evidence, and intended behavior it needs;
- explain a small repair and verify it with different inputs.

## Get the files for this class

1. [Download the Class 7 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-07/class-07-files.zip).
2. Extract the ZIP and locate the folder named `class-07`. On Windows, it may be inside an additional folder named `class-07-files`.
3. Move `class-07` into your local course folder, alongside the earlier classes.
4. Open the course folder in VS Code.

If you already have these files, use your existing copy.

## Rehearsal — reuse a function from Class 6

Create `class_07_rehearsal.py` inside `class-07`. Try this from memory before opening the example below.

An experiment pays **10 pence per point**. Two participants earned `12` and `25` points.

1. Define `points_to_bonus(points)` to **return** the bonus in pence. Add a short docstring describing its purpose.
2. Call the same function for both scores and store the results in `first_bonus` and `second_bonus`.
3. Add a **100-pence participation fee** to `first_bonus` and store the result in `total_payment`. Print both bonuses and the first participant's total payment.

Predict the three amounts before running your code. Why does this function need to return its result rather than only print it?

<details>
<summary>Check one possible version</summary>

```python
def points_to_bonus(points):
    """Return the bonus in pence at 10 pence per point."""
    return points * 10


# Reuse the same payment rule for two participants.
first_bonus = points_to_bonus(12)
second_bonus = points_to_bonus(25)

# Use a returned bonus in a further calculation.
total_payment = 100 + first_bonus

print("First bonus (pence):", first_bonus)
print("Second bonus (pence):", second_bonus)
print("First total payment (pence):", total_payment)
```

```text
First bonus (pence): 120
Second bonus (pence): 250
First total payment (pence): 220
```

`return` makes the calculated bonus available to the caller. Printing alone would show it on screen, but would not supply the number for the total-payment calculation.

</details>

## First debugging task — a quick fix you can make yourself

Open [`syntax_error_demo.py`](syntax_error_demo.py). A participant's choice should select the appropriate message. Spot the problem, run the file, then repair it.

<details>
<summary>Check the fix</summary>

The `if` header needs a colon:

```python
if choice == "left":
```

The repaired program prints `Left option selected`. Change `choice` to `"right"` and run it again to check the other branch.

</details>

## Three kinds of error

| Type | What you see | Example |
| --- | --- | --- |
| **Syntax error** | Python cannot read the file as valid code, so it does not start running it | A missing colon after `if` |
| **Runtime error** | The program starts, then stops at an operation it cannot perform | Adding a number to text (`TypeError`), or using an undefined name (`NameError`) |
| **Logic error** | The program runs, but does the wrong thing | Adding only the first trial's points instead of all trials |

**`IndexError`** is another runtime error: it occurs when you request a list position that does not exist. Remember that positions start at `0`, so a list with four items has positions `0` through `3`.

A **traceback** shows where execution reached a runtime error. Start with its final line—the error type and message—then find the last `File ... line ...` entry referring to your file. That is where the failure appeared; its cause may be earlier in the code.

## Activity 1 — repair a familiar error yourself

You are calculating a participant's payment: **10 pence per point**, plus a **100-pence participation fee**.

Open [`runtime_error_demo.py`](runtime_error_demo.py), run it, and enter `12`. You expect a bonus of `120` pence and a total payment of `220` pence, but the program stops.

Use what you already know about `input()`, types, and conversion to find the repair yourself:

1. Read the traceback's final line and find the line in your script where execution stopped.
2. Trace the value from `input()` through `points_to_bonus`. What value and type does each step produce? Why does the program reach the addition before it crashes?
3. Fix the cause, then check all three cases below.

<details>
<summary>Need a hint?</summary>

Add this line immediately before `total_payment = 100 + bonus`, then run the file again:

```python
print("Bonus before addition:", bonus, type(bonus))
```

Does multiplying text by `10` do the same thing as multiplying a number by `10`?

</details>

| Points entered | Bonus (pence) | Total payment (pence) |
| --- | ---: | ---: |
| `12` | 120 | 220 |
| `0` | 0 | 100 |
| `25` | 250 | 350 |

<details>
<summary>Check the diagnosis and repair</summary>

`input()` supplies text. Multiplying that text by `10` repeats it; it does not calculate a numeric bonus. The program then tries to add the integer fee to the repeated text and raises a `TypeError`.

Convert the input before calculating:

```python
# Convert the entered text to a whole-number score before calculating payment.
participant_points = int(input("Points earned: "))
```

Changing the fee to text might remove the error, but would join pieces of text rather than calculate a payment. The expected amounts reveal why that is not a repair.

</details>

## Activity 2 — investigate a wrong result with no error message

Open [`trial_points_debug.py`](trial_points_debug.py). Each dictionary describes one trial. The function should add the points from **every** trial and return the total.

The supplied points are `4`, `10`, and `1`: the expected total is `15`. Run the file. It prints `4` instead, without raising an error.

### Trace the code

Follow the function one line at a time with the supplied trials. Which lines run during the first iteration? Does execution reach the second trial? Use the indentation to explain the result, then make the smallest repair you can.

Run your repaired file: the actual total should now match the expected `15`.

<details>
<summary>Check the execution trace and repair</summary>

| Trial | What the original function does |
| --- | --- |
| First: 4 points | Adds 4, then returns 4 and exits |
| Second: 10 points | Never reached |
| Third: 1 point | Never reached |

`return` is inside the loop. Move it one indentation level left so it runs **after** the loop, while still inside the function:

```python
def calculate_total_points(trials):
    """Return the total points across all trials; return 0 for no trials."""
    # Start a fresh total for this participant.
    total_points = 0

    # Visit every trial record.
    for trial in trials:
        # Add this trial's points to the running total.
        total_points = total_points + trial["points"]

    # Return only after all trials have been processed.
    return total_points
```

</details>

## Activity 3 — investigate errors that are hard to see

### A CSV column that looks correct

A CSV exported from another program may contain small differences in its column names. Open [`csv_header_demo.py`](csv_header_demo.py) and [`trial_results.csv`](trial_results.csv). As in Class 6, each row holds one participant's ID and three trial scores. The script should calculate the bonus and add the participation fee.

Run the Python file with VS Code's **▶** button. It stops with `KeyError: 'trial_1'`. This means the dictionary has no key exactly matching `trial_1`. Compare the CSV header with the names used in the code. Can you spot the mismatch?

Attach **both files** to an AI chat in your browser and paste the error, followed by this prompt:

> This script should read each participant's three trial scores, calculate a bonus at 10 pence per point, and print the bonus and total payment including a 100-pence fee. It stops with `KeyError: 'trial_1'`, although the CSV seems to have that column. Inspect the attached files and compare the exact header names with the dictionary keys used in the code. Explain the mismatch and show the smallest repair, keeping the scores and payment calculation unchanged. If you change Python code, explain any unfamiliar syntax in clear English `#` comments.

If your chat cannot accept files, paste their contents instead. Apply the repair, save, and rerun. Check the printed amounts:

| Participant | Bonus (pence) | Total payment (pence) |
| --- | ---: | ---: |
| P001 | 100 | 200 |
| P002 | 360 | 460 |
| P003 | 40 | 140 |

Then change P001's third score from `2` to `4` in the CSV and save it. Rerun: P001's bonus should become `120` and total payment `220`; the other participants' payments should stay the same.

<details>
<summary>Check the mismatch and repair</summary>

The CSV header contains `trial_1 `, with a space before the comma. `csv.DictReader` uses the header text exactly as written, including that space. The first row therefore becomes:

```python
{"participant_id": "P001", "trial_1 ": "3", "trial_2": "5", "trial_3": "2"}
```

The code asks for `row["trial_1"]`, which is a different key. Remove the extra space in the CSV header and save:

```csv
participant_id,trial_1,trial_2,trial_3
```

The Python code can stay unchanged. To make hidden spaces visible when investigating a header, you can temporarily add `print(reader.fieldnames)` immediately below the `reader = csv.DictReader(input_file)` line, with the same indentation. It displays the column names in quotes, including any spaces inside them.

</details>

<details>
<summary>Another example — identical-looking variable names</summary>

You copied a few lines into a payment script. Open [`copied_name_demo.py`](copied_name_demo.py) and run it. Python reports a `NameError`, even though the variable names look alike.

Paste the exact code and error into AI:

> These variable names look identical, but I get a `NameError`. Compare their exact characters, identify any difference, and show the corrected lines using ordinary English letters. Explain the change in a short `#` comment.

Inspect the proposed spelling, apply the repair, and rerun. Twelve points should produce `120` pence; changing the score to `7` should produce `70`.

<details>
<summary>Reveal the hard-to-see difference</summary>

The name on the calculation line contains a Cyrillic `о` where the definition uses an English `o`. They look almost identical, but they are different characters and create different Python names.

Retype the name on that line using English letters:

```python
# Use the same English-letter variable name as the definition above.
bonus_pence = participant_points * 10
```

</details>

</details>

## Class 7 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Traceback | A report showing the calls and line locations leading to a runtime error, followed by its type and message | Find the last `File ... line ...` entry for your file; the cause may be earlier |
| Syntax error | Code that breaks Python's writing rules and prevents the file from running | A missing colon after an `if` header |
| Logic error | Code that runs but does not produce the intended result | Returning the first trial's points instead of the total |
| Runtime error | An error raised when execution reaches an operation Python cannot perform | Adding an integer fee to a text bonus |
| `TypeError` | A runtime error caused by using a value of an unsuitable type for an operation | `100 + "120"` cannot add a number to text |
| `IndexError` | A runtime error raised when you request a list position that does not exist | `responses[4]` fails if the list has only four items (positions `0`–`3`) |
| `KeyError` | A runtime error raised when a dictionary does not contain the requested key | `"trial_1"` does not match the CSV header `"trial_1 "` |
| `NameError` | A runtime error raised when Python cannot find a name where it is used | A copied variable name contains a lookalike character and does not match the defined name |

## Companion tutorial

For another worked example, watch Khan Academy's 5:49 **[Debugging with stack traces | Intro to CS — Python](https://www.youtube.com/watch?v=WUoCSkSW4cs)**.

---

[Back to the course](https://github.com/EdenHeilprin/technion-096609-python-ai)
