# Git and GitHub setup

Complete this setup during **Class 9**, ready to contribute a lesson in Class 10. **Git** records file versions; **GitHub CLI** (`gh`) lets you use your GitHub account from the terminal. Both are free.

## 1. Create or check your account

Sign in to **[GitHub](https://github.com)**, or create an account and verify your email. Note your **username**, which is different from your email address. Use your own account, not your partner's password.

## 2. Open VS Code's terminal

First stop the experiment: click the VS Code terminal where `otree devserver` is running and press **Control+C**.

Choose **Terminal → New Terminal** in VS Code. This opens a panel below your code. At the top right of that panel, click the small arrow beside **+** and choose **zsh (Mac)** or **Command Prompt (Windows)**. These are names for the programs that read terminal commands; they open inside VS Code, not in a separate app. Use this same choice in Class 10.

Enter these commands separately:

```text
git --version
gh --version
```

Each should print a version number. If both work, skip to Step 4. If one is missing, install only that tool using your computer's section below.

## 3. Install missing tools

### Mac

**Git:** if `git --version` opens an Apple developer-tools installation window, choose **Install**, accept the terms, and let it finish. You do not need the full Xcode app. If no window appears and Git is unavailable, enter:

```bash
xcode-select --install
```

Wait for the installation to finish before continuing. This can take several minutes.

**GitHub CLI:** open the **[official latest release](https://github.com/cli/cli/releases/latest)**. Expand **Assets** if necessary and download the file ending in **`macOS_universal.pkg`**. Open that installer and follow its prompts. It supports both Apple Silicon and Intel Macs; do not download the source-code ZIP.

If you already use Homebrew, `brew install gh` is an alternative. You do not need to install Homebrew just for this lesson.

### Windows

In the **Command Prompt** terminal you opened inside VS Code, run the command for each missing tool:

```bat
winget install --id Git.Git -e --source winget
winget install --id GitHub.cli -e --source winget
```

Accept the installation prompts and let each command finish. If Git asks which editor to use, select **Visual Studio Code**. Keep its recommended PATH option, **Git from the command line and also from 3rd-party software**.

If `winget` is unavailable, use the installers instead: **[Git for Windows](https://git-scm.com/install/windows)** and **[GitHub CLI releases](https://github.com/cli/cli/releases/latest)**. For GitHub CLI, download the Windows `.msi` matching your processor: `amd64` for standard Intel/AMD laptops, or `arm64` for Windows on ARM. Check **Windows Settings → System → About → System type** if unsure.

### Check the installation

Completely quit and reopen VS Code so it can find the new tools. Open a new terminal using Step 2 (**zsh on Mac; Command Prompt on Windows**) and run again:

```text
git --version
gh --version
```

Both must now show version numbers. If not, stop and get help rather than continuing with commands that depend on them.

## 4. Sign in from the terminal

Enter:

```bash
gh auth login --hostname github.com --git-protocol https --web
```

If asked whether to authenticate Git with your GitHub credentials, choose **Yes**. The terminal shows a one-time code and asks you to continue in the browser. Follow that prompt, paste the code on GitHub's page, check that the browser is signed into **your** account, and authorize GitHub CLI. Do not paste your password or authentication code into an AI chat.

Back in the terminal, run:

```bash
gh auth setup-git --hostname github.com
gh auth status
```

The first command lets Git use your GitHub CLI sign-in for future pushes. The second should confirm your GitHub username and a successful login. If an existing login is already correct, keep it; there is no need to log out.

## 5. Find your private commit email

A **commit** is a saved version recorded by Git. It includes an author's name and email, which can be seen when you publish it. GitHub provides a **noreply address** that identifies your account without revealing your personal email.

1. In your browser, open **[GitHub Settings → Emails](https://github.com/settings/emails)**. Check that you are signed into your own account.
2. Select **Keep my email addresses private**.
3. Find the GitHub-provided address beside that setting. It ends in **`@users.noreply.github.com`**. Copy the whole address, including any numbers before your username, and keep it in your personal notes for Class 10.

This is not a new mailbox: you do not need to open it or send an email. In Class 10 you will tell Git to use this address when recording your lesson changes. Enabling the checkbox alone does not configure Git on your laptop.

## Ready for Class 10

- `git --version` and `gh --version` both show a version number.
- `gh auth status` shows a successful login to your own GitHub account.
- You know your GitHub username and have copied your noreply address.

Return to **[Class 9](README.md#before-you-finish)** and watch the recommended Git/GitHub video before Class 10.

## When a step does not work

| What you see | What to do |
| --- | --- |
| `git` or `gh` is not recognized | Finish installing that tool, completely reopen VS Code, and check its version in a new terminal. |
| macOS cannot verify the GitHub CLI installer's developer | Confirm the file came from the official `cli/cli` release linked above. For this specific installer, follow Apple's [Open Anyway instructions](https://support.apple.com/en-us/102445) in **System Settings → Privacy & Security**. Do not disable security globally or bypass a malware warning. |
| Authentication fails | Run `gh auth status`; repeat Step 4 if needed. Do not use your GitHub password as a terminal token. |
| “Not a git repository” after the cloning step | Open the cloned folder with **File → Open Folder**, create a new terminal, and check `pwd` (Mac) or `cd` (Windows). |
| The destination folder is not empty | Keep its contents. Create a separate empty folder for this contribution; do not delete earlier work to make cloning succeed. |
| The branch already exists | You may already have completed that step. Run `git status` and `git branch --show-current`; continue on `add-my-lesson` if already there. Otherwise ask before switching. |
| “Nothing to commit” | Save your edited file, run `git status --short`, and confirm that you changed the copy inside your lesson folder. |
| A push is rejected or a PR reports conflicts | Stop and ask for help. Do not force-push or reset your files. |

For help, show the command, its error, and the folder shown by `pwd` (Mac) or `cd` (Windows), without passwords or tokens. You can email **[edenheilprin@campus.technion.ac.il](mailto:edenheilprin@campus.technion.ac.il)** with that information.

Official references: [Git installation](https://git-scm.com/install), [GitHub CLI installation](https://github.com/cli/cli#installation), [CLI sign-in](https://cli.github.com/manual/gh_auth_login), and [commit email privacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).
