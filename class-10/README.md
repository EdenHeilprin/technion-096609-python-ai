# Class 10 — Create and Contribute Your Own Lesson

Until now, you have used GitHub to get course materials. Today, you will use it to contribute your own: prepare a lesson with a partner and submit it for the **repository owner** to review. In Classes 11–13, each pair will teach an approximately **30-minute lesson**.

The aim is **familiarity through a live demonstration and a small activity**. Help classmates recognize a useful tool, see what its code does, and follow it when working with AI. Choose a manageable introduction, not a complete course on your topic.

You can use **Codex, an online AI chatbot, or no AI**. Start with a small working draft today; develop and rehearse it before your presentation. Git and GitHub sign-in should already be ready from [Class 9](../class-09/git-setup.md).

## By the end of class

- Make your own GitHub copy of the course and edit it on your laptop.
- Prepare a first lesson draft with a live example and a short activity.
- Submit a **pull request**: a proposal to add your lesson to the course.
- Update that same proposal after feedback.

## Rehearsal — where did your Class 9 edit go?

In Class 9, you changed the thank-you page on your laptop. If a classmate now downloads the experiment from GitHub, will they receive your edited sentence?

<details>
<summary>Check your answer</summary>

No. You changed the copy on **your computer**, not the copy on **GitHub**. Saving a file does not upload it. Today, you will learn how to send a change and ask the repository owner to include it in the course.

</details>

## 1. Choose one useful thing to introduce

Work in pairs. **Get the instructor's approval before building your lesson**, including when choosing from this list. Send both names, your topic, and one sentence about what you will demonstrate. Each pair needs a different topic.

### Topic pool

| Topic | What you could show live | Starting source |
| --- | --- | --- |
| **pandas** | Open a small CSV, select some rows, and compare two group averages | [Getting started](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html) |
| **Randomization with `random`** | Shuffle trial order and show how a seed makes an example repeatable | [Random tools](https://docs.python.org/3.13/library/random.html) |
| **Figures with Matplotlib** | Turn a few values into a labeled figure, then change its labels or axes | [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) |
| **Files with `csv` and `pathlib`** | Read a small table and save a summary beside the script | [CSV](https://docs.python.org/3.13/library/csv.html) · [Paths](https://docs.python.org/3.13/library/pathlib.html) |
| **Cleaning text** | Turn inconsistent response labels into consistent ones using `.strip()`, `.lower()`, and `.replace()` | [String methods](https://docs.python.org/3.13/library/stdtypes.html#string-methods) |
| **Useful built-in tools** | Use `enumerate`, `zip`, or `sorted` to label trials, pair stimuli with answers, or rank scores | [Built-in functions](https://docs.python.org/3.13/library/functions.html) |
| **Reusable modules** | Put a function in one `.py` file and use it from another | [Modules](https://docs.python.org/3.13/tutorial/modules.html) |
| **Python's history** | Tell Python's origin story, show three or four milestones, and connect its development to uses in research | [Python's origins](https://docs.python.org/3.13/faq/general.html#why-was-python-created-in-the-first-place) |
| **A GitHub tutorial** | Give a guided live tour: find a file, inspect its history, and follow a proposed change through a pull request | [Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) |
| **Improve the experiment scientifically** | Identify one methodological weakness, change the experiment to address it, and demonstrate the original and revised versions | [Class 9 experiment](../class-09/) |

For the **experiment improvement**, identify a methodological weakness and explain why it matters. For example, a randomized-order condition could help distinguish payoff preferences from order effects. Implement one focused change and **demonstrate the original and revised versions locally on your laptop**, sharing your screen. Explain what you changed, its scientific merit, and what the resulting data would help you learn. Classmates discuss the design rather than participate in the experiment; no online deployment is needed.

For **Python's history**, organize the lesson around three questions: **Who created Python, and why? How did it develop and spread? How did it become useful in research?** Use a short timeline of three or four milestones and show two concrete applications, such as analyzing a dataset and building a web experiment. This is an option for a less technical presentation.

You may also propose another subject. `random` is a built-in **module**; libraries such as pandas need installation.

### What to prepare

Use the [lesson template](lesson-template/README.md): **one clear goal, a live example, and a small activity with an answer or expected result**. For the experiment-improvement topic, the activity is a discussion of the design you demonstrate. Keep the code short and explain it with concise English `#` comments. Include the files needed to repeat it and links to your sources. Slides are optional; your lesson page can be your presentation.

## 2. Understand where your work will go

**Git** records versions on your computer. **GitHub** stores repositories online and lets people propose and review changes. A **repository** is a project's files together with their version history.

```text
Course repository → your fork on GitHub → your local copy
                                             ↓
                                  edit on a new branch
                                             ↓
                                  commit → push to your fork
                                             ↓
                             pull request → owner reviews → merge
```

- **Fork:** your own GitHub copy of the course.
- **Clone:** download that repository to your laptop, including its history.
- **Branch:** a separate line of changes, so your lesson can be reviewed together.
- **Commit:** record a version of selected file changes locally.
- **Push:** send those commits to GitHub.
- **Merge:** include accepted changes in the course's main version, called `main`.

You upload to **your fork**, not directly to the course. The owner decides whether to merge your pull request. **Your fork and pull request are public**, even while awaiting review. Until the owner accepts them, your changes are **not part of the official course**. Use fictional data; do not upload participant IDs, passwords, or private files.

Choose one partner's account and laptop for the submission. Both partners develop and present the lesson; submit **one PR per pair**.

## 3. Open a fresh folder and terminal

1. In **Finder (Mac)** or **File Explorer (Windows)**, create an empty **`class-10`** folder next to your previous classes. If you already have work in a folder with that name, keep it and name the new folder **`class-10-contribution`** instead.
2. In **VS Code**, choose **File → Open Folder** and select this new empty folder.
3. Choose **Terminal → New Terminal**. A panel opens below the editor. Click the small arrow beside **+** at the top right of that panel, then select **zsh (Mac)** or **Command Prompt (Windows)**, as in Class 9. These are terminal types inside VS Code; do not open a separate application.
4. In that panel, type **`pwd` on Mac** or **`cd` on Windows**, then press Enter. The displayed path should end in your new folder's name. If it does not, reopen the correct folder and create a new terminal.

Keep this lesson open in your browser. Paste terminal commands **one at a time**, pressing Enter after each. Stop if a command reports an error; [setup help](../class-09/git-setup.md#when-a-step-does-not-work) is available.

This time we **clone**, rather than download a ZIP, to keep Git's connection to your online copy. The folder will contain the whole course; your own lesson will go inside `student-lessons`.

## 4. Make your fork and branch

Choose **one** route below. After it, both routes continue at **Check your copy**.

<details>
<summary><strong>A — With Codex</strong></summary>

Open the same empty folder as a **local project** in Codex. Start a local chat and paste:

```text
Use local Git and GitHub CLI to prepare this empty folder for contributing to https://github.com/EdenHeilprin/technion-096609-python-ai. Confirm my signed-in GitHub username. Fork the course into that account and clone it directly here: origin must be my fork, and upstream the original course. Reuse my fork if it already exists. Create branch add-my-lesson from the latest upstream/main.

Ask for my name and the GitHub noreply address I copied during setup; configure them only for this repository. Preserve existing work and stop if the folder is not empty. Do not edit course files or push anything. Show me the folder, branch, and both remotes.
```

</details>

<details>
<summary><strong>B — Without Codex</strong></summary>

In the VS Code terminal from Step 3, enter:

```bash
gh repo fork EdenHeilprin/technion-096609-python-ai --clone -- .
git remote -v
```

The first command makes or reuses your fork and downloads it into this folder (`.`). The second lists its online connections: **origin** must contain **your username** and **upstream** must contain **EdenHeilprin**. Stop if they do not.

Now make your lesson branch:

```bash
git fetch upstream
git switch -c add-my-lesson upstream/main
```

Tell Git who is recording these changes. Replace the quoted placeholders with **your name** and the **noreply address from Class 9**. Keep the quotation marks:

```bash
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB NOREPLY ADDRESS"
git branch --show-current
```

The last command should print **add-my-lesson**. The name/email settings apply only to this copy of the repository.

</details>

### Check your copy — everyone

Your **noreply address** labels commits without exposing your personal email. If you did not copy it in Class 9, follow [these three steps](../class-09/git-setup.md#5-find-your-private-commit-email).

1. In your browser's address bar, enter **`https://github.com/YOUR-USERNAME/technion-096609-python-ai`**, replacing `YOUR-USERNAME` with your actual GitHub username.
2. Check that **your username** appears before the repository name and that the page says **forked from EdenHeilprin/technion-096609-python-ai**. This is your online copy.
3. Return to VS Code. Its Explorer now shows folders such as `class-01`, `class-09`, and `student-lessons` inside the folder you opened. This outer folder is called the **repository root**. Keep the terminal there for the Git commands below.

## 5. Write your lesson

Use **`student-lessons/YOUR-USERNAME`** for all your lesson files. For example, username `maya-research` would use `student-lessons/maya-research`. Replace `YOUR-USERNAME` everywhere it appears in a command.

Choose **A or B**, then continue to Step 6.

<details>
<summary><strong>A — With Codex or an online AI chatbot</strong></summary>

In the same Codex project, replace the two bracketed placeholders and send:

```text
Our approved topic is [TOPIC AND WHAT WE WILL DEMONSTRATE]. Our names are [BOTH NAMES].

Read class-10/README.md and its lesson template, and consult Classes 1–7 for the audience's background. Create our first lesson draft in student-lessons/<my GitHub username>. Aim for about 30 minutes: introduce one useful idea, demonstrate it live, and give classmates a small activity with an answer and a compact reference. Aim for familiarity and recognition, not mastery. Use and link reliable original sources.

Include all necessary files. For a Python example, use demo.py, fictional input data located relative to the script, concise English # comments, and requirements.txt listing only external packages. For an oTree improvement, copy the clean Class 9 experiment into our lesson's experiment folder and preserve the original. Plan a local screen-shared demonstration by the presenters, followed by discussion of the methodological weakness, the change, and its scientific merit. Do not require online deployment or classmates' participation in the experiment. For Python history, follow the topic outline in class-10/README.md and illustrate research uses with examples from this course. For a GitHub tutorial, use a guided live tour and audience activity.

Save the draft; we will prepare and test it in the next step. Change only our lesson folder, do not use real participant data, and do not commit or publish. Show me the lesson and files to review.
```

For an **online chat with an AI chatbot**, such as ChatGPT in your browser, upload the [lesson template](lesson-template/README.md) and relevant course pages. Explain that the chatbot should return file contents for you to save, rather than edit your computer. Create those files in VS Code inside your lesson folder. Continue with the manual setup and submission steps below.

</details>

<details>
<summary><strong>B — Without AI</strong></summary>

Use the **VS Code terminal already opened in Step 3**, not a Python `>>>` prompt. Choose your computer's commands and replace `YOUR-USERNAME`:

**Mac — zsh terminal:**

```bash
mkdir student-lessons/YOUR-USERNAME
cp class-10/lesson-template/README.md student-lessons/YOUR-USERNAME/README.md
cp class-10/lesson-template/requirements.txt student-lessons/YOUR-USERNAME/requirements.txt
```

**Windows — Command Prompt terminal:**

```bat
mkdir student-lessons\YOUR-USERNAME
copy class-10\lesson-template\README.md student-lessons\YOUR-USERNAME\README.md
copy class-10\lesson-template\requirements.txt student-lessons\YOUR-USERNAME\requirements.txt
```

In VS Code's Explorer, open **student-lessons → your username → README.md** and replace the template's bracketed instructions with your lesson. Markdown is plain text: `#` makes a heading, `-` starts a list, and triple backticks enclose code. See the formatted page with **Cmd+Shift+V (Mac)** or **Ctrl+Shift+V (Windows)**. Save after edits.

For a Python topic, right-click your lesson folder in the Explorer, choose **New File**, and name it **demo.py**. Adapt a small example from the official documentation, explain it with comments, and credit the source. Put any fictional input files beside it. Make the activity one useful change to the example.

For an external library, put its package name on its own line in `requirements.txt`, such as `pandas` or `matplotlib`. Built-in modules such as `random`, `csv`, and `pathlib` do not need installing.

For an experiment improvement, create **experiment** inside your lesson folder. Copy these clean items from the repository's **class-09** folder into it: `settings.py`, `requirements.txt`, `check_setup.py`, `choice_task`, and `_static`. Edit this copy, not Class 9 or the experiment in your personal student-work folder. Explain the original weakness, the change, and what new comparison or interpretation it enables.

</details>

## 6. Test the lesson on your own laptop

This step applies **whether or not AI wrote your files**. First prepare the files to run; then check the example yourself.

### Prepare to run — choose one route

<details>
<summary><strong>A — Ask Codex to prepare and test it</strong></summary>

```text
Prepare our student lesson to run independently of Codex. For a Python script, use Python 3.13 and a .venv in the outer course-copy folder; install only our lesson's requirements and test demo.py. For an oTree project, use Python 3.13 and oTree 6.0.15 in a .venv inside our lesson's experiment folder, test it locally, and provide the exact VS Code terminal commands and starting folder for otree devserver. For a noncoding lesson, check its links and live example instead.

Update our lesson's Get ready section with short numbered instructions: which folder and file to open, what to run, and what should appear. Explain new steps in ordinary language. Record tested external package versions in requirements.txt. Show the results and tell me how to repeat the check myself. Do not commit or publish.
```

</details>

<details>
<summary><strong>B — Prepare it yourself</strong></summary>

**If your lesson uses `demo.py`:** we will give it its own Python packages, kept in a folder called **`.venv`**. This leaves Class 9's oTree packages alone.

In the VS Code terminal, check your location again: **`pwd` (Mac)** or **`cd` (Windows)** must show the outer folder you opened in Step 3, not your lesson's subfolder. Run the commands for your computer, replacing `YOUR-USERNAME`:

**Mac:**

```bash
python3.13 -m venv .venv
.venv/bin/python -m pip install -r student-lessons/YOUR-USERNAME/requirements.txt
```

**Windows — Command Prompt:**

```bat
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install -r student-lessons\YOUR-USERNAME\requirements.txt
```

The first command creates the package folder; the second installs what your example needs. Wait until the terminal is ready for another command. If repeating this step, you can skip the first command when `.venv` already exists here.

**If your lesson changes the oTree experiment:** choose **File → New Window** in VS Code, then **File → Open Folder** and open your lesson's **experiment** folder. Follow the [Class 9 Mac setup](../class-09/macos.md) or [Windows setup](../class-09/windows.md), using this **experiment** folder wherever the guide says `class-09`. It contains the same setup files. Use `otree devserver` to start it and complete a participant run. Stop another oTree server first if port 8000 is already in use. Return to the original VS Code window for the Git commands in Step 7.

**If your lesson is Python history or a GitHub tour:** there are no Python packages to install unless your own example needs them. Check the pages and live demonstration you plan to show.

</details>

### Run and check — everyone

For a **`demo.py` example**, do this yourself even if Codex already tested it:

1. In the original VS Code window, open **student-lessons → your username → demo.py**.
2. Press **Cmd+Shift+P (Mac)** or **Ctrl+Shift+P (Windows)**. Type **Python: Select Interpreter** and select it. Choose the Python entry containing **`.venv` from your Class 10 folder**. If absent, choose **Enter interpreter path → Find** and select `.venv/bin/python` on Mac or `.venv/Scripts/python.exe` on Windows. On Mac, **Cmd+Shift+.** reveals hidden folders in the file picker.
3. Click the **triangle ▶ in the upper-right corner of the code editor**. If needed, use its adjacent arrow and choose **Run Python File in Terminal**. VS Code runs the file and opens its output below. You do not need to type a run command.
4. Does the result match your lesson? Make the small change from your activity, save, run again, and check the new result. Restore the starting example afterward.

For an **oTree example**, repeat the local participant test using your lesson's written instructions. Check both the behavior you changed and the saved responses. Use `otree devserver`, not the triangle on a Python file.

For **every topic**, have your partner follow the page. Improve any instruction they cannot follow. Both of you should be able to explain the live example in simple terms.

<details>
<summary>Record the library version you tested, if you installed one manually</summary>

From the outer Class 10 folder, run `.venv/bin/python -m pip show pandas` on Mac or `.venv\Scripts\python.exe -m pip show pandas` on Windows, replacing `pandas` with your package. Find **Version** in the output and change its line in `requirements.txt` to `package-name==that-version`. Built-in modules need no line. The oTree starter already specifies its version.

</details>

## 7. Submit your lesson for review

Choose **A or B**, then continue to Step 8.

<details>
<summary><strong>A — With Codex</strong></summary>

First ask it to show you what will be submitted:

```text
Review our student lesson against class-10/README.md. Check that the instructions match the files and our example and activity work. Use local Git and GitHub CLI. Confirm the account, origin is my fork, and the branch is add-my-lesson. Show only our lesson's proposed changes, excluding private data, credentials, environments, and unrelated files. Stop for my approval before committing or publishing.
```

After you inspect the changes, replace `[TOPIC]` and send:

```text
Commit only our reviewed lesson folder inside student-lessons and push add-my-lesson to my fork using GitHub CLI's signed-in account. Open one pull request to EdenHeilprin/technion-096609-python-ai, base main, titled “Student lesson: [TOPIC]”. Include our names, the goal, the live example, the activity, and checks we completed. Add a link to the lesson in my branch for the reviewer. Give me the PR link. Do not merge or push directly to the course. If a PR already exists for this branch, update it instead.
```

</details>

<details>
<summary><strong>B — Without Codex</strong></summary>

Return to the **original VS Code window**, with the outer Class 10 folder open. Open its terminal using Step 3. Replace `YOUR-USERNAME` below.

First check your branch and select your lesson's files:

```bash
git branch --show-current
git status --short
git add -- student-lessons/YOUR-USERNAME
git diff --cached --stat
git --no-pager diff --cached
```

The branch must be **add-my-lesson**, and the selected files must all be inside **your lesson folder**. The last command shows their changes: `+` means added text and `-` means removed text. These signs are not part of your file. If other files are included, stop and ask for help.

Record the version, upload it to your fork, and open the review-request form:

```bash
git commit -m "Add our student lesson"
git push -u origin add-my-lesson
gh pr create --repo EdenHeilprin/technion-096609-python-ai --base main --head YOUR-USERNAME:add-my-lesson --web
```

In the browser, the destination (**base**) should be **EdenHeilprin/technion-096609-python-ai → main**. The source (**head**) should be **your fork → add-my-lesson**.

Title it **Student lesson: your topic**. In the description, include both names, your goal, live example, activity, and what you tested. Also paste a link to your lesson: open your fork using Step 4, choose **add-my-lesson** from the branch dropdown above its files, open **student-lessons → your username**, and copy the browser address.

Click **Create pull request**. This asks for review; it does not add your lesson to the official course yet.

</details>

## 8. Check your submission and respond to feedback

### Check that the owner received it — everyone

1. Open **[Pull requests in the course repository](https://github.com/EdenHeilprin/technion-096609-python-ai/pulls)** and click your lesson's title.
2. Open **Files changed**. Check that it contains your lesson and no unrelated files. Your partner should recognize and understand the changes.
3. Copy this PR's browser address and send it to the instructor.

### When you receive feedback

Open the same PR and read its comments under **Conversation** or **Files changed**. Edit the files in your **existing lesson folder**, then test the change. You keep the same branch and PR.

**With Codex:** give it the feedback and ask it to update this lesson, test it, and show the changes. After reviewing, ask it to commit and push to the **same fork and add-my-lesson branch**, without merging or creating another PR.

**Without Codex:** in the original VS Code terminal, replace `YOUR-USERNAME` and run:

```bash
git branch --show-current
git add -- student-lessons/YOUR-USERNAME
git --no-pager diff --cached
```

Check that the branch is **add-my-lesson** and the changes are only yours. Then run:

```bash
git commit -m "Revise lesson after feedback"
git push origin add-my-lesson
```

**For either route:** refresh the PR page. Your new changes appear in that same request. Reply to the reviewer with a short note about what you changed.

### After acceptance

When the owner merges the PR, your folder appears in **[Student lessons](../student-lessons/)** in the official course. A PR marked **Closed** without **Merged** was not added.

For your **30-minute presentation**, introduce the problem, demonstrate a small example live, and lead the activity or discussion described in your lesson. For an experiment improvement, run it locally on your laptop and explain the design change and its scientific merit. Both partners should present. Rehearse with the actual files, aiming for recognition and understanding of the basic idea rather than covering every feature.

## Before you finish

- [ ] Our topic was approved and is different from other pairs' topics.
- [ ] Our lesson introduces a useful idea with a live example and a small activity.
- [ ] We checked the example ourselves and can explain what it does.
- [ ] Our PR appears in the course repository and contains only our lesson.
- [ ] We know how to update that same PR after feedback.

## Class 10 reference

| Term or command | Meaning here |
| --- | --- |
| Fork / clone | Your GitHub copy / its copy on your laptop |
| `origin` / `upstream` | Your fork / the original course repository |
| `git branch --show-current` | Show which branch you are working on |
| `git status --short` | List changed and new files |
| `git add -- folder` | Select that folder's changes for the next commit |
| `git diff --cached` | Inspect the selected changes |
| `git commit` / `git push` | Record a version locally / send it to GitHub |
| Pull request / merge | Ask for review / incorporate accepted changes |

## Companion tutorial

**[Git Explained in 100 Seconds — Fireship](https://www.youtube.com/watch?v=hwP7WQkmECE).** Watch the full short video. Revisit **00:33** for staging, **00:39** for committing, and **01:12** for branching. The video uses the older branch name `master`; this course uses `main`. Here, you propose a merge through a PR and the repository owner performs it.

Further help: [GitHub's fork walkthrough](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo), [PRs from forks](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork), and [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow).
