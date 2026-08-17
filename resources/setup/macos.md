# macOS setup

Use a current macOS account where you are allowed to install ordinary applications.

## 1. Install Python 3

Do not rely on an old system-provided Python.

1. Open [Python downloads for macOS](https://www.python.org/downloads/macos/).
2. Download the current stable macOS universal installer.
3. Open the downloaded package and complete the ordinary installation.
4. Close and reopen VS Code and Terminal after installation.

If you already use Homebrew confidently, the official VS Code tutorial also supports installing Python through Homebrew. Beginners do not need to install Homebrew solely for this course.

## 2. Install VS Code

1. Open [Download Visual Studio Code](https://code.visualstudio.com/Download).
2. Download the macOS Universal build.
3. Move Visual Studio Code to Applications and open it.

## 3. Install the Python extension

1. Open Extensions in VS Code.
2. Search for **Python**.
3. Select the extension published by **Microsoft**.
4. Install it.

## 4. Open the course folder

1. Download the Week 1 ZIP from the course website.
2. Double-click the ZIP to extract it.
3. In VS Code, choose **File → Open Folder**.
4. Select the extracted week-01-materials folder.
5. Confirm folder trust only when the folder came from the official course link.

## 5. Select Python

1. Open the Command Palette with Shift+Command+P.
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
- Confirm that the extracted folder is open.
- Reselect the interpreter.
- Prefer the VS Code Run button. The terminal command may be python3 rather than python on macOS.
- If no interpreter appears, post the exact screen/error in Moodle Technical Help and use the browser fallback for Class 1.

Official references:

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python releases for macOS](https://www.python.org/downloads/macos/)
