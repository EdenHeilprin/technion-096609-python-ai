# Class 8 — From Answers to Delegation

We will use Codex to build a simple decision experiment, collect responses, analyze them, and draft a research report.

## Start here

**[Download the Class 8 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip)**

1. Extract the ZIP: double-click it on macOS, or right-click and choose **Extract All** on Windows.
2. Move the extracted **class-08** folder into your course-work folder.
3. Open **class-08** as a new project in Codex. Keep this GitHub page open for the prompts.

The folder starts with just two files:

- **experiment-brief.docx** describes the experiment and how to build it.
- **preregistration.docx** provides the research background, hypothesis, and analysis plan.

The research question: **Do people choose the gamble more often as its prize increases?** Each participant makes six choices between a sure **10 points** and a **50% chance of a larger prize**. All points are hypothetical.

Paste one prompt at a time and inspect the result before continuing.

## 1. Get oriented

```text
Read the files in this working folder and inspect the available Python environment. Summarize the research question and your proposed build in five short bullets. Ask about any missing decision. Do not change anything yet.
```

## 2. Build the experiment

```text
Build the experiment described in this folder using oTree.

Keep its Python logic understandable to a beginner: variables, basic types and arithmetic, lists and dictionaries, if/elif/else, for loops, and simple functions with parameters and return values. Use only what the task needs. Add concise English # comments explaining each meaningful step and unfamiliar oTree structure.

Test it in a laptop browser, then start otree devserver and give me the local participant link. Stop for my review.
```

Try all six decisions. Then open the Python file: find the prize list, follow how one decision gets its prize, and locate where the response is stored.

## 3. Improve the design

```text
Give the experiment a cleaner, more polished design for laptop screens: a centered layout, larger readable text, generous spacing, and two matching choice cards with a clear selected state. Keep both options equally prominent and retain the Next button to confirm the choice. Use simple HTML and CSS with clear comments. Do not change the wording, choices, order, or recorded data. Let me test the result.
```

Compare the updated design with the original. Try all six decisions and check the opening and thank-you pages. Keep the generated files in this same **class-08** project.
