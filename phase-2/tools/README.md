# Maintainer tools

Students use their class README and `research-project` helpers; they do not need these release tools.

- Edit canonical code in `phase-2/project`, the one-round reference in `phase-2/minimal-experiment`, and the Class 8 display-only overlay in `phase-2/showcase-improvement`. Edit lesson prose in each class's top-level Markdown files. Do not hand-edit generated `research-project` or checkpoint copies.
- With the project environment, run `build_example_results.py` to regenerate the synthetic worked results, then run `build_downloads.py` to rebuild the five public class folders and ZIPs. The builder replaces only its named generated children in this repository.
- Run `verify_release.py --runtime` in the course environment for archive/source/hash/link/privacy checks and disposable local participant/export/analysis runs.
- `ci_student_smoke.py` extracts a fresh Class 8 ZIP, installs its environment, runs its environment check, and invokes the full release verification. The GitHub workflow runs this on macOS, Windows, and Linux.
- `verify_hosting.py` is restricted to the disposable Linux CI Postgres service. It tests the production server's authentication and data path, not Heroku provisioning or a live course URL. It must never be pointed at a real research database.

`DOWNLOADS.json` identifies the released archives. Each class's `DOWNLOAD_MANIFEST.json` hashes the files inside its archive (excluding the manifest itself). ZIP metadata are fixed so unchanged sources produce identical ZIP bytes.

Only synthetic example data and their derived outputs belong in the public release. Real exports, secrets, environments, databases, and personal student work must remain outside it.
