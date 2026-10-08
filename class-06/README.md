# Class 6 — Functions, Parameters, and Return Values

At the end of a game, you need to convert each participant's points into a bonus payment. Instead of copying the same calculation for every participant, you can write it once as a **function** and reuse it. If the payment rule changes, you update it in one place.

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

## Write the payment rule once, use it for every participant

The game pays **10 pence for each point**. Two participants earned 12 and 25 points. This function calculates and displays a bonus for either score:

```python
def show_bonus(points):
    bonus_pence = points * 10
    print("Bonus (pence):", bonus_pence)

show_bonus(12)
show_bonus(25)
```

A **function** is a named, reusable block of instructions. The first three lines form its **definition**:

- `def` begins the definition, and `show_bonus` is the function name.
- `points` is a **parameter**: a name for the information this function receives.
- The colon `:` starts the body; the indented lines are the instructions that belong to it.

The final two lines are **function calls**. Each call supplies a score and runs the same calculation. For another participant, add another call—not another copy of the calculation and output code.

A definition tells Python how to perform the task; a call tells it to perform the task now. Reading the definition alone does not run its body.

### Parameter versus argument

| Term | Where it appears | Example |
| --- | --- | --- |
| Parameter | In the definition; a name for incoming information | `points` |
| Argument | In a call; the value or expression supplied | `12` in `show_bonus(12)` |

During `show_bonus(12)`, `points` has the value `12`. During `show_bonus(25)`, it has the value `25`. The definition stays the same.

## Activity 1 — calculate bonuses for different participants

Open [`function_call_demo.py`](function_call_demo.py). Predict its output before running it.

<details>
<summary>Check your prediction</summary>

```text
Bonus (pence): 120
Bonus (pence): 250
```

Python first reads the definition. The first call then uses 12 points; the second uses 25 points.

</details>

Run the file, then add `show_bonus(8)` for a third participant. Predict the new bonus and run it again.

What would happen if the file contained only the definition, with no calls? Test this by temporarily placing `#` at the beginning of each call line, then restore the calls.

## A docstring records the function's job

We can document the payment function's job with a **docstring** immediately after its header:

```python
def show_bonus(points):
    """Display the bonus in pence at 10 pence per point."""
    bonus_pence = points * 10
    print("Bonus (pence):", bonus_pence)
```

Use `#` comments to explain individual lines or choices. A **docstring** uses triple quotes as the first statement in a function and describes the function as a whole; Python also makes it available through `help()`. Neither prints a message when you call the function.

A function's **contract** is its agreement with the caller: what it accepts and what it does or returns. A useful docstring summarizes that agreement.

## Activity 2 — change the payment rule in one place

Open [`parameter_demo.py`](parameter_demo.py). It contains the documented function and calls for scores of `12`, `25`, and `8`.

For the next game, the rate increases to **15 pence per point**. Change the calculation inside the function and update its docstring to match. Leave all three calls unchanged.

Predict the new bonuses, then run the program.

<details>
<summary>Check the complete output</summary>

```text
Bonus (pence): 180
Bonus (pence): 375
Bonus (pence): 120
```

One change to the calculation updates all three bonuses. The payment rule lives in the function; the calls provide the different scores.

</details>

## A returned value leaves the function

Our payment function displays a bonus. If we wanted to add that bonus to a participation fee, the rest of the program would need the calculated number—not just a printed message. The `return` statement sends a value back to the line that called the function.

The same idea applies to a response-time label that another part of an experiment needs:

```python
def classify_response_time(response_time):
    """Return `fast` for times at or below 1000 ms; otherwise return `slow`."""
    if response_time <= 1000:
        speed_label = "fast"
    else:
        speed_label = "slow"

    return speed_label

label = classify_response_time(850)
print("Speed:", label)
```

Read the call from right to left:

1. `850` is passed into the parameter `response_time`.
2. The function chooses and stores a value in `speed_label`.
3. `return speed_label` sends that text back to the caller.
4. The returned text is assigned to `label`.
5. The final line displays the stored result.

`return` and `print()` are not interchangeable:

| Operation | What it does |
| --- | --- |
| `return value` | Sends a value back to the caller so it can be stored or used |
| `print(value)` | Displays a value in the output area |

## Activity 3 — trace two function calls

Open [`return_value_demo.py`](return_value_demo.py). Do not run it yet. Complete the prediction table:

| Call | Argument | Returned value | Variable receiving the result |
| --- | ---: | --- | --- |
| First | `850` | | `first_label` |
| Second | `1200` | | `second_label` |

<details>
<summary>Check the completed table and output</summary>

| Call | Argument | Returned value | Variable receiving the result |
| --- | ---: | --- | --- |
| First | `850` | `"fast"` | `first_label` |
| Second | `1200` | `"slow"` | `second_label` |

```text
First response: fast
Second response: slow
```

</details>

Run the file. Change the first argument to `1000`, predict whether its returned value changes, and run the file again. Then try `1001`.

## Each call has its own local values

The parameter `response_time` and the variable `speed_label` are created inside the function. They have **local scope**: they belong to the current function call.

When the function is called again, Python creates a new local `response_time` and a new local `speed_label`. The first call's values do not become the second call's values. Information enters through arguments and leaves through the returned value.

The variables `first_label` and `second_label` are created outside the function. They preserve the two returned results after the calls finish.

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

## Use AI to build a reusable bonus calculator

Your next experiment records points separately for each trial. You need to turn each participant's list of points into a payment: **10 pence per point**, a maximum bonus of **300 pence**, and a fixed participation fee of **100 pence** on top.

### 1. Describe the task to AI

Open your preferred AI tool. You can write your own request or start with this:

> Write a Python function named `calculate_bonus(trial_points)` for an experiment. Its input is a list of non-negative whole-number points earned on individual trials.
>
> Add the points, convert the total at 10 pence per point, and cap the bonus at 300 pence. Return the bonus as a whole number of pence. An empty list should return 0.
>
> Use one `for` loop with a running total, multiplication, an `if` statement for the cap, and one final `return`. Keep printing outside the function.
>
> Add a concise docstring stating the input, payment rule, and returned value. Include clear English `#` comments explaining each code line and its purpose, so a beginner can understand the code itself.
>
> Below the function, show a call with `[3, 5, 2]`. Store the returned bonus, add a participation fee of 100 pence outside the function, and print both the bonus and the total payment, clearly labeled in pence.

### 2. Read it, then run it

Create `bonus_calculator.py` inside `class-06` and paste the proposed code.

Read its documentation and locate the running total, conversion, cap, and returned value. Check that the participation fee is added **after** the function returns, so it is not included in the bonus cap. Then run it.

### 3. Check the payment rules

Replace the argument in the example call with each list below. Predict the result, run the program, and compare both printed amounts with the table.

| Trial points | Expected bonus (pence) | Total payment including fee (pence) |
| --- | ---: | ---: |
| `[3, 5, 2]` | 100 | 200 |
| `[12, 9, 15]` | 300 | 400 |
| `[10, 20]` | 300 | 400 |
| `[]` | 0 | 100 |

## Class 6 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Function | A named block of instructions that performs a task | `count_fast_responses` |
| Function definition | The code that teaches Python the task | `def count_fast_responses(response_times):` |
| Function header | The first line of a definition | The line beginning with `def` |
| Function body | The indented instructions belonging to the function | The loop and `return` below the header |
| Function call | An instruction to perform the function now | `count_fast_responses(session_a)` |
| Parameter | A name for incoming information in the definition | `response_times` |
| Argument | An actual value supplied in a call | `session_a` |
| Return value | The result sent back to the caller | The final count |
| Local scope | The region inside one function call where its parameters and variables exist | `fast_count` inside the function |
| Contract | A concise description of expected inputs, behavior, and returned result | “Returns the number of times at or below 1000” |
| Docstring | A concise description placed inside a function to record its purpose or contract | `"""Return the number of fast responses."""` |

### Definition and call

```python
def classify_response_time(response_time):
    """Return `fast` for times at or below 1000 ms; otherwise return `slow`."""
    if response_time <= 1000:
        speed_label = "fast"
    else:
        speed_label = "slow"

    return speed_label


label = classify_response_time(850)
```

The definition describes a reusable task. The call supplies one argument and receives one returned value.

### Information flow

```text
argument → parameter → function body → return value → receiving variable
   850   → response_time → classify →   "fast"    → label
```

Each call follows the same route with its own argument and local values.

### `return` versus `print()`

```python
def double_points(points):
    return points * 2


doubled = double_points(4)
print(doubled)
```

The function returns `8`; the final line chooses to display it. Because the result was returned, the rest of the program could instead store it, compare it, or use it in another calculation.

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
