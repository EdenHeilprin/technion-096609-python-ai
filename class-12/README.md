# Class 12 — Direct a Research Workflow

Your experiment, data, and analysis now belong to one project. Today you will use that context to answer one further question, explain the work accurately, and leave a project that someone else can continue.

The goal is a small, complete research handoff: **a question, a reproducible result, a short Method and Results draft, and clear instructions for the next researcher.**

## Get ready

1. [Download the Class 12 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-12/class-12-files.zip).
2. Extract to a new `class-12` folder. Open `class-12/research-project` in VS Code and Codex, and follow [SETUP.md](SETUP.md).
3. Run `analysis/analyze_choices.py`. With the default data, open `outputs/synthetic_choices/choice_by_offer.png`, `outputs/synthetic_choices/summary.json`, and `outputs/synthetic_choices/exclusions.csv`.

This download includes the completed reference project, so you can start without replacing Class 11 work. Use this fresh project for the route below. If you prefer to continue your completed Class 11 project, copy the reference `analysis/explore_confidence.py` from the Class 12 download into its `analysis` folder when needed. Keep the selected data settings consistent throughout today's tasks.

The default source is fictional teaching data. To use a classroom export, follow `data/CODEBOOK.md`; do not describe synthetic records as actual participants.

**Today's route:** choose a question, agree on its calculation, implement and check, draft Method/Results, and hand off the project.

## 1. Choose one question worth answering

Pick **one**, or propose another question that the recorded variables can answer:

- **Confidence:** How does mean reported confidence vary across guaranteed offers?
- **Individual differences:** Do participants all gamble at similar rates, or does the overall average hide a wide range?
- **A closer comparison:** How do gamble rates compare for the 4-point and 6-point guaranteed offers, using the same included participants?

Keep this extension descriptive. The study has repeated observations from the same people, and offer/order are confounded. If you use the synthetic file, the result describes the teaching fixture rather than human behavior.

Create `docs/MY_QUESTION.md` with three short lines:

```text
Question:
Data source:
The table or figure that would answer it:
```

Ask Codex to plan before writing code:

> Read `PROJECT.md`, `docs/MY_QUESTION.md`, `data/CODEBOOK.md`, `analysis/settings.py`, and the current analysis and outputs. Propose one simple descriptive calculation and one useful table or figure for my question. State what one row represents at each step, who is included, and the denominator or weighting. Reuse the existing inclusion rule. Identify any information the data cannot supply. Do not edit files yet.

Read the plan as the researcher. For confidence by offer, each included person supplies exactly one rating to each offer mean. For individual differences, use the **participant-level** table: a person with six trials is still one person. For the 4-versus-6 comparison, the two groups of rows come from the same people, not two independent samples.

**Without Codex:** choose the confidence question and write its calculation in your question file: include six-round completers, group their ratings by offer, and calculate each mean from one rating per included participant. Continue with the worked route below.

## 2. Implement the extension and check an actual number

Once the plan answers your question, send:

> Implement the agreed extension in a separate, clearly named script under `analysis/`. Preserve the original CSV, inclusion rule, and base analysis. Use the existing data settings, rebuild from the selected source rather than relying on stale outputs, and save results in that source's output folder. Include clear English # comments that explain the important lines and concepts. Run the script. Show one result traced back to the contributing records and report the files created. Do not add unrelated analyses.

Open the new table and image. Choose one value and follow the contributing rows. For a confidence mean, inspect the confidence ratings at that offer and check their count and sum; for a proportion, check its numerator and denominator. Ask about any line of code you cannot connect to the calculation.

### Worked route: confidence by offer

`analysis/explore_confidence.py` is a complete reference for the first question. You can run it directly if Codex is unavailable, or compare it with your implementation after trying the task.

Its central calculation is:

```python
# One included participant supplies one rating at each offer.
confidence = clean.groupby("sure_points", as_index=False).agg(
    mean_confidence=("confidence", "mean"),
    participant_count=("confidence", "size"),
)
```

It rereads and validates the original CSV using the provided inclusion helper, then writes `confidence_by_offer.csv`, `confidence_by_offer.png`, and `confidence_summary.json` to the selected source's output folder. It does not depend on your Class 11 analysis script or its saved outputs. The confidence scale runs from 1 to 7. A confidence rating of 6 does not mean a 60% chance of winning.

For the synthetic example, all six offer means use 15 fictional participants. The number of plot points—six—is the number of offers, not the sample size.

## 3. Turn files into a grounded research description

Now Codex has useful context: the implemented procedure, the variable meanings, the analysis decisions, and the actual outputs. Use it to draft two short sections in `docs/RESEARCH_SUMMARY.md`:

> Draft a concise Method and Results in `docs/RESEARCH_SUMMARY.md` from this project's actual experiment code, page text, codebook, analysis scripts, and freshly generated outputs. Start by clearly identifying the selected data source as synthetic teaching data or an actual classroom pilot. Check that the main analysis and extension identify the same input file and source hash before combining their results. Describe the six fixed-order offers, 50/50 gamble, hypothetical points, required confidence scale, and inclusion rule only where supported by the implementation. Report the actual participant and trial counts, main result, and my chosen extension with appropriate rounding. Keep every numerical claim traceable to an output filename and row or field. Explain the offer/order limitation. Do not invent demographics, recruitment details, ethics approval, payment, or citations; place any needed unknown procedural facts under “To confirm.” Distinguish the implemented procedure from a hypothetical future improvement. Do not alter the experiment or analysis.

Open the Markdown file in VS Code and preview it with **Cmd + Shift + V** on Mac or **Ctrl + Shift + V** on Windows ([VS Code Markdown guide](https://code.visualstudio.com/docs/languages/markdown)). It should read like a short research account, not a transcript of the agent's work.

Check three things directly:

1. **Procedure:** does the Method match what a participant actually sees? Open the choice page or run the experiment if needed.
2. **Numbers:** do the included N, trial count, and one reported result match the generated files?
3. **Meaning:** does the wording distinguish a descriptive pattern from a causal explanation—and synthetic examples from observations?

Ask for a specific revision if any answer is no. For example:

> This sentence claims that increasing the offer caused the decline. Our offers also changed with round order. Revise that interpretation without changing the numerical result.

**Without Codex:** use [the writing guide](WRITING_GUIDE.md) to write the same two short sections from your outputs. Producing a Word document is an optional formatting step after the facts and wording are checked.

## 4. Make the project understandable without your conversation

Ask for a focused handoff:

> Create `docs/HANDOFF.md` for someone opening this project without our conversation. Include the project question, experiment and analysis entry points, selected source and whether it is synthetic, inclusion rule, exact run order, generated outputs, my extension, known limitations, and one useful next step. Keep it concise. Link to existing explanations rather than duplicating them. Do not change working code. Identify any disagreement between the documents and implementation.

**Without Codex:** create `docs/HANDOFF.md` yourself using these headings: **Question**, **Data source**, **Run order**, **Outputs**, **Extension**, **Limitations**, **Next step**. Under Run order, name the setup guide, `analysis/settings.py`, `analysis/analyze_choices.py`, and your extension script in that order. State where their results appear.

Then close the chat and use **only the files** to explain how to rerun the work. A partner should be able to find the input, run the analysis, locate the figure, and identify the main limitation without asking what happened in the conversation. When working alone, close and reopen the project and follow your own handoff from the beginning.

Keep real classroom exports, derived participant data, and private notes out of public sharing. The supplied fictional example can be shared with its source label and provenance intact.

## 5. Explain your result and your decisions

Give a short demonstration:

- State your question and show the figure or table that answers it.
- Trace one number to the underlying records.
- Show one useful contribution from Codex and one judgment you made yourself.
- Name a limitation and propose a next study or project change that would address it.

For example, counterbalancing offer order could help separate offer size from order. That is a proposal for a new experiment version, not a repair we should silently make to an already-collected dataset.

## Optional: revisit the project from another angle

If time and access allow, use a separate conversation to ask a second research question or request a read-only review of the draft against its evidence. Give it the relevant project files and ask for concrete discrepancies, not a general approval. Bring back only the useful finding; keep the finished core analysis intact.

## Your completed Phase 2 project

You should now be able to open a project and locate:

| Part | What it contributes |
| --- | --- |
| `experiment/` | The participant experience and saved variables |
| `data/` | The untouched input and its codebook/provenance |
| `analysis/` | Reproducible calculations with readable explanations |
| `outputs/` | Traceable tables, figures, and source-specific results |
| `docs/` | Your question, evidence-grounded research summary, and handoff |

The transferable skill is choosing a useful goal, supplying the relevant context, directing manageable tasks, checking the evidence, and leaving work that can be continued.

[Setup](SETUP.md) · [Troubleshooting](TROUBLESHOOTING.md)
