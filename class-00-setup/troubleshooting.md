# Class 0 Troubleshooting

Most setup problems are small and fixable. Work through the matching section below, then run `setup_check.py` again.

## I cannot find the Run button

1. Confirm that `setup_check.py` is open in the editor.
2. Open Extensions and confirm that **Python**, published by **Microsoft**, says **Installed**.
3. Close and reopen VS Code.

## `Python: Select Interpreter` is missing

The Microsoft Python extension is probably not active. Confirm that it is installed, then restart VS Code.

## No Python 3.13 interpreter appears

1. Close VS Code completely.
2. Install or repair Python 3.13.15 using your operating-system guide. Do not uninstall any other Python version you use.
3. Reopen VS Code and the extracted course folder.
4. Run **Python: Select Interpreter** again.

On Windows, select **Add Python to PATH** if the installer shows that option. On macOS, use the official python.org installer rather than Apple's system Python.

## VS Code opened one file, but I cannot see the course folders

You opened a file instead of the repository folder. Choose **File → Open Folder** and select the extracted folder whose name begins with `technion-096609-python-ai`.

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

## I am still stuck

Do not spend hours repeating the same steps. After one careful attempt with this guide, email [edenheilprin@campus.technion.ac.il](mailto:edenheilprin@campus.technion.ac.il) using the [help-request template](email-help-template.md).

Include the exact error text or a screenshot of the entire VS Code window. Before sending a screenshot, remove or hide passwords, API keys, student-ID numbers, private research data, and any personal information you do not want to share.

[Back to the Class 0 start page](README.md)
