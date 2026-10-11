# Class 9 troubleshooting

## The terminal shows `>>>`

You are inside Python, not the system terminal. Type `exit()` and press Enter. Run the installation and server commands at the normal terminal prompt. Do not type a leading `$`, `%`, or `>` from an example.

## `requirements.txt`, `settings.py`, or `.venv` cannot be found

Use **File → Open Folder** to open the extracted `class-09` folder, then **Terminal → New Terminal**. `ls` on Mac or `dir` on Windows should show `settings.py`. Create `.venv` if you have not completed that step yet.

## Wrong Python or oTree version

Use the exact commands in your [Mac](macos.md) or [Windows](windows.md) guide. Activate `.venv` before `otree devserver`, even if you selected that interpreter in VS Code. Run `check_setup.py` using the guide's command and read the printed interpreter path. If an existing `.venv` uses the wrong Python, rename that folder to `.venv-old` and repeat the environment-creation step with Python 3.13.

## The browser shows a different experiment or a TEST ONLY entry

The Class 9 download has one configuration, **Sure or gamble**, and no separate **TEST ONLY** entry. A different list can mean an earlier project's oTree is still running at `localhost:8000`; changing the folder in VS Code does not stop it.

Find the VS Code terminal where you started the earlier experiment and press **Control+C** there. Then open `class-09` in VS Code, create a new terminal, check the folder with `pwd` on Mac or `cd` in Windows Command Prompt, activate this folder's `.venv`, and run `otree devserver`. Refresh the browser. Do not delete the earlier project's database.

## Package installation fails

Check your connection and the complete error message. Retry the same install command after restoring access. Do not disable certificate verification or download replacement installers from an unofficial site. A managed university laptop may need IT help.

## PowerShell says scripts are disabled

Open a **Command Prompt** terminal using the dropdown beside the terminal's **+** button. Follow the Windows guide there, using `activate.bat` before `otree devserver`. You do not need `Activate.ps1` or a PowerShell execution-policy change.

## The browser cannot open localhost

In VS Code, look at the terminal where you entered `otree devserver`. It should show the browser address, not an error. Use `http://localhost:8000`, not `https`. If port 8000 is already in use, stop your earlier experiment with Control+C in its terminal. To keep that experiment running instead, use `otree devserver 8001` for Class 9 and open `http://localhost:8001`.

## My edit is not visible

Save the file. Check that VS Code and Codex opened the same `class-09` folder. Stop and restart the server, then refresh the participant page. For changes to prizes or saved fields, use a new session; ask for help if oTree requests a database change. Preserve exports before any database reset.

## Codex cannot access the project, or has no usage left

Open a local project pointing to `class-09`, not a web chat or cloud task. Use ChatGPT sign-in. Review any project-access request and allow only the access needed for this folder. If account access or quota blocks the task, complete the manual edit in the lesson; it does not require Codex. Do not buy a subscription for this setup check.

## Still stuck?

Email [edenheilprin@campus.technion.ac.il](mailto:edenheilprin@campus.technion.ac.il) with your operating system, the step/command, and the complete error text or a screenshot. Include the output of `check_setup.py` if it runs. Keep passwords, account tokens, and actual participant data out of the message.
