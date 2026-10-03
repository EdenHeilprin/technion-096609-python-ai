# Package setup troubleshooting

Use this page only if `install_packages.py` reports an error or `check_packages.py` still says that a package is not ready.

## Check the selected Python

1. In VS Code, open the Command Palette with **Command+Shift+P** on macOS or **Ctrl+Shift+P** on Windows.
2. Enter `Python: Select Interpreter`.
3. Select Python 3.13 or the existing course interpreter whose path contains `.venv`.
4. Run `install_packages.py` again, followed by `check_packages.py`.

## Create a local environment if needed

1. Open the Command Palette.
2. Enter `Python: Create Environment`.
3. Choose **Venv**, then choose Python 3.13.
4. If VS Code asks for a dependency file, select `requirements.txt`. Otherwise, run `install_packages.py` after the environment is ready.
5. Run `check_packages.py`.

## If the check still fails

Email `edenheilprin@campus.technion.ac.il` with:

- your operating system;
- a screenshot of the complete output from `install_packages.py`;
- the line beginning `Python used for installation:`.
