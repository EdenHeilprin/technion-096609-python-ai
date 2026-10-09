# Write a short Method and Results

Use your selected data source and freshly generated outputs. Two or three short paragraphs can be enough.

## Method

Describe the implemented task: six choices between a guaranteed number of hypothetical points and a 50% chance of 10 points (otherwise 0), the fixed offer sequence, and the confidence question. Confirm these details against the actual page text and code.

State the data source. For the bundled example, write **synthetic teaching data**: the records were generated, not collected from people. For a classroom pilot, use only known details about how that pilot was conducted. Identify unconfirmed facts separately.

State the inclusion rule: all six unique rounds must have valid choices and confidence ratings. Say how many participants were included and excluded, using `summary.json` and `exclusions.csv`.

## Results

Report the included participant count and number of choices. Describe the pattern in `choice_by_offer.csv` with one or two informative percentages; label their denominators clearly. Add the result of your chosen extension and refer to its table or figure.

Record the output filename and field or row supporting each numerical statement, either in a short “Evidence” list or directly after the paragraph. Keep full precision in the generated files and round only the prose.

End with the relevant limit: offer size and order vary together in this fixed-order pilot. A synthetic-data result demonstrates the analysis, not how a population behaves.

## Example of a traceable statement

For the supplied synthetic file:

> The analysis retained 15 of 16 fictional participants, contributing 90 choices. At the 3-point guaranteed offer, 12 of 15 choices were gambles (80.0%).

Evidence: `outputs/synthetic_choices/summary.json` (`included_participants`, `input_participants`, `included_trials`) and `choice_by_offer.csv` (row with `sure_points = 3`). This example must change if you analyze another input.
