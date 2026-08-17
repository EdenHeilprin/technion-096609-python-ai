# Windows setup

Use Windows 10 or 11 on a computer where you are allowed to install ordinary applications.

## 1. Install Python 3

1. Open [Python downloads for Windows](https://www.python.org/downloads/windows/).
2. Use the current stable Python install manager or the current 64-bit Python 3 installer.
3. Complete the installer with its ordinary recommended options.
4. Close and reopen VS Code and any terminals after installation.

You do not need WSL, Conda, Anaconda, or a virtual environment for Class 1.

## 2. Install VS Code

1. Open [Download Visual Studio Code](https://code.visualstudio.com/Download).
2. Download the Windows user installer matching your computer.
3. Complete the normal installation and open VS Code.

## 3. Install the Python extension

1. Open Extensions in VS Code.
2. Search for **Python**.
3. Select the extension published by **Microsoft**.
4. Install it. The supporting Python tools may be installed automatically.

## 4. Open the course folder

1. Download the Week 1 ZIP from the course website.
2. Extract the ZIP before opening it.
3. In VS Code, choose **File → Open Folder**.
4. Select the extracted week-01-materials folder.
5. If VS Code asks whether you trust the folder, confirm only when it came from the official course link.

## 5. Select Python

1. Open the Command Palette with Ctrl+Shift+P.
2. Search for **Python: Select Interpreter**.
3. Choose the current Python 3 installation.
4. The selected interpreter should appear in the VS Code status area.

## 6. Verify

Open setup/verify_setup.py inside the Week 1 folder and select **Run Python File**.

Expected final line:

    SETUP CHECK PASSED

Then run examples/reaction_time_summary.py.

Expected output:

    Participant: SYN001
    Condition: gain
    Mean reaction time (ms): 500.0

## If it does not work

- Restart VS Code once after installing Python.
- Confirm that the extracted folder—not the ZIP itself—is open.
- Reselect the interpreter.
- Use the VS Code Run button rather than guessing a terminal command.
- If no interpreter appears, post the exact screen/error in Moodle Technical Help and use the browser fallback for Class 1.

Official references:

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python releases for Windows](https://www.python.org/downloads/windows/)
