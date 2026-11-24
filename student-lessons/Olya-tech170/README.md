# Student lesson — From CSV to group averages with pandas

**Presenters:** Naama Cohen, Olya Brailovskaya

A CSV file stores data in rows and columns, like a spreadsheet. Today you’ll use **pandas**, a Python library for working with tables, to open a CSV, keep the rows you need, and compare averages for two groups.

## By the end of class

You should be able to

- open a CSV as a pandas table and preview its first five rows;
- select a subset of a `DataFrame` by filtering rows and choosing columns;
- calculate a mean for each group and explain why changing the filter can change the results.

## Get the files for this class

Open this lesson’s folder in the course materials. Check that it contains `README.md`, `demo.py`, `titanic.csv`, and `requirements.txt`. Keep `demo.py` and `titanic.csv` together because the script looks for the CSV beside it.

## Get ready

1. In VS Code, use **File → Open Folder** to open **this lesson folder**. The Explorer should show [demo.py](demo.py), [titanic.csv](titanic.csv), and [requirements.txt](requirements.txt).
2. In the VS Code menu bar at the top, click **Terminal → New Terminal**. Enter the commands for your system there, one line at a time, and press **Enter** after each command. This creates a Python 3.13 environment called `.venv` and installs pandas into it. 

   **Mac**

   ```bash
   python3.13 -m venv .venv
   .venv/bin/python -m pip install -r requirements.txt
   ```

   **Windows — Command Prompt**

   ```bat
   py -3.13 -m venv .venv
   .venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Open `demo.py`. Press **Cmd+Shift+P** on Mac or **Ctrl+Shift+P** on Windows, select **Python: Select Interpreter**, and choose the interpreter in this lesson's `.venv`. Its path ends in `.venv/bin/python` on Mac or `.venv\Scripts\python.exe` on Windows.
4. Leave `demo.py` open. After making your prediction below, run it in Activity 1. The starter should display five rows and **Passenger rows: 891**. You will add the filter and group averages in Activities 2 and 3.

<details>
<summary>Stuck during setup? Ask AI for one check</summary>

Copy this prompt into an AI chat and fill in the brackets. You can paste the terminal output or attach a screenshot if your chat supports images.

```text
I’m setting up a beginner pandas lesson in VS Code. The lesson uses
Python 3.13. I open the lesson folder, create a virtual environment
called .venv, install pandas from requirements.txt, and select the
Python interpreter from .venv in VS Code.

My operating system: [Mac or Windows]
The setup step I’m on: [creating .venv / installing pandas /
selecting the interpreter / running demo.py]
What I typed or clicked: [paste the exact command or describe the click]
What I see: [paste the full terminal output or attach a screenshot.
If there is no output, say how long you waited and whether you can
type a new command.]

Help me figure out which setup step failed or is still running.
Explain the clue you see and give me one check to try. Tell me
where to do it and what I should see if it works. If you need more
information, ask for one detail first.
```

</details>

##  Which Titanic rows should count?

- In the `Survived` column, `1` means the passenger survived and `0` means the passenger did not survive.
- `Fare` is the cost of the trip recorded for that passenger.

These are the first five rows of `titanic.csv`. Identify the preview row numbers where `Survived` equals `1`. Then read the `Fare` in each of those rows.

| Preview row | Survived | Sex | Fare |
| ---: | ---: | --- | ---: |
| 1 | 0 | male | 7.25 |
| 2 | 1 | female | 71.2833 |
| 3 | 1 | female | 7.925 |
| 4 | 1 | female | 53.1 |
| 5 | 0 | male | 8.05 |

<details>
<summary>Check your prediction</summary>

Rows **2, 3, and 4** match. Their fares are **71.2833**, **7.925**, and **53.1**. In Activity 2, you will see how pandas applies this same comparison to the whole table.

</details>

## A DataFrame is a table with rows and columns

A pandas table is called a **DataFrame**. In our Titanic table, each row represents one passenger, and each column holds one kind of information.

```python
from pathlib import Path

import pandas as pd


# Find the CSV beside this script, even if VS Code runs it from another folder.
csv_path = Path(__file__).with_name("titanic.csv")
passengers = pd.read_csv(csv_path)

print("First five rows:")
print(passengers.head())
print("Passenger rows:", len(passengers))
```

- **Find the file.** `from pathlib import Path` gives us a tool for working with file locations. `__file__` is the path to `demo.py`. `.with_name("titanic.csv")` uses the same folder and changes the filename to `titanic.csv`.
- **Load the table.** `import pandas as pd` lets us use pandas under the short name `pd`. `pd.read_csv(csv_path)` loads the CSV into a DataFrame called `passengers`.
- **Preview and count.** `head()` shows the first five rows. `len(passengers)` counts all the rows, and the last `print()` displays that count after **Passenger rows**.

## Activity 1 — read the CSV and check the preview

1. Run `demo.py`. If you see `ModuleNotFoundError` for pandas, check that VS Code is using the interpreter from step 3 of **Get ready**.
2. In the terminal, find First five rows. You may see extra columns or ..., which means some columns are hidden in the terminal preview. The numbers at the far left are pandas row labels, starting at 0.
3. Find **Passenger rows**. How many rows did pandas load? How many did it display in the preview?

<details>
<summary>Check your result</summary>

Pandas loaded **891 rows** and displayed **five** in the preview. `head()` only limits the preview. The rest of the table is still available in `passengers`.

</details>

4. **Change the preview yourself.** Edit `demo.py` to show the **first 10 rows** and update the heading above the preview. Before running the file, predict whether **Passenger rows** will change. Run it and explain what you see.



<details>
<summary>Check one possible solution</summary>

```python
print("First ten rows:")
print(passengers.head(10))
```

The preview now shows **10 rows**. **Passenger rows** still shows **891** because `head(10)` changes the preview and `len(passengers)` counts the full table.


</details>

Before moving on, restore the original heading and the five-row preview.

## A filter keeps rows that match a condition

This comparison checks whether the recorded fare is greater than 30. It gives one `True` or `False` for each row.

```python
higher_fare = passengers["Fare"] > 30
higher_fare_passengers = passengers[higher_fare]
```

The first line checks the condition. The second line keeps the matching rows. 

## Choosing columns

Use one column name to select a single column, such as `passengers["Fare"]`. To select several columns, put their names in a list inside the brackets.

```python
print(higher_fare_passengers[["Survived", "Fare"]].head())
```

Read this from left to right. Start with the filtered table, choose two columns, and preview the first five rows.

## Activity 2 — filter rows and choose columns

Add your code at the end of `demo.py`.

1. Create a table called `survivors` that keeps passengers whose `Survived` value is `1`. Print the number of rows in the table.
2. Print the first five rows of `survivors`, showing only `Sex` and `Fare`.
3. Before running the file, predict which column headings will appear. Will the survivor count be smaller than **Passenger rows**?
4. Save and run the file. Explain to a partner which line chooses the passengers and which line chooses the information you see about them.

<details>
<summary>Check one possible solution</summary>

```python
survived = passengers["Survived"] == 1
survivors = passengers[survived]

print("Survivor rows:", len(survivors))
print(survivors[["Sex", "Fare"]].head())
```

The filter keeps **342** of the **891** passenger rows. The preview shows only `Sex` and `Fare`. The `survivors` table still has all its columns.

</details>


## A group mean gives one average per group

Suppose you want to compare average fares for passengers who survived and passengers who did not survive. Group all passenger rows by `Survived`, select `Fare`, and calculate a mean for each group.

```python
passengers.groupby("Survived")["Fare"].mean()
```

`groupby("Survived")` separates rows with `0` from rows with `1`. `["Fare"]` selects the numbers to average. `mean()` calculates one average for each group by adding its fares and dividing by the number of fares.

## Activity 3 — compare average fares among survivors

**Our question**  
Among the passengers in this file who survived, what was the average recorded fare in each of the two groups in the `Sex` column?

1. At the end of `demo.py`, choose the table and the grouping column that answer this question. Calculate and print the two mean fares.
2. Before running the file, predict which labels will appear next to the means. 
3. Change the calculation to use all passenger rows.

<details>
<summary>Check one possible solution</summary>

```python
analysis_rows = survivors
mean_fare = analysis_rows.groupby("Sex")["Fare"].mean()
print(mean_fare)
```

`survivors` is the filtered table from Activity 2. Grouping by `Sex` gives one mean fare for each of the two labels, `female` and `male`.

For step 3, replace the first line with `analysis_rows = passengers`. The same two group labels appear, and the means now use all passenger rows.

The table below shows the results rounded to two decimal places.

| Rows used | female mean fare | male mean fare |
| --- | ---: | ---: |
| Survivors only | 51.94 | 40.82 |
| All passenger rows | 44.48 | 25.52 |

Both means decrease. In each group, the added passengers had a lower average fare than the survivors in that group.

</details>

**Optional bonus — make the output easier to read.** Replace `print(mean_fare)` with:

```python
print(mean_fare.round(2))
```

The `2` tells pandas to round each value to two decimal places. For example, `51.937` becomes `51.94`. This line prints the rounded values. The original values in `mean_fare` are still available.

## Optional bonus activities — if time allows

### Bonus 1 — find the five highest fares

Find the five highest recorded fares among the survivors. Sort `survivors` by `Fare` from highest to lowest, then show only `Sex` and `Fare` for the first five rows.

Use `sort_values()` with `ascending=False` to put the largest values first. Before running your code, explain why you need to sort before using `head()`.

<details>
<summary>Check one possible solution</summary>

```python
highest_fares = survivors.sort_values("Fare", ascending=False)
print(highest_fares[["Sex", "Fare"]].head())
```

Sorting first puts the highest fares from the entire filtered table at the top. Taking five rows first would limit the search to those five passengers.

</details>

### Bonus 2 — compare each fare with the average

Calculate the average fare for all passengers. Add a column called `Fare_difference` that shows how much each fare is above or below that average. Subtract the average from each value in `Fare`. Before running your code, predict what a negative result means. Then preview `Fare` and `Fare_difference` side by side.

<details>
<summary>Check one possible solution</summary>

```python
average_fare = passengers["Fare"].mean()
passengers["Fare_difference"] = passengers["Fare"] - average_fare
print(passengers[["Fare", "Fare_difference"]].head().round(2))
```

The average fare is about `32.20`. A fare of `7.25` is about `24.95` below average, so its difference is `-24.95`. A positive difference means the fare was above average.

</details>

## What we learned

You loaded the Titanic CSV into a DataFrame and used `head()` to preview it. Then you filtered the table to keep passengers who survived and displayed just the `Sex` and `Fare` columns. Finally, you calculated the mean fare for each group in `Sex` and compared the results for survivors with the results for all passengers in the file.

## Pandas reference

### Central terms

| Term | Simple meaning | Example from this lesson |
| --- | --- | --- |
| CSV | A text file that stores tabular data | `titanic.csv` |
| DataFrame | A pandas table with rows and named columns | `passengers` |
| Condition | A question with a `True` or `False` answer for each row | `passengers["Survived"] == 1` |
| Filter | Keeps rows where the condition is `True` | `passengers[survived]` |
| Group mean | The average of the selected values in each group | Mean `Fare` for each label in `Sex` |

### Commands from this lesson

| Code | What it does |
| --- | --- |
| `pd.read_csv(csv_path)` | Reads the CSV into a table. |
| `passengers.head()` | Previews the first five rows. |
| `len(passengers)` | Counts the rows in the table. |
| `passengers[survived]` | Keeps rows where the condition in `survived` is `True`. |
| `analysis_rows.groupby("Sex")["Fare"].mean()` | Calculates one mean fare per group. |

## Companion tutorial

Read the official pandas introduction to see how a `DataFrame` represents a table. Start with the Titanic example and find where the tutorial selects one column by name. [What kind of data does pandas handle?](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)

For more practice, see the pandas tutorials on [selecting rows and columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html) and [calculating summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html).

The lesson’s CSV uses the `Survived`, `Sex`, and `Fare` columns from the supplied historical Titanic data.
