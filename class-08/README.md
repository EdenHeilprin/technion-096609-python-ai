# Class 8 — From Answers to Delegation

We will use Codex to build a simple decision experiment, collect responses, analyze them, and draft a research report. In class, the instructor operates Codex and students join the experiment on their phones.

**We are building this lesson together.** The opening sequence below is ready for review. Deployment, analysis, and writing will follow after we test it.

## Start here

**[Download the Class 8 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip)**

1. Extract the ZIP: double-click it on macOS, or right-click and choose **Extract All** on Windows.
2. Move the extracted **class-08** folder into your course-work folder. For our walkthrough, use **Course Materials → 02 - My Student Work → class-08**.
3. Open **class-08** as a new project in Codex. Keep this GitHub page open for the prompts.

The folder starts with just two files:

- **experiment-brief.docx** describes the experiment and how to build it.
- **preregistration.docx** provides the research background, hypothesis, and analysis plan.

These documents give Codex the detailed context. You can introduce the study briefly without reading them aloud: participants make six choices between a sure **10 points** and a **50% chance of a larger prize**. The prize increases across choices. All points are hypothetical.

Paste one prompt at a time and inspect the result before continuing.

## 1. Get oriented

```text
Read experiment-brief.docx and preregistration.docx. Inspect the available Python environment. Summarize the research question and your proposed build in five short bullets. Flag any missing decision. Do not build or change anything yet.
```

## 2. Build the experiment

```text
Build the experiment in experiment-brief.docx using oTree.

For its logic, use the Python we covered in Classes 1–7: variables, basic types and arithmetic, lists and dictionaries, if/elif/else, for loops, and simple functions with parameters and return values. Use only what the task needs. Add concise # comments explaining each meaningful step and unfamiliar oTree structure. Students must be able to follow the code.

Test it, then start otree devserver and give me the local link. Stop for my review.
```

Try all six decisions. Then open the Python file: find the prize list, follow how one decision gets its prize, and locate where the response is stored.

## 3. Make one visible improvement

```text
Replace the radio choices and Next button with two large, equally prominent choice buttons that work well on phones. Each click should save one choice and advance once. Keep the options, order, and data coding unchanged. Let me test the result.
```

Try the updated experiment, including its opening and thank-you pages. Keep the generated files in this same **class-08** project.

We will continue from here after reviewing this opening sequence.
