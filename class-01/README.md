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

## First five minutes — get the current course files

If your local course folder already contains `class-01`, you are ready. Otherwise:

1. [Download the current course files](https://github.com/EdenHeilprin/technion-096609-python-ai/archive/refs/heads/main.zip).
2. Extract the downloaded ZIP file.
3. Open the newly extracted repository folder in VS Code.

We will do this together at the beginning of class.

## Today's path

### First teaching block

1. **0–5 minutes:** download and open the current course files.
2. **5–12 minutes:** course orientation and our approach to AI.
3. **12–18 minutes:** distinguish the repository, VS Code, a Python file, and output.
4. **18–25 minutes:** open and run the first program.
5. **25–38 minutes:** understand value, variable, assignment, and `print()`.
6. **38–47 minutes:** predict, change, save, and rerun the program.
7. **47–50 minutes:** recap.

### Second teaching block

1. **50–56 minutes:** retrieve the four ideas from the first block.
2. **56–65 minutes:** watch a three-line program being created from an empty file.
3. **65–79 minutes:** write and run your own three-line program.
4. **79–89 minutes:** make one deliberate change and explain its effect.
5. **89–95 minutes:** optional arithmetic extension.
6. **95–100 minutes:** consolidate what you learned.

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
