# Sure or gamble — minimal checkpoint

One choice: **4 points for certain** or a **50% chance of 10 points / 50% chance of 0 points**. Points are hypothetical. No confidence question is included yet.

Follow the Class 9 checkpoint instructions to place this experiment inside your `research-project`. Use the project's `setup_environment.py`, then `run_experiment.py`. Visit `http://localhost:8000`, create a **sure_or_gamble** session, and open a participant link.

`choice_task/__init__.py` defines the stored variables, pages, and export. `Choice.html` displays the form; `ThankYou.html` confirms that the response has been saved. `_static/choice_task/study.css` controls the appearance.

Try **Save my choice** without selecting an option. Then select one and submit. You should reach **Your choice is recorded.** Refreshing the receipt does not create a second response. Create a new session for a fresh test.

In the administration **Data** tab, download the `choice_task` **custom export**. The version is `minimal-v1`; `confidence` is blank because this checkpoint has no confidence question. This minimal export is not input for the Class 11 six-round analysis.

Keep the local database and real participant exports out of GitHub. For a hosted deployment, the settings require private `OTREE_SECRET_KEY` and `OTREE_ADMIN_PASSWORD` values, `OTREE_AUTH_LEVEL=STUDY`, and `OTREE_PRODUCTION=1`. Shared deployment is an instructor task, not a prerequisite for this checkpoint.
