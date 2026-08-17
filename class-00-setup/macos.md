# macOS Setup Guide

Follow these steps in order. You do not need to type any Terminal commands.

## 1. Install Python 3.13.15

1. Open the official [Python 3.13.15 release page](https://www.python.org/downloads/release/python-31315/).
2. Scroll to **Files** and click **macOS installer**.
3. Open the downloaded `.pkg` file.
4. Continue through the installer using its default options.
5. When installation finishes, open the `Python 3.13` folder in Applications.
6. Double-click `Install Certificates.command`.
7. Wait until its Terminal window reports `Successfully installed certifi` and `update complete`, then close that window.

The official installer works on both Apple Silicon and Intel Macs. Do not install a source-code archive.

## 2. Install VS Code

1. Open the official [VS Code download page](https://code.visualstudio.com/Download).
2. Under Mac, choose the **Universal** download.
3. Open the downloaded file.
4. Move **Visual Studio Code** into your Applications folder if macOS does not do so automatically.
5. Open VS Code from Applications.

If macOS asks whether you want to open an application downloaded from the internet, choose **Open**.

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
4. Open your Downloads folder and double-click `technion-096609-python-ai-main.zip` if it was not extracted automatically.

You should now have a normal folder named `technion-096609-python-ai-main`. Do not work inside the ZIP file.

## 5. Open the repository folder in VS Code

1. In VS Code, choose **File → Open Folder**.
2. Select the extracted folder named `technion-096609-python-ai-main`.
3. Click **Open**.
4. If VS Code asks whether you trust the authors of the files, choose **Yes, I trust the authors**.

The left Explorer panel should now show `README.md` and the `class-00-setup` folder.

## 6. Select Python 3.13

1. Press `Command` + `Shift` + `P`.
2. Type `Python: Select Interpreter` and select that command.
3. Choose an interpreter whose version begins with **Python 3.13**.

If several interpreters appear, do not choose Apple's system Python or one with a different version number. If no Python 3.13 interpreter appears, use the [troubleshooting guide](troubleshooting.md).

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
