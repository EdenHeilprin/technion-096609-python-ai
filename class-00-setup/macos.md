# macOS Setup Guide

Follow these steps in order. You do not need to type any Terminal commands.

Already use Python or VS Code? **Do not uninstall them.** If you already have Python 3.13.x, you can skip section 1. If you use another Python version, keep it and install Python 3.13.15 alongside it for this course. If VS Code is already installed, you can skip section 2.

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

1. Click **[Download all course files as a ZIP](https://github.com/EdenHeilprin/technion-096609-python-ai/archive/refs/heads/main.zip)**. This link downloads the entire course repository—not only the instruction page you are reading.
2. Open your Downloads folder and find `technion-096609-python-ai-main.zip`.
3. If your Mac did not extract it automatically, double-click the ZIP file.

You should now have a normal folder named `technion-096609-python-ai-main`. Do not work inside the ZIP file.

> **Important:** On GitHub, the **Code** tab beside **Preview** only changes how the current instruction page is displayed. The download arrow beside **Raw** downloads only that one page. Use the blue download link in step 1 to obtain all course files.

## 5. Open the repository folder in VS Code

1. On the VS Code **Start** screen, click the blue **Open...** link beside the folder icon.
2. In the window that opens, go to **Downloads** and select the extracted folder named `technion-096609-python-ai-main`.
3. Click **Open**.
4. If VS Code asks whether you trust the authors of the files, choose **Yes, I trust the authors**.

If the **Start** screen is no longer visible, use the macOS menu bar at the top of the screen: choose **File → Open Folder...**, select the same folder, and click **Open**.

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
