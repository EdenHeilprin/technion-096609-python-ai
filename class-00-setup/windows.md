# Windows Setup Guide

Follow these steps in order. You do not need to type any terminal commands.

Already use Python or VS Code? **Do not uninstall them.** If you already have Python 3.13.x, you can skip section 1. If you use another Python version, keep it and install Python 3.13.15 alongside it for this course. If VS Code is already installed, you can skip section 2.

## 1. Install Python 3.13.15

1. Open the official [Python 3.13.15 release page](https://www.python.org/downloads/release/python-31315/).
2. Scroll to **Files** and click **Windows installer (64-bit)**. It is marked **Recommended**.
3. Open the downloaded installer.
4. On its first screen, select **Add Python to PATH** if that option appears.
5. Choose **Install Now** and keep the default components.
6. When the installer reports that setup was successful, close it.

Use the installer marked **Recommended** and ignore the other files on the release page.

## 2. Install VS Code

1. Open the official [VS Code download page](https://code.visualstudio.com/Download).
2. Under Windows, download the **User Installer — x64**. This is the standard choice for almost all Windows computers.
3. Open the installer and accept its default options.
4. Open VS Code when installation finishes.

## 3. Install the Microsoft Python extension

1. In VS Code, click the **Extensions** icon in the left sidebar. It looks like four small blocks.
2. Search for `Python`.
3. Select the extension named **Python**, published by **Microsoft**.
4. Click **Install**.

There may be many similarly named extensions. For Class 0, install only the one published by Microsoft.

## 4. Download and extract the course repository

1. Click **[Download all course files as a ZIP](https://github.com/EdenHeilprin/technion-096609-python-ai/archive/refs/heads/main.zip)**. This link downloads the entire course repository—not only the instruction page you are reading.
2. Open your Downloads folder and find `technion-096609-python-ai-main.zip`.
3. Right-click that ZIP file and choose **Extract All**.
4. Accept the suggested location and click **Extract**.

Do not work inside the ZIP file. You need the normal extracted folder.

> **Important:** On GitHub, the **Code** tab beside **Preview** only changes how the current instruction page is displayed. The download arrow beside **Raw** downloads only that one page. Use the blue download link in step 1 to obtain all course files.

## 5. Open the repository folder in VS Code

1. In VS Code, choose **File → Open Folder**.
2. Select the extracted folder whose name begins with `technion-096609-python-ai`.
3. Click **Select Folder**.
4. If VS Code asks whether you trust the authors of the files, choose **Yes, I trust the authors**.

The left Explorer panel should now show `README.md` and the `class-00-setup` folder.

## 6. Select Python 3.13

1. Press `Ctrl` + `Shift` + `P`.
2. Type `Python: Select Interpreter` and select that command.
3. Choose an interpreter whose version begins with **Python 3.13**.

If several interpreters appear, do not choose one with a different version number. If no Python 3.13 interpreter appears, use the [troubleshooting guide](troubleshooting.md).

## 7. Run the setup check

1. In the Explorer panel, open `class-00-setup`.
2. Click `setup_check.py`.
3. Click the triangular **Run Python File** button in the upper-right corner of the editor.
4. Look at the Terminal panel that opens at the bottom of VS Code.

The final line should be:

```text
SETUP CHECK PASSED
```

You do not need to understand the Python code yet. Your task is only to run it successfully.

## 8. Finish on Moodle

Complete the **Class 0 readiness check** on Moodle before its deadline. If your output does not say `SETUP CHECK PASSED`, troubleshoot the setup before reporting completion.

[Back to the Class 0 start page](README.md)
