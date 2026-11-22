# Cleaning text in Python

**Yishai Kandler · 45 minutes · Live demo and two games**

A classmate types `yes`. Another types ` YES `. A third writes “Yes, if I can work with a partner.” If the survey question is “Would you try another Python puzzle?”, which differences can Python tidy up? Which ones change the meaning?

## By the end of this lesson

You can take a raw survey answer, predict what `.strip()`, `.lower()`, and `.replace()` will do to it, and decide whether the cleaned text is clear enough to count. We’ll use the comparisons, loops, and functions from earlier classes. Keep the original answer beside the cleaned copy so you can explain each decision.

## Get ready

1. Open the outer course folder in VS Code and open [demo.py](demo.py) inside `student-lessons/yishaikandler-dotcom`. The [eight fictional answers](fictional_responses.csv) come with the lesson. Python 3.13 includes everything the demo imports.
2. If the course folder has no `.venv` yet, open **Terminal → New Terminal** there. Run `py -3.13 -m venv .venv` on Windows or `python3.13 -m venv .venv` on macOS.
3. Open the command palette with **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on macOS. Choose **Python: Select Interpreter** and select the course folder’s `.venv`. Open the Python file and click **▶ Run Python File** at the upper right. Expect eight rows, each showing an original answer, its cleaned text, and a label.

### Using the live poll

Answer the [one-question class poll](https://docs.google.com/forms/d/e/1FAIpQLSftFrMOZL0QeG3nbh_NIH9UfnkjPFR0ACBn0ZKM80kaCdDNQg/viewform) in your own words. Your response may appear on screen. Leave out names and personal details. You can also play along using the fictional examples.

**Presenter:** In the form editor, choose **Responses → ⋮ → Download responses (.csv)**. Extract the ZIP into Downloads. Check the answers privately before sharing your screen. In VS Code, right-click this lesson’s folder and choose **Open in Integrated Terminal**. Use the first command below to show only the answers. After the class votes, run it again without `--raw` to reveal the cleaning and counts.

```powershell
# Windows, starting in the lesson folder. Substitute the actual extracted file path.
..\..\.venv\Scripts\python.exe demo.py --raw "C:\path\to\responses.csv"
```

On macOS use `../../.venv/bin/python demo.py --raw "/path/to/responses.csv"`. Omit the CSV path to use the fictional answers. If the poll is slow or everyone types the same thing, switch to the fictional answers for the games. Keep live exports in Downloads.

## Lesson plan

| Minutes | What we’ll do |
| --- | --- |
| 0–5 | Take the poll. While responses arrive, type two versions of the same answer on screen and ask which characters differ. |
| 5–12 | **Game 1 — Beat Python.** Show the raw answers. Everyone privately predicts the exact `yes` count and the number they personally interpret as yes. Vote by chat or hands. Ask two people who disagree which row explains the difference. |
| 12–22 | **Live demo.** Walk through the three string operations below. Give classmates a minute to fill in the trace, reveal the result, then run the full script on the poll. If anyone loses track, trace just one row together. |
| 22–32 | **Game 2 — Break my rule.** Predict what an overbroad replacement will break (3 min). Make one change to the real counting rule and rerun it (4 min). Invite a classmate to invent an answer that should still go to review (3 min). |
| 32–40 | **Human decision round.** Vote on the conditional answer, hear two reasons, then change the purpose of the count and vote again. |
| 40–45 | **Exit ticket and questions.** Predict the cleaned text and label for `" Y "` and `"not sure"`. Reveal the answers (`"y"` → yes, `"not sure"` → review). Take questions. |

## A worked example

Look at `clean_answer` in [demo.py](demo.py). Python reads the methods from left to right. Try them one at a time in a Python terminal. The quotes printed by `repr` help you spot spaces.

```python
raw = " I’M IN "
trimmed = raw.strip()
lowercase = trimmed.lower()
clean = lowercase.replace("’", "'")
print(repr(raw), repr(trimmed), repr(lowercase), repr(clean), sep="\n")
```

Predict each result for the last row of the fictional survey. At which step do the curly and straight apostrophes become identical?

| Original | After strip | After lower | After replace |
| --- | --- | --- | --- |
| `" YES "` | `"YES"` | `"yes"` | `"yes"` |
| `" I’M IN "` | ? | ? | ? |

<details>
<summary>Reveal the trace and count</summary>

The second row goes from `"I’M IN"` to `"i’m in"` to `"i'm in"`. The space between the words stays. The original string keeps its outer spaces and curly apostrophe.

Now run the sample. Only one original answer equals `"yes"`. After cleaning, `label_answer` counts the exact answers `yes` and `y` as yes, and `no` and `n` as no. Everything else goes to review. The result is **3 yes, 2 no, 3 review**. Trace which counter changes for `" I’M IN "`. It has been cleaned successfully even though the current rule sends it to review.

</details>

## Try it yourself

**Game 2.** Someone suggests expanding the letter y with `clean.replace("y", "yes")`. Try it on `"y"` and `"yesterday"`. Predict both outputs before running the expressions.

Now suppose the class agrees to count the whole answer “I’m in” as a yes. In `label_answer`, find `if clean in ("yes", "y"):`. Add one spelling to that tuple. Which of the eight fictional rows will move? Save, run **▶** with the fictional CSV, and compare the counts. Undo your edit, save, and rerun to restore the starting example.

<details>
<summary>Reveal the answer and check your change</summary>

Replacing every y gives `"yes"` and `"yesesterdayes"`. Both ends of “yesterday” changed. An exact comparison lets the class expand an abbreviation without rewriting ordinary words.

The edited line is `if clean in ("yes", "y", "i'm in"):`. The curly apostrophe in the file becomes a straight one in `clean_answer`, so the eighth row now matches. Expect **4 yes, 2 no, 2 review**. After undoing the change, expect **3 yes, 2 no, 3 review** again. What would happen if you added the curly spelling to the rule instead?

</details>

**Human decision round.** Show the fictional answer “Yes, if I can work with a partner.” You’re counting definite volunteers for a *solo* puzzle. Vote: yes, no, or needs clarification? Now you’re counting people who expressed *any interest*. Who changed their vote, and why?

<details>
<summary>Discuss one defensible interpretation</summary>

For solo volunteers, ask whether the person would work alone. For general interest, count the interest and keep the partner condition alongside it. The characters in the answer stayed the same. The question you wanted the count to answer changed.

</details>

## Quick reference

| Expression | Effect |
| --- | --- |
| `repr(raw)` | Shows where the string starts and ends. |
| `raw.strip()` | Removes whitespace from both ends. |
| `raw.lower()` | Returns a lowercase copy. |
| `raw.replace(old, new)` | Replaces every matching substring by default. |
| `clean in ("yes", "y")` | Checks the whole cleaned answer against two accepted spellings. |

## Sources and further learning

- Check the method definitions and try the examples in the [Python 3.13 string documentation](https://docs.python.org/3.13/library/stdtypes.html#string-methods).
- See how the script reads the survey question by its column heading in the [Python CSV documentation](https://docs.python.org/3.13/library/csv.html#csv.DictReader).
- See the CSV download instructions in [Google Forms Help](https://support.google.com/docs/answer/139706).
