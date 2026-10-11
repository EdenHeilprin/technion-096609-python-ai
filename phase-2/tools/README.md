# Maintainer tools

Students use their class README; these tools check releases in disposable folders.

- **Class 8:** `build_downloads.py 8` packages only the two authored Word documents. The personal live-generated project is not a release source.
- **Class 9:** authored directly in `class-09`. Run `build_downloads.py 9` after edits. `verify_hands_on.py --class9 class-09` checks both orders, saved responses, restart persistence, and the two thank-you-page edits in a temporary copy.
- **Class 10:** students fork and clone the course, so there is **no Class 10 ZIP**. Its README, Git setup guide, and two-file lesson template are authored directly. `verify_contribution.py` checks local links and rehearses clone/branch/copy/commit/push/revision commands using disposable local repositories. It does not impersonate a student account or test GitHub login or PR creation against the live course.
- **Earlier Classes 11/12:** the old materials remain in Git for reference, but current course navigation points to student-led lessons in `student-lessons`. The old packages still come from `phase-2/project`. Do not regenerate or remove them as part of a Class 10 change.
- **Release checks:** `verify_release.py` checks ZIP contents, manifests, syntax, and links for Classes 8, 9, and the retained earlier 11/12 packages. `--runtime` also exercises the earlier experiment/analysis package. `ci_student_smoke.py` installs the Class 9 and earlier Class 12 environments separately and runs their checks plus the Class 10 local Git rehearsal on macOS, Windows, and Linux.
- **Hosting check:** `verify_hosting.py` targets only the disposable CI Postgres service, never a live research database or Heroku app.

`DOWNLOADS.json` identifies the released ZIPs; `DOWNLOAD_MANIFEST.json` records their source hashes. Fixed ZIP metadata make unchanged builds byte-for-byte identical. Personal student-work folders are never build targets.

These checks do not replace a student's installer/sign-in walkthrough or the instructor's pedagogical review. Public data must be fictional or appropriately prepared for sharing; never package real classroom exports, secrets, databases, or environments.
