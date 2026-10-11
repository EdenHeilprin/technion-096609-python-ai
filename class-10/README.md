# Class 10 — Create and Contribute Your Own Lesson

Until now, you have used GitHub to get course materials. Today, you will use it to contribute your own: prepare a short lesson with a partner and send it to the course repository for review. In Classes 11–13, each pair will teach an approximately **30-minute lesson**.

You can build with **Codex, another AI tool, or without AI**. All routes lead to the same result: a lesson that classmates can follow and a **pull request** that Eden can review before adding it to the course.

Start with a small working draft today, then develop and rehearse the full lesson before your presentation. If possible, complete the [Git setup](git-setup.md) before class.

## By the end of class

- Create your own copy of the course repository and work on a separate branch.
- Prepare a first lesson draft with a useful example and a short activity.
- Inspect the changes you are submitting and open a pull request.
- Update that same submission after feedback.

## Rehearsal — where did your Class 9 edit go?

You changed the thank-you page on your laptop. Did that change the file on the course's GitHub page?

<details>
<summary>Check your answer</summary>

No. Saving a file changes your local copy. Git records selected changes as a **commit**; a **push** sends those commits to GitHub. Neither happens just because you press Save.

</details>

## 1. Choose one useful thing to teach

Work in pairs. **Get Eden's approval for your topic before building the lesson**, so two pairs do not prepare the same subject. Send your names, proposed topic, and one sentence describing what classmates will be able to do afterward.

Choose a focused task, not an entire library. “Use pandas to compare two groups in a CSV” is a manageable lesson; “Everything about pandas” is not.

### Topic pool

These topics extend the Python foundations from Classes 1–7. The first six are especially useful for working with research data and experiments.

| Topic | A practical 30-minute lesson | Starting source |
| --- | --- | --- |
| **pandas** | Load a small CSV, select relevant rows, and compare group averages | [Getting started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) |
| **Randomization with `random`** | Shuffle trial order, draw a sample without replacement, and reproduce it with a seed | [Random tools](https://docs.python.org/3.13/library/random.html) |
| **NumPy** | Convert response times into an array, change units, and select values with a condition | [Absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) |
| **Figures with Matplotlib** | Create a labeled plot and explain how the choice of axes affects its interpretation | [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) |
| **Files with `csv` and `pathlib`** | Read a table and save a summary beside the script, without a personal computer path | [CSV](https://docs.python.org/3.13/library/csv.html) · [Paths](https://docs.python.org/3.13/library/pathlib.html) |
| **Cleaning text** | Standardize messy response labels using `.strip()`, `.lower()`, and `.replace()`, preserving the original data | [String methods](https://docs.python.org/3.13/library/stdtypes.html#string-methods) |
| Useful built-in tools | Use `enumerate`, `zip`, and `sorted` to label trials, pair stimuli with answers, or rank scores | [Built-in functions](https://docs.python.org/3.13/library/functions.html) |
| Reusable modules | Put a useful function in a separate `.py` file and import it into two programs | [Modules](https://docs.python.org/3.13/tutorial/modules.html) |
| Python alongside R and JavaScript | Compare one small task across languages, then choose suitable tools for three scenarios | [Python](https://www.python.org/about/) · [R](https://www.r-project.org/about.html) · [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction) |
| GitHub beyond this lesson | Use commit history and issues to investigate a change and coordinate a repair | [History](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-and-understanding-files) · [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues) |

You may propose another subject, including a focused improvement to the experiment. Explain its value and what the audience will actually do. `random` is a **module** containing functions; pandas and NumPy are **third-party libraries** that need installation.

### What your lesson should contain

Use the [lesson template](lesson-template/README.md). Build around **one clear goal, one worked example, and one short activity with an answer or expected result**. Explain new code with concise English `#` comments. Include the files and installation instructions needed to repeat the example, plus links to your sources.

A conceptual topic still needs an activity: compare two approaches, predict an outcome, or justify a tool choice. Slides are optional; the lesson page can be your presentation.

## 2. Understand the route to the course repository

**Git** tracks file versions on your computer. **GitHub** hosts repositories and provides a place to review proposed changes.

```text
Course repository → your fork on GitHub → your local copy
                                             ↓
                                  edit on a new branch
                                             ↓
                                  commit → push to your fork
                                             ↓
                             pull request to the course → Eden reviews
                                             ↓
                               merge into the official course
```

A **fork** is your own GitHub copy of the course. A **clone** is its copy on your laptop, including Git history. A **branch** keeps your lesson changes separate from `main`. A **pull request (PR)** proposes bringing those changes into the original course.

You do not need write access to Eden's repository. You push to **your fork**, and Eden decides whether to merge your PR. **Forks and PRs are public too**: approval makes the lesson part of the official course, not visible for the first time. Use fictional example data; do not include student IDs, real participant data, passwords, or private files.

Choose one partner's account and laptop for the submission. Both partners develop and rehearse the lesson; make one PR per pair.

## 3. Prepare your tools and folder

Complete **[Git and GitHub setup](git-setup.md)**. It covers Mac and Windows, checks `git` and `gh`, and signs you into GitHub. `gh` is GitHub's command-line tool, not an AI subscription.

In Finder or File Explorer, create an **empty `class-10` folder** next to your previous classes. If that name already contains work, keep it and name the new empty folder `class-10-contribution` instead.

Open that empty folder in **VS Code → File → Open Folder**, then choose **Terminal → New Terminal**. On Windows, use **PowerShell**; on Mac, use **zsh**. Type:

```text
pwd
```

The path must end in your new folder's name. Otherwise, reopen the correct folder and create a new terminal. Keep this lesson open in your browser.

**This time we clone instead of downloading a ZIP:** the clone includes Git's connection to your fork and its history. It contains the whole repository; your new lesson will live inside `student-lessons`.

## 4. Make your fork and working branch

Choose **A or B**, not both. Both routes create the same working arrangement.

### A — With Codex

Open the same empty folder as a **local project** in Codex. Use a local chat, not a separate worktree. Paste:

```text
Set up this empty folder for contributing a lesson to https://github.com/EdenHeilprin/technion-096609-python-ai. Check Git and GitHub CLI and identify my signed-in GitHub account. Fork the course into my account and clone the fork directly here, with origin pointing to my fork and upstream to Eden's repository. Create branch add-my-lesson from the current upstream/main. If my fork already exists, reuse it. Preserve existing work; stop if this folder is not empty. Ask me for a commit display name and my GitHub noreply email, and set them only for this repository. Do not change course files or push anything. Show me the local folder, branch, and both remotes, with a short explanation of each.
```

Your GitHub noreply address is in **[Settings → Emails](https://github.com/settings/emails)** after enabling **Keep my email addresses private**. Copy the address GitHub supplies; do not invent one.

### B — Without Codex

Paste these commands **one at a time** in your VS Code terminal. If one reports an error, stop there and use the [setup help](git-setup.md#when-a-step-does-not-work).

```bash
gh repo fork EdenHeilprin/technion-096609-python-ai --clone -- .
git remote -v
```

The first command creates or reuses your fork and clones it into the current folder (`.`). The second must show **origin** pointing to **your username's** repository and **upstream** to **EdenHeilprin's**. Do not continue if that is not the case.

```bash
git fetch upstream
git switch -c add-my-lesson upstream/main
```

This starts your lesson branch from the latest course version, even if your fork was created earlier. Replace the two quoted placeholders below with your chosen display name and your GitHub noreply address from **[Settings → Emails](https://github.com/settings/emails)**. Enable **Keep my email addresses private** there to see the address.

```bash
git config user.name "YOUR DISPLAY NAME"
git config user.email "YOUR GITHUB NOREPLY EMAIL"
git branch --show-current
```

The last command should print **add-my-lesson**. These identity settings apply only to this repository.

**For either route:** open your fork on GitHub and check that your username appears as its owner, with **forked from EdenHeilprin/technion-096609-python-ai** underneath. In VS Code, the folder you opened now contains the course folders. This outer folder is the **repository root**; keep your terminal there for the remaining commands.

## 5. Build your lesson

Your lesson belongs in **`student-lessons/YOUR-USERNAME`**, using the submitting partner's actual GitHub username—for example, `student-lessons/maya-research`. Keep all lesson materials there, and leave existing classes unchanged.

### A — With Codex or another AI tool

In the same Codex project, replace the topic and presenter placeholders:

```text
Our approved topic is: [TOPIC AND PRACTICAL GOAL]. Presenters: [OUR CHOSEN NAMES OR GITHUB HANDLES].

Read class-10/README.md and its lesson template. Consult Classes 1–7 to match what our classmates already know. In student-lessons/<my GitHub username>, build a first draft of our approximately 30-minute lesson: a useful worked example, a short hands-on activity, a revealable answer, and a compact reference. Use current official sources and link them. Keep explanations direct and beginner-friendly, with clear English # comments explaining unfamiliar code.

Include every file needed to repeat the example, with the main runnable example in demo.py. If packages are needed, list tested versions in requirements.txt, install only those packages in this project's .venv using Python 3.13, and test the example. Document how to select that interpreter and run the example using VS Code's top-right play button, independently of Codex. For a conceptual topic, use a concrete comparison and discussion activity rather than unnecessary code.

Change lesson content only inside our student-lessons folder. Do not change existing classes, use real participant data, commit, or push. Open the lesson and example for review; report what you tested and anything we still need to check.
```

For an online chat, provide the [template](lesson-template/README.md) and relevant course materials as context. Ask it to return file contents, then create and save those files in VS Code. Use the manual Git steps to submit them. If Codex usage runs out, your files remain available and you can continue manually.

### B — Without AI

Replace `YOUR-USERNAME` in **every command below** with the submitting partner's GitHub username. From the same repository-root terminal:

```bash
mkdir student-lessons/YOUR-USERNAME
cp class-10/lesson-template/README.md student-lessons/YOUR-USERNAME/README.md
cp class-10/lesson-template/requirements.txt student-lessons/YOUR-USERNAME/requirements.txt
```

These commands work in Mac zsh and Windows PowerShell. Open the copied `README.md` in VS Code and fill in its sections. Markdown is plain text: `#` marks a heading, `-` starts a list, and triple backticks enclose code. Open its formatted preview with **Cmd+Shift+V** on Mac or **Ctrl+Shift+V** on Windows.

For a coding topic, use the Explorer's **New File** button to create `demo.py` inside your lesson folder. Start with one small example from the topic's official documentation, adapt it to a useful task, add comments, and credit the source. Include any small fictional input files beside it. Make the activity one deliberate change to that example, with a result classmates can check.

The template's `requirements.txt` starts with only a comment. For an external-library topic, add its package name on its own line: `pandas`, `numpy`, or `matplotlib`, for example. List only what the example imports. Built-in modules such as `random`, `csv`, and `pathlib` need no installation.

## 6. Run it yourself and rehearse

For a coding lesson, use an environment **inside the cloned repository**, separate from Class 9. If Codex already created `.venv`, reuse it and skip the creation command.

<details>
<summary>Mac commands — Python environment and lesson packages</summary>

Run from the repository root, replacing `YOUR-USERNAME`:

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r student-lessons/YOUR-USERNAME/requirements.txt
```

</details>

<details>
<summary>Windows PowerShell commands — Python environment and lesson packages</summary>

Run from the repository root, replacing `YOUR-USERNAME`:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r student-lessons/YOUR-USERNAME/requirements.txt
```

</details>

1. In VS Code, open the Command Palette (**Cmd+Shift+P** / **Ctrl+Shift+P**) and select **Python: Select Interpreter**. Choose this repository's `.venv`. If absent, use **Enter interpreter path → Find** and select `.venv/bin/python` on Mac or `.venv/Scripts/python.exe` on Windows.
2. Open your `demo.py` and click the **▶ play button at the top right**. Its Python action is called **Run Python File in Terminal**: VS Code sends the command for you. If another action is selected, use the adjacent dropdown to choose that action. Save first only after edits.
3. Check the output against the expected result, then complete your activity from its written instructions without asking AI what to do next.

Record the tested versions of external packages in `requirements.txt`, using `package-name==tested-version`. To find a version, run `.venv/bin/python -m pip show pandas` on Mac or `.\.venv\Scripts\python.exe -m pip show pandas` on Windows, substituting your package's name. Read the **Version** line.

For a conceptual lesson, check its links, examples, and activity instead; no Python environment is necessary. For either type, have your partner follow the page and identify one unclear instruction. Improve it before submitting.

## 7. Send a pull request to the course

### A — With Codex

After reviewing and testing the lesson, send:

```text
Review our student lesson against class-10/README.md. Check that instructions match the files, sources are linked, and any example and activity work. Show me the files and diff proposed for submission; exclude private data, credentials, environments, and unrelated changes. Confirm origin is my fork and the branch is add-my-lesson. Stop for my approval before committing or publishing.
```

After inspecting the changes, send:

```text
Commit only our reviewed student-lessons folder and push add-my-lesson to my fork. Open one pull request to EdenHeilprin/technion-096609-python-ai, base main. Title it “Student lesson: [TOPIC]”. Include both presenters, the learning goal, the activity, and checks we actually completed. Link the lesson in my branch so Eden can preview it. Give me the PR link. Do not merge, push to Eden's repository, or include unrelated files. If a PR already exists for this branch, update it instead.
```

### B — Manually

In VS Code's terminal at the repository root, replace `YOUR-USERNAME` and first check what will be submitted:

```bash
git branch --show-current
git status --short
git add -- student-lessons/YOUR-USERNAME
git diff --cached --stat
git --no-pager diff --cached
```

The branch must be **add-my-lesson**. All staged files must belong to **your lesson folder**. In the diff, `+` marks additions and `-` marks removals; these signs are not part of the file. Check the content, not only filenames. If unrelated files are staged, stop and ask for help.

Record and send the changes, then open the PR form:

```bash
git commit -m "Add our student lesson"
git push -u origin add-my-lesson
gh pr create --repo EdenHeilprin/technion-096609-python-ai --base main --head YOUR-USERNAME:add-my-lesson --web
```

In the browser, confirm **base repository: EdenHeilprin/technion-096609-python-ai**, **base: main**, and **head: your fork's add-my-lesson**. Title it **Student lesson: your topic**. Include both presenters' chosen names or handles, the learning goal, the activity, and the checks you performed. Add a link to the lesson's `README.md` in your fork's **add-my-lesson** branch so Eden can preview it.

Click **Create pull request**. This requests review; it does **not** merge the lesson.

## 8. Review, revise, and teach

Open the PR's **Files changed** tab. Can your partner explain what you are proposing? Confirm the PR appears under **[Pull requests in the course repository](https://github.com/EdenHeilprin/technion-096609-python-ai/pulls)**, not only in your fork. Share its link with Eden.

For requested changes, edit and test the files in the **same folder and branch**. With your username substituted, run:

```bash
git add -- student-lessons/YOUR-USERNAME
git --no-pager diff --cached
git commit -m "Revise lesson after feedback"
git push origin add-my-lesson
```

The same PR updates automatically. Reply with what changed. You can also ask Codex to make the requested edits, show the diff, and update that PR after your approval. Do not create a second submission or merge it yourself.

After Eden merges it, check **[Student lessons](../student-lessons/)** on the course's `main` branch: your lesson is now part of the official course. A PR closed without merging has not been added.

For your approximately **30-minute presentation**, a useful starting balance is 5 minutes for the problem, 10 for the example, 10 for the audience activity, and 5 for discussion. Both partners should explain part of the lesson and help classmates during the activity. Rehearse with the actual files and keep a working local copy.

## Before you finish

- [ ] Our approved topic does not duplicate another pair's.
- [ ] Our lesson has a clear goal, example, activity, and answer or expected result.
- [ ] We personally checked the files and instructions, including AI-generated content.
- [ ] Our PR targets the original course and contains only our lesson.
- [ ] We can distinguish saving, committing, pushing, and merging.

## Class 10 reference

| Term or command | Meaning here |
| --- | --- |
| Fork / clone | Your GitHub copy / its local copy with Git history |
| `origin` / `upstream` | Your fork / Eden's original repository |
| `git switch -c add-my-lesson upstream/main` | Start a branch from the fetched course version |
| `git status --short` | List changed and new files |
| `git add -- folder` | Select that folder's changes for the next commit |
| `git diff --cached` | Inspect those selected changes |
| `git commit` / `git push` | Record a local version / send commits to GitHub |
| Pull request / merge | Request review / incorporate accepted changes |

## Companion tutorial

**[Git Explained in 100 Seconds — Fireship](https://www.youtube.com/watch?v=hwP7WQkmECE).** Watch the full short video. Revisit **00:33** for staging, **00:39** for committing, and **01:12** for branching. The video uses the older branch name `master`; this course uses `main`. Here, you propose a merge through a PR and Eden performs it.

Further help: [GitHub's fork walkthrough](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo), [PRs from forks](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork), and [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
