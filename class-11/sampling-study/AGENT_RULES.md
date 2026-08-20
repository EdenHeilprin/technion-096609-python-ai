# Agent rules

These rules apply to every milestone in this project.

1. Work only inside the current `sampling-study` folder.
2. Treat `EXPERIMENT_SPEC.md`, `DATA_CONTRACT.md`, and `MILESTONES.md` as authoritative.
3. Implement only the requested milestone. Do not anticipate later milestones.
4. Use the current oTree one-file app style and APIs supported by `otree==6.0.15`.
5. Keep the experiment local. Do not add deployment, payment, Prolific, consent, demographics, passwords, secrets, or real participant identifiers.
6. Do not copy code, databases, environments, or credentials from another project.
7. Do not add dependencies beyond `requirements.txt` without asking first.
8. Preserve the field names and meanings in `DATA_CONTRACT.md`.
9. Validate external stimulus data explicitly. Invalid data should stop with a clear error rather than silently becoming a default value.
10. Add concise module or function docstrings and comments for non-obvious research, data, timing, or verification decisions. Do not narrate obvious syntax line by line.
11. Before editing, inspect the current project and report any conflict or missing decision that blocks the requested milestone.
12. After editing, show the diff, run the milestone's safe checks, report the exact results, and stop.

When browser behavior must be checked manually, state the exact action and expected observation rather than claiming that a code inspection proves it.
