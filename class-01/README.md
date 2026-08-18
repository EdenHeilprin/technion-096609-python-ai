# Class 1 — Your First Python Program

Today you will run a short Python program, understand its basic ingredients, make a deliberate change, and write a few lines yourself.

No previous programming experience is assumed.

AI tools are permitted in this course and will be taught in depth later. Today's programs are intentionally small enough to write and understand directly. You remain responsible for understanding and checking any code you use.

## By the end of class

You should be able to:

- move from the course repository to a Python file in VS Code and run it;
- recognize a value, variable, assignment, and `print()` instruction;
- predict how a small change will affect the output;
- write and run a three-line Python program yourself.

## Get the files for this class

1. [Download the Class 1 files](class-01-files.zip?raw=1).
2. Extract the downloaded ZIP file and locate the resulting folder named `class-01`. On Windows, it may appear inside an additional folder named `class-01-files`.
3. Find the course folder that you used in Class 0. This is the folder that already contains `class-00-setup`.
4. Move the new `class-01` folder into that course folder, **next to** `class-00-setup`—not inside it.
5. Open the course folder in VS Code. Its Explorer panel should now show both `class-00-setup` and `class-01`.

If your course folder already contains `class-01`, you do not need to download it again.

## Activity 1 — run an existing program

Open [`first_program.py`](first_program.py) in VS Code.

Before running it, predict the two lines of output. Then select **Run Python File** and compare the result with your prediction.

```python
participant_name = "Dana"
selected_option = "Option A"

print(participant_name)
print(selected_option)
```

## Four ideas to recognize

| Idea | Working meaning for today | Example |
| --- | --- | --- |
| Value | A piece of information used by the program | `"Dana"` |
| Variable | A name through which the program can refer to a value | `participant_name` |
| Assignment | Associates the name on the left with the value on the right | `participant_name = "Dana"` |
| `print()` | Displays what is placed inside the parentheses | `print(participant_name)` |

Quotation marks tell Python that something is text. For now, read `=` in an assignment as “gets the value.”

## Activity 2 — make a deliberate change

1. Choose a different participant name and option.
2. Predict the new output.
3. Edit the two values in `first_program.py`.
4. Save the file and run it again.
5. Explain what you changed and whether the output matched your prediction.

## Activity 3 — write a program yourself

Create a new Python file inside `class-01` named `my_first_program.py`.

Write three lines that:

1. assign the text `"Risk and Reward"` to a variable named `experiment_name`;
2. display the value of `experiment_name`;
3. display the text `"Ready to begin"`.

Run the file. Your output should be:

```text
Risk and Reward
Ready to begin
```

Next, choose a different experiment name. Predict the output, make the change, save, rerun, and explain the result.

## Optional extension — arithmetic

If time permits, open [`arithmetic_extension.py`](arithmetic_extension.py).

Predict `total_points` before running the file. Then change one number and predict the new result before running it again.

## Before you leave

Check that you can:

- locate the repository, VS Code, a Python file, and its output;
- point to a value, variable, assignment, and `print()` instruction;
- run, change, save, and rerun a Python file;
- write a small Python program yourself.
