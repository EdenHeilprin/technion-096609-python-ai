# Compare two group averages with pandas

**Presenters:** Student Rehearsal A and Student Rehearsal B

You have response times from people who saw brief or detailed task instructions. We will use a small fictional CSV to see how pandas reads a table and calculates an average for each group. Times are in milliseconds (ms): 1000 ms is one second.

## By the end of this lesson

- Read a CSV and recognize a pandas table, called a DataFrame.
- Compare group averages and see how an inclusion rule changes them.

## Get ready

1. Open your cloned course folder in **VS Code**. In the Explorer, find **student-lessons → student-rehearsal**. Keep `demo.py` and `responses.csv` together.
2. Choose **Terminal → New Terminal**. Its starting folder should be the outer course folder, not `student-rehearsal`. Use the Class 10 `.venv` if you already made it; otherwise create it with the first command below. Run the second command to install pandas.

**Mac, zsh terminal:**

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r student-lessons/student-rehearsal/requirements.txt
```

**Windows, Command Prompt terminal:**

```bat
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r student-lessons\student-rehearsal\requirements.txt
```

3. Open `demo.py`. Press **Cmd+Shift+P (Mac)** or **Ctrl+Shift+P (Windows)**, choose **Python: Select Interpreter**, and select the `.venv` in your outer course folder.
4. Click the **triangle ▶ at the upper right of the code editor**, choosing **Run Python File in Terminal** if the adjacent menu offers more than one action. The output should show six rows and group averages of **800 ms for brief** and **700 ms for detailed** instructions.

## A worked example

Open [responses.csv](responses.csv). Each row is one fictional participant's response time. Before running [demo.py](demo.py), calculate the average of 600, 800, and 1000: it is 800.

The first new instruction reads the CSV:

```python
responses = pd.read_csv(data_file)
```

`pd` is the short name we gave pandas. `responses` now holds the rows and columns. `Path(__file__).parent` in the script finds the folder containing the script, so it can find the CSV even if the terminal is elsewhere.

Next, the script groups the rows by instruction type, selects the response-time column, and calculates each group's mean:

```python
group_means = responses.groupby("instructions")["response_ms"].mean()
```

Read this left to right: **group → choose a column → calculate**. The `print()` calls display the table and the result.

**Expected result:** brief instructions have a mean of **800 ms**; detailed instructions have a mean of **700 ms**. These are descriptions of this tiny example, not evidence that one instruction style causes faster responses.

## Try it yourself

Suppose you want to see the result when keeping only times of **900 ms or less**. Predict the two means before running anything.

Add this line immediately after `responses = pd.read_csv(data_file)`:

```python
responses = responses[responses["response_ms"] <= 900]
```

Save the file and click the triangle again. How many rows remain, and do the group averages still differ?

<details>
<summary>Answer and discussion</summary>

Five rows remain. The 1000 ms response is removed from the brief group, leaving 600 and 800, whose mean is **700 ms**. The detailed group's mean stays at **700 ms**.

The expression inside the brackets asks which rows satisfy the comparison. The outer brackets keep those rows. We already know comparisons from Python; pandas applies this one across a column.

Why should a researcher decide and report exclusion rules rather than quietly choose the version with the preferred result?

After the activity, remove the added line and save to restore the original example.

</details>

## Quick reference

| Tool or idea | What it does |
| --- | --- |
| `pd.read_csv(path)` | Read a CSV into a table |
| `table["column"]` | Select a column |
| `table[condition]` | Keep rows where a condition is true |
| `.groupby("instructions")` | Separate rows into instruction groups |
| `.mean()` | Calculate an average |

## Sources and further learning

- [pandas: read tabular data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- [pandas: calculate summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
- The example and fictional data were created for this student-workflow rehearsal, using the pandas operations described in these tutorials.
