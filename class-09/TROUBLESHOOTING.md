# Class 9 troubleshooting

## The terminal shows `>>>`

You are inside Python, not the system terminal. Type `exit()` and press Enter. Run the installation and server commands at the normal terminal prompt. Do not type a leading `$`, `%`, or `>` from an example.

## `requirements.txt`, `settings.py`, or `.venv` cannot be found

Use **File → Open Folder** to open the extracted `class-09` folder, then **Terminal → New Terminal**. `ls` on Mac or `dir` on Windows should show `settings.py`. Create `.venv` if you have not completed that step yet.

## Wrong Python or oTree version

Use the exact command in your [Mac](macos.md) or [Windows](windows.md) guide, including `.venv`. Running a plain `python` or `otree` command may use another installation. Run `check_setup.py` using the guide's command and read the printed interpreter path. If an existing `.venv` uses the wrong Python, rename that folder to `.venv-old` and repeat the environment-creation step with Python 3.13.

## Package installation fails

Check your connection and the complete error message. Retry the same install command after restoring access. Do not disable certificate verification or download replacement installers from an unofficial site. A managed university laptop may need IT help.

## PowerShell says scripts are disabled

Use `.\.venv\Scripts\python.exe` and `.\.venv\Scripts\otree.exe` as shown in the Windows guide. You do not need to run `Activate.ps1` or change the execution policy. An automatic-activation warning from VS Code does not stop these direct commands.

## The browser cannot open localhost

The terminal must still be running `devserver`, without an error. Use `http://localhost:8000`, not `https`. If port 8000 is already in use, stop your earlier devserver with Control+C. Alternatively append `8001` to the start command and use `http://localhost:8001`.

## My edit is not visible

Save the file. Check that VS Code and Codex opened the same `class-09` folder. Stop and restart the server, then refresh the participant page. For changes to prizes or saved fields, use a new session; ask for help if oTree requests a database change. Preserve exports before any database reset.

## Codex cannot access the project, or has no usage left

Open a local project pointing to `class-09`, not a web chat or cloud task. Use ChatGPT sign-in. Review any project-access request and allow only the access needed for this folder. If account access or quota blocks the task, complete the manual edit in the lesson; it does not require Codex. Do not buy a subscription for this setup check.

## Still stuck?

Email [edenheilprin@campus.technion.ac.il](mailto:edenheilprin@campus.technion.ac.il) with your operating system, the step/command, and the complete error text or a screenshot. Include the output of `check_setup.py` if it runs. Keep passwords, account tokens, and actual participant data out of the message.
