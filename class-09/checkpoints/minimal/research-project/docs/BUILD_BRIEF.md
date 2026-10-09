# Build brief — one real choice

## Participant experience

Build a minimal oTree experiment named **Sure or gamble**.

The participant chooses between:

- **Sure:** 4 points for certain.
- **Gamble:** a 50% chance of 10 points and a 50% chance of 0 points.

State that points are hypothetical and no payment is made. Neither option is selected initially. The participant must select one option before continuing. After submission, show a final acknowledgement that the response was recorded.

## Implementation

- Use the project's pinned oTree version and the existing `experiment/settings.py` scaffold.
- App folder: `experiment/choice_task`.
- Session configuration name: `sure_or_gamble`.
- Session display name: `Sure or gamble — one decision`.
- Study version: `minimal-v1`.
- One round; `Choice.html` followed by `ThankYou.html`.
- Save choices as the strings `sure` or `gamble`.
- Keep presentation wording separate from saved values: changing a label must not change the recorded category.
- Preserve selected but unsubmitted inputs when the participant refreshes the same page in the same browser. Submitted responses must remain saved.
- Use clear English `#` comments to explain the Python lines, concepts, and functions. Use HTML comments where the template needs explanation.
- Retain the project's environment helpers and dependency versions.

## Data

Provide a `choice_task` custom CSV export with this exact header:

```text
session_code,participant_code,study_version,round_number,sure_points,gamble_high,gamble_probability,choice,confidence
```

There is one row per participant in this one-round study. The row records round `1`, sure points `4`, gamble high outcome `10`, and gamble probability `0.5`. `confidence` stays blank because the question is not part of this version. If a participant has not submitted, `choice` stays blank too.

Use oTree's generated session and participant codes. Do not collect names or other identifiers.

## Completion checks

1. A new participant sees the full offer and no preselected answer.
2. Submitting without an answer does not advance.
3. Submitting either valid option reaches the final acknowledgement.
4. The export contains the chosen value, correct offer, version, and participant/session codes.
5. Refreshing does not silently substitute an answer or alter a submitted response.

Keep the build focused on this specification. The next class adds multiple rounds and confidence.
