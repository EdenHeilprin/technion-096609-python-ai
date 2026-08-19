# Class 6 — Functions, Parameters, and Return Values

Today you will package familiar Python instructions into named, reusable functions. You will pass information into a function, return a result, and call the same function with more than one dataset.

## By the end of class

You should be able to:

- distinguish a function definition from a function call;
- define and call a simple function;
- distinguish a parameter from an argument;
- use `return` to send a result back to the caller;
- store and use a returned value;
- explain why parameters and variables created inside a function are local to that call;
- move familiar loop-and-condition logic into a reusable function.

## Get the files for this class

1. [Download the Class 6 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-06-functions/class-06/class-06-files.zip).
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

## A function gives a task a name

A **function** is a named block of instructions that performs a task. We first define the task, then call the function whenever we want Python to perform it.

```python
def show_task_name():
    print("Reaction-time task")

show_task_name()
```

The first two lines form the **function definition**:

- `def` begins a new function definition.
- `show_task_name` is the function name.
- The parentheses `()` hold any parameters. This first function has none.
- The colon `:` begins the function body.
- The indented line is the **function body**.

The final line is a **function call**. A definition teaches Python how to perform the task; a call tells Python to perform it now. The function body does not run merely because Python reads the definition.

## Activity 1 — predict definition and call order

Open [`function_call_demo.py`](function_call_demo.py). Before running it, predict all three output lines and their order.

<details>
<summary>Check your prediction</summary>

```text
Before the function call
Reaction-time task
After the function call
```

Python stores the function instructions when it reads the definition. The body runs later, when Python reaches `show_task_name()`.

</details>

Run the file. Then add a second call to `show_task_name()` immediately after the first call. Predict the new output before running the file again.

## Parameters make a function reusable

A function becomes more flexible when it receives information through a **parameter**.

```python
def show_trial(stimulus):
    print("Stimulus:", stimulus)

show_trial("circle")
```

The two related terms describe different places:

| Term | Where it appears | Example |
| --- | --- | --- |
| Parameter | In the function definition; a name for incoming information | `stimulus` |
| Argument | In a function call; the actual value supplied | `"circle"` |

During `show_trial("circle")`, the argument `"circle"` becomes the current value of the parameter `stimulus`. A later call can provide a different argument without changing the function definition.

## Activity 2 — call one function with different arguments

Open [`parameter_demo.py`](parameter_demo.py). Predict the output, then run it.

Add this third call:

```python
show_trial("triangle")
```

Next, add the following line inside the function body, immediately below its existing `print()` line:

```python
print("Respond now")
```

Predict the complete output before running the program again. One change to the function body should affect all three calls.

<details>
<summary>Check the complete output</summary>

```text
Stimulus: circle
Respond now
Stimulus: square
Respond now
Stimulus: triangle
Respond now
```

The function is defined once but called three times. Each call supplies its own argument.

</details>

## A returned value leaves the function

Some functions display an action. Other functions calculate a result that the rest of the program needs. The `return` statement sends a value from the function back to the line that called it.

```python
def classify_response_time(response_time):
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

## Review a function contract with AI

A **function contract** states what callers may provide and what the function promises to return or do. Use your completed `count_fast_responses` function for this contract review.

Open a new AI chat. Paste the following prompt, followed by your complete function definition:

> Review the Python function below against this contract:
>
> - Its exact name is `count_fast_responses`.
> - It accepts one list of integer response times.
> - It returns the number of values less than or equal to `1000`.
> - It returns `0` for an empty list.
> - It does not print anything.
> - It does not change the supplied list.
>
> For each requirement, report `Met` or `Not met` and cite the specific line or behavior that supports your judgment. Do not rewrite the function if every requirement is met. If one is not met, show only the smallest necessary change.
>
> My function appears below.

Check the review against the code yourself. Then run these calls and compare the actual values with the contract:

```python
print(count_fast_responses([1200, 700, 900]))
print(count_fast_responses([1000, 1001]))
print(count_fast_responses([]))
```

The expected values are `2`, `1`, and `0`. If the review and the executed results disagree, the executed evidence determines whether the function met the tested requirement.

<details>
<summary>What a sound review should notice</summary>

For the example implementation:

- the function name and single parameter match the contract;
- the counter increases only for values satisfying `<= 1000`;
- the returned result is an integer count;
- an empty list leaves the counter at `0`;
- there is no `print()` inside the function;
- the loop reads values from the list but never assigns to an index or calls a method that changes it.

The three executed tests do not prove correctness for every possible list, but they provide direct evidence for an ordinary case, the boundary, and the empty-list case.

</details>

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

### Definition and call

```python
def classify_response_time(response_time):
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
