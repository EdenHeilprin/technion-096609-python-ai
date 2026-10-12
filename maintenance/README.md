# Repository maintenance

Students follow the class pages. These scripts build downloads and check releases in temporary folders; they never modify personal student work.

- **Build downloads:** `python build_downloads.py` packages Classes 8 and 9 from explicit file lists and updates [DOWNLOADS.json](DOWNLOADS.json). Class 8 contains only the two context documents. Class 10 uses a clone, and Classes 11–13 use `student-lessons`; neither has a ZIP.
- **Check the release:** `python verify_release.py` checks download contents against their sources, the download index, and course links.
- **Check Class 9:** run `python verify_hands_on.py --class9 ../class-09` with Python 3.13 and oTree 6.0.15 available. It checks both presentation orders, saved responses, restart persistence, and the thank-you-page edits in a temporary copy.
- **Check Class 10:** `python verify_contribution.py` rehearses the local clone, branch, copy, scoped commit, push, and revision commands. It uses Command Prompt on Windows. It does not create real accounts or pull requests.
- **Check a fresh installation:** `python ci_student_smoke.py` installs the downloaded Class 9 experiment in a temporary environment and runs the checks above. GitHub Actions runs this on macOS, Windows, and Linux.

Run these commands from this folder. Fixed ZIP metadata keep unchanged builds identical. The manifests list source hashes; the download index lists only current packages. Real response exports, databases, credentials, and environments must not enter a download.
