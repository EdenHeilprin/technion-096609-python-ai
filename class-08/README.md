# Class 8 — From an Experiment to a Research Report

Today, we will take part in a short experiment and follow its results all the way to a research report—with Codex helping along the way.

This is a live demonstration. You only need your phone for the experiment; there is nothing to install or download.

## 1. Meet Codex

We begin with an introduction to Codex. Unlike copying code between a browser chat and an editor, we can give Codex a task inside a project and watch it work with the files.

During the demonstration, follow three things: **what we ask for, what Codex does, and the result we open together.**

## 2. Take part in the experiment

Scan the QR code shown in class. In each of six decisions, choose between:

- **Sure:** a guaranteed number of points.
- **Gamble:** a 50% chance of 10 points and a 50% chance of 0 points.

The guaranteed amount changes. The points are hypothetical; no money is paid.

After everyone finishes: **at which offers was the choice difficult?**

## 3. Look behind the screen

We open the experiment in Codex and connect the page you just saw to a few lines of Python.

This list controls the guaranteed offers:

```python
SURE_OFFERS = [2, 3, 4, 6, 7, 8]
```

oTree displays the pages and saves the answers. The experiment's own rules still use familiar ideas: a list of offers, a loop, a saved value, and a condition for showing the final page.

We then open the responses. Each row records one participant's choice at one offer.

## 4. Analyze our choices

Our question is: **do people choose the gamble less often when the guaranteed alternative is larger?**

We give Codex the response file and a short preregistration—a plan written before collecting the data. We ask it to explain its analysis plan, then carry it out.

The result is one graph: the percentage choosing the gamble at each guaranteed offer. We check one point ourselves by counting the choices behind it.

Does the pattern agree with our prediction? The offers appeared in increasing order, so we also consider what might change if their order were randomized.

## 5. Write from the evidence

We ask Codex to draft two short sections:

- **Method:** what participants actually did.
- **Results:** what their responses showed.

We check a sentence about the procedure against the experiment and a numerical claim against the results. We also see how a separate Codex reviewer can help check the draft, and how a conversation fork lets us explore an alternative design without losing the main discussion.

## Your next project

Next, you will set up Codex and oTree, then work individually or in pairs on an improvement to this experiment. You might add a condition, randomize the offers, or improve the participant pages.

**What would you change—and what would that change help you learn?**

---

[Teaching notes](Teaching%20Notes.md) · [Minimal project](minimal-project) · [Download demonstration files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-08/class-08-files.zip)
