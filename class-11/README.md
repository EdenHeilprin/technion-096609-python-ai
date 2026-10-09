# Class 11 — From Choices to Evidence

You have an experiment and a table of responses. Now answer its question: **how does choosing the gamble vary as the guaranteed alternative increases?** You will build the first analysis yourself, then direct Codex to turn it into a reproducible script.

By the end, you will have a checked dataset, an offer-by-offer summary, a figure, and an explanation of what the figure can—and cannot—tell you.

## Get ready

1. [Download the Class 11 files](https://raw.githubusercontent.com/EdenHeilprin/technion-096609-python-ai/refs/heads/main/class-11/class-11-files.zip).
2. Extract to a new `class-11` folder next to your earlier classes. Keep your previous work.
3. Open `class-11/research-project` in VS Code and Codex. Follow [SETUP.md](SETUP.md) to prepare and select this project's Python environment.
4. Open `data/SOURCE.md` and `data/CODEBOOK.md`.

Start with the supplied **synthetic teaching data** so that you can check your calculations against known results. Later, the same script can analyze the class's custom oTree export. The data file contains one row per round, not one row per person.

**Today's route:** inspect the data, build a summary, make a figure, delegate the repeatable workflow, and explain the result.

## 1. Read the table before asking for a result

Open `analysis/inspect_data.py`, read its comments, and use **Run Python File**. The script finds the CSV relative to its own location, so it works without changing the terminal's current folder.

Focus on these operations:

```python
print(data.head())       # Show the first five rows.
print(data.shape)        # Report the number of rows and columns.
print(data.dtypes)       # Show the type of each column.
print(data.isna().sum()) # Count blank cells in each column.
```

`data` is a pandas **DataFrame**: a table with named columns. pandas is the Python package that helps us inspect and transform tables.

You should find **96 rows, 9 columns, and 16 participant codes**, with four blanks in `choice` and four in `confidence`. Look at the end of the CSV: SYN16 answered only the first two rounds. The remaining rows exist, but their responses are blank.

Before continuing, explain why neither “96 participants” nor “every row is a completed choice” is correct.

## 2. Decide which participants belong in the analysis

Our rule is: **include a participant only if all six rounds have a valid choice and confidence rating.** This gives each included person the same six offers. A blank response is not a sure choice and is not confidence 0.

Open `analysis/my_analysis.py` and run it. Its provided helper reads the export, checks the study values and unique participant/round keys, and applies the rule. You do not need to rewrite that helper. The table it prints explains each participant's status.

Expected result: **15 included participants, 1 excluded participant, 90 included trial rows.** SYN16 is excluded because four rounds are unanswered. If a row is malformed or duplicated, the helper stops and tells you what needs investigation; it does not quietly repair the data.

`raw` retains the original table in memory. `clean` contains the eligible trials. The CSV itself has not changed.

## 3. Build the first summary in small steps

Work in `analysis/my_analysis.py`. Add each block below its corresponding comment, save, and run the **whole file** after each addition. This keeps the steps in a reproducible order.

### Select useful rows and columns

First, inspect one fictional participant:

```python
# .loc selects the rows matching our condition and the columns we want to see.
one_person = clean.loc[
    (clean["session_code"] == "SYNTHETIC") & (clean["participant_code"] == "SYN01"),
    ["round_number", "sure_points", "choice", "confidence"],
]
print(one_person)
```

The comparison creates a True/False test for each row. `&` means that **both** conditions must hold. The second part of `.loc` names the columns to display. Keep the parentheses around each comparison.

SYN01 has six gamble choices. Change the participant code to `SYN15`: this person has six sure choices. These are invented patterns, but they help us check that we are reading the table correctly.

### Make the outcome easy to count

```python
# True becomes 1 and False becomes 0 when converted to an integer.
clean["chose_gamble"] = (clean["choice"] == "gamble").astype(int)
print(clean[["choice", "chose_gamble"]].head())
```

This new column is a convenient numeric version of `choice`. Its **sum** counts gamble choices. Its **mean** is the proportion of choices that are gambles.

### Group choices by guaranteed offer

```python
# Combine the rows for each offer into counts, keeping sure_points as a column.
by_offer = clean.groupby("sure_points", as_index=False).agg(
    gamble_count=("chose_gamble", "sum"),
    choice_count=("chose_gamble", "size"),
)

# Divide the number of gambles by the number of included choices at that offer.
by_offer["gamble_rate"] = by_offer["gamble_count"] / by_offer["choice_count"]
print(by_offer)
```

`groupby` puts matching rows together. Inside `.agg`, each new column has a source column and an operation. For example, `gamble_count=("chose_gamble", "sum")` means “sum `chose_gamble` in each group and call the result `gamble_count`.”

Check one number manually: at the 3-point offer, **12 of 15** included participants chose the gamble. The rate is `12 / 15 = 0.8`, or **80%**. Dividing by all 90 trials would answer a different question.

<details>
<summary>Check the full synthetic-data summary</summary>

| Guaranteed offer | Gambles | Included choices | Gamble rate |
| --- | ---: | ---: | ---: |
| 2 | 14 | 15 | 93.3% |
| 3 | 12 | 15 | 80.0% |
| 4 | 10 | 15 | 66.7% |
| 6 | 6 | 15 | 40.0% |
| 7 | 3 | 15 | 20.0% |
| 8 | 1 | 15 | 6.7% |

Across all offers: 46 gamble choices out of 90, or 51.1%. Each offer's denominator is 15; the overall denominator is 90.

</details>

## 4. Save a table and make a figure

Add `OUTPUT_DIR` to the existing import near the top of your file:

```python
from settings import DATA_FILE, DATA_LABEL, OUTPUT_DIR
```

Add this block after the summary:

```python
# Create the output folder if needed, then save without a redundant row-number column.
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
by_offer.to_csv(OUTPUT_DIR / "my_choice_by_offer.csv", index=False)
```

Then add:

```python
import matplotlib.pyplot as plt

# Create a figure and its plotting area.
figure, axis = plt.subplots(figsize=(8, 5))
axis.plot(by_offer["sure_points"], by_offer["gamble_rate"] * 100, marker="o")
axis.set_xlabel("Guaranteed alternative (points)")
axis.set_ylabel("Gamble choices (%)")
axis.set_title(DATA_LABEL)
axis.set_xticks(by_offer["sure_points"])
axis.set_ylim(0, 100)

# Save an image that can be opened directly from the VS Code file list.
figure.tight_layout()
figure.savefig(OUTPUT_DIR / "my_choice_by_offer.png", dpi=150)
plt.close(figure)
```

Open the new PNG in `outputs/synthetic_choices`. Point to a dot and explain both axes and the denominator behind it.

The decline is a feature of our fictional example. With actual data, the shape may differ. Also, everyone received the offers in ascending order: **offer size and order change together**. This figure alone cannot separate them or establish a causal effect.

## 5. Delegate the repeatable workflow

You have now built the central calculation. Ask Codex to turn it into a complete, documented analysis:

The requested `summary.json` is a small text file of named results. Its SHA-256 hash is a fingerprint identifying the exact input file, so you can tell which data produced an output.

> Read `data/CODEBOOK.md`, `data/SOURCE.md`, `analysis/settings.py`, `analysis/study_data.py`, and my `analysis/my_analysis.py`. Create `analysis/analyze_choices.py` for the full-v1 study. Reuse the provided validation and six-complete-round inclusion rule. Preserve the original CSV and my working file. Save clean trials, all participants' inclusion/exclusion status, the offer summary, a one-row-per-participant summary, and a labeled offer-by-offer gamble-rate figure under the configured output folder. Save `summary.json` with the exact source filename and SHA-256 hash, synthetic status, participant/trial counts, exclusion reasons, and unrounded rates. Use clear English # comments for each important step. Run the script with this project's Python, compare its counts and rates with my calculation, and report the files created and any mismatch. Do not add significance tests or change the experiment.

While it works, follow which files it reads, changes, and runs. When finished, inspect `analyze_choices.py` and open the outputs—not just the chat summary.

If generation stalls, move to the working checkpoint below. The essential outcome is a checked summary and figure that you can explain; leave time for that evidence check.

Check that `participant_summary.csv` has **15 rows**, whereas `clean_trials.csv` has **90**. Each included participant supplies six trials. This is why we can average their individual gamble rates without giving more weight to someone who answered more questions.

**If you are working without Codex access, or need a reference:** the download includes `checkpoints/analysis/research-project`. Open that folder as a separate project, follow the setup guide again for its environment, and run `analysis/analyze_choices.py`. Keep your working file in the original project; compare the two implementations rather than overwriting it.

## 6. Use an actual class export

If the instructor provides a **full-v1 custom export**, save it unchanged as `data/classroom_choices.csv`. In `analysis/settings.py`, change these three settings:

```python
DATA_FILE = PROJECT_DIR / "data" / "classroom_choices.csv"
DATA_LABEL = "Classroom pilot"
IS_SYNTHETIC = False
```

Run the inspection and completed analysis again. Results now go to `outputs/classroom_choices`. Read the new inclusion counts and figure; the synthetic example's expected numbers no longer apply. Keep real responses and their derived files local.

If no class export is available, the synthetic example completes every activity in this lesson.

## Finish with an explanation

Show a partner your figure—or explain it aloud if you are working alone—and describe:

1. What one raw row represents and how many people were included.
2. How one plotted percentage was calculated.
3. What pattern is present and why it does not isolate an offer-size effect from order.

Keep the analysis script, its original input, and its generated outputs for Class 12.

## Quick reference

| Term | Simple meaning | Example |
| --- | --- | --- |
| DataFrame | A table in Python | `data` |
| Column selection | Choose a variable | `data["choice"]` |
| Boolean filter | Keep rows meeting a condition | `data.loc[data["choice"] == "gamble"]` |
| Derived column | Calculate a new variable from existing ones | `chose_gamble` |
| `groupby` | Put rows into groups for a calculation | Group by `sure_points` |
| `.agg()` | Name calculations for each group | Sum and count choices |
| Denominator | What a count or rate is relative to | 15 choices at one offer |
| Participant-level table | One row per person, not per trial | `participant_summary.csv` |
| `index=False` | Do not save pandas' extra row labels | `to_csv(..., index=False)` |

[Setup](SETUP.md) · [Troubleshooting](TROUBLESHOOTING.md)
