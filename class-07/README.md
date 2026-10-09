# Class 7 — Debugging with AI

A payment calculator crashes. A variable looks correctly spelled, but Python cannot find it. A trial summary runs without complaint—and reports the wrong total.

Today you will use AI to investigate these problems, understand the proposed repairs, and check that the results are right.

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

A game pays **10 pence per point**. Two participants earned `12` and `25` points.

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

A **traceback** shows where execution reached a runtime error. Start with its final line—the error type and message—then find the last `File ... line ...` entry referring to your file. That is where the failure appeared; its cause may be earlier in the code.

## Working with AI on a bug

Give AI **the relevant code + the exact error or output + what should happen instead**. Paste code as text so indentation and individual characters can be inspected.

Ask for a short diagnosis, a small repair, and clear English `#` comments explaining the purpose of each line in any replacement code. Read the change, run the original case again, and check another input. A program that stops crashing is not necessarily correct.

## Activity 1 — turn a traceback into a useful repair

You are calculating a participant's payment: **10 pence per point**, plus a **100-pence participation fee**.

Open [`runtime_error_demo.py`](runtime_error_demo.py), run it, and enter `12`. You expect a bonus of `120` pence and a total payment of `220` pence, but the program stops.

Copy the code and the full traceback into AI, then add:

> I entered `12`. The bonus should be 120 pence and the total payment 220 pence. Explain this traceback in plain English. Trace the value and type from `input()` through the calculation to the failing line. Find the cause, not just a way to hide the error. Show the smallest repair, with an English `#` comment explaining it.

Apply the repair you understand, then run these cases:

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

## Activity 2 — a tiny error that is hard to see

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

## Activity 3 — investigate a wrong result with no error message

Open [`trial_points_debug.py`](trial_points_debug.py). Each dictionary describes one trial. The function should add the points from **every** trial and return the total.

The supplied points are `4`, `10`, and `1`: the expected total is `15`. Run the file. It prints `4` instead, without raising an error.

### Use AI to make execution visible

Paste the program into AI and ask:

> This function should total every trial's points. The supplied trials contain 4, 10, and 1 points: I expect 15, but the program prints 4. Trace the current code in a small table showing which trials are reached, the running total, and when the function exits. Identify the cause and show the smallest repair. Keep the existing function and loop; add clear English `#` comments explaining each line of the repaired function and its purpose.

Compare the table with the code's indentation, then apply the repair. Rerun the file: the actual total should now match the expected `15`.

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

### Let AI help you challenge the fix

In the same chat, ask:

> Propose two small trial lists and their expected totals to check this repair. Include one case where the original program would appear correct and one where it would lose points. Explain why each case matters. Show simple `print()` calls with labeled expected and actual results.

Calculate the expected totals yourself, then run the suggested calls. Also add these checks below your function:

```python
print("One trial — expected: 7 actual:", calculate_total_points([{"points": 7}]))
print("Two trials — expected: 5 actual:", calculate_total_points([{"points": 2}, {"points": 3}]))
print("No trials — expected: 0 actual:", calculate_total_points([]))
```

The one-trial case also works in the original program. The two-trial case reveals lost points; the empty case checks that the function still returns a useful zero when there is nothing to process.

## Keep this debugging habit

**Run → collect evidence → ask for an explanation and repair → inspect the change → rerun and compare.**

You decide what the program should do. AI can help locate the cause, make execution easier to follow, and suggest revealing tests. The output—not the confidence of the explanation—shows whether a tested case works.

## Class 7 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Debugging | Finding the cause of a problem, repairing it, and checking the result | Trace the payment calculation to find where text was used instead of a number |
| Syntax error | Code that breaks Python's writing rules and prevents the file from running | A missing colon after an `if` header |
| Runtime error | An error raised when execution reaches an operation Python cannot perform | Adding an integer fee to a text bonus |
| Logic error | Code that runs but does not produce the intended result | Returning the first trial's points instead of the total |
| Traceback | A report showing the calls and line locations leading to a runtime error, followed by its type and message | Find the last `File ... line ...` entry for your file; the cause may be earlier |
| `TypeError` | A runtime error caused by using a value of an unsuitable type for an operation | `100 + "120"` cannot add a number to text |
| `NameError` | A runtime error raised when Python cannot find a name where it is used | A copied variable name contains a lookalike character and does not match the defined name |
| Execution trace | A step-by-step record of which lines run and how values change | The first trial makes the total `4`; an early `return` skips the remaining trials |
| Expected and actual results | What the program should produce, compared with what it really produces | Expected total: `15`; actual total: `4` |
| Test case | A specific input with a known expected result used to check behavior | An empty trial list should give a total of `0` |

## Companion tutorial

For another worked example, watch Khan Academy's 5:49 **[Debugging with stack traces | Intro to CS — Python](https://www.youtube.com/watch?v=WUoCSkSW4cs)**.
