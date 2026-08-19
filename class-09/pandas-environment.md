# pandas local-environment fallback

Use this page only if the main installation command reports `externally-managed-environment`. The fallback installs pandas inside the course folder instead of changing the Python installation managed by your computer.

In VS Code, open **Terminal → New Terminal**. Confirm that the terminal is in your course folder—the folder that contains `class-00-setup` through `class-09`—then run the commands for your operating system.

## macOS

```text
python3 -m venv .venv
.venv/bin/python -m pip install pandas==3.0.5
```

## Windows

```text
py -3.13 -m venv .venv
.venv\Scripts\python.exe -m pip install pandas==3.0.5
```

When installation finishes:

1. press `Command` + `Shift` + `P` on macOS or `Ctrl` + `Shift` + `P` on Windows;
2. enter `Python: Select Interpreter` and select that command;
3. choose the Python 3.13 interpreter whose path contains `.venv`;
4. run `class-09/check_pandas.py` again.

The final line should be:

```text
pandas is ready: 3.0.5
```

[Return to Class 9](README.md)
