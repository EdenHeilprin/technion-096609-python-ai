# Class 10 — Turn a Prototype into a Study

One choice can tell us what someone preferred at one particular offer. To examine how preferences vary, we need several offers—and an interface that presents each one clearly.

Today, you will use Codex to extend the prototype into a six-choice experiment, collect confidence ratings, improve the participant interface with HTML/CSS/JavaScript, and inspect the recorded results.

Our question is: **how does choosing the gamble vary as the guaranteed alternative increases?**

## Start from a clean copy

1. [Download the Class 10 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-10/class-10-files.zip) and extract the `class-10` folder.
2. Keep it beside your Class 9 folder. Do not replace your Class 9 work. If `class-10` already exists, give this new copy a different name.
3. Stop any experiment server still running from Class 9 with **Ctrl+C** in its terminal.
4. Open the new `class-10/research-project` folder in VS Code and Codex. Follow [SETUP.md](SETUP.md) to prepare and check its environment.

This download starts with the working one-choice experiment from Class 9, without your previous test database. It also includes a separate full-study checkpoint in `checkpoints/full/research-project`.

Keep all work below inside this new project. Its `experiment`, `data`, and `docs` folders now belong to Class 10.

## 1. Specify what changes—and what stays the same

Read [the extension brief](EXTENSION_BRIEF.md). The guaranteed offers become:

```python
[2, 3, 4, 6, 7, 8]
```

The gamble stays the same on every round: a 50% chance of 10 points and a 50% chance of 0 points. After each choice, the participant reports confidence in that choice from **1 — Not at all confident** to **7 — Very confident**.

Before asking Codex to build, write a prediction in `docs/PREDICTION.md`: at which guaranteed offers do you expect more people to choose the gamble? Why?

The gamble's expected value is:

```python
0.5 * 10 + 0.5 * 0  # 5 points
```

That is a long-run average, not a promised outcome. A participant can prefer certainty, so expected value does not supply a single correct choice.

Send Codex:

> Read `PROJECT.md`, `AGENTS.md`, `docs/EXTENSION_BRIEF.md`, and the existing experiment. Plan the change from one choice to the six-round `full-v1` study. Explain how the offer is selected for each round, where choice and confidence are saved, and how the export will represent six responses from one participant. Keep the current package versions and environment helpers. Do not edit yet.

Check the plan for the six offers, fixed gamble, required confidence, and the same nine-column export. Then send:

> Implement that plan. Use concise English `#` comments to explain the Python lines and concepts, and suitable comments for HTML/CSS/JavaScript. Keep the implementation focused on the extension brief. Run the checks available to you, report actual results, and list the browser checks that remain for me. Do not describe a check as passed unless it was executed.

## 2. Understand the repeated rounds

Open `experiment/choice_task/__init__.py`. Find the offer list and the number of rounds. Then locate the code that selects an offer using the current `round_number`.

oTree numbers rounds from **1**; Python list positions begin at **0**. The selection will therefore use the equivalent of:

```python
sure_points = offers[round_number - 1]
```

Predict the results before checking them:

| Round number | List position | Sure points |
| --- | --- | --- |
| 1 | 0 | 2 |
| 3 | 2 | 4 |
| 6 | 5 | 8 |

Each round has its own `Player` record, so the next answer does not overwrite the previous round's answer. The participant code connects those records to the same person.

Everyone receives offers in the same ascending order in this pilot. **Offer and position therefore change together.** If gambling becomes less common later, this study alone cannot separate the effect of the offer from effects of order, practice, or fatigue. Keep that limitation in mind when interpreting the data in Class 11.

## 3. Improve what the participant sees

Run `run_experiment.py` from the root of `research-project` and open [http://localhost:8000](http://localhost:8000). Choose **Sessions → Create new session**, select **Sure or gamble — six decisions** (the `sure_or_gamble` configuration), enter **2 participants**, and choose **Create**. Open the first participant link.

You should see a short introduction followed by the first choice. On each choice page, look for the current round, both options, and the confidence question.

The interface has four complementary parts:

| Part | Job | Example in your project |
| --- | --- | --- |
| Python | Study rules, valid values, and saved responses | `choice_task/__init__.py` |
| HTML | Page structure and labeled inputs | `choice_task/Choice.html` |
| CSS | Spacing, sizing, contrast, and layout | `_static/choice_task/study.css` |
| JavaScript | Immediate behavior in the browser | `_static/choice_task/confidence.js` |

Those paths are inside `experiment`. Open the three interface files and find one recognizable element in each: a heading or form, a style rule, and the JavaScript that responds to a confidence selection.

Choose confidence **2**, then **6**, without submitting yet. The small selected-value preview should update immediately. This is JavaScript changing the current page; the form is saved by oTree when you submit it.

Now make one practical improvement. Narrow the browser window to approximately phone width. Look for text that is cramped, buttons that are hard to use, or information that is easy to miss. Ask Codex to improve one specific issue. For example:

> On a narrow screen, make the two alternatives easier to compare by stacking them vertically with equal visual weight and generous spacing. Keep the wording, option order, offers, form values, and study behavior unchanged. Explain the CSS changes and let me verify the page before making further changes.

Use your own observation if the page already stacks well. A useful improvement might instead clarify a heading or make the progress indicator easier to read. Refresh the page and compare wide and narrow views. If a style looks unchanged, try a hard refresh: **Cmd+Shift+R** on Mac or **Ctrl+Shift+R** on Windows.

Keep both options equally easy to see and select. A visual improvement should not accidentally tell participants which answer you prefer.

## 4. Test the participant journey

Create a **new session** after the interface change so you can test from the beginning. Use the first participant link for this full path:

1. On the first choice page, submit without answering. It must not advance.
2. Select a choice but leave confidence unanswered. It must still not advance.
3. Select confidence **1**, then change it to **7**. Check that the preview follows your selection. Neither value should be selected automatically on a new round.
4. Refresh the page before submitting. Your current selections should remain selected in the same browser.
5. Complete the six rounds, recording your answers as you go. Use this known sequence for an easy export check:

| Round | Sure offer | Choice to select | Confidence |
| --- | --- | --- | --- |
| 1 | 2 | Gamble | 7 |
| 2 | 3 | Gamble | 6 |
| 3 | 4 | Gamble | 5 |
| 4 | 6 | Sure | 5 |
| 5 | 7 | Sure | 6 |
| 6 | 8 | Sure | 7 |

After round 6, you should reach the final acknowledgement. Refresh that page; it should not create another response or restart the study.

Use the second participant link to complete **only the first two rounds**, then close that participant tab. This intentionally unfinished case will help you recognize incomplete records.

Record any failed check with its inputs and observed behavior, then ask Codex to fix that specific problem. Retest the affected path after the change.

The server—not just JavaScript—must enforce the allowed answers. Ask Codex to check and explain where the Python code rejects missing choices, invalid choice values, and confidence outside 1–7. If it can run a direct submission check, ask for its actual result; otherwise record that it reviewed the code rather than tested the submission.

## 5. Export and recognize a participant's records

Return to oTree's **Data** page. Under **Custom exports**, find **`choice_task (custom_export)`** and choose **CSV**. Save it as `data/class10_pilot.csv` inside this project.

Open it in VS Code. The header remains:

```text
session_code,participant_code,study_version,round_number,sure_points,gamble_high,gamble_probability,choice,confidence
```

Find the codes for your final test session. For the completed participant, check:

- Six rows share the same participant and session codes.
- `study_version` is `full-v1`.
- Rounds 1–6 contain offers 2, 3, 4, 6, 7, and 8, respectively.
- Choices and confidence values match your six test responses.
- The gamble remains `10` with probability `0.5` on every row.

For the unfinished participant, rounds they did not submit should have blank response fields. A created participant record is not proof that the participant finished.

Your export may also contain earlier sessions. Identify records using the combination of **session code, participant code, and round number**; those three values identify one expected row. Keep the original export unchanged.

## 6. Leave a usable handoff

Ask Codex:

> Write `docs/CLASS10_NOTES.md` explaining the implemented study, the purpose of its Python/HTML/CSS/JavaScript files, and my interface change. Include the fixed-order limitation and the actual checks performed. Identify `data/class10_pilot.csv` as a local test export; do not treat its known test answers as research findings. Separate passed checks from checks not yet performed.

Read the note and correct anything that does not match what you did. Keep the project and export: Class 11 will show how to turn rows like these into checked tables and figures.

## Collecting responses together

When your instructor shares the hosted study link or QR code, you can take part from your phone or laptop. The instructor will collect the class export from that server. Your own `localhost` link is for your own computer; it is not the link to share with the class.

If you are reviewing alone, your local completed and unfinished test participants are enough to finish this lesson. Class 11 also supplies clearly labeled synthetic data for practicing analysis.

## If you need the working checkpoint

Stop the running server with **Ctrl+C**. Open `checkpoints/full/research-project` from this download as a **separate folder** in VS Code and Codex. Follow `SETUP.md` for that folder and start from **Improve what the participant sees** above.

Keep your original attempt. The checkpoint lets you inspect the implementation, make your own interface improvement, and perform every browser/export check without generating the full study again. If you have no remaining AI allowance, make a small wording or spacing change directly in the commented HTML/CSS files and write `docs/CLASS10_NOTES.md` yourself.

## Optional — improve the design, not only the page

Sketch a study version that could help separate offer effects from order effects. What would change for the participant? What additional information would you need to save to analyze it correctly?

Discuss or ask Codex to critique your proposal **without implementing it in the core project**. Class 12 will give you room for a focused extension.

## Quick reference

| Term | Simple meaning | Example here |
| --- | --- | --- |
| Round | One repeated decision in the experiment | Sure 4 versus the gamble in round 3 |
| HTML | The structure and labeled content of a web page | A heading and a confidence form |
| CSS | Rules controlling the page's appearance | Cards stack on a narrow screen |
| JavaScript | Code that responds within the browser | The selected-confidence preview |
| Validation | Checking whether a submitted response is allowed | Confidence must be an integer from 1 to 7 |
| Participant code | A generated code linking one participant's records | The same code on six round rows |
| Row key | Values that identify one expected record | Session + participant + round |
| Incomplete response | A record without all required submitted answers | Blank choice and confidence on an unvisited round |
| Confounding | Two things vary together, so their effects cannot be separated by this design | Higher offers always occur later |

Further reference: [oTree templates](https://otree.readthedocs.io/en/latest/templates.html), [oTree forms and validation](https://otree.readthedocs.io/en/latest/forms.html), [oTree data exports](https://otree.readthedocs.io/en/latest/admin.html#export-data).
