# Class 5 — Loops, Counters, and Totals

Today you will use one loop to process every item in a list. You will trace how variables change from one iteration to the next, then use the same pattern to count responses and calculate totals.

## By the end of class

You should be able to:

- read and write a `for` loop that processes a list in order;
- explain the roles of the loop variable, loop body, and indentation;
- trace the value of a variable across several iterations;
- use a counter to record how many items meet a condition;
- use a running total to combine numeric values;
- place an `if` statement inside a loop.

## Get the files for this class

1. [Download the Class 5 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/agent/class-05-structure/class-05/class-05-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-05`. On Windows, it may appear inside an additional folder named `class-05-files`.
3. Move `class-05` into your local course folder, next to `class-00-setup`, `class-01`, `class-02`, `class-03`, and `class-04`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-05`.

If your course folder already contains `class-05`, you do not need to download it again.

## Rehearsal — make one deliberate Class 4 change

Create a new Python file inside `class-05` named `class_05_rehearsal.py` and enter this code:

```python
trials_completed = 5

if trials_completed >= 6:
    print("Session complete")
else:
    print("More trials required")
```

Before running the program:

1. predict its output;
2. change only the value assigned to `trials_completed` so that the other message will appear;
3. run both versions.

<details>
<summary>Check one possible change</summary>

The original value `5` displays `More trials required`. Changing the first line to the following makes the condition `True`:

```python
trials_completed = 6
```

The program then displays `Session complete`.

</details>

## A loop processes one item at a time

A **loop** repeats a block of code. This `for` loop visits each value in `response_times`, in order:

```python
response_times = [1200, 700, 1500]

for response_time in response_times:
    print("Current response time:", response_time)

print("All response times processed")
```

Read the loop header from left to right: **for each `response_time` in `response_times`**.

- `response_times` is the complete list.
- `response_time` is the **loop variable**. It holds one current item at a time.
- `in` connects the current item to the list being processed.
- The colon `:` begins the **loop body**.
- The indented line belongs to the loop and runs once for each item.
- The final unindented line runs once, after the loop finishes.

One pass through the loop body is called an **iteration**. This list contains three items, so the loop has three iterations.

## Activity 1 — predict and run a list loop

Open [`loop_demo.py`](loop_demo.py). Before running it, write the three response times in the order you expect them to appear. Also predict where the final message will appear.

<details>
<summary>Check your prediction</summary>

```text
Current response time: 1200
Current response time: 700
Current response time: 1500
All response times processed
```

The loop follows the list order. The unindented final `print()` runs only after all three iterations.

</details>

Run the file. Then:

1. change `700` to `800`;
2. add `response_times.append(950)` immediately before the loop;
3. predict the new output;
4. run the file again.

The loop itself does not need to change when the list changes.

## A counter remembers how many

A **counter** is a variable that records how many times something happens.

```python
left_count = 0

for response in responses:
    if response == "left":
        left_count = left_count + 1
```

The pattern has three parts:

1. **Initialize** the counter once, before the loop.
2. **Check** the current item during each iteration.
3. **Update** the counter when the condition is `True`.

In `left_count = left_count + 1`, Python first reads the current value on the right, adds `1`, and stores the new value back in the same variable.

## Activity 2 — trace a conditional counter

Open [`response_counter.py`](response_counter.py). Do not run it yet. Complete this trace table on paper or in a text file:

| Iteration | Current `response` | `left_count` after this iteration |
| ---: | --- | ---: |
| 1 | `"left"` | |
| 2 | `"right"` | |
| 3 | `"left"` | |
| 4 | `"left"` | |

<details>
<summary>Check the completed trace</summary>

| Iteration | Current `response` | `left_count` after this iteration |
| ---: | --- | ---: |
| 1 | `"left"` | `1` |
| 2 | `"right"` | `1` |
| 3 | `"left"` | `2` |
| 4 | `"left"` | `3` |

The counter changes only when the current response equals `"left"`.

</details>

Run the file and compare its final output with your trace. Then change the final response from `"left"` to `"right"`. Predict the new count before running the file again.

## A running total remembers how much

A **running total** is a variable that accumulates numeric values across iterations.

```python
total_points = 0

for points in trial_points:
    total_points = total_points + points
```

A counter usually adds `1`. A running total adds the current value. Both are examples of an **accumulator**: a variable that stores a result as it is gradually built.

## Activity 3 — follow a running total

Open [`running_total.py`](running_total.py). The program displays the total after every iteration.

Before running it, predict the four running totals and the final total.

<details>
<summary>Check the totals</summary>

```text
Running total: 4
Running total: 7
Running total: 12
Running total: 14
Final total: 14
```

Each iteration starts with the total left by the preceding iteration.

</details>

Run the file. Change the first value in `trial_points` from `4` to `6`, predict all five output lines, and run it again.

## Activity 4 — build a response-time summary

Create a new Python file inside `class-05` named `response_time_summary.py`.

Start with this list of response times in milliseconds:

```python
response_times = [1200, 700, 1500, 900, 1100]
```

Write a program that:

1. initializes `total_response_time` and `fast_response_count` to `0`;
2. uses one `for` loop to process every response time;
3. adds every response time to `total_response_time`;
4. counts a response as fast when it is less than or equal to `1000` milliseconds;
5. prints both final results after the loop.

Your output should be:

```text
Total response time: 5400
Fast responses: 2
```

Try to write and test the program before revealing an example.

<details>
<summary>Check one possible version</summary>

```python
response_times = [1200, 700, 1500, 900, 1100]

total_response_time = 0
fast_response_count = 0

for response_time in response_times:
    total_response_time = total_response_time + response_time

    if response_time <= 1000:
        fast_response_count = fast_response_count + 1

print("Total response time:", total_response_time)
print("Fast responses:", fast_response_count)
```

</details>

Change the list to `[1000, 1001]`. Before running the program, predict both final results.

<details>
<summary>Check the second test</summary>

```text
Total response time: 2001
Fast responses: 1
```

The value `1000` is included because the condition uses `<=`. The value `1001` is not counted as fast.

</details>

## Compare two implementations with AI

Restore the original list in `response_time_summary.py`. Open a new AI chat, paste the following prompt, and then paste your complete program:

> I wrote the beginner Python program below to calculate the total response time and count response times no greater than 1000.
>
> Suggest one shorter implementation that produces exactly the same two output lines for any list of integer response times.
>
> - Keep an explicit `for` loop for counting the fast responses.
> - You may replace the total-calculation steps with one relevant built-in function.
> - Do not use list comprehensions, user-defined functions, imports, `while`, `break`, or `continue`.
> - Show the revised code, then explain the change in no more than three bullets.
>
> My code appears below.

Inspect the suggestion. It should replace the running-total calculation with `sum(response_times)` while retaining a loop for the conditional count.

1. Predict whether the original and revised programs will produce the same results.
2. Run both programs with the original list.
3. Run both programs with `[1000, 1001]`.
4. Confirm or reject the claim that the implementations are equivalent for these tests.
5. Decide which version makes the step-by-step accumulation easier to see, and which is shorter.

<details>
<summary>Compare with one likely shorter version</summary>

```python
response_times = [1200, 700, 1500, 900, 1100]

total_response_time = sum(response_times)
fast_response_count = 0

for response_time in response_times:
    if response_time <= 1000:
        fast_response_count = fast_response_count + 1

print("Total response time:", total_response_time)
print("Fast responses:", fast_response_count)
```

`sum(response_times)` is a built-in shortcut that adds the numeric values in the list. The explicit accumulator is longer, but it exposes every update and therefore helps us understand how the total is built.

</details>

## Class 5 reference

### Central terms

| Term | Simple meaning | Example |
| --- | --- | --- |
| Loop | Code that repeats a block | `for response in responses:` |
| `for` loop | A loop that processes items from a collection | `for score in scores:` |
| Loop variable | The variable holding the current item | `score` |
| Loop body | The indented code repeated during each iteration | The lines below the loop header |
| Iteration | One pass through the loop body | Processing one response time |
| Initialize | Give a variable its starting value before repetition begins | `count = 0` |
| Update | Replace a variable's value with a new value | `count = count + 1` |
| Counter | A variable that records how many times something happens | Number of fast responses |
| Running total | A variable that adds values over time | Total response time |
| Accumulator | A variable that stores a result as it is built | A counter or running total |

### Read a loop header

```python
for response_time in response_times:
```

Read it as: **for each `response_time` in `response_times`**.

A useful naming pattern is:

- plural name for the list: `response_times`;
- singular name for one current item: `response_time`.

### Before, inside, and after the loop

```python
total = 0                  # once, before the loop

for value in values:
    total = total + value  # once per item

print(total)               # once, after the loop
```

Indentation determines whether a line runs once or repeats. Initializing `total` inside the loop would reset it during every iteration.

### Counter and running-total patterns

| Goal | Starting value | Update inside the loop |
| --- | ---: | --- |
| Count matching items | `count = 0` | `count = count + 1` |
| Add numeric items | `total = 0` | `total = total + current_value` |

If the list is empty, the loop body runs zero times. A counter or total initialized to `0` therefore remains `0`.

### Explicit process and built-in shortcut

These two versions can produce the same total:

```python
total = 0
for value in values:
    total = total + value
```

```python
total = sum(values)
```

The explicit loop shows the state change on every iteration. `sum()` expresses the completed operation more concisely. Understanding the explicit version makes it easier to inspect the shortcut and verify AI-generated alternatives.

## Companion tutorial

For a concise explanation of the exact list loop used in this class, watch the final two-minute segment of Khan Academy's **[List iteration | Intro to CS — Python](https://www.youtube.com/watch?v=jNjRP0tVY5s&t=170s)**, beginning at `2:50`.

The segment explains the `for`/`in` structure, the loop variable, descriptive singular names, and how Python visits each list item in order.
