# Class 6 — Functions, Parameters, and Return Values

Each participant earns points across several trials of an experiment. To calculate their bonus, we first add up their points, then convert the total into pence. We already know how to do this with a loop. Today we will turn those steps into a named, reusable **function**.

Today you will build that function, learn how to pass in different values and return results, and use functions to process more than one dataset.

## By the end of class

You should be able to:

- distinguish a function definition from a function call;
- define and call a simple function;
- distinguish a parameter from an argument;
- use `return` to send a result back to the caller;
- store and use a returned value;
- recognize a function docstring that explains the function's contract;
- explain why parameters and variables created inside a function are local to that call;
- move familiar loop-and-condition logic into a reusable function.

## Get the files for this class

1. [Download the Class 6 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-06/class-06-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-06`. On Windows, it may appear inside an additional folder named `class-06-files`.
3. Move `class-06` into your local course folder, next to `class-00-setup`, `class-01`, `class-02`, `class-03`, `class-04`, and `class-05`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-06`.

If your course folder already contains `class-06`, you do not need to download it again.

## Rehearsal — reconstruct a running total

Create a new Python file inside `class-06` named `class_06_rehearsal.py`. Enter the first two and final lines below, then reconstruct the two missing loop lines from memory.

```python
trial_points = [3, 5, 2]
total_points = 0

# Write the loop header and its indented update here.

print("Total points:", total_points)
```

Predict the final output, complete the program, and run it.

<details>
<summary>Check one possible version</summary>

```python
trial_points = [3, 5, 2]
total_points = 0

for points in trial_points:
    total_points = total_points + points

print("Total points:", total_points)
```

The final output is:

```text
Total points: 10
```

</details>

## Give the whole calculation a name

The experiment pays **10 pence for each point**. The rehearsal already adds up one participant's trial points. To calculate their bonus, we multiply that total by 10.

Here is a working program that repeats those steps for two participants:

```python
# Calculate the first participant's bonus.
first_points = [3, 5, 2]
first_total = 0
for points in first_points:
    first_total = first_total + points
first_bonus = first_total * 10

# Calculate the second participant's bonus.
second_points = [4, 1, 3]
second_total = 0
for points in second_points:
    second_total = second_total + points
second_bonus = second_total * 10

print("First bonus (pence):", first_bonus)
print("Second bonus (pence):", second_bonus)
```

Which instructions do the same job? If the rate changes to **15 pence per point**, how many calculations must we edit? What would happen if we changed only one?

We can give the complete calculation a name: `calculate_bonus`. Its **definition** contains the instructions for doing the job:

```python
def calculate_bonus(trial_points):
    # Start a fresh total for this participant.
    total_points = 0

    # Add each trial's points to the total.
    for points in trial_points:
        total_points = total_points + points

    # Convert the total to pence at 10 pence per point.
    bonus_pence = total_points * 10
    # Send the calculated bonus back to the code that called the function.
    return bonus_pence
```

Now we can use that whole calculation with a **function call**:

```python
# Calculate and store a bonus for each participant.
first_bonus = calculate_bonus([3, 5, 2])
second_bonus = calculate_bonus([4, 1, 3])

print("First bonus (pence):", first_bonus)
print("Second bonus (pence):", second_bonus)
```

Each call starts a fresh total, adds the supplied trial points, and calculates the bonus. **`return` sends the result back**, so it can be stored in `first_bonus` or `second_bonus`. The outputs are 100 and 80 pence.

**Loops repeat instructions. Functions let us define a task once and use it by name wherever we need it.** A loop can also call a function for each item. The loop inside `calculate_bonus` still does the adding; the function packages the whole bonus calculation into one meaningful operation. Changing the payment rule in the definition changes it for every call.

You already call `input()`, `type()`, and `print()` without writing the instructions inside them. Now you can create your own function. Its name tells you **what** it does; its definition specifies **how** it works.

### Read the definition and the calls

```python
def calculate_bonus(trial_points):  # trial_points is the parameter.
    total_points = 0                # Start a fresh total.
    for points in trial_points:
        total_points = total_points + points
    bonus_pence = total_points * 10  # Convert points to pence.
    return bonus_pence              # Send the result back to the caller.

# Each call supplies a list as its argument and stores the returned bonus.
first_bonus = calculate_bonus([3, 5, 2])
second_bonus = calculate_bonus([4, 1, 3])
```

- `def` begins a function definition; `calculate_bonus` is the function's name.
- `trial_points` is a **parameter**: a name for the information the function receives.
- The colon `:` starts the body. The indented lines belong to the function; the update inside the loop is indented one level further.
- `calculate_bonus([3, 5, 2])` is a **call**: it runs the function with that list.

A definition tells Python how to perform the task; a call tells it to perform the task now. Reading the definition alone does not run its body.

### Parameter versus argument

| Term | Where it appears | Example |
| --- | --- | --- |
| Parameter | In a definition; a name for incoming information | `trial_points` |
| Argument | In a call; the actual information supplied | `[3, 5, 2]` in `calculate_bonus([3, 5, 2])` |

During the first call, `trial_points` holds `[3, 5, 2]`. During the second, it holds `[4, 1, 3]`. The definition stays the same.

## Activity 1 — calculate bonuses for different participants

Open [`function_call_demo.py`](function_call_demo.py). Predict its output before running it.

<details>
<summary>Check your prediction</summary>

```text
First bonus (pence): 100
Second bonus (pence): 80
```

Python first reads the definition. Each call then calculates a bonus from its own list of trial points.

</details>

Run the file. Then add a call for a third participant who earned `[2, 4]`: store the result in `third_bonus` and print it. Predict the bonus before running it again.

Inside `calculate_bonus`, comment out **only** `return bonus_pence` by adding `#` before it:

```python
    # return bonus_pence
```

Keep the function calls and print lines active. Predict the output, then run the file. What appears in place of each bonus? Remove the `#` and run it again to compare.

<details>
<summary>Why does the output change?</summary>

Without `return bonus_pence`, the function still calculates the bonus, but it does not send that number back. Python returns `None` instead, so each printed bonus is `None`. Restoring `return bonus_pence` sends the calculated number back to the caller.

</details>

## A docstring records the function's job

A **docstring** describes the function as a whole. Put it immediately after the header, before the other instructions:

```python
def calculate_bonus(trial_points):
    """Return the bonus in pence for a list of trial points, at 10 pence per point."""
    # Start a fresh total for this participant.
    total_points = 0

    # Add each trial's points to the total.
    for points in trial_points:
        total_points = total_points + points

    # Convert the total to pence at 10 pence per point.
    bonus_pence = total_points * 10
    # Send the calculated bonus back to the code that called the function.
    return bonus_pence
```

Use `#` comments to explain individual lines or choices. A **docstring** uses triple quotes as the first statement in a function; Python also makes it available through `help()`. Neither prints a message when you call the function.

A function's **contract** is its agreement with the caller: what it accepts and what it does or returns. A useful docstring summarizes that agreement.

## Activity 2 — change the payment rule in one place

Open [`parameter_demo.py`](parameter_demo.py). It contains the documented function and calls with `[3, 5, 2]`, `[4, 1, 3]`, and `[2, 4]`.

For the next experiment, the rate increases to **15 pence per point**. Change the calculation inside the function and update its docstring and conversion comment to match. Leave all three calls unchanged.

Predict the new bonuses, then run the program.

<details>
<summary>Check the complete output</summary>

```text
First bonus (pence): 150
Second bonus (pence): 120
Third bonus (pence): 90
```

One change to the calculation updates all three bonuses. Each call still means “calculate this participant's bonus,” even though the payment rule has changed.

</details>

## Use the returned value in another calculation

The experiment also pays a fixed participation fee of **100 pence**. Add these lines at the end of `parameter_demo.py` to use the bonus already stored in `first_bonus`:

```python
# Add the participation fee to the bonus (both in pence).
total_payment = 100 + first_bonus
print("Total payment (pence):", total_payment)
```

`return` and `print()` do different jobs:

| Operation | What it does |
| --- | --- |
| `return value` | Sends a value back to the caller so it can be stored or used |
| `print(value)` | Displays a value in the output area |

Printing a bonus inside the function would display it, but would not send that number back for the payment calculation. Returning it lets the calling code decide how to use it.

## Activity 3 — trace two function calls

Open [`return_value_demo.py`](return_value_demo.py), which uses the original rate of **10 pence per point**. Do not run it yet. Complete the prediction table. Each total payment includes a participation fee of **100 pence**.

| Call | Argument | Returned bonus (pence) | Variable receiving the bonus | Total payment (pence) |
| --- | --- | --- | --- | --- |
| First | `[3, 5, 2]` | | `first_bonus` | |
| Second | `[4, 1, 3]` | | `second_bonus` | |

<details>
<summary>Check the completed table and output</summary>

| Call | Argument | Returned bonus (pence) | Variable receiving the bonus | Total payment (pence) |
| --- | --- | ---: | --- | ---: |
| First | `[3, 5, 2]` | 100 | `first_bonus` | 200 |
| Second | `[4, 1, 3]` | 80 | `second_bonus` | 180 |

```text
First total payment (pence): 200
Second total payment (pence): 180
```

</details>

Run the file. Change the first argument to `[3, 5, 3]`. Predict which payment changes and by how much, then run it again. Finally, try an empty list `[]` for the first participant: what happens to the bonus and the participation fee?

## Each call has its own local values

The parameter `trial_points` and the variables `total_points`, `points`, and `bonus_pence` belong to the function call. They have **local scope**: these names are used inside the function.

Each call starts again with `total_points = 0`. The second participant's calculation does not continue adding to the first participant's total. Information enters through arguments and leaves through the returned value.

The variables `first_bonus` and `second_bonus` are created outside the function. They preserve the two returned results after the calls finish.

## Activity 4 — turn a Class 5 counter into a function

Create a new Python file inside `class-06` named `fast_response_function.py`.

Define a function named `count_fast_responses` that:

1. has one parameter named `response_times`;
2. initializes a local counter to `0`;
3. loops over every response time;
4. counts values less than or equal to `1000`;
5. returns the final count after the loop;
6. does not print anything inside the function.

Below the function definition, create these two lists:

```python
session_a = [1200, 700, 1500, 900, 1100]
session_b = [800, 1000, 1001]
```

Call the function once with each list, store the two returned values, and display:

```text
Session A fast responses: 2
Session B fast responses: 2
```

Try to write and test the complete program before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
def count_fast_responses(response_times):
    """Return the number of response times at or below 1000 ms."""
    fast_count = 0

    for response_time in response_times:
        if response_time <= 1000:
            fast_count = fast_count + 1

    return fast_count


session_a = [1200, 700, 1500, 900, 1100]
session_b = [800, 1000, 1001]

session_a_fast = count_fast_responses(session_a)
session_b_fast = count_fast_responses(session_b)

print("Session A fast responses:", session_a_fast)
print("Session B fast responses:", session_b_fast)
```

</details>

Test the function with two additional calls:

```python
print("Empty list:", count_fast_responses([]))
print("Boundary only:", count_fast_responses([1000]))
```

Predict both results before running the file.

<details>
<summary>Check the additional tests</summary>

```text
Empty list: 0
Boundary only: 1
```

The local counter begins at `0` during every call. An empty list produces zero loop iterations, while the boundary value `1000` satisfies `<= 1000`.

</details>

## Use AI to prepare participant payments

The experiment has finished. Its results contain **one row per trial**, but you need a payment file with **one row per participant**. Your bonus function can do the calculation; AI can help connect it to reading and writing files.

### 1. Give AI the script and the data

Open [`trial_results.csv`](trial_results.csv) from your `class-06` folder in VS Code. A CSV is a plain-text table with columns separated by commas. Here, each participant has three trials:

```csv
participant_id,trial,points
P001,1,3
P001,2,5
P001,3,2
P002,1,12
P002,2,9
P002,3,15
P003,1,2
P003,2,0
P003,3,2
```

Open your preferred AI chat in your browser. Attach **`return_value_demo.py` and `trial_results.csv`**, then send the prompt below. If the chat does not accept a file, paste its contents into the message instead.

> Adapt the attached Python script to prepare participant payments from the attached `trial_results.csv`.
>
> Gather each participant's trial points and pass their list to `calculate_bonus`. Use 10 pence per point, cap the bonus at 300 pence, and add a participation fee of 100 pence outside the function.
>
> Return one complete replacement script. It should write `payments.csv` with the columns `participant_id`, `bonus_pence`, and `total_payment_pence`, with one row per participant. Print the participant count and total amount to pay in pence. Replace the output file each time the script runs.
>
> Keep the existing bonus function recognizable. Use lists, dictionaries, ordinary `for` loops, conditions, and functions, with simple statements and one operation per line. Avoid comprehensions and unpacking multiple variables in a loop. For the participant loop, use `for participant_id in participant_points:` and then `trial_points = participant_points[participant_id]` inside it, rather than `.items()`.
>
> Use the built-in `csv` module; no additional installations should be needed. Include brief function docstrings and clear English `#` comments.
>
> File handling is new to me. At the first use of unfamiliar syntax, add short `#` comments explaining both what the line does and how to read it. Explain `import`, `Path(__file__).resolve().parent`, joining paths with `/`, `with ... as`, file-opening options, and CSV readers/writers and their methods. Prefer familiar syntax whenever it can do the same job.
>
> Use `Path(__file__).resolve().parent` from `pathlib` to find the script's folder. Read `trial_results.csv` from that folder and save `payments.csv` there. Do not use a hard-coded path or depend on the terminal's current folder.

### 2. Run it in VS Code

Replace the contents of **`return_value_demo.py`** with the returned Python code and save. Keep `trial_results.csv` beside it in `class-06`.

With `return_value_demo.py` open, click the **▶ button at the top right of the editor** to run the whole file. Open the generated `payments.csv` in VS Code's Explorer panel.

### 3. Check the payments

Follow three connections in the code: where CSV rows become each participant's list of points, where that list is passed to `calculate_bonus`, and where the returned bonus becomes a payment row. Use the comments to understand unfamiliar lines. Check that the participation fee is added **after** the bonus cap is applied.

Compare the generated file with these expected payments:

| Participant | Bonus (pence) | Total payment including fee (pence) |
| --- | ---: | ---: |
| P001 | 100 | 200 |
| P002 | 300 | 400 |
| P003 | 40 | 140 |

The printed summary should report **3 participants** and **740 pence** in total.

Now add this trial as a new line at the bottom of `trial_results.csv` and save:

```csv
P001,4,2
```

Run the script again. P001's payment should increase to **220 pence**; the other payments should stay unchanged. The output should still contain three participants, with a total payment of **760 pence**.

## Class 6 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Function (`def`) | A named, reusable block of code, defined with `def` | `def count_fast_responses(response_times):` |
| Function call | An instruction to perform the function now | `count_fast_responses(session_a)` |
| Parameter | A name for incoming information in the definition | `response_times` |
| Argument | An actual value supplied in a call | `session_a` |
| Return value | The result sent back to the caller by `return` | `return fast_count` |
| Local scope | A function's parameters and local variables are available inside that function | `fast_count` inside the function |
| Docstring | A description of the function, placed first in its body inside triple quotes | `"""Return the number of fast responses."""` |

### Definition and call

```python
def calculate_bonus(trial_points):
    """Return the bonus in pence for a list of trial points, at 10 pence per point."""
    # Start a fresh total for this participant.
    total_points = 0

    # Add each trial's points to the total.
    for points in trial_points:
        total_points = total_points + points

    # Convert the total to pence at 10 pence per point.
    bonus_pence = total_points * 10
    # Send the calculated bonus back to the code that called the function.
    return bonus_pence


# Call the function and keep its returned value.
bonus = calculate_bonus([3, 5, 2])
```

The definition describes a reusable task. The call supplies one argument and receives one returned value.

### Information flow

```text
argument → parameter → function body → return value → receiving variable
[3, 5, 2] → trial_points → add and convert → 100 → bonus
```

Each call follows the same route with its own argument and local values.

### `return` versus `print()`

```python
bonus = calculate_bonus([3, 5, 2])  # Receive and store the returned number.
print(bonus)                     # Display that number.
total_payment = 100 + bonus       # Use it in another calculation.
```

### A function can contain familiar structures

Function bodies may contain assignments, comparisons, conditionals, and loops. The syntax inside Activity 4 is not a new kind of counter—it is the Class 5 counter placed inside a named, reusable task.

### Test through calls

Test a function by calling it with chosen arguments and comparing its actual return values with expected values. Useful cases often include:

- an ordinary input;
- a boundary value;
- an empty collection, when the contract allows one;
- a second ordinary input that differs from the first.

## Companion tutorial

For another concise explanation, watch Khan Academy's 4:41 **[Functions | Intro to CS — Python](https://www.youtube.com/watch?v=UmNKiV7Lekk)**.

It explains code duplication, function definitions, parameters, arguments, return values, function calls, and why functions improve reuse and organization—the same conceptual path used in this class.

---

[Back to the course](https://github.com/EdenHeilprin/technion-096609-python-ai)
