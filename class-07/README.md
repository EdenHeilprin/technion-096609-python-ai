# Class 7 — Errors, Tracebacks, and Tests

Programs rarely work perfectly on the first attempt. Today you will use error messages, selected test cases, and executable expectations to find and repair defects in small pieces of decision-making experiment code.

## By the end of class

You should be able to:

- distinguish syntax errors, runtime errors, and logic errors;
- use a traceback to locate the line where a runtime error occurred;
- compare an actual result with an expected result;
- use `assert` to make a test executable;
- choose cases that can reveal a defect;
- make a small fix and rerun the relevant tests;
- use AI to investigate a failing test while checking its diagnosis against the code and executed results.

## Get the files for this class

1. [Download the Class 7 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-07-debugging/class-07/class-07-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-07`. On Windows, it may appear inside an additional folder named `class-07-files`.
3. Move `class-07` into your local course folder, next to `class-00-setup`, `class-01`, `class-02`, `class-03`, `class-04`, `class-05`, and `class-06`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-07`.

If your course folder already contains `class-07`, you do not need to download it again.

## Rehearsal — reconstruct a small function

Create a new Python file inside `class-07` named `class_07_rehearsal.py`. Write a function named `points_to_bonus` that accepts one `points` parameter and returns the number of bonus currency units when every 100 points are worth 1 unit.

Then call the function with `250`, store the returned value in `bonus`, and display:

```text
Bonus: 2.5
```

Try to reconstruct the program before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
def points_to_bonus(points):
    return points / 100


bonus = points_to_bonus(250)
print("Bonus:", bonus)
```

</details>

## Three ways a program can be wrong

Different defects produce different evidence.

| Error type | What happens | Small example |
| --- | --- | --- |
| **Syntax error** | Python cannot understand the program's structure, so execution does not begin | A missing colon after an `if` header |
| **Runtime error** | Execution begins, but Python reaches an operation it cannot perform | Dividing text by a number |
| **Logic error** | The program runs, but its result does not match the intended rule | Applying a bonus cap in the wrong direction |

Syntax and runtime errors normally produce an error message. A logic error may produce completely ordinary-looking output. To find it, you need to know what result you expected and compare that expectation with what the program actually did.

## A practical debugging cycle

When a program does not behave as intended:

1. **Reproduce** the problem by running the same code again.
2. **Read the evidence**: the error message, traceback, or incorrect output.
3. **Locate** the smallest relevant part of your code.
4. **Inspect** the values and the rule the code is meant to implement.
5. **Change one thing** that could explain the evidence.
6. **Rerun** the original case and any related tests.

Debugging is not guessing randomly. Each run gives evidence for the next inspection or change.

## Activity 1 — repair a syntax error

Open [`syntax_error_demo.py`](syntax_error_demo.py). Inspect the code before running it. Which line prevents Python from understanding the program?

Run the file and read the final line of the message. It should identify a `SyntaxError` and point toward the incomplete `if` header.

Make the smallest necessary fix and rerun the file.

<details>
<summary>Check the fix and output</summary>

The `if` header needs a colon:

```python
if choice == "left":
```

The repaired program displays:

```text
Left option selected
```

</details>

Change `choice` to `"right"` and run the repaired program once more. Both branches should now be reachable without another code change.

## How to read a traceback

A **traceback** records where Python was executing when a runtime error occurred. Start at the bottom:

1. Read the final line for the error type and message.
2. Move upward to the lowest `File ... line ...` entry that refers to your Python file.
3. Inspect that line and the values that reached it.
4. If one function called another, continue upward to see how execution arrived there.

A shortened traceback can look like this:

```text
Traceback (most recent call last):
  File "runtime_error_demo.py", line 8, in <module>
    bonus = points_to_bonus(participant_points)
  File "runtime_error_demo.py", line 2, in points_to_bonus
    return points / 100
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

The final line names a `TypeError`: the operation received incompatible types. The code locations show both the function call and the operation inside the function where the error occurred.

## Activity 2 — follow a runtime error

Open [`runtime_error_demo.py`](runtime_error_demo.py). Before running it, inspect the value assigned to `participant_points` and the division inside `points_to_bonus`.

Run the file, then use the traceback to answer:

1. Which output line appears before the error?
2. What error type appears on the final traceback line?
3. Which two value types were used with `/`?
4. Which line inside the function attempted that operation?
5. What is the smallest change that makes the supplied value match the function's intended integer input?

<details>
<summary>Check the diagnosis and fix</summary>

`participant_points` contains the text value `"250"`. The function attempts to divide that `str` by the integer `100`, so Python raises a `TypeError` on the `return` line.

Remove the quotation marks so that the supplied value is an integer:

```python
participant_points = 250
```

The repaired output is:

```text
Converting points
Bonus: 2.5
```

</details>

Rerun the repaired program with `participant_points` equal to `0` and then `500`. Predict each returned bonus before executing it.

## Turn expectations into tests

A **test case** combines a chosen input with an expected result. The program supplies the actual result.

```python
expected_bonus = 2.5
actual_bonus = points_to_bonus(250)

print("Expected:", expected_bonus)
print("Actual:", actual_bonus)
```

The comparison can also become an executable **assertion**:

```python
assert actual_bonus == expected_bonus
```

- If the comparison is `True`, the assertion produces no output and execution continues.
- If the comparison is `False`, Python stops with an `AssertionError` at that line.

An assertion records a result that must be true for that test. It does not explain the defect by itself; it makes the mismatch visible and locates the failed expectation.

## Activity 3 — expose a logic error

Open [`logic_error_demo.py`](logic_error_demo.py). The intended rule is:

- every 100 points are worth 1 bonus unit;
- the maximum bonus is 5 units.

Before running the file, predict the actual bonus for `250` points and for `600` points. Then run it.

The program completes the calculation but fails one assertion. This is a logic error rather than a syntax or runtime error.

Inspect the line inside the `if` block. Recall the difference between:

```python
bonus = 5
```

and:

```python
bonus == 5
```

Make the smallest fix, rerun the program, and confirm that it reaches:

```text
All bonus tests passed
```

<details>
<summary>Check the diagnosis</summary>

The expression `bonus == 5` compares two values and produces a Boolean result, but the program does not store or use that result. It does not change `bonus`.

The line should assign the capped value:

```python
bonus = 5
```

After that fix, `calculate_bonus(250)` returns `2.5` and `calculate_bonus(600)` returns `5`.

</details>

Add these tests below the existing assertions:

```python
assert calculate_bonus(0) == 0
assert calculate_bonus(500) == 5
assert calculate_bonus(750) == 5
```

Run all five tests together. A later fix should preserve the cases that already worked.

## Choose cases that can reveal the defect

Different cases test different claims.

| Case | Example | What it checks here |
| --- | ---: | --- |
| Ordinary uncapped value | `250` | Normal conversion below the cap |
| Boundary value | `500` | Exactly 5 units |
| Value beyond the boundary | `750` | The cap remains 5 |
| Zero | `0` | No points produce no bonus |

A passing test gives evidence for the particular behavior it checks. Several deliberately different cases are more informative than repeating nearly identical inputs.

## Activity 4 — debug a flawed trial summary

Open [`trial_points_debug.py`](trial_points_debug.py). It represents each experiment trial as a dictionary with a recorded `choice` and earned `points`. The function should add the points from **every** trial and return the final total.

Before running the file:

1. calculate the expected total from the three trial records;
2. trace the function body by hand;
3. predict the actual value the current function returns.

Run the file. Use the printed expected and actual values, the failing assertion, and the function's indentation to locate the logic error. Write down the smallest fix you would try.

### Investigate the failing test with AI

After your own first diagnosis, paste the complete contents of `trial_points_debug.py` into a new AI chat. Immediately below the code, add this prompt:

> The function should add the points from every trial record. The test expects `15`, but the actual result is `4`. Identify the exact cause, cite the relevant line and indentation, and show the smallest necessary edit. Then propose one additional test containing at least two trial records that would expose the same defect. Do not rewrite the complete program.

Check whether the response agrees with the executed evidence and your own diagnosis. Apply only the smallest justified edit, then rerun the original test.

Finally, add these three assertions immediately above the final `print("All trial-point tests passed")` line:

```python
assert calculate_total_points([]) == 0
assert calculate_total_points([{"choice": "left", "points": 7}]) == 7
assert calculate_total_points([
    {"choice": "right", "points": 2},
    {"choice": "left", "points": 3},
]) == 5
```

Rerun the file. Compare the AI-proposed test with the final two-trial test above: does its expected result depend on processing more than the first record?

<details>
<summary>Check the diagnosis and repaired function</summary>

The `return` line is indented inside the loop. The function therefore returns after the first iteration, before Python can process the remaining trials.

Move `return total_points` out of the loop while keeping it inside the function:

```python
def calculate_total_points(trials):
    total_points = 0

    for trial in trials:
        total_points = total_points + trial["points"]

    return total_points
```

The empty-list and one-trial tests are useful, but neither one can expose this particular early-return defect. A test with at least two trials and a nonzero contribution after the first trial is needed to reveal it.

</details>

## Class 7 reference

### Central terms

| Term | Simple meaning |
| --- | --- |
| Bug or defect | A problem that makes a program invalid or inconsistent with its intended behavior |
| Debugging | Finding the cause of a defect, making a justified change, and checking the result |
| Syntax error | Code Python cannot understand as a valid program |
| Runtime error | A failure that occurs while valid Python code is executing |
| Logic error | Code that runs but produces unintended behavior |
| Traceback | A record of the code locations Python passed through before a runtime error |
| Error type | The error category named at the end of an error message, such as `TypeError` |
| Test case | A chosen input together with its expected result |
| Expected result | What the stated rule says should happen |
| Actual result | What the program really produces when executed |
| Assertion | An executable statement that requires a condition to be `True` |

### Assignment and equality

```python
bonus = 5
```

Assignment changes the stored value of `bonus`.

```python
bonus == 5
```

Equality comparison asks whether `bonus` is equal to `5` and produces `True` or `False`.

### Read runtime evidence from the bottom

For a runtime error, begin with the traceback's final line. It identifies the error type and describes the incompatible operation or missing value. Then find the lowest referenced line in your own file and inspect the values that arrived there.

### Print a value when the program's state is unclear

Temporary output can make an intermediate value visible:

```python
print("Current total:", total_points)
```

Place the line near the calculation you are investigating, run the program, and remove the temporary output after the problem is understood.

### Assertions compare actual behavior with an expectation

```python
actual = calculate_bonus(600)
expected = 5
assert actual == expected
```

If the values match, execution continues. If they differ, the assertion fails at a known expectation.

### Retest after a fix

First rerun the case that exposed the defect. Then rerun cases that already passed. A repair is stronger when it corrects the failing behavior without breaking established behavior elsewhere.

## Companion tutorial

For another concise worked example, watch Khan Academy's 5:49 **[Debugging with stack traces | Intro to CS — Python](https://www.youtube.com/watch?v=WUoCSkSW4cs)**.

It demonstrates a practical debugging process across syntax errors, runtime errors, and logic errors, including how stack traces and visible code evidence help narrow the problem.
