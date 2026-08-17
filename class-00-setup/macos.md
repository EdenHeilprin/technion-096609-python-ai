# macOS Setup Guide

Follow these steps in order on a Mac running **macOS 12 or later**. You do not need to type any Terminal commands.

Already use Python or VS Code? **Do not uninstall them.** Skip the relevant installation section if you already have Python 3.13.x or VS Code. If you are unsure about your Python version, install Python 3.13.15 alongside your existing version.

## 1. Install Python 3.13.15

1. Click **[Download Python 3.13.15 for macOS](https://www.python.org/ftp/python/3.13.15/python-3.13.15-macos11.pkg)**.
2. Open **Downloads** in Finder and double-click `python-3.13.15-macos11.pkg`.
3. In the installer, choose **Continue**, accept the license, and use the default installation options.
4. Choose **Install**. Enter your Mac login password if macOS asks for it.
5. When the installer reports that the installation was successful, close it.
6. In Finder, open **Applications**, then open the `Python 3.13` folder.
7. Double-click `Install Certificates.command`.
8. Wait until the Terminal window reports `update complete`, then close it.

The official installer works on both Apple Silicon and Intel Macs. You are opening Terminal only by double-clicking the supplied file; you do not need to type a command.

## 2. Install VS Code

1. Click **[Download VS Code for macOS](https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal-dmg)**. The Universal version works on both Apple Silicon and Intel Macs.
2. Open **Downloads** in Finder and double-click `VSCode-darwin-universal.dmg`.
3. A small Finder window will open. Drag the **Visual Studio Code** icon onto the **Applications** folder icon shown in that window.
4. Wait for the copy to finish, then open **Applications** in Finder.
5. Double-click **Visual Studio Code**.

If macOS asks whether you want to open an application downloaded from the internet, choose **Open**.

VS Code may offer sign-in, Copilot, theme, or introductory options. None is required for Class 0; you may close or skip those prompts.

## 3. Install the Microsoft Python extension

1. In VS Code, click the **Extensions** icon in the left sidebar. It looks like four small blocks.
2. Search for `Python`.
3. Select the extension named **Python**, published by **Microsoft**.
4. Click **Install**.

Select **Python** published by Microsoft, not a similarly named extension. It may automatically add other Microsoft Python components; that is normal.

## 4. Download and extract the course repository

1. Click **[Download all course files as a ZIP](https://github.com/EdenHeilprin/technion-096609-python-ai/archive/refs/heads/main.zip)**. This link downloads the entire course repository—not only the instruction page you are reading.
2. In Downloads, double-click `technion-096609-python-ai-main.zip` if your Mac did not extract it automatically.
3. Open the extracted folder and confirm that it contains `README.md` and `class-00-setup`.

Use the download link in step 1. GitHub's small file-download icon downloads only the page currently displayed.

## 5. Open and trust the repository folder in VS Code

1. On the VS Code **Start** screen, click the blue **Open...** link beside the folder icon.
2. In the window that opens, click **Downloads** in the left sidebar and select the normal extracted folder that you verified in section 4—not the ZIP file.
3. Click **Open**.
4. If VS Code asks whether you trust the authors of the files, choose **Yes, I trust the authors**.
5. If a banner at the top says **Restricted Mode**, click **Manage** in that banner and then choose **Trust**.

If the **Start** screen is no longer visible, use the macOS menu bar at the top of the screen: choose **File → Open Folder...**, select the same folder, and click **Open**.

Trust enables extensions and allows code to run. Trust this folder because you downloaded it from the official course repository; do not automatically trust unfamiliar folders.

The Explorer panel should now list the repository contents, including `README.md` and the `class-00-setup` folder. It may also show files such as `.gitignore`.

## 6. Select Python 3.13

1. In the Explorer panel, expand `class-00-setup` and click `setup_check.py`. This activates the Python extension.
2. Wait a few seconds, then click the Python version—or **Select Interpreter**—shown in the bottom status bar.
3. If neither appears there, press `Command` + `Shift` + `P`, type `Python: Select Interpreter`, and select that command.
4. Choose an interpreter whose version begins with **Python 3.13**. If one is marked **Recommended**, choose it.

If several interpreters appear, do not choose Apple's system Python or one with a different version number. If no Python 3.13 interpreter appears, use the [troubleshooting guide](troubleshooting.md).

After selection, the bottom status bar in VS Code should show a Python version beginning with `3.13`.

## 7. Run the setup check

1. With `setup_check.py` open, click the triangular **Run Python File** button in the upper-right corner of the editor.
2. Look at the Terminal panel that opens at the bottom of VS Code.

The final line should be:

```text
SETUP CHECK PASSED
```

You do not need to understand the Python code yet. Your task is only to run it successfully.

## 8. Finish on Moodle

Complete the **Class 0 readiness check** on Moodle to report whether everything worked. If your output does not say `SETUP CHECK PASSED`, troubleshoot the setup before reporting completion.

[Back to the Class 0 start page](README.md)
