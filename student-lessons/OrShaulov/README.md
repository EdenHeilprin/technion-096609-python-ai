# The History of Python: how a language built for people took over research and AI

**Presenters:** Or Shaulov and Michael Kometiani

**Length:** 40–50 minutes

We are learning Python in this course, but where did it come from, and why does it look the way it does? Python was designed for the *human* reader rather than the machine, and that decision helps explain how a holiday hobby project became the language of research and AI.

## 🎮 Opening quiz

Join at **[kahoot.it](https://kahoot.it)**. The game PIN and QR code will appear on the screen in class.

## 🎞️ The presentation

### [▶ Open the slides: History_of_Python.pptx](History_of_Python.pptx)

(Please view it in slideshow mode, one slide at a time, and don't scroll ahead to the answers.)

## 🧪 Activity: The Zen of Python

1. In VS Code, create a new file named `poem.py`.
2. Type this line into it:

```python
import this
```

3. Run the code. A poem called *The Zen of Python* appears in the terminal: Python's design philosophy, written by Tim Peters in 1999 and hidden inside the language itself.

**Your turn:** choose one line of the poem. Explain it in plain words.

<details>
<summary>Answer and discussion</summary>

| Line of the Zen | In plain words | Example from the lesson |
| --- | --- | --- |
| Readability counts. | Code is read far more often than it is written. | Travis Oliphant could read his own Python a year later, but not his Perl. |
| Special cases aren't special enough to break the rules. | No surprising exceptions. | ABC's *Fair-Expectation Rule*, linked to the Gestalt principle of good continuation. |
| Errors should never pass silently. | When something goes wrong, the program should say so. | In Python 2, the mean of `[512, 430, 610, 475]` came out as 506 instead of 506.75, with no warning. |
| In the face of ambiguity, refuse the temptation to guess. | When it's unclear what you meant, stop and ask. | `"3" + 3` raises an error in Python; JavaScript guesses `"33"`. |
| There should be one-- and preferably only one --obvious way to do it. | Fewer choices, less confusion. | A reply to Perl's motto, "There's more than one way to do it." |

</details>

## Recap

<details>
<summary>Python's story in four milestones</summary>

| Milestone | What happened |
| --- | --- |
| 1991 | Guido van Rossum releases Python publicly, after starting it over the 1989 Christmas break. He builds it on ABC, a teaching language, to keep its readability and accessibility. |
| 2003 | Neurobiologist John D. Hunter releases matplotlib to analyze brain signals without paid software, and scientists start adopting Python. |
| 2008–2020 | Python 3 deliberately breaks compatibility; the move from Python 2 takes more than a decade. |
| 2018–2019 | Guido steps down as "Benevolent Dictator For Life"; a five-person Steering Council takes over. |

</details>

## Sources and further learning

- Meertens, L. (2022). [The origins of Python](https://doi.org/10.37282/991819.22.56). *Inference: International Review of Science, 7*(3).
- CultRepo. (2025). [*Python: The documentary*](https://www.youtube.com/watch?v=GfH4QL4VqJ0) [Film]. YouTube. Recommended viewing.
- Python Software Foundation. [Why is it called Python?](https://docs.python.org/3/faq/general.html#why-is-it-called-python) · [Python 3.0 release](https://www.python.org/downloads/release/python-300/) · [Sunsetting Python 2](https://www.python.org/doc/sunset-python-2/)
- [Why Python is the language of AI: Insights from Guido van Rossum (creator of Python)](https://www.youtube.com/watch?v=QXE5rEVlu20) [Video]. YouTube.
- van Rossum, G. (2018, July 12). [Transfer of power](https://mail.python.org/archives/list/python-committers@python.org/thread/GQONAGWBBFRHVRUPU7RNBM75MHKGUFJN/) [Mailing list post].
- [PEP 20: The Zen of Python](https://peps.python.org/pep-0020/)
- Hunter, J., & Droettboom, M. (2012). [matplotlib](https://aosabook.org/en/v2/matplotlib.html). In *The Architecture of Open Source Applications, Vol. 2*.
- Chen, D. L., Schonger, M., & Wickens, C. (2016). [oTree](https://doi.org/10.1016/j.jbef.2015.12.001). *Journal of Behavioral and Experimental Finance, 9*, 88–97.
- The full reference list is on the last slides of the presentation.

