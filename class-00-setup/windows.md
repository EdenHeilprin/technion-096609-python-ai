# Windows Setup Guide

Follow these steps in order. You do not need to type any terminal commands.

## 1. Install Python 3.13.15

1. Open the official [Python 3.13.15 release page](https://www.python.org/downloads/release/python-31315/).
2. Scroll to **Files** and click **Windows installer (64-bit)**. It is marked **Recommended**.
3. Open the downloaded installer.
4. On its first screen, select **Add Python to PATH** if that option appears.
5. Choose **Install Now** and keep the default components.
6. When the installer reports that setup was successful, close it.

Do not install Python from the Microsoft Store for this course. Do not select the 32-bit, ARM64, embeddable, or source-code files.

## 2. Install VS Code

1. Open the official [VS Code download page](https://code.visualstudio.com/Download).
2. Under Windows, download the **User Installer — x64**.
3. Open the installer and accept its default options.
4. Open VS Code when installation finishes.

If you know that your Windows computer uses an ARM processor, email the instructor before choosing a different installer.

## 3. Install the Microsoft Python extension

1. In VS Code, click the **Extensions** icon in the left sidebar. It looks like four small blocks.
2. Search for `Python`.
3. Select the extension named **Python**, published by **Microsoft**.
4. Click **Install**.

There may be many similarly named extensions. For Class 0, install only the one published by Microsoft.

## 4. Download and extract the course repository

1. Return to the [main repository page](../README.md).
2. Near the top of the repository, click the green **Code** button.
3. Choose **Download ZIP**.
4. Open your Downloads folder.
5. Right-click the ZIP file whose name begins with `technion-096609-python-ai`, choose **Extract All**, and complete the extraction.

Do not work inside the ZIP file. You need the normal extracted folder.

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
