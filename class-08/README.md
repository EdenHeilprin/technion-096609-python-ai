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
Build the experiment described in this folder using oTree.

Keep its Python logic understandable to a beginner: variables, basic types and arithmetic, lists and dictionaries, if/elif/else, for loops, and simple functions with parameters and return values. Use only what the task needs. Add concise English # comments explaining each meaningful step and unfamiliar oTree structure.

Make it runnable without Codex. Save a short experiment/README.md with the exact VS Code terminal commands for my computer: which folder to start in, how to activate the Python environment, and how to start and stop otree devserver. Verify the commands in a fresh terminal and open the app's __init__.py in VS Code for inspection.

Test it in a laptop browser, then start otree devserver and give me the local participant link. Stop for my review.
```

Try all seven decisions in each condition. Then open the Python file: find the prize list, follow how the assigned condition determines the order, and locate where the response is stored.

## 3. Improve the design

```text
Give the experiment a cleaner, more polished design for laptop screens: a centered layout, larger readable text, generous spacing, and two matching choice cards with a clear selected state. Keep both options equally prominent and retain the Next button to confirm the choice. Use simple HTML and CSS with clear comments. Do not change the wording, choices, order, or recorded data. Let me test the result.
```

Compare the updated design with the original. Try all seven decisions and check the opening and thank-you pages. Keep the generated files in this same **class-08** project.

**Possible extension:** Add a third condition with randomly ordered decisions.

## Analyze the responses

After collecting responses, download the experiment's CSV from oTree. Continue in the same **class-08** project; the analysis files will live beside the experiment, not inside it.

### 4. Organize the analysis workspace

```text
Find the oTree CSV in Downloads. If several files match, ask me which to use.

Create an analysis folder beside the experiment folder, with raw and outputs subfolders. Copy the CSV unchanged into raw.

Read the project documents and inspect the export. Briefly summarize what it contains and how you will prepare it for the preregistered analyses. Do not run the analyses yet.
```

### 5. Run the preregistered analyses in R

```text
Create analysis.R in the analysis folder to prepare the data and run the analyses specified in the preregistration.

Keep the code simple and readable, with descriptive variable names and concise English # comments explaining each meaningful step. Use as few packages as practical.

Save the cleaned data, tables, and figures in outputs; leave raw unchanged. Also create a short results.html with readable tables and figures, plain-language headings, percentages rounded to one decimal place, and a brief explanation of each result and its measures. Put notes in captions rather than repeating them in every row.

Make the script runnable from start to finish in RStudio without Codex, using relative paths and brief run instructions at the top. Test it in a fresh R session, then open the R script in RStudio and results.html in my browser.
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

1. Journal guidelines: Read the current official Journal of Experimental Psychology: General submission guidelines. Save a concise, actionable summary in journal-guidelines.md, including the source links and access date.
2. Literature: Find and read 5–8 relevant primary papers. Summarize the findings and limitations that will support our Introduction in literature.md, with verified references and DOI or source links.
3. Method: Inspect the experiment, project documents, and data-preparation rules. Draft method.md with enough detail to replicate what was actually done, noting any departures from the preregistration.
4. Results: Check the preregistered analysis code and outputs. Draft results.md, tracing reported numbers to their source tables or data and identifying the relevant tables and figures.

Each agent writes only its assigned file in writing; all other project files are read-only. Do not use the exploratory folder.

Wait for all four agents. Then act as lead author: verify citations and numerical claims, resolve inconsistencies, and integrate the work into a coherent manuscript.docx in writing. Include a title, abstract, Introduction, Method, Results, Discussion, references, and relevant tables and figures, following the journal guidelines. Keep conclusions proportionate to the design and evidence. Mark missing facts as [TO CONFIRM] rather than inventing them. Inspect the document's layout, then open it for me.
```

### 8. Revise with a custom skill

This prompt uses the locally installed **global-revision-process** skill. Continue in the original chat after the manuscript is ready.

```text
Use $global-revision-process to review and improve the first three paragraphs of the Introduction in writing/manuscript.docx. Follow the skill's paragraph-by-paragraph revision workflow and show the proposed revisions here. Leave the saved manuscript unchanged until I approve them.
```
