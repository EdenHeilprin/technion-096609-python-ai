# Class 2 — Types, Input, and Conversion

Today you will ask a user for information, distinguish text from numbers, convert text into a number, and use the result in a calculation.

AI tools are permitted. For the rehearsal, try the task from memory first; consult the Class 1 materials or another tool if you become stuck.

## By the end of class

You should be able to:

- recognize text, integer, and decimal values;
- use `type()` to inspect a value;
- explain the difference between `6` and `"6"`;
- collect information using `input()`;
- convert suitable input into an integer and use it in a calculation.

## Get the files for this class

1. [Download the Class 2 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-02-structure/class-02/class-02-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-02`. On Windows, it may appear inside an additional folder named `class-02-files`.
3. Move `class-02` into your local course folder, next to `class-00-setup` and `class-01`—not inside either of them.
4. Open the course folder in VS Code. Its Explorer panel should now show `class-00-setup`, `class-01`, and `class-02`.

If your course folder already contains `class-02`, you do not need to download it again.

## Rehearsal — bring back Class 1

Create a new Python file inside `class-02` named `class_02_rehearsal.py`.

Without copying from the Class 1 files, try to write three lines that:

1. assign the text `"Risk and Reward"` to a variable named `experiment_name`;
2. display the value of `experiment_name`;
3. display the text `"Ready to begin"`.

Run your program. If you become stuck, consult the Class 1 page or another tool, then return to your file and complete it.

<details>
<summary>Check one possible version</summary>

```python
experiment_name = "Risk and Reward"
print(experiment_name)
print("Ready to begin")
```

</details>

Change the experiment name, predict the new output, and run the file again.

## Three types to recognize

| Python name | Meaning for today | Examples |
| --- | --- | --- |
| `str` | Text inside quotation marks | `"P014"`, `"control"`, `"6"` |
| `int` | A whole number without quotation marks | `6`, `0`, `-2` |
| `float` | A number containing a decimal point | `1.42`, `0.0` |

`type(value)` asks Python which type a value has.

## Activity 1 — recognize types

Open [`types_demo.py`](types_demo.py). Before running it, predict the type of each value using the table above.

```python
participant_code = "P014"
trials_completed = 6
response_time = 1.42
```

Run the file and compare the output with your predictions. In output such as `<class 'str'>`, focus on the short name inside the quotation marks.

The file also compares these two expressions:

```python
6 + 2
"6" + "2"
```

Predict both results before running them. Explain why the results differ even though the characters look similar.

<details>
<summary>Check your prediction</summary>

`6 + 2` produces `8` because Python adds two integers.

`"6" + "2"` produces `"62"` because Python joins two strings.

</details>

## Activity 2 — collect text with `input()`

Open [`input_demo.py`](input_demo.py). Read the code before running it.

`input()` displays a prompt, waits for the user to type, and returns the typed information as text.

Run the file and enter a synthetic participant code such as `P014` and a condition such as `control`. Run it again with different values.

Before running the next line, predict which type Python will report. Then add the line temporarily and run the program again:

```python
print(type(participant_code))
```

<details>
<summary>Check your prediction</summary>

The result is `str` because `input()` returns text.

</details>

## Activity 3 — convert and calculate

Open [`points_calculator.py`](points_calculator.py).

When the program asks for the number of completed trials, enter `6`. Before running it, predict the total number of points.

The important transition is:

```python
trials_text = input("Trials completed: ")
trials_completed = int(trials_text)
```

`input()` produces text. `int()` converts suitable text, such as `"6"`, into the integer `6`. Python can then use that integer in arithmetic.

Run the program with `6`, then run it again with `10`. Compare each result with your prediction.

## Activity 4 — build an interactive participant summary

Create a new Python file inside `class-02` named `participant_summary.py`.

Write a program that:

1. asks for a synthetic participant code;
2. asks how many trials were completed;
3. converts the trial count into an integer;
4. assigns `5` to `points_per_trial`;
5. calculates the total points;
6. displays the participant code and total points with clear labels.

For participant `P014` and `6` completed trials, the final two lines of output should be:

```text
Participant: P014
Total points: 30
```

Check your program with `0`, `6`, and `10` completed trials. Predict each total before running it.

## Class 2 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Type | A category that tells Python what kind of value it is handling | `str`, `int`, `float` |
| `str` | Text, written inside quotation marks | `"P014"` |
| `int` | A whole number | `6` |
| `float` | A number with a decimal point | `1.42` |
| `type()` | Reports the type of a value | `type(6)` |
| `input()` | Displays a prompt and returns what the user types as text | `input("Condition: ")` |
| Conversion | Creating a value of one type from a suitable value of another type | `int("6")` produces `6` |
| `int()` | Converts a suitable value into an integer | `int("6")` |
| Prompt | The message shown before the program waits for input | `"Trials completed: "` |

### Similar-looking values can behave differently

| Code | Type | Meaning |
| --- | --- | --- |
| `6` | `int` | The number six; it can be used directly in arithmetic. |
| `"6"` | `str` | The text character 6. |
| `6 + 2` | arithmetic with integers | Produces `8`. |
| `"6" + "2"` | joining two strings | Produces `"62"`. |

### Follow the value

In the points calculator, one piece of information changes form:

1. The user types `6`.
2. `input()` returns the text `"6"`.
3. `int()` converts that text into the integer `6`.
4. Python multiplies the integer by `points_per_trial`.
5. `print()` displays the calculated result.

A useful debugging question is: **What value does this variable hold right now, and what type is that value?**

## Companion tutorial

For another concise explanation, watch **[Type casting | Intro to CS — Python — Khan Academy](https://www.youtube.com/watch?v=y-FlANhhNiA)** (4 minutes).

The video revisits `str`, `int`, `float`, `input()`, and conversion, and briefly shows why incompatible values can produce an error.
