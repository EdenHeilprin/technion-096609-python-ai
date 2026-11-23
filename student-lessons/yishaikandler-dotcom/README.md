# Text Cleaning in Python

**Presenter** · yishai kandler  

If three students answer `"YES"`, `" yes "`, and `"Yes!"`, how many said yes? A Python counter sees three distinct labels. In this workshop we give equivalent answers one spelling before counting them.

[Get ready](#get-ready) · [Opening quiz](#opening-quiz) · [Live example](#live-example) · [Practice](#practice) · [Survey challenge](#survey-challenge) · [Closing quiz](#closing-quiz) · [Bonus](#bonus) · [Quick reference](#quick-reference)

## By the end of this lesson

Given a messy survey label, predict what three short string methods will return. Use the cleaned labels to explain a change in a frequency table. We’ll use the same idea as the Class 5 response counter and put the cleaning rule in a function like the ones from Class 6.

## Get ready

1. In Windows VS Code, choose **File → Open Folder** and open the outer course copy, the folder containing `student-lessons`. If you downloaded a course ZIP, extract it first. In Explorer, open **student-lessons → yishaikandler-dotcom → demo.py**. Keep [survey_responses.csv](survey_responses.csv) beside [demo.py](demo.py).
2. Choose **Terminal → New Terminal**. The terminal should start in the outer course folder (`dir` should list `student-lessons`). If this copy does not yet have a `.venv`, run `py -3.13 -m venv .venv`. This creates a local Python environment for the course. Run `.\.venv\Scripts\python.exe -m pip install --no-index -r student-lessons\yishaikandler-dotcom\requirements.txt`. The lesson uses only the standard library, so an empty requirements file is expected.
3. From that same terminal, run `.\.venv\Scripts\python.exe student-lessons\yishaikandler-dotcom\demo.py`. Look for five lines, starting with `Original: ' CLAUDE!! '`. The cleaned value is `'claude'`, and the last line shows the original again. Compare your output with the [live example](#live-example).
4. For the exercises below, select the course Python with **Ctrl+Shift+P → Python: Select Interpreter → .venv**. Open a **Command Prompt** terminal from the dropdown beside **+**, run `.venv\Scripts\activate.bat`, then `cd student-lessons\yishaikandler-dotcom`. Run `python practice.py`. Four quoted labels should appear. Keep this terminal open for `python starter.py` later.

## Opening quiz

**Kahoot.** Join using the presenter’s game PIN. Opening game link: https://kahoot.it/. Pick your best guess on each of the five questions. We’ll revisit the same questions at minute 40.

## Live example

**STOP & DISCUSS.** How often does the exact label `"yes"` appear in the three opening answers? Zero. How often did someone mean yes? Three. Counting exact text answers a different question until we decide which spellings belong together.

Display the first fictional row of the CSV. The survey asks whether the student uses AI for studying and which tool they use most. For these fixed-choice questions, edge spaces, capitalization, and exclamation marks carry no category information. Run the demo and predict each line before revealing it.

```text
Original: ' CLAUDE!! '
After strip: 'CLAUDE!!'
After lower: 'claude!!'
After replace: 'claude'
Original again: ' CLAUDE!! '
```

Each method returns a string. Saving that result lets the next step use it. The final line shows why we can still inspect the original answer.

## Practice

**LEARN / TRY IT NOW.** Open [practice.py](practice.py). For each row below, predict the result, edit the matching TODO, save, and run `python practice.py`. The quotes in the output help you see spaces.

| Minutes | Example | Expected value | Where it helps |
| --- | --- | --- | --- |
| 9–13 | `"  AI tools  ".strip()` | `"AI tools"` | Trim a pasted label and keep the space between words. |
| 13–17 | `"YES!".lower()` | `"yes!"` | Group uppercase and lowercase entries. |
| 17–21 | `"no!!".replace("!", "")` | `"no"` | Remove every occurrence of one known punctuation mark. |

**TRY IT NOW.** For exercise 4, start with `"  CHATGPT!!!  "`. Write one line that passes the result of each method to the next. Can you predict the intermediate value just before the exclamation marks disappear?

<details>
<summary>Check the chain</summary>

```python
clean = response.strip().lower().replace("!", "")
```

The intermediate value is `"chatgpt!!!"`. The final value is `"chatgpt"`.

</details>

## Survey challenge

**min · Work independently, then compare answers.** Can one cleaning function recover the intended choices across 40 fictional responses? The CSV reader and counters are provided. Edit only the three assignments in [starter.py](starter.py).

1. **CHECKPOINT 1 · Inspect.** Run `python starter.py`. Find two labels under `uses_ai` that you would count together. BEFORE and AFTER initially match because the function returns its input.
2. **CHECKPOINT 2 · Edit.** Inside `clean_text`, replace each `text = text` with one assignment. Trim the ends, lowercase the result, then remove every `!`. Save.
3. **CHECKPOINT 3 · Compare.** Run the same command. Read the number of categories and responses for each column. How many students named ChatGPT?
4. **CHECKPOINT 4 · STOP & DISCUSS.** Explain to a neighbor why the number of labels fell while the number of responses stayed at 40. Would throwing away exclamation marks make sense if the question asked students to describe their enthusiasm in their own words?

<details>
<summary>Answer and expected counts</summary>

```python
def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace("!", "")
    return text
```

| Column | Raw categories | Clean categories | Expected counts |
| --- | ---: | ---: | --- |
| uses_ai | 10 | 2 | yes 32, no 8 |
| favorite_tool | 19 | 4 | chatgpt 16, claude 8, gemini 8, none 8 |

Sixteen of the 40 responses named ChatGPT. Each row still contributes one vote per question. Alternate spellings now contribute to the same total. In free text, punctuation can carry meaning worth preserving.

</details>

## Closing quiz

**Kahoot.** Closing game link: https://kahoot.it/. Answer the same five questions. Which prediction would you change now, and which step explains why?

## Bonus

**Optional.** A regular expression (regex) describes a pattern. For three fictional phone formats, predict what `re.sub(r"\D", "", phone)` keeps. Run `python regex_bonus.py`. Each line should read `0541234567`. The pattern matches each non-digit and substitutes an empty string. One rule handles spaces, hyphens, and parentheses without listing each separator. [Bonus script](regex_bonus.py) · [Python regular expression operations](https://docs.python.org/3.13/library/re.html#re.sub)

## Quick reference

| When you see… | Read it as… |
| --- | --- |
| `text.strip()` | Remove whitespace from both ends. |
| `text.lower()` | Convert cased letters to lowercase. |
| `text.replace("!", "")` | Remove every literal exclamation mark. |
| `a.strip().lower()` | Use the trimmed string as input to the next method. |
| `text = text.strip()` | Save the returned value for the next line. |

## Sources and further learning

The method definitions come from the Python 3.13 documentation. The survey, examples, and questions were written for this workshop. [str.strip](https://docs.python.org/3.13/library/stdtypes.html#str.strip) · [str.lower](https://docs.python.org/3.13/library/stdtypes.html#str.lower) · [str.replace](https://docs.python.org/3.13/library/stdtypes.html#str.replace)

The supplied counting code reads each CSV row by column name and tallies each distinct label. [csv.DictReader](https://docs.python.org/3.13/library/csv.html#csv.DictReader) · [collections.Counter](https://docs.python.org/3.13/library/collections.html#collections.Counter)

[Instructor guide and quiz key](instructor/teaching_guide.md)
