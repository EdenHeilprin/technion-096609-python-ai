# Week 01 — Start: VS Code, GitHub, and first Python

## Why this matters

Research code becomes much less mysterious once you can identify the file, run it, observe what it does, and make one deliberate change. This meeting establishes that complete loop before we add more Python concepts or ask an agent to work across a project.

## By the end of this meeting, you can

- identify the editor, Python interpreter, source file, terminal, and program output;
- run a `.py` file in the supported VS Code setup;
- use variables, basic arithmetic, and `print()` to summarize synthetic behavioral data;
- predict the effect of a small edit, run it, and explain the observed result;
- read the useful final line of a simple `NameError` and repair the cause;
- explain the difference between receiving an AI suggestion and verifying that it works.

## Before class — about 10 minutes

1. Complete the short operating-system and access survey in Moodle.
2. Open the course setup page and follow the supported path as far as you can.
3. Bring the computer you expect to use for the course.

Do not spend hours troubleshooting alone. A zero-install fallback will be available in the first meeting, and setup issues belong in the Moodle Technical Help forum.

## Files for this week

- [`examples/reaction_time_summary.py`](examples/reaction_time_summary.py) — the first complete program.
- [`starter/first_research_script.py`](starter/first_research_script.py) — the core practice file you will edit.
- [`checks/check_first_research_script.py`](checks/check_first_research_script.py) — a public self-check.

## In class

### 1. Orient: file → interpreter → output

Open `reaction_time_summary.py`. Before running it, find:

- a text value;
- a number;
- a variable name;
- an arithmetic expression;
- a line that displays a result.

Run the file from VS Code. The important first success is not memorizing the button: it is knowing which file ran and where its output appeared.

### 2. Predict → run → explain

Without running again, predict what will happen after each change:

1. Change `trial_2_ms` from `510` to `540`.
2. Change `condition` from `"gain"` to `"loss"`.
3. Remove the quotation marks around `"gain"`.

Run after each prediction and explain the evidence. Restore the original file when finished.

### 3. Read the first traceback

Removing the quotation marks asks Python to find a variable named `gain`. Because that name has not been defined, Python reports a `NameError`.

For now, use this three-part routine:

1. read the final error line;
2. locate the referenced line in your file;
3. change one plausible cause and run again.

We will learn a more systematic debugging process in Week 7; the habit begins now.

### 4. Meet GitHub without turning it into a second programming language

GitHub is the versioned home of the public course materials. In this meeting you need only be able to:

- open the course repository;
- navigate to a week;
- download or clone the materials using the demonstrated route;
- recognize that the history records intentional changes.

Creating branches and resolving merge conflicts are not Week 1 learning outcomes.

## Core practice — First Research Script

Open `starter/first_research_script.py`. It contains synthetic data for one fictional participant and three trials.

### Required core

1. Calculate the mean reaction time from the three trial variables.
2. Calculate the proportion of correct trials.
3. Round accuracy to two decimal places.
4. Print the five-line summary shown below.
5. Run the public self-check.

Expected output:

```text
Participant: SYN001
Condition: gain
Mean reaction time (ms): 500.0
Correct trials: 2 of 3
Accuracy rate: 0.67
```

Run the program from the `01-start` folder:

```bash
python starter/first_research_script.py
```

Then run the check:

```bash
python checks/check_first_research_script.py
```

Depending on the operating system and setup, the demonstrated command may be `python3` or the VS Code Run button. Use the course setup page as the authoritative guide.

### Submit

- `first_research_script.py`
- Deadline and submission activity: Moodle

Before submitting, close and reopen the file, run it once more, and compare all five output lines.

## Stretch — optional

Add a fourth trial. Update the calculation and output so the program remains correct without manually typing the mean. Write down every line you had to change; later weeks will give us structures and loops that reduce this repetition.

## AI learning target — ask for an explanation, then test it

All AI tools are permitted. This week, deliberately practise using an available chat tool to explain evidence rather than replace the entire task.

Suggested interaction:

> I am a Python beginner. Explain the final line of this traceback in plain language. Give me two possible causes, but do not rewrite my whole program. [Paste the traceback and the relevant synthetic-data code only.]

Before accepting the explanation:

1. state which cause you think applies;
2. make one small change;
3. rerun the file;
4. decide whether the new output supports the explanation.

Never paste passwords, access tokens, identifiable participant data, confidential research material, or private repository contents into a chat.

## Two-minute reflection

Answer in your own words:

1. What exactly happened between pressing Run and seeing output?
2. What evidence convinced you that your calculation was correct?
3. What can an AI explanation contribute, and what must you still do yourself?

## Get help

- Ask conceptual and logistics questions in the Moodle Course Q&A.
- Share privacy-safe errors in the Moodle Technical Help forum.
- For a technical question, include your operating system, how you ran the file, the full error text, the smallest relevant code, and what you already tried.
