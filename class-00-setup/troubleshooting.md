# Class 0 Troubleshooting

Most setup problems are small and fixable. Work through the matching section below, then run `setup_check.py` again.

## I cannot find the Run button

1. Confirm that `setup_check.py` is open in the editor.
2. Open Extensions and confirm that **Python**, published by **Microsoft**, is installed and enabled.
3. Wait for extension installation to finish, then close and reopen VS Code.
4. Reopen `setup_check.py`.

If the triangular button is still missing, open the Command Palette with `Command` + `Shift` + `P` on macOS or `Ctrl` + `Shift` + `P` on Windows. Run **Python: Run Python File in Terminal**.

## `Python: Select Interpreter` is missing

First confirm that the course folder is trusted, then open `setup_check.py` and wait a few seconds. The Python extension activates when a Python file is open. If the command is still missing, confirm that **Python** published by Microsoft is installed and enabled, then restart VS Code.

## No Python 3.13 interpreter appears

1. Close VS Code completely.
2. Install or repair Python 3.13.15 using your operating-system guide. Do not uninstall any other Python version you use.
3. Reopen VS Code and the extracted course folder.
4. Run **Python: Select Interpreter** again.

On Windows, select **Add Python to PATH** if the installer shows that option. On macOS, use the official python.org installer rather than Apple's system Python.

## VS Code opened one file, but I cannot see the course folders

You opened one file instead of the repository folder. Close that VS Code window, then open the normal extracted folder that contains both `README.md` and `class-00-setup`:

- macOS Start screen: click **Open...**. If the Start screen is not visible, choose **File → Open Folder...** from the macOS menu bar.
- Windows: choose **File → Open Folder...** from the top menu.

Do not select the ZIP file or the `class-00-setup` folder by itself.

## VS Code says Restricted Mode

Click **Manage** in the Restricted Mode banner, then choose **Trust** for the course folder. Only trust folders obtained from a source you recognize; this folder came from the official course repository.

## VS Code asks me to sign in or try Copilot

Neither is required for Class 0. Close or skip the prompt and continue with the setup guide.

## The downloaded files behave strangely or cannot be saved

You may be working inside the ZIP archive. Return to Downloads and extract it first:

- Windows: right-click the ZIP and choose **Extract All**.
- macOS: double-click the ZIP.

Then open the extracted folder in VS Code.

## The output says `SETUP CHECK NEEDS ATTENTION`

Read the Python version printed above that message.

- If it does not begin with `3.13`, run **Python: Select Interpreter** and choose Python 3.13.
- If Python 3.13 is not listed, follow **No Python 3.13 interpreter appears** above.

## I see red text or another error

Read the final lines first; they usually contain the useful message. Check that:

- the open file is exactly `class-00-setup/setup_check.py`;
- the selected interpreter is Python 3.13;
- you opened the extracted repository folder, not the ZIP file.

Then close VS Code, reopen the folder, and try once more.

## An installer says it cannot run on my computer

Do not download a random alternative installer. Use the [help-request template](email-help-template.md) and include the computer model and the exact installer message.

## I am still stuck

Do not spend hours repeating the same steps. After one careful attempt with this guide, email [edenheilprin@campus.technion.ac.il](mailto:edenheilprin@campus.technion.ac.il) using the [help-request template](email-help-template.md).

Include the exact error text or a screenshot of the entire VS Code window. Before sending a screenshot, remove or hide passwords, API keys, student-ID numbers, private research data, and any personal information you do not want to share.

[Back to the Class 0 start page](README.md)
