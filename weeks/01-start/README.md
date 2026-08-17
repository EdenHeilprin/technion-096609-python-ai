# Class 1 — one file, one run, one deliberate change

Welcome to your first Python class. No previous programming experience is required.

## Before class

1. Follow the [Windows setup](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/resources/setup/windows.md) or [macOS setup](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/resources/setup/macos.md).
2. Download and unzip [the complete Class 1 materials](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/main/weeks/01-start/week-01-materials.zip).
3. Open the extracted week-01-materials folder in VS Code.
4. Run setup/verify_setup.py.
5. Complete the Moodle access survey.

Do not spend hours troubleshooting alone. Use Moodle Technical Help. A [browser fallback](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/resources/setup/browser-fallback.md) is available and requires no installation or paid AI account.

## By the end of class, you can

- identify the source file, editor, Python interpreter, and output;
- run a Python file in VS Code or the browser fallback;
- predict and test one small code change;
- read the final line of a simple NameError and repair it;
- explain why a program that runs can still be wrong;
- check a small synthetic behavioral-data summary.

## Class files

- [First complete example](examples/reaction_time_summary.py)
- [Core-practice starter](starter/first_research_script.py)
- [Public self-check](checks/check_first_research_script.py)
- [Setup check](setup/verify_setup.py)
- [Browser-fallback notebook](fallback/week_01_browser_fallback.ipynb)
- [Student handout](student-handout.md)
- [Troubleshooting guide](troubleshooting.md)
- Class slides: linked here after the final instructor rehearsal

## The learning loop

> locate the file → predict → run → inspect → change → rerun → explain

### First run

Open examples/reaction_time_summary.py and run it.

Expected output:

    Participant: SYN001
    Condition: gain
    Mean reaction time (ms): 500.0

### Predict and change

Before each run:

1. change trial_2_ms from 510 to 540 and predict the new mean;
2. restore 510;
3. change condition from “gain” to “loss” and predict which output line changes;
4. restore “gain.”

### Read the first traceback

Remove the quotation marks around gain. Run the file and read the final error line.

Ask:

- Which name did Python try to find?
- Did we mean a variable name or text?
- What is the smallest repair?

Restore the quotation marks and rerun.

## Core practice

Open starter/first_research_script.py.

Complete both TODO calculations:

1. mean reaction time from the three trial variables;
2. accuracy as correct trials divided by total trials, rounded to two digits.

Required output:

    Participant: SYN001
    Condition: gain
    Mean reaction time (ms): 500.0
    Correct trials: 2 of 3
    Accuracy rate: 0.67

Run the program:

    python starter/first_research_script.py

Then run the public check:

    python checks/check_first_research_script.py

The demonstrated command may be python3 on macOS. The VS Code Run button is also valid.

## AI learning target

AI tools are permitted. No individual paid account is required in Class 1.

Ask an available tool for a bounded explanation:

> I am a Python beginner. Explain the final line of this traceback in plain language. Give two possible causes, but do not rewrite the whole program.

Then:

1. decide which cause matches the actual line;
2. predict the effect of one repair;
3. make only that change;
4. rerun;
5. use the output as evidence.

Never paste credentials, identifiable data, confidential research material, or private repository content into an AI chat.

## Submit

Submit first_research_script.py through Moodle. Moodle contains the authoritative deadline and submission activity.

Before submitting:

- reopen the file;
- run it once more;
- run the public check;
- compare all five output lines;
- confirm that the file contains only synthetic data.

## Optional stretch

Add a fourth trial and update the result. List every line you had to change. Later classes introduce structures and loops that reduce this repetition.
