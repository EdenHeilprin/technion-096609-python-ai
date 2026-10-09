# Class 8 — From Chatting to Delegating with Codex

You have learned enough Python to follow a program, make changes, and investigate a problem. Now we change the scale of what you can do: work with an AI assistant inside a project containing code, data, and research documents.

Today is a live demonstration with decisions for you to make along the way. You do not need to install Codex during class. In Class 9, you will start building your own experiment with it.

**The question connecting Classes 8–12:** How does choosing a gamble vary as the guaranteed alternative increases?

We will go from taking part in a small experiment to inspecting its code, analyzing its data, and drafting a short research report. The interesting part is not how quickly text appears. It is how a clear goal becomes working, checkable files.

## Materials

**[Download the Class 8 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip)** and extract them into a new folder. The download includes the complete demonstration project and this lesson.

- **In class:** follow the demonstration; open the files if useful. Keep a note of a task you would like to delegate in your own work.
- **Reviewing independently:** follow [SETUP.md](SETUP.md), then use the replay route at the end of this lesson. Working checkpoints and evidence-linked examples let you inspect the full workflow without a paid AI subscription.

## 1. Start as a participant

Open the experiment link or scan the QR code shown in class. Make six choices between a guaranteed number of points and a gamble. After each choice, indicate how confident you are.

The points are hypothetical. The activity does not ask for your name.

Before looking at results, discuss:

- Which offers made the decision difficult?
- What would you expect the graph of gamble choices against guaranteed points to look like?
- What information must the program save for us to draw that graph?

The gamble is always a 50% chance of 10 points and a 50% chance of 0. The guaranteed offer changes. There are already several decisions that the researcher—not Codex—must make: the offers, their order, the response scale, and the question the graph should answer.

## 2. Give Codex a project, not a pile of pasted messages

The instructor opens `research-project` in Codex. It contains:

| Location | What it contributes |
|---|---|
| `docs/STUDY_SPEC.md` | Study decisions and the meaning of the data |
| `experiment/` | The oTree experiment participants use |
| `data/` | A CSV file and its codebook |
| `analysis/` | Python scripts that inspect and analyze the CSV |
| `outputs/` | Generated tables, figures, and numerical summaries |
| `AGENTS.md` | Standing instructions for work in this project |

Instead of copying the experiment into a chat, start with a bounded request:

> Read PROJECT.md, docs/STUDY_SPEC.md, and the experiment and analysis files. Do not edit anything yet. Explain the route from a participant clicking an answer to one row in the exported CSV, then to the planned figure. Point me to the relevant files. Flag anything you cannot verify from these files.

Follow one response through that route. Python stores it; an HTML template displays the page; a CSV carries it into the analysis. Codex can connect those files, but we can inspect the evidence ourselves.

### Three controls worth understanding

- **Project and files:** check that Codex is looking at the intended folder. A file somewhere on your computer is not necessarily part of the current task's context.
- **Permissions:** the permission mode determines what actions can run without approval. “Ask for approval” can still allow routine workspace edits; it is not a read-only mode. For inspection, explicitly ask for no edits. Read an approval request before accepting it.
- **Model and reasoning effort:** use the available controls to balance a difficult planning task against a small routine edit. More reasoning is not automatically useful for every task. Faster options, when offered, can trade additional usage for lower latency; check the displayed terms.

Codex works with local files, but model requests are sent to an online service. Use the supplied synthetic data or the instructor-approved classroom export, not unrelated personal or confidential research files.

## 3. Delegate a change you can see and test

You have just made six decisions, but the final page only acknowledges completion. A useful addition would let you review your choices and confidence together: **a personal response summary, shown after the study ends**.

First, ask for a plan:

> Inspect the local experiment. Plan a read-only summary on the final page, showing this participant's six guaranteed offers, recorded choices, and confidence ratings. Use their submitted round records, not invented example values or other participants' data. Keep the study rules, response pages, validation, and export unchanged. Do not implement yet. Explain which Python and HTML files need changes and show the proposed table layout.

Check that the plan displays already-saved answers without changing how the study collects them. Then authorize it:

> Implement the agreed final-page summary in this local project only. Make it readable on a narrow screen. Add clear English # comments explaining the Python and appropriate comments in HTML/CSS. Run the checks available to you, report their actual results, and tell me which browser checks remain. Do not deploy or change the saved fields or export.

Compare the changed files with their earlier versions. Complete a fresh test participant, noting the choices and confidence you enter. On the final page, check that all six rows match those responses. Check the narrow-screen layout and compare one displayed response with the participant's CSV record.

**What would count as success?** The participant can review their own actual answers, and the study still collects and exports the same data. A pleasing table filled with made-up examples would not count.

**Working reference:** the download includes `checkpoints/participant-summary/research-project`. To inspect the finished interface without an AI request, stop the current server with **Ctrl+C**, open that checkpoint as a separate project, follow [SETUP.md](SETUP.md) for its environment, and run its `run_experiment.py`. Complete all six rounds to reach the summary. Keep the original project intact.

This is different from “give me some code”: Codex can inspect relevant files, edit them, run commands, and report what happened. You remain responsible for the request and for accepting the result.

## 4. Turn the responses into an answer

The instructor downloads the custom oTree export into `data/`. We use the supplied synthetic file if live data are unavailable. The active source is named in `analysis/settings.py` and on the generated figure.

Here is an analysis request with the important decisions already stated:

> Read docs/STUDY_SPEC.md and data/CODEBOOK.md. Check the active data file in analysis/settings.py. Use the existing analysis scripts to summarize gamble choices at each guaranteed offer. Include only participants with six valid completed rounds, and show how many were excluded. Preserve the original CSV. Run the analysis and check the output against the input. Give me the figure and a short factual description, identifying whether the data are synthetic or classroom responses.

Inspect three pieces of evidence:

1. A few CSV rows: what does one row represent?
2. `outputs/<data-file-name>/summary.json`: how many participants and decisions were included?
3. `choice_by_offer.png`: does the pattern match the table behind it?

The folder uses the data filename without `.csv`; for the supplied example it is `outputs/synthetic_choices/`. A JSON file stores named values, such as an included-participant count.

Look for familiar Python ideas inside `analysis/analyze_choices.py`: variables, functions, comparisons, and grouping repeated observations. Class 11 will unpack the analysis.

The offers always increase in the same order. That makes this a useful descriptive classroom pilot, but offer size and order are mixed together. A downward line does not by itself prove what caused the change.

## 5. Use parallel work and forks for a reason

### Two independent checks

One reviewer can inspect the experiment while another checks the analysis. They need not wait for each other:

> Use two subagents for independent, read-only checks. One should compare experiment/ against docs/STUDY_SPEC.md. The other should compare the active data, analysis scripts, and generated summaries against the analysis rules. Give each a bounded task. Neither should change files. Bring back concrete discrepancies with file references, and verify any important finding before proposing a fix.

Subagents are useful when tasks are separable. They consume additional usage, and two agents agreeing is not proof. Follow one important claim back to a file or an executed check. When agents make changes, assign separate files or working copies so their edits do not collide.

### A side question without losing the main thread

In the current Codex chat, type `/fork` in the composer and choose a new **local chat** rather than a worktree. This copies the conversation so far into a separate chat. In that branch, ask:

> Without changing files, explain what randomizing the offer order would change in this study. What would stay the same in the analysis, and what would need to be recorded differently? Keep the answer grounded in our current project.

Return to the main conversation afterward. A fork gives you a separate conversational path; it does **not** automatically give you a separate copy of your files. Keep the exploration read-only unless you deliberately create an isolated alternative.

## 6. Go from code and evidence to research writing

The project now contains the implemented experiment, a specification, raw data, analysis code, and numerical outputs. Ask Codex to connect them:

> Draft a short Method and descriptive Results section in outputs/<active-data-folder>/report.md, using the experiment files, docs/STUDY_SPEC.md, data/CODEBOOK.md, and the generated summaries. Replace <active-data-folder> with the actual output folder. Identify the data source and whether it is synthetic. Trace every numerical claim to an output. Do not invent recruitment, demographics, payments, ethics approval, or significance tests. Put unresolved information in a short “To confirm” list. Mention the fixed-order limitation.

Check one sentence about the procedure against the experiment. Check one numerical sentence against a table. Is a possible explanation clearly distinguished from something the data actually show?

Finally, make the work easy to resume:

> Update docs/DECISIONS.md with the decisions we actually made. Create docs/HANDOFF.md with the current state, changed files, commands that worked, data source, checks completed, and the next task. Do not record credentials or participant-level responses there.

A long conversation has limited working context. Short, accurate project documents let a new conversation—or a colleague—resume from a durable record. A file is useful context when it is relevant and read, not simply because it exists.

The download also includes a [worked research summary](worked-examples/RESEARCH_SUMMARY.md) and [worked handoff](worked-examples/HANDOFF.md), with synthetic reference results in `reference-results/`. They illustrate the finished artifacts without claiming that fictional responses came from the class.

## Replay on your own

After following [SETUP.md](SETUP.md):

1. Run `run_experiment.py`, open the local address, and try the six-round study. The instructor's public link is not required for this route.
2. Stop the server with **Ctrl+C** in its terminal when finished.
3. Run `analysis/inspect_data.py`, then `analysis/analyze_choices.py`, using **Run Python File** in VS Code. Both use the supplied synthetic CSV by default.
4. Open `outputs/synthetic_choices/choice_by_offer.png` and `outputs/synthetic_choices/summary.json`. The reference includes **15 complete synthetic participants, 90 analyzed decisions, and 46 gamble choices**; one incomplete participant is excluded.
5. From the downloaded class folder, open `worked-examples/RESEARCH_SUMMARY.md`. Check one procedural sentence against the experiment and one numerical sentence against the outputs you just regenerated. Open `worked-examples/HANDOFF.md` and locate its data source and run order. The bundled `reference-results/` provides the same synthetic results for comparison.
6. To see the final-page improvement, open the separate `checkpoints/participant-summary/research-project`, prepare its environment, and complete the six-round study as described in **Working reference** above. Do not overwrite your original project.
7. If you have Codex access, try one bounded read-only request from this lesson. Without access, trace a CSV column through the experiment and analysis files yourself. The experiment, analysis, and worked writing examples remain available without an AI response.

Before Class 9, complete the **Codex** part of [SETUP.md](SETUP.md) if you will use it on your laptop. The next class starts from a small scaffold: you will build the experiment rather than watch it.

## A compact delegation reference

| Include in a request | Example |
|---|---|
| Goal | Show participants their recorded responses after completion |
| Relevant context | The final-page template, saved round records, and study specification |
| Boundaries | Do not change fields or export columns |
| Permission to act | Plan first; implement after agreement |
| Evidence of completion | Run checks, inspect the page, verify a saved response |
| Handoff | Changed files, results, unresolved points, next task |

Current product details: [Codex setup](https://learn.chatgpt.com/docs/quickstart), [permissions](https://learn.chatgpt.com/docs/permission-modes), [speed options](https://learn.chatgpt.com/docs/agent-configuration/speed), [subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents?surface=app), and [desktop slash commands, including `/fork`](https://learn.chatgpt.com/docs/reference/slash-commands). Controls and available models can differ between accounts and versions.
