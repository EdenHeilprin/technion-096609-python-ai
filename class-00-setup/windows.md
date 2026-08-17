# Windows Setup Guide

Follow these steps in order on **Windows 10 or Windows 11**. You do not need to type any terminal commands.

Already use Python or VS Code? **Do not uninstall them.** Skip the relevant installation section if you already have Python 3.13.x or VS Code. If you are unsure about your Python version, install Python 3.13.15 alongside your existing version.

## 1. Install Python 3.13.15

1. Click **[Download Python 3.13.15 for Windows](https://www.python.org/ftp/python/3.13.15/python-3.13.15-amd64.exe)**.
2. Open **Downloads** in File Explorer and double-click `python-3.13.15-amd64.exe`.
3. On the first installer screen, select the checkbox whose label includes **Add Python to PATH** if that option appears.
4. If Windows asks whether to allow this application to make changes, choose **Yes**.
5. Choose **Install Now** and keep the default components.
6. When the installer reports that setup was successful, close it.

If Windows says that this installer cannot run on your computer, stop and use the [help-request template](email-help-template.md). Do not guess among other installer versions.

## 2. Install VS Code

1. Click **[Download VS Code for Windows](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user)**.
2. Open **Downloads** in File Explorer and double-click the file whose name begins with `VSCodeUserSetup-x64-` and ends with `.exe`.
3. Accept the license and keep the default installation options as you move through the installer.
4. When installation finishes, select **Launch Visual Studio Code** if that option appears, then close the installer.

VS Code may offer sign-in, Copilot, theme, or introductory options. None is required for Class 0; you may close or skip those prompts.

## 3. Install the Microsoft Python extension

1. In VS Code, click the **Extensions** icon in the left sidebar. It looks like four small blocks.
2. Search for `Python`.
3. Select the extension named **Python**, published by **Microsoft**.
4. Click **Install**.

Select **Python** published by Microsoft, not a similarly named extension. It may automatically add other Microsoft Python components; that is normal.

## 4. Download and extract the course repository

1. Click **[Download all course files as a ZIP](https://github.com/EdenHeilprin/technion-096609-python-ai/archive/refs/heads/main.zip)**. This link downloads the entire course repository—not only the instruction page you are reading.
2. Open **Downloads** in File Explorer and find `technion-096609-python-ai-main.zip`.
3. Right-click that ZIP file and choose **Extract All...**.
4. Click **Extract**.

Open the extracted folder until you see `README.md` and `class-00-setup` together. That is the folder you will open in VS Code.

Use the download link in step 1. GitHub's small file-download icon downloads only the page currently displayed.

## 5. Open and trust the repository folder in VS Code

1. At the top of VS Code, open the **File** menu and choose **Open Folder...**.
2. In the window that opens, go to the normal extracted folder that contains `README.md` and `class-00-setup`—not the ZIP file.
3. Click **Select Folder**.
4. If VS Code asks whether you trust the authors of the files, choose **Yes, I trust the authors**.
5. If a banner at the top says **Restricted Mode**, click **Manage** in that banner and then choose **Trust**.

Trust enables extensions and allows code to run. Trust this folder because you downloaded it from the official course repository; do not automatically trust unfamiliar folders.

The Explorer panel should now list the repository contents, including `README.md` and the `class-00-setup` folder. It may also show files such as `.gitignore`.

## 6. Select Python 3.13

1. In the Explorer panel, expand `class-00-setup` and click `setup_check.py`. This activates the Python extension.
2. Wait a few seconds, then click the Python version—or **Select Interpreter**—shown in the bottom status bar.
3. If neither appears there, press `Ctrl` + `Shift` + `P`, type `Python: Select Interpreter`, and select that command.
4. Choose an interpreter whose version begins with **Python 3.13**. If one is marked **Recommended**, choose it.

If several interpreters appear, do not choose one with a different version number. If no Python 3.13 interpreter appears, use the [troubleshooting guide](troubleshooting.md).

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
