# Class 9 — Codex and oTree Setup

In Class 8, you saw how Codex could build an experiment. Today, you will run that experiment on your own laptop, find its saved responses, and change its thank-you page—first by hand, then with Codex.

You need the Python 3.13 and VS Code setup from [Class 0](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-00-setup). This lesson uses **oTree 6.0.15** in a separate project environment. Keep any other Python installations you already use.

## 1. Download and open the project

**[Download Class 9 files](https://github.com/EdenHeilprin/technion-096609-python-ai/raw/refs/heads/main/class-09/class-09-files.zip)**

Extract the ZIP: double-click it on Mac, or right-click → **Extract All** on Windows. Move the extracted `class-09` folder into your course-work folder, next to your earlier classes. **Open VS Code**, choose **File → Open Folder**, and select this `class-09` folder. Trust the folder if VS Code asks, after checking that it came from this repository.

You should see `settings.py`, `requirements.txt`, and the `choice_task` folder directly in the Explorer. This is an already working experiment; you do not need to ask AI to build it again.

## 2. Install oTree and start the experiment

We will use **VS Code's terminal**: the panel where you type commands to run programs. Follow the guide for your computer from beginning to end. It takes you through opening that terminal, checking Python and your folder, installing oTree, and starting it:

- **[macOS setup](macos.md)**
- **[Windows setup](windows.md)**

The guide creates `.venv`: a folder containing this project's Python environment and installed packages. It also runs the supplied `check_setup.py` file, which prints **CLASS 9 SETUP PASSED** when the Python and oTree versions are correct.

The final command is `otree devserver`. It starts the **local server**: the program that displays the experiment's pages in your browser and saves your responses on your laptop. Downloading the files alone does not start it.

Return here when the terminal displays **Open your browser to http://localhost:8000/**. Leave that terminal open.

## 3. Complete a run and find your answers

After completing the setup guide, open **[http://localhost:8000](http://localhost:8000)** in your browser. This is oTree's **administrator page**, where you create a session before opening a participant's experiment.

1. Click **Sessions** in the top menu, then **Create new session**.
2. In the **Session Config** dropdown, select **Sure or gamble**. This is the name of our experiment.
3. In **Number of participants**, type **2**, then click **Create**. This creates two participant places, each with its own link. You will complete both yourself to check the two presentation orders; you do not need another person.
4. Open the session's **Links** tab. Open the first **single-use participant link** in a new browser tab, keeping the administrator tab open. Complete consent and details with a made-up ID such as `practice-a`.
5. Complete all **seven decisions**. Note your first and last prize and at least one choice. Keep the thank-you tab open; you will use it again shortly.
6. Return to the administrator tab and open the second participant link with a different made-up ID, `practice-b`. Complete all seven decisions again. The prizes should now appear in the opposite order.

Each participant sees the same prizes: **2, 8, 14, 20, 26, 32, 38**, either ascending or descending. The sure option stays at **10 points**. A stored choice is `sure` or `gamble`.

**Note:** `localhost` means **this computer**. These pages are running on your laptop, not on a public website, so sending this address to someone else will not let them join your experiment.

## 4. Find your saved responses

1. Return to the administrator tab and click **Data** in the top menu.
2. Scroll to **Per-app data**. In the **choice_task** row, click **CSV**.
3. Create an `exports` folder inside `class-09` and save the downloaded file there. Open it in Excel or RStudio.
4. Find `participant.code`, `subsession.round_number`, `player.prize`, and `player.choice`. Each row represents **one participant's decision in one round**. Your two completed runs therefore contribute **14 rows**. If you created additional sessions, the file will include their rows too; `session.code` identifies each session.
5. Match the saved prizes and choices to the responses you entered. Find the ascending/descending assignment in `player.condition` on each participant's **round 1** row.

The **All apps (wide format)** export is another layout of the data: one row per participant, with separate columns for every round. Here, we use the per-app file because it is easier to inspect one decision at a time.

## 5. Change the thank-you message yourself

Return to **VS Code**, with `class-09` still open.

1. In the Explorer on the left, expand `choice_task`. Which file looks like it controls the final page? Open **ThankYou.html**.
2. Find `Your seven decisions have been recorded.` Change only that text to **Your seven decisions have been saved.** Keep the surrounding `<p>` and `</p>` tags; they mark a paragraph.
3. Save the file with **Cmd+S** on Mac or **Ctrl+S** on Windows.
4. Open VS Code's **Terminal** panel, where you previously typed `otree devserver`. If the panel is hidden, choose **View → Terminal**. Click inside that same terminal and press **Control+C** on either operating system. This stops oTree and returns you to a command prompt.
5. In that terminal, type the command below and press Enter:

   ```bash
   otree devserver
   ```

6. When the terminal displays the browser address again, return to your completed participant's thank-you tab and **refresh** it. Does it show your new sentence?

Your saved responses remain after a restart. Use `otree devserver` to start again, not `resetdb`, which deletes the database. If you open a **new terminal** instead of reusing the same one, activate `.venv` again using your setup guide before starting oTree.

A small wording change is often quicker to make directly. Next, you will ask Codex to format one part of that sentence.

## 6. Install Codex and open this folder

1. Use OpenAI's **[official desktop download and setup page](https://learn.chatgpt.com/docs/quickstart)**. Install the app for your operating system and sign in with your **ChatGPT account**. The current desktop app includes Codex; select **Codex** in its ChatGPT/Codex selector. If you already have the Codex desktop app, use it.
2. Add/open a **local project** and select this exact `class-09` folder. Keep the work on your computer, not in a cloud environment. On Windows, follow the app's native setup prompts; this lesson does not require WSL.
3. Keep the normal project-limited permissions. On Windows, select **Ask for approval** below the composer. Review requests for access outside the project or for network access; do not select unrestricted/full access just to complete this lesson.

On Mac, check **Apple menu → About This Mac**: the [current Mac desktop download](https://learn.chatgpt.com/docs/app) is labeled **Apple Silicon**. If you have an Intel Mac or the installer reports an unsupported operating system, complete the local oTree steps and manual edit, then contact the instructor for a compatible Codex route.

The [Free plan currently includes limited Codex access](https://learn.chatgpt.com/docs/pricing), subject to availability and usage limits. No paid subscription or API key is required for this activity. If access is unavailable or you reach a limit, use the manual alternative below and try the Codex step when access returns.

## 7. Ask Codex for a precise formatting change

In your Class 9 Codex project, send this prompt:

```text
In choice_task/ThankYou.html, make only the word “saved” in “Your seven decisions have been saved.” bold and dark green (#166534). Use a <strong> tag with an inline color style. Keep all wording, other styling, and experiment logic unchanged. Edit only this file; do not access exports or the database. Show me the changed line and briefly explain the HTML tag and the color style.
```

Open `ThankYou.html` in VS Code and inspect the edit. The sentence should still have exactly the same words; only **saved** should have added formatting.

Repeat the check from Step 5: save the file, stop oTree with **Control+C** in the VS Code terminal, run `otree devserver` again, and refresh the thank-you tab. Only **saved** should now appear **bold and dark green**.

<details>
<summary>Manual alternative and expected HTML</summary>

Replace the paragraph with:

```html
<p>Your seven decisions have been <strong style="color: #166534;">saved</strong>.</p>
```

`<strong>` marks the word as important and displays it in bold by default. The `color` style sets its text color. Save and check the page using the same steps above. This uses no Codex allowance.

</details>

## A quick map of the code

| File | What it controls |
| --- | --- |
| `settings.py` | The session listed on the administrator page |
| `choice_task/__init__.py` | Prizes, order assignment, saved responses, and page sequence |
| `choice_task/*.html` | The words and forms shown to participants |
| `_static/choice_task/design.css` | Colors, spacing, and layout |
| `requirements.txt` | The required oTree version |

In `__init__.py`, find `PRIZES` and `prize_for_round`. Recognize the list, function, parameter, `if`, and `return`? Those are the same Python tools you already know. The classes and oTree-specific methods connect that logic to pages and saved responses.

## Before you finish

- [ ] I can start and stop this experiment from VS Code's terminal.
- [ ] I completed both presentation orders and found my saved decisions in the per-app CSV.
- [ ] I changed the thank-you text by hand and saw the new wording in the browser.
- [ ] I checked the bold, green word after the Codex edit or manual alternative.

When finished, stop oTree with **Control+C** in the VS Code terminal. Your files and saved responses stay on your computer. For help with a step, see [Troubleshooting](TROUBLESHOOTING.md).

## Complementary videos

- **[Getting Started with Python in VS Code — Visual Studio Code](https://www.youtube.com/watch?v=D2cwvpJSBX4&t=149s), 02:29–04:50.** A visual explanation of virtual environments and selecting a Python interpreter. It shows VS Code's environment-creation menu; we created the same kind of `.venv` through terminal commands.
- **[HTML in 100 Seconds — Fireship](https://www.youtube.com/watch?v=ok-plXXHlWw).** Watch the full short video for an overview of how tags structure a web page. Connect it to the `<p>` and `<strong>` tags you edited today. Pause or slow playback when needed.
