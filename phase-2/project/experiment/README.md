# Sure or gamble — full reference

Six fixed-order decisions: guaranteed offers **2, 3, 4, 6, 7, 8 points** versus a 50% chance of 10 points and a 50% chance of 0 points. Each decision requires a choice and an explicitly selected confidence rating from 1 to 7. Points are hypothetical; no money is paid.

## Run locally

Use the project-root `setup_environment.py`, then `run_experiment.py`, following the shared setup guide. Open `http://localhost:8000`. Create a **sure_or_gamble** session and open a participant link. A new session starts a new study without erasing earlier sessions.

For a terminal, activate the project `.venv`, enter this `experiment` folder, and run `otree devserver`. Keep local development on your own computer; it is not the server for a shared classroom study.

## Read the project

| File | Role |
|---|---|
| `choice_task/__init__.py` | Stored variables, six-round design, page order, and custom export |
| `choice_task/Welcome.html` | Short introduction before the first decision |
| `choice_task/Choice.html` | Choice and confidence form |
| `choice_task/ThankYou.html` | Receipt after the final saved choice |
| `_static/choice_task/study.css` | Layout, colors, mobile styling, and keyboard focus |
| `_static/choice_task/confidence.js` | A live preview of the selected confidence rating |
| `settings.py` | Session configuration and hosting safeguards |

Python controls the design and validates submitted responses. HTML structures the page, CSS styles it, and JavaScript updates the confidence preview. The form still works with JavaScript disabled. oTree saves each round when **Save and continue** is pressed. Refreshing an unfinished page in the same browser restores its selections; that browser recovery is not a server-side submission.

## Export

In the administration **Data** tab, download the `choice_task` **custom export** (not the wide all-apps export). It contains:

```text
session_code,participant_code,study_version,round_number,sure_points,gamble_high,gamble_probability,choice,confidence
```

Each row is one participant-round. The version is `full-v1`; choices are `sure` or `gamble`. Unvisited or unfinished rounds have blank answers. The analysis requires six complete valid rounds per participant. A final ThankYou page has no further submission: arriving there means the sixth response has already been saved.

## Before collecting shared responses

The instructor deploys the project; students do not need hosting accounts. A hosted server needs a database and private environment variables: `OTREE_PRODUCTION=1`, `OTREE_AUTH_LEVEL=STUDY`, a strong `OTREE_ADMIN_PASSWORD`, and a random `OTREE_SECRET_KEY` of at least 32 characters. Store secrets in server settings, not in this folder. See the instructor deployment checklist before provisioning or collecting data.

The custom export contains generated participant codes, not names. Do not add names or identifying participant labels. Keep real exports and the local oTree database outside the public repository. Hosting services may keep technical logs; generated codes are not a promise of complete anonymity. A shared start link may allow repeat participation: ask each person to participate once and retain their individual page if they need to resume.

## Interpret the pilot

Everyone sees the offers in the same ascending order. Offer size and round order therefore vary together. The classroom data can describe choices across these six offers; it cannot isolate a causal effect of offer size from order effects.
