# Class 1 troubleshooting

Do not spend hours alone on one error. If the checks below do not solve it, use Moodle Technical Help and the browser fallback.

## I cannot find Run Python File

1. Confirm that the Microsoft Python extension is installed.
2. Open the Command Palette.
3. Select Python: Select Interpreter.
4. Choose a current Python 3 interpreter.
5. Reopen the Python file.

## VS Code says no interpreter is selected

Python must be installed separately from VS Code.

- Windows: follow the [Windows guide](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/resources/setup/windows.md).
- macOS: follow the [macOS guide](https://github.com/EdenHeilprin/technion-096609-python-ai/blob/main/resources/setup/macos.md).
- Restart VS Code after installation, then select the interpreter again.

## The terminal cannot find python

Prefer the VS Code **Run Python File** control.

On macOS, the terminal command may be python3. On Windows, restart VS Code after installing Python.

## The wrong output appears

- Save the active file.
- Read the filename in the active tab.
- Confirm that VS Code opened the extracted week-01-materials folder.
- Run the active file again.

## I see NameError: name 'gain' is not defined

Decide whether gain is intended as text or as a previously defined variable name. Text needs quotation marks.

## The public check says NOT YET

Read only the first reported mismatch. Compare:

- the calculation;
- rounding;
- all five output labels;
- the order of the lines.

Repair one cause and rerun.

## Ask for help safely

Include:

- operating system;
- exact filename;
- how you ran it;
- expected behavior;
- complete error text;
- smallest relevant synthetic code;
- what you already tried.

Never post passwords, tokens, student/participant identifiers, confidential data, or private links.
