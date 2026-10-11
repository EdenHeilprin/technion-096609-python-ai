# Class 9 setup — macOS

Start with the extracted `class-09` folder open in VS Code. Python 3.13 and the Microsoft Python extension should already be installed from [Class 0](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-00-setup).

## 1. Check Python and the folder

Choose **Terminal → New Terminal** in VS Code. Run each command separately, pressing Enter after each:

```bash
python3.13 --version
```

Expect **Python 3.13.x**. If the command is not found, return to the Class 0 macOS guide; do not substitute an arbitrary Python version.

```bash
ls
```

You should see `settings.py`, `requirements.txt`, and `choice_task`. If not, reopen the correct folder and create a new terminal there.

## 2. Create this project's environment

```bash
python3.13 -m venv .venv
```

This creates a `.venv` folder. No output usually means success.

```bash
.venv/bin/python -m pip install -r requirements.txt
```

Wait for the command to finish. It installs the version in `requirements.txt` from Python's package index. You only need this installation once per project.

```bash
.venv/bin/python check_setup.py
```

Expect **CLASS 9 SETUP PASSED**, Python 3.13.x, and oTree 6.0.15.

## 3. Select the environment in VS Code

Press **Cmd+Shift+P**, choose **Python: Select Interpreter**, and select the interpreter in this folder's `.venv`. If it is not listed, choose **Enter interpreter path → Find** and select `.venv/bin/python`. In a Mac file picker, **Cmd+Shift+.** shows hidden folders such as `.venv`.

## 4. Start oTree

In the terminal, run:

```bash
.venv/bin/otree devserver
```

The terminal stays busy while the server runs. Open **http://localhost:8000** in your browser. Keep the terminal open and [continue at Step 3 of the lesson](README.md#3-complete-a-run-and-find-your-answers).

To stop: click this terminal and press **Control+C**. To start again: run `.venv/bin/otree devserver` from the `class-09` folder. You do not need to reinstall oTree or recreate `.venv`.

These commands call the project's executables directly, so no environment-activation command is needed. Do not use the editor's Play button to run `__init__.py`; oTree starts the app for you.

[Troubleshooting](TROUBLESHOOTING.md) · [Official oTree installation guide](https://otree.readthedocs.io/en/latest/install.html)
