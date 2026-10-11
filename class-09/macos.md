# Class 9 setup — macOS

Start with the extracted `class-09` folder open in VS Code. Python 3.13 and the Microsoft Python extension should already be installed from [Class 0](https://github.com/EdenHeilprin/technion-096609-python-ai/tree/main/class-00-setup).

## 1. Check Python and the folder

Choose **Terminal → New Terminal** in VS Code. A terminal panel opens below the editor. Run each command separately, pressing Enter after each:

```bash
python3.13 --version
```

Expect **Python 3.13.x**. If the command is not found, return to the Class 0 macOS guide; do not substitute an arbitrary Python version.

Check that Python can run a simple calculation:

```bash
python3.13 -c "print(2 + 3)"
```

It should print **5**. The `-c` option runs the Python code inside the quotes.

Now check which folder this terminal is using:

```bash
pwd
```

The displayed path should end in **class-09**. List its files:

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

## 3. Activate and check the environment

In the same terminal, run:

```bash
source .venv/bin/activate
```

Activation makes this terminal use the Python and packages inside `.venv`. Check them by running the supplied setup-check file:

```bash
python check_setup.py
```

It prints the Python version, the interpreter's location, and the oTree version. Its final line should be **CLASS 9 SETUP PASSED**. That means this project is using Python 3.13.x and oTree 6.0.15.

Press **Cmd+Shift+P**, choose **Python: Select Interpreter**, and select the interpreter in this folder's `.venv`. If it is not listed, choose **Enter interpreter path → Find** and select `.venv/bin/python`. In a Mac file picker, **Cmd+Shift+.** shows hidden folders such as `.venv`.

## 4. Start oTree

Return to that same VS Code terminal and run:

```bash
otree devserver
```

This starts oTree on your laptop. Wait for **Open your browser to http://localhost:8000/**. The terminal stays occupied because oTree is now serving the experiment's pages; that is expected. Leave it open and [continue at Step 3 of the lesson](README.md#3-complete-a-run-and-find-your-answers), where you will open the browser and create a session.

To stop: click this terminal and press **Control+C**. To start again in the same terminal: run `otree devserver`. If you open a **new terminal**, activate `.venv` again first. You do not need to reinstall oTree or recreate `.venv`.

**Note:** use `otree devserver`, not the editor's Play button on `__init__.py`, to run this experiment.

[Troubleshooting](TROUBLESHOOTING.md) · [Official oTree installation guide](https://otree.readthedocs.io/en/latest/install.html)
