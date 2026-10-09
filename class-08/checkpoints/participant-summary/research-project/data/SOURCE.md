# Data source

`synthetic_choices.csv` is entirely fictional. It contains no student responses, names, demographics, or research findings.

`analysis/generate_synthetic_data.py` deterministically creates 15 complete fictional participants (90 answered rounds) and one additional fictional participant with two answered and four blank rounds. The file therefore has 96 rows and 16 participant codes. The standard inclusion rule retains 15 participants and 90 choices.

For fictional participants SYN01–SYN15, the numbers of initial gamble choices are respectively:

`6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 1, 1, 0`

All subsequent choices are sure. Confidence is invented using `1 + (participant_number + round_number) % 7`. These simple patterns make the lesson reproducible; they are not a model of human behavior. SYN16 has two gamble choices with confidence 4, followed by four blank responses.

After excluding SYN16, the gamble counts at offers 2, 3, 4, 6, 7, and 8 are 14, 12, 10, 6, 3, and 1 (out of 15 each). Overall there are 46 gamble choices out of 90, or 51.1% after rounding. The completed analysis records the input file's SHA-256 hash in `summary.json`.

Use `CODEBOOK.md` for variable meanings and the inclusion rule. Keep any actual classroom export under a different filename; never relabel this synthetic example as observed data.
