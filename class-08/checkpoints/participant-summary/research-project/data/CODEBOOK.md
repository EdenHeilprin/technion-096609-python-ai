# Sure-or-gamble data

One row represents one round for one participant within one session. The unique row key is `session_code` + `participant_code` + `round_number`. Unanswered rounds can still have rows in an oTree export.

## Original export columns

| Column | Meaning | Full-v1 values |
| --- | --- | --- |
| `session_code` | oTree session identifier; keep as text | Nonempty code |
| `participant_code` | oTree participant identifier; keep as text | Nonempty code, interpreted within session |
| `study_version` | Version of the experiment that produced the row | `full-v1` |
| `round_number` | Position in the experiment | Whole numbers 1–6 |
| `sure_points` | Guaranteed alternative, in hypothetical points | 2, 3, 4, 6, 7, 8 in that fixed order |
| `gamble_high` | Gamble's higher outcome; the other outcome is 0 | 10 |
| `gamble_probability` | Probability of the higher outcome | 0.5 |
| `choice` | Selected alternative | `sure`, `gamble`, or blank if unanswered |
| `confidence` | Reported confidence in the selected choice | Whole numbers 1–7, or blank if unanswered |

The confidence endpoints are **1 = not at all confident** and **7 = very confident**. These are ratings, not probabilities. The offers always increase, so offer size and presentation order cannot be separated in this pilot.

## Inclusion rule

Include a participant only with all six unique rounds and a valid choice and confidence rating in each. Exclude the entire incomplete participant from the main summaries, rather than giving them fewer observations or treating blanks as zeros. Save every participant's status and reason in `exclusions.csv`.

Missing required study fields, unexpected values, mismatched offers, duplicate participant/round keys, or unsupported versions stop the analysis. They are not silently repaired or excluded. Original exports stay unchanged.

## Derived files

| File | One row represents | Important columns |
| --- | --- | --- |
| `clean_trials.csv` | One included choice | Original columns plus `chose_gamble`: 1 for gamble, 0 for sure |
| `exclusions.csv` | One participant in a session | `rows_present`, `answered_rounds`, `included`, `reason` |
| `choice_by_offer.csv` | One guaranteed offer | `gamble_count`, `choice_count`, `gamble_rate` (count divided by count) |
| `participant_summary.csv` | One included participant | `completed_rounds`, `gamble_count`, `gamble_rate`, `mean_confidence` |
| `summary.json` | One analysis run | Exact input hash, data label, synthetic status, counts, rates, exclusion rule |
| `confidence_by_offer.csv` | One guaranteed offer | `mean_confidence`, `participant_count`; produced by the Class 12 extension |

`gamble_rate` is a proportion from 0 to 1; figures display percentages. A rate of 0.8 means 80% of choices were gambles, not an 80% probability of winning. The overall trial-level rate and mean participant rate coincide here because every included participant contributes exactly six trials.

## Selecting a classroom export

Put the untouched **full-v1 custom export** in this folder under a new filename, such as `classroom_choices.csv`. In `analysis/settings.py`, change `DATA_FILE` to that filename, set `DATA_LABEL` to `Classroom pilot`, and set `IS_SYNTHETIC = False`. Run the analysis again. Its outputs go to `outputs/classroom_choices/`, separate from the fictional example. Keep real responses and their derived outputs local, not in the public course repository.
