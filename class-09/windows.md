# Class 9 setup — Windows

Start with the **extracted** `class-09` folder open in VS Code, not the ZIP preview. Python 3.13 and the Microsoft Python extension should already be installed from [Class 0](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-00-setup).

## 1. Check Python and the folder

In VS Code, open the dropdown beside the terminal's **+** button and choose **Command Prompt**. If no terminal is visible, choose **Terminal → New Terminal** first. Use Command Prompt for the commands below, not PowerShell. Run each command separately, pressing Enter after each:

```bat
py -3.13 --version
```

Expect **Python 3.13.x**. If `py` or that version is not found, return to the Class 0 Windows guide; do not substitute an arbitrary Python version.

```bat
dir
```

You should see `settings.py`, `requirements.txt`, and `choice_task`. If not, reopen the correct folder and create a new terminal there.

## 2. Create this project's environment

```bat
py -3.13 -m venv .venv
```

This creates a `.venv` folder. No output usually means success.

```bat
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Wait for the command to finish. It installs the version in `requirements.txt` from Python's package index. You only need this installation once per project.

```bat
.\.venv\Scripts\python.exe check_setup.py
```

Expect **CLASS 9 SETUP PASSED**, Python 3.13.x, and oTree 6.0.15.

## 3. Select the environment in VS Code

Press **Ctrl+Shift+P**, choose **Python: Select Interpreter**, and select the interpreter in this folder's `.venv`. If it is not listed, choose **Enter interpreter path → Find** and select `.venv\Scripts\python.exe`.

## 4. Start oTree

In the Command Prompt terminal, activate this project's environment:

```bat
.\.venv\Scripts\activate.bat
```

You should see `(.venv)` at the start of the prompt. Then start the server:

```bat
otree devserver
```

The terminal stays busy while the server runs. Open **http://localhost:8000** in your browser. Keep the terminal open and [continue at Step 3 of the lesson](README.md#3-complete-a-run-and-find-your-answers).

To stop: click this terminal and press **Ctrl+C**. To start again in the same terminal: run `otree devserver`. If you open a **new Command Prompt terminal**, activate `.venv` again first. You do not need to reinstall oTree or recreate `.venv`.

Activation makes this terminal use the project's Python and oTree, including the extra process that oTree starts. Command Prompt uses `activate.bat`, so no PowerShell execution-policy change is needed. Do not use the editor's Play button to run `__init__.py`; oTree starts the app for you.

[Troubleshooting](TROUBLESHOOTING.md) · [Official oTree installation guide](https://otree.readthedocs.io/en/latest/install.html) · [OpenAI's native Windows app guide](https://learn.chatgpt.com/docs/windows/windows-app)
