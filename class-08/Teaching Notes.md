# Class 8 Teaching Notes

Read [the lesson](README.md) first. The [minimal project](minimal-project) contains the demonstration, not student setup work. [Download and unzip the demonstration files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip) to rehearse locally.

## Prepare once

Use your existing introduction slides. Open `minimal-project` in Codex. It starts with the experiment, `preregistration.txt`, and one example CSV. Codex will create the analysis and report during the demonstration. Settings and requirements only support running the experiment.

Read the preregistration before collecting classroom responses and keep it unchanged afterward. Its title identifies it as a teaching exercise, not an externally registered study. Do not reveal its prediction until after students participate.

Live hosting and its participant QR code still need to be set up before teaching. For local rehearsal, use the commands at the end of these notes. `example_responses.csv` contains four fictional participants for rehearsal. [Analysis reference.py](Analysis%20reference.py), kept outside the demonstration project, is a working fallback if you need it.

## Teach one connected story

### Introduce, then participate

Start with your slides. Students then use the live participant link/QR to make six choices. Ask which offers were difficult. They do not install anything or open a project.

### Reveal the small program

Open `choice_task/__init__.py` and `choice_task/Choice.html`. Ask Codex:

> Read these experiment files without changing them. Show us where the six offers are defined, where a choice is saved, and how the final page appears. Explain the familiar Python ideas briefly; distinguish them from the structure supplied by oTree.

Point to the offer list, the loop in `creating_session`, and the final-page condition. Open the HTML next to the participant page. Do not teach the whole framework here.

While Codex works, point out the selected project, the files it reads, and the model/effort and permission controls. Keep the focus on the task. Local file access does not mean offline AI; use only the course files and approved classroom responses.

### Analyze, then compare with the plan

Note the classroom session's code in oTree. In **Data → Custom exports → choice_task**, download the **CSV** and save it in the project as `responses.csv`. This export can contain rehearsal sessions too. Open a few rows and the preregistration, and give Codex the classroom session code:

> Read preregistration.txt and responses.csv. Use only session [paste the classroom session code]. Explain briefly how you would calculate and plot the percentage choosing Gamble at each offer. Do not edit files yet.

Once the plan matches the preregistration:

> Create analysis.py to analyze responses.csv according to that plan. Use straightforward Python, with clear English # comments; use csv to read rows and matplotlib for the graph. Preserve the CSV. Save one figure as results.png, labelled "Classroom responses", and the participant count and counts/percentages at each offer as results.txt. Run it, then open the outputs.

For rehearsal, use `example_responses.csv`, session `FICTIONAL`, and the label "Fictional example data". Keep the live task bounded to this one script, one graph, and one summary. Use the reference if waiting is displacing the discussion.

Open `results.txt` and `results.png`. Count one offer's Gamble responses together and divide by the recorded responses at that offer. Compare the graph with the prediction, including an unexpected or flat pattern if that is what occurred. Keep the preregistration unchanged.

**If the masterclass spans two meetings, pause here.** Resume with the graph and prediction visible; continue the same story into writing and extensions.

### Write and inspect the report

> Write short Method and Results sections in report.md, using the experiment, preregistration.txt, the active response CSV, and results.txt. Identify the data source accurately. Compare the observed pattern with the prediction and mention the fixed offer order. Do not invent recruitment details, demographics, or statistical tests. Flag missing information rather than guessing it.

Check one procedural sentence and one number together. Then demonstrate delegation with a useful, small review:

> Use one read-only subagent to check report.md against the experiment, preregistration, and data. Ask it to identify any unsupported statement or incorrect number. Bring back its findings without changing files.

Follow a finding back to the evidence; do not manufacture an error if the draft is correct.

Finally, type `/fork` and choose a **local chat**. In that conversation:

> Without editing files, suggest a simple way to randomize the offer order. What research question or design problem would that help us address?

Return to the main chat. Explain that the conversation is separate, but the local files are shared. This leads directly to students proposing their own improvements.

## Rehearse locally

In VS Code, open the `minimal-project` folder and open its terminal. These commands are for your review, not part of the student lesson. They use Python 3.13, as in the existing course setup.

**Mac**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
source .venv/bin/activate
otree devserver
```

**Windows PowerShell**

```powershell
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
$env:PATH = "$PWD\.venv\Scripts;$env:PATH"
otree devserver
```

Open `http://localhost:8000`, select **Sure or Gamble**, and open its demo. Complete the six choices. This local address is for your computer, not students' phones.

Stop the server with **Ctrl+C**. To review the working fallback without an AI request, run:

```bash
python "../Analysis reference.py"
```

Open `results.png` and `results.txt` inside `minimal-project`. For the actual Codex demonstration, use the prompts above to create `analysis.py` from the data and preregistration. No other setup document is needed.

Feature references: [Codex projects](https://learn.chatgpt.com/docs/projects?surface=app), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents?surface=app), [fork command](https://learn.chatgpt.com/docs/reference/slash-commands), [oTree data export](https://otree.readthedocs.io/en/latest/admin.html#custom-data-exports).
