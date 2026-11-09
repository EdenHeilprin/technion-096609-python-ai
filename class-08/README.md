# Class 8 — From Answers to Delegation

We will use Codex to build a simple decision experiment, collect responses, analyze them, and draft a research report.

## Start here

**[Download the Class 8 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip)**

1. Extract the ZIP: double-click it on macOS, or right-click and choose **Extract All** on Windows.
2. Move the extracted **class-08** folder into your course-work folder.
3. Open **class-08** as a new project in Codex. Keep this GitHub page open for the prompts.

The folder starts with just two files:

- **experiment-brief.docx** describes the experiment and how to build it.
- **preregistration.docx** provides the hypothesis, design, and analysis plan.

The research question: **How much extra expected value do people require to choose a gamble over a sure outcome?** Each participant makes seven choices between a sure **10 points** and a **50% chance of a varying prize**, otherwise **0**. Participants are randomly assigned to ascending or descending prize order. All points are hypothetical.

For Prompts 1–5, inspect each result before continuing. Prompts 6 and 7 can run in parallel in separate chats.

## 1. Get oriented

```text
Read the files in this working folder and inspect the available Python environment. Summarize the research question and your proposed build in five short bullets. Ask about any missing decision. Do not change anything yet.
```

## 2. Build the experiment

```text
Build the experiment described in this folder using oTree. Follow the brief’s beginner-level Python and commenting requirements.

Set up the environment, test both conditions in a laptop browser, and verify that the choices are saved.

Start the experiment locally and open a fresh participant page in my browser. Open the experiment’s Python code in VS Code. Leave the experiment running and stop for my review.
```

Try the experiment. In the Python file, find the prize list, condition assignment, and where each response is stored.

## 3. Improve the design

```text
Give the experiment a cleaner, more polished design for laptop screens: a centered layout, larger readable text, generous spacing, and two matching choice cards with a clear selected state. Keep both options equally prominent and retain the Next button to confirm the choice. Use simple HTML and CSS with clear comments. Do not change the wording, choices, order, or recorded data. Check both conditions, then open a participant page for me to review.
```

Try the updated design and compare it with the original.

**Possible extension:** Add a third condition with randomly ordered decisions.

### 3b. Put the experiment online

```text
Prepare this experiment for deployment through my Heroku CLI setup. Check the target app with me, deploy it, verify that it works online, and give me the participant link.
```

Open the participant link on the shared screen. Once responses are collected, continue below in the same project.

## Analyze the responses

The analysis files will live beside the experiment, not inside it.

### 4. Organize the analysis workspace

```text
Create an analysis folder beside experiment, with raw and outputs subfolders.

Retrieve the choice_task CSV export from the live experiment using the available authenticated access and save it unchanged in raw. If access is unavailable, open the export page for me to download it; then find the CSV in Downloads and copy it into raw. If several exports match, ask me which to use.

Read the project documents and inspect the export. Briefly summarize what it contains and how you will prepare it for the preregistered analyses. Do not run the analyses yet.
```

### 5. Run the preregistered analyses in R

```text
Create analysis.R in the analysis folder to prepare the data and run the analyses specified in the preregistration.

Keep the code simple and readable, with descriptive variable names and concise English # comments explaining each meaningful step. Use as few packages as practical.

Save the cleaned data, tables, and figures in outputs; leave raw unchanged. Create a short results.html with readable tables and figures, sensible rounding, and brief explanations.

Keep the R script independently runnable, using relative paths. Run it from start to finish in a fresh R session, then open the script in RStudio and results.html in my browser.
```

### 6. Branch in new chat — Explore beyond the preregistration

After Prompt 5 finishes, choose **Branch in new chat** and keep the same project folder. Run this prompt in the new chat.

```text
Consider two useful exploratory analyses beyond the preregistration. Briefly compare them, choose the most promising based on scientific relevance and what the data can support, and run it in R.

Keep all exploratory code, outputs, and notes in an exploratory folder beside analysis. Treat all existing project files as read-only inputs.

Write a simple, clearly commented exploratory.R that I can run independently in RStudio. Save a short results.html with readable tables or figures, an explanation of the findings, and their limitations. Clearly identify the work as exploratory. Open the script and results for me.
```

## Write the manuscript

Return to the original chat for Prompt 7. The exploratory analysis can continue in its branch while the writing agents work from the completed preregistered analyses.

### 7. Main chat — Write with parallel agents

```text
Read the project documents and create a writing folder beside analysis. Spawn four subagents, working in parallel as capacity allows:

1. Journal guidelines: Summarize the current official Journal of Experimental Psychology: General submission requirements in journal-guidelines.md, with source links and access date.
2. Literature: Read 5–8 relevant primary papers and summarize their findings and limitations in literature.md, with verified references and DOI or source links.
3. Method: Inspect the experiment and data-preparation rules; write method.md with enough detail to replicate the study, noting departures from the preregistration.
4. Results: Check the preregistered analysis and write results.md, tracing reported numbers to the outputs and identifying relevant tables and figures.

Each agent writes only its assigned file in writing; other files are read-only. Do not use exploratory outputs.

Wait for all four agents. As lead author, verify citations and numbers, resolve inconsistencies, and assemble writing/manuscript.docx following the journal guidelines. Include a title, abstract, Introduction, Method, Results, Discussion, references, tables and figures. Keep conclusions proportionate to the evidence and mark missing facts as [TO CONFIRM]. Inspect the layout, then open the manuscript for me.
```

### 8. Revise with a custom skill

This prompt uses the locally installed **global-revision-process** skill. Continue in the original chat after the manuscript is ready.

```text
Use $global-revision-process to review and improve the first three paragraphs of the Introduction in writing/manuscript.docx. Follow the skill's paragraph-by-paragraph revision workflow and show the proposed revisions here. Leave the saved manuscript unchanged until I approve them.
```

---

[Back to the course](https://github.com/EdenHeilprin/technion-096609-python-ai)
