# Class 9 — Codex and oTree Setup

Run the seven-choice experiment from Class 8 on your own laptop, then make and check one small change with Codex.

You need the Python 3.13 and VS Code setup from [Class 0](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-00-setup). This lesson uses **oTree 6.0.15** in a separate project environment. Keep any other Python installations you already use.

## 1. Download and open the project

**[Download Class 9 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-09/class-09-files.zip)**

Extract the ZIP: double-click it on Mac, or right-click → **Extract All** on Windows. Move the extracted `class-09` folder into your course-work folder, next to your earlier classes. Open that folder in VS Code using **File → Open Folder**. Trust the folder if VS Code asks, after checking that it came from this repository.

You should see `settings.py`, `requirements.txt`, and the `choice_task` folder directly in the Explorer. This is an already working experiment; you do not need to ask AI to build it again.

## 2. Install oTree and start the experiment

Follow **only the guide for your computer**, then return to Step 3:

- **[macOS setup](macos.md)**
- **[Windows setup](windows.md)**

The guide creates `.venv`: a folder containing this project's Python environment and installed packages. The experiment's code stays outside it. Installing oTree here does not replace the packages used by your other projects.

## 3. Complete a run and find your answers

With the server running, open **[http://localhost:8000](http://localhost:8000)** in your laptop browser.

1. Open **Sessions → Create new session**. Choose **Seven choices — local practice** and **2 participants**, then create the session.
2. Open the session's **Links** tab. Open one participant link and complete consent and details, using a made-up ID such as `practice-a`.
3. Complete all **seven decisions**. Note your first and last prize and at least one choice. Stop at the thank-you page.
4. Open the second participant link with a different made-up ID, `practice-b`. Its prizes should appear in the opposite order. Complete this run too.
5. Return to the administrator page and open **Data**. Download the CSV labeled **All apps (wide format)**. Create an `exports` folder inside `class-09` and save the file there.
6. Open the CSV in Excel or RStudio. There is one row per participant, with separate columns for each round. Find `choice_task.1.player.condition`, then the `prize` and `choice` columns for rounds 1–7. Check them against the responses you entered.

Each participant sees the same prizes: **2, 8, 14, 20, 26, 32, 38**, either ascending or descending. The sure option stays at **10 points**. A stored choice is `sure` or `gamble`.

`localhost` means **this computer**. Sending that link to someone else does not give them access to your experiment.

## 4. Stop and restart it yourself

Click the terminal running the server and press **Control+C** on either operating system. Start it again using the same command from your setup guide, then reopen `http://localhost:8000`.

Your completed runs remain in the local database. Open an existing session to inspect them, or create a new session for another test. Do not run `resetdb` to restart the server: that command deletes saved responses.

## 5. Install Codex and open this folder

1. Use OpenAI's **[official desktop download and setup page](https://learn.chatgpt.com/docs/quickstart)**. Install the app for your operating system and sign in with your **ChatGPT account**. The current desktop app includes Codex; select **Codex** in its ChatGPT/Codex selector. If you already have the Codex desktop app, use it.
2. Add/open a **local project** and select this exact `class-09` folder. Keep the work on your computer, not in a cloud environment. On Windows, follow the app's native setup prompts; this lesson does not require WSL.
3. Keep the normal project-limited permissions. On Windows, select **Ask for approval** below the composer. Review requests for access outside the project or for network access; do not select unrestricted/full access just to complete this lesson.

On Mac, check **Apple menu → About This Mac**: the [current Mac desktop download](https://learn.chatgpt.com/docs/app) is labeled **Apple Silicon**. If you have an Intel Mac or the installer reports an unsupported operating system, complete the local oTree steps and manual edit, then contact the instructor for a compatible Codex route.

The [Free plan currently includes limited Codex access](https://learn.chatgpt.com/docs/pricing), subject to availability and usage limits. No paid subscription or API key is required for this activity. If access is unavailable or you reach a limit, use the manual alternative below and try the Codex step when access returns.

## 6. Make one change and verify it

First, open `choice_task/ThankYou.html` in VS Code. Notice the sentence `Your seven decisions have been recorded.`

In your Class 9 Codex project, send:

```text
Read README.md and choice_task/ThankYou.html. Change the final message to “Your seven decisions have been saved. Thank you for your time.” Keep everything else unchanged. Show me the edit and explain briefly what the HTML does. Do not access exports or the database.
```

Inspect the changed file yourself. Only that sentence should change. Save it, restart the server, and refresh a completed participant's thank-you page. Does the displayed message match the requested edit?

**Manual alternative:** replace that sentence directly in `ThankYou.html`, save, and perform the same check. Local editing, running oTree, and checking responses use no Codex allowance.

## A quick map of the code

| File | What it controls |
| --- | --- |
| `settings.py` | The session listed on the administrator page |
| `choice_task/__init__.py` | Prizes, order assignment, saved responses, and page sequence |
| `choice_task/*.html` | The words and forms shown to participants |
| `_static/choice_task/design.css` | Colors, spacing, and layout |
| `requirements.txt` | The required oTree version |

In `__init__.py`, find `PRIZES` and `prize_for_round`. Recognize the list, function, parameter, `if`, and `return`? Those are the same Python tools you already know. The classes and oTree-specific methods connect that logic to pages and saved responses.

## Ready to continue?

- [ ] The setup check prints **CLASS 9 SETUP PASSED**.
- [ ] I completed seven decisions in each order and found the saved answers in the CSV.
- [ ] I can stop and restart oTree without Codex.
- [ ] I opened this folder in Codex and checked a small edit, or noted the account/access issue to resolve.
- [ ] I can point to the Python logic, the HTML page, and the CSS styling.

For a problem, see [Troubleshooting](TROUBLESHOOTING.md). To rebuild the experiment from scratch later, use the [Class 8 prompts](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-08) in a **different, empty folder**.

[Next: Class 10 — Python Files and Your First GitHub Project](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-10)
