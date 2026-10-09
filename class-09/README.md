# Class 9 — Build Your First Experiment with Codex

In Class 8, you saw a research workflow carried out with Codex. Today, you direct one yourself: turn a short study specification into an experiment that runs in a browser and records a participant's choice.

Your first version asks one question: **would you prefer 4 points for sure, or a 50% chance of 10 points and a 50% chance of 0?** These are hypothetical points. There is no correct answer; the experiment records a preference.

By the end, you will have a working oTree project, a checked response in an exported file, and a clear understanding of where the page, study rules, and recorded answer come from.

## Get your workspace ready

1. [Download the Class 9 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-09/class-09-files.zip).
2. Extract the ZIP. Find the `class-09` folder inside it and place it in your local course folder. If you already have a `class-09`, keep that folder and give this new copy a different name, such as `class-09-review`.
3. In VS Code, choose **File → Open Folder** and open this download's `research-project` folder—not the whole course folder or just `experiment`.
4. Complete the short [setup guide](SETUP.md). It covers Codex access, selecting this local project, and running `setup_environment.py` followed by `check_environment.py`.

The project has its own `.venv`, a folder holding its Python environment. The setup does not replace your existing Python installation. Use the project's Python environment as explained in the setup guide.

You will work in this structure:

```text
class-09/
├── README.md
├── BUILD_BRIEF.md
├── SETUP.md
├── research-project/           ← open this folder in VS Code and Codex
│   ├── PROJECT.md
│   ├── AGENTS.md
│   ├── setup_environment.py
│   ├── check_environment.py
│   ├── run_experiment.py
│   ├── experiment/             ← the browser experiment goes here
│   ├── data/                   ← exported responses go here
│   └── docs/BUILD_BRIEF.md      ← the task Codex will implement
└── checkpoints/minimal/research-project/
```

The starter contains the project setup and a build brief, **not a finished experiment**. You will ask Codex to build it. The checkpoint is a separate working example if you need it later.

## 1. Define the task before generating code

Read [the build brief](BUILD_BRIEF.md). It says what the participant should see, what must be recorded, and how you will check the result.

Then begin a Codex chat attached to your `research-project` folder. Send:

> Read `PROJECT.md`, `AGENTS.md`, and `docs/BUILD_BRIEF.md`, then inspect the starter files. Explain your plan for building this one-choice oTree experiment. Identify the files you need to create or change and how you will verify that a submitted answer is recorded. Do not edit yet. Ask me if a requirement is genuinely unclear.

Check the plan against the brief. You are looking for **one choice page followed by a final acknowledgement**, not a larger study.

Three ideas will help you follow the plan:

| Part | Its job in this project |
| --- | --- |
| Python | Defines the study settings, available responses, saved fields, and page order. |
| HTML template | Defines the text and form that a participant sees in the browser. |
| oTree | Connects those pages to participant records and saves submitted responses. |

The familiar Python ideas still matter. The answers are strings, the offer is a number, a list gives the page order, and functions provide information for the page or export.

## 2. Delegate the build

Once the plan matches the brief, send:

> Implement the plan for the `minimal-v1` study in `experiment/`, using the existing pinned oTree environment. Follow `docs/BUILD_BRIEF.md` exactly. Add concise English `#` comments explaining the Python lines, concepts, and functions so a beginner can follow them; explain the HTML with appropriate HTML comments. Keep the provided environment helpers and package versions unchanged. Run the checks you can perform, report their actual results, and tell me which browser checks remain for me. Stop after this minimal version works.

Watch the work: Codex is creating files in your project, not merely displaying code for you to copy. When a permission request appears, read the requested action and location before approving it. Keep the normal project-scoped permissions; this task does not need unrestricted computer access.

When Codex finishes, look for these files in VS Code:

- `experiment/settings.py`: the session configuration named `sure_or_gamble`.
- `experiment/choice_task/__init__.py`: the study's Python logic and saved fields.
- `experiment/choice_task/Choice.html`: the participant's choice page.
- `experiment/choice_task/ThankYou.html`: the final acknowledgement.

Inspect Codex's change summary alongside the files. If a detail is unclear, select a short section and ask what it does in this experiment.

## 3. Run it as a participant

1. In VS Code, open `run_experiment.py` in the root of `research-project` and choose **Run Python File**.
2. Leave that terminal running. Open [http://localhost:8000](http://localhost:8000) in your browser. `localhost` means your own computer.
3. In oTree administration, choose **Sessions → Create new session**. Select **Sure or gamble — one decision** (the configuration named `sure_or_gamble` in Python), enter **2 participants**, and choose **Create**.
4. Open the first participant's start link in a new tab. Keep the administration tab open so you can return to it.

Before choosing anything, check that the page describes both options completely. Press the submit button (**Save my choice** in the checkpoint) without choosing: you should remain on the choice page with a request to answer.

Choose the sure option and continue. You should reach the final acknowledgement.

Open the second participant's start link and choose the gamble. Complete that participant too. These two test participants give you known answers to find in the data.

If the page fails, give Codex the **exact error text or a screenshot**, the action you took, and the expected result. For example:

> I ran `run_experiment.py` and opened the first participant link. Instead of the choice page, I see this error: [paste the error]. Find the cause in the existing project, make the smallest necessary fix, and rerun the relevant check. Keep the study specification unchanged.

Use [troubleshooting](TROUBLESHOOTING.md) for environment or server-start problems.

## 4. Find the responses you just recorded

Return to the administration interface and open **Data**. Under **Custom exports**, find **`choice_task (custom_export)`** and choose **CSV**. It is the compact course export, not oTree's wider all-app export.

Save it inside `research-project/data` as `class09_pilot.csv`, then open it in VS Code. CSV is a plain-text table: the first line names the columns and each later line contains a record.

Its header should be:

```text
session_code,participant_code,study_version,round_number,sure_points,gamble_high,gamble_probability,choice,confidence
```

Find the rows belonging to your two participant codes:

| Check | Expected result |
| --- | --- |
| Study version | `minimal-v1` |
| Round | `1` |
| Guaranteed offer | `4` |
| Gamble | High outcome `10`; probability `0.5` |
| First participant's choice | `sure` |
| Second participant's choice | `gamble` |
| Confidence | Blank; this version has no confidence question |

If you created other sessions, the export can contain their records too. Use `session_code` and `participant_code` to identify these two tests. Extra rows are not automatically duplicates.

This closes the first complete loop: **a requirement became a page, a participant used it, and the answer became data.** A good-looking page alone would not establish that the experiment works.

## 5. Connect the page to its Python

Open `experiment/choice_task/__init__.py` and find the saved field named `choice`, then the page class named `Choice`. oTree uses `class` blocks to organize the app. For today, read them as labeled sections with different jobs:

- `C`: study constants, such as the number of rounds.
- `Player`: fields saved for one participant in one round.
- `Choice`: the page that collects a response.

In `Choice`, look for:

```python
form_model = 'player'
form_fields = ['choice']
```

Together, these tell oTree that the page submits the `choice` field to that participant's record. In `Choice.html`, find the form that displays it.

Then find `page_sequence`. Its list determines the page order. Follow the path from the `choice` field to the form, then back to the `choice` column in your exported CSV.

If you get stuck, ask:

> Trace one answer through this project: where is the allowed value `gamble` defined, where does the participant select it, how is it saved, and where does it enter the custom export? Point to the relevant lines and explain them in plain English. Do not edit anything.

## Optional: make one deliberate improvement

If you spotted wording that could be clearer, choose **one improvement** without changing the offers, probabilities, or saved values. If the page is already clear, you can skip this extension.

Describe the specific change to Codex. Inspect the changed text, run the project again if you stopped it, and create a **new test session**. Confirm that the new wording appears and both options still work.

Finally, ask:

> Create `docs/CLASS09_NOTES.md` with a brief record of the implemented study, the files responsible for the page and saved response, my wording change, and the checks we actually completed. Separate executed checks from any checks we have not performed.

You now have a runnable project and a short explanation that another person—or a future Codex chat—can use.

## If you need the working checkpoint

Stop any running server with **Ctrl+C** in its terminal. Open `checkpoints/minimal/research-project` from the Class 9 download as a **separate folder** in VS Code and Codex. Follow `SETUP.md` for that folder, then continue from **Run it as a participant** above.

Your original attempt stays in the first `research-project`. Compare its files with the checkpoint to understand the difference. You can complete the browser tests, response export, and code tracing without a further AI request. For the wording improvement, edit the relevant text in `Choice.html` yourself and write a short `docs/CLASS09_NOTES.md` recording what you changed and tested.

## Ready for Class 10

Keep your project and CSV. You are ready when you can run the experiment, find a known response in its export, and point to the files that control the question and save the answer.

Next, this one-choice prototype will become a six-choice study with confidence ratings and a clearer participant interface.

## Quick reference

| Term | Simple meaning | Example here |
| --- | --- | --- |
| Specification | A precise description of the requested behavior | One required choice, then an acknowledgement |
| Local project | Files that Codex can work with as one project | Your `research-project` folder |
| Virtual environment | A separate set of Python packages for a project | `.venv` |
| Server | A running program that responds to browser requests | The process started by `run_experiment.py` |
| Template | A page layout filled with study content | `Choice.html` |
| Field | A named value stored in a participant record | `choice` |
| Form | Inputs a participant fills and submits | Sure-or-gamble radio buttons |
| Session | One created run of the study with participant records | Your two-participant test |
| CSV | A text file arranged as rows and columns | `class09_pilot.csv` |
| Checkpoint | A separate known-working project to inspect or continue from | `checkpoints/minimal/research-project` |

Further reference: [oTree forms](https://otree.readthedocs.io/en/latest/forms.html), [oTree pages](https://otree.readthedocs.io/en/latest/pages.html), [Codex local projects](https://learn.chatgpt.com/docs/projects?surface=app).
