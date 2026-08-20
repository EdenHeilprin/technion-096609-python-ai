# Package setup troubleshooting

Use this page only if `install_packages.py` reports an error or `check_packages.py` still says that a package is not ready.

## First check the selected Python

1. In VS Code, open the Command Palette with **Command+Shift+P** on macOS or **Ctrl+Shift+P** on Windows.
2. Enter `Python: Select Interpreter`.
3. Select Python 3.13.
4. Run `install_packages.py` again, followed by `check_packages.py`.

## If the installation is externally managed

Create a local environment for the course folder:

1. Open the Command Palette again.
2. Enter `Python: Create Environment`.
3. Choose **Venv**, then choose Python 3.13.
4. If VS Code asks which dependency file to install, select `class-10/requirements.txt`. Otherwise, wait for the environment to finish and run `install_packages.py`.
5. Run `check_packages.py`.

VS Code should now show a Python path containing `.venv` in its bottom status bar. The environment belongs to the course folder; do not move or submit it.

## If the check still fails

Email `edenheilprin@campus.technion.ac.il` with:

- your operating system;
- a screenshot of the complete output from `install_packages.py`;
- the line beginning `Python used for installation:`.
