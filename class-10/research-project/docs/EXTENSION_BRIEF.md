# Extension brief — six choices and confidence

## Study question

How does choosing the gamble vary as the guaranteed alternative increases?

## Participant experience

1. Show a brief introduction explaining the choices, the confidence scale, and that points are hypothetical with no payment.
2. Present six rounds in the fixed order of guaranteed offers **2, 3, 4, 6, 7, 8**.
3. On each round, offer that sure amount versus a **50% chance of 10 points and a 50% chance of 0 points**.
4. Require one choice (`sure` or `gamble`) and confidence in that choice from **1 — Not at all confident** to **7 — Very confident**.
5. End with an acknowledgement after the sixth submitted round.

Use no preselected choice or confidence response. Participants must actively select both on every round.

## Files and behavior

- Retain oTree app `choice_task` and session configuration `sure_or_gamble`.
- Use session display name `Sure or gamble — six decisions`.
- Set study version to `full-v1`.
- Use `Welcome.html` once, `Choice.html` for the six rounds, and `ThankYou.html` once at the end.
- Store one participant-round record per round. Refresh must not change its assigned offer or overwrite a submitted answer.
- Preserve unsubmitted selections when refreshing the same page in the same browser.
- Keep offer descriptions readable and both alternatives equally prominent on wide and narrow screens.
- Keep styling in `experiment/_static/choice_task/study.css`.
- Use accessible labeled radio buttons for confidence, with a small selected-value preview updated by `experiment/_static/choice_task/confidence.js`.
- The confidence preview should describe the actual selection, including after refresh. Before selection, it should invite a response rather than display a fabricated rating.
- Validate choice and confidence in Python on the server. JavaScript provides feedback; it does not replace validation.
- Explain Python lines, concepts, and functions with concise English `#` comments. Explain the important HTML/CSS/JavaScript pieces with comments in the appropriate syntax.
- Keep environment helpers and dependency versions unchanged.

## Data contract

Keep this exact custom CSV header:

```text
session_code,participant_code,study_version,round_number,sure_points,gamble_high,gamble_probability,choice,confidence
```

For each participant, export six rows with rounds 1–6. The guaranteed amounts must follow the specified list; `gamble_high` is `10` and `gamble_probability` is `0.5` in every row. Save confidence as integers 1–7. Unsubmitted answers stay blank, including rounds a participant never reached.

The combination of session code, participant code, and round number identifies one expected record. Do not collect names or other identifiers.

## Completion checks

- First and last rounds present the correct offers: 2 and 8.
- Missing choice or missing confidence prevents submission.
- Valid confidence values 1 and 7 are accepted; values outside the allowed set are rejected by the server.
- New rounds have no default responses.
- The selected-confidence preview updates and remains accurate after refresh.
- A complete run produces the six known responses entered during the manual test.
- An incomplete run leaves unsubmitted response fields blank.
- Refreshing the final page does not restart the study or duplicate submitted records.

## Interpretation boundary

This is a fixed-order pilot: higher offers always occur later. The collected data can describe choice patterns across offers, but this design does not separate offer effects from order effects. Retain that fact in project notes and later reporting.
