# Worked example — synthetic teaching data

This is a reference for checking the writing workflow, not a report of an actual classroom data collection. It uses the unchanged `synthetic_choices.csv` supplied with the course.

## Method

The implemented oTree task presents six choices between a guaranteed alternative and a gamble offering a 50% chance of 10 points and a 50% chance of 0. Guaranteed offers are 2, 3, 4, 6, 7, and 8 points, in that ascending order for every participant. All points are hypothetical. Each round requires a choice and an explicitly selected confidence rating from 1 to 7 before the response is saved. The custom export contains one row per participant per round.

For this worked analysis, responses were generated deterministically rather than collected from people. The fixture contains 16 fictional participant records and 96 round rows. The analysis includes only records with six unique, valid, answered rounds. One fictional participant has only two answered rounds and is excluded, leaving 15 complete records and 90 analyzed choices. The generator and its construction rules are documented in `data/SOURCE.md`.

## Descriptive results

In the synthetic example, 46 of 90 included choices were gambles (51.1%). Gamble choice rates at guaranteed offers of 2, 3, 4, 6, 7, and 8 points were 93.3%, 80.0%, 66.7%, 40.0%, 20.0%, and 6.7%, respectively. Each rate uses 15 choices, one from each included fictional participant.

The decline was deliberately built into the teaching fixture; it is not evidence about human behavior. In an actual deployment of this fixed-order design, offer size and round order would change together, so the same descriptive graph would not isolate their separate effects.

## Evidence map

| Claim | Source within `research-project/` |
|---|---|
| Offers, gamble, six rounds, required fields | `experiment/choice_task/__init__.py` |
| Participant instructions and response scale | `experiment/choice_task/Welcome.html` and `Choice.html` |
| Synthetic construction, partial record | `data/SOURCE.md` and `analysis/generate_synthetic_data.py` |
| 16 input, 15 included, 1 excluded, 90 choices | `outputs/synthetic_choices/summary.json` |
| Reason for exclusion | `outputs/synthetic_choices/exclusions.csv` |
| 46 gambles, overall rate | `outputs/synthetic_choices/summary.json` |
| Six offer-specific rates | `outputs/synthetic_choices/choice_by_offer.csv` |

Run the analysis to generate these outputs. The Class 8 `reference-results/` folder also includes checked copies for viewing without running Python. `summary.json` records the SHA-256 fingerprint of the exact source CSV.

## To confirm for an actual classroom report

The actual collection setting and dates, any departures from this procedure, and the provenance of the export must be supplied from the real session. Recalculate the results using that export; do not reuse the numerical sentences above.
