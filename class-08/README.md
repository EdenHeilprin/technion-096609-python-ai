# Class 8 — Working with Codex

Today you will use Codex as a coding agent on a small decision-making research project. The goal is not merely to obtain working code. You will define the task, control the folder and permissions, inspect the proposed plan, review every change, run tests, and correct or revert an unwanted edit.

## By the end of class

You should be able to:

- open a bounded local project in Codex;
- distinguish an ordinary AI chat from a coding agent that can inspect, edit, and run project files;
- give the agent useful context, a precise goal, scope limits, and success checks;
- ask for a plan before authorizing changes;
- choose read-only or editing permissions for the current task;
- inspect a code diff rather than relying only on the agent's summary;
- rerun tests and add an independent check;
- steer a correction or revert a change you do not want.

## Before class — prepare Codex

Install the [ChatGPT desktop app](https://learn.chatgpt.com/docs/quickstart), sign in with a ChatGPT account, and select **Codex** in the app. Codex is included in the [free ChatGPT plan](https://learn.chatgpt.com/docs/pricing); a paid subscription is not required for this class.

You will add the project folder during class.

## Get the files for this class

1. [Download the Class 8 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-08/class-08-files.zip).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-08`. On Windows, it may appear inside an additional folder named `class-08-files`.
3. Move `class-08` into your local course folder, next to `class-00-setup` through `class-07`—not inside any of them.
4. Open the course folder in VS Code. Its Explorer panel should now also show `class-08`.

Use the downloaded ZIP for this class. Its `bonus-project` folder contains the clean local history that Codex uses to display changes; nothing in that history is uploaded anywhere.

## Rehearsal — correct one executable expectation

Create a new Python file inside `class-08` named `class_08_rehearsal.py`. The function below should convert points to bonus units and cap the result at 5:

```python
def points_to_bonus(points):
    bonus = points / 100

    if bonus > 5:
        bonus = 5

    return bonus
```

Copy the function, then correct the expected result in this assertion:

```python
assert points_to_bonus(750) == 7.5
```

Add one printed confirmation after the assertion and run the file.

<details>
<summary>Check one possible version</summary>

```python
def points_to_bonus(points):
    bonus = points / 100

    if bonus > 5:
        bonus = 5

    return bonus


assert points_to_bonus(750) == 5
print("Rehearsal test passed")
```

</details>

## A coding agent works with a project

In an ordinary chat, you provide the code or information you want discussed. A coding agent can work inside a folder that you select: it can inspect related files, propose or make edits, and run commands such as the project's tests.

That added ability makes three choices important:

| Choice | Question to answer |
| --- | --- |
| Project | Which folder may the agent inspect and change? |
| Permission | Should this task be read-only, or may the agent edit and run code? |
| Evidence | What output, tests, and changed lines will show that the task is complete? |

For this class, open only the `class-08/bonus-project` folder as the Codex project. This keeps the task separate from your other course files.

## The project has four pieces of context

Open `bonus-project` in VS Code and inspect its contents:

| File | Role |
| --- | --- |
| [`PROJECT.md`](bonus-project/PROJECT.md) | Describes the current rule and the requested change |
| [`bonus_rules.py`](bonus-project/bonus_rules.py) | Defines `points_to_bonus` |
| [`run_bonus.py`](bonus-project/run_bonus.py) | Calls the function with several point totals |
| [`test_bonus_rules.py`](bonus-project/test_bonus_rules.py) | Records executable expectations |

The line below appears at the top of the two runnable files:

```python
from bonus_rules import points_to_bonus
```

It makes the function defined in `bonus_rules.py` available in the current file. You do not need to write imports independently today; you only need to recognize which file supplies the function.

## Activity 1 — establish the baseline, then ask for inspection

Before opening Codex, use VS Code to run `test_bonus_rules.py`. It should display:

```text
All bonus-rule tests passed
```

Then run `run_bonus.py` and predict its three output lines before revealing them.

<details>
<summary>Check the baseline output</summary>

```text
250 points -> 2.5 bonus units
500 points -> 5.0 bonus units
750 points -> 7.5 bonus units
```

The baseline is internally consistent, but it does not yet implement the requested maximum of 5 units.

</details>

In the ChatGPT desktop app, select **Codex** and add `bonus-project` as a local project. If the app presents an **Add** menu, choose **Files and folders** and select that folder.

Type `/permissions` and choose **Read only**. Then send:

> Inspect this project without changing any files. State the purpose of each file, trace what happens when `run_bonus.py` processes 750 points, list the test cases that already exist, and state which two files you would run to verify the current project.

Compare the response with the files and the output you already observed. A useful inspection should identify the missing cap without claiming that the current tests fail.

<details>
<summary>What a sound inspection should notice</summary>

- `PROJECT.md` requests a maximum bonus of 5 units.
- `bonus_rules.py` currently returns `points / 100` without applying that maximum.
- `run_bonus.py` therefore displays `7.5` for 750 points.
- The existing tests cover 0, 250, and 500 points, but no value above 500.
- `test_bonus_rules.py` and `run_bonus.py` are the two files to execute.

</details>

## A reviewable agent workflow

Use this loop for a bounded coding change:

1. **Inspect** the project and reproduce its current behavior.
2. **Specify** the goal, relevant context, scope limits, and success checks.
3. **Plan** the smallest justified change before editing.
4. **Authorize** the agent to work within the selected project.
5. **Review** the diff—the exact lines added and removed.
6. **Test** the changed behavior and related existing behavior.
7. **Correct or revert** anything that is unsupported or outside the task.

The agent's explanation is useful context. The diff and executed results are evidence.

## Activity 2 — turn a request into an inspectable task

Read the eight requirements in `PROJECT.md`. Imagine giving the agent only this request:

> Fix the bonus code.

Write down at least three decisions that this request leaves unclear. Then draft a better request that tells the agent:

- where the authoritative requirements are;
- what it should inspect before editing;
- which familiar Python structures it may use;
- what names or output must remain unchanged;
- which tests it must add and run;
- what documentation should help a reader understand;
- whether it should begin editing immediately.

<details>
<summary>Check a precise task request</summary>

> Read `PROJECT.md` and inspect all three Python files. Propose the smallest plan that satisfies every requirement. Keep the public function name, parameter name, `run_bonus.py`, and its output labels unchanged. Use the familiar arithmetic, comparison, `if`, assignment, and `return` approach rather than introducing a shortcut. Add a concise function docstring explaining the conversion and maximum; do not add comments that merely restate individual lines. Add the required above-cap assertion, then run `test_bonus_rules.py` and `run_bonus.py`. Before editing, show me the plan and wait for my confirmation.

This request is effective because the result and its verification are explicit. It does not prescribe every line of the implementation.

</details>

## Activity 3 — authorize, review, and verify the change

Type `/permissions` and choose **Auto**, which allows Codex to edit and run code inside the selected project. Send the precise task request above.

Do not approve the plan merely because it sounds confident. Check that it intends to:

1. modify `bonus_rules.py`;
2. add an above-cap assertion to `test_bonus_rules.py`;
3. add one useful docstring to `points_to_bonus` without comment clutter;
4. leave `run_bonus.py` unchanged;
5. run both Python files.

If the plan matches the task, reply:

> Proceed with that plan. Keep the scope minimal and report the files changed and the verification results.

When Codex finishes, open the **Changes** or review pane. If a scope selector is shown, choose **Last turn**. Inspect the diff line by line.

Your diff should show:

- a comparison and capped assignment inside `points_to_bonus`;
- an assertion that 750 points return 5;
- no change to `run_bonus.py`;
- no unrelated new files.

<details>
<summary>Check one valid implementation</summary>

```python
def points_to_bonus(points):
    """Convert points to bonus units, with a maximum of 5 units."""
    bonus = points / 100

    if bonus > 5:
        bonus = 5

    return bonus
```

One required new test is:

```python
assert points_to_bonus(750) == 5
```

</details>

Now return to VS Code and independently run both files. The final runner output should be:

```text
250 points -> 2.5 bonus units
500 points -> 5.0 bonus units
750 points -> 5 bonus units
```

Add these two assertions yourself to `test_bonus_rules.py` and rerun it:

```python
assert points_to_bonus(499) == 4.99
assert points_to_bonus(501) == 5
```

These neighboring cases check both sides of the boundary rather than repeating the same kind of example.

## Activity 4 — inspect and revert an unwanted change

Send Codex this deliberately temporary request:

> In `run_bonus.py`, change only the output label `bonus units` to `payment`. Make no other change.

Open the review pane and select **Last turn**. Confirm that the diff contains exactly one changed line in `run_bonus.py`.

The label change is outside the approved project requirement. Use the review pane to **revert** the change to `run_bonus.py`. Then run `run_bonus.py` in VS Code and confirm that:

- the original `bonus units` label is restored;
- the 5-unit cap still works;
- your two independent assertions still pass.

Reverting is not a failure. It is how you keep a correct project state after inspecting a change you do not want.

## Class 8 reference

### Central terms

| Term | Simple meaning |
| --- | --- |
| Coding agent | An AI system that can inspect and act on files and commands within a selected project |
| Project or workspace | The folder that supplies the agent's local code and context |
| Scope | The files, behavior, and boundaries included in the requested task |
| Requirement | A condition the completed change must satisfy |
| Acceptance check | Executable or observable evidence that a requirement is met |
| Plan | The proposed sequence of work before files are changed |
| Diff | The exact lines added, removed, or replaced relative to the earlier project state |
| Read-only | Permission to inspect without changing files |
| Auto | Permission for Codex to edit and run code inside the selected project |
| Revert | Restore an earlier file state by discarding a selected change |

### Context can live in files

A project document such as `PROJECT.md` can record the goal, file roles, constraints, and success checks once. The task request can then tell the agent to read that source rather than repeating every detail from memory.

### A precise request is not necessarily long

A useful task request answers four questions:

1. What result is required?
2. What existing context should be inspected?
3. What must remain unchanged?
4. What evidence will demonstrate success?

### Review both behavior and scope

A program may pass its tests while still containing an unnecessary file or label change. Review asks two different questions:

- Does the new behavior satisfy the requirements?
- Did the agent change only what the task justified?

### Verification is independent

If the agent says that tests passed, rerun them yourself. Add at least one meaningful case that was not the agent's only evidence. Here, `499` and `501` check the two sides of the cap boundary.

## Companion tutorial

Watch OpenAI's 4:21 **[Introducing the Codex app](https://www.youtube.com/watch?v=HFM3se4lNiw)**.

The tour shows projects, agent tasks, progress, diff review, line-specific feedback, and running the result. This class applies that same cycle to a much smaller project whose complete code and tests you can inspect yourself.

For current interface guidance, use OpenAI's [desktop-app quickstart](https://learn.chatgpt.com/docs/quickstart) and [code-review guide](https://learn.chatgpt.com/docs/code-review).
