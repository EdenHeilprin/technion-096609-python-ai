# Class 10 — Python Files and Your First GitHub Project

Turn a CSV of decisions into a small, reusable summary program. Then share the code on GitHub and review a change before merging it.

## 1. Open and run the project

**[Download Class 10 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-10/class-10-files.zip)**

Extract the ZIP and keep `class-10` next to your earlier class folders. Open it in VS Code and select your Python 3.13 interpreter. No new packages are needed.

Open `summarize_choices.py`, save it, and choose **Run Python File in Terminal**. You should see:

```text
Decisions: 14
Gamble choices: 7
Gamble choices (%): 50.0
Saved: ...summary.csv
```

Open the new `summary.csv`. It contains one summary row. Running the program again updates this file; it does not change `sample_choices.csv`.

Our input contains **two fictional participants, each making seven choices**. It is a small, tidy teaching example, not a raw oTree export. Each row is one decision. You can check every count yourself.

## 2. Read a file instead of typing the data into Python

Open `sample_choices.csv` in VS Code. Its first line names the columns:

```csv
participant_id,condition,round_number,prize,choice
```

The remaining lines contain the values. A **CSV** is a plain-text table: commas separate its columns.

Return to the Python file. Its first lines import two **modules**: reusable Python tools. `csv` handles CSV tables; `pathlib` handles file paths. Both come with Python, so there is nothing to install.

```python
import csv
from pathlib import Path

folder = Path(__file__).resolve().parent
input_file = folder / "sample_choices.csv"
```

`__file__` identifies this script. The next steps obtain its folder and construct the path to a file beside it. Here, `/` joins a folder and filename; it is not arithmetic. This works on Mac and Windows without writing your personal Desktop path into the code.

Now find the reading block:

```python
with open(input_file, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    choices = list(reader)
```

`with open(...)` opens the file and closes it when the indented block ends. `DictReader` turns each row into a **dictionary**, using the column headings as keys. `list(reader)` collects those dictionaries into a list.

**Try it:** temporarily add `print(choices[0])` just below the block and run the script. Find the keys `prize` and `choice`. You are back to the lists and dictionaries from Class 3.

One detail matters: values read from this CSV are **strings**. To calculate the expected value of the first gamble:

```python
first_prize = int(choices[0]["prize"])
gamble_ev = 0.5 * first_prize
print("First gamble EV:", gamble_ev)
```

The result is **1.0 point**. Remove these temporary inspection lines after checking them.

## 3. Follow the calculation and saved output

Find the loop that counts `gamble` responses. It is the familiar combination of a list, loop, dictionary lookup, `if`, and counter.

Next, the `percentage` function converts a count and total into a percentage. We round it to one decimal place for display.

The writing block creates a CSV:

```python
with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["choice", "count", "percentage"])
    writer.writerow(["gamble", gamble_count, gamble_percentage])
```

`"w"` means **write**, replacing the previous contents of this output file. Each `writerow` writes one row. Keep `output_file` different from `input_file` so you never overwrite the source data.

**Check your interpretation:** 50% of what? It is 50% of the **14 decisions**, not 50% of participants. Each participant contributes seven responses.

## 4. Put your working program on GitHub

Git records versions of files. GitHub hosts repositories and lets people inspect, discuss, and share changes. The program still runs on your computer.

1. Sign in to [GitHub](https://github.com), or create a free account and verify your email.
2. Select **+ → New repository**. Name it `choice-summary`, choose **Public** if you want classmates to see it, and enable **Add a README file**. You may choose Private instead; only invited people will be able to access it.
3. Create the repository. Use **Add file → Upload files** to upload only `summarize_choices.py` and `sample_choices.csv` from your local folder.
4. Use the commit message **Add working choice summary** and commit these initial files to `main`.
5. Open `README.md` on GitHub, select its pencil/edit button, and replace the initial text with the description below. Commit the change to `main`.

```markdown
# Choice summary

A small Python program that summarizes fictional sure-versus-gamble choices.
The sample contains 14 decisions from two fictional participants.

## Run

Download and extract the repository. Open the folder in VS Code.
With Python 3.13 selected, run summarize_choices.py using Run Python File in Terminal.
No additional packages are needed.

The program reads sample_choices.csv and writes summary.csv beside the script.
The initial version reports 7 gamble choices out of 14 decisions (50.0%).

Based on the Class 10 exercise in Technion course 096609:
https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-10
```

A **commit** is a recorded version with a message explaining the change. Open the repository's commit history and find your uploads and README edit.

Only upload the two named teaching files. Do not upload your Class 9 database, exports, `.venv`, passwords, or real participant data. Uploading in the browser does **not** automatically synchronize your local folder.

## 5. Improve the program on a branch

The summary currently reports only gamble choices. Make it report **sure choices too**.

1. On GitHub, open the branch selector labeled `main`. Type `add-sure-summary` and create that branch from `main`. A branch lets you propose changes while leaving the main version intact.
2. In **VS Code**, edit your local `summarize_choices.py`:
   - Calculate `sure_count` from the total and gamble count.
   - Call `percentage` again to calculate `sure_percentage`.
   - Print both new values.
   - Add a second data row to the output CSV for `sure`.
3. Save and run the entire file. Check that the two counts sum to **14** and the two percentages sum to **100.0**. For these data, both choices have count **7** and percentage **50.0**.
4. With `add-sure-summary` still selected on GitHub, upload the revised `summarize_choices.py`. Confirm that you are committing to that branch. Use **Report sure choices alongside gambles** as the commit message.
5. Edit the branch's README to mention the two-row output, and commit that edit on the same branch.

<details>
<summary>Need a hint for the Python change?</summary>

After the gamble percentage is calculated, add:

```python
sure_count = total_decisions - gamble_count
sure_percentage = percentage(sure_count, total_decisions)
print("Sure choices:", sure_count)
print("Sure choices (%):", sure_percentage)
```

Inside the output-writing block, below the gamble row, add:

```python
    writer.writerow(["sure", sure_count, sure_percentage])
```

Keep this last line indented so it runs while the output file is still open.

</details>

**An extra check:** temporarily change one `sure` response in the sample to `gamble`. Predict the output, then run the script: gamble **8 / 57.1%**, sure **6 / 42.9%**. Restore that response and rerun before sharing your final version. This checks more than the easy 50–50 case.

## 6. Review, merge, and share

1. Open **Pull requests → New pull request** in your repository. Set **base: main** and **compare: add-sure-summary**.
2. Review the **diff**: removed lines appear red, added lines green. Check that only your intended Python and README changes appear.
3. Create the pull request. Describe the improvement and the two checks you ran.
4. Show a partner the diff. Can they explain why `total_decisions - gamble_count` gives the sure count for this dataset? Have them check the output too.
5. Once satisfied, choose **Merge pull request → Confirm merge**. Return to `main` and check that it now contains the updated program.

A **pull request** proposes a change; a **merge** incorporates it into the target branch. In your own repository, you control this decision. A branch in your repository is separate from a fork, which is your own copy of someone else's repository.

Finally, select **Code → Download ZIP** on `main`. Extract it to a separate folder and run that downloaded program. This checks that someone else receives everything needed, not just the copy that happens to work on your computer.

Show a partner your repository and give a **two-minute explanation**: what goes in, what comes out, one important line of Python, and the change visible in your pull request.

## Optional: use Codex as a reviewer

After completing your edit, open the local `class-10` folder in Codex and ask:

```text
Review summarize_choices.py without changing files. Does it count both choices correctly and preserve the input CSV? Explain one line I might misunderstand, and suggest one concrete check I can run myself. Keep your response short.
```

Check its answer against the code and your results. The exercise is complete without this step if you have no Codex usage available.

## Reference

| Tool | Purpose |
| --- | --- |
| `import csv` | Use Python's CSV tools |
| `Path(__file__).resolve().parent` | Locate the folder containing this script |
| `csv.DictReader(file)` | Read rows as dictionaries |
| `with open(...)` | Open a file and close it after the block |
| `int(...)` | Convert text to a whole number |
| `writer.writerow([...])` | Save one CSV row |
| Commit / branch / pull request / merge | Record / propose separately / review / incorporate a change |

Further help: [Python CSV documentation](https://docs.python.org/3.13/library/csv.html), [GitHub's Hello World walkthrough](https://docs.github.com/en/get-started/using-github/hello-world), [creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [uploading files](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), and [creating a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request).
