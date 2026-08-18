# Class 4 — Comparisons and Decisions

Today you will ask yes-or-no questions in Python, use the answers to choose which code runs, and test whether a small program behaves correctly at its boundaries.

AI tools are permitted. For the rehearsal, try to find the mistake yourself before consulting the Class 3 materials or another tool.

## By the end of class

You should be able to:

- write comparisons that produce `True` or `False`;
- distinguish assignment with `=` from comparison with `==`;
- use `if`, `elif`, and `else` to choose between branches;
- combine two comparisons using `and` or `or`;
- test a conditional program with ordinary inputs and boundary values.

## Get the files for this class

1. [Download the Class 4 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-04/class-04-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-04`. On Windows, it may appear inside an additional folder named `class-04-files`.
3. Move `class-04` into your local course folder, next to `class-00-setup`, `class-01`, `class-02`, and `class-03`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-04`.

If your course folder already contains `class-04`, you do not need to download it again.

## Rehearsal — correct one Class 3 mistake

Create a new Python file inside `class-04` named `class_04_rehearsal.py` and enter these two lines:

```python
stimuli = ["circle", "square", "triangle"]
print(stimuli[3])
```

The program is intended to display `triangle`, but one number is wrong. Correct the mistake and run the program.

<details>
<summary>Check one possible version</summary>

```python
stimuli = ["circle", "square", "triangle"]
print(stimuli[2])
```

The indices are `0`, `1`, and `2`, so index `2` retrieves the third item.

</details>

## Comparisons answer yes-or-no questions

A **comparison** asks about the relationship between two values. Its result is one of two **Boolean** values: `True` or `False`. Python calls this type `bool`.

| Operator | Question | Example | Result |
| --- | --- | --- | --- |
| `==` | Are the values equal? | `6 == 6` | `True` |
| `!=` | Are the values different? | `6 != 6` | `False` |
| `<` | Is the left value smaller? | `5 < 6` | `True` |
| `<=` | Is the left value smaller or equal? | `6 <= 6` | `True` |
| `>` | Is the left value larger? | `5 > 6` | `False` |
| `>=` | Is the left value larger or equal? | `6 >= 6` | `True` |

`=` and `==` have different jobs:

```python
trials_completed = 6       # assign the value 6
trials_completed == 6      # ask whether the value equals 6
```

## Activity 1 — predict comparison results

Open [`comparisons_demo.py`](comparisons_demo.py). Before running it, predict the four Boolean results and the type reported on the final line.

<details>
<summary>Check your predictions</summary>

```text
Enough trials: True
Exactly required: False
Control condition: True
Not treatment: True
Comparison type: <class 'bool'>
```

</details>

Run the file and compare the output with your predictions. Then change:

- `trials_completed` from `8` to `6`;
- `condition` from `"control"` to `"treatment"`.

Predict which results will change before running the file again.

## Conditions choose which code runs

A **conditional** contains one or more possible paths, called **branches**. Python checks a condition and uses its Boolean result to decide which branch to run.

```python
if trials_completed >= required_trials:
    print("Session complete")
else:
    print("More trials required")
```

Read this structure carefully:

- `if` introduces the first condition;
- the colon `:` begins a branch;
- indentation shows which lines belong to that branch;
- `else` runs when the `if` condition is `False`.

Exactly one of these two messages is displayed on each run.

## Activity 2 — follow an `if`/`else` decision

Open [`completion_check.py`](completion_check.py). Predict the output for each input before running it:

| Input | Your prediction |
| ---: | --- |
| `5` | |
| `6` | |
| `10` | |

Run the file three times and check your predictions.

<details>
<summary>Check the three results</summary>

- `5` displays `More trials required`.
- `6` displays `Session complete`.
- `10` displays `Session complete`.

The comparison uses `>=`, so the boundary value `6` belongs to the complete branch.

</details>

Change `required_trials` to `8`. Predict and test the outputs for `7` and `8`.

## Combine two comparisons

Sometimes one comparison is not enough.

| Operator | Result is `True` when | Example |
| --- | --- | --- |
| `and` | both comparisons are `True` | `rating >= 1 and rating <= 7` |
| `or` | at least one comparison is `True` | `rating < 1 or rating > 7` |

The first example asks whether a rating is inside the allowed range. The second asks whether it is outside that range.

## Activity 3 — validate a rating and test its boundaries

Open [`rating_validator.py`](rating_validator.py). Before running it, predict both output lines for each input:

| Input | Inside the range `1` through `7`? |
| ---: | --- |
| `1` | |
| `7` | |
| `0` | |
| `8` | |

Run the program with all four values. Then test one ordinary value inside the range, such as `4`.

<details>
<summary>Check the boundary results</summary>

- `1` and `7` are valid because both boundaries are included.
- `0` and `8` are invalid because they fall just outside the boundaries.

</details>

An **edge case** is an input at or near a boundary. Edge cases are especially useful because a program can work for an ordinary value while still being wrong at its limits.

## More than two branches

Use `elif` when a decision has more than two possible outcomes:

```python
if first_condition:
    print("First branch")
elif second_condition:
    print("Second branch")
else:
    print("Final branch")
```

Python checks the conditions from top to bottom. It runs the first branch whose condition is `True`, then skips the rest of the chain. The order therefore matters.

## Activity 4 — build and test a rating classifier

Create a new Python file inside `class-04` named `rating_classifier.py`.

Write a program that:

1. asks for an integer rating from `1` through `7`;
2. displays `Invalid rating` if the number is smaller than `1` or larger than `7`;
3. otherwise displays `Lower range` for ratings from `1` through `3`;
4. displays `Middle range` for ratings `4` and `5`;
5. displays `Upper range` for ratings `6` and `7`.

Use one `if`/`elif`/`elif`/`else` chain so that every run displays exactly one result. Try to write and test the program before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
rating = int(input("Rating from 1 to 7: "))

if rating < 1 or rating > 7:
    print("Invalid rating")
elif rating <= 3:
    print("Lower range")
elif rating <= 5:
    print("Middle range")
else:
    print("Upper range")
```

</details>

## Use AI as a test designer

Use any general-purpose AI chat assistant available to you. A free account is sufficient; no particular platform is required. Open a new chat—the assistant does not know anything about this class or your VS Code files unless you provide that information.

Paste only the synthetic program you just wrote. Never paste real participant data or other confidential information into this activity.

Use this prompt, followed by your code:

> I wrote a beginner Python program with these requirements:
>
> - ratings outside 1–7 are invalid;
> - ratings 1–3 are "Lower range";
> - ratings 4–5 are "Middle range";
> - ratings 6–7 are "Upper range".
>
> My code appears below.
>
> Create the smallest useful test table that checks every branch and every boundary. For each test, provide the input, the expected output according to the requirements, and why that test is necessary. Do not rewrite or correct my program. If you notice a possible mismatch, describe it without providing corrected code.

Then:

1. check whether the proposed tests include every branch and boundary;
2. predict each result yourself;
3. run every proposed test in VS Code;
4. investigate any disagreement between the requirements, the AI prediction, and the actual output;
5. compare your work with the test plan below.

If an AI assistant is unavailable, create the same test table manually and continue with the remaining steps.

<details>
<summary>Compare with one complete test plan</summary>

| Input | Expected output |
| ---: | --- |
| `0` | `Invalid rating` |
| `1` | `Lower range` |
| `3` | `Lower range` |
| `4` | `Middle range` |
| `5` | `Middle range` |
| `6` | `Upper range` |
| `7` | `Upper range` |
| `8` | `Invalid rating` |

This is one complete plan. A different set can also be useful if it checks every branch and the values on both sides of each boundary.

</details>

For now, enter whole numbers. Handling input such as `hello` will be covered when we study errors and debugging.

## Class 4 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Boolean | A value that is either `True` or `False` | `6 >= 5` produces `True` |
| `bool` | Python's name for the Boolean type | `type(6 >= 5)` |
| Comparison | A yes-or-no question about values | `condition == "control"` |
| Comparison operator | A symbol that compares values | `==`, `!=`, `<`, `<=`, `>`, `>=` |
| Condition | A Boolean expression used to make a decision | `rating <= 7` |
| Conditional | Code that chooses a branch according to a condition | `if`/`else` |
| Branch | One possible path through a conditional | The indented code under `if` |
| `elif` | Checks another condition if earlier branches were not selected | `elif rating <= 5:` |
| Indentation | Spaces at the start of a line that show which block it belongs to | The four spaces before `print()` |
| Edge case | A value at or near a boundary | `1` and `7` for an allowed range of `1`–`7` |
| Validation | Checking whether information follows a rule | Is the rating inside the allowed range? |

### Assignment is not equality testing

| Code | Meaning |
| --- | --- |
| `condition = "control"` | Assign the text to the variable. |
| `condition == "control"` | Ask whether the variable currently holds that text. |

### Follow one chained conditional

For a rating of `5`, the Activity 4 program proceeds in order:

1. `rating < 1 or rating > 7` is `False`.
2. `rating <= 3` is `False`.
3. `rating <= 5` is `True`, so Python displays `Middle range`.
4. Python skips the final `else` branch.

Only the first matching branch runs.

### A small boundary-testing pattern

When a valid range has a lower and upper boundary, test:

1. one value just below the lower boundary;
2. the lower boundary itself;
3. an ordinary value inside the range;
4. the upper boundary itself;
5. one value just above the upper boundary.

For the range `1` through `7`, those values could be `0`, `1`, `4`, `7`, and `8`.

## Companion tutorials

For two concise explanations from Khan Academy:

1. **[if statements | Intro to CS — Python](https://www.youtube.com/watch?v=7o1wX-jEnP8)** (5 minutes) explains Boolean conditions, colons, indentation, and how Python runs or skips an `if` branch.
2. **[if-elif-else | Intro to CS — Python](https://www.youtube.com/watch?v=q0bQrGhdPm4)** (5 minutes) explains two-way and multi-way decisions, the order of conditions, and why only the first matching branch runs.

Together they reinforce the control-flow structure used in Activities 2 and 4.
