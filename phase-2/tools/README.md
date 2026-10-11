# Maintainer tools

Students use their class README; they do not need these release tools.

Classes 9 and 10 are now authored directly in their class folders. Class 9 contains the seven-choice local oTree app from the successful Class 8 project, with public-hosting credentials and Prolific completion redirects omitted. Class 10 contains the CSV/Python/GitHub exercise. `build_downloads.py 9 10` packages only an explicit allowlist of their source files; it must not regenerate the old scaffolds or checkpoints. `verify_hands_on.py` exercises both presentation orders, validation, saved exports, restart persistence, and the Class 10 starter and exercise solution in disposable copies.

- Class 8's current starter is its two authored Word files, packaged by `build_downloads.py 8`. Its live-generated personal project is not a release source. Edit the Classes 9/10 sources in their class folders and package them with `build_downloads.py 9 10`.
- The unrevised Classes 11/12 still use canonical code in `phase-2/project`; do not hand-edit their generated `research-project` or checkpoint copies. Older `phase-2/minimal-experiment` and `phase-2/showcase-improvement` directories are historical, not the current Class 8 starter.
- Only when revising Classes 11/12, use their project environment and `build_example_results.py` to regenerate the synthetic worked results, then `build_downloads.py 11 12` to package them. The builder replaces only its named generated children in this repository.
- Run `verify_release.py --runtime` in the course environment for archive/source/hash/link/privacy checks and disposable local participant/export/analysis runs.
- `ci_student_smoke.py` extracts Classes 9 and 10, creates a fresh Python 3.13 environment from Class 9's requirement, and runs their checks. It separately installs the old Class 12 environment for the unchanged Class 11/12 checks. The GitHub workflow runs this on macOS, Windows, and Linux. These checks do not substitute for a novice's manual Codex sign-in or operating-system installer walkthrough.
- `verify_hosting.py` is restricted to the disposable Linux CI Postgres service. It tests the production server's authentication and data path, not Heroku provisioning or a live course URL. It must never be pointed at a real research database.

`DOWNLOADS.json` identifies the released archives. Each class's `DOWNLOAD_MANIFEST.json` hashes the files inside its archive (excluding the manifest itself). ZIP metadata are fixed so unchanged sources produce identical ZIP bytes.

Only synthetic example data and their derived outputs belong in the public release. Real exports, secrets, environments, databases, and personal student work must remain outside it.
