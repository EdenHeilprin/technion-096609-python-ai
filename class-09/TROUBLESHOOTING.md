# Workspace troubleshooting

| What you see | What to do |
| --- | --- |
| Python version message | Select Python 3.13 in VS Code, then run `setup_environment.py` again. Keep your other Python installations. |
| Installation stopped or download failed | Check your connection and rerun `setup_environment.py`. It reuses the project environment. Copy the final error if it still fails. |
| `No module named pandas`, `matplotlib`, or `otree` | Run `check_environment.py`, then select this project's `.venv` interpreter in VS Code. Close old Python interactive terminals before rerunning. |
| `.venv` belongs to a different Python version | Extract the class ZIP into a new folder and set it up using Python 3.13. Keep your work in the original folder. |
| Browser cannot connect | Keep `run_experiment.py` running and open the exact local address printed by it. Look for an error in that terminal. |
| Port 8000 is already in use, or the browser shows the previous class | Stop the previous server with Ctrl+C in its terminal. Start the current project's helper. Do not close unrelated processes. |
| The offer sequence or round count changed, but an old session looks wrong | Create a new session; existing sessions were created with the earlier settings. |
| `no such column` or a database-field error after adding a saved field | A new session may not fix an old database schema. Stop the server and keep the original project intact. Set up a fresh copy of the class project, then copy your edited source files into it—not the old database or `.venv`. Ask for help if you are unsure which files to copy. Do not reset a database containing collected responses. |
| A required answer is missing | Select the response explicitly and submit again. A confidence preview is not a substitute for selecting a radio button. |
| Data validation stops the analysis | Read the named row/column problem. Confirm that you downloaded the custom `choice_task` export, not oTree's full wide export. Keep the original export unchanged. |
| No complete participants | Complete all six rounds in a new full-study session, or use `synthetic_choices.csv` to continue the analysis lesson. |
| Codex cannot access a file | Confirm the project folder and task permissions. Ask it to report the exact missing path; do not grant Full access merely to avoid diagnosing a path problem. |
| Codex usage runs out | Continue with the lesson's separate working checkpoint, inspect/run the code, and record the next change you would ask for. |

For help, send me the class number, operating system, the step you reached, and the complete error text at **edenheilprin@campus.technion.ac.il**. Do not include passwords or participant-level classroom data.
