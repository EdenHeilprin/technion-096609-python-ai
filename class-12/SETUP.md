# Set up your research workspace

Use this guide with the `research-project` folder in your class download. Class 8's live demonstration does not require installation; complete this before doing its replay or starting Class 9.

## 1. Open the right folder

Extract the class ZIP first. In VS Code, choose **File → Open Folder** and select `research-project` inside the extracted class folder. You should see `setup_environment.py` in the Explorer.

Keep this folder on your computer, not inside the ZIP preview. Use a fresh folder for each class download or recovery checkpoint.

## 2. Prepare Python

Use the Python **3.13.x** installation from Class 0. In VS Code, open the Command Palette (**Cmd+Shift+P** on Mac; **Ctrl+Shift+P** on Windows), choose **Python: Select Interpreter**, and select Python 3.13.

Open `setup_environment.py` and use **Run Python File in Terminal**. It creates `.venv` in this project and installs the exact packages from `requirements.txt`. The first installation can take several minutes. Wait for:

```text
ENVIRONMENT READY
```

Now use **Python: Select Interpreter** again. Select this project's `.venv` interpreter. If it is not listed, choose **Enter interpreter path** and paste the full path printed after `Select this interpreter in VS Code:` at the end of setup. The path ends with:

- macOS: `research-project/.venv/bin/python`
- Windows: `research-project\.venv\Scripts\python.exe`

Run `check_environment.py`. You should see `ENVIRONMENT CHECK PASSED`, the Python path, and the three package versions.

The `.venv` keeps the project's packages separate from other Python projects. A new class folder needs its own setup; do not copy a `.venv` between folders or computers.

## 3. Open the project in Codex (if using AI)

If you are following the no-AI route, skip this section. Use the supplied complete project, or the lesson's named checkpoint, in VS Code. Prepare its environment as above and continue with the local run instructions below. You do not need a Codex account to run the supplied code.

Use the download for your operating system from the [official desktop-app quickstart](https://learn.chatgpt.com/docs/quickstart). Sign in with your ChatGPT account. Choose **Codex** from the app's product selector and open `research-project` as a local project. If Codex is already installed, use your existing app.

Start a chat in that project. Check the folder shown for the chat before sending a task. Selecting a project provides the working context; it is not a guarantee that every file elsewhere on your computer is unreadable.

Choose **Ask for approval** in the permissions control beneath the composer when available. This mode still permits routine edits and commands in the workspace. A prompt such as “inspect only” expresses your task scope; it is not a technical read-only sandbox. You do not need Full access for these classes. [Permissions reference](https://learn.chatgpt.com/docs/permission-modes)

Use a model available in your account, with its normal/default effort to begin. Check the account's usage display if a task stops. A paid subscription is not a course requirement; the instructor's demonstrations and the provided checkpoints cover work beyond your available usage.

## 4. Run the experiment

Once the lesson has a working experiment, open `run_experiment.py` and use **Run Python File in Terminal**. Leave that terminal running. Open **http://localhost:8000** in your browser. For a quick preview, select the demo whose name begins **Sure or gamble**. For the lessons' recorded tests, follow their **Sessions → Create new session** instructions instead.

`localhost` means this computer. It is not a link that classmates can open on their phones. For shared collection, use the instructor's hosted participant link.

To stop the server, click its terminal and press **Ctrl+C** on either operating system. Stop it before changing to another class project, then launch the new project's helper. Refresh the browser after changing the page's HTML or JavaScript.

## Terminal equivalents

These commands are alternatives to the VS Code run button. Open **Terminal → New Terminal** with `research-project` as the open folder. Do not type a leading `$`, `%`, or `>>>`.

| Action | macOS | Windows PowerShell |
| --- | --- | --- |
| First setup | `python3 setup_environment.py` | `py -3.13 setup_environment.py` |
| Check | `.venv/bin/python check_environment.py` | `.\.venv\Scripts\python.exe check_environment.py` |
| Start experiment | `.venv/bin/python run_experiment.py` | `.\.venv\Scripts\python.exe run_experiment.py` |
| Inspect data | `.venv/bin/python analysis/inspect_data.py` | `.\.venv\Scripts\python.exe analysis\inspect_data.py` |

The first command must use Python 3.13. If `python3` or `py` chooses another version or is unavailable, use VS Code's selected-interpreter route above. No shell activation or PowerShell execution-policy change is required.

For a specific problem, see [Troubleshooting](TROUBLESHOOTING.md).
